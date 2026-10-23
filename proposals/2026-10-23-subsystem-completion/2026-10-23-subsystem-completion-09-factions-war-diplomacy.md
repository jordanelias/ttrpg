# Factions, war and diplomacy — completion proposal (T09 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/2026-10-22-system-description-10-t09-factions-war-diplomacy.md` (cited `T09 §n` / `T09:L`) and `…-00-overview.md` §3 (FA, GV, MB rows), §5.2, §6 #8, #11; `research/game_precedent_suite/dispositions/D_T09.md` (`D_T09 #n`) and `D_T09_also.md` (`also #n`); `research/game_precedent_suite/THROUGHLINES.md` (`P##`, `TM##`, §6); `proposals/2026-10-16-verbs/2026-10-16-verbs-15-lexicon-faction-actions.md` (`FA §3.n`, `S1`…`S9`, `M1`…`M10`) and `…-20-gap-register-mb-and-fa.md` (FA half, `FA-G##`); `proposals/2026-10-21-v9-remediation/` parts 02-04 (`REM-##`, `JQ-#`); `workplans/valoria_master_workplan_v9_part5.md` (IN-30, IN-36, IN-48, IN-57, IN-58, IN-60, IN-61, §A A-28…A-37) and `_part7.md` (FA-01, FA-03, FA-07); `skills/ners/SKILL.md`; code at HEAD as cited.

Abbreviations: `es/` = `engine/season/`; `VT` = `es/verb_table.yaml`; `RY` = `es/rosters.yaml`; `WQ` = `es/queries/world_q.py`;
`PQ` = `es/queries/person_q.py`; `FQ` = `es/queries/faction_q.py`; `EI` = `es/loop/effects_information.py`. Evidence grades are the suite's
(RUNS-IN-LOOP, TESTS-ONLY, DESIGN-ONLY), carried and never upgraded. `[UNVERIFIED]` marks a claim whose code I did not open at `2decf4a`.
`[MEASURED-HEAD]` marks a count from my one probe at `2decf4a` (`build_realm(0)`, two seasons; a scratchpad script, not committed; §7).

