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

**Six stories had a link no proposal carried**, and they reduce to three mechanisms, written here as
proposals: what a roll leaves behind (the disaster, the success that costs, the contest with a loser, the
comeback remembered: `23_STORY_A`); a house that continues (a marriage, a birth, a coming of age, and so
a minority and its regency: `23_STORY_B`); a founded place that can fail (`23_STORY_C`). Two more
proposals carry what the plan itself needs: a **story census** on the one story instrument, which names a
story by its beats in the cause graph and prints its rate, its spread of endings and its control
(`23_STORY_D`), and a **first playable**, *The Lean Year*, a valley of three towns, one granary, one old
lord, two claimants and one bench, which can produce 31 of the 73 in eight seasons from persons' acts
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
from this lane** (whether named persons are born in play, §8 J-1); eleven items other lanes already
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
witness holds "X bested Y" and Y's regard for X moves by M5. (4) A person's own failed attempt is read
from the act store by `person_q.attempts_before`, never deposited (the `undeposited_kinds` decision
stands), and weighs in `admission_weight`.

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

