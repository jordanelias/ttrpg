# Attribute derivation: what each practice, verb and subsystem demands of a person, and which of those demands should be attributes

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. It recommends a set of primaries and two alternatives; the choice is Jordan's.
## Lane: IN (cross-cutting), with PC, MB, SC, FI, WR, SE, FA, NPC as sources. IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions possible).
## Parts, in reading order: this file (words, §1 the evidence: demands, ingredients, source formulas, learned skills, sourced uses, the command) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§2–§5, the interrogation: practice domains, verbs, subsystems) · [`_part3`](2026-10-16-attribute-derivation_part3.md) (§6–§13: principles, candidate pool, selection, coverage, the one grouping, NERS, limits, both critic reconciliations). The recommended set with what hangs off each primary: [`_aptitudes`](2026-10-16-attribute-derivation_aptitudes.md). The word study: [`_equivalences`](2026-10-16-attribute-derivation_equivalences.md).

**What this answers.** Jordan, 2026-10-16: *"perform interrogation of each 'PRA' to identify what kind
of skills/aptitudes are required for each. after doing so, we are to flatten our list and collate all
of these together to see what should be an attribute."* Then: *"like our VERB interrogation is
supposed to be doing this too"*; *"ie WHAT does each verb/subsystem require"*; *"show me the flattened
aptitude list when it's done. we will work from those to think about attributes we have."* After the
first critic pass: *"Learned skills and derived scores etc all need to be folded in to this."* During
this pass: ***"ANY of these can be an attribute. ignore all prior rulings for this exercise"***, and
***"there are no derived scores when we don't even know our primaries."***

So the work runs in this order, and nothing is called *derived* until the primaries are chosen:

| step | what | where |
|---|---|---|
| **1. DEMANDS** | what each practice, verb and subsystem demands of a person; 46 demands, each marked by what kind of thing it is, independent of any attribute roster; every formula the sources compute, with the ingredients the source uses today, as history | `_part2` §2–§5; this file §1 |
| **2. CANDIDATE POOL** | every demand, every formula, every ingredient a formula names, every learned skill | `_part3` §7.1 |
| **3. SELECT PRIMARIES** | by principles derived from the evidence and stated before they are applied | `_part3` §6, §7.2 |
| **4. RELATIVE TO THE SELECTION** | each demand and each source formula is classified against the chosen set: expressed by a formula over the primaries (only now *derived*), a learned skill sitting on a primary, a resource or track, or **UNCOVERED**. Coverage is the main test of a set, run on the recommendation and two alternatives | `_part3` §7.3–§7.5 |
| **5. THE RESOLVER** | the pool, odds, obstacle or gate an act is settled by | the sources |

---

## Words

**Demand**: something an act or a subsystem asks of a person, named by one of the 46 words the first
pass collected (the *term*). Each is marked as exactly one **kind**, a statement about the thing and
not about any roster:

- **CAPACITY**: something a person carries that varies between persons and that no source computes by
  formula (`strength`, `observation`, `memory`).
- **COMPUTED QUANTITY**: something the sources compute by a formula they write down; the formula and
  the ingredients the source uses **today** are recorded as history (`stamina`: the source computes
  `3·Endurance + 2·Spirit`). It is not called derived: the ingredients themselves are in question.
- **PRACTICE**: a learned skill that grows by use (`numeracy`, `land-sense`).
- **LIMIT**: a cap on how much a person can hold (`breadth`).
- **TEMPERAMENT**: a lean, not a capacity (`boldness`).
- **RESOURCE / TRACK**: a quantity that changes in play (a stamina pool's current level, Coherence,
  Truth). No demand is of this kind; several source formulas compute the maximum of one.

**Ingredient**: a quantity a source names inside a roll, a check, a gate or a formula: Agility, Spirit,
Thread Sensitivity, `resilience`, BODY, `disp`. Every ingredient is a candidate primary; so is every
demand and every formula. **Primary**: a quantity chosen, in `_part3` §7, to be carried as an
attribute. **Derived**: only after selection, a quantity a stated formula computes from the chosen
primaries.

**What the tree currently says, recorded as history and applied as no constraint here.** The registry
holds nine attributes and leaves a ruled tenth unnamed (`references/descriptor_registry.yaml:30-48`;
ED-IN-0185, ED-IN-0193). J-13 records *"It's a derived score … not a character attribute in and of
itself"* and *"pool only it is"* (`workplans/valoria_master_workplan_v9_part5.md:433`). The 2026-09-05
ruling says *"ignore their use of attributes"* (`04_VERBS.md:465-466`), and its gloss reaches the
inquiry acts (`:473-476`). V-2 and V-3 let an attribute reach a verb only through a faculty and only
on a `contests:` row (`10_verbs_and_attributes.md:198-199`). K-3 gates `thread_read` on TS. Code
says *"BALANCE is NOT a stat (Jordan)"* (`modules/combat/combat_systems.py:185`). ID-13 says a field
needs a reader; **it is used here as a quality criterion** (an attribute nothing reads is useless),
never as a ruling that excludes. **Jordan, 2026-10-16: *"ignore all prior rulings for this
exercise."*** None of the above excludes a candidate below, and the number of attributes is open.

