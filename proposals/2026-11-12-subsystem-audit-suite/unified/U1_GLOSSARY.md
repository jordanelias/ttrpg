# U1 — the suite glossary: one word, one meaning, across the suite and the tree

## Status: REFERENCE (vocabulary for the suite's documents and the code they order; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of `main`, 2026-11-12. Lane: U1 (wave 2). Companion to `unified/U1_OWNERS_AND_VOCABULARY.md` (decisions cited `D-U1-nn`).

Reconciled: 2026-11-12, A-100/A-101 supersession pass (MBA-01, MBA-04, MBA-05, MBA-06 / PCR-3; `master/mb_abstraction/MBA_DESIGN_part3.md` §8.3): §E gains *contact draw*, *felling chance*, *exposure*, *matchup row*, *range band*; §J's *power* is retired as a troop stat (the men's martial skill, `skill`, replaces it) and its *duel round* row names the contact draw's unit; §K's *duel round* row says the same. The *round*, *exchange*, *lap* and *duel round* rows of §D, §E and §K were written by the A-101 round lane and are checked, not rewritten. Per `STAGES.md` rule 2 each row's owner is a proposal until its item lands; the landing item's commit replaces the proposal pointer by the code owner.

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
| **pool** | the dice a roller throws for one act: `max(pool_floor, skill score + addends + pool_add)` | `sigma_leverage.pool_of` (P, D-U1-08); host reader `seam/wrappers/pool.py::faculty` (T) | "faculty" (for the pool), "dice count"; "Pool" names in DR `not_descriptors.pools` (Combat, Argue…) are retired design names; A-98: a reserve an attribute sizes and events drain (health, stamina) is a **derived score**, never a "pool" (`work/A98_DERIVED_SCORES.md` mislabel 1) | `10_DICE_capability_axiom_map.md` §A (`resource` row, A-98 sweep), §D, `U5b_PC_rulings_in_the_fight.md` §2 |
| **skill score** | a person's number in a skill (A-6's phrase; A-98 (2)): his held rank in it, or the untrained score where he holds none; what he rolls with and what he opposes with | `pool.py::score` (P; B on lane A), the skill score's reader | bare "score" (A-98 (5): always with its kind, **skill score**, **derived score** or **choice score**), "trained score", "trained rank", "training" (for the rank), "rating", "prowess" (for a person), "faculty", "history" (CR-85's old field); "ordinary score" | A-98 sweep (`work/A98_SWEEP.md`); `29_DICE` 29-2 (`defender.faculty` → `defender.score`); `03_PC_person_inputs_content.md` Part A |
| **training** | the act of learning a skill (A-98 (2)): the verb `train`, the growth rule `grows_by: train`; a **training site** is the place where the act happens | `verb_table.yaml: train` (T); the skill row's `grows_by` (P) | "training" for the learned rank (→ **skill score**), "skill level", "prowess" | A-98 sweep |
| **governing attribute** | the attribute a skill is governed by (the skill row's `base:`), as held (1–7); gives named levels by steps from the scale's mid-point, for the roller above it and against him below (A-7's second input). **A verb names one to three** (B05.24), whose mean is his **governing score** | the skill row's `base:` (P); `capability_uses` `edge` rows `key: verb.base, per: mid` (P) | "talent", "aptitude" (A-98 (1): both retired), "base" in prose (`base:` stays the row's key) | A-98 sweep |
| **governing score** | (B05.24, Jordan 2026-11-13) the mean of a person's scores on the 1 to 3 attributes a verb names (one he does not hold reads at the untrained score `pool_default`), rounded to the nearest tenth, a value halfway between two tenths rounding up; a fractional number (2.5, not 3) that feeds the dice as a fractional pool | `pool.py::governing_score` on `sigma_leverage.governing_mean` (B05.25, T) | "rounded to a whole number", `round_half_up` (B38.55's, for integer counts only) | B05.24 |
| **talent** | **retired as a suite word (A-98 (1)).** Say **attribute**, or **governing attribute** for the one a skill names | — | — | A-98 sweep (every live file) |
| **untrained score** | the skill score of a person who holds no rank in the skill: what a non-holder rolls and opposes with ("untrained": he has not done the act of training, so the word keeps A-98's sense) | `Fixtures.pool_default` (T) | "ordinary score", "stand-in" (for the score), `obstacle_default` (deleted, C-04) | `16_PESSIMIST_DICE_task_difficulty…`, `10_DICE_one_score_two_roles.md` |
| **base** (of the pool) | `pool_add`: the dice everyone holds (A-6) | `Fixtures.pool_add` (P) | "base" for a skill's attribute in prose (say "governing attribute"); an army's **base** (A-70, Jordan's word: where it returns on a draw, A-67's "original station") is the ordinary military sense and stays | U1 architecture §2 (done), CAP |
| **even line** | the base dice's mean, `MU_PER_DIE × pool_add`; the social obstacle's first term | `sigma_leverage.even_line` (P) | — (coined by lane 29; kept, defined at its call site) | — |
| **obstacle** | what stands against an act, in successes: difficulty + opposition + hostile terms, under the ceiling | `modules/social_contest/roll.py::obstacle`, `modules/combat/core.py::ob_from_defender` | "Ob" in prose (code may keep `ob`); "obstruction" is a different thing (a prior act's refusal, `verb_table.yaml` head) | — |
| **difficulty** | the act's own term in the obstacle: a named **difficulty level** on the verb row | `verb_table.yaml` `difficulty:` (P), `rosters.yaml: difficulty_levels` (P) | "task difficulty" as a separate table (`task_difficulty`, B, retired D-U1-04) | lane A's branch |
| **difficulty level** | one of `plain, routine, demanding, hard` | `rosters.yaml: difficulty_levels` (P) | bare "level" (that is a sigma level) | `13_SC_tuning_tables.md`, `05_SC_obstacle_difficulty…_B.md` |
| **opposition** | the obstacle term the person opposite contributes: `opposition_rate × his skill score` | `sigma_leverage.opposed_ob` (P) | "his pool" (A-79), "half his score" (retired), "standard" (that is the room's term) | D-U1-02 list |
| **leverage** | what a party brings to a roll, in named levels, on the one channel | `rosters.yaml: advantage_sources` (T) | "advantage" (the roster's key keeps its name; prose says leverage), "edge" (a capability role, below), "bonus" | `16_PESSIMIST_SC_A`, `10_DICE_advantage_sources_for_the_arcs.md` prose |
| **level** | one named step of `LEVEL_SIGMA` (`minor .25, moderate .50, strong .75, major 1.00`σ) | `sigma_leverage.LEVEL_SIGMA` (T) | "level" for a difficulty level, a skill's rank, a decay step, `waiting_level`, `precedence_level` — say the full name each time | `28_CORE_scene_access_*` (`precedence_level`, `waiting_level` → `precedence_step`, `waiting_step` if they are not sigma levels) |
| **degree** | one of the four bands `Overwhelming, Success, Partial, Failure` of the one ladder | `dice_engine.py::degree_from_net` (T), `Degree` (T) | "band" for a degree is allowed only as "degree band"; combat's `Felled/Wounded/Untouched` and the field's `Won/Lost/…` are **end states**, never degrees | `03_PC_*`, `04_MB_*`, `26_*` new text |
| **end state** | how a fought scene ended: combat's three (`combat_degree_bands`), the field's (`field_degree_bands`) | `rosters.yaml` (T) | "degree", "outcome band" | as above |
| **margin** | the real-valued net minus the obstacle; the ladder compares it | `degree_from_net` | "settled margin" (A-5 removes settling) | `10_DICE_believed_odds…`, `U5a_DICE_owed_edits.md` |
| **band** | (1) a degree band; (2) a named range of a quantity with a recorded crossing (`band_floors`, T) | `rosters.yaml: tables.band_floors` (T) | "band" for distance (27_MB_A → **distance step**), for ranks of troop types in a unit (`04_MB_cell_hierarchy` §4 → **layers**), for firmness (30_GO_F → **firmness grade**) | the three files named |
| **ceiling** | (1) the obstacle's bound per pool (`obstacle_ceiling`); (2) a skill scale's top rank | `Fixtures.obstacle_ceiling` (T); a skill row's `scale` (P) | — say "obstacle ceiling" or "rank ceiling" | — |
| **stand-in** | the opposition used where nobody stands opposite: `opposed_ob(pool_default)` | OBS §2 | "fallback", "ordinary score" | — |
| **task** | an act with a draw and nobody opposite (a `graded_tasks` row); the path its draw takes in the fold is the **task route** (U4d) | `rosters.yaml: graded_tasks` (P) | "graded route" (→ task route), "uncontested"; "graded inquiry" as a name for the class (the three inquiry verbs on the roster may be called "graded inquiries", inquiry sense 2); "graded act" stays for its ordinary sense, any act the ladder grades, contested or not | MAT_A–E, PHY_B, PHY_D, MIL_A–D, COL_B |
| **inquiry** | (1) the skill `inquiry`; (2) a verb that writes nothing and deposits to its actor (`research`, `examine`, `surveil`, `reconstruct`) | DR `capabilities` (P); C-22 | "graded inquiry" for a task | as above |
| **switch** | an `on/off` (or named-value) fixture | `Fixtures` | "arm" for the value of a switch | every `14_VERBS_*` and `16_*` that writes "arm: off" |
| **arm** | one setting of an experiment: the control arm and the test arm | — (plain English) | "arm" for a weapon (→ **weapon** / **arms** plural), for a service (`ARM_SHARES` → **branch**), for the skill (`arms`, kept as an id) | — (U4d: `04_MB_campaign_party_economy.md` was named here in error; its `veterancy: {arm: off}` is a switch setting, this row's own sense, as W3-1 reported) |

## B. Attributes, skills, traits and derived scores (A-98)

A person's numbers come in three families and one roster apart (A-98): an **attribute** (one of the ten, inborn),
a **skill** (a learned rank; his number in it is his **skill score**), and a **derived score** (computed from
attributes, skills and state; never learned, never trained). His **traits** (the four held-or-not dispositions) are
a roster of their own `[ASSUMPTION, A-98 (4)]`. Bare "score" is never written without its kind (skill score,
derived score, choice score).

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **attribute** | one of the ten on the 1–7 scale; inborn, never trained. An aptitude is an attribute (A-98 (1)) | DR `attributes` (T), names NI `attr.*` (T) | "aptitude", "talent" (A-98 (1), retired as suite words; A-71's quotation keeps its wording), "faculty" (the DR/NI alias of Reason, §*faculty*); display names only in prose for players (Presence, Reason, Spirit, Coordination); keys in data; "Spirit/Will" both resolve to `attr.mind.will` | A-98 sweep; `02_CHAR_what_an_act_risks.md`, `04_MB_*` ("Spirit" in prose is fine; never invent "Willpower" keys) |
| **aptitude** | **retired as a suite word (A-98 (1)): an aptitude is an attribute.** Say **attribute**. The former capability kind `aptitude` (its one row, `insight`) is a skill whose use rows give no dice | — | A-71's quotation (*"someone's aptitude/prowess"*) keeps its wording | A-98 sweep |
| **skill** | a learned rank a person holds and can train (A-98 (2)); the one kind of the skill roster (A-98 (4): the `kinds:` roster collapses to `skill`). Each skill names its governing attribute, what opposes it, its scale and how it grows; its use rows say where it changes an outcome. A skill whose use rows give no dice is still a skill (`insight`) | DR `capabilities` (P), the roster's tree name (§*capability*) | "capability" in prose (A-98: a tree identifier for skill), "aptitude" and "trait" as kinds of skill; "training" or "talent" for its two inputs (say **skill score** and **governing attribute**); the combat module's `skill` slots (`balance, parry, dodge, bind`) are **combat axes**, not skills | A-98 sweep; `03_PC_person_inputs_content.md` Part A (slot family `skill` → `axis`) |
| **capability** | **the tree's second name for skill (A-98).** Identifiers keep it: `Person.capability` (T), DR `capabilities` (P), `capability_uses`, `capability_roles`, `capability_use_sites`, `capability_factor`, `capability_admits` (P). Prose says **skill** and gives the identifier in backticks once where the code symbol is meant | `Person.capability` (T); DR `capabilities` (P) | "capability" in prose; "vocation" (code's old name: `data/verbs.py::VOCATIONS`, `rosters.yaml: vocation_attribute`; ordinary "vocation" is a calling or trade, so the tree names fail the word test: deleted by CAP A2/A3, OWNERS C-04), "faculty", "key" (the retired Key substrate's word, ED-IN-0232; "holds the key at 2" → "holds the skill at 2") | rename candidate (§H; v12 batch, cost to measure, a `Person` key may enter `World.content_hash()`); prose: A-98 sweep. Document and batch names that carry the word (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`, `U5a_capability_home…`, B04-capability-home) keep it |
| **martial skill** | skill at arms: a person's skill score in the skills used in fighting (`arms`, the one such row today) (A-98 (3)) | DR `capabilities` row `arms` (P) | "prowess" for a person (A-98 (3): prowess is a unit's), "training", "fighting value" | A-98 sweep |
| **trait** | one of a person's held-or-not dispositions: `moved_by_evidence`, `moved_by_consequence`, `moved_by_authority`, `moved_by_solidarity`, seated from `npc_registry.yaml: resonant_style`; acts only through `edge` rows, never dice. **Not a skill**: it leaves the skill table and is a roster of its own `[ASSUMPTION, A-98 (4); reversible, listed for Jordan]` | the trait roster (P: U1 architecture §2a gives its home and loader) | "capability kind trait" (retired with the `kinds:` roster); "susceptibility" as a kind (U4d: it stays as the ordinary description of what a trait does, as `02_CHAR_which_ground_moves_whom.md` uses it); `resonant_style` stays the cast key | A-98 sweep; `02_CHAR_which_ground_moves_whom.md`, `02_CHAR_capability_definitions.md` |
| **ability** | not a kind: a skill whose use row names its scene's site (A-98 (4)) | U1 architecture §2 | "a fourth/fifth kind"; "a trait or aptitude whose use row…" (U1's old wording); the combat "abilities" (`ABILITIES`) are levers (below) | — |
| **derived score** | a value computed from attributes, skills and state, never held as a learned rank and never trained (A-98 (5); Jordan: *"health, wound count, etc"*). Its maximum is computed; where it drains, the current level is a **track** events write (`Person.body`, the fight's damage). The `resource` role is the door by which an attribute sizes one. The inventory with each owner: `work/A98_DERIVED_SCORES.md` | the family rows below; the tree's list name is DR `not_descriptors.derived_values` (T, which also lists faction and settlement values) | bare "score"; "pool" for a reserve (the pool is dice for one act); "stat"; "resource" for the value (it names the role); "resolve" (the RESOLVE step; the registry's "Resolve" has no reader, §C *resolve*) | `10_DICE_capability_axiom_map.md` §A `resource` row (A-98 sweep) |
| **health and wounds** (derived scores) | Wound Interval, Max Wounds, full Health, Health remaining, the wound count and *felled* in a fight; between scenes, the body band | `modules/combat/combatant.py` (`wound_interval`, `max_wounds`, `health_full`, `WoundTracker.health_remaining`/`.wounds`/`.felled`) (T); `decision/budget.py::body_band_penalty` (T); `seam/wrappers/combat.py::party_end` (T, Endurance in the fight less the body band) | "Health" for `Person.body` (that is the track the fight's Health remaining writes, `loop/effects_combat.py::_harm`); "wound" for the scar (§C) | — |
| **reserves** (derived scores) | the maxima of Stamina (3 × Endurance + 2 × Spirit) and Concentration (Focus and Spirit, ED-902) that a fight drains | `combatant.py::stamina_max`, `Combatant.rederive` (`conc_max`) (T) | "stamina pool"; Thread Fatigue (a practitioner's, no reader yet) | — |
| **the body over time** (derived scores) | age (the clock less `Person.born`) and the season's body hazard | `queries/world_q.py::age_of`, `::body_hazard` (T) | a stored age | — |
| **the interior** (derived scores) | standing, confliction, religious intensity; proposed: decisiveness, legibility `[ASSUMPTION: counted in the family by A-98 (5)'s "computed from … state"; Jordan's examples are bodily]` | `decision/options.py::standing_of`, `queries/person_q.py::confliction`, `::religious_intensity` (T); `person_q.decisiveness`, `person_q.legibility` (P) | "resolve" for decisiveness (D-U1-11m) | — |
| **Thread Pool Score** (`prac.tps`) | a practitioner's derived score, `floor(Thread Sensitivity / 10)` | DR `practitioner_stats` (T; registry only, no reader) | — | **tree name fails** twice (it is neither a pool nor a skill score); renamed by the WR lane when a reader is built `[ASSUMPTION]` |
| **role** (skill) | one of the ten ways a skill changes an outcome (`dice, addend, opposes, edge, circumstance, resource, threshold, rate, judgement, gate`) | `rosters.yaml: capability_roles` (P) | composition **role** (`composition_roles:`, a provider the engine requires) and MB **unit role** (`ShieldWall`…): always qualify ("skill role", "composition role", "unit role") | `04_MB_unit_loadout…_B.md`, `U5b_MB_*` |
| **site** (skill) | the one reader of a set of use rows (`social_roll`, `fight`, `field`, …) | `rosters.yaml: capability_use_sites` (P) | Layer 1 `Site` (a matter carrier, capitalised) and a training site → always "use site" for this sense | U1 architecture (done) |
| **edge** (role) | a use row whose value becomes named levels (ordinary English: "an edge" is an advantage, so the role passes the word test) | U1 architecture §3 | a Tenure **edge** (`04` §B.8): write "edge row" for the role, "edge" alone only for a Tenure. U4d: the Tenure sense is graph vocabulary (a link between a person and a seat or place); ordinary "edge" is a border or an advantage, so it fails the word test as a tree name, see §H | `28_CORE_scene_access_A` |
| **gate** | (1) the write gate `state/gate.py`; (2) the skill role `gate` (Thread Sensitivity only, A-11); (3) the loader's refusal → **refusal**; (4) a proposal's execution check → **check** in new suite text | `04` §C.2 (1); U1 (2) | "gate" for (3) and (4) in new text | new suite text only |
| **judgement** | the skill role: a factor about the scale's mid-point | U1 | `judgment` as a skill name (→ `law`, C-U5a-11) | — |
| **law** | the skill of knowing and applying a forum's rules | DR (P) | `judgment` (FA) | `06_FA_office_capabilities.md` body |
| **deception** | the skill of making another believe what one knows false | DR (P) | `copying` for a lie | `05_SC_capability_surface.md` edit 1 (withdrawn) |
| **insight** | the skill of reading a person or a bench; its use rows give no dice, so it is never rolled (A-98 (4): formerly the one row of kind `aptitude`) | DR (P) | "rhetoric" (not created, D-U1-03); "aptitude" (the retired kind) | `05_SC_hearing_capabilities.md` |
| **command** | the skill by which an order takes effect | DR (P, `27_MB_A`) | `MassBattleInput.command` integer (retired), "Command Rating" (NI `mass.command` legacy), "chain of command" for A-22's authority → **command basis** | `04_MB_typed_outcome_and_one_path.md`, `15_INSTITUTIONS_SYNTHESIS_C` |
| **faculty** | **retired as a suite word.** The code symbol `pool.py::faculty` keeps its name (no retrofit) until D-U1-08's split replaces it (§H candidate). Ordinary "faculty" is an inborn power of mind or body (the faculty of speech), so it is kept only where a document means exactly that (`09_WR_B_threadwork_session_and_practitioner.md`, "the faculty judging itself") | — | collides three ways: the pool (code), the attribute Reason (DR/NI alias `Faculty` on `attr.mind.acuity`), "a learned skill" (A-59). Say **pool**, **attribute** or **skill score** (A-98) | every suite file using "faculty" in prose; DR and NI: drop the `Faculty` alias of `attr.mind.acuity` (an ordered edit for the IN lane; check `tools/names.py` callers first) |
| **rank** | (1) a skill's held level 0–7, which is the person's skill score in it (A-98 (2)); (2) a seat's rung ordinal | (1) the skill row's `scale` (P); (2) `RUNG_KINDS.index` (T) | one word, two ranks in one file (`02_CHAR_capability_definitions.md` `rank_at_least`; 28A `rank_gap`): write "skill rank" and "seat rank"; `hol` §9.2's "rank supplies dice" is the **skill** rank | `02_CHAR_capability_definitions.md`, `28_CORE_scene_access_A` |
| **rank_gap** | how far the person acted on stands above the actor's exercised seat; an obstacle term | OBS member 6 | `standing`, `standing_step` | BIND_C, S1_D, S2_C, S2_D |
| **modifier** (seat) | a seat's named level on rolls made through it | `offices.yaml` row `modifier:` (P, D-U1-01a) | "bench die", `standing_dice`, "office weight", "seat addend" | T13 T4, `27_MB_A` §5, `15_INSTITUTIONS_*` |
| **prowess** | a unit's quality of troops and equipment (A-59: "martial prowess"); never a person's (A-98 (3)) | `27_MB_B` (P) | a person's skill at arms → **martial skill** (A-98 (3), answering J-U4d-03; supersedes D-U1-11p's "training"); A-71's quotation (*"someone's aptitude/prowess"*) keeps its wording | A-98 sweep; the unit words are the mass-battle lexicon's (`MB_LEXICON.md`, A-95) |
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
| **Disputant** | a person in a dispute with another: the referent class stamped on a man beside the asker whom the asker holds a dispute with, which `challenge` declares (B01.01, lane A `e5d6ab9`) | `data/verbs.py::DISPUTANT_CLASS`, `rosters.yaml: referent_classes` (T); stamped by `world_q.disputes_held` over `person_q.holds_dispute` | "enemy" (the war-context class `Enemy`), "rival", "adversary" for the class | — |
| **stance** | a stored row `(referent, valence, weight)` | `04` §B.2; NI `season.stance` | MB unit "stance" (`hold`, `retreat`) → **posture**; `march_postures` (T) is the precedent; the MB code field `stance` (`modules/mass_battle/orderofbattle.py`) keeps its name and is written in backticks once (§H candidate) | `04_MB_*`, `26_*` (U4d: done) |
| **standing** | S18.2's scalar: the gap between what others say of a person and what he holds of himself (`condition_scale`); and the prize `a standing` | `decision/options.py::standing_of` (T); `contest_subsystems.prizes` (T) | rank against an act (`rank_gap`), a document's band (`force`), the bench die (`modifier`), a fight's victor (`prevailed`), a stake on a stance row (→ `regard`, ledger F-40); "standing order" is a fixed MB phrase | D-U1-11a; ledger F-40; BIND_C; S1_B; T13 |
| **resolve** | the RESOLVE step; `faction_q.resolve` (`04` §B.6.1) | `04` | `person_q.resolve` → `person_q.decisiveness` (D-U1-11m); SOCIAL1_D's pool `resolve` → its skill name; "resolve" as a derived score (the registry's "Resolve, Spirit's derived value" has no reader; A-98's own list says "resolve and the like", Jordan's words do not): a built one takes another name (`work/A98_DERIVED_SCORES.md` mislabel 5) | `02_CHAR_resolve_and_temper.md`, `14_VERBS_SOCIAL1_D` |
| **voice** | on the player surface only: one owned part of one person's choice score for one candidate | — (coined by CHAR; kept on the surface only) | in code it is a **score term** (`score_terms`, T) | `02_CHAR_voices_and_the_room.md` |
| **room** | the audience at a hearing as the actor believes it | — | `the_room(w, event_id)` (witnesses' regard, the truth) → `witness_regard`; `margin_endings.room` (retired) | `02_CHAR_voices_and_the_room.md` |
| **reception** | the audience's disposition toward the speaker; hostile half an obstacle term | `SocialContestInput.reception` (T) | "favour" for the favourable half (→ the `favour` level) | — |
| **ground** | why one person regards another (`relation_grounds`) | `rosters.yaml: relation_grounds` (P) | the Thread as a condition of places (A-40) → **the Thread** / "worn ground" only with "Thread"; a march's basis → **casus belli** or **claim**; a question's reason (`occasion_grounds`) → **occasion ground** in full | `12_ARCS_substrate_as_ground.md`, `20_NARRATIVE_E` |
| **regime** | a cluster of persons and bodies sharing opinions to some extent, with a core and a fringe (A-82, A-83) | `rosters.yaml: regime_cores` (P) | "regime" = a creed-exact set (`30_WR_B`) or a three-valued control (NARR_A); never a faction (NARR_D). U4d: ordinary "regime" is a government or a system of rule, so a reader lands on "who governs", not "a camp of shared opinion"; Jordan's own word, listed for him with "camp" as the plain alternative (`U4D_FOR_JORDAN.md` J-U4d-01); not renamed | `30_WR_B`, `20_NARRATIVE_A` |
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
| **post** | (1) a seat's label (`Seat.post`); (2) an MB formation post: `centre, left, right, rear, reserve` (MB lexicon D-4: the proposed `front` is renamed `centre`, owed S-6); the units at one post form a **subformation** | `04` §B.7 (1); `troops.yaml: formations` (P*) (2) | always "seat post" or "formation post" | `27_MB_A`, `04_MB_cell_hierarchy_as_data.md` |
| **officer** | (MB) the person a unit row names to lead it | `hierarchy/units.py::Officer` (T) | a seat-holder → **holder**; "Church officers" (A-35) are holders of Church seats | `15_INSTITUTIONS_PAPACY_*` |
| **holder** | the person a seat's `hold` Tenure names | `04` §B.8 | "officer", "incumbent" | — |
| **rung** | an address in the realm (territory, settlement, …) | `04` §B.3 | "ladder" for a chain of seats → **chain of seats**. U4d: ordinary "rung" is a step of a ladder, so "a rung of office" (A-64, Jordan's verbatim) passes and "the army marched into the rung" does not; "rung = world side" is Jordan's ruling (ED-IN-0302), so the word is listed for him, not renamed (`U4D_FOR_JORDAN.md` J-U4d-04). Prose says "place" or the kind ("territory", "settlement") where it can, with `Rung` in backticks once | `16_PESSIMIST_FA_B`, `_C` |
| **territory** | a rung of kind `territory`; counted at read under a `realm` rung | `rosters.yaml: rung_kinds`, `endings` (T) | "province" (the geography file's key `provinces:` is a file name, not a game term) | — |
| **holding** | a rung a faction holds (`Faction.holdings`) | `04` §B.6.1 | `Holding` referent class (BIND_A) keeps its capital; "hold" as a draw outcome → "a position holds" only in prose | — |
| **record / Record** | `Record`: a document carrier (petition, writ, army, works…) | `04` §B.5; `rosters.yaml: record_kinds` (T) | `person_q.record(p, teller)` (a teller's reliability) → `reliability`; "typed record" → **dataclass** or "typed input"; the "reading record" (`requirements.yaml`) → **reading** | `05_SC_*` (SC_E), `01_CORE_requirements_reading_record.md` |
| **writ** | a `dispensation` Record (the roster key stays `dispensation`) | `record_kinds.dispensation` (T) | "decree" for one proclaimed by `issue` (A-21); "order" for a writ the issuer commands; "instrument" for one naming a `form` | `06_FA_hygiene.md` e4 (rename withdrawn, D-U1-11h) |
| **proclaimed** | of a Record kind and minting verb: its terms reach everyone who learns it was made, not only its addressee (A-21: a decree) | `rosters.yaml: proclaimed` (P, `06_FA_decree_binds.md` edit 1, U6 R-C), sibling of `read_to_addressee` | "public terms" (`public_terms`, not made, D-U1-05); "delivered" (the option A-21 did not take) | — (passes: to announce publicly) |
| **exhibit** | an item entered on a case file | the module's `Exhibit` (T) | "item" once entered (FI keeps "cited item" for the operand before entry), "proof" (a `proofs` kind), "evidence" (the leverage it yields) | `08_FI_05_*`, `19_LACUNA_*` |
| **receipt** | a Layer 1 `Receipt`: the gate-minted record of one write | `04` §B.9 | the GO host reading `receipt` → **`act_result`** (D-U1-11n); A-62's "refusal receipt" → "the budget's reading" | `11_GO_player_surface_contract_B.md`, `30_GO_F` |
| **Event** | the occurrence (no actor, no target) | `state/carriers.py::Event` (T) | "message"; a "deed" is a **claim** whose predicate is an Event kind (below) | — |
| **observed** | an Event's Observations: what the fold read and what the effect derived for WITNESS to deposit | `Event.observed` (T; docstring amended, D-U1-06) | `draws` field, `roll` field | `03_PC_typed_outcome_one_door.md`, `27_MB_C` |
| **deed** | a claim whose predicate is an Event kind an act emits | `person_q.is_deed` (T) | "act" (the `Act`), "event" | — |
| **scene** | Layer 1's `Scene`: what the budget counts (person, occasion, place, interactions) | `04` §B.9 | Godot's scene → **scene instance** (ED-IN-0302); "a fought scene" for one provider call → **fight**; "scenario" for a playable situation (below) | `11_GO_*`, `03_PC_*`, `04_MB_*`, `18_*`, `22_*` |
| **interaction** | one Act inside a Scene | `04` §B.9 | "step" (A-9's word; prose may say "step" only where it quotes A-9) | `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` |
| **scenario** | a standalone playable setup of one subsystem (AUDIT_BRIEF) | — (plain English) | "case file", "situation" (FA-P4 function keeps its name); `04` PART D 27a's "scenario block" is the naming rule's word | `15_INSTITUTIONS_SYNTHESIS_D` |
| **occasion** | the Question an act answers (`Scene.occasion`) | `04` §B.9 | the Event that opened a question → **opening Event** | `16_PESSIMIST_GAME_standing_occasions` |
| **lap** (was *round* in this sense; A-101 takes "round" for the fight) | one pass of DELIBERATE, RESOLVE and WITNESS inside a season; a season runs `scene_budget` laps | `state/carriers.py::Claim.round`, `SeasonDriver.round`, `scenes_per_round` (T; identifiers keep their names until the rename candidate `master/pc_round/PC_ROUND_SPEC_part2.md` §6 PCR-4) | **round** for this sense (A-101's round is personal combat's, §K); "season round" → **season**; "cycle" (the suite's word for a dependency cycle) | `27_MB_E`, `28_CORE_scene_access_A`/`_B`/`_C`, `16_PESSIMIST_CORE_no_stored_plan`, `_a_scene_runs_in_its_own_order`, `_the_nine_gate_and_a_knockout_reading`, `18_DETERMINISM_rival_acts_in_one_fold` (each given a `Reconciled:` note, 2026-11-12, A-101); every other file at its next edit (STAGES.md rule 3) |
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
| **sworn** | a person with a live `oblige` to a seat; in prose **a sworn man**, **the men sworn to a seat** | `04` §B.7 | "obligee" (ordinary "obligee" is the party an obligation is owed TO, the seat's side; the tree's `offices.yaml` key `obligees` lists those who owe, so the tree name reads backwards: §H candidate), "establishment" (the Query over the sworn) | U4d: prose done in seven files |

## E. Mass battle and personal combat

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **unit** | a row of an army Record (A-2): men of one troop type with an officer and orders | `armyrecord.py` (T; Record key `subformations`, renamed `units` by `MB_LEXICON_part3.md` §4 L1-1) | Layer 1 "unit" = `PersonId[]` at weight (`04` §C.5.1: no unit class) — write "unit row"; a person's "unit" → **side**; "subformation", "subunit", "body", "block" for a unit in prose (U4d: done in five files; the tree key `subformations`, `orderofbattle.Subformation` and the engine's `Subunit` are renamed by lexicon L1-1, L1-2, L2-1) | `03_PC_loadout_and_carry.md` |
| **formation** | always qualified (MB lexicon D-3): the **unit formation** is a unit's cell arrangement (`ranks, files, shape`; columns renamed `depth, width`, owed S-7); the **army formation** (Jordan's "grand formation") is the army's layout (`line, envelopment, refused_flank`) | `troops.yaml: formations` (P*) | bare "formation" where both could be meant; **subformation** for the unit's arrangement. Settled by A-94 and the MB lexicon (D-1): **subformation** is Jordan's word for the units at one post of the army formation; D-U1-11o's "formation post group" is retired | `04_MB_cell_hierarchy_as_data.md`, A-59 restatements |
| **cell** | the smallest square of the field the battle resolves, and the men on it: today 40 to 200 men (`config.CELL_FLOOR`/`CELL_CAP`, T); proposed 16 men, about 4 m square | `troops.yaml: deployment.cell_troops` (P*) | squad grid "cell" → **grid place**; alignment-table "cell" stays; lifepath "cells" stays | `04_MB_squad_grid…` |
| **body** | `Person.body`: the health track | `04` | MB "a body of troops" → **unit** (MB lexicon D-2; not "block", which is the engine's hundred men, `config.BLOCK_SIZE`; owed S-8 in 22 MB files). U4d: "body" for an institution (a council, a bench, a house: A-82's "persons and bodies", `06_FA_seat_terms_by_body_B.md`) is the ordinary English sense and stays; never in a sentence that also uses `Person.body` | `04_MB_cell_hierarchy`, `27_MB_E` |
| **posture** | a unit's or march's tactical setting (`hold`, `besiege`…) | `rosters.yaml: march_postures` (T) | "stance" (the MB code field `stance` on a unit, `orderofbattle.py`, keeps its name: §H candidate) | `04_MB_*` (U4d: prose done in eight files) |
| **approach** | (PC) a lean per phase: `defensive, normal, aggressive` | `modules/combat/vocabulary.py: APPROACHES` (P) | MB `approach_rows` (a starting distance) → **opening distance**; LACUNA `calm/press` → **questioning** (ledger P-03). A-83's "approaches" (Jordan: how a regime's members do things) is the ordinary sense, compatible with this one; write "manner" or "way of doing things" where a sentence also names the PC lean | `04_MB_cell_hierarchy`, `19_LACUNA_questioning…` |
| **exchange** | (PC) one closed-measure attack attempt and the defence against it, resolved in one beat (one roll); a round holds 1 to 4 (A-101, §K); also the name of the round's closed phase in `PHASES` | `wrapper.py` `exchanges` / `outcome` event (T); `PHASES` (P) | the MB squad's round of pairings → **pairing round** (`FIELD_EXCHANGES` keeps its name); the mass-battle contact's casualty draw is the **contact draw** (§E, A-100), never an "exchange" (the old `exchange.py` pool of the field is retired with the pool); the verb `exchange` (trade) stays | `04_MB_squad_grid…` |
| **bout** | (MB) one clash of 18 field ticks; the engine calls it an "engagement turn" (`battle_loop.run_battle`) and the suite never does ("turn" is A-9's; the duel's twelve "turns" are rounds, A-101, §K; MB lexicon D-7); never a personal-combat word (the combat code's `max_bouts` counts rounds, rename candidate PCR-3) | `troops.yaml: deployment.scale` (P*) | illness or age striking a person (HAP_A) → **spell of illness** / **decline** | `22_HAPPENINGS_A` |
| **stamina / fatigue** | stamina: the reserve, a share in [0, 1] at every boundary; fatigue: its loss | `MassBattleInput.entry_stamina` (P); `troops.yaml: fatigue` (P*) | Thread Fatigue (NI `thread.thread_fatigue`) is a practitioner's, never "stamina" | `26_MASS_BATTLE_movement…`, `27_MB_E` |
| **yield** | (PC) a fighter gives up | `fight_endings: yielded` (T) | a Site's produce → **harvest** in new prose (`yield.taken`, `Rung.yield` keep their names) | `07_SE_*` new text |
| **prevailed** | the fight ending of a party left standing whose opponent fell or yielded | `fight_endings` (P, D-U1-11a) | `standing` | `03_PC_typed_outcome_one_door.md` |
| **rout / break** | **break**: the moment a unit stops fighting as a body and runs; **rout**: the running that follows (U4d: was "a body's", which this table's *body* row refuses for troops); `rally, withdraw, run` its three end bands | `26_…rout…` (P); engine `routed` (T) | "yield" (PC) at the army scale; the engine's `broken` (Discipline at nothing, formation gone, still on the field) is **disordered** (MB lexicon D-16, rename L2-2) | — |
| **riposte** (at the felling: code id `finalblow_riposte`) | the answering blow of the fighter who is about to be felled: at the felling that would decide a fight, one keyed draw (probability `UPSET_FLOOR`) turns the blow, he lands a blow back through the one damage site, and the fight continues from there (Jordan, 2026-11-12: *"it's still a riposte. it just also happens to be a final blow"*; code names the trigger: `finalblow_riposte`) | `18_DETERMINISM_no_certain_matchup.md` (P; ids `finalblow_riposte(round, by)` (was `turn`, A-101), `_wound('finalblow_riposte', …)`); the combat module's own riposte (`wrapper.py`, `RIPOSTE_ON_FAIL`, `RIPOSTE_ON_NEUTRALIZE`, `RIPOSTE_CAP`) is the same kind of return blow with a different trigger (a failed or neutralised attack) | "counterblow" (U4d's rename, reversed by Jordan), "flip" (`UPSET_FLOOR` names the old override); "upset" stays for its ordinary sense, the weaker side winning, which a riposte at the felling can cause | whether the two triggers are one code path (one owner for the riposte) is a v12 batch decision for `valoria-simplify`; U4d's nine-file rename is reversed |
| **nested contest** | a duel round called from inside a field (A-4, depth 1) | `nested_entry` (P) | "nested scene" | — |
| **kit** (was *loadout / kit*) | (person) `(primary, secondary, armour)`; (troop type) the same three | `world_q.kit_of` (T); `troops.yaml` (P*) | one primitive, two holders; "loadout" in new prose (MB lexicon D-13: the tree's word is *kit*; file names keep "loadout"; owed S-9) | — |
| **armour tier** | `none, light, medium, heavy` | `troops.yaml: armour` (P*) | "mail" for `medium` (the `arms_kinds` seed `harness_mail` maps to `medium`) | `03_PC_person_inputs_content.md` |
| **doctrine** | (MB) a row that writes standing orders | `troops.yaml: doctrines` (P*) | ED-SC-0013's "doctrine" (auto/manual) → **play mode**; Layer 1's "delegation doctrine" keeps its phrase; the pursuit `doctrine` (NI `season.pursuit.doctrine`) | `04_MB_*` |
| **frontage / front** | (MB) the width in contact | engine `MB_FRONTAGE_REF`, `MB_FRONTAGE_BLEND` (T) | `Front` referent class (BIND_E) keeps its capital; `front` as a formation post (renamed `centre`, MB lexicon D-4) | — |
| **contact draw** (A-100) | (MB) the one draw that sets how many men one side of a contact loses in one field tick: a bell curve around the count of independent duel rounds the contact holds, each at the opponent's felling chance (`MBA_DESIGN.md` §1.3); the contact has no obstacle and no pool | `modules/mass_battle/core/contact_draw.py::contact_casualties` (P, MBA-04) | **exchange** (personal combat's phase and one attack with its defence, above), "melee roll", "pool" | `04_MB_cr12_linear_law.md`, `16_PESSIMIST_MB_partition_and_the_pair_rule.md`, `27_MB_B` (superseded, marked) |
| **felling chance** (A-100) | (MB, measured from PC) the chance one man is put out of the fight in one duel round against one opponent; stored per round index, read by the contact draw | `engine/engine_params/mb_contact.json` (P, MBA-03) | "hazard", "lethality" | — |
| **exposure** (A-100, Jordan's word) | (MB) how many duel rounds a front-rank man fights in one field tick; set by posture, arc and cover, and it scales the tick's stamina drain | `references/troops.yaml: contact.exposure` (P, MBA-01) | — (Jordan's word, A-100; a count of duel rounds, never a share or a duration in seconds) | — |
| **matchup row** (A-100) | (MB) a row of data saying how one class of troops meets another in one situation (a braced pike block against a frontal charge): whether it closes, its first-tick exposure and its stand; its `status` says how it is known (`seed`, `calibrated`, `derived`, or `stated`: a row for equipment personal combat does not have, checked against history and banded to the derived rows, A-113) | `references/troops.yaml: matchups` (P, MBA-01, MBA-06) | "counter table", a name test on a troop (the charge reads the class) | `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` |
| **range band** (A-100) | (MB) a distance band in which a missile arm hits at a stated rate (close, effective, long: shares of the arm's range) | `references/troops.yaml: contact.missile.bands` (P, MBA-01, MBA-05) | "range" for a band (the arm's *range* is its maximum) | `26_MASS_BATTLE_cell_scale_and_time.md` §2 |

## F. Process words the suite uses about itself

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **owner** | the one file and key a fact is authored in | CLAUDE.md §0.05 | "home" (allowed as a synonym in prose), "source of truth" | — |
| **check** (of a proposal) | the execution artifact that shows an edit landed (a run, a hash, a test) | — | "gate" (the write gate's word, D-section above) in new text | new suite text |
| **refusal** | the loader's or the gate's refusal; a precondition failed with no contest | `04` §C.4 | "loss" (a contest that went against), "the gate refuses" for a loader | — |
| **reading** | a measurement a named instrument prints | — | the `reading:` record on a requirement row keeps its key | — |
| **pin** | a recorded hash a test compares | `engine/season/tests/_realm_goldens.py` (P) | "golden" (allowed as the tree's process word, CLAUDE.md §7; it is software jargon with no ordinary sense, so new prose says "pin" and keeps "golden" for file and test names) | — |
| **mover** | an edit declared to change seeded results | — | — | — |
| **Layer** | always numbered and capitalised (Layer 0, Layer 1, Layer 2) | CLAUDE.md (RULED) | "layer" for an epistemic or narrative layer in code keeps its lower case and its qualifier | — |
| **loop** | the season loop | CLAUDE.md | the apparatus pathology is "the apparatus loop", never bare (VOC's measured collision) | — |
| **roll / draw / check / test** | see §A | — | "test" only for a pytest test | `07_SE_*`, `16_PESSIMIST_SE_A` |
| **wire / reader / orphan** | a declared thing and its caller | `04` ID-13 ("a field nothing reads is not a field") | "cut wire", "dead": say "has no reader". U4d: "uncalled" (a function) and "unread" (a field) are ordinary and exact, and stay | `17_CENSUS_*` new text (U4d: `17_CENSUS_REST_2_wiring.md` done) |
| **removal test** | suppress one person's choice at one round, replay, and count the others' acts that differ (renamed by U4d from the coinage "knockout"; ids `removal_arm`, `--remove`) | `16_PESSIMIST_CORE_the_nine_gate_and_a_knockout_reading.md` (P; the file name keeps its word) | "knockout" | — (U4d: done in four files) |
| **roga, fisc, Kontor, rector, sekreton, catasto, missus, dedizione, commenda…** | historical loan words in institutions prose | — | prose uses the plain word (stipend, treasury, trading house, …); data ids are plain words (`warrant`, `commission`, `tithe`, already) | `15_INSTITUTIONS_BYZANTINE_*`, `_VENICE_*`, `_COLONIAL_*` |

## G. Names the naming gate binds

The canonical name of the god and the Church is **Solmund** (`world.solmund`, NI, `enforce: block`); the Church's
display name is **Church of Solmund** with the alias **Church** (`world.church`). Valorsmark's alias is **Crown**
(`world.valorsmark`). No suite file may introduce a name for a faction, house or person that `names_index.yaml` or
`references/proper_noun_registry.yaml` does not carry; a new one is a registry row first.

## H. Rows added by U4d, and tree names that fail the word test

Terms the reconciled proposals use that had no row. The last column is the ordinary-English test (`STAGES.md`):
**passes** where a reader with no memory of this repository lands on the meaning; **tree name fails** where the
word is a code identifier whose ordinary sense differs (not renamed here: the plain word is recommended, prose
uses it and gives the identifier in backticks once, and the rename is a v12 candidate, `OWED_TO_UNIFICATION.md`
§B).

| term | meaning | owner | rejected / other senses | word test |
|---|---|---|---|---|
| **venue** | the place where a sitting or hearing is held (a `Date`'s venue; a bench's seat of judgement) | `state/carriers.py` (T, the `Date` venue) | the SC kernel's "venue preset" is that retired module's word for a hearing type | passes (law: the place a case is heard) |
| **WITNESS / witness** | WITNESS: the loop step that deposits claims into each holder's own ledger; a witness: a person present at an Event | `04` §A.2 `loop/witness` (T) | `the_room(w, event_id)` → `witness_regard` (see *room*) | passes |
| **deposit** | WITNESS's write of a claim into a holder's ledger, and the confidence written then | `04` §A.2 (`claim.deposited`, T) | — | passes (to put something in keeping) |
| **claim** | `Claim`: a statement a person holds about the world, with a confidence; it may be false | `state/carriers.py::Claim` (T) | a right asserted (to land, a throne, a seat: A-19, A-58, A-74) is always "a claim **to** X"; a creed Proposition is named in full | passes (an assertion that may be disputed); the two senses kept apart by "to" |
| **ledger** | a person's own store of claims; also the deed ledger (institutions) and the ED ledgers (process) | `04` §A.3 `state/ledgers` (T) | — | passes (a book of account, figuratively of what one holds against others) |
| **Tenure / hold** | a held relation of a person to a seat, place or person (`hold`, `commit`, `oblige`, `reside`, `contain`, …); **hold** is the Tenure by which a holder has a seat | `04` §B.8 (T) | MB posture `hold` (a unit standing its ground) is the ordinary verb and keeps its key | passes (tenure: the holding of an office or land) |
| **cohort** | a population group: a `Person` at `weight > 1` | `04` S9; `engine/season/cohorts.yaml` (T) | a Roman cohort (a body of troops) is not meant | passes (demographic sense) |
| **chronicle** | the reader that prints a world's Events in order with their causes | `engine/season/harness/chronicle.py` (T) | — | passes |
| **carrier** | (1) a Layer 1 state carrier (`Person`, `Office`, `Record`, `Site`, `Rung`, `Event`, …); (2) the proposal that carries an edit ("the carrier") | `state/carriers.py` (T); (2) plain English | — | passes (that which carries) |
| **channel** | the one route a quantity takes into a roll: leverage enters as named levels on one channel; a seat reaches a roll by two (its `office` level and `rank_gap`) | `sigma_leverage` (T); D-U1-01 | a news "channel" (a `reach` row) is named in full | passes (a means by which something passes) |
| **key** | (1) a data key (a roster or YAML key, a seat id); (2) a draw's key `H(seed, tick, subject, purpose)` (A-30: "one draw per key") | `engine/dice_engine/draw.py` (P) for (2) | a skill ("holds the key at 2" → "holds the skill"); the retired Key substrate (ED-IN-0232) | passes in senses (1) and (2) |
| **dial** | a setting that sizes a rate or a weight, shipped at its control value ("a dial at zero") | a `Fixtures` field (T) | — | passes (a control one turns to a level) |
| **docket / bench / remit** | the matters waiting before a bench; the judges of a court as a body; the acts a seat may perform | `DocketItem`, `Seat.remit_acts` (T) | — | pass (legal and administrative English) |
| **slate** | the list of questions a season puts to the player (A-48) | `11_GO_player_surface_contract_B.md` (P) | — | passes (a list of candidates or business) |
| **strife / strand** | the realm's open lines of conflict; one strand opens, grows, joins and ends (A-45) | `world_q.Strand` (P) | "flow" (see *strand* above) | pass |
| **dataclass** | a typed Python class holding a module's input or outcome | `queries/inputs.py` (T) | "typed record" (U4d: `Record` is the document carrier) | passes for its readers (code prose only) |
| **choice score** | the chooser's valuation of one candidate act, a sum of score terms | `decision/choose.py` score terms (T) | "ordinary score" (U4d); bare "score" anywhere (A-98 (5): always with its kind) | passes |
| **fixture** (`Fixtures`) | a named setting in `engine/season/data/fixtures.py::Fixtures` | `data/fixtures.py` (T) | — | **tree name fails**: ordinary "fixture" is a thing fixed in place or a scheduled match. Plain word: **setting**. Rename cost: class and readers in 52 code files; no hash moves [ASSUMPTION: no fixture's class name enters hashed state; not measured] |
| **obligees** (`offices.yaml` key) | the persons sworn to a seat | `engine/season/offices.yaml` (T) | — | **tree name fails**: ordinary "obligee" is the party an obligation is owed to (the seat), the reverse. Plain word: **sworn**. Cost: 17 code and data files (`harness/obligee_report.py` among them); no hash moves [ASSUMPTION: the key is read at build and becomes `oblige` Tenures, so its name is not in hashed state; not measured] |
| **subformations** (`armyrecord.KEYS`), `orderofbattle.Subformation` | one unit (a row of the army Record, A-2) | `modules/mass_battle/` (T) | — | **tree name fails** (it names one unit, while ordinary English and Jordan's A-59 mean a group of units). Plain word: **units** / `UnitRow` (not `Unit`: the engine's `Unit` is one side's army, itself a failing name, L2-1). Cost (MB lexicon, `MB_LEXICON_part3.md` §4 L1-1, L1-2, measured by `git grep -l`): 15 files hold `subformations`, 6 hold `Subformation`; the Record's keys enter `World.content_hash()` (`state/world.py:1667-1707`), but no shipped season should hold an army Record (the army verbs are withheld, `fixtures.py:1157`) [ASSUMPTION; the batch gate reads the realm pins]. J-U4d-02 answered by A-94; the word is freed for Jordan's sense (L1-6) |
| MB **`stance`** (unit field) | a unit's tactical setting | `modules/mass_battle/orderofbattle.py` (T) | Layer 1 `stance` (a stored regard row) | **tree name collides**: both senses are ordinary, but one word names two things. Plain word: **posture** (`march_postures` precedent). Cost (MB lexicon §4 L1-4, D-9): the army Record's row key and payload key are renamed (the L1 files); the engine attribute `Subunit.stance` (41 files mention `stance` in the MB code and tests) is **not** renamed, because the order vocabulary sets attributes by name (`check_orders`, `_ORDER_SAFE_FIELDS`), which makes it a change of the exported order format |
| **`pool.py::faculty`** | the pool reader | `engine/season/seam/wrappers/pool.py` (T) | — | **tree name fails** (ordinary "faculty" is an inborn power). Plain word: **pool**; D-U1-08 already splits it into `score` + addends. Cost: 38 code files mention `faculty`; no hash moves by the rename alone |
| **storybar** (`harness/storybar.py`) | the story instrument: counts story shapes per arm | `engine/season/harness/storybar.py` (T) | — | **tree name fails** (no ordinary sense). Plain word: **story count** (the *census* row's word). Cost: 18 code files; harness only, no hash moves |
| **aperture** (`harness/aperture.py`) | per-verb counts of acts attempted, executed and refused over a run | `engine/season/harness/aperture.py` (T) | — | **tree name fails** (an aperture is an opening). Plain word: **act count**. Cost: 23 code files; harness only, no hash moves |
| **spine** (`governance_spine`) | the hand-built governance test world (thirteen seats) | `engine/season/` builders (T) | — | **tree name fails** (a backbone). Plain word: **governance test world**. Cost: 13 code files; no hash moves by the rename alone |
| Tenure **edge** | a Tenure seen as a link between a person and a seat, place or person (`one_edge`, "ended edges", `04` AX-6) | `04` §B.8 (T, Layer 1 vocabulary) | the skill role *edge* | **tree name fails** (graph jargon; an edge is a border or an advantage). Plain word: **link**. A Layer 1 wording amendment, not a batch edit alone. Cost: not taken (the word "edge" appears in about 210 tree files in several senses) |
| `VOCATIONS`, `vocation_attribute` | the tree's old skill roster | `data/verbs.py`, `rosters.yaml` (T) | — | tree name fails ("vocation" is a calling); already ordered deleted by CAP A2/A3 (OWNERS C-04), so not a new candidate |
| **`capability`** (`Person.capability`, DR `capabilities`, `capability_uses`, `capability_roles`, `capability_use_sites`, `capability_factor`, `capability_admits`) | a person's skills; the skill roster and its tables | `state/carriers.py::Person` (T); the rest (P) | — | **second name** (A-98): ordinary "capability" is a power to do something, close enough that the word passes alone, but one thing now has two names. Plain word: **skill**. Cost (measured 2026-11-12 by `git grep -l -w`): 106 files under `engine/`, `modules/`, `references/`, `tools/`, `tests/` hold the word, 31 code files read `.capability`; the proposed names (P) cost nothing to rename before they land `[ASSUMPTION: whether the field name `capability` enters `World.content_hash()` is not measured]` |
| combat attribute **`faculty`** (`modules/combat/attributes.py` SPEC) | the party's skill score for the fight's verb, carried as a combat attribute | `modules/combat/attributes.py` (T) | — | **mislabel** (A-98 (1)–(2): a skill score is not an attribute) as well as a failing word (§*faculty*). D-U1-08 replaces the input field `faculties` with `scores`; the spec entry is not yet ordered out (`work/A98_DERIVED_SCORES.md` mislabel 2; for the orchestrator) |

## I. Record of the U4d pass (2026-11-12)

**Rows checked:** 129 rows of §A–§F plus §G (the naming gate). **Matches fixed:** 246 occurrences in 91 live
files (88 proposals, `U1_OWNERS_AND_VOCABULARY.md`, `U3_CONFLICT_LEDGER.md`, `U3_DEPENDENCY_ORDER.md`): "Ob" →
obstacle (19 files), "fought scene" → fight (10), "typed record" → dataclass (11), "vocation" → capability (11),
"obligee" → sworn man (7), MB "stance" → posture (8), "subformation" (a unit) → unit (6), "graded route" → task
route (6), "patient" → counterparty (5), "fisc" → treasury (4), "faculty" → capability or score (5), "ordinary
score" → untrained score (3) or choice score (3), "province" → territory (2), "highest-held" → strongest (2),
"distance band" → distance step (2), and one file each for "task difficulty", "settled margin", "reading
record", "cut wire", "aptitude" (the attribute), "key" (a capability). Each file's last `Reconciled:` line names
its changes; the full ledger is `work/U4D_RENAMES.md`. **Rows added:** 17 rows of terms and 10 rows of tree names (§H), plus
**removal test**, **task route** and **choice score** inside existing rows. **Words renamed:**
knockout → **removal test** (four files). (riposte → counterblow, nine files, was reversed by Jordan the same day: the word is *riposte*; the code id is `finalblow_riposte`.) **Tree-name mismatches listed
as v12 candidates:** eight (§H: `Fixtures`, `obligees`, `subformations`/`Subformation`, MB `stance`,
`pool.py::faculty`, `storybar`, `aperture`, `governance_spine`) plus one Layer 1 wording (Tenure *edge*).
**Jordan's terms flagged:** four (`U4D_FOR_JORDAN.md`: regime, subformation, prowess with aptitude, rung).
**Corrections to rows:** *arm* (a file named in error), *rout* ("a body's" → a unit's or side's), *susceptibility*,
*upset* (kept in its ordinary sense), *golden*, *uncalled*/*unread*, *graded act*, *base* (an army's base), *body*
(an institution), *approach* (A-83's sense).

**The word test, word by word** (the lane's list; judged against ordinary English, not the tree's use). *Pass:*
band, degree, venue, loadout, receipt (an acknowledgement of a transaction), witness, ground, hold, seat, body
(two ordinary senses, kept apart), claim (with "a claim to" for a right), record, approach, capability, cohort,
chronicle, deposit, carrier, stake, habit, strand, register, key (data and draw senses), channel, pool (the dice
pool of tabletop play), score, talent, base, ledger, reading (a meter's figure), passage, lapse, gate (a check
to pass), site, row, edge (the role: an advantage), member, leverage (influence or advantage), engine, surface
(the player's surface only; the glossary heading "The capability surface" became "Capabilities"). *Fail, suite
coinage, renamed:* knockout (riposte was renamed and the rename reversed by Jordan). *Fail, tree name, candidate:* faculty, vocation (already ordered), the
Tenure edge, fixture, obligee, storybar, aperture, spine, `subformations`. *Fail or narrowed, Jordan's word,
listed:* regime, subformation, prowess (with aptitude), rung (for a place).

**Left as they are** (ordinary-word uses or quotations): "faculty" in Jordan's A-59 quote (`27_MB_A`), in
`09_WR_B_threadwork_session_and_practitioner.md` ("the faculty judging itself"), in `AUDIT_BRIEF.md` (Disco
Elysium's faculties) and in code (`def faculty`); "Ob" inside quoted rulings and old text (`16_PESSIMIST_SC_A`
§*"never an Ob reduction"*, `16_PESSIMIST_SC_D`'s quoted figure, OWNERS charge 3), in "Three-Axis Ob" (the
threadwork design's name) and in `OB_MIN`, `opposed_ob`; "patient" for a person being tended (`03_PC_exits`,
`14_VERBS_MATERIAL_A`, `U5c_SC_one_obstacle_form` member 28) and "the patient man" (`28_CORE_C`); "graded
inquiries" for the three inquiry verbs and "graded act" (ordinary); "upset" (ordinary: the weaker side winning);
"fallback" (45: a plan's or code's fallback, never the stand-in); "province" in history and the geography file's
`provinces` key; "set piece" (CL-OPEN's design name); "copying" (the scribe's capability, not a lie); "rhetoric"
(NPC-001's canon trait, quoted); "susceptibility" (ordinary description); "uncalled", "unread"; "half the score",
"bench die", "office weight", "settled margin" where a sentence names the retired rule as retired; the historical
loan words in italics as historical parallels (*sekreton*, *missus*, *catasto*, *commenda*, *dedizione*,
Kontor glossed as a league chapter); `storybar` in command lines; "obligees" as a YAML key; file names
(`…_knockout_reading.md`, `…_roga_and_the_fisc.md`, `01_CORE_requirements_reading_record.md`).

**Not checked** (one round): the rejected senses that are common words ("check", "test", "level", "post",
"step", "price", "cost", "risk", "advantage", "edge", "message", "bonus") were not swept, since most uses are
ordinary; `IMPLEMENTATION_BRIEF_A.md` (one "fought scene" in a brief, not a proposal); the `unified/` documents
outside OWNERS and U3 (`DECISIONS_FOR_JORDAN.md`, `U4_*`, `U5_CONFLICTS_*`, `work/`); every `14_VERBS_*` body
for "stance" in the person sense was read only at the hit lines.

**The A-98 pass (2026-11-12; ledger `work/A98_SWEEP.md`).** Jordan's A-98 (aptitude = attribute; learned rank =
skill; martial skill; one kind, skill; derived scores) superseded the rows *talent*, *aptitude*, *training*,
*prowess* (of a person) and D-U1-11p/q. **Rows rewritten:** §A *pool*, *score* (now *skill score*), *training*,
*talent* (retired), *untrained score*, *base*, *opposition*, *ceiling*, *inquiry*, *arm*; §B whole (heading,
*attribute*, *aptitude* (retired), *skill*, *capability* (the tree's second name for skill), *trait* (a roster of
its own `[ASSUMPTION]`), *ability*, *role*, *site*, *gate*, *judgement*, *law*, *deception*, *insight*, *command*,
*faculty*, *rank*, *prowess*); §C *resolve*, *voice*; §H *key*, *choice score*, Tenure *edge*, `VOCATIONS`.
**Rows added:** *skill score*, *governing attribute* (§A); *martial skill*, *derived score* and five derived-score
families (*health and wounds*, *reserves*, *the body over time*, *the interior*, *Thread Pool Score*) (§B); §H
`capability` (rename candidate: 106 tree files hold the word, 31 code files read `.capability`) and the combat
attribute `faculty` (a skill score held as an attribute). **Derived scores found in the tree:** 18 a person's
(`work/A98_DERIVED_SCORES.md`), six mislabels named there. **Swept:** 115 files (101 proposals, 13 `unified/`,
1 `master/`): *capability* in prose → skill 371 (scripted) plus this file, OWNERS and the architecture; *trained
score/rank* → skill score 137; *talent* → attribute or governing attribute 75 (plus 15 in OWNERS and the
architecture); *training* (the rank) → skill score 24; *aptitude* 10 by hand; *prowess* of a person 1 (no other live
use); proposed identifiers 35 (`talent_level` → `attribute_level`, `pool.py::talent` → `governing_attribute`, three
test names); 8 places where *capability* had meant a trait or Thread Sensitivity reworded. **Left:** quotations,
`Reconciled:` history, the closure and question records, document and batch names, identifiers, ordinary senses
(training as the act, troops trained, a unit's prowess) (`work/A98_SWEEP.md` §Left). **Layer 1:** no retired word
but *capability*, mostly as the identifier; listed in `work/A98_LAYER1_WORDS.md`, not edited. **Not checked** (one
round): bare "score" outside the phrases swept; the suite-root briefs.

## J. Mass battle lexicon (A-95; `unified/MB_LEXICON.md`, `_part2`, `_part3`)

The army vocabulary is settled in the lexicon; each row here is a pointer. Where a §E row and the lexicon
differ, the lexicon governs (the §E rows were corrected to it on 2026-11-12). "Group" is the lexicon's §2
group (A–D in `MB_LEXICON.md`, E–G in `_part2`); "D-n" a ladder decision and "L/S-n" a rename in `_part3`.

| term | one line | lexicon |
|---|---|---|
| **realm, faction** | the kingdom; a house, Church or movement that may raise one army | §1.3 |
| **army** | a faction's one fighting force, its men in units under the commander who holds its Record | A; engine `Unit` → `Army` (L2-1) |
| **side** (attacker, defender) | the men on one side of one battle | A, G |
| **subformation** | the units at one post of the army formation, fighting by one set of tactics (Jordan's word, A-59, A-94) | A, D-1 |
| **unit** | a row of the army Record: men of one troop type with an officer and orders | A, D-2; L1-1, L1-2, L2-1 |
| **cell**; **rank, file** | the smallest square of the field and its men; period words for lines of men (the engine's are cell rows and cell columns) | §1.3, A, C |
| **squad** | a handful of named characters on a small grid, below a unit | A |
| **troops**, **troop type**, **levy** | the men; the kind of soldier; the lowest-grade foot (never the act of raising) | A, D-6 |
| host, company, banner, battalion, regiment, retinue, van | not game terms | A, C, D-20 |
| **commander**; **officer** | the holder of the army Record; the leader of a unit (one may lead several, C5) | B, D-5 |
| general, captain, marshal, constable | not army roles (*marshal* is a verb and a canon seat title) | B |
| **command**; **command basis** | the skill by which an order takes effect (skill score plus attributes, A-59, A-7, A-98); whom a seat may order (A-22) | B |
| **order**, **standing order**, **signal**, **window** | an instruction to a unit; one given in advance; one fired to release others; a moment in a bout to act | B, C, D-14; L1-3 |
| **order of battle** | an army's units as fielded in one battle | C, D-14 |
| **army formation**, **unit formation** | the army's layout (`line`, `envelopment`, `refused_flank`; Jordan's "grand formation"); a unit's depth, width and shape | C, D-3, D-15 |
| **post**; **centre, wing, rear, reserve**; **rearguard** | the five places of the army formation and their subformations; a unit ordered to hold while its side withdraws | C, D-4 |
| **line**, **frontage**, **depth** | the battle line; the width in contact; how deep (A-60) | C |
| **tactics**, **doctrine**, **role**, **posture** | what a subformation fights by; the default standing orders by (troop class, post); a unit's job; a unit's readiness to close | C, D-9; L1-4 |
| **kit** | primary, secondary, armour | C, D-13 |
| **muster**; **recruit**; **form, assign, order, disband, discharge** | men gathered at a place to march; to raise men into the army; the army verbs | C, D-6 |
| **strength**, **numbers** | men present and fit to fight; A-60's word for the same | D, D-12 |
| **prowess** | a unit's quality of troops and equipment (A-59); never a person's: a person's skill at arms is his **martial skill** (A-98) | D, D-19 |
| **morale**, **discipline**, **raw**, **experience** | the unit's will, steadiness, newness, battles fought | D |
| **power** (retired, A-100) | was a troop type's weight of blow, one input to its prowess; the weight of blow now belongs to the arm and the armour (measured) and the men's quality is their **martial skill**: the troop column `skill`, a skill score on the duel's scale (A-98 (3)) | `troops.yaml: troops.<type>.skill` (P, MBA-01 step 2; `power` is an alias until MBA-04) | "power" for an army's or side's fighting value (A-59) | `27_MB_B_unit_prowess_on_the_row.md`, `MB_LEXICON.md` |
| **stamina, fatigue, endurance** | the reserve, its loss, A-60's lasting | D |
| **battle** (field) | a fight between two sides at one place in one season, of one or more bouts | E, D-18 |
| engagement, skirmish (as a size), fight (for a battle) | refused | E |
| **field tick** < **engine phase** < **bout** < **battle** < **season**; **lull** | one clock word per quantity; the pause between bouts | E, D-7; L2-3 |
| **contact**, **flank**, **envelopment**, **refused flank**, **wheel** | ordinary tactical words, as the engine uses them | E |
| **stand** (draw), **give ground**, **fall back**, **withdraw** | hold; step back still fighting; leave at the fall-back point; leave the field in order | E, D-10 |
| **break**, **rout**, **disordered**, **rally**, **run**, **pursuit** | start to run; the running; formation gone but not fled (engine `broken`); brought back in the battle; flee; chase the broken | E, D-16; L2-2 |
| **duel round** | one round of a duel called from inside a battle (A-4, A-72); also the contact draw's unit: the felling chance is measured per duel round (A-100); the same round as any personal-combat round (A-101) | E; §K |
| **contact draw**, **felling chance**, **exposure**, **matchup row**, **range band** | the A-100 rows: how a contact is resolved from measured duel rounds, not a pool against an obstacle | §E |
| **end state**: won, lost, drawn; unopposed, invested | how a battle ended, from the attacker's side; never "a draw" as the noun in MB prose | F, D-8 |
| **casualty**, **loss**; **dead, captured, injured, fled**; **regroup**, **deserter**, **return** | the engine's count; every man missing after; its four kinds; fled men coming back; those who never do; the partial return | F, D-17; S-2 |
| **march**; **storm, besiege, invest, siege**; **garrison** | the verb; the march postures and their states; (tree) a place's defences | G |
| **station** (Jordan also: base); camp | where an army stands when not marching; not a game term | G, D-11 |
| **occupy, seize, withdraw, raze**; **aggressor, rescuer** | A-57 to A-73's land acts and parties | G |

Record of this section (MB lexicon lane, 2026-11-12): §E rows *unit*, *formation*, *cell*, *body*, *bout*,
*rout / break*, *kit* (was *loadout / kit*), *frontage / front*, §D *post*, and §H rows `subformations` and MB
`stance` corrected to the lexicon. The §B *prowess* row and D-U1-11p are A-98's sweep lane's.

## K. Fight and clock words (A-101; `master/pc_round/PC_ROUND_SPEC.md`)

A personal-combat fight is a sequence of rounds (A-101): two fighters close, exchange attempts to attack, and
separate, many times, as boxers and fencers do. The words below hold one meaning each; the clock table under them
is the one statement of how the game's time words nest. **No clock in the game counts seconds**: the seconds column
is an indicator (A-101's 4 to 10 seconds for a round; the field tick's about four seconds, MB lexicon), never a
stored duration.

| term | meaning | owner | rejected / other senses | files to change |
|---|---|---|---|---|
| **fight** | violence between persons with no terms agreed beforehand (war, crime, defence, enmity), played in personal-combat rounds from the first round to its ending (felling, yield, withdrawal, or twelve rounds undecided); A DUEL IS NOT A FIGHT (Jordan, 2026-11-14) | `modules/combat/fight.py::fight` (the module's function name resolves both and stays in code); `wrapper.fight` (T); the verb `fight` | "fight" for a battle is refused (§J) | — |
| **duel** | a contest run through the personal-combat engine between two combatants, in which the victor, who is not to kill or severely wound the other, resolves a dispute with it, with duelling weapons only: rapiers, arming swords, épées or spears (Jordan, 2026-11-14, `[ASSUMPTION: the list is Jordan's "I think", to confirm]`); a challenge and its acceptance (an executed `accept`) open it; played in the same rounds as a fight, but a different thing: agreed, formal, bounded by that restraint, and a means of settling a dispute | the verbs `challenge` and `accept`; `duel.yielded`; `modules/combat/fight.py::fight` resolves it | "duel" is not used for violence with no agreed terms, nor for a killing | — |
| **round** | one engagement of a fight: the two close, exchange attempts to attack (1 to 4 exchanges, the cap `BURST_MAX`), and separate; about 4 to 10 seconds as an indicator, never a clock (A-101) | `wrapper.engagement` (T; one call is one round; the name `engagement` is kept in code only); `fight_round` (P, PCR-2) | **turn** (the code's `turn_start`, `decide(turn)`, `Yield.turn`, `CombatTurnView`: rename candidate PCR-3), **bout** (the code's `max_bouts`; a bout is the battle's), **engagement** in prose; the season's within-season pass → **lap** (§D) | the PC proposals carry a `Reconciled:` note (2026-11-12, A-101); `03_PC_typed_outcome_one_door.md`'s `turns`/`turn` fields renamed `rounds`/`round` |
| **duel round** | a round called from inside a battle (A-4, A-72: a battle may call one; it calls nothing); the same round, named for where it is called; it is also the unit in which mass battle's felling chance is measured by simulated fights (A-100: the contact draw, §E) | `nested_entry("combat.round", …)` (P); `fight_round` (P, PCR-2) | "nested scene", "single combat" | — |
| **closing** | the part of a round in which the gap is closed: the approach at open measure, with the longer weapon's stop-hits; instant when the reaches are near equal or the point cannot hold the closer off | `wrapper.py` open-measure block (T) | "approach" for this (the word is the PC lean's, §E) | — |
| **attack attempt** | any attack in a round: an exchange's attack, a stop-hit on the closing, a pursuit strike on a failed withdrawal | the `roll`, `stophit`, pursued `disengage` trace events (T) | — | — |
| **separation** | the end of a round with both standing: the fighters are apart (a clean defence, the exchange cap, a stamina collapse, a clean withdrawal, a re-opened measure, met terms) | `ROUND_ENDS` (P, `modules/combat/vocabulary.py`) | "break" (an army's, §E) | — |
| **beat** | one step of a round's loop, in which at most one attack is made; the engine's unit of cadence, never a unit of time a player sees | `wrapper.engagement`'s `beats`, `BEAT_BUDGET` (T) | "exchange" (an exchange happens in a beat; a beat may hold none); "turn"; "beat" as "defeat" in ordinary prose stays | — |
| **turn** | A-9's short sequence of a scene's steps; nothing in a fight | A-9 | the duel's iteration → **round**; the battle's 18 ticks → **bout**; "one turn of the loop" for a season (§D) is the plain phrase and stays | the PC files listed in the *round* row |
| **lap** | see §D | | | |

**The clock table** (one word per quantity, smallest first within each scale):

| scale | word | size | what counts it | owner |
|---|---|---|---|---|
| person (a fight) | **beat** | one loop step; no seconds | `beats` | `wrapper.engagement` (T) |
| person | **exchange** | one attack attempt and its defence; about 1 to 2 s, an estimate | `exchanges` | `wrapper.engagement` (T) |
| person | **round** | closing, 1 to 4 exchanges, separation; about 4 to 10 s, an indicator (A-101) | one `engagement` call | `wrapper.engagement` (T) |
| person | **fight** | up to 12 rounds | `max_bouts` (T; `max_rounds`, PCR-3) | `wrapper.fight` (T) |
| battle | **field tick** | about 4 s | `troops.yaml: deployment.scale.tick_s` (P*) | MB lexicon D-7 |
| battle | **engine phase** | 6 field ticks | `TICKS_PER_PHASE` (T) | MB lexicon D-7 |
| battle | **bout** | 18 field ticks, about 70 s; two windows (a duel round may be called at a window) | `bout_ticks` (P*) | MB lexicon D-7 |
| battle | **battle** | one or more bouts, a lull between | `max_bouts` of the field (P*) | MB lexicon D-7 |
| season | **lap** | one pass of DELIBERATE, RESOLVE, WITNESS; `scene_budget` of them a season | `Claim.round` (T; `lap`, PCR-4) | `state/carriers.py` (T) |
| season | **season** | one turn of the loop | `tick` | `loop/driver.py` (T) |
| year | **year** | four seasons | `seasons_of_year` | §D |

A fight is one act inside one scene and never advances the season's clock; a duel round inside a battle does not
advance the field's ticks (it is about one to two field ticks by the indicators, nothing more).
