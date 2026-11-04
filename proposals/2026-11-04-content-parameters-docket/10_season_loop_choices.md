# Content parameters docket, chapter 10: Season loop: phases, decision points, choices

## Status: PROPOSED (2026-11-04). Collation of what code and the active plan call for; reference under CLAUDE.md §0.05, not a mechanism; merging ratifies nothing.
## Lane: IN

Part of `00_MASTER_DOCKET.md`; read its legend first.

---

Paths relative to `/home/user/ttrpg/engine/season/` unless absolute. Counts measured by loading code (2026-11-04).
Key-substrate re-check (orchestrator correction): `engine/substrate/` holds no keys.py/KeyStore; grep of `loop/ decision/ seam/ queries/ epistemic.py harness/play_surface.py` for KeyStore / keys.py / echo transport / emit-consume / adjudicator found NO live source. Channel names `witness_key` / `document_key` (rosters.yaml `witness_channels`) are LIVE roster names over `knot`/`hold` Tenures, not the retired Key substrate. The only `echo` hit is the `total` fan-out mode described as "the echo model" in `data/fixtures.py` comments (history). No row below is `RETIRED-KEY`.

Measured: verbs in `VERB_TABLE` = 63 (62 in `resolvable_verbs()`, `loop/driver.py:101`); `REQUIRES_PREDICATES` = 9 {confer, convene, dispatch, establish, interrogate, oblige, release, revoke, succeed} (`loop/predicates.py`); `EFFECTS` = 48 (`loop/effects.py`); `DEFAULT_FIXTURES` keys = 86 (`data/fixtures.py:213`); Step enum = 7, WriteClass = 4 (`data/matrix.py`).

## SEASON PHASE / STEP  — carrier/loader: `loop/driver.py:251` `SeasonDriver`, `season()` at `:388`
Population now: 7 steps bound onto the class (`loop/driver.py:575-592`); 4 barriers (CALENDAR=1, MATTER=2, RESOLVE=3 [shared by ENCOUNTER], WITNESS=4 [shared by CENSUS]). Status: AUTHORED (code)

Order inside `season()` (`loop/driver.py:465-537`): CALENDAR(once) -> MATTER(once) -> `rounds = fixtures.scene_budget` times { re-freeze; DELIBERATE -> RESOLVE -> ENCOUNTER -> realised-set bookkeeping -> append to log -> WITNESS } -> CENSUS(once) -> `endings_reached` read -> `w.tick += 1`. Returns `dict(acts, events, rounds, deposits, hash, endings)` (`:549`). Caller supplies `choose`, `question`, `actorless`, `contest_max_depth` (no default; `:433-455`).

| # | step | token (WriteClass) | inputs from content | choice offered (who) | returns | file:line |
|---|---|---|---|---|---|---|
| 1 | CALENDAR | CALENDAR | `w.dates` (due_at == tick, holder, venue) | engine, none (fire-and-lapse if vacant, fire-as-sitting if held) | list[Event] (`date.fired`, `docket.formed`) | `loop/calendar.py:28` |
| 2 | MATTER | MATTER | `actorless` events; tenure `term.matures_at`; claims (decay `claim_decay_per_season`); `wear_per_season`, `band_floors`, `site_yield`, `subsistence_weight`, body/age/illness fixtures; travel legs; settlements `subsist`/`produce` step_calls | engine, none (clocks only) | list[Event] (`term.matured`, `tenure.closed`, `claim.decayed`, `body.changed`, `stores.changed`, `yield.taken`, `travel.ended`, `condition.worn`, `standing.band_crossed`) | `loop/matter.py:284` |
| 3 | DELIBERATE | none (a map) | per person: `questions` (barrier-2 projection), Sensation, View, budget | PERSON/PLAYER via `choose` (see choice table) | list[Act] | `loop/deliberate.py:69` |
| 4 | RESOLVE | ACTS | acts; verb_table rows; `strata` order; `obstacle_refusal_multiple`; `condition_scale`; `contest_max_depth` | engine, none (fold per act; contests go to seam) | list[Event] | `loop/resolve.py:968` |
| 5 | ENCOUNTER | ACTS | Events of the round with degree `Declared` (`march`) | engine, none | list[Event] | `loop/encounter.py:43` |
| 6 | WITNESS | INTERIOR | round's Events (+ CALENDAR/MATTER events in round 0); `fan_out_mode`, `ledger_cap`, `confidence_default`, `claim_subject_rule`, `refraction_gain`, `telling_privacy`, `observation_deposit_mode` | engine, none (channel predicates decide who learns) | int deposits | `loop/witness.py:318` |
| 7 | CENSUS | MATTER | `person.demanded` events this tick; `age_at_build` | engine, none (individuates only a demanded id) | None (writes `person.individuated`) | `loop/census.py:35` |

