# Shared reference for the ten tutorials: glossary, id key, action economy, time, resources, comparison handles

Repo `jordanelias/ttrpg` at HEAD `a4ca9a5`. Every locator was opened for this part. Abbreviations: `es/` = `engine/season/`;
**CR** `es/state/carriers.py`; **RY** `es/rosters.yaml`; **VT** `es/verb_table.yaml`; **FX** `es/data/fixtures.py`;
**WQ** `es/queries/world_q.py`; **DE** `engine/dice_engine/dice_engine.py`; **DR** `references/descriptor_registry.yaml`;
**ctl0/ctl1** the control run `scratchpad/ctl/realm_seed{0,1}_2seasons.txt` (attempted/ok, two seasons). Grades are ERRATA G1's
only: **RUNS-IN-LOOP** (a non-refusal outcome inside `SeasonDriver.season` over `build_realm`), **at control** (runs, inert at the
shipped value), **TESTS-ONLY** (wired, executes only under tests/fixtures/oracles, or zero successes in the realm run), **DESIGN-ONLY**
(no executing code). A refusal firing is not the verb executing. **[PROPOSED]** marks anything only a proposal describes.
Where a tutorial and the code disagree, the code wins; the cases are listed at the end.

## 1 Glossary

One entry per primitive or component the tutorials use, alphabetical. "Kinds" and closed sets are given as the code holds them.

