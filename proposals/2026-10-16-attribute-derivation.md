# Attribute derivation: what each practice, verb and subsystem requires of a person, collated as a stack (base inputs → derived scores → learned skills → the resolver)

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. It recommends; it decides nothing (J-T1 and J-T2 stay Jordan's).
## Lane: IN (cross-cutting), with PC, MB, SC, FI, WR, SE, FA, NPC as sources. IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions possible).
## Parts, in reading order: this file (words, §1 the stack and the classified terms, the command) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§2–§5, the interrogation: practice domains, verbs, subsystems) · [`_part3`](2026-10-16-attribute-derivation_part3.md) (§6–§12: the one grouping, what should be an attribute, meta-rule, NERS, limits, both critic reconciliations). The base-input list alone: [`_aptitudes`](2026-10-16-attribute-derivation_aptitudes.md). The word study: [`_equivalences`](2026-10-16-attribute-derivation_equivalences.md).

**What this answers.** Jordan, 2026-10-16: *"perform interrogation of each 'PRA' to identify what kind
of skills/aptitudes are required for each. after doing so, we are to flatten our list and collate all
of these together to see what should be an attribute."* Then: *"like our VERB interrogation is
supposed to be doing this too"*; *"ie WHAT does each verb/subsystem require"*; *"show me the flattened
aptitude list when it's done. we will work from those to think about attributes we have."* And, after
the first critic pass: ***"Learned skills and derived scores etc all need to be folded in to this."***

So the first pass's flat list of 46 words is re-cast here as a **stack**. Every word is classified by
the layer it lives in, and the question *what should be an attribute* is answered from the bottom
layer only. The primary deliverable is §1.6 (and its extract, `_aptitudes`): the base inputs, with the
derived scores and learned skills that hang off each, and the 46 words mapped into them.

---

## Words

**The stack.** Four layers, each computed from the ones below it.

| layer | name | what it is | examples |
|---|---|---|---|
| **L1** | **BASE INPUT** | a quantity a person carries that no source computes from another of the person's quantities | the registry's nine; Recall; Thread Sensitivity; `resilience` (a stub slot); BODY (the season loop's state); temperament (`disp`) |
| **L2** | **DERIVED SCORE** | a quantity a source computes from base inputs and **writes down as a formula of its own**: a tracker, cap, threshold, rate, obstacle or score; or any formula that blends two or more base inputs | `stamina_max = 3·END + 2·WIL`; Command; Reading; Cover; the thread pool |
| **L3** | **LEARNED SKILL** | what is acquired or grows by doing, and enters a pool, an obstacle or a derived score | History and its levels; `capability` keys; the contest `faculty`; Combatant `skills`, `equipped`, `tradition`; tactic cards; the Histories skills; Mentor dice |
| **L4** | **the resolver** | the pool, odds, obstacle or gate an act is settled by | `roll_pool(command)`; `max(5, History + 6)`; Ob = ⌈opponent's Charisma ÷ 2⌉ |

- **A USE of a base input** is a source naming that input alone in a roll, check, gate or pool, with
  at most the ×2 dice convention and a practice addend: *"Pacify rolls Charisma + local History"*;
  the knot's `spirit × 2 + history_relationships`; the Argue pool, *"(Primary Attribute × 2) + History
  bonus"*. A use is not a derived score. §1.4 lists every sourced use, once per statement.
- **A USE of a derived score** is the same for a derived score: Command's span of control, its recall
  roll, its feint roll and tactic execution are four uses of one derived score.
- **LIMIT**: a cap on how much a person can hold, set by a base input (equip slots, the practice depth
  ceiling).
- **TEMPERAMENT**: a lean, not a capacity (`disp`).

**The split rule (J-13, controlling).** Jordan, 2026-09-06, recorded at
`workplans/valoria_master_workplan_v9_part5.md:433`: *"It's a derived score that is used for the
subsystem for a character, but it is not a character attribute in and of itself."* The first pass read
it as about the contest's social figure only. **This pass applies it to the whole stack, uniformly:
a derived score is never an attribute, and a base input is never split by its derived scores or by
its uses.** So Agility is not split into Tempo, Reflex and Balance, and Command is not split into
leadership, tactical read and situational awareness. Jordan's ruling in code says the same of one
case: *"BALANCE is NOT a stat (Jordan): it is GOVERNED BY AGILITY, modulated by CURRENT poise"*
(`modules/combat/combat_systems.py:185`).

**Requirement term** (*term* for short): one of the 46 words the first pass collected for what an act
requires of a person. Each is classified in §1.5 as exactly one of **BASE INPUT** (the term is a use of
one base input), **DERIVED SCORE** (of which inputs), **LEARNED SKILL**, **USE OF A DERIVED SCORE**,
**LIMIT** or **TEMPERAMENT**.

- ⚠ **Why not "aptitude".** The first pass called these words *aptitudes*. The tree uses that word in
  three other senses: a learned skill (*"History (a person's combat aptitude)"*,
  `modules/combat/core.py:106-107`; *"martial aptitude (Combat ≥ …)"*, `faction_politics_v30.md:541`);
  an attribute input (V-3's *"aptitude slot"*, `10_verbs_and_attributes.md:199`, and *"how aptitude
  enters today"* for the derived per-beat faculties, `:140`); and a progression slot, *"Aptitude
  (rate/price, never rolled)"* (`proposals/2026-08-15-character-and-faction-stats-and-progression.md:1288`).
  *Requirement term* collides with nothing: `git grep -i "requirement term"` prints nothing. The file
  `_aptitudes.md` keeps its name for continuity only.
- It avoids "axis" (the engine's `AXES` roster), "capacity" as a type name, "Retention" (`examine`'s
  obstacle, `04_VERBS.md:455`; a roster owner, `rosters.yaml:2002`) and "equivalence class" (§6).
- Codes STR AGI END FOC ACU WIL ATT CHA BON are the registry's nine
  (`references/descriptor_registry.yaml:33-48`); REC, TS, RES and TMP are the character template's
  (`proposals/2026-10-16-character-template_part2.md:34-57`); BODY is `Person.body`
  (`engine/season/state/carriers.py:667`).

**The evidence grammar.** A **draw** is one item (a practice domain, a verb or a subsystem, `_part2`)
requiring one term. It is written `` `term` (roles, [key] basis: …) ``.

- **Roles**: odds (adds to a pool), difficulty/cost (sets or resists an obstacle or a cost),
  eligibility (a gate or a cap), effect size (how much lands), resists another (the person as someone
  else's obstacle). A draw may carry several, joined by ` + `. ⚠ **A role carries no magnitude**: a
  gate and a 0.25-weight noise term count alike. Roles say how, never how much.
- **A key is one source statement, or one inference.** §1.5 counts **distinct statements** per term:
  a key counts once however many items (domain, verb, subsystem) draw on it, at its best basis. Draw
  entries are shown too, and they re-count by construction.

**Evidence tiers** are the character template's. **T1** is code the season loop runs on a per-person
value. **T2** is code outside the loop (`modules/`, `systems/*/sim/`), or loop-run code on a class
default. **T3** is a ratified specification, a v9 plan position, or a proposal the plan records as
RATIFIED AS INTENT. **T4** is design intent only: unratified proposals, the quarantined `.designs/`
documents and `research/by_lane/`. Under `CLAUDE.md` §0.05 no design document shows a behaviour is
correct. **The sources are cited for what a design says an act REQUIRES: intent, not mechanism.**

- ⚠ **T1 is not empty.** The season loop builds each fighter from one per-person number, `end`,
  derived from BODY: `max(1, 4 − body bands)` (`engine/season/seam/wrappers/combat.py:130-138`;
  `engine/season/queries/inputs.py:51`). That one input drives `stamina_max`, the Wound Interval, Max
  Wounds and Health in the fight the loop runs. Every other Combatant field is the class default. So
  at T1 the one personal input is itself a derived score (D13), and the terms `stamina` and
  `toughness` are NAMED at T1.
- **NAMED (Tn)**: the source states the requirement.
- **overridden**: named at T4 but overridden for DICE by a higher source. Three causes:
  - **by the kernel**: a `social_contest_v30` (SCV) draw. The T2 contest kernel binds `faculty` (a
    practice) and `charisma` (`resolver.py:184-195`); `charisma` sets only Face's ceiling, a view no
    outcome reads (`:226-236`). So SCV's attribute pools are superseded for dice.
  - **by the 2026-09-05 gloss**: an inquiry act's dice. Contestable (`_part2` §3 note 1, which also
    says why the gloss reaches `investigation_systems_v30.md:243`).
  - **by the T3 row**: the T3 `conceal` row has no roll (one draw, #52).

  A gate is not dice, and no cause reaches it. **Overridden statements are shown, and are not weighted
  as source-stated**: §1.5 orders by NAMED statements alone.
- **INFERRED**: this proposal's reasoning. An inference never overrides a sourced statement. **Where a
  source names only a base input or a derived score, and not the function, the choice of term is
  INFERRED; the base input or derived score is still NAMED in §1.2 or §1.4.** That is why the four
  Command-derived terms are INFERRED in `_part2` and Command is NAMED T2 in §1.2.

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
`combatant.py`, `core.py` (all `modules/combat/`); `modules/mass_battle/core/exchange.py`;
`modules/mass_battle/orchestration.py`; `modules/mass_battle/hierarchy/units.py`;
`systems/social_contest/sim/contest/resolver.py`; `systems/threadwork/sim/operations.py`;
`systems/fieldwork/sim/knots.py`; `engine/season/seam/wrappers/combat.py`. Tagged *not opened*:
`combat_c4_draft_v0.md:127` (grep only).

**How the verb interrogation differs from the character template's matrix.** The template asks what a
resolver READS off a person (43 of 65 verbs read nothing, true of the code). This proposal asks what
performing the act well REQUIRES of the person when complete. Twelve of the template's zero rows carry
requirements here (`_part2` §4). Every template read stays visible in `_part2`'s *resolver* column.

**Method, and fan-out.** One producer, no subagent spawned in either pass. This pass is one
restructure in which every table feeds the next (the evidence keys feed §1.5, the stack tables feed
§1.6 and `_part3` §7), so the reading cannot be shared out without the verdict travelling with it; a
second producer would buy independence on the classification, and the relay already buys that more
cheaply with the critic stage and the divergence test that follows this correction. **An independent
Opus critic has read the first two passes**; both reconciliations are tables at the end of `_part3`.

---

## 1. THE STACK

### 1.1 Layer 1: base inputs

| B | code | base input | where it is held | scale | status |
|---|---|---|---|---|---|
| B01 | `STR` | Strength | registry :37; `Combatant.strength` (combatant.py:96) | 1–7 | registry attribute |
| B02 | `AGI` | Agility (alias Dexterity) | registry :39; `Combatant.agi` (:96) | 1–7 | registry attribute |
| B03 | `END` | Endurance (alias Vitality) | registry :38; `Combatant.end` (:96); on the season path derived from BODY (D13) | 1–7 | registry attribute |
| B04 | `FOC` | Focus | registry :41; `Combatant.focus` (:97) | 1–7 | registry attribute |
| B05 | `ACU` | Acuity (aliases Reasoning, Cognition: *"[ASSUMPTION] … Jordan veto"*) | registry :42; `Combatant.cog` (:97); `derive_command(cognition)` | 1–7 | registry attribute |
| B06 | `WIL` | Will (alias Spirit) | registry :43; `Combatant.spirit` (:97); the thread and knot actors' `spirit` | 1–7 | registry attribute |
| B07 | `ATT` | Attunement (alias Perception) | registry :45; `Combatant.att` (:97) | 1–7 | registry attribute |
| B08 | `CHA` | Charisma (alias Presence) | registry :47; `derive_command(charisma)`; the contest spec's `charisma` | 1–7 | registry attribute |
| B09 | `BON` | Bonds (aliases Sincerity, Affability) | registry :48; the knot actor's `bonds` | 1–7 | registry attribute |
| B10 | `REC` | Recall | **not in the registry** (the tenth is unnamed, :30-31); **no code field**: `git grep -i recall -- '*.py'` finds only Command's recall roll and the contest's per-source citation count; rolled in designs (FW:95, :306; SCV:155; threadwork_v30:688) | 1–7 (HIST:517) | candidate (J-T2) |
| B11 | `TS` | Thread Sensitivity | registry :64, a practitioner stat; the thread and knot actors' `ts`; a Track that **grows** by exposure (derived_stats_v30:578; HIST:127, :324; FW:254) | 0–100+ | own field (J-T1a), not a 1–7 attribute |
| B12 | `RES` | resilience | a duck-typed slot the thread module reads, *"a placeholder"* at gain 0 (operations.py:142-147, :264-275); canon: *"how resilient their spirit is"* (:144) | int ≥ 0 | candidate (the plan's *"'spirit' (resilience, R-14)"*, v9 _part5.md:444) |
| B13 | `BODY` | the body's condition | `Person.body` (carriers.py:667), the season loop's one personal state | condition scale | a state, not an attribute |
| B14 | `TMP` | temperament | `Combatant.disp` (combatant.py:99), *"disposition / temperament, aggression axis"* | 1–7 | temperament, not a capacity |

### 1.2 Layer 2: derived scores

Every derived score the sources define for a person, each re-opened at the locator. A score's basis
is the tier of the source that writes its formula. *Terms* are the §1.5 terms it carries.

| D | derived score | formula | base inputs | basis | locator | terms |
|---|---|---|---|---|---|---|
| D01 | Tempo | `BASE + K·(AGI − 4) − penalties`, × (1 − K·fatigue) × poise | `AGI` | NAMED T2 | combat_systems.py:113-116 | quickness |
| D02 | Reflex | `(w₁·AGI + w₂·ATT) / (w₁ + w₂)` | `AGI` `ATT` | NAMED T2 | combat_systems.py:172 | reflexes |
| D03 | Balance | `(½AGI + ½STR − 1 + skill('balance'))` × fatigue × poise; *"NOT a stat … GOVERNED BY AGILITY"* | `AGI` `STR` | NAMED T2 | combat_systems.py:184-188 | balance |
| D04 | Initiative emphasis | `K·ΔAGI + K·ΔReading + K·ΔHistory`, × the tempo channel | `AGI` `ACU` `ATT` | NAMED T2 | combat_systems.py:1416-1421 | quickness, anticipation |
| D05 | Counter success | `base + K·(History − 3) + K·(Reflex − 3) + ability`, bounded | `AGI` `ATT` | NAMED T2 | combat_systems.py:1438-1444 | reflexes |
| D06 | Reading | `(2·ACU + ATT)/3 + K·(History − 3)` | `ACU` `ATT` | NAMED T2 | combat_systems.py:171 | anticipation |
| D07 | Impact | `STR + heft` | `STR` | NAMED T2 | core.py:560-571 | strength |
| D08 | Handling penalty | `K·max(0, weapon's strength demand − STR) + K·fatigue` | `STR` | NAMED T2 | combat_systems.py:174-179 | strength |
| D09 | Bind and wind Strength term | `K·(STR_a − STR_d)` in the bind; `(strength − opponent's)` in the wind | `STR` | NAMED T2 | combat_systems.py:1062; :349 | strength |
| D10 | Durability | `WI = round(END + 4 + 0.4·WIL)`; `MW = min(⌊END/2⌋ + 1, 3)`; `Health = round(WI·(MW + 1) + 0.25·STR·END)` (the WIL and STR terms are labelled noise, *"reduces uniformity"*, combatant.py:20-21) | `END` `WIL` `STR` | NAMED T1 | combatant.py:20-42; derived_stats_v30:73-75 | toughness |
| D11 | Stamina reserve | `3·END + 2·WIL` | `END` `WIL` | NAMED T1 | combatant.py:45-47; derived_stats_v30:106 | stamina |
| D12 | Take a Breath | `(END + combat History) × 2`, capped at the reserve | `END` | NAMED T4 | derived_stats_v30:110 | stamina |
| D13 | Season `end` | `max(1, 4 − body bands)` | `BODY` | NAMED T1 | engine/season/seam/wrappers/combat.py:130-138; engine/season/queries/inputs.py:51 | stamina, toughness |
| D14 | Concentration tracker | `3·FOC + 2·WIL`; sets consistency and mental fatigue in combat; depletes per exchange in the contest | `FOC` `WIL` | NAMED T2 | combatant.py:147; combat_systems.py:1423-1431; derived_stats_v30:159; SCV:267 | concentration |
| D15 | Disruption resistance | `logistic(K·(FOC − 3))` | `FOC` | NAMED T2 | combat_systems.py:1449-1452 | concentration |
| D16 | Poise regathering | `poise + R·(1 + K·(FOC − 3))·(1 − poise)` | `FOC` | NAMED T2 | combat_systems.py:1433-1436 | concentration |
| D17 | Disposition lean | `(TMP − 4)/3` | `TMP` | NAMED T2 | combat_systems.py:180-182 | boldness |
| D18 | Command | `clamp(round((2·CHA + ACU)/3), 1, 7)`; its uses: span of control (MB:309), recall (orchestration.py:2585-2590), feint recognition (:2593-2599), tactic execution (MB:312), troop Discipline and Morale start (MB:209-210, :230), re-establishing command (MB:343-344) | `CHA` `ACU` | NAMED T2 | exchange.py:57-66; MB:306 | leadership, tactical-read, situational-awareness |
| D19 | Resolution pool | `max(5, History + 6)`: attribute-independent (ED-901) | — | NAMED T2 | core.py:54-56 | — |
| D20 | Focus defence | `⌊FOC/2⌋ × 3` strain absorbed | `FOC` | NAMED T4, overridden for dice by the kernel | SCV:199; derived_stats_v30:149 | concentration |
| D21 | Charisma strain modifier | `max(0, ⌊(CHA − 3)/2⌋) × 3` strain dealt | `CHA` | NAMED T4, overridden for dice by the kernel | SCV:198; derived_stats_v30:148 | presence |
| D22 | Face | `Face_max = CHA × 3`; `Face_current = round(Standing/10 × Face_max)`; moves no outcome | `CHA` | NAMED T2 | resolver.py:226-236; SCV:247 | presence |
| D23 | Standing, Rank, Credit, Reserve | the kernel's trackers, built from the spec (`standing_start`, `reserve_max`) and by ethos | — | NAMED T2 | resolver.py:202-215 | — |
| D24 | Composure | `CHA × 3` (earlier `Cha + 6`); retired as the contest tracker by CR3, still charged by threadwork | `CHA` | NAMED T4 | derived_stats_v30:136-140, :554; SCV:242-247; threadwork_v30:177 | concentration (by the merge, §1.5) |
| D25 | Appraise pool | `ATT + REC` | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | SCV:155, :511 | reading-people, memory |
| D26 | Appraise Ob | `⌈opponent's CHA ÷ 2⌉`, min 1 | `CHA` | NAMED T4, overridden for dice by the kernel | SCV:155 | presence |
| D27 | Impress Ob | `⌊NPC's ACU ÷ 2⌋ + 1` | `ACU` | NAMED T4 | FW:411 | reasoning |
| D28 | Cover | `ACU + most relevant History`; sets Exposure thresholds (*"Cover (Derived Value)"*) | `ACU` | NAMED T4 | FW:575-577 | reasoning |
| D29 | Resolve / Inspiration cap | `WIL × 1` | `WIL` | NAMED T4 | derived_stats_v30:178, :557 | devotion |
| D30 | Thread Fatigue threshold | `WIL × 5`; meditation clears it by WIL | `WIL` | NAMED T4 | threadwork_v30:195, :203; derived_stats_v30:239 | contact-endurance |
| D31 | Operations per contact | `FOC − 1` | `FOC` | NAMED T4 | threadwork_v30:199; derived_stats_v30:258-266 | concentration |
| D32 | Thread pool | `2·WIL + min(3, History + 3) + ⌊TS/10⌋` (also the Thread-Read pool, FW:305) | `WIL` `TS` | NAMED T2 | operations.py:235-247; threadwork_v30:163 | will, thread-sensitivity |
| D33 | Thread Pool Score | `⌊TS/10⌋` | `TS` | NAMED T2 | registry :65; operations.py:244 | thread-sensitivity |
| D34 | Coherence-cost resistance | `RESILIENCE_GAIN × RES` toward zero; the identity at the shipped gain 0 | `RES` | NAMED T2 | operations.py:249-275 | self-coherence |
| D35 | Dissolution Ob on a person | `END + WIL + armour` | `END` `WIL` | NAMED T4 | threadwork_v30:82 | toughness |
| D36 | Knot cap | `⌊BON/2⌋ + 1` | `BON` | NAMED T2 | knots.py:201-203 | relational-depth |
| D37 | Effective Recall | `REC − 1` (Fragmented), `REC − 2` (Fractured, Severed) | `REC` | NAMED T4 | HIST:36 | breadth |
| D38 | Spark bonus and spark check | `⌊REC/2⌋` dice on spark checks; the check is `WIL + ⌊REC/2⌋` | `REC` `WIL` | NAMED T4 | HIST:35, :41 | learning |
| D39 | Equip slots (a LIMIT) | set by REC; `REC ≥ 5` equips all | `REC` | NAMED T4 | HIST:517, :521 | breadth |
| D40 | Practice depth ceiling (a LIMIT) | the *"skill depth ceiling"*; History points *"per Recall cap per History"* | `REC` | NAMED T4 | HIST:517, :522 | practice-ceiling |
| D41 | Negotiate Ob | `⌊NPC's highest relevant stat ÷ 2⌋ + 1`; the input is not named | — | NAMED T4 | FW:413 | — |

**Checked and found to be USES, not derived scores** (one input, the ×2 convention, a practice
addend): the knot formation roll, `spirit × 2 + history_relationships` (knots.py:212-215); the Argue
pool, `(Primary × 2) + History`, whose input the adjudicator sets (SCV:129-135); the Concealment pool,
`Cognition × 2 + History` (FW:361). They are §1.4 rows. **Not person-level:** army Morale (a unit
quantity that reads Command, derived_stats_v30:407) and every faction meter (derived_stats_v30 §8).

### 1.3 Layer 3: learned skills

**How they are gained.** History is allocated at creation, *"per Recall cap per History"* (HIST:522).
A Histories skill is a starting skill (★, HIST:205) or on a History's spark list; it sparks after a
meaningful roll at Ob ≥ 2 on the spark check (D38, HIST:41); Level 2 needs History dice_bonus ≥ 3 and
Level 3 ≥ 5, each plus a spark (HIST:43). § and *unique* are the source's own marks. **The Histories
rows are a sweep, not a sample:** every Histories skill whose effect text names an attribute, a pool
or a derived score, found by the pattern in the command's comment. Skills that name none (Riposte,
Formation Discipline and the rest) are not listed one by one.

| L | learned skill | how gained | where it enters | base inputs it enters on | basis | locator |
|---|---|---|---|---|---|---|
| L01 | combat History (`Combatant.history`) | allocated | the resolution pool (D19), Reading (D06), the counter (D05), initiative (D04), Take a Breath (D12) | `ACU` `ATT` `AGI` `END` | NAMED T2 | combatant.py:98; core.py:54-56 |
| L02 | thread History | allocated | the thread pool (D32), capped +3D | `WIL` `TS` | NAMED T2 | operations.py:238-246 |
| L03 | relationship History (`history_relationships`) | allocated | the knot formation roll (U22) | `WIL` | NAMED T2 | knots.py:213-214 |
| L04 | `capability` keys (`Person.capability`) | written by `train` where a case names a vocation (IN-12 step 9) | the sigma pool; reads no base input | — | NAMED T1 | carriers.py:651; rosters.yaml:1082-1107 |
| L05 | contest `faculty` | the spec | the kernel's pool and leverage | — | NAMED T2 | resolver.py:184-195, :300-301 |
| L06 | Combatant `skills` (bind, parry, dodge, balance, technique, grab) | set at build | Balance (D03); the dodge and wind σ | `AGI` `STR` | NAMED T2 | combatant.py:115; combat_systems.py:188, :1057-1060 |
| L07 | `equipped` techniques (`{name: level}`) | levels of investment (ED-PC-0023); AUG's Investment slot | channel ability factors, e.g. the counter (D05) | `AGI` `ATT` | NAMED T2 | combatant.py:116; combat_systems.py:1442; AUG:1285 |
| L08 | `tradition` (the school) | set at build | channel reweighting; familiarity scales the bind read (D06) | `ACU` `ATT` | NAMED T2 | combatant.py:101; combat_systems.py:1058-1061; AUG:168-176 |
| L09 | tactic cards | — | tactic execution, Command dice (MB:312) | `CHA` `ACU` | NAMED T4 | AUG:1285 (`tactic_cards = {}`) |
| L10 | Histories skill levels and sparking | the rule above | the acquisition of L11–L54, through the spark check (D38) | `WIL` `REC` | NAMED T4 | HIST:41, :43 |
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
| L23 | Institutional Instinct | § | +1D on Appraise (D25) | `ATT` `REC` | NAMED T4, overridden for dice by the kernel | HIST:93 |
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
| L42 | Economic Reasoning | § | +1D to the Argue pool; the adjudicator sets the input | — | NAMED T4, overridden for dice by the kernel | HIST:242 |
| L43 | Crisis-Forged Conviction | ★ unique | +1D Argue on Church doctrine | — | NAMED T4, overridden for dice by the kernel | HIST:474 |
| L44 | Veteran's Eye | ★ unique | +1D on Command tactic rolls (D18) | `CHA` `ACU` | NAMED T4 | HIST:462 |
| L45 | Smooth Liar | ★ § | −1 strain when using Obscuring, a contest move | — | NAMED T4 | HIST:339 |
| L46 | Intimidation | ★ § | +1D Obscuring in private negotiation | — | NAMED T4 | HIST:349 |
| L47 | Shadow Work | § | +1D surveillance and counter-intelligence (Surveil rolls Cognition, FW:304) | `ACU` | INFERRED | HIST:339 |
| L48 | Garrison Eyes | unique | +1D detect infiltration | `ACU` | INFERRED | HIST:311 |
| L49 | Precision Hands | § | +1D examining crafted objects: a perceptual examination (Examine rolls Cognition, FW:93), not exactness of execution | `ACU` | INFERRED | HIST:350 |
| L50 | Dead Drop | ★ unique | −1 Ob on Intel ops, which roll the faction's Intel | — | NAMED T4 | HIST:339, :505 |
| L51 | Craft Expertise | ★ unique | +2D on any roll involving the craft | — | NAMED T4 | HIST:241 |
| L52 | Folk Healer | ★ unique | +1D Medicine, a roll that names no input | — | NAMED T4 | HIST:362 |
| L53 | Field Medicine | ★ unique | −1 Ob stabilise | — | NAMED T4 | HIST:378 |
| L54 | Haggler's Nerve | ★ § | −1 strain in private negotiation (strain is what the Focus defence absorbs, D20) | `FOC` | INFERRED | HIST:312 |
| L55 | Literacy | by Formation; *"available as spark"* for the self-taught | presupposed by records and research | — | NAMED T4 | HIST:44-55 |
| L56 | Mentor | a rank's named NPC | *"+1D on one specified roll per season"*: a held bonus die, not a learning rate | — | NAMED T4 | faction_politics_v30:56 |
| L57 | Officer practice | — | *"named officer with Cavalry History"* gates a troop type | — | NAMED T4 | military_layer_v30:132-133 |
| L58 | Investment, Practice and Record slots | — | the 2026-08-15 progression slots | — | NAMED T4 | AUG:1285-1287 |

### 1.4 Layer 1 read by layer 4: every sourced USE of a base input

One row per source statement that names a base input alone in a roll, check, gate or pool. A row is
INFERRED where the statement's input is not one the registry names (*"Intellect"*, a *"Coherence
check"*, a *"Composure check"*). *Term* is the `_part2` coding.

| U | statement | base inputs | basis | locator | term |
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
| U20 | Practitioner inference from census data: an *"Intellect check"* (no registry alias) | `ACU` | INFERRED | npc_behavior_v30:350, :352 | reasoning |
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
| U64 | A monster hex, a non-practitioner: a *"Composure check"* (Composure is `CHA × 3`, D24) | `CHA` | INFERRED | valoria_ui_ux_v4_1:916 | concentration |

**No source uses STR, FOC, BODY or TMP alone.** Strength and Focus reach every act through derived
scores (D03, D07–D10, D14–D16, D20, D31); BODY only through `end` (D13); temperament only through the
lean (D17).

### 1.5 The 46 requirement terms, classified

**Key.** *Class* is exactly one of the six (Words). *Of* names the base input a BASE INPUT term is a
use of, or the derived score a DERIVED SCORE or USE term is. *Group* is §6's one grouping. Columns P, V
and S count the practice domains, verbs (distinct resolvers in brackets) and subsystems that draw the
term. **Draws** counts draw entries, which re-count. **Statements** count distinct keys at their best
basis: **named** (by tier), **overridden** (by cause) and **inferred**, each once. **Order: by named
statements, then by name.** Overridden statements are shown and do not order the list.

| T | term | class | of | group | P | V [res] | S | draws | named statements (by tier) | overridden (by cause) | inferred | flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T01 | `reasoning` | BASE INPUT | `ACU`, used directly (U08–U21) and in D27, D28 | ACU | 7 | 5 [5] | 5 | 26 | 10 (T4 10) | 1 (kernel 1) | 3 | conditional on the Cognition alias (registry :42) |
| T02 | `thread-sensitivity` | BASE INPUT | `TS`, used directly (§1.4 U57–U61) and in D32, D33 | TS | 4 | 10 [4] | 6 | 23 | 9 (T2 2 · T3 1 · T4 6) | 0 | 1 | also rolled on ATT (FW:91; L16–L21): `_part3` S-defect 5 |
| T03 | `steadfastness` | BASE INPUT | `WIL`, used directly (U28–U32); `ACU` at U19 | WIL | 0 | 0 [0] | 4 | 7 | 6 (T4 6) | 0 | 0 | two ladders: Spirit in five statements, Cognition in one (S-defect 4) |
| T04 | `will` | BASE INPUT | `WIL`, used directly (U22–U25) and in D32 | WIL | 2 | 10 [4] | 3 | 17 | 6 (T2 2 · T4 4) | 0 | 0 | — |
| T05 | `presence` | BASE INPUT | `CHA`, used directly (U42–U48) and in D21, D22, D26 | CHA | 4 | 4 [4] | 5 | 18 | 4 (T4 4) | 2 (kernel 2) | 2 | — |
| T06 | `concentration` | DERIVED SCORE | D14 Concentration tracker (FOC, WIL); also D15, D16, D20, D31 | FOC | 8 | 12 [5] | 5 | 26 | 3 (T2 1 · T4 2) | 1 (kernel 1) | 5 | merged: absorbs composure and nerve (Merges) |
| T07 | `memory` | BASE INPUT | `REC`, used directly (U54, U56) and in D25 | REC | 5 | 2 [2] | 5 | 13 | 3 (T4 3) | 2 (2026-09-05 gloss 1 · kernel 1) | 2 | — |
| T08 | `reading-people` | BASE INPUT | `ATT`, used directly (U35–U40) and in D25 | ATT | 5 | 4 [4] | 6 | 15 | 3 (T4 3) | 2 (2026-09-05 gloss 1 · kernel 1) | 3 | — |
| T09 | `relational-depth` | BASE INPUT | `BON`, used directly (U51–U53) and in D36 | BON | 2 | 2 [2] | 2 | 6 | 3 (T2 1 · T4 2) | 0 | 0 | — |
| T10 | `self-coherence` | DERIVED SCORE | D34 Coherence-cost resistance (RES) | RES | 1 | 6 [1] | 3 | 10 | 3 (T2 1 · T4 2) | 0 | 0 | dark: gain 0 |
| T11 | `stamina` | DERIVED SCORE | D11 Stamina reserve (END, WIL); also D12, D13 | END | 4 | 6 [5] | 6 | 16 | 3 (T1 1 · T4 2) | 0 | 5 | — |
| T12 | `breadth` | LIMIT | D39 Equip slots (REC); D37 Effective Recall | REC | 0 | 1 [1] | 1 | 3 | 2 (T4 2) | 0 | 0 | a LIMIT on Recall |
| T13 | `devotion` | DERIVED SCORE | D29 Resolve / Inspiration cap (WIL) | WIL | 0 | 0 [0] | 2 | 2 | 2 (T4 2) | 0 | 0 | — |
| T14 | `observation` | BASE INPUT | `ACU`, used directly (U09, U10, U18) | ACU | 5 | 3 [3] | 4 | 12 | 2 (T4 2) | 2 (2026-09-05 gloss 2) | 3 | — |
| T15 | `persuasiveness` | BASE INPUT | `CHA`, used directly (U44, U49, U50) | CHA | 3 | 4 [4] | 4 | 11 | 2 (T4 2) | 1 (2026-09-05 gloss 1) | 6 | — |
| T16 | `spatial-sense` | BASE INPUT | `ACU`, used directly (U07) | ACU | 3 | 0 [0] | 2 | 5 | 2 (T4 2) | 0 | 1 | — |
| T17 | `toughness` | DERIVED SCORE | D10 Durability (END, WIL, STR); also D13, D35 | END | 1 | 2 [1] | 3 | 6 | 2 (T1 1 · T4 1) | 0 | 1 | — |
| T18 | `anticipation` | DERIVED SCORE | D06 Reading (ACU, ATT); also D04 | ACU | 2 | 3 [2] | 2 | 7 | 1 (T2 1) | 0 | 1 | its feint draws are uses of Command (INFERRED) |
| T19 | `balance` | DERIVED SCORE | D03 Balance (AGI, STR) | AGI | 2 | 2 [1] | 1 | 5 | 1 (T2 1) | 0 | 1 | — |
| T20 | `boldness` | TEMPERAMENT | D17 Disposition lean (TMP) | TMP | 1 | 2 [1] | 2 | 5 | 1 (T2 1) | 0 | 1 | a lean, not a capacity |
| T21 | `contact-endurance` | DERIVED SCORE | D30 Thread Fatigue threshold (WIL) | WIL | 1 | 7 [1] | 1 | 9 | 1 (T4 1) | 0 | 0 | merged: absorbs recovery |
| T22 | `empathy` | BASE INPUT | `ATT`, used directly (U06, U38) | ATT | 2 | 1 [1] | 2 | 5 | 1 (T4 1) | 0 | 1 | — |
| T23 | `hardiness` | BASE INPUT | `END`, used directly (U03, U05) | END | 1 | 1 [1] | 2 | 5 | 1 (T4 1) | 0 | 2 | — |
| T24 | `judgment` | BASE INPUT | `CHA` or `ACU`, used directly (U15) | CHA | 2 | 1 [1] | 4 | 7 | 1 (T4 1) | 0 | 3 | Hold Court names CHA or ACU; grouped by the first named |
| T25 | `land-sense` | LEARNED SKILL | L12 Seasons Reader, on `ACU` | ACU | 2 | 0 [0] | 1 | 3 | 1 (T4 1) | 0 | 0 | a skill bonus on a Cognition roll |
| T26 | `learning` | DERIVED SCORE | D38 Spark bonus (REC, WIL) | REC | 1 | 1 [1] | 1 | 3 | 1 (T4 1) | 0 | 1 | — |
| T27 | `practice-ceiling` | LIMIT | D40 Practice depth ceiling (REC) | REC | 0 | 1 [1] | 1 | 2 | 1 (T4 1) | 0 | 0 | a LIMIT on Recall |
| T28 | `quickness` | DERIVED SCORE | D01 Tempo (AGI); also D04 | AGI | 2 | 2 [1] | 2 | 7 | 1 (T2 1) | 0 | 3 | — |
| T29 | `reflexes` | DERIVED SCORE | D02 Reflex (AGI, ATT); also D05 | AGI | 1 | 2 [1] | 1 | 4 | 1 (T2 1) | 0 | 0 | — |
| T30 | `sincerity` | BASE INPUT | `WIL`, used directly (U27) | WIL | 2 | 1 [1] | 1 | 4 | 1 (T4 1) | 0 | 1 | registry aliases it to BON; sources roll WIL (FW:430, :822): S-defect 2 |
| T31 | `strength` | BASE INPUT | `STR`, only through D03, D07–D10 | STR | 3 | 3 [2] | 2 | 8 | 1 (T2 1) | 0 | 2 | moves odds, cost and effect size |
| T32 | `deception` | LEARNED SKILL | L45 Smooth Liar, L46 Intimidation (Obscuring) | practice | 1 | 1 [1] | 2 | 4 | 0 | 0 | 3 | **ALL INFERRED**; the skills are on the Obscuring move |
| T33 | `dexterity` | BASE INPUT | `AGI`, by the registry alias only | AGI | 3 | 4 [4] | 2 | 9 | 0 | 0 | 5 | **ALL INFERRED**; no code reads `agi` for hand work |
| T34 | `discernment` | BASE INPUT | `ATT` (FW:94 "calibrating trust") | ATT | 0 | 2 [2] | 2 | 4 | 0 | 0 | 2 | **ALL INFERRED**; AX-7 "competence" may be practice |
| T35 | `discipline` | LEARNED SKILL | practice (drill) | practice | 0 | 1 [1] | 1 | 2 | 0 | 0 | 1 | **ALL INFERRED** |
| T36 | `inference` | BASE INPUT | `REC`, used directly (U55) | REC | 1 | 1 [1] | 1 | 3 | 0 | 1 (2026-09-05 gloss 1) | 0 | overridden only (gloss) |
| T37 | `intimidation` | LEARNED SKILL | L46 Intimidation (Obscuring) | practice | 0 | 2 [2] | 0 | 2 | 0 | 0 | 1 | **ALL INFERRED** |
| T38 | `leadership` | USE OF A DERIVED SCORE | D18 Command (CHA, ACU) | CHA | 1 | 1 [1] | 3 | 5 | 0 | 0 | 3 | **ALL INFERRED as a term**; Command is NAMED T2 (D18) |
| T39 | `numeracy` | LEARNED SKILL | administrative and trade practice | practice | 3 | 1 [1] | 2 | 6 | 0 | 0 | 2 | **ALL INFERRED** |
| T40 | `patience` | TEMPERAMENT | no source | TMP | 5 | 1 [1] | 3 | 9 | 0 | 0 | 4 | **ALL INFERRED**; a lean by this proposal's reading |
| T41 | `planning` | LEARNED SKILL | administrative practice | practice | 2 | 0 [0] | 1 | 3 | 0 | 0 | 1 | **ALL INFERRED** |
| T42 | `precision` | LEARNED SKILL | craft practice (L51) | practice | 2 | 1 [1] | 1 | 4 | 0 | 0 | 3 | **ALL INFERRED**; its one source is craft practice (HIST:241); Precision Hands is perceptual (L49) |
| T43 | `quick-thinking` | LEARNED SKILL | P02 practice (the rebut move) | practice | 1 | 0 [0] | 1 | 2 | 0 | 0 | 1 | **ALL INFERRED** |
| T44 | `situational-awareness` | USE OF A DERIVED SCORE | D18 Command (CHA, ACU) | CHA | 1 | 1 [1] | 2 | 4 | 0 | 0 | 2 | **ALL INFERRED as a term**; Command is NAMED T2 (D18) |
| T45 | `tactical-read` | USE OF A DERIVED SCORE | D18 Command (CHA, ACU) | CHA | 1 | 1 [1] | 1 | 3 | 0 | 0 | 1 | **ALL INFERRED as a term**; Command is NAMED T2 (D18); "tactical read" is a docstring gloss |
| T46 | `verbal-fluency` | LEARNED SKILL | P02 practice | practice | 1 | 3 [3] | 1 | 5 | 0 | 0 | 3 | **ALL INFERRED** |

**Classes** (from the table): BASE INPUT 19, DERIVED SCORE 11, USE OF A DERIVED SCORE 3, LEARNED SKILL
9, LIMIT 2, TEMPERAMENT 2 = 46. **Fourteen terms have no named or overridden statement:** the three
Command uses, whose score is NAMED T2 (D18); `dexterity` and `discernment`, whose base input is
named but whose function is not; and the nine practice and lean terms (eight in the *practice* group,
plus `patience`). `inference` rests on one overridden statement.

**What the classification changes.** Nineteen of the 46 are a base input under another name, eleven
are a derived score, three are a use of one derived score (Command), two are limits Recall sets, two
are leans, and nine are learned skills (eight naming no base input, and `land-sense`, a skill bonus on
a Cognition roll). By J-13 none of the 32 that are not BASE INPUT is a candidate
attribute, whatever its draws. **Of the nineteen BASE INPUT terms, every one maps to one of the
registry's nine except `memory` and `inference` (Recall) and `thread-sensitivity` (TS)** (§1.6).

**Merges, kept from the first passes, and why.**

- **`composure` is in `concentration`.** In T2 combat code one tracker, 3·Focus + 2·Spirit
  (`combatant.py:147`), drains on hits and per bout and sets consistency and mental fatigue
  (`combat_systems.py:1423-1431`); AUG files it all under *Concentration*, also *Steadiness*
  (AUG:90, :413, :479); SCV's CR3 split the old Charisma × 3 *Composure* buffer into Concentration
  and Face (SCV:242-247). *Nerve* (HIST:312) is this term. ⚠ The monster-hex *"Composure check"*
  (`valoria_ui_ux_v4_1:916`) is coded here by the merge, but *Composure* is Charisma × 3 in
  `derived_stats_v30:554` (D24), so its input is unstated (U64): `_part3` S-defect 1.
- **`recovery` is in `contact-endurance`**: one track, threadwork_v30:195, :203 (D30).
- **`courage` stays out, narrowed.** Its one first-pass draw is troop Morale, which starts at Command
  plus unit quality (MB:230), a use of D18. A nerve check does exist (`valoria_ui_ux_v4_1:916`); it is
  coded to `concentration` by the merge above.
- **SCV:147 is `reading-people`**, not also empathy; **FW:306 is `inference`**, not also memory.
- *Affability* (registry :48) names no function any source draws; *vigilance* is `observation`
  sustained by `concentration`; *Perception* is Attunement's alias.
- **The first pass's splits are undone as attributes, kept as terms.** Endurance's three terms,
  Spirit's five, Cognition's five, Recall's five and Agility's four each sit in one group (§6) under
  their base input. The terms stay, because they are what the designs ask for; under J-13 they are
  uses and derived scores of one input, not candidate attributes.

### 1.6 The base inputs, with what hangs off each (the flattened list, re-issued)

**Each row is one base input.** Its derived scores (§1.2), the learned skills that enter on it
(§1.3), its sourced uses (§1.4), each counted once per source statement, and the §1.5 terms that hang
off it. *Group statements* are the distinct keys of those terms, at best basis. *Best tier* is the
highest tier at which the input carries a per-person value. The last row holds the terms that hang
off no base input. The cut test is `_part3` §9.

| code | base input | derived scores (L2) | learned skills on it (L3) | sourced uses (§1.4) | terms that hang off it | group statements named / overridden / inferred | best tier | cut test (`_part3` §9) |
|---|---|---|---|---|---|---|---|---|
| `STR` | Strength | **5**: D03 Balance, D07 Impact, D08 Handling penalty, D09 Bind and wind, D10 Durability (a noise term) | **1**: L06 | **0** | strength | 1 / 0 / 2 | T2 | holds, narrowed to combat |
| `AGI` | Agility | **5**: D01 Tempo, D02 Reflex, D03 Balance, D04 Initiative, D05 Counter | **6** (5 named, 1 inferred): L01, L06, L07, L22, L36, L37 | **3**: U01–U03 | quickness, reflexes, balance, dexterity | 3 / 0 / 9 | T2 | holds, narrowed: combat at T2, three world uses at T4 |
| `END` | Endurance | **4**: D10 Durability, D11 Stamina reserve, D12 Take a Breath, D35 Dissolution Ob | **2**: L01, L38 | **4**: U03–U06 | stamina, toughness, hardiness | 6 / 0 / 8 | T2 (BODY stands in at T1, D13) | holds |
| `FOC` | Focus | **5** (4 named, 1 overridden): D14 Concentration, D15 Disruption, D16 Poise, D20 Focus defence, D31 Operations per contact | **3** (2 retired, 1 inferred): L32, L33, L54 | **0** | concentration | 3 / 1 / 5 | T2 | holds: every requirement is through a derived score |
| `ACU` | Acuity (Cognition) | **5**: D04 Initiative, D06 Reading, D18 Command, D27 Impress Ob, D28 Cover | **13** (9 named, 1 overridden, 3 inferred): L01, L08, L09, L11–L15, L41, L44, L47–L49 | **15** (11 named, 3 overridden, 1 inferred): U07–U21 | reasoning, observation, spatial-sense, land-sense, anticipation | 15 / 3 / 8 | T2 | holds, conditional on the Cognition alias |
| `WIL` | Will (Spirit) | **8**: D10, D11, D14, D29 Resolve cap, D30 Thread Fatigue, D32 Thread pool, D35, D38 Spark check | **6**: L02, L03, L10, L21, L34, L35 | **12**: U22–U33 | will, steadfastness, sincerity, devotion, contact-endurance | 16 / 0 / 1 | T2 | holds |
| `ATT` | Attunement | **5** (4 named, 1 overridden): D02, D04, D05, D06, D25 Appraise pool | **15** (10 named, 5 overridden): L01, L07, L08, L16–L27 | **9** (7 named, 2 overridden): U06, U34–U41 | reading-people, empathy, discernment | 4 / 2 / 6 | T2 | holds |
| `CHA` | Charisma | **5** (3 named, 2 overridden): D18 Command, D21 Strain modifier, D22 Face, D24 Composure, D26 Appraise Ob | **4** (2 named, 2 overridden): L09, L39, L40, L44 | **11** (8 named, 2 overridden, 1 inferred): U15, U42–U50, U64 | presence, persuasiveness, judgment, leadership, situational-awareness, tactical-read | 7 / 3 / 17 | T2 | narrowed at T2 (Command runs on ACU alone; Face moves nothing); holds at T4 |
| `BON` | Bonds | **1**: D36 Knot cap | **0** | **3**: U51–U53 | relational-depth | 3 / 0 / 0 | T2 | narrowed: the knot gate also needs Disposition |
| `REC` | Recall | **5** (4 named T4, 1 overridden): D25, D37 Effective Recall, D38 Spark bonus, D39 Equip slots, D40 Depth ceiling | **10** (4 named, 6 overridden): L10, L23–L31 | **3** (1 named, 2 overridden): U54–U56 | memory, inference, learning, breadth, practice-ceiling | 7 / 3 / 3 | T4 | **false today**: no reader above T4 |
| `TS` | Thread Sensitivity | **2**: D32 Thread pool, D33 TPS | **2**: L02, L19 | **5**: U57–U61 | thread-sensitivity | 9 / 0 / 1 | T2 | holds, as its own field |
| `RES` | resilience | **1**: D34, dark at gain 0 | **0** | **2**, both inferred: U62, U63 | self-coherence | 3 / 0 / 0 | T2, dark | **false today**: D34 is the identity |
| `BODY` | the body's condition | **1**: D13 Season `end` | **0** | **0** | (stamina and toughness, through D13) | — | **T1** | holds at T1, as a state |
| `TMP` | temperament | **1**: D17 Disposition lean | **0** | **0** | boldness, patience | 1 / 0 / 5 | T2 | holds, narrowed to combat; a lean |
| — | none (*practice*) | 3 with no base input: D19 Resolution pool, D23 kernel trackers, D41 Negotiate Ob | 14 with no base input: L04, L05, L42, L43, L45, L46, L50–L53, L55–L58 | — | numeracy, verbal-fluency, precision, deception, planning, intimidation, quick-thinking, discipline | 0 / 0 / 15 | — | — |

**Read it bottom-up.** Every requirement the sources name reaches one of fourteen base inputs, and
nine of them are the registry's nine. The other five are Recall (rolled in designs, read by no code),
TS (its own growing field), `resilience` (a dark stub slot), BODY (a state) and temperament (a lean).
**No named statement lands on a term that hangs off no base input**: the *practice* row's 15
statements are all inferred. **The first pass's "homeless" named draws are gone**: judgment is Hold
Court (U15, CHA or ACU), anticipation is Reading (D06), situational awareness is Command (D18).

### 1.7 The command that reproduces §1.5, §1.6 and the totals

Run from the repository root. It reads the evidence draws in `_part2` and the stack tables in this
file (rows `B`, `D`, `L`, `U`, `T`), refuses a term that is in one and not the other, prints every
key with more than one basis, and prints per term, per base input, and the totals. The Histories
sweep behind §1.3 is the pattern in its first comment, run over HIST.

```sh
python3 - <<'EOF'
# L3 sweep (run separately over HIST): skills whose effect names an input, a pool or a derived score:
#   r"\*\*([A-Z][A-Za-z'’ /-]+)\*\*\s*§?\s*\(([^)]*)\)" and the vocation form "★ Name § (…)", each
#   kept if its effect matches \b(Cognition|Attunement|Recall|Spirit|Agility|Charisma|Focus|Endurance|
#   Strength|Bonds|Appraise|Argue|Command|Medicine|Obscuring|Concentration)\b
import re, collections
B = 'proposals/2026-10-16-attribute-derivation'
head, ev = open(B + '.md').read(), open(B + '_part2.md').read()
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
rows = lambda p: [cells(l) for l in head.splitlines() if re.match(r'\| ' + p + r'\d\d \|', l)]
T = {re.search(r'`([a-z-]+)`', r[1]).group(1): r for r in rows('T')}
assert set(T) == set(A), sorted(set(T) ^ set(A))
for t in A:
    for k, v in A[t]['keys'].items():
        if len(v) > 1: print('mixed key:', t, k, sorted(v))
order = sorted(A, key=lambda t: (-grp(best(A[t]), 'named'), t))
for t in order:
    a, c = A[t], best(A[t])
    print(t, '|', T[t][2], '|', T[t][4], '|', len(a['P']), f"{len(a['V'])} [{len(a['res'])}]", len(a['S']), a['n'],
          '| named', grp(c, 'named'), {k[6:]: v for k, v in sorted(c.items()) if k[0] == 'n'},
          '| overridden', grp(c, 'overridden'), '| inferred', c['inferred'])
inp = lambda s: re.findall(r'`([A-Z]+)`', s)
kind = lambda s: 'inferred' if 'INFERRED' in s else 'retired' if 'RETIRED' in s else 'overridden' if 'overridden' in s else 'named'
D, L, U = rows('D'), rows('L'), rows('U')
print('base input | derived scores | learned skills | uses | terms in group | group statements named/overridden/inferred')
for x in [r[1].strip('`') for r in rows('B')] + ['practice']:
    d = collections.Counter(kind(r[4]) for r in D if x in inp(r[3]))
    s = collections.Counter(kind(r[5]) for r in L if x in inp(r[4]))
    u = collections.Counter(kind(r[3]) for r in U if x in inp(r[2]))
    g = [t for t in A if T[t][4] == x]
    ks = {}
    for t in g:
        for k, v in A[t]['keys'].items(): ks.setdefault(k, set()).update(v)
    gc = collections.Counter(min(v, key=rank)[0] for v in ks.values())
    print(x, '|', sum(d.values()), dict(d), '|', sum(s.values()), dict(s), '|', sum(u.values()), dict(u),
          '|', len(g), '|', gc['n'], gc['o'], gc['i'])
ev_all = collections.Counter()
for a in A.values(): ev_all.update(best(a))
items = set().union(*(a['P'] | a['V'] | a['S'] for a in A.values()))
print(len(A), 'terms;', sum(a['n'] for a in A.values()), 'draw entries over',
      sum(i[0] == 'P' for i in items), 'domains,', sum(i[0] not in 'PS' for i in items), 'graded verbs,',
      sum(i[0] == 'S' for i in items), 'subsystems; statements per term:', dict(sorted(ev_all.items())))
print('classes:', dict(collections.Counter(r[2] for r in T.values())))
print('stack:', len(rows('B')), 'base inputs,', len(D), 'derived scores,', len(L), 'learned skills,', len(U), 'uses;',
      'with no base input:', sum(not inp(r[3]) for r in D), 'derived scores,', sum(not inp(r[4]) for r in L), 'learned skills')
EOF
```

Its output, at this writing, after the 46 per-term lines that §1.5 tabulates:

```
mixed key: presence fw-cover-identity ['named T4', 'overridden T3 row']
base input | derived scores | learned skills | uses | terms in group | group statements named/overridden/inferred
STR | 5 {'named': 5} | 1 {'named': 1} | 0 {} | 1 | 1 0 2
AGI | 5 {'named': 5} | 6 {'named': 5, 'inferred': 1} | 3 {'named': 3} | 4 | 3 0 9
END | 4 {'named': 4} | 2 {'named': 2} | 4 {'named': 4} | 3 | 6 0 8
FOC | 5 {'named': 4, 'overridden': 1} | 3 {'retired': 2, 'inferred': 1} | 0 {} | 1 | 3 1 5
ACU | 5 {'named': 5} | 13 {'named': 9, 'overridden': 1, 'inferred': 3} | 15 {'named': 11, 'overridden': 3, 'inferred': 1} | 5 | 15 3 8
WIL | 8 {'named': 8} | 6 {'named': 6} | 12 {'named': 12} | 5 | 16 0 1
ATT | 5 {'named': 4, 'overridden': 1} | 15 {'named': 10, 'overridden': 5} | 9 {'named': 7, 'overridden': 2} | 3 | 4 2 6
CHA | 5 {'named': 3, 'overridden': 2} | 4 {'named': 2, 'overridden': 2} | 11 {'named': 8, 'overridden': 2, 'inferred': 1} | 6 | 7 3 17
BON | 1 {'named': 1} | 0 {} | 3 {'named': 3} | 1 | 3 0 0
REC | 5 {'overridden': 1, 'named': 4} | 10 {'named': 4, 'overridden': 6} | 3 {'overridden': 2, 'named': 1} | 5 | 7 3 3
TS | 2 {'named': 2} | 2 {'named': 2} | 5 {'named': 5} | 1 | 9 0 1
RES | 1 {'named': 1} | 0 {} | 2 {'inferred': 2} | 1 | 3 0 0
BODY | 1 {'named': 1} | 0 {} | 0 {} | 0 | 0 0 0
TMP | 1 {'named': 1} | 0 {} | 0 {} | 2 | 1 0 5
practice | 0 {} | 0 {} | 0 {} | 8 | 0 0 15
46 terms; 355 draw entries over 19 domains, 34 graded verbs, 16 subsystems; statements per term: {'inferred': 80, 'named T1': 2, 'named T2': 13, 'named T3': 1, 'named T4': 63, 'overridden 2026-09-05 gloss': 6, 'overridden kernel': 6}
classes: {'BASE INPUT': 19, 'DERIVED SCORE': 11, 'LIMIT': 2, 'TEMPERAMENT': 2, 'LEARNED SKILL': 9, 'USE OF A DERIVED SCORE': 3}
stack: 14 base inputs, 41 derived scores, 58 learned skills, 64 uses; with no base input: 3 derived scores, 14 learned skills
```

**The totals, in words, as every part of this proposal quotes them.** 46 terms; 355 draw entries
over 19 practice domains, 34 graded verbs (of 65) and 16 subsystems; **171 term-statements: 79 named
(T1 2, T2 13, T3 1, T4 63), 12 overridden (kernel 6, gloss 6) and 80 inferred.** The stack: 14 base
inputs, 41 derived scores (38 with a base input), 58 learned-skill rows (44 with a base input) and 64
sourced uses. The first pass's 297 draws, 166 named, 30 overridden and 101 inferred counted draw
entries over ten subsystems and are superseded.