**The one-line reading today.** A faction is a creed Proposition plus `commit` edges (`T09 §2.1`); everything a grand-strategy player
expects of it — pressure, war, binding treaties, land that rewards, a realm that outlives its king — is either a carrier nothing reads
(`at_war`, `FQ:219`, no non-test caller; covenant "in force", `EI` `_eff_covenant` writes_note `VT:311`) or a route no computed question
supplies an operand for (`T09 §2.6`). Since the description landed, three things moved that this file builds on and does not repeat:
`give` + Rung (cession, `VT:571-592`, `EI:796-849`, PR #496), IN-70's opinion of a faction (`WQ:2072-2105` `opinion_of`, `PQ:507-549`,
read only by `WQ:2108-2161` `opinion_referents`, PR #496), and B-V's foreign cast (Altonia's two seats behind
`build_realm(foreign=True)`, default OFF, `es/harness/populated.py:722-733`; the Katepano's `goal_katepano_press_the_capital`,
`es/goals.yaml:449`; FA-01's trade-demand clause held on `ED-IN-0298`, `_part7:122`).

**The layer constraints every item below obeys** (Layer 1, cited by v9 `_part5` §A A-29, A-31, A-37 and `RY:2576-2577`): no stored gauge (T-a),
no threshold that produces an outcome (T-b), no scheduled clock (T-c), a decision receives no World (AX-2), a goal never acts and
nothing aggregates (A-31), a Seat carries no modifier (`04` §B.7, cited at `_part5:152`). So in this file **pressure is always a person's
act on a Query read when his question forms**, never a meter that fires.

## §0 The genre loop

The yardstick: what a player of CK3, Bannerlord, Imperator, CK2, HOI4, the Dragon Age: Inquisition war table, EU4, Pax Pamir or Oriental
Empires expects to choose at faction scale, at what cost, with what lasting consequence — and what the realm does with nobody watching.
"Today" is the grade the suite's evidence supports at HEAD; it is carried, never upgraded.

| # | play opportunity (choice · cost · lasting consequence) | precedent | today | evidence |
|---|---|---|---|---|
| G1 | **Choose, keep or change allegiance.** Join a faction, leave it, switch to a rival; the switch should cost what the old side gave and carry what the switcher holds. | `D_T09 #12` (Bannerlord join), `#43` (Pax Pamir: switching free but total), `#54` (Stellaris: values move membership), `#28` (Imperator secession with land); P08 | **PARTLY.** Leaving is `release` (public, `VT:1028-1037`); 0 faction `commitment.ended` in seeds 0-2 (`T09 §0`). Joining a faction has no computed route (`T09 §2.1`); a switcher carries his land and loses nothing (`T09 §5b` "Defect with your land") | leave RUNS-IN-LOOP for non-faction edges; join and switch TESTS-ONLY (hand-built, `T09:487-495`) |
| G2 | **A faction presses its leader.** Discontented members band behind a demand on the seat-holder; he concedes, buys them off or faces their withdrawal. | `D_T09 #1` (CK3 factions and ultimatum), `#26` (CK2 levy by opinion), `#31` (Rome II secession risk); `also #10`, `#20`, `#22` (Syx riots, FoG2 revolts, Tropico demands); P10, P02; TM02 | **ABSENT.** A faction "wants" only by ordering its members' questions (`T09 §2.5`); `opinion_of` is computed and read only to add referents to a question already formed (`WQ:2108-2161`; IN-58/IN-70's EXIT not met in computed play, `_part5:57`, H-225) | DESIGN-ONLY |
| G3 | **Swear and keep service.** A vassal swears; the liege pays upkeep or the oath lapses; the sworn man fights and yields for the liege. | `D_T09 #2` (CK3 contract owed up), `#15` (Bannerlord wages), `#35` (RTK unpaid officers), `#65` (JA2 contracts); `also #18`, `#33`; P14, P20 | **PARTLY.** `oblige` 4-season term, upkeep flows down, lapse at MATTER (`T09 §5b`); the vassal yields purview only (IN-40); an obligee outside the seat's faction marches with nobody (`WQ:1477` `mustered`; `T09:448`) | `oblige` RUNS-IN-LOOP at seed 1 only; renewal and lapse TESTS-ONLY (`T09:479-482`) |
| G4 | **Go to war with a casus and a cost; make peace.** A declaration opens targets and brings allies in; aggression is priced; peace ends it on terms. | `D_T09 #3` (CK3 casus belli), `#48` (Empires in Arms war price), `#53` (EU4 coalitions), `#55` (Stellaris wargoals); `also #1`, `#19`, `#48` (Vic3 play, M2TW act of war, Shadow Empire); P06, P12 | **ABSENT.** War is a WAR Proposition plus commits (`FQ:219-252`); nothing reads `at_war`; any `dispatch` seat may march on any foreign-held town with no prior state (`T09 §5c`); 0 WAR Propositions in seeds 0-2 | DESIGN-ONLY (`declare`, `FA §3.3` S2); `at_war` TESTS-ONLY (`T09:447`) |
| G5 | **Make agreements that bind.** Treaty, alliance, tribute, truce: kept because breaking costs, read by what people then do. | `D_T09 #17` (Warband peace), `#25` (CK2 truce breach priced), `#42` (KoH II pact chain), `#46` (Pax Pamir non-binding deals); `also #12`, `#13`, `#21`, `#27`; P12, P14 | **PARTLY.** `covenant` + `give` + both `commit`s makes a treaty "in force" that nothing reads (`T09 §3.3`); breach is a public `release`, judged only at `release`'s cells (`VT:1039`); the instrument's `Record.stages` is its term and matures at MATTER (`VT:311`), but the `commit` edges that make it "in force" carry none (`T09:470-472`) | TESTS-ONLY (covenant 13/0, 4/0, 1/0; `test_in12_covenant.py`) |
| G6 | **Take, hold and grant land.** Conquer a town or a territory; reward a follower with land; land so granted binds him. | `D_T09 #13` (Bannerlord fief by vote), `#44` (Pax Pamir rule by plurality); `also #11` (Syx region conquest), `#16` (Total War capture choice), `#34` (JA2 counterattack), `#47` (Dominions independents); P15 | **PARTLY.** `march` + `seize` takes an occupied settlement (`T09 §3.2`); cession of a held rung exists since PR #496 (`give` + Rung, `rung.ceded`, `EI:816-849`); a territory is refused by kind under an open assumption (`EI:961-963`) and an unheld place under H-166 (`EI:967`) | seize, march TESTS-ONLY; `give` + Rung TESTS-ONLY (`es/tests/test_in12_give_rung.py`) |
| G7 | **A realm survives its ruler.** On a death the seat and the land pass by a rule or a claim; a vacancy is contested, never permanent. | `D_T09 #4`, `#5`, `#36` (CK3 succession, titles on death, RTK replacement); `also #4`, `#39`, `#59` (Old World heirs, Nemesis refill, EN VII.3); P30, TM05 | **ABSENT.** The King dies in season 0 in every seed; seven seats have no conferral basis; 11 of 16 territories uncontrolled at tick 2 in every seed (`T09 §2.2`, overview §6 #11); IN-61 STOPPED (`_part5:158`) | the collapse RUNS-IN-LOOP; succession DESIGN-ONLY |
| G8 | **Delegate.** Send an agent on a mission that runs for a while and comes back with a result attributable to him. | `D_T09 #21` (DAI war table), `#24` (CK2 councillor missions); `also #31`, `#60` (GK2 unreliable orders, EN compliance below 1); P04, P15; TM04 | **ABSENT.** `dispatch` writes nothing; its `order.given` fills every ledger and no decision reads it (`T09 §4`) | `dispatch` RUNS-IN-LOOP as a no-write |
| G9 | **Plot against a seat.** Draw backers into a secret project against a holder; a refusal or a discovery has consequences. | `D_T09 #27` (CK2 plots with backers), `#33` (Rome II adopt/bribe/assassinate); `also #25` (Suzerain coups); P13; TM06 | **ABSENT.** No plot carrier; `conceal` exists (IN-12 step 10) | DESIGN-ONLY (`conspire`, `FA §3.3` S7) |
| G10 | **The realm acts and can end without the player.** Rivals declare, lords defect, revolts take land, a faction can be destroyed, and the season reports when the realm is won or lost. | `D_T09 #14` (Bannerlord AI wars and secession), `#49` (EiA elimination), `#59` (Brigandine win state); `also #3`, `#14`, `#38` (Vic3 revolution, Frostpunk faction ending, Nemesis power struggles); P38, P42 | **PARTLY.** Violence empties offices unwatched (`also #38`, RUNS-IN-LOOP); `endings_reached` reports and reaches nothing (`T09 §0a` Failure); the Katepano's march on the capital forms at witness seeds 39 and 53 only, behind `foreign=True` (`_part5:102`) | endings report RUNS-IN-LOOP; war, defection, revolt DESIGN-ONLY; foreign march TESTS-ONLY at witness seeds |

These ten are the completeness yardstick. A later section that adds nothing to one of them is padding; one that leaves a row ABSENT
says so in §7.

`[MEASURED-HEAD]` at `2decf4a`, `build_realm(0)`, two seasons (the collapse holds; the B-V cast is off by default): provinces
Crown 6 / Hafenmark 4 / Varfell 4 / Church 1 at tick 0, Varfell 4 / Church 1 at ticks 1 and 2; `uncontrolled` 1 → 11 → 11; faction
members 40 → 35 → 31; WAR Propositions 0; faction `commit` edges closed by an act 0; `endings_reached` `[]` every tick. Acts reaching the
fold / ok: `give` 0/0 (so `give` + Rung never formed), `seize` 0/0, `covenant` 16/0, `raze` 22/0, `march` 20 declared, 0 fields,
`oblige` 0/0, `dispatch` 14/7, `transfer` 51/1; events `rung.ceded` 0, `rung.seized` 0, `commitment.made` 0, `term.renewed` 0.

## §1 Gap ledger

Every LACKS row of `D_T09` (26, plus #4's LACKS half) and of `also` (35), and every DIFFERS row either file marks as a risk
(`D_T09` 19, `also` 9): **90 rows**, in 20 gaps, each ending in exactly one disposition. Not counted, because they are not design
gaps: the CONTRADICTS rows about precedent or repo text (`D_T09 #52, #58, #62, #63, #67, #75, #78, #79, #90`; `also #5, #30, #58,
#64-#68`), whose edits fall on the suite and on `research/` files outside this lane; and the DIFFERS rows the dispositions call ruled or
neutral (`D_T09 #7, #23, #72, #85, #89`; `also #41`). A "declined" line is the five-step answer in one line (step named).

| gap | rows | what is missing | disposition |
|---|---|---|---|
| GP-1 · allegiance moves by nothing | `D_T09 #16, #28, #31, #43, #54, #57, #68, #71`; `also #10, #20` (10) | No computed join; no defection caused by what a member thinks of his faction (`loyalty` is read only at world-gen, `T09 §2.5`); a ruler's death changes nothing for his followers (`#57`); a switch is free and carries land | **closed by CP-T09-01** (an opinion filter on T02's CP-T02-05 `oughts_named` for rival creeds, and a leave body on IN-70's `opinion_of`; a dead head leaves `opinion_of`'s regard term). The switcher's price stays witnesses' reception (ruled C-1, quoted at `VT:1044`), plus the retaking CP-T09-04 opens against land carried to a rival; the cell that prices a vow-break is v9 IN-11/IN-08's (`VT:1039`), not repeated |
| GP-2a · a faction presses nobody | `D_T09 #1`; `also #22` (2) | No bloc with a demand; nothing for a seated player to receive | **closed by CP-T09-01** (members leave with their land; a discontented member's petition to his head forms on REM-24's Person class, no new term) |
| GP-2b · a stored bloc, an opinion-gated muster, conflicting goals | `D_T09 #26, #69`; `also #2` (3) | CK2 levy by opinion; Tropico's exclusive demands; Victoria 3's interest groups | **declined.** Step 3: a goal never acts and nothing aggregates (A-31), every stored track is refused (A-37, T-a); a muster refused below an opinion is a threshold producing an outcome (T-b); "nothing tests whether [a goal] is met" (overview §6 #8) is A-31 as built |
| GP-3a · service yields nothing up | `D_T09 #2, #15, #34, #66` (4) | A sworn man is not in his liege's army; no seat can bring a man into service | **closed by CP-T09-07** (`recruit`; the exercised seat's obligees march with it) |
| GP-3b · a following that turns as a bloc | `also #51` (1) | A steward's men follow him | **declined.** Step 5: no carrier is needed — each obligee's own opinion moves with his lord's witnessed deeds and CP-T09-01 acts on it; a "bloc follows" rule (M8, FA-G36) would move edges other persons own (D-5) |
| GP-4 · war has no producer, reader or price | `D_T09 #3, #19, #48, #53, #55`; `also #1, #19, #48` (8) | No seat act declares; nothing reads `at_war`; aggression costs nothing; no coalition forms | **closed by CP-T09-02** (`declare`, its grievance occasion, the war's target stamp; a coalition is several declarations on one grievance; a wound starts one, a killing does not until H-209 closes). `#19`'s world-tension meter and `also #1`'s phased play are the parts not built (T-a; T-c), named in CP-T09-02's block |
| GP-5a · treaties perform nothing | `D_T09 #46`; `also #12, #21, #44, #46` (5) | A covenant in force changes no later act; no ally joins a side | **closed by CP-T09-03** (alliance and peace as acts on the war Proposition) |
| GP-5b · truce, pact chain, dated terms, breach price | `D_T09 #25, #42`; `also #13, #27` (4) | CK2's priced truce; KoH II's pact chain; Oriental Empires' dated terms; Frostpunk 2's broken-promise price | **declined.** Truce: step 5 — the reader verbs-15 proposes is "Not a refusal" but a rank term, *"the chooser ranks a march on a truce partner down"* (`proposals/2026-10-16-verbs/2026-10-16-verbs-15-lexicon-faction-actions.md:86`), and no new chooser score term is proposed by any file (rulings sheet R1; the score's shape is `ARCHITECTURE_V2.md:508-528`'s). Dated terms: step 5 — terms exist on the instrument (`Record.stages`, matured at MATTER, `VT:311`) and on a seat hold (`confer` writes `Tenure.term`, `VT:274`, IN-10 (b)), but nothing ends a `commit` at its instrument's maturity, and doing so would widen T-n's maturity close to `commit` edges, a gate change this file does not make. Pact chain: step 3, the `league` content is unbuilt (`FA §3.3` S1). Breach price: step 3, v9 IN-11 schedules the `deed:commitment.ended` cell (`VT:1039`) |
| GP-6a · land under no one, territories, one head | `D_T09 #5, #44`; `also #3, #11, #28, #34, #47` (7) | A dead holder's land cannot be taken; territories refused by kind; one resident licenses a seizure; nothing retakes | **closed by CP-T09-04** (`seize` takes unheld places and territories by plurality occupation; IN-30's stopped caller re-scoped as its occasion) |
| GP-6b · province hysteresis | `D_T09 #6` (1) | A province that survives a death | **declined.** Step 4: a province "appears and vanishes with no act" by the 2026-07-13 ruling (`WQ:1570`, quoted at `T09 §2.2`); CP-T09-04 gives the route back instead |
| GP-7 · land cannot reward | `D_T09 #13` (1) | No follower is ever given land | **closed by CP-T09-05** (`give` + Rung, built at PR #496, gets an occasion on questions about the giver's sworn men; the land moves, and the regard it buys waits on an IN-08 cell, named there) |
| GP-8a · the throne and its household pass to nobody | `D_T09 #4, #36`; `also #4, #33, #40, #59` (6) | CK3/RTK/Old World/GK2 succession; Shadow of War's conquest that seats a new holder | **declined here, not closed.** Step 3: the throne is v9 IN-61's, which is STOPPED (`_part5:158`, H-230); H-230's arm 2 is T02's CP-T02-01 and the `off_npc_084` row is IN-61's content decision (rulings R4). `also #40`: step 4, taking a town and filling its seats stay separate verbs (`seize`, `confer`), the tree's own split (`EI` "A SEAT is never seized", `VT:1141`) |
| GP-8b · a vacated duchy is never refilled | `also #39` (1) | Nemesis refill | **closed by CP-T09-06** (`off_duke_valorsmark` gets a basis; data only) |
| GP-9 · delegation is inert | `D_T09 #21, #24`; `also #31, #60` (4) | An order moves nobody; no agent can fail in character | **closed by CP-T09-08** (`dispatch` rebuilt to send an obligee; the name is D-V7's) |
| GP-10 · no plot | `D_T09 #27, #33`; `also #25` (3) | No backers, no coup, no refused invitation | **closed by CP-T09-09** (`conspire`; `#33`'s buy-a-man half is CP-T09-07's `recruit`; `turn` stays parked, `FA §3.3` S3) |
| GP-11a · nobody wars or secedes unwatched | `D_T09 #14` (1) | Bannerlord's AI wars and secession | **closed by CP-T09-01 and CP-T09-02** (both occasions run for every person, seated or not) |
| GP-11b · defeat, elimination, limits, directors | `D_T09 #20, #49, #59`; `also #6, #7, #14, #62` (7) | A defeat state; a faction destroyed; a season limit; threat sized to wealth; a cost on concentration; faction resolution as the ending | **declined.** Step 3: the ending vocabulary is GD-1's and IN-27's (RS-21 D6, `RY:2549-2577`), and a season limit is a clock (T-c); a threat director is a per-season emitter (A-29, T-b); the +1-per-hold budget is ruled (`es/decision/budget.py:19-20`). CP-T09-04 makes the existing victory row reachable (`RY:2591-2592`) |
| GP-12 · no collective decision | `D_T09 #11, #73`; `also #50` (3) | No vote on war, peace or fiefs; no expulsion | **declined.** Step 1: T05 declines the vote as held on J-4 / H-161 (T05's file `:59`, `:382`); a body's decision is SC's `convene` + `determine` under an arrangement; expulsion is a second-person closer, refused by ruling (D-5, quoted at `VT:1044`) |
| GP-13 · kin, rank, founding | `D_T09 #8, #38, #39`; `also #29, #45, #69` (6) | Marriage, hostage, tribute, a rank ladder in a faction, schism and founding | **declined.** Step 3: kin and marriage wait on the closed cast (ED-WR-0011; FA-G43 parked); hostage is parked (FA-G30); tribute has no due carrier (`_renewals` reads `oblige` only, `VT:311`); founding and schism are IN-30's emergence half, untouched here. Step 5: a rank ladder needs a `commit` degree writer and a ladder ordering degree families, which `FQ:132-140` refuses to invent. `#38`'s ally-joining half is CP-T09-03's |
| GP-14 · no public reputation | `also #42, #57` (2) | Nothing a third party reads before dealing with someone | **declined.** Step 5: a public standing is either a stored aggregate (T-a) or World truth read into a decision (AX-2); the carrier is one person's `opinion_of` (IN-70); showing it is the play surface's (REM-30, IN-47) |
| GP-15 · another subsystem's | `D_T09 #30, #32, #40, #77`; `also #16, #17, #24, #26, #35, #36, #56` (11) | Field glory, troop raising, yield by governor, supply, capture choice, presence, foreign bloc reaction, embargo, income by share, population levy | **declined here, routed** (step 5, lane): `#30` to v9 IN-08's `deed:` cells; `#32`, `#77`, `also #56` to T04 (`levy` is MB's by R-01; weight → troop is JQ-4); `#40`, `also #35` to T08; `also #16` superseded by `raze` (PR #496, `VT:1105-1127`); `also #17`, `#36` ruled presence (`WQ:1477`); `also #24` by design (the foreign root stays outside realm queries; Altonia is seated only by `foreign=True`); `also #26` parked (FA-G33) |

**Rows addressed: 90.** Closed by an item: 46 (GP-1 10, GP-2a 2, GP-3a 4, GP-4 8, GP-5a 5, GP-6a 7, GP-7 1, GP-8b 1, GP-9 4, GP-10 3,
GP-11a 1). Closed by a remediation item alone: 0 (REM-21, -23, -24 and -27 are dependencies, §5). Declined: 44 (GP-2b 3, GP-3b 1, GP-5b 4,
GP-6b 1, GP-8a 6, GP-11b 7, GP-12 3, GP-13 6, GP-14 2, GP-15 11). Asked of Jordan: 0 rows (the one ask, §6, is about an item's eligibility).

### §1.1 Where the dispositions disagree (THROUGHLINES §6), resolved

| primitive | the disagreement | resolution, and on what |
|---|---|---|
| P09 vote | `D_T05 #27` grades a kernel ballot HAS (TESTS-ONLY); `D_T09 #88` says no vote exists | **Both hold at different tiers.** The ballot is in the SC kernel, which the season does not adopt (overview §2.3: "the code keeps the roll and does not adopt the kernel", SM-15); no season act resolves a vote. GP-12 declines a faction vote and names SC as its owner |
| P12/P14 binding agreements | `D_T05 #53` finds binding commitment as a Tenure edge (HAS); `D_T09 #46` finds a treaty non-binding in effect | **Both hold; they measure different halves.** The carrier binds in Layer 1's sense — an edge whose close is public, witnessed and *"priced by reception, and accepted by ruling"* (C-1, quoted at `VT:1044`) — and nothing *performs* its terms, because no reader exists (`VT:311`). CP-T09-03 adds performance on the one content that needs no new carrier (the war Proposition); the bond stays reception |
| P11 at faction scale | `D_T10 #60`: stance rows may name a faction and `stance_toward` sums them (HAS); `D_T09_also #42`: nothing aggregates regard into a faction standing | **Superseded in part by IN-70** (PR #496, after both rows' base): `WQ:2072` `opinion_of` is one person's opinion of a faction, computed at read on `[-3, +3]` (`PQ:541-549`). `#42` still holds for a *public* standing a third party reads; GP-14 declines that. `#60` holds for the stored half (`PQ:70-79`) |
| P20 upkeep | `D_T09 #35` and `also #18` grade unpaid-service lapse HAS; `D_T08_also #24` records the payment as DIFFERS (an act, not a charge) | **Compatible, as THROUGHLINES says, and the cadence is ruled:** the lapse is MATTER's term maturity (T-n) and the payment is a `transfer` because a MATTER charge "would be a fourth clock" (`es/loop/effects_economy.py:291-292`, quoting `04` F.18). Nothing here changes either; but `D_T08_also #24` records the act-paid payment as a risk (0 `term.renewed` in every seed), and CP-T09-05's oath bond and CP-T09-07's retinues rest on `oblige` edges that lapse unpaid after four seasons, so G3 depends on T08's CP-T08-08 (the upkeep payment gets a question) |

## §2 Items

Nine items. Every one binds **Layer 2** (`engine/season/` code and the YAML it reads); none amends Layer 1, and each says so where it
comes close. The occasion terms all sit on **REM-21's `STAMPERS` registry** (`@stamps("<Class>")` in `WQ`, remediation part 02 `:324-346`,
unbuilt): it is the single owner of "what a question may carry", and this file adds terms to it, never a second registry. Each term
below is a **new stamper body** (or, for CP-T09-01's join, a filter on T02's), registered and checked separately under REM-21 (v)'s
`check_stampers()`; none inherits REM-21 (iv)'s "no fifty petitions" property, which belongs to stamping a question's own plain referents,
and each is bounded instead by the question it attaches to. A class is
shared by every row that declares it, so each term carries the **shared-class cost, measured** clause the tree already uses (REM-25,
REM-2C, REM-27; the H-163 precedent): the wrong-kind formations a term causes are counted at `aperture 1 s` and a stopping rule reverts
the term if they do not fall. Every realm reading is **recorded, not required** (P1 §0.5's precedent, as REM-27 states it).
Shorthand: *mover* = moves the seeded content hash and is declared in its commit, with the pre-change hash read on the base commit
first; *base* = `[MEASURED-HEAD]` above unless named.

### CP-T09-01 · Allegiance follows opinion: join, leave, switch

- **Adds.** (rulings sheet R9) **Join is a filter, not a route.** T02's CP-T02-05 `oughts_named` is the one stamper by which a person
  takes up a cause he has heard of; creeds are OUGHT (`WQ:1961-1965`), so without a filter `commit` forms on every rival creed he has
  heard of, ungated. This item filters that stamper's output for **creed** Propositions (rostered factions' only; other OUGHTs pass
  untouched): a rival creed F passes iff `opinion_of(w, p, F) > max(0, opinion_of(w, p, own))` (own = 0 for a person in no faction).
  `commit` (REM-23's class) then forms only on creeds he favours over his own. **Leave** is a new stamper body: on a question whose
  referent is the head of p's own faction (the creed subject, `WQ:2099-2100`) or a member-doer his ledger names, stamp his own creed iff
  `opinion_of(w, p, own) < 0`; `release` forms on it (T02 offers an own cause for release only when it is met or spent). A switch is the
  two in turn, each his own act; **joining before leaving** gives two memberships, which by `faction_holding` (`WQ:1649-1660`) makes any
  land he holds uncontrolled (`WQ:1731-1733`) — declared, not prevented. The score is untouched (`es/decision/choose.py:130`). A
  discontented member's **petition** to his head needs no term: the head is tier 0 for every creed member (ambition referent, IN-57) and
  REM-24 classes `petition` on Person. Execution of a computed `commit` is also screened by IN-57's own-act screen (ED-IN-0296 (3),
  remediation part 02 `:383`), which this item does not decide.
- **Owner · Layer.** `WQ` (the filter, registered and checked as its own body on `oughts_named`'s output; the leave body; the
  indifference point 0 named once, beside `opinion_of`, and read by IN-70's gate at `WQ:2157` too) · Layer 2. Note `opinion` is documented
  as consumed only as `< 0` (`PQ:545-547`); the join reads it as `>`, so that docstring changes in the same commit.
- **Primitives.** P11 at faction scale (IN-70), P33 (scar-shifted pursuits enter `opinion_of` through `projected_axes`), P08 refused
  (dual membership stays possible and priced by land, as built).
- **Reads / writes.** Reads `opinion_of`, `faction_holding`, `members`, the creed Propositions. Writes nothing; the acts it lets form write
  `(Tenure, since)` and `(Tenure, until)`, existing matrix pairs.
- **Joins.** T02 (persons): **CP-T02-05** (`oughts_named`, the stamper this item filters), REM-21's registry and REM-23's class. T05 (SC):
  `petition` on Person (REM-24). T08 (GV): land follows `faction_holding` with no edit.
- **Decision.** Whether to act on the occasion (join, leave, petition, or any other act the question offers). Unwatched: one witnessed
  deed by a head (a killing, a seizure, a revocation) moves the regard term of every witness's `opinion_of` at once, so a faction loses
  members — and, through `faction_holding`, their land — in one season with nobody aiming at land: Imperator's secession (`D_T09 #28`)
  without its timer, and a shock on a ruler's death (`#71`), since a dead head leaves the regard term.
- **Falsifier.** Hand-built through the real fold, seed 0, tick 0: two Crown members with equal pursuits; one carries a stance row
  (−5, 5) toward the King. His question about the King carries `fac_crown` and `release` on it forms; the other's does not. Mutation:
  delete the leave body → neither forms. Join arm (on T02 landed): a person in no faction who holds a told claim naming `fac_varfell`
  (so `oughts_named` offers it) and a positive stance toward Varfell's creed subject → `commit` to `fac_varfell` forms and executes, and
  `members(fac_varfell)` lists him; the same person with a negative stance → the filter removes it and no `commit` forms. Mutation: drop
  the filter → the second arm forms it.
  Realm reading: faction `commitment.made` / `commitment.ended`, seeds 0-2, base 0 / 0.
- **Control.** Against **T02 landed** (CP-T02-05 built, this item off): the filter and the leave body off reproduce that arm's hash;
  seeds 0-2 paired. The control's own reading is the number of computed faction `commit`s on rival creeds T02 alone produces.
- **Measure first, both halves.** IN-58 found that stance reaches formation only under `stance_polarity: declared` (`_part5:138`), and
  B-V's prefect read no negative `legitimacy` at its three placements (`_part7:122`). The join gate is the opposite risk: `opinion_of`'s
  pursuit term is a cosine against a faction's expected pursuits and needs no deed (`PQ:513-517`, `:532`), so it can pass at tick 0 for
  anyone whose pursuits fit a rival's template. One hash-equal reading at ticks 0-2 comes first: how many members read their own faction
  below 0, and how many (person, rival creed) pairs pass the join gate. If none read below 0, the leave body is not built; if the join gate
  passes for most of the cast at tick 0, the filter is too loose to build as written; either residue is recorded (REM-26's shape).
- **Hash · revert.** Mover · remove the filter and the body. **Size** M.

### CP-T09-02 · `declare`: a war has a producer, an occasion and a target set

- **Adds.** (a) **The `declare` row** as `FA §3.3` S2 designs it: a seat-holder `via` a seat granting `dispatch` (`march`'s and `raze`'s
  eligibility, `VT:1109`; but see §6 A1); subject the target faction's creed Proposition; stratum `binding_decision`, so the chronicle's
  kind filter carries `war.declared` to every living ledger (`es/epistemic.py:649-686`, per `T09 §2.1`); writes `(Proposition, exists)` —
  mood `WAR` (`FQ.WAR_MOOD`), subject the seat's faction creed, value the target — and `(Tenure, since)`, the declarer's own `commit`, so a
  war is never "of one" (FA-G03); refuses (`declare.refused`) a target that is his own faction or no rostered faction's Proposition;
  celled on the seven axes in IN-08's pass (IN-08 → every verb-adding position, `_part5:44`). The row declares **`referent_class:
  Proposition`**, so it forms only on Proposition-classed referents (an unclassed row forms on every plain referent, `RY:604-608`;
  `commit`'s 66/0 before REM-23, remediation part 02 `:381`). Its feeders are T02's `oughts_named` as CP-T09-01 filters it, and term (b).
  **`at_war` is edited, as `FA §3.3` S2 asks** (verbs-15 `:130`, `:159`; M1 `:580`): it counts only WAR Propositions whose creating
  Event's causing act is a `declare` (read through `state/attribution.py::causing_act`, the reader `EI:992` uses). Without it an `own`
  `utter` of mood WAR plus a `commit` (`FQ:234-238`; `at_war` needs a live commit, `FQ:250`) still makes a war that term (c) reads, and
  §6 A1 would be moot. The hand-built WAR chains in `es/tests/test_faction_q.py:220-260` are re-recorded to mint through `declare`.
  (b) **The grievance occasion**: a new `Proposition`-class stamper body on a question for which IN-70's `opinion_referents`
  (`WQ:2108-2161`) is non-empty — a **wound** p judges, by a doer of faction F that p regards below indifference — stamping F's creed.
  **A killing raises nothing yet:** a dead victim's claim is held and never asked about (H-209, `es/hole_register.yaml:4539-4545`;
  `WQ:2124-2125`), so no killing starts a war until H-209 closes (T03, T05 and T10 name the same hole). IN-72's tier 2 acts on wound
  (`body.changed`) and `contest.undecided` claims only.
  (c) **The war's target set, `at_war`'s first production reader** (M1): a `Rung`-class standing term for a holder of a seat granting
  `dispatch` or `issue` whose side in a live war W is `seat_faction(via)` when that faction is one of W's two sides, else `side_in(w, p,
  W)` (an ally, CP-T09-03) — one rule, consistent with `sides_of` and `occupying_faction`, which also key on the seat: the settlements the other side holds
  (`holder_faction_of`) inside that seat's purview (`es/state/gate.py:353` `purview_reaches`). `march` (classed `Rung` by REM-27) and the
  seat's self-warrant `issue` form on them, and `seize` then forms through `warrant_sourced` (`RY:1912`). War widens a seat's targets from
  the towns its ledger names (REM-27's `fields_named`) to every enemy town it reaches; when every committer has released W, the term
  withdraws. Nothing is refused (direction 8; "a march needs no war" stays true).
  (d) **Rallying**: on a question about a `war.declared` claim, stamp W for a person whose faction is one of W's two sides; `commit` to W
  forms (defenders too — `at_war` is symmetric).
- **Not built.** A world-tension or aggressive-expansion meter (`D_T09 #19`, `#53`: T-a); a phased play with a countdown (`also #1`:
  T-c); a casus-belli gate on `march` (direction 8). A coalition against an expander is several declarations on one public grievance.
- **Owner · Layer.** `VT` (the row), `es/loop/effects_information.py` (`_eff_declare`, `_eff_utter`'s one mint and `_eff_commit`'s opener
  in one write), `WQ` (three terms) · Layer 2. The new verb is checked against `architecture/VOCABULARY.md` at the build, `give`'s
  precedent (`VT:594`) [UNVERIFIED].
- **Primitives.** P06 (the price is a public deed and exposure, not a currency), P12 (war as one state on a ladder of one), P35 (MB
  resolves what forms), P27 (the declaration spreads through the chronicle).
- **Reads / writes.** Reads `opinion_referents`, `opinion_of`, `holder_faction_of`, `purview_reaches`, `at_war`, `side_in`. Writes
  `(Proposition, exists)`, `(Tenure, since)` — existing pairs (`utter`, `commit`).
- **Joins.** T04 (MB): the Rung stamper already carries REM-27's `fields_named`; this term sits beside it, deduped by REM-21 (iv-b), and
  MB fights what forms. T06 (information): `war.declared` is realm-public through the chronicle kind filter, live at HEAD
  (`es/epistemic.py:685-686`) — but its docstring schedules the filter's deletion in the change that builds the `<rung kind>` reach channel
  (`:675-684`), which is one of `ED-IN-0298`'s options; the publicity of a declaration depends on that channel being kept or replaced.
  T02: CP-T02-05 and IN-08's cells for `declare`; the hostile ranking depends on `stance_polarity` (ED-IN-0296's ask-then), which this item
  does not decide. **H-209** (a dead victim's claim raises no question) is a dependency for wars over killings.
- **Decision.** A marshal decides whether a grievance becomes a war; members decide whether to rally; seat-holders at war decide which
  enemy town to march on. Unwatched: a wounding across factions becomes a war (a killing too, once H-209 closes), the war offers every
  enemy town a seat reaches, and the declarer's own towns enter the enemy's set — the cost of declaring is becoming a target.
- **Shared-class cost, named.** `declare` and `commit` share the Proposition class: term (b)'s creed stamp lets `commit` form on the hated
  faction's creed, and CP-T09-01's filtered (favoured) creeds let `declare` form on a faction the declarer favours. Stopping rule: if any
  computed faction `commit` names a faction the committer reads below 0, or any computed `declare` names one the declarer reads at or above
  0, revert (b) and record the residue against REM-21's per-row `referent_source:` question (K4). A seat whose purview a won `recruit` of
  a seat-holder widened (IN-40's `oblige` clause, `es/state/gate.py:389-398`; CP-T09-07) reaches across factions, so term (c)'s target set
  grows with every sworn seat-holder: counted in the same reading.
- **Falsifier.** (1) Hand-built: a Hafenmark seat-holder with a `dispatch` grant who holds the firsthand claim of a Crown member
  **wounding** a Hafenmark man (`body.changed`, the `seen.who` pairing naming the Crown member) and reads `opinion_of(fac_crown) < 0` forms
  `declare` on `fac_crown`; executed, `at_war(fac_hafenmark, fac_crown)` is True and a person not co-located holds a `war.declared` claim
  at the next WITNESS. Control: a hand-built `utter` of mood WAR **plus** a `commit` leaves `at_war` False (the S2 edit). (2) With W live,
  a Crown `dispatch` seat forms `march` on a Hafenmark-held settlement its ledger never named; with every committer released, the same
  seat forms none. Mutation: delete term (c) → none. Realm reading: WAR Propositions, `war.declared`, `field.won` + `field.lost`, seeds
  0-2; base 0, 0, 0.
- **Control.** The formation count: with term (b) off, `declare` forms only on the filtered `oughts_named` creeds — that count, with
  `declare.refused`, is the arm term (b) is measured against (the row alone moves the hash, by its load and its formations, a declared
  mover of the verb-table pins); seeds 0-2 paired.
- **Hash · revert.** Mover · the row, the three terms and the `at_war` edit (re-records `es/tests/test_faction_q.py:220-260`). **Size** L.

### CP-T09-03 · Alliance and peace are acts on the war Proposition

- **Adds.** No content roster, one roster cell and one Query. (a) **`side_in(w, p, W)`** in `FQ`, beside `at_war`: p's faction if it is W's
  subject or value; else the faction of the seat that issued a dispensation p holds, is addressed by and whose `terms` is W — the issuing
  seat read through `state/attribution.py::causing_act`, the read `EI:992` `_issuing_seat` already makes (moved to one shared reader, not
  copied); else `None`. CP-T09-02 (c) reads it, so an ally fights on the side that invited him. (b) **Alliance**: a `covenant` whose subject
  is W — in the maker's reach through his own `commit` (`WQ:785-817`, limb 2) — addressed to a person of a third faction; acceptance is his
  `commit` to W through the existing `terms_sourced` route (`RY:1951`); he is then at war on the maker's side. (c) **Peace**: the same
  covenant addressed to a person on the other side; acceptance is his `release` of his own `commit` to W, formed by `terms_sourced` gaining
  `release: [dispensation]` (one roster cell). The offerer's own release is his own act; the war ends when no committer is left
  (`FQ:229-233`).
- **What binds.** Reception, by ruling: a peace broken by a new `declare` is a public deed judged at its cells, *"public, witnessed,
  priced by reception, and accepted by ruling"* (C-1, `VT:1044`). Nothing refuses it. Truce, tribute, dated terms and the pact chain are
  declined (GP-5b, GP-13).
- **Owner · Layer.** `FQ` (`side_in`), `RY: terms_sourced` (one cell) · Layer 2.
- **Primitives.** P12 (alliance and peace as states on the war), P14 (the instrument is the obligation token), P27.
- **Reads / writes.** Reads held dispensations, `causing_act`, the WAR Propositions. Writes nothing new; `covenant`, `commit` and `release`
  write their existing pairs.
- **Joins.** T08/GV: `covenant` as built (IN-12 step 7). T04: an ally marches with his own seat's army; M3's ally-in-`mustered` half is not
  built (a joint army would widen `occupying_faction`'s occupation too). CP-T09-08 delivers an instrument at a distance.
- **Decision.** Whom to invite, whom to offer peace, whether to accept. Unwatched: wars widen on invitation and end on sealed peace,
  every step a person's act.
- **Asymmetry.** `terms_sourced` is read person-side by `decision/options.py` (formation only; `T09 §2.6`); no getter of world state
  changes.
- **Falsifier.** (1) Hand-built: a Varfell seat-holder holding the Crown's covenant on W(Crown, Hafenmark) forms `commit` to W; afterwards
  CP-T09-02 (c) offers him Hafenmark-held towns in his purview. Control: without the instrument, neither. (2) A Hafenmark committer
  holding a Crown peace covenant on W forms `release` on W; executed, his edge closes, and with every committer released `at_war` is
  False. Mutation: drop the `release` cell → no release forms from the instrument. (3) **One instrument, two offers:** `terms_sourced`
  forms each listed verb on whatever the held writ's terms name (`RY:1960-1968`), so a peace covenant held by an enemy committer also
  offers him `commit` to W — an escalation, or a redundant second edge if he already holds one. Stated, not prevented; the arm records
  which forms (`release`, `commit`, or both) and how often each is chosen, and a `commit` chosen from a peace offer is counted in
  CP-T09-02's stopping reading.
- **Hash · revert.** Mover · the cell and the Query. **Size** M.

### CP-T09-04 · Land with no holder, and territories, are taken by plurality occupation

- **Adds.** Edits at one owner, `es/loop/effects_shared.py:149` `occupying_faction`, which `seize`'s Rung half and `raze` share, and an
  occasion. (a) **Unheld place** (H-166): for `seize`, a place whose `holder_faction_of` is `None` licenses when the seat's faction is the
  strict plurality of the factions `mustered` there. **`_eff_raze` has no decline of its own** — it relies wholly on `occupying_faction`
  (`es/loop/effects_founding.py:285-287`), and the `holder is None` test lives in the shared owner (`es/loop/effects_shared.py:163`) — so
  the same commit adds the "nobody holds the place" decline to `_eff_raze` explicitly; without it `raze` would destroy every unheld
  settlement (after the season-0 collapse, those under 11 of 16 territories). `raze`'s realm reading (base 22 reached the fold / 0 ok) is a
  declared mover. (b) **Plurality against a holder, for a town taken without a fight**: where no field was won there this round, a held
  place licenses only when the seat's faction has strictly more members mustered there than the holder's faction — Pax Pamir's rule
  (`D_T09 #44`), replacing "one resident suffices" (`T09 §5b`) and re-recording the arm at `es/tests/test_march.py:918-930`. **After a won
  field the licence is unchanged**: a won field removes no defender (`es/tests/test_march.py:913`), and the seizure that follows is
  admitted by #453 exit (vii) (`EI:958-959`, pinned at `test_march.py:893-915`); T04 relies on it ("Title after a win is already
  `seize`", T04's file `:76`; its §4 walk-through takes title by `seize` after an arrival). Plurality after a win too is the stated revert, and
  taking it re-records `:893-915` and collides with T04. "A field was won here this round" is read off the round's own `field.won`
  Event naming the place [UNVERIFIED: which Event field names the field's rung]. (c) **Territories**: `seize`'s target kinds become a roster key, `RY: seizure_target_kinds`
  = `march_target_kinds` ∪ {territory}, taking the stated revert of the open assumption at `EI:961-963` (*"revert: any Rung kind, the
  licence still occupation"*), restricted to territory; `raze` still reads `march_target_kinds`. A territory's occupation is `mustered` in
  its subtree (`WQ:1477` reads the subtree). (d) **The occasion — IN-30 re-scoped** (an edit to `_part5:66-71`): a `Rung`-class standing
  term offering a holder of a seat granting `issue` the rungs `uncontrolled` (`WQ:1714`) returns inside that seat's purview where the seat's
  faction is mustered; the seat's self-warrant (`issue`, C3, `VT:1141`) forms on them and `seize` follows through `warrant_sourced`. This
  is the production caller IN-30's EXIT asks for (`_part5:70`); IN-30's emergence half stays IN-30's.
- **Consequence.** After a death the land is contested by every seat that reaches it, in order of who has people standing there; the
  victory row `peninsular_sovereignty` becomes reachable (`terr_T15` can be taken), and its assumption note (`RY:2591-2592`, *"no verb opens
  a `hold` on any territory"*) is rewritten in the same commit — it is already stale for cession (`give` + Rung opens one).
- **Owner · Layer.** `es/loop/effects_shared.py`, `EI` `_seize_rung`, `RY` (one key), `WQ` (one term) · Layer 2.
- **Primitives.** P35 (the field, where one is fought), P42 (the existing ending row made reachable); Pax Pamir's rule by plurality
  (`D_T09 #44`) as the licence.
- **Reads / writes.** Reads `mustered`, `holder_faction_of`, `uncontrolled`, `purview_reaches`. Writes `seize`'s existing pairs.
- **Joins.** T08 (GV): `seize` (remit `issue`) and the self-warrant, and **`raze`'s occupation licence**, which is GV's act on a place
  (routed to T08, not T04): it moves with (a)'s explicit decline and (b). T04 (MB): none required; the won-field licence T04 relies on is
  kept.
- **Decision.** A seat-holder chooses whether to take the land his people stand on; any member's residence is a vote of presence.
  Unwatched: the season-0 collapse (11 of 16 territories uncontrolled at tick 2 in every seed) becomes a scramble instead of a steady state.
- **Asymmetry.** `occupying_faction` is a getter with two callers (`seize`, `raze`; grep both before the edit); the writers of `contain`
  and `hold` are untouched.
- **Falsifier.** (1) Seed 0, tick 1, King dead: the Widow Regent's seat (`off_npc_032`, realm purview, `issue`) seizes a former royal
  territory where Crown members are the plurality; a territory where another faction outnumbers the Crown refuses. (2) (b)'s arm at
  `set_s_036` (Church 6 of 9 persons, Crown 1), no field: `seize.refused`; move at least six more Crown members in (Crown 7 > Church 6) →
  `rung.seized`. Mutation: drop the comparison → the first arm executes. (3) After a won field at `set_s_036` the seizure is still admitted
  (`test_march.py:893-915` unchanged). (4) `raze` on an unheld settlement → `raze.refused` (the explicit decline). Realm reading:
  `uncontrolled` at tick 2, seeds 0-2, base 11; `raze`, base 22/0.
- **Stopping rule.** A seat's purview widens with every seat-holder sworn to it (IN-40's `oblige` clause, `es/state/gate.py:389-398`), so
  a won `recruit` (CP-T09-07) of a rival seat-holder brings his ground into term (d)'s seizable land across factions: the reading counts
  seizures through a sworn seat's ground separately, and if they exceed seizures in the seat's own ground, the `recruit` arm is reverted
  first.
- **Hash · revert.** Mover (re-records `test_march.py:918-930`; `raze` moves) · per sub-edit: H-166's decline back; one head; the roster
  key; the term. **Size** M.

### CP-T09-05 · Land rewards the sworn: an occasion for a fief

- **Adds.** On a question about a person X who holds a live `oblige` to one of p's seats (`establishment_of`, `WQ:1868`), add the rungs p
  holds as **plain** referents — the shape IN-70's `opinion_referents` already uses to add plain referents to a formed question — so `give`
  + Rung (PR #496, `VT:571-592`, unclassed) forms on them. **The occasion is bounded; the recipient is not:** `give` fans `to` over every
  person the giver knows — *"the receiver is somebody known, never the referent"* (`VT:585`) — so X is one of the candidate receivers,
  not the only one. Binding `to` to the question's referent would be a new formation rule for one term (shape divergence), so it is not
  proposed; the bound is the stopping rule below.
- **What it buys, stated narrowly.** **Land moves to a follower.** `give` is celled, and the cells are null on six axes and −0.2 on
  `deontological_instrumental` (`RY:3192`, `:3238`, `:3278`, `:3335`, `:3376`, `:3429`, `:3487`), so a witnessed cession does not raise the
  grantee's regard of the giver: the "a granted man stays" arm fails by construction today. It becomes true only with a demand on v9
  IN-08's cell pass — a `deed:rung.ceded` cell pair, the shape IN-11 names for `deed:commitment.ended` (`VT:1039`) — which this item asks
  for and does not author. The bond that exists without it is the oath: the land lies under the liege's purview through it (IN-40); if the
  vassal defects, CP-T09-04 lets the liege's seat retake it by plurality.
- **Owner · Layer.** `WQ` (one term) · Layer 2.
- **Primitives.** P15 (the office slot whose holder is rewarded), P14 (the oath as the token), P11.
- **Reads / writes.** Reads `establishment_of`, live `hold`s. Writes `give`'s existing pair.
- **Joins.** T08 (GV): `give` + Rung as built; IN-08 (the `deed:rung.ceded` cell, demanded); T08's CP-T08-08 (the oath lapses unpaid
  otherwise).
- **Decision.** Whom to reward, and with what; the grantee's loyalty stays his own. Unwatched: lords hand land to their men; whether a
  grant keeps a follower longer waits on the IN-08 cell.
- **Shared-class cost, named.** Other unclassed rows may form on the added Rung referents, and `give` may name any known receiver;
  both counted. Stopping rule: any computed cession to a person holding no `oblige` to the giver's seat, or the realm's held territories
  falling against the base over two seasons with no rise in obligees' holdings → revert.
- **Falsifier.** Hand-built: a territory holder with a seat and a co-located obligee forms `give {subject: terr, to: obligee}`; executed,
  `rung.ceded` and the obligee holds it. Control: the same holder with no obligee forms no `give` on the rung. The reward arm, run only
  with the IN-08 cell authored: the grantee's `regard` of the giver after the cession exceeds it before; at today's cells it does not,
  and the item says so. Realm reading: `rung.ceded`, and cessions to non-obligees, seeds 0-2, base 0.
- **Hash · revert.** Mover · the term. **Size** S.

### CP-T09-06 · The Crown's own ducal seat can be refilled (data only)

- **Adds.** `es/offices.yaml`: `off_duke_valorsmark` (the King's second seat: post Duke, rung the Crown duchy, faction Crown, `revocation:
  null`, `offices.yaml:196-204`), `conferral: null` → `appointed` [ASSUMPTION; medium; Jordan to correct]. A vacant Valorsmark then enters
  the `vacancies` of a seat with `confer` and purview over the Crown duchy (IN-53, `WQ:2164`) — the realm seat — so the Widow Regent or a
  crowned heir appoints a Crown duke. It sits in the hereditary set the file's translation left null as "a JUDGMENT CALL flagged for
  attack" (`offices.yaml:43-44`), and IN-61 keeps it out of the `successions` registry — *"not inherited with the throne"*
  (`_part5:159`, LIMITS) — so without a basis it is empty for good; `appointed` is that limit's answer, and IN-61's throne is untouched.
- **Not done, and why.** `off_duchess_hafenmark` stays null: `appointed` would let the Crown's realm seat appoint a rival faction's head,
  and the row's own note says the seat is *"unreachable by the Crown specifically — a real consequence of the ruling, not smoothed over"*
  (`offices.yaml:219`; no duchy is in anyone's holdings as built, `:83-84`). Its route is `elected` by its own body, which waits on the
  unruled "which act fills an `elected` seat" (`RY:2289-2303`, ED-IN-0256 (2)); a residue, not an ask. The `off_npc_084` row is IN-61's
  content decision (rulings R4): it is rungless (`offices.yaml:125-126`), a rung of `None` is reached by no seat's purview, and a row
  here would be inert. The precedent claim the first draft made from Jordan's 2026-10-12 revocation is withdrawn: that note sits on the
  Hafenmark and Varfell rows (`offices.yaml:215`, `:228`), not on Valorsmark's.
- **Owner · Layer.** `es/offices.yaml` (content) · Layer 2. No code: `may_fill` admits every rostered basis today (`es/state/gate.py:675-697`).
- **Primitives.** P30 without lineage (the seat passes by an act, not by blood), P15.
- **Joins.** T08 (GV): `confer`, `vacancies`, `may_fill` unchanged. IN-61's gate edit (`may_fill` refusing `inheritance`) does not touch
  `appointed`.
- **Decision.** The realm seat chooses whom to appoint. Unwatched: the Crown's duchy, emptied by the King's death, is refilled instead of
  staying empty.
- **Falsifier.** Seed 0, tick 1, the King dead: the Widow Regent's `vacancies` lists `off_duke_valorsmark`, and her `confer` on a known
  person executes. Control: `null` → absent. Realm reading: seats still vacant at tick 2, seeds 0-2, base 8 / 6 / 10 (`T09:451`).
- **Hash · revert.** Mover · `null` again, or the `annex`-by-land reading cut in §3. **Size** S.

### CP-T09-07 · Service that serves: `recruit`, and the seat's obligees in its army

- **Adds.** (a) **The `recruit` row** as `FA §3.3` S3: a seat-holder `via` a seat granting `confer` [S3's ASSUMPTION], `to` a known person;
  contested on the counterparty through the season's social roll, the obstacle read world-side at the fold — his live `oblige` or
  `commit` to a rival seat or faction, his `opinion_of` the recruiter's faction (IN-70), his regard of the recruiter. These terms are an
  **explicit demand on the obstacle's single owner, `modules/social_contest/roll.py::obstacle`** (T05's file `:389-390`); T05 has no
  `recruit` item and "M10" is verbs-15's name for this demand, not a T05 item (rulings R10). Won opens his `oblige` to the exercised seat
  with `oblige_term` (the edge, its upkeep and its lapse are built); Lost emits `recruit.declined`, a witnessed refusal. Opening an edge
  the counterparty owns has its precedent: `determine`'s disposal opens an `oblige` owned by the party it binds (C-1, RULED A, `VT:1044`).
  (b) **Obligees march**: `es/loop/sides.py:115`'s claimants become `mustered(origin, faction)` ∪ the exercised seat's obligees present
  in the origin's subtree (`establishment_of(via)`), and `es/state/gate.py:865` `may_muster` admits a moved man holding a live `oblige`
  to `via` as well as one committed to its faction. Retainers fight (`D_T09 #15`); a vassal's oath yields men (`#2`).
- **B-V, declared.** Under `build_realm(guards=True)` the guard cohorts' `oblige` to the throne and duchy seats (`_part5:152`) puts
  cohorts in those seats' armies — a weight-carrying army that JQ-4's weight → troop value then prices. Read on that arm only (default
  OFF).
- **Owner · Layer.** `VT` (the row), its effect beside `_eff_oblige` in `es/loop/effects_governance.py:420` (the `oblige` opener, with the
  literal `Tenure(..., "oblige")` that `data/verbs.py`'s opener walk reads), `es/loop/sides.py`, `es/state/gate.py` · Layer 2.
- **Primitives.** P14, P20 (upkeep and lapse, built), P18 (a seat's retinue), P23 (the contest).
- **Reads / writes.** Reads ties, `opinion_of`, regard, `establishment_of`. Writes `(Tenure, since)` and `Tenure.term` on `oblige`
  (existing); (b) writes nothing.
- **Joins.** **T05 (SC):** the obstacle terms above, added at `roll.py::obstacle`, and a `contests:` prize on the season roll whose Won
  band opens the counterparty's edge. **T01:** at the shipped ceiling (default 2 = ceiling 2, `es/data/fixtures.py:416-419`;
  `modules/social_contest/roll.py:89-113`) an added obstacle term is clipped, so falsifier (1) runs on H-213's uncapped arm, whose owner is
  T01's CP-T01-06 (rulings R2). **T04 (MB):** none demanded — this item owns the `sides_of` claimant edit and `may_muster`'s clause; it
  merges with T04's CP-T04-01 (one subunit per person on a side: each obligee becomes his own subunit) and CP-T04-04 (the field fought a
  round later, which edits the same `es/loop/sides.py`), batch order to be set by the batch. **T08:** CP-T08-08 (a retinue lapses unpaid
  without it).
- **Decision.** Whom to bring into service, whom to pay, whom to take to the field. Unwatched: seats compete for men, poach from rivals,
  and lose retinues they do not pay.
- **Asymmetry.** `may_muster` and `sides_of` are getters; the openers of `oblige` (`oblige`, `determine`'s disposal, B-V's guard build)
  are untouched — grep the `oblige` opener list (`data/verbs.py` `_OPENERS_FROM_EFFECTS`) before the edit.
- **Falsifier.** (1) S3's, on H-213's uncapped arm: a seeded `recruit` of an unattached known person opens his `oblige` on Won; over seeds
  0-9, a person with a live `oblige` to a rival seat is declined more often (control: the tie removed). A won `recruit` of a seat-holder
  also widens the recruiter's purview over that seat's ground (IN-40, `es/state/gate.py:389-398`), feeding CP-T09-02 (c) and CP-T09-04
  (d) across factions — counted in their stopping readings. If the degree distribution does not move with the tie, the
  obstacle is not reading him. (2) A hand-built settlement march whose marcher's seat has one obligee, not a faction member, at home:
  the army is one larger than base. Mutation: drop the union → base.
- **Hash · revert.** Mover · the row; the union and the gate clause. **Size** L.

### CP-T09-08 · `dispatch` sends: an obligee posted to a place

- **Adds.** The `dispatch` row rebuilt per `FA §3.3` S5, **without** its posting payload (S5's `Tenure.payload` has no reader, M5; a write
  nothing reads fails ID-13): subject a destination Rung inside the seat's purview, `to` a person; the effect relocates `to` through
  `_relocate(w, a, dest, mover)` (`es/loop/effects_migration.py:91`, the mover-not-actor body, which also charges him the journey's leg)
  iff he holds a live `oblige` to `via`; otherwise `dispatch.refused`. Writes the `contain` pairs `march` writes; `order.given` stays.
  His answer is his own: he acts on what he finds at the post, `move`s back (desertion), or `evade / defy`s once REM-2B restores it — a
  compliance below one that is attributable to him (`also #31`, `#60`). **Envoy**: a seat-holder hands his covenant to his obligee
  (`give`, at home) and sends him; the obligee's own `give` delivers it, which is how CP-T09-03 works at a distance.
- **The gate, and the dependency.** Moving another person's presence is admitted only by the gate's MUSTER basis
  (`es/state/gate.py:1222-1230`; `_relocate` leaves that to the gate, `es/loop/effects_migration.py:105`), and `may_muster` requires a
  `commit` to the seat's faction (`gate.py:885-888`): a non-member obligee is refused until CP-T09-07 (b)'s `oblige` clause lands. So this
  item **depends on CP-T09-07 (b)**.
- **Owner · Layer.** `VT` (`dispatch` rebuilt; the name is D-V7's), its effect, `es/state/gate.py` (through CP-T09-07 (b)'s clause) ·
  Layer 2. The row is graded `ruled` with the writes_note *"it names a person; their own choose decides"* (`VT:422-423`): the rebuild
  changes a ruled row, so it is listed in §6's rulings touched. **Lane, flagged:** T10 routes `dispatch` to T08 (T10's file `:82`) and T08
  declines moving a man for an employer citing T-e (T08's file `:58`); T-e is *"An `Event` carries no target"*
  (`architecture/meta/01_AXIOMS.md:404`), which does not forbid a re-home the MUSTER basis admits. `dispatch` is an FA host by the
  verbs roster (`FA §3.3` S5); the orchestrator reconciles the lane.
- **Primitives.** P04 without a clock (the posting lasts until he leaves), P15, P17 refused (no standing order: the agent decides).
- **Reads / writes.** Reads `oblige`, `purview_reaches`. Writes `(Tenure, until)`, `(Tenure, since)` on `contain`, `Person.travel_leg`.
- **Joins.** T10 (WT): `_relocate` and its leg. T06: nothing returns by itself — the result reaches the principal only through the agent's
  own `tell` or `give`, or a witness; no report channel is added (a reach channel is a Layer-1 C.6 row, the question `ED-IN-0298` holds).
- **Decision.** Whom to send where; the agent decides what to do there. Unwatched: seats place men, men desert, envoys carry treaties.
- **Shared-class cost, named.** `to` fans over known persons and the fold refuses non-obligees (a scene tax); REM-28 already lists
  `dispatch`'s refusals for a reading first. Stopping rule: refusals rise and executions do not → revert. (Base: my probe's `dispatch`
  14/7 counts `order.given` as a non-refusal; the row's note "14 of 15 computed orders name a non-person" is the old in-tree figure
  `T09 §8` round-2 item 6 already corrected — the two count different things.)
- **Falsifier.** S5's: a dispatch of an obligee to another rung leaves his `contain` there; naming a non-obligee emits `dispatch.refused`
  and moves nobody. Chain: an envoy dispatched to the counterparty's settlement delivers a covenant and the counterparty's `commit`
  forms (hand-built).
- **Hash · revert.** Mover · today's row. **Size** M.

### CP-T09-09 · `conspire`: a plot with backers

- **Adds.** `FA §3.3` S7: any person (`own`), `to` an invitee. The first `conspire` with no plot held mints an OUGHT plot Proposition
  (subject the target seat's holder, predicate naming the seat) and the plotter's `commit`; a later one on a held plot is contested on the
  invitee (obstacle terms — his live `oblige` or `commit` to the target seat or its faction, his regard of the target — demanded of
  `roll.py::obstacle`, as CP-T09-07's; falsifiers on H-213's uncapped arm, T01's CP-T01-06); Won opens his `commit`
  to the plot, Lost emits `plot.refused` and leaves him a claim against the plotter (he may `petition`, or `arrest` from a seat). **The
  reader (M7) is already built:** a `commit` to an OUGHT is an ambition (`WQ:1946`) and an ambition's referent is tier 0 (IN-57), so every
  conspirator attends to the target first, and the hostile acts already on the table (`fight`, `challenge`, `petition`, `arrest`) form on
  him. The first act's occasion: a question about a seat-holder H for whom p's own `legitimacy(p, H)` (`PQ:452`) is below 0.
- **Owner · Layer.** `VT` (the row), its effect, `WQ` (the first act's term) · Layer 2.
- **Primitives.** P13 without a breach counter (exposure is witnessing; `conceal`, IN-12 step 10, does not hide `who` from those present,
  overview §6 #6), P27, P23.
- **Reads / writes.** Reads ties, regard, `legitimacy`. Writes `(Proposition, exists)`, `(Tenure, since)`.
- **Joins.** T05 (SC): the obstacle terms at `roll.py::obstacle`, as CP-T09-07. T01: the uncapped ceiling arm. T06 (FI): discovery by `surveil` / `interview`. T03 (PC): a coup's execution is a `fight`. T08
  (GV): `arrest` (PR #496).
- **Decision.** Whom to plot against, whom to invite, whether to join or denounce. Unwatched: plots gather among the discontented, and a
  refusal turns into a denunciation.
- **Measure first.** As CP-T09-01: B-V's foreign prefect read no negative `legitimacy` at three placements (`_part7:122`); one reading
  over the realm's persons toward seat-holders at ticks 0-2 first.
- **Falsifier.** S7's: a `conspire` on a held plot opens the invitee's edge on Won only; over seeds an invitee with a live `oblige` to the
  target seat refuses more often. The reader: a conspirator's first question each round is about the target where a non-conspirator's
  is not.
- **Hash · revert.** Mover · the row and the term. **Size** L.

## §3 NERS — the cut test over this proposal

Method: `skills/ners/SKILL.md`; definitions: `CLAUDE.md` §0.06. Instrument A only (nothing here resolves by a draw of its own; the
contests of CP-T09-07 and -09 are SC's roll, whose diagnostic is T05's).

**Cuts already applied while drafting** (each a false or narrowed N-line, the object removed):

| object cut | the N-line it claimed | why it was false or narrowed | disqualifier |
|---|---|---|---|
| a `covenant_contents` roster (peace, alliance, tribute…) | "a treaty must say what it is for a reader to perform it" | the war Proposition already carries the content: who commits to it is an alliance, who releases it is a peace (CP-T09-03) | 1, the carrier exists |
| an ally-in-`mustered` reader (M3's ally half) | "allies must fight in one army" | an ally marches with his own seat's army; widening `mustered` would also widen occupation (`occupying_faction`) | narrowed; a joint army is not needed for G5 |
| `dispatch`'s posting payload (S5's `Tenure.payload`) | "the posted man must know his task" | nothing reads it (M5 unbuilt); presence at the post already shapes his questions | 2, no reader (ID-13) |
| a plot reader (M7) | "conspirators must act on the plot" | `ambitions` + IN-57's tier 0 already turn every OUGHT committer toward its referent | 1 |
| a petition-the-head term | "discontent must reach the head" | the head is tier 0 for every creed member and REM-24 classes `petition` on Person | 1 |
| an `annex`-by-land rule for the duchies | "the title must follow the land" | narrowed: refilling the Crown's duchy survives with `appointed` and no code (CP-T09-06); what dies is only "the biggest landholder claims it" | kept as CP-T09-06's revert, MEDIUM |
| a fief bound to its sworn receiver (`to` = the question's referent) | "land must go only to sworn men" | a formation rule for one term (shape divergence); the stopping rule bounds it instead | cut; CP-T09-05's N narrowed to "land moves" |
| a casus-belli gate on `march` | "war must license attack" | direction 8 refuses a refusal-reader; war works by widening targets instead | refused by the tree |

**N — the N-line ledger for what remains** (each attacked by walking the loss with the object gone):

| item | N-line (cut it and the game can no longer…) | directions | verdict |
|---|---|---|---|
| 01 | …lose a member because of what he thinks of his faction, or gain one who was not born into it | bottom-up (a member's view), lateral (to a rival), vertical (land follows) | HOLDS. Attack: `release` exists and forms on own edges — but no candidate reflects opinion, and 0 faction edges closed at HEAD; nothing else carries the step |
| 02 | …go to war: no act makes `at_war` true and nothing reads it | top-down, lateral, diagonal (a duel's wound → a field) | HOLDS. Attack: a hand-built `utter` + `commit` makes `at_war` true today — but no computed act mints mood WAR (FA-G02), no reader exists, and the S2 edit closes that route |
| 03 | …bring a third faction into a war, or end one on an offer | lateral, horizontal | HOLDS, NARROWED: peace survives the cut as each committer's unprompted `release`; what dies is the offered peace and every alliance |
| 04 | …retake land after a death, take a territory, or make a contested town turn on numbers | vertical, bottom-up (residence as presence) | HOLDS. Attack: cession (`give` + Rung) moves held land, never unheld land |
| 05 | …move land to a follower in computed play | top-down, vertical | HOLDS, NARROWED: `give` + Rung exists hand-built; what dies is the occasion on a sworn man's question (0 formed at HEAD). "A grant keeps a man" is not an N-line yet: `give`'s cells give it no regard (`RY:3192` ff.), so it waits on IN-08 |
| 06 | …refill the Crown's duchy | top-down | HOLDS, NARROWED to one seat; cheapest item in the file (data only) |
| 07 | …have a seat initiate service, or a retainer fight | top-down, vertical, diagonal (a retinue to a field) | HOLDS, NARROWED for `recruit`: the joiner's own `oblige` survives (IN-10 (a)); what dies is poaching against a tie. HOLDS for the muster half |
| 08 | …place another man somewhere | top-down, lateral (an envoy) | HOLDS, NARROWED: an envoy's delivery survives the cut (the seat-holder can `move` and `give` himself); what dies is sending someone else, and the desertion that follows |
| 09 | …draw backers into a secret project, or refuse one | bottom-up, lateral | HOLDS, NARROWED: the lone killing survives (`fight`); what dies is the backers and the refused invitation. Weakest N in the file, ordered last, and the first to drop if its measure-first reading is null |

No false N-line remains among the nine. The trail: each row's attack is named; the disqualifier-4 check ("a reward for a behaviour the
ranking already weights") was run on 01 and 05 and fails to fire — the score never reads opinion, so an occasion gated on it is not a
second thumb on the scale. 01's join half is a filter on T02's CP-T02-05, not a second route (rulings R9): cut the filter and joining
survives, ungated; what dies is joining *by opinion*.

**R.** R-WORLD binds everywhere: every item throws hooks with no player (each block's "Unwatched"; §4 walks them together). R-COMPLETE at
the extremes: a plurality **tie** licenses nobody (the town stays its holder's; an unheld one stays unheld); a faction whose **head is dead**
loses the head term of `opinion_of` and keeps its member-doer term; **dual membership** stays legal and makes land nobody's, as built; a
**seat-holder who switches** keeps his seat as staff, and CP-T09-02 (c) keys on `seat_faction(via)` exactly as `occupying_faction` and
`sides_of` do (falling back to `side_in` only for an ally whose seat's faction is neither side), so a staff marshal's war targets are his
seat's faction's, not his own (one reading, three readers); a **won field** still licenses the seizure it always did (CP-T09-04 (b) applies
only without a fight); a war with **no committers
left** is over. R-CHOICE, for a player seated as a duke, intent "keep my followers": grant land (costs a hold, so a scene action) · pay upkeep
(costs stores) · do nothing (a defection then emits `commitment.ended`, public — silence does not beat refusal here). Intent "take a town":
march (risks bodies) · move members in until they outnumber, then seize (costs legs, risks nothing) — the second is cheaper but slower and
visible; no strict dominance found, an **upper bound** (NERS skill §6.2). R depends on the act economy (budget 5 buys 7 acts, `T09 §2.6`): each chain
here costs 2-4 acts, so it is affordable per season, and that dependency is stated, not scored around.

**S.** S-UP passes on its shape: a discontented member's petition is a real object on a dated docket, carried by him at a scene's cost and
dropped by a convener who pays (SC proceedings). S-DOWN passes: `war.declared` and a defection's `commitment.ended` are published by the
chronicle and picked up by each person's own ledger (while the chronicle stands: its deletion is scheduled with the `<rung kind>`
channel, `es/epistemic.py:675-684`). Re-run on CP-T09-05 after its bound was dropped: the occasion is the giver's own question about a man
sworn to him, and the receiver is whomever the giver picks among the persons he knows (`VT:585`) — nothing is routed to a recipient by
name, so it passes, and the cost of passing is the land-leak risk its stopping rule watches. Vertical: a duel's wound (PC) → a witness's
opinion (persons) → a declaration (FA) → a march (MB) → a hold (GV) → the ending row — every handoff is an existing carrier (claim, Tenure,
field). Diagonal: the same chain crosses families. Lateral/horizontal: covenant between factions; upkeep (EC), confer (GV). **Pauses
correctly:** a war adds no clock and ticks nothing; a march still declares at RESOLVE and fights at ENCOUNTER (IN-46's deferral is REM-31's).
**Consistent methodology:** every opinion gate reads one owner and one indifference point (`opinion_of`, 0, named once); every occupation reads
one count (`mustered`). Kept at MEDIUM: CP-T09-09 reads `legitimacy` (of a holder) where CP-T09-01 reads `opinion_of` (of a faction) — two
referents of the same `regard` owner, not two ladders for one quantity. **Shape and tree, separately:** the shape passes; the tree scores
zero until REM-21 lands, because every occasion term needs its registry.

**§8 run on this file's own discipline** ("every effect traces to a person's act; no threshold produces an outcome"). Hits: the gates in
CP-T09-01 (opinion vs 0), CP-T09-04 (plurality) and CP-T09-09 (legitimacy below 0). Classified: CP-T09-04 passes by tracing (the plurality is
a licence on a person's act, a precondition like every typed cell); the other two are one family, a threshold that produces an **occasion**,
never an outcome — borderline, licensed narrowly by IN-70's own gate (`WQ:2127-2128`, `[ASSUMPTION; medium; Jordan to correct]`) and by
naming the indifference point once so the family cannot grow a second constant.

**E, scored last, as a ratio.** E-OVERHEAD, counted: rows +3 (`declare`, `recruit`, `conspire`), 1 rebuilt (`dispatch`); stamper bodies
+7 and one filter on T02's stamper, on one existing registry; Queries +1 (`side_in`), one edited (`at_war`, S2); roster keys +1
(`seizure_target_kinds`) and one cell (`terms_sourced.release`); data rows 1 (`offices.yaml`); edits at five existing sites
(`occupying_faction`, `_seize_rung`, `_eff_raze`'s explicit decline, `sides_of`, `may_muster`). Stores, gauges, fixtures,
guards, clocks: **0**. Folded rather than added: alliance and peace (into `covenant` + `commit`/`release`), the plot reader (into
ambitions), the envoy (into `dispatch` + `give`), petitioning the head (into REM-24). Against N and R — nine N-lines, six of the ten genre
rows moved from ABSENT or PARTLY toward AFFORDED — the ratio is high. E-LEGIBILITY: the outcomes a player must intuit are short sentences —
"a wounding makes a war", "whoever has more people there can take it, unless he won it in the field", "land goes to my men" — and the one opaque term is `opinion_of`'s
three-term sum, whose display is REM-30's. Watchlist: the content roster cut (HIGH: nothing in computed play could have produced a content);
the ally-in-`mustered` cut (MEDIUM: a joint army may be wanted later); the `annex` rule cut (MEDIUM: kept as CP-T09-06's revert).

**Self-audit (§9).** Run: the N attack per row, disqualifier 4 on two items, the §8 enumeration. Residual: the R verdicts are provisional on
the play surface (REM-30) and on the act economy; the tree verdict is zero until REM-21 lands.

## §4 One season, after

Seed 0, `build_realm(0)`, with every item and its dependencies built. Season 0 is as measured today; season 1 is **illustrative** — the
code cannot yet produce it, and no number below season 0's is a reading.

**Season 0 (measured, `T09 §0a`, `[MEASURED-HEAD]`).** The King (p_npc_020) dies as the subject of the Queen's (p_npc_032) `accept`; the
Duchess of Hafenmark (p_npc_050) dies to a Crown member's (p_npc_083) `fight`. Tick 1: provinces Varfell 4 / Church 1; 11 of 16 territories
uncontrolled; the Queen still holds the realm seat `off_npc_032` (`issue`, `confer`, `dispatch` among its acts).

**Season 1 (illustrative).**
1. *The land is contested (CP-T09-04).* The Queen's questions carry the uncontrolled royal territories her seat reaches where Crown members
   stand (five lived at `set_s_001` at build, `T09 §3.1`). She issues herself a warrant and seizes one; a territory where Varfell's people
   outnumber the Crown's refuses her. No ducal seat can contest her for the dead Duchess's land: a duchy seat's purview stops at its own
   duchy (`es/state/gate.py:353`), so only the realm seat reaches across.
2. *The Crown's duchy is refilled (CP-T09-06).* `off_duke_valorsmark`, the dead King's second seat, is in her `vacancies`; she confers it
   on a Crown man she favours. Hafenmark's ducal seat stays empty: it is not hers to fill.
3. *A grievance becomes a war (CP-T09-02).* The Duchess's killing raises nothing — a dead victim's claim is never asked about (H-209). But in
   a later round a Crown man wounds a Hafenmark man in a duel; Hafenmark members who saw it hold the `seen.who` pairing on `body.changed`;
   IN-70 turns them toward the Crown's members, and a Hafenmark marshal with a `dispatch` grant declares on `fac_crown`. `war.declared`
   reaches every living ledger through the chronicle; Hafenmark's members rally to W, and some Crown members commit to it as defenders.
4. *The war finds targets.* Hafenmark's seats are offered every Crown-held settlement their purview reaches — which, after step 1, includes
   the territory the Queen has just taken. The Crown's seats find almost no Hafenmark-held town: the Duchess's land died with her. The war is
   lopsided because of the season-0 deaths, not because anyone wrote it so.
5. *The Queen seeks an ally (CP-T09-03, -08).* She covenants W to Varfell's duke, gives the instrument to an obligee of her seat and
   dispatches him to Varfell (the MUSTER basis admits it once CP-T09-07 (b)'s `oblige` clause is built); he delivers it; the duke commits to W and now sees Hafenmark-held towns as targets — or does not, because his own opinion of the
   Crown is low after watching her seize the dead King's land.
6. *Unwatched, at the same time.* A Crown member who saw the Queen kill the King reads his faction below indifference and leaves it, taking
   any land he holds (CP-T09-01); a Church seat-holder, untouched by the war, recruits him into service (CP-T09-07). The heir claims the
   throne by IN-61's `succeed`, and the Löwenritter Grand Master's oath to `off_king` (`es/offices.yaml:191`) now serves him and marches in
   his army (CP-T09-07 (b)).
7. *What the season reports.* One live WAR Proposition, two or three provinces where there were two, a refilled Crown duchy, and `endings` still
   `[]` — but now because nobody holds every territory, not because nobody can.

What the player at the Queen's seat chose: which land to take, whom to appoint, whom to court, whom to send. What the world chose without
her: a war on her, a defection from her, and a rival throne.

## §5 Order and dependencies

**Within the proposal.** CP-T09-06 (data, no dependency) → CP-T09-04 (needs REM-21) → CP-T09-01 (needs REM-21, REM-23 and T02's CP-T02-05;
its two measure-first readings) → CP-T09-05 (land moves; its reward arm waits on IN-08's `deed:rung.ceded` cell) → CP-T09-02 (needs REM-27's
Rung class and 04's seizable targets; wars over killings wait on H-209) → CP-T09-03 (needs 02's W and term (c)) → CP-T09-07 (its muster half
any time after REM-27; `recruit` after the `roll.py::obstacle` terms) → CP-T09-08 (**needs 07 (b)'s `oblige` clause** and REM-28's
`dispatch` reading; serves 03 at a distance) → CP-T09-09 (after the obstacle terms and its measure-first reading). v9 IN-61 is independent
and on G7's path. Collisions: `occupying_faction` (04) is shared with `raze`, whose explicit decline lands in the same commit; `sides.py`
(07) is also edited by T04's CP-T04-01 and CP-T04-04 — merge order to be set by the batch; CP-T09-04 (b) leaves the won-field licence T04
relies on untouched (its revert would collide); `verb_table.yaml` (02, 07, 08, 09) collides with B-T's IN-52 on the `march` row only through
REM-27, which already declares it.

**What it needs from other subsystems** (the interface, as expected — not waited on):
- **T02 (season, persons choosing):** CP-T02-05 (`oughts_named`, which CP-T09-01 filters and `declare` forms on); REM-21's `STAMPERS`
  registry with the `Proposition`, `Person` and `Rung` classes; REM-23 (`commit` on Proposition); IN-08's cells for `declare`, `recruit`,
  `conspire` and rebuilt `dispatch`, and a `deed:rung.ceded` cell pair (CP-T09-05); the indifference point of `opinion_of` named once in
  `WQ`. CP-T02-01 owns H-230's arm 2, on IN-61's path.
- **T05 (social contest):** obstacle terms read from the counterparty's ties, `opinion_of` and regard, added at the single owner
  `modules/social_contest/roll.py::obstacle` (T05's file `:389-390`), and a `contests:` prize whose Won band opens the counterparty's edge —
  for `recruit` and `conspire`; REM-24 (`petition` on Person); collective decisions stay SC's arrangements (J-4 / H-161).
- **T01 (resolution):** CP-T01-06's derived obstacle ceiling (H-213); the T09 falsifiers for contested acts run on that arm (rulings R2).
- **T04 (mass battle):** none demanded (rulings R10); this file owns its `sides_of` and `may_muster` edits and merges with CP-T04-01 and
  CP-T04-04 on `es/loop/sides.py`.
- **T08 (settlements, governance, economy):** `seize`, the self-warrant `issue`, `give` + Rung, `confer`/`vacancies` as built; **`raze`'s
  occupation licence** (GV's act, moved by CP-T09-04); **CP-T08-08** (the upkeep payment gets a question), on which G3's retinues and
  CP-T09-05's oath bond depend; tax owed up, yield by governor and income by share stay T08's. Flagged: T08 (`:58`) and T10 (`:82`) route
  or decline moving another's man; CP-T09-08 owns `dispatch` (FA host) and reconciles there.
- **T06 (information):** the chronicle's kind filter keeps `binding_decision` kinds realm-public (`war.declared`, `commitment.ended`) — its
  deletion is scheduled with the `<rung kind>` channel (`es/epistemic.py:675-684`), one of `ED-IN-0298`'s options;
  `surveil`/`interview` discover plots.
- **T10 (world, travel, NPC life):** `_relocate`'s leg for a dispatched man; kin and marriage stay NP's (closed cast, ED-WR-0011, ruled
  "for now").
- **T03 (personal combat):** a wound's `seen.who` pairing is the grievance's source; **H-209**, which T03, T05 and T10 also name, decides
  when a killing can be one; the coup's execution is a `fight`.

**What it gives them.** T04: computed marches on settlements beyond the ledger-named ones, and retainer armies (cohorts on the guards arm).
T08: a taker for unheld land (`uncontrolled` gets its caller), refilled duchies, fiefs. T05: petitions from discontented members and
denunciations from refused plots. T02: occasions through which faction state reaches a choice. IN-27: a reachable victory row.

## §6 Jordan asks, and the rulings the items touch

**A1 (survives the five steps) — who may declare war?** (`FA §3.9` Q3, carried, not new.)
1. Superseded? No later ruling. 2. Irrelevant? No. 3. Design document? FA-01 says a faction's act is a person's act through a seat and seats
   the heads (`_part7:121`), but does not restrict war to them. 4. Precedent? `march` and `raze` gate on `remit:dispatch` — but under
   `remit_default` that is 25 of 32 seats (`T09 §1`). 5. Architecture? Both are buildable: option one is the row as written; option two is an
   effect-side decline reading the creed subject, the head `opinion_of` already reads (`WQ:2099-2100`). The ask is live only because
   CP-T09-02 adopts S2's `at_war` edit; without it an `own` `utter` plus a `commit` makes a war any person can start, and A1 is moot.
- **Option one — any `dispatch` seat:** marshals and spymasters start wars; wars are frequent and local.
- **Option two — the creed subject of the declarer's faction only:** rulers start wars; wars are rare, and a faction whose head is dead
  cannot declare at all (the King dies in season 0 in every seed). **Reframed, said so:** verbs-15's option two is "the faction's head
  seat only", reading `faction_q.head` (`FA §3.9` Q3), which is always `None` (`FQ:116-147`); this file substitutes the creed subject,
  the head `opinion_of` reads, because the verbs proposal's reading is unbuildable as written.
- **Default if unanswered:** option one is built, option two is its revert; J-8 (whether `dispatch` is a remit act) is already Jordan's and
  moves this row with it.

**Not raised (one-line five-step answers).**
- Does a treaty bind the signer or the seat (`FA §3.9` Q1)? Step 5: a Seat carries no field (`04` §B.7) and edges are persons' (membership,
  war); a successor re-seals. The signer.
- `dispatch` or `assign` (Q2)? Step 1: D-V7 holds it; this file uses `dispatch` and changes no name.
- May a won contest open an edge the counterparty owns (Q4)? Step 4: `determine`'s disposal does (C-1, RULED A, `VT:1044`); `confer` opens
  the conferee's `hold`. Yes.
- Territories seizable, and the unheld place (H-166)? Step 3: GD-1 makes "control all 15 territories" the victory (`RY:2584-2585`), and the
  open assumption names its own revert (`EI:961-963`); taken (CP-T09-04).
- A basis for the Crown's ducal seat? Step 5: IN-61's own LIMIT keeps `off_duke_valorsmark` out of the `successions` registry
  (`_part5:159`), so without a basis it is empty for good; `appointed` keeps it inside the Crown, tagged [ASSUMPTION]. Hafenmark's seat
  is not given one: its row says the Crown cannot reach it (`offices.yaml:219`), and `elected` waits on the unruled act (ED-IN-0256 (2)).
- Tribute, truce, dated treaty terms, a pact chain: step 3 / step 5 and rulings R1 (GP-5b).
- A faction vote, expulsion: step 1, J-4 / H-161 hold the vote (T05); D-5 (GP-12).
- An opinion gate on mustering: T-b (GP-2b).
- A public reputation: T-a / AX-2 (GP-14).
- A rank ladder, founding, schism: step 3 / step 5 (GP-13).
- New ending rows: step 3, GD-1 and IN-27 (GP-11b).
- The FA-01 trade-demand clause: held on `ED-IN-0298` (needs_jordan, the border perception channel); nothing here touches or duplicates it.
- JQ-1…JQ-6: referenced only — JQ-4 (weight → troop) prices CP-T09-07's cohort armies on the guards arm.

**Rulings the items touch.** RS-27/RS-29 (the heir is a title; CP-T09-06 leaves the throne to IN-61); ED-IN-0256 (2) (the three conferral
bases; CP-T09-06 authors `appointed` within them); C-1 RULED A and D-5 (binding by reception; no second-person closer; CP-T09-03, -07,
-09); #453 exit (vii) (a won field licenses the seizure; kept by CP-T09-04 (b)); the `dispatch` row's `ruled` grade and its writes_note
*"their own choose decides"* (`VT:422-423`), which CP-T09-08 rebuilds — the agent still decides what he does at the post, but his
presence is moved; the 2026-07-13 province ruling (unchanged); direction 8 (no refusal reader; CP-T09-02); 04 F.18 (upkeep is a verb;
unchanged); T-a, T-b, T-c, A-29, A-31, A-37 (obeyed throughout); J-8 and D-V7 (moved with, not decided); rulings sheet R1, R2, R4, R9,
R10 (applied).

## §7 Risks, and what this deliberately does not do

**Risks.**
- **Degenerate inputs.** The occasions in CP-T09-01, -02 and -09 fire only where `opinion_of` or `legitimacy` reads below 0. IN-58 found
  stance reaches formation only under `stance_polarity: declared` (`_part5:138`); B-V's prefect read no negative `legitimacy` at three
  placements (`_part7:122`). The join gate has the opposite risk: it can pass at tick 0 on pursuit fit alone. If the measure-first
  readings are null (or, for the join, near-universal), those items stop before they are built, and G1, G2, G4 and G9 stay where they are —
  said now, not discovered later. No killing starts a war until H-209 is answered. The polarity is ED-IN-0296's ask-then, not this file's.
- **Formation floods and the scene tax.** Every term widens a shared class; the stopping rules are the defence, measured at `aperture 1 s`.
  The chooser sees verb identity, not consequence (overview §6 #1): a duke can give away land, to anyone he knows, without seeing his
  budget fall. CP-T09-05's stopping rule is the whole of the protection.
- **Purview across factions.** A won `recruit` of a seat-holder widens the recruiter's purview over that man's ground (IN-40), which
  CP-T09-02 (c) and CP-T09-04 (d) then read: wars and seizures can reach across factions through one oath. Counted in their readings.
- **Map churn.** Opinion-driven defection with land (01) plus plurality seizure (04) can make provinces flicker season to season; the
  ruled province has no hysteresis (GP-6b). That is the design's answer, and it may read as noise; the realm readings will show it.
- **Hash movers.** Every item moves the seeded content hash; CP-T09-04 also re-records `test_march.py:918-930`'s arm and moves `raze`;
  CP-T09-02's `at_war` edit re-records `es/tests/test_faction_q.py:220-260`. Goldens
  re-pinned by these items are re-pins of intended change, and each commit must say so (`CLAUDE.md` §7).
- **Paper until REM-21.** Eight of nine items need the stamper registry, which is itself a held proposal.
- **The chronicle may go.** `war.declared` and a defection's `commitment.ended` are public only through the chronicle kind filter
  (live, `es/epistemic.py:685-686`), whose deletion is scheduled with the `<rung kind>` channel (`:675-684`); if it goes with no
  replacement, wars are declared to no one absent.
- `[UNVERIFIED]`: how `issue` forms a self-warrant on a Rung referent in computed play (no computed warrant has named a settlement,
  `EI:974-975`); which `field.won` Event field names the field's rung (CP-T09-04 (b)); that new verb names pass
  `architecture/VOCABULARY.md`.

**What this does not do.** It builds no faction stat, treasury, meter, track, timer or director (T-a, T-b, T-c, A-37); it does not make a
faction act; it does not settle who may declare war (A1), the stance polarity (ED-IN-0296), the border channel (ED-IN-0298), the weight →
troop value (JQ-4) or J-8; it does not build succession (IN-61), faction emergence (IN-30's other half), tribute, truce, marriage, hostages,
votes, a public reputation or new endings; it designs no screen. G8's agent returns no report by himself, and G9's plots are visible to
anyone present — both stated residues, not gaps this file closes.
