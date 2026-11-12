# HOUSE STANCES AND CAST VALUES — Jordan's A-87 to A-90 as opinion rows, regime cores and the 46 principals' values

## Status: REFERENCE (an audit and a plan; resolves nothing at runtime, CLAUDE.md §0.05)
## Read at: aa9a4fb (working tree)
## Lane: WR with CHAR (31), completing lane 30's `30_WR_G` commit 2

Proposals carried (each with its coding instructions):

| file | what it decides |
|---|---|
| `proposals/31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` | the five roster rows and their cells, the six regime cores, the link table, the cast rule and the 46-row table, the faction `creed:` signs |
| `proposals/31_WR_B_the_revival_gathers.md` | A-89's momentum: a stand moves by a draw when a man takes in a deed by one of a creed; cohorts seeded from their house's core |
| `proposals/31_WR_C_what_the_stances_feed.md` | the deed race, the vote, the strands, the chronicle and the player's view |

## 0. Verdict

**The stances can be landed as data today and they do what Jordan asks of them in the static reading: on the built realm, with the 46 rows of `31_WR_A` applied in memory, the three houses order exactly as A-87 says on caste, royal order and government, the Church holds no stand on caste or parliament, and the six regime cores each find their people, where on the shipped values they find one wide tent and a church (36, 0, 0, 6, 0, 0).** Three things stand between that and a game in which regimes differ in play. (1) `30_WR_G` commit 1 as written does not build: its three `concerns:` keys make `conviction_of` refuse all 46 cast rows (P-31-5). (2) The rows discriminate only under `20_NARRATIVE_A`'s `stands` reading; under the shipped reading 1,032 of 1,035 pairs still read −1 (P-31-2). (3) Nothing moves a stand except the fixed crisis, so A-89's "momentum building" has no carrier until `31_WR_B`, and its leaners (the populace) hold no conviction at all. In play the difference is so far thin: two seasons hold nine and five tellings between cast members (P-31-7), which is the channel the credit term acts on.

`30_WR_G` commit 2's INCOMPLETE mark is removed: the values are authored, with 57 cells grounded in the registry, `goals.yaml` or canon, 106 marked assumption, and 67 left as no key because nothing bears on them. Four items go to Jordan (§11).

## 1. What exists, as coded

- **The scale and its readers.** `Person.conviction` is `{affiliation: 0..5}`; `person_q.conviction_stand` (`queries/person_q.py:456`) reads it signed about the midpoint, an absent key as 0 and a stored 0 as −1. `world_q.commensurate` (`:5317`) reads −1, 0, +1 from `_held` (`:5339`, above zero today) and `data/affiliations.py::INCOMPATIBILITY`. `loop/witness.py::_credit` (`:240`) multiplies a told claim's confidence by `1 + regime_gain × commensurate`.
- **The cast's values** are the `affiliations:` mapping of each row of `references/npc_registry.yaml`, read by `data/cast.py::conviction_of` (`:234`), which refuses a row holding no member of each concern (`:253-262`). `engine/season/npcs.yaml` is the case roster and holds none.
- **The caste estimate** is `person_q.heritage_regard` (`:468`): the mean, over the affiliations of the concern a believed heritage engages, of the observer's own stand, an absent key counted as 0 (`:478`, `:501-502`). `southern_einhir` engages concern `einhir`, whose one member is `einhir_restoration` (`references/descriptor_registry.yaml:214-228`, `:236-247`).
- **A faction's creed** is a Proposition subject-ed on its leader (`harness/populated.py:1419`); nine exist at `build_realm(0)`. It declares no pole (`20_NARRATIVE_D` proposes the `creed:` key).
- **Goals** carry the houses' programmes as data: `goal_restoration_caste_ended`, `goal_hafenmark_constitutional_order`, `goal_hafenmark_church_influence_suppressed`, `goal_jarl_council_confederacy`, `goal_lowenritter_throne_security`, `goal_church_suppress_restoration` (`engine/season/goals.yaml`). None carries an `axis:`.
- **A stand moves** in one place: `loop/resolve.py::_conviction_crisis` (`:703-727`), a fixed function.
- **Cohorts** hold no conviction (`engine/season/cohorts.yaml:106-107`). The realm is 46 principals and 37 cohorts.

## 2. Steelman