Owed: none code-side. Season-level fixtures the loop needs from content authoring are in the FIXTURES table below.
Conflicts: `loop/driver.py:252` class docstring says "Six steps, four barriers" while the file header and `season()` bind seven (ENCOUNTER added; barrier count unchanged).
Belongs elsewhere: verb rows (`verb_table.yaml`); MATTER's per-site/body tables (`rosters.yaml` tables `site_yield`, `band_floors`, `wear_per_season`, `capacity_floor`, `works_cost`) -> settlements/world docket.

## DECISION: QUESTION  — carrier/loader: `queries/world_q.py:3340` `questions_for`, `decision/questions.py:22,53,87`
Population now: 2 closed sources (`rosters.yaml: question_sources` = [claim_landed, need], ordered); 7 referent classes {Office, Record, Rung, Site, Proposition, Person, Detainee}; occasion-only classes {Office, Rung, Detainee}. Status: AUTHORED (code + roster)

| # | step | parameter / input | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | question source | `claim_landed`: a claim in own ledger landed since last deliberation whose subject/place/named content is in `reach(w,p)` | roster `question_sources` | DERIVED | HAS | `queries/world_q.py:3395-3410` |
| 2 | question source | `need`: a live `commit` to an OUGHT Proposition (ambition, `goals.yaml` 38 rows) with unmet `aim_state` | roster | DERIVED | HAS | `queries/world_q.py:3416-3422` |
| 3 | sitting / docket / standing-crossed questions (claim_landed, no third source) | fired sittings with docketed matter on a bench he sits; docketed matters with own `case.opened`/`petition.carried` claim; own standing crossing | — | DERIVED | HAS | `world_q.py:291,375,3315` |
| 4 | standing occasions stamped on first question | vacancies, seats told of, writs held, held Records, places told of, larders in purview, own referents of declared class, works sites, detainees | classes above | DERIVED | HAS | `world_q.py:3535-3560` |
| 5 | ordering | `attention_key` 5 tiers (ambition referents, own tenure/purview, deed valence, `need`, rest) | tiers 0-4 | DERIVED | HAS | `world_q.py:3183` |
| 6 | aggregation (which question reaches View) | fixture `question_aggregation_rule` | enum {first, all, one_per_source} (`rosters.yaml: question_aggregation`, ordered) | REQ (fixture) | `first` | `decision/questions.py:53`, `loop/deliberate.py:114` |
| 7 | view builder | fixture `view_k` K; rule | enum {recent, highest_confidence, question_relevant} (`rosters.yaml: view_builder_rules`); K int | REQ | K=12; rule default `recent` | `decision/questions.py:87`, `loop/deliberate.py:84` |

Owed: `view_builder_rules` has no fixture key in `DEFAULT_FIXTURES` (rule param `rule="recent"` defaulted in `assemble`, `decision/questions.py:22`; DELIBERATE passes none, `loop/deliberate.py:123`).
Conflicts: none.
Belongs elsewhere: ambitions/goals rows (`goals.yaml`, `npcs.yaml`).

