# 23 · Story enablement: how the stories the game cannot tell become stories it can

## Status: REFERENCE (a planning lane; resolves nothing at runtime, CLAUDE.md §0.05; its edits are proposals `proposals/23_STORY_*.md`)

## Read at: 54a7c25 (working tree)

Work order (Jordan, 2026-11-12): *"Fable to plan how to make the impossible stories possible."* Briefs:
`AUDIT_BRIEF.md` (the standing rule, *we do not do deterministic*; playable standalone; the NPC and chooser
intent; authority to design, as proposals) and `PESSIMIST_BRIEF.md` (the emergent-narrative method: beginning,
escalation, reversal, cost, an ending that is not an arbitrary stop, retelling).

Inputs, cited and not redone: the twelve pessimist audits (`audits/16_PESSIMIST_{GAME,CORE,CHAR,PC,MB,SC,FA,SE,FI,WR,DICE,GO}.md`),
`20_NARRATIVE_CHURN.md`, `22_HAPPENINGS.md`, `12_ARCS_adjudication.md`, `09_WR_audit*.md`,
`15_INSTITUTIONS_SYNTHESIS.md`, `19_LACUNA_investigation_to_proceedings.md`, `21_PROCEDURAL_GENERATION.md`,
`18_DETERMINISM_SWEEP.md`, and the suite's proposals. A count or a run quoted here is the cited lane's unless
it is in this file's evidence log (§9).

Layout: §0 verdict · §1 what counts as a story · §2 the story inventory · §3 the shared missing mechanisms,
ranked · §4 the mechanisms designed at their owners · §5 per-story chains · §6 the enablement plan (batches,
gates, story bars) · §7 the first playable · §8 decisions, and what is Jordan's · §9 evidence log.

## 0. Verdict

**Every impossible story the lanes named can be made possible without a script, and almost all of the
design already exists in this suite; what does not exist is the order that makes one story complete and
an instrument that can say a story occurred.** The twelve pessimist audits, the narrative-churn audit and
the happenings audit name **73 distinct stories** the shipped game cannot tell (42 of them named by more
than one lane; 56 have no code path, 15 have a path computed play never reaches, 2 occur only in a
hand-built world). Their minimal chains share **nineteen mechanisms**. Three are a floor under all 73:
the offer makes sense, the act is drawn and its bands write, the record keeps cause, value and margin.
Above the floor the count of stories each unlocks is: a hearing that binds and ends 13; regard that moves
with deeds and dues 13; seats that pass by a draw 10; places that differ and stores that bind 10; deeds
that leave a trail 9; instruments and ties 9; a field that can be won 8; news that travels with a name 8;
violence with a cause and a mercy 6; the world that strains and ends 6; bodies and time 6; the interior
that draws 5 (§3, counted from §2 by `p2_count.py`). **Sixty-seven of the 73 have every absent link
carried by a proposal already on file**; the chains in §5 cite it link by link.

**Six stories had a link no proposal carried** (and two more, the regency and the made name, gain a
variant), and they reduce to three mechanisms, written here as
proposals: what a roll leaves behind (the disaster, the success that costs, the contest with a loser, the
comeback remembered: `23_STORY_A`); a house that continues (a marriage, a birth, a coming of age, and so
a minority and its regency: `23_STORY_B`); a founded place that can fail (`23_STORY_C`). Two more
proposals carry what the plan itself needs: a **story census** on the one story instrument, which names a
story by its beats in the cause graph and prints its rate, its spread of endings and its control
(`23_STORY_D`), and a **first playable**, *The Lean Year*, a valley of three towns, one granary, one old
lord, two claimants and one bench, which can produce 33 of the 73 in eight seasons from persons' acts
(`23_STORY_E`).

**The single largest obstacle is not a missing mechanism; it is that no gate in the suite is a story.**
Each lane gates its own link (a verb executes, a band occurs, a claim is held). A realm in which every
such gate passes can still tell nothing, because a story is a chain across lanes: a drawn cause in the
world, a person's drawn act on it, a named consequence, news of it reaching someone who minds, and that
person's drawn answer. The enablement plan (§6) therefore orders the suite's proposals into **twelve
batches by what each completes**, opens with the instrument, and gates every batch on the census: the
story occurs in a seeded multi-seed run from persons' acts, at some seeds and not all, with more than one
ending, and does not occur with its mechanism at control.

**On the standing rule.** No chain in §5 has a link that is a fixed function of state. Where a lane's
story list implied one (a counter that ends an arc; a town that dies when its number reaches zero; a
disaster "at" a threshold), the link is restated as a draw whose odds are set by persons, seats, places,
evidence and history, or as bookkeeping that follows a draw (§8 R-01 to R-04). **One item is Jordan's
from this lane** (whether named persons are born in play, §8 J-1); twelve items other lanes already
escalated bear on the plan and each has a default under which no batch waits (§8.3).

The steelman holds and is the plan's premise: the kernel is honest (one clock, one gate, causes on every
Event, seeded replay), nothing is scripted, and the suite's proposals between them name nearly every
closing verb. This file adds the sum.

## 1. What counts as a story, and how a chain is marked

**The bar.** A happening counts as a story when a reader of the record, with no access to the code, can
say all six of these, and when a seeded run can fail to produce it:

1. **a beginning with a cause**: someone wanted, was wronged, was owed, feared or learned something, and
   the record names what;
2. **stakes**: something a person in the fiction would mind losing (a life, a seat, a store, a tie, a
   name, a belief) is put at risk by an act or by the world's own drawn motion;
3. **a turn**: a draw falls, or another person answers, so that what the opener expected is not what
   happened;
4. **a cost**: somebody ends worse off in a quantity the record holds;
5. **an ending that is not an arbitrary stop**: a closing Event by a person's act or a drawn break, never
   a counter reaching a number, never the run ending;
6. **retelling**: the chain can be rendered with who, what, about what, on what odds, how it fell and
   who learned of it.

**Non-degeneracy.** Over seeds the story occurs sometimes and not always, and when it occurs it does not
always end the same way. A story that occurs at every seed with one ending is a schedule; a story that
occurs at none is absent; a story that occurs equally often with its mechanism at control is something
else being counted (§6.1 states these as the six clauses every gate here uses).

**Chain marks** (§5). Each link of a story's minimal chain carries one mark:

| mark | meaning |
|---|---|
| `[R]` | exists in code and is reached in computed play (some lane saw it execute with no planted state) |
| `[N]` | exists in code and is not reached: refused, unformed, or shipped at its control |
| `[A]` | absent: no code path; the carrying proposal is cited, or the link is a **GAP** this lane fills |

Evidence for a mark is the cited lane's run unless §9 lists it. A mark of `[R]` is a claim that the thing
works today and was checked at the call site by the lane cited (§0.1 pt 3); I re-ran none of the realm
readings (the machine was loaded; §9).

**The floor.** Three mechanisms stand under every story and are not repeated in the inventory's
mechanism column: **M1** the offer makes sense (an act is formed on a thing it can be done to),
**M2** the act is drawn and its bands write, **M3** the record keeps the cause, the value and the
margin. A story whose only missing links are floor links is marked `floor`.

## 2. The story inventory

Seventy-three stories, merged across lanes. *Named by* gives the lane(s) whose list holds it. *Today*:
**X** no code path · **N** a path exists and computed play never reaches it · **H** occurs only in a
hand-built or planted world. *Needs* lists the mechanisms of §3 beyond the floor; **G1** to **G3** are
gaps no suite proposal carried before this lane.

Short names for proposal files (all under `proposals/`): HAPP-x = `22_HAPPENINGS_x_*`; PES-LANE-x =
`16_PESSIMIST_LANE_x_*`; VB-x = `14_VERBS_BINDING_x_*`; SOC1-x, SOC2-x, MAT-x, MIL-x, PHY-x =
`14_VERBS_{SOCIAL1,SOCIAL2,MATERIAL,MILITARY,PHYSICAL}_x_*`; BYZ-x, COL-x, PAP-x, VEN-x, SYN-x =
`15_INSTITUTIONS_{BYZANTINE,COLONIAL,PAPACY,VENICE,SYNTHESIS}_x_*`; NARR-x = `20_NARRATIVE_x_*`;
PROC-x = `21_PROCEDURAL_x_*`; LAC-n = `19_LACUNA_*` (1 admission, 2 conclusion, 3 verdict ladder,
4 questioning); DET-x = `18_DETERMINISM_*` (A task draw, B notice, C rival acts, D no certain matchup);
FI-nn = `08_FI_nn_*`; STORY-x = `23_STORY_x_*`.

