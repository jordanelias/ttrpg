# Content parameters docket, chapter 07: Social contest, Proceedings, fieldwork and investigation

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Measured 2026-11-04 by loading the YAML/Python named below. Paths are repo-relative. Collation only.
Conventions: REQ/OPT/DERIVED/PLAN/PROPOSED-ONLY per brief. "kernel" = `systems/social_contest/sim/contest/` (evaluated, NOT wired to the season loop; `modules/social_contest/roll.py:16-37`).

**RETIRED-KEY re-check (orchestrator correction, ED-IN-0232).** Grepped `modules/social_contest/`, `modules/fieldwork/`, `systems/social_contest/sim/contest/` for `keys.py`, KeyStore, echo transport, emit/consume, "key-based": zero hits. Every row in this file is sourced from non-Key code (loaders, rosters, fixtures, carriers) or from PROPOSED-ONLY proposals, so no row is tagged `RETIRED-KEY`. Residual caveats: (a) kernel rows (Part 0.A #19-21 and the "Kernel input tables" entity) come from the older `social_contest_v30`-era kernel, which is unwired (`modules/social_contest/roll.py:16-37`); the kernel's only substrate import is `engine/substrate/stubwire.py` (wrapper.py:23), which is not a Key file. Treat kernel rows as non-current: live equivalents are the arrangement rows (`engine/season/arrangements.yaml`, 8 proceedings) and `social_contest.roll`. (b) `verb_table.yaml` row text and rosters notes cite `ARCHITECTURE_V2`/#353 prose; those are doc citations, not Key sources.

---
# PART 0 — THE MODULES' OWN ACTIONS / CHOICES (complete)

Neither module draws a player choice itself: both are typed-record-in, typed-record-out functions. Choices live in the season-level verbs/payload keys that reach them. Season-level verbs are another agent's; here are the module entries, their arguments, and every payload key/choice that reaches them.

## 0.A Social contest / Proceedings — module entries and choice surfaces

| # | action / function | who chooses | choice inputs / arguments | preconditions | outputs | cited at |
|---|---|---|---|---|---|---|
| 1 | `social_contest.roll(inp, rng)` — the one module entry (composition row `entry: verb_call`, `verb: tell`) | none: called by host adapter `seam/wrappers/sigma.py::resolve` for prizes `a standing`, `a proposition`, `a matter`, and for graded inquiries `research`/`examine`/`surveil` | `inp: SocialContestInput` (12 fields, Part A below); `rng: Optional[random.Random]` (driver-built, never constructed in module) | host builds record; S27.4 refusal applied by host on returned pair | `Margin(net, ob)` — no band, no winner | modules/social_contest/roll.py:157-166; rosters.yaml `contest_subsystems.prizes`, `graded_inquiries` |
| 2 | `social_contest.obstacle(inp)` — composes the Ob | none (pure) | `opposition` (score; halved), `obstacle_default`, `reception_gain*reception + proof_step*proofs` (subtracted, floored at OB_MIN), `forgery_quality` (added), `obstacle_ceiling`, `ceiling_per_pool`, `pool` | `obstacle_ceiling >= OB_MIN` else `ValueError` | float Ob | modules/social_contest/roll.py:89-154 |
| 3 | `_chance_floor_cap(pool, ceiling)` — per-pool cap | none (pure, cached) | `pool`, `ceiling` | ceiling gives nonzero one-die floor else returns `None` | cap float / None | modules/social_contest/roll.py:64-86 |
| 4 | Effort (advantage) choice on any contested act | the acting person (payload `effort` ∈ non-negative int); computed chooser forms none | `effort` e: fills `1+e` of `interactions_per_scene` slots, brings e copies of fixture `effort_level` into σ | e whole, non-negative, `1+e <= interactions_per_scene` (checked in DELIBERATE) else `Forbidden` | `leverage` for `net_boost` | engine/season/state/carriers.py:601-633; seam/wrappers/sigma.py:177-181; rosters.yaml `advantage_sources` (`effort` only) |
| 5 | Verb choice: `speak` (prize `a matter`) | person | subject = matter on a docket | live occasion at actor's venue whose docket names the subject | `matter.carried/advanced/held/turned` by band | verb_table.yaml:1243 |
| 6 | Verb choice: `argue` (prize `a proposition`) | person | `to` (hearer), argued Proposition | uttered Proposition, hearer with arguer | `argument.won/lost`, `pursuit.moved` by band | verb_table.yaml:133 |
| 7 | Verb choice: `tell` (prize `a standing`) | person | `to`, subject claim | teller holds a claim on subject, hearer with teller | `news.told`, `confidence.broken`, `news.untold` | verb_table.yaml:1346 |
| 8 | Verb choice: `determine` (prize `a proposition`) | bench member (`remit:determine`) | subject (party on docket) | fired Date with a DocketItem; bench conjunct; `bench_quorum` | `matter.determined/undetermined`, `pursuit.moved`; writes disposal per arrangement `disposes` | verb_table.yaml:360; loop/effects_information.py:446 |
| 9 | Verb choice: `interrogate` (prize `a proposition`) | questioner (`remit:determine`) | subject (Detainee) | subject in live `detain`; docketed petition's terms names | `confession.full/made/partial/withheld` | verb_table.yaml:1543 |
| 10 | Verb choice: `arrest` (prize `a standing`) | `remit:dispatch` holder | subject person | subject is a person | `arrest.made/resisted` | verb_table.yaml:171; loop/effects_information.py:1028 |
| 11 | Verb choice: `open_case` | `remit:determine` holder | `subject` (matter, a Person), payload `arrangement` (`DOCKET_ARRANGEMENT`), `petition` (`DOCKET_PETITION`), `record` (case-file id), `stages` | arrangement is a row id whose `disposes` is a Tenure kind `determine` can open; petition is a Record of kind `petition`; matter not already docketed | docket item `{date, matter, arrangement, petition}`; case-file Record kind `text` | verb_table.yaml:1007; loop/effects_information.py:301-379 |
| 12 | Verb choice: `carry` (puts petition before the room, by right) | person | petition Record | holds the Record | `petition.carried`; docket item | verb_table.yaml:108; loop/effects_information.py:383 |
| 13 | Verb choice: `petition` | person | `to` (Person), terms | both sides exist | `petition.filed`, Record kind `petition` | verb_table.yaml:1062; loop/effects_information.py:641 |
| 14 | Verb choice: `convene` | `remit:convene` holder | venue rung | `rank(subject.kind) > person` | `date.scheduled` (Date + ConveningCondition) | verb_table.yaml:287 |
| 15 | Verb choice: `comply` / `evade / defy` | the summoned party | held writ | writ names holder | `compliance.given` / (evade) | verb_table.yaml:227, :449 |
| 16 | Verb choice: `utter`, `commit`, `forge`, `conceal`, `give` (social-adjacent) | person | proposition / record / forgery quality | per row | per row | verb_table.yaml:1850, :209, :500, :251, :603 |
| 17 | Arrangement row choice (which proceeding a matter is heard under) | the `open_case` actor (hand-built only; computed `open_case` writes `None`) | one of 8 arrangement ids | row in `ARRANGEMENTS` | docket `arrangement` | engine/season/data/arrangements.py:233-252; effects_information.py:355-363; verb_table.yaml:1007 |
| 18 | Speech kinds (issue ladder) | speaker at a forensic bench | one of 6 rostered kinds | `genres` ∩ bench genre; `min_rank`; `reachable_bands` cap (demote-only) | band cap (only `impugn_motive` → `[Partial]`) | arrangements.yaml:`speech_kinds` (lines ~56-100); data/arrangements.py:134-153. **UNREAD by game code** (repo-wide grep outside .designs/.audit/proposals: only the loader `engine/season/data/arrangements.py:134-153,238-252` builds `SPEECH_KINDS`; the only other readers are tests `engine/season/tests/test_arrangements.py:69-92` and `test_stress_proceedings_rehost.py:145`; no `loop/`, `queries/`, `decision/` or `seam/` file references it; `hole_register.yaml:3512-3556` records H-153/H-154 rows as blocked on a not-yet-built resolution ladder) |
| 19 | Kernel (NOT WIRED): `build_contest(side_a, side_b, *, venue, adjudicator, stakes, world, use_tracker, degree_extension)` | caller | `venue` ∈ 8 proceedings; `adjudicator` ∈ {expert_judge, crowd, no_adjudicator, panel}; `use_tracker` tri-state | — | `Contest` | systems/social_contest/sim/contest/wrapper.py:110 |
| 20 | Kernel (NOT WIRED): `resolve_contest(contest, *, game, policy_a, policy_b, record)` | caller | `game` ∈ {agon, consensus, negotiation, inquiry} (last three are stubs); policy ∈ 11 (logos, demagogue, courtier, build_then_close, exploiter, fallback, off_ground, advocate, overreacher, staller, counterpuncher) | — | `((band, reason), bout)` — a winner, not a margin | wrapper.py:248, :236; policy.py:56 |
| 21 | Kernel style/interaction choice | contestant | style ∈ {precedent, suppression, vision, insinuation}; derived interaction ∈ {clash, reinforce, cross, tie} | — | — | dictionaries.py:90, :283, :310 |
| 22 | PROPOSED-ONLY (P4): plea (deny / concede fact / concede definition); appear-evade-defy; forum; proofs; advocate; speech kind; move against bench/file; appeal (`appeal_to`); warrant-holder duty | party / bench / warrant holder | see P4 §4.2-4.10 | per P4 | per P4 | proposals/2026-10-29-parliament-and-debate/2026-11-01-social-contest-proposal-4-authority-staged.md:337-497; plan CR-57..CR-65 (workplans/valoria_master_workplan_v10_part3.md:346-356) |

## 0.B Fieldwork / investigation — module entries and choice surfaces

| # | action / function | who chooses | choice inputs / arguments | preconditions | outputs | cited at |
|---|---|---|---|---|---|---|
| 1 | `fieldwork.find(inp)` — the only module entry (composition `fieldwork.find`, `entry: step_call`) | none: RESOLVE's per-act bookkeeping, for an Event of kind `finding.made` | `FieldworkInput(band, items, terms)`; `terms.get(band)` | band has a `finding_terms` row, else uncovers nothing; takes no rng | `Findings(((event_id, terms_shown), ...))` in `(emitted_at, event_id)` order | modules/fieldwork/find.py:28-34; queries/inputs.py:181-210; rosters.yaml `inquiry_modules` |
| 2 | Host builder `fieldwork_input(w, act, event)` / provider `find(w, act, event, *, module_entry)` | none | projects `trail_of` | — | `FieldworkInput` | seam/wrappers/fieldwork.py:49, :64; epistemic.py:368 (`trail_of(w, subject, pid)`) |
| 3 | `research` | investigator | subject Record at a site; payload `effort` | record exists; presence at site (`presence:<site>`) | `finding.made` (O/S/P) or `finding.none` (F); roll via `social_contest.roll` (`graded_inquiries`) | verb_table.yaml:1575; rosters.yaml `graded_inquiries` |
| 4 | `examine` | investigator | subject Site | site exists, actor present | same | verb_table.yaml:1498 |
| 5 | `surveil` | investigator | subject = a rung (place watched) | place exists, actor present (`presence:<rung>`) | same | verb_table.yaml:1598 |
| 6 | `interview` | investigator | person questioned | person exists | `finding.made` (ungraded; module finds nothing — no degree) | verb_table.yaml:1527 |
| 7 | `reconstruct` | investigator | subject | actor holds a claim on subject | `finding.made` (ungraded) | verb_table.yaml:1641 |
| 8 | `thread_read` | investigator | subject Site | `Thread Sensitivity >= 30` (fixture `thread_sensitivity.gate`); `Person.thread_sensitivity` not None | `finding.made` (ungraded) | verb_table.yaml:1623; carriers.py:756 |
| 9 | `survey` | person | subject (faction/person/rung) | coheres under one faction; surveyor has heard of subject | Record kind `faction_sheet` | verb_table.yaml:1304; loop/effects_information.py:663 |
| 10 | `forge` | person | forgery (`default_forgery_quality` fixture = 1) | forger has heard of what he forges | Record + `forgery_quality`; `record.forged` (a `covert_kinds` member) | verb_table.yaml:500; effects_information.py:777 |
| 11 | `conceal` | person | cover | — | `cover.assumed`; Record kind `cover` `[terms]` | verb_table.yaml:251; effects_information.py:286 |

---
# PART A — ENTITY TABLES

## Social-contest action (verb rows that run a contest)  — carrier/loader: engine/season/verb_table.yaml, engine/season/data/verbs.py
Population now: measured 63 verb rows in table; contest-prize rows: `argue`, `determine`, `interrogate` (a proposition); `tell`, `arrest` (a standing); `speak` (a matter); `fight`/`accept` (the body), `march` (a field) belong elsewhere. Graded inquiries (`research`,`examine`,`surveil`) route to `social_contest.roll` via rosters.yaml. Status: AUTHORED (grades: 40 `assumption`, 23 `ruled` table-wide).
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `verb` | string, unique | REQ | HAS | verb_table.yaml (e.g. :133) |
| 2 | identity | `stratum` | enum {uncontested_material, social, binding_decision, contested_physical, movement} (rosters/strata) | REQ | HAS | verb_table.yaml; rosters.yaml `strata` |
| 3 | gate | `eligibility` | list of {own, remit:<act>, hold:<record>, presence:<site/rung>}; never `capability` | REQ | HAS | data/verbs.py:872-878 |
| 4 | gate | `requires` / `requires_typed` | typed requires grammar (`data/requires.py` STEMS/COMPARATORS) | REQ | HAS | data/verbs.py |
| 5 | referent | `referent_class`, `counterparty` | {Office, Record, Rung, Site, Proposition, Person, Detainee} / {to, subject, None} | OPT | HAS | rosters.yaml `referent_classes` |
| 6 | contest | `contests` | prize ∈ {the body, a field, a standing, a proposition, a matter} (`contest_subsystems.prizes`) or none | OPT | HAS | rosters.yaml `contest_subsystems` |
| 7 | contest | capability key a verb draws dice from (`verb_capability`) | map verb→key; only `tell`,`speak`→`copying` | OPT | STUB (2 of 63) | rosters.yaml `verb_capability`; seam/wrappers/sigma.py:109-121 |
| 8 | outcome | `emits` per band (Overwhelming/Success/Partial/Failure) | event kinds | REQ | HAS | verb_table.yaml |
| 9 | outcome | `writes` per band | write_matrix cells | REQ | HAS | verb_table.yaml |
| 10 | grade | `grade` | {ruled, assumption} | REQ | HAS | verb_table.yaml |
Owed:
- `capability` keys for verbs other than `tell`/`speak`: `verb_capability` has 2 rows; VERB_CAPABILITY is replaced by `faculties:` under P4 §3.2 (PROPOSED-ONLY, proposals/2026-10-29-parliament-and-debate/...proposal-4...:73).
- `interrogate` and `arrest` contest cells: plan CP-T05-05 CUT (workplans part12:291).
- Plan rows adding verbs: CR-27 `lie` (part3:177), CR-63 five decision verbs (part3:355), CR-58 consent/`<verb>.unlicensed` (part3:349; "which acts need consent is content (Jordan's)").
Conflicts: roll.py:30-33 says kernel reads a faculty; live path reads `Person.capability` (empty on all but one authored cast entry, cases/exercises/NPC-088.yaml).
Belongs elsewhere: combat/mass-battle prizes (`the body`, `a field`).

## Attribute / skill read by contests  — carrier/loader: engine/season/state/carriers.py:702 (`Person.capability`), seam/wrappers/sigma.py:145-174
Population now: 1 authored cast entry holds `capability` (Carin Vedel, `copying: 3`, cases/exercises/NPC-088.yaml); every other person → fixture `pool_default`. Attribute roster (registry) 9 keys, scale 1-7, default 1: attr.body.{strength,endurance,agility}, attr.mind.{focus,acuity,will}, attr.social.{attunement,charisma,bonds}; no `Person` carrier for them. Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | pool | `Person.capability[key]` | dict key→int; key must be a `verb_capability` value (cast refusal) | OPT | HAS (1 person) | carriers.py:702; harness/corpus_run.py:265, :313-336 |
| 2 | pool | `pool_default` | int | REQ (fixture) | HAS =2 | data/fixtures.py:414 |
| 3 | pool | pool addends (`practice_window`,`practice_step`,`practice_cap`) | ints | REQ (fixture) | HAS 4/2/2 | data/fixtures.py:443-444; sigma.py:124-129 |
| 4 | opposition | subject's score on same key, halved | float or None | DERIVED | — | sigma.py:162-174; roll.py:141 |
| 5 | advantage | `effort_level` | `sigma_leverage.LEVEL_SIGMA` name | REQ (fixture) | HAS "moderate" | data/fixtures.py:431 |
| 6 | attributes | 9 attribute keys with per-person values | int 1-7 | PLAN | NONE on Person | references/descriptor_registry.yaml (attributes); P4 §3.2 |
| 7 | faculties | `faculties:` table (eloquence, reasoning, reading, composure → attribute weights) | weights | PROPOSED-ONLY | NONE | P4 :99-103 |
| 8 | thread | `Person.thread_sensitivity` | int or None | OPT | NONE (None for corpus) | carriers.py:756 |
Owed: person attribute sheets (P4 says 83 persons; unverified here); `faculties:` table; per-row `faculty_weights` — all PROPOSED-ONLY (P4 :130-135, open question Q3). Plan: CR-20 "attribute carrier" in B10-10 (part3:339).
Conflicts: P4 :86-90 says registry nine attributes "no carrier on Person" — consistent with carriers.py; J-13 vs 2026-09-05 ruling on attributes unresolved (P4 :132-135).
Belongs elsewhere: Person identity/characters.

## Social-roll tunables (fixtures the contest reads)  — carrier/loader: engine/season/data/fixtures.py
Population now: 12 social/inquiry fixtures measured below. Status: AUTHORED (all `assumption`/swept)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | obstacle | `obstacle_default` | float | REQ | HAS 2 | fixtures.py:416 |
| 2 | obstacle | `obstacle_ceiling` | float≥OB_MIN or None | REQ | HAS 2 | fixtures.py:419; roll.py:148 |
| 3 | obstacle | `ceiling_per_pool` | bool | REQ | HAS True | fixtures.py:425 |
| 4 | obstacle | `obstacle_refusal_multiple` | float | REQ | HAS 2 | fixtures.py:417 |
| 5 | room | `reception_gain` | float (swept 0/1/2) | REQ | HAS 1.0 | fixtures.py:450 |
| 6 | room | `proof_step` | float (swept 0/.25/.5) | REQ | HAS 0.25 | fixtures.py:452 |
| 7 | forgery | `default_forgery_quality` | int | REQ | HAS 1 | fixtures.py |
| 8 | bench | `bench_quorum` | int swept 1/2/3 | REQ | HAS 1 | fixtures.py:989 |
| 9 | scene | `scene_budget`, `interactions_per_scene`, `extended_scene_cost`, `scenes_per_round` | ints | REQ | HAS 5/3/2/1 | fixtures.py; carriers.py:563 |
| 10 | stages | `record_stages_default`, `record_stage_term` | ints | REQ | HAS 3/1 | fixtures.py; effects_information.py:183-185 |
| 11 | telling | `told_weight`, `told_drift_band`, `told_valence_gain`, `telling_privacy`, `said_slant`, `regard_gain`, `stance_polarity`, `stance_gain` | floats / enums | REQ | HAS .5/.5/.5/0.0/"newest"/.5/"declared"/1.0 | fixtures.py:851; rosters.yaml `said_slants`, `stance_polarities` |
Owed (plan): `lapse number` (CR-55, `[ASSUMPTION; medium; revert: never]`, part3:173); `heritage_gain` shipped 0.5 (CR-31, part3:178); `lie_offered` (CR-27, part3:177); `hearing_step` operand (CP-T05-02 (i), part3:170).

## Venue type (buildings)  — carrier/loader: engine/season/venues.yaml, read by harness/populated.py
Population now: 7 settlement kinds with quarters (Seat 3, City 2, Cathedral-City 2, Fortress-City 2, Fortress 1, Town 2, Village 1 quarters); 42 building rows (Seat 9, City 6, Cathedral-City 6, Fortress-City 6, Fortress 4, Town 7, Village 4); 27 distinct building slugs; 11 institution seats; 2 planned works. Status: AUTHORED (AUTHORED FOR PLAY, ED-IN-0223; works rows `[ASSUMPTION]`)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | settlement kind keys | {Seat, City, Cathedral-City, Fortress-City, Fortress, Town, Village} | REQ | HAS | venues.yaml:47-119 |
| 2 | quarters | `quarters[kind]` | list of slugs (`community` rung) | REQ | HAS | venues.yaml:47-54 |
| 3 | building | `slug` | string, unique within kind | REQ | HAS | venues.yaml:64-119 |
| 4 | building | `name` | string | REQ | HAS | same |
| 5 | building | `quarter` | member of kind's `quarters` | REQ | HAS | same |
| 6 | building | `serves` | list of institution tags (Crown, court, Parliament, Church, Guild, Einhir, Altonian, Löwenritter...) | REQ | HAS | same |
| 7 | seats | `seats[institution]` | geography code (e.g. S-001) verified against geography file | REQ | HAS 11 | venues.yaml:143-154 |
| 8 | seats | `seat_precedence` | ordered list, must equal `seats` keys (refused both ways) | REQ | HAS 11 | venues.yaml:140-141 |
| 9 | works | planned_works `{id, kind: works, plan, at, rung, master, terms}` | plan ∈ rung_kinds/site_kinds; master = offices.yaml seat id | OPT | HAS 2 | venues.yaml:188-198 |
Owed: none stated by loader; no hearing-room / sitting-place attribute exists on a building (a sitting's venue is the `convene` rung, not a building).
Conflicts: none.
Belongs elsewhere: planned_works and settlements geography (settlements scope).

## Arrangement / proceeding shape (closed set)  — carrier/loader: engine/season/arrangements.yaml, engine/season/data/arrangements.py:233-252
Population now: 8 arrangement rows loaded: arbitration, parliamentary_debate, council_of_state, legal_trial, tribunal, interrogation, inquisition_hearing, excommunication_deliberation (all `disposal: bench`; 0 `mutual`, 0 `none`, 0 `declared`). Unseeded per file header: negotiation (+envoys), audience/embassy, appeal, public debate, succession row. Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `id` | string unique | REQ | HAS 8 | data/arrangements.py:158-159 |
| 2 | disposal | `disposal` | enum {bench, mutual, none, declared} (_DISPOSAL_VALUES) | REQ | HAS (all bench) | data/arrangements.py:64, :168 |
| 3 | disposal | `bench_basis` | `none` or `remit_acts` member {issue, determine, confer, revoke, dispatch, convene} | REQ | HAS (all determine) | arrangements.py:170-172; rosters.yaml `remit_acts` |
| 4 | disposal | `quorum` | required iff `disposal: declared`, refused otherwise | REQ-cond | NONE | arrangements.py:210-221 |
| 5 | disposal | `disposes` | `Record` / `none` / `tenure_kinds` member {hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban} | REQ | HAS | arrangements.py:195-199 |
| 6 | disposal | `disposal_reach` | `room`/`body` or `rung_kinds` member {person, hearth, community, settlement, territory, province, duchy, realm} | REQ | HAS | arrangements.py:200-204 |
| 7 | floor | `floor` | `open` / `closed` / `admitted[:remit act]` | REQ | HAS | arrangements.py:117-131 |
| 8 | floor | `venue_min_rank` | `rung_kinds` member | REQ | HAS | arrangements.py:178-180 |
| 9 | record | `records_dissent` | bool | REQ | HAS | arrangements.py:174-177 |
| 10 | time | `term_required` | bool | REQ | HAS | arrangements.py:181-184 |
| 11 | appeal | `appeal_basis` | `none` or remit act | REQ | HAS | arrangements.py:185-187 |
| 12 | latitude | `interposed` | subset of {person, office, document, procedure, ceremony, pair} (rosters `interposition_kinds`) | REQ | HAS | arrangements.py:188-190 |
| 13 | order | `order` | enum {free, rank, alternating, scripted, written_only} (_ORDER_VALUES) | REQ | HAS | arrangements.py:66, :191-192 |
| 14 | evidence | `proofs` | subset of {record, testimony, oath, confession} (rosters `proofs`; may need `performance`) | REQ | HAS | arrangements.py:193-194 |
Row values (measured): venue_min_rank — arbitration hearth, parliamentary_debate duchy, council_of_state duchy, legal_trial/tribunal/inquisition_hearing/excommunication_deliberation settlement, interrogation hearth. disposes — oblige, Record, Record, detain, ban, detain, ban, ban. Exactly 13 keys (14 listed because `floor_basis` is parsed out of `floor`); unknown keys refused (arrangements.py:72-76).
Owed: 5 unseeded games above (arrangements.yaml header; `negotiation` is SC-04, plan part3:172); `excommunication_deliberation` → `disposal: declared`, `quorum: 2` (CR-34, part3:175); P4 adds keys `authority`, `rite`, `faculty_weights`, `appeal_to` and a `rites:` block with 3 entries (PROPOSED-ONLY, P4 :68-69); 13th game "examination" (PROPOSED-ONLY, proceedings 03_PARAMETERS.md PART F.1, ~:744).
Conflicts: loader C-1 check is a REPORT, not a refusal (data/arrangements.py:255-287); `succession` row blocked: no `hold` site in `_disposal` (arrangements.yaml header).
Belongs elsewhere: `rosters.yaml` members `genres`, `tenure_kinds`, `remit_acts`, `rung_kinds` are shared rosters.

## Speech kinds (issue ladder)  — carrier/loader: arrangements.yaml `speech_kinds`, data/arrangements.py:134-153
Population now: 6 of the design's 10: deny, cite_incompatible, impugn_motive, concede_fact, concede_harm, hand_error_back (rosters `ladder_rungs` has the same 6). Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | `id` | string unique | REQ | HAS 6 | arrangements.py:135-137 |
| 2 | fit | `genres` | subset of {forensic, deliberative, epideictic} | OPT | HAS (all `[forensic]`) | arrangements.py:139-140; rosters.yaml `genres` |
| 3 | fit | `min_rank` | `rung_kinds` member | OPT | HAS (all hearth) | arrangements.py:141-144 |
| 4 | cap | `reachable_bands` | subset of the 4 degree labels; `[]` = no cap | OPT | HAS (only impugn_motive `[Partial]`) | arrangements.py:145-147 |
Owed: 4 unrostered kinds (arrangements.yaml speech_kinds header; "ten members, two starred not rostered", plan `19_PLAN.md` step 7 quoted there). P4 also names speech kinds as moves within pleas (P4 :191-193).

## Closed rosters feeding proceedings  — carrier/loader: engine/season/rosters.yaml
| roster | members (measured) |
|---|---|
| genres (3) | forensic, deliberative, epideictic |
| interposition_kinds (6) | person, office, document, procedure, ceremony, pair |
| proofs (4) | record, testimony, oath, confession |
| remit_acts (6) | issue, determine, confer, revoke, dispatch, convene |
| rung_kinds (8) | person, hearth, community, settlement, territory, province, duchy, realm |
| tenure_kinds (10) | hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban |
| ladder_rungs (6) | deny, cite_incompatible, impugn_motive, concede_fact, concede_harm, hand_error_back |
| contest_subsystems.prizes (5) | the body, a field, a standing, a proposition, a matter |
| standing_routes (2) | dominance, prestige |
| advantage_sources (1) | effort |
| stance_polarities (3) | legacy, regard, declared |
| said_slants (2) | newest, valence |
| claim_sources (4) | firsthand, told_by, inferred, firsthand_via_knot |
| degree labels (4) | Overwhelming, Success, Partial, Failure (`dice_engine.py` DEGREE_LABEL) |

## Proposition / claim / docket item inputs  — carrier/loader: carriers.py:898 (Proposition), carriers.py:292 (Claim), World.docket, effects_information.py:189
Population now: runtime carriers, none authored. Status: EMPTY (authored content); schema AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | proposition | `id, mood, subject, predicate, value, when, scope` | frozen dataclass | REQ | none authored | carriers.py:898-908 |
| 2 | docket | `date` | Date id or None | REQ | runtime | effects_information.py:194 |
| 3 | docket | `matter` | person id (or None for empty slot) | REQ | runtime | same |
| 4 | docket | `arrangement` (`DOCKET_ARRANGEMENT`) | arrangement id or None | OPT | None on computed cases | effects_information.py:355-363 |
| 5 | docket | `petition` (`DOCKET_PETITION`) | Record id of kind `petition` or None | OPT | None | same |
| 6 | petition | Record kind `petition`, keys `[terms, to, from]` | rosters `record_kinds` | REQ | runtime | rosters.yaml `record_kinds` |
| 7 | record | `Record.stages` list of `(due_tick, label, act id)` | — | OPT | default 3 stages | effects_information.py:170-186 |
| 8 | record | `Record.forgery_quality` | int | OPT | default 0 | carriers.py:813 |
Owed (plan): record kind `case` (CR-61, part3:352); docket items naming a row (CR-55/56, part3:173-174); `matter.lapsed`.

## Parliament / debate inputs
Population now: arrangement `parliamentary_debate` and `council_of_state` only (rows above); office bodies live in offices.yaml (not read here). Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | proceeding | row `parliamentary_debate` (open floor, records_dissent true, duchy rank, rank order, disposes Record, reach realm) | per Arrangement table | REQ | HAS | arrangements.yaml |
| 2 | bench | judging set = live `hold` Tenures granted the bench basis whose Office `scope_rung` contains venue | derived | DERIVED | — | queries/world_q.py:569 |
| 3 | sitting | `convene` Date + slots `{date, matter:None}` | derived | DERIVED | — | loop/calendar.py; world_q.py:266 |
| 4 | vote | `vote` position / declared-disposal reader | — | PLAN | NONE | plan part12:301 (H-90, unscheduled); CR-34 part3:175 |
| 5 | — | Parliament as constraint / sovereign power | — | PLAN (held) | NONE | part12:301 |
Owed: PROPOSED-ONLY content in proposals/2026-10-29-parliament-and-debate/2026-10-29-parliament-and-debate.md, `...reasons-to-convene.md`, `...resolution-design.md` — not extracted in this pass (files not opened).

## Stance / audience inputs  — carrier/loader: carriers.py:703 (`Person.stance`), queries/world_q.py:676 (`reception`), :736 (`proofs`), :660 (`remove_weight`)
Population now: runtime-derived; no authored audience. Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | stance | `Person.stance` list of tuples | — | OPT | runtime | carriers.py:703 |
| 2 | reception | Σ over bench × deeds × remove_weight × confidence × valence | float signed | DERIVED | — | world_q.py:676-690 |
| 3 | proofs | unmirrored deeds against opponent × remove_weight | float | DERIVED | — | world_q.py:736 |
| 4 | remove | `REMOVE_ORDINAL` order firsthand > knot > told > inferred | ordered list (`data/rosters.py`) | REQ | HAS | world_q.py:660-670 |
| 5 | valence | alignment table `tables.alignment` (verb × pursuit axes) | map | REQ | HAS | rosters.yaml `tables.alignment` |
| 6 | polarity | `stance_polarity`, `stance_gain`, `regard_gain` fixtures | see Social-roll tunables | REQ | HAS | fixtures.py |
| 7 | legitimacy | legitimacy index L per territory | float | PROPOSED-ONLY | NONE | P4 :208-229; plan CR-65 (part3:356) |

## Kernel input tables (NOT WIRED; evaluated, not deleted)  — systems/social_contest/sim/contest/dictionaries.py
Population now: styles 4; interactions 4; adjudicators 4 (expert_judge, crowd, no_adjudicator, panel); faction boosts 7 (church, crown, varfell, hafenmark, restoration, guilds, lowenritter); proceedings 8 (formal_contest, grand_contest, royal_audience, church_tribunal, guild_arbitration, casual_dispute, private_negotiation, personal_appeal), each with fields key,name,exchange_count,role_structure,resistance_modifier,adjudicator_type,track_start,tracker_mode,mechanical_key,flavor,source; trackers 3 (Face, Concentration, PersuasionTrack); games 4. Status: AUTHORED, unreachable from the season loop (roll.py:16-37). Retirement timing is Jordan's (`SM-15`).

---
## Investigation action (module-level and verb-level)  — see Part 0.B; carrier: verb_table.yaml rows 1498-1641, modules/fieldwork/find.py
Population now: 6 inquiry verbs (research, examine, surveil, interview, reconstruct, thread_read) + survey; 3 graded via `social_contest.roll`, 3 ungraded. Status: AUTHORED
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | identity | verb row (same keys as social verb table above) | — | REQ | HAS 6 | verb_table.yaml:1498-1641 |
| 2 | route | `graded_inquiries[verb]` = `{provider: social_contest, module_entry: social_contest.roll}` | verbs research, examine, surveil | REQ | HAS 3 | rosters.yaml `graded_inquiries` |
| 3 | route | `inquiry_modules.findings[<event kind>]` = `{module, provider, module_entry}` | one row: `finding.made` → fieldwork | REQ | HAS 1 | rosters.yaml `inquiry_modules` |
| 4 | route | `undeposited_kinds` | `[finding.none]` | REQ | HAS | rosters.yaml |
Owed (plan B10-14): CP-T06-01 trail from place/alias writes (part3:194); -02 `surveil` finds covert deeds at its place (:197); -03 retry after Partial (:195); -04 refused inquiry teaches actor (:196); -05 `interview` retype so the person answers by own act (:199); -07 cover borrowing another's name (:198); -09 room files covered deed under the hand (:192); CR-29 reach channel/`reach` roster (:193); CP-T06-08 paper burned PARKED on JA-1 (:200).

## Interaction (scene)  — carrier: carriers.py:561 (`Scene`), :636 (`Act`)
Population now: runtime; fixtures only. Status: AUTHORED (fixtures)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | scene | `scene_budget` | int | REQ | 5 | fixtures; carriers.py:563 |
| 2 | scene | `interactions_per_scene` | int | REQ | 3 | fixtures |
| 3 | scene | act `effort` | non-negative int | OPT | none formed by computed chooser | carriers.py:617-633 |
| 4 | scene | `occasion` (Question) | — | DERIVED | — | carriers.py:592 |

## Find / clue / evidence type  — carrier: rosters.yaml `finding_terms`, `observation_terms`, `covert_kinds`, `site_kinds`, `record_kinds`
Population now: finding_terms 3 band rows; observation_terms 4; covert_kinds 1; site_kinds 9; record_kinds 7. Status: PARTIAL
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | terms | `observation_terms` | ordered {stratum, marks, who, why} | REQ | HAS 4 | rosters.yaml |
| 2 | terms | `finding_terms.bands[band]` | band ∈ degree labels; values ⊂ observation_terms | REQ | HAS: Overwhelming/Success `[stratum,marks,who]`; Partial `[stratum,marks]`; Failure none | rosters.yaml; data/rosters.py `_load_finding_terms` |
| 3 | channel | `witness_channels` {co_located, witness_key, document_key, chronicle, post_remit} → claim source; `observation_terms.supplied_by` per channel | — | REQ | HAS 5 | rosters.yaml |
| 4 | trail | `covert_kinds` | verb deed kinds; has `record.forged` | REQ | HAS 1 | rosters.yaml; data/verbs.py `_check_covert_kinds` |
| 5 | site | `site_kinds` | {harbour, seam, body, dwelling, garrison, barracks, archery_range, stable, siege_workshop} | REQ | HAS 9 | rosters.yaml:1506 |
| 6 | record | `record_kinds` with key sets | text[], dispensation[terms,to,at], petition[terms,to,from], works[plan,at], faction_sheet[proposition,members,holdings,seats,head], cover[terms], army[faction,strategy,trained,subformations] | REQ | HAS 7 | rosters.yaml; carriers.py:854 |
| 7 | forgery | `Record.forgery_quality` | int ≥0, added to Ob | OPT | 0 default | carriers.py:813; roll.py:144 |
| 8 | trail item | `TrailItem(event_id, kind, emitted_at)` | derived by `trail_of` | DERIVED | — | queries/inputs.py:181 |
Owed: no site kind for a fieldwork scene (e.g. a library or archive) beyond the 9 above; `why` term never supplied (rosters finding_terms note, `epistemic._term_why`).

## Information carrier (claims, Records, sources, confidence)  — carrier: carriers.py:292 (`Claim`), rosters `claim_sources`
Population now: runtime; fixtures `confidence_default`=100, `claim_decay_per_season`=5. Status: AUTHORED (schema)
| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | claim | `id, holder, subject, predicate, value, when, source, confidence, visibility` (+`round`, `chain`, `doer`) | `source` ∈ claim_sources {firsthand, told_by, inferred, firsthand_via_knot} | REQ | runtime | carriers.py:310-349 |
| 2 | confidence | `confidence_default`, `claim_decay_per_season` | ints | REQ | 100 / 5 | fixtures.py:293 |
| 3 | visibility | `"own"` or circle tuple; `telling_privacy` fixture | — | OPT | 0.0 | carriers.py:318-324 |
| 4 | claim subject | `claim_subject_rules` {actor, per_change, both} | — | REQ | HAS 3 | rosters.yaml |
| 5 | knowledge | `knowledge_kinds` {mundane, thread_substrate} | — | REQ | HAS 2 | rosters.yaml |
| 6 | question | `question_sources` {claim_landed, need} | — | REQ | HAS 2 | rosters.yaml |
Owed (plan): REACH roster row keyed on event kind (CR-29, part3:193); chain-claim counts (CP-T05-03, part3:171).

## Interview inputs
Population now: 1 verb row `interview` (verb_table.yaml:1527): `eligibility [own]`, `emits [finding.made]`, `writes []`, `requires` "the person questioned exists", ungraded, no `contests`. Status: PLACEHOLDER (per plan retype)
Owed: CP-T06-05 retype so the answer is the questioned person's own act, "the answer is a contest" (part3:199); interrogation arrangement row (above) for detainees. ED-921 note (part10:76) concerns old Dialogue Lattice — superseded, not a parameter.

---

Follow-up answers: (2) `speech_kinds`: UNREAD by game code (Part 0.A row 18 gives the grep evidence). (3) Fieldwork cards' home file: `proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-06-fieldwork-and-information.md` (plan handle `cp-fieldwork-and-information`, cards cite `:72-153`); social-contest cards' home is `...-05-social-contest.md` (`cp-social-contest`). Neither was read beyond the plan card rows.

---
# PART B — PROPOSED-ONLY PARAMETERS AND CHOICES (follow-up pass)

Sources (all PROPOSED/REFERENCE; nothing here is read by code): RD = `proposals/2026-10-29-parliament-and-debate/2026-10-29-resolution-design.md` (supersedes PD in part); PD = `...-parliament-and-debate.md`; RC = `...-reasons-to-convene.md`; P03/P04V/P05 = `proposals/2026-09-05-proceedings-subsystem/03_PARAMETERS.md`, `04_VERBS.md`, `05_PROCEDURE.md`. Status lines: PD :3-4, RD :3-4, RC :3, P03 :3, P05 :3; P04V :3 says "RATIFIED AS INTENT" (a status line, not a mechanism). Where live code differs, code wins.

## B.0 Actions / choices added to Part 0 (PROPOSED-ONLY)
| # | action / choice | who chooses | inputs | preconditions | outputs | cited at |
|---|---|---|---|---|---|---|
| 23 | Table a motion: `carry` a petition Record naming a Proposition into the nearest open slot of a Date convened at a council's rung | any person | the motion's Proposition (a seeded goal row's own id in RM1); keys `DOCKET_MOTION`, `DOCKET_FILE` | tabler alive; motion not already satisfied; one live motion per subject | person-less docket item `{date, matter: None, motion, file}` | RD :103-105, :147 (RJ-3) |
| 24 | Convene a council sitting | any `convene`-holder whose seat's rung equals the council's rung (no chair) | venue rung | `convene` in grant | `Date`; `date.scheduled` | RD :109, :187 |
| 25 | Join the council: `oblige` with `binds: council` | the joiner | council seat | joiner's own act; no term | membership via `establishment_of` | RD :109, :145, :188 |
| 26 | Commit / release (vote) | each member | motion Proposition | a commit counts only if made in a season after tabling | live `commit` edges; `commitment.ended` on release | RD :113-115; PD :50-58 |
| 27 | `argue` for or against, with `toward` (pursuit map signed by arguer's own motion term) | arguer | a present member, the motion | co-presence; only Success/Overwhelming moves | pursuits moved along the motion's engaged pursuits | RD :111, :153 |
| 28 | `speak` to the body | any person | docketed matter | live occasion naming the subject; writes nothing at any band today (H-63) | `matter.*` events | PD :113; P04V :44-80 |
| 29 | Owner's licensed act (`confer`, `revoke`, `give`, `requisition`, `transfer`) carrying the motion as a typed operand | the owner | motion id | count of sworn non-imposed council members with a live post-tabling `commit` meets `council_share` | the act's write, or `<verb>.unlicensed` | RD :117-119 |
| 30 | Declare the motion (`determine`, `disposal: declared`, `quorum`) — WITHDRAWN by RD | council chair (withdrawn) | — | — | `resolution` Record (withdrawn) | PD :51; RD :4 |
| 31 | Motion-kind roster (RM2): `utter` binding `subject` and `to` from two classed referents | the utterer | strain query + predicate verb + executing verb per kind | row refused at load without both | motion Proposition | RD :103, :155; PD :67-80 |
| 32 | `speak` kinds (12 named, 10 rostered; `withhold`, `elicit-in-room` starred, not rostered): propose, concede, refute, define, construe, amplify, object, impugn, pre-empt, recapitulate | speaker | kind; aptness by genre, rung, registers, proofs | aptness PRICES (obstacle term `aptness`), never refuses | band + matter movement | P04V :222-284 |
| 33 | Frank-speech licence (Fig 26): goodwill shown first, private, unrepeated, advantage absent | speaker | 4 conditions | all four, else demoted; failure read as hostile / competing / characterizing / bargaining | demotion + named reading | P03 :163-200 |
| 34 | Descend the issue ladder by `speak` at a lower rung (procedural, conjecture, definition, quality); charge ladder (Fig 27, 6 rungs) | speaker | rung | each descent concedes | rung is a fold over the run's `matter.*` emissions, not stored | P05 :97-104; P03 :29, :50 |
| 35 | Choose a register (7 manners) | speaker | register | arrangement `registers[]` admits it | misreading map at deposit | P03 :32; P05 :125-145 (P-16 unresolved) |
| 36 | Appeal | party | `appeal_basis` remit act | `max_depth` cap, typed `Refusal` | nested run | P05 :36-54 |
| 37 | Proceed (nested run) `seam.proceed(proj, venue, matter, arrangement, attendees, depth, max_depth)` | seam | listed args | depth < max_depth (no default, H-87) | `Margin` | P05 :35-56 |
| 38 | P04V investigation rows: `examine`, `interview`, `research`, `reconstruct`, `surveil`; `Thread-Read` unwritten (P-19) | investigator | subject; for `surveil` a declared interval (untypable, no `Tenure.term`, P-04) | per-row requires (contain_path, existence, own_ledger) | `facet.found`, `said.given`, `record.read`, `inference.made`, `watch.kept` | P04V :487-588 |
| 39 | Convene at any rung above `person` (`rank(venue.kind) > rank(person)`) | convener | venue | form 2 ordinal | Date | P03 :327-356 |
| 40 | Roles by edge, not field: party (own `commit`), adjudicator (seat via `confer`), audience (travel), advocate (`commit` to another + `oblige`), witness (`tell`), clerk (holds case Record via `carry`) | the person's own acts | — | — | derived membership | P03 :392-428 |
| 41 | Attend: `move` to the venue, or a writ delivered by `give` | member | venue | co-presence for `argue`; chooser cannot reach `give` (H-229) | presence | PD :122 |

## B.1 Parameters, PROPOSED-ONLY
| # | entity | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | motion | operands `subject`, `to`, later `amount` (no new operand name) | operand roster closed at eight | PROPOSED-ONLY | NONE | RD :103, :192 |
| 2 | motion | docket keys `DOCKET_MOTION`, `DOCKET_FILE` + write-matrix rows | keys | PROPOSED-ONLY | NONE | RD :105, :147 |
| 3 | motion | declared term at least 2 seasons from tabling; lapse = last stage's maturation | int | PROPOSED-ONLY | NONE | RD :147 |
| 4 | motion | lapse number | `[ASSUMPTION; medium; revert: never]` | PLAN | NONE | plan CR-55 (part3:173) |
| 5 | council | one council `Office` per rung in `offices.yaml`: `body`, `rung`, `obligees:` (ladder title-holders in the venue), `holder: null`, remit without `determine`/`convene` | data | PROPOSED-ONLY | NONE | RD :109, :145 |
| 6 | council | `binds` basis `council` (rule at `purview_reaches`, `guard_weight`, `admits_audience` limb 3) | roster member | PROPOSED-ONLY | NONE | RD :109, :185 |
| 7 | council | join term | none (data value) | PROPOSED-ONLY | NONE | RD :109, :188 |
| 8 | count | `council_share` fixture | float, start 0.5, swept {0.5, 0.6, 2/3} | PROPOSED-ONLY | NONE | RD :115, :190 |
| 9 | count | post-tabling rule (a commit counts only if `Tenure.since` > tabling season) | rule | PROPOSED-ONLY | NONE | RD :115; PD :57 |
| 10 | licence | consent row `(executing verb, object kind, council seat, threshold)`; first row a holder's `give` of his last territory | data row, refused at load if verb or seat unknown | PROPOSED-ONLY | NONE | RD :117, :189 |
| 11 | vote | fourth `score_terms` term `motion` (`aim`, `stake`), `motion_gain`, odds fixture | floats; gain 0 first | PROPOSED-ONLY | NONE | RD :113, :152-153, :183 |
| 12 | vote | per-verb polarity: `commit +1`, `release -1`, `argue`/`speak` = sign of arguer's term | ints | PROPOSED-ONLY | NONE | RD :113 |
| 13 | vote | risk appetite and horizon per person | source NOT DECIDED (ED-IN-0304; CR-17) | PROPOSED-ONLY | NONE | RD :113, :154, :184 |
| 14 | speech | clamps on `consequence_pursuits` and the argue step to the authored range (LP1, LP2) | range | PROPOSED-ONLY | NONE | RD :111, :153 |
| 15 | motion kinds | roster rows (kind, strain query, party, predicate verb, executing verb); 6 candidates: fill a seat (`vacancies`), dispose of an ungoverned place (`uncontrolled`), relieve a shortfall (`hunger`, `larders_in_purview`), end/enter a war (`at_war`), censure/restrain (`restrained`, `legitimacy`), dispute a hold (rival `commit`s) | 6 | PROPOSED-ONLY | NONE | PD :67-80; RD :103 |
| 16 | motion kinds | strain band per kind (how low legitimacy is "low") | swept `[ASSUMPTION]`, unruled; kind not seeded until ruled | PROPOSED-ONLY | NONE | PD :80 |
| 17 | motion kinds | independent legitimating trigger of a different claim kind than the strain | rule `[ASSUMPTION; medium]` | PROPOSED-ONLY | NONE | PD :77 |
| 18 | salience | stamped standing occasion / attention-key rank for the sitting question | tier | PROPOSED-ONLY | NONE | PD :78; RD :107 |
| 19 | convening | RL1 `matters_awaiting` stamp; RL2 `convene` reads Rung only from matter-bearing stamps; RL3 distinct refusal kind (e.g. `give.unlicensed`); RL4 petition `to` = holder of the seat governing `from`'s tier; RL5 matter-specific sign; RL6 strain producer; RL7 council join term as periodic reason | levers | PROPOSED-ONLY | NONE | RC :102-110 |
| 20 | convening | instruments: motivation rate, latency, jurisdiction fit, salience | measurements | PROPOSED-ONLY | NONE | RC :114-121 |
| 21 | arrangement key | `registers[]` (subset of 7 manners, Fig 8; roster not in tree) | set | PROPOSED-ONLY; deleted from live 13-key schema | NONE | P03 :483; data/arrangements.py:12-13 |
| 22 | arrangement key | `verdict_reasons` {given, withheld}; `stakes_grade` {terminal, costly, free} | enum | PROPOSED-ONLY; deleted from live schema | NONE | P03 :493-494 |
| 23 | arrangement rows | 5 unseeded games: negotiation (mutual, closed, alternating, costly); negotiation through envoys (one key changed, `pair`); audience/embassy (bench, admitted, ceremony+person+document, scripted, terminal); appeal to authority (bench, admitted, document, written_only, costly); public debate (disposal none, open, free, costly) | rows | PROPOSED-ONLY | NONE | P03 :528-541, E.2 :553-733 |
| 24 | arrangement row | 13th game `examination` (bench, determine, admitted, no dissent, settlement, term_required, appeal none, interposed [procedure, document], scripted, registers [restricted], proofs [testimony], disposes a tenure, withheld, costly) | row | PROPOSED-ONLY | NONE | P03 :750-766 |
| 25 | roster | `proofs` may need a fifth member `performance` (P-13) | roster edit | PROPOSED-ONLY | live has 4 | P03 :775 |
| 26 | roster | `proofs` Fig 6 set {record, testimony, oath, ordeal, confession, sign} vs live {record, testimony, oath, confession} | set | PROPOSED-ONLY | live 4 | P03 :30 |
| 27 | derived | `latitude` (from `interposed`), `genre` (from bench remit), `ladder` (from genre), `bench`, `parties`, `floor` membership, eloquence-vs-consequence | Queries, not keys | DERIVED | NONE | P03 :497-508 |
| 28 | figure keys | `provenance` {ascribed, accumulated, performed, staged} (Fig 3); `route` {prestige, dominance} (Fig 25; live `standing_routes` has both); step grade {TERMINAL, COSTLY, FREE} (Fig 11/21); issue ladder (Fig 5); discoverable claim predicates (Fig 19) | enums | PROPOSED-ONLY | partial | P03 :27-50 |
| 29 | speech kinds | 10 rostered kinds (list in B.0 #32) vs live 6 ids | roster | PROPOSED-ONLY | live roster has 6 different ids | P04V :235-242 |
| 30 | obstacle term | `aptness` price | composed and floored like other terms | PROPOSED-ONLY | NONE in `roll.py:obstacle` | P04V :281 |
| 31 | determine row | `quorum` cardinality conjunct; degree-keyed writes `Tenure.since`, `Tenure.degree` | row | PROPOSED-ONLY (live row already degree-keyed) | HAS | P04V :311-333 |
| 32 | procedure | `max_depth` for appeals | caller-supplied, no default | PROPOSED-ONLY | NONE | P05 :37, :54 |
| 33 | procedure | `order` values {free, rank, alternating, scripted, written_only} | enum | live | HAS | P05 :18; data/arrangements.py:66 |
| 34 | investigation | five rows keyed on the ladder's four bands; per-act cost/risk | table | PROPOSED-ONLY | live rows emit `finding.made`/`finding.none` | P04V :453-488, :524-588 |

Owed (stated by the sources): RM1 mechanism slice RJ-0a..RJ-9 and RM2 (RJ-10, RJ-11) with hash and falsifier per step (RD :141-155); Layer-1 hunks RH-1 (score term) and RH-3 (`council` basis) (RD :183, :185, :195 call 5); two-parliaments split (RD :117, :195 call 3); no-convener failure mode (RD :107); offence supply upstream of trials (RC :112); contrary motions, several motions per subject, weighted votes, sortition, Parliamentary Stay named not built (RD :157, :232).
Conflicts: (a) PD's Speaker, council-seat `determine`, `resolution` and `evade / defy` route are withdrawn by RD (PD :4). (b) P03 PART D lists 15 keys; live loader has 13 (`data/arrangements.py:12-13`). (c) P04V's speech-kind roster vs live `ladder_rungs` ids (rosters.yaml; arrangements.yaml:56+). (d) P04V investigation emission kinds vs live `finding.made`/`finding.none` (verb_table.yaml:1498-1641). (e) PD :51 says shipped `bench_quorum` is 1 and cannot refuse; `data/fixtures.py:989` agrees.
Belongs elsewhere: risk appetite and horizon per person (characters, CR-17); council seat rows in `offices.yaml` and `populated.py:1427-1483` holderless seat (governance); legitimacy barrier index in `queries/cache` (P4 §3.6, factions).