## DECISION: OPTION SET (opening set)  — carrier/loader: `decision/options.py:59` `opening_set`
Population now: formed per person per deliberation from all 63 verbs; filtered by clauses below. Status: AUTHORED (code)

Returns `list[Candidate(verb, subject, operands)]`. Who chooses: engine forms it; nobody chooses membership. Filters, in order (all person-side):

| # | filter | input from content | domain / closed set | now | file:line |
|---|---|---|---|---|---|
| 1 | verb withheld | fixture `withheld_verbs` (names must exist in verb table else `Forbidden`) | subset of 63 verbs | HAS (non-empty tuple) | `options.py:119-135` |
| 2 | eligibility | verb row `eligible:` kinds; person's Tenures (`hold` granted_acts) | `eligibility_kinds` {own, remit, hold, presence}; `presence` always declines (H-33) | HAS | `options.py:495` |
| 3 | own-state precondition | typed `requires` stems in `OWN_STATE_STEMS` vs person's own body/ledger | — | HAS | `options.py:146-157` |
| 4 | deontological refusal | fixture `refusal_axis`; person projected weight; roster `pursuit_axes.refusing_pole` | axis in 7 `pursuit_axes`; pole {-1} authored for `deontological_instrumental` only | `refusal_axis=None` (off) | `options.py:452,475` |
| 5 | held-document / held-edge / own-stance / own-hold / own-title declines | `rosters.yaml`: `held_document_declines`(1: conceal->cover), `held_edge_declines`(1: commit), `own_stance_declines`(1: forgive), `own_hold_declines`(2: destroy_record, give), `own_title_declines`(1: succeed) | per roster | HAS | `options.py:160-190` |
| 6 | referents | question referents by verb's `referent` class; `terms_sourced`(commit), `warrant_sourced`(seize, arrest), `vocation_sourced`(train: kind) | rosters | HAS | `options.py:166-230` |
| 7 | referent_named | verb row flag; ledger names | — | HAS | `options.py:235` |
| 8 | operands derivable | `requires_operands` 10 {actor, subject, from, to, site, kind, amount, floor, return_kind, return_amount}; fixtures `default_store_kind`, `default_transfer_amount`, `default_return_kind`; `shortfall_sourced_operands`(kind, amount), `known_person_operands`(to), `record_sourced_operands`(3) | rosters | HAS | `options.py:965,1143,1190` |
| 9 | known-false belief | person's own claims contradicting the verb `requires`; `told_weight`/`rank_gain`/`regard_gain`/`record_gain` weighting | — | HAS | `options.py:1426-1480`, `epistemic.py:72` |
| 10 | seats | `exercisable_seats`; several seats -> one Candidate per seat (`VIA`) | — | HAS | `options.py:566` |

Owed: none code-side.
Conflicts: `decision/options.py:59` docstring "FIVE/clauses" and `person_side_eligible` docstring partly stale (history paragraphs say remit declines; code admits, `options.py:495`).
Belongs elsewhere: verb rows, `requires` grammar, affiliations.

## DECISION: CHOOSER (engine-side NPC choice policy)  — carrier/loader: `decision/choose.py:358` `make_chooser`
Population now: one shipped policy (§F2 score + sampled order + scene packing). Status: AUTHORED (code); weights are authored-content inputs.

Who chooses: ENGINE POLICY for every non-seated person; a seated PLAYER callback overrides one person id (`harness/play_surface.py:41`). Score per candidate `= pursuit + stance` (`choose.py:129`):
- pursuit = `damp * Σ_axis axis_w[axis] * align(verb, axis)`; `axis_w = project(p, scar_weight_shift)` (15 convictions -> 7 axes via `pursuit_projection`); `damp = 1/(1+confliction_weight*confliction(p))` (`choose.py:115,147`).
- stance = `(1+stance_gain) * stance_arm`, arm by `stance_polarity` (`choose.py:54,89`).
- order = Plackett-Luce sample, noise keyed `(person, verb, subject)`, `choice_temperature` tau (`choose.py:192,301`); tau=0 -> deterministic by score then (verb, subject) (`choose.py:350`).
- pack: `pack_scenes` by `scene_packing_rule`, bounded by budget cost (`choose.py:514`); then `declare_intents` by `intent_disclosure` (`choose.py:436`).