| term | what it is | where |
|---|---|---|
| **Act** | One intended application of a verb by one person: `id, actor, verb, changes, reads, contests, payload, stratum, obstacle, pool, scene, via` (`via` = the seat exercised). The chooser forms it; RESOLVE folds it. | CR:598-612 |
| **affiliation** | See *conviction*. | — |
| **alignment cell** | A verb's value in [−1, +1] on one value axis; the chooser's pursuit term reads it. 40 of 53 verbs carry cells (T02). | RY `tables.alignment` (:2916) |
| **ambition** | A live `commit` to a Proposition of mood `OUGHT` (a creed, an organization goal, a personal want). | WQ:1817 |
| **attention tier** | The order in which a person's questions are taken: 0 ambition referent, 1 own tenure or purview, 2 valued deed, 3 need, 4 rest. | WQ:2092-2135 |
| **axis** | One of seven bipolar value axes onto which pursuits are projected: hierarchical_equal, precedent_substantive, partisan_equitable, selfish_selfless, rigid_flexible, grandiose_humble, deontological_instrumental. `exposure` is refused as an axis name. | DR:168-178; RY:498-503, :526-528 |
| **barrier** | A step that writes under its own token. The season is CALENDAR → MATTER → 5 × (DELIBERATE → RESOLVE → ENCOUNTER → WITNESS) → CENSUS → `tick += 1`. | `es/loop/driver.py:447-515` |
| **bench** | `judging_set`: live holders of seats granted `determine` whose scope contains the venue; quorum 1. | WQ:439; FX:913 |
| **body** | `Person.body`, an integer on `condition_scale` 1000; floors 800 / 500 / 100 (full_operations, limited, withdrawal_only) each cost one scene action. | CR:679; FX:217; RY:2562-2564; `es/decision/budget.py:64-83` |
| **Calamity** | Canon: the historical event, a rendered-side over-drawing of threads by the Einhir's sustained Weaving. **Code defines none**: `check_calamity_threshold` is struck, "no carrier". | `canon/philosophy/08_history.md:13-22`; `systems/threadwork/sim/rendering.py:33` |
| **CALENDAR** | Step 1, once per season: due Dates fire; a sitting with a holder opens an empty docket slot. Own write class. | `es/loop/calendar.py:28`; `es/data/matrix.py:53-57` |
| **candidate** | One formable option `(verb, subject, operands)` for the current question; the chooser scores and orders candidates. | CR:524-528; `es/decision/options.py` `opening_set` |
| **CENSUS** | Final step: individuates a person named by an order but absent from the world (weight 1, `contain` only); writes in the MATTER class. 0 individuations in ctl0. | `es/loop/census.py:35, :103`; `es/data/matrix.py:60-62`; ctl0 |
| **channel** (witness) | A rule admitting a person to an Event. Five, strongest first: `co_located`, `witness_key`, `document_key`, `chronicle`, `post_remit`; the first admitting channel sets the claim's source. | RY:378-419 |
| **Claim** | One belief in its holder's own ledger: `holder, subject, predicate, value, when, source, confidence, visibility, round`, plus keyword `chain` (who told it, origin first) and `doer`. Sources: firsthand, told_by, inferred, firsthand_via_knot. | CR:291-348; RY:434 |
| **Coherence** | Threadwork's cost carrier: a distance from the human equilibrium, held as a resting point plus an elastic displacement 0-6; resting point 6+ = crossed (`HUMAN_BAND_LIMIT` 5); elastic returns 6 per season of rest in equilibrium. No Person field; oracle only (TESTS-ONLY). | `systems/threadwork/sim/coherence.py:115-133, :374`; `canon/philosophy/09_terminology.md:101` |
| **cohort** | A Person of `weight > 1` ("the people of" a settlement); 37 in the realm at weight 2, no pursuits. The only eaters. | CR:726-730; `es/cohorts.yaml`; ctl0 "pursuits empty 37" |
| **commit** | Tenure kind: membership in or adherence to a Proposition. A faction is its Proposition plus its live `commit`s; there is no stored Faction entity. | WQ:1365; `es/queries/faction_q.py:84-95` |
| **contests / prize** | A verb row's `contests:` names a prize, and the prize routes the act to a resolver: `the body` → combat, `a field` → mass battle (fought at ENCOUNTER, declared `Declared`), `a standing`, `a proposition`, `a matter` → `social_contest.roll`. Seven rows contest (`tell`, `argue`, `determine`, `speak`, `fight`, `accept`, `march`). | RY:1270-1325; ERRATA G3 |
| **conviction / affiliation** | `Person.conviction`: intensity 0-5 per affiliation, five affiliations (solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics). A conviction crisis at scar ≥ 3 folds or destroys one. | CR:655-690; DR:204-218; `es/queries/person_q.py:575-581, :680` |
| **degree** | The outcome band of a contested act. Ladder (social path, graded inquiries): margin = net − Ob; Failure < 0 ≤ Partial < 1 ≤ Success < 3 ≤ Overwhelming. Combat: Felled / Wounded / Untouched off the *subject's* wound tracker. Field: Declared / Won / Lost / Unopposed. | DE:286-301; RY:803, :888; `es/seam/ladder.py:136, :209` |
| **ENCOUNTER** | Per-round step after RESOLVE: declared `march` acts are fought; shares RESOLVE's write class. | `es/loop/driver.py:475`; `es/data/matrix.py:72`; RY:1283 |
| **establishment** | The persons holding a live `oblige` to a seat; a Query, stored nowhere. | WQ:1739 |
| **Event** | The occurrence (not a message): `id, kind, changes, causes, emitted_at, degree, observed`. No actor, no target; `causes` must be non-empty. Refusals are Events. | CR:232-287 |
| **Exposure** | **Code defines no Exposure mechanic.** The word is refused as an axis name ("three senses of one word"); canon uses it for presence near a drifting being, which develops Thread Sensitivity. Tutorials' WT "exposure" is DESIGN-ONLY. | RY:526-528; `canon/philosophy/07_drift.md:311-315` |
| **gate** (write gate) | `World.write`, which accepts a write only with a Token and a write-matrix row (40 rows + 6 retired). | `es/state/gate.py:66`; `es/write_matrix.yaml` (ERRATA G4) |
| **hold** | Tenure kind of possession, object ∈ {Office, Rung, Record, Proposition}; one live holder per object. Every live hold adds 1 scene action. | RY:164; `es/decision/budget.py:57-58` |
| **ledger** | `Person.ledger`, the person's list of Claims; cap 200, evicting the lowest `confidence × (when+1)`; only WITNESS deposits. | FX:231; `es/state/ledgers.py:17-32` |
| **Locked Zone** | Canon: a place where becoming has been precluded, persisting indefinitely. **Code defines none** (no identifier in `engine/`, `modules/` or `systems/` Python). | `canon/philosophy/09_terminology.md:117`; `08_history.md:147` |
| **MATTER** | The actorless step, once per season before any scene: term lapse, claim decay, larder draw, body fall (0 shipped), yield, travel-leg end, wear, ageing/illness (0 shipped). | `es/loop/matter.py:165-709` (:296-303, :317, :513-520, :549, :585-616) |
| **matter kind** | A registered good: grain, salt, timber, ore, coin. Open roster; an unregistered kind raises. | RY:1409-1420 |
| **oblige** | Tenure kind: service to a seat, the joiner's own act; an act-opened edge carries a Term of `oblige_term` 4 seasons, renewed by a `transfer` covering `upkeep` (default 1). The two authored at world-gen carry no term. | VT:878-899; FX:882, :895; WQ:1768 |
| **Ob / TN / pool** | Pool = number of d10s (social default 2); TN = the success face, always 7; Ob = the number net is compared against. Faces 1 → −1, 2-6 → 0, 7-9 → +1, 10 → +2. Social Ob default 2, ceiling 2, floor 1. | DE:150-206; FX:414-419; `modules/social_contest/roll.py:103-113` |
| **Observation** | One recorded read `(subject, predicate, value)`, "what a Claim would be if the reader wrote one"; rides `Event.observed`. A larder shortfall is carried as one. | `es/data/requires.py:168-177`; CR:279; `es/loop/matter.py:469-474` |
| **Office / seat** | A post at a rung with `remit_acts, scope_rung, binds, conferral, revocation, upkeep, body, faction`. Realm: 31 authored + `off_npc_084`. A seat is an Office someone holds. | CR:899-912; `es/offices.yaml`; ERRATA C5 |
| **Person** | The only actor type: `id, name, weight, capability, stance, pursuits, ledger, body, born, scar, conviction, travel_leg, tenures`. `capability` is empty on every realm person. | CR:655-680; ctl0 "capability nonempty 0" |
| **Proposition** | An immutable uttered statement `id, mood, subject, predicate, value, when, scope`. **Mood** is a plain string with no roster; the tree mints `OUGHT` (default of `utter`), `HOLDS` (leaderless factions) and reads `WAR` (`at_war`). | CR:849-858; `es/loop/effects_information.py:1028`; `es/harness/populated.py:941`; `es/queries/faction_q.py:210-216` |
| **purview** | Where a seat's writ runs: its own rung and every rung below, plus the ground of seats whose holders owe it a live `oblige`, one edge deep. Asked of the seat (`Act.via`), never of the actor. | `es/state/gate.py:353-400` |
| **pursuit** | One of 15 weighted wants on `Person.pursuits` (virtue, honour, liberty, justice, wealth, reputation, scholastics, stability, individuality, community, doctrine, happiness, family, love, stewardship). | DR:136-152; RY:462 |
| **question** | The one item a person deliberates on in a round: `id, source, referents, about, classes`; sources `claim_landed`, `need`; aggregation keeps the first. | CR:469; RY:595; WQ:2249 |
| **Record** | A world-side document `id, rung, kind, forgery_quality, subject_matter, ttl, stages, matured`. Kinds: text, dispensation, petition, works, faction_sheet, cover. | CR:751-760; RY:222-234 |
| **refusal kinds** | Three fold-level kinds `act.ineligible` (actor gone or eligibility declined), `act.refused` (fallback), `attempt.refused` (S27.4, Ob > 2 × pool); plus each row's own `emits_on_refusal` (e.g. `travel.blocked`). A refusal costs the scene action. | RY:1168-1188; VT:875; ERRATA G10 |
| **remit** | The acts a seat licenses: issue, determine, confer, revoke, dispatch, convene. The holder exercises a snapshot taken at seating. `remit_default` ("NOT CANON, A TESTING FIXTURE") is applied in the shipped realm. | RY:314-332; CR:119-158; CROSS C4 |
| **Rung** | "THE HOLON": one class for every place, fields `id, kind, stores, sites, records, dates, envelope, yield`; eight kinds person < hearth < community < settlement < territory < province < duchy < realm. No province rung is built. | CR:1040-1073; RY:259 |
| **scar** | `Person.scar`, a count per pursuit or affiliation raised in witnesses of a violating act, at RESOLVE/ENCOUNTER (never at WITNESS). 2 = weight shift (inert, `scar_weight_shift` 0), 3 = crisis. | `es/loop/resolve.py:597`; `es/queries/person_q.py:575-581`; FX:707 |
| **Scene** | A bundle of 1-3 acts released together; cost 1, or `extended_scene_cost` 2 if it holds more than one act. | CR:553-594; FX:488-489 |
| **Site** | Built fabric on a rung `id, rung, kind, condition` (0-1000); kinds harbour, seam, body, dwelling, garrison. | CR:737-741; RY:1383 |
| **stance** | Rows `(referent, valence −5..+5, weight 0..5)`; `stance_toward` = Σ valence × weight. Written at runtime only by a lost field (grudge, morale) and `forgive`. | `es/queries/person_q.py:68-77`; `es/loop/effects_combat.py:303-306, :449` |
| **stratum** | A verb's resolution-order class; RESOLVE sorts by it, then a seeded hash. Five: movement, binding_decision, contested_physical, uncontested_material, social. | RY:436-444; `es/loop/resolve.py:57-58` |
| **Tenure** | "THE ONE EDGE", owned by its subject: `id, subject, object, kind, since, until, degree, payload, term`. Ten kinds: hold, contain, commit, oblige, succeed, tie, knot, reside, detain, ban. A Term `(matures_at, declared_by)` is closed by MATTER. | CR:43-107; RY:101-127 |
| **Thread Sensitivity** | A practitioner's access to threadwork, 0-100+; Thread Pool Score = floor(TS/10). **No Person field** (H-85); the oracle reads `.ts` off any object. | DR:64-65; `systems/threadwork/sim/operations.py:235-247` |
| **token** | `Token(write_class, tick)`, minted only by `mint_token` in the driver, one per barrier; write classes CALENDAR, MATTER, ACTS, INTERIOR (WITNESS). | `es/state/gate.py:66`; `es/loop/driver.py:80-98, :447-514`; `es/data/matrix.py:53-57` |
| **typed precondition** | A row's `requires_typed` cell, evaluated against the world to `True / False / UNKNOWN` (only True admits). Seven forms: existence, scalar_threshold, contain_path, cardinality, relation, own_ledger, basis. Rows without a cell use a hand predicate. | RY:2172-2209; `es/data/requires.py:179-195`; ERRATA G3 |
| **verb row** | One line of the closed menu: `verb, stratum, eligibility, requires, requires_typed, contests, writes, emits, emits_on_refusal, grade`. 53 rows; 47 resolvable; menu 46. | VT:10-20, :863-877; ERRATA G3 |
| **weight** | `Person.weight`, headcount in queries: 1 for a named person, 2 for a realm cohort; no runtime writer. | CR:659; WQ:1262 |
| **WITNESS** | Per-round step: fans each Event to the observers each channel admits and deposits refracted Claims; `finding.none` goes to nobody. | `es/loop/witness.py:234-315`; `es/loop/driver.py:510`; RY:1145 |
| **"with"** | A typed-cell stem: two persons in the same place by `place_of`. The world answers it; the person side always reads UNKNOWN, so a hearer's absence refuses at the fold. | `es/data/requires.py:775-793`; WQ:2717-2727 |
| **writes / emits** | `writes:` (per degree) names write-matrix rows the effect may touch; `emits:` the Event kinds on success, `emits_on_refusal` on refusal. | VT:10-20 |

