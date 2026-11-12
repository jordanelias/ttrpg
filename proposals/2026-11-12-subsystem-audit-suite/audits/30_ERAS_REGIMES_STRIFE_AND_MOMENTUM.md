# ERAS, REGIMES, STRIFE AND MOMENTUM — audit, design and plan

## Status: REFERENCE (an audit and a plan; resolves nothing at runtime, CLAUDE.md §0.05)
## Read at: 2600cb0 (working tree)
## Lane: WR (with GO for the player-facing part), under the standing charge at the end of `AUDIT_BRIEF.md`

Charge (Jordan, 2026-11-12): *"have Fable extend author and plan how to improve upon eras regimes and strife alongside methods to make the plot legible to player. work to improve era endings (like death of monarch, change of rule, civil war breaks out, etc) and momentum mechanisms. cascade effects and compounding are real"*.

Proposals carried by this audit (each with its coding instructions, per the brief's last standing charge):

| file | what it decides |
|---|---|
| `proposals/30_WR_A_the_era_is_a_named_period.md` | the era as a named reading with a kind, a bearer and a successor; the era endings |
| `proposals/30_WR_B_regimes_who_believes_whom.md` | the regime as a reading over held affiliations and seats: forming, merging, splitting, ending |
| `proposals/30_WR_C_strands_open_grow_join_conclude.md` | the strand life cycle, several at once, the ending that fails to come |
| `proposals/30_WR_D_momentum_and_its_brakes.md` | compounding by drawn acts on person-side readings, and the brakes |
| `proposals/30_WR_E_cascade_chains_and_the_census.md` | the cascade chains for the stories and happenings; census gates and controls |
| `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` | the player's marker, strands as named stories, news, slate, recap, foreshadowing, end reveal, the reason trail |
| `proposals/30_WR_G_regime_opinions_and_the_pull_of_ones_own.md` | A-82 and A-83: the opinion axes as roster rows, a regime's core and fringe, graded accord, and the unsaid pressure of one's circle |

Standing requirements carried: every proposal has an **Instructions to code** section (files, symbols, order, rows, call sites, named tests, gate, falsifier, control, movers, dependencies, cost, tier); A-80 (entrenchment still moves the world) is `30_WR_D` §4 and `30_WR_E` clause C8; A-81 (no scene is still) is `30_WR_D` §3 and clause C9; A-82 and A-83 are `30_WR_G` and clause C10. One item is marked **INCOMPLETE**: `30_WR_G` commit 2 (the cast's values on three new opinion axes are not authored).

## 0. Verdict

**Not yet a sound basis, and the obstacle is one of kind, not of quantity: the engine has strife and calls its realm-wide scope an era, but it has no era in the sense the charge asks for (a named period that ends when a monarch dies, the rule changes or a civil war breaks out), no regime beyond a pairwise credit factor, no momentum that is a person's rather than a count's, and nothing of any of it reaches a player.** What exists is good ground and should be kept whole: `queries/world_q.py::flows_in` (`:5172`) reads strands and eras from the Event log and stores nothing; `flows_known` (`:5473`) reads a person's own strands from his ledger; `flow_stakes` (`:5524`) stamps what is at stake onto his questions, shipped on (`data/fixtures.py:1024`); `commensurate` (`:5317`) and `loop/witness.py::_credit` (`:240`) grade a told claim by whether teller and hearer hold compatible affiliations, shipped at 0.5 (`data/fixtures.py:1086`). Every one of those is a reading or a factor on belief; none fires anything, which is what `ED-IN-0225` and the strife master's T-a/T-b require and what this plan keeps.

Three things are missing, in order of weight. (1) **The engine's `Era` is a scope with no content**: it opens on the first strife move in the realm and closes on a realm-rung terminal move with no open referent (`world_q.py:5233-5252`); it has an id and a move list, and no kind, no bearer, no name and no successor, so "the reign of Almud ended and the interregnum began" cannot be said by any reader; a monarch's death is a `joins` kind (`rosters.yaml:3390`) and natural death is off (`data/fixtures.py:690-691`), so the commonest era ending in the tree's own history cannot occur in default play. (2) **Compounding is unmeasured and unbounded by design rather than by reading**: the loops L1 to L4 are declared with asserted signs (`strife-00` §6), the guard reads terminal-code shares, and nothing distinguishes a chain that compounds (the first act raised the odds of the second) from one that merely co-occurs. (3) **The player is shown none of it**: the chronicle renders one deepest cause chain for an outside observer (`harness/chronicle.py`), the person reading holds "no era object" (`world_q.py:5379`), and the player-surface contract (`proposals/11_GO_player_surface_contract*.md`) carries no era marker, no strand list and no recap.

The plan below adds no stored era, no counter, no trigger and no era-level draw. An era ends because a person's drawn act, or the world's drawn motion, changed the state the era reading reads; the reading then names what ended and what began. `ED-IN-0352` needs no change for any era ending (§5.4); five sentences of the ratified strife master are reworded (§6); three items are listed for Jordan, each with the answer the ladder took (§11).

Four later requirements of the same day are carried and are findings in their own right. **A-80** (a held position must still move the world) and **A-81** (no scene is still): one season at seed 0 holds 59 acts that left nothing at all and 396 whose only trace is that someone watched (§12, P-2). **A-82** (a regime shares opinions on caste, religion, politics, Altonia, militarism): religion and Altonia exist as conviction poles, politics in part, caste and militarism do not (§12, P-4). **A-83** (a regime is also an unsaid pressure on conduct): no channel carries it; the design reads it from what a person believes his own circle does and leans his own weights, so it stays person-side and resistible.

## 1. What exists, as coded

(Execution evidence is in §12; line numbers are at the SHA above.)

**Strife (built, shipped).** A move is an Event whose kind is in `rosters.yaml: strife_kinds` `opens` or `joins` (`:3388-3393`). The world reading also opens a strand on a challenger's or outsider's `march.declared`, a `person.died` caused by `fight` or `accept`, and the second `succession.claimed` or `petition.filed` on one matter (`world_q.py:4768-4817`). Moves link by a shared referent, a one-rung step, or the same doer (`_links`, `:5068`); a linking move merges strands, oldest id kept (`_attach`, `:5094`). A strand is read at the lowest rung covering its moves (`_strand_of`, `:5120`). It is concluded while its latest move is terminal and no open referent remains: a live `detain` or `ban` on a party, `at_war` between parties' factions, a docketed referent (`open_referents`, `:5135`; `_concluded`, `:5158`). A later move reopens it. The instrument (`harness/strife.py`) grades 40 move codes by route and by observation, and reads link order against a shuffled control (`link_profile`, `:294`).

**The era (built as a scope).** `_eras` (`world_q.py:5233`) walks every strand move placed under the realm in log order; the first opens the era; a terminal move whose place is the realm rung, not the era's first, with no open referent among the era's realm-rung moves, closes it; the next move opens another. `Era` is `(id, moves, strands, concluded)` (`:4929`). Nothing in the loop reads it: `presented` (`:5267`) uses the open era to type a duchy's two slots, and that function has no loop consumer either. Between eras "nothing is of an era" (`strife-00` §4).

**The regime (built as one factor).** `commensurate(w, a, b)` returns −1, 0 or +1 from two persons' held affiliations against `data/affiliations.py::INCOMPATIBILITY`; `_credit` multiplies a told claim's confidence by `1 + regime_gain × c` at WITNESS. `incompatible_span` (`:5350`) reports whether an incompatible pair spans a strand's parties. There is no reading of *a* regime (who is in it, which institutions it holds, how large it is), so a regime cannot be seen to form, merge, split or end.

**Person side.** `flows_known` builds his strands from his ledger at kind level; `concluded_known` closes one on a `concludes` kind with no restraint he knows of; the war and docket arms are dropped person-side (`world_q.py:5403-5427`). "No era object exists in his reading" (`:5379`).

**Not built.** The unaware's field (`flow_stakes_within`, CR-100), flow salience (CR-101), office influence (CR-102, CR-104's `influence_rung`): a grep for each symbol under `engine/season/` returns no definition (§12). Natural death and the drawn year ship at their controls (`age_step=0.0`, `illness_rate=0.0`, `season_factor_draw=()`).

## 2. Steelman

Ranked by the weight each bears.

1. **Nothing is stored and nothing fires.** `flows_in`, `flows_known`, `commensurate` and `endings_reached` recompute from the log, the ledgers and the live Tenures; the loop consumes only the person reading, through one stamp. That is why era, regime and strife can be redesigned here without a migration: there is no state to migrate. *Attack:* grep for a writer of any strand, era or regime field: none; `world_q.py:4749-4752` states it and `tests/test_strife_flows.py` pins it. **Holds.**
2. **The person reading is honest about ignorance.** A man reads strands only from claims he holds; the war and docket arms are dropped person-side because no ledger source names them (`world_q.py:5403-5427`). *Attack:* the reading places a person by his live home (`:5366-5370`), which moves with no claim landing. **Holds with a stated limit**, already tagged in the code.
3. **The instrument refuses to flatter.** `harness/strife.py` separates a static route from an observation, prints an upper bound as an upper bound, and reads order against a shuffle. *Attack:* run it (P-1): it prints 25 codes KIND-ONLY and no link beating control. **Holds**: it reports the absence this audit builds on.
4. **The credit term is the right shape for a regime.** One factor at the telling, two persons, never an aggregate, binding the unaware. *Attack:* `20_NARRATIVE_A`'s measurement, one value for 1,031 of 1,035 pairs. **The shape holds; the reader under it fails**, and that lane repairs it.
5. **"Era by decision only" keeps the engine from authoring history.** `ED-IN-0352`: conditioning acts on decisions; no obstacle, pool or draw is touched by a flow. *Attack:* does it prevent an era from ending? No: an era ends because acts and the world's draws change what the reading reads. **Holds**, and §5.4 shows no amendment of it is needed for era endings.

## 3. Adversarial findings

Ranked worst first. R-ids are the nine requirements.

| id | severity | claim | evidence | falsifier run, outcome | touches | fix |
|---|---|---|---|---|---|---|
| **F-30-01** | blocks legibility | The engine's `Era` is a scope with no content: no ruler, kind, cause of ending or successor, and no run concludes one | `world_q.py:4929-4935`, `:5233-5252`; P-1: `1 era(s)`, `OPEN`; `audits/20` W3 (one open era at four and six seasons) | an era line printing `concluded`: none in any reading of the suite | R-01, R-03; NERS-S (zoom across time) | `30_WR_A` commits 1, 4 |
| **F-30-02** | blocks the charge's endings | None of the endings Jordan names can occur in default play: natural death off; `successions` one title deep; no WAR Proposition is ever uttered; no field is won | `data/fixtures.py:690-691`; `22_HAPPENINGS_B`; `world_q.at_war` docstring; `audits/23` S-21; P-2: zero of ten turn kinds in a season | any of `person.died`, `tenure.closed`, `succession.claimed`, `field.won` in P-2: none | R-09 | `30_WR_A`'s ending table names the carrier of each; no new mechanism |
| **F-30-10** | blocks A-81 | Scenes are still: 59 of 821 acts in one season left no change and no claim; 396 more left only bystanders' sightings | P-2 | a `null` count of 0: read 59 | R-02 | `30_WR_D` §3; `30_WR_E` C9 |
| **F-30-06** | degrades narrative | Strands do not stay several: all three read at the realm rung; a referent named once joins a strand for ever | P-1 (`per rung kind: realm 3`); `world_q.py:5054-5059`, `:5081`; WR's E-07, E-12 | a strand at a rung below the realm at seed 0, two seasons: none | R-01; A-45 | `30_WR_C` commit 1 |
| **F-30-08** | degrades narrative | Compounding is asserted and unmeasured: order equals its shuffle; none of 16 links appears; no instrument separates cause from co-occurrence | P-1; `strife-00` §6 ("asserted and unmeasured") | a pair above control by more than one: none | R-09 | `30_WR_E` §2 (the fork lift), C7 |
| **F-30-09** | degrades narrative | The one measured feedback is perverse: a refusal makes the same act likelier | `16_PESSIMIST_CORE_a_refusal_is_remembered.md` (41% against 21%) | not re-run here; cited | R-08 | that proposal; `30_WR_D` L15 |
| **F-30-04** | degrades narrative | A regime is a pairwise sign: no reading of which regimes exist, who is in one, what it holds; so forming, splitting and ending are unobservable | `world_q.py:5317-5353`; P-1 (`incompatible-span True` on all three strands) | a function returning bodies: none under `engine/season/` | R-07 | `30_WR_B` |
| **F-30-12** | degrades narrative | A regime changes what is believed and not what is done: no channel carries the pull of one's own circle (A-83) | `decision/choose.py:193-207` (two terms: pursuit, stance); `projected_axes` shifts by scar only (`person_q.py:895`) | a reader of circle deeds into the axis weights: none | R-06, R-08 | `30_WR_G` commit 5 |
| **F-30-05** | gap | Two of the opinion axes Jordan names are not conviction poles (caste, militarism); politics is partial; Altonia and religion exist | `references/descriptor_registry.yaml:214-228`, `:236-247`; `rosters.yaml:2086-2107`, `:2358-2361` | opened at the lines | R-06 | `30_WR_G` commits 1, 2 (2 INCOMPLETE) |
| **F-30-11** | defect in a proposal on file | `20_NARRATIVE_B`'s `dues_unmet` counts each lapse for ever: a compounding term with no brake | that file, edit 1 ("Each edge once") | read | R-07 | `30_WR_D` commit 1 |
| **F-30-07** | gap | Failing to conclude has no reading; XP ("trouble persists", 20 of the study's 102 endings) is a `GAP` | P-1; `strife-00` §4 | the code table: `XP … GAP` | R-01 | `30_WR_C` §3 |
| **F-30-03**, **F-30-13** | blocks legibility | No person holds an era reading and the player is shown none of era, strand, regime, recap or portent; the chronicle is an observer's, outside the simulation | `world_q.py:5379`; `harness/chronicle.py:1-12`; `11_GO_player_surface_contract_B.md` (five readings, none of these); P-2 (0 of 83 hold a strand) | grep `era` under `decision/`: none | R-03; T2 | `30_WR_A` commit 2; `30_GO_F` |
| **F-30-14** | hygiene, with consequence | The era's open-referent test and a march's side are read from live state, so a past era is judged by today's restraints | `world_q.py:5135-5139`, `:5185-5187`, `:4884-4886` (each a stated limit) | stated in the code | R-03 | `30_WR_A` reads turns by replaying the log (CR-97's own rule for TURN) |
| **F-30-15** | degrades narrative | Two petitions on one matter put the realm in an era of strife: two of three realm-rung strands at seed 0 are petitions only | P-1 | read | NERS-E | `30_WR_A`'s narrowed `troubled` |

## 4. Code matters

- **Ownership.** One owner each: the linking rule (`_links`), the conclusion rule (`_concluded`), the side read (`side_against`), the terminal codes (`harness/strife.py::terminal_codes`). `LINK_WINDOW` is spelt in the harness and wanted by `world_q` (`30_WR_C` moves it to one owner). `commensurate`'s rule will be wanted for sets as well as pairs (`30_WR_B` gives it one body).
- **Reached or declared.** `Era`, `presented`, `within`, `open_era` have no consumer but the harness and tests. `flow_stakes` is the one loop consumer and is reached (the stamp ships on) and starved (0 of 83 after one season).
- **Determinism.** Nothing in the strife readings resolves an outcome. The deterministic resolutions this subject depends on are other lanes' and carried there: a first valid claim wins (`22_HAPPENINGS_B`), a crisis of faith by rule (`16_PESSIMIST_CHAR_A`), a lapse at a fixed age, a body falling at a floor (`09_WR_B_readings_of_closure_and_tension.md`'s `threshold` count).
- **Test strength.** `tests/test_strife_credit.py:216-241` asserts `commensurate` is called and cannot observe that it returns one value (`20_NARRATIVE_A`). Every test this lane specifies plants the failure and asserts it asserted.
- **Cost.** `flows_in` is cheap (0.011 s at the plan's base, CR-97). `held_by_anyone` (`30_WR_C`) calls `flows_known` for every person: harness only, once per block.

## 5. Design matters

### 5.1 Three things, defined so they cannot be confused

| | answers | is | changes when | owner of the reading |
|---|---|---|---|---|
| **era** | who rules, and is the realm whole and fed | the span during which RULE and the realm's conditions stand | a turn: one logged Event that changes either | `world_q._eras`, `era_turns`; `person_q.era_known` |
| **regime** | whose word is taken, and what is expected of one | a graded cluster of persons and seats sharing opinions and approaches: a core, a fringe | an opinion moves (a persuasion, a drawn crisis, a scar) or a seat changes hands | `world_q.regimes`, `accord`; `person_q.custom_of` |
| **strife** | what is being fought over, by whom | strands: chains of moves about a subject, several at once, each able to end | a move opens, joins, turns, concludes or revives one | `world_q.flows_in`, `flows_known` |

They cross and the crossings are the plot: an era turn is a move in every strand whose subject is the head seat; a strand is between regimes or inside one; a regime has its own account, and its own name, for the era; a faction (allegiance, FA's) may hold two regimes.

### 5.2 Where intent, ruling and code agree and disagree

- *Agree:* nothing stored, nothing triggered (`ED-IN-0225`, R15, T-a, T-b); the person reads only what he holds (AX-7); conditioning acts on decisions (`ED-IN-0352`).
- *Disagree, resolved toward the later ruling:* the strife master makes the era the realm's strife scope with quiet between; the charge of 2026-11-12 names endings (a civil war *breaking out*) that only a period can have. Ladder step 1. The text edits owed to `strife-00` are in §6.
- *Disagree, resolved toward the code:* the master's linking rule lets any shared referent join; A-45 rules several strands; the code's own reading at seed 0 shows one rung. The bound is `30_WR_C`'s.
- *Prose only, not yet game:* the era's kinds and names; a regime as a body; cascade chains; every surface of `30_GO_F`.

### 5.3 NERS cuts

- The **realm's one slot** (R4, A1) survives: it is now the era itself. What dies is the *competition* for it, which produced grouping at the realm and nothing a player could see.
- **Capacity n+1** survives as presentation (it is what `30_GO_F` shows per rung).
- The **16 drawn links** as a weight source die (they are `[UNVERIFIED]`, four unreachable, CR-97); as a reading they stay.
- A proposed **era-level draw** ("the realm recognises the new age by a roll") fails E: it adds a second resolution of something persons' claims and accessions already resolve. Not proposed.
- A proposed **director** that paces events (the RimWorld adaptation shape, `research/game_precedent_suite/tables/R3a_colony_sims_1.md:125-126`) fails the tree's own refusals (R1, T-b) and is not proposed; damping here is persons' and places'.

### 5.4 Reconciliation with `ED-IN-0352` and `ED-IN-0225`

- **No era ending needs `ED-IN-0352` changed.** Every ending in `30_WR_A`'s table is a drawn act or a drawn motion of the world; the era reading recognises it. The era stays a reading, conditions decisions only (through stamps and their order), and touches no obstacle, pool or draw.
- **One draw sits near the line**: A-68's reading of an unopposed entry as trespass or aggression "if there is enough tension or strife". Taken here as a draw on the two parties' own state (regard, grievances between them, a live war, a working bench), which keeps `ED-IN-0352` (3) whole. The alternative reads the realm's strife level into the draw and needs a one-clause amendment. §11, J-30-2.
- **`ED-IN-0225`** (no arc carrier): kept. The census, the era, the regime and the cascade table are readings; none is a stored arc.
- **The strife master** (`ED-IN-0316`) is reworded in five sentences (§6); that is the amendment this lane does need, and it is to a design document.

### 5.5 The NPC and the chooser

Stated in `30_GO_F` ("The NPC and the AI chooser"): six channels, all existing or on file, none era-specific; the same person-side state serves player and NPC; an NPC takes the first question and a player triages (A-48). Hard-coded NPC rules found in this subject: none (there is no era or regime branch under `decision/`). What an NPC needs to be characterful here is supply, not policy: strands he holds, a regime that is more than one value, a custom to lean with or against.

## 6. Dispositions and resolutions

### 6.1 Plan positions CR-97 to CR-103

| position | listed | verified | action |
|---|---|---|---|
| CR-97 measure plot points and influence | PROPOSED, ratified on merge, unbuilt | unbuilt (no column (a) to (h) in `harness/strife.py`) | stands; its era line gains `30_WR_A`'s fields; its closure class and TURN are what `30_WR_C` reads; column (g) is re-read after `strand_links` flips |
| CR-98 loops as rows | unbuilt | unbuilt | stands; rows L8 to L16 are appended after it (`30_WR_D` commit 2, `30_WR_G` commit 5) |
| CR-99 a positive control for the strife guard | unbuilt | unbuilt | stands; its arms gain `strand_links`, `era_mandatory_vacancy`, `credit_form`, `custom_shift` |
| CR-100 the unaware's field | unbuilt | `flow_stakes_within`: no definition under `engine/season/` (P-3) | stands; under the bounded link it stamps fewer, smaller strands; a dormant strand stamps nobody, which is the bound its L5 row says it lacks |
| CR-101 flow salience | unbuilt | no `flow_salience_gain` (P-3) | stands; inside a tier, order by `flow_capacity` (`30_WR_A`) |
| CR-102 office influence (conditional) | unbuilt | no `influence_rung` (P-3) | unchanged |
| CR-103 the evaluation | unbuilt | unbuilt | stands; the fork lift (`30_WR_E` §2) is read beside its arms so that a lift is not mistaken for correspondence. Its decision rule is not edited |
| CR-105 (held) | held | held | unchanged; `30_WR_G`'s lean is not CR-105's term (it reads a ledger, not a flow, and adds no term to the score) |

### 6.2 Inconsistencies, gaps and unclear passages, decided

| # | item | resolution | ladder | carried by |
|---|---|---|---|---|
| R-30-01 | "era": the strife scope, or a period | a period: RULE and conditions; always one | 1 (the charge of 2026-11-12) | `30_WR_A`; §11 J-30-1 |
| R-30-02 | may the world's drawn motion end an era (a natural death, a year), when the master says "a terminus is recognized when persons' acts produce it" | yes | 1 (A-15, A-54) | `30_WR_A` |
| R-30-03 | "no era object exists in his reading" against a player's era marker | his account is computed from his ledger and returned as a tuple; nothing stored | 3 (`strife-00` §4's own sentence: "a person's account of an era is the strands he holds together with the realm-rung moves he knows") | `30_WR_A` commit 2 |
| R-30-04 | which strife makes the realm troubled | a realm-rung strand with an opening other than a content opener | 5 | `30_WR_A` |
| R-30-05 | does a second trouble end a troubled era | no (R11) | 3 | `30_WR_A` |
| R-30-06 | what bounds linking by referent | the strand's subject and its last three moves | 1 (A-45), 4 (the study's window) | `30_WR_C` |
| R-30-07 | what an unconcluded strand is | open, dormant (held by nobody living) or revived; no timer | 3 (R6), 4 (D-48) | `30_WR_C` |
| R-30-08 | regime: a sign, or a body | a creed set with seats; core and fringe; graded accord | 1 (A-82), 3 (`strife-00` A4) | `30_WR_B`, `30_WR_G` |
| R-30-09 | may two regimes merge by treaty | not established in the tree; conversion only | no source: said so | `30_WR_B` |
| R-30-10 | how a regime presses on conduct without a flow or omniscience | a lean of his own axis weights toward the custom he believes his circle keeps | 1 (A-83), 4 (`scar_weight_shift`) | `30_WR_G` |
| R-30-11 | is Altonia missing as an opinion axis | no: `altonian_civics` | verified | `30_WR_G` §1 |
| R-30-12 | does a grievance fade | yes: the estimate window, and a renewed tie nets it | 4 (`legitimacy`, `stability`) | `30_WR_D` commit 1 |
| R-30-13 | what counts as a durable write | a Receipt on a `RES` or `WIT` cell; a claim only in the actor's or counterparty's ledger | 5; `[ASSUMPTION]` kept | `30_WR_D` §3, `30_WR_E` |
| R-30-14 | how compounding is told from correspondence | the fork lift on one built world | 5 | `30_WR_E` §2 |
| R-30-15 | a campaign ending against an era ending | different things; `endings_reached` is read on top | 3 (`rosters.yaml: endings`) | `30_WR_A` |
| R-30-16 | does a ruler's conversion end the era | yes, as a change of ruling regime; `[ASSUMPTION]` | 5 | `30_WR_B` commit 3; §11 J-30-3 |