The strongest case for leaving `30_WR_G` commit 2 open was that lane's own: "a value read off a faction template or a heritage would be a guess". It held until A-87 to A-90: the cores are now Jordan's, and 57 cells have a ground in the person's own row. Attack tried: are the remaining 106 a guess dressed as a rule? They are assumptions, marked per cell, bounded to one step from a ruled core, and the alternative (no key) was taken wherever no core and no text bore on a cell (67). What survives: the house means are Jordan's; a single officer's cell is not, and is cheap to correct.

## 3. Findings

| id | severity | claim | evidence | falsifier run | fix |
|---|---|---|---|---|---|
| **F-31-01** | blocks | `30_WR_G` commit 1's `concerns:` keys (`caste`, `arms`, `crown`) make the realm unbuildable: every cast row is refused for holding no member of the new concern | `data/cast.py:253-262` | P-31-5: 46 of 46 shipped rows accepted; 46 of 46 refused once a concern `caste` exists | `31_WR_A` §1: no new concern; an absent key is "has not considered it" |
| **F-31-02** | gap | on the shipped values the houses cannot be told apart on any question A-87 names, and the six cores read 36 / 0 / 0 / 6 / 0 / 0 | P-31-1 (control: `n/a` on every new pole), P-31-6 | the treated arm: 18 / 6 / 5 / 12 / 9 / 10 | `31_WR_A` commit 2 |
| **F-31-03** | inconsistency | the shipped religion cells contradict A-89: mean stand on `solmund_orthodoxy` is −0.30 for Hafenmark ("devout"), −0.20 for Valorsmark ("pro"), −0.60 for Varfell ("neutral") | P-31-1, control arm | after 12 cells re-authored: +0.70, +0.16, −0.36 | `31_WR_A` §4 (`*` cells) |
| **F-31-04** | design | with ten axes `30_WR_B`'s exact creed-set bodies split the cast into 25 sets, the largest of five; the reading that was to show regimes shows fragments | P-31-3 (control: 6 sets, 20 persons in none) | n/a (a count) | `31_WR_A` commit 3: `core_standing` over the six core rows |
| **F-31-05** | design | the product form (`accord`) cannot see a core at the midpoint: naming by highest accord sends 21 persons to the Church's row and none to Varfell's or the Movement's | P-31-3b | the distance form, P-31-3c and P-31-6: Varfell's core is Varfell's five | `person_q.closeness` (a distance); `accord` stays the credit form |
| **F-31-06** | degrades narrative | the shared vow column of `affiliation_engagement` applies to every roster member, so an opinion on government would take a scar from every forgery seen and the fixed crisis would fold it into its `true` partner | `rosters.yaml:3706-3765`; `16_PESSIMIST_CHAR_A` §2 | not observed in this lane's runs (the five rewrites at seed 1 were religious poles, P-31-8); derived from the rule | `31_WR_A` §1 item 4: `vowed:` |
| **F-31-07** | gap | A-89's momentum has no carrier: the one mechanism that moves a stand is the fixed crisis, which rewrote five persons in two seasons at seed 1, each toward a creed he held at 1 or 2 | `loop/resolve.py:703-727`; P-31-8 | n/a | `31_WR_B` commit 1, after `16_PESSIMIST_CHAR_A` |
| **F-31-08** | gap | Varfell's five principals stand at 4 or 5 on the tradition pole on their own rows' text; the leaners A-89 describes are the populace, and a cohort holds no conviction | `references/npc_registry.yaml` (NPC-002, -052, -073, -074, -082); `cohorts.yaml:106-107` | n/a | `31_WR_B` commit 2 |
| **F-31-09** | degrades narrative | regimes differ in the reading and barely yet in play: the credit term fired on nine and five cast-to-cast tellings in two seasons | P-31-7 | treated against control at the same seeds: the signs move (seed 0: one 0 becomes −1; seed 1: four 0 become three 0, one −1, and the fifth +1) | `08_FI_02_rumour-that-travels.md` supplies the tellings; not this lane's |
| **F-31-10** | dependency | the new rows discriminate only at `held_reading: stands`: at the shipped reading the treated realm reads 1,032 / 0 / 3 | P-31-2 | `stands`: 357 / 247 / 431 | land after `20_NARRATIVE_A` commit 2 |
| **F-31-11** | hygiene | `30_WR_G` commit 2 names `engine/season/npcs.yaml` as the cast rows `conviction_of` reads | `data/cast.py:236`, `:45` | opened | corrected in `31_WR_A` commit 2 and the `Folded:` line |

## 4. The readings Jordan left open, and how each was settled

