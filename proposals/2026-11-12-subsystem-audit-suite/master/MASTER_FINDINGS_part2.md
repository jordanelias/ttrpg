# The master findings — part 2: the recommendations, what is not established, Layer 1, what v11 carried, what is not resolved, how to read the suite

## Status: REFERENCE (part 2 of `master/MASTER_FINDINGS.md`; resolves nothing at runtime; dies with the suite)

Paths, words and the batch handles are as in the head part. "Owner" is a lane of the nine-lane roster; a batch handle is v12's (`master/workplan_v12/V12_STRUCTURE.md` §2.1).

---

## 4. The recommendations: the design directions this session settled

Each direction is a ruling or a cluster of rulings that changed the shape of the game, with the findings it answers, the carrier that holds the edit, the v12 batch that lands it and the lane that owns it. A direction is a recommendation in the plain sense: the finding is answered by building this, in this order. None has executed.

**4.1 The bell curve everywhere, score plus a base, two inputs (A-5, A-6, A-7, A-8, A-98, A-112).** Every roll in the game, social, material and martial, draws on one sampler (the bell curve the fight already uses); the whole-dice social roll, the battle's whole-dice sampler, the exact-odds table and the fraction rule are deleted. A skill score counts outside a fight as score plus a base with a floor of five, which offsets the bell curve's extra difficulty; the roll takes two inputs, an attribute and a skill (A-7, A-98: an aptitude *is* an attribute); a wound is a level against the roll at every pool, as combat spends it (A-8); combat reads skill scores through the skill table and drops its own `faculty` (A-112). Answers F-DICE-01 (the engine fed a constant), F-PC-02 and F-DICE-17/-18 (every person the same), F-PES-DICE-01 (the degree changes nothing; with the verb batches). Carriers: `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`, `U5a_capability_home_and_two_inputs` (Part A in **B04**, Part B in **B05**), `U5a_DICE_owed_edits`, `10_DICE_one_roller_one_fraction_rule` and `10_DICE_one_score_two_roles` (**B05**). Calibrated jointly with A-26 and A-31 in B05 (one re-pin of every seeded result). Owner **IN**.

**4.2 One opposed rule for fight and argument (A-26, A-71, A-79; A-31).** A defender's trained skill score stands against the roll at 0.4 per point (the dice it would net); his attribute and his wounds reach the roll as named levels under the soft cap; the six base dice both sides hold are never part of the opposition (`audits/29_ONE_OPPOSED_RULE.md` §0). One rule, one better-one-wins curve; the centres differ (an even blow draws blood about one time in two; an even routine argument fails 59 %, half-lands 16 %, carries 25 %: a position holds unless something moves it). The fight's obstacle moves from 1.0 to 0.8 at the shipped realm, against A-31's letter, accepted by A-79; A-31's damage scale (1.07) stands, so a fight runs about 4.3 turns and 4.5 wounding blows where it ran 3.4 and 3.2. Answers F-PES-PC-01 (a fight is two blows), F-SC-03 (equal opponents drift), the half-score ruling of 2026-08-14 (overridden). Carrier: `29_DICE_one_opposed_rule_form_and_tuning` (**B05**), with the SC tuning tables recomputed (`13_SC_tuning_tables`, B05) and the combat calibration in **B15**. The docstring of `engine/dice_engine/dice_engine.py::degree_from_net` still states the old rule and is rewritten in B05 (`L1-A26`, a CODE row). Owner **IN** (B05), **PC** (B15).