## 2 Process-id key

Ids that appear in the tutorials. Several prefixes are overloaded across documents; the source column says which family is meant.

| id | means | owner / where defined |
|---|---|---|
| **H-NN** | A hole-register row: a named unknown or injected value, with `kind, owner, grade, default, site, sweep, unblocks, cite`. Fixture lines carry `[JUSTIFIED: ... H-NN]`. | `es/hole_register.yaml:1-15`; read by `es/register.py` |
| **R-01..R-09** (requirements) | THE NINE ruled requirements the loop is graded against (3 met, 5 partial, 1 not met). | `es/requirements.yaml:190, :503 ... :1327` |
| **R-01..R-29** (verbs) | Reconciliation rulings of the verbs proposal, overriding any lexicon body. Distinguish from the requirements by document. [PROPOSED] | `proposals/2026-10-16-verbs/...-03-...md:225-231` |
| **REM-NN** | One remediation item (40 indexed; some numbers cut, e.g. REM-43). [PROPOSED] | `proposals/2026-10-21-v9-remediation/...-03-...md:498`; `...-01-...md:69-72` |
| **RB-0..RB-5** | Remediation batches (RB-0 paper, RB-1 instruments, RB-2a/b formation and scarcity, RB-3 scale builds, RB-4 Layer 1 + NERS, RB-5 hunger). [PROPOSED] | `...-01-...md:34`; ERRATA G18 |
| **JQ-1..JQ-6** | Remediation's open forks for Jordan (JQ-1 how much of a person is the draw; JQ-6 hunger ratio). | `...-04-...md:14, :85` |
| **D-1, D-2** | Rulings Jordan recorded 2026-10-21 in the remediation (D-2 yes: RB-3 builds IN-46/IN-47). | `...-01-...md:18, :38-39` |
| **D-V1..D-V21** | Verbs-proposal items surviving the five answer-it-first tests ("Items for Jordan"). | `...-verbs-04-...md:140-146` |
| **M-…** | Overloaded. (a) Verbs proposal: a named mechanic a verb waits on, numbered per lane (`M-WT-1`, `MB-M1`, `M-EDICT`; 127 named). (b) Research lane files: a missing area, `M-<lane>-N`. (c) `M1` = the milestone. (d) `M-7`, `M-10`: measurements from the proceedings plan. | `...-verbs-04-...md:119-121`; `research/by_lane/IN_infrastructure.md:582-590`; `es/tests/test_sc01_obstacle_ceiling.py:16` |
| **J-T1..J-T4** | Verbs-proposal decisions on persons (J-T1 source of personal inputs; J-T2 the tenth attribute; J-T3 kin; J-T4 do attributes change). | `...-verbs-01-...md:49-53, :332-339` |
| **J-NN, J-C-N** | Plan-level Jordan asks (J-13 personal source; J-C-2 troops as stock or people; J-C-9 population). | `research/by_lane/00_COMPARATIVE_ANALYSIS.md:527, :534` |
| **ED-NNNN / ED-<LANE>-NNNN** | Editorial-ledger items: flat sequence frozen; new ones lane-tagged (`ED-IN-0261`). | `registers/editorial_ledger*.jsonl` (CLAUDE.md §4) |
| **PP-NNN** | Patch-register entries. | `registers/patch_register_active.yaml` |
| **IN-NN, PC-NN, MB-NN, SC-NN, FI-NN, GV/FA…** (no `G`) | v9 workplan positions by lane (IN-46 played fight, IN-47 character-sheet space, PC-06 #445 recommendations). | `workplans/valoria_master_workplan_v9.md:269, :294` |
| **K-N, K-<lane>-N** | Key recommendations: `K-1..K-6` of proposal #445 (K-1 build the Combatant from the person); `K-IN-1` etc. in the research lane files. | `proposals/2026-09-30-character-and-play-surface/09_the_character_sheet.md:128`; `research/by_lane/IN_infrastructure.md:966-971` |
| **T-<lane>-N** | A research throughline (T-IN-1 "persons differ in what they want, not in what they can do"). | `research/by_lane/IN_infrastructure.md:483-488` |
| **SM-N** | Open items carried from the v8 plan (SM-15: when the SC kernel retires, Jordan's). | `workplans/valoria_master_workplan_v9_part4.md:142-149` |
| **L1-01, L1-04; L1-6** | `L1-01`/`L1-04` = `architecture/meta/01_AXIOMS.md` / `04_CODE_ARCHITECTURE.md`; `L1-6` = a Layer-1 conformance fork ruled 2026-10-21 (option B: `subsistence` leaves `Sensation`). | `00_COMPARATIVE_ANALYSIS.md:18`; `...-v9-remediation-01-...md:40` |
| **PC-G01.., NP-G01.., MB-/FA-/SC-/GV-/FI-/TW-/EC-/WT-Gnn** | Verb gap-register rows per lane (PC 40, NP 41 …); evidence, not rules. A gap id is never a built rule (CROSS C13). | `...-verbs-19-...md:12` (and parts 20-23) |
| **Tier T1-T4** | Evidence tier: T1 code the season loop runs; T2 code outside the loop; T3 a ratified spec, a v9 position or a proposal ratified as intent; T4 design intent only. | `...-verbs-01-...md:20-22` |
| **Evidence grades** | Suite grades: ERRATA G1 (above). In-tree row grades: `ruled`, `measured`, `assumption`, `absent` (hole register; verb rows use ruled/assumption/absent); remediation grade `paper`; tags `[CHECKED]`, `[ASSUMPTION]`, `[MEMORY]` (unchecked). | ERRATA G1; `es/hole_register.yaml` `grade:`; VT `grade:`; `...-v9-remediation-01-...md:5` |

## 3 Action economy

**The budget** (`es/decision/budget.py:19-20, :57-61`) is in **scene actions**, recomputed at each deliberation:
`budget = max(1, 5 + 1 × live hold tenures − body floors below − 1 × travel legs this season)`.
Hold-minters: `create_record`, `issue`, `open_case`, `petition`, `survey`, `forge`, `utter`, and `conceal` (via a cover Record) (CROSS C1).

**How it is spent** (CROSS C1, the authoritative ruling; code checked):
- `choose` packs the ordered candidates greedily into chunks of up to 3 (`interactions_per_scene`, FX:488); a chunk of more than one
  act is extended and costs 2 (FX:489); if only 1 action is left the chunk is cut to one act (`es/decision/choose.py:643-657`).
- The driver runs 5 rounds (`rounds = scene_budget`, `es/loop/driver.py:449, :456`) and releases at most `scenes_per_round` = 1 scene
  per round (FX:511), charging `Scene.cost` against the remainder (`es/loop/deliberate.py:250-259`; CR:593-594).
- Result: budget 5 → 2+2+1 = **7 acts**; budget 6 → 2+2+2 = **9**; a travel leg costs a budget-6 holder one act (9 → 7). Ceiling:
  5 scenes × 2 = 10 actions. What `deliberate.py:89-97` calls unspendable is a sixth *scene*, not the sixth *action*.
- Acts per person-season observed: about 6.3-8.0 depending on basis (ctl0: 1,132 acts reached the fold, 74 persons alive at the end,
  2 seasons ≈ 7.6). Name the basis when quoting.
- A refused act still costs its place and leaves an `actor` observation in the actor's own ledger (later vetoable as known-false);
  a refused act stays retryable, a succeeded opportunity leaves the queue (T02 §2.7; `es/decision/options.py:308`).

**Per subsystem.** Every verb costs its place in a scene; no verb has a separate action price. Material costs are listed where they
exist. Odds are for the shipped default (pool 2, Ob 2) unless stated. ctl0 = attempted/ok at seed 0; [seed 1] where it differs in kind.

| subsystem | verbs (row names) | extra cost | resolver and typical odds | what each degree buys | ctl0 |
|---|---|---|---|---|---|
| SC | `tell`, `speak`, `argue`, `determine`; `petition`, `open_case`, `carry`, `convene`, `commit`, `utter` | `determine`, `open_case` need `remit:determine`; `convene` `remit:convene` | one d10 roll; pool 2 vs Ob 2: F 74 / P 19 / S 7 / O 0 % (T01:160, Table A :171). `speak` with a favourable room: Ob 1 → 42 / 32 / 25 / 1 | `tell`: F nothing deposited, P drifted told claim, S/O told claim. `argue`: S/O shift hearer's pursuits by step × 0.1 (`DEGREE_STEP` −1/0/+1/+2). `determine`: P opens the disposal (`oblige`/`detain`/`ban`), S/O also shift the judge's pursuits | tell 23/4; speak 3/3; argue 0 rolled; determine 0 [1/1]; petition 42/14; open_case 12/6 |
| FI | graded `research`, `examine`, `surveil`; ungraded `interview`, `reconstruct`; makers `survey`, `forge`, `conceal`, `create_record`; `give` | maker verbs mint a Record (+1 hold, +1 budget) | graded inquiries take the social roll (pool 2, Ob 2 + forgery, ≤ 2) | O/S uncover `stratum, marks, who`; P `stratum, marks`; F nothing (RY:2446-2472) | research 14/7; surveil 30/5; interview 32/11; reconstruct 39/33; survey 57/13; forge 52/12; conceal 19/19; create_record 87/87; give 16/0 |
| PC | `fight`, `accept` (contest *the body*), `challenge` (writes nothing) | none | beat-level duel, Gaussian roll per exchange, pool `max(5, history+6)` = 9, Ob history/2 = 1.5; season reads the subject: mirror fight Felled 48.5 / Wounded 28 / Untouched 23.5 % (T03:202, n = 400) | Felled: subject removed, every tenure naming him closed. Wounded: body scaled by health remaining. Untouched: nothing. The actor is never written | fight 7/4; accept 18/11; challenge 23/6 |
| MB | `march` (contests *a field*) | `remit:dispatch` | declared at RESOLVE (band `Declared`), fought at ENCOUNTER by `mass_battle.resolve_field` | Won / Lost / Unopposed; a lost field writes grudge and morale stance rows | march 21 declared, 25 `march.refused`, 0 fields |
| GV | `issue`, `confer`, `revoke`, `dispatch`, `convene` (remit); `release`, `oblige`, `establish`, `succeed` | upkeep 1 per obligee per term, paid by `transfer` | no dice; typed precondition decides | one outcome or a refusal | release 45/3; issue 6/5; dispatch 18/6; revoke 6/0; oblige 0 [24/22]; confer 0 [5/1] |
| EC | `transfer` (default amount 1, FX:559), `requisition`, `work`, `restore`, `found`, `build`, `sabotage` | `found`: {grain 10} for hearth/community; `build`: {timber 10} per Site (RY:1532-1538) | no dice | — | transfer 45/1; requisition 2/0; work 77/0; restore 23/0; found 24/0; build 19/0; sabotage 34/0 |
| FA | `survey`, `covenant`, `seize`, `sabotage`; FA rides GV seats and `march` | `seize` needs `issue` and purview | no dice | — | survey 57/13; covenant 13/0 |
| WT | `move`, `migrate` | each leg −1 budget for the rest of the season | no dice | — | move 42/16; migrate 81/0 |
| NP | `tend`, `train`, `forgive`, `give`, `commit` | none | no dice | `tend` body to 1000 (requires *with*) | forgive 1/1; tend 34/0; train 38/0; commit 61/0 |
| TW | none in the loop (`thread_read` not resolvable) | Coherence by scale (Object/Personal 0, Relational/Field −1, Structural/Foundational −2; −1 more on P/F) | oracle only: pool `spirit×2 + min(3, history+3) + ts//10` = 14 by default | — | 0 (TESTS-ONLY) |

## 4 Time scales

| scale | length | where |
|---|---|---|
| **season = tick** | One `SeasonDriver.season` call; `w.tick += 1` is the only clock advance. Ruled as the unit a character plays ("5 scenes for a character to play per season"). No year exists: `season_of_year` is `None` while `season_factor_draw` is `()`. | `es/loop/driver.py:447-515`; FX:494, :469; WQ:951-957 |
| **round** | 5 per season (DELIBERATE → RESOLVE → ENCOUNTER → WITNESS); a driver-local index, not world state; `Claim.round` says which round a claim landed. | `es/loop/driver.py:449-456`; CR:294-308 |
| **scene** | ≤ 1 released per person per round; 1-3 acts. | FX:488-489, :511 |
| **MATTER cadence** | Once per season, before round 0; CALENDAR before it, CENSUS after round 4. MATTER at tick 0 is the first MATTER (CROSS C3). | `es/loop/driver.py:447-448, :514` |
| **combat** | `fight` ≤ 12 turns; each turn one engagement "~10 s"; an engagement ≤ 24 beats and ≤ 4 exchanges (`BURST_MAX`); resolved whole inside RESOLVE. | `modules/combat/wrapper.py:487, :504, :111-118, :463`; `modules/combat/config.py:112` |
| **mass battle** | One battle turn = up to 18 ticks = 3 phases × 6 ticks; one call at ENCOUNTER. No in-world duration stated for a tick. | `modules/mass_battle/orchestration.py:1815-1818`; `modules/mass_battle/config.py:155` |
| **terms** | `oblige` 4 seasons (renewable by upkeep `transfer`); Record stages 3, one season apart (a cover is live about 3 seasons); a convened Date is due at `tick + 1` by default. | FX:882, :524-525; `es/loop/effects_governance.py:363` |
| **claim decay** | −5 confidence per claim per season at MATTER, floored at 0: a firsthand claim at 100 reaches 0 after 20 seasons unless evicted first. | FX:293; `es/loop/matter.py:317` |
| **wear** | Condition −10 per season for harbour, seam and the `body` site row; dwelling and garrison 0. With no repair, yield reaches 0 only at tick 100 (CROSS C9). | RY:1465-1470; `es/loop/matter.py:663` |
| **body / hunger / age** | `body_step` 0, `age_step` 0.0, `illness_rate` 0.0: no seasonal body change at control. | FX:594, :606-607; `es/loop/matter.py:513-520, :549` |
| **Coherence** | Elastic return 6 per season of rest in equilibrium (oracle). | `systems/threadwork/sim/coherence.py:133, :374` |
| **world clock** | None in the loop. The MS track (0-100, −1 per year, start 60) has no live caller. [designed, deleted] | `systems/overview/sim/ms_track.py:25, :45`; ERRATA G17 |

## 5 Resources

Everything stored is an integer on a carrier; there is no currency in play. "Conserved" means a two-sided move: what leaves one carrier
arrives at another (`es/loop/effects_economy.py:215-219`; `es/loop/effects_governance.py:432-435`).

| resource | carrier | sources | sinks | rules and absences | where |
|---|---|---|---|---|---|
| **grain, salt** | `Rung.stores` | MATTER yield of a harbour Site: grain 40, salt 30 × condition/1000 × season factor (1.0), credited to the Site's rung | MATTER larder draw: each cohort wants weight × {grain 2, salt 1} from the nearest rung up its presence chain holding the kind; `found` stake {grain 10} | `transfer`/`requisition` conserved; named persons do not eat; a shortfall becomes an Observation to governors. Stores accumulate in the run (`stores.changed` 111, `yield.taken` 74 in ctl0) | RY:2511-2514, :1554-1556; `es/loop/matter.py:556-616`; WQ:902, :1017 |
| **ore, timber** | `Rung.stores` | seam Site: ore 50, timber 10 | `build`: {timber 10} consumed one-sided into the fabric; harbour/seam/dwelling/garrison works cost | not eaten; a draw against them raises | RY:2515-2517, :1532-1538, :1551-1553; `es/loop/effects_founding.py:206` |
| **coin** | — | none | none | registered matter kind only; no site yields it, no shipped world holds it; used by a harness probe | RY:1420; ERRATA C7 |
| **condition** | `Site.condition` 0-1000 | `work`/`restore` (TESTS-ONLY: 77/0, 23/0), bounded by a works ceiling | MATTER wear; `sabotage` (TESTS-ONLY) | band floors emit crossings (harbour 800/100; seam 700/50) | RY:2554-2560; WQ:382 |
| **body** | `Person.body` 0-1000 | `tend` → 1000 (TESTS-ONLY, 0/34) | combat Wounded (scaled), Felled (death); hunger at `body_step` (0 shipped) | every realm death is combat (ERRATA G9) | `es/loop/effects_combat.py:371`; FX:594, :624 |
| **stance** | `Person.stance` rows | seeded at build; a lost field adds grudge (valence −1) and morale rows (no field fought) | `forgive` drops rows (1/1) | nothing else writes it at runtime | `es/loop/effects_combat.py:278-306, :431-450` |
| **confidence** | `Claim.confidence` | WITNESS deposit at 100, refracted by remove and dissent (`refraction_gain` 0.5) | decay 5 per season; eviction over cap 200 | 11,869 deposits, 5,329 decays in ctl0 | FX:231, :293, :864 |
| **scene budget** | per person-season | base 5; +1 per live hold | body bands, travel legs, every act's place (cost 1 or 2) | not carried over; reset each season | `es/decision/budget.py:57-61` |
| **Coherence** | oracle store (`world.practitioners` or a module dict) | elastic recovery 6/season; a restorative working returns displacement to the mender (`coherence_restored`) | workings cost by scale | no Person field; no loop reader | `systems/threadwork/sim/coherence.py:141-151`; `systems/threadwork/sim/operations.py:214-217` |
| **stores (seat treasury)** | the seat's own `Rung.stores` | `requisition` (conserved, from a rung in purview) | upkeep `transfer` to obligees | no Treasury class; a territory seat's treasury yields nothing | `es/loop/effects_governance.py:426-464` |

Absent in code: coin flow, prices, trade, credit, tax, crafting, troop stocks (DESIGN-ONLY; T08 §7, ERRATA C7).

## 6 Comparison handles: Valoria on the repo's own axes

The axes are those of *Twenty Games, One Frame* ("20G"), an uploaded document that is not in the tree; the repo's own table of
Valoria's cells is `research/by_lane/00_COMPARATIVE_ANALYSIS.md:307-316` (axes 1-7 numbered, clock count and legibility in one row).
The tree states no definitions; each axis is read here as the file applies it. No other game is compared.

| axis | as built (code at `a4ca9a5`) | as proposed [PROPOSED] |
|---|---|---|
| **1 population resolution** | 46 named persons at weight 1 plus 37 cohorts, each one Person at weight 2; population is Σ weight over `reside` edges; weight has no runtime writer, so cohorts never change size (CR:659; WQ:1262; COMP:309) | population grows at CENSUS to `capacity` (J-C-9, COMP:534); hunger binds settlements (RB-5, `...-v9-remediation-03-...md:193`) |
| **2 named-agent cardinality** | 46, closed "for now" (ED-WR-0011, COMP:37); CENSUS individuation exists and fired 0 times (ctl0) | unchanged in the proposals read; births have no position (COMP:37) |
| **3 contested object** | the body (`fight`), a standing / proposition / matter (SC), seats (`confer`/`revoke`), stores (`requisition`); a field is declared but never fought (ctl0); labour and time uncontested (COMP:311) | land by occupation (IN-13, COMP:311); troops levied from settlements (J-C-2, COMP:527; verbs R-01 `levy`) |
| **4 player position** | none: no player interface; every person is a chooser (ERRATA G16) | embedded: "for a player character the player IS the decision procedure" (`architecture/meta/04_CODE_ARCHITECTURE.md:844-846`); IN-46 played fight, IN-47 character-sheet space (D-2) |
| **5 control channel** | a verb and its subject from the menu for one question per round; seats add remit acts; a person never commands another (VT; `es/decision/options.py`); COMP's ladder: rung 1 present, rung 4 partly (computed `open_case`/`determine`), rungs 2-3 absent (COMP:313) | rung 4's vote over commitments blocked on J-4; rung 2 (zone) absent in the plan (COMP:313) |
| **6 coupling latency** | an Event reaches observers' ledgers at WITNESS in the same round and can shape the next round's question (`es/loop/driver.py:510`); telling carries belief onward (4 of 1,270 claims, COMP:314); no lagged cohort | a lagged population (J-C-9, COMP:534) |
| **7 durability / ending** | persistent with no ending condition; `victory` (MS = 0 → Post-Calamity; all factions dissolved → Anarchy) was deleted (`references/module_contracts.yaml:675-680`; ERRATA G17) | a relational victory as a Query over seats (IN-27, COMP:315, :327) |
| **clock count** | one world clock, `w.tick` (seasons), with five rounds as a driver-local sub-index; combat turns and battle ticks run to completion inside one step (auto-resolve); the MS world clock has no caller (CR:305-308; ms_track.py:45). COMP counts "two clocks, auto-resolve only" (COMP:316) | a paused, played fight (IN-46) would give the second clock a player (COMP:316) |
| **legibility** | no surface: the chooser sees verb identity, not odds, opponent, place, witnesses or clock (T02 §2.4); odds exist in closed form (`sigma_leverage.p_success`) and are shown to no one; COMP: "legibility empty" (COMP:316) | Layer 1 says "No state is hidden from the player" (`architecture/meta/01_AXIOMS.md:301-302`), split against its own §C.11 (COMP:36); IN-47 |

COMP = `research/by_lane/00_COMPARATIVE_ANALYSIS.md`.

## Discrepancies found

1. **Budget above 5 treated as disputed.** T01:9, :65, :218-219, T08:33-36 and `overview_v2.md:199-200` say spending a budget over 5
   is disputed in the tree. The code settles it: `deliberate.py:250-259` charges each released scene's cost against the whole remainder
   and `choose.py:643-657` packs against that cost budget, so budget 6 → 9 acts. `deliberate.py:89-97` describes a sixth *scene* as
   unspendable, which stays true. CROSS C1 governs.
2. **Acts per season.** T08:36 says "about 8–10 acts a season (ERRATA G11)". CROSS C1: about 6.3–8.0 by basis (ctl0: 1,132 acts
   reached the fold over 2 seasons).
3. **"Up to 5 scene actions".** T07:7 ("picks up to 5 scene actions per season") and T04:9-10 ("5 scenes of up to 3 acts") misstate the
   budget: it is `max(1, 5 + holds − bands − legs)` actions, at most 5 scenes and 10 actions, and budget 5 buys 7 acts.
4. **Grade definition.** T07:27-29 defines the grades as the draft did ("RUNS-IN-LOOP = the season loop reaches it"), which CROSS C12
   replaces with ERRATA G1. The tutorial's own grades for threadwork come out the same.
5. **Tenure kinds locator.** T02:45 cites `state/carriers.py:77` for the ten kinds; the class is there but the kind list is
   `rosters.yaml:127` (`open: true`, :103). The list itself agrees.
6. **Remit roster called closed.** T09:47 calls the remit a "closed roster"; the flag is `open: true` (RY:316) while the source line
   says "CLOSED" (RY:315). The tree contradicts itself (CROSS C4); T08:61 states it correctly.
7. **Affiliation count inside the tree.** `rosters.yaml:553` says `affiliation_roster` has "count 4"; the registry the loader reads
   says count 5 and lists five (DR:206-214). T02:38 ("5 affiliations") agrees with the registry.

## Checks

Opened: CR:43-107, :232-348, :469-612, :655-760, :849-912, :1040-1073; RY:101-262, :314-462, :498-566, :595, :784-888, :1168-1190,
:1270-1325, :1376-1557, :2172-2209, :2491-2566; FX `grep` of 40 constants (lines cited above); `es/decision/budget.py:15-84`;
`es/loop/deliberate.py:86-98, :242-262`; `es/decision/choose.py:640-660`; `es/loop/driver.py:1-12, :80-98, :447-515`;
`es/data/matrix.py:53-72`; `es/state/gate.py:66-72, :353-358`; `es/data/requires.py:168-195, :770-793`; WQ:945-962, :2092-2100,
:2705-2735, :1739-1742; DE:284-301; `es/loop/matter.py` anchors (`grep`); `es/loop/effects_*.py` conservation and stance `grep`;
DR:136-218; `modules/combat/wrapper.py:111-118, :463, :487-504`; `modules/combat/config.py:112`; `modules/mass_battle/orchestration.py:1810-1820`;
`modules/mass_battle/config.py:150-160`; `systems/threadwork/sim/coherence.py:115-133, :374`; `systems/overview/sim/ms_track.py:25, :45`;
canon `09_terminology.md:77-117`, `08_history.md:13-24`, `07_drift.md:311-315`; `architecture/meta/04_CODE_ARCHITECTURE.md:844-846`;
`01_AXIOMS.md:301-302`; `references/module_contracts.yaml:675-680`; COMP:10-39, :290-336; proposal headers named in §2. `grep` of
`engine/`, `modules/`, `systems/` Python for Calamity/Locked Zone carriers (only the struck `rendering.py` function) and for `coin`.
Counts from ctl0/ctl1 as printed. T01-T10 §1 tables read as of 22:07; tutorials were being edited, so their line numbers may move.
