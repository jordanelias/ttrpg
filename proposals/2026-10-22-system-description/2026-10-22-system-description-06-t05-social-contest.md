# Tutorial: Social Contest and Proceedings (SC) — telling, arguing, pleading and judging: how one person moves another's beliefs, wants and legal standing

Repo `jordanelias/ttrpg`, HEAD `a4ca9a5`. Every behaviour claim cites a file I opened; runs are listed in §9.
Revised in round 3 (2026-10-22) against `51d7b05` and the precedent suite (`research/game_precedent_suite/`): §0a is new, the
edits are listed under "Round-3 corrections" at the end of §8, and code citations in §§0-8 were re-based to `51d7b05` where
PR #494 moved them. §9's Opened and Ran lists record the original `a4ca9a5` session.

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that picks scene actions each
season from a closed table of verbs, and the engine resolves each one. The budget counts *scene actions*:
`max(1, 5 + 1 per live hold − body bands − 1 per travel leg)` (`decision/budget.py:17-20, 57-61`). A scene holding more
than one act is *extended* and costs `extended_scene_cost` 2 (`data/fixtures.py:489`), and a chunk is cut to one act when
only 1 is left (`decision/choose.py:643-657`), so a budget of 5 buys 2+2+1 = 7 acts and a budget of 6 buys 9 (audit
ruling C1). Basis for the realm figure: seed 0, 74 persons, 1,132 acts reaching the fold (`d.resolved`) and 1,407 formed
(`w.acts`) over 2 seasons, i.e. about 7.6 resolved acts per person-season. "You" below means the acting person (a player's character if one is ever seated, an NPC
today), so this tutorial teaches what an actor can do, what the rules do with it, and what the actor must arrange first
to reach a goal.

**What you need from other subsystems.** A *place* (`world_q.place_of`) and people *with* you there (the `with` stem) for
`tell`/`argue`; claims in your own *ledger* (the list of beliefs a person holds, each with a source and a confidence) to
have anything to tell; an uttered *Proposition* (an immutable statement minted by `utter`) for `argue`/`commit`; and, for
proceedings, a *seat*: a live `hold` Tenure (a holding edge between a person and an office) on an Office whose grant
includes the remit act `determine` (to open cases and judge) or `convene` (to schedule sittings). Seats come from
Governance (GV); claims come from Fieldwork and witnessing (FI); pursuits come from the person model (NP).

**Primitives used below, one clause each.** A *Rung* is a place node in the containment tree (hearth, settlement, …); a
*Record* is a document entity (petition, case file); a *Proposition* carries a *mood* (`OUGHT` by default); an *Office* is
a seat and its *purview* the rungs its scope reaches; a verb row's *stratum* is its class (`social`, `binding_decision`,
…); a *prize* is what a contest is about; *with* means two persons share a place; a seat's *establishment* is the persons
bound to it; an *Observation* is the read a refusal records on its Event. Ids such as `H-`, `REM-`, `M-`, `R-`, `D-V`,
`J-C-` are register, remediation, lexicon-mechanic, ruling and decision labels, never rules in themselves.

**Status (per seed, seeds 0 · 1 · 2).** The season roll is **RUNS-IN-LOOP** (degenerate: pool 2, leverage 0). `tell`
executes on all three seeds; `speak` on seeds 0 and 2 (not 1); `determine` on seed 1 only (one Partial); `argue` on none
(**TESTS-ONLY**: no `argument.won` or `argument.lost`). `petition` and `open_case` execute on all three seeds; `commit`
executes on seeds 1 and 2 (one each), not 0; `convene` on seed 2 (1 of 5), not 0 or 1; `carry` on none (**TESTS-ONLY**).
Arrangements and speech kinds are loaded and almost unread (**TESTS-ONLY** / **DESIGN-ONLY**). The Bout kernel is
**TESTS-ONLY**. The lexicon's seven suites are **DESIGN-ONLY**. (Grade rule, from the audit errata G1: RUNS-IN-LOOP = a
non-refusal outcome inside `SeasonDriver.season` over `build_realm`; a refusal firing is not the verb executing;
TESTS-ONLY = wired, but executes only under tests/oracles or zero successes in the realm run; DESIGN-ONLY = no executing
code.)