### 2.1 Life, death and lineage

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-01 | a natural death, with warning: an illness survived, a death in bed | GAME, CHAR, WR, HAPP, NARR | X | everyone is zero seasons old; illness and age ship at 0 and kill outright | M8 | HAPP-A; PES-WR-C; PROC-B (`age_bands`); the on-switch is Jordan's (ED-IN-0317) |
| S-02 | a death reported: the news travels, with a name or without | FI, GAME, HAPP, GO | X | a death is held only by those in the room; the second teller says "there was a telling" | M4 | FI-02; FI-06; PES-FI-A; PES-FI-C edit 3 |
| S-03 | he acted on a dead man's standing | FI | X | who exists and where is read from the world, not the ledger | M4, M11 | PES-FI-C edit 4; FI-01 |
| S-04 | a contested succession | GAME, FA, NARR, HAPP, CHAR | X | one claimant; the first valid claim wins; `succeed` never forms | M6, M8, M5 | VB-C; BYZ-E; HAPP-B; SYN-B |
| S-05 | a regency; an interregnum or a vacancy that costs someone | GAME, FA | X | a claim has no provisional form; an empty seat owes nothing | M6, M5, G2 | VB-C (`provisional_term`); HAPP-B (the consort's Partial); NARR-B; BYZ-B; the minor heir: STORY-B |
| S-06 | the line fails and the throne passes to a house | FA, HAPP | X | `successions` is one title deep: stranded for ever | M6 | HAPP-B edits 2 to 4 (Jordan's item 3 there) |
| S-07 | a marriage, a birth, a coming of age; a person enters the world | GAME, CORE | X | no verb and no clock: persons never increase | G2, M16, M8 | **GAP** → STORY-B (PROC-D's PG-7 carries only an arrival individuated from a cohort) |
| S-08 | revenge, for the dead or the wronged | GAME, PC, CHAR | X | the patient of a deed is not read; the hand that killed is not named | M4, M5, M10 | `02_CHAR_relations_have_a_ground` with PES-CHAR resolution 11; PES-PC-C; FI-06; HAPP-C; `03_PC_duel_chain_reach` |
| S-09 | a killing as a crime: a murder, an ambush, a man cut down unready | PC, HAPP, FI | X | violence has no doer-side context; the opener has no edge | M10, M11 | HAPP-C (`enmity`, the guard, notice by a draw); PHY-A A3 (`context_terms`); surprise decided in §8 R-12 |

### 2.2 Seats and power

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-10 | a seat conferred and resisted, stripped and withstood; a fall short of the ban | CHAR, FA, NARR, WR | N | `confer` 0 of 8, `revoke` 0 of 11; both fixed where admitted | M6 | VB-C; PES-FA-A |
| S-11 | a deposition: an officer tried and removed; a head unseated | FA | X | a bench cannot close a seat-hold; four heads have `revocation: null` | M6, M12, M16 | COL-C (`release` as a disposal); PAP-B; PAP-D; CR-37; §8 R-05 |
| S-12 | a reinstatement, a pardon, a return | FA, NARR, SC | N | `pardon` 0 of 15; a dismissal is for life | M6, M12 | PES-FA-A; VB-B; LAC-3 |
| S-13 | an election; a Church that chooses its own head | FA | X | no ballot, no electorate | M6, M16 | VEN-C; PAP-B; `13_SC_draw_for_unrolled_contests` |
| S-14 | a usurpation, a coup | GAME, FA | X | no act takes a held seat but the superior's | M6, M13 | VB-C; COL-D (`annex`); BYZ-E |
| S-15 | a decree obeyed or defied; an order carried out; a duty failed and answered | GAME, FA, NARR | N | `comply` 0 of 193: a writ has no addressee | M7, M5 | `06_FA_decree_binds`; VB-D; SOC1-B; NARR-B |
| S-16 | a defection; a vassal who breaks with a new lord; a faction split; a rising that names its leader | NARR, FA | X | nobody knows who holds what; a man is never asked about his own side | M5, M6 | NARR-C; NARR-D; BYZ-E |
| S-17 | an excommunication and each believer's answer | NARR | X | no verb, no kind | M16, M7 | PAP-D |
| S-18 | an alliance, a treaty, a peace with terms; a debt called in | FA, NARR | X | `covenant` 0 of 47; no instrument forms | M16 | COL-A; VEN-B; `13_SC_draw_for_unrolled_contests`; SOC1-A |
| S-19 | an ennoblement by deed; a faction founded and regarded | FA | X | no deed ledger | M16, M6 | BYZ-A; COL-D; SYN-B |

### 2.3 War

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-20 | a war: declared for a cause, between two parties, with an end | GAME, FA, NARR, HAPP | X | anyone declares for anyone; marches are unaimed | M13, M5 | `06_FA_war_lives_in_seats_B`; PES-FA-B edit 4; CR-91; NARR-C |
| S-21 | a field won; a place taken; a province lost | MB, FA, GAME | N | 0 `field.won` in any run; the attacker loses 60 of 60 at the shipped scale | M13 | `04_MB_headcount_grade_and_scale`; PHY-B; COL-D |
| S-22 | a siege that ends; a town starved out; a place that yields | GAME, MB, SE | X | `march_postures` is `[storm]`; `surrender` withheld; a larder cannot be cut off | M13, M9 | VB-E; `07_SE_campaign_supply_and_muster`; `04_MB_playable_field_scenario`; §8 R-07 |
| S-23 | a rout rallied; a pursuit; a rearguard | MB | X | rally is an empty hook; no unit is ever Fast | M13 | PES-MB (`rout_has_two_exits`) |
| S-24 | a battle decided for a reason someone can state | MB, DICE | X | the deciding draw is not returned; flank, pike and fatigue are inert | M13, M3 | `04_MB_manager_battle_one_resolver`; `04_MB_typed_outcome_and_one_path`; `04_MB_cell_hierarchy_as_data`; `04_MB_unit_loadout_and_weapon_in_hand_B`; Jordan's (PES-DICE §6) |
| S-25 | a named man falls in the field; a general is taken | MB, ARCS | N | reachable, never observed | M13, M10 | `04_MB_typed_outcome_and_one_path`; `03_PC_typed_outcome_one_door`; `04_MB_squad_grid_of_named_characters` |
| S-26 | an army eats a province bare | SE | X | the field ration reads one empty rung | M9, M13 | `07_SE_campaign_supply_and_muster`; PES-SE-B edit 4 |

### 2.4 Violence between persons

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-27 | a duel: heard, answered, fought, with more than one outcome | GAME, PC, HAPP, GO | N | `challenge` 0 of 393: the challenged never holds the challenge | M10 | `03_PC_duel_chain_reach`; PHY-A A4; SOC1-D; PES-PC-A |
| S-28 | a fight with a middle: he yields, quits, fights on, runs; a surrender refused | PC | X | the yield is one threshold for all; an NPC has no decider | M10 | PES-PC-A; `03_PC_duel_round_and_approach_B`; `03_PC_exits_withdrawal_recovery` |
| S-29 | the famous swordsman; a name made or ruined by a fight or a trial | PC, SC | X | a fight names no winner; a verdict names no party | M3, M5, G1 | PES-PC-C; PES-SC-C; STORY-A edit 3 |
| S-30 | an arrest that takes its man; a questioning; a confession; an execution | SC, HAPP, NARR | N | a capture kills (3 dead, 0 prisoners in 9 scenes); a confession writes nothing | M10, M12 | PHY-A A1 to A3; SOC2-C; LAC-4 |
| S-31 | a wound carried, and mended over time | CHAR, PC | N | `tend` restores a body whole, free and certain | M8 | MAT-A (`tend` drawn); `03_PC_exits_withdrawal_recovery` Part C |

### 2.5 Place, economy and the world

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-32 | a famine: the town thins, is relieved or is not, and recovers | GAME, SE, WR, NARR | H | stores hold 21 times need; rest cures hunger; nothing writes a population's weight | M9, M8 | `07_SE_ground_and_granaries`; `07_SE_treasury_granary_B`; PES-SE-A; `07_SE_population_census`; `07_SE_population_regrowth_B`; PES-GAME (`the_world_draws`) |
| S-33 | blame: the hungry, the unpaid, the unheard blame the one who owed it, and it costs him | SE, NARR, GAME, HAPP | X | an omission has no author | M5, M9 | NARR-B; NARR-C; `01_CORE_unmet_need_is_attended_first`; BYZ-B |
| S-34 | refugees arrive and strain the next town | SE | X | no cohort migration executes; an arrival changes a count | M9 | MIL-A; `02_CHAR_offer_what_can_be_done` (a population's aperture); PES-SE-A edit 1 |
| S-35 | a harvest remembered | SE, WR | X | the harvest is not an Event; there is no year | M8, M9, M3 | PES-SE-B edits 1, 2; `09_WR_B_weather_with_memory_and_the_year`; NARR-E edit 1 |
| S-36 | trade: a mining town buys its bread | GAME, SE | N | `exchange` 0 of 225: it names no kind the town has or lacks | M9 | MAT-B; PES-SE resolutions 5 and 9 |
| S-37 | a hoarder, a profiteer, a cornered market | SE, NARR | X | no price | M9, M5 | decided (§8 R-09): no price mechanism; told as relief withheld (S-33) and a debt called in (S-18) |
| S-38 | a founded place grows past its founder, or fails | GAME, SE, CORE | H | `found` 0 of 25; nothing founded can end | M17, M9, G3 | MAT-C (the founding, drawn); the ending: **GAP** → STORY-C; a new settlement on the map is Jordan's (PES-SE J-3) |
| S-39 | a place decays and is repaired; a granary burned; a road cut | WR, SE, GAME | X | `restore` never forms; `sabotage` reaches no store; no route | M17, M9 | MAT-A; PES-WR-A; PES-GAME (`the_world_draws`); §8 R-08 |
| S-40 | a journey that goes wrong | WR | X | travel is free, instant and certain | M17 | PES-WR-A; MIL-A |
| S-41 | a calamity that builds and breaks; an era that ends; an ending | WR, GAME, CORE, NARR, HAPP | X | no source, no break; no strand concludes; no ending row can be reached | M17 | PES-WR-B; `09_WR_strand_conclusion`; `09_WR_B_draws_not_thresholds`; `09_WR_world_motion` |
| S-42 | the Thread read to some purpose; a mending that costs and can fail | WR | X | the reading finds its own gate; a rise is certain and free | M17 | `09_WR_B_threadwork_session_and_practitioner`; PHY-D |

### 2.6 Law

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-43 | a verdict that changes a life, in proportion to the case | GAME, SC, NARR | N | 2 determinations in 12 seed-seasons; one obstacle term; the sentence serves the judge's seat | M12 | `05_SC_obstacle_difficulty_and_modifiers_B`; `05_SC_arrangement_rows_that_bind`; PES-SC-C; LAC-3 |
| S-44 | an acquittal | SC | X | `determine` at Failure is "undetermined" and is asked again | M12 | `05_SC_acquittal`; LAC-3 |
| S-45 | an appeal; a reversal | SC, WR | X | no route to a higher bench | M12 | LAC-3; `13_SC_draw_for_unrolled_contests` |
| S-46 | a perjury exposed; a document entered and answered | SC | X | `speak` writes nothing at any band; nothing held can contradict | M12, M11 | `05_SC_evidence_and_rebuttal_B`; `08_FI_05_evidence-interface_B`; SOC2-C; LAC-1 |
| S-47 | a false accuser pays | SC | X | an accuser loses nothing | M12, M5 | `05_SC_evidence_and_rebuttal_B` (the two faults); LAC-2 |
| S-48 | a judge recused, bought or challenged; a split bench | SC | X | a judge may sit on himself; there is no tally | M12, M16 | VB-B; PES-SC resolution 6; VEN-A; VEN-C; PAP-B |
| S-49 | a petition for relief; a remedy that goes to the wronged | SC | X | a petition dockets its own addressee; the disposal is owed to the bench | M12 | SOC2-B; PES-SC resolution 5; `05_SC_arrangement_rows_that_bind`; the disposal's object is Jordan's (PES-SC §5 item 3) |
| S-50 | a negotiation settled | SC | X | two unilateral acts | M12, M16 | `05_SC_negotiation_scene`; `13_SC_draw_for_unrolled_contests`; COL-A |
| S-51 | the wrong man accused, or convicted | FI, LACUNA | X | no conclusion can be stated | M11, M12 | LAC-2; `08_FI_03_playable-inquiry`; `08_FI_07_shortest-playable-case` |

### 2.7 Knowledge

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-52 | a rumour past one mouth, that moves or ruins someone | FI, GAME, NARR, GO | X | 0 chains over one hop in every arm | M4, M5 | FI-02; PES-FI-A; NARR-A |
| S-53 | a forgery believed, in play | FI | N | 0 of 376 forgeries left the forger's hand | M11, M4 | MAT-D; SOC1-B |
| S-54 | a forgery exposed; a liar caught | FI, SC | X | knowing a paper false changes nothing; being caught is a private number | M11, M4 | PES-FI-B; SOC1-C (`deceit.exposed`); PES-SC-E |
| S-55 | an unwitnessed crime found out | FI | X | a deed leaves no trace but the memory of those present | M11 | PES-FI-C; `08_FI_07_shortest-playable-case`; PHY-C; PROC-C |
| S-56 | deceived, and acting on it | CHAR, FI | N | 8 false beliefs from a teller in 21,312 claims | M4, M11 | FI-01; PES-SC-B; PES-SC-E |
| S-57 | a village that hides its grain | SC | X | a numeric lie is always upward | M4 | PES-SC-E |
| S-58 | a planted clue that misleads | FI | X | nothing can be planted; a finding is never false | M11 | decided out of this plan (§8 R-10) |

### 2.8 The interior

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-59 | persuasion: a man talked round, about a particular thing | CHAR, SC | N | `argue` 0 Success of 19; Partial and Failure move nobody | M14 | PES-SC-D; SOC1-C; `02_CHAR_which_ground_moves_whom` |
| S-60 | learning: a skill gained; an apprenticeship | GAME, CHAR | N | `train` 0 of 324; capability moved for nobody | M15 | MIL-B; `02_CHAR_capability_definitions` |
| S-61 | temptation: a scruple held, or overridden and seen | CHAR | X | the refusal axis is dormant and leaves no trace | M14 | PES-CHAR-C |
| S-62 | a tie formed: friendship, feud, patronage; an oath kept or broken | GAME, CHAR, NARR | X | `tie` has no opener; stance moved for 1 to 7 of 83 | M16, M5 | SOC2-D; FI-08; `02_CHAR_relations_have_a_ground` |
| S-63 | an ambition achieved or abandoned | CHAR | X | a `commit` has no closer (0 of 243 ended) | M14 | `12_ARCS_arcs_as_staged_goals` with PES-CHAR resolution 10 |
| S-64 | a crisis of faith held or lost, and seen | CHAR, NARR | X | fixed at world-gen, silent, the same six persons at every seed | M14 | PES-CHAR-A; NARR-E edit 3; Jordan's (ED-IN-0261) |
| S-65 | a man changed by his own judgement | CHAR | N | one move of 0.027 in six seed-seasons | M14, M12 | PES-SC-C; `12_ARCS_arcs_as_staged_goals` |

### 2.9 The scene, the dice and the seat

| id | story | named by | today | first missing link | needs | carried by |
|---|---|---|---|---|---|---|
| S-66 | an errand: he is not here, so I go and find him | CORE | X | absence refuses the act and nothing forms the journey | M17 | MIL-A (`whereabouts_named`); SOC1-A; PES-CORE (`a_refusal_is_remembered`) |
| S-67 | a scene whose second step hangs on its first; two people occupied with each other | CORE | X | one global fold order; a scene has one occupant | M18 | PES-CORE (`a_scene_runs_in_its_own_order`); Jordan's (PES-CORE §6) |
| S-68 | the disaster | DICE | X | the margin is discarded; on 11 of 11 contested rows Failure writes nothing (§9 E-1) | G1 | **GAP** → STORY-A edits 1, 2 |
| S-69 | the success that costs | DICE | X | no band carries a price | G1 | per row: MAT-C, MAT-A; the one rule: **GAP** → STORY-A edit 1 |
| S-70 | the contest with a loser | DICE | X | one roller; the other party gains, loses and records nothing | G1, M5 | **GAP** → STORY-A edit 3; `10_DICE_one_score_two_roles`; PES-SC-D |
| S-71 | the comeback remembered; a record of rolls that shows a character | DICE, CORE | X | a failed attempt leaves its maker nothing to remember | G1, M15 | **GAP** → STORY-A edit 4; PES-CORE (`a_refusal_is_remembered`) |
| S-72 | a retold magnitude; an inner change the record holds | CORE | X | 0 of 36,586 receipts carry a value; scar and crisis writes reach no Event | floor | PES-CORE (`the_record_holds_what_changed`) |
| S-73 | a story a seat can follow: the rumour with its speaker, the course of a fight, a search that found nothing, his own odds | GO | X | `Seen.why` is `None` by construction; the offer is unpinned | M19 | PES-GO (four files); `11_GO_player_surface_contract_B` |

### 2.10 What can and does happen today (the control set)

From the lanes' lists, merged: a record of what the granary held; a petition that lapses; a forgery
nobody examines; a cover nobody penetrates; an oath that matures by the clock; a march that finds an
empty field or is beaten off; a move of house; a stale store corrected by a refusal; a seat known empty;
an introduction; a silent, pre-set conversion; one cardinal (and at seed 2, in the fourth season, the
King) killed in a `capture`. These are the census's **positive controls**: an instrument that cannot see
them cannot be trusted on the seventy-three (§6.1 clause C0).

## 3. The shared missing mechanisms, ranked by stories unlocked

Counted from §2's *needs* column (`runs/STORY/p2_count.py`; a story needing two mechanisms counts under
both). "Unlocked" is a necessary condition, not a demonstration: the demonstration is the batch gate
(§6). The floor is listed first because nothing above it can be observed without it.

| rank | id | mechanism (one sentence) | stories | which | state today | carried by |
|---|---|---|---|---|---|---|
| floor | **M1** | the offer makes sense: an act is formed only on a thing it can be done to, by someone placed to do it, and a refusal is remembered | 73 | all | 1,585 of 7,940 acts are one of eighteen verbs refused at every attempt (GAME §3.3); 4 in 10 acts refused (HAPP H-03) | `02_CHAR_offer_what_can_be_done`; VB-A, SOC1-A, SOC2-A; PES-CORE (`a_refusal_is_remembered`); PES-FI-D; PES-CHAR-B; `01_CORE_unmet_need_is_attended_first` |
| floor | **M2** | the act is drawn and every band writes something | 73 | all | 7.8% to 10.8% of acts drawn (GAME §0); Failure writes nothing on 11 of 11 contested rows and Overwhelming equals Success on 9 (§9 E-1) | DET-A; `13_SC_draw_for_unrolled_contests`; `05_SC_obstacle_difficulty_and_modifiers_B`; PES-DICE (both); `10_DICE_one_score_two_roles`; the per-row bands in every `14_VERBS_*` file; **G1** |
| floor | **M3** | the record keeps the cause, the value and the margin | 73 | all | closing acts carry no cause; 0 of 36,586 receipts carry a value; the margin is dropped after one call | PES-GAME (`standing_occasions_carry_their_cause`); PES-CORE (`the_record_holds_what_changed`); `05_SC_contest_record_on_event`; `01_CORE_reason_trail_in_the_act_store`; `09_WR_B_chronicle_that_tells`; NARR-E edit 2; PES-PC-C |
| 1 | **M12** | a hearing that binds and ends: evidence enters by a draw, is answered, and one closing draw gives five results | 13 | S-11, 12, 30, 43 to 51, 65 | `speak` writes `[]` at every band; 2 verdicts in 12 seed-seasons; no acquittal | `05_SC_evidence_and_rebuttal_B`; `08_FI_05_evidence-interface_B`; LAC-1, LAC-3; `05_SC_acquittal`; `05_SC_arrangement_rows_that_bind`; VB-B; SOC2-C; `05_SC_playable_hearing_B`; `05_SC_negotiation_scene`; PES-SC-A, -C |
| 1 | **M5** | regard moves with deeds and with dues, and has a ground: a person knows who did it, who holds what, and what he was owed | 13 | S-04, 05, 08, 15, 16, 20, 29, 33, 37, 47, 52, 62, 70 | stance moved for 1 to 7 of 83 persons; 0 `held_by` claims; an omission has no author | `02_CHAR_relations_have_a_ground` (+ PES-CHAR resolution 11); `02_CHAR_scar_is_a_wound`; `02_CHAR_which_ground_moves_whom`; NARR-A to -D; PES-SC-C |
| 3 | **M6** | seats pass by a draw: an appointment resisted, a dismissal withstood or undone, a claim contested, a term that ends | 10 | S-04, 05, 06, 10 to 14, 16, 19 | no seat changed hands by an act in any lane's runs but one founded lordship at seed 3 | VB-C; BYZ-E; HAPP-B; `06_FA_seat_terms_and_turnover`; `06_FA_seat_terms_by_body_B`; PES-FA-A, -B, -C; `06_FA_remit_grant_by_row`; VEN-C; PAP-B; SYN-B |
| 3 | **M9** | places differ and stores bind: endowment, a granary that shares, a population that thins and returns, store moves that name a kind and are drawn | 10 | S-22, 26, 32 to 39 | 37 settlements are one settlement; stores 21 times need; `exchange` 0 of 225 | `07_SE_ground_and_granaries`; `07_SE_treasury_granary_B`; PES-SE-A, -B; `07_SE_population_census`; `07_SE_population_regrowth_B`; MAT-B; MIL-A; PROC-A |
| 5 | **M11** | a deed leaves a trail, a paper is about something, and an inquiry ends in a committed conclusion | 9 | S-03, 09, 46, 51, 53 to 56, 58 | an unwitnessed deed is unknowable for ever; `reconstruct` writes `[]` | PES-FI-B, -C; FI-01, -03, -07; MAT-D, MAT-E; PHY-C; LAC-2, LAC-4; PROC-C |
| 5 | **M16** | instruments and ties: a bond, a debt, a treaty, a sanction, each a typed thing with terms that a draw reads | 9 | S-07, 11, 13, 17, 18, 19, 48, 50, 62 | `covenant` 0 of 47; `tie` has no opener; no debt carrier | SYN-A; COL-A, COL-C; VEN-A, VEN-B; PAP-D; BYZ-B; SOC2-D; FI-08 |
| 7 | **M13** | a field that can be won and leaves something: a war with two parties, one scale, a drawn field, a rout with two exits, a seat that falls with the ground | 8 | S-14, 20 to 26 | 0 `field.won` in any run of the suite | `04_MB_headcount_grade_and_scale`; `06_FA_war_lives_in_seats_B`; PES-FA-B edit 4; PHY-B; VB-E; MIL-C, MIL-D; PES-MB; `04_MB_typed_outcome_and_one_path`; `04_MB_manager_battle_one_resolver`; `07_SE_campaign_supply_and_muster`; `06_FA_levy_through_the_seat_B`; COL-D; CR-91 |
| 7 | **M4** | news that travels with a name: what is passed on has content, a deed keeps its hand, notice is a draw | 8 | S-02, 03, 08, 52, 53, 54, 56, 57 | 0 chains over one hop; a death known to 16 of 82 and to 17 three seasons on | FI-02; FI-06; PES-FI-A; DET-B; PES-SC-B, -E; SOC2-B; CR-29 |
| 9 | **M10** | violence with a cause and a mercy: a context for every attack, a challenge that is heard, a yield and a mortal wound that are drawn | 6 | S-08, 09, 25, 27, 28, 30 | `challenge` 0 of 393; a felling is a death 200 of 200; `capture` kills its man | PHY-A; `03_PC_duel_chain_reach`; SOC1-D; PES-PC-A, -B, -D; DET-D; `03_PC_duel_round_and_approach_B`; HAPP-C; `03_PC_person_inputs_content` |
| 9 | **M17** | the world strains, breaks and ends, and what is built can fall: a road, a calamity, a strand, an ending, each by a draw | 6 | S-38 to 42, 66 | no ending in any run; `restore` attempted 0 times; travel certain | PES-WR-A, -B; `09_WR_strand_conclusion`; `09_WR_B_draws_not_thresholds`; `09_WR_world_motion`; MAT-A, MAT-C; `09_WR_B_threadwork_session_and_practitioner`; PHY-D; **G3** |
| 9 | **M8** | bodies and time: an age, a year, weather with memory, illness on the body ladder, hunger and wear drawn, healing that takes time | 6 | S-01, 04, 07, 31, 32, 35 | everyone is zero seasons old; every harvest and every town the same | HAPP-A; PES-WR-C; `09_WR_B_weather_with_memory_and_the_year`; NARR-E edit 1; PES-GAME (`the_world_draws`); MAT-A; `03_PC_exits_withdrawal_recovery`; PROC-B |
| 12 | **G1** | what a roll leaves: the shortfall scales the loss, the other party is named, the maker remembers his attempt | 5 | S-29, 68 to 71 | margin discarded; one roller; `finding.none` is deposited to nobody | **GAP → `23_STORY_A_what_a_roll_leaves`** |
| 12 | **M14** | the interior draws: a crisis tried, a scruple that can give way, an argument that moves someone, a want that can end | 5 | S-59, 61, 63, 64, 65 | 0 of 19 arguments succeeded; six fixed silent conversions | PES-CHAR-A, -B, -C; PES-SC-D; SOC1-C; NARR-E edit 3; `12_ARCS_arcs_as_staged_goals` |
| 14 | **G2** | a house continues: a marriage as an instrument, a birth by a draw, a majority | 2 | S-05, 07 | persons never increase | **GAP → `23_STORY_B_a_house_continues`** |
| 14 | **M15** | capability differs and grows | 2 | S-60, 71 | every cast pool is the default; `train` 0 of 324 | `02_CHAR_capability_definitions`; `10_DICE_capability_axiom_map`; MIL-B; `03_PC_person_inputs_content` |
| 14 | **M7** | an order is answered by a draw | 2 | S-15, 17 | `comply` 0 of 193 | `06_FA_decree_binds`; VB-D; SOC1-B |
| 17 | **G3** | a founded place can fail | 1 | S-38 | nothing founded can end | **GAP → `23_STORY_C_a_founded_place_can_fail`** |
| 17 | **M18** | a scene runs in its own order | 1 | S-67 | 120 of 525 steps in order (chance) | PES-CORE (`a_scene_runs_in_its_own_order`); Jordan's |
| 17 | **M19** | a seat can read it | 1 | S-73 | `Seen.why` is `None` | PES-GO (four); `11_GO_player_surface_contract_B` |

**Reading the ranking.** Direct counts understate four mechanisms that *supply* others: **M8** (no
natural death, so no vacancy for M6 to contest: the succession family has no supply, NARR §4.2);
**M4** (regard cannot move on a deed nobody hears of, so M5's thirteen wait on it); **M9** (no dearth, so
no blame, no refugees, no levy refused); **M10** (no killing, so no crime for M11 to trace or M12 to
try). The batch order in §6 follows supply, not count.

## 4. The mechanisms, each at its single owner

For each mechanism: where the fact lives (the one owner code reads, §0.05), the keys and interface, the
draw (what sets the odds, what the bands do), and the trail it leaves for a narrator. For a carried
mechanism the keys are the carrying proposal's own names, read at its head unless a line is cited; this
table is a map to those files and restates none of their edits. The three gaps are designed in full in
`23_STORY_A`, `_B`, `_C` and summarised in §4.2.

### 4.1 Carried mechanisms

| id | single owner(s) | keys and interface | the draw: odds from → graded outcomes | the trail |
|---|---|---|---|---|
| M1 | `decision/options.py::opening_set`; `verb_table.yaml` (`referent_class` per row); `decision/choose.py::score_terms` | one person-side decline read off the row; a declared aperture for a population; `refused_before(ledger, holder, kinds, subject)` and `admission_weight` behind `refusal_memory` (control 0.0); `whereabouts_named(w, p, persons)` splices the believed place of a sought person as a `Rung` referent | no draw of its own (eligibility, the brief's carve-out): it decides whether an act may be attempted, never how it falls | the Scene's question and its `grounds` (NARR-E edit 2) say what was offered and why |
| M2 | `loop/resolve.py` (the one fold); `rosters.yaml` (`graded_inquiries`, to be `graded_routes`); `modules/social_contest` (`roll`); the row's `difficulty` and `obstacle_terms` | every writing row declares its route; `Margin.terms: ((name, value), …)` sums to `ob` | pool: the actor's capability for the row (M15) plus named levels of leverage (effort, proofs, favour); obstacle: the task's difficulty plus the counterparty's score and the named modifiers (venue, tie, distance, contradiction, standing) → the four bands, each with a write | `Event.degree`; `Event.ending` carries pool, obstacle, net, settled margin and terms |
| M3 | `loop/resolve.py::_act_events`; `state/world.py::World.write`; `rosters.yaml: margin_endings` | an act on a standing occasion names the Event that opened it; `Receipt.delta` filled from what the gate read; interior writes emit their declared kind | none | the whole of it: this mechanism *is* the trail |
| M4 | `loop/witness.py`; `epistemic.py`; `rosters.yaml` (`reach`, CR-29) | what a person passes on, to whom, with the chain kept; a deed's `seen.who` pairing travels with it; quantities drift, existence does not, a deed can lose its hand | notice of a deed: the bystander's attention against the doer's concealment (DET-B); a telling: the teller's roll against the hearer's knowledge and regard → told exactly, told garbled, told without the name, untold | `told_by` chains; `news.*` kinds; the credited confidence in the hearer |
| M5 | `queries/person_q.py::regard`; the stance rows; the person's own ledger | `_bond` for every deed with a person as patient; `dues_unmet(p, x)`; `believed_holder(p, seat)` from a `held_by` claim; `opinion_of(w, p, own faction)`; `commensurate(hearer, teller)` | none of its own: a pull orders attention and enters `regard`; the acts it occasions are drawn by their own rows | recomputed at the tick by a pure person-side function, so a chronicle can print "because his oath had lapsed unpaid" with nothing stored (NARR §7.5) |
| M6 | `offices.yaml` (`conferral`, `revocation`, a term, `may_fill`); `rosters.yaml: successions`; `loop/effects_governance.py` | `provisional_term` (proposed 2 seasons); `_provisional_term(w, a) -> Term`; a set of claimants per title; kinds `succession.claimed`, `succession.contested`, `revocation.resisted` | pool: the claimant's (or appointer's) standing, by title, deed ledger and backers present; obstacle: the rival's or holder's standing, the audience, distance → Overwhelming seated and acclaimed · Success seated · Partial a termed, provisional hold that must be confirmed · Failure contested or resisted, the seat stays as it was | the claim Event with its terms; `tenure.opened` with a term; the losers hold a claim of the contest |
| M7 | `verb_table.yaml` rows `issue`, `dispatch`, `comply`, `evade / defy`; `loop/effects_governance.py` | a writ's terms reach its addressee as a held Record; the answer is the addressee's own act | pool: the issuer's seat and standing with the addressee; obstacle: the addressee's interest against, distance, a live obligation the other way → obeyed in full · obeyed · obeyed in part or late · defied (the issuer's occasion) | `order.*` kinds on the addressee; the defiance is a deed against the issuer |
| M8 | `loop/matter.py` (the bodies clock); `queries/world_q.py::body_hazard`; `data/fixtures.py`; a year roster | `Person.born = -age` from authored ages or `age_bands`; illness as a bout on the body ladder; `season_factor_draw` with memory; hunger and wear drawn per subject; `tend` drawn and partial | pool: the body's band and the place's plenty; obstacle: age, the season, want in the land, a wound carried → hale · a season of illness · a fall of a band · death only from the lowest band | `person.sickened`, `body.changed` and `person.died` each naming its cause (the larder, the bout, the blow) |
| M9 | `modules/settlements/` (`subsist.py`, `produce.py`); `loop/census.py`; `geography` and endowment rows; rows `transfer`, `exchange`, `requisition`, `migrate` | endowment by territory; the treasury is the granary; shares in proportion to want; `weight.changed` at CENSUS (thinning) and MATTER (regrowth); a store move names a place, a kind and a size | harvest: the ground and the hands against the year → four bands of yield; a store move: the mover's capability and the holder's consent against distance and the size asked → carried whole · carried · carried in part · lost or refused | `yield.taken` with an amount; `stores.changed` with a value; the dearth Observation at the first short rung |
| M10 | `rosters.yaml: violence_contexts`; `modules/combat/`; `loop/effects_combat.py` | contexts `war`, `crime` (the officer's side), `defence`, `duel`, and `enmity` (the doer's side, HAPP-C); `context_terms`; the yield and the mortal wound as draws | the exchange roll as built, on per-person inputs; yield: the wounded man's resolve against his wound and the terms; mortal wound: the blow against the body → walks away · yields · maimed · dies | the scene's shape as Observations; `fell_to` naming the standing party |
| M11 | `loop/witness.py` (trail rows); `state/carriers.py::Record` (`subject_matter`, `stages`); `decision/` (the goal `deed_doers`) | a trail at the place by deed kind; a paper's content is about its subject; `Proposition.support` binds a conclusion to cited claims | each look: the looker's skill against the trail's age and the doer's concealment → the hand · the deed without a hand · that something happened · nothing; the conclusion: `reconstruct`'s band sets what it may say | findings by band (`finding_terms`); the committed Proposition; later, `record` of the concluder in whoever holds the contradiction |
| M12 | `arrangements.yaml` (`disposes:` as a band map); `verb_table.yaml` rows `speak`, `determine`, `carry`, `open_case`, `pardon`; the case file's `stages` | `contradicts(a, b)`; stages `filed`, `excluded`, `struck`, `dismissed`, `voided`, `reversed`; faults `self_contradiction`, `discredited_source`; `appeal_basis` | admission: the citing speaker's roll; an answer: the answerer's roll with the held contradiction as leverage; the verdict: the standing items, the bench's regard and ties, the venue → conviction · the lesser sentence · acquittal · (no closing draw) mistrial · (on appeal) reversal | the case thread (LAC-3): who said what on what, what the bench held, what later contradicted it |
| M13 | `modules/mass_battle/`; row `march`; `rosters.yaml` (`march_postures`); the war as a fact about seats | one survivor share, one scale; `Field` as the referent class; the typed outcome with the day's fortune, who broke, who fell; rally and pursuit as two draws | pool: headcount, kind, ground, orders, the commander; obstacle: the same of the other side, with fortune as Jordan rules its form (PES-DICE §6) → field won and place entered · won at cost · drawn off · lost; then rally and pursuit | `field.*` with the typed outcome; `army.arrived`; the beaten army at a place |
| M14 | `queries/person_q.py` (crisis, scruple); `rosters.yaml` (`pursuit_axes.refusable`, pursuit signatures); `goals.yaml: goal_stages` | `conviction.moved` emitted; `Scene.forgone`; `scruple.overridden`; `argument.held`; a commitment closed when the holder's ledger reads it met | crisis: the creed's intensity against what was witnessed → firmer · holds · shaken · breaks; scruple: the axis's share against the prize → refuses · refuses and is seen to · gives way · gives way gladly; argument: the arguer's rhetoric and ground against the hearer's commitment → moved far · moved · held · the arguer moved | the interior Events, deposited to the person and to a drawn subset of those present |
| M15 | the capability definitions file (`02_CHAR_capability_definitions`, `10_DICE_capability_axiom_map`); row `train` | a capability defined once; `train` as a season's lesson | the pupil's aptitude and the teacher's skill against the level sought → two steps · one · half a step kept as practice · nothing | `capability.changed` with a value |
| M16 | `engine/season/instruments.yaml` (SYN-A, one registry); the `obligation` obstacle term; row `tie` | a closed set of forms (`homage`, `farm`, `tribute`, `debt`, treaty forms), each a Record with terms, `dues`, `kept`, `breaches`; `tie_gain` | forming one: `covenant`'s draw, both parties' interest and regard; while it stands it is a term in other draws; breaking it is the breaker's act and a deed against him | the instrument Record; `kept` as each party reads it |
| M17 | `loop/matter.py` (wear, the lattice); rows `restore`, `work`, `move`; `queries/world_q.py::endings_reached`; strands | the road as a route row; `travel.turned_back`; a calamity with a source, a strain and a drawn break; a strand that concludes on a conclusion | the road: the traveller's body and company against distance, season and war on the way → arrives fresh · arrives · arrives spent · turned back; the break: the strain against the mending done | `condition.band_crossed`, the break Event, the ending Event (WR's) |
| M18 | `loop/driver.py`, `loop/resolve.py` (fold order) | Jordan's choice of PES-CORE §6 | — | — |
| M19 | `epistemic.py::Seen.why`; `decision/sheet.py` | `why` is the id of a claim the witness himself holds | whether the witness connects two things he has seen is a draw | `Seen.why` |

### 4.2 The three gaps, in brief (full edits in the proposals)

**G1 · what a roll leaves (`23_STORY_A`).** Owner: `data/rosters.py` beside `DEGREE_STEP`; the fold.
(1) `SHORTFALL_STEP`, the mirror of `DEGREE_STEP` below the bar: a Failure's settled margin, already
kept on the Event by `05_SC_contest_record_on_event`, gives a step of 1, 2 or 3 (short by less than
one whole success; by one to less than three; by three or more, the mirror of *"3 or more is always
overwhelming"*), and a Failure write that has a magnitude is scaled by it exactly as a Success write is
scaled by `DEGREE_STEP`. No band is added and `degree_from_net` is not touched (the ladder is ruled);
"disaster" is a word the chronicle reads off the kept margin. (2) A row may declare `stake:`, what the
actor puts down, from a closed set; Partial pays one step of it while still achieving, which is the
success that costs, and Failure pays `SHORTFALL_STEP` steps. (3) A contested row's outcome kinds name the counterparty as their patient, so a
witness holds "X bested Y" and Y's regard for X moves by M5. (4) A person's failed attempts are read
from the act store and the log by the chronicle and the census (a harness read), so a later success can
be told as "at the third attempt". Nothing is deposited (the `undeposited_kinds` decision stands) and
nothing is weighed by the chooser: PES-DICE's F-PES-DICE-05 measured, with a control, that weighing a
failed search changes nothing, and a *refusal* is what PES-CORE's `admission_weight` already weighs.

**G2 · a house continues (`23_STORY_B`).** Owner: `instruments.yaml` (a `marriage` form), the bodies
clock at MATTER, CENSUS's individuation. A marriage is a covenant between two persons, drawn like any
other; a birth is a yearly draw for a co-resident couple (odds from their ages, bodies and the plenty of
the place; Overwhelming two children, Success one, Partial one and the mother sickens, Failure none, and
at the deepest shortfall a loss with a fall of her body); the child is a Person with an age and no
aperture until `majority_age`; a minor may hold a seat only provisionally, which is the regency VB-C's
Partial already is.

**G3 · a founded place can fail (`23_STORY_C`).** Owner: `loop/matter.py`'s wear pass and
`effects_founding.py`. A founded rung is a dwelling Site on drawn wear; tended, it stands; untended and
unpeopled, its Site falls by the same draws as any other, and when the last Site of a founded rung
stands at zero with nobody residing there MATTER closes the rung by `raze`'s own tail. Growth is the
other outcome and needs no new rule: a population that regrows and migrants who lodge.

## 5. Per-story chains

One row per story. *Must be seen* is the bar of §1 made particular. *Chain* is the minimal sequence from
a person's act (or the world's drawn motion) through draws to written, readable consequences, each link
marked `[R]`, `[N]` or `[A]` (§1) with the file that carries a missing link. *Draws* names what sets the
odds and what the bands do. *Fails and varies* says how the story can not happen and how it can happen
more than one way: a story with an empty last column would be a schedule and is not admitted.

### 5.1 Life, death and lineage

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-01 | an age; a season of visible illness others can act on; recovery or death; a cause on the death | an authored age `[A → HAPP-A edit 1, PROC-B]` → the bout at MATTER `[N: body_hazard exists, rates 0, and it kills outright → HAPP-A edits 2 to 5, PES-WR-C]` → `person.sickened` seen by the household `[A → same]` → another's `tend` `[N: certain and whole today → MAT-A]` → recovery or a further fall `[A]` → `person.died` citing the bout `[N: _die cites ROOT → HAPP-A, PES-SE-A edit 3]` → `tenure.closed` `[R]` | the body's band and the plenty of his town against age, the season, want in the land, a wound carried → hale · sickens · falls a band · dies only from the lowest band | most old men live the year; some recover; the death may fall in the middle of a suit, a war or a harvest, or before an heir is named |
| S-02 | someone absent learns of the death, from a named teller, late, and perhaps wrongly | `person.died` `[R]` → notice by those present `[R, fixed → DET-B]` → a telling that carries the deed and its hand `[A: the second teller passes "there was a telling" → FI-02, FI-06]` → a second hop `[A → FI-02]` → the hearer's claim with a chain and a credited confidence `[N]` → an act occasioned by it `[N: 0 of 19 tellings answered]` | each telling: the teller's roll against the hearer's knowledge and regard → exact · garbled quantity · the hand lost · untold | news may never arrive; may arrive without the killer's name (PES-FI-A); may arrive after the heir has acted |
| S-03 | a man petitions, challenges or obeys someone who is dead, and learns it | S-02's delay `[A]` → candidates formed on the asker's own `exists` cell and believed place `[A: the engine deletes the dead from his options → PES-FI-C edit 4, FI-01]` → the act refused "he is dead" `[N]` → the refusal teaches the cell `[R for stores, GAME §2.5]` | no draw of its own; it is S-02's delay made visible | happens only where news is slow (distance, PES-WR-A; a border, COL-B) |
| S-04 | a seat emptied for a cause; two or more claimants on different grounds; a contest; a loser who remains | a death `[S-01 or S-09]` → `tenure.closed` `[R]` → each eligible title forms `succeed` `[N: never formed, H-289; one title deep → HAPP-B edit 2]` → the claim drawn before an audience `[A: the first valid claim wins → VB-C, BYZ-E]` → a provisional or full hold `[A → VB-C `provisional_term`]` → the loser holds a claim of the contest and a new holder meets old oaths `[A → NARR-C]` | the claimant's title, deeds (SYN-B) and backers present against the rival's and the audience's regard → acclaimed · seated · provisional, to be confirmed · contested, seat still open | no rival may come forward; the heir may win outright; a provisional reign may be confirmed or lapse; a house may take it (S-06) |
| S-05 | an empty or half-held seat, and people who are worse off for it | a Partial claim or a minor heir `[A → VB-C; STORY-B edit 4]` → a termed hold by the consort or guardian `[A → HAPP-B edit 4]` → the seat's remit acts not done: writs unissued, a docket lapsing, stipends unpaid `[R as lapses: 23 by clock against 3 by act]` → those owed attribute the lapse `[A → NARR-B, BYZ-B]` → acts against the regent `[N]` → the term ends: confirmed, or the seat reopens `[A → VB-C]` | the regent's `succeed` again while the term runs (BYZ-E); each grievance's petition or challenge | the regency may be confirmed, may lapse, may be displaced by a rival; a vacancy nobody is owed anything under costs nobody, and that is correct |
| S-06 | the royal line gone and the throne not stranded | King and heir dead `[H: planted, GAME X2b]` → the further titles may claim `[A → HAPP-B edits 2 to 4]` → S-04's contest among them | as S-04, with the deed order as odds (SYN-B) | which house, or the consort, or the Princess; or a season with no King |
| S-07 | two houses joined; a child of a named couple; a youth who becomes able to hold | a `covenant` of form `marriage` `[A → STORY-B edit 1, on COL-A's registry]` → the couple co-reside `[R: reside edges]` → the yearly birth draw at MATTER `[A → STORY-B edit 2]` → a Person individuated at CENSUS with an age and kin claims in the parents' ledgers `[A → STORY-B edit 3, on PROC-B's generator]` → `majority_age` reached `[A → STORY-B edit 4]` → seats, verbs and claims open to him | the match: both parties' interest and their houses' regard (the `covenant` draw, `13_SC`); the birth: the couple's ages and bodies and the plenty of the place → two children · one · one and the mother sickens · none, and at the deepest shortfall a loss with a fall of her body | a match may be refused; a marriage may be childless; a child may die young (S-01's bout applies to every Person); an heir may come of age after the regency has already been lost |
| S-08 | a wrong with a named doer; someone who minds; an answer aimed at the doer, with a risk | a killing or injury with a hand `[N: the pairing is `seen.who` only; a slain attacker's killer is unnamed → PES-PC-C, FI-06]` → the news reaches kin or the sworn `[A → S-02]` → regard for the doer falls `[A: the patient is not read → `02_CHAR_relations_have_a_ground`, PES-CHAR resolution 11]` → an act against him: `challenge`, `petition`, `open_case`, or an attack under `enmity` `[N/A → `03_PC_duel_chain_reach`, HAPP-C, NARR-C G4]` | none of its own; the answering act's draw (the duel, the hearing, the attack) | the avenger may never learn the name; may prefer the court; may be refused the duel; may lose it |
| S-09 | a reason; an opening; a guard passed or not; a body; a doer who may be known or not | a recorded reason and hostility `[A → HAPP-C `enmity`; M5]` → the attempt formed `[A]` → the guard, a draw `[A → HAPP-C]` → the scene, with the opener's edge as a context term `[N: scene exists; no edge → PHY-A A3, §8 R-12]` → the mortal-wound draw `[A → PHY-A A3]` → notice by a draw `[A → DET-B]` → a trail at the place `[A → PES-FI-C]` | resolve to act: the scruple (PES-CHAR-C); the guard: the doer's stealth against the household; the scene; the wound; the notice | he may not dare; may be stopped at the door; may wound and flee; may be seen, or not; fewer than one attempt per seed-season by HAPP-C's own gate |

### 5.2 Seats and power

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-10 | someone raised or brought down by another's act, and able to resist | a vacancy or a displeasure `[R: vacancies exist; M5 for the displeasure]` → `confer` or `revoke` formed on a seat the actor may fill or strip `[N: refused at clause 1 → PES-FA-A, VB-A]` → the draw `[A → VB-C]` → a hold opened or closed, with the lesser forms at Partial `[A → VB-C]` | the appointer's standing against the candidate's rivals; the stripper's against the holder's own → done · done · provisional or unseated without the ban · resisted | the holder may withstand it; the fall may stop short of the ban |
| S-11 | an officer or a head removed by a process, not by his superior's word | a grievance or an audit due `[A → NARR-B, COL-C]` → a case docketed under an arrangement whose disposal closes a hold `[A → COL-C, `05_SC_arrangement_rows_that_bind`]` → the hearing (S-43) → the hold closed, or a sentence whose `avoidance` his sworn men each answer `[A → PAP-D]` | the hearing's draws; each sworn man's answer to the avoidance writ (S-15) | acquitted; sentenced and obeyed anyway; abandoned by some and not others. A crowned head falls only this way, by conquest (S-14) or by his own `release` (§8 R-05) |
| S-12 | a fall undone | a ban or a closed hold `[R]` → `pardon` formed only for the restrained `[N: 0 of 15 → VB-B]` → mercy by a draw `[A → VB-B]` → the ban lifted; a second `confer` `[A → PES-FA-A]`; or a reversal on appeal (S-45) | the pardoner's seat and regard for the man against the offence and those he wronged | refused; granted and resented by the wronged (M5) |
| S-13 | a body that chooses, with a count | a seat with an electorate `[A → PAP-B, VEN-C]` → candidacy `[A]` → each elector's ballot, his own drawn act `[A → `13_SC_draw_for_unrolled_contests`]` → the tally against `quorum_share` (bookkeeping) `[A]` → a hold | each elector: his regard, ties and obligations toward each candidate (VEN-A) → for · for · abstains · against | no quorum; a split; the favourite beaten by ties |
| S-14 | a held seat taken by one with no right to it but force or acclaim | a cause against the holder `[A → NARR-C G4]` → a march on his ground `[N → M13]` → the field won `[N: never → `04_MB_headcount_grade_and_scale`]` → the seat falls with the ground `[A → COL-D `annex`]`; or a claim before a crowd while he lives `[A → BYZ-E]` | the field; the acclamation (the crowd's regard for each) | beaten in the field; acclaimed by one town and refused by the next |
| S-15 | an order with content, a person it reaches, his answer, and what the issuer does about it | `issue` `[R: 40/23/47 writs]` → the writ reaches its addressee as a held Record `[A → `06_FA_decree_binds`, SOC1-B]` → `comply` or `evade / defy`, his choice then a draw `[N: 0 of 193 → VB-D]` → defiance is the issuer's occasion `[A → `06_FA_decree_binds`]` → enforcement or a grievance (S-33) | the issuer's seat and standing with him against his interest, distance and any obligation the other way → obeyed in full · obeyed · in part or late · defied | lost on the way (COL-B); obeyed badly; defied and unpunished |
| S-16 | a man who leaves his side, or a side that divides, for a reason he could state | a pull: his opinion of his own faction below indifference, or a new holder he despises `[A → NARR-D, NARR-C]` → the creed as a standing occasion `[A]` → `argue`, `release`, `commit` to another `[R rows; N in this aim]` → others hold the defection as a deed `[A → `strife_kinds`, Jordan's, NARR §10 item 2]` | `argue`'s roll; `release` and `commit` as drawn acts (VB-A, SOC1-D) → reconciled · stays and resents · leaves quietly · leaves and is seen to | most stay; a leader emerges only if others `commit` to his uttered cause |
| S-17 | a sentence that works through other people's choices | a Church bench's verdict `[A → PAP-D, PAP-A]` → publication `[A]` → each believer's answer to the `avoidance` `[A → PAP-D; S-15's draw]` → absolution on penance `[A]` | the verdict; each answer: the believer's conviction against his tie to the condemned | ignored by his own men; obeyed by rivals only; lifted |
| S-18 | terms two parties agreed, kept or broken, with a remedy | `covenant` on a form `[N: 0 of 47 → SOC1-A, COL-A]` → the draw `[A → `13_SC_draw_for_unrolled_contests`]` → the instrument Record with `dues` `[A → SYN-A]` → `kept` read by each party; a breach is a deed `[A → COL-A]` → a suit or a reckoning `[A → VEN-B]` | forming: both parties' interest and regard; each due: the debtor's stores and will | refused; kept; breached and forgiven; breached and sued |
| S-19 | rank that cites what someone did | a deed held by witnesses `[R]` → a keeper who records it `[A → SYN-B, BYZ-A]` → `confer` of a dignity citing it `[A → BYZ-A]` → standing that enters later draws `[A → COL-D]` | the conferral's draw (M6); what the keeper tells or withholds | unrecorded; recorded and disputed; honoured instead of paid (SYN's King's Bill) |

### 5.3 War

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-20 | a cause; a declarer with the right; an enemy who knows; fields; an end by treaty, death or exhaustion | a ground: an enemy with a place `[A → NARR-C G4, CR-91]` → a declaration by a seat that may declare `[N: anyone declares for anyone → PES-FA-B edit 4]` → the war lives in the seats that wage it `[A → `06_FA_war_lives_in_seats_B`]` → muster and march `[N → MIL-C, `06_FA_levy_through_the_seat_B`]` → fields (S-21) → peace as an instrument `[A → COL-A]` or the declarer's fall | the muster (who answers the levy, S-15); each field; the peace (`covenant`) | never declared; declared and never fought; ended by a successor who does not continue it |
| S-21 | a place that changes hands by arms, with losses on both sides | a march on a `Field` `[N: formed on anything → PHY-B]` → the field drawn at one scale `[N: 60 of 60 lost at the shipped scale → `04_MB_headcount_grade_and_scale`]` → `field.won`, the marchers enter `[N: never observed]` → the seat over the ground `[A → COL-D]` → the losers' grudge (M5) | headcount, kind, ground, orders and commander on each side, and fortune → won · won at cost · drawn off · lost | beaten off; a walk-in; won and then lost to hunger (S-26) |
| S-22 | a town shut in, its stores falling, and an end by yield, relief or storm | `march` with posture `besiege` `[A: `[storm]` only → `04_MB_playable_field_scenario`]` → the town's larder ladder cut from the rungs above `[A → §8 R-07, on `07_SE_campaign_supply_and_muster`]` → hunger by the season (S-32) → `surrender`, a draw `[N: withheld → VB-E]` or a relieving march | the holder's will to yield: his stores, his men's bodies and his hope of relief against his oath → opens the gates on terms · yields · holds another season · holds and sallies | relieved; starved out; the besieger starves first (S-26) |
| S-23 | a beaten army that is saved, or destroyed, by what was done after it broke | a rout `[R in the module]` → the commander's rally, a draw `[A: empty hook → PES-MB]` → else the winner's pursuit, a draw per mounted body, recallable `[A → PES-MB]` → the beaten army somewhere, weaker `[A → `04_MB_typed_outcome_and_one_path`]` | rally: the commander's presence against the rout's depth; pursuit: the pursuers' speed and order against a rearguard | rallied; run down; let go because the horse were spent |
| S-24 | a result with a stated reason: the flank, the reserve, the pike, the night march | orders set before and at windows `[A → `04_MB_manager_battle_one_resolver`]` → kinds and loadouts that matter `[N: the pike is inert → `04_MB_unit_loadout_and_weapon_in_hand_B`, `04_MB_cell_hierarchy_as_data`]` → the report: fortune, who broke first, why `[A → `04_MB_typed_outcome_and_one_path`]` | as S-21; the form of fortune is Jordan's (PES-DICE §6) | the reason may be luck, and the report says so |
| S-25 | a named person's fate inside a battle | a named man in a body that is struck `[N]` → the mortal-wound draw or capture `[A → PHY-A A3]` → `person.died` or a `detain` edge with the field among its causes `[N]` → his seat (S-04), his army's next acts | his body's share of the day's losses; the wound draw | unhurt; wounded (S-31); taken and ransomed (S-18); killed |
| S-26 | an army that takes its bread from the land it stands on, and what that does to the land | the standing ration charged each season in the field `[N: reads one empty rung → `07_SE_campaign_supply_and_muster`, PES-SE-B edit 4]` → `requisition` on the towns it stands in, drawn `[N → MAT-B]` → their dearth (S-32), their blame (S-33) | the requisition: the commander's force and warrant against the town's will and what it has hidden (S-57) | the army disbands unfed; the town hides its grain; the province empties |

### 5.4 Violence between persons

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-27 | a dispute; a challenge that reaches its man; his answer; a fight on terms; an outcome that is not always a death | a recorded wrong `[A: nobody holds one → M5; SOC1-D]` → `challenge` on a person with a dispute `[N: 0 of 393 → `03_PC_duel_chain_reach`]` → the challenged holds the Record `[A → same]` → `accept`, decline or ignore `[N → PHY-A A4]` → the scene on terms `[R as a module]` → the yield, a draw `[A → PES-PC-A]` → the scene's shape kept `[A → PES-PC-C]` | acceptance: his honour and regard against his fear (`02_CHAR_what_an_act_risks`); the exchanges; the yield: resolve against the wound | declined and shamed; first blood and peace; a death nobody meant |
| S-28 | a fight whose middle matters: a man who gives up, runs or will not stop | the scene `[R]` → an approach per phase chosen by each party's chooser `[A → `03_PC_duel_round_and_approach_B`]` → the yield draw each turn `[A → PES-PC-A]` → withdrawal at a price `[N: free → `03_PC_exits_withdrawal_recovery`]` → the victor's acceptance or refusal of a surrender, his act `[A → PES-PC-A]` | per phase: the approach chosen against the other's; the yield; the pursuit of a man who runs | every ending in the module's list becomes reachable from the season |
| S-29 | a name others carry: he who won, how, and against whom | an outcome that names both parties `[A → PES-PC-C, PES-SC-C, STORY-A edit 3]` → witnesses' claims `[R]` → tellings (S-52) → regard and, in later contests, the `notoriety` term `[A → SOC1-C]` | none of its own; it is the residue of other draws | a fight in private makes no name; a name may be for losing |
| S-30 | a lawful seizure that usually takes its man; a questioning he can resist; a sentence carried out | a warrant or a war `[A → PHY-A A1, A2]` → `arrest` or `capture`, custody at Success, resistance at Failure `[N: fought to the death → PHY-A A3]` → `interrogate`, the questioned man's own draw `[N: writes nothing → SOC2-C, LAC-4]` → a confession on file `[A → SOC2-C]` → the hearing (S-43); an execution only as a disposal an arrangement names `[A → `05_SC_arrangement_rows_that_bind`]` | the seizure: the officers against the man and his household; the questioning: approach and pressure against his resolve | escapes; resists and is hurt; says nothing; confesses falsely (S-51) |
| S-31 | a wound that lasts and limits, and care that may not work | a body fall `[R]` → the ceiling mark `[R]` → `tend` by another, drawn and partial, refused on a hungry body with a short larder `[N → MAT-A, PES-SE-A edit 4]` → recovery over seasons `[A → `03_PC_exits_withdrawal_recovery` Part C]` | the healer's skill and the patient's body against the wound's depth | heals; heals short; festers into S-01's bout |

### 5.5 Place, economy and the world

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-32 | a cause (a bad year, a levy, a cut road); a town short; relief sent or not; a toll; a recovery | a harvest drawn low `[N: `season_factor_draw` ships `()` → `09_WR_B_weather_with_memory_and_the_year`]` on ground that differs `[A → `07_SE_ground_and_granaries`]` → a larder short, the granary sharing by want `[N: id order → PES-SE-A edit 1]` → the dearth reported to its holder `[N: 0 Observations → PES-SE-A edit 2]` → the holder attends to it first `[A → `01_CORE_unmet_need_is_attended_first`]` → `transfer` of a real amount, drawn `[N: 1 grain → MAT-B, `07_SE_kernel_repairs`]` → hunger falls bodies by a draw per cohort `[N: in step → PES-GAME `the_world_draws`]` → the cohort thins `[A → `07_SE_population_census`]` and later regrows `[A → `07_SE_population_regrowth_B`]` | the harvest; each cohort's hunger draw (its body and stores against the shortfall); the relief's draw | no bad year; relieved in time; one town breaks first; a town emptied |
| S-33 | a person who was owed, a person who owed it, and a cost to the second | a due unmet: an unpaid term, an unheard petition, a dearth under a full granary `[R as lapses and shortfalls]` → the wronged attributes it to the believed holder `[A → NARR-B, NARR-C]` → regard falls `[A]` → `petition`, `speak`, `tell`, `challenge`, `release` `[R rows]` → the holder's standing, sworn men or seat at stake (S-11, S-16) | none of its own; each answering act's draw | he blames no one (he does not know who holds); he blames the wrong man (a stale `held_by`); the lord pays in time |
| S-34 | people on the move for a reason, and a host that feels them | a cohort short at MATTER `[H]` → `migrate` formed on a place it has heard is fed `[N: 0 executed → MIL-A, `02_CHAR_offer_what_can_be_done`]` → the road (S-40) → lodged, not housed `[A → MIL-A]` → it draws on the host's larder by want `[A → PES-SE-A edit 1]` → the host's own dearth and blame (S-32, S-33) | the journey; the host's reception (a `petition` to its holder) | they stay and thin; they are turned back; the host has plenty |
| S-35 | a year people refer to afterwards | a year exists `[A → NARR-E edit 1]` → the harvest is an Event with an amount `[A → PES-SE-B edits 1, 2]` → witnesses hold it `[R: WITNESS]` → later acts and the chronicle cite it `[A → `09_WR_B_chronicle_that_tells`]`; weather with memory makes a second bad year likelier `[A → `09_WR_B_weather_with_memory_and_the_year`]` | the weather draw | forgotten as claims decay; remembered wrongly at second hand |
| S-36 | a town that has one thing and lacks another, and a bargain | endowment `[A → `07_SE_ground_and_granaries`]` → `exchange` formed on the kind held in surplus and the kind short `[N: fixture kinds → PES-SE resolution 9, MAT-B]` → the bargain drawn, with a size `[A → MAT-B]` → stores move both ways `[R as an effect]` | each side's need and regard, distance, the size asked → a good bargain · a bargain · a poor one · none | no partner in reach; a poor bargain resented; a road cut (S-39) |
| S-37 | someone holding what others need and not releasing it | S-32's dearth beside a full store `[H: `harness/scarce.py`]` → the holder's choice not to `transfer` (the chooser, with his pursuits) `[R]` → S-33's blame; or a `debt` advanced on terms `[A → VEN-B]` | none of its own | he relieves; he lends; he is petitioned, sued or attacked |
| S-38 | a place begun by someone, that thrives or is abandoned, for reasons | a works its master holds `[R: two authored]` → `found`, drawn `[N: 0 of 25 → MAT-C]` → a hearth with a Site on drawn wear `[N → PES-GAME `the_world_draws`]` → people come: regrowth and lodgers `[A → `07_SE_population_regrowth_B`, MIL-A]` or nobody does → mending by a draw `[N → MAT-A]` or decay → the rung closed when its last Site stands at zero with nobody residing `[A → **STORY-C**]` | the founding (it can cost more than the price, or fail and lose part); each season's wear; each mending | never founded; founded and peopled; founded and dead with its founder |
| S-39 | a thing that wears, someone who minds, a repair that may not take; or a deliberate ruin | wear by a draw per Site `[N: uniform → PES-GAME]` → a band crossing seen `[R]` → the holder asked about his Site `[A: no question carries a Site → MAT-A]` → `restore` or `work`, drawn `[N: never formed]`; ruin: `sabotage` on a Site or a store, drawn, with a trail `[N: 900 to 0, no store → MAT-A, §8 R-08, PES-FI-C]` | the mender's skill and stores against the damage; the saboteur's stealth against the watch | neglected; mended short; burned and the burner seen |
| S-40 | a traveller who arrives late, hurt or not at all | `move` to a real elsewhere `[N: 20 of 37 to where he stands → `07_SE_kernel_repairs`]` → the road priced by distance `[A → PES-WR-A]` → the road's draw `[A → PES-WR-A, MIL-A]` → arrival, a spent body, or `travel.turned_back` | his body and company against distance, the season and war on the way → fresh · arrives · spent · turned back | most journeys are uneventful; the one that is not delays a claim, a relief or a warning |
| S-41 | something that gathers, can be seen coming, breaks at a moment, and leaves a before and after | a source `[A → `09_WR_world_motion` edit 1]` → strain spreading `[N: weight 0]` → crossings seen `[R when planted]` → mending as a bound (S-39) → the break, a draw `[A → PES-WR-B]` → an ending Event that a strand's conclusion or the roster names `[A → `09_WR_strand_conclusion`, `09_WR_B_draws_not_thresholds`]` | the break: the strain against the mending done; the ending: by persons' closing acts, never a count | bounded by mending; breaks early; ends in a peace instead |
| S-42 | a reading that tells something true and costs the reader; a mending that can fail | `thread_read` aimed at a place `[N: aimed at Records → PHY-D]` → a graded diagnosis `[A → PHY-D]` → the reader's cost `[A → `09_WR_B_threadwork_session_and_practitioner`]` → a working that mends, drawn `[A → same]` | the practitioner's sensitivity and state against the strain | reads nothing; reads and is harmed; mends short |

### 5.6 Law

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-43 | a charge; a case made of things held; a bench moved by them; a sentence that fits and binds | `open_case` with a charge or `petition` and `carry` to the right bench `[N: the addressee is docketed as the accused → SOC2-B, SOC2-C, PES-SC resolutions 5, 6]` → `speak` citing held items, admitted by its own band `[N: writes `[]` → `05_SC_evidence_and_rebuttal_B`, LAC-1]` → `determine` with named terms `[N: one term → `05_SC_obstacle_difficulty_and_modifiers_B`]` → a disposal by band `[A → `05_SC_arrangement_rows_that_bind`]` → the verdict witnessed as done to a named party `[A → PES-SC-C]` | the standing items for and against, the bench's regard and ties (VEN-A), the venue → conviction · the lesser sentence · (Failure) acquittal | lapses; acquits; convicts on a thin case |
| S-44 | a bench that says no, and a matter that stays ended | as S-43 to `determine` at Failure `[N: "undetermined", asked again]` → `matter.dismissed` and a `dismissed` stage `[A → `05_SC_acquittal`, LAC-3]` → no re-opening without a new item `[A → PES-SC resolution 4]` | S-43's closing draw | reopened on new evidence (S-45's sibling) |
| S-45 | a loser who goes higher, and a first bench that is corrected | a disposal `[R]` → a petition whose terms name it, carried to a bench at a higher rung `[A → LAC-3, `appeal_basis`]` → `determine` there `[R as a row]` → the disposal closed and a `reversed` stage `[A → LAC-3]` → the first bench heard with less weight after `[A → PES-SC-C]` | the appeal's own closing draw, with what is new | refused a hearing; upheld; reversed |
| S-46 | a statement on file, a held thing that contradicts it, and a cost to whoever made the statement | testimony filed `[A → SOC2-C]` → an answering `speak` citing a contradicting item `[A → `05_SC_evidence_and_rebuttal_B` rule 2, `contradicts(a, b)`]` → the answer's draw: the item struck or standing `[A]` → the fault on the citer (`self_contradiction`) or its source (`discredited_source`) `[A]` → every judge's regard for him `[A → PES-SC-C]` | the answerer's roll with the contradiction as leverage (PES-SC-A) | the lie stands unanswered; the answer fails its draw; a true statement is struck |
| S-47 | an accuser worse off for a charge that failed | S-44 or S-46 → the accuser's `record` in those who hold the contradiction `[A → LAC-2]` → a counter-suit as an ordinary `petition` `[R row]` | none of its own | the charge was honest and costs little; the accused does not pursue it |
| S-48 | a bench that is not neutral, and someone who says so | a judge with a tie or a gift to a party `[A → VEN-A `obligation`, SOC2-D]` → the term in `determine`'s obstacle `[A]` → a judge may not sit on himself `[A → PES-SC resolution 6, VB-B]` → a tally where several sit `[A → VEN-C, PAP-B]` | the closing draw, visibly moved by the tie (the term is on the Event) | the tie is unknown; known and unanswered; the verdict reversed for it (S-45) |
| S-49 | a wrong put right for the person wronged | a petition for a thing (a store, a seat, a pardon for another) `[A: every petition is for a binding → SOC2-B]` → an arrangement whose disposal goes to the petitioner `[A → `05_SC_arrangement_rows_that_bind`; the object is Jordan's, PES-SC §5 item 3]` | S-43's draws | granted in part; granted and not carried out (S-15) |
| S-50 | two parties who each give something | a sitting under a mutual disposal `[A → `05_SC_negotiation_scene`]` → exchanges, each drawn `[A → `13_SC_draw_for_unrolled_contests`]` → consent is each party's own act `[A]` → an instrument (S-18) | each offer: the offerer's leverage against the other's need | no agreement; a lopsided one |
| S-51 | an investigator who names the wrong person, a bench that agrees, and the truth arriving later | findings that point two ways `[A → S-55's trail]` → a committed conclusion with its support `[A → LAC-2]` → the hearing (S-43) → a later finding that contradicts it `[A]` → `record` of the concluder; an appeal (S-45) | `reconstruct`'s band (what the conclusion may say); the choice among suspects is the chooser's | he names nobody; names rightly; is never contradicted |

### 5.7 Knowledge

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-52 | a thing said that outruns its first hearer, changes, and makes someone act | a telling with content `[N: 9 of 11 landed tellings told the hearer what he held]` → the hearer passes on the content, not the telling `[A → FI-02 with PES-FI-A edit 5]` → drift by kind `[N: numbers only → PES-FI-A]` → credit by where teller and hearer stand `[N: one sign → NARR-A]` → an act on the told claim `[N: 16 non-information answers in three seasons]` → the subject's standing (M5) | each telling's draw; the credit sets how firmly it is held | dies at the first mouth; arrives true; arrives ruinous and false |
| S-53 | a false paper in someone else's hands, acted on | `forge` `[R: 52 a run]` → the paper is about a subject `[A → PES-FI-B, MAT-D]` → `give` or an `issue` that cites it `[N: 0 of 376 leave the forger → SOC1-B]` → the holder reads it as true and acts `[R on a hand-built handover]` | the forging: the forger's skill against the form (MAT-D); the reader's look against its quality | never used; doubted at sight; believed for years |
| S-54 | the moment a falsehood is known for one, by someone, and what the teller loses | a look that finds the forging `[N: 15% and then locked out → CP-T06-03]` → the finder no longer reads the content as true `[A → PES-FI-B]` → he tells or cites it (S-46) → `deceit.exposed` held against the forger or liar `[A → SOC1-C]`; for a spoken lie, a hearer who knows hears it for a lie by a draw `[A → PES-SC-E]` | the look; the hearer's knowledge as opposition | never examined; found and kept quiet (a hold over the forger) |
| S-55 | a deed nobody saw, a trail, a looker, a name | a deed in private `[R]` → a trail at the place by deed kind `[A → PES-FI-C edits 1 to 3]` → `examine` or `surveil` there, graded `[N: nothing to find → PHY-C]` → findings by band `[A → FI-03]` → a conclusion (S-51) | the looker's skill against the trail's age and the doer's concealment → the hand · the deed · that something happened · nothing | never looked for; the trail gone cold; the wrong name |
| S-56 | a man who believes something false because he was told it, and does something he would not have | a `lie` that lands `[N: 4 in four seasons]` → one belief every reader of his ledger uses `[A → PES-SC-B]` → candidates formed on it `[A → FI-01]` → the act, and the world's answer | the lie's draw against what the hearer knows (SOC1-C) | disbelieved; believed and harmless; believed and costly |
| S-57 | a population that under-reports to a taker | a levy or requisition expected `[A → S-26]` → a downward numeric `lie` `[A → PES-SC-E]` → the taker's belief; a later count that contradicts it (S-54) | the lie's draw | believed; found out and punished |
| S-58 | a false clue | — | — | decided out of this plan (§8 R-10): no shipped game solves it, K-37 refuses a false finding, and PES-FI's survivor S-PES-FI-1 (a garbled deed naming the wrong person) is its nearest form and is Jordan's there |

### 5.8 The interior

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-59 | an argument about a thing, a hearer who resists, and one of the two changed | a Proposition reaches an arguer `[N: formed on nobody after CP-T05-04]` → `argue` on a ground that suits the hearer `[A → `02_CHAR_which_ground_moves_whom`]` → the draw `[R]` → Success moves the hearer, Partial is held, Failure moves the arguer `[A → PES-SC-D]` → `pursuit.moved` seen `[R kind]` | the arguer's rhetoric and ground against the hearer's commitment (SOC1-C) | nobody moves; the arguer is the one talked round |
| S-60 | a pupil, a teacher, a season, a skill that did or did not take | `train` formed on a capability and a teacher `[N: on persons as Sites → MIL-B]` → the lesson's draw `[A → MIL-B]` → `capability.changed` `[A]` → later rolls differ (S-71) | aptitude and the teacher's skill against the level sought | nothing learned; a step; a teacher who will not |
| S-61 | a man who will not, at a cost; or who does, and is seen to | a candidate on a refusable axis `[A → PES-CHAR-C `pursuit_axes.refusable`]` → the scruple's draw `[A]` → `Scene.forgone` or `scruple.overridden` `[A]` → witnesses and his own scar (`02_CHAR_scar_is_a_wound`) | the axis's share of his vector against the prize → refuses · refuses and is seen to · gives way · gives way gladly | never tempted; holds every time (and is known for it) |
| S-62 | two people bound, by choice, with something that later tests it | a deed between them or an authored relation `[A → `02_CHAR_relations_have_a_ground`]` → `tie`, a draw `[A → SOC2-D, after FI-08's two conditions]` → the bond read by tellings and by obstacle terms (VEN-A) → a test: an oath due, a rival's offer (S-33, S-16) | the bond's draw: mutual regard and what each has seen of the other | refused; taken and kept; taken and broken (a deed) |
| S-63 | a want with stages, met or given up | a goal with `goal_stages` armed by what he learns `[A → `12_ARCS_arcs_as_staged_goals`]` → acts toward it `[R]` → the commitment closed when his own ledger reads it met `[A → PES-CHAR resolution 10]`; or `release` of it `[R row]` | each stage's own act | never armed; met; abandoned after a refusal remembered (S-71) |
| S-64 | a believer tried by what he saw, who holds or breaks, with others knowing | witnessed violations `[R: the scar]` → the crisis as a draw `[A: fixed and silent → PES-CHAR-A, NARR-E edit 3; Jordan's]` → `conviction.moved` to the person and a drawn subset of those present `[A]` → regard, credit (NARR-A) and his standing in his Church (PAP-B) | the creed's intensity against what was witnessed → firmer · holds · shaken · breaks | holds through a scandal; breaks alone; breaks in public |
| S-65 | a judge who is not the same man after the judgement | `determine` graded `[R: once]` → `consequence_pursuits` moves him by band `[R: 0.027]` → the verdict held as *his* deed by others `[A → PES-SC-C]` → their regard returns to him | S-43's draw | unmoved; hardened; haunted (a scar, if the sentence violated his creed) |

### 5.9 The scene, the dice and the seat

| id | must be seen | minimal chain | draws: odds from → bands | fails and varies |
|---|---|---|---|---|
| S-66 | a person who wanted to do something to someone absent, went, and did it or did not | an act refused for absence, the refusal remembered `[A → PES-CORE `a_refusal_is_remembered`]` → the believed place of the sought person spliced as a referent `[A → MIL-A `whereabouts_named`]` → `move` there, the road's draw (S-40) → the act formed again where he now stands `[A → SOC1-A]` | the road; then the act's own | he has moved on (a stale `at` claim); the road turns him back; he arrives and is refused |
| S-67 | a second step that depended on how the first fell | a scene folded in the chooser's order `[A → PES-CORE `a_scene_runs_in_its_own_order`; Jordan's]` → the second step's eligibility reads the first step's band `[A]` | each step's own | under option A of that file this story is told across rounds instead, and S-66 is its form |
| S-68 | a failure that was worse than a failure, for a reason on the record | a drawn act with a `stake:` `[A → STORY-A edit 2]` → the settled margin kept `[A → `05_SC_contest_record_on_event`]` → the Failure write scaled by `SHORTFALL_STEP` `[A → STORY-A edit 1]` → the chronicle's word from the margin `[A → STORY-A edit 5]` | whatever the row's draw is; the margin is the same draw read further | a miss by a hair costs one step; most failures are plain; the disaster is rare where the task is fair |
| S-69 | something achieved, and paid for | a row with a `stake:` at Partial: the write and one step of the stake `[A → STORY-A edit 2; per row MAT-C, MAT-A]` | the row's draw | clean success; success at a price; the price refused by choosing not to press (effort) |
| S-70 | two parties, one of whom came off worse, and both know it | a contested row `[R: eleven]` → the outcome kinds name the counterparty as patient `[A → STORY-A edit 3]` → both and the witnesses hold it as a paired deed `[A → FI-06's pairing]` → the loser's regard for the winner moves (M5) | the row's draw, with the counterparty's score as the obstacle (`10_DICE_one_score_two_roles`) | a draw that is held (Partial) has no loser; a private contest has no audience |
| S-71 | a person who failed, tried again and succeeded, and a record that shows what he is good at | a failed attempt that witnesses hold `[R for the non-inquiry rows; a failed search is seen by nobody, by decision]` → he tries again (a slot spent each time) `[R: 49 of 151 failed aims retried]` → a later Success on the same aim `[N: 20 Successes in 284 rolls]` → the attempts counted from the act store and told as "at the third attempt" `[A → STORY-A edits 4, 5]`; capability that differs (M15) makes the record a character | the row's draw each time | he gives up; he succeeds at once; he never does |
| S-72 | "how much", and "what changed in him" | receipts carry the value the gate read `[A → PES-CORE `the_record_holds_what_changed` edit 1]` → interior writes emit their declared kind `[A → edit 2]` | none | — (a record, not a story; it is what lets every other row be retold) |
| S-73 | a player on one seat following one thread from its opening to its end | `Seen.why` filled by a draw `[A → PES-GO `a_witness_may_connect_what_he_holds`]` → the offer names what the seat holds `[A → PES-GO `the_offer_names_what_is_held`]` → the surface pinned `[A → PES-GO `surface_pins`]` → the census run from a seat's ledger `[A → STORY-D edit 4]` | the connection is a draw | he sees one end only; he connects wrongly (which is a story) |

## 6. The enablement plan

### 6.1 The gate every batch uses

One instrument (`23_STORY_D_story_census_and_gate.md`: a `--stories` block on `harness/storybar.py`, the
owner of "does the engine produce stories"; it composes on `09_WR_story_instruments_that_can_fail.md`'s
arms and `edge_null`, on `20_NARRATIVE_F_story_inventory_and_gate.md`'s crossings block and on
`16_PESSIMIST_GAME_consequence_reading.md`). A story is named by its **shape**: an opening, a turn, a
close and a cost, each a set of Event kinds with role constraints, linked through `causes[]` ancestry,
with a **variant** key read off the close (its kind, its band, who it fell on). The census mints no
carrier, field, kind or register row (ED-IN-0225 stands): it is a pure read of the log, the act store and
the Tenures, and it grades nothing. The closing session reads seven clauses off what it prints:

| clause | reads | fails when |
|---|---|---|
| **C0** the instrument sees | the control set of §2.10 on the shipped engine | a story that does occur today reads 0 (the census is blind) |
| **C1** it occurs | story *s*, from no planted state, over *n* seeds | *s* occurs at fewer than 2 seeds |
| **C2** it can fail to occur | the same | *s* occurs at every seed with the same count (a schedule); a common story passes on a spread of counts, a rare one on being absent at 2 seeds or more |
| **C3** more than one way | variants of *s* across seeds | one variant holds every occurrence |
| **C4** the mechanism causes it | the control arm: the batch's fixtures at control | *s* occurs in the control arm at the on arm's rate, within the on arm's seed spread |
| **C5** not written into the build | one built world, four draw seeds (`--draw-seeds`) | the occurrence-and-variant vector is equal at all four |
| **C6** the draws carry it | every roll pinned to Success (the planted failure of SYN-D's gate); and `edge_null` | the variants survive pinning, or the shape reads as often on the edge null as on the log |

Sizes, proposed `[ASSUMPTION; Jordan to correct]`: the valley scenario (§7) at *n* = 20 seeds and 8
seasons; the realm at *n* = 5 and 6 seasons, the size `20_NARRATIVE_F` already uses (a realm season is
the expensive thing). Eight seasons needs `01_CORE_claim_fade_as_read.md` (ARCS M-SPAN); until it lands
the valley gate is read at 6. Every count is printed with its seeds; none is a balance claim (§0.1 pt 4:
the control is C4, and three seeds are three trajectories).

**The story bar that can fail, per batch.** Each batch adds, to `engine/season/tests/test_storybar.py`
(the file `20_NARRATIVE_F` edit 4 opens), one planted log per story it claims: the shape reads 1 on the
plant; 0 with any one beat removed; 0 with the plant's causes re-drawn by `edge_null`
(`09_WR_story_instruments_that_can_fail.md` edit 2); and a shape whose reader does not exist prints
`n/a`, never 0. That test is what makes "the story occurred" an assertion that can observe the failure it
excludes (§0.1 pt 2). It is the one file a batch's mid-session run covers (§0.4).

### 6.2 The batches

Order follows supply (§3's last paragraph): E-0 → E-1 → E-2 → {E-3, E-4} → {E-5, E-6, E-7, E-9} →
{E-8, E-10} → E-11. Braces mark batches with no edge between them; they may be built in separate
worktrees and are closed one at a time (§0.4). "Completes" lists the stories whose every needed
mechanism has landed once the batch closes. Cost classes as the suite's (edit · small build ·
design-first).

| batch | lands (proposals) | completes | gate, beyond §6.1's clauses for the listed stories | hash | cost | edges |
|---|---|---|---|---|---|---|
| **E-0 the instrument** | STORY-D; `09_WR_story_instruments_that_can_fail`; `20_NARRATIVE_F`; `16_PESSIMIST_GAME_consequence_reading`; `09_WR_B_readings_of_closure_and_tension`; `12_ARCS_case_on_the_realm`; `07_SE_valley_scenario` (the fixture world) | none | C0 holds; every one of the 73 shapes that has a reader prints 0 on the shipped realm at seeds 0 to 2, and each planted log reads 1: the bar failing on today's engine | EQUAL (harness and one fixture world) | small build | WR, NARR, GAME, ARCS, SE |
| **E-1 the offer makes sense** | `02_CHAR_offer_what_can_be_done`; VB-A; SOC1-A; SOC2-A; PES-CORE (`a_refusal_is_remembered`, `no_stored_plan`); PES-FI-D; PES-CHAR-B; `01_CORE_unmet_need_is_attended_first`; `01_CORE_predicates_name_their_clause` | none alone | refusals fall below one act in ten at seeds 0 to 2 with no verb's executed count falling to 0 (HAPP batch 2's reading); the retry rate after a refusal falls against the `refusal_memory` 0 arm | movers: every realm golden (formation) | edit + small build | CHAR, CORE, the verb lanes; HAPP-D §2 |
| **E-2 drawn, written, kept** | DET-A, DET-C; `13_SC_draw_for_unrolled_contests`; `05_SC_obstacle_difficulty_and_modifiers_B`; `05_SC_contest_record_on_event`; PES-DICE (both); `10_DICE_one_score_two_roles`; `10_DICE_capability_axiom_map`; `02_CHAR_capability_definitions`; `03_PC_person_inputs_content`; MIL-B; PES-GAME (`standing_occasions_carry_their_cause`); PES-CORE (`the_record_holds_what_changed`); `01_CORE_reason_trail_in_the_act_store`; **STORY-A**; (Jordan's choice) PES-CORE (`a_scene_runs_in_its_own_order`) | S-60, 68, 69, 71, 72; S-67 on Jordan's option B | the share of acts drawn rises from under 11% to over half (GAME §0's census); every one of the four bands occurs on at least five verbs across seeds; `SHORTFALL_STEP` 3 occurs on under one failure in five at the calibrated pair (`13_SC_calibration`); with `stake` rows at control, S-68 and S-69 read 0 | movers: every realm and case golden | small build ×3 | DICE, SC, CHAR, CORE; `13_SC_tuning_tables` |
| **E-3 bodies, time and places** | HAPP-A; PES-WR-C; `09_WR_B_weather_with_memory_and_the_year`; NARR-E edit 1; PES-GAME (`the_world_draws`); `07_SE_ground_and_granaries`; `07_SE_treasury_granary_B`; PES-SE-A, -B; `07_SE_population_census`; `07_SE_population_regrowth_B`; `07_SE_kernel_repairs`; MAT-A (`tend`), MAT-B; MIL-A; PES-WR-A; `03_PC_exits_withdrawal_recovery` Part C; PROC-A, PROC-B (ages) | S-01, 31, 32, 34, 35, 36, 40, 66 | the played arm differs from the no-act arm in stores and in cohort weight at each seed (GAME's game gate, first clause); site condition and yield differ between seeds; S-32's variants include relieved, unrelieved and recovered; under the `bodies` arm natural deaths number one to three in twelve seasons, nearly all after a season of illness (HAPP-A's own gate) | movers: `Person.born` (every world); the weather, hunger and wear draws; endowment | small build ×4; natural death's on-switch is Jordan's | SE, WR, GAME, HAPP, PROC; B10-18 CL-EVENTS |
| **E-4 news and regard** | FI-01, FI-02, FI-06; PES-FI-A; DET-B; PES-SC-B, -E; SOC2-B; CR-29; `02_CHAR_relations_have_a_ground` (with PES-CHAR resolution 11); `02_CHAR_scar_is_a_wound`; `02_CHAR_scar_cap_and_regard_unit`; `02_CHAR_which_ground_moves_whom`; NARR-A, -B, -C; PES-SC-C; PES-PC-C; PES-GO (`a_witness_may_connect_what_he_holds`, `the_offer_names_what_is_held`) | S-02, 29, 33, 37, 52, 57, 70, 73 | told chains of two hops or more above 0 at three seeds of five (FI-02's gate); `20_NARRATIVE_F` clauses 2 and 5 for G1, G3, G5; a death is held by more persons each season after it and by fewer than all (S-02); S-33's blamed holders number three or more at two seeds, none above 60% (NARR-B's gate) | movers: the telling and notice draws; `basis_off` reproduces today | small build ×3 | FI, CHAR, NARR, SC, GO |
| **E-5 seats pass, orders bind, houses continue** | VB-C, VB-D; BYZ-E; HAPP-B; `06_FA_seat_terms_and_turnover`; `06_FA_seat_terms_by_body_B`; `06_FA_remit_grant_by_row`; PES-FA-A, -B, -C; `06_FA_decree_binds`; SOC1-B; NARR-D; SYN's batch I-1 (the registry, EQUAL) ; **STORY-B** | S-04, 05, 06, 07, 10, 15, 16 | seat holders differ between the played and no-act arms and between at least two seeds (GAME's gate, second and fourth clauses); over 40 seeds with King and heir dead the throne is held, fully or provisionally, at the end of four seasons (HAPP-B G2) and by more than one title across seeds; `comply` executes at each of its four bands; with `provisional_term` at control S-05 reads 0 | movers: runs with a death, a writ or a marriage; I-1 EQUAL | small build ×3; STORY-B's births behind a control, on-switch Jordan's (§8 J-1) | FA, institutions (I-1, I-6), HAPP, NARR |
| **E-6 violence with a cause and a mercy** | PHY-A (A0 to A4); `03_PC_duel_chain_reach`; SOC1-D; PES-PC-A, -B, -D; DET-D; `03_PC_duel_round_and_approach_B`; `03_PC_typed_outcome_one_door` | S-08, 27, 28 | HAPP-D §2's four-season reading at seed 2 (no ruler seized to death by his own officer); duels fought at two seeds of five or more with at least three of the scene's endings occurring; a `person.died` or a wounding is among the causes of another person's executed act (GAME's gate, third clause) | movers: every log with a fought scene | small build ×2; the duel round is design-first with PC | PC, HAPP batch 1, CHAR (`02_CHAR_what_an_act_risks`) |
| **E-7 crime, inquiry, hearing** | HAPP-C; PES-FI-B, -C; FI-03, FI-07; `08_FI_05_evidence-interface_B`; MAT-D, MAT-E; PHY-C; LAC-1 to LAC-4; `05_SC_evidence_and_rebuttal_B`; `05_SC_acquittal`; `05_SC_arrangement_rows_that_bind`; VB-B; SOC2-C; `05_SC_playable_hearing_B`; PES-SC-A; PROC-C (case seeds) | S-03, 09, 12, 30, 43 to 47, 49, 51, 53 to 56 | LACUNA §6's standalone case, shipped chooser in every seat, 20 seeds: all five verdict results occur across seeds except reversal, which occurs at one or more; a conclusion is held and wrong at one seed or more (S-51) and right at one or more; closing Events by act exceed closing Events by clock (`20_NARRATIVE_F` clause 6); with the trail rows at control S-55 reads 0 | movers: every log with a hearing or an inquiry; `enmity` dark at control | small build ×4; HAPP-C design-first | FI, SC, LACUNA; the forced order of LACUNA §6 |
| **E-8 the field and the war** | `04_MB_headcount_grade_and_scale`; `04_MB_typed_outcome_and_one_path`; PES-MB; `04_MB_manager_battle_one_resolver`; `04_MB_playable_field_scenario`; `04_MB_unit_loadout_and_weapon_in_hand_B`; `06_FA_war_lives_in_seats_B`; PES-FA-B edit 4; `06_FA_levy_through_the_seat_B`; PHY-B; VB-E; MIL-C, MIL-D; `07_SE_campaign_supply_and_muster`; COL-D (`annex`); CR-91 | S-14, 20 to 26 | `field.won` above 0 and below the count of fought fields at three seeds of five; a place changes hands by arms at one seed or more and a seat with it; a war ends by an instrument at one seed or more and by a declarer's fall or a successor at another; with `field_troops_per_weight` at today's value S-21 reads 0 (the control is the shipped scale) | movers: every fought field | small build ×4; the form of fortune is Jordan's | MB, FA, SE, institutions |
| **E-9 the interior** | PES-CHAR-A, -C; PES-SC-D; SOC1-C; NARR-E edit 3; `12_ARCS_arcs_as_staged_goals`; `02_CHAR_goal_lean_on_its_own_question`; `02_CHAR_resolve_and_temper` | S-59, 61, 63, 64, 65 | the converts differ between seeds (today the same six at every seed); a scruple is held at some seeds and overridden at others for one person; an argument moves the hearer at one seed and the arguer at another; `20_NARRATIVE_F` clause 5 (`noconv` falls outside the seed spread) | movers; the crisis and scruple dark at control | small build ×2; two of Jordan's (ED-IN-0261) | CHAR, SC, NARR, ARCS |
| **E-10 instruments and institutions** | SYN-E's batches I-2 to I-9 as that file orders them (VEN-A to -D; COL-A to -E; PAP-A to -F; BYZ-A to -F; SYN-A to -D); SOC2-D; FI-08; `05_SC_negotiation_scene` | S-11, 13, 17, 18, 19, 48, 50, 62 | SYN-D's gate for *The King's Bill* (three of six ways of meeting the bill attempted; two endings; an act by a person who is not the King occasioned by his) plus the census: an instrument formed, kept at one seed and breached at another | movers per row; keys EQUAL | SYN-E's own | the whole of `15_INSTITUTIONS_SYNTHESIS_E_implementation_plan` |
| **E-11 the world strains and ends; what is built can fall** | PES-WR-B; `09_WR_world_motion`; `09_WR_strand_conclusion`; `09_WR_B_draws_not_thresholds`; MAT-A (`restore`, `work`, `sabotage`), MAT-C; `09_WR_B_threadwork_session_and_practitioner`; PHY-D; **STORY-C** | S-38, 39, 41, 42 | an ending Event at one seed or more and none at one or more within the horizon; the calamity's front stops where it was mended at one seed (PES-WR-B's gate); a founded hearth stands at the end at some seeds and is closed at others, and with `founded_lapse` at control none closes | movers: every world with a source or a founding | small build ×2; threadwork design-first | WR, MAT, SE (PES-SE J-3 for a town-scale founding) |

Seventy-two of the 73 complete by E-11; S-58 is decided out (§8 R-10). By batch: E-2 six, E-3 eight,
E-4 eight, E-5 seven, E-6 three, E-7 fifteen, E-8 eight, E-9 five, E-10 eight, E-11 four.

### 6.3 Where Jordan's intent meets Layer 1 (named at the site; none resolved by editing Layer 1)

| the intent | the Layer 1 or ruled item it meets | how the plan holds both |
|---|---|---|
| *we do not do deterministic*; arcs that end when a counter fires | `loop/matter.py` L5: *a crossing MAY NEVER PRODUCE AN OUTCOME* | they agree against the arcs' text. Every ending in §5 is a person's drawn act or a drawn break (PES-WR-B, `09_WR_B_draws_not_thresholds`); GAME's J-3 stays Jordan's for the arcs as written |
| blame, loyalty that erodes, a side resented | no social quantity moves at MATTER (`state/world.py:64-107`, as ARCS §4 reads it); no stored grievance (ED-IN-0225) | every pull is recomputed person-side from the person's own ledger and edges (NARR §7.6); nothing here stores one |
| "a story occurred" as a gate | ED-IN-0225: no carrier, field, kind or row for an arc, story or thread | the census is a pure read in the harness (STORY-D); a shape is a reading, like `strands_block` |
| the margin a narrator can read | `04` §A.2 and `holonic_ARCHITECTURE.md` §43, §45: a module takes typed input, returns typed outcome, keeps no state | the margin travels in the typed result and lands on the Event (`05_SC_contest_record_on_event`); STORY-A reads it there and nowhere else |
| births in play | Layer 1 §25 (births and deaths of envelope weight at MATTER; bodies a licensed clock) and §29 (CENSUS runs no clock), as `07_SE_population_regrowth_B` cites them | the draw is on the bodies clock at MATTER; the Person is individuated at CENSUS, PG-7's precedent (STORY-B; `[ASSUMPTION]` that a named birth is §29-conformant, named for the Layer 1 reader) |
| a founder's town that fails | SE-9(a): the settlement registry gains no node | STORY-C ends hearths and communities, the only things `found` makes; a town-scale founding is PES-SE J-3 |
| chains inside a scene (R-09) | the ratified fold order (#353 §27) | PES-CORE's survivor; S-67 waits on it and S-66 tells the same story across rounds meanwhile |
| a famine that reaches a lord | ED-IN-0255: only a cohort eats | it reaches him through blame (NARR-B), his seat and his chance of sickness (HAPP-A), never his own larder |
| affiliation, venue and personality set the odds | ED-IN-0352: a flow, an era or a regime never sets odds | only a person's own edges and interior, and the counterparty's as a contest already reads them, enter a roll (NARR R-N3) |
| natural death as the supply of successions | ED-IN-0317 (c): the values are deferred to Jordan | the shape lands dark; the gates read the `bodies` instrument arm until a rate is set |
| the disaster | the degree ladder's single owner (ruling of 2026-08-14) | no fifth band; the shortfall is the kept margin read further (STORY-A) |
| a failure its maker remembers | `rosters.yaml: undeposited_kinds` (ED-FI-0009: a failed inquiry deposits nothing) | the act store and the log are read by the chronicle and the census, in the harness; nothing is deposited and no person-side reader is added (STORY-A edit 4) |
| playable alone, one code path | the standing requirement | *The Lean Year* runs the unmodified `SeasonDriver` with `play_surface.dispatching_chooser`; no standalone fork |

## 7. The first playable: *The Lean Year*

Exact edits: `proposals/23_STORY_E_first_playable_the_lean_year.md`. One scenario on the valley fixture
(`07_SE_valley_scenario.md`: three towns unlike in endowment, one granary, one seat), extended by rows:
no second world, no third case base (`12_ARCS_case_on_the_realm.md` allows two and this is a scenario
beside `harness/scarce.py`, not a case). Roles, no canon names; nothing is authored but the starting
persons, seats, stores, one works and a prehistory of acts folded through the real RESOLVE and WITNESS
(ARCS's prehistory rule: a setup may not contain an outcome).

**The situation at tick 0.** An old lord holds the valley's seat and its granary. His heir of the body
is a grandchild under age with a mother; his nephew is of age and has a following in the harbour town.
A steward keeps the granary and has, in the prehistory, forged a sheet that moves a field from the
seam village to himself. The seam village mines and grows nothing. A bench of three sits in the field
town. A road joins the three towns and one of its legs is long. The year is about to turn.

**What can happen, and by what** (33 of the 73, by cut):

| cut | after batch | stories it can produce |
|---|---|---|
| 1 · the year | E-3 | the harvest falls short or does not (S-35); the seam village goes short and the granary shares (S-32); the steward relieves it or does not, by a real amount; the villagers move toward the harbour (S-34) or trade ore for bread (S-36); the old lord sickens, is tended, recovers or dies (S-01, S-31); a messenger sent to the nephew finds him gone and goes after him (S-66, S-40); an act that fails by a wide margin costs its maker more (S-68), a relief that only just arrives costs the granary (S-69), a second attempt succeeds (S-71) |
| 2 · the seat | E-5 | the news of the death reaches the harbour late (S-02) and grows in the telling (S-52); the nephew and the child's mother each claim (S-04); a regency or a provisional lord (S-05); the lord's sworn men are told to obey and each answers (S-15); a household is raised or put out (S-10); the hungry blame whoever they believe held the granary (S-33, S-37); the village under-reports its stores to a levy (S-57); the loser of the claim is known as its loser (S-70) |
| 3 · the wrong | E-7 | the dispossessed villager's grievance; a challenge to the steward, heard and answered (S-27, S-28); or a killing by night, guarded against and perhaps seen (S-09); an inquiry that finds the forged sheet or the trail at the place (S-53, S-54, S-55); a conclusion that names the steward, or the wrong man (S-51); a hearing with the sheet cited and answered (S-46), a verdict, an acquittal or an appeal to the realm's bench above (S-43, S-44, S-45); revenge by the dead man's kin (S-08) |

**Choices for a played seat** (any of: the lord, the nephew, the mother, the steward, the village
head, a judge, the investigator): what to do with the granary; whom to tell and what; whether to
claim, swear, obey or leave; whether to accuse, on what, before which bench; whether to fight. Each is
the same Candidate an NPC is offered, with its believed odds and its `stake` shown.

**Endings** (each a Query over Tenures and the log, none a counter): the seat held in full by one
claimant; a regency confirmed or lapsed; the valley's population at or under half its weight; the
steward convicted, acquitted or dead; the seam village closed or grown; eight seasons with none of
these (a stable continuation, reported as such).

**Gate.** Seeds 0 to 19, 8 seasons, the shipped chooser in every seat, no played seat: at least 12
distinct stories occur across the seeds; no story occurs at all 20 with one variant; at least four
distinct endings occur; no more than three seeds share one story set and one ending; in the control arm (every batch fixture at control) the census reads only §2.10's set. Planted
failure: every roll pinned to Success, and the seeds must then agree on the ending. One played run per
seat at seed 0 shows a choice changing the ending against the unplayed seed 0 (the control is the same
seed with the callback returning the chooser's own pick: equal hash).

**One code path.** `harness/valley.py::run(seasons, seed, play=None)` as `07_SE_valley_scenario`
proposes it; the played seat is `play_surface.dispatching_chooser`; the hearing is ENCOUNTER's deferred
sitting (`05_SC_playable_hearing_B`) and the field is RESOLVE's graded routes, as in LACUNA §6. The
realm's first playable remains SYN's *The King's Bill*; the two do not merge: this one is small enough
for a reader to hold entire and is what the census is first read on.

## 8. Decisions

### 8.1 Decided by the five-step ladder (twenty)

Steps: 1 superseded · 2 irrelevant · 3 a design document or ruling · 4 precedent · 5 architecture.

| id | question | decided | step | carried by |
|---|---|---|---|---|
| R-01 | lanes' story lists include endings that fire on a count (an arc's counter, an era's clock) | every ending in this plan is a person's drawn act or a drawn break; L5 stands; the arcs' text is GAME's J-3 and is not re-raised here | 3 (`loop/matter.py` L5; the standing rule) | §5; PES-WR-B; `09_WR_B_draws_not_thresholds` |
| R-02 | "a town dies when its body reaches zero" | a population thins by a drawn fall and a census; its removal at the weight floor is bookkeeping that follows draws | 3 (CR-08's text, as `07_SE_population_census` cites it) | `07_SE_population_census`; PES-GAME (`the_world_draws`) |
| R-03 | is the disaster a fifth band | no: the ladder is single-owned and ruled; the shortfall is the kept margin read further, mirrored on the ladder's own "3 or more" | 3 | STORY-A edit 1 |
| R-04 | a founded place "ends at zero": is that a threshold deciding an outcome | no: the wear and each mending are drawn; closing a rung whose last Site stands at zero with nobody residing is bookkeeping after them, as `_die` at body zero is | 4 (`_die`; `raze`'s tail) | STORY-C |
| R-05 | the deposition of a crowned or anointed head (`revocation: null`, ruled) | no new row and no change to the ruled null: such a head falls by conquest (COL-D), by a sentence his sworn men each answer (PAP-D), by a College after a crisis (CR-37, `06_FA_seat_terms_by_body_B`), or by his own `release` | 3, 4 | §5 S-11; no file |
| R-06 | what a regency is | the consort's or guardian's claim landing at Partial (HAPP-B), and any hold by a person under `majority_age`, which is always provisional | 4 (VB-C's Partial) | STORY-B edit 4 |
| R-07 | a besieged town's larder | while a `besiege` posture stands on a rung, the larder ladder's walk for cohorts under it stops at that rung (which rungs may feed whom is eligibility); the field ration of the besieger is the season's ration (PES-SE R-14) | 5 | a constraint on `07_SE_campaign_supply_and_muster`; listed for SE and MB |
| R-08 | a burned granary | `sabotage`'s referent class gains a rung's store of a kind beside a Site; the loss is drawn and graded as MAT-A draws the Site case, and leaves a trail (PES-FI-C) | 4 (MAT-A's own row) | listed for the MATERIAL lane; no file |
| R-09 | a hoarder, a profiteer, a cornered market | no price mechanism is planned: `coin` has no source (PES-SE R-08) and a price would be a second economy. The story is told as relief withheld (S-33) and a debt on terms (VEN-B) | 2, 5 | §5 S-37 |
| R-10 | a planted clue that misleads | out of this plan: K-37 (ratified as intent) refuses a false finding, no shipped game solves it, and its near form is already Jordan's (PES-FI S-PES-FI-1) | 3 | — |
| R-11 | who is blamed for a due that lapses under an empty seat | the believed holder of the seat that may fill it (`may_fill`), else nobody: a vacancy costs the one who left it open | 5 | an amendment to `20_NARRATIVE_B`'s `dues_unmet`; listed for that lane |
| R-12 | an ambush: the opener's edge | one `context_terms` entry, `unready`, on the `enmity` and `war` contexts: a named level for the attacker in the first exchange when the victim's notice draw (DET-B) failed; no surprise input on the module | 4 (`context_terms`, PHY-A A3) | listed for PHY-A and HAPP-C; no file |
| R-13 | may a story be counted | yes, as a reading: the census mints nothing (ED-IN-0225) | 3 | STORY-D |
| R-14 | where the gates are read | the valley at 20 seeds, the realm at 5; one process per seed and arm | 5 (cost; `20_NARRATIVE_F`'s size) | §6.1 |
| R-15 | batch order by count or by supply | by supply: bodies, places, news and violence before the seats, hearings and regard that consume them | 5 | §6.2 |
| R-16 | where capability lands | with E-2: a draw whose pools do not differ gives one distribution for everyone (PES-DICE §3.3), so every later gate's spread depends on it | 5 | §6.2 |
| R-17 | the errand | no new mechanism and no stored plan (PES-CORE's deletion stands): a remembered refusal, a believed place, a journey, the act again | 1 (carried by MIL-A, PES-CORE, SOC1-A) | §5 S-66 |
| R-18 | refugees need a population that can move | `02_CHAR_offer_what_can_be_done`'s declared aperture for a population is the default; it is GAME's J-2 option (b) in shape and that item stays Jordan's | 4 | §5 S-34 |
| R-19 | *The Lean Year*: a case or a scenario | a scenario on the valley fixture; it borrows ARCS's prehistory fold and adds no case base | 3 (`12_ARCS_case_on_the_realm`: two bases, no third) | STORY-E |
| R-20 | where the success that costs sits | at Partial, on rows that declare a `stake:`: the obstacle met and not exceeded | 4 (Partial's own definition in `degree_from_net`) | STORY-A edit 2 |

### 8.2 For Jordan from this lane (one)

**J-1 · Are named persons born in play?** It survives the ladder: no ruling covers a named birth, PG-7's
arrivals are held by `21_PROCEDURAL_D` for Jordan, and the two options are different games.
- **(a) Births on**, in STORY-B's shape, behind `birth_rate` (control 0): a couple under a `marriage`
  may have children; a house can continue or fail; a regency has a child at its centre; over a long
  campaign the cast grows and the port carries a roster with no fixed size.
- **(b) No births**: the cast is what the build made. Minors exist only where the build or the
  generator placed them, come of age (STORY-B edit 4 stands either way), and a house ends when its
  living members do. Succession is a game of the people already on the board.
Recommended: (a), dark at control, since under (b) every line in the realm is finite and the succession
family runs out of claimants in a long campaign. STORY-B's marriage and majority land under either.

### 8.3 Already Jordan's, with the default under which no batch waits (twelve)

| item (owner lane) | bears on | the plan's default |
|---|---|---|
| natural death on or off (HAPP §4 item 1; ED-IN-0317) | S-01, S-04, S-05 | the shape lands dark; gates read the `bodies` instrument arm |
| may a person commit a killing (HAPP §4 item 2) | S-09, S-55 | `enmity` dark at control; E-7 gates on PROC-C's case seeds meanwhile |
| who may claim when the line fails (HAPP §4 item 3) | S-06 | HAPP-B's list (its recommendation) |
| a crisis of faith: by rule or drawn (PES-CHAR §6 item 1; NARR §10 item 1) | S-64 | drawn, behind the control arm |
| a scruple: a line or a tendency (PES-CHAR §6 item 2) | S-61 | a draw, behind the control arm |
| a scene: a budget unit or a short sequence (PES-CORE §6) | S-67 | option A as built; S-66 tells it across rounds |
| is leaving a side a strife move (NARR §10 item 2) | S-16 | `never` stands; the defection is still a deed others hold |
| the form of fortune in a field (PES-DICE §6) | S-24 | option A, owned and written on the result |
| may a place begin and end (PES-SE J-3) | S-38 | option A: hearths only, with STORY-C's ending |
| who is a verdict for (PES-SC §5 item 3) | S-49 | option A as ruled; a remedy to the petitioner waits |
| how fast a death travels beside the seat it empties (PES-FI S-PES-FI-2) | S-02, S-03 | option B (apart): the plan's S-02 and S-03 need the delay |
| does a chronic dearth speak (PES-SE J-1) | S-32, S-33 | option A: once, at the first short season, then memory and rumour |

## 9. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/STORY/`.
`PYTHONHASHSEED=0` for both probes. **No season was run by this lane**: every realm and module reading
in §2 and §5 is the cited lane's, and a mark of `[R]` or `[N]` rests on that lane's run.

| id | probe | reading |
|---|---|---|
| E-1 | `p1_rows.py` → `p1_rows.txt`: a static read of `engine/season/verb_table.yaml` (no engine import) | 67 rows, 11 with `contests:`. Of the 11: Failure `writes` is empty or absent on 11 (seven margin rows write `[]`; the four scene rows key by ending, not band); Partial writes on 2 (`arrest`, `determine`); Overwhelming equals Success in both `writes` and `emits` on 9. Control: the reader does see band-keyed writes where they exist (`argue` Success `Person.pursuits`) |
| E-2 | `p2_count.py` → `p2_count.txt`: counts from this file's own §2 tables | 73 stories; today X 56, N 15, H 2; 42 named by more than one lane; the per-mechanism counts of §3 |
| E-3 | `ls audits/`, re-checked before finishing | the twelve `16_PESSIMIST_*` audits are present; `16_PESSIMIST_PC.md` and `16_PESSIMIST_GO.md` were still being appended when read (PC §4 marked "appended below"), so a finding those lanes add after this read is not in §2 |
| E-4 | code opened at the line for a fact a design here rests on | `engine/dice_engine/dice_engine.py:236-248` (the ladder: margin ≥ 3, ≥ 1, ≥ 0, < 0); `engine/season/data/rosters.py:1111` (`DEGREE_STEP`); `engine/season/rosters.yaml:1458` (`undeposited_kinds: ["finding.none"]`); `engine/season/state/acts.py:1-40` (the act store holds refused acts too); `engine/season/data/fixtures.py:690-692` (`age_step`, `illness_rate`, `age_at_build` at 0); `engine/season/harness/storybar.py:1-60` (grades nothing; ED-IN-0225) |

Not read, and what rests on it: the bodies of most of the suite's proposals were read at their heads
only (title, status, runtime paragraph), so §4.1's key names are those files' and are cited, not
verified at the line `[UNVERIFIED beyond the head]` except where §5 or §9 E-4 quotes a line;
`audits/09_WR_audit*.md`, `15_INSTITUTIONS_{BYZANTINE,COLONIAL,PAPACY,VENICE}.md`, `21_PROCEDURAL_GENERATION.md`
and `12_ARCS_adjudication.md` §3 were read through their synthesis sections and through the pessimist
lanes that cite them.