- ⚠ **Why not "aptitude".** The tree uses that word in three other senses: a learned skill
  (`modules/combat/core.py:106-107`; `faction_politics_v30.md:541`); an attribute input (V-3's
  *"aptitude slot"*, `10_verbs_and_attributes.md:199`; *"how aptitude enters today"*, `:140`); and a
  progression slot, *"Aptitude (rate/price, never rolled)"*
  (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:1288`). *Demand* is the plain
  word; the code's `str_demand` (a weapon's demand on Strength, `combat_systems.py:174-176`) uses it
  in the same sense. The file `_aptitudes.md` keeps its name for continuity only.
- It avoids "axis" (the engine's `AXES`), "capacity" as a type name outside the kinds above,
  "Retention" (`04_VERBS.md:455`; `rosters.yaml:2002`) and "equivalence class" (`_part3` §8.1).
- Codes STR AGI END FOC ACU WIL ATT CHA BON are the registry's names for today's ingredients; REC, TS,
  RES, TMP and KIT are the character template's (`proposals/2026-10-16-character-template_part2.md:34-57`);
  BODY is `Person.body` (`engine/season/state/carriers.py:667`).

**The evidence grammar.** A **draw** is one item (a practice domain, a verb or a subsystem, `_part2`)
demanding one term, written `` `term` (roles, [key] basis: …) ``.

- **Roles**: odds, difficulty/cost, eligibility, effect size, resists another; several may be joined
  by ` + `. ⚠ **A role carries no magnitude.**
- **A key is one source statement, or one inference.** §1.5 counts **distinct statements** per term,
  once however many items draw on it, at its best basis. Draw entries re-count by construction.

**Evidence tiers** (the character template's). **T1**: code the season loop runs on a per-person
value. **T2**: code outside the loop, or loop-run code on a class default. **T3**: a ratified
specification, a v9 plan position, or a proposal recorded as RATIFIED AS INTENT. **T4**: design
intent only. Under `CLAUDE.md` §0.05 no design document shows a behaviour is correct; **the sources
are cited for what a design says an act DEMANDS.**

- ⚠ **T1 is not empty.** The season loop builds each fighter from one per-person number, `end`,
  computed from BODY as `max(1, 4 − body bands)` (`engine/season/seam/wrappers/combat.py:130-138`;
  `engine/season/queries/inputs.py:51`). That number drives the stamina reserve, the Wound Interval,
  Max Wounds and Health in the fight the loop runs; every other Combatant field is the class default.
  So `stamina` and `toughness` are NAMED at T1 (F13).
- **NAMED (Tn)**: the source states the demand.
- **overridden**: named at T4, and today's code or the tree's reading does not read it for DICE. Three
  causes: **the kernel** (the T2 contest kernel binds `faculty` and `charisma`, `resolver.py:184-195`,
  and `charisma` sets only Face's outcome-inert ceiling, `:226-236`); **the 2026-09-05 gloss**
  (contestable, `_part2` §3 note 1); **the T3 row** (`conceal` has no roll, #52). **The tags record
  the tree; the selection (`_part3` §7) counts an overridden statement as a source statement**, and
  shows it apart from the named ones.
- **INFERRED**: this proposal's reasoning. Where a source names only an ingredient or a formula and
  not the function, the choice of term is INFERRED; the ingredient or formula is still NAMED in §1.2
  or §1.4. That is why the four uses of Command are INFERRED as terms and Command is NAMED T2 (F18).

**Abbreviated sources** (each opened in this pass unless tagged): **FW**
`.designs/systems/fieldwork/reference/fieldwork_v30.md` · **SCV**
`.designs/systems/social_contest/reference/social_contest_v30.md` · **HIST**
`.designs/systems/characters/reference/character_histories_v30.md` · **MB**
`.designs/systems/mass_battle/reference/mass_battle_v30.md` · **AUG**
`proposals/2026-08-15-character-and-faction-stats-and-progression.md`. Also cited by bare filename, all
under `.designs/systems/`: `derived_stats_v30.md`, `threadwork_v30.md`, `faction_politics_v30.md`,
`factions_personal_v30.md`, `ci_political_v30.md`, `npc_behavior_v30.md`, `investigation_systems_v30.md`,
`npc_relational_graph_v30.md`, `southernmost_v30.md`, `miraculous_event_v30.md`,
`solmund_master_document.md`, `conviction_track_v1.md`, `knots_v30.md`, `combat_reference_v1.md`,
`fieldwork_v30_infill.md`, `military_layer_v30.md`, `settlement_layer_v30.md`,
`governance_play_redesign_v1.md` and `valoria_ui_ux_v4_1.md`. Code: `combat_systems.py`,
`combatant.py`, `core.py`, `config.py` (all `modules/combat/`); `modules/mass_battle/core/exchange.py`;
`modules/mass_battle/orchestration.py`; `modules/mass_battle/hierarchy/units.py`;
`systems/social_contest/sim/contest/resolver.py`; `systems/threadwork/sim/operations.py`;
`systems/fieldwork/sim/knots.py`; `engine/season/seam/wrappers/combat.py`. Tagged *not opened*:
`combat_c4_draft_v0.md:127` (grep only).

**How the verb interrogation differs from the character template's matrix.** The template asks what a
resolver READS off a person (43 of 65 verbs read nothing, true of the code). This proposal asks what
performing the act well DEMANDS of the person when complete. Twelve of the template's zero rows carry
demands here (`_part2` §4); every template read stays in `_part2`'s *resolver* column.

**Method, and fan-out.** One producer, no subagent spawned in any pass. Every table feeds the next
(the evidence keys feed §1.5; the formula, skill and use tables feed the selection and its coverage
test), so the reading cannot be shared out without the verdict travelling with it; a second producer
would buy independence on the selection, which the relay buys more cheaply with the critic stage and
the divergence test scheduled after this correction. An independent Opus critic has read the first two
passes; both reconciliations are tables at the end of `_part3`.

---

## 1. THE EVIDENCE

### 1.1 The ingredients the sources use today (history, not a roster)

| C | code | ingredient | where the tree holds it today | scale | what the tree does with it today |
|---|---|---|---|---|---|
| C01 | `STR` | Strength | registry :37; `Combatant.strength` (combatant.py:96) | 1–7 | a registry attribute |
| C02 | `AGI` | Agility (alias Dexterity) | registry :39; `Combatant.agi` (:96) | 1–7 | a registry attribute |
| C03 | `END` | Endurance (alias Vitality) | registry :38; `Combatant.end` (:96); on the season path computed from BODY (F13) | 1–7 | a registry attribute |
| C04 | `FOC` | Focus | registry :41; `Combatant.focus` (:97) | 1–7 | a registry attribute |
| C05 | `ACU` | Acuity (aliases Reasoning, Cognition: *"[ASSUMPTION] … Jordan veto"*) | registry :42; `Combatant.cog` (:97); `derive_command(cognition)` | 1–7 | a registry attribute |
| C06 | `WIL` | Will (alias Spirit) | registry :43; `Combatant.spirit` (:97); the thread and knot actors' `spirit` | 1–7 | a registry attribute |
| C07 | `ATT` | Attunement (alias Perception) | registry :45; `Combatant.att` (:97) | 1–7 | a registry attribute |
| C08 | `CHA` | Charisma (alias Presence) | registry :47; `derive_command(charisma)`; the contest spec's `charisma` | 1–7 | a registry attribute |
| C09 | `BON` | Bonds (aliases Sincerity, Affability) | registry :48; the knot actor's `bonds` | 1–7 | a registry attribute |
| C10 | `REC` | Recall | **not in the registry; no code field**: `git grep -i recall -- '*.py'` finds only Command's recall roll and the contest's per-source citation count; rolled in designs (FW:95, :306; SCV:155; threadwork_v30:688) | 1–7 (HIST:517) | a design ingredient only |
| C11 | `TS` | Thread Sensitivity | registry :64 (a practitioner stat); the thread and knot actors' `ts`; a Track that **grows** by exposure (derived_stats_v30:578; HIST:127, :324; FW:254) | 0–100+ | its own field |
| C12 | `RES` | resilience | a duck-typed slot the thread module reads, *"a placeholder"* at gain 0 (operations.py:142-147, :264-275); canon: *"how resilient their spirit is"* (:144) | int ≥ 0 | a dark stub slot |
| C13 | `BODY` | the body's condition | `Person.body` (carriers.py:667), the season loop's one personal state | condition scale | a state the loop carries |
| C14 | `TMP` | temperament | `Combatant.disp` (combatant.py:99), *"disposition / temperament, aggression axis"*, neutral at 4 | 1–7 | a combat field |

**Also carried by a person, and in the pool in `_part3` §7.1:** History and every other learned skill
(§1.3); KIT, what a person carries (weapon heft, armour; `core.py:560-571`, threadwork_v30:82);
Disposition, a relational state per NPC (`knots.py:189-193`; derived_stats_v30:398); the Coherence
and Truth tracks and Inspiration (derived_stats_v30:172-179, :575-578).

### 1.2 The formulas the sources compute (each re-opened; formula and ingredients as the source writes them today)

*What it is* says what the formula's output is, independent of any roster. *Demands* are the §1.5
terms it carries.

| F | quantity | formula as the source writes it | ingredients the source uses | what it is | basis | locator | demands |
|---|---|---|---|---|---|---|---|
| F01 | Tempo | `BASE + K·(AGI − 4) − penalties`, × (1 − K·fatigue) × poise | `AGI` | a rate | NAMED T2 | combat_systems.py:113-116 | quickness |
| F02 | Reflex | `(2·AGI + 1·ATT) / 3` (REFLEX_AGI 2.0, REFLEX_ATT 1.0, config.py:122) | `AGI` `ATT` | a score | NAMED T2 | combat_systems.py:172 | reflexes |
| F03 | Balance | `(½AGI + ½STR − 1 + skill('balance'))` × fatigue × poise | `AGI` `STR` | a score | NAMED T2 | combat_systems.py:184-188 | balance |
| F04 | Initiative emphasis | `K·ΔAGI + K·ΔReading + K·ΔHistory`, × the tempo channel | `AGI` `ACU` `ATT` | a σ term | NAMED T2 | combat_systems.py:1416-1421 | quickness, anticipation |
| F05 | Counter success | `base + K·(History − 3) + K·(Reflex − 3) + ability`, bounded | `AGI` `ATT` | a probability | NAMED T2 | combat_systems.py:1438-1444 | reflexes |
| F06 | Reading | `(2·ACU + ATT)/3 + K·(History − 3)` | `ACU` `ATT` | a score | NAMED T2 | combat_systems.py:171 | anticipation |
| F07 | Impact | `STR + heft` | `STR` | an effect size | NAMED T2 | core.py:560-571 | strength |
| F08 | Handling penalty | `K·max(0, weapon's strength demand − STR) + K·fatigue` | `STR` | a penalty | NAMED T2 | combat_systems.py:174-179 | strength |
| F09 | Bind and wind Strength term | `K·(STR_a − STR_d)` in the bind; `(strength − opponent's)` in the wind | `STR` | a σ term | NAMED T2 | combat_systems.py:1062; :349 | strength |
| F10 | Durability | `WI = round(END + 4 + 0.4·WIL)`; `MW = min(⌊END/2⌋ + 1, 3)`; `Health = round(WI·(MW + 1) + 0.25·STR·END)` (the WIL and STR terms labelled noise, combatant.py:20-21) | `END` `WIL` `STR` | a resource's maximum | NAMED T1 | combatant.py:20-42; derived_stats_v30:73-75 | toughness |
| F11 | Stamina reserve | `3·END + 2·WIL` | `END` `WIL` | a resource's maximum | NAMED T1 | combatant.py:45-47; derived_stats_v30:106 | stamina |
| F12 | Take a Breath | `(END + combat History) × 2`, capped at the reserve | `END` | a refill | NAMED T4 | derived_stats_v30:110 | stamina |
| F13 | Season `end` | `max(1, 4 − body bands)` | `BODY` | an input the loop computes | NAMED T1 | engine/season/seam/wrappers/combat.py:130-138; engine/season/queries/inputs.py:51 | stamina, toughness |
| F14 | Concentration tracker | `3·FOC + 2·WIL`; sets consistency and mental fatigue in combat; depletes per exchange in the contest | `FOC` `WIL` | a resource's maximum | NAMED T2 | combatant.py:147; combat_systems.py:1423-1431; derived_stats_v30:159; SCV:267 | concentration |
| F15 | Disruption resistance | `logistic(K·(FOC − 3))` | `FOC` | a probability | NAMED T2 | combat_systems.py:1449-1452 | concentration |
| F16 | Poise regathering | `poise + R·(1 + K·(FOC − 3))·(1 − poise)` | `FOC` | a rate | NAMED T2 | combat_systems.py:1433-1436 | concentration |
| F17 | Disposition lean | `(TMP − 4)/3` | `TMP` | a lean | NAMED T2 | combat_systems.py:180-182 | boldness |
| F18 | Command | `clamp(round((2·CHA + ACU)/3), 1, 7)`; rolled for the span of control (MB:309), the recall (orchestration.py:2585-2590), feint recognition (:2593-2599), tactic execution (MB:312), troop Discipline and Morale start (MB:209-210, :230), re-establishing command (MB:343-344); `Officer.command` also accepts a given value (units.py:2700-2722) | `CHA` `ACU` | a score | NAMED T2 | exchange.py:57-66; MB:306 | leadership, tactical-read, situational-awareness |
| F19 | Resolution pool | `max(5, History + 6)` | — | a pool | NAMED T2 | core.py:54-56 | — |
| F20 | Focus defence | `⌊FOC/2⌋ × 3` strain absorbed | `FOC` | an absorption | NAMED T4, overridden for dice by the kernel | SCV:199; derived_stats_v30:149 | concentration |
| F21 | Charisma strain modifier | `max(0, ⌊(CHA − 3)/2⌋) × 3` strain dealt | `CHA` | an effect size | NAMED T4, overridden for dice by the kernel | SCV:198; derived_stats_v30:148 | presence |
| F22 | Face | `Face_max = CHA × 3`; `Face_current = round(Standing/10 × Face_max)`; moves no outcome | `CHA` | a resource view | NAMED T2 | resolver.py:226-236; SCV:247 | presence |
| F23 | Standing, Rank, Credit, Reserve | the kernel's trackers, from the spec (`standing_start`, `reserve_max`) and built by ethos | — | resources | NAMED T2 | resolver.py:202-215 | — |
| F24 | Composure | `CHA × 3` (earlier `Cha + 6`); retired as the contest tracker by CR3, still charged by threadwork | `CHA` | a resource's maximum | NAMED T4 | derived_stats_v30:136-140, :554; SCV:242-247; threadwork_v30:177 | concentration (by the merge, §1.5) |
| F25 | Appraise pool | `ATT + REC` | `ATT` `REC` | a pool | NAMED T4, overridden for dice by the kernel | SCV:155, :511 | reading-people, memory |
| F26 | Appraise Ob | `⌈opponent's CHA ÷ 2⌉`, min 1 | `CHA` | an obstacle | NAMED T4, overridden for dice by the kernel | SCV:155 | presence |
| F27 | Impress Ob | `⌊NPC's ACU ÷ 2⌋ + 1` | `ACU` | an obstacle | NAMED T4 | FW:411 | reasoning |
| F28 | Cover | `ACU + most relevant History`; sets Exposure thresholds | `ACU` | a threshold | NAMED T4 | FW:575-577 | reasoning |
| F29 | Resolve / Inspiration cap | `WIL × 1` | `WIL` | a cap | NAMED T4 | derived_stats_v30:178, :557 | devotion |
| F30 | Thread Fatigue threshold | `WIL × 5`; meditation clears it by WIL | `WIL` | a threshold | NAMED T4 | threadwork_v30:195, :203; derived_stats_v30:239 | contact-endurance |
| F31 | Operations per contact | `FOC − 1` | `FOC` | a cap | NAMED T4 | threadwork_v30:199; derived_stats_v30:258-266 | concentration |
| F32 | Thread pool | `2·WIL + min(3, History + 3) + ⌊TS/10⌋` (also the Thread-Read pool, FW:305) | `WIL` `TS` | a pool | NAMED T2 | operations.py:235-247; threadwork_v30:163 | will, thread-sensitivity |
| F33 | Thread Pool Score | `⌊TS/10⌋` | `TS` | a pool term | NAMED T2 | registry :65; operations.py:244 | thread-sensitivity |
| F34 | Coherence-cost resistance | `RESILIENCE_GAIN × RES` toward zero; the identity at the shipped gain 0 | `RES` | a resistance | NAMED T2 | operations.py:249-275 | self-coherence |
| F35 | Dissolution Ob on a person | `END + WIL + armour` | `END` `WIL` | an obstacle | NAMED T4 | threadwork_v30:82 | toughness |
| F36 | Knot cap | `⌊BON/2⌋ + 1` | `BON` | a cap | NAMED T2 | knots.py:201-203 | relational-depth |
| F37 | Effective Recall | `REC − 1` (Fragmented), `REC − 2` (Fractured, Severed) | `REC` | a modifier | NAMED T4 | HIST:36 | breadth |
| F38 | Spark bonus and spark check | `⌊REC/2⌋` dice on spark checks; the check is `WIL + ⌊REC/2⌋` | `REC` `WIL` | a pool | NAMED T4 | HIST:35, :41 | learning |
| F39 | Equip slots | set by REC; `REC ≥ 5` equips all | `REC` | a limit | NAMED T4 | HIST:517, :521 | breadth |
| F40 | Practice depth ceiling | the *"skill depth ceiling"*; History points *"per Recall cap per History"* | `REC` | a limit | NAMED T4 | HIST:517, :522 | practice-ceiling |
| F41 | Negotiate Ob | `⌊NPC's highest relevant stat ÷ 2⌋ + 1`; the ingredient is not named | — | an obstacle | NAMED T4 | FW:413 | — |

**Checked and found to be single-ingredient rolls, not formulas** (one ingredient, the ×2 dice
convention, a practice addend): the knot formation roll, `spirit × 2 + history_relationships`
(knots.py:212-215); the Argue pool, `(Primary × 2) + History`, whose ingredient the adjudicator sets
(SCV:129-135); the Concealment pool, `Cognition × 2 + History` (FW:361). They are §1.4 rows. **Not
person-level:** army Morale (a unit quantity that rolls Command, derived_stats_v30:407) and every
faction meter (derived_stats_v30 §8).

### 1.3 Learned skills (practice): what grows by use, and what it enters

**How they are gained.** History is allocated at creation, *"per Recall cap per History"* (HIST:522).
A Histories skill is a starting skill (★, HIST:205) or on a History's spark list; it sparks after a
meaningful roll at Ob ≥ 2 on the spark check (F38, HIST:41); Level 2 needs History dice_bonus ≥ 3 and
Level 3 ≥ 5, each plus a spark (HIST:43). § and *unique* are the source's own marks, undefined in the
file. **The Histories rows are a sweep, not a sample:** every Histories skill whose effect text names
an ingredient, a pool or a formula, by the pattern in the command's comment.

| L | learned skill | how gained | where it enters | ingredients it enters on (as the source writes it) | basis | locator |
|---|---|---|---|---|---|---|
| L01 | combat History (`Combatant.history`) | allocated | the resolution pool (F19), Reading (F06), the counter (F05), initiative (F04), Take a Breath (F12) | `ACU` `ATT` `AGI` `END` | NAMED T2 | combatant.py:98; core.py:54-56 |
| L02 | thread History | allocated | the thread pool (F32), capped +3D | `WIL` `TS` | NAMED T2 | operations.py:238-246 |
| L03 | relationship History (`history_relationships`) | allocated | the knot formation roll (U22) | `WIL` | NAMED T2 | knots.py:213-214 |
| L04 | `capability` keys (`Person.capability`) | written by `train` where a case names a vocation (IN-12 step 9) | the sigma pool; reads no ingredient | — | NAMED T1 | carriers.py:651; rosters.yaml:1082-1107 |
| L05 | contest `faculty` | the spec | the kernel's pool and leverage | — | NAMED T2 | resolver.py:184-195, :300-301 |
| L06 | Combatant `skills` (bind, parry, dodge, balance, technique, grab) | set at build | Balance (F03); the dodge and wind σ | `AGI` `STR` | NAMED T2 | combatant.py:115; combat_systems.py:188, :1057-1060 |
| L07 | `equipped` techniques (`{name: level}`) | levels of investment (ED-PC-0023); AUG's Investment slot | channel ability factors, e.g. the counter (F05) | `AGI` `ATT` | NAMED T2 | combatant.py:116; combat_systems.py:1442; AUG:1285 |
| L08 | `tradition` (the school) | set at build | channel reweighting; familiarity scales the bind read (F06) | `ACU` `ATT` | NAMED T2 | combatant.py:101; combat_systems.py:1058-1061; AUG:168-176 |
| L09 | tactic cards | — | tactic execution, Command dice (MB:312) | `CHA` `ACU` | NAMED T4 | AUG:1285 (`tactic_cards = {}`) |
| L10 | Histories skill levels and sparking | the rule above | the acquisition of L11–L54, through the spark check (F38) | `WIL` `REC` | NAMED T4 | HIST:41, :43 |
| L11 | Border Vigilance | ★ unique | +1D on Cognition: ambush, enemy strength, terrain | `ACU` | NAMED T4 | HIST:177 |
| L12 | Seasons Reader | ★ § | +1D Cognition: weather, terrain, agriculture | `ACU` | NAMED T4 | HIST:314 |
| L13 | Weatherwise | § | a Cognition roll for an environmental modifier | `ACU` | NAMED T4 | HIST:333 |
| L14 | Eagle Eyes | ★ unique | a Cognition roll to reveal an element of the opposing Phase 1 | `ACU` | NAMED T4 | HIST:369 |
| L15 | Anomaly Recognition | ★ unique | +1D Cognition to assess a threadcut being | `ACU` | NAMED T4 | HIST:371 |
| L16 | Calamity Familiarity | § | +1D on Attunement rolls near the node | `ATT` | NAMED T4 | HIST:105, :128 |
| L17 | Wound Proximity | unique | +1D on Attunement rolls at node distance 1 | `ATT` | NAMED T4 | HIST:121 |
| L18 | Street Wisdom | § | +1D Attunement: danger, intentions | `ATT` | NAMED T4 | HIST:254 |
| L19 | Thread Perception | § | +1D Attunement to perceive Thread phenomena, at TS ≥ 30 | `ATT` `TS` | NAMED T4 | HIST:280 |
| L20 | Post-Leap Clarity | unique | +2D Attunement to perceive Thread phenomena | `ATT` | NAMED T4 | HIST:450 |
| L21 | Intuitive Threadwork | ★ unique | an Attunement + Spirit roll for minor Weaving, pre-Leap | `ATT` `WIL` | NAMED T4 | HIST:362 |
| L22 | Combat Reflexes | § | Attunement ties: act last regardless of the Agility tiebreaker | `ATT` `AGI` | NAMED T4 | HIST:463 |
| L23 | Institutional Instinct | § | +1D on Appraise (F25) | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | HIST:93 |
| L24 | Cathedral Raised | ★ unique | +1D to Appraise and Argue in Church settings | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | HIST:140 |
| L25 | Political Literacy | ★ unique | +1D on Appraise in a political context | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | HIST:228 |
| L26 | Silence Reader | § | Appraise at TN 6 in small groups | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | HIST:295 |
| L27 | Read the Room | ★ § | Appraise at TN 6 in formal settings | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | HIST:310 |
| L28 | Archive Access | § | +1D on Recall-based rolls researching records | `REC` | NAMED T4 | HIST:294 |
| L29 | Doctrinal Authority | ★ unique | +3D Recall bonus in the Memory genre on theology | `REC` | NAMED T4, overridden for dice by the kernel | HIST:320 |
| L30 | Obsessive Recall | unique | +1D on Recall about the witnessed event | `REC` | NAMED T4 | HIST:401 |
| L31 | Treaty Language | unique | +1D Recall on prior agreements | `REC` | NAMED T4 | HIST:381 |
| L32 | Trained Memory | § | *"Concentration (Focus + Recall) +2"*: a formula derived_stats_v30:166 removed | `FOC` | RETIRED | HIST:217 |
| L33 | Contemplative Focus | ★ unique | Focus +1 for Contact Duration: a rule threadwork_v30:199 retired | `FOC` | RETIRED | HIST:293 |
| L34 | Vaynard's Confidence | ★ unique | a Spirit roll for +1D on a Thread roll | `WIL` | NAMED T4 | HIST:342 |
| L35 | Deniable Action | ★ unique | a Spirit roll to deflect an evidence trail | `WIL` | NAMED T4 | HIST:370 |
| L36 | Invisible | § | +1D on Agility concealment in crowds | `AGI` | NAMED T4 | HIST:165 |
| L37 | Slippery | ★ § | Escape −1 Ob; +1D pursuit evasion (disengage rolls Agility, combat_reference_v1:598) | `AGI` | INFERRED | HIST:382 |
| L38 | Road Survival | § | +1D Endurance in unfamiliar territory | `END` | NAMED T4 | HIST:322 |
| L39 | Community Voice | § | +1D Argue before a Crowd; a Crowd sets Charisma (SCV:134) | `CHA` | NAMED T4, overridden for dice by the kernel | HIST:340 |
| L40 | Incendiary Rhetoric | ★ unique | +2D Argue before a Crowd | `CHA` | NAMED T4, overridden for dice by the kernel | HIST:360 |
| L41 | Courtly Grace | ★ unique | +1D Argue before an Expert Judge; a judge sets Cognition (SCV:133) | `ACU` | NAMED T4, overridden for dice by the kernel | HIST:310 |
| L42 | Economic Reasoning | § | +1D to the Argue pool; the adjudicator sets the ingredient | — | NAMED T4, overridden for dice by the kernel | HIST:242 |
| L43 | Crisis-Forged Conviction | ★ unique | +1D Argue on Church doctrine | — | NAMED T4, overridden for dice by the kernel | HIST:474 |
| L44 | Veteran's Eye | ★ unique | +1D on Command tactic rolls (F18) | `CHA` `ACU` | NAMED T4 | HIST:462 |
| L45 | Smooth Liar | ★ § | −1 strain when using Obscuring, a contest move | — | NAMED T4 | HIST:339 |
| L46 | Intimidation | ★ § | +1D Obscuring in private negotiation | — | NAMED T4 | HIST:349 |
| L47 | Shadow Work | § | +1D surveillance and counter-intelligence (Surveil rolls Cognition, FW:304) | `ACU` | INFERRED | HIST:339 |
| L48 | Garrison Eyes | unique | +1D detect infiltration | `ACU` | INFERRED | HIST:311 |
| L49 | Precision Hands | § | +1D examining crafted objects: a perceptual examination (Examine rolls Cognition, FW:93), not exactness of execution | `ACU` | INFERRED | HIST:350 |
| L50 | Dead Drop | ★ unique | −1 Ob on Intel ops, which roll the faction's Intel | — | NAMED T4 | HIST:339, :505 |
| L51 | Craft Expertise | ★ unique | +2D on any roll involving the craft | — | NAMED T4 | HIST:241 |
| L52 | Folk Healer | ★ unique | +1D Medicine, a roll that names no ingredient | — | NAMED T4 | HIST:362 |
| L53 | Field Medicine | ★ unique | −1 Ob stabilise | — | NAMED T4 | HIST:378 |
| L54 | Haggler's Nerve | ★ § | −1 strain in private negotiation (strain is what the Focus defence absorbs, F20) | `FOC` | INFERRED | HIST:312 |
| L55 | Literacy | by Formation; *"available as spark"* for the self-taught | presupposed by records and research | — | NAMED T4 | HIST:44-55 |
| L56 | Mentor | a rank's named NPC | *"+1D on one specified roll per season"*: a held bonus die, not a learning rate | — | NAMED T4 | faction_politics_v30:56 |
| L57 | Officer practice | — | *"named officer with Cavalry History"* gates a troop type | — | NAMED T4 | military_layer_v30:132-133 |
| L58 | Investment, Practice and Record slots | — | the 2026-08-15 progression slots | — | NAMED T4 | AUG:1285-1287 |

### 1.4 Every sourced use of one ingredient alone

One row per source statement that names one ingredient alone in a roll, check, gate or pool. A row is
INFERRED where the statement's ingredient is not one the tree names (*"Intellect"*, a *"Coherence
check"*, a *"Composure check"*). *Term* is the `_part2` coding.

| U | statement | ingredients | basis | locator | term |
|---|---|---|---|---|---|
| U01 | Border zone shifting objects: *"Agility Ob 2 to avoid"* | `AGI` | NAMED T4 | southernmost_v30:103 | quickness |
| U02 | Disengage: the disengager and a pursuer roll Agility pools | `AGI` | NAMED T4 | combat_reference_v1:598 | quickness |
| U03 | Environmental hazard: *"Endurance or Agility check; Ob 2–3"* | `END` `AGI` | NAMED T4 | southernmost_v30:123 | hardiness, quickness |
| U04 | Endurance-based exploration: forced marches, exposure | `END` | NAMED T4 | FW:92 | stamina |
| U05 | An Endurance check per Calamity territory crossed | `END` | NAMED T4 | FW:239 | hardiness |
| U06 | Tend the wounded: *"Endurance or Attunement check, Ob 2"* | `END` `ATT` | NAMED T4 | MB:925 | stamina, empathy |
| U07 | Exploration by terrain and navigation: Cognition | `ACU` | NAMED T4 | FW:90 | spatial-sense |
| U08 | Exploration depth gates: Cognition ≥ 2 / ≥ 3 | `ACU` | NAMED T4 | FW:84, :446 | reasoning |
| U09 | Examine: Cognition | `ACU` | NAMED T4, overridden for dice by the 2026-09-05 gloss | FW:93, :301 | observation |
| U10 | Surveil: Cognition | `ACU` | NAMED T4, overridden for dice by the 2026-09-05 gloss | FW:304 | observation |
| U11 | The interview Lattice's intellectual approaches: Cognition ≥ 3 | `ACU` | NAMED T4 | investigation_systems_v30:254 | reasoning |
| U12 | Argue before an expert judge: Cognition | `ACU` | NAMED T4, overridden for dice by the kernel | SCV:133 | reasoning |
| U13 | Develop: Cognition + Wealth-history | `ACU` | NAMED T4 | settlement_layer_v30:560; governance_play_redesign_v1:61 | reasoning |
| U14 | Survey (settlement): Cognition + Governance-history | `ACU` | NAMED T4 | governance_play_redesign_v1:87 | reasoning |
| U15 | Hold Court: *"Charisma/Cognition + Governance-history"* | `CHA` `ACU` | NAMED T4 | governance_play_redesign_v1:64 | judgment |
| U16 | Investigate (settlement): Cognition + relevant history vs concealment | `ACU` | NAMED T4 | governance_play_redesign_v1:68 | reasoning |
| U17 | Concealment pool: Cognition × 2 + History sets the Concealment Ob | `ACU` | NAMED T4 | FW:361 | reasoning |
| U18 | Survey the damage: a Cognition check | `ACU` | NAMED T4 | MB:926 | observation |
| U19 | A Miraculous Event's witness: Cognition vs Ob = current Truth | `ACU` | NAMED T4 | miraculous_event_v30:132; solmund_master_document:494 | steadfastness |
| U20 | Practitioner inference from census data: an *"Intellect check"* | `ACU` | INFERRED | npc_behavior_v30:350, :352 | reasoning |
| U21 | A covert cue: *"Cognition ≥ 3 parses it"* | `ACU` | NAMED T4 | valoria_ui_ux_v4_1:408-410 | reasoning |
| U22 | Knot formation: `spirit × 2 + history_relationships` | `WIL` | NAMED T2 | knots.py:212-215; FW:483 | will |
| U23 | A sworn bond: Spirit_A + Spirit_B | `WIL` | NAMED T4 | npc_relational_graph_v30:277 | (not coded as a term) |
| U24 | Thread Approach Training: a Spirit pool | `WIL` | NAMED T4 | threadwork_v30:119 | will |
| U25 | A Wound during contact: a Spirit check, or contact drops | `WIL` | NAMED T4 | threadwork_v30:229 | will |
| U26 | Dissonance for a non-sensitive: a Spirit check | `WIL` | NAMED T4 | fieldwork_v30_infill:48 | (not coded: no failure stated) |
| U27 | Sincerity Check: Spirit | `WIL` | NAMED T4 | FW:430; ED-503 at FW:822 | sincerity |
| U28 | Belief integrity check: a Spirit pool | `WIL` | NAMED T4 | npc_behavior_v30:1054 | steadfastness |
| U29 | Witness to a caste-transgressive Conviction: a Spirit check, Ob 2 | `WIL` | NAMED T4 | faction_politics_v30:741 | steadfastness |
| U30 | Conviction Reformation: a Spirit pool, Ob 3 | `WIL` | NAMED T4 | faction_politics_v30:752 | steadfastness |
| U31 | Witness to a Thread event: a Spirit pool | `WIL` | NAMED T4 | conviction_track_v1:95 | steadfastness |
| U32 | Core zone, a non-practitioner: a Spirit check, Ob 2, or Truth −1 | `WIL` | NAMED T4 | southernmost_v30:105 | steadfastness |
| U33 | Acquiring an Inspiration: a Spirit check, TN 7 Ob 1 | `WIL` | NAMED T4 | derived_stats_v30:191 | devotion |
| U34 | Thread-aware exploration: Attunement, *"sensing Thread phenomena, reading the substrate"* | `ATT` | NAMED T4 | FW:91 | thread-sensitivity |
| U35 | Interview: Attunement | `ATT` | NAMED T4, overridden for dice by the 2026-09-05 gloss | FW:94, :302 | reading-people |
| U36 | Read: Attunement | `ATT` | NAMED T4 | FW:97, :408 | reading-people |
| U37 | Negotiate: Attunement | `ATT` | NAMED T4 | FW:101, :413 | reading-people |
| U38 | The Lattice's emotional approaches: Attunement ≥ 4 | `ATT` | NAMED T4 | investigation_systems_v30:255 | empathy |
| U39 | Argue with no adjudicator: Attunement | `ATT` | NAMED T4, overridden for dice by the kernel | SCV:135 | reading-people |
| U40 | Administer: Attunement + Governance History | `ATT` | NAMED T4 | settlement_layer_v30:563 | reading-people |
| U41 | Combat initiative by Attunement | `ATT` | NAMED T4 | FW:106; combat_c4_draft_v0:127 (not opened) | (reflexes; `_part3` S-defect 3) |
| U42 | Impress: Charisma | `CHA` | NAMED T4 | FW:98, :411 | presence |
| U43 | Rumour: Charisma | `CHA` | NAMED T4 | FW:100, :412 | presence |
| U44 | Converse: Charisma | `CHA` | NAMED T4 | FW:409 | persuasiveness |
| U45 | A cover identity: a Charisma roll, Ob 2 | `CHA` | NAMED T4 | FW:620 | presence |
| U46 | Argue before a crowd: Charisma | `CHA` | NAMED T4, overridden for dice by the kernel | SCV:134 | presence |
| U47 | Pacify: Charisma + local History | `CHA` | NAMED T4 | settlement_layer_v30:562 | presence |
| U48 | Keep Order by Consent: Charisma | `CHA` | NAMED T4 | governance_play_redesign_v1:63 | presence |
| U49 | Address the population: a Charisma check | `CHA` | NAMED T4 | MB:927 | persuasiveness |
| U50 | The Interview action: a Charisma pool | `CHA` | NAMED T4, overridden for dice by the 2026-09-05 gloss | investigation_systems_v30:243 | persuasiveness |
| U51 | The knot gate: Bonds ≥ 5 | `BON` | NAMED T2 | knots.py:185-187; FW:477 | relational-depth |
| U52 | Connect: Bonds | `BON` | NAMED T4 | FW:99, :410 | relational-depth |
| U53 | An Anchoring Scene: a Bonds check | `BON` | NAMED T4 | threadwork_v30:678, :707; knots_v30:149 | relational-depth |
| U54 | Research: Recall | `REC` | NAMED T4, overridden for dice by the 2026-09-05 gloss | FW:95, :303 | memory |
| U55 | Reconstruct: Recall | `REC` | NAMED T4, overridden for dice by the 2026-09-05 gloss | FW:306 | inference |
| U56 | Fragmented fallout: a *"Memory check Ob 2"*; "Memory" is Recall's former name (SCV:22) | `REC` | NAMED T4 | threadwork_v30:688 | memory |
| U57 | The knot gate: either party TS ≥ 30 | `TS` | NAMED T2 | knots.py:195-198 | thread-sensitivity |
| U58 | Investigation depth gates: TS ≥ 10 / ≥ 30 | `TS` | NAMED T4 | FW:84, :301, :447 | thread-sensitivity |
| U59 | `thread_read`: TS ≥ 30 | `TS` | NAMED T3 | K-3; FW:305 | thread-sensitivity |
| U60 | Site and monster visibility by TS | `TS` | NAMED T4 | FW:208-218; valoria_ui_ux_v4_1:914 | thread-sensitivity |
| U61 | Rendering strain by depth and TS | `TS` | NAMED T4 | FW:252-254 | thread-sensitivity |
| U62 | The Depth-4 Coherence check, Ob 1 | `RES` | INFERRED | FW:253 | self-coherence |
| U63 | A monster hex, a practitioner: a *"Coherence check"* | `RES` | INFERRED | valoria_ui_ux_v4_1:916 | self-coherence |
| U64 | A monster hex, a non-practitioner: a *"Composure check"* (Composure is `CHA × 3`, F24) | `CHA` | INFERRED | valoria_ui_ux_v4_1:916 | concentration |

**No source uses STR, FOC, BODY or TMP alone.** Strength and Focus reach every act through formulas
(F03, F07–F10, F14–F16, F20, F31); BODY through `end` (F13); temperament through the lean (F17).

### 1.5 The 46 demands, by kind

**Key.** *Kind* is exactly one of the six (Words), independent of any roster. *Ingredients* are the
ones the sources use today (history); `A`/`B` means the source names either. *Group* is the one
grouping, **relative to the recommended set** (`_part3` §8.1), so it is filled only after selection.
Columns P, V and S count the practice domains, verbs (distinct resolvers in brackets) and subsystems
that draw the term. **Draws** counts draw entries (they re-count). **Statements** count distinct keys
at best basis: **named** (by tier), **overridden** (by cause) and **inferred**, each once. **Order: by
named statements, then by name.**

| T | demand | kind | ingredients the sources use | group (recommended set) | P | V [res] | S | draws | named statements (by tier) | overridden (by cause) | inferred | flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | `reasoning` | CAPACITY | `ACU` | ACU | 7 | 5 [5] | 5 | 26 | 10 (T4 10) | 1 (kernel 1) | 3 | Cognition is the registry's *"[ASSUMPTION]"* alias (:42) |
| T02 | `thread-sensitivity` | CAPACITY | `TS` | TS | 4 | 10 [4] | 6 | 23 | 9 (T2 2 · T3 1 · T4 6) | 0 | 1 | also rolled on ATT (FW:91; L16–L21): `_part3` S-defect 5 |
| T03 | `steadfastness` | CAPACITY | `WIL`/`ACU` | WIL | 0 | 0 [0] | 4 | 7 | 6 (T4 6) | 0 | 0 | Spirit in five statements, Cognition in one (S-defect 4) |
| T04 | `will` | CAPACITY | `WIL` | WIL | 2 | 10 [4] | 3 | 17 | 6 (T2 2 · T4 4) | 0 | 0 | — |
| T05 | `presence` | CAPACITY | `CHA` | CHA | 4 | 4 [4] | 5 | 18 | 4 (T4 4) | 2 (kernel 2) | 2 | — |
| T06 | `concentration` | COMPUTED QUANTITY | `FOC` `WIL` | FOC | 8 | 12 [5] | 5 | 26 | 3 (T2 1 · T4 2) | 1 (kernel 1) | 5 | the source computes `3·Focus + 2·Spirit` (F14); also F15, F16, F20, F31; absorbs composure and nerve (Merges) |
| T07 | `memory` | CAPACITY | `REC` | REC | 5 | 2 [2] | 5 | 13 | 3 (T4 3) | 2 (2026-09-05 gloss 1 · kernel 1) | 2 | — |
| T08 | `reading-people` | CAPACITY | `ATT` | ATT | 5 | 4 [4] | 6 | 15 | 3 (T4 3) | 2 (2026-09-05 gloss 1 · kernel 1) | 3 | — |
| T09 | `relational-depth` | CAPACITY | `BON` | BON | 2 | 2 [2] | 2 | 6 | 3 (T2 1 · T4 2) | 0 | 0 | — |
| T10 | `self-coherence` | COMPUTED QUANTITY | `RES` | uncovered | 1 | 6 [1] | 3 | 10 | 3 (T2 1 · T4 2) | 0 | 0 | the source computes `gain × resilience` (F34), dark at gain 0 |
| T11 | `stamina` | COMPUTED QUANTITY | `END` `WIL` | END | 4 | 6 [5] | 6 | 16 | 3 (T1 1 · T4 2) | 0 | 5 | the source computes `3·End + 2·Spirit` (F11); also F12, F13 |
| T12 | `breadth` | LIMIT | `REC` | REC | 0 | 1 [1] | 1 | 3 | 2 (T4 2) | 0 | 0 | equip slots by Recall (F39); effective Recall (F37) |
| T13 | `devotion` | COMPUTED QUANTITY | `WIL` | WIL | 0 | 0 [0] | 2 | 2 | 2 (T4 2) | 0 | 0 | the source computes the Inspiration cap as `Spirit × 1` (F29) |
| T14 | `observation` | CAPACITY | `ACU` | ACU | 5 | 3 [3] | 4 | 12 | 2 (T4 2) | 2 (2026-09-05 gloss 2) | 3 | — |
| T15 | `persuasiveness` | CAPACITY | `CHA` | CHA | 3 | 4 [4] | 4 | 11 | 2 (T4 2) | 1 (2026-09-05 gloss 1) | 6 | — |
| T16 | `spatial-sense` | CAPACITY | `ACU` | ACU | 3 | 0 [0] | 2 | 5 | 2 (T4 2) | 0 | 1 | — |
| T17 | `toughness` | COMPUTED QUANTITY | `END` `WIL` `STR` | END | 1 | 2 [1] | 3 | 6 | 2 (T1 1 · T4 1) | 0 | 1 | the source computes Durability (F10); also F13, F35 |
| T18 | `anticipation` | COMPUTED QUANTITY | `ACU` `ATT` | ACU | 2 | 3 [2] | 2 | 7 | 1 (T2 1) | 0 | 1 | the source computes Reading (F06); its feint draws are uses of Command (INFERRED) |
| T19 | `balance` | COMPUTED QUANTITY | `AGI` `STR` | AGI | 2 | 2 [1] | 1 | 5 | 1 (T2 1) | 0 | 1 | the source computes `½Agi + ½Str − 1 + skill` (F03) |
| T20 | `boldness` | TEMPERAMENT | `TMP` | temperament | 1 | 2 [1] | 2 | 5 | 1 (T2 1) | 0 | 1 | a lean, `(disp − 4)/3` (F17) |
| T21 | `contact-endurance` | COMPUTED QUANTITY | `WIL` | WIL | 1 | 7 [1] | 1 | 9 | 1 (T4 1) | 0 | 0 | the source computes `Spirit × 5` (F30); absorbs recovery |
| T22 | `empathy` | CAPACITY | `ATT` | ATT | 2 | 1 [1] | 2 | 5 | 1 (T4 1) | 0 | 1 | — |
| T23 | `hardiness` | CAPACITY | `END` | END | 1 | 1 [1] | 2 | 5 | 1 (T4 1) | 0 | 2 | — |
| T24 | `judgment` | CAPACITY | `CHA`/`ACU` | CHA | 2 | 1 [1] | 4 | 7 | 1 (T4 1) | 0 | 3 | Hold Court names either (U15); grouped by the first named |
| T25 | `land-sense` | PRACTICE | `ACU` | ACU | 2 | 0 [0] | 1 | 3 | 1 (T4 1) | 0 | 0 | Seasons Reader (L12), a skill bonus on a Cognition roll |
| T26 | `learning` | COMPUTED QUANTITY | `REC` `WIL` | REC | 1 | 1 [1] | 1 | 3 | 1 (T4 1) | 0 | 1 | the source computes `⌊Recall/2⌋` spark dice; the check is `Spirit + ⌊Recall/2⌋` (F38) |
| T27 | `practice-ceiling` | LIMIT | `REC` | REC | 0 | 1 [1] | 1 | 2 | 1 (T4 1) | 0 | 0 | the depth ceiling by Recall (F40) |
| T28 | `quickness` | COMPUTED QUANTITY | `AGI` | AGI | 2 | 2 [1] | 2 | 7 | 1 (T2 1) | 0 | 3 | the source computes Tempo (F01); also F04 |
| T29 | `reflexes` | COMPUTED QUANTITY | `AGI` `ATT` | AGI | 1 | 2 [1] | 1 | 4 | 1 (T2 1) | 0 | 0 | the source computes Reflex, `(2·Agi + Att)/3` (F02); also F05 |
| T30 | `sincerity` | CAPACITY | `WIL` | WIL | 2 | 1 [1] | 1 | 4 | 1 (T4 1) | 0 | 1 | the registry aliases it to Bonds; the sources roll Spirit (FW:430, :822): S-defect 2 |
| T31 | `strength` | CAPACITY | `STR` | STR | 3 | 3 [2] | 2 | 8 | 1 (T2 1) | 0 | 2 | moves odds, cost and effect size (F03, F07–F10) |
| T32 | `deception` | PRACTICE | — | practice | 1 | 1 [1] | 2 | 4 | 0 | 0 | 3 | **ALL INFERRED**; the skills are on the Obscuring move (L45, L46) |
| T33 | `dexterity` | CAPACITY | `AGI` | AGI | 3 | 4 [4] | 2 | 9 | 0 | 0 | 5 | **ALL INFERRED**; Agility by the registry alias only; no code reads `agi` for hand work |
| T34 | `discernment` | CAPACITY | `ATT` | ATT | 0 | 2 [2] | 2 | 4 | 0 | 0 | 2 | **ALL INFERRED**; FW:94 *"calibrating trust"*; AX-7's *"competence"* may be practice |
| T35 | `discipline` | PRACTICE | — | practice | 0 | 1 [1] | 1 | 2 | 0 | 0 | 1 | **ALL INFERRED** |
| T36 | `inference` | CAPACITY | `REC` | REC | 1 | 1 [1] | 1 | 3 | 0 | 1 (2026-09-05 gloss 1) | 0 | overridden only (gloss) |
| T37 | `intimidation` | PRACTICE | — | practice | 0 | 2 [2] | 0 | 2 | 0 | 0 | 1 | **ALL INFERRED** |
| T38 | `leadership` | COMPUTED QUANTITY | `CHA` `ACU` | CHA | 1 | 1 [1] | 3 | 5 | 0 | 0 | 3 | **ALL INFERRED as a term**; the sources roll Command, NAMED T2 (F18) |
| T39 | `numeracy` | PRACTICE | — | practice | 3 | 1 [1] | 2 | 6 | 0 | 0 | 2 | **ALL INFERRED** |
| T40 | `patience` | TEMPERAMENT | — | temperament | 5 | 1 [1] | 3 | 9 | 0 | 0 | 4 | **ALL INFERRED**; a lean by this proposal's reading |
| T41 | `planning` | PRACTICE | — | practice | 2 | 0 [0] | 1 | 3 | 0 | 0 | 1 | **ALL INFERRED** |
| T42 | `precision` | PRACTICE | — | practice | 2 | 1 [1] | 1 | 4 | 0 | 0 | 3 | **ALL INFERRED**; its one source is craft practice (HIST:241); Precision Hands is perceptual (L49) |
| T43 | `quick-thinking` | PRACTICE | — | practice | 1 | 0 [0] | 1 | 2 | 0 | 0 | 1 | **ALL INFERRED** |
| T44 | `situational-awareness` | COMPUTED QUANTITY | `CHA` `ACU` | CHA | 1 | 1 [1] | 2 | 4 | 0 | 0 | 2 | **ALL INFERRED as a term**; the sources roll Command, NAMED T2 (F18) |
| T45 | `tactical-read` | COMPUTED QUANTITY | `CHA` `ACU` | CHA | 1 | 1 [1] | 1 | 3 | 0 | 0 | 1 | **ALL INFERRED as a term**; the sources roll Command (F18); "tactical read" is a docstring gloss |
| T46 | `verbal-fluency` | PRACTICE | — | practice | 1 | 3 [3] | 1 | 5 | 0 | 0 | 3 | **ALL INFERRED** |

**Kinds** (from the table): CAPACITY 19, COMPUTED QUANTITY 14, PRACTICE 9, LIMIT 2, TEMPERAMENT 2 =
46; no demand is a RESOURCE. **Fourteen demands have no named or overridden statement:** the three
uses of Command, whose formula is NAMED T2 (F18); `dexterity` and `discernment`, whose ingredient is
named but whose function is not; and the nine practice and lean demands other than `land-sense`.
`inference` rests on one overridden statement.

**Merges, kept from the first passes, and why.**

- **`composure` is in `concentration`.** In T2 combat code one tracker, 3·Focus + 2·Spirit
  (`combatant.py:147`), drains on hits and sets consistency and mental fatigue
  (`combat_systems.py:1423-1431`); AUG files it all under *Concentration*, also *Steadiness* (AUG:90,
  :413, :479); SCV's CR3 split the old Charisma × 3 *Composure* buffer into Concentration and Face
  (SCV:242-247). *Nerve* (HIST:312) is this demand. ⚠ The monster-hex *"Composure check"*
  (`valoria_ui_ux_v4_1:916`) is coded here by the merge, but *Composure* is Charisma × 3 in
  `derived_stats_v30:554` (F24): `_part3` S-defect 1.
- **`recovery` is in `contact-endurance`**: one track, threadwork_v30:195, :203 (F30).
- **`courage` stays out, narrowed.** Its one first-pass draw is troop Morale, which the source starts
  at Command plus unit quality (MB:230); a nerve check does exist (`valoria_ui_ux_v4_1:916`), coded to
  `concentration` by the merge above.
- **SCV:147 is `reading-people`**, not also empathy; **FW:306 is `inference`**, not also memory.
- *Affability* (registry :48) names no function any source draws; *vigilance* is `observation`
  sustained by `concentration`; *Perception* is Attunement's alias.

### 1.6 What the sources hang on each ingredient today (evidence for the selection)

**One row per ingredient.** Its formulas (§1.2), the learned skills that enter on it (§1.3), its
sourced uses (§1.4), each counted once per source statement, and the demands whose sources name it
(§1.5, any position). *Best tier* is the highest tier at which the ingredient carries a per-person
value. This is history: it says how the sources combine ingredients today, and it does not make a
candidate a primary or exclude one.

| code | ingredient | formulas that use it | learned skills on it | sourced uses | demands naming it | best tier |
|---|---|---|---|---|---|---|
| `STR` | Strength | **5**: F03, F07, F08, F09, F10 | **1**: L06 | **0** | 3 | T2 |
| `AGI` | Agility | **5**: F01–F05 | **6** (5 named, 1 inferred): L01, L06, L07, L22, L36, L37 | **3**: U01–U03 | 4 | T2 |
| `END` | Endurance | **4**: F10, F11, F12, F35 | **2**: L01, L38 | **4**: U03–U06 | 3 | T2 (BODY stands in at T1, F13) |
| `FOC` | Focus | **5** (4 named, 1 overridden): F14, F15, F16, F20, F31 | **3** (2 retired, 1 inferred): L32, L33, L54 | **0** | 1 | T2 |
| `ACU` | Acuity (Cognition) | **5**: F04, F06, F18, F27, F28 | **13** (9 named, 1 overridden, 3 inferred) | **15** (11 named, 3 overridden, 1 inferred): U07–U21 | 10 | T2 |
| `WIL` | Will (Spirit) | **8**: F10, F11, F14, F29, F30, F32, F35, F38 | **6**: L02, L03, L10, L21, L34, L35 | **12**: U22–U33 | 9 | T2 |
| `ATT` | Attunement | **5** (4 named, 1 overridden): F02, F04, F05, F06, F25 | **15** (10 named, 5 overridden) | **9** (7 named, 2 overridden): U06, U34–U41 | 5 | T2 |
| `CHA` | Charisma | **5** (3 named, 2 overridden): F18, F21, F22, F24, F26 | **4** (2 named, 2 overridden) | **11** (8 named, 2 overridden, 1 inferred): U15, U42–U50, U64 | 6 | T2 |
| `BON` | Bonds | **1**: F36 | **0** | **3**: U51–U53 | 1 | T2 |
| `REC` | Recall | **5** (4 named T4, 1 overridden): F25, F37–F40 | **10** (4 named, 6 overridden) | **3** (1 named, 2 overridden): U54–U56 | 5 | T4 |
| `TS` | Thread Sensitivity | **2**: F32, F33 | **2**: L02, L19 | **5**: U57–U61 | 1 | T2 |
| `RES` | resilience | **1**: F34, dark at gain 0 | **0** | **2**, both inferred: U62, U63 | 1 | T2, dark |
| `BODY` | the body's condition | **1**: F13 | **0** | **0** | 0 | **T1** |
| `TMP` | temperament | **1**: F17 | **0** | **0** | 1 | T2 |
| — | none | 3: F19 Resolution pool, F23 kernel trackers, F41 Negotiate Ob | 14: L04, L05, L42, L43, L45, L46, L50–L53, L55–L58 | — | 9 practice, 1 lean | — |

### 1.7 The command that reproduces §1.5, §1.6, `_part3`'s coverage test and the totals

Run from the repository root. It reads the evidence draws in `_part2`, the tables here (rows `C`, `F`,
`L`, `U`, `T`) and the candidate sets in `_part3` (rows `K`); refuses a demand that is in the evidence
and not in §1.5 or the reverse; prints every key with more than one basis; and prints per demand, per
ingredient, per group, the coverage of each candidate set, and the totals. The Histories sweep behind
§1.3 is the pattern in its first comment, run over HIST.

```sh
python3 - <<'EOF'
# L-table sweep (run separately over HIST): skills whose effect names an ingredient, a pool or a formula:
#   r"\*\*([A-Z][A-Za-z'’ /-]+)\*\*\s*§?\s*\(([^)]*)\)" and the vocation form "★ Name § (…)", each
#   kept if its effect matches \b(Cognition|Attunement|Recall|Spirit|Agility|Charisma|Focus|Endurance|
#   Strength|Bonds|Appraise|Argue|Command|Medicine|Obscuring|Concentration)\b
import re, collections
B = 'proposals/2026-10-16-attribute-derivation'
head, ev, p3 = (open(B + s).read() for s in ('.md', '_part2.md', '_part3.md'))
R = r'(?:odds|difficulty/cost|eligibility|effect size|resists another)'
DRAW = re.compile(r'`([a-z-]+)` \((' + R + r'(?: \+ ' + R + r')*), \[([a-z0-9-]+)\] '
                  r'(?:NAMED (T\d)(?:, overridden for dice by the (kernel|2026-09-05 gloss|T3 row))?|(INFERRED))')
A = collections.defaultdict(lambda: dict(P=set(), V=set(), S=set(), res=set(), n=0, keys={}))
for l in ev.splitlines():
    m = re.match(r'\| (P\d\d|S\d\d|\d+) \|', l)
    if not m or l.count(' | ') < 6: continue
    i = m.group(1); lv = i[0] if i[0] in 'PS' else 'V'
    for t, roles, key, tier, cause, inf in DRAW.findall(l):
        a = A[t]; a['n'] += 1; a[lv].add(i)
        if lv == 'V': a['res'].add('thread' if 58 <= int(i) <= 64 else 'bout' if i in ('18', '20') else i)
        a['keys'].setdefault(key, set()).add('inferred' if inf else 'overridden ' + cause if cause else 'named ' + tier)
rank = lambda b: (0 if b[0] == 'n' else 1 if b[0] == 'o' else 2, b)
best = lambda a: collections.Counter(min(v, key=rank) for v in a['keys'].values())
grp = lambda c, p: sum(v for k, v in c.items() if k.startswith(p))
cells = lambda l: [c.strip() for c in l.strip().strip('|').split(' | ')]
rows = lambda p, s=head: [cells(l) for l in s.splitlines() if re.match(r'\| ' + p + r'\d\d \|', l)]
T = {re.search(r'`([a-z-]+)`', r[1]).group(1): r for r in rows('T')}
assert set(T) == set(A), sorted(set(T) ^ set(A))
for t in A:
    for k, v in A[t]['keys'].items():
        if len(v) > 1: print('mixed key:', t, k, sorted(v))
for t in sorted(A, key=lambda t: (-grp(best(A[t]), 'named'), t)):
    a, c = A[t], best(A[t])
    print(t, '|', T[t][2], '|', T[t][4], '|', len(a['P']), f"{len(a['V'])} [{len(a['res'])}]", len(a['S']), a['n'],
          '| named', grp(c, 'named'), {k[6:]: v for k, v in sorted(c.items()) if k[0] == 'n'},
          '| overridden', grp(c, 'overridden'), '| inferred', c['inferred'])
inp = lambda s: re.findall(r'`([A-Z]+)`', s)
tok = lambda s: [inp(x) for x in re.findall(r'`[A-Z]+`(?:/`[A-Z]+`)*', s)]
kind = lambda s: 'inferred' if 'INFERRED' in s else 'retired' if 'RETIRED' in s else 'overridden' if 'overridden' in s else 'named'
C, F, L, U = rows('C'), rows('F'), rows('L'), rows('U')
print('ingredient | formulas | learned skills | uses | demands naming it')
for x in [r[1].strip('`') for r in C]:
    f = collections.Counter(kind(r[5]) for r in F if x in inp(r[3]))
    s = collections.Counter(kind(r[5]) for r in L if x in inp(r[4]))
    u = collections.Counter(kind(r[3]) for r in U if x in inp(r[2]))
    print(x, '|', sum(f.values()), dict(f), '|', sum(s.values()), dict(s), '|', sum(u.values()), dict(u),
          '|', sum(x in inp(r[3]) for r in T.values()))
print('group | demands | statements named/overridden/inferred')
for g in dict.fromkeys(r[4] for r in sorted(T.values())):
    ks = {}
    for t in (t for t in A if T[t][4] == g):
        for k, v in A[t]['keys'].items(): ks.setdefault(k, set()).update(v)
    gc = collections.Counter(min(v, key=rank)[0] for v in ks.values())
    print(g, '|', sum(T[t][4] == g for t in A), '|', gc['n'], gc['o'], gc['i'])
STATE = {'BODY'}   # a condition every person has whatever the roster: never a missing primary
for k in rows('K', p3):
    S = set(inp(k[2])) | STATE
    sat = lambda toks: all(any(c in S for c in t) for t in toks)
    miss = lambda toks: '/'.join(sorted({'/'.join(t) for t in toks if not any(c in S for c in t)}))
    dc, du = collections.Counter(), []
    for t, r in sorted(T.items()):
        toks = tok(r[3])
        if r[2] == 'PRACTICE': dc['practice'] += 1
        elif not toks: dc['unsourced ' + r[2].lower()] += 1
        elif sat(toks): dc['expressed'] += 1
        else: dc['UNCOVERED'] += 1; du.append(f'{t} (needs {miss(toks)})')
    fc, fu = collections.Counter(), []
    for r in F:
        toks = tok(r[3])
        if not toks: fc['no person ingredient'] += 1
        elif sat(toks): fc['expressed'] += 1
        else: fc['UNCOVERED'] += 1; fu.append(f'{r[0]} (needs {miss(toks)})')
    print(k[0], k[1], len(S - STATE), 'primaries | demands', dict(sorted(dc.items())), '| formulas', dict(sorted(fc.items())))
    print('   uncovered:', '; '.join(du + fu) or 'none')
ev_all = collections.Counter()
for a in A.values(): ev_all.update(best(a))
items = set().union(*(a['P'] | a['V'] | a['S'] for a in A.values()))
print(len(A), 'demands;', sum(a['n'] for a in A.values()), 'draw entries over',
      sum(i[0] == 'P' for i in items), 'domains,', sum(i[0] not in 'PS' for i in items), 'graded verbs,',
      sum(i[0] == 'S' for i in items), 'subsystems; statements per demand:', dict(sorted(ev_all.items())))
print('kinds:', dict(collections.Counter(r[2] for r in T.values())))
print('evidence:', len(C), 'ingredients,', len(F), 'formulas,', len(L), 'learned skills,', len(U), 'uses;',
      'with no ingredient:', sum(not inp(r[3]) for r in F), 'formulas,', sum(not inp(r[4]) for r in L), 'learned skills')
EOF
```

Its output, at this writing, after the 46 per-demand lines that §1.5 tabulates:

```
mixed key: presence fw-cover-identity ['named T4', 'overridden T3 row']
ingredient | formulas | learned skills | uses | demands naming it
STR | 5 {'named': 5} | 1 {'named': 1} | 0 {} | 3
AGI | 5 {'named': 5} | 6 {'named': 5, 'inferred': 1} | 3 {'named': 3} | 4
END | 4 {'named': 4} | 2 {'named': 2} | 4 {'named': 4} | 3
FOC | 5 {'named': 4, 'overridden': 1} | 3 {'retired': 2, 'inferred': 1} | 0 {} | 1
ACU | 5 {'named': 5} | 13 {'named': 9, 'overridden': 1, 'inferred': 3} | 15 {'named': 11, 'overridden': 3, 'inferred': 1} | 10
WIL | 8 {'named': 8} | 6 {'named': 6} | 12 {'named': 12} | 9
ATT | 5 {'named': 4, 'overridden': 1} | 15 {'named': 10, 'overridden': 5} | 9 {'named': 7, 'overridden': 2} | 5
CHA | 5 {'named': 3, 'overridden': 2} | 4 {'named': 2, 'overridden': 2} | 11 {'named': 8, 'overridden': 2, 'inferred': 1} | 6
BON | 1 {'named': 1} | 0 {} | 3 {'named': 3} | 1
REC | 5 {'overridden': 1, 'named': 4} | 10 {'named': 4, 'overridden': 6} | 3 {'overridden': 2, 'named': 1} | 5
TS | 2 {'named': 2} | 2 {'named': 2} | 5 {'named': 5} | 1
RES | 1 {'named': 1} | 0 {} | 2 {'inferred': 2} | 1
BODY | 1 {'named': 1} | 0 {} | 0 {} | 0
TMP | 1 {'named': 1} | 0 {} | 0 {} | 1
group | demands | statements named/overridden/inferred
ACU | 5 | 15 3 8
TS | 1 | 9 0 1
WIL | 5 | 16 0 1
CHA | 6 | 7 3 17
FOC | 1 | 3 1 5
REC | 5 | 7 3 3
ATT | 3 | 4 2 6
BON | 1 | 3 0 0
uncovered | 1 | 3 0 0
END | 3 | 6 0 8
AGI | 4 | 3 0 9
temperament | 2 | 1 0 5
STR | 1 | 1 0 2
practice | 8 | 0 0 15
(… the four coverage lines, quoted in `_part3` §7.3 …)
46 demands; 355 draw entries over 19 domains, 34 graded verbs, 16 subsystems; statements per demand: {'inferred': 80, 'named T1': 2, 'named T2': 13, 'named T3': 1, 'named T4': 63, 'overridden 2026-09-05 gloss': 6, 'overridden kernel': 6}
kinds: {'CAPACITY': 19, 'COMPUTED QUANTITY': 14, 'LIMIT': 2, 'TEMPERAMENT': 2, 'PRACTICE': 9}
evidence: 14 ingredients, 41 formulas, 58 learned skills, 64 uses; with no ingredient: 3 formulas, 14 learned skills
```

**The totals, in words, as every part of this proposal quotes them.** 46 demands (19 CAPACITY, 14
COMPUTED QUANTITY, 9 PRACTICE, 2 LIMIT, 2 TEMPERAMENT); 355 draw entries over 19 practice domains, 34
graded verbs (of 65) and 16 subsystems; **171 demand-statements: 79 named (T1 2, T2 13, T3 1, T4 63),
12 overridden (kernel 6, gloss 6) and 80 inferred.** The evidence: 14 ingredients, 41 source formulas
(38 with an ingredient), 58 learned-skill rows (44 with an ingredient), 64 sourced uses. **Coverage:**
the recommended eleven leave 2 demands and 2 formulas uncovered; the smaller eight 9 and 13; the
larger thirteen none; today's nine 8 and 9. The first pass's 297 draws (166 named, 30 overridden, 101
inferred) counted draw entries over ten subsystems and are superseded.