| # | group | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|---|
| 1 | person input | `Person.pursuits` (15 convictions) | roster `pursuits` = {virtue, honour, liberty, justice, wealth, reputation, scholastics, stability, individuality, community, doctrine, happiness, family, love, stewardship} (15) | REQ per person | per npcs/characters docket | `queries/person_q.py:744,810`; `decision/options.py:413` |
| 2 | person input | stance / regard (ledger-derived; `regard_gain`, `judged_gain`, `told_valence_gain`) | floats | DERIVED | fixtures HAS (0.5) | `queries/person_q.py:70,393` |
| 3 | table | `alignment`: verb x axis cells | 7 axes {precedent_substantive, grandiose_humble, selfish_selfless, hierarchical_equal, partisan_equitable, deontological_instrumental, rigid_flexible}; 90 cells measured; 41 of 63 verbs celled; 22 uncelled verbs: argue, arrest, assign_troops, carry, conceal, covenant, disband_unit, discharge_troops, examine, forgive, form_unit, interrogate, interview, order_unit, pardon, raze, recruit, sabotage, tell, tend, thread_read, train; 5 non-verb `deed:*` keys | OPT (sparse default 0.0) | PARTIAL | `rosters.yaml tables.alignment`; `data/verbs.py` `ALIGNMENT` |
| 4 | table | `pursuit_projection`: 15 convictions x 7 axes | cells | OPT (default 0.0) | 15 rows HAS | `rosters.yaml tables.pursuit_projection` |
| 5 | fixture | `choice_temperature` | float >=0 | REQ | 0.1 | `choose.py:301` |
| 6 | fixture | `stance_polarity` | enum {legacy, regard, declared} (`stance_polarities`) | REQ | declared | `choose.py:92` |
| 7 | fixture | `stance_gain` | float >=0 | REQ | 1.0 | `choose.py:81` |
| 8 | fixture | `confliction_weight` | float >=0 | REQ | 0 | `choose.py:121` |
| 9 | fixture | `scar_weight_shift` | float | REQ | 0 | `choose.py:125` |
| 10 | fixture | `scene_packing_rule` | enum {greedy, one_per_scene, by_subject} | REQ | greedy | `choose.py:536` |
| 11 | fixture | `interactions_per_scene` | int or None | REQ | 3 | `choose.py:544`, `deliberate.py:211` |
| 12 | fixture | `extended_scene_cost` | int | REQ | 2 | `choose.py:588`, `deliberate.py:117` |
| 13 | fixture | `intent_disclosure` | chance [0,1] | REQ | 0.0 | `choose.py:462` |
| 14 | fixture | `refusal_axis` | one of 7 axes or None | REQ | None | `options.py:119` |
| 15 | fixture | `withheld_verbs` | subset of verb table | REQ | tuple present | `options.py:132` |
| 16 | goal use | ambitions -> `need` questions; salience = cosine(crisis_weights, org expectations); `goals.yaml` 38 rows | — | REQ upstream | see goals docket | `world_q.py:2544,3183` |
| 17 | stance_polarity `legacy` | stance from `stance_toward` | — | OPT arm | — | `person_q.py:70` |

Owed: 22 verbs with no `alignment` cell score pursuit 0 (sparse default 0.0, `rosters.yaml tables.alignment.default_cell`); `uncelled` note exists for `recruit` (ED-IN-0306 phase 2).
Conflicts: `decision/options.py:413` and `choose.py:129` docstrings say "thirteen" convictions / "four-axis basis"; roster measures 15 convictions and 7 axes.
Belongs elsewhere: per-person `pursuits`/`stance` values (characters/npcs docket); verb alignment per verb (verb docket).