**Text owed to `proposals/2026-11-04-strife-flows/00_MASTER.md`** (a ratified reference; edited only on Jordan's merge, not by this lane): §4 "The era": "It opens at the first strife move in the realm and holds the realm's one slot" becomes "There is always one era: the span during which who rules the realm, and whether it is troubled, stand unchanged"; "After the era concludes nothing is of an era until a new one opens" is struck; §4 "Linking" (i) becomes "it shares a referent with the strand's subject or with one of its last three moves"; §4's last paragraph, "no era object exists in his reading", gains "his account is computed when read (`era_known`)"; §6 "A terminus is recognized when persons' acts produce it" gains "or the world's drawn motion (a death no one caused, the year)".

## 7. Research transfer

Used, each at its recorded tier (`research/game_precedent_suite/`; shapes, not figures):

| precedent | where | what it changes here |
|---|---|---|
| a strip of standing concerns that nags without pausing (CK3's "Important Actions"; King of Dragon Pass and Six Ages "Concerns") | `tutorials/T01_realm.md:23` [V3]; `tutorials/T16_managers_narrative.md:246` [V3]; `THROUGHLINES.md:167` | the slate with grounds and the `waits` line of the recap (`30_GO_F` surfaces 4, 5) |
| control passes on death; succession is the consequential moment | `T01_realm.md:24`; `THROUGHLINES.md:95`, `:132` (TM05, the dynastic relay) | a change of RULE is the era's first kind of turn; A-49's reveal is at the line's end |
| regents for child rulers | `tables/R1_dynasty_realm.md:173` [V2] (Old World) | `minority` as a standing of RULE |
| power struggles among others, shown as markers the player may help, hinder or ignore | `tutorials/T15_pressure_political.md:206` [V3] (Shadow of War) | strands shown as named stories with a slot per rung |
| rumours spread person to person and fade | `THROUGHLINES.md:92` (P27) | credit and fade as the brakes on L4 |
| repeat suppression (an event a quarter as likely each time it recurs) | `THROUGHLINES.md:103`, `:117` (Wildermyth, R8:136 [V2]) | the shape of cause fatigue; the engine's form is `refused_before`, person-side |
| a skipped offer escalates (the doom clock with a mission menu) | `THROUGHLINES.md:138` (TM11) | A-64's petition that intensifies; L13 |

Tried, did not transfer: **RimWorld's storyteller and adaptation** (`tables/R3a_colony_sims_1.md:117`, `:125-126` [V2]): a director that sizes threats to the colony's state. It is the commonest shipped answer to runaway and freeze, and the tree refuses it (R1: nothing triggered; T-b). **Technology eras as unlock gates** (Victoria 3, Oriental Empires: `T01_realm.md:152`, `T12_paradox_classical.md:294`): an era there is a tier bought or reached, not a reading of who rules.

History in the tree: `research/historical/precedents_analysis.md` §2 (invasion on the heels of civil war: an invader times his entry to internal division; one side invites him and he stays; faction blocks the reading of warnings) supports chain K-6 and A-68's reading of entry in a troubled realm; its §3 and §4 (movements that split under pressure) support K-5. That file records no sources or tiers for its cases, so it is used for shape only and nothing is quoted from it as fact. The strife study's tallies (`strife-00` §2, §4; `harness/strife_moves.yaml`) are in the tree; **the study itself is not** (`harness/strife.py:268`), and its 16 links are `[UNVERIFIED]`. **Not established in the tree, and not relied on:** any sourced account of a particular succession crisis, regency, deposition or dynastic end; rates of any of them; how often a civil war followed a ruler's death. A grounding lane would store such a note under `research/historical/` before any number is set from it.

**Null:** no precedent in the tree solves "tell compounding from correspondence" in a shipped game. The fork lift is this lane's, from the engine's own seeded draws.

## 8. Best path forward: batches for later sequencing

Each proposal carries its own instructions; this is the order. EQUAL items may share a commit window; movers land one at a time (§0.4).

| batch | lands | gate | hash | needs first |
|---|---|---|---|---|
| **B30-1 the instrument** | `30_WR_E` (null scenes, the entrenched arm, the fork lift, the shapes) | its own gate on the shipped engine: `null` above 0, C8 failing, the control shapes above 0 | EQUAL | `23_STORY_D`, `09_WR_story_instruments_that_can_fail`, `20_NARRATIVE_F` (the suite's batch E-0) |
| **B30-2 the readings** | `30_WR_A` commit 1; `30_WR_B` commits 1, 2; `30_WR_C` commits 1a, 2; `30_WR_G` commits 1, 3; `30_WR_D` commit 2 | each file's gate; `register --check` | EQUAL | `09_WR_strand_conclusion` edits 1 to 3; CR-97, CR-98 (it sits with B11-F2) |
| **B30-3 the movers**, one commit each, in this order | `30_WR_C` 1b (`strand_links`); `30_WR_D` commit 1 with `20_NARRATIVE_B`; `30_WR_A` commit 3 (`era_mandatory_vacancy`); `30_WR_G` commit 4 (`credit_form`); `30_WR_G` commit 5 (`custom_shift`) | the strife guard on against off for each; C12, C7 (L8), C11, C13, C10 | declared movers; pins re-recorded once per commit | B30-2; `20_NARRATIVE_A`, `C`; `12_ARCS_arcs_as_staged_goals`; `22_HAPPENINGS_B` |
| **B30-4 the era's conditions**, a row at a time | `30_WR_A` commit 4's rows; `30_WR_B` commit 3 | C11 and the shape of each row | EQUAL | each row's emitter: the suite's batches E-3 (`dearth`, minority), E-5 (`contested`, `schism`), E-8 (wars, `occupation`) |
| **B30-5 the player's plot** | `30_GO_F` | its gate: the seat test, the reader test | EQUAL | `11_GO_player_surface_contract_B`; B30-2; `20_NARRATIVE_C`, `E` |
| **B30-6 content** | `30_WR_G` commit 2 | the regimes block prints a holder of each new pole | a build-hash mover | Jordan's values, or `21_PROCEDURAL_B`'s rule. **INCOMPLETE** until then |

Needed for the subject to run well alone: B30-1, B30-2, B30-5. Needed for it to compose: B30-3, B30-4.

### Hash movers declared by this lane

| fixture or edit | control | mover at | proposal |
|---|---|---|---|
| `strand_links` | `all` | `subject_recent` | `30_WR_C` 1b |
| `dues_unmet` window and netting | `dues_valence` 0 | any live `dues_valence` (already a mover of `20_NARRATIVE_B`) | `30_WR_D` 1 |
| `era_mandatory_vacancy` | `False` | `True`, in a season with a vacant head seat | `30_WR_A` 3 |
| `credit_form` | `sign` | `accord` | `30_WR_G` 4 |
| `custom_shift` | 0 | above 0 | `30_WR_G` 5 |
| the cast's values on three poles | absent | authored | `30_WR_G` 2 (build hash) |
| `engine/engine_params/descriptors.json` | five affiliations | eight | `30_WR_G` 1 (the port's file; no season hash) |

### Layer 1 rows this lane meets

| row | grade | how it is met |
|---|---|---|
| `04` §A.2: `queries/` owns nothing, holds no token | STRUCTURAL | every reading recomputes; no stored era, regime, strand state or custom |
| `04` §B.9: an Event has no actor; no person-side query reaches the act store | STRUCTURAL | `era_known`, `custom_of`, the sheet readers take no World; the world half rides the `View` |
| AX-2: `decision/` reads no World | STRUCTURAL | the custom lean enters by `person_q` and the memo, as the scar shift does; named at the site in `30_WR_G` |
| AX-7: a character holds a reading of the world, never the world | STRUCTURAL | the marker, stories, portents and the pull are all his beliefs and may be false |
| T-a, T-b; `ED-IN-0225` | STRUCTURAL | nothing stored, nothing fired, no arc carrier |
| `ED-IN-0352` (3): no flow touches an obstacle, pool or draw | STRUCTURAL | kept; J-30-2 names the one draw near it |
| ID-16 (`01_AXIOMS.md:616-619`): feedback paths declared before an amplifier | MECHANICAL (G13) | nine LOOP rows before any mover of B30-3 |
| `04` §C.11: hidden in existence, never in arithmetic | STRUCTURAL | a portent shows its basis; bands withhold values the person does not hold |
| S18.1: a `View` holds ids, never references | MECHANICAL | four tuple slots of ids |
| `01_AXIOMS.md:719-721`: `regime` refused in the governance sense | CONVENTION | R17's sense, defined at `Regime`'s declaration |
| A12 (the credit form) | CONVENTION | `accord` is within its listed revert |

No hunk is asked of Layer 1.

## 9. Playable, alone and integrated

- **Alone.** The subject's playable is a seat in a realm whose head is old: *The Lean Year* (`23_STORY_E`) already holds an old lord, two claimants and a bench; with `30_WR_A` and `30_GO_F` the seated player is shown the marker, the vacancy as a mandatory question, the two claims as one story, and the recap when the lord dies. Entry point: `harness/play_surface.py` on the valley fixture. Choice surface: the slate (A-48). Legibility: `30_GO_F`. Stakes: the seat, the granary, the sworn men. End condition: the valley's ending row, or the line's end and the reveal. Instrument: `storybar --stories --seat`. Missing today: every one of those but the fixture's proposal.
- **One code path.** The readings are the same functions for the harness, the NPC's chooser inputs and the player's sheet; there is no standalone fork.
- **Integrated.** Executed edges today: `flows_known` → `flow_stakes` → `questions_for` (shipped); `commensurate` → `_credit` at WITNESS (shipped). Designed, not executed: everything else in §5.1.
- **No GM.** Nothing here needs one: an era is read, not announced by a referee; a story is named from its subject by a table.

## 10. Interfaces

| with | consumes | emits | real today? |
|---|---|---|---|
| FA (seats, wars, land) | `tenure.opened`/`closed` on the head seat; WAR commits by waging seats; `rung.seized`; presence | the era's conditions as stamps' order | the Tenure Events are real; the war and occupation Events are designed |
| CHAR (convictions, regard, the chooser) | `Person.conviction`, `conviction.moved`, `regard`, `projected_axes` | `custom_of` into the axis weights; `dues_unmet`'s window | conviction and regard are real; `conviction.moved` has no producer |
| SE (stores, cohorts) | shortfall claims; cohort moves (A-56) | `dearth` as a condition | shortfall is real; the cohort moves are designed |
| SC (hearings, petitions) | `matter.determined`, the petition's stages | the strand's closure class | determined is real and rare (2 in 12 seed-seasons) |
| PC, MB | `person.died` by `fight`; `field.won`/`lost`; losses carried | a death as an opener; a field as a turn | deaths real; no field is won |
| FI (news) | chains and confidence on told claims | credit by sign or accord | real |
| GO | every sheet reading | nothing back | `Situation`, `Offer` are proposals; these add to them |
| WR (weather, wear) | the year's spell; a broken site | natural shock as an opener | the arms ship off |

## 11. Survivors for Jordan

Each was first put through the ladder; the answer taken is marked, and work does not wait on any of them.

**J-30-1. What an era is.** *(A, taken: ladder step 1, the charge's own examples.)* An era is the span during which who rules and whether the realm is troubled stand unchanged; there is always one; it ends on a death, a change of rule, a war breaking out, a peace. *(B)* The era stays the realm's strife scope as ratified (it opens on the first strife move and there is quiet between), and the reign is a separate marker shown beside it. *As games:* under A the player lives in named ages and a king's death is the largest thing that can happen; under B the calendar of rule and the calendar of trouble are two lines, a war "breaking out" opens an era instead of ending one, and a quiet reign has no name. A rewords two sentences of the ratified strife master.

**J-30-2. What A-68's draw reads.** *(A, taken: ladder step 5; it keeps `ED-IN-0352` (3) whole.)* Whether an unopposed entry is trespass or aggression is drawn on the two parties' own state: the holder's regard for the entrant, grievances between them, a live war, a working bench. *(B)* It is drawn on the realm's strife level (how many strands are open, whether the era is troubled). B needs one clause added to `ED-IN-0352` (3): "except where Jordan rules that a draw reads a strife level; the first is A-68". *As games:* under A the same march is tolerated between friends and a provocation between enemies in the same year; under B a troubled age makes every crossing a provocation, friends included, which is K2's "even the unaware are modulated" applied to an outcome.

**J-30-3. Does a ruler's conversion end the era.** *(A, taken, `[ASSUMPTION]`.)* Yes: the ruling regime is part of RULE. *(B)* No: it is of the era, a strand and nothing more. *As games:* under A a king who changes faith opens a new age that each regime names its own way; under B only a change of person or of peace does.

**Owed content, not a decision:** the three opinion rows of `30_WR_G` §2 (names and whether any new pair strains) and the cast's values on them. Until given, the rows are held by nobody.

## 12. Evidence log

All at `2600cb0`, working tree, `PYTHONHASHSEED=0`. Outputs under `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/ERAS/`.

| id | command | seed, seasons | outcome |
|---|---|---|---|
| P-1 | `python -m engine.season.harness.strife 2 0 --strands` (`strife_2_0.txt`) | 0, 2 | 40 codes: OBSERVED 4, UNOBSERVED 8, KIND-ONLY 25, DARK 0, GAP 3 (SH, CH, XP); DN no route. `3 strands, 1 era(s)`; `per rung kind: realm 3`; `concluded 1 of 3`; era `OPEN`, 38 moves, opening kinds `march.declared, petition.filed`; `incompatible-span True` on all three; open referents `docketed 3`, others 0; `presented: 0 in 0 rung(s); grouped 2`; pairs `WN->WN` 9 against 8.23, `PT->PT` 7 against 6.25; 0 of 16 links shown; route check 13 of 312 pairs with no route, all `-> DN` |
| P-2 | `null_scene_probe.py 0 1` (a scratch probe: `populated.build_realm`, `populated.run`, `corpus_run.attempts`, `world_q.flows_in`, `flows_known`; `null_scene_s0_k1.txt`) | 0, 1 | 821 acts: 444 made, 377 refused. No change on any Event and no claim deposited from them: 59, all refused (`research` 24, `surveil` 19, `interview` 14, `reconstruct` 2). Sighting claims only: 318 refused, 78 made. 3 strands, 1 era open (kind-level terminal). 0 of 83 persons hold a strand in their own reading. `person.died`, `succession.claimed`, `tenure.closed`, `tenure.opened`, `rung.seized`, `field.won`, `field.lost`, `commitment.ended`, `matter.determined`, `matter.lapsed`: 0 each. One seed, one season: a reading, not a rate |
| P-3 | `grep -n "flow_stakes_within\|flow_salience_gain\|influence_rung" -r engine/season --include=*.py` | n/a | no definition (CR-100, CR-101, CR-104 unbuilt); `stamp_flow_stakes=True` (`data/fixtures.py:1024`), `regime_gain=0.5` (`:1086`), `age_step=0.0`, `illness_rate=0.0` (`:690-691`), `season_factor_draw=()` (`:535`) |
| P-4 | opened at the line: `references/descriptor_registry.yaml:144-162`, `:178-189`, `:214-247`; `engine/season/rosters.yaml:2343-2367`, `:3348-3398`, `:3669-3698` | n/a | the affiliation roster is five (three of religion, Einhir, Altonia); no caste or militarism pole; seven approach axes |

Not run: `pytest` (a close step); any reading beyond two seasons (the machine was loaded); the fork lift (unbuilt). Cited from other lanes and not reproduced here: WR's E-07 and E-12, NARRATIVE's E-N01, E-N04 and W-rows, PES-CORE's retry rates, HAPPENINGS §1.3.

## 13. Provided arcs and characters

`[SKIPPED: engine/season/cases/*, corpus_run — not opened by this lane; the adjudication is `audits/12_ARCS_adjudication.md`'s and is not redone.]` What this lane adds to it, from the rulings only:

| cases (as `unified/DECISIONS_ANSWERED.md` names them) | need | what this lane supplies | proposal |
|---|---|---|---|
| the 27 arcs closed or forced by a counter (A-47) | a threshold opens a mandatory scene | the vacancy of a head seat and a minor's majority as two such thresholds; the mandatory mark is `12_ARCS_arcs_as_staged_goals`' | `30_WR_A` commit 3 |
| ARC-28, 29, 30 (zero coherence, A-43) | an unknowable person keeps seats | he appears in stories and news by his acts, with no reasons and no standing | `30_GO_F` |
| NPC-038, 004, 070 (a head strips an officer, A-35) | a resistible strip | "he is deposed" as an era ending when the seat is a head seat; otherwise a turn of a strand | `30_WR_A` |
| NPC-088, ARC-31 (a killing of one's own motive, A-16) | a murder | chain K-4; when the victim rules, an era turn opened by KL | `30_WR_E`, `30_WR_A` |
| the Confrontation arc (A-36: nobody judges the Confessor) | no lawful route | schism or violence: chain K-5, the `schism` condition | `30_WR_A` commit 4 |

Dependency edge for ARCS: its staged goals arm on claims in a ledger; an era turn reaches a person as claims (`held_by`, the death apart), so a stage may be armed by an era turn with no new mechanism.

## 14. Capability authoring surface

This subject takes no skill as input. What it adds to the one authoring surface is opinion, not capability: an opinion axis is a row of `references/descriptor_registry.yaml: affiliation_roster` (name, concern), its strains are cells of `rosters.yaml: tables.incompatible`, what it condemns is `affiliation_engagement`, a faction's profession is its `creed:` (`20_NARRATIVE_D`), and a person's position is `Person.conviction`. A designer adds "what people think about X" by adding the row; regimes, accord, credit and the pull follow by declaration (`30_WR_G`). The seven approach axes are the existing `axis_roster`; nothing is added to them.
