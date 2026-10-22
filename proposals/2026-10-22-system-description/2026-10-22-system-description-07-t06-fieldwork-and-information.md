# Tutorial: Fieldwork, investigation and the information model — how a person comes to know, hide, plant and spread what happened

Repo HEAD `a4ca9a5`; revised in round 3 against `51d7b05` (after PR #494) and the precedent suite
(`research/game_precedent_suite/`); the round-3 changes are listed in `### Round-3 corrections`, before
§9. Paths are relative to `/home/user/ttrpg`, except that a path with no directory prefix or starting
`harness/`, `loop/`, `decision/`, `queries/`, `state/`, `seam/` or `data/` is under `engine/season/`
(`modules/...`, `systems/...`, `engine/dice_engine/...` and `proposals/...` are repo-root). "Ctl" means the control run files
`proposals/2026-10-22-system-description/ctl/realm_seed{0,1,2}_2seasons.txt` (seeds 0-2, two seasons). Every run column reads
**attempted/ok**:

- *attempted* counts acts that reached the fold (`d.resolved`): `_fold` appends the act on entry
  (`loop/resolve.py:377-379`), before its own admission check (`:428-430`). The three graded inquiries and the
  contested verbs are admitted before the fold (`:1012-1032`), so their admission refusals are not counted.
  For every other verb the admission refusal is counted (seed 0: interview 21 of 32 and reconstruct 6 of 39
  attempts were refusals; restore 23 attempted, 0 ok). Also left out: acts whose actor was already gone, and
  refusals for an obstacle too high for the pool (`:974-998`).
- *ok* means at least one Event that is not a refusal. For a graded inquiry that means Partial or better.

"Probe" means a read-only script I ran for this tutorial (§9). The scripts are not committed, so a figure
marked probe is an uncommitted round-3 probe figure; ctl is the only committed instrument. Times are given as **ticks** (one tick per
season; the first MATTER runs at tick 0), not as "season N".

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that spends a
**scene-action budget** each season on verbs from a closed table. The budget is
`max(1, 5 + 1 per live hold − body bands − 1 per travel leg)` (`decision/budget.py:19-20,57-61`), where a
*hold* is a Tenure (a stored relation edge) saying you have a seat, a landholding, a Record or a
Proposition.

- A scene of one act costs 1. A scene of up to `interactions_per_scene = 3` acts is "extended" and costs
  `extended_scene_cost = 2` (`fixtures.py:488-489`; `decision/choose.py:643-657`).
- The driver releases at most one scene per round, over 5 rounds (`loop/driver.py:456`).
- So budget 5 buys 2+2+1 = 7 acts, and budget 6 buys 9. Seed 0 shows about 7.6 acts per person per
  season (basis: 1,132 resolved acts / ~74 persons / 2 seasons).

"You" in this tutorial is the person acting: a player's character if one is ever seated, an NPC today.
So the tutorial teaches three things: what a person can do, what the rules do with it, and what a person
has to arrange to reach a goal.

**What this subsystem is.** Two layers that cannot be pulled apart:

1. **The information model (WITNESS).** Truth is one Event log. Belief is a per-person list of Claims
   (the *ledger*). Only the WITNESS barrier writes a ledger. Every subsystem's outcomes reach people
   this way and no other.
2. **Fieldwork (FI).** These are the verbs a person uses on that model on purpose: six *inquiries*
   (`examine`, `interview`, `research`, `surveil`, `thread_read`, `reconstruct`), the document makers
   (`survey`, `forge`, `conceal`, `create_record`), and the carriers `give` and `tell`.

**What you need from other subsystems.** The social-contest roller (`modules/social_contest/roll.py`)
grades three of the inquiries, and it also grades `tell`. Factions (`faction_q.resolve`) supply what a
survey or a forgery says. MATTER supplies decay and stage maturation, which is how covers lapse. The
decision layer (`questions_for`, `opening_set`) turns your claims into your next choices.

**Status, with grades** (the grade rule is the errata's G1):

| part | grade |
|---|---|
| WITNESS fan-out, refraction, decay, cap and eviction | RUNS-IN-LOOP |
| `co_located`, `chronicle` and `document_key` channels | RUNS-IN-LOOP |
| `witness_key` channel | TESTS-ONLY: it admitted nobody in seeds 0 or 2 (0 `firsthand_via_knot`) |
| `post_remit` slot (the obligee channel and IN-22 seat reports) | RUNS-IN-LOOP through the obligee channel (errata Part 3 R-13): at tick 0 the King's obligee p_npc_070 holds an `inferred` claim of a refused royal act in seeds 0, 1 and 2 (uncommitted round-3 probe). Seed 0's end-of-run count of 0 `inferred` is a survival count, not an absence: p_npc_070 dies at tick 1 there. Test: `engine/season/tests/test_obligees.py:167` |
| the inquiry rolls, `survey`, `forge`, `conceal`, `create_record`, `tell` | RUNS-IN-LOOP |
| what an inquiry uncovers (the found deposit) | TESTS-ONLY: 0 found deposits in seeds 0, 1 and 2 (uncommitted round-3 probe) |
| `give` | 0 of 16 in seed 0; 1 of 19 in seed 2 (a cover changed hands) |
| told drift and private circles | Partial drift TESTS-ONLY in effect; circles are RUNS-IN-LOOP at control (`telling_privacy=0`) |
| `systems/fieldwork/sim/knots.py` | TESTS-ONLY (unplugged) |
| `destroy_record` | TESTS-ONLY. The row is typed and has an effect (`verb_table.yaml:292-313`; `effects_information.py:969`), so a hand-built act executes, but formation is withheld by fixture (`fixtures.py:933`) |
| `thread_read`, every proposed verb | DESIGN-ONLY |

`engine/season/requirements.yaml:169-172` lists the scale "investigations / detective / interactive
fiction" as `in_loop: false`. The verbs run, but there is no playable investigation mode.

## 0a How it plays

Round 3. As built first, then a `[PROPOSED]` block. "T06 precedent" is
`research/game_precedent_suite/tutorials/T06_investigation.md` (Obra Dinn, Shadows of Doubt, Pentiment,
L.A. Noire), "T19 precedent" is `.../T19_tactics_narrative.md` (Lacuna, Ace Attorney), "D_T06" is
`research/game_precedent_suite/dispositions/D_T06.md`; their tags (`[V3]`, `[M]`, `[CONTESTED]`) stay there.

### How it plays (as built)

**Setup choices.**
- World build: `build_realm(seed)` seats the same 83 persons, 322 Sites and 412 Rungs at seeds 0, 1 and 2;
  the seed changes the draws, not who exists (uncommitted round-3 probe). Nothing in the information model is chosen per world.
  Shipped: `refraction_gain 0.5` (`fixtures.py:874`), `claim_decay_per_season 5` (`:293`), `told_weight 0.5`
  (`:788`), `record_gain 0.5` (`:801`), `telling_privacy 0.0` (`:863`); inquiry pool 2, obstacle 2, ceiling 2
  (§2.8).
- No person has a background that changes what he can learn: no `VERB_CAPABILITY` row names an inquiry
  (`rosters.yaml:1229-1231`), so every investigator rolls `pool_default` 2 whatever his capability (§2.8);
  capability is also empty on every realm person (ctl "capability nonempty 0"). `[precedent: T06 precedent,
  Pentiment §1: a biography per act unlocks lines and points]`.
- The season loop has no player interface. The one seam is `dispatching_chooser`
  (`harness/play_surface.py:14-16,41-51`, tests only): it sends the choosing of each person named in
  `overrides` to a callback that receives the person, a View, a Sensation, the budget query and `auto` (the
  delegate chooser), not the World (`loop/deliberate.py:119-170`).
  The callback may return any of the 47 resolvable verbs (`loop/driver.py:101`) with any payload, so it can do
  what the chooser never does: `examine` a Site he stands at (hand-built, it reached the roll; probe; the
  graded `examine` is also exercised by `engine/season/tests/test_fi01_graded_inquiries.py:223-239`) or `give`
  a forged sheet. Elsewhere `systems/social_contest/sim/contest/agon_harness.py`
  is a stdin-driven human-played social contest, and the combat and mass-battle `workbench/server.py` files
  are HTTP designer tools; none plays an investigation.

**The loop.** One season, every person, all of it automated (overview §2.1; §2):
1. MATTER takes 5 confidence off every claim (`loop/matter.py:317-347`) and matures Record stages, so covers
   lapse after about three seasons (§2.10).
2. Five rounds (`loop/driver.py:449-456`). DELIBERATE: claims that landed since a person's last deliberation
   raise questions, ordered by `attention_key` (`queries/world_q.py:2217`; `questions_for` at `:2374`);
   candidates form on the question's referent; his ledger vetoes what it knows false
   (`decision/options.py:308-309`); he packs scenes from his budget (7 acts at budget 5, §0).
3. RESOLVE: the graded inquiries roll 2d10 against Ob 2 (Failure 0.74, Partial 0.19, Success 0.07; §2.8) and
   nobody is shown these odds (overview §7, information row). Refusals and Failures emit `finding.none`. A
   graded finding on an open trail returns `(event, terms)` (`modules/fieldwork/find.py:28-34`, through the
   `inquiry` role, §2.9). `[precedent: T06 precedent, Pentiment §7: its check is shown as triangles at the
   moment of choice]`.
4. WITNESS: each Event reaches each person through the first channel that admits him, refracted
   (§2.2-2.4); found claims land at 50; a telling lands at the teller's confidence with the chain extended
   (§2.5); a ledger over 200 evicts (`state/ledgers.py:17-32`).
5. The next round's questions come from what just landed. No one is ever asked to state a conclusion.

Outside the loop, `harness/chronicle.py` (IN-37, PR #494) prints the deepest cross-person act chain of a
finished log. It reads acts and Events, not ledgers, and the loop never imports it.

**The choice menu.** Every act spends scene-action budget: 1 as a lone scene, or a share of an extended scene
costing 2 for up to 3 acts (§0; errata Part 2 C1). Run figures: ctl attempted/ok, seeds 0 · 1 · 2. Grades
per part are in §0 (status table); per-verb prerequisites and refusal causes are in §4. Where this summary
differs from them, they govern.

| verb | cost | effect | when a person picks it | grade (ctl) |
|---|---|---|---|---|
| (be present) | none | firsthand 100 with `who` on everything in the room | always: it is where he is | RUNS-IN-LOOP |
| `research` | one act of a scene | graded; uncovers a forged Record's trail if one is open | formed on the question's referent, which must be a Record to pass admission; about 108 formed acts in seed 0 are refused there (§4) | RUNS-IN-LOOP 14/7 · 8/1 · 4/2; 0 found deposits |
| `surveil` | one act of a scene | graded; a Rung he stands in; no Person case | a question about the place he is in | RUNS-IN-LOOP 30/5 · 29/9 · 22/5 |
| `examine` | one act of a scene | graded; a Site he stands at | formed on the question's referent, never a Site in 160 formations (uncommitted round-3 probe); fix tracked as REM-22 (§4) | TESTS-ONLY 0/0 (62 / 59 / 39 formed, all refused); test `engine/season/tests/test_fi01_graded_inquiries.py:223-239` |
| `interview` | one act of a scene | ungraded `finding.made`; reads nothing from the interviewee | a question about a person | RUNS-IN-LOOP 32/11 · 16/2 · 39/11; uncovers nothing |
| `reconstruct` | one act of a scene | ungraded; uncovers nothing | a held claim on the subject | RUNS-IN-LOOP 39/33 · 52/46 · 55/49; uncovers nothing |
| `survey` | one act of a scene; +1 budget while held | a true faction sheet in his hold | a held claim; the subject coheres under one faction | RUNS-IN-LOOP 57/13 · 38/5 · 59/13 |
| `forge` | one act of a scene; +1 budget | a sheet naming him head; `forgery_quality 1`, capped away | as `survey` | RUNS-IN-LOOP 52/12 · 51/6 · 57/15 |
| `conceal` | one act of a scene; +1 budget | a cover: later deposits are about the alias; `who` still shows | any time | RUNS-IN-LOOP 19/19 · 34/34 · 28/28 |
| `create_record` | one act of a scene; +1 budget | a `text` Record in his hold | any time; the cheapest budget lever | RUNS-IN-LOOP 87/87 · 88/88 · 89/89 |
| `give` | one act of a scene | moves a held Record and its content to a person with him | a question naming a Record he holds (formed mostly on persons and buildings) | TESTS-ONLY at seeds 0-1 (16/0, 21/0); executes at seed 2 (19/1, a cover) |
| `tell` | one act of a scene | contested; the hearer copies his best claim with him in the chain | a held claim; the hearer with him | RUNS-IN-LOOP 23/4 · 25/7 · 19/6 |

**First season, step by step** (seed 0, tick 0; a read-only probe of one season on the ctl recipe; uncommitted
round-3 probe, figures listed in §9).
1. Every ledger starts empty (83 persons, 0 claims). p_npc_037, the season's busiest fieldwork actor (nine
   acts; the next two have seven), holds 0.
2. He takes nine fieldwork acts. Five are `research`: on the King (p_npc_020), on p_npc_030 and three times
   on the cathedral building. None names a Record, so all five are refused at admission; each spent budget
   and left nothing in any ledger, his own included (`rosters.yaml:1145`). Three are `create_record`: each
   mints a `text` Record into his hold and adds 1 to his next budget (`decision/budget.py:57-61`). One is
   `reconstruct` on the cathedral: `finding.made` with no degree; it uncovers nothing, and everyone in the
   room now holds a claim that he asked.
3. Meanwhile WITNESS fills his ledger from where he stood: 0 to 187 claims, 177 firsthand and 10 `told_by`
   at 67 (`order.given`, `tenure.closed` and the `seen` claims about them; the realm mean is 68.3 claims per
   ledger: 5,329 claims over the 78 persons alive after the season). Everything
   he learned came from presence and those 67-grade copies; his inquiries uncovered nothing.
4. Realm-wide that season: `research` formed 59 and reached the roll twice (both Partial, both by cohorts,
   on a Record); `surveil` formed 28 and reached the roll 14 times (1 Partial, 13 Failures); `examine` formed 30,
   refused 30; `forge` formed 21 and minted 4 sheets; `give` formed 8, refused 8, so no forged sheet changed
   hands; `tell` formed 3 and landed 2. Nothing uncovered a trail (0 found deposits); the only route that does is the hand-built
   forge, give, research chain of §3, which the realm does not take.

**What changes later.** Ledgers fill: 13 of 74 at the cap after two seasons in seed 0, mean 199 of 200 after
four (ERRATA C9). Eviction then removes old firsthand claims first (§2.6). Covers lapse after about three
seasons. Held Records keep raising budgets. No verb unlocks and no inquiry gets stronger.

**Failure and ending.** No failure state and no case to fail (§5a). A failed or refused inquiry leaves nothing
in any ledger. A Partial finding closes that trail to its finder for as long as the claim stays in his ledger
(`epistemic.py:356-365`). The season now reports `endings` and halts on none (`loop/driver.py:515-518`,
`queries/world_q.py:1764`); at seed 0 both seasons report `[]` (probe), and `rosters.yaml: endings` calls its
sovereignty row unreachable in computed play. `[precedent: T06 precedent, Obra Dinn §6: it cannot be failed
either, a wrong entry costs nothing beyond staying out of the lock, and it ends on a count of fates solved;
here a Partial closes that trail until its claim is evicted from his ledger (`epistemic.py:356-365`; `state/ledgers.py:24-32`). Shadows of Doubt §6: a wrong name costs 100 and the killer keeps
killing]`.

**Consequential vs cosmetic choices.**
- Consequential: where a person stands (firsthand 100 with `who`, against an inferred 50); what he holds (it
  gates `tell`, `survey`, `forge`, `reconstruct`); whether his act's kind is one a binding row emits
  (chronicle) or is done through a seat (`post_remit`); a `conceal` before acting (the alias); whom he tells,
  since a teller's record re-weights his word (TESTS-ONLY at seed 0, where all 4 tellings were deduped,
  `engine/season/tests/test_told_by_channel.py:1363`; untested at seed 1, where 7 tellings were not traced; one
  chained claim alive at seed 2; §2.5).
- Inert at shipped values: `forgery_quality` (capped), capability (empty), `telling_privacy` (0), `Seen.why`
  (always None, `epistemic.py:932-938`).
- Inert for other reasons: `examine` never passes admission (the operand is filled with a non-Site referent,
  §4), and `interview` and `reconstruct` uncover nothing by construction (no degree, so no `finding_terms`
  row; §5d).
- Dominant: presence over inquiry; `create_record` as a budget lever (§4, §5d).

### How it plays [PROPOSED]

Nothing below executes. Sources: IN-47 (`proposals/2026-10-07-character-sheet-spaces.md` §2 arm C1 `:88-90`,
§4 `:162-185`; to be built by REM-30, `proposals/2026-10-21-v9-remediation/2026-10-21-v9-remediation-02-items-rb0-to-rb3.md:559-568`;
IN-47 is unbuilt, appearing only in a `blocks` list at `requirements.yaml:818`. D-2 RULED that the build
proceeds; keeping the design PROPOSED is an [ASSUMPTION; medium; Jordan to correct], same file `:552-555`); IN-46 (REM-31, same file `:570-589`: a paused
fight, no investigation content); the fieldwork lexicon's M1-M10 (§7).
- Setup: a player takes a person the world builder already seated (IN-47 arm C1) and reads his case from the
  ledger the loop already writes ("unknowns stay unknown, false beliefs stay believed",
  `character-sheet-spaces.md:180-181`), with an out-of-sim chronicle rendered over `causes[]` (`:171-175`).
  That is the Obra Dinn book (T06 precedent, Obra Dinn §2) or the Lacuna phone log (T19 precedent, Lacuna
  §2) made from claims instead of authored clues.
- Loop: unchanged; the player's choice enters at the chooser slot (`season(self, choose, ...)`,
  `loop/driver.py:370`, called at `loop/deliberate.py:170`; REM-30's `loop/driver.py:355` is stale at HEAD)
  through his own View, Question and Candidates.
- Choice menu: every inquiry yields a selected fact at remove 0 (M1); a refusal says so (`inquiry.refused`,
  M2: the precedents' completeness hints, Obra Dinn's blurred face, T06 precedent Obra Dinn §4 step 8 (`:53`),
  and L.A. Noire's music stopping, L.A. Noire §2 step 2 (`:248`)); a Failure can mislead (M3); the hider's skill sets the obstacle
  (M4); the interviewee answers by his own act next season (M5); `watch` can unmask a cover (M1, M4); a
  finding can be brought as a proof (M9). Each waits on the item §7 names.
- Still absent, by axiom: a verifier of the player's conclusion (AX-7;
  `proposals/2026-10-03-verb-coverage-and-gap-fill.md:787-788`), a standing counter-intelligence task (T-i;
  same file `:819`), an intelligence meter (T-a; `:820`). Of the four T06 precedents it would sit nearest
  Pentiment (no truth check, consequence only; T06 precedent, Pentiment §7), over a simulated truth that
  Pentiment lacks.
- Failure and ending: nothing in the loop halts on an ending. IN-27 is built only as the report above, and
  `endings_reached` says the realm as built reaches none.

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| Event, log | what happened (truth): kind, causes, changes, degree | append-only | `state/carriers.py:232` |
| Rung | a node of the containment tree: a place, a holding, or a person's own rung | — | `state/carriers.py` |
| Site | a built thing at a Rung, with an integer `condition` that gates verbs; a different carrier from a Rung and from a Record | kinds in the realm: dwelling, harbour, seam, garrison; 322 at build | `state/carriers.py:737` |
| cohort | a Person at `weight > 1`, standing for the people of one populated rung; a named individual has weight 1 | rows authored in `cohorts.yaml` | `state/carriers.py` (`Person`); `cohorts.yaml` |
| View, Sensation | the chooser's two person-side inputs besides the budget query: a View holds ids (`holder`, `claim_ids`, `question`), never references; a Sensation is the only bridge from world truth into `choose` | — | `state/carriers.py:435`, `:388` |
| Tenure | a stored relation edge (`hold`, `commit`, `oblige`, `knot`, …) with `since`/`until` | live while open | `state/carriers.py:77` |
| Proposition | an immutable uttered statement with a mood (default `OUGHT`); `utter` makes one | never edited | `carriers.py:849`; `effects_information.py:1001` |
| Office, purview, establishment | a seat; the places it reaches; the people attached to it (who the `post_remit` channel admits) | — | `epistemic.py:563-646` |
| stratum | a verb's resolution-order band (`social`, `uncontested_material`, `binding_decision`…); the `seen` term `stratum` reports it | — | `verb_table.yaml` per row |
| prize | what a contested verb is contested over (`tell`: "a standing"); inquiries have none | — | `verb_table.yaml:1186` |
| `with` | the typed relation "the other person stands where you stand" | — | `data/requires.py` (REQUIRES_STEMS) |
| Claim | one belief held by one person: `holder, subject, predicate, value, when, source, confidence, visibility, round, chain, doer` | `confidence` is an integer, default 100 | `state/carriers.py:291`; `data/fixtures.py:247` |
| ledger | `Person.ledger`, the person's list of Claims. Only WITNESS writes it | cap 200 | `data/fixtures.py:231` |
| event-kind claim | `(subject, e.kind, True)`: "this happened to/by subject" | subjects by `claim_subject_rule="both"` (the anchor plus each changed thing, minus a hidden actor) | `epistemic.py:185`; `fixtures.py:512` |
| `seen` claim | a Claim whose value is a `Seen(stratum, marks, who, why)`. `None` means the channel withheld that term | `who` = the act's actor; `marks` is always `()`; `why` is always `None` | `epistemic.py:874,901-932` |
| content claim | `content:<kind>`: what a Record you newly hold says, frozen | one per newly held Record | `loop/witness.py:68-83` |
| source | how the claim came to be held: `firsthand`, `told_by`, `inferred`, `firsthand_via_knot` | fixed by the channel | `rosters.yaml:419-434` |
| chain, hops, teller | who passed it on (origin first); `hops = len(chain)`, `teller = chain[-1]` | empty for anything that was not told | `state/carriers.py:337-379` |
| visibility, circle | `"own"`, or `(teller, addressee)` for a confided telling | circles form with probability `telling_privacy = 0.0` | `fixtures.py:863`; `witness.py:108-133` |
| witness channel | a rule deciding whether a person learns of an Event; precedence order `co_located, witness_key, document_key, chronicle, post_remit` | one channel per person per Event (the strongest one) | `rosters.yaml:419`; `epistemic.py:794-840` |
| remove | how far a channel is from seeing the thing | 0, 1/3, 2/3, 2/3, 1 | `decision/options.py:1338-1353` |
| refraction | received confidence = `int(conf·(1−g·remove)·(1−g·dissent)+0.5)` | `refraction_gain g = 0.5`; competence factor fixed at 1 | `options.py:1410-1448`; `fixtures.py:874` |
| dissent | 1 if the incoming claim contradicts your own firsthand claim about yourself or about a cell, or your ledger makes the reported act impossible for its actor | 0 or 1 | `options.py:1365-1407` |
| decay | MATTER takes 5 confidence off every claim each season, floored at 0 | `claim_decay_per_season = 5` | `loop/matter.py:317-347`; `fixtures.py:293` |
| eviction | while a ledger is over the cap, drop the claim with the lowest `confidence × (when+1)` | cap 200 | `state/ledgers.py:17-32` |
| Said | what a `tell` carries, copied from the teller's ledger when he chooses | best non-`seen` claim on the subject | `carriers.py:369`; `queries/person_q.py:999` |
| teller weight | weight given to hearsay when it is read: `told_weight^hops × relation × record`, clamped to [0,1] | `told_weight = 0.5`; `rank()` always 0 | `options.py:1513`; `fixtures.py:788` |
| Record | a world-side document: `kind`, `subject_matter`, `stages`, `forgery_quality` | kinds seen in the realm: `text`, `faction_sheet`, `cover`, `petition`, `dispensation` | `carriers.py:751` |
| hold | a `hold` Tenure: who has a Record. Each live hold also adds 1 to your scene budget | one live holder per Record | `effects_information.py:170-196`; `budget.py:57` |
| `_mint_document` | the one function that makes a Record and opens the maker's hold | 3 stages, one season apart (`record_stages_default=3`, `record_stage_term=1`) | `effects_information.py:170`; `fixtures.py:524-525` |
| faction sheet | a frozen snapshot of `faction_q.resolve`: `proposition, members, holdings, seats, head` | written by `survey` and `forge` | `effects_information.py:635,704` |
| `forgery_quality` | a forgery's grade; it is added to an inquiry's obstacle | `default_forgery_quality = 1`; the obstacle ceiling is 2 | `fixtures.py:419,439`; `roll.py:103-113` |
| cover | a `cover` Record whose `terms` names its maker. While it is live, your acts are *anchored* on the cover's id | live while a stage is unmatured, about 3 seasons | `effects_information.py:258`; `state/attribution.py:183-235` |
| anchor | what an Event is *about* (`anchor_of`): the actor, or his live cover | `seen.who` still reads the real actor | `attribution.py:105-150` |
| inquiry | the six verbs that write nothing to the world and emit `finding.made` or `finding.none` | 3 are graded (`research`, `examine`, `surveil`) | `verb_table.yaml:1321-1438`; `rosters.yaml:1115-1143` |
| degree, band | Overwhelming / Success / Partial / Failure, from `margin = net − Ob` | ≥3 / ≥1 / 0 to <1 / <0 | `engine/dice_engine/dice_engine.py:227-239` |
| `finding_terms` | which `Seen` terms a band uncovers | O and S: `[stratum, marks, who]`; P: `[stratum, marks]`; F: none | `rosters.yaml:2447-2473` |
| covert kind | a deed kind that leaves a findable *trail* | one member: `record.forged` | `rosters.yaml:2475-2490` |
| trail | `trail_of`: the most recent covert Event on the subject, if a person did it, it was not you, and you do not already hold it | at most one per kind per side | `epistemic.py:368-404` |
| `holds_trail` | "already known": you hold `(s, e.kind, True)` on a subject specific to the Event, made no earlier than the Event | any source counts | `epistemic.py:336-365` |
| found claim | what a finding deposits: source `inferred` (the `post_remit` slot), refracted at remove 1 | 100 → 50 | `witness.py:259-315` |
| `undeposited_kinds` | Event kinds that WITNESS gives to nobody | `finding.none` only | `rosters.yaml:1145` |
| Question | an item on your agenda for your next deliberation, raised by claims that landed since your last one | one question per deliberation | `queries/world_q.py:2374` |
| known-false veto | drops an option whose precondition your own ledger says is false | absence of a claim is UNKNOWN, never False | `options.py:308`; `epistemic.py:72-134` |
| knot (engine) | a `knot` Tenure that feeds the `witness_key` channel | its opener `tie / knot` cannot be resolved (H-182) | `epistemic.py:543-560` |
| knot (sim) | a separate bond model: tiers, strain, rupture | no season caller | `systems/fieldwork/sim/knots.py` |

## 2 How it works

This is the order in which an actor meets the rules.

**2.1 You act, and the act becomes an Event.** RESOLVE folds your act. It writes the world, or writes
nothing in the case of inquiries and `tell`, and emits Events. Nobody "observes" by choosing to.
Observation is computed afterwards.

**2.2 WITNESS decides who learns it** (barrier 4, once per round; `loop/driver.py:510`). Events of an
undeposited kind (`finding.none`) are dropped first (`witness.py:365`). For each remaining Event and
each person, the engine asks the channels in precedence order and takes the **first** one that admits
the person (`epistemic.py:794-840`):

| channel | admits | source | remove | `Seen` terms shown |
|---|---|---|---|---|
| `co_located` | anyone at the Event's place | firsthand | 0 | stratum, marks, who |
| `witness_key` | the anchor himself, or a live `knot` partner of the anchor | firsthand_via_knot | 1/3 | stratum, who |
| `document_key` | anyone holding an object the Event wrote | told_by | 2/3 | (none) |
| `chronicle` | **everyone**, if the Event's **kind** appears in the `emits:` of any `binding_decision`-stratum row | told_by | 2/3 | stratum |
| `post_remit` | the establishment of the seat the act was done through, within its purview | inferred | 1 | stratum |

(`rosters.yaml:419-425,1020-1025`; `epistemic.py:428-686`.)

`chronicle` is a **kind filter, not an act filter** (`epistemic.py:652-654,685-686`). Any Event whose
kind some `binding_decision` row emits goes to every person alive, whatever caused it:

- `determine` emits `pursuit.moved` (`verb_table.yaml:355`), so `argue`'s `pursuit.moved`
  (`verb_table.yaml:157`) is also realm-wide;
- MATTER's `tenure.closed` is broadcast too (round-2 audit, CROSS C5).

The consequence for play: matters of record, including some that are not governance acts, are public
across the whole realm. A private act whose kind no binding row shares is seen only by the people in
the room.

**2.3 What each admitted person receives** (`witness.py:590-972`):

- an **event-kind claim** for each subject;
- a **`seen` claim**, masked to the channel's terms;
- **observation claims** of cells (for example `stores:grain`), which go **only to the actor** at
  `observation_deposit_mode="actor"` (`fixtures.py:518`);
- **content**: if the Event made you the new holder of a Record, you get `content:<kind>` with what it
  says. "A held document is a held belief". The deposit carries no attribution, so a forged sheet and
  a genuine one land identically;
- **told content**, for `news.told` (2.5).

**2.4 Refraction.** Every copy except the actor's own is refracted once, at deposit (`witness.py:606`):

```
conf' = int( conf × (1 − 0.5·remove) × (1 − 0.5·dissent) + 0.5 )
```

| channel | from 100, no dissent | from 100, with dissent |
|---|---|---|
| co_located | 100 | 50 |
| witness_key | 83 | 42 |
| document_key / chronicle | 67 | 33 |
| post_remit, and found claims | 50 | 25 |

Refraction can only lower a confidence. The seed-0 realm shows confidences of 100, 95, 67 and 62. 67 is
the chronicle copy, and 62 is that copy after one decay (67 − 5).

**2.5 Telling.** `tell` needs a claim on the subject in your own ledger, and the hearer must be `with`
you, at the same place (`verb_table.yaml:1169-1192`). It is contested over "a standing". On O, S or P
the result is `news.told`; on Failure it is `news.untold`. Each hearer gets a copy of your `Said`:

- source `told_by`, with **your** confidence, `chain = your chain + (you,)`, refracted by the channel
  that admitted the hearer (`co_located` for the hearer you addressed, so ×1);
- **dedup**: the copy is skipped if the hearer already holds the same subject, predicate and value
  with an empty chain or the same origin (`witness.py:932-935`);
- **drift at Partial only** (`witness.py:136-231`): a hash, not a die, selects either one dropped
  addressee from a document's `to` list, or a plain number moved by `1 + sel % ceil(0.5·|v|)`, keeping
  its sign. Event-kind `True` values and `Seen` values pass through verbatim;
- **circles**: with probability `telling_privacy` (0.0) the copy is held "in confidence". Retelling it
  outside the circle emits `confidence.broken`. At shipped values this never happens.

When a told claim is *read*, it weighs `0.5^hops × relation × record` (`options.py:1513-1545`): 0.5
for one hop, 0.25 for two. `ledger_weigh` returns `None` (plain reading) for a ledger with no chained
claim (`options.py:1356-1362`).

**Provenance.** Each claim keeps its `source`, its `chain` and so its `teller` (`state/carriers.py:337-379`),
and `record()` (`decision/options.py:1470-1510`, `record_gain 0.5` at `fixtures.py:801`) re-weights
everything a teller passed on by how often his told cells matched the hearer's own firsthand claims. Two
uploaded surveys (not in the repo, `research/game_precedent_suite/README.md:30`) find belief with provenance
*and fabricable, traceable evidence* in only one title, The Guild 2 (`consolidated_twenty_games.md:179,235`,
of twenty titles; `Citizens_Settlements_and_Factions_-_Nine_Titles.md:390`, of nine).
`research/game_precedent_suite/dispositions/ATTACHMENTS_CROSSCHECK.md` §A row 2 marks that "Holds" within v2,
and its verdict rests on the fabrication half, since Dwarf Fortress rumours also originate with witnesses.
Valoria holds the provenance half; D_T06 row 66 grades the fabrication-tracing half LACKS in the realm (§3
shows it only in a hand-built world). The chained half is nearly unused at shipped values: 0, 0 and 1
chained claims were alive at the end of two seasons in seeds 0, 1 and 2 (uncommitted round-3 probe), a
survival count that cannot see a claim evicted, or held by someone who died.

**2.6 Fading and forgetting.** MATTER, once per season, takes 5 off every claim's confidence and emits
`claim.decayed` (`matter.py:317-347`). Over the cap of 200, WITNESS evicts the lowest
`confidence × (when + 1)` (`ledgers.py:17-32`). A 100-confidence claim from tick 0 scores 100, and a
50 from tick 2 scores 150, so **old firsthand knowledge is forgotten before fresh hearsay**. Nobody
can witness a forgetting, and nothing "unsays" a claim.

**2.7 How beliefs drive choice.** The chooser sees your ledger, never the World. Claims that landed
since your last deliberation raise **Questions** about subjects within your reach
(`world_q.py:2374`), and `opening_set` forms candidates on the question's referents. Your ledger also
vetoes options it makes known-false (`options.py:308`) and supplies names and operands. News sets the
agenda; beliefs do not create preferences.

**2.8 Inquiries.** An inquiry writes nothing to the world. The three graded rows roll through
`social_contest.roll` (`rosters.yaml:1115-1143`):

- pool = `pool_default = 2`, for everyone. **The reason is structural, not data.** `VERB_CAPABILITY`
  maps only `tell` and `speak` (to `copying`; `rosters.yaml:1228-1231`), and `_capability` returns
  `None` for an unmapped verb (`seam/wrappers/sigma.py:113-116,130-131`). Writing a person's capability
  would therefore not change any inquiry pool. (Capability is also empty on every realm person; ctl
  "capability nonempty 0".)
- Ob = `obstacle_default = 2`, plus the Record's `forgery_quality`, then capped at
  `obstacle_ceiling = 2` (`roll.py:103-113`; `fixtures.py:414-419`). So **a forgery adds nothing**;
- dice: TN 7, a face of 1 counts −1, 2-6 count 0, 7-9 count +1, 10 counts +2
  (`dice_engine.py:153-161`).

With two dice the net is at most 4, so the margin is at most 2. The odds are **Overwhelming 0,
Success 0.07, Partial 0.19, Failure 0.74** (exact enumeration, §9).

Results: O, S or P emit `finding.made` with that degree; Failure emits `finding.none`; a refusal (a
failed precondition) also emits `finding.none`. `interview` and `reconstruct` are ungraded: they emit
`finding.made` with `degree None`.

**2.9 What a finding uncovers** (the "planted trail"). At RESOLVE, `find_trail` dispatches only
`finding.made` (`rosters.yaml:2424-2446`). The host builds a `FieldworkInput` with the band, the trail
and `finding_terms` (`seam/wrappers/fieldwork.py:49-63`), and `modules/fieldwork/find.py` returns
`(trail event, terms[band])` for each trail item. No band (Failure, or ungraded) means nothing is
uncovered.

The trail is `trail_of(subject, you)`: the latest `record.forged` that wrote the subject (deeds done to
it) or that is anchored on it (deeds done by it). An item is dropped if no person did it, if you did it,
or if you already hold it. At the next WITNESS, `_found_claims` gives you what a witness would have
held, masked to the band's terms. At Partial, `who` is masked, and so is the event-kind claim on the
actor. The source is `inferred`, refracted at remove 1 (`witness.py:276-315`).

The docstring states the consequence: the trail is "REACHABLE ONLY THROUGH A PLANT" (`epistemic.py:379`).
You learn a forged Record's id either by witnessing the forging, which already tells you and closes the
trail, or by being given the Record.

**2.10 Covers.** `conceal` mints a `cover` naming you (`effects_information.py:258-269`). While one of
its 3 stages is unmatured, `anchor_of` answers the cover's id for your acts. Deposits are then *about*
the alias, `witness_key` partners stop seeing you, and the "deeds by" side of `trail_of` moves. **`seen.who`
still names you to everyone present** (`attribution.py:118-121`).

## 3 A worked example

The world is `test_fi03_trail.py::trail_world`: `tiny_world` with the Crown faction planted. I ran it
read-only (§9). Its ticks are seasons, advanced by hand between stages. The cast: **p_other** (the
forger) and p_mid and p_low are in Hh; **p_high** (the investigator) is in S; p_king is in R.

**Tick 0 — forge.** p_other already holds a claim about p_mid (the `own_ledger` precondition), and p_mid
commits to the Crown. `forge` mints Record `rec:fi03_forge`, kind `faction_sheet`:
`{proposition: fac_crown, members: [p_high, p_mid], holdings: [], seats: [off_duke], head: p_other}`.
`head` is the one false key. The Record has `forgery_quality 1` and stages at ticks 1, 2 and 3. Its hold
opens to p_other. The Event is `record.forged`.

WITNESS: p_mid is co-located and gets `(p_other, record.forged)`, `(rec, record.forged)` and
`seen{stratum: uncontested_material, who: p_other}`, all firsthand at 100. p_high gets nothing.
`trail_of(rec, p_high)` returns `[record.forged]`.

**Tick 1 — the plant.** p_other `move`s to S (`travel.moved`), then `give`s the Record to p_high
(`record.given`). `give` requires that the subject is a Record, that you hold it, and that the receiver
is `with` you. p_high, co-located, now holds at 100 firsthand: `travel.moved` and `record.given` on
p_other, `seen{who: p_other}` and `content:faction_sheet` with `head: p_other`. He now believes the
forger heads the Crown, at full confidence.

**Tick 2 — research.** The real chooser path forms `research` on the Record.

- Ob = min(2 + 1, ceiling 2) = 2. Pool 2.
- Across 40 act ids the degrees came out Success 5, Partial 7, Failure 28 (theory: 7%, 19%, 74%).

*Success (act id 0):* `finding.made`, terms `[stratum, marks, who]`. p_high gains three `inferred`
claims at `int(100 × (1 − 0.5×1) × (1 − 0) + 0.5) = 50`:
`(p_other, record.forged, True)`, `(rec, record.forged, True)` and `seen(rec){who: p_other}`. Each
`claim.deposited` names both the finding and the forging as causes. His own act also deposits
`(rec, finding.made)` and `seen(S){who: p_high}` at 100, unrefracted because he is the actor.

*Partial (act id 1):* only `(rec, record.forged)` and `seen(rec){who: None}`, at 50. He learns the
sheet was forged, not by whom. **The trail is now closed to him until that claim is evicted from his
ledger** (`epistemic.py:356-365`; `state/ledgers.py:24-32`): a later Success on the same Record deposits
nothing (`holds_trail`; decay leaves a claim in place even at 0 confidence, `loop/matter.py:321-322`).

*Counter-information:* p_other is in S and receives `(rec, finding.made)` and `seen(S){who: p_high}` at
100. **The forger learns he was investigated, and by whom, with more confidence than the investigator
has in his finding.**

*Next deliberation:* `questions_for` raises a question about the claim `(p_other, record.forged)`, and
`opening_set` forms candidates on p_other from it (`test_fi03_trail.py:565-588`). In the control arm,
with `finding_terms` emptied, he forms none.

**Tick 3 — spreading it.** p_high `move`s to R and `tell`s p_king about p_other. His Said is
`(p_other, record.forged, True, conf 50, chain ())`. Across 12 act ids the result was 2 `news.told`
(Success) and 10 `news.untold`. On a told: p_king holds `(p_other, record.forged, True)`, `told_by`,
confidence 50 (co_located, ×1), chain `(p_high,)`, read weight 0.5^1 × 1 × 1 = **0.5**.

**After that.** Each MATTER takes 5 off: 50 → 45 → 40, reaching 0 after ten seasons. The eviction score
at tick 2 is 50 × 3 = 150.

**The same chain under a cover** (probe). If p_other takes `conceal` first, the bystander's deed
claims are about `rec:cv` instead of p_other, but his `seen.who` is still p_other. A Success finder
gets `(rec:cv, record.forged)` plus `seen{who: p_other}`. **The cover moves what the claim is about. It
does not hide the hand.**

## 4 What you can do

**Who may act.** Eligibility is a list of alternatives. Every row below except `issue` (`remit:issue`) and
`open_case` (`remit:determine` only, `verb_table.yaml:902`) includes `own`, so anyone may attempt those
rows. A `presence:` alternative never admits by itself: it is unevaluable person-side
(`options.py:623-625`).

**Cost.** Each act spends from your scene-action budget (§0): 1 as a lone scene, or a share of an
extended scene that costs 2 for up to 3 acts. Holding the Record a maker verb mints raises next
season's budget by 1.

The "seed 0" column is ctl attempted/ok. Formation counts come from my `w.acts` probe: these are acts
the chooser formed, including those refused at admission.

| verb | prerequisites (typed) | outcome | writes | seed 0 |
|---|---|---|---|---|
| `research` | subject is a Record (you need only know its id) | graded, 2.8. O/S/P: `finding.made`, uncovers a trail if one exists | nothing | 14 / 7 (probe: 6 P, 1 S, 7 F); 115 `finding.none`, so about 108 formed acts were refused at admission |
| `surveil` | subject is a Rung and you are `present_at` it | graded. The Person case is absent, so the trail's "deeds by" side is unreachable | nothing | 30 / 5 (2 P, 3 S, 25 F) |
| `examine` | a Site exists and you are present at it | graded | nothing | **0 / 0 in seeds 0-2: it never passes admission.** It is formed 62 / 59 / 39 times in seeds 0 / 1 / 2, and every one emits `finding.none` at admission. The cause is the operand: `site` is filled with the question's subject (`decision/options.py:1047-1048`), and none of the 160 formed acts was given a Site (322 Sites exist; seed 0, by act: 45 Rungs, 15 Persons, 4 of them dead by the end, and 2 Records; probe), although `verb_table.yaml:996` says a referent can be a Site since `11a`. The cause is not new: `verb_table.yaml:1312-1313` already names the Site binding as the reason `examine` is always refused, and REM-22 (rev. 3 adds `examine`, D-04; `proposals/2026-10-21-v9-remediation/2026-10-21-v9-remediation-02-items-rb0-to-rb3.md:360-379`) is the tracked fix; no `referent_class: Site` exists in `verb_table.yaml` yet. Test of the graded roll once a Site is given: `engine/season/tests/test_fi01_graded_inquiries.py:223-239`. `restore` (`verb_table.yaml:988-995`), `work` (`:1512-1517`) and `sabotage` (`:1025-1032`) also take a `site` operand, so the same fill reaches them (ctl attempted/ok, seeds 0 · 1 · 2: restore 23/0 · 31/0 · 30/0, sabotage 34/0 · 22/0 · 33/0, work 77/0 · 70/0 · 63/0). For those three the fill is one cause among several: `work` stages a rise only where a live works names the Site (`loop/effects_economy.py:103-104`), a dwelling or garrison floor is empty (`rosters.yaml:2631-2632`; 248 of 322 Sites), and natural play mints no works Record (seed 0, two seasons: Records of kind `text`, `faction_sheet`, `cover`, `petition` and `dispensation` only; uncommitted round-3 probe) |
| `interview` | subject is a Person | ungraded `finding.made`. Uncovers nothing and reads nothing from the interviewee | nothing | 32 / 11 |
| `reconstruct` | you hold a claim on the subject | ungraded. Uncovers nothing | nothing | 39 / 33 |
| `thread_read` | `requires_typed: none` (TS ≥ 30, no carrier, H-85) | not resolvable | — | never formed |
| `survey` | a claim on the subject, and the subject coheres under one faction | `faction.surveyed`; a true sheet in your hold, and its content in your ledger | Record | 57 / 13 |
| `forge` | as `survey` | `record.forged`; a sheet with `head` = you, `forgery_quality 1`, in your hold | Record | 52 / 12 |
| `conceal` | none | `cover.assumed`; a cover naming you, live about 3 seasons | Record | 19 / 19 |
| `create_record` | none | `record.created`; a `text` Record in your hold | Record | 87 / 87 |
| `give` | a Record you hold, to a person `with` you | `record.given`; your hold closes and the receiver's opens; he gets the content | Tenures | 16 / 0 (seed 1: 21 / 0; seed 2: 19 / 1, a cover) |
| `tell` | a claim on the subject, and the hearer `with` you | contested; 2.5 | nothing | 23 / 4 (seed 1: 25 / 7; seed 2: 19 / 6) |
| `destroy_record` | a Record you hold | `record.destroyed` | Record | withheld from formation (`fixtures.py:933`); TESTS-ONLY |
| `utter`, `petition`, `issue` (`remit:issue`), `open_case` (`remit:determine`) | (their own rows) | make Propositions, petitions, dispensations and case files. Their kinds are chronicle-public only if a `binding_decision` row emits them (2.2) | Record / Proposition | 39/39, 42/14, 6/5, 12/6 |

Every Record you hold adds 1 to your scene budget (`budget.py:57-58`). A failed or refused inquiry is
invisible to everyone, you included, because `finding.none` is never deposited.

## 5 Pursuing goals here

**(a) Goals and how the code represents them.** No "investigation" goal object exists. An actor's
pursuits do not name a culprit to find. (In ctl, 37 of 74 persons have empty pursuits after two
seasons in seed 0.) What drives fieldwork is the **agenda**: a claim landing in your ledger raises a
Question (2.7). The goals below are what a person can *arrange*. The code marks success only as claims
in someone's ledger.

| goal | what success is, in code |
|---|---|
| find out who did X | you hold `(doer, kind, True)`, or a `seen` claim on the thing with `who` set |
| hide what you did | nobody else holds your deed claim, or holds it only about your cover's id |
| plant evidence | someone else holds the `content:` of a Record you made, which says what you chose |
| spread news | hearers hold your claim as `told_by`, with you in the chain |
| suppress news | others hold no claim, or a weak one (low confidence, evicted, decayed) |

**(b) The plays, step by step.**

*Play 1: find the hand behind a document.*

1. Get the Record's id into your ledger without witnessing its creation. Being given it is the only
   built route, since witnessing the creation closes the trail.
2. `research` it.
3. Per attempt: 7% the hand is found (Success), 19% the deed without the hand (Partial, and the trail
   then closes to you), 74% nothing.

Only forged Records have a trail. A survey, a cover or a text Record yields nothing, because they are
not in `covert_kinds`. `surveil` and `examine` cannot reach a forging, since a forging writes a Record,
not a Rung or a Site.

*Play 2: just be there.* Standing where the deed happens gives `firsthand` 100 with `who`, which beats
any finding (50, `inferred`). Being in the room is the strongest information act in the game, and it
costs no slot.

*Play 3: hide a deed.*

- Act where nobody else stands.
- Avoid acts whose Event kind a `binding_decision` row also emits. `chronicle` broadcasts those to
  every person.
- Avoid acting through a seat (`post_remit`).
- Avoid writing a thing others hold (`document_key`).
- `conceal` first, so that later learners file the deed under an alias. This costs one act, and the
  cover lapses after about 3 seasons.

A cover does not hide you from anyone present (3, cover probe).

*Play 4: plant false paper.*

1. `forge`. You need a claim on a subject that coheres under one faction; 40 of 52 forges were refused
   in seed 0.
2. `move` to the target.
3. `give` the Record. He must be `with` you. You keep no copy, but your own ledger keeps the content.

He now holds the false `head` at 100, indistinguishable from a true sheet. What reads it: a petition
he files on it is addressed to the forger (`effects_information.py:756-758`). Nothing else in the
decision layer reads the sheet's `members`, `holdings` or `seats` (G20 FI-G03).

*Play 5: spread news.*

1. Have a claim on the subject.
2. Stand with the hearer.
3. `tell`.

The hearer gets **your** confidence, discounted at read time by 0.5 per hop. If he already holds the
same triple from anywhere, the telling deposits nothing. A Partial telling may garble a number or drop
a name.

*Play 6: suppress.* No verb removes a claim. `destroy_record` is withheld from formation. Your levers
are prevention (Play 3) and time: −5 per season, plus eviction at 200 claims, where old claims go
first.

**(c) Costs, risks, counter-play, blockers.**

- Every act spends scene-action budget (1 alone, or a share of a 2-cost extended scene; §0). There is
  no Exposure meter, no money cost and no wound.
- Inquiries are themselves witnessed. **Anyone co-located** gets the `finding.made` claim and
  `seen{who: you}` at 100 (`epistemic.py:428-453`). That includes the forger, if he is there.
- Failure and refusal both leave nothing in any ledger. You cannot tell a missed roll from an
  impossible inquiry, and nobody else can either.
- A Partial on a trail denies you the hand until that claim is evicted from your ledger
  (`epistemic.py:356-365`; `state/ledgers.py:24-32`).
- The forger can see you coming (3, tick 2). There is no counter-espionage verb (ED-FI-0002 unbuilt).
- Blockers: no `give` of a forged Record in seed 0 (the chooser's `give` subjects are people and
  buildings, §8), so in practice the plant never happens.

**(d) What the mechanics structurally reward and punish.**

- **No investigator is better than another.** Pool 2 and Ob 2 apply to everyone. Even a written
  capability would not change this, because no `VERB_CAPABILITY` row names an inquiry.
- **Forgery quality is inert**: the ceiling 2 swallows the +1.
- **`interview` and `reconstruct` are dominated**: they spend budget, uncover nothing by construction
  (no degree, so no `finding_terms` row), and emit a `finding.made` that tells bystanders you asked.
- **`examine` never passes admission** in seeds 0-2. It is formed 62 times in seed 0 and refused every
  time, because the question that forms it never names a Site (§4). So a person who was not at a place
  when something happened there cannot read it off the place later: `examine` never runs, and the only
  covert kind, `record.forged`, writes a Record, not a place (Play 1).
- **Presence dominates inquiry**: 100 firsthand against 50 inferred.
- **Telling something your hearer saw with you deposits nothing.** This is a mechanism: dedup skips a
  copy the hearer already holds unchained (`witness.py:932-935`). The evidence is small: all 4 seed-0
  tellings hit it (probe). That is one seed, n = 4. Seeds 1 and 2 have 7 and 6 `news.told`; at the end of
  season 2 they leave 0 and 1 chained claims alive (probe), a survival count that cannot tell a copy skipped
  by dedup from one evicted, or held by someone who died (ctl `person.died` 9 / 6 / 11 in seeds 0 / 1 / 2);
  I did not trace which. I make no claim that telling is generally wasted. A telling to someone
  who was absent does land (the §3 example).
- **Kind-sharing broadcast.** Any Event whose kind a `binding_decision` row emits reaches every person
  at 67 (2.2). That includes kinds produced by non-binding acts (`argue`'s `pursuit.moved`) and by
  MATTER.

**(e) What success leaves in the world.**

- *A finding:* claims in the finder's ledger only, at 50 and decaying; `claim.deposited` Events whose
  causes chain claim → finding → forging; and a question on his next agenda. No world state changes.
- *A plant:* a hold moved and a false content claim at 100.
- *A cover:* a Record and an anchor map entry (`World._covers_logged`) that fixes forever what each
  logged Event is about.
- *A telling:* a chained claim, the only place a path of hearsay is recorded.

## 6 How it connects

- **Social contest (SC):** owns the roll for the graded inquiries and for `tell`. Reads deed claims for
  `reception` and `proofs`, and reads `Record.forgery_quality` through the input builder
  (`seam/wrappers/sigma.py:174-191`). No inquiry product is a proof kind yet (FI-G47).
- **Governance (GV):** `issue`, `dispatch`, `confer` and `release` are `binding_decision` rows, so every
  Event of a kind they emit is chronicle-public, whoever or whatever caused it. Seat reports of MATTER changes go to governors via `post_remit`
  (`witness.py:513-524`). `petition` and `open_case` make Records.
- **Factions (FA):** `survey` and `forge` freeze `faction_q.resolve`. The forged `head` addresses the
  holder's later petitions.
- **Decision layer:** claims become Questions, vetoes, names and operands. The chooser never reads the
  World.
- **MATTER:** decay, plus stage maturation, which ends covers and document terms.
- **Threadwork (TW):** `thread_read` waits on a Thread Sensitivity carrier. The sim knots and `trace`
  are TW-side.
- **Combinations:** `conceal` → `forge` → `give` puts the deed claims under an alias for bystanders but
  not for a hand-band finder. `research` → `tell` moves a 50-confidence inference outward at a read
  weight of 0.5 per hop.

## 7 Playing it as proposed

**[PROPOSED] throughout this section.** The rows come from the lexicon `proposals/2026-10-16-verbs/2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md`
(Status PROPOSED, 2026-10-17; named mechanics in §3.7 `:860-875`). None of it executes.

| you would… | how it would work | waits on |
|---|---|---|
| learn something from every inquiry | a per-verb selector over the world: `examine` reads the Rung's log, `research` reads a Record's content and whether it is forged, `reconstruct` names the best-supported candidate; confidence by degree, at remove 0 | **M1** finding producer (FI-G01) |
| tell a missed roll from an impossible ask | refusal → `inquiry.refused`; Failure stays `finding.none` | **M2** |
| be honestly wrong | on Failure, a wrong `who` drawn from the inquiry's candidate set | **M3** (K-37) |
| face a skilled hider | Ob = the concealer's score/2; `forgery_quality` = the forger's score/2; a graded cover | **M4**, J-T1 (stored score), H-210 |
| hear the interviewee's answer | the question lands in his ledger; he answers, evades or lies by his own act next season | **M5**, J1 (lexicon prefers option (b)), ED-FI-0004 Lattice |
| destroy or access paper by holding | `hold:<object>` eligibility typed | **M6** (H-75) |
| survey a place | `rung_sheet` (holder, persons, stores, forces); `audit`, `census` and `scout` as modes | **M7** |
| bribe | `transfer`'s write plus an inducement deposit to a circle of two; payee-side weight | **M8**; `suborn` parked on J-C-6 (lying) |
| bring a finding to court | `determine` and contests read held findings by proof kind | **M9** (SC) |
| shadow a person | co-movement | **M10** |
| unmask a cover | `watch` (the proposed rename of `surveil`): the true `who` of a covered act at the watched Rung, rolled against the cover's grade | M1, M4; ED-FI-0002 |
| disguise yourself | a cover with scope `room` hides `seen.who` from those present | `conceal` scope decision |
| infiltrate | a cover plus `oblige`'s duty edge | live cover; R-21/22 |

Also proposed: `search` and `track` as modes of `examine`, `decipher` (parked), `eavesdrop` and
`intercept` (parked), `trace` (TW, needs plugged knots). The lexicon also proposes that `forge` emit
`faction.surveyed` in place of `record.forged`. My reading: that would leave `covert_kinds` naming a
kind no row emits, which `data/verbs.py::_check_covert_kinds` refuses at import (`rosters.yaml:2481-2485`),
so the two would have to move together. The canon price "+2 Exposure" was declined (FI-G29).

**Stubbed or inert at shipped values today:**

- `telling_privacy 0`, `intent_disclosure 0`, `stance_polarity "legacy"` (regard does not enter
  choice);
- `rank()` ≡ 0, competence ≡ 1 (H-200), `Seen.why` ≡ None, `marks` ≡ ();
- `witness_key` admits nobody new, because no `knot` Tenure can be opened (`tie / knot` effect declined,
  H-182);
- `forgery_quality` is capped away;
- `thread_read` is unresolvable; `destroy_record` is withheld;
- `surveil`'s Person case is absent.

**The knots sim** (`systems/fieldwork/sim/knots.py`, called only by `engine/tests/test_knots_ed912.py`).

| element | rule |
|---|---|
| formation | bonds ≥ 5, disposition ≥ 5, one party with TS ≥ 30; roll `spirit×2 + history_relationships` d10s at TN 7 against Ob 2 (`:52-59,214-227`). Overwhelming gives a Close knot, Success a Distant one. At the default spirit 3 (pool 6): Close 14%, Distant 33%, none 53% (my enumeration) |
| strain | clamped to Distant (−2, 5) and Close (−5, 5); start 0 and −2; breaks at ≥ 5 (`:68-80`) |
| tempered | a Close knot at ≤ −5 absorbs one rupture |
| loss | composure 4 and disposition −3 are *returned, not applied*. A Close knot with positive strain lands a conviction Scar 1; a rupture costs Coherence −1 (`[UNVERIFIED post-ED-912]`) |

## 8 Common mistakes and traps

**Wrong assumptions about the rules:**

1. **"A cover hides me."** Not from those present, and not from a finder whose band shows `who`. It
   changes what claims are *about* (verified, §9).
2. **"A forgery is hard to detect."** Its quality is capped away. Every research on it rolls 2 dice
   against Ob 2.
3. **"A Partial is a step toward the answer."** It closes that trail to you until that claim is evicted from your ledger (`epistemic.py:356-365`;
   `state/ledgers.py:24-32`).
4. **"`research` needs the document in hand."** It needs only an existing Record id
   (`verb_table.yaml:1364-1372`). The *trail*, however, is reachable only through a plant.
5. **"`interview`/`reconstruct` succeeded, so something was learned."** Ctl counts their
   `finding.made` as ok, but they carry no degree and uncover nothing.
6. **"Findings are certain."** They land at 50 (`inferred`, remove 1), half of what a bystander gets.
7. **"Claims are frozen at deposit."** C10 said so. `refracted_confidence`'s "FROZEN AT DEPOSIT"
   (`options.py:1433`) refers to the refraction factors only. MATTER decays every claim by 5 each
   season (errata G8).
8. **"Old firsthand knowledge is safest."** Eviction ranks `confidence × (when+1)`, so old claims go
   first.
9. **Two "knots".** The engine's `knot` Tenure (the `witness_key` channel) and the unplugged sim are
   unrelated.
10. **"Inquiry runs, so investigation is in the loop."** The register grades the scale `in_loop: false`.

**Stale statements in the tree and the extracts:**

11. `rosters.yaml:2485-2486` says `conceal` is unbuilt. It is built (`verb_table.yaml:207`; 19 of 19 in
    seed 0).
12. G20 FI-G23/G24 ("`forgery_quality` written by nothing") and FI-G26 ("no `conceal` verb") are stale
    at HEAD. L12's `watch` is a *proposed* rename; HEAD has only `surveil` (errata C8).

**Where the draft appendix A8 was wrong, and the correction:**

- *"G20 does not exist."* It does: `extract/G20_gaps_SC_GV_FI_TW.md` holds FI-G01..G58.
- *"`examine` formed and refused only", "62 `finding.none`"* (A8 A3, A4). **A8 was right.** My
  round-1 text, which said examine is never formed, was wrong. `w.acts` holds 62 `examine` acts in seed
  0, and all 62 emit `finding.none` at admission; ctl's 0 counts only resolved acts. Corrected wording:
  "never passes admission".
- *"250 `finding.none` (218 refusals, 32 Failures)."* **Now reproduced** by attributing on `w.acts`.
  The 250 are research 115, examine 62, surveil 46, interview 21, reconstruct 6. Of these, 32 are
  rolled Failures (research 7, surveil 25), leaving 218 refusals. Errata C8 had marked the breakdown
  unverified; the probe verifies it.
- *"Uncertain why every `give` is refused."* Answered by the probe: of the 16, 15 name a person or a
  building as subject (the question's referent), which fails `existence(subject, Record)`. One names a
  cover held by someone else. Seed 2 has 1 success, a cover.
- *"Why no chained `told_by` survives."* Answered: each of the 4 seed-0 tellings carried a triple its
  hearer already held unchained, so the dedup skipped it.
- *"`witness_key`/`post_remit` RUNS-IN-LOOP"* (A8 B4). `witness_key` is TESTS-ONLY: it admitted
  nobody. `post_remit` is TESTS-ONLY at seed 0 and executes at seed 2 (one `inferred` claim).
- *Scene allowance.* A8 says "one season = up to `scene_budget=5` rounds". The correct reading is in §0
  (CROSS C1): `budget()` returns scene actions; an extended scene costs 2 for up to 3 acts; one scene is
  released per round. Budget 5 therefore buys 7 acts, and seed 0 shows ~7.6 resolved acts per person per
  season. Errata G11's "~8-10" is not supported.
- *`dissents`* (A8 B2 "disagrees with the holder's own firsthand claims about a person"). It is only
  about the holder **himself** (a person predicate with `subject == holder`) or a cell, plus the act
  prior (`options.py:1393-1407`; errata C8).

**§8 Round-2 corrections** (each cited line re-opened before accepting it):

1. *H-F2, inquiry pools.* Accepted. I had given the wrong reason ("no capability is written").
   `VERB_CAPABILITY` maps only `tell`/`speak` (`rosters.yaml:1228-1231`), and an unmapped verb gets
   `None` (`sigma.py:113-116`), so a written capability would not move any inquiry pool. Fixed in 2.8
   and 5(d).
2. *H-F4, seed-2 `inferred`.* Accepted. The `post_remit` slot is regraded per seed: TESTS-ONLY at seed
   0, executing at seed 2 (§0). The producers are `witness.py:289` (found, 0 in seed 2), `:513-524`
   (seat report) and `:598` (channel).
3. *H-F6, `destroy_record`.* Accepted. It is TESTS-ONLY, not DESIGN-ONLY: the row is typed with an
   effect, and formation is withheld by `fixtures.py:933` (`verb_table.yaml:306-312`).
4. *H-F7, `open_case`.* Accepted. Its eligibility is `remit:determine` only (`verb_table.yaml:902`), and
   `issue`'s is `remit:issue`. The §4 claim "every row includes `own`" is fixed.
5. *H-F10 and CROSS C1, scene budget.* Accepted. `interactions_per_scene = 3` (`fixtures.py:488`) and
   `extended_scene_cost = 2` (`:489`); the spend loop is `choose.py:643-657`; one scene per round is
   released (`driver.py:456`). Every "one slot per act" phrasing is replaced (§0, §4, §5c).
6. *H-F16 and L-X6, `examine` and who sees an inquiry.* Accepted. "Never formed" becomes "never passes
   admission" (62 formed in seed 0, by probe). "The subject's holder learns who inquired" becomes
   "anyone co-located".
7. *H-OBS, CROSS C5 and L-X17, chronicle.* Accepted. It is a kind filter (`epistemic.py:652-654,685-686`);
   `pursuit.moved` comes from `determine` (`verb_table.yaml:355`) and also from `argue` (`:157`).
   Rewritten in 2.2, Play 3, 5(d) and §6. MATTER's `tenure.closed` I took from CROSS C5 without
   re-tracing which binding row emits it.
8. *L-X19, column order.* My columns already read attempted/ok. The header now defines attempted as
   "passed admission" and ok as Partial-or-better for graded rows (CROSS C2).
9. *L framing note.* Accepted. "Telling to companions is wasted" generalised from 4 tellings in one seed.
   It is restated as the dedup mechanism plus its n = 4 evidence, with no general claim (5d).
10. *CROSS C3 and C11.* Ticks replace "season N" in 2.6. Rung, Tenure, Proposition, Office, purview,
    establishment, stratum, prize and `with` are added to §1.

### Round-3 corrections

Against `51d7b05` and the precedent suite. Each cited line was re-opened at the current tree; evidence in
brackets (probe = a read-only run of `build_realm(seed)` for seeds 0, 1 and 2, two seasons, the ctl recipe).

1. §0, `post_remit` row. Old: one `inferred` claim at seed 2 only, "this slot executes at seed 2". New:
   seeds 1 and 2 each end season 2 with one `inferred` claim, so the slot executes at both. [probe: sources
   alive `inferred` 0 / 1 / 1; found deposits 0 / 0 / 0; D_T06 E1]
2. §0, found-deposit row. Old: 0 found deposits "in seeds 0 and 2". New: in seeds 0, 1 and 2. [probe; D_T06 E2]
3. §4, `examine` row. Old: 62 formed in seed 0, "reason not traced". New: 62 / 59 / 39 formed, all refused,
   because the `site` operand is filled with the question's subject (`decision/options.py:1047-1048`) and
   none of the 160 acts named a Site (322 exist). [probe; code opened; D_T06 E3]
4. §5(d), `examine` bullet. Old: formed 62 times in seed 0 and refused every time. New: adds the cause and
   what it means for reading a place later. [as 3; `epistemic.py:379` and Play 1 for the Record-only trail;
   D_T06 E4, second sentence narrowed to what the code shows]
5. §5(d) and §9. Old: seeds 1 and 2 have 7 and 6 `news.told`, "which I did not trace"; §9 lists the
   `examine` refusal as unexplained. New: they leave 0 and 1 chained claims alive at the end of season 2; the
   `examine` line is deleted from §9 and the `inferred` and tellings lines are narrowed to match 1 and 3.
   [probe: chained claims alive 0 / 0 / 1; D_T06 E5]
6. §2.5, new "Provenance" paragraph: source, chain and teller are stored, `record()` re-weights a teller's
   word, the chained half is nearly unused (0 / 0 / 1 alive). [`state/carriers.py:337-379`;
   `decision/options.py:1470-1510`; `fixtures.py:801`; probe; D_T06 E6; `ATTACHMENTS_CROSSCHECK.md` §A]
7. Line shifts from PR #494 (`e093d63`), no change of claim. `fixtures.py` gained 10 lines after 715:
   `:853` to `:863`, `:864` to `:874`, `:778` to `:788`, `:923` to `:933`, `761-864` to `771-874`.
   `rosters.yaml` gained 1 line before 2420: `2423-2445` to `2424-2446`, `2446-2472` to `2447-2473`,
   `2474-2489` to `2475-2490`, `2480-2484` to `2481-2485`, `2484-2485` to `2485-2486`. `world_q.py:2249`
   to `:2374` (`questions_for`); `person_q.py:909` to `:999` (`said_of`). [`git diff a4ca9a5 e093d63` hunks;
   each new line opened]
8. Inquiry yield re-checked against PR #494: no change needed. §1 and §2.9 already describe the FI-02 and
   FI-03 `inquiry` role and trail (`rosters.yaml: inquiry_modules`, `finding_terms`, `covert_kinds`;
   `seam/wrappers/fieldwork.py`; `modules/fieldwork/find.py`), which landed before `a4ca9a5`. #494 changed
   none of `modules/`, `seam/`, `epistemic.py`, `decision/`, `state/` or `verb_table.yaml`, and the control
   run is byte-identical. `modules/fieldwork` is 36 lines (`find.py` 34, `__init__.py` 2) and one entry,
   `fieldwork.find` (`references/module_contracts.yaml:70`).
9. Paths. Old: ctl and probe scripts named by directories outside the repo. New: ctl at
   `proposals/2026-10-22-system-description/ctl/`; probe scripts not committed.
10. History kept as written: §8's "Where the draft appendix A8 was wrong" and round-2 item 2 still say
    `post_remit` executes "at seed 2"; they record what round 2 found, and §0 governs.
11. New `## 0a How it plays`. Departures from the D_T06 draft, each checked at the tree: "M1-M11" is
    M1-M10 (lexicon §3.7 lists ten); "the loop has no ending (ERRATA G17)" and "IN-27 DESIGN-ONLY" are
    replaced by the season's `endings` report (`loop/driver.py:515-518`, `queries/world_q.py:1764`; IN-27
    is built as a read that the realm as built never reaches); the callback's inputs are cited to
    `loop/deliberate.py:119-170`, not to a session note; the options.py veto is `:308-309`, not `:300-307`;
    "a Partial closes the trail for good" reads "for as long as the claim stays in his ledger".

#### Audit fixes

Each line is old -> new, with the line that was re-opened; the number is the audit finding. Figures marked probe
are uncommitted round-3 probes (§9, "Audit-fix pass").

1. Header "attempted": "passed admission; admission refusals are not counted" -> counted at fold entry
   (`loop/resolve.py:377-379`, before the check at `:428-430`) and uncounted only for graded or contested verbs
   (`:1012-1032`), so interview 21 of 32 and reconstruct 6 of 39 attempts were refusals.
2. Partial closure: "terminal", "for good", "permanently" (0a, §3, §5c, §8 trap 3) -> until the claim is evicted
   from his ledger (`epistemic.py:356-365`; `state/ledgers.py:24-32`; `loop/matter.py:321-322` keeps a claim at 0).
3. §0 `post_remit` row: TESTS-ONLY at seed 0 and "which of the two I did not trace" -> the obligee channel (errata
   Part 3 R-13) puts an `inferred` claim in p_npc_070's ledger at tick 0 in seeds 0, 1 and 2, and seed 0's end-of-run
   0 is a death artefact (he died at tick 1; probe), one step past the audit; the §9 "Not confirmed" bullet is deleted.
4. 0a setup: "capability is empty ..., so every investigator rolls the same two dice" -> no `VERB_CAPABILITY` row
   names an inquiry (`rosters.yaml:1229-1231`), so capability would not change the pool.
5. 0a callback: `research` of a held Record listed as something the chooser never does -> dropped, since §3 has the
   chooser forming it.
6. 0a menu cost: "Every act costs one act of budget" and "1 act" -> 1 as a lone scene or a share of an extended
   scene costing 2 for up to 3 acts, "one act of a scene" (errata Part 2 C1).
7. `examine` cause: "no question's subject is a Site", `work` and `restore` only -> formed on the referent, never
   a Site in 160 formations (probe), already named at `verb_table.yaml:1312-1313`, fix REM-22
   (`...remediation-02...:360-379`) unbuilt, `sabotage` added with lines `:988-995`, `:1025-1032`, `:1512-1517`,
   and the fill given as one cause among several for the three (`effects_economy.py:103-104`,
   `rosters.yaml:2631-2632`, no works Record minted; probe).
8. `examine` TESTS-ONLY grade: probe alone -> cites `engine/season/tests/test_fi01_graded_inquiries.py:223-239`.
9. Survival counts: "TESTS-ONLY at seeds 0-1" for the teller record and "skipped or evicted" for seeds 1 and 2 ->
   TESTS-ONLY at seed 0 (`test_told_by_channel.py:1363`), untested at seed 1, "or held by someone who died" added
   (ctl `person.died` 9 / 6 / 11).
10. Provenance paragraph: surveys "find a model of where a belief came from in only one title" -> provenance and
    fabricable, traceable evidence, uploads not in the repo, "Holds" resting on the fabrication half that D_T06
    row 66 grades LACKS in the realm, `20G:235` added.
11. Proposed setup: "logbook, case board or phone log" -> the Obra Dinn book and the Lacuna phone log only (the
    Shadows of Doubt board is player-built, VCD `:784` DOES NOT APPLY).
12. M2: the precedents' quoted "nothing more here" -> Obra Dinn's blurred face (T06 `:53`) and L.A. Noire's music
    stopping (T06 `:248`).
13. IN-47: "built by REM-30 ..., the design stays PROPOSED" as ruled -> to be built, unbuilt (`requirements.yaml:818`),
    D-2 ruled the build proceeds and keeping the design PROPOSED is an [ASSUMPTION] (`remediation-02:552-555`).
14. AX-7 cite: `fieldwork-architecture-and-nonadversarial-play.md:91-92` -> dropped, since it rejects only Obra
    Dinn's global oracle; `verb-coverage-and-gap-fill.md:787-788` stays.
15. Chooser entry: REM-30's `loop/driver.py:355` -> `loop/driver.py:370`, called at `loop/deliberate.py:170`.
16. First season: figures in neither D_T06 nor §9 -> each reproduced by a one-season probe and listed in §9, with
    68.3 defined as claims per ledger (5,329 over 78 persons) and forge as formed 21, minted 4.
17. `research` menu cell: "most formed acts name a person or place" -> formed on the referent, which must be a
    Record to pass, about 108 refused at seed 0 (§4: 115 `finding.none` less 7 Failures).
19. Undefined terms: Site, cohort, View, Sensation and "the precedents' verification scale" -> §1 rows
    (`state/carriers.py:737,435,388`; `cohorts.yaml`), "of the four T06 precedents", and an `examine` trigger cell
    that holds a trigger instead of a grade.
20. Path base: "relative to /home/user/ttrpg" -> unprefixed and `harness/`, `loop/`, `decision/`, `queries/`,
    `state/`, `seam/`, `data/` paths are under `engine/season/`.
21. "Inert at shipped values": listed `examine`, `interview`, `reconstruct` -> a separate line, since they are
    inert by a formation defect or by construction, not by a fixture value.
22. `dispatching_chooser`: "one named person's choosing" -> every person in `overrides`, and the callback also
    receives `auto` (`harness/play_surface.py:14-16,41-51`).
23. §5(d) `examine`: "cannot learn it by going there later" -> "cannot read it off the place later", since a
    `tell` from someone still there is a route.
24. 0a menu: re-stated grades and causes -> points at §0 and §4, and the drifted cells (items 2, 4, 5) are
    corrected, with 0a not restructured.

## 9 Checks

- Opened: `modules/fieldwork/find.py:28-34`; `seam/wrappers/fieldwork.py:46-64`;
  `epistemic.py:329-404,428-686,794-840`; `loop/witness.py:86-315,365,386-391,606,932-966`;
  `decision/options.py:615-625,1338-1448,1513-1545`; `state/ledgers.py:17-32`; `loop/matter.py:312-347`;
  `state/attribution.py:105-265`; `loop/effects_information.py:170-200,258-270,744-830`;
  `verb_table.yaml:207-222,281-313,434-452,533-580,925-948,1127-1200,1321-1438,1495-1505`;
  `rosters.yaml:415-434,1018-1025,1115-1160,2424-2490`;
  `data/fixtures.py:228-247,293,386,414-439,489-527,771-874,933`;
  `modules/social_contest/roll.py:96-125`; `engine/dice_engine/dice_engine.py:153-161,196-239`;
  `seam/wrappers/sigma.py:119-191`; `decision/budget.py:40-61`; `requirements.yaml:169-180`;
  `systems/fieldwork/sim/knots.py:46-97,201-227`; `engine/season/tests/test_fi03_trail.py:1-300,534-625`;
  the lexicon §3.7.
- Ran (`python -I`; scripts not committed):
  - `chain.py` (trail_world): record content, stages, `forgery_quality 1`; removes 0/.333/.667/.667/1;
    bystander claims at 100; Success deposits 3 claims at 50; Partial deposits 2 with `who=None`;
    40 act ids gave S 5, P 7, F 28.
  - `tell.py`: 2 of 12 tellings succeed; told claim at 50 with chain `(p_high,)`, weight 0.5.
  - `cover.py`: deed claims go to `rec:cv`; `seen.who = p_other` for bystander and finder.
  - `seen_by_forger.py`: the forger gets `finding.made` and `seen{who: p_high}` at 100.
  - `resp.py`: 1 trail question and candidates on the forger.
  - `realm.py`, `realm2.py`, `realm3.py` (`build_realm(0)` and `(2)`, two seasons, the ctl recipe):
    inquiry degrees; give subjects; 0 found deposits and 0 chained claims in seed 0; 1 `record.given`
    and 1 `inferred` in seed 2; 250 `finding.none` in seed 0; 0 resolved `examine`; tellings deduped.
  - `examine.py` (round 2, seed 0): `w.acts` 1,407 against `d.resolved` 1,132. 62 `examine` formed, all
    `finding.none`. `finding.none` by verb: research 115, examine 62, surveil 46, interview 21,
    reconstruct 6.
- Round 3 (`python -I`, `build_realm(seed)` for seeds 0, 1 and 2, two seasons, the ctl recipe; scripts not
  committed): `examine` formed 62 / 59 / 39, no `site` operand one of the 322 Sites (seed 0, by act: 45 Rungs,
  15 Persons, 2 Records); found deposits 0 / 0 / 0; ledger sources alive `inferred` 0 / 1 / 1 at the end of two
  seasons; chained claims alive 0 / 0 / 1; `news.told` 4 / 7 / 6; same 83 persons, 322 Sites and 412 Rungs at
  build in all three seeds; `endings` `[]` in both seasons at seed 0; seed 0, one season: p_npc_037 took nine
  fieldwork acts and went from 0 to 187 claims (177 firsthand, 10 `told_by` at 67); a hand-built `examine` of a
  Site where a person stands reached the roll (degree Failure). Re-opened: `rosters.yaml:1145,2424-2490`;
  `decision/options.py:300-309,1043-1049,1470-1545`; `queries/world_q.py:2217-2240,2374,1764`;
  `loop/deliberate.py:119-170`; `harness/play_surface.py:41-52`; `loop/driver.py:101,449-456,510,515-518`;
  `fixtures.py:293,788,801,863,874,933`; `epistemic.py:336-404,932-938`; `loop/witness.py:276-315`.
- Audit-fix pass (`python -I`, `build_realm(seed)`, the ctl recipe; scripts not committed; uncommitted round-3
  probe). Seed 0, one season: 78 persons alive after it holding 5,329 claims (mean 68.3 per ledger); p_npc_037
  took nine fieldwork acts, the next two persons seven each; `research` formed 59 (55 refused at admission, 2
  ineligible, 2 reached the roll, both Partial, both by cohorts, on a Record); `surveil` formed 28 (14
  refused, 14 rolled: 1 Partial, 13 Failures); `examine` formed 30, all refused; `forge` formed 21 (17 refused,
  4 minted); `give` formed 8, all refused; `tell` formed 3 (2 Success, 1 Failure). Seeds 0, 1 and 2, two
  seasons: p_npc_070 holds an `inferred` claim at the end of the first season (tick 0) in all three seeds
  (`act.ineligible` on p_npc_020 at seeds 0 and 1, `revoke.refused` at seed 2) and still holds it at the end of
  the second at seeds 1 and 2; at seed 0 he died at tick 1, so the end-of-run `inferred` count is 0 there. Seed 0 Records after two seasons: `text` 93,
  `faction_sheet` 25, `cover` 19, `petition` 14, `dispensation` 5, no works Record; Sites: dwelling 211,
  harbour 37, seam 37, garrison 37. Re-opened: `loop/resolve.py:372-382,424-432,965-1035`; `epistemic.py:354-365`;
  `state/ledgers.py:17-32`; `loop/matter.py:318-324`; `decision/options.py:1040-1050`; `rosters.yaml:1225-1231,2629-2633`;
  `verb_table.yaml:985-998,1020-1034,1308-1315,1508-1518`; `engine/season/tests/test_fi01_graded_inquiries.py:223-239`;
  `engine/season/tests/test_obligees.py:167`; `engine/season/tests/test_told_by_channel.py:1363`;
  `harness/play_surface.py:8-20,40-56`; `loop/driver.py:353-372`; `loop/deliberate.py:168-171`.
- Round 2, re-opened: `rosters.yaml:1226-1232`; `sigma.py:110-117`; `verb_table.yaml:155-158,300-313,355,900-903`;
  `fixtures.py:486-490`; `epistemic.py:650-656,683-687`; `decision/choose.py:643-657`; `loop/driver.py:454-458`;
  `decision/budget.py:18-22`.
- Enumerated: 2d10 at TN 7 against Ob 2 gives O 0, S 0.07, P 0.19, F 0.74. 6d10 against Ob 2 gives
  O 0.142, S 0.328. The refraction table in 2.4 is computed from the formula.
- Not confirmed:
  - why 40 of 52 forges are refused in seed 0;
  - the seed-1 and seed-2 tellings beyond their surviving chained claims (0 and 1);
  - which binding row emits `tenure.closed` (taken from CROSS C5);
  - `deliberate.py:252-259` (CROSS C1), which I did not find at that path.