## DECISION: BUDGET  — carrier/loader: `decision/budget.py:18` `budget`, `body_band_penalty:71`
Population now: formula `max(1, k + office_bonus*live_holds - body_band_penalty - leg_penalty*len(travel_leg))`; k = `scene_budget`. Status: AUTHORED (code)

| # | parameter | domain | req | now | called for by |
|---|---|---|---|---|---|
| 1 | `scene_budget` (k; also number of rounds per season) | int | REQ | 5 | `budget.py:58`, `driver.py:467` |
| 2 | `budget_office_bonus` | int | REQ | 1 | `budget.py:58` |
| 3 | `budget_leg_penalty` | int | REQ | 1 | `budget.py:60` |
| 4 | `band_floors["body"]` | dict band->floor | REQ | present (tables.band_floors body cell) | `budget.py:81` |
| 5 | `scenes_per_round` (scenes released per round) | int | REQ | 1 | `loop/deliberate.py:115,255` |
| 6 | `extended_scene_cost` | int | REQ | 2 | as above |
| 7 | person `body`, `tenures`, `travel_leg` | per person | DERIVED | — | `budget.py:57-60` |

Owed: none. Conflicts: none. Belongs elsewhere: `band_floors` site rows (settlements docket).

## DELIBERATION (DELIBERATE step)  — carrier/loader: `loop/deliberate.py:69`
Population now: per person per round. Status: AUTHORED (code)

Per person: `sense()` (`:523`, returns `Sensation(standing_of(p,fx))`), `questions[p.id]`, `aggregate_questions` (rule), `assemble` -> View, `ask_budget = max(0, budget - spent)` (`:143`). If budget>0 and inputs-fingerprint changed or queue empty -> `choose(p, v, s, ask_budget)` (`:170`); else the queued scenes are released. Release: while queue and released < `scenes_per_round` and cost <= left (`:255`). Refusals (raise): unfrozen world `Forbidden` (`:73`); returned scenes cost > budget `Forbidden` S26.3 (`:202`); scene slots > `interactions_per_scene` `Ungraded` (`:223`); returned item not Act/Scene `InstrumentDefect` (`:550`); act whose actor != deciding person `Forbidden` (`:284`). Filters: `_drop_what_was_already_done` removes same `opportunity_key` already realised this season (`:308`); `_qualify_by_round` re-mints ids for rounds >0 (`:386`); fingerprint terms: q_ids+classes, tenures, requires-vocabulary ledger claims, body, travel_leg, told-classed (`:436`). Sensation: `Sensation.standing` only (no chooser term reads it, REM-44). Content inputs: fixtures only (`view_k`, `scene_budget`, `question_aggregation_rule`, `scenes_per_round`, `extended_scene_cost`, `interactions_per_scene`); standing via `standing_of` (`options.py:1380`, `condition_scale`, `told_weight`, `rank_gain`, `record_gain`).

## ENCOUNTER / SIDES / WITNESS / CENSUS / MATTER / RESOLVE / PREDICATES (non-choice steps; what each reads and returns)