**4.3 The seat modifier and three optional seat facts (A-12, A-13, A-14, A-105).** Holding an office may make a roll easier: a seat carries a modifier (against the register's recommendation), and may declare the clerks an order passes, the hands its paper needs and an audit at its holder's exit; a seat that declares none behaves as today. A vote is a draw on the voter inside the presiding person's act (A-14). A re-grant that narrows a sitting holder's grant is a revocation, its odds read the power relation between the two factions (A-105). Answers F-FA-01, F-FA-02, F-PES-FA-01 and -02 (a polity that neither binds nor turns over) and the institutions kit's chancery, paper and exit audit. Carriers: `14_VERBS_BINDING_C_turnover` (the standing term, **B21**), `13_SC_tuning_tables` T4 (the bench die, B05), `IS-B3-FA-07` (H-132's clause, B21, D-01), the institutions kit `15_INSTITUTIONS_SYNTHESIS_A`, `_B` (**B32**), `_C` (B33), `_D`, `_E` (B40). Layer 1 amended (`L1-A12`, `L1-A13`, `L1-A105`). The unification must keep the seat's modifier and regard from counting twice (A-12's consequence). Owner **FA**.

**4.4 Land and the march (A-57, A-58, A-65 to A-70, A-73, A-74, A-103).** A won battle takes land if and only if the aggressor marched to take it and won; seats pass with holdings; a draw leaves the defender holding, and both armies return to their stations at once; the winner chooses to seize, occupy without seizing, or withdraw, and so may an uninvited rescuer; an unopposed entry onto held land is tolerated and disliked in peace with a working bench, and is aggression where there is enough tension or strife (read with the realm's strife level, A-85); the taker may raze what he holds; a march may be thought of on a claim or a grievance, and a claim is its occasion, never its admission gate (A-103). Answers F-FA-13 (a defeat costs bodies and never a holding or a seat) and Layer 1's faction contract ("holdings and seats", now met). Carriers: `U5d_FA_land_and_seats_pass_on_a_won_march`, `26_MASS_BATTLE_aggression_and_land`, `IS-B3-FA-04` (**B23**); the claim carrier CR-91 (1), (2), (4), (5) and IN-36's cap of one march a season a territory (**B21b**); A-76's stand-in for "parliament is functional" (any working realm bench, switchable, until H-90's Court Parliament exists). Owner **FA**.

**4.5 Eras, regimes and strife (A-45, A-46, A-82 to A-86, A-80, A-81).** An era is a named period that always exists and ends on a death, a change of rule (a ruler's conversion included), a war breaking out or a peace; the next is named from what happened. A regime is a camp of shared opinion on caste, religion, politics, Altonia, militarism and more, held to some extent, with a core and a fringe, and it presses its members to behave its way while they stay individuals; the pressure is read from what each person believes those around him think, never from an omniscient count. Strife is several strands that can each end; leaving a creed or a head seat is the era's Split. Entrenchment must still move the world, and no scene may leave it still (A-80, A-81). Answers `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §0 (no era, no regime beyond a credit factor, no momentum that is a person's), `audits/20_NARRATIVE_CHURN.md` §0 (chains with causes and no plot), F-NARR-02. Carriers: `30_WR_A` to `_E`, `30_WR_G`, `30_GO_F`, `IS-B3-FA-03`, `IS-B3-GO-04`, `IS-B3-SE-02` (**B38**), with `30_WR_A:65` corrected by A-103; the no-null-scene reading from **B02** (the `NULL SCENES` baseline) to B38 (asserted 0). Owner **WR**. The five sentences of the ratified strife master that A-84 rewords are held (§6).

**4.6 The houses' and the Church's stances (A-87 to A-91, A-92).** Varfell anti-caste, leaning Einhir, militaristic, unhappy with the royal order, with the Einhir Revival gathering inside it; Hafenmark pro-caste, devout, parliamentary, content with the royal order; Valorsmark tolerant of caste, pro-Solmund with Einhir sympathies, mixed in government (a fault line between its Marshal and its Clerk), pro-royal order; the Church neutral on the royal order, indifferent to caste and parliament, set on religious affiliation and anti-Einhir; the Einhir are both a faith and a people, two linked axes. What a person has seen and been told of others' deeds may enter his own drawn change of conviction and nowhere else (A-92; the setting ships at zero). `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md` §0 measured it: with the 46 rows applied in memory, the houses order as the rulings say and six regime cores each find their people (on the shipped values, one wide tent and a church). Carriers: `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes`, `31_WR_B_the_revival_gathers`, `31_WR_C_what_the_stances_feed`, `30_WR_G_regime_opinions_and_the_pull_of_ones_own` (**B38**); `30_WR_G` commit 1 as written does not build (its three `concerns:` keys make `conviction_of` refuse all 46 rows, P-31-5). `sway_gain` is set in **B98**. Owner **WR**.

**4.7 Mass battle as an abstraction of personal combat (A-100, A-113, A-59, A-60, A-61, A-77, A-78, A-99).** A mass-battle exchange draws from a damage distribution set by armour, discipline, exposure, morale and fatigue, not a pool against an obstacle; the weapon-on-weapon and weapon-on-armour numbers are derived by simulating personal combat (an exporter with `--check`), and the matchups personal combat does not model (shields, pikes, horse with lance, missiles) ship as stated rows, each checked against history and banded between its derived neighbours, a test failing when one leaves its band (A-113). An order takes effect by a draw on the commander's command; each unit carries its own prowess; the army's strength is dynamic, and the side-wide luck multiplier ships at zero if its test's first arm passes (A-77); numbers act through frontage, depth and endurance (A-60); a body may break below the 15 % band by a stand draw (A-61); the dead, captured and deserted are lost and some of the injured and the regrouped return unprompted (A-78). Answers F-MB-01, F-PES-MB-01 to -03, F-MB-14, F-MB-21, `audits/26_*` §0 (the sources decide a battle by a shock at small loss). Carriers: `master/mb_abstraction/MBA_DESIGN_part3.md` MBA-01 to MBA-03 (**B19a**), MBA-04 to MBA-06 and MBA-08 with `26_MASS_BATTLE_*` and `27_MB_A`, `_C` (**B19**), `27_MB_D` (B20), `27_MB_E` (B22), MBA-07 (B30), MBA-09 and `27_MB_B` (**B31**); the words (army formation, unit formation, no size word) land in **B16L** and **B16M**. The duel's own defects are a precondition (F-PC-04: a plain `fight` still kills every time). Owner **MB**.

**4.8 A fight is a sequence of rounds (A-101, A-72, A-4).** A round is one engagement: two combatants close, exchange one to four attacks, and part; four to ten seconds is an indicator, not a clock; between rounds wounds, stamina, poise and weapon form carry over and initiative resets; a fight ends at a felling, a yield, a withdrawal or the engine's budget. A battle may call one duel round, and a duel round calls nothing (A-72). The season's pass is renamed a **lap** so "round" means one thing. Answers F-PC-13 (the duel and the grid round are not one path), F-PES-PC-01. Carriers: `master/pc_round/PC_ROUND_SPEC_part2.md` PCR-1 (**B15**), PCR-2 and PCR-3 with `03_PC_duel_round_and_approach_B` (**B16**), PCR-4, the `lap` rename (**B04**'s first item, D-05). Layer 1 keeps its word "round" for the lap at `04:1065` and `hol:1166` (held, §6). Owner **PC**.

**4.9 Hidden places and events (A-109).** No general exploration act: travel and inquiry cover ordinary discovery. There must be a way to find what is concealed (a place or an event hidden from public view): a concealment, a drawn search against it under the one opposed rule where a person conceals, what a find yields, and the exposure risk at depth (which gives `surveil`'s Exposure its carrier). Answers H-325 and H-326's residue (MISSING-DEP). Carriers: a design item first (`IS-B2-FI-07` with `IS-B3-SE-06`, at **B11**'s open, `opus` with a `ners` critic, D-18), then `IS-B3-SE-06`'s build (**B12c**). What the design cannot settle by the ladder stops for Jordan. Owner **FI** (design) and **SE** (build).

**4.10 Traits (A-107, A-98 (4)).** The four `moved_by_*` dispositions (evidence, consequence, authority, solidarity), seated from `npc_registry.yaml: resonant_style`, are a separate roster, not skills: a new `Person.traits` field with its own loader, giving no dice. It is an encoding mover (a new field on a hashed carrier moves every content hash, `V12_STRUCTURE.md` §0 fact 1), re-pinned once. Carrier: `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §2a with `IS-B2-CHAR-05` (**B04**). Layer 1 amended (`L1-A107`). Owner **IN**.

**4.11 Manner offsets (A-108).** A person may carry a stored offset on each manner axis (rigid/flexible, grandiose/humble, deontological/instrumental), so two people with the same pursuits differ in manner; manner is what his pursuits project plus his offset. Carrier: `IS-B2-CHAR-07` (CL-PERSON's build, **B10**) with a neutral control that reproduces today's hashes at zero offset; the cast's offsets are content (**BA1**). Layer 1 amended (`L1-A108`). Owner **IN**.

**4.12 The tenth module (A-102).** "Start a new game" lives in `engine/season/boot/`: the realm builder and the chooser's set-up move out of `harness/populated.py`; a pure move, no outcome changes. Answers H-02 (the game has no entry point of its own). Carrier: `CI-07` (**B03c**), with `CI-06` (one owner of the chooser's composition, B03). Layer 1 amended (`L1-A102`, `ED-IN-0359`). Owner **IN**.

**4.13 Also settled, in one line each.** Everything consequential is drawn (A-24): the task draw for uncontested verbs (**B07**, with the loader edit G-01 requires) and the keyed draw, one draw per key with no recorder (A-30, **B06**). A scene is a short sequence in the chooser's order (A-9, **B08**); a visit occupies the person visited, with precedence by rung, appointments and a petition that grows while it waits (A-63, A-64, `28_CORE_scene_access_*`, **B28**, **B38**). Management orders cost no scene budget and may prompt scenes (A-104). A failed attempt on a guarded target is always caught and detained (A-96, **B37**). Natural death on behind authored ages, named births behind a rate (A-15, A-75, **B37**, **B39**). The common people's few heavy moves (A-56, **B38**). Caste expressed in regard, vote blocks and informal tiers (A-41, A-42). A learned skill is never lost (A-106). The prologue simulates five years (A-51, **B39**). Persons are generated, about 94 plus kin, capped (A-44, **B39**). A world that fails its checks rolls the next seed (A-53).

---

## 5. What is not established, and what each gap blocks

**5.1 Numbers not yet calibrated.** Every value below ships at its control or as `[ASSUMPTION]`, and its batch's PR body lists it for Jordan's correction (D-19).

| what | where it is set | what it blocks until then |
|---|---|---|
| the re-centring of the bell curve with score plus a base (A-5, A-6) and the 0.4 a point against it (A-26, A-79) | B05, one joint calibration (C1–C8 read red then green) | every seeded result; R-09's readings at M1 |
| the fight's obstacle 0.8 and damage scale 1.07 (A-79, A-31) | B15 | R-04's combat scale; the round (B16) |
| the field's contact table, the side-wide multiplier's six-arm test (A-77), stand and pursuit draws, the troop file's seeds and the stated matchup rows (A-113) | B19a (the instrument), B19, B31 | every fought field; R-04.c4–c5 |
| the settings that ship dormant: `sway_gain` (A-92), `faction_power_step`, the load of `management_orders`, `sitting_exchanges` above 0, `npc_decider_roles`, the thread curve (the six named in `V12_STRUCTURE_part3.md` §7.8; the full list waits on the author lanes) | B98, one item each against its source's target reading | the mechanisms the batches ship run at all (CLAUDE.md §0.2); a setting whose source names no target reading is BLOCKED |
| A-63's occupancy throughput (the 62-of-87 baseline counts acts *about* a person, not meetings: 32 of 50 by the counterparty column, `audits/28_SCENE_ACCESS.md` §0) | B28's own measurement before it ships | the scene-access rows |
| a season's cost (A-44's cast roughly doubles it); every v12 batch's runtime (`V12_STRUCTURE.md` §2.4: a formula, not a measurement) | B00–B02 record their measured wall time | the schedule's makespan |

**5.2 Content owed (authored values; each is Jordan's or a content pass he corrects).**

| content | carrier and batch | what it blocks |
|---|---|---|
| **the ages table**: the 46 cast persons' ages, and `majority_age` (A-15, A-75) | B37 (content) | natural death and births; succession, vacancy and inheritance reached in play (F-FA-02's turnover through death) |
| **the cast's values**: the five tables of `IS-A-11` (stage 1 drafting in B04, stage 2 in **BA1**); authored attributes and skill scores; per-task difficulties (lane A measured the obstacle at 2.0 in 998 of 1,106 rolls because every person holds the default score 2, `unified/OWED_TO_UNIFICATION.md` §E); manner offsets (A-108); the 46 opinion rows of `31_WR_A` and `30_WR_G`'s three opinion rows (caste, militarism, royal order: content given by A-87 to A-91, the names and any new strain still owed) | BA1; B38 | R-06, R-08, R-09.b (BA1's rows); R-06.e at B39; the regimes in play |
| **the name lists and texts** of procedural generation (`21_PROCEDURAL_E_names_and_texts`) | B39 | the generated cast and world (A-44, A-50) |
| **the ducal homes**: where three Hafenmark and three Varfell seats' `rung:` anchors sit (`{duchy: …}` to a territory: T8 for Hafenmark, T12 for Varfell), marked `[ASSUMPTION: the ducal seat's territory]` (`master/workplan_v12/workplan_v12_part15.md:94`) | B21 | the seats' reach under a ducal anchor |
| **authored scores and difficulties** for the duel's persons (`03_PC_person_inputs_content`) | B18 | the standalone duel's content |
| what an army carries back: the shares of dead, injured, fled, captured and deserted, and the recovery rate (A-69, A-78; the dead-to-wounded ratio is not established in the tree's research) | B22, then B98 | the returning army's numbers |
| the surface pins (`16_PESSIMIST_GO_surface_pins`) | B41 | the port's surface parity |

**5.3 Files and claims not read, or not verifiable.**

- **Audits 24 to 31 have no closure rows**, and 162 live proposals have no closure row naming them (`unified/U6_VERDICT_AND_REPAIRS.md`, "Not checked by the verdict"). Their findings reach v12 through their own proposals and the rulings.
- **225 `[UNVERIFIED]` lines** remain outside the institutions family (`audits/25_GROUNDING_ENGINE.md` §6), in nine groups (§5 U-01 to U-09): causes not traced in a run, behaviours over more seasons than any lane was allowed to run, a test's behaviour (no lane ran pytest), WITNESS's deposit rules (sixteen proposals ask `loop/witness.py:537-700` one question), and about sixty loader or gate shapes a proposal hopes for, each with its stated fallback; 55 more in the institutions family.
- **Not opened by the closure lanes:** the test digests' per-entry bodies (about 305), the census's false-positive rows (tallied), most proposals below their heads (`OWED_TO_UNIFICATION.md` §C); about 275 proposals unopened by the unification verdict.
- **The INCOMPLETE proposals: 82** (39 waiting on a v11 position, 23 needing a design pass, 15 content, 12 with a dependency no file carries, 7 a site not located; `U6` row 1, after repair lane R-B); 211 COMPLETE is an upper bound. In v12 their missing parts are design items, content items or BLOCKED items with owners (D-18, D-19).
- **Unlocated:** the 2026-07-08 directive A-60 narrows (leads unopened: `registers/editorial_ledger_mb_archive.jsonl` rows ED-MB-0004 to -0007 and ED-MB-0041; `proposals/04_MB_cr12_linear_law.md:40-43`); the carrier of the game reader of `write_matrix.yaml:375-381` (`V12_STRUCTURE_part3.md` §11), whose dependents are BLOCKED until an author finds one.
- **Research still memory-grade** (`OWED_TO_UNIFICATION.md` §C): mass-battle history rests on two fully read sources and does not establish pre-1700 foot pace, formation-change times, bout length, break threshold, the dead-to-wounded ratio, the desert-to-regroup proportion or a second weapon's cost.
- **Implementation lane A's two commits** (`e5d6ab9`, `c5bf18a`) are unmerged; B01 rebases them (A-93). Their residues: an accepted challenge is never used up; `ob_terms` ride the roll's in-memory result, not the log; a plain `fight` still kills every time (`OWED_TO_UNIFICATION.md` §E).
- **This file**: the extract's severity parse found no grade for 77 of the 439 rows whose id is an `F-` finding (26 CORE, 17 PC, 13 FI, the rest scattered); their grade is in the audit's prose, printed **—** here.

**5.4 Blocked entries** (each waits on something outside the tree's reach; `V12_STRUCTURE_part3.md` §8.2): CR-07 with H-89 (`off_npc_084`'s rung is content), H-191, H-198 with M9 (the deed lie), the B10-16 gates entry (SE), CP-T08-07, H-325 with H-326 (A-109's design), TL-B6.n, GO-06 and H-5 (a `valoria-game` checkout).

---

## 6. The Layer 1 amendments

Jordan's A-97 (*"Layer 1: make amendments as required"*) applied every amendment the rulings owe, both halves of each (the PART B/C sentence and its PART D twin), each marked in place with its node id (`unified/U3_LAYER1_AMENDMENTS.md`; the applied text in `unified/work/L1_APPLIED.md`). `grep -c "L1-A"` reads 46 marks in `architecture/meta/04_CODE_ARCHITECTURE.md` and 16 in `architecture/holonic_ARCHITECTURE.md` at this HEAD; the three ledger ids exist in `registers/editorial_ledger_in.jsonl`.

| node | ruling | where (as the ledger records it) | ledger id |
|---|---|---|---|
| `L1-A3` | a field returns an end state | `04:777`, `:786`, `:182`, rows 24, 30; `hol:1407` | ED-IN-0358 |
| `L1-A4` | a person-supplied decider is a declared adapter input | `04:182`, row 22; `hol:1684` | ED-IN-0358 |
| `L1-A72` | nesting cap 1, as data | row 19 `04:1045`; `hol:1396` | ED-IN-0358 |
| `L1-A9` | a scene is a short sequence | `04:662`, rows 29, 36, 41a, F.26; `hol:974`, `:1125` | ED-IN-0358 |
| `L1-A64` | precedence of access by rung, a keyed draw | row 36 `04:1065`, F.26; `hol:974`, `:1166` | ED-IN-0358 |
| `L1-A12` | a seat carries a modifier | `04:331`, `:332`, `:351`, row 33; `hol:430` | ED-IN-0358 |
| `L1-A13` | three optional seat facts | `04:331` | ED-IN-0358 |
| `L1-A20` | war lives in the seats that wage it | `04:460`, row 48, F.32 | ED-IN-0358 |
| `L1-A29` | declared floats (the float contract) | PART E step 13, `04:1131` | ED-IN-0358 |
| `L1-A30` | one draw per key | `04:927`, rejection 4, row 35 | ED-IN-0358 |
| `L1-A62` | a refusal's receipt (the budget is a Query) | row 51 `04:1081` | ED-IN-0358 |
| `L1-A92` | evidence enters a conviction only as a term in the person's own drawn act | `04:251`, row 18; `hol:122`, `:362` | ED-IN-0358 |
| `L1-A96`, `L1-A96b` | the engine-formed `capture` on a failed attempt; the `detention` basis | `04:177`, `:654`, rows 1, 41, new row 52; `04:619`, row 10a | ED-IN-0358 |
| `L1-A102` | the tenth module, `boot/` | `04:127`, `:156`, `:183`, `:1010`, row 46, new row 53, F.31; `hol:1739`, `:1797` | ED-IN-0359 |
| `L1-A104` | a `Scene` carrying only management orders costs 0 | `04:449`, row 51 | ED-IN-0360 |
| `L1-A105` | a grant reduction is a revocation | `04:605`, row 10a | ED-IN-0360 |
| `L1-A107`, `L1-A108` | `Person.traits`, `Person.manner_offset?` | `04:235`, mark `:241` | ED-IN-0360 |
| `L1-A22`, `L1-A85`, `L1-A77`, `L1-A24` | ledger rows superseded (ED-IN-0256 (4) command; ED-IN-0352 (3) strife exception; ED-MB-0016 multiplier at zero; ED-IN-0261 "rolls nothing") | superseding rows in the IN and MB ledgers | ED-IN-0358 |

**Still owed or held** (none is Layer 1 that a batch is gated on: `U3` §1.4, "all APPLIED, no batch is gated on one"):

| node | what | why held | its text |
|---|---|---|---|
| `L1-A17` (REF) | canon lines 76, 90, 96 and the Coup Counter wording | canon changes only by Jordan's amendment; no v12 item edits canon | `audits/15_INSTITUTIONS_SYNTHESIS.md` §4.6, A1–A4 |
| `L1-A84` (REF) | five sentences of the ratified strife master (ED-IN-0316) | a ratified design document; B38 builds the era, the master's text waits | `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` §6 |
| `L1-A60` (REF) | the 2026-07-08 directive's words on numbers in the melee dice | its sentence was not located by any lane | — |
| `L1-A26` (CODE) | `degree_from_net`'s docstring states the half-score rule | rewritten in B05, not left as a second statement | — |
| — | Layer 1's word "round" for the lap (`04:1065` row 36; `hol:1166`), and "exchange" at `03:126` | a word, not a rule; the code is renamed (PCR-4), Layer 1 is not edited to match | `unified/work/L1_FURTHER.md` |
| — | the identifier `capability` (a second name for skill) and the Tenure "edge" | Layer 1 names both; a rename is Jordan's amendment and an encoding mover (D-06) | `unified/U1_GLOSSARY.md` §H |
| — | CLAUDE.md §3's sentence on the `pc_engine` path seam | B13 deletes the seam; edited in B13's commit, named in its PR | D-09 |

---

## 7. What workplan v11 and the gap register carried, and what was retired

From `master/V11_EVALUATION.md` §1 and `master/GAP_REGISTER_EVALUATION.md` §1 (each counted by script from the lanes' tables). Every position of v11 (`_part1` to `_part17`) and every row of `engine/season/hole_register.yaml` (352 rows) has one settled disposition.

| deliverable | rows | DONE-IN-CODE | SUPERSEDED | WRONG | STILL-NEEDED | MISSING-DEP | RULED-CONFLICT |
|---|---|---|---|---|---|---|---|
| workplan v11 (lanes E1–E5), settled | 1,692 | 693 | 350 | 67 | 565 | 17 | 0 |
| gap register (lanes E6–E8), settled | 360 | 150 | 157 | 4 | 44 | 5 | 0 |
| **both** | **2,052** | **843** | **507** | **71** | **609** | **22** | **0** |

The 631 carried rows collapse to **273 v12 intake items** (`master/eval/V12_INTAKE.md`: 264 STILL-NEEDED, 9 MISSING-DEP; 22 are head rules, 54 held until a named trigger fires). Retired items do not enter v12 in any form; each has its reason in the ledgers (`V11_EVALUATION_part2.md`, `GAP_REGISTER_EVALUATION_part2.md`). **Errors in v11 the evaluation verified** (`V11_EVALUATION.md` §6): part 12's batch column is stale; ED-MB-0070 and -0071 cite deleted closing tests; two LEAVE triggers have fired (ED-SC-0001, carried in B15; ED-1043, at MBA-04 step 0 in B19); `modules/mass_battle/core/state.py:26,28` and `core/exchange.py:46` cite a forked file as canonical (a B03 comment fix). Workplan v11 is retired by v12's adopting commit (`V12_STRUCTURE_part3.md` §8.1), which is Jordan's.

---

## 8. What is not resolved

- **DISPUTED (9 rows)** — each stays in its document, marked. The two verb rows (U5b S1, U5c D-1) are the same refutation, G-01: a band-keyed `writes:` on a route row does not load (`engine/season/data/verbs.py:848-851`, `:872-876`); the draw stands and the band map's form is what changes. Three FI and SC rows dispute an audit's reading on the lane's own evidence (U5c R-04, R-26: Layer 1 is not edited to match `loop/witness`; cell 5 and R-4 of the contest interrogation). F-SE-15 (a season's cost grew with the tick) is a load-confounded reading with no cause named. The institutions row L-4 (four readers that read the World to hand a person a referent, graded CONVENTION). The determinism row on `world_q.subsistence_d…` (two readings recorded, the function unopened). Rows: `U5a`, `U5b:478`, `U5c:174`, `:184`, `:258`, `:280`, `:494`, `U5d:226`, `:766`, `:819` (the determinism and SE rows counted once each).
- **JORDAN (7 rows), every one since answered:** J-U5a-03 (a refusal's receipt, three rows) by A-62; D-34 (luck in battle) by A-59 and A-77; D-62 (the scene slate) by A-48; J-1 (named births) by A-75; A-68's "parliament is functional" by A-76.
- **For Jordan now:** nothing survives the ladder (`V12_STRUCTURE.md` §1, "Nothing survives the ladder for Jordan"; `master/eval/EVAL_FOR_JORDAN.md` holds no open question). What waits on him is v12's adoption and the held-back list of `V12_STRUCTURE_part3.md` §8.2: the canon rewordings (A-17), the strife master's five sentences (A-84), A-60's unlocated directive, Layer 1's "round", the identifier `capability` and Tenure "edge", every authored value (§5.2), the nine blocked entries (§5.4), the 54 held entries, the CI cadence of a parallel step, and the record that the design and instruction documents were written by Fable at his direction.

---

## 9. How to read the suite, v12 and this file together

1. **Start here, §1**: the verdict and the readings. Then §3 (the forty) to see what is worst, and §4 to see what was decided about it.
2. **For one finding**: find its row in §10 (`_part3` onward, by subsystem); its evidence cell names the closure row (`U5a:66`) and the audit line (`01_CORE_audit.md:206`); open the audit section for the argument and the closure row for the disposition; its carrier names the proposal under `proposals/` whose head gives `Lands in batch:` and whose `Exact edits` hold the instruction.
3. **For the work**: v12 (`master/workplan_v12/`), whose structure is `V12_STRUCTURE.md` (§2 the 61 batches, §3 the milestones M0 to M5 and the requirement map) and whose items copy the proposals' edits; the batch cell of a row here is the handle to search for in v12's parts. v12 orders; this file does not.
4. **For a ruling**: `unified/DECISIONS_ANSWERED.md` (A-1 to A-114) governs every lane document; a proposal built on the other answer carries a `Reconciled:` head line.
5. **For the suite's own index**: `README.md` (its §3 reading order; its counts are U4's, re-run them rather than trust them); `audits/25_GROUNDING_ENGINE.md` settles what the suite claims about the engine.
6. **What nothing here is**: canon, a mechanism, or done. Done means the behaviour executes (CLAUDE.md §0.2); the only executions in this file are the readings of §1.1, and the nine move only at B99.
