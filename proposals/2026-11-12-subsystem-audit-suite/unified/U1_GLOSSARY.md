# U1 — the suite glossary: one word, one meaning, across the suite and the tree

## Status: REFERENCE (vocabulary for the suite's documents and the code they order; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of `main`, 2026-11-12. Lane: U1 (wave 2). Companion to `unified/U1_OWNERS_AND_VOCABULARY.md` (decisions cited `D-U1-nn`).

**Owners checked.** `references/descriptor_registry.yaml` (DR) and `references/names_index.yaml` (NI) were opened
whole. `architecture/VOCABULARY.md` (VOC) was opened whole: its head says **PROPOSED — a ballot, DO NOT RULE ON THIS
FILE YET**, so it owns no term; it is cited only for its measured collisions. Layer 1 (`04` = `architecture/meta/
04_CODE_ARCHITECTURE.md`; `hol` = `holonic_ARCHITECTURE.md` §0.4) owns the world's types, and a type name in code is
its call-site definition (CLAUDE.md §4: define in both places). Where nothing in the tree owns a word the row says
**coined by the suite** and gives the plain word to use, or keeps the coinage with the definition sentence the
landing lane writes at its call site.

**How to read a row.** *Term* — the one meaning — the owner — rejected words for the same thing, and other things
the same word must not be used for — the files whose text changes (the wave-3 rewrite lane of each file's family
makes the change; new text only, no retrofit of frozen ids, CLAUDE.md §4).

## A. The roll