| step | module:line | reads from content | returns |
|---|---|---|---|
| ENCOUNTER | `loop/encounter.py:43` | act_of map; `Declared` Events; `field_degree_bands`; prize row `step: ENCOUNTER`/`declares: Declared` | Events of the real field fight |
| sides_of | `loop/sides.py:55` | prize row module; `march_target_kinds` {settlement, territory}; `subtree_occupation_kinds`; act.via seat faction; musters | `(claimants, subject, rung)` |
| `_contests_of` | `loop/sides.py:42` | act.contests or verb row `contests:` | list of prizes |
| WITNESS | `loop/witness.py:318` | `fan_out_mode` {total, presence_only, all_five}; channels {co_located, witness_key, document_key, chronicle, post_remit} (ordered); `claim_subject_rule` {actor, per_change, both}; `observation_deposit_mode` {none, actor, total}; `witness_channel_predicates`; `observation_terms` {stratum, marks, who, why}; `undeposited_kinds` {finding.none} | deposit count |
| CENSUS | `loop/census.py:35` | `person.demanded` Events | individuates a demanded id only |
| RESOLVE helpers | `loop/resolve.py` | `_canonical_order:50` (5 strata {movement, binding_decision, contested_physical, uncontested_material, social} then hash); `_eligible:93`; `_admits:186`; `_fold:342`; `_contest:749`; `_grade:856`; `_apply_write:880` | Events |
| PREDICATES | `loop/predicates.py:55` `requires_predicate` | 9 registered (list above) | bool per act |

## CONTEST / LADDER SEAM  — carrier/loader: `seam/contest.py:182`, `seam/ladder.py:243`
Population now: 5 contest prizes in `rosters.yaml: contest_subsystems.prizes` {the body -> combat/personal_combat/combat.fight; a field -> mass_battle/mass_battle.resolve_field (step ENCOUNTER, declares Declared); a standing, a proposition, a matter -> social_contest/social_contest.roll (a matter heard_by bench)}; 3 graded inquiries {research, examine, surveil -> social_contest.roll}; 1 inquiry module {finding.made -> fieldwork.find}. Status: AUTHORED

| # | choice point / function | who | options (closed set + owner) | inputs | file:line |
|---|---|---|---|---|---|
| 1 | which subsystem for a prize | engine (roster lookup) | 5 prizes (`rosters.yaml contest_subsystems.prizes`) | verb row `contests:` | `seam/contest.py:65,182` |
| 2 | depth cap | CALLER decides (no default) | int | fixture `contest_max_depth`=2 passed by harness | `driver.py:388`, `contest.py:182`; returns `ContestError` |
| 3 | provider outcome | subsystem | status RESOLVED / PARTY-GAP / REFUSED (`REFUSAL_STATUSES`) | claimants, causes, verb, subject, effort | `contest.py:94,46` |
| 4 | graded inquiry (no prize) | engine | 3 verbs in `graded_inquiries` | actor as sole claimant | `contest.py:118` |
| 5 | finding trail | fieldwork provider | `inquiry_modules` (1 row) | Event kind | `contest.py:146` |
| 6 | degree from result | engine (decides nothing) | scene branch (`wound_state`) -> `combat_degree_bands` {Felled, Wounded, Untouched}, edges `combat_band_edges` {Felled: felled>0, Wounded: wounds>0}, fixture `combat_wounded_above`; field branch `attacker_wins` -> `field_degree_bands` {Declared, Won, Lost, Unopposed}; margin branch (`net`,`ob`) -> `degree_from_net` labels {Overwhelming, Success, Partial, Failure} (`engine/dice_engine/dice_engine.py`) | provider result | `seam/ladder.py:243,142,195,219` |
| 7 | social-roll inputs | wrapper | fixtures `pool_default`=2, `obstacle_default`=2, `obstacle_ceiling`=2, `ceiling_per_pool`=True, `obstacle_refusal_multiple`=2, `effort_level`=moderate, `reception_gain`=1.0, `proof_step`=0.25; roster `advantage_sources` {effort}; `genres`{forensic, deliberative, epideictic}; `proofs`{record, testimony, oath, confession}; `ladder_rungs`{deny, cite_incompatible, impugn_motive, concede_fact, concede_harm, hand_error_back} | act | `seam/wrappers/sigma.py:158,181,240-259` |
| 8 | field-fight inputs | wrapper | fixtures `field_walls_dr`, `field_provisioning`, `field_morale_loyalty_gain`, `subsistence_weight`; `field_casualty_model` {scaled_by_degree, total, none} | — | `seam/wrappers/mass_battle.py:195-277` |