- **"correlate is restoration movement and Einhir Revival."** Reading used: *the anti-caste side goes with the Restoration Movement and the Einhir Revival.* **Grounded, not assumed**: the Movement's own goal row is to end the caste (`goals.yaml: goal_restoration_caste_ended`); both registry rows that name a caste goal name revival beside it and on the same side (NPC-032 "Einhir revival through Crown authority" with "Caste dismantlement through royal decree"; NPC-052 "Einhir cultural revival at any cost" with "Dismantle post-war caste order"); the one pro-caste house's head is canon's "Pure RM adversary" (`canon/03_canonical_timeline.md:143`); the caste is the relegation of the southern Einhir (`:96`). No row pairs revival with keeping the caste. What stays `[ASSUMPTION]`: that the sentence is a tendency (carried as two link rows, sign −1) and not a rule that every anti-caste man is a revivalist. The Church shows it is a tendency: against the Einhir and without a stand on caste.
- **The "Einhir Revival" is not a faction.** `names_index.yaml` has no such faction and no row belongs to one. In the registry it is a goal held across three factions. It is authored as a regime core with `of: null`, and on the treated realm its core is Varfell's five, the Movement's four and the Queen (P-31-6).
- **"Varfell unhappy royal order due to caste."** One row of `tables.opinion_links` (`caste_order → royal_order`, +1), read two ways: `link_fit` in the regime reading (Varfell +0.50, the Movement +0.60, Hafenmark 0.00, Valorsmark −0.16, the Queen −1.0; P-31-4) and a dice term in `31_WR_B`'s sway. Nothing fires. Limit stated in `31_WR_A` §3: the row does not lapse if the Crown ends the caste; the decree itself is then the evidence.
- **A-88 with A-90, "anti-Einhir" on which axis.** Both, as ruled. The Church's core holds `einhir_restoration` 0 and `einhir_folk` 0.5 and has no key on `caste_order`. Because `einhir_folk` joins the concern the caste estimate reads, the Church's regard for a person it believes southern Einhir stays the lowest in the realm (mean stand −0.80) with no opinion on the tiers; Valorsmark's rises from −0.45 to −0.13 (its sympathies, on the people pole); `heritage_roster.engages` is untouched. So the split A-88 names is in the data: hostile to the Einhir, indifferent to the order of birth.
- **"Neutral" against "does not care".** Neutral is a considered midpoint (2.5: members at 2 and 3). Does not care is no key.
- **Devout Hafenmark against its goal to suppress the Church's influence.** Not a contradiction: `solmund_orthodoxy` is the theology, the goal is about jurisdiction (canon's own parallel, `:143`). It leaves the Duchess nearer the Church's core (0.80) than her own (0.77), and her house's four in the Church's core of twelve.

## 5. The check that the realm's regimes now differ (seed 0, `PYTHONHASHSEED=0`; control: the shipped values)