**Two things share the name "social contest".** (A) The *season roll*, one dice roll per act, is what the game runs.
(B) The *Bout kernel*, a multi-exchange rhetorical duel, is a tested laboratory that the season loop never calls. The
code says so: *"KEEP THIS ROLL, DO NOT ADOPT THE KERNEL … the timing of its retirement is Jordan's, `SM-15`"*
(`modules/social_contest/roll.py:16-18`). The kernel is also the repo's one human-played social contest:
`systems/social_contest/sim/contest/agon_harness.py` reads `input()` (`:148-155`) and lets a person play Side A of one
named proceeding (default `formal_contest`, 3 exchanges) against a kernel policy (default `logos_spammer`), choosing each
exchange a move kind from a list built from the exchange's state (`:323-345`), then a Style (4) and an Appeal (3), with the
venue's tracker printed after each exchange. It counts its own prompts: `yes 1 | python3 -m
systems.social_contest.sim.contest.agon_harness` asks 9 over 3 exchanges (four complete runs: `A_decisive` three times,
`committee` once, because the harness does not seed `random`). It is an oracle harness, imported by no `.py` file, so the
season cannot reach it; §0a shows a session. Parts 1-6 below teach (A) and the proceedings built around it. Part 2.4 teaches
(B) as a standalone game. Part 7 teaches what is only proposed. [precedent: `research/game_precedent_suite/dispositions/D_T05.md`, row 12]

## 0a How it plays

As built, then [PROPOSED]. Counts are seeds 0 · 1 · 2 over two seasons from `ctl/`, graded by the rule in §0, unless a line says
"probe": one season of `build_realm(0)` on the recipe of `ctl/control.py`, re-run at `51d7b05`. Other games' versions of each
heading are in `research/game_precedent_suite/tutorials/T05_social_rpgs.md`; what each comparison means for this file is in
`research/game_precedent_suite/dispositions/D_T05.md` (reference, tier 3).

### Setup choices
- Nothing here is chosen at world build. `build_realm(seed)` seats the authored cast (46 named persons and 37 cohorts, overview §1)
  and its offices; whoever holds a seat whose remit grants `determine` or `convene` is the bench or the convener (§0). At build
  there is no Date and the docket is empty, on every seed (probe).
- `Person.capability` is empty on all 83 persons (ctl "capability nonempty 0"), so every social roll is two dice
  (`seam/wrappers/sigma.py:119-131`). The seed is the only lever and it moves outcomes, not rules (§0).
- A person at the callback (`harness/play_surface.py:41-52`, used by tests only) is handed one person's turn and returns `Act`s to
  the same RESOLVE. He chooses a verb row and its operands (`subject`, `to`, the `said` claim) and nothing inside the contest.

### The loop (one season; overview §2.1)
1. CALENDAR: a due Date with a holder forms an empty docket slot; one without a holder lapses (`loop/calendar.py:39-74`).
2. MATTER: claim confidence decays 5 per season (overview §2.1).
3. Five rounds (`scene_budget` 5, `data/fixtures.py:228`; `loop/driver.py:449-512`), each DELIBERATE → RESOLVE → ENCOUNTER →
   WITNESS. DELIBERATE: the chooser forms candidates, scores verb alignment plus stance, then samples (§5a); it never reads the room
   (§5c). RESOLVE: the typed precondition (refusal kind, slot spent), one roll (`modules/social_contest/roll.py:120-125`), the band,
   the row's writes and emits. WITNESS: told claims and emitted kinds deposit by channel; `binding_decision` kinds go realm-wide (§6).
4. CENSUS, the season's `endings_reached` read, then `tick += 1` (`loop/driver.py:514-519`). The only choice is which act fills a slot.

### The choice menu (§4; grades per seed)
| verb | cost | what it does | what it takes | grade, seeds 0 · 1 · 2 |
|---|---|---|---|---|
| `tell` | 1 slot (2 per extended scene) | told claim to everyone present; Failure is witnessed | a held claim; hearer present | RUNS-IN-LOOP: `news.told` 4 · 7 · 6 |
| `argue` | slot | hearer's held pursuits move 10% (S) or 20% (O) of the gap | an uttered Proposition; hearer present | TESTS-ONLY: 0 won, 0 lost |
| `speak` | slot | a witnessed `matter.*`; writes nothing | a docketed matter not his own | RUNS-IN-LOOP s0, s2 (all `matter.turned`); none s1 |
| `determine` | slot | graded disposal on the party; judge's pursuits move on S/O | seat granted `determine`; docketed Person in his ground | RUNS-IN-LOOP s1 only (one Partial) |
| `petition` | slot; mints a hold (+1 budget) | petition Record addressed to its own subject (H-94) | anyone | RUNS-IN-LOOP: 14 · 7 · 11 filed |
| `carry` | slot | would docket the petition | a held petition | TESTS-ONLY: 0 on every seed |
| `open_case` | slot; mints a hold | case file and docket item | seat granted `determine`, purview reaches | RUNS-IN-LOOP: 6 · 1 · 5 |
| `convene` | slot | a Date due next tick | seat granted `convene` | RUNS-IN-LOOP s2 only (1 of 5) |
| `utter` | slot; mints a hold | a Proposition | anyone; never refuses | RUNS-IN-LOOP: 39 · 39 · 49 |
| `commit` | slot | a commitment Tenure | a Proposition as subject | RUNS-IN-LOOP s1, s2 (one each) |

### First season, step by step (probe: seed 0, tick 0)
1. CALENDAR finds no Date: none exists at build and none is written on seed 0 in two seasons (§5c).
2. Over five rounds persons form 115 social-contest acts (formed / reaching the fold): `commit` 39/36, `petition` 22/22, `utter` 18/17,
   `carry` 12/12, `speak` 9/2, `open_case` 8/7, `tell` 3/3, `argue` 2/0, `determine` 1/0, `convene` 1/1.
3. Admission refuses 84: 36 `commitment.refused`, 16 `petition.refused`, 12 `carry.refused`, 7 `speech.unheard`, 4 `case.unauthorized`,
   2 `argument.refused`, 1 `determine.refused`, 1 `convene.refused`, 5 `act.ineligible`. The other 31 run: 17 `proposition.uttered`,
   6 `petition.filed`, 3 `case.opened`, 2 `news.told`, 1 `news.untold`, 2 `matter.turned` (both `speak`s that rolled drew Failure).
4. One actor, `p_npc_086`: `transfer` refused, `tend` refused, `petition {to: p_npc_010, subject: p_npc_010}` filed (addressed to the
   person it is about), then three `tell`s of one claim about `p_npc_010` (`transfer.refused`, confidence 100): to `p_npc_010` drew
   `news.told`; to `p_npc_007` drew `news.untold`; the same act again, in a later scene, drew `news.told`.
5. The docket after tick 0: three dateless items, `terr_T13`, `p_npc_038`, `b_s_001_court`, arrangement `None`. Only `p_npc_038` is a
   Person, so only it can ever be determined (§2.3).

### What changes later
- By the end of season 2 (ctl seed 0, attempted / ok): `tell` 23/4, `speak` 3/3, `petition` 42/14, `open_case` 12/6, `carry` 28/0,
  `commit` 61/0, `convene` 1/0. The docket only grows (3 items after season 1, 6 after season 2, none determined); no Date is written;
  13 of 74 ledgers sit at the 200-claim cap.
- No capacity grows: `train` raises only a capability key a person already holds (`sigma.py:119-131`), so the pool stays 2, and Ob
  never exceeds the ceiling 2 (`data/fixtures.py:416-419`).
- Seed 1 holds the one verdict of the three seeds: `p_npc_021`, seated at `off_npc_021`, opened the case on `p_npc_004` and
  determined it, Partial (`matter.determined`).

### Failure and ending
- A Failure writes nothing and is witnessed; a refusal spends the slot; a Failed `determine` leaves the matter docketed
  (`matter.undetermined`). No contest ends anything: a party loses at most an `oblige`, `detain` or `ban` edge.
- The season now reports `endings_reached` after CENSUS (`loop/driver.py:518`). It "halts nothing and writes nothing", and "the realm
  as built reaches nothing" (`rosters.yaml:2494-2522`; `queries/world_q.py:1764-1795`), so no social act ends a run.

### Consequential and cosmetic choices
- Consequential: `utter`, `petition`, `open_case` (each mints a hold, +1 scene budget; Records and docket items persist); `determine`
  (a binding Tenure; the party joins the seat's establishment); `tell` (claims that feed others' questions and choices). Dominant:
  `utter`, which never refuses and raises the budget (§5b play 6).
- Inert at shipped values: a room below 1.0, a hearer's capability, forgery and hostile rooms under the ceiling, quorum 1, and `speak`
  as a means to a verdict (§5d).

### A played contest inside the repo: `agon_harness.py`
The kernel's stdin harness is the one place a person plays a social contest here. It is oracle code: no `.py` file imports it, so
`engine/season/` cannot reach it. Run `python3 -m systems.social_contest.sim.contest.agon_harness` (`--proceeding` any of the 8 in
§2.4, `--human-faculty` 5, `--ai-faculty` 4, `--ai-policy` `logos`; `:503-520`).
- **Setup screen:** venue ("Formal Contest (3 exchanges)"), adjudicator ("Crowd"), the Argue pool (13D at faculty 5, §2.4's
  `max(5, 2·faculty+3)`), the track's start and bands, and a stakes line the docstring calls a demo frame, not a scene.
- **Each exchange:** Face, Concentration and the venue's own tracker; an "Appraise" line (a local pool roll fed to the armature reader,
  not a kernel move; docstring WORKAROUND 1); then a menu of move kinds built from the exchange's state: `advance`, `support`, `pass`
  always, `hard` when `can_hard`, `evidence` while an item is held, `shift` while a higher ground exists, `rebut` only where the venue
  allows it (`:323-345`). `advance` and `hard` then ask a Style (4: Precedent, Suppression, Vision, Insinuation) and an Appeal (3: Ethos,
  Pathos, Logos); `shift` asks a ground; the rest ask nothing. The AI side plays a kernel policy (`logos_spammer`). The "Interaction"
  line it prints is flavour; resolution does not read it.
- **A session:** answering `1` at every prompt (`yes 1 | python3 -m ...`) gives six options on each of the 3 exchanges and 9 prompts
  in all. Four complete runs ended `A_decisive` three times and `committee` once, because the harness does not seed `random` (n = 4).
- **Why it exists:** its docstring says no human had played the kernel and that the 2026-07-05 audit (D4/N-7) put an exchange at about
  13 per-decision consults against a 3-4 ceiling; the harness counts prompts to check. It counts prompts, not consults, so 3.0 per
  exchange on one path is not a refutation. [precedent: `research/game_precedent_suite/dispositions/D_T05.md`, rows 12, 74]

### [PROPOSED]
- Played mode: D-2 (ruled) builds IN-46 (a played, paused fight, PC) and IN-47 (character-sheet space) (overview §2.1). Neither is a
  played social contest, and neither document was read for this pass. The harness above is the repo's only played-mode social
  precedent; its menu is the same move kinds filtered by state, never drawn, and the season roll offers no in-contest choice at all. A
  drawn per-turn hand (Griftlands) has no counterpart in either resolver (`D_T05.md` row 12).
- Verbs: V11's seven suites and remediation items REM-23, REM-24, REM-25, REM-10 and REM-06 are in §7.
- Precedent-named gaps §7 does not list (design-level, reference only, `D_T05.md` rows): an evidence-to-verdict link (18); a retry gate
  on failed acts (5); agenda-bearing voters (57); a docket that refuses non-person matters or can dispose them (75).

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **contested act** | a verb row with a `contests:` prize; the act rolls once and the band it lands in selects the row's writes and emits | 1 roll per act; no rounds | `engine/season/loop/resolve.py:771-825` |
| **prize** | the thing a contest is "about", which routes it to a provider: `a standing` (`tell`), `a proposition` (`argue`, `determine`), `a matter` (`speak`) | all three → provider `social_contest`, entry `social_contest.roll`; only `a matter` has `heard_by: "bench"` | `engine/season/rosters.yaml:1299-1325` |
| **pool** | number of d10 the actor rolls | actor's `capability[VERB_CAPABILITY[verb]]`, else `pool_default` = **2**; `VERB_CAPABILITY` maps only `tell` and `speak` (to `copying`); the roster note counts one cast entry carrying a capability (`{copying: 3}`, 1 of 430 persons) in the *case corpus overlay*; `build_realm` writes none, so every realm person rolls 2 (ctl: "capability nonempty 0") | `seam/wrappers/sigma.py:119-131`; `rosters.yaml:1223-1231`; `data/fixtures.py:414` |
| **die result** | face 1 → −1, 2-6 → 0, 7-9 → +1, 10 → +2 (TN 7); *net* = sum | pool 2 nets −2…+4 | `engine/dice_engine/dice_engine.py:153-161` |
| **leverage** | the σ μ-shift (`net_boost`) added to net | **always 0.0** on this path ("zero until something supplies leverage") | `sigma.py:160-162, 191` |
| **opposition** | the opponent's score on the same capability key, if the opponent is a person holding it | else `None`; `determine`/`argue` have no capability row, so always `None` | `sigma.py:134-146` |
| **obstacle (Ob)** | what the net must clear: `opposition/2`, else `obstacle_default`, then the room, then forgery, then the ceiling | default **2**, `OB_MIN` 1, ceiling **2** | `modules/social_contest/roll.py:103-113`; `data/fixtures.py:416-419` |
| **room** | `reception_gain·reception + proof_step·proofs`, subtracted from Ob; only for `a matter` | gains **1.0** and **0.25**; a favourable room cannot take Ob below 1 | `roll.py:104-105`; `fixtures.py:425-427` |
| **reception** | signed sum, over the bench, of each judge's ledger regard for the speaker's attributed deeds | weighted by remove (firsthand 1.0, knot 0.75, told 0.5, inferred 0.25) × confidence/100 × the judge's valence | `queries/world_q.py:533-543, 549-606` |
| **proofs** | sum of remove weights of the speaker's claims about the opponent's deeds that the opponent does not *mirror* (hold the same subject+predicate) | 0 if no bench, no opponent, or opponent = speaker | `world_q.py:609-636` |
| **forgery_quality** | added to Ob for a graded inquiry examining a Record (FI's verbs, not SC's) | cannot raise a default Ob under ceiling 2 | `roll.py:96-106`; `sigma.py:184-191` |
| **S27.4 refusal** | `Ob > 2 × pool` → the act is refused, scene spent | under ceiling 2 only a pool below 1 is refused | `sigma.py:273-275` |
| **degree / band** | `margin = net − Ob`: <0 Failure, [0,1) Partial, [1,3) Success, ≥3 Overwhelming | no extension on the season path | `dice_engine.py:227-240`; C07 §4A.8 |
| **`DEGREE_STEP`** | band → step used by every pursuit mover | Failure −1, Partial 0, Success +1, Overwhelming +2 | `engine/season/data/rosters.py:842` |
| **pursuits** | a person's weighted wants (`Person.pursuits`), which drive the chooser's scoring | moved by `argue` (hearer) and `determine` (judge), step × `pursuit_shift` **0.1** | `queries/person_q.py:570-613`; `fixtures.py:433` |
| **told claim** | the claim a `tell` deposits in every hearer present (source `told_by`, at the teller's confidence, refracted) | Partial drifts it: one addressee dropped, or a number moved within `told_drift_band` 0.5; Failure deposits nothing | `loop/witness.py:136-230, 822-870`; `fixtures.py:771, 874` |
| **docket** | `World.docket`, a list of items `{date, matter, arrangement, petition}` | a matter can be docketed once; an empty slot has `matter: None` | `world_q.py:182-213` |
| **petition** | a `Record` of kind `petition` `{terms, to, from}` held by its maker | minted by `petition`, docketed by `carry` | `loop/effects_information.py:613-631, 355-414` |
| **case file** | a `text` Record minted by `open_case`, which dockets its subject | needs a seat granted `determine` whose purview reaches the matter | `effects_information.py:273-351`; `verb_table.yaml:900-923` |
| **Date / sitting** | `convene` writes a Date `{venue, holder = convener's seat, due_at = tick+1}`; at CALENDAR a due Date with a holder forms an empty docket slot, one without a holder lapses | the slot re-opens after each determination ("a standing court") | `loop/effects_governance.py:326-370`; `loop/calendar.py:28-75`; `world_q.py:235-305` |
| **bench (`judging_set`)** | live `hold`ers of seats granted `determine` whose scope contains the venue | its `matter` argument is accepted and unused | `world_q.py:442-519` |
| **quorum** | `bench.size >= bench_quorum` | shipped **1**, so it cannot refuse a seated judge | `verb_table.yaml:337-342`; `fixtures.py:923` |
| **disposal** | the Tenure `determine` opens on the party, owned by the party, on the judge's seat: `oblige` (with a term), `detain` or `ban`, graded with the band | kind from the docket item's arrangement row; `None` (every computed case) → `oblige` | `effects_information.py:513-524, 583-609` |
| **arrangement** | a proceeding's rules row (13 keys plus `id`, closed-set loader) | 8 rows; only `disposes` is read, and only on a hand-named item; the 2 rows disposing `Record` are refused by `open_case` | `arrangements.yaml:8-14`; `engine/season/arrangements.yaml:106-276` |
| **speech kind** | a forensic move name | 6 rows (`deny … hand_error_back`), `impugn_motive` capped at Partial; no reader | `arrangements.yaml:56-95` |
| **Bout (kernel)** | a staged duel: 2 sides × up to `budget` exchanges × 7 move kinds | Standing 0-10 (start 5), Reserve 12, Room cap 3.0 | `systems/social_contest/sim/contest/{primitives,resolver,modes}.py` |

## 2 How it works

### 2.1 One contested act, step by step (the season roll)

1. **Formation.** Your chooser forms the act as a candidate. `tell` and `argue` bind `to` by the *known-person fan*: one
   candidate per person you know (`verb_table.yaml:145, 1184`). You never form a contest against yourself.
2. **Admission.** The row's typed precondition is checked against the world. If it fails, the act emits the verb's
   refusal kind (`news.untold`, `argument.refused`, `speech.unheard`, `determine.refused`), the scene slot is spent and
   nothing is rolled.
3. **Sides.** The opponent is the payload operand the row names as `counterparty:`, else `subject`
   (`loop/resolve.py:771-775`): the hearer `to` for `tell`/`argue`, the party `subject` for `determine` and `speak`.
4. **Generator.** Each act gets its own seeded generator, `draw_factory(world_seed, tick)(actor, "roll:<prize>:<act id>")`
   (`resolve.py:792`), so adding one roll never moves another.
5. **Input record.** `pool`, `opposition`, `obstacle_default` 2, `obstacle_ceiling` 2, `leverage` 0.0; for `a matter`
   only, the room terms `reception` and `proofs` read off the bench (`sigma.py:149-191, 255-260`).
6. **Roll.** `net = Σ die results + net_boost(leverage, pool)`, and the boost is exactly 0 (`roll.py:124-125`).
7. **Obstacle** (`roll.py:103-113`; admission in step 2 is decided by the typed cell `requires_typed`, not the prose
   `requires:` string — `speak`'s venue half and `determine`'s date half are untyped and never checked,
   `verb_table.yaml:1077, 322`):
   `ob = opposition/2 if opposition else 2` → `room = 1.0·reception + 0.25·proofs` → if `room > 0`:
   `ob = max(ob − room, min(ob, 1))`, else `ob = ob − room` (a hostile room raises it) → `ob += forgery_quality` →
   `ob = min(ob, 2)`.
8. **S27.4.** If `ob > 2 × pool` the act is refused (`sigma.py:273-275`). With the ceiling at 2, any pool of 1 or more passes.
9. **Band.** `margin = net − ob` → Failure / Partial / Success / Overwhelming.
10. **Fold.** The verb row's `writes[band]` and `emits[band]` are applied. The contest writes nothing itself.

### 2.2 The odds, and why a fractional obstacle often does nothing

The net is always a whole number, so the three thresholds (Partial needs `net ≥ ob`, Success `net ≥ ob+1`, Overwhelming
`net ≥ ob+3`) depend only on `ceil(ob)`. **An obstacle of 1.45 plays exactly like 2; one of 0.5 plays exactly like 1.**
Exact odds (all d10 faces enumerated with the repo's `_die_result` and `degree_from_net`):

| pool | Ob (effective) | Failure | Partial | Success | Overwhelming | when you meet it |
|---|---|---|---|---|---|---|
| 2 | 2 (any Ob in (1,2]) | .74 | .19 | .07 | .00 | almost every act in the realm |
| 2 | 1 (any Ob in (0,1]) | .42 | .32 | .25 | .01 | a room ≥ 1.0, or a hearer with capability ≤ 2 |
| 2 | 0 | .11 | .31 | .51 | .07 | opponent holds the key at 0 |
| 3 | 2 | .60 | .228 | .162 | .01 | teller with `copying: 3` (corpus overlay only; no realm person) |
| 4 | 2 | .488 | .232 | .242 | .038 | pool 4 (no corpus person) |
| 2 | 3 (uncapped control only) | .93 | .06 | .01 | .00 | ceiling `None` arm, hostile room −1 |

Overwhelming is impossible at pool 2 against Ob 2: two dice net at most +4 and the band needs 5.

### 2.3 Proceedings: bringing, hearing and determining a matter

A *matter* is whatever a docket item names: a person or, in computed play, often a Rung that is no person (seed 0 after
tick 0: `terr_T13`, `p_npc_038`, `b_s_001_court`; 2 of the 6 `case.opened` over two seasons on seed 0 name such a Rung, a
territory and a building). `determine`'s `party` conjunct requires a Person (`verb_table.yaml:327-328`), so a Rung matter
can be spoken to (`b_s_001_court` drew a `matter.turned`) but never determined, and it stays on the docket.
There are two ways onto the docket and one way off. [precedent: `research/game_precedent_suite/dispositions/D_T05.md`, row 75]

- **Without a seat (petition route).** `petition` mints a petition Record `{terms, to, from}` into your hand
  (`effects_information.py:613-631`). A *computed* petition's `to` and `subject` bind the question's one referent, so it is
  addressed to the very person it is about (H-94, `verb_table.yaml:941`); a complaint to a third party cannot be formed. Whoever holds it may `carry` it: the petition's stages are re-wound and a dateless
  docket item `{matter: the petition's terms, arrangement: None, petition: <id>}` is appended (`:355-414`). `give` can hand
  the petition to another person first.
- **From a seat (case route).** A holder of a seat granted `determine` whose purview reaches the matter's place may
  `open_case`: a `text` case file is minted at the seat's rung, and the matter fills the first open slot at the nearest
  sitting whose venue contains the matter's place, or else is appended dateless (`:273-351`; `world_q.py:247-269`). A
  matter already docketed is declined. A computed case always writes `arrangement: None` (`effects_information.py:331-332`).
- **A sitting.** A holder of `remit:convene` names a venue above the person tier; `convene` writes a Date due next tick
  whose holder is the convener's seat (`effects_governance.py:357-370`). At CALENDAR a due Date *with* a holder fires and
  forms an empty slot; one without a holder fires and lapses (`calendar.py:39-74`). A slot re-opens after each
  determination, so one convening is a standing court (`world_q.py:289-290`). Judges on the bench whose ledger holds a
  `date.fired` claim about that venue stamped with the firing's tick, from any source (`world_q.py:301-302`), are then asked about the sitting's person matters (`sittings_before`, `:272-305`).
- **Hearing (`speak`).** Anyone at a place may speak to a docketed matter that is not his own. The contest reads the bench
  at the speaker's place through the room terms. Its four bands emit `matter.carried` / `.advanced` / `.held` / `.turned`
  and **write nothing** (`verb_table.yaml:1080-1090`); witnesses learn which way it went.
- **Determination (`determine`).** The judge (actor) must exercise a seat granted `determine`, the subject must be a
  person, docketed, inside his bench's ground, and the bench must meet quorum 1 (`verb_table.yaml:323-341`). The roll is
  the judge's pool 2 against Ob 2 *for every party*: prize `a proposition` has no bench room and `determine` has no
  capability key (`verb_table.yaml:346`). Overwhelming/Success: the disposal Tenure opens graded with the band, the
  matter leaves the docket, and the **judge's own** pursuits move by consequence. Partial: the disposal opens graded
  Partial, no pursuit moves. Failure: nothing opens; the matter stays; `matter.undetermined` (`effects_information.py:513-550`).
  The disposal kind is the docket item's arrangement's `disposes` (`oblige`/`detain`/`ban`); with `None` it is an
  `oblige` carrying `oblige_term`, which the party may later `release` (`:599-608`).
- **What the bench is.** `judging_set(w, venue)` = live `hold`ers of seats granted `determine` whose scope rung contains
  the venue. Its `matter` argument is unused: *"nothing yet maps a docketed matter to its governing arrangement row"*
  (`world_q.py:461-471`). **Arrangements and speech kinds** are loaded but the only key read is `disposes`, on a hand-named
  item; no act carries a speech kind.

### 2.4 The Bout kernel (standalone, TESTS-ONLY)

A *bout* sets two `Contestant`s (a faculty, default 4) in a *venue* for up to `budget` exchanges. Each exchange, side A
then side B choose a `Move` through a *policy* (a function reading a `ContestView`), `Bout.resolve` applies it, checks
faults after every move, and checks the win condition at the end of each exchange and at close (`resolver.py:440-466`).

| element | rule (all `[SEED]` values) | where |
|---|---|---|
| Standing (Face) | 0-10, start 5; an ethos gain builds `+0.8·degree`; `support` builds +0.8 | `primitives.py:32-33` |
| Reserve | 12; cost advance 3, hard 5, shift 4, support 2, pass 0, evidence 3, rebut 3; `support`/`pass`/unaffordable regain 4 | `primitives.py:50-56` |
| Room | per side, cap 3.0; a pathos gain builds `+0.5·degree`; feeds readiness | `primitives.py:233` |
| stasis ground | `fact < definition < quality < jurisdiction < consequence < feasibility`; `shift` may only move up; moving down or naming none is self-contradiction | `primitives.py:14`; `resolver.py` `_apply` |
| reception roll | pool `max(5, 2·faculty+3)`, leverage `(faculty−4)/6`, plus 0.5 only on-ground (`Leverage.net`); the resolver always passes `on_ground=True` because an off-ground `advance` is an evasion that returns before any roll; Ob 2, pool-desaturation extension → ordinal 0-3 | `primitives.py:209, 225-230`; `resolver.py:301, 380-381` |
| advancement | `gain = 2.6 · degree · resonance · readiness · U(0.92,1.08) · bias`; resonance mixes the venue's appeal × tense weight with the judge's character by a leak `(1−discipline) + 0.5·standing_frac` (cap .9), floor .15; readiness `0.40 + 0.60·min(1, 0.4·standing_frac + 0.4·room_frac)` | `resolver.py:35-44`, C07 §4B.5 |
| moves | `advance`/`hard` (on the live ground; `hard` licit only when well ahead before a lay or hostile judge), `shift`, `support`, `pass`, `evidence` (best dossier item on the ground, corroboration 1.0/.7/.5/.35/.25, cap 3), `rebut` (venue must allow; a degree ≥ 2 erases up to 3 of the opponent's tally) | `resolver.py:341-438, 371-373` |
| faults (clinch, immediate loss) | barred device, self-contradiction, evasion × 2 (off-ground or disallowed rebut), silence × 2 (pass or unaffordable) | `primitives.py:262-279` |
| win conditions | ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, PersuasionTrack (`clamp(start + 1.5·(advA−advB), 0, 10)`: ≥9 A_total, ≥7 A_decisive, >3 committee, >1 B_decisive, else B_total), VoteAtClose (a terminal secret ballot: each juror votes A iff `sharpness·(advA−advB) + N(0, noise)` > 0, defaults 0.6 and 0.8, so a close room is near a coin-flip; simple majority, or for the Panel the summed `discipline` weight, which `guild_arbitration` uses; draws on the global `random` stream) | `resolver.py:52-147`; `modes.py:502-509` |
| proceedings (8) | `formal_contest` 3 ex., `grand_contest` 5, `royal_audience` 3, `church_tribunal` 5 (start FACT, track 6.0), `guild_arbitration` 3 (panel vote), `casual_dispute` 1, `private_negotiation` 3, `personal_appeal` 1 | `modes.py:485-519` |
| adjudicators | `expert_judge` (learned, discipline .75, logos .55), `crowd` (15, discipline .30, pathos .55), `no_adjudicator`, `panel` (5 expert judges) | `modes.py:433-468` |

The kernel reads a faculty, draws from the global `random` stream and returns a winner, which is why the season roll
does not use it (`roll.py:19-35`).

## 3 A worked example

### 3.1 A `tell` (season roll, shipped constants)

Odile holds a firsthand claim that a granary holds 40 measures and stands with Bram. Neither has a capability, so pool 2,
opposition `None`, Ob 2, room 0, ceiling 2 → **Ob 2**; S27.4: 2 > 4? no. Two dice produce these nets out of 100 face
pairs: −2:1, −1:10, 0:31, +1:32, +2:19, +3:6, +4:1. Partial needs net 2 (19); Success net 3-4 (7); Overwhelming net ≥ 5
(0); Failure is the other 74. **F .74 · P .19 · S .07 · O .00.**

- *Success:* `news.told` is emitted. Every person present except Odile who does not already hold the triple receives a
  `told_by` claim at Odile's confidence, lowered by refraction (`refraction_gain` 0.5) if he holds a contrary firsthand
  claim (`witness.py:822-870`). `tell` writes no world cell.
- *Partial:* the same, but each hearer's copy of the number drifts: `max_delta = ceil(0.5 × 40) = 20`, so a hearer
  receives 40 ± (1…20), chosen by a hash, never crossing zero (`witness.py:217-230`).
- *Failure:* `news.untold`. The told *content* is not deposited (`witness.py:860`), but witnesses still receive the
  event-kind claim that a telling happened and failed, and their `seen` record of it; only `finding.none` is skipped at
  WITNESS (`witness.py:359-365`; `rosters.yaml:1145`).
- Variants (hypothetical: no realm person holds a capability): if Bram had `copying: 3`, Ob = 1.5, **the same odds**. If
  Odile had `copying: 3`, pool 3: .60/.228/.162/.01.

### 3.2 A `speak` before a favourable bench, then the determination

Ines speaks to the docketed matter of Corvin at her place, where judges J1 and J2 sit. Constructed ledger contents,
shipped formulas:

- **reception.** J1 holds one firsthand claim (weight 1.0, confidence 100/100) of a deed of Ines's that his own pursuits
  value at `deed_term` +0.4 → 0.40. J2 holds one told claim (weight 0.5, confidence 80/100) of a deed valued +0.5 → 0.20.
  reception = **0.60** (`world_q.py:549-606`).
- **proofs.** Ines holds two firsthand claims of Corvin's deeds that Corvin does not hold (1.0 each) and one told claim
  he mirrors (0). proofs = **2.0** (`world_q.py:609-636`). ⚠ This is the unusual case: a deed claim counts only when its
  doer is the opponent (`person_q.py:147-157`), and the doer witnesses his own act through `co_located`
  (`epistemic.py:548-551`), so he normally holds the same (subject, predicate) and the mirror cancels it
  (`world_q.py:635-636`). Proofs survive only where Corvin's own claim has left his ledger (the 200-claim cap, decay).
  In practice proofs are near zero and the room is reception alone.
- **room** = 1.0 × 0.60 + 0.25 × 2.0 = **1.10**. Ob = max(2 − 1.10, min(2, 1)) = max(0.90, 1) = **1.0**; ceiling 2 leaves 1.0.
- **Odds:** F .42 · P .32 · S .25 · O .01 (against .74/.19/.07/0 with no room). Had J2's claim been absent and Ines held
  one proof, room = 0.40 + 0.25 = 0.65 → Ob 1.35, **identical to Ob 2**. A hostile room of −1.0 gives Ob 3, capped back to 2.
- **State written:** none. One of `matter.carried/advanced/held/turned` is emitted and witnessed.

Now J1 determines Corvin. The speech is not an input: J1 rolls pool 2 against Ob 2 → F .74 (nothing; matter stays) ·
P .19 (an `oblige` on Corvin to J1's seat, graded Partial, with `oblige_term`; matter cleared) · S .07 (the same graded
Success, plus J1's held pursuits move by `0.1 × 1 × pursuit_lean(determine, e)`) · O .00.

### 3.3 One bout in the kernel (`church_tribunal`, faculty 6 vs 4, `build_then_close` vs `logos`, `random.seed(7)`)

Venue: budget 5, start ground `fact`, PersuasionTrack from 6.0, judge `expert_judge`. Pools: A `max(5, 15)` = 15 dice at
leverage 0.83; B 11 dice at 0.50. Trace (`t05_bout.py`, §9):

| ex. | A move | gain A | B move | gain B | tally A / B |
|---|---|---|---|---|---|
| 0 | advance ethos @fact | 0.521 | advance logos @fact | 1.573 | 0.521 / 1.573 |
| 1 | advance pathos | 0.584 | advance logos | 1.534 | 1.105 / 3.108 |
| 2 | advance logos | 2.290 | advance logos | 1.438 | 3.395 / 4.545 |
| 3 | support (Reserve 3/12 < 30%) | 0 | support | 0 | 3.395 / 4.545 |
| 4 | advance logos | 2.220 | advance logos | 1.615 | 5.615 / 6.160 |

Check of the first gain: A's ethos landed at degree 2 (Standing ends 5 + 0.8·2 + 0.8 support = 7.4, as the run reports).
venue weight = 0.30 (ethos) × 0.85 (ethos, past) × 1.0 = 0.255; leak = 0.25 + 0.5·0 = 0.25; resonance = 0.75·0.255 +
0.25·0.25 = 0.254; readiness = 0.40 (no standing or room yet); gain = 2.6 × 2 × 0.254 × 0.40 = 0.528 × jitter → 0.521 means
jitter 0.987, inside 0.92-1.08. Close: track = 6.0 + 1.5 × (5.615 − 6.160) = **5.18 → `committee`**. Over 200 seeds the
same pairing gives committee 100, A_decisive 71, A_total 26, B_decisive 3: the stronger speaker who spends two exchanges
on ethos and pathos is outscored early by plain logos before a learned judge, and the track's wide middle band
absorbs the difference.

## 4 What you can do

An act is not one budget point: a lone act costs 1, an extended scene of 2-3 acts costs 2 (§0). "ctl" = attempted / ok,
seeds 0 · 1 · 2, 2 seasons (`ctl/realm_seed*_2seasons.txt`): *attempted* = acts that reached the fold (`d.resolved`,
`resolve.py:375-379`); contested acts refused at their typed precondition never reach it, so I add the refusal counts and
the formed count (`w.acts`) from my own probes (§9). For contested verbs *ok* includes the Failure band (e.g. `speak`'s
`matter.turned`). The prerequisites column gives the typed cell (`requires_typed`).

| verb | who | prerequisites (typed) | contest | by band | writes | realm |
|---|---|---|---|---|---|---|
| `tell` | anyone (`own`) | you hold a claim on `subject`; `to` is with you | `a standing` vs `to` | O/S/P `news.told` (+`confidence.broken` only if you break a confidence circle; none exist at `telling_privacy` 0); F `news.untold` | nothing; WITNESS deposits the told claim | ctl 23/4 · 25/7 · 19/6; +4 admission refusals (s0). Seed 0 bands: S 3, P 1, F 19 |
| `argue` | anyone | `subject` is an uttered Proposition; `to` is with you | `a proposition` vs `to` | O/S hearer's held pursuits move toward yours by 0.1·step of the gap (`person_q.py:593-613`); P `argument.won`, no write; F `argument.lost` | `Person.pursuits` (hearer) | not in ctl; admission refusals 10 (s0), 17 (s1), seed-1 refusals all `exists:Proposition` = 0; `argument.won`/`.lost` 0 |
| `speak` | anyone | `subject` is docketed (not yourself) | `a matter` vs `subject`, bench room | O `matter.carried`, S `.advanced`, P `.held`, F `.turned` | nothing | ctl 3/3 · 0 · 2/2 (seed 0: all three `matter.turned`); seed 0 formed 22 (`w.acts`): 3 resolved, 18 `speech.unheard`, 1 untraced; `speech.unheard` 14 (s1) |
| `determine` | seat granted `determine` | subject is a Person, docketed, you sit on the bench over his home, bench ≥ quorum 1 | `a proposition` vs party | O/S disposal graded + judge's pursuits; P disposal graded Partial; F `matter.undetermined` | `Tenure.since/degree`, `DocketItem.matter`, `Person.pursuits` (judge) | ctl 0 · 1/1 · 0 (seed 1: one `matter.determined` at Partial); `determine.refused` 2 (s0), 5 (s1) |
| `petition` | anyone | `to` is a Person, `from` is a Rung; not to yourself; computed `to` = `subject` (H-94) | none | `petition.filed` | `Record.exists` (petition, your `hold`, +1 budget) | ctl 42/14 · 31/7 · 34/11; seed-1 refusals all `exists:Person` = 0 |
| `carry` | holder of the petition | `subject` is a petition you hold | none | `petition.carried` | `Record.stages`, docket item | ctl 28/0 · 32/0 · 34/0, seed-1 refusals all `exists:petition` = 0 |
| `open_case` | seat granted `determine` | seat's purview reaches the matter's place; matter not already docketed | none | `case.opened`; refusals `case.unauthorized`/`case.refused` | case file, docket item | ctl 12/6 · 2/1 · 9/5 |
| `convene` | seat granted `convene` | venue ranks above the person tier (a hand predicate, `_req_convene`, not a typed cell) | none | `date.scheduled` | `Date.due_at` (+ holder) | ctl 1/0 · — · 5/1 |
| `utter` | anyone | — | none | `proposition.uttered` | `Proposition.exists` (+ your `hold`, so +1 budget) | ctl 39/39 · 39/39 · 49/49 |
| `commit` | anyone | `subject` is a Proposition | none | `commitment.made` | `Tenure.since` | ctl 61/0 · 56/1 · 63/1, seed-1 refusals all `exists:Proposition` = 0 |

`research`, `examine` and `surveil` borrow the same roll with no prize and a forgery term; they are Fieldwork's verbs.

## 5 Pursuing goals here

**(a) Goals and their representation.** The code has no SC goal object. The chooser scores each candidate by the verb's
alignment with the person's value axes and his stance toward the subject, then samples (errata G12); a person's wants are
`Person.pursuits`. What an actor can bring about here is a world state: (1) someone holds a claim (a `told_by` entry in
his ledger); (2) someone wants something else (his pursuits); (3) a matter is before a room (a docket item); (4) a room
has heard it go your way (a witnessed `matter.*` event); (5) a person is bound (a disposal Tenure, graded); (6) a
statement exists that others can commit to (a Proposition, `commit` Tenures).

**(b) Plays.**
1. *Spread news:* acquire a claim (witness, inquire), stand with the person, `tell`. Everyone present hears, not only `to`;
   a hearer who already holds the triple receives nothing.
2. *Change a mind:* `utter` the Proposition first, stand with the hearer, `argue`. Only pursuits he already holds above
   zero move; Success closes 10% of the gap to your weight, Overwhelming 20%.
3. *Complain without a seat:* `petition` (to a person, from your rung) → keep or `give` the petition → `carry` it →
   `speak` to the docketed matter. A verdict still needs a seated judge. Computed, the petition is addressed to its own
   subject (H-94), and in the realm `carry` has never passed admission.
4. *Prosecute from a seat:* hold a seat granted `determine` whose purview reaches the matter → `open_case` → optionally
   `convene` (a separate `convene` remit) so the bench is asked at a sitting → `determine`.
5. *Win the room before you speak:* be the doer of deeds the judges value (reception), and hold claims of your
   opponent's deeds that he no longer holds (proofs, rare: §3.2). You must reach room ≥ 1.0 to change anything.
6. *Widen your own budget:* every live `hold` adds a scene action, and `utter`, `petition` and `open_case` each mint
   one; `utter` never refuses, so it is a reliable budget lever (audit ruling C1).

**(c) Costs, risks, counter-play, blocks.** Each act spends budget (1 alone, 2 per extended scene); at the defaults three in four contested acts
fail, and Failure writes nothing ("no failing forward"). Nothing stops a failed `tell` being formed again in a later scene
at the same odds: the season bars a repeat only of an act already realised (`loop/deliberate.py:305-340`;
`data/verbs.py:1193`), and `tell`'s Failure emits `news.untold`, which is also its refusal kind, so it is not recorded as
realised (`loop/driver.py:488-503`). Seed 0, tick 0: `p_npc_086`'s `tell` to `p_npc_007` drew `news.untold`, then the
same act in a later scene drew `news.told`, so the odds per act understate the odds per intention. You cannot read the
bench's or the opponent's ledgers: the room is resolver-side only (`world_q.py:522-531`), so you guess. In computed play
nobody guesses: decision code never reads the room (`decision/` names `reception` only in a comment,
`decision/options.py:1335`). For `tell`, `argue` and `determine` there is nothing hidden to guess at shipped values: every
realm act rolls pool 2 against Ob 2 (§2.2), F .74 · P .19 · S .07 · O 0 whoever the hearer or party, and only `speak`'s
bench room is unknown. [precedent: `research/game_precedent_suite/dispositions/D_T05.md`, rows 4, 5, 62] Counter-play is structural, not chosen: an opponent who comes
to hold the same (subject, predicate) cancels that proof; a judge who saw someone successfully dominate you discounts
your earlier dominance deeds (route erosion, `world_q.py:572-581`); a bound party may `release` an `oblige`. Realm
blocks: pool 2 and leverage 0 for everyone; formation mismatches (computed `argue`, `commit`, `carry`, and some
`petition`s form on referents of the wrong kind and are refused); no Date was ever written on seed 0, so every docket
item there was dateless.

**(d) What the mechanics structurally reward or punish.**
- `speak` does not change `determine`'s odds: the verdict roll reads no room and no prior speech. As a means to a
  verdict, pleading is dominated; its only product is witnessed events.
- The verdict does not read the party either: `determine` rolls the judge's pool against Ob 2 for every party
  (`verb_table.yaml:346`: *"the roll is the same for every party"*), so a party whose deeds the bench witnessed and one it
  never heard of face the same .26 chance of a disposal. [precedent: `research/game_precedent_suite/dispositions/D_T05.md`, row 18]
- Room below 1.0, and a hearer's capability of 3, are inert (Ob rounds up). Only a teller's capability, a room ≥ 1, or an
  opponent at capability ≤ 2 move odds.
- Overwhelming is unreachable at defaults, so `argue`'s 20% move and `determine`'s top band do not occur.
- A Partial `determine` still binds: 26% of hearings at defaults (P .19 + S .07) open a disposal.
- Quorum 1 cannot refuse a seated judge; a determination moves the **judge's** pursuits, not the party's.
- A hostile room cannot hurt you against a *defaulted* Ob 2 under ceiling 2. Against an opponent holding the
  capability key the base is `score/2`, below 2, and a hostile room raises it up to the ceiling (`roll.py:89-94,
  103-113`). In the realm it is inert only because no one holds a capability.

**(e) What success leaves.** `tell`: told claims (chained to you) that feed others' questions and choices. `argue`: a
hearer whose chooser now scores differently. `determine`: a graded `oblige`/`detain`/`ban` edge from the party to the
seat (the party joins the seat's establishment), the docket slot freed, and a judge whose pursuits hardened. `petition`/
`open_case`: Records and docket items that persist across seasons. `speak`: nothing but the record of who heard it.

## 6 How it connects

- **Fieldwork / information (FI):** claims are what you tell and what proofs count; FI's inquiries use this roll and
  ladder; `forgery_quality` enters only an inquiry's obstacle and is inert under ceiling 2.
- **Governance (GV):** seats, granted remit acts (`determine`, `convene`), purview and the bench all come from Tenures and
  Offices. `determine`'s disposal is a Tenure GV readers see. The chronicle channel is an Event-*kind* filter: any Event whose
  kind appears in the `emits:` of any `binding_decision` row is admitted for everyone alive (`epistemic.py:649-686`,
  opened). So `matter.determined`, `matter.undetermined` and `date.scheduled` are public, and because `determine` emits
  `pursuit.moved`, a won `argue`'s `pursuit.moved` also goes realm-wide. `tell`, `speak`, `petition` and `open_case` kinds
  are on no binding-decision row and reach only the channels that admit them (presence, knot, document).
- **NPC life (NP):** pursuits are what `argue` and `determine` move and what the chooser reads.
- **Factions (FA):** factions are Propositions and `commit` edges; `utter` is the only creator of a Proposition.
- **Economy (EC):** `give` hands a petition to another hand before `carry`.
- **Personal combat (PC):** `fight`/`accept` share the contest dispatcher but route to `the body`; the lexicon proposes
  insult as a duel trigger.

## 7 Playing it as proposed

[PROPOSED] items are intent only (`proposals/2026-10-16-verbs/2026-10-16-verbs-11-lexicon-social-contest.md`, "V11",
status PROPOSED; extract L11). V11 opens with rulings that override its body, and the roster `verbs-03` governs where they
differ (errata G19): `utter` stays (its rename to `declare` is withdrawn, R-06; candidate `propound`), `carry` → `lodge`
is adopted in the rename batch (R-10, still unexecuted at HEAD), `interrogate` is SC's (R-07), `forge` is FI's (R-14),
"challenge a claim" is `dispute` (R-24, no body row).

| suite [PROPOSED] | what you could do | waits on (V11 M-id) | decision id |
|---|---|---|---|
| 1 `tell` | testify, confess, confide, warn, confront, praise, flatter, insult, counsel, deny a rumour, as contents of one `tell` | a valence reader so praise or insult moves anything (M14); teller's standing in the Ob (M10); a proofs reader for testimony/confession (M9) | H-194, H-196, SC-G21, SC-G22 |
| 2 `persuade` (= today's `argue`) | manner `reason` (Ob reads the hearer's claims against the course; he keeps your reasons) or `appeal` (Ob reads his regard; no claim left); `preach` to a set parked | pursuits operand (M16) | H-221, H-62, SC-G34, SC-G43 |
| 3 `utter` | propose (OUGHT), allege (HOLDS), threaten (THREAT), declare war (WAR, FA) | mood source for a computed act (M13); threat reader (M15) | D-V6, SC-G36 |
| 4 `commit` | vote (counted by `determine`), swear an oath (proof `oath`) | cardinality count (M12) | SC-G25 |
| 5 `petition` / `lodge` | accuse; deny and withdraw as `release`; address a petition to someone other than its subject | addressee apart from subject (M3); a denial the petitioner learns (M4) | H-94, D-V3, SC-G03-G05 |
| 6 the sitting | `speak` contents plead, refute, concede, object, define, impugn, each moving a persistent `issue` rung; adjourn keeps the rung; arbitrate; `determine` disposing a Record (parliament, council) | Date holder (M1, built at HEAD); computed-case arrangement (M2: "a killing → `legal_trial`"); Record disposal (M5); `issue` rung (M7); speech-kind reader (M8) | PHASE 2 step 10, H-63, SC-G12-G14, SC-G29 |
| 7 deception | `lie` as a `tell` of an unheld claim emitting `tell`'s kinds; detection through proofs | the ruling and M9 | **J-C-6** (V11's one item for Jordan; recommends yes) |

Remediation items (`proposals/2026-10-21-v9-remediation/`, extract D02) that would change what executes here: REM-23
(`commit` forms only on Propositions), REM-24 (`petition` *forms* only on a Person referent, `referent_class: Person`), REM-25 (`carry` forms only on a held
Record), REM-10 (count admission-refused contested acts as attempts), REM-06 (R-09 needs a non-combat verb at two bands
with differing writes; `speak`'s empty bands no longer count, `determine` is the candidate).

**Stubbed, inert at shipped defaults, or refused in the realm run:** leverage (no producer); `confidence.broken`
(`telling_privacy` 0); quorum (1); the ceiling makes hostile rooms and forgery inert; `determine` at Failure moving the
judge against his axis (H-221, not built); every arrangement key except `disposes`; all six speech kinds; the proofs
roster `record, testimony, oath, confession` (`rosters.yaml:2318`) as a reader; the proceedings design's nested
multi-exchange run inside one act (`roll.py:36-37`); kernel games `consensus`, `negotiation`, `inquiry` and unanimity
(stubs); kernel `stakes`, `resistance`, `roles` and the Doubt Marker (stored, unread).

## 8 Common mistakes and traps

1. **"A favourable room lowers the obstacle."** Only once it reaches 1.0; below that the integer net makes it inert.
2. **"Pleading helps you win the case."** `speak` and `determine` are separate rolls; nothing passes between them.
3. **"`tell` reaches only the person told."** Everyone present who lacks the claim receives the told copy.
4. **"The bench decides whether a date lapses."** CALENDAR lapses a Date with no *holder* (`calendar.py:42`);
   `judging_set`'s docstring line about an empty set does not describe that branch.
5. **"`determine` needs a fired Date."** Its typed cell reads only that the matter is docketed (`verb_table.yaml:322`).
6. **"Two proceeding vocabularies are one."** The kernel's 8 proceedings and the season's 8 arrangements share no names
   and no mapping.
7. **Reading ctl "ok" as success.** For `speak` it counts `matter.turned`, a Failure band.

**Draft appendix A7 corrections:**
- A7 says G20 "does not exist"; it does (`extract/G20_gaps_SC_GV_FI_TW.md`, 59 SC rows).
- A7: arrangements have "14 keys"; the file says thirteen plus `id` (`arrangements.yaml:8-14`), and `quorum`, required
  only for `disposal: declared`, is used by no row (errata C3).
- A7 omits that `open_case` refuses a named arrangement disposing `Record` (`effects_information.py:333-336`), so the two
  Record rows cannot even be docketed (errata C3).
- A7 cites H-221 at `verb_table.yaml:146`; the text is at `:155` (errata C3).
- A7 grades `argue`/`determine` from the refusal counts; under errata G1 the evidence is `argument.won = argument.lost = 0`
  (seeds 0-2), and `determine` did execute once on seed 1 (`matter.determined`, Partial), so "TESTS-ONLY in practice" holds
  for seed 0 only.
- A7 says `determine` requires "a fired Date with a DocketItem"; the date is not checked (trap 5).
- A7 (and L11) list a Date holder as missing; at HEAD `_eff_convene` sets `holder` to the convener's seat
  (`effects_governance.py:370`).
- A7 calls V11's R-06/R-07/R-14/R-24 "internal contradictions … unresolved"; the rulings override the body (errata G19).
- A7 presents "1 of 430" as a quotation; it paraphrases `rosters.yaml:1223-1224` (errata C3).
- The control run under-counts contested attempts refused at admission (e.g. `speak` 3 in ctl vs 22 formed on seed 0);
  A7's figures for those refusals are right, and the ctl file is right for non-refusal outcomes.
- A further trap: the remit roster is internally contradictory. `rosters.yaml:314` calls the remit acts "the CLOSED five
  … plus `convene`" while `:315` sets `open: true` (`verb_table.yaml:801` also says "a CLOSED roster"). `determine` and
  `convene` are on it either way.

**§8 Round-2 corrections** (audit2; each cited line opened before accepting):
1. *F1 / X4 grades per seed.* My §0 said `commit` and `convene` were refused every time. Wrong: ctl shows `commit` ok 1 on
   seeds 1 and 2, `convene` 1 of 5 on seed 2. §0 now grades every SC verb per seed; only `carry` (and `argue`) never execute.
2. *X1 / C1 scene budget.* "Every act costs one action" was wrong: an extended scene of 2-3 acts costs 2
   (`fixtures.py:489`, `choose.py:643-657`), so budget 5 buys 7 acts. Fixed in §0, §4 and §5c, and I added play 6 (hold-minting
   verbs raise the budget).
3. *F3 proofs.* Accepted after opening `person_q.py:147-157`, `epistemic.py:548-551`, `world_q.py:635-636`: the opponent
   normally witnesses his own deed and so mirrors it; §3.2 and play 5 now say proofs are near zero in practice.
4. *F5 Failure deposits.* "Nothing is deposited" was wrong: `news.untold` still deposits event-kind and `seen` claims
   (`witness.py:359-365`); only the told content is withheld (`:860`).
5. *F8.* The per-act generator is at `resolve.py:792`, not `:806`.
6. *F9 / H-94.* Added: a computed petition is addressed to its own subject (`verb_table.yaml:941`).
7. *F11 hostile room.* My "a hostile room cannot hurt you" holds only against a defaulted Ob 2; against a capability
   holder the base is below 2 and a hostile room raises it (`roll.py:89-94, 103-113`). Corrected in §5d.
8. *F12 capability.* The `copying: 3` person is in the case-corpus overlay, never in a realm build; variants relabelled.
9. *F13 sitting question.* `sittings_before` checks subject, predicate and tick, not source (`world_q.py:301-302`); its
   docstring's "firsthand" is not enforced. §2.3 corrected.
10. *F14 kernel leverage.* `Leverage.net` adds 0.5 only on-ground (`primitives.py:228-230`). My figure stands for every
    *rolled* move, because the resolver always passes `on_ground=True` (`resolver.py:301`) after an off-ground advance has
    already returned as an evasion (`:380-381`). Stated both ways in §2.4.
11. *F15.* REM-24 is a formation change (`referent_class: Person`), not a binding change. Fixed in §7.
12. *Chronicle (OBS, C5, X17).* Opened `epistemic.py:649-686`: an Event-kind filter over every `binding_decision` row's
    `emits`. So `pursuit.moved` from a won `argue` is public too. §6 rewritten; no longer "not confirmed". (The function's own
    docstring still says the channel "matches NOBODY" in one paragraph and is re-measured lower down; the code governs.)
13. *X3 / C10 typed cells.* §2.1 and §4 now say admission reads `requires_typed`, and name the untyped halves (`speak`'s venue,
    `determine`'s date). `convene` has no typed cell: its precondition is the hand predicate `_req_convene`.
14. *X19.* Run columns are attempted/ok throughout; §4 now defines both (attempted = reached `d.resolved`).
15. *X21.* Seed-0 `speak`: 22 formed (`w.acts`, my run), 3 resolved, 18 `speech.unheard`; the 22nd is untraced. My earlier
    "21" counted events, not acts.
16. *C11.* Added one-clause definitions of the shared primitives and id families in §0.

### Round-3 corrections
Each line is old claim -> new claim, with the evidence. Round 3 read the code at `51d7b05`; the precedent record is
`research/game_precedent_suite/dispositions/D_T05.md`.
1. *§0 (B), D_T05 row 12 / 74.* "a tested laboratory that the season loop never calls" -> also the repo's one human-played social
   contest, `agon_harness.py`, unreachable from the season (`agon_harness.py:148-155, 323-345`; no `.py` imports it; ran it four times
   with scripted input: 9 prompts over 3 exchanges each time, `A_decisive` x3, `committee` x1). New §0a section.
2. *§2.4 win conditions, row 27.* "VoteAtClose" named without its rule -> the ballot is stated (`resolver.py:98-147`, defaults
   `sharpness` 0.6, `noise` 0.8, `random.gauss`; Panel weights by `discipline`; `modes.py:502-509` binds it to `guild_arbitration`).
3. *§2.3, row 75.* "a matter is whatever a docket item names (in practice a person)" -> a person or a Rung that is no person; `determine`
   needs a Person (`verb_table.yaml:327-328`). Evidence: seed 0 docket after tick 0 is `terr_T13`, `p_npc_038`, `b_s_001_court`; 2 of
   its 6 `case.opened` over two seasons name a territory or building (re-run at `51d7b05`).
4. *§5c, rows 4 and 62.* "so you guess" -> in computed play nobody guesses (`decision/options.py:1335` is the only mention of
   `reception` under `decision/`); at shipped values `tell`, `argue` and `determine` have no hidden odds (`verb_table.yaml:346`,
   `sigma.py:119-131`).
5. *§5c, row 5.* "Failure writes nothing" with no word on repeats -> a failed `tell` can be formed again at the same odds: the season
   records only realised acts (`loop/deliberate.py:305-340`, `loop/driver.py:488-503`) and `tell`'s Failure kind `news.untold` is also its
   refusal kind (`verb_table.yaml:1196, 1240-1243`). The disposition says "a failed act"; I scoped it to `tell` because other rows'
   Failure kinds (for example `matter.turned`) are not refusal kinds and I did not trace what that does for them.
6. *§5d, row 18.* New bullet: `determine` reads neither the party nor the room (`verb_table.yaml:346`); .26 for every party.
7. *Line drift after #494.* Citations to `queries/world_q.py` +3 (every cite here sits after line 44), `queries/person_q.py` +2 below line
   416 and +90 above it, `data/fixtures.py` +10 above line 715, `data/rosters.py` +1 (`git diff a4ca9a5 51d7b05 -U0` on each; the text at
   every re-based range is identical to the old one). Re-based: `world_q.py` 530-540/546-603/606-633/179-210/232-302/439-516/244-266/
   286-287/298-299/269-302/458-468/632-633/519-528/569-578 -> 533-543/549-606/609-636/182-213/235-305/442-519/247-269/289-290/301-302/
   272-305/461-471/635-636/522-531/572-581; `person_q.py` 480-523/503-523 -> 570-613/593-613 and 145-155 -> 147-157; `fixtures.py`
   761/864/913 -> 771/874/923; `rosters.py` 841 -> 842. §9's Opened/Ran lists are left as the `a4ca9a5` record.
8. *Not applied, by instruction.* The overview edits (player interface, player-position row) and the nine bracketed corrections to
   repo precedent documents belong to other files; they are in `D_T05.md` rows 30-40, 71-74.

## 9 Checks

- Opened: `modules/social_contest/roll.py:1-125`; `seam/wrappers/sigma.py:80-278`; `verb_table.yaml:108-369, 900-964,
  1068-1095, 1169-1202`; `rosters.yaml:1206-1231, 1299-1325`; `data/fixtures.py` lines 247, 391, 414-433, 761, 853, 864, 913;
  `data/rosters.py:835-842`; `queries/world_q.py:179-302, 439-633`; `queries/person_q.py:464-523`;
  `loop/effects_information.py:273-631`; `loop/effects_governance.py:326-370`; `loop/calendar.py:28-75`;
  `loop/witness.py:136-230, 570-600, 815-905`; `loop/resolve.py:765-830`; `dice_engine.py:153-161, 227-240`;
  `arrangements.yaml:1-122` and the `disposes` lines; `decision/budget.py:50-61`; kernel `primitives.py`, `resolver.py`
  (constants, `resolve`), `policy.py`, `wrapper.py:110, 180-264`.
- Ran (`python -I`, scratchpad scripts, tree unchanged by `git status`): `tutorial/t05_odds.py` (odds table, room and
  argue arithmetic: Success moves {wealth .8 → .74, faith .2 → .27} toward {.2, .9}); `tutorial/t05_bout.py church_tribunal
  7 6 4 build_then_close logos` (trace and 200-seed tally); `tutorial/t05_rv.py` (all SC verbs except `construe` are in
  `resolvable_verbs()`); `tutorial/t05_kinds.py 0|1`, `t05_ref.py`, `t05_obs.py 1` (event kinds, bands, refusal
  observations, docket and date counts on `build_realm(seed)`, 2 seasons). Execution counts in §4 are from `ctl/`.
- Round 2: opened `epistemic.py:548-551, 649-686`, `person_q.py:145-155`, `witness.py:355-367, 856-862`,
  `resolver.py:301, 376-406`, `primitives.py:225-230`, `budget.py:17-20`, `fixtures.py:486-490`, `choose.py:643-657`,
  `rosters.yaml:313-317`; ran `tutorial/t05_acts.py 0` (formed vs fold-reaching counts: tell 27/23, speak 22/3, argue
  10/0, determine 2/0, petition 42/42, carry 28/28, open_case 13/12, convene 1/1, utter 40/39, commit 64/61).
- Round 3 (2026-10-22, `51d7b05`): opened `agon_harness.py:1-160, 313-530`, `resolver.py:95-150`, `modes.py:480-560`,
  `verb_table.yaml:314-346, 1068-1092, 1193-1246`, `loop/deliberate.py:215-230, 305-375`, `loop/driver.py:440-560`,
  `loop/calendar.py:36-76`, `data/verbs.py:1193-1235`, `rosters.yaml:2494-2534`, `queries/world_q.py:519-534, 1764-1795`,
  `harness/play_surface.py:30-60`; ran `yes 1 | python3 -m systems.social_contest.sim.contest.agon_harness` (4 complete runs),
  a one-season `build_realm(0)` probe on the `ctl/control.py` recipe (formed/reached `tell` 3/3, `speak` 9/2, `argue` 2/0,
  `determine` 1/0, `petition` 22/22, `carry` 12/12, `open_case` 8/7, `convene` 1/1, `utter` 18/17, `commit` 39/36; docket after
  tick 0: three dateless items) and a two-season probe of seeds 0, 1, 2 for the docket and the subjects of `case.opened`.
  Those probe scripts are not committed.
- Not confirmed: the one seed-0 `speak` formed but producing no `speak` event; `reception`'s
  `deed_term` values in §3.2 are constructed inputs, not read from a realm ledger.

