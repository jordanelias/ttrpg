# A3: what a faction is, what a settlement is (Q4, Q5)

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

Appendix A3 of the suite, an analyst report copied from the session's `analysis/` into the suite at 07:10:35Z. Source: the session's own record of the analysis file written at 06:14:37Z and patched in place (14,115 bytes), recovered 2026-10-30 from the 2026-10-28 transcript (third pass). Edit-tool and heredoc changes found in the transcript were replayed in time order and the replayed size matches the size the session printed with `ls -la`. Text otherwise unchanged. Analyst reports are subagent output: figures in them are the analyst's, not verified here, and the suite's three-lens review (parts 07a to 07d, `critic_lens3.md`) found errors in some.

---

HEAD `be24c71`, measured on `build_realm(0)`. `WQ`/`FQ` = `engine/season/queries/{world_q,faction_q}.py`; `CR` = `…/state/carriers.py`; `POP` = `…/harness/populated.py`; `RO` = `…/rosters.yaml`; `GEO` = `systems/settlements/valoria_geography_v30.yaml`.

## Verdicts
- **Q4. Is a faction a record with stats? No.** A faction is a creed `Proposition` plus the live `commit` Tenures to it. Everything else about it (members, leaders, land, strength, wealth, war) is a query over its members' Tenures. The template needs no stored faction field, and it must not gain one.
- **Q5. Is a settlement an entity with stats? No.** A settlement is a `Rung` of kind `settlement` under a territory, given a type by its geography row. Its "stats" are queries over its own subtree (Sites, stores, its cohort) and over the seats whose purview reaches it. The minimum viable settlement needs one data change (seed the cohort's motives) and three queries.
- **4-faction canon vs the cast.** The old four (Crown, Church, Hafenmark, Varfell) are the four factions holding land at world build. In the engine that is a query (holdings non-empty), not a class. The cast is 8 canon factions, plus Altonia (off by default) and the test faction `faction x`.

## Q4. FACTION

**VERDICT.** The template is a view: `Faction(proposition, members, holdings, seats, head)` (`FQ:84-96`), "NEVER a member of `World` ... `Act.actor` ... or a `hold` subject" (`FQ:86-90`). A person holding its office acts.

**WHAT EXISTS (BUILT, measured).**
- **Creed.** An `OUGHT` whose subject is the authored leader, with value = the faction and scope = its role template (`POP:1079-1091`). A faction with no leader keeps `HOLDS` (Guilds, Schoenland).
- **Members.** Membership is `commit`, "THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE" (`WQ:1548-1559`). Leaders are the members who also hold a seat (`WQ:1562`).
- **Measured (members/held rungs/seats):** Crown 11/6/11, Church 7/1/7, Hafenmark 4/4/4, Varfell 5/4/4, Löwenritter 4/0/3, Restoration 4/0/1, Guilds 4/0/2, Schoenland 1/0/0. Every held rung is a territory; `head` is `None` for all (no writer of `Tenure.degree`, `FQ:116-147`).
- **Authored inputs.** The roster comes from `names_index` (`RO:1561`). Role templates cover 6 of 9 factions (`RO:1598`). Leaders cover 6, plus Altonia (`RO:1640`). Sub-organisations are `office_bodies` (`RO:1714`). `goals.yaml` has 38 OUGHT goals, each with a pursuits vector: 20 owned by a faction, 18 by a body or seat.
- **Queries.** `footprint` `WQ:1602`, `mustered` `:1653`, `holder_faction_of` `:1885`, `superiors`/`subordinates` `FQ:180-207`, `opinion_of` `WQ:2294`, per-person `legitimacy` (`engine/season/queries/person_q.py:452`; R7: no single faction number), `at_war` `FQ:219` (no producer in play).
- **[RETIRED]** `fac.*` stats (`references/descriptor_registry.yaml:76-78`, 29b); the canon 6-stat block, priority tree and AI posture; `stats_1_7_scale.md` (not in `git ls-files`). `registers/supersession_register.yaml:22-28` still calls `fac.legitimacy` a base: stale (D1).

**WHAT IS MISSING (ranked).**
1. No producer for war: `declare` (CP-T09-02).
2. No computed route to join a faction (CP-T09-01) and no `recruit` (CP-T09-07).
3. `head` is empty. The leader is authored once, at build.
4. No `conspire` (CP-T09-09).
5. Runtime founding of a faction is parked (FA-G39): see E1.

**TEMPLATE** (E = exists, D = designed, N = new). Every stat is a query over the five-field view; nothing is stored on the faction.

| tier | field | st | carrier / query |
|---|---|---|---|
| identity | name, token | E | `names_index` token_class faction |
| | creed | E | `Proposition fac_<slug>` (OUGHT, subject = leader) |
| | role template (expected pursuits) | E | `RO:1598` by_faction |
| | founding leader | E | `RO:1640` (build-time referent) |
| | foreign | E | the territory is a root rung with no `contain` into the realm (`POP:836-848`) |
| state | members, leaders | E | `members`, `leaders` |
| | standing ("legitimacy") | E | `person_q.legitimacy(p, holder)` per viewer; never one number |
| | cohesion ("stability") | N | share of members with `opinion_of(m, own) > 0` |
| | strength ("military") | E | `mustered` / `density` per rung |
| | wealth | N | Σ `stores` on members' seat rungs (`decision/options.py:711` `treasury_of`) |
| | knowledge ("intel") | D | ST F-2 holdings ledger; read the members' claims |
| relations | war | E/D | `at_war` (built); `declare` (D) |
| | treaty, alliance | D | `covenant` (tests-only); `side_in` (CP-T09-03) |
| | service | E | `superiors`, `subordinates`, `establishment_of` `WQ:2090` |
| holdings | land, seats | E | `holdings`, `seats`; `sovereign_fraction`, `provinces_of` |
| | sub-organisations | E | `Office.body` → `office_bodies` |
| behaviour | goals | E | `goals.yaml` OUGHTs that members commit to |
| | decision | E | each member's own chooser. The faction AI is [RETIRED] |
| authored colour | mission text, culture, beliefs, parallel, foils | D | canon prose, display only |
| | headquarters | E | `venues.yaml` `seats` / buildings' `serves` |

**GENERATED vs AUTHORED.** Factions are authored, not generated: a closed cast (ED-WR-0011), with names given by `systems/world/` (`RO:1561` note). Of the FACTION stack (`.designs/systems/settlements/reference/generation_sourcebook_v1.md:40-47`):
- **Survive:** F1 substrate posture (as members' `conviction`), F2 role template, F4 holdings (as seeded `hold`s), F5 sub-org ladder (as `office_bodies` + offices), F7 political axes (as goals and pursuits).
- **Die:** F3 stat block [RETIRED] and F8 directive tree [RETIRED].
- **Parked:** F6 emergence path (E1).

**ACTION MENU.** A faction has none. The holder of a faction seat acts through its remit (`verb_table.yaml` eligibility, grouped this session):

| remit | built verbs |
|---|---|
| issue | `issue`, `covenant`*, `requisition`, `seize`*, `transfer` |
| confer / revoke | `confer`, `establish` / `revoke` |
| determine | `determine`, `open_case`, `pardon` |
| dispatch | `dispatch` (writes nothing), `march`*, `arrest`, `raze` |
| convene | `convene` |

\* runs in tests only.

- **Missing:** `declare`, `recruit`, `conspire`, `levy` (troops), and `succeed`'s effect (the row exists, with no effect).
- **Canon "unique actions" become seat verbs** (D4): Royal Decree → King's `issue`; Excommunication → Church `determine` + ban; Economic Leverage → `transfer`; Private Collection → `surveil`; Martial Law → `arrest`/`march`.

## Q5. SETTLEMENT

**VERDICT.** A settlement is a `Rung` (`CR:1050-1106`; fields at `:1083`) that "owns NO social aggregate ... EVERY ONE IS A QUERY" (`:1097`): geography row + type template + queries. No `class Settlement`, and none should be added.

**WHAT EXISTS (BUILT, measured).**
- **Map.** 37 settlement rungs under 17 territories. Each settlement has 1 to 3 quarters (`community` rungs) and buildings (`hearth` rungs), chosen by `type` from `venues.yaml` (`POP:849-853`, `:882-899`). Seven types are in use: Town 15, Village 14, Seat 2, Fortress 2, City 2, Fortress-City 1, Cathedral-City 1.
- **People.** One cohort per settlement (weight 2). **Its `pursuits`, `stance` and `conviction` are empty and it holds no `commit`** (measured): the people have no politics.
- **Places, goods, queries.** Sites with `condition`; `stores` = larder; MATTER in `modules/settlements/`; `population` `WQ:1422`, `capacity` `:1492`, `fortification_of` `:1673`, `governors_of` `:869`.
- **Who governs.** 36 of 37 settlements are reached by 4-14 governors, all from territory, duchy or realm seats. **No seat sits at a settlement rung** (32 offices built). Title `Mayor: settlement` is ruled (`engine/season/offices.yaml:171`, H-90); no Mayor seat exists.
- **Unread data.** `GEO` rows carry `name`, `controller`, `coords`, `description`, `stats: [Prosperity, Defense, Order]` (`GEO:244`); the engine reads only `territory` and `type`, and never `settlement_adjacency`.
- **Orphaned.** `set.*` (`references/descriptor_registry.yaml:84-90`); only the loader `engine/substrate/descriptors.py:56` touches it. `governance_modes` was deleted as unread (`RO:86`).

**WHAT IS MISSING (ranked).**
1. Motives for the people. Without them, allegiance and unrest have no input.
2. Mood: `unrest(w,S)` (CP-T08-06, D).
3. A standing levy: the `tax` edict (CP-T08-07, D).
4. A local seat (E2).
5. Ground endowment: every place gets one harbour and one seam (CP-T08-02). 6. `work` cannot run on dwellings or garrisons (empty floors).

**TEMPLATE**

| tier | field | st | carrier / query |
|---|---|---|---|
| identity | id, kind, parent territory | E | `Rung` + `contain` |
| | name, type, coords, description | E (data) | `GEO` row; the cohort's name carries the place name |
| | type → quarters, buildings | E | `venues.yaml` |
| state | population, capacity, larder, yield | E | `population`, `capacity`, `stores`, `yield` |
| | Defence | E | `fortification_of` |
| | Prosperity | N | query: yield and stores per head over the subtree |
| | Order / mood | D | `unrest(w,S)`, read from the cohort's own claims |
| | standing of the holder | N | mean of `person_q.legitimacy(resident, holder)` over cohorts that `reside` here |
| | piety | N (data) | the cohort's `conviction` (an existing field), seeded |
| relations | holder faction | E | `holder_faction_of` |
| | adjacency | E (data, unread) | `GEO settlement_adjacency` |
| holdings, offices | governors | E | `governors_of` |
| | local seat (Mayor) | D (title ruled) | `offices.yaml` row (E2) |
| | facilities | E | Sites. Facility tiers and `fort_level` are [RETIRED] as stats |
| | treasury | E | `stores` of the seat's rung |
| behaviour | eat, produce, wear | E | MATTER |
| | standing edicts | D | `tax`, `ration` |
| authored colour | cast, deck, situations | D | Goldenfurt (S-006): 6+3 dossiers, 28 cards (`.designs/…/goldenfurt_slice/`) |

**GENERATED vs AUTHORED.** `build_realm` already is the generator: geography row + `venues` template → rungs, Sites and a cohort, deterministically. Extend it; do not build the VSG. Of the VSG stack (`.designs/systems/settlements/reference/settlement_generator_v1.md:53-67`):

- **Built:** P1 location, P2 starting faction, P4 type, P7 infrastructure (buildings + Sites).
- **Seeds on existing fields:** P3 size, P5 piety → cohort `conviction`, P8 economy → Site endowment, P12 temperament → cohort `pursuits`, `GEO` stats (D2).
- **Authored / reframed / gate:** P13 cast (closed); P14 deck → occasions (D7); P15 → tests.
- **Die:** P6 Altonian scalar, P9 caste scalar, P10 governance type (D3), P11 allegiance (→ query).

**ACTION MENU** (holder of a seat that reaches S / person present at S)

| canon governance verb | built equivalent | status |
|---|---|---|
| Develop, Fortify | `work`, `build`, `restore` on a Site | built; inert on dwelling and garrison (no floors) |
| Hold Court | `convene` → `open_case` → `determine` | built |
| Sponsor | `transfer` from the treasury | built |
| Treat | `covenant` | tests-only |
| Levy (goods / men) | `requisition` / `levy` | built / missing (MB) |
| Investigate | `examine`, `interview`, `surveil` | built |
| Keep Order | `patrol` | parked; needs `unrest` |
| Tax, Ration, Proclaim, Craft | edict rows; `craft` | missing (lexicon `proposals/2026-10-16-verbs/…-03:139`); `ration` is blocked on D-V13 |

Residents: `migrate`, `move`, `petition`, `found`, `sabotage`.

## Connections and the minimum viable set
- **Edges.** person `commit`→creed (faction) · `hold`→seat (office; purview descends to settlements) · `hold`→territory (land; `holder_faction_of` walks up) · `oblige`→seat (officers = `establishment_of`) · cohort `reside`→settlement (the people) · `Office.body`→sub-organisation · `serves` places the cast in faction buildings.
- **4-faction reconciliation.** The landed four hold 15 territories: Crown 6, Hafenmark 4, Varfell 4, Church 1. The rest are landless at the start (Löwenritter, Restoration, Guilds) or foreign (Schoenland, Altonia). No player-faction flag.
- **MVP faction.** The 5-field view, role template, leader, goals and `at_war`. Add `cohesion` and `wealth` (2 queries). No field.
- **MVP settlement.**
  - Data: seed each cohort's `pursuits` / `conviction` / `stance` (existing fields).
  - Build seeds from the `GEO` triplet: Defense → garrison condition, Prosperity → starting stores, Order → stance toward the holder.
  - Add `prosperity` and `standing` (new) and `unrest` (designed).

## Decisions taken
- **D1. Close the stale supersession row.** `supersession_register` says `fac.legitimacy` is live. It is superseded by 29b and by R7.
- **D2. Retire `set.*`.** It is orphaned; follow the 29b precedent. The `GEO` stats become build seeds only.
- **D3. Governance mode stays deleted.** It becomes a query over the conferral and body of the seats in `governors_of` (H-100: provenance = `Office.conferral`).
- **D4. No faction-named verbs.** That would be scripting drift.
- **D5. `declare` is gated on `remit:dispatch`.** This is `march`'s gate and CP A1's built default.
- **D6. The seven `venues` types are the type roster.** Port, Mine, Outpost and Cathedral die; Sites carry those functions.
- **D7. A deck card only deposits a claim or question to a named person**, whose verb writes the outcome; per-settlement authored "situations" (vacancy, debt, grievance) seed freestanding storylines.
- **D8. Guilds and Schoenland stay without a template.** The `RO:1598` sourcing rule decides it.

## Escalations
- **E1. Runtime founding of factions and settlements** (FA-G39 parked, Γ22 declined). Without it the cast is closed forever and the Restoration Movement cannot rise in play. Recommend: a faction is founded by `utter` OUGHT + `commit` (already a fold), with seats only through `establish`.
- **E2. A Mayor seat in each of the 37 settlements**, vacant at the start (each vacancy becomes a `confer` storyline), or none (towns are governed from their territory). Goldenfurt's whole premise needs the former. Recommend: vacant seats, after the confer load is measured.