| term | meaning | owner | rejected synonyms / other senses refused | files to change |
|---|---|---|---|---|
| **roll** | one resolution of a pool against an obstacle on the one sampler (`roll_net_continuous`) | `engine/dice_engine/` | "check", "test" (for the same thing); "roll" for a membership list (VEN_C) → **list** | `16_PESSIMIST_PC_A` ("yield check" → "yield roll"); `15_INSTITUTIONS_VENICE_C` ("roll" → "list") |
| **draw** | one keyed uniform sample `H(seed, tick, subject, purpose)`; every roll is made of draws | `04` D-35; `engine/dice_engine/draw.py` (P) | "a draw" for a stalemate → **drawn** (adjective) or **a draw (end state)** only in the field's end-state sense, never in a sentence that also uses the sampling sense | `26_MASS_BATTLE_aggression…`, A-58 restatements in `U5d_FA_land…` |
| **pool** | the dice a roller throws: `max(pool_floor, score + addends + pool_add)` | `sigma_leverage.pool_of` (P, D-U1-08); host reader `seam/wrappers/pool.py::faculty` (T) | "faculty" (for the pool), "dice count"; "Pool" names in DR `not_descriptors.pools` (Combat, Argue…) are retired design names | `10_DICE_capability_axiom_map.md` §D, `U5b_PC_rulings_in_the_fight.md` §2 |
| **score** | a person's trained rank in a capability, or the untrained score where he holds none; what he opposes with | `pool.py::score` (P; B on lane A) | "rating", "prowess" (for a person), "faculty", "history" (CR-85's old field) | `29_DICE` 29-2 (`defender.faculty` → `defender.score`); `03_PC_person_inputs_content.md` Part A |
| **training** | the score's source: the learned rank; gives dice | `capability_uses` `dice` rows (P) | "skill level", "prowess" | — |
| **talent** | the governing attribute of a capability, as held (1–7); gives named levels by steps from the scale's mid-point | `capability_uses` `edge` rows `key: verb.base, per: mid` (P) | "aptitude" (a capability kind, below), "base" (for the attribute in prose; `base:` stays the row's key) | `29_DICE` (its "aptitude" → "talent") |
| **untrained score** | what a non-holder rolls and opposes with | `Fixtures.pool_default` (T) | "ordinary score", "stand-in" (for the score), `obstacle_default` (deleted, C-04) | `16_PESSIMIST_DICE_task_difficulty…`, `10_DICE_one_score_two_roles.md` |
| **base** (of the pool) | `pool_add`: the dice everyone holds (A-6) | `Fixtures.pool_add` (P) | "base" for a capability's attribute in prose (say "governing attribute") | U1 architecture §2 (done), CAP |
| **even line** | the base dice's mean, `MU_PER_DIE × pool_add`; the social obstacle's first term | `sigma_leverage.even_line` (P) | — (coined by lane 29; kept, defined at its call site) | — |
| **obstacle** | what stands against an act, in successes: difficulty + opposition + hostile terms, under the ceiling | `modules/social_contest/roll.py::obstacle`, `modules/combat/core.py::ob_from_defender` | "Ob" in prose (code may keep `ob`); "obstruction" is a different thing (a prior act's refusal, `verb_table.yaml` head) | — |
| **difficulty** | the act's own term in the obstacle: a named **difficulty level** on the verb row | `verb_table.yaml` `difficulty:` (P), `rosters.yaml: difficulty_levels` (P) | "task difficulty" as a separate table (`task_difficulty`, B, retired D-U1-04) | lane A's branch |
| **difficulty level** | one of `plain, routine, demanding, hard` | `rosters.yaml: difficulty_levels` (P) | bare "level" (that is a sigma level) | `13_SC_tuning_tables.md`, `05_SC_obstacle_difficulty…_B.md` |
| **opposition** | the obstacle term the person opposite contributes: `opposition_rate × his score` | `sigma_leverage.opposed_ob` (P) | "his pool" (A-79), "half his score" (retired), "standard" (that is the room's term) | D-U1-02 list |
| **leverage** | what a party brings to a roll, in named levels, on the one channel | `rosters.yaml: advantage_sources` (T) | "advantage" (the roster's key keeps its name; prose says leverage), "edge" (a capability role, below), "bonus" | `16_PESSIMIST_SC_A`, `10_DICE_advantage_sources_for_the_arcs.md` prose |
| **level** | one named step of `LEVEL_SIGMA` (`minor .25, moderate .50, strong .75, major 1.00`σ) | `sigma_leverage.LEVEL_SIGMA` (T) | "level" for a difficulty level, a skill's rank, a decay step, `waiting_level`, `precedence_level` — say the full name each time | `28_CORE_scene_access_*` (`precedence_level`, `waiting_level` → `precedence_step`, `waiting_step` if they are not sigma levels) |
| **degree** | one of the four bands `Overwhelming, Success, Partial, Failure` of the one ladder | `dice_engine.py::degree_from_net` (T), `Degree` (T) | "band" for a degree is allowed only as "degree band"; combat's `Felled/Wounded/Untouched` and the field's `Won/Lost/…` are **end states**, never degrees | `03_PC_*`, `04_MB_*`, `26_*` new text |
| **end state** | how a fought scene ended: combat's three (`combat_degree_bands`), the field's (`field_degree_bands`) | `rosters.yaml` (T) | "degree", "outcome band" | as above |
| **margin** | the real-valued net minus the obstacle; the ladder compares it | `degree_from_net` | "settled margin" (A-5 removes settling) | `10_DICE_believed_odds…`, `U5a_DICE_owed_edits.md` |
| **band** | (1) a degree band; (2) a named range of a quantity with a recorded crossing (`band_floors`, T) | `rosters.yaml: tables.band_floors` (T) | "band" for distance (27_MB_A → **distance step**), for ranks of troop types in a unit (`04_MB_cell_hierarchy` §4 → **layers**), for firmness (30_GO_F → **firmness grade**) | the three files named |
| **ceiling** | (1) the obstacle's bound per pool (`obstacle_ceiling`); (2) a capability scale's top rank | `Fixtures.obstacle_ceiling` (T); a capability row's `scale` (P) | — say "obstacle ceiling" or "rank ceiling" | — |
| **stand-in** | the opposition used where nobody stands opposite: `opposed_ob(pool_default)` | OBS §2 | "fallback", "ordinary score" | — |
| **task** | an act with a draw and nobody opposite (a `graded_tasks` row) | `rosters.yaml: graded_tasks` (P) | "graded inquiry", "graded route", "graded act", "uncontested" | MAT_A–E, PHY_B, PHY_D, MIL_A–D, COL_B |
| **inquiry** | (1) the capability `inquiry`; (2) a verb that writes nothing and deposits to its actor (`research`, `examine`, `surveil`, `reconstruct`) | DR `capabilities` (P); C-22 | "graded inquiry" for a task | as above |
| **switch** | an `on/off` (or named-value) fixture | `Fixtures` | "arm" for the value of a switch | every `14_VERBS_*` and `16_*` that writes "arm: off" |
| **arm** | one setting of an experiment: the control arm and the test arm | — (plain English) | "arm" for a weapon (→ **weapon** / **arms** plural), for a service (`ARM_SHARES` → **branch**), for the capability (`arms`, kept as an id) | `04_MB_campaign_party_economy.md` (`arm` → `branch`) |

## B. The capability surface

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **capability** | a defined, rated thing a person holds: a skill, an aptitude or a trait | DR `capabilities` (P); held on `Person.capability` (T) | "vocation" (code's old name: `data/verbs.py::VOCATIONS`, `rosters.yaml: vocation_attribute`), "faculty", "key" (the retired Key substrate's word, ED-IN-0232) | `06_FA_office_capabilities.md` (`vocation:` → `capability:`), `05_SC_capability_surface.md`, `07_SE_*` |
| **skill** | a capability kind: a learned rating that gives dice | DR `capabilities.kinds` (P) | the combat module's `skill` slots (`balance, parry, dodge, bind`) are **combat axes**, not skills | `03_PC_person_inputs_content.md` Part A (slot family `skill` → `axis`) |
| **aptitude** | a capability kind: a rated knack that gives no dice and acts through use rows | DR (P) | "aptitude" for the attribute (29, A-71's loose use) → **talent** | `29_DICE`, `U5b_PC_rulings` |
| **trait** | a capability kind held or not (scale `[0, 1]`) | DR (P) | "susceptibility" (the four `moved_by_*` traits are traits; `resonant_style` stays the cast key) | — |
| **ability** | not a kind: a trait or aptitude whose use row names its scene's site | U1 architecture §2 | "a fourth/fifth kind"; the combat "abilities" (`ABILITIES`) are levers (below) | — |
| **attribute** | one of the ten on the 1–7 scale | DR `attributes` (T), names NI `attr.*` (T) | display names only in prose for players (Presence, Reason, Spirit, Coordination); keys in data; "Spirit/Will" both resolve to `attr.mind.will` | `02_CHAR_what_an_act_risks.md`, `04_MB_*` ("Spirit" in prose is fine; never invent "Willpower" keys) |
| **role** (capability) | one of the ten ways a capability changes an outcome (`dice, addend, opposes, edge, circumstance, resource, threshold, rate, judgement, gate`) | `rosters.yaml: capability_roles` (P) | composition **role** (`composition_roles:`, a provider the engine requires) and MB **unit role** (`ShieldWall`…): always qualify ("capability role", "composition role", "unit role") | `04_MB_unit_loadout…_B.md`, `U5b_MB_*` |
| **site** (capability) | the one reader of a set of use rows (`social_roll`, `fight`, `field`, …) | `rosters.yaml: capability_use_sites` (P) | Layer 1 `Site` (a matter carrier, capitalised) and a training site → always "use site" for this sense | U1 architecture (done) |
| **edge** (role) | a use row whose value becomes named levels | U1 architecture §3 | a Tenure **edge** (`04` §B.8): write "edge row" for the role, "edge" alone only for a Tenure | `28_CORE_scene_access_A` |
| **gate** | (1) the write gate `state/gate.py`; (2) the capability role `gate` (Thread Sensitivity only, A-11); (3) the loader's refusal → **refusal**; (4) a proposal's execution check → **check** in new suite text | `04` §C.2 (1); U1 (2) | "gate" for (3) and (4) in new text | new suite text only |
| **judgement** | the capability role: a factor about the scale's mid-point | U1 | `judgment` as a capability name (→ `law`, C-U5a-11) | — |
| **law** | the capability of knowing and applying a forum's rules | DR (P) | `judgment` (FA) | `06_FA_office_capabilities.md` body |
| **deception** | the capability of making another believe what one knows false | DR (P) | `copying` for a lie | `05_SC_capability_surface.md` edit 1 (withdrawn) |
| **insight** | the capability of reading a person or a bench; never rolled | DR (P) | "rhetoric" (not created, D-U1-03) | `05_SC_hearing_capabilities.md` |
| **command** | the capability by which an order takes effect | DR (P, `27_MB_A`) | `MassBattleInput.command` integer (retired), "Command Rating" (NI `mass.command` legacy), "chain of command" for A-22's authority → **command basis** | `04_MB_typed_outcome_and_one_path.md`, `15_INSTITUTIONS_SYNTHESIS_C` |
| **faculty** | **retired as a suite word.** The code symbol `pool.py::faculty` keeps its name (no retrofit) | — | collides three ways: the pool (code), the attribute Reason (DR/NI alias `Faculty` on `attr.mind.acuity`), "a learned skill" (A-59). Say **pool**, **talent** or **training** | every suite file using "faculty" in prose; DR and NI: drop the `Faculty` alias of `attr.mind.acuity` (an ordered edit for the IN lane; check `tools/names.py` callers first) |
| **rank** | (1) a capability's held level 0–7; (2) a seat's rung ordinal | (1) the capability row's `scale` (P); (2) `RUNG_KINDS.index` (T) | one word, two ranks in one file (`02_CHAR_capability_definitions.md` `rank_at_least`; 28A `rank_gap`): write "capability rank" and "seat rank"; `hol` §9.2's "rank supplies dice" is the **capability** rank | `02_CHAR_capability_definitions.md`, `28_CORE_scene_access_A` |
| **rank_gap** | how far the person acted on stands above the actor's exercised seat; an obstacle term | OBS member 6 | `standing`, `standing_step` | BIND_C, S1_D, S2_C, S2_D |
| **modifier** (seat) | a seat's named level on rolls made through it | `offices.yaml` row `modifier:` (P, D-U1-01a) | "bench die", `standing_dice`, "office weight", "seat addend" | T13 T4, `27_MB_A` §5, `15_INSTITUTIONS_*` |
| **prowess** | a unit's quality of troops and equipment (A-59) | `27_MB_B` (P) | a person's training (29) | `29_DICE` |
| **lever** | one of the fifteen combat levers | `modules/combat/ability_primitives.py` (T file) | the army-wide strategy "lever" → **strategy**; an approach's "lean" | `U5b_PC_*` |

## C. People, belief and the interior

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **pursuit** | one of the fifteen wants on seven bipolar axes | DR `pursuit_roster` (T), NI `season.pursuits` | "conviction" for a want (NI legacy `Person.convictions`) | — |
| **conviction** | the creed-intensity map on `Person` (0–5 per affiliation) | DR `affiliation_roster` (T) | "faith", "creed" for the same map in CHAR_A; "conviction" for a pursuit | `16_PESSIMIST_CHAR_A` |
| **affiliation** | one member of the affiliation roster (a doctrine held) | DR (T) | "pole" (say "affiliation"), "member", "faith" | `31_WR_A` |
| **creed** | a **faction's** declared affiliations (`factions.creed`) | `rosters.yaml: factions` (T) | a person's conviction; a creed Proposition (say "creed Proposition" in full) | `20_NARRATIVE_A`, `30_WR_B` |
| **stands for** | holds an affiliation above the scale's mid-point | `person_q.conviction_stand` (T) | "held" in the old sense (above zero) → "stored above zero" | `16_PESSIMIST_CHAR_A` ("highest-held") |
| **scar** | the count of violations per axis | `04` §B.2 (`scar[axis]`) | "wound" for the scar (`02_CHAR_scar_is_a_wound.md` title stays; body says scar) | `02_CHAR_scar_is_a_wound.md` body |
| **regard** | one person's disposition toward another, in the stance unit | `person_q.regard` (T) | "favour" (a leverage source, the favourable half), "reception" (an audience's), "opinion" | — |
| **stance** | a stored row `(referent, valence, weight)` | `04` §B.2; NI `season.stance` | MB unit "stance" (`hold`, `retreat`) → **posture**; `march_postures` (T) is the precedent | `04_MB_*`, `26_*` |
| **standing** | S18.2's scalar: the gap between what others say of a person and what he holds of himself (`condition_scale`); and the prize `a standing` | `decision/options.py::standing_of` (T); `contest_subsystems.prizes` (T) | rank against an act (`rank_gap`), a document's band (`force`), the bench die (`modifier`), a fight's victor (`prevailed`), a stake on a stance row (→ `regard`, ledger F-40); "standing order" is a fixed MB phrase | D-U1-11a; ledger F-40; BIND_C; S1_B; T13 |
| **resolve** | the RESOLVE step; `faction_q.resolve` (`04` §B.6.1) | `04` | `person_q.resolve` → `person_q.decisiveness` (D-U1-11m); SOCIAL1_D's pool `resolve` → its capability name | `02_CHAR_resolve_and_temper.md`, `14_VERBS_SOCIAL1_D` |
| **voice** | on the player surface only: one owned part of one person's score for one candidate | — (coined by CHAR; kept on the surface only) | in code it is a **score term** (`score_terms`, T) | `02_CHAR_voices_and_the_room.md` |
| **room** | the audience at a hearing as the actor believes it | — | `the_room(w, event_id)` (witnesses' regard, the truth) → `witness_regard`; `margin_endings.room` (retired) | `02_CHAR_voices_and_the_room.md` |
| **reception** | the audience's disposition toward the speaker; hostile half an obstacle term | `SocialContestInput.reception` (T) | "favour" for the favourable half (→ the `favour` level) | — |
| **ground** | why one person regards another (`relation_grounds`) | `rosters.yaml: relation_grounds` (P) | the Thread as a condition of places (A-40) → **the Thread** / "worn ground" only with "Thread"; a march's basis → **casus belli** or **claim**; a question's reason (`occasion_grounds`) → **occasion ground** in full | `12_ARCS_substrate_as_ground.md`, `20_NARRATIVE_E` |
| **regime** | a cluster of persons and bodies sharing opinions to some extent, with a core and a fringe (A-82, A-83) | `rosters.yaml: regime_cores` (P) | "regime" = a creed-exact set (`30_WR_B`) or a three-valued control (NARR_A); never a faction (NARR_D) | `30_WR_B`, `20_NARRATIVE_A` |
| **core / fringe** | a regime's members near / farther from its authored core (`closeness`) | `31_WR_A` (P) | core = creed-exact (`30_WR_B`) | `30_WR_B`, `30_WR_G` |
| **accord** | the graded agreement of two persons' stands (mean product) | `world_q.accord` (P) | `commensurate` (the three-valued control form, kept as `credit_form sign`'s control), `closeness`, `link_fit` (each a different formula: keep each, name it as the formula it is; no fourth) | `30_WR_G`, `31_WR_A` |
| **custom** | the axis vector a person believes his circle keeps | `person_q.custom_of` (P) | "customs" (canon: tariffs) | — |
| **circle** | doers in his ledger who share his faction or his home | `world_q.circle_of` (P) | "Inner Circle" (a canon body) — capitalised, never bare | — |
| **legibility** | how far others can read a person (A-43) | `person_q.legibility` (P) | — | — |
| **knowledge kind** | `mundane` or `thread_substrate`: what a claim is about | `rosters.yaml: knowledge_kinds` (T) | "ground" | — |

## D. World, places, seats and documents

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **seat** | the Layer 1 `Seat` (code class `Office`, ids `off_*`) | `04` §B.7; `state/carriers.py::Office` (T) | "office" in new prose (code keeps `Office`); "post" (a seat's label field, below); "title" (no `Title` type: a seat with an empty remit); "dignity" (a seat-row key, not a kind) | `06_FA_*`, `15_INSTITUTIONS_*` new text |
| **post** | (1) a seat's label (`Seat.post`); (2) an MB formation place (`front, rear, …`) | `04` §B.7 (1); `troops.yaml: formations` (P*) (2) | always "seat post" or "formation post" | `27_MB_A`, `04_MB_cell_hierarchy_as_data.md` |
| **officer** | (MB) the person a unit row names to lead it | `hierarchy/units.py::Officer` (T) | a seat-holder → **holder**; "Church officers" (A-35) are holders of Church seats | `15_INSTITUTIONS_PAPACY_*` |
| **holder** | the person a seat's `hold` Tenure names | `04` §B.8 | "officer", "incumbent" | — |
| **rung** | an address in the realm (territory, settlement, …) | `04` §B.3 | "ladder" for a chain of seats → **chain of seats** | `16_PESSIMIST_FA_B`, `_C` |
| **territory** | a rung of kind `territory`; counted at read under a `realm` rung | `rosters.yaml: rung_kinds`, `endings` (T) | "province" (the geography file's key `provinces:` is a file name, not a game term) | — |
| **holding** | a rung a faction holds (`Faction.holdings`) | `04` §B.6.1 | `Holding` referent class (BIND_A) keeps its capital; "hold" as a draw outcome → "a position holds" only in prose | — |
| **record / Record** | `Record`: a document carrier (petition, writ, army, works…) | `04` §B.5; `rosters.yaml: record_kinds` (T) | `person_q.record(p, teller)` (a teller's reliability) → `reliability`; "typed record" → **dataclass** or "typed input"; the "reading record" (`requirements.yaml`) → **reading** | `05_SC_*` (SC_E), `01_CORE_requirements_reading_record.md` |
| **writ** | a `dispensation` Record (the roster key stays `dispensation`) | `record_kinds.dispensation` (T) | "decree" for one proclaimed by `issue` (A-21); "order" for a writ the issuer commands; "instrument" for one naming a `form` | `06_FA_hygiene.md` e4 (rename withdrawn, D-U1-11h) |
| **exhibit** | an item entered on a case file | the module's `Exhibit` (T) | "item" once entered (FI keeps "cited item" for the operand before entry), "proof" (a `proofs` kind), "evidence" (the leverage it yields) | `08_FI_05_*`, `19_LACUNA_*` |
| **receipt** | a Layer 1 `Receipt`: the gate-minted record of one write | `04` §B.9 | the GO host reading `receipt` → **`act_result`** (D-U1-11n); A-62's "refusal receipt" → "the budget's reading" | `11_GO_player_surface_contract_B.md`, `30_GO_F` |
| **Event** | the occurrence (no actor, no target) | `state/carriers.py::Event` (T) | "message"; a "deed" is a **claim** whose predicate is an Event kind (below) | — |
| **observed** | an Event's Observations: what the fold read and what the effect derived for WITNESS to deposit | `Event.observed` (T; docstring amended, D-U1-06) | `draws` field, `roll` field | `03_PC_typed_outcome_one_door.md`, `27_MB_C` |
| **deed** | a claim whose predicate is an Event kind an act emits | `person_q.is_deed` (T) | "act" (the `Act`), "event" | — |
| **scene** | Layer 1's `Scene`: what the budget counts (person, occasion, place, interactions) | `04` §B.9 | Godot's scene → **scene instance** (ED-IN-0302); "a fought scene" for one provider call → **fight**; "scenario" for a playable situation (below) | `11_GO_*`, `03_PC_*`, `04_MB_*`, `18_*`, `22_*` |
| **interaction** | one Act inside a Scene | `04` §B.9 | "step" (A-9's word; prose may say "step" only where it quotes A-9) | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` |
| **scenario** | a standalone playable setup of one subsystem (AUDIT_BRIEF) | — (plain English) | "case file", "situation" (FA-P4 function keeps its name); `04` PART D 27a's "scenario block" is the naming rule's word | `15_INSTITUTIONS_SYNTHESIS_D` |
| **occasion** | the Question an act answers (`Scene.occasion`) | `04` §B.9 | the Event that opened a question → **opening Event** | `16_PESSIMIST_GAME_standing_occasions` |
| **round** | one of `scene_budget` slots in a season (`Claim.round`) | `state/carriers.py::Claim` (T) | a duel's unit → **duel round** in full; "season round" → **season** | `04_MB_playable_field_scenario.md` §C, `27_MB_E` |
| **season / tick** | one turn of the loop; `tick` its index | `loop/driver.py` (T) | "season of the year" → **season of the year** in full (`seasons_of_year`, D-U1-10) | — |
| **year** | four seasons | ED-IN-0332; `rosters.yaml: seasons_of_year` (P) | "year = len(season_factor_draw)" | `09_WR_B_weather_with_memory_and_the_year.md` |
| **era** | the named span during which who rules and whether the realm is troubled stay unchanged (A-84) | `world_q.Era` (P) | "reign" (the observer's line, kept apart), "realm-rung slot" (strife master's old sense) | `09_WR_strand_conclusion.md` |
| **strand** | a strife strand (A-45) | `world_q.Strand` (P) | "flow" (strife master's word; code `flows_in` keeps it), "movement" for two petitions → **joined petitions** | `30_WR_A` |
| **census** | the CENSUS loop step (individuation) | `04` §A.2 `loop/census` | the audit family → **reachability audit**; the story instrument → **story count** | `17_CENSUS_*` new text, `23_STORY_D`, A-81's restatements |
| **crossing** | a recorded change of band (`_crossings`) | `loop/matter.py` (T) | storybar's "crossing" (a person standing on two things) → **overlap** | `23_STORY_*` |
| **lapse** | a term's end unpaid; a docket matter's end (`matter.lapsed`) | — | an empty founded rung's end → **abandonment** (`rung.abandoned`) | `22_HAPPENINGS_*` |
| **card** | a role-bound bundle of goal rows drawn at build | `engine/season/world_cards.yaml` (P*) | "deck", "template", "set piece", "tension" (also a world reading, A-68) | `21_PROCEDURAL_*` |
| **stake** | what an actor puts down on a drawn act | `rosters.yaml: stakes` (P) | "price", "cost", "risk" (CHAR's `what_an_act_risks` keeps "risk" for the score term) | `14_VERBS_MILITARY_A`, `MATERIAL_C` |
| **party** | a person on a docket; a party to an instrument | — | a battle's **side**; the person served → **beneficiary**; the one acted on → **counterparty** (`verb_table.yaml: counterparty:`, T); "patient" → counterparty | `16_PESSIMIST_SC_C`, `23_STORY_A`, `02_CHAR_*` |
| **occupy** | an army holds ground it does not own (A-66) | `world_q.occupies` (P) | a visited person's being busy (A-63) → **engaged** | `28_CORE_scene_access_*` |
| **command basis** | whom a seat may order (A-22) | `basis: command` (P) | "chain of command", "purview" (a different basis), "under the seat" | `16_PESSIMIST_FA_C`, `14_VERBS_BINDING_D` |
| **sworn** | a person with a live `oblige` to a seat | `04` §B.7 | "obligee", "establishment" (the Query over the sworn) | — |

## E. Mass battle and personal combat

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **unit** | a row of an army Record (A-2): a troop kind with an officer and orders | `armyrecord.py` (T; Record key `subformations`) | Layer 1 "unit" = `PersonId[]` at weight (`04` §C.5.1: no unit class) — write "unit row"; a person's "unit" → **side** | `03_PC_loadout_and_carry.md` |
| **formation** | a unit's cell arrangement (`ranks, files, shape`) and the army's layout (`line, envelopment, refused_flank`) | `troops.yaml: formations` (P*) | **subformation** for the arrangement or for a grouping above units (D-U1-11o) | `04_MB_cell_hierarchy_as_data.md`, A-59 restatements |
| **cell** | 16 men, about 4 m square | `troops.yaml: deployment.cell_troops` (P*) | squad grid "cell" → **grid place**; alignment-table "cell" stays; lifepath "cells" stays | `04_MB_squad_grid…` |
| **body** | `Person.body`: the health track | `04` | MB "a body of troops" → **block** | `04_MB_cell_hierarchy`, `27_MB_E` |
| **posture** | a unit's or march's tactical setting (`hold`, `besiege`…) | `rosters.yaml: march_postures` (T) | "stance" | `04_MB_*` |
| **approach** | (PC) a lean per phase: `defensive, normal, aggressive` | `modules/combat/vocabulary.py: APPROACHES` (P) | MB `approach_rows` (a starting distance) → **opening distance**; LACUNA `calm/press` → **questioning** (ledger P-03) | `04_MB_cell_hierarchy`, `19_LACUNA_questioning…` |
| **exchange** | (PC) the `exchange` phase and one roll in it | `PHASES` (P) | the MB squad's round of pairings → **pairing round** (`FIELD_EXCHANGES` keeps its name); the verb `exchange` (trade) stays | `04_MB_squad_grid…` |
| **bout** | (MB) one 18-tick clash | `troops.yaml: deployment.scale` (P*) | illness or age striking a person (HAP_A) → **spell of illness** / **decline** | `22_HAPPENINGS_A` |
| **stamina / fatigue** | stamina: the reserve, a share in [0, 1] at every boundary; fatigue: its loss | `MassBattleInput.entry_stamina` (P); `troops.yaml: fatigue` (P*) | Thread Fatigue (NI `thread.thread_fatigue`) is a practitioner's, never "stamina" | `26_MASS_BATTLE_movement…`, `27_MB_E` |
| **yield** | (PC) a fighter gives up | `fight_endings: yielded` (T) | a Site's produce → **harvest** in new prose (`yield.taken`, `Rung.yield` keep their names) | `07_SE_*` new text |
| **prevailed** | the fight ending of a party left standing whose opponent fell or yielded | `fight_endings` (P, D-U1-11a) | `standing` | `03_PC_typed_outcome_one_door.md` |
| **rout / break** | a body's collapse; `rally, withdraw, run` its three end bands | `26_…rout…` (P) | "yield" (PC) at the army scale | — |
| **riposte** | the deciding blow turned by a draw | `18_DETERMINISM_no_certain_matchup.md` (P) | "upset", "flip" (`UPSET_FLOOR` names the old override) | — |
| **nested contest** | a duel round called from inside a field (A-4, depth 1) | `nested_entry` (P) | "nested scene" | — |
| **loadout / kit** | (person) `(primary, secondary, armour)`; (troop kind) the same three | `world_q.kit_of` (T); `troops.yaml` (P*) | — one primitive, two holders | — |
| **armour tier** | `none, light, medium, heavy` | `troops.yaml: armour` (P*) | "mail" for `medium` (the `arms_kinds` seed `harness_mail` maps to `medium`) | `03_PC_person_inputs_content.md` |
| **doctrine** | (MB) a row that writes standing orders | `troops.yaml: doctrines` (P*) | ED-SC-0013's "doctrine" (auto/manual) → **play mode**; Layer 1's "delegation doctrine" keeps its phrase; the pursuit `doctrine` (NI `season.pursuit.doctrine`) | `04_MB_*` |
| **frontage / front** | (MB) the width in contact | — | `Front` referent class (BIND_E) keeps its capital | — |

## F. Process words the suite uses about itself

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **owner** | the one file and key a fact is authored in | CLAUDE.md §0.05 | "home" (allowed as a synonym in prose), "source of truth" | — |
| **check** (of a proposal) | the execution artifact that shows an edit landed (a run, a hash, a test) | — | "gate" (the write gate's word, D-section above) in new text | new suite text |
| **refusal** | the loader's or the gate's refusal; a precondition failed with no contest | `04` §C.4 | "loss" (a contest that went against), "the gate refuses" for a loader | — |
| **reading** | a measurement a named instrument prints | — | the `reading:` record on a requirement row keeps its key | — |
| **pin** | a recorded hash a test compares | `engine/season/tests/_realm_goldens.py` (P) | "golden" (allowed) | — |
| **mover** | an edit declared to change seeded results | — | — | — |
| **Layer** | always numbered and capitalised (Layer 0, Layer 1, Layer 2) | CLAUDE.md (RULED) | "layer" for an epistemic or narrative layer in code keeps its lower case and its qualifier | — |
| **loop** | the season loop | CLAUDE.md | the apparatus pathology is "the apparatus loop", never bare (VOC's measured collision) | — |
| **roll / draw / check / test** | see §A | — | "test" only for a pytest test | `07_SE_*`, `16_PESSIMIST_SE_A` |
| **wire / reader / orphan** | a declared thing and its caller | `04` ID-13 ("a field nothing reads is not a field") | "cut wire", "dead", "uncalled", "unread": say "has no reader" | `17_CENSUS_*` new text |
| **knockout** | coined (NARR/16_ nine-gate): suppress one person's choice and count the others' differing acts | — | plain word: **removal test**; kept only with its definition at the call site | `16_PESSIMIST_CORE_the_nine_gate…` |
| **roga, fisc, Kontor, rector, sekreton, catasto, missus, dedizione, commenda…** | historical loan words in institutions prose | — | prose uses the plain word (stipend, treasury, trading house, …); data ids are plain words (`warrant`, `commission`, `tithe`, already) | `15_INSTITUTIONS_BYZANTINE_*`, `_VENICE_*`, `_COLONIAL_*` |

## G. Names the naming gate binds

The canonical name of the god and the Church is **Solmund** (`world.solmund`, NI, `enforce: block`); the Church's
display name is **Church of Solmund** with the alias **Church** (`world.church`). Valorsmark's alias is **Crown**
(`world.valorsmark`). No suite file may introduce a name for a faction, house or person that `names_index.yaml` or
`references/proper_noun_registry.yaml` does not carry; a new one is a registry row first.