Owed: none. Conflicts: none. Belongs elsewhere: subsystem-internal rules (combat, social, fieldwork, mass battle agents).

## PLAYER-FACING CHOICE SEAM  — carrier/loader: `harness/play_surface.py:41` `dispatching_chooser`
Population now: one function (52 lines). Status: AUTHORED, but it is a dispatch hook only.

What the player sees: callback is called `callback(p, v, s, ask_budget, auto)` (`:51`): `Person`, `View` (K claim ids, the question, the person's ordered `questions`), `Sensation` (standing), `ask_budget()` (season remainder in scene-actions), and `auto` (shipped chooser for replay/preview). What the player may select: return `list[Act | Scene]`; options come from the caller (the seam supplies none; `opening_set(p, v, q, fx)` exists to compute them, `options.py:59`, but needs `Fixtures`, not reachable from the callback args). Opening set / budget / refusals: not computed or checked by the seam; DELIBERATE enforces budget, slots bound, actor identity (see DELIBERATION). Scene choices: a bare Act = one-interaction scene; Scenes carry up to `interactions_per_scene` acts, cost 1 (plain) or `extended_scene_cost`=2 (more than one slot) (`pack_scenes`, `choose.py:590-603`). No UI, option labels, or player-facing text exist in this file. Control test named in docstring: `test_play_surface_dispatch.py`.
Owed: nothing in code supplies a player-readable option list; PLAN: Godot mapping is `04` §C.12 (not read here).

## EVERY CHOICE POINT (complete)

| # | name | who chooses | options (closed set + owner) | inputs | file:line |
|---|---|---|---|---|---|
| C1 | which question each person answers | engine (sort) | 2 sources, 5 attention tiers | ledger, ambitions, tenures | `world_q.py:3183,3340` |
| C2 | question aggregation | engine rule | {first, all, one_per_source} `rosters.yaml: question_aggregation` | `question_aggregation_rule` | `questions.py:53` |
| C3 | View builder | engine rule | {recent, highest_confidence, question_relevant} `rosters.yaml: view_builder_rules` | own ledger, K=`view_k` | `questions.py:87` |
| C4 | opening-set membership | engine (filters) | 63 verbs minus declines | see OPTION SET | `options.py:59` |
| C5 | seat a verb is exercised through | engine at formation (one Candidate per seat) | held `hold` Tenures granting the act | tenures | `options.py:566,578` |
| C6 | refuse a verb on principle | person (threshold = own projected weight) | 7 axes; pole data per axis | `refusal_axis`, pursuits, alignment | `options.py:452,475` |
| C7 | candidate ranking | NPC policy (score + sampled order); PLAYER overrides per person | score terms pursuit/stance; tau | pursuits, alignment, stance/regard, confliction | `choose.py:129,192,358` |
| C8 | stance polarity arm | fixture | {legacy, regard, declared} | `stance_polarity` | `choose.py:92` |
| C9 | triage: what to leave undone | the PERSON (budget asked, never imposed) | scenes within `budget()` | budget | `choose.py:431`, `deliberate.py:143` |
| C10 | scene packing | policy | {greedy, one_per_scene, by_subject} `scene_packing_rules` | `scene_packing_rule`, `interactions_per_scene` | `choose.py:514` |
| C11 | extended-scene affordability | policy | else downgrade to plain scene | `extended_scene_cost` | `choose.py:598` |
| C12 | declare intent (tell a later act) | chance draw | rate [0,1] | `intent_disclosure` | `choose.py:436` |
| C13 | re-deliberate vs release queued scene | driver | fingerprint equal -> release | 6-term fingerprint | `deliberate.py:166-168,436` |
| C14 | scenes released per round | driver | int | `scenes_per_round`=1 | `deliberate.py:255` |
| C15 | drop already-realised opportunity | driver | `(verb, subject[, counterparty])` key | `_realised` | `deliberate.py:308` |
| C16 | player seat override | PLAYER | per person id | callback | `play_surface.py:41` |
| C17 | resolution order | engine | 5 strata then hash | verb row `stratum` | `resolve.py:50,1259` |
| C18 | act eligibility at fold | engine | {own, remit, hold, presence} | tenures, `a.via` | `resolve.py:93` |
| C19 | obstacle refusal | engine | refuse if Ob > multiple x Pool | `obstacle_refusal_multiple` | `resolve.py:1018` |
| C20 | route: fold / contest / graded inquiry | engine | by verb row `contests:` / `graded_inquiries` | verb row | `resolve.py:1066-1080` |
| C21 | contest prize -> provider | engine roster | 5 prizes | `contest_subsystems` | `contest.py:65` |
| C22 | contest depth cap | harness caller | int | `contest_max_depth`=2 | `driver.py:433` |
| C23 | degree token from result | engine | combat 3 / field 4 / margin 4 | provider result | `ladder.py:243` |
| C24 | field fight deferral | engine | Declared at RESOLVE, fought at ENCOUNTER | prize `step` | `encounter.py:43` |
| C25 | WITNESS who learns | engine | channels (5 ordered), fan-out mode (3) | event, tenures, presence | `epistemic.py:794`, `witness.py:353` |
| C26 | claim subject rule | fixture | {actor, per_change, both} | `claim_subject_rule` | `witness.py:382` |
| C27 | observation deposit mode | fixture | {none, actor, total} | `observation_deposit_mode` | `witness.py:396` |
| C28 | told-claim privacy / drift / refraction | chance & gain | [0,1], band, gain | `telling_privacy`, `told_drift_band`, `refraction_gain` | `witness.py:217,386,389` |
| C29 | CALENDAR fire-and-lapse vs fire-as-sitting | engine | by holder presence | `w.dates` | `calendar.py:41-50` |
| C30 | MATTER stock report mode | fixture | {crossing, season, off} `stock_reports` | `stock_report` | `matter.py:559` |
| C31 | CENSUS individuation | engine | only a demanded id with a containable place | `person.demanded` | `census.py:35` |
| C32 | endings read | engine (read only, no halt) | `endings` (2 members: peninsular_sovereignty [victory], theocracy [not victory]) | rungs, tenures | `world_q.py:2366` |

## FIXTURES READ BY THE LOOP (86 in `DEFAULT_FIXTURES`; those read by scoped files, with shipped value)
scene_budget 5 · scenes_per_round 1 · interactions_per_scene 3 · extended_scene_cost 2 · scene_packing_rule greedy · question_aggregation_rule first · view_k 12 · ledger_cap 200 · confidence_default 100 · choice_temperature 0.1 · stance_polarity declared · stance_gain 1.0 · confliction_weight 0 · scar_weight_shift 0 · intent_disclosure 0.0 · refusal_axis None · withheld_verbs (tuple) · budget_office_bonus 1 · budget_leg_penalty 1 · condition_scale 1000 · fan_out_mode all_five · claim_subject_rule both · observation_deposit_mode actor · refraction_gain 0.5 · telling_privacy 0.0 · told_drift_band 0.5 · told_weight/rank_gain/regard_gain/record_gain/judged_gain/told_valence_gain 0.5 · said_slant newest · contest_max_depth 2 · combat_wounded_above None · stock_report crossing · age_step 0.0 · illness_rate 0.0 · age_at_build 0 · lattice_coupling 0 · default_store_kind grain · default_transfer_amount 1 · default_return_kind salt · thread_sensitivity_gate 30 (+ the sigma/mass_battle wrapper fixtures in the seam table). All are `Fixtures` params (hole-register `[JUSTIFIED]` assumptions), not authored content.

Count of choice-point rows: 32. Parameter/table rows: see tables above.
