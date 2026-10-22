# Tutorial: Faction Actions (FA) — how a person in a seat joins, leads, takes ground for, treats on behalf of, and (one day) makes war for a faction

Repo `jordanelias/ttrpg`, written against HEAD `a4ca9a5` and **revised in round 3 against `51d7b05`** (PR #495 on PR #494) and
the precedent suite (`research/game_precedent_suite/`, reference, tier 3; the changes are listed in "Round-3 corrections" at the end
of §8). All `engine/season/` paths are written `es/`. Counts come from the control run
(`proposals/2026-10-22-system-description/ctl/realm_seed{0,1,2}_2seasons.txt`: `build_realm(seed)`, two seasons, acts attributed by
`Event.causes[0]`, "ok" = at least one non-refusal event) unless a probe of mine is named (§9); round 3 re-ran the probes at
`51d7b05` and the counts held. Line cites in §§0-8 are current at `51d7b05` (PR #494 moved `world_q.py` and `rosters.yaml` lines);
§9 and the round-2 list keep the `a4ca9a5` numbers they were read at. "I1v" below is the independent re-run of the capability
inventory's claims (seeds 0-2, two seasons, hand-built acts through the callback); it is not committed, and the precedent suite's
dispositions (`research/game_precedent_suite/dispositions/D_T09.md`) quote its results.

## 0 Before you start

**The frame.** In the code there is no player character and no GM. Every person is a chooser that spends a per-season budget of
scene actions (five, plus one per live `hold`, less penalties; §2.6) on acts drawn from one closed table of verbs (`es/verb_table.yaml`, 53 rows). "You" below means the
acting person — a player's character if one is ever seated, an NPC today — so this tutorial teaches what an actor can do,
what the rules do with it, and what an actor must arrange to reach a goal. Rules that exist only in a proposal are marked
**[PROPOSED]** and kept in §7.

**The one idea to hold.** *A faction never acts.* A person holding an office acts, through that office (`es/data/verbs.py:125`;
`es/rosters.yaml:1588`). A faction is not an object in the world: it is an uttered sentence (a `Proposition`) plus the live
`commit` edges people hold to it. Everything else — its members, leaders, land, provinces, army, wars — is a question asked
of those edges at the moment it is needed, and stored nowhere (`es/queries/faction_q.py:85-95`, a frozen view "NEVER a member
of `World`").

**What you need from other subsystems.**
- *Governance (GV):* offices (seats), the rung ladder (person → hearth → community → settlement → territory → province → duchy
  → realm), `hold` edges, purview, `oblige` (service) and its term. A seat-holder's remit licenses `covenant`, `seize`, `march`
  and `dispatch`; every other act used here (`survey`, `forge`, `commit`, `release`, `utter`, `oblige`, `give`, `sabotage`)
  is `own`-eligible, a person's own right.
- *Social contest / NPC life:* `utter` (the only verb that mints a Proposition) and `commit` (the only membership edge).
- *Mass battle (MB):* `march`, the one contested FA-adjacent act; its field is resolved by MB. Occupation, which `seize` needs,
  is any member of the seat's faction standing in the town's subtree — a resident counts; a march's arrival is one way to
  put members there (§3.2).
- *Information (FI):* `survey` and `forge` produce the faction sheet, the only way a person "reads" a faction.
- *The decision layer:* which acts a person even considers is decided by what his questions are about (§2.6). This is why
  so little FA executes.

**Status (grade per the draft preamble and errata G1).** Mixed: membership, the faction view, faction-goal salience and
`survey` are **RUNS-IN-LOOP**; `oblige` (entering service) is RUNS-IN-LOOP at seed 1 only (22 of 24), never attempted at seeds 0 and 2; `commit`
executes once each at seeds 1 and 2, on uttered Propositions, never on a faction; `dispatch` executes (6, 7, 10 per seed) but
writes nothing; `covenant`, `seize`, `sabotage`,
`at_war` and the march arrival are **TESTS-ONLY** (wired, 0 successful executions in all three seeds); `declare`, `recruit`,
`conspire`, `assign` are **DESIGN-ONLY**. No computed defection and no computed war: 0 faction `commitment.ended` and 0 WAR
Propositions in seeds 0-2 (my probe).

## 0a How it plays

What a run of this subsystem looks like, as built and then as proposed. Counts are `build_realm(seed)` at seeds 0-2, two seasons,
from the control run and round-3 probes at `51d7b05` (session scripts, not committed); "reached the fold / ok" follows §4.
`[precedent: …]` tags are reference, tier 3, and decide nothing (`research/game_precedent_suite/`, dispositions in `D_T09.md`).

### As built

#### Setup choices
- **At world build nothing is chosen; `build_realm(seed)` fixes the board.** It mints nine faction Propositions (six OUGHT creeds
  naming an authored leader, three HOLDS; `es/harness/populated.py:940-946`), opens one `commit` per affiliated cast member
  (`:975`; 40 members, 43 persons in none), seats 32 offices of which 7 have no conferral basis (§1), gives 15 of 17 territories
  to four persons (the King ×6, p_npc_050 and p_npc_052 ×4 each, p_npc_021 ×1), mints the non-`orientation` rows of the 35-row
  `goals.yaml` as OUGHT Propositions (`populated.py:468-620`), and seats 25 of the 32 offices with `dispatch`, which is what lets
  their holders `march` (`es/offices.yaml:100-119, :141`; §1). The build is identical in seeds 0-2.
- **The seed decides only what follows:** which candidates the chooser draws (`choice_temperature = 0.1`,
  `es/data/fixtures.py:286`), who dies, and whether anyone swears service (seed 1 only).
- **A player at the callback** (`es/harness/play_surface.py:41-52`, `dispatching_chooser`; tests only, and the season loop has no
  other player interface) picks acts for one named person per call: any of the 47 resolvable verbs with any operands (I1v claim 5).
  It is today's only way to name a faction to join, a settlement to march on, terms to covenant or a war to utter (§2.6).

#### The loop (one season = one tick)
1. CALENDAR, then MATTER: a matured `oblige` term closes (`es/loop/matter.py:296-303`); claim confidence decays (`:305`).
2. Five rounds of DELIBERATE → RESOLVE → ENCOUNTER → WITNESS (overview §2.1). Each round a person may submit one scene; a one-act
   scene costs 1 and a scene of 2-3 acts costs 2, from a budget of `max(1, 5 + 1 per live hold − body band − 1 per leg)`
   (`es/decision/budget.py:57-61`; §2.6). Budget 5 buys 7 acts, 6 buys 9; spending is capped at 10 actions (five scenes at cost 2),
   at most 15 acts (three per scene, `fixtures.py:488`).
3. DELIBERATE: candidates form from what each question is about, an ambition's referents first (`es/queries/world_q.py:2217`). An
   FA verb forms only on an operand those questions carry (§2.6).
4. RESOLVE folds uncontested acts at once (a write or a `*.refused` Event). A `march` is declared here; its field is fought at
   ENCOUNTER in the same round (`es/verb_table.yaml:803-831`).
5. WITNESS deposits claims. A `release` (and every other `binding_decision` kind) reaches every living ledger
   (`es/epistemic.py:649-686`, a kind filter).
6. CENSUS (`es/loop/census.py`), then the driver reads `endings_reached` and returns it (`es/loop/driver.py:514-531`): a read,
   never an actor. `members` and `mustered` are among the Queries the loop asks, recomputed each time (`leaders`, `provinces_of` and
   `at_war` have no production caller, §1); the `Faction` view is never stored (`es/queries/faction_q.py:85-95`).

Automated: everything. No faction acts; a person acts, through a seat where the verb needs a remit (§2.4).

#### The choice menu (realm totals over two seasons, ok counts, seeds 0/1/2, from the control run; a one-act scene costs 1, a scene of 2-3 acts costs 2)
| verb | seat | effect | when a person picks it | grade |
|---|---|---|---|---|
| `survey` / `forge` | none | a frozen faction sheet in hand (`forge`: `head` falsified to the forger) | a held claim on someone who coheres under one faction | RUNS-IN-LOOP (survey 13/5/13; forge 12/6/15) |
| `utter` | none | a Proposition plus his hold on it (a live hold: +1 budget) | always admitted; never fails | RUNS-IN-LOOP (39/39, 39/39, 49/49) |
| `commit` | none | membership, acceptance or ambition edge | subject must be a Proposition; forms on his own utterances | RUNS-IN-LOOP at seeds 1-2 only (0/1/1), never on a faction |
| `release` | none | closes his own edge; public | to leave, breach or drop a hold | RUNS-IN-LOOP (3/5/3) |
| `oblige` | none | service to a seat for 4 seasons | a seat his ledger names | RUNS-IN-LOOP at seed 1 only (22 of 24) |
| `covenant` | `issue` | a dispensation naming the terms, held by him | needs a Proposition subject | TESTS-ONLY (0 ok; `test_in12_covenant.py`) |
| `march` | `dispatch` | army = the seat's faction's members present at his home settlement (`sides.py:110-115`); field at ENCOUNTER | needs a settlement subject to muster anyone | TESTS-ONLY (21/10/4 reached the fold, each `march.declared` then `march.refused`; 0 fields; `test_march.py:82-136`) |
| `seize` | `issue` | his hold on an occupied town | forms only on a town a held warrant names | TESTS-ONLY (0 attempted; `test_in12_seize.py`, `test_march.py:793-824`) |
| `dispatch` | `dispatch` | no state write; `order.given` in every ledger (I1v claim 4) | any person named | RUNS-IN-LOOP (6/7/10), writes nothing |
| `sabotage` / `give` | none | Site condition down / a Record moves | present at a Site / receiver co-located | `sabotage` TESTS-ONLY (0; `test_in12_step9.py`); `give` RUNS-IN-LOOP at seed 2 only (0/0/1) |

#### First season, step by step (seed 0, tick 0 → 1; round-3 probes)
1. Tick 0: Crown 11 members; provinces Crown 6, Hafenmark 4, Varfell 4, Church 1; `uncontrolled` = [terr_T15]; 32 of 32 seats
   held; 2 live `oblige`; 0 WAR Propositions.
2. Over the five rounds the realm spends these FA acts (reached the fold / ok): survey 27/5, forge 21/4, utter 17/17, commit 36/0,
   release 26/2, covenant 8/0, give 8/0, march 9/9 (each declared and each refused), dispatch 5/2, sabotage 17/0, seize 0, oblige 0.
3. The decisive acts are personal combat, not FA. The King (p_npc_020) dies as the subject of the Queen's (p_npc_032) `accept`, and
   the Duchess of Hafenmark (p_npc_050) of a Crown member's (p_npc_083) `fight`; the seam writes only the subject (overview §6 #7).
   In seeds 1 and 2 the King also dies in season 0, to the Prince's `fight` (seed 1) and the Queen's `accept` (seed 2).
4. A death closes every tenure naming the dead (`es/state/world.py:645-646`). At tick 1: 78 persons, Crown 10 members; the King's 6
   and the Duchess's 4 territories are unheld; provinces Varfell 4, Church 1; `uncontrolled` 11 of the realm's 16 territories (5
   still held); `sovereign_fraction` (0.8, 314); 6 seats vacant, 3 of them (King, Duke of Valorsmark, Duchess) with no conferral
   basis, so empty for good (`es/loop/predicates.py:126-127`; `es/state/gate.py:643-657`). The Queen's realm seat (`off_npc_032`,
   offices row `off_widow_regent`, which carries the King's remit) stays held at seed 0, by the woman whose `accept` killed him; the
   King's land does not pass to it (uncommitted round-3 probe at seed 0; `offices.yaml:234-245`).
5. Nothing answers. No faction acts; `uncontrolled` is read by one line of the harness report (`es/harness/populated.py:1518`, after
   the run), never by the loop; no verb can retake or grant
   the land (`es/loop/effects_information.py:950, 959`; only `seize` and `found` open a rung hold); nobody declares war or defects
   (0 WAR Propositions, 0 faction `commitment.ended`).
6. By hand the same tick admits the chains §3 traces (march + seize; the treaty); a settlement march through the callback folds
   `march.declared`, then `field.lost`, inside a real season (re-run in round 3 at seed 0; I1v claim 2).

#### What changes later
- Season 1 (tick 1 → 2): seed 0 ends at 31 members and 8 vacant seats; seed 1 opens 22 `oblige` to Church seats (24 live; they mature
  at tick 5 unless the seats pay upkeep, and the runs stop at tick 2, so the lapse is unmeasured) and one self-conferral (I1v
  claim 3); seed 2 loses Hafenmark's holder in this season. At tick 2 every seed reads provinces Varfell 4 / Church 1 and 11
  territories uncontrolled.
- No act refills a dead holder's land; provinces change only when a holder dies, releases his `hold`, or changes his own commits.
  `[precedent: Crusader Kings III passes titles on death by the title's succession law, and losing titles on succession is normal there [V3]; T01 precedent, Crusader Kings III §2 item 5 and §6]`

#### Failure and ending
None that the loop acts on. The season reports `endings` (`world_q.endings_reached`, v9 IN-27): a read that takes no token, emits no
Event and halts nothing, and the realm as built reaches none (`[]` after every season at seeds 0-2). `peninsular_sovereignty`
(every territory under one faction) is unreachable in computed play whoever holds what: `terr_T15` starts unheld and no verb opens
a `hold` on a territory (`es/rosters.yaml:2524-2541`; `hole_register.yaml` H-176). `theocracy` (the King's seat held by a Church
man) has been reached only by a hand-built act (`es/tests/test_in27_endings.py:78`) and needs a King. A faction with no members
persists as a Proposition (Schoenland at seed 0, tick 2). A realm with no King and 11 of its 16 territories uncontrolled is a
steady state, not a loss. `[precedent: in Crusader Kings III control passes to the heir under the title's succession law, and the
run ends when the player dies with no dynasty heir [V3]; T01 precedent, Crusader Kings III §2 item 5 and §6]` Here nothing passes, and the loop ends nothing.

#### Consequential vs cosmetic choices
- **Consequential:** who fights whom (through the personal-combat seam it decides the map); whether a landholder commits to one
  faction, two or none (it decides provinces, `world_q.py:1623-1656`); residence (one member present licenses a seizure,
  `effects_information.py:959`); which seat a person holds (its remit snapshot, though nearly every seat has `dispatch`).
- **Cosmetic today:** `covenant` ("in force" is "a reading nothing performs yet", `effects_information.py:248-253`); `at_war`
  (no reader); `head` (always `None`, `faction_q.py:116-147`); `legitimacy` and `stability` (IN-23: one person's own estimates,
  `queries/person_q.py:451, :480`, read only by the observer's report `harness/storybar.py:185-186`, so no chooser, gate or
  faction reads them).
- **Not cosmetic, but not live choices:** `loyalty` is frozen at world-gen, yet the creed and goal stance rows it weights enter
  every candidate's score (`harness/populated.py:991-992, :1047-1049`; `decision/choose.py:54, :150`); `dispatch` writes no state
  of its own, yet its public `order.given` fills every living ledger (`Person.ledger`, `state/carriers.py:669`).
- **Dominated:** offering a treaty costs a seat act and binds no one, so it loses to doing nothing (§5d).

### As proposed [PROPOSED]
- **[PROPOSED] Played mode and formation.** D-2 (ruled yes) lets RB-3 (a v9-remediation build batch) build IN-46 (grid-mode
  suspension) and IN-47 (character-sheet spaces), neither built; their designs stay PROPOSED and held, which is an
  [ASSUMPTION; medium; Jordan to correct] (`proposals/2026-10-21-v9-remediation/2026-10-21-v9-remediation-01-verdict-and-coverage.md:153`).
  IN-46 would also defer every fight from RESOLVE to ENCOUNTER, which moves the content hash
  (`proposals/2026-10-07-grid-mode-suspension.md:37-49`). A played person would choose
  operands computed play never forms (a faction to join, a settlement to march on, terms to covenant); the callback accepts them
  today (I1v claim 5). REM-27 would give `march` a settlement referent, aiming at a fought field, and REM-23 would give `commit` a
  Proposition referent (§7).
- **[PROPOSED] Verbs** (governing roster `proposals/2026-10-16-verbs/2026-10-16-verbs-03-standards-roster-and-reconciliation.md:148-158`,
  errata G19): `declare` (a public WAR Proposition; `at_war` would read True, its reader M1 still open, §7), covenant readers (M2, §7: peace
  releasing war commits, alliance counted in `mustered`, tribute renewing like upkeep), `recruit` (a contested offer of service),
  `conspire` (a plot Proposition), `assign` (post an obligee with a task); GV succession IN-61 (an heir claims a vacant throne,
  `workplans/valoria_master_workplan_v9_part2.md:198`). None exists in code.
- **[PROPOSED] What the list does not cover.** None of these items, nor those in §7, says what happens to a dead holder's
  territories (IN-61 names the throne's hold only), so under every one of them the season-0 land collapse (§2.2) would stand unless
  that is added; and `peninsular_sovereignty` would stay unreachable without a verb that opens a `hold` on a territory.

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| faction Proposition | the faction's identity: id `fac_<slug>`; a creed of mood `OUGHT`, `subject` = the authored leader, `value` = the faction name, `scope` = its role template; or mood `HOLDS` where canon gives no leader | 9 at build: 6 OUGHT creeds (Crown, Church of Solmund, Hafenmark, Varfell, Löwenritter, Restoration Movement), 3 HOLDS (Guilds, Schoenland, test `faction x`) | `es/harness/populated.py:940-946`; `es/data/rosters.py:359` (`faction_prop_id`, `'Crown'→'fac_crown'`) |
| membership | a live `commit` Tenure person → faction Proposition. "THIS IS THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE" | build_realm(0): 40 members; 43 persons belong to none (37 cohorts + 6 unplaced cast); nobody holds two | `es/queries/world_q.py:1368-1379`; opened at world-gen `populated.py:975` |
| `members(w,f)` | sorted subjects of live `commit`s to `f` | Crown 11, Church 7, Varfell 5, Hafenmark 4, Löwenritter 4, Restoration 4, Guilds 4, Schoenland 1, faction x 0 (build) | `world_q.py:1368` |
| `leaders(w,f)` | members who hold a live `hold` on an Office whose `faction` is `f` — the intersection, not either half | one entry per held SEAT, not per person (`world_q.py:1415-1419`): Crown 11 entries = 10 people (p_npc_020 holds two Crown seats), Church 7, Hafenmark 4, Varfell 4, Löwenritter 3, Guilds 2, Restoration 1; entries sum to 32 = seats, 31 distinct holders; no production caller (grep of non-test `es/` `.py`: comments and docstrings only) | `world_q.py:1382-1419` |
| `head(w,f)` | the subject of the last live `commit` to `f` carrying a non-`None` `Tenure.degree` | **always `None`**: no builder or verb writes a degree on a `commit` | `faction_q.py:116-147` |
| Office (seat) | a post anchored at a rung, with a remit, a conferral and a revocation basis; its `faction` is derived from its `body` | 32 offices (31 authored + unauthored `off_npc_084`); all 32 held at build, by 31 distinct persons; 7 have no conferral basis and can never be refilled (§5a): the six authored `conferral: null` rows and the unauthored `off_npc_084`, built with no row (`harness/populated.py:1240-1251`) | `es/offices.yaml`; `es/state/carriers.py` |
| remit | the acts a seat licenses, from the roster `issue, determine, confer, revoke, dispatch, convene`; the holder exercises a *snapshot* (`granted_acts`) taken when he was seated. The tree contradicts itself on whether the roster is closed: `rosters.yaml:315` "the CLOSED five", `:316` `open: true`, `verb_table.yaml:257` "is closed" | `remit_default` ("NOT CANON", a testing fixture) IS applied in the shipped build: loop-built seats are seated with every remit act and keep `dispatch` through `remit_unruled` even where `offices.yaml` names a remit; 25 of the 32 seats hold `dispatch` (all but the six minted rows and `off_npc_008`, whose overlay declares `remit: [issue]`; `offices.yaml:106-114` counted 22 of 23 loop-built seats at 29 authored seats, before IN-64 added two), which is where `march` comes from (`offices.yaml:100-119, :141`; round-3 probe) | `es/rosters.yaml:314-322`, `:324-332`; `es/state/gate.py:312-342` |
| `Act.via` | the seat an act is exercised through; refused "the instant the occupant is not seated" | — | `gate.py:312` (`seat_hold`) |
| `seat_faction(via)` | the faction Proposition id of the seat exercised | — | `gate.py:345-350` |
| purview | where a seat reaches: its own rung + every descendant, plus (since IN-40) the ground of any seat whose holder owes it a live `oblige`, one edge deep | upward reach is never purview | `gate.py:353-400` |
| `hold` on a rung | title to a place, owned by a person | build_realm(0): 15 of 17 territories held by four persons (King p_npc_020 ×6, p_npc_050 ×4, p_npc_052 ×4, p_npc_021 ×1); `terr_T15` unheld; `terr_T16` is Schoenland's, whose authored hold does not re-home to a person (`populated.py:1084-1087`); no settlement held | `world_q.py:169` (`hold_force`, one holder or `Forbidden`) |
| `faction_holding(w,s)` | which faction a holder coheres under: the faction itself if `s` is a rostered faction Proposition, else the one faction he is committed to; `None` for none **or two** | — | `world_q.py:1623-1656` |
| `holder_faction_of(w,r)` | walk `r`'s ancestry to the nearest held rung, return its holder's faction | a settlement under a held territory reads the territory's faction | `world_q.py:1659-1681`, walk `:1684-1692` |
| `provinces_of(w,r)` | `{faction: [territories]}` beneath `r` whose holders cohere under one faction; no minimum size; `r` itself excluded | realm, build: Crown 6, Hafenmark 4, Varfell 4, Church 1; no production caller (grep of non-test `es/` `.py`: comments and docstrings only) | `world_q.py:1566-1620` |
| `uncontrolled(w,r)` | territories at/under `r` whose `holder_faction_of` is `None` ("the revolt query"); one caller, a census report | realm, build: `['terr_T15']` | `world_q.py:1710-1750` |
| `sovereign_fraction(w,r)` | (largest single holder's share of HELD non-person rungs, count of unheld) | realm, build: `(0.4, 304)` = 6 of 15 held; no production caller (grep of non-test `es/` `.py`: comments and docstrings only) | `world_q.py:1517-1563` |
| `footprint(w,f)` | rungs `f` holds + rungs its members stand in | — | `world_q.py:1422-1441` |
| `mustered(w,r,f)` | members of `f` with a live `contain` (presence) anywhere in `r`'s subtree | — | `world_q.py:1473-1490` |
| `density(w,r,f)` | (members present in subtree, persons present in subtree) | no production caller (grep of non-test `es/` `.py`: comments and docstrings only; `_check_alignment_density`, `es/data/verbs.py:1576`, is a different function) | `world_q.py:1452-1470` |
| `fortification_of(w,r)` | `Σ garrison condition / (condition_scale × n garrisons)` in the subtree; 0.0 with none | `condition_scale = 1000` (`es/data/fixtures.py:217`); one garrison per settlement seeded | `world_q.py:1493-1514` |
| `at_war(w,a,b)` | True iff some Proposition of mood `WAR` with `{subject, value} == {a, b}` has any live `commit` | no production caller; `False` for every pair in every computed run (a hand-built WAR Proposition plus a `commit` makes it True, even inside a real season, I1v claim 5) | `faction_q.py:216-252` |
| `oblige` | service: a live Tenure person → seat, the joiner's own act, with a term | `oblige_term = 4` seasons; lapses at MATTER unless a `transfer` through the seat renews it; `default_upkeep = 1` per obligee per term | `es/verb_table.yaml:878`; `fixtures.py:892, :905` |
| `establishment_of(w,seat)` | the persons obliged to a seat (its retinue) | build_realm(0): 2 live `oblige` (both authored, term-less) | `world_q.py:1864-1890`; `populated.py:1317-1339` |
| `may_muster` | gate: may this seat move that person's presence? Seat sits + grant carries `dispatch` + the person holds a live `commit` to the seat's faction | — | `gate.py:309` (`MUSTER_ACT = "dispatch"`), `:864-887` |
| `may_seize` | gate: may this seat close another person's `hold`? Seat sits + grant carries `issue` + purview reaches the object's place | — | `gate.py:288` (`SEIZURE_ACT = "issue"`), `:833-861` |
| dispensation | a `Record` of kind `dispensation`, content `{terms, to, at}`; the instrument of both a writ (`issue`) and a covenant | stages wound by default: `record_stages_default 3`, `record_stage_term 1` | `es/loop/effects_information.py:170-237` |
| warrant | a held dispensation whose `terms` names a Record or Rung; the only source of a computed `seize` | `warrant_sourced: {seize: dispensation}` | `es/rosters.yaml:1869-1900` |
| faction sheet | a `Record` of kind `faction_sheet` freezing `faction_q.resolve` (proposition, members, holdings, seats, head) at the moment it is made | keys checked against the roster at import | `faction_q.py:255-281`; `effects_information.py:634-735` |
| organization goal | a `goals.yaml` row minted at world-gen as an OUGHT Proposition; the organization's persons `commit` to it | 35 rows; `orientation` rows mint nothing (pursuit weights only) | `es/goals.yaml`; `populated.py:468-620` |
| role template | a faction's expected-pursuit vector | 6 templates; Varfell and Löwenritter share `military-order`; Guilds and Schoenland have none; `intelligence-diplomatic` held by no faction | `es/rosters.yaml:1594-1634`, `:2746+` |
| `loyalty` | cosine of a person's pursuits against his faction's template, mapped to 0–100; 50 = indifferent; `None` with no template | read only at world-gen, to seed stance rows (`populated.py:620`, goal rows; `:1047`, the creed row toward the leader); no loop caller | `es/data/cast.py:328-367` |
| ambition | a live `commit` to an OUGHT Proposition (so every creed member has his creed as an ambition) | — | `world_q.py:1942-1977` |

## 2 How it works

### 2.1 A faction is a sentence and the people who hold to it

At world-gen each rostered faction with an authored leader and template gets a creed: `Proposition(fac_<slug>, "OUGHT",
<leader's person id>, "carries the creed of", <faction name>, 0, scope=<template>)`; the others get a `HOLDS` Proposition
naming themselves (`populated.py:940-946`). Each cast member whose authored affiliation is on the faction roster then gets
one `commit` to it (`populated.py:975`). A person with no rostered affiliation stays unaffiliated, by ruling ("Not everyone
has to belong to a faction", quoted at `populated.py:954`). Cohorts (persons of weight > 1) get no membership.

From then on, membership changes only by acts:
- **Leaving** is `release` of your own `commit` (`verb_table.yaml:965-979`, domain `hold, commit, oblige, succeed, tie,
  knot`). It writes `Tenure.until` and emits `tenure.closed` + `commitment.ended`. The chronicle channel is a
  KIND filter: any Event whose kind some `binding_decision` row emits goes to everyone alive (`es/epistemic.py:649-686`), and
  `release` is such a row, so a defection is public (so is MATTER's own `tenure.closed`).
- **Joining** is `commit` to the faction Proposition (`verb_table.yaml:167-182`; effect `effects_information.py:1038`).
  The only precondition is that the subject is an existing Proposition. A Proposition has no place, so it enters a person's
  reach only as the object of one of his own live edges (`effects_information.py:1013-1018`; `verb_table.yaml:1501`): the
  utterer's maker's `hold` puts his own utterance in reach, which is why `commit` executes once each at seeds 1 and 2. A
  non-member has no edge to a faction's Proposition, so no computed `commit` ever names a faction he does not already belong
  to: joining has no computed route (§2.6).

A faction's leadership is read *through* membership: `leaders` is members ∩ holders of that faction's offices; an office-
holder who is not committed is "staff, not a leader" (`world_q.py:1385-1389`), and only an uncommitted holder can be displaced by
`confer` (`loop/predicates.py:158-159`: a holder with any live `commit` is refused). There is no head: `head` reads a `degree`
that nothing writes.

A faction never forms, grows or splits by what people value: `loyalty` measures each member's fit (`data/cast.py:328-367`) and is
read at world-gen to weight goal and creed stance rows, never to move membership; runtime founding is parked (FA-G39, §7). Its membership
changes only when a person acts on his own edge. `[precedent: in Stellaris factions form at runtime after contact and their
approval moves what they give or cost (bonuses above 60%, a happiness cost below 20%) [V3]; T18 precedent, Stellaris §3 and §4 item 12]`

### 2.2 Land, title and provinces

Title is a `hold` edge from a **person** to a rung, one live holder per object (`hold_force`, `world_q.py:169-171`). A
faction "holds" land only through its members:

1. `faction_holding(holder)` = the single faction the holder is committed to; none or two → `None` (`world_q.py:1650-1656`).
2. `holder_faction_of(rung)` = walk the rung's ancestry (the rung itself first) to the first held rung and apply step 1 to its
   holder (`:1679-1681`, over the walk in `governing_hold`, `:1684-1692`). Settlements are unheld at build, so a town reads its territory's faction.
3. `provinces_of(rung)` groups the held territories beneath `rung` by step 1. A province exists only while its territories
   share a faction holder, so it appears and vanishes with no act (`:1566-1620`, quoting the 2026-07-13 ruling).
4. `uncontrolled(rung)` lists territories where step 2 gives `None`: unheld up the chain, a holder of no faction, or a holder
   of two (`:1710-1750`). A holder's death closes his `hold`, so a death can turn land uncontrolled.

Measured at `build_realm(0)`: provinces Crown 6, Hafenmark 4, Varfell 4, Church 1; `uncontrolled` = `terr_T15`. `terr_T16`
and its settlement `set_s_037` are not under `r_valoria` at all (my probe: 10 non-person rungs outside the realm's subtree).
This is by design: Schoenland is foreign and is built as a root rung so it stays out of the realm's queries
(`populated.py:725-735`).

**What one season does to this map.** Land passes on no death: a dead holder's `hold` closes and nothing reopens a territory
(`seize` refuses territories by kind and any town whose holder chain is empty, `loop/effects_information.py:950, 959`; no verb
grants land: `give` moves Records only, `:819`, and only `seize` and `found` open a rung `hold`, `:858-873`,
`loop/effects_founding.py:169`; v9 IN-30 tried to give `uncontrolled` a caller and stopped for want of a verb that takes unheld
land, `world_q.py:1744-1746`). The King (6 territories) dies in season 0 in every seed, the Duchess of Hafenmark (4) in season 0
at seeds 0-1 and in season 1 at seed 2, so at tick 2 every seed reads provinces Varfell 4 / Church 1, `uncontrolled` 11 of the
realm's 16 territories and `sovereign_fraction` (0.8, 314) (my probe, seeds 0-2). `uncontrolled` has one caller, a census line
(`harness/populated.py:1518`), so nothing revolts or reacts.

### 2.3 Presence and strength

An army is not a unit; it is whoever of a faction is standing somewhere when the question is asked.
- `mustered(r, f)` = members of `f` with a live `contain` edge to any rung in `{r} ∪ descendants(r)` (`world_q.py:1486-1490`).
  It reads the subtree because persons live in buildings under a settlement, never at the settlement rung itself.
- `density(r, f)` = (those members, all persons present in the same subtree); the denominator is people present, so it reads
  "how much of this place is theirs" (`:1460-1470`). It has no production caller (grep of non-test `es/` `.py`).
- `fortification_of(r)` = mean garrison condition over 1000; any positive value makes the field a WALLS terrain row when MB
  resolves it (`:1504-1514`). Nothing about strength is stored on a faction.

### 2.4 Acting through a seat: three gates in order

The four `remit:`-eligible acts here (`covenant`, `seize`, `march`, `dispatch`) pass three gates in turn; `own` acts skip
the seat half of gate 1. A failure at any of them is an
event (`<verb>.refused` or `.unauthorized`), never an error.
1. **Eligibility.** `Act.via` must be a seat the actor holds now (`seat_hold`), and that hold's snapshot `granted_acts` must
   carry the remit act the row names (`gate.py:312-342`). `covenant` and `seize` need `issue`; `march` and `dispatch` need
   `dispatch`.
2. **Typed precondition.** The row's `requires_typed` cell, three-valued (an unevaluable clause refuses). Examples:
   `covenant` = `to` exists and is a Person ∧ `subject` exists and is a Proposition (`verb_table.yaml:254-268`); `seize` =
   the seat's purview reaches the subject's place (`:1042-1054`); `march` = the subject is an existing Rung (`:803-813`).
3. **The effect's own decline.** The body may return `NO_CHANGE` (refused at the `write` clause). `seize` declines unless an
   occupation exists (§3.2); `survey` declines unless the subject coheres under exactly one faction.

Purview is asked of the seat, not the person: a seat reaches its rung and everything below it, and since IN-40 also the
ground of any seat whose holder owes it a live `oblige` (vassalage), one edge deep (`gate.py:353-400`).

### 2.5 What a faction "wants"

Wanting is expressed on persons, through three code paths:
- **Goals.** `es/goals.yaml` (35 rows) names goals for factions, bodies and seats. At world-gen every non-`orientation` goal is
  minted as an OUGHT Proposition and the organization's persons `commit` to it; `influences` links make a child body's
  persons also commit to the parent goal, `establishes` links take the parent off them (`populated.py:468-620`).
- **Ambitions and attention.** Every live `commit` to an OUGHT is an ambition (`world_q.py:1942`), so each member's creed and
  his organizations' goals become ambitions. `attention_key` (`world_q.py:2217`) orders a person's questions: tier 0 =
  questions about an ambition's referents (a creed's referent is its leader; a `seat_holders` goal's referent is whoever sits
  in the named seats), tier 1 = his own tenure objects and purview, then deeds, then the standing need question, then the
  rest. Within tiers 0 and 3 the order is by **salience**, the cosine of the person's pursuit weights against `expected(org)`
  = role-template pursuits + the summed `pursuits:` of that organization's goals (`es/data/goals.py:208-226`).
- **Loyalty.** `cast.loyalty` maps the same kind of cosine to 0–100 and sets the sign and weight of the stance rows a goal
  seeds toward its referents (`cast.py:328-367`; `populated.py:616-620`).

So a faction "wants" something only in the sense that its members look at certain people first, and lean toward or against
them. No faction has a treasury, mandate or stat line (errata G17: the `faction_state` layer was deleted). Legitimacy and stability
are not faction numbers either: IN-23 added them as one person's own windowed estimate, `person_q.legitimacy(p, holder, window)`
of a seat-holder and `person_q.stability(p, rung, window)` of a place (`queries/person_q.py:420-425, :451, :480`; ruling R7: "there
is no single faction-legitimacy number"), recomputed when read; their only caller is the observer's report
`harness/storybar.py:185-186`, so no chooser, gate or faction reads them.

### 2.6 How an actor arrives at an FA act

Each season a person's budget is `max(1, 5 + 1 per live hold − body-band penalty − 1 per travel leg)` SCENE ACTIONS
(`es/decision/budget.py:19-20, 57-61`; `budget_office_bonus = 1`, `fixtures.py:526`). Every live `hold` counts — a seat, a
landholding, a Record or Proposition you made — so `utter`, which always succeeds and opens a hold, is a budget lever. The
budget is a cost budget: a scene holding more than one act is extended and costs `extended_scene_cost = 2` (`fixtures.py:489`),
and the driver releases at most one scene per round over five rounds (`loop/driver.py:456`), so a budget of 5 buys 2+2+1 = 7
acts and a budget of 6 buys 9; the cap is 10 (cross-audit ruling C1). In the seed-0 run that is about 7.6 acts per person
per season on the basis `d.resolved` 1,132 / ~74 persons / 2 seasons. For each question (in `attention_key` order) the chooser forms one Candidate per
verb row per **referent the question carries** (`es/decision/options.py:134-238`), scores it on value alignment and stance,
and samples at `choice_temperature = 0.1` (`fixtures.py:286`). Two rosters narrow FA formation further:
- `warrant_sourced: {seize: dispensation}` — `seize` forms only on a referent that a held dispensation's `terms` names
  (`options.py:194-206`).
- `terms_sourced: {commit: [dispensation]}` — `commit` also forms on the `terms` of a dispensation the person holds and is
  addressed by (`options.py:150-165`). This is the acceptance route for a covenant.

The consequence is the main fact of this subsystem in play: a verb forms on whatever the question is about, and the FA verbs
need operands that questions rarely carry — a Proposition (`covenant`, `commit`), a Site (`sabotage`), a settlement
(`march`), a warranted settlement (`seize`). In the seed-0 run the 13 `covenant` subjects were 5 Rungs, 3 Persons and 5
absent; the 21 `march` acts that reached the fold targeted 16 person-rungs, 3 hearths and 2 vanished ids (the act store holds 25; 4 more, on dead persons, were refused before the fold), and seeds 1 and 2 targeted persons, territories, hearths and dead ids, never a settlement (I1v claim 2 and its systematic-error note); no `sabotage` named a Site; the 5 issued
dispensations named 3 Persons and 2 Records, so no warrant ever named a settlement (my probe, §9).

## 3 A worked example

**Scenario.** The Crown takes Hafenmark's town `set_s_016`, then the King offers Hafenmark's leader a treaty. Everything below
was folded through the real `SeasonDriver.resolve`/`encounter` on `build_realm(0)` at tick 0, in memory (§9 commands).
The example runs at tick 0. Its King's acts (the seizure, the treaty) cannot be rerun at tick 1 in the realm run: the King dies in
season 0 in every seed (§2.2).

### 3.1 How many men the Crown can raise, and where

`members(fac_crown)` = 11: p_npc_008, 009, 020, 030, 031, 032, 033, 035, 036, 037, 083. Their homes (nearest settlement by
`ancestry`): set_s_001 ×5 (009, 030, 031, 036, 083), set_s_002 (020), set_s_004 (032), set_s_014 ×2 (033, 035), set_s_018
(008), set_s_036 (037 — a Crown man lodged in the Church's cathedral).

The marcher is p_npc_033, holder of `off_npc_033` ("Crown's Spymaster", rung `terr_T1`, `granted_acts = (dispatch, issue)`).
`sides_of` finds his home `b_s_014_barracks`, climbs to the first settlement, `set_s_014`, and musters there
(`es/loop/sides.py:40`, body after the H-149 check):

- `mustered(set_s_014, fac_crown)` = [p_npc_033, p_npc_035] → an army of **2**.
- `density(set_s_014, fac_crown)` = (2, 5) → the Crown is 2 of the 5 persons present, 0.4 of the place.

The target: `holder_faction_of(set_s_016)` walks `set_s_016 → terr_T7` (held by p_npc_050, committed only to Hafenmark) →
`fac_hafenmark`. `fortification_of(set_s_016)` = 1000 / (1000 × 1) = **1.0** (one garrison at full condition).
`mustered(set_s_016, fac_hafenmark)` = [] and `density` = (0, 1): the only person present is `cohort_set_s_016`, a cohort that
belongs to no faction. The walls are perfect and nobody is on them.

### 3.2 March, then seize

| step | act | what the code asked | events | state written |
|---|---|---|---|---|
| 1 | `march` p_npc_033 via off_npc_033, subject set_s_016 | remit `dispatch` ✓; subject is a Rung ✓; target kind in `march_target_kinds` (settlement) ✓; defending side = Hafenmark, mustered there = none | `march.declared`, `field.unopposed`, `army.arrived` | 033 and 035's `contain` closed and reopened at set_s_016 (`_relocate`); no title written ("an arrival wrote a title" is refused, R-6) |
| 2 | (query) | `mustered(set_s_016, fac_crown)` | — | [p_npc_033, p_npc_035]: the Crown now occupies the town; `holder_faction_of` still `fac_hafenmark` |
| 3 | `seize` p_npc_020 (King) via off_npc_020, subject set_s_016 | remit `issue` ✓ (King's grant: confer, convene, determine, dispatch, issue, revoke); purview of `r_valoria` reaches set_s_016 ✓; effect: settlement kind ✓, seat faction `fac_crown` = actor's faction ✓, holder faction `fac_hafenmark` ≠ Crown ✓, Crown mustered there ✓, `hold_force(set_s_016)` = None so no hold to close | `rung.seized` | one new `hold` p_npc_020 → set_s_016 (`_take_hold`, `effects_information.py:858-873`) |
| 4 | (queries) | `holder_faction_of(set_s_016)`; `holder_faction_of(terr_T7)` | — | `fac_crown`; `fac_hafenmark` — the town changed hands, the territory did not |

Because the fortification only enters a *contested* field, an unopposed march ignores it. Because the town had no holder of
its own, the seizure closed nothing: the King's new hold *shadows* Hafenmark's territory hold in the ancestry walk. Crown
`resolve(...).holdings` gains `set_s_016`; `provinces_of` is unchanged (it counts territories only). The control (no march,
same seize) folds to `seize.refused` (`es/tests/test_march.py:793-824` runs the same sequence).

**A march is not the only way to occupy.** The licence is `mustered(town, seat faction)` (`effects_information.py:927-931,
959`), which counts any member standing in the subtree, residents included. At seed 0, tick 0, the Crown already occupies
the Church-held `set_s_036` through its resident `p_npc_037`, and the King's seat can seize it with no march and no field
(`es/tests/test_march.py:918-930`; control: re-house the resident and the same act is refused). That this never happens in
the realm run is a formation fact, not a rule: `seize` forms only on a referent a held warrant names, and no issued
dispensation's `terms` named a settlement.

### 3.3 The treaty

| step | act | result | written |
|---|---|---|---|
| 0 | control: `covenant` King via off_npc_020, subject p_npc_050 (a person), to p_npc_050 | `covenant.refused` | nothing — the subject must be a Proposition |
| 1 | `utter` King, payload `{mood: OUGHT, subject: p_npc_020, predicate: "keeps peace with", value: fac_hafenmark}` | `proposition.uttered` | `Proposition(prop:cv_u, OUGHT, p_npc_020, 'keeps peace with', fac_hafenmark, when=0)` + the King's maker's `hold` on it |
| 2 | `covenant` King via off_npc_020, subject prop:cv_u, to p_npc_050 | `covenant.offered` | `Record rec:cv_c`, kind `dispensation`, rung `r_valoria` (the seat's), content `{terms: prop:cv_u, to: [p_npc_050], at: None}`, stages at ticks 1, 2, 3; held by the King alone |
| 3 | `give` King → p_npc_050 | `give.refused` | nothing: the King stands at `b_s_002_cottage`, Baralta at `b_s_001_court`, and `give` needs the receiver present |
| 4 | `move` p_npc_050 to b_s_002_cottage, then `give` again | `travel.moved`; `record.given` | King's hold on the Record closed, Baralta's opened |
| 5 | WITNESS deposits the content; Baralta's own `questions_for` → `opening_set` | 1 `commit` Candidate on prop:cv_u (via `terms_sourced`) | — |
| 6 | that Candidate packed and folded; then the King's own `commit` | `commitment.made` ×2 | live edges on prop:cv_u: King `hold`, King `commit`, Baralta `commit` |

Now both parties are committed, which is what the effect's docstring calls "in force" — "a reading nothing performs yet"
(`effects_information.py:248-253`). `at_war(fac_crown, fac_hafenmark)` is `False` before and after; `members(fac_hafenmark)`
is unchanged. The one thing that did change is Baralta's mind: `ambitions(p_npc_050)` now ends in `prop:cv_u`, whose
referent is the King, so questions about the King move into Baralta's attention tier 0. The offerer is not committed by
offering; step 6's second `commit` is his own, separate act.

## 4 What you can do

All rows below are uncontested except `march` (prize "a field", bands Declared/Won/Lost/Unopposed, resolved by MB). An
uncontested act either writes or is refused. Acts are paid from the scene-action budget (§2.6). Counts: attempted/ok, seeds 0/1/2, where "attempted" = acts that passed
admission and reached the fold (admission refusals are uncounted) and "ok" = at least one non-refusal event.

| verb | who may | precondition | writes on success | refusal | realm |
|---|---|---|---|---|---|
| `survey` | anyone (`own`) | a claim on the subject in your own ledger; subject coheres under one faction (faction, member, or held place) | a `faction_sheet` Record in your hand, content = the five-field view now; `faction.surveyed` (private) | `survey.refused` | 57/13, 38/5, 59/13 |
| `forge` | anyone | as `survey` | the same sheet with `head` falsified to the forger | `forge.refused` | 52/12, 51/6, 57/15 |
| `commit` | anyone | subject is an existing Proposition | your `commit` edge; `commitment.made` | `commitment.refused` | 61/0, 56/1, 63/1 |
| `release` | owner of the edge | a live releasable edge of yours | `Tenure.until`; public `tenure.closed`/`commitment.ended` | `release.refused` | 45/3, 44/5, 46/3 |
| `utter` | anyone | — | a Proposition (mood from payload; computed acts mint OUGHT) + your hold on it | — | 39/39, 39/39, 49/49 |
| `oblige` | the joiner (`own`) | subject is a seat you were told of, whose `binds` admits you, that you do not hold, with no live `oblige` to it | your `oblige` with a 4-season term; `duty.taken` | `duty.refused` | 0/0, 24/22, 0/0 |
| `covenant` | seat-holder, `remit:issue` | `to` is a Person (not you); `subject` is a Proposition | a dispensation (terms, to) held by you; `covenant.offered` (not broadcast) | `covenant.refused` | 13/0, 4/0, 1/0 |
| `give` | holder of the Record | receiver present where you are | hold moves to the receiver; `record.given` | `give.refused` | 16/0, 21/0, 19/1 |
| `seize` | seat-holder, `remit:issue` | purview reaches the object's place; Record half: you hold a warrant naming it and someone else holds it; Rung half: a settlement held by another faction, your seat's faction mustered there (residents count), you committed to that faction; forms only on a warrant-named referent | closes the displaced `hold` (if any), opens yours; `record.seized`/`rung.seized` | `seize.unauthorized` (seat), `seize.refused` (world) | 0/0 in all seeds |
| `march` | seat-holder, `remit:dispatch` | subject a Rung; only a settlement musters an army | Won/Unopposed: army relocated to the target, `army.arrived`; Lost: casualties and stance on the attacker; Won: casualties and stance on the defenders (a grudge row toward the winning faction, a morale row toward their own; `effects_combat.py:259-261, 293-306`) | `march.refused` | 21, 10, 4 declared; 0 fields, 0 arrivals |
| `dispatch` | seat-holder, `remit:dispatch` | the named person exists | no tenure, store or person field (`writes: []`); `order.given`, public by kind, reaches every living ledger at WITNESS (a hand-built dispatch plus one season: 79 ledgers, 219 `told_by`, 18 firsthand; I1v claim 4) | `dispatch.refused`, `person.demanded` | 18/6, 18/7, 10/10 |
| `sabotage` | anyone present at the Site | Site exists, you stand at it | stages −(condition × 1/n) on `Site.condition`, n = persons present; `site.damaged` | `sabotage.refused` | 34/0, 22/0, 33/0 |
| `succeed` | the holder designating an heir | you hold the office | row declared, **no effect registered** (decline note at `verb_table.yaml:1113`) | — | not resolvable |

Notes: `march`'s "ok" in the ctl files counts `march.declared` as a non-refusal; every one of those acts also emitted
`march.refused`. `sabotage` alone at a fabric would take it to 0 in one act (`effects_economy.py:141-157`), but in the realm a garrison sits
on the settlement rung, where that settlement's cohort is always present (`share` counts persons on the rung,
`world_q.py:439, 1184-1189`; probe: `share(s_s_016_garrison) = (1, 1)` with only `cohort_set_s_016` there), so a saboteur
makes n ≥ 2 and one act takes at most half.

## 5 Pursuing goals here

**(a) Goals and their representation.**

| goal | how the code represents success | today |
|---|---|---|
| belong to / leave a faction | a live / closed `commit` to `fac_*` | leave: yes; join: no computed route |
| lead a faction | be in `leaders` (member + faction office); "head" | `leaders` yes; `head` never |
| take territory or a title | your `hold` on a rung; `holder_faction_of` flips | settlements only, via march + seize; territories and seats cannot be taken; no verb grants a territory to another person, and a settlement whose `holder_faction_of` is `None` (no held rung above it, or a holder in no faction or two) cannot be seized at all (`effects_information.py:959`; H-166 leaves who holds an unheld place unruled, `:939`): `set_s_037` at build, and 25 settlements under the realm at seed 0, tick 1 (round-3 probe) |
| lose territory | your `hold` closed (seized, released, your death) or your faction ties break | death and release yes; death is the realm's main land event (by tick 2, 11 of the realm's 16 territories uncontrolled in every seed, §2.2) |
| make peace or a treaty | both parties' `commit` to an uttered Proposition named in a dispensation | runs hand-built only |
| make war | a WAR Proposition with a live `commit`; `at_war` True | hand-built only (`tests/test_faction_q.py:220-260`; also inside a real season, I1v claim 5); gates nothing |
| raise retainers | `oblige` edges to your seat = `establishment_of(seat)` | seed 1: 22 men swore to Church seats; terms lapse unless paid; retainers are not an army: `mustered` and `may_muster` count faction members only (`world_q.py:1473-1490`, `state/gate.py:864-887`), so an obligee who is not a member of the seat's faction is in no march: `may_muster` drops him (`gate.py:887`) |
| raise an army | your faction's members present where you march from | yes, but only men already housed there |
| know a rival | hold a `faction_sheet` | yes (`survey`) |
| secure succession | an heir claims the vacant seat | no: `succeed` has no effect (`verb_table.yaml:1113`). A dead holder's seat falls vacant; `confer` can refill it only if the seat has a conferral basis (`loop/predicates.py:126-127`; `gate.py:643-657`). Seven of the 32 seats have no conferral basis: six authored `conferral: null` rows — King, Duke of Valorsmark, Duchess of Hafenmark, Widow Regent, Heir, Princess (`offices.yaml:188, 201, 214, 240, 253, 266`) — and the unauthored guild-leader seat `off_npc_084`, built with no row (`harness/populated.py:1240-1251`). Once vacant, the throne stays empty for good, and it is vacant after season 0 in all three seeds: the King dies in personal combat, as the subject of the Queen's `accept` (seeds 0 and 2) or of the Prince's `fight` (seed 1). Elsewhere `confer` executed once (seed 1: 1 of 5), against 8, 7 and 10 seats vacated by the end of season 2 (8, 6 and 10 still vacant; I1v claim 3, round-3 probe). `[precedent: in Crusader Kings III control passes to the heir on death and a run ends when none exists or at the 1453 end date [V3]; T01 precedent, Crusader Kings III §2 item 5 and §6]` |

**(b) The plays.**
- *Take a town without a fight.* If members of your faction already live in a rival-held settlement, it is already
  occupied: a seat granting `issue` whose purview reaches it can `seize` it at once, however many of the holding faction's people stand
  there: the effect "asks nothing of the defenders", only that your seat's faction is mustered there
  (`effects_information.py:927-931, 959`). At seed 0 the Church has 6 of the 9 persons in `set_s_036` and the Crown's one resident
  still licenses the King's seizure (`tests/test_march.py:918-930`; my probe). A member's own `move` into the town is enough as
  well (hand-built at seed 0: a Crown member `move`d into Hafenmark's `set_s_016` and the King's `seize` folded to `rung.seized`,
  where the control without the move was refused; `effects_migration.py:24-74`, and `mustered` reads `contain`). In computed play
  the act forms only on a town a held warrant names; at the effect the licence is occupation, not the warrant.
- *Take a town.* (1) Hold a seat granting `dispatch` whose holder lives in a settlement where your faction has members.
  (2) `march` on a foreign-held settlement; if no defender of the holding faction stands in its subtree, the field is
  Unopposed and your army arrives. (3) A seat granting `issue` whose purview reaches the town — your own or a fellow member's
  higher seat — `seize`s it. Your faction now reads as its holder while the territory above stays the rival's.
- *Hold a town.* Keep members standing in it: the next rival march meets defenders and a contested field, where the garrison's
  condition becomes WALLS. Lowering a rival's garrison with `sabotage` before marching is the designed counter.
- *Make a treaty.* `utter` the terms; `covenant` them to the other party through an `issue` seat; get the instrument into his
  hands with `give` (co-located; arrange it with `move`); he accepts with his own `commit`; you commit too. Breach is either
  party's `release`, which is public, and costs the breaker nothing else but witnesses' judgment of the `release` deed. A covenant
  carries no term (its `commit` edges are opened with none, `effects_information.py:1094-1096`): it lasts until a release or a
  party's death.
- *Bind a vassal.* A seat-holder who `oblige`s to your seat extends your purview over his seat's ground (IN-40). The oath is
  his act, not yours. He owes nothing by any act of his own: no tax, no troops. What your seat gains is purview over his ground,
  which `requisition` and `seize` read (`gate.py:389-428, :861`; `verb_table.yaml:766-780`); his oath lapses after `oblige_term` (4 seasons) unless
  your seat pays him upkeep (`upkeep_of`: "WHAT THIS SEAT PAYS EACH PERSON OBLIGED TO IT", `world_q.py:1893-1924`). The liege pays
  the vassal. `[precedent: in Crusader Kings III a vassal contract sets how much tax and levy the vassal owes the liege (tax steps
  0/2.5/10/15/25%) [V2 R1 D2]; T01 precedent, Crusader Kings III §3]`
- *Keep retainers.* Each `oblige` runs 4 seasons; a `transfer` through the seat of `upkeep_of(seat)` (default 1) per obligee
  renews it (`world_q.py:1893-1924`). 0 renewals occurred in any seed, and no 4-season term can mature within a two-season run
  (seed 1's 22 service terms were opened in season 1 and mature at tick 5, `loop/matter.py:296-303`), so neither lapse nor renewal
  is observed.
- *Undermine a faction's land.* Make its holder commit to a second faction (or none): his land becomes `uncontrolled` and
  its province dissolves, with no act aimed at the land at all. The towns under it then cannot be seized by anyone
  (`effects_information.py:959`; territories are refused by kind regardless, `:950`), and a march into them is Unopposed with no
  title written (`loop/sides.py:131-132`; H-166).
- *Defect with your land.* A landholder who `release`s his creed and `commit`s to another faction takes his territories with him:
  `faction_holding` reads his one live `commit` (`world_q.py:1623-1656`), so the province moves with no war, no timer and no act
  aimed at land (hand-built at seed 0: the Duke of Varfell's `release`, then `commit` to the Crown, took provinces Crown 6 → 10 and
  Varfell 4 → 0). He loses nothing else: a seat he holds stays its body's faction and keeps its remit (he becomes staff), though he
  can no longer `seize` through it (`effects_information.py:956`). His old faction's creed still names him as its leader
  (`populated.py:944`), so its members keep attending to him (§2.5). The `release` is public; witnesses judge it as a deed (its
  `alignment` cells are +0.3 on `precedent_substantive` and `rigid_flexible`, `rosters.yaml:3162, 3300`). Joining has no computed
  route (§2.1), so this happens only hand-built. `[precedent: in Pax Pamir changing loyalty is free but total, since you lose every
  gift, prize and patriot of the old coalition [V3 rulebook]; T15 precedent, Pax Pamir §3]` Valoria inverts it.

**(c) Costs, risks, counter-play, blocks.** Scenes are the only cost; there is no resource, casus belli or war score. War state
gates nothing: `march` asks for none (`loop/sides.py:107-133`), so any `dispatch` seat may march on any foreign-held settlement at
any time; a WAR Proposition can be uttered by anyone about any two factions (`utter` is `own` and requires nothing,
`verb_table.yaml:1495-1499`) and ends when its committers release (`faction_q.py:229-233`). A breach of a treaty is public and
costs the breaker only witnesses' judgment of the `release` deed (§5b). A
march with defenders present is a real field: a loss writes casualties and stance on the attacker. A seized town is retaken the
same way. The blocks are formation blocks, not rules: no computed question supplies the King a settlement to march on or a
warrant naming one, a Proposition to covenant, or a Site to sabotage (§2.6).

**(d) What the structure rewards and punishes.** Presence is everything: `mustered` counts heads present, so the faction with
people living in a town defends it against a march (a contested field), but not against a seizure, which one rival member present
licenses (§5b), and an unfortified but occupied town beats a fortified empty one. Single allegiance is
rewarded: two commits make your land nobody's. Offering a treaty costs the offerer a seat act and binds nobody until both
commit, and nothing reads the result — today a treaty is dominated by doing nothing, except for its effect on the acceptor's
attention. `dispatch` is a dead end mechanically (it writes nothing). `seize` of a territory or a seat is impossible by
construction ("A SEAT is never seized", `effects_information.py:892`; territory refused by kind, `:933-935`, tagged there `[ASSUMPTION; medium; Jordan to correct]`).

**(e) What success leaves.** A seizure leaves one `hold` and a `rung.seized` event handed to the seat's obligees (post_remit),
and changes every later `holder_faction_of`, `survey` sheet and march defender read for that town. A treaty leaves a Record,
two `commit` edges and two new ambitions. A defection leaves a public `commitment.ended`. Nothing leaves a faction-level
record, because there is no faction-level store. A death leaves the most: every tenure naming the dead closes
(`state/world.py:645-646`), so the ruler's death empties his seats and his land in one step. A faction left with no members
persists as an unread Proposition (Schoenland at seed 0 by tick 2).

## 6 How it connects

- **From GV:** seats, remits, purview, `oblige`, `transfer` upkeep, `confer`/`revoke` to fill and empty seats. A faction's land
  is GV's `hold`; FA only interprets it through `commit`.
- **From SC/NP:** `utter` and `commit` are the raw material of creeds, treaties and wars; `release` is breach and defection.
- **To MB:** `sides_of` builds the attacking army with `mustered` at the marcher's home settlement under `seat_faction(via)`,
  excluding detained men; the defender is `holder_faction_of(target)`, and the provider musters defenders and reads
  `fortification_of` (`sides.py:40-144`; `es/seam/wrappers/mass_battle.py`). `may_muster` requires each moved man's live
  `commit` to the seat's faction (`gate.py:864-887`).
- **From and to FI:** `survey`/`forge` make the sheet; a forged sheet's false `head` redirects petitions to the forger; the
  sheet's holder is the only person who knows its content.
- **Information reach:** `binding_decision` kinds (`release`, `dispatch`'s `order.given`) are public via chronicle; `seize`'s
  and `covenant`'s kinds go only to the exercised seat's obligees (`verb_table.yaml` emits notes at `:1058` and `:274`).
- **Combination worth knowing:** `seize` (FA) on occupation (`mustered`: a resident, a member's `move`, or a march's (MB) arrival)
  is the only working route by which title moves without consent.

## 7 Playing it as proposed

The governing roster is `proposals/2026-10-16-verbs/2026-10-16-verbs-03-standards-roster-and-reconciliation.md:148-158`
(errata G19): **seven FA hosts — `covenant`, `declare`, `recruit`, `conspire`, `assign`, `seize`, `sabotage`**. `levy` belongs to
MB (ruling R-01) and `succeed` to GV (R-11); the FA lexicon's nine-host list (verbs-15) is overridden on both. Everything in
this section is **[PROPOSED]**.

- **[PROPOSED] `declare` (war).** A seat makes a WAR Proposition naming two factions plus its own edge, as a `binding_decision`,
  so it is public; `at_war` then reads True. Waits on: M1 (a reader of `at_war`; MB-G15, which act it gates), D-V6 (own
  row), D-V3 (public channel past SC-01 step 13), Q3 (any `dispatch` seat, "marshals starting wars", versus the faction head
  only — which needs `head`, always `None` today).
- **[PROPOSED] covenant readers (M2).** An in-force Query; peace releasing war commits; alliance counted in `mustered` (M3,
  FA-G07); truce ranking; tribute renewing like upkeep; breach priced by one `deed:` cell. Open: Q1, does a treaty bind the
  signer or the seat (as built, it lapses with a signer's death).
- **[PROPOSED] `recruit`.** A contested offer of service through a seat; on Won the recruit's `oblige` to your seat with a term.
  Waits on: M10 (SC's contest resolver on the counterparty), IN-70 (opinion as obstacle), Q4 (may a won contest open an edge
  the counterparty owns). Today the only route to retainers is the recruit's own `oblige`.
- **[PROPOSED] `conspire`.** Draw a person into a plot against a seat: the first act mints an OUGHT plot Proposition naming the
  seat; later acts open invitees' edges on Won. Waits on: M7 (a plot reader), `conceal` (IN-12 step 10), M10.
- **[PROPOSED] `assign`** (was the rebuilt `dispatch`; rename held as D-V7). Post a named obligee to a place with a task:
  writes `Tenure.payload` on his `oblige` and, for elsewhere, his `contain` via `_relocate`. Waits on: M5 (a posting reader).
- **[PROPOSED] MB `levy`.** `recruits −n`, `troops_raw +n` on one rung; waits on M4 / J-1 (no `recruits` matter kind exists).
- **[PROPOSED] GV succession (IN-61).** The heir claims a vacant throne under an `inheritance` basis; RS-27: heirship is a title.
- **[PROPOSED] remediation (`proposals/2026-10-21-v9-remediation/`, held back).** REM-27 would give `march` `referent_class: Rung`
  offered only for settlements the marcher's ledger names, aiming at the first realm field; REM-23 would give `commit`
  `referent_class: Proposition`. No remediation item names a faction mechanic as its primary subject.
- **Parked:** runtime faction founding (FA-G39 / H-186), marriage alliance (FA-G43 / D-V2), hostage (FA-G30), embargo (FA-G33).

**Inert or refused at shipped values:** `head` (no degree writer); `at_war` (no reader, no computed WAR utterance); `dispatch`
(writes nothing; the in-tree "14 of 15 computed orders name a non-person" at `verb_table.yaml:383` is an old figure — ctl shows
18/6, 18/7, 10/10); `succeed` (no effect); covenant "in force" (no reader);
`remit_default` is a test fixture, not canon. Anything that needs a faction-level treasury or stat track will not appear: that
layer was deleted (errata G17).

## 8 Common mistakes and traps

- **"A faction is an entity with state."** No: a Proposition plus edges; `faction_q.Faction` is a view rebuilt per barrier.
- **"Covenanting binds both sides."** The offer writes only the offerer's Record. The addressee must hold it (a co-located
  `give`) and `commit`; the offerer must also `commit`. And nothing reads the result.
- **"Seize takes territory or a seat."** Only a held Record under warrant or an occupied *settlement*. A settlement seizure
  usually closes no hold (nobody held the town) and shadows the territory holder.
- **"Fortification protects a town."** Only if someone defends it; an Unopposed field never reads it.
- **"`march` executes in the realm."** The ctl column counts `march.declared`; all 21/10/4 refused, 0 arrivals. A hand-built
  settlement march does fight inside a real season: `march {subject: set_s_036}` by p_npc_033 folds `march.declared`, then
  `field.lost` with two `body` writes on the attacker (I1v claim 2; re-run in round 3 through the callback at seed 0).
- **"A member of two factions counts for both."** He counts for neither as a land-holder (`faction_holding` → `None`), though
  `members` lists him in both.
- **Seat ids.** `offices.yaml` ids (`off_spymaster`) are not the built ids of loop-built seats (`off_npc_033`); six minted
  seats keep their row ids (e.g. `off_duke_valorsmark`); read the built world.
- **"A dead ruler's seat is refilled."** Not if the seat has no conferral basis (`conferral: null`, or no row at all) — the throne,
  five other top seats and `off_npc_084` (§5a).
- **"Occupation needs a march."** Any resident member of the seat's faction occupies (§3.2).
- **"Defection costs the defector."** It costs him only witnesses' judgment; his land goes with him (§5b).
- **"`leaders` counts people."** It lists one entry per seat held; the Crown's 11 are 10 people.
- **"The remit roster is closed."** The tree says both: "CLOSED" in prose, `open: true` in data (`rosters.yaml:315-316`).
- **"`remit_default` is only a test fixture."** It is labelled one, and it is applied in the shipped realm build (§1).
- **`levy`.** `world_q.py:1121-1130` "ruled `levy` deleted" refers to a round-one extraction clause, not troop raising.
- **Code-docstring drift:** `faction_q.py:36,126` cite the world-builder's commit opener at `populated.py:692`; it is at `:975`.

Draft appendix A5 (FA block) corrected here:
1. A5 §2 lists nine FA hosts including `levy`, `dispatch`, `succeed`. Governing roster is seven (verbs-03:148-158; errata G19);
   `levy` MB's, `succeed` GV's, `dispatch` → `assign`.
2. A5 §4 "`covenant` … the lexicon says it does not [exist] … refuted". The lexicon claim is stale at its base, not refuted (errata C6).
3. A5 §3 lists `holder_faction_of` callers as `sides.py` and the MB wrapper. The code callers are `sides.py:131`,
   `_eff_march` (`effects_combat.py:270`), `seize` (`effects_information.py:958`), `uncontrolled` (`world_q.py:1750`) and
   `faction_of` (`:1706`, which `survey` uses); `seam/wrappers/mass_battle.py` mentions it only in prose (my grep, §9).
4. A5's opening P1 table gives `march` as "21 attempted, — executed"; the ctl file shows 21 "ok", which is only
   `march.declared`. My probe: all 21 also refused, targets never settlements.
5. A5 §2 "service = live `oblige` … (P1: 0)" and "0 live `oblige` edges" are seed-0 only: build has 2 authored term-less obligees
   (`populated.py:1317-1339`), and seed 1 ends with 24 live (errata G2, C5).
6. A5 §2's `seize` "closes one `hold`, opens one": the Rung half closes one only if the settlement itself was held (§3.2).
7. A5 §1 "Nine factions are rostered" is right, but A5's membership counts (Crown 9 …, 31) are after two seasons with deaths; at
   build there are 40 members (Crown 11).
8. A5 §4 grades `holder_faction_of`/`mustered`/`fortification_of` "reachable from loop; not measured". Sharper: no realm march
   reaches `mustered` or `fortification_of`, because `sides_of` returns an empty army for a non-settlement target before
   either is called (`sides.py`, H-149 check), and every realm target was a non-settlement (probe 4).
9. A5 does not say `sovereign_fraction`'s denominator is held rungs only (errata C5): realm (0.4, 304) is 6 of 15.

§8 Round-2 corrections (audit2; each cited line reopened before accepting):
1. F1 / C8 — §5a said `confer` can refill a dead holder's seat. Six null-conferral seats, the throne included, can never be
   refilled (`predicates.py:126-127`, `gate.py:643-657`, `offices.yaml:188-266`). Accepted.
2. F2 — §0/§5b/§6 implied occupation comes from a march. It is `mustered`, residents included (`test_march.py:918-927`).
   Accepted; §3.2 note and a §5b play added.
3. F3 — §1 said 16 of 17 territories held; the counts sum to 15 (`populated.py:1084-1087`; my own probe printed 15). Accepted.
4. F5 — `leaders` is one entry per seat (`world_q.py:1412-1416`); Crown 11 entries = 10 people (probe). Accepted.
5. F6 / X7 / C4 — §1 called the remit roster closed; the tree contradicts itself (`rosters.yaml:315-316`, `verb_table.yaml:257`).
   Accepted.
6. F7 — the dispatch "14 of 15" is an old in-tree figure (`verb_table.yaml:383`); ctl figures substituted. Accepted.
7. F10 — §2.1 said no computed `commit` names a Proposition. Utter's maker's hold puts a Proposition in reach, and `commit`
   executes at seeds 1 and 2; the claim holds only for a non-member joining a faction. Accepted, reworded.
8. F11 — caller list corrected (item 3 above). Accepted.
9. F13 — `remit_default` is applied in the shipped build and is the source of `dispatch`/`march` (`offices.yaml:100-119, 141`).
   Accepted.
10. F17 — T16/set_s_037 outside the realm is by design, not a defect (`populated.py:725-735`). Accepted.
11. F18 / X18 — "every FA act except sabotage is remit-eligible" was false; limited to `covenant`, `seize`, `march`,
    `dispatch`. Accepted.
12. C1 — scene budget rewritten as scene actions with extended-scene cost; "each act takes one slot in a scene" removed.
    I opened `budget.py:19-20, 57-61`, `fixtures.py:489, 526` and `driver.py:456`; the 7/9/10 arithmetic is the ruling's.
13. C2 / C5 — "attempted" defined as reached the fold; the chronicle channel described as a kind filter. Accepted.
14. X20 — this tutorial uses tick numbers for its example (tick 0) and "two seasons" only as run length. No change needed.
15. F9 (not in the requested list, but it affected §4) — "one saboteur takes a fabric to 0" is false in the realm because the
    cohort shares the garrison's rung; reopened `world_q.py:436` and probed `share`. Accepted.
No finding was rejected.

### Round-3 corrections

Revised against `51d7b05` and the precedent suite. Each line: old claim → new claim, with the evidence; code lines reopened at the
current tree before they went in. Where another suite file states the same fact, it is aligned in that file, not here.
1. Header — the control-run outputs were cited from a session directory → the committed `proposals/2026-10-22-system-description/ctl/…`; counts re-run at `51d7b05` and held (probes, seeds 0-2).
2. Line cites (PR #494, `git diff a4ca9a5 51d7b05`) — `world_q.py` +3 (imports, from `:45`), +11 (after the new `governing_hold`), +14, and +125 from `establishment_of` on; `holder_faction_of`'s walk `:1676-1681` → `:1679-1681`, over `governing_hold` `:1684-1692`; `rosters.yaml:2680+` → `:2746+`; `fixtures.py:882, :895` → `:892, :905`; `rosters.py:358` → `:359`; `test_march.py:918-927` → `:918-930` in §3.2.
3. §1 Office row, §5a, §8 — "6 seats have `conferral: null`" → seven seats have no conferral basis: the six authored rows plus the unauthored `off_npc_084` (`offices.yaml:188, 201, 214, 240, 253, 266`; `harness/populated.py:1240-1251`; probe lists the same seven at seeds 0-2); this supersedes the six of round-2 item 1.
4. §5a succession — silent on the outcome → the throne is vacant after season 0 in all three seeds (King dead in personal combat), with 8, 7 and 10 seats vacated by the end of season 2 (probe; I1v claim 3).
5. §1 remit row — "22 of 23 loop-built seats hold `dispatch`" → 25 of the 32 seats (`offices.yaml:106-114` counted 22 of 23 at 29 authored seats, before IN-64; per-seat `granted_acts`, round-3 probe).
6. §0 Status — no statement on defection or war → none computed: 0 faction `commitment.ended`, 0 WAR Propositions (probe, seeds 0-2).
7. §2.1 — `loyalty` unmentioned as read-only at world-gen, and no note on `confer` → added (`data/cast.py:328-367`; `populated.py:620, :1047`; `loop/predicates.py:158-159`).
8. §1 `leaders`, `provinces_of`, `sovereign_fraction`, `density`, `loyalty` rows and §2.3 — callers unstated → no production caller (`loyalty`: world-gen only) (grep of non-test `es/` `.py`: comments and docstrings only).
9. §2.2 — land after a death unstated → a dead holder's land is never refilled; at tick 2 provinces Varfell 4 / Church 1, 11 of 16 territories uncontrolled in every seed (probe; `effects_information.py:950, 959`; `world_q.py:1744-1746`).
10. §2.5 — "no treasury, mandate or stat line" → adds that legitimacy and stability (IN-23, PR #494) are one person's estimate, read only by `harness/storybar.py:185-186` (`queries/person_q.py:451, :480`).
11. §2.6 — "the 21 `march` targets" → the 21 that reached the fold (25 in the act store; seeds 1-2 also never a settlement) (I1v claim 2 and its systematic-error note).
12. §3 — example presented without a date → runs at tick 0 only; the King dies in season 0 in every seed (probe).
13. §4 `march` — "Won also writes the defenders' bodies" → Won writes casualties and stance on the defenders (`effects_combat.py:259-261, 293-306`; `verb_table.yaml:816-820`).
14. §4 `dispatch` — "**nothing** (`writes: []`); public `order.given`" → no tenure, store or person field, and `order.given` reaches every living ledger (I1v claim 4; `epistemic.py:649-686`); §9's "not confirmed" clause answered.
15. §5a — "death and release yes" (lose territory), "hand-built only" (make war), the retainers cell → add the death-collapse figure, the in-season hand-built war chain (I1v claim 5), and that retainers are not an army (`world_q.py:1473-1490`; `gate.py:864-887`); "take territory" adds that an unheld town cannot be seized (`effects_information.py:939, 959`).
16. §5b "Take a town without a fight" — "provided it holds a warrant naming it" → the licence is occupation however many defenders stand there, and a member's own `move` suffices (`effects_information.py:927-931, 959`; `test_march.py:918-930`; hand-built `move` then `seize` folded to `rung.seized`, control refused).
17. §5b "Make a treaty", "Bind a vassal", "Keep retainers", "Undermine a faction's land" — add: breach costs only witnesses' judgment; a covenant carries no term (`effects_information.py:1094-1096`); nothing flows up to the liege, who pays (`world_q.py:1893-1924`); no term matures within a two-season run (`matter.py:296-303`; seed 1 terms mature at tick 5); unheld land is unseizable (`effects_information.py:958-960`; `sides.py:131-132`).
18. §5b — no defection play → "Defect with your land" added (`world_q.py:1623-1656`; `effects_information.py:956`; `rosters.yaml:3162, 3300`); §8 trap "Defection costs the defector" added.
19. §5c — "no resource, casus belli or war score" → also: war state gates nothing, any person may utter a WAR Proposition (`sides.py:107-133`; `verb_table.yaml:1495-1499`; `faction_q.py:229-233`); §1 `at_war` row "False in every run" → "every computed run" (a hand-built WAR chain makes it True, I1v claim 5).
20. §5d — "the faction with people living in a town defends it" → against a march, not against a seizure; territory refusal is tagged `[ASSUMPTION; medium; Jordan to correct]` (`effects_information.py:933-935`).
21. §5e — "nothing leaves a faction-level record" → adds that a death leaves the most (`state/world.py:645-646`).
22. §8 `march` trap and dead-ruler trap — "all 21/10/4 refused" only → adds the hand-built settlement march that fights inside a season (re-run, seed 0: `march.declared`, `field.lost`); "the throne and five other top seats" → "the throne, five other top seats and `off_npc_084`".
23. §0a (new) — the draft's "the running loop has no ending condition (errata G17: `victory` deleted)" → the season reports `endings` (`world_q.endings_reached`, IN-27, PR #494) and the realm as built reaches none (`[]` at seeds 0-2); `peninsular_sovereignty` is unreachable in computed play (`rosters.yaml:2524-2541`).

## 9 Checks

- Read: `es/queries/faction_q.py` (whole); `es/queries/world_q.py:166-168, 1365-1852, 2092-2200`; `es/state/gate.py:272-400,
  833-891`; `es/loop/effects_information.py:92-256, 634-1095`; `es/loop/effects_economy.py:109-177`; `es/loop/sides.py` (whole);
  `es/verb_table.yaml` rows `commit :167`, `covenant :254`, `dispatch :372`, `give :533`, `march :803`, `oblige :878`,
  `release :965`, `sabotage :1019`, `seize :1042`, `succeed :1096`, `survey :1127`; `es/rosters.yaml:314-332, 1594-1700,
  1869-1935, 2680-2720`; `es/data/goals.py:191-226`; `es/data/cast.py:328-367`; `es/decision/options.py:100-250`;
  `es/decision/budget.py:50-61`; `es/epistemic.py:649-686`; `es/harness/populated.py:468-620, 940-980, 1317-1340`;
  `es/data/fixtures.py:217, 228, 286, 391, 526-527, 882, 895`; `es/tests/test_in12_covenant.py`, `test_march.py:500-860`,
  `test_faction_q.py:200-260`; proposals `verbs-03:140-160`; ctl files; `audit/ERRATA.md`.
- Round 2, opened: `loop/predicates.py:120-130`; `state/gate.py:643-657`; `offices.yaml:100-119, 141, 188-266` (six `conferral:
  null`); `rosters.yaml:314-317`; `verb_table.yaml:257, 1499-1502`; `decision/budget.py:19-20`; `data/fixtures.py:487-490`;
  `loop/driver.py:454-458`; `harness/populated.py:725-736, 1084-1088`; `tests/test_march.py:918-927`; `world_q.py:430-436,
  1181-1186`; grep of `holder_faction_of(` over non-test `.py`. Probe 5: `leaders(fac_crown)` 11 entries / 10 distinct
  (p_npc_020 twice); 31 distinct office holders; `share(s_s_016_garrison) = (1, 1)`.
- Probe 1 (`python -I`, build_realm(0)): faction table of §1 (members/leaders/seats/holdings/head), 40 members, 43 none, 0 with
  two; provinces Crown 6/Hafenmark 4/Varfell 4/Church 1; `uncontrolled` = [terr_T15]; `sovereign_fraction` = (0.4, 304), 15
  held rungs in the realm subtree (020 ×6, 052 ×4, 050 ×4, 021 ×1); 10 rungs (terr_T16, set_s_037 …) outside it; 2 live oblige.
- Probe 2 (march + seize, §3.1-3.2): events `['march.declared','field.unopposed','army.arrived']` then `['rung.seized']`;
  values as quoted.
- Probe 3 (covenant, §3.3): events and Record content as quoted; 1 commit Candidate formed after the give.
- Probe 4 (seed 0 and seed 1, two seasons, populated.run recipe): subject classes of `covenant`, `march`, `sabotage` (`site`
  operand: Rung 15, Person 7, Record 6, none 6 — never a Site), `commit`; issued dispensation `terms` classes; 0 WAR
  Propositions (103 OUGHT, 3 HOLDS); seed 1 `oblige` 24 (22 `duty.taken`, all to Church of Solmund seats), 0 `term.renewed`.
- `git status` clean after every probe. Not confirmed: why seed 0's two authored obligees closed; the `forge` cell details (row
  not opened). Whether the chronicle channel carried `order.given` was answered in round 3: it reached all 79 living ledgers in a
  hand-built dispatch plus one season (I1v claim 4).
- Round 3, run at `51d7b05` (`python -I`, repo untouched; session scripts, not committed): `build_realm(seed)` at seeds 0-2 for two
  seasons (provinces, `uncontrolled`, `sovereign_fraction`, members, WAR Propositions, live `oblige` and their terms, null-conferral
  and vacant seats at each tick); season-0 FA act counts and death causes; `mustered` and `density` at `set_s_036`; each seat's
  `granted_acts` (25 of 32 hold `dispatch`); the `endings` each season returned (`[]` at every seed and tick); a hand-built
  settlement march through `dispatching_chooser` inside a season at seed 0 (`march.declared`, `field.lost`); a hand-built `move`
  then `seize` at seed 0 with a no-move control; a hand-built `release` then `commit` by the Duke of Varfell at seed 0; `holder_faction_of` over the 37 settlements at seed 0, tick 1. Opened for the round-3
  edits: `loop/effects_information.py:240-254, 789-830, 855-1000, 1039-1100`; `loop/effects_combat.py:225-310`;
  `loop/effects_migration.py:24-80`; `loop/sides.py:100-135`; `loop/driver.py:505-535`; `loop/matter.py:288-310`;
  `loop/predicates.py:118-162`; `queries/world_q.py:1368-1750, 1864-1977`; `queries/person_q.py:415-505`;
  `harness/storybar.py:185`; `harness/populated.py:606-624, 1036-1052, 1236-1256, 1482-1520`; `rosters.yaml:2488-2545`;
  `offices.yaml:86-150`; `state/world.py:645-690`; `tests/test_march.py:880-930`; `tests/test_in27_endings.py:78, 357`.