| reading | control (shipped) | treated (`31_WR_A`'s table applied in memory) |
|---|---|---|
| mean stand, `caste_order`: Varfell / Valorsmark / Hafenmark | n/a (unheld) | −0.92 / −0.20 / +0.60 |
| `royal_order`: Varfell / Hafenmark / Valorsmark | n/a | −0.52 / 0.00 / +0.67 |
| `parliamentary_rule`: Varfell / Valorsmark / Hafenmark | n/a | −0.36 / −0.02 / +0.70 |
| `militarism`: Hafenmark / Valorsmark / Varfell | n/a | −0.50 / −0.24 / +0.60 |
| `solmund_orthodoxy`: Varfell / Valorsmark / Hafenmark / Church | −0.60 / −0.20 / −0.30 / +0.83 | −0.36 / +0.16 / +0.70 / +0.83 |
| `einhir_folk`: Church / Hafenmark / Valorsmark / Varfell / Movement | n/a | −0.83 / −0.60 / +0.20 / +0.92 / +1.00 |
| Church: persons with a key on caste, parliament | 0, 0 | 0, 0 (one cardinal holds `militarism`) |
| `commensurate`, 1,035 cast pairs, shipped reading (above zero) | 1,031 / 0 / 4 | 1,032 / 0 / 3 |
| the same at `stands` (emulated: value 3 or more) | 130 / 779 / 126 | 357 / 247 / 431 |
| mean `commensurate` at `stands`: Hafenmark–Varfell; Hafenmark–Church; Valorsmark–Varfell; Varfell–Movement; inside Valorsmark | 0.00; 0.00; −0.09; +1.00; −0.02 | −1.00; +0.71; −0.36; +0.50; +0.53 |
| mean `accord`: Hafenmark–Varfell; Hafenmark–Church | 0.00; +0.24 | −0.26; +0.39 |
| distinct exact creed sets; persons standing for nothing | 6; 20 | 25; 1 |
| cores at `closeness` 0.6 (Valorsmark, Hafenmark, Varfell, Church, Movement, Revival) | 36 / 0 / 0 / 6 / 0 / 0 | 18 / 6 / 5 / 12 / 9 / 10 |
| persons in 0 / 1 / 2 / 3 cores | not read | 10 / 17 / 14 / 5 |
| build hash | `600d8b271474` | `137ea5c9e053` (a build-hash mover, as declared) |

Read from all directions. Top-down: six cores, each with people. Bottom-up: the Parliamentary Clerk sits in Hafenmark's core (0.66) and outside his own house's; the Queen sits in the Revival's (0.87) and at 0.23 from her house. Laterally: the Guilds' four are on Hafenmark's fringe; the Löwenritter's four are on Varfell's fringe (arms) and three of them in Valorsmark's core (the Crown). Diagonally: Varfell's militarists and the Movement's reformist leader read −1 with each other inside one cause (the +0.50, not +1.00). What the check does **not** show: that any of this changes what happens over seasons (F-31-09).

## 6. Resolutions

| # | inconsistency, gap or unclear passage | decided | ladder step | carrier |
|---|---|---|---|---|
| R-31-01 | which side "correlate" means | the anti-caste side; a tendency, as link rows | 3 (the registry and `goals.yaml`) | `31_WR_A` §3 |
| R-31-02 | government form: one pole or two | two, with a `true` cell | 4 (the pair-3 precedent) | `31_WR_A` §1; §11 J-31-2 |
| R-31-03 | where the new members are filed | under no concern; `einhir_folk` under `einhir`, with the values | 5 (the build refuses otherwise) | `31_WR_A` §1 |
| R-31-04 | "neutral" and "does not care" | midpoint; no key | 4 (IN-63: an absent key is never considered) | `31_WR_A` §2 |
| R-31-05 | the words on the scale | one vocabulary for every axis | 5 (§0.06 S) | `31_WR_A` §2 |
| R-31-06 | whether the Church's hostility is a caste stance | no: it is two Einhir stands; the estimate by descent reads them | 1 (A-88, A-90) | `31_WR_A` §1, §2 |
| R-31-07 | Varfell's principals against "neutral leaning" | kept at their own rows' values: the vanguard; the populace is seeded at the core | 3 (their rows' text) | `31_WR_B` §6; §11 J-31-3 |
| R-31-08 | what a regime core is | data that seeds and names; membership a reading by distance; a person may be near several | 5 | `31_WR_A` commit 3 |
| R-31-09 | a strain invented for caste against the Einhir poles | none; the correlate is a link | 3 (A-87's word is "correlate") | `31_WR_A` §1 |
| R-31-10 | how a house's opinion moves | a draw at the deposit of a deed by one of a creed | 5, under A-24 and A-83 | `31_WR_B` |
| R-31-11 | the vow column and opinions | opinions are outside it | 5 | `31_WR_A` §1 item 4 |
| R-31-12 | the persons with no core and no text | no key | 1 (the standing rule: do not guess) | `31_WR_A` §4 R4 |

## 10. Interfaces

Consumes: `20_NARRATIVE_A` (`stands_for`), `20_NARRATIVE_D` (`creed:`), `30_WR_B` and `30_WR_G` (regimes, `accord`, `circle_of`), `16_PESSIMIST_CHAR_A` (`conviction.moved`). Emits to: the deed race and the ballot (one step row each), `U5d_FA` §4 (a block's lean), `U5d_SE` (the tiers are what `caste_order` is an opinion about), `30_WR_C` (`strand_fault`), `09_WR_B` and `30_GO_F` (phrases), CR-107 and `21_PROCEDURAL_B` (seeding from a core). Every edge is designed; none is executed.

## 11. Survivors for Jordan

**J-31-1. The Duchess's faith.** *(A, taken: A-89 read onto the head, and canon's own parallel.)* `solmund_orthodoxy` 4: devout in doctrine and set against the Church's jurisdiction. *(B)* It stays 2, as her row says ("faith privatised"): a sceptic at the head of a devout house. *As games:* under A she sits in the Church's own core and her quarrel with the Confessor is between believers; under B her house can come to doubt her and the Church can call her faithless.

**J-31-2. Is "mixed" a split.** *(A, taken.)* `parliamentary_rule × militarism` is `true`: a mixed house is one whose Marshal and whose Clerk discount each other's word. *(B)* The cell is `null`: mixed is moderate, and the two are opinions a man may hold together without strain. *As games:* under A the Crown's party has a fault line a rival can work; under B it is a centre.

**J-31-3. Where Varfell's momentum sits.** *(A, taken.)* The five principals keep 4 and 5 on the tradition pole; the populace starts at the core and is what gathers. *(B)* The principals are lowered to the core (3 and 4) and only the Duke and the Skald-Chief stand at 5: the jarls themselves are undecided. *As games:* under A the Revival is a valley catching up with its lords and needs cohort convictions to move at all; under B it is fought for in the Jarl Council and a jarl can be won back by the Church.

**J-31-4. The Movement and the Crown.** *(A, taken: its goal row, "communal sovereignty in its place".)* `royal_order` 1 for the Movement's four. *(B)* 3 or 4: the Movement is the Queen's ally and works through the Crown. *As games:* under A the Queen and the Movement share a cause and part on the Crown, so she is pulled apart and they are not; under B the Movement is a court party and Varfell is alone against the order.

## 12. Evidence log

All `PYTHONHASHSEED=0`; scripts and outputs under `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/HOUSES/` (`probe31.py`, `cores31.py`, `static.out`, `cores.out`, `runs.out`). The treated arm parses the cast table out of `proposals/31_WR_A_…md` and applies it to `build_realm(0)` in memory; `stands` is emulated by replacing `world_q._held` with "value 3 or more"; the three decided cells are patched into `data/affiliations.INCOMPATIBILITY` in process. No tracked file was written by a probe.

| id | what | seed, seasons | outcome |
|---|---|---|---|
| P-31-0 | parse of the table | n/a | 46 rows; 57 `g`, 106 `a`, 67 no key, 12 re-authored |
| P-31-1 | mean stand per house per axis, control and treated | 0, built | §5 rows 1 to 7 |
| P-31-2 | `commensurate` and `accord` over cast pairs, two readings, both arms | 0, built | §5 rows 8 to 11 |
| P-31-3 | exact creed sets; nearest core by accord (b) and by closeness (c) | 0, built | 6 → 25 sets; (b) Church 21, Revival 12, Hafenmark 8, Valorsmark 4, Varfell 0, Movement 0; (c) see P-31-6 |
| P-31-4 | `link_fit` means; the caste estimate over one pole and two | 0, built | §4 |
| P-31-5 | `conviction_of` on the shipped registry with a concern nobody holds | n/a | 46 accepted; 46 refused |
| P-31-6 | cores and fringes at 0.6 and 0.3 | 0, built | treated 18 / 6 / 5 / 12 / 9 / 10; control 36 / 0 / 0 / 6 / 0 / 0; own-house closeness min and mean: Valorsmark 0.23, 0.65; Hafenmark 0.71, 0.77; Varfell 0.63, 0.72; Church 0.60, 0.80; Movement 0.87, 0.97 |
| P-31-7 | two-season runs, arms C0 (shipped), C1 (shipped values at `stands`), T (treated at `stands`); `_credit` calls between cast members by sign −1 / 0 / +1 | 0, 2 | acts 1,529 / 1,529 / 1,531; C0 9 / 0 / 0; C1 1 / 1 / 7; T 2 / 0 / 7 |
| | | 1, 2 | acts 1,519 / 1,519 / 1,520; C0 4 / 1 / 0; C1 0 / 5 / 0; T 1 / 3 / 1 |
| P-31-8 | the same T run, persons whose conviction the loop rewrote | 1, 2 | five (NPC-005, -009, -031, -036, -083), each by the fixed crisis, on religious poles only. The first attempt at this arm stopped in `conviction_map` because the in-memory roster had not been extended; rerun with it extended |

Not run: any season with the proposed mechanisms (none is built); the strand readings; more than two seasons or two seeds (the machine was loaded; a season took about ten seconds). Citations carried from other lanes and not opened here: `world_q.py:3055-3062` (`30_WR_G`), the E-N figures of `20_NARRATIVE_A` (reproduced by P-31-2's control), `16_PESSIMIST_CHAR_A`'s 31 of 46.
