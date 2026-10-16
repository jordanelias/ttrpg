# Attribute derivation: what each practice, verb and subsystem requires of a person, flattened into one list of aptitudes

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. It recommends; it decides nothing (J-T1 and J-T2 stay Jordan's).
## Lane: IN (cross-cutting), with PC, MB, SC, FI, WR, SE, FA, NPC as sources. IDs: none allocated.
## Read at the working tree of 2026-10-16 (uncommitted edits by sibling sessions present).
## Parts, in reading order: this file (head, §1 the flattened list, §2 practice domains, §3 per-practice interrogation) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§4 per-verb, §5 per-subsystem interrogation) · [`_part3`](2026-10-16-attribute-derivation_part3.md) (§6–§11, secondary: clusters, cross-tabs, the attribute recommendation, meta-rule, NERS, limits, the critic reconciliation). The flattened list alone: [`_aptitudes`](2026-10-16-attribute-derivation_aptitudes.md).

**What this answers.** Jordan, 2026-10-16: *"perform interrogation of each 'PRA' to identify what kind
of skills/aptitudes are required for each. after doing so, we are to flatten our list and collate all
of these together to see what should be an attribute."* Then: *"like our VERB interrogation is supposed
to be doing this too"*; *"ie WHAT does each verb/subsystem require"*; and *"show me the flattened
aptitude list when it's done. we will work from those to think about attributes we have."* So the
primary deliverable is the flattened list in §1. The attribute recommendation is last, in `_part3`,
and is secondary.

**Words.**

- An **aptitude** is a capacity that underlies both learning and doing: stamina, memory, reading
  people. It is what makes one person better placed than another to do a thing well before either has
  practised it. ⚠ **The tree already uses the word in two other senses, and this proposal means
  neither.** It is used for a learned skill: *"History (a person's combat aptitude)"*
  (`modules/combat/core.py:106-107`) and *"martial aptitude (Combat ≥ …)"*
  (`faction_politics_v30.md:541`) are both *practice* in this proposal's words. It is also used for an
  attribute input: V-3's *"aptitude slot"* (`10_verbs_and_attributes.md:199`) is the attribute term
  of `faculty(domain)`. No identifier `Aptitude` exists in any `.py`, `.yaml` or `.json` file, so the
  word carries no code meaning.
- A **practice** is learned domain skill that grows by doing: combat practice, administration,
  copying. In code it is a key of `Person.capability` (`engine/season/state/carriers.py:651`). It is
  the "PRA" code of the character-template proposal.
- A **draw** is one item (a practice domain, a verb or a subsystem) requiring one aptitude. Each item
  draws each aptitude at most once.
- A draw's **role** is how the aptitude would move the outcome: **odds** (it adds to a pool),
  **difficulty/cost** (it sets or resists an obstacle or a cost: wounds, strain, fatigue), **eligibility**
  (a gate or a cap), **effect size** (how much lands), or **resists another** (the person as someone
  else's obstacle).
- Every draw carries a **reason key** in brackets after its role, such as `[thread-pool]`. Draws of one
  aptitude that share a key rest on one reason (one source statement, or one inference) counted at
  several items. §1's *distinct reasons* column counts the keys.
- This proposal avoids "axis" (the engine's `AXES` roster), "capacity" as a type name, and loose "kind".
  It avoids "Retention", which the tree uses twice already: `examine` contests *vs `retention`*
  (`04_VERBS.md:455`, *"what persists"*, `:528`), and `rosters.yaml:2002` is *"THE ONE OWNER OF
  RETENTION"* of modules kept. The memory cluster and the candidate tenth are called **Recall**, the
  name the Histories design and the template already use.
  It writes "the nine" for the registry's nine attributes (`references/descriptor_registry.yaml:33-48`).
  Codes STR AGI END FOC ACU WIL ATT CHA BON, and TS, TMP, RES, REC, KIT, are the character template's
  (`proposals/2026-10-16-character-template_part2.md:34-57`).

**Evidence tiers** are the character template's. **T1** is code the season loop runs. **T2** is code
outside the loop (`modules/`, `systems/*/sim/`). **T3** is a ratified specification, a v9 plan
position, or a proposal the plan records as RATIFIED AS INTENT. **T4** is design intent only:
unratified proposals, the quarantined `.designs/` documents, and `research/by_lane/`. Under
`CLAUDE.md` §0.05 no design document shows a behaviour is correct. **Here the sources are cited as
evidence of what a design says an act REQUIRES, which is intent, not mechanism.**

- **NAMED (Tn)**: the source states the requirement, usually as the attribute it rolls and the reason it
  gives, such as the fieldwork design's *"Reasoning"* column (`FW:90-101`).
- **overridden**: named at T4 but overridden for DICE by a higher source. Each overridden draw names
  its cause, and there are three:
  - **by the kernel**: a `social_contest_v30` (SCV) design draw. The T2 contest kernel binds only
    `faculty` (`resolver.py:184-195`), so SCV's attribute pools are superseded. This is the largest
    group.
  - **by the 2026-09-05 gloss**: a fieldwork inquiry-act draw. Jordan's words, *"ignore their use of
    attributes"* (`04_VERBS.md:465-466`), are about the proceedings design's own pool column. The
    reading that they also reach the fieldwork §4.2 column is the proceedings author's gloss
    (`:473-476`). The template records that *"Jordan's words do not name it"*
    (`2026-10-16-character-template.md:297`). So this cause is **contestable** (§3 note 1).
  - **by the T3 row**: the T3 `conceal` row has no roll (one draw, #52).

  A gate or a threshold is not dice, and no cause above reaches it. Those draws stay NAMED.
- **INFERRED**: this proposal's reasoning. An inference never overrides a sourced statement. Where a
  source names only an attribute this proposal splits (Agility, Cognition, Endurance, Charisma) and not
  the function, the choice of aptitude is INFERRED.

**Abbreviated sources** (each opened in this pass unless tagged):

- **FW** `.designs/systems/fieldwork/reference/fieldwork_v30.md`
- **SCV** `.designs/systems/social_contest/reference/social_contest_v30.md` (superseded for dice by the
  T2 contest kernel)
- **HIST** `.designs/systems/characters/reference/character_histories_v30.md` (the lifepath "Histories")
- **MB** `.designs/systems/mass_battle/reference/mass_battle_v30.md`
- **AUG** `proposals/2026-08-15-character-and-faction-stats-and-progression.md`
- `threadwork_v30` is `.designs/systems/threadwork/reference/threadwork_v30.md`.
- The settlement documents are under `.designs/systems/settlements/reference/`.
- Also cited by bare filename, all under `.designs/systems/`: `derived_stats_v30.md` (read whole),
  `faction_politics_v30.md`, `npc_behavior_v30.md`, `investigation_systems_v30.md`,
  `npc_relational_graph_v30.md`, `southernmost_v30.md`, `conviction_track_v1.md`, `knots_v30.md`,
  `combat_reference_v1.md` and `fieldwork_v30_infill.md`.
- Code locators re-opened in the critic reconciliation: `combat_systems.py`, `combatant.py`,
  `wrapper.py` (all `modules/combat/`), `modules/mass_battle/core/exchange.py`,
  `modules/mass_battle/orchestration.py`, `modules/mass_battle/hierarchy/units.py`, the contest
  `resolver.py`, `sigma.py`, `fixtures.py`, `world_q.py` and `person_q.py`. `engine.py`, `knots.py`
  and `operations.py` are reused from the template's `_part2` §A.4 and were not re-opened.

**How the verb interrogation here differs from the character template's matrix.** The template's
verb × personal-input matrix (`2026-10-16-character-template_part2.md` §A.3) asks **what a resolver
READS** off a person, today or in a named stub or design. By that test 43 of 65 verbs read nothing,
and that is a true statement about the code and the sources. This proposal asks **what performing the
act well REQUIRES of the person** when the act is complete, whether or not anything reads it. A verb
the template scores 0 can therefore carry requirements here: 12 of the template's 43 zero rows do (§4,
the rows marked *graded* that the template's matrix omits). Each verb row also keeps two things apart:

- **ACT**: what the act itself asks of the actor;
- **DOMAIN**: which practice domains the act draws, interrogated once each in §3, not repeated per
  verb.

The template's reads stay visible in the column *resolver already names*. Verbs whose quality IS the
choice (`commit`, `confer`, `issue` …) carry no aptitude of their own. Their one requirement, choosing
well, is counted once, at the chooser (S10), and not 24 times. Pure bookkeeping verbs are reported as
such.

**Method, and what was not done.** The brief allowed up to six Sonnet readers for parallel batches.
**None was spawned: this lane's toolset holds no agent-dispatch tool**, so the three interrogations
were done by one reader, from one shared source pack. That costs the independence a fan-out would have
bought on the verdicts. **An independent critic has since read the evidence coding**, and its findings
are reconciled in place (the table at the end of `_part3`). The interrogation is encoded once as data.
Every count below is reproducible from the evidence tables by the command in §1.

---

## 1. THE FLATTENED APTITUDE LIST (the primary deliverable)

**Key.**

- **One row per atomic aptitude.** ⚠ **The order is by source-stated draws** (NAMED plus overridden),
  descending, then NAMED alone, then total, then alphabetical. **It is not by total**: a total counts
  each re-use of one inference again at the domain, verb and subsystem levels, so ordering by it let
  inferred repetition outrank named evidence. The total order is still shown, in *rank by total*.
- **Columns 3–5** count the practice domains (§2–§3), the verbs (§4) and the subsystems (§5) that draw
  the aptitude. Verbs carry distinct resolvers in brackets: the seven thread operations share one pool,
  and `fight` and `accept` share one bout. In parentheses: the ids of up to three items, NAMED and
  highest tier first.
- **Distinct reasons** counts the reason keys (Words): one source statement or one inference counted
  once, however many items draw on it. Where it is far below the total, the total is repetition.
- **Named / overridden / inferred** shows how many draws a source names (by tier), how many are
  overridden (by cause: kernel, gloss, T3 row; see the tiers above), and how many are inferred.
- **Flags.** **ALL INFERRED** marks a row no source names. *One reason, re-counted* marks a row whose
  draws all rest on one key. *Practice-named* marks a row whose word a source uses for a learned skill,
  so it may be practice, not aptitude. *Temperament* marks a lean, not a capacity.
- **The last column** maps the aptitude to the nine only where the registry's name or alias, or a
  source using that attribute for that function, says so. Otherwise it reads "none". **The list was
  NOT bent toward the nine** (Jordan: keep it raw). The merges, and the splits the sources forced, are
  listed under the table.

| # | aptitude: what it is | PRA domains | verbs [distinct resolvers] | subsystems | total draws | distinct reasons | named / overridden / inferred | rank by total | flags | maps to the nine today |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Thread sensitivity** (`thread-sensitivity`, perceptual): perceiving the substrate | 3 (P05, P06, P07) | 10 [4] (#42, #58, #59) | 3 (S05, S04, S09) | 16 | 5 | named T2 11·T3 1·T4 4 | 2 | — | none of the nine (TS, a practitioner stat, registry :64) |
| 2 | **Concentration (steadiness)** (`concentration`, cognitive): sustaining mental effort over time and holding it against strain, shock and disruption | 8 (P03, P05, P02) | 12 [5] (#18, #20, #58) | 4 (S01, S05, S03) | 24 | 8 | named T2 4·T4 9; overridden kernel 3; inferred 8 | 1 | merged: absorbs *composure* (head §1, Merges) | FOC (+WIL): the one tracker 3·Focus + 2·Spirit in combat code (combatant.py:147) and the contest (SCV:267); Focus defence against strain (SCV:199); operations per contact = Focus − 1 (threadwork_v30:199) |
| 3 | **Will** (`will`, volitional): persistence of intent against resistance; the force a practitioner brings to the thread | 2 (P05, P06) | 10 [4] (#42, #58, #59) | 2 (S05, S04) | 14 | 4 | named T2 11·T4 3 | 3 | — | WIL (registry name, alias Spirit) |
| 4 | **Reasoning** (`reasoning`, cognitive): logical and structural analysis | 6 (P07, P08, P09) | 5 [5] (#37, #52, #50) | 3 (S04, S06, S03) | 14 | 8 | named T4 8; overridden kernel 3; inferred 3 | 4 | — | ACU (registry alias Reasoning, :42) |
| 5 | **Presence** (`presence`, social): bearing that draws attention and carries authority | 4 (P08, P09, P16) | 4 [4] (#32, #50, #52) | 4 (S04, S06, S03) | 12 | 6 | named T4 5; overridden kernel 4·T3 row 1; inferred 2 | 7 | — | CHA (registry alias Presence, :47; SCV:134; FW:98); the Charisma × 3 buffer once called Composure is Face (SCV:242-247) |
| 6 | **Reading people** (`reading-people`, perceptual): perceiving another's state, intent or lies | 5 (P09, P10, P16) | 4 [4] (#37, #50, #12) | 5 (S06, S03, S04) | 14 | 6 | named T4 4; overridden kernel 3·gloss 3; inferred 4 | 5 | — | ATT (FW:94 "reading people, sensing deception"; SCV:135, :147 "empathetic perception") |
| 7 | **Contact endurance** (`contact-endurance`, volitional): how long one can hold contact with the thread before it breaks, and how fast that fatigue clears | 1 (P05) | 7 [1] (#58, #59, #60) | 1 (S05) | 9 | 1 | named T4 9 | 10 | one reason, re-counted; merged: absorbs *recovery* (head §1, Merges) | WIL (threadwork_v30:195, threshold = Spirit × 5; :203, meditation clears it by Spirit) |
| 8 | **Self-coherence** (`self-coherence`, volitional): resisting the erosion of one's own self under thread strain | 1 (P05) | 6 [1] (#58, #59, #60) | 2 (S05, S09) | 9 | 2 | named T2 8·T4 1 | 11 | — | none (RES, `resilience`; plan names "spirit (resilience, R-14)" a candidate input, _part5.md:444) |
| 9 | **Stamina** (`stamina`, physical): sustained exertion before fatigue | 3 (P03, P15, P17) | 6 [5] (#18, #20, #39) | 5 (S01, S04, S09) | 14 | 7 | named T2 4·T4 4; inferred 6 | 6 | — | END (+WIL): `stamina_max = 3·end + 2·spirit` (combatant.py:45-47); FW:92 |
| 10 | **Anticipation** (`anticipation`, perceptual): reading an opponent's next move | 2 (P03, P04) | 3 [2] (#18, #20, #22) | 2 (S01, S02) | 7 | 2 | named T2 7 | 16 | — | none directly: a blend, ACU + ATT (reading `(2·Cog + Att)/3`, AUG:84); in a field, Command (CHA, ACU) |
| 11 | **Relational depth** (`relational-depth`, social): capacity to form and hold deep bonds | 2 (P06, P16) | 2 [2] (#42, #37) | 2 (S04, S05) | 6 | 3 | named T2 2·T4 4 | 18 | — | BON (FW:479 "deep relational capacity that Bonds represents"; knots.py:185); registry alias Affability (:48) |
| 12 | **Observation** (`observation`, perceptual): noticing physical detail | 5 (P04, P07, P08) | 3 [3] (#36, #39, #49) | 2 (S02, S04) | 10 | 7 | named T4 2; overridden gloss 4; inferred 4 | 8 | — | ACU (FW:93 Cognition; HIST:177 Cognition to detect ambush; MB:926) |
| 13 | **Memory** (`memory`, cognitive): retaining and retrieving what one learned or saw | 5 (P13, P02, P07) | 1 [1] (#38) | 2 (S03, S04) | 8 | 4 | named T4 1; overridden kernel 2·gloss 3; inferred 2 | 13 | — | none of the nine (Recall, which the registry does not list) |
| 14 | **Toughness** (`toughness`, physical): absorbing wounds and pain before failing | 1 (P03) | 2 [1] (#18, #20) | 3 (S01, S05, S09) | 6 | 3 | named T2 4·T4 1; inferred 1 | 19 | — | END (+WIL, STR at low weight): `wound_interval`, `health_full` (combatant.py:30-42) |
| 15 | **Persuasiveness** (`persuasiveness`, social): moving another by appeal or argument | 3 (P16, P07, P10) | 4 [4] (#37, #27, #35) | 3 (S02, S04, S07) | 10 | 8 | named T4 4; overridden gloss 1; inferred 5 | 9 | — | CHA (FW:409, Converse rolls Charisma; MB:927) |
| 16 | **Strength** (`strength`, physical): raw force: lifting, striking, grappling, carrying | 3 (P03, P11, P17) | 3 [2] (#18, #20, #45) | 2 (S01, S08) | 8 | 3 | named T2 4; inferred 4 | 14 | — | STR (registry name; Impact = Strength + heft, AUG:88) |
| 17 | **Balance** (`balance`, physical): footing and whole-body control | 2 (P03, P18) | 2 [1] (#18, #20) | 1 (S01) | 5 | 2 | named T2 4; inferred 1 | 21 | — | AGI + STR (AUG:86) |
| 18 | **Boldness** (`boldness`, volitional): a disposition to press and attack rather than wait | 1 (P03) | 2 [1] (#18, #20) | 2 (S01, S10) | 5 | 2 | named T2 4; inferred 1 | 22 | temperament: a lean, not a capacity (_part3 §7.3) | none (TMP, combat `disp`) |
| 19 | **Quickness** (`quickness`, physical): speed of movement and of a body's working tempo | 2 (P03, P18) | 2 [1] (#18, #20) | 1 (S01) | 5 | 2 | named T2 4; inferred 1 | 23 | — | AGI (tempo `BASE + K·(Agi−4)`, AUG:87) |
| 20 | **Spatial sense** (`spatial-sense`, cognitive): pathfinding, maps, positions and ground | 3 (P04, P15, P11) | 0 [0] (—) | 2 (S04, S09) | 5 | 3 | named T4 4; inferred 1 | 24 | — | ACU (FW:90 Cognition, "pathfinding, cartography") |
| 21 | **Reflexes** (`reflexes`, physical): speed of reaction to what was not foreseen | 1 (P03) | 2 [1] (#18, #20) | 1 (S01) | 4 | 1 | named T2 4 | 27 | one reason, re-counted | AGI + ATT (reflex blend, AUG:85); FW:106 rolls initiative on ATT |
| 22 | **Leadership** (`leadership`, social): getting others to follow, hold and rally | 1 (P04) | 1 [1] (#22) | 3 (S02, S06, S07) | 5 | 3 | named T2 3; inferred 2 | 25 | — | CHA (Command, Charisma primary 2:1, "inspire/hold the line", exchange.py:57-66; MB:306) |
| 23 | **Hardiness** (`hardiness`, physical): resisting cold, hunger, exposure and sickness | 1 (P15) | 1 [1] (#24) | 2 (S04, S09) | 4 | 1 | named T4 3; inferred 1 | 28 | one reason, re-counted | END (FW:92 "exposure, harsh terrain"; FW:239) |
| 24 | **Sincerity** (`sincerity`, social): genuineness that others can feel | 2 (P06, P16) | 1 [1] (#35) | 1 (S04) | 4 | 2 | named T4 3; inferred 1 | 29 | — | BON by alias (registry :48 Sincerity); but FW:430 rolls Spirit (WIL) for the Sincerity Check |
| 25 | **Situational awareness** (`situational-awareness`, perceptual): tracking many moving parts at once | 1 (P04) | 1 [1] (#22) | 2 (S02, S01) | 4 | 2 | named T2 3; inferred 1 | 30 | — | none directly: CHA + ACU through Command as span of control (engine.py:93) |
| 26 | **Empathy** (`empathy`, social): feeling with another | 1 (P07) | 1 [1] (#37) | 1 (S04) | 3 | 1 | named T4 3 | 33 | one reason, re-counted | ATT (investigation_systems_v30:255, Attunement ≥ 4 for emotional approaches) |
| 27 | **Land sense** (`land-sense`, perceptual): reading weather, terrain and soil | 2 (P15, P17) | 0 [0] (—) | 1 (S09) | 3 | 1 | named T4 3 | 35 | one reason, re-counted | ACU (HIST:314, Seasons Reader rolls Cognition) |
| 28 | **Steadfastness** (`steadfastness`, volitional): holding one's beliefs and framework against shock and contradiction | 0 (—) | 0 [0] (—) | 3 (S07, S09, S10) | 3 | 3 | named T4 3 | 36 | added by the critic reconciliation (_part3 §11, finding 4) | WIL (Spirit pool or check: npc_behavior_v30:1054; faction_politics_v30:752; southernmost_v30:105; FW:822 groups these as "metaphysical grounding") |
| 29 | **Tactical read** (`tactical-read`, cognitive): reading a field to choose and carry out a tactic | 1 (P04) | 1 [1] (#22) | 1 (S02) | 3 | 1 | named T2 3 | 37 | one reason, re-counted; added by the critic reconciliation (_part3 §11, finding 3) | ACU, as Command's secondary term (exchange.py:59-60: "Cognition secondary (tactical read)") |
| 30 | **Inference** (`inference`, cognitive): assembling partial evidence into a coherent picture | 1 (P07) | 1 [1] (#41) | 1 (S04) | 3 | 1 | overridden gloss 3 | 34 | one reason, re-counted | none of the nine (FW:306 rolls it on Recall; overridden for dice) |
| 31 | **Judgment** (`judgment`, cognitive): choosing well under uncertainty and pressure | 2 (P09, P04) | 1 [1] (#22) | 4 (S06, S02, S07) | 7 | 4 | named T4 2; inferred 5 | 17 | — | none |
| 32 | **Discernment** (`discernment`, perceptual): judging how far to credit what one is told or reads | 0 (—) | 2 [2] (#8, #35) | 2 (S10, S03) | 4 | 2 | named T3 1; inferred 3 | 31 | — | ATT (FW:94 "calibrating trust"; SCV:135 "calibrate"); AX-7's reader input is open (J-T9) |
| 33 | **Learning** (`learning`, cognitive): speed of acquiring and deepening a practice | 1 (P14) | 1 [1] (#51) | 1 (S07) | 3 | 3 | named T4 1; inferred 2 | 38 | — | none of the nine (Recall, HIST:35) |
| 34 | **Breadth** (`breadth`, cognitive): how many practices one can keep in use at once | 0 (—) | 1 [1] (#51) | 0 (—) | 1 | 1 | named T4 1 | 43 | — | none of the nine (Recall as equip slots, HIST:34, :521) |
| 35 | **Devotion** (`devotion`, volitional): depth of investment in a person, place or ideal | 0 (—) | 0 [0] (—) | 1 (S04) | 1 | 1 | named T4 1 | 44 | added by the critic reconciliation (_part3 §11, finding 4) | WIL ("Resolve / Inspiration cap" = Spirit × 1, derived_stats_v30:557, :178) |
| 36 | **Practice ceiling** (`practice-ceiling`, cognitive): how far one can deepen any one practice | 0 (—) | 1 [1] (#51) | 0 (—) | 1 | 1 | named T4 1 | 45 | added by the critic reconciliation (_part3 §11, finding 11) | none of the nine (Recall as the "skill depth ceiling", HIST:517, :522) |
| 37 | **Patience** (`patience`, volitional): sustaining slow, unrewarded effort | 5 (P07, P09, P11) | 1 [1] (#38) | 3 (S04, S06, S08) | 9 | 4 | inferred 9 | 12 | **ALL INFERRED** | none |
| 38 | **Dexterity** (`dexterity`, physical): fine control of the hands | 3 (P01, P11, P12) | 4 [4] (#13, #30, #48) | 1 (S08) | 8 | 5 | inferred 8 | 15 | **ALL INFERRED** | AGI by alias only (registry :39 lists Dexterity as an alias); no code reads `agi` for hand work |
| 39 | **Numeracy** (`numeracy`, cognitive): reckoning numbers, accounts and value | 3 (P09, P10, P19) | 1 [1] (#12) | 2 (S06, S08) | 6 | 2 | inferred 6 | 20 | **ALL INFERRED** | none |
| 40 | **Verbal fluency** (`verbal-fluency`, cognitive): command of words, spoken and written | 1 (P02) | 3 [3] (#27, #32, #35) | 1 (S03) | 5 | 3 | inferred 5 | 26 | **ALL INFERRED** | none |
| 41 | **Precision** (`precision`, physical): exactness in execution: fine work, copying, forgery | 2 (P01, P11) | 1 [1] (#13) | 1 (S08) | 4 | 3 | inferred 4 | 32 | **ALL INFERRED**; practice-named: HIST:350 *Precision Hands* | none |
| 42 | **Deception** (`deception`, social): misleading convincingly | 1 (P08) | 1 [1] (#28) | 1 (S04) | 3 | 3 | inferred 3 | 39 | **ALL INFERRED**; practice-named: HIST:339 *Smooth Liar* | none (FW rolls CHA for a cover identity, :620, and ACU for Cover, :575) |
| 43 | **Planning** (`planning`, cognitive): foresight and sequencing toward a goal | 2 (P09, P19) | 0 [0] (—) | 1 (S06) | 3 | 1 | inferred 3 | 40 | **ALL INFERRED**; one reason, re-counted | none |
| 44 | **Intimidation** (`intimidation`, social): compelling by threat | 0 (—) | 2 [2] (#54, #56) | 0 (—) | 2 | 1 | inferred 2 | 41 | **ALL INFERRED**; one reason, re-counted; practice-named: HIST:349 *Intimidation* | none |
| 45 | **Quick thinking** (`quick-thinking`, cognitive): finding an apt answer under time pressure | 1 (P02) | 0 [0] (—) | 1 (S03) | 2 | 1 | inferred 2 | 42 | **ALL INFERRED**; one reason, re-counted | none |
| 46 | **Discipline** (`discipline`, volitional): self-control: holding to drill, method or practice | 0 (—) | 1 [1] (#51) | 0 (—) | 1 | 1 | inferred 1 | 46 | **ALL INFERRED** | none (HIST:293 pairs Focus with "discipline" only in flavour text) |

**Totals.** 46 aptitudes; 297 draws (domains 94, verbs 117, subsystems 86). **166 are NAMED** (T2 80,
T3 2, T4 84), **30 overridden** (by the kernel 15, by the 2026-09-05 gloss 14, by the T3 row 1) and
**101 inferred**. T1 is 0: no aptitude is named by code the season loop runs. The draws come from 19
practice domains, 34 graded verbs (of 65) and 10 subsystems. They rest on **142 distinct reasons**:
72 source statements and 70 inferences. Four keys are shared by a sourced draw and an inferred draw
that leans on the same source (FW:94 at #56, FW:413 at #12 and S08, FW:239 at #24, AX-7 at #8 and
#35), so the per-row column sums to 138.

**Every draw of ten aptitudes is INFERRED**: patience, dexterity, numeracy, verbal fluency, precision,
deception, planning, intimidation, quick thinking and discipline. No source names them as
requirements, and they sit at the foot of the list. By total, patience (9 draws from 4 reasons) would
rank 12th, above Strength (14th by total, 16th here) and above anticipation, toughness, balance,
quickness and reflexes, all named in T2 code.

**Merges, and the splits the sources forced.** Each merge is one the sources make, not a convenience.

- **`composure` is merged into `concentration`, renamed "Concentration (steadiness)".** The sources
  treat the two as one faculty:
  - In T2 combat code, one tracker, 3·Focus + 2·Spirit (`combatant.py:147`), drains on hits and per
    bout (`wrapper.py:186`, `:427`, `:523`) and sets consistency and mental fatigue
    (`combat_systems.py:1423-1431`).
  - The resistance to disruption is *"Concentration disruption-resistance"* in the code's own
    docstring (`:1449-1452`). Poise regathers on Focus (`:1433-1436`).
  - AUG files all of it under one faculty, *Concentration* (AUG:90), also called *Steadiness*
    (AUG:413, :479).
  - In the contest, the Focus defence absorbs strain (SCV:197-199). SCV's ratified CR3 retired the
    Charisma × 3 *Composure* buffer as a conflation of two roles (SCV:242-247): sustained effort (now
    Concentration) and standing (now Face). So the Charisma side of the old word is `presence`, and
    the Focus side is this row. `derived_stats_v30:554` still lists *Composure = Charisma × 3*: the
    pre-CR3 reading.

  *Nerve* (HIST:312), *steadiness*, *attention span* and *sustained attention* are this aptitude.
- **`recovery` is merged into `contact-endurance`.** Its two draws were the Thread Fatigue track's own
  clearing (threadwork_v30:203), the track whose threshold is contact endurance (:195): one track,
  one aptitude. The combat *Take a Breath* refill, (Endurance + History) × 2
  (`derived_stats_v30:110`), is the same for `stamina`.
- **`courage` is gone.** Its one draw (S02) held troop Morale's per-person input to be an unnamed
  courage. MB:230 names it: Morale starts at the general's Command plus unit quality, which is
  `leadership`, already drawn there.
- **`empathy` is no longer drawn by SCV:147.** That one source cell was counted as both reading people
  and empathy, and SCV:147's *"empathetic perception"* is the source's word for reading people.
  Empathy's three draws now rest on one source: the interview Lattice's Attunement ≥ 4 gate for
  emotional approaches (`investigation_systems_v30:255`).
- **FW:306 (Reconstruct) is one draw, `inference`**, and no longer also `memory`. It rolls Recall, so
  inference maps to the Recall candidate.
- *Affability*, the registry's alias for Bonds (`descriptor_registry.yaml:48`), names no function any
  source draws. It is noted on `relational-depth` and is not a row.
- *vigilance* was not coined: it is `observation` sustained by `concentration`.
- **Split, not merged:**
  - *Endurance* splits into `stamina`, `toughness` and `hardiness`, because the sources use the one
    word for three functions: Endurance exploration (FW:92), the wound interval and health
    (`combatant.py:30-42`), and the travel exposure check (FW:239).
  - *Spirit* splits into `will`, `contact-endurance` (threadwork_v30:195, :203), `steadfastness`
    (the belief and conviction checks) and `devotion` (*"Resolve / Inspiration cap"*,
    `derived_stats_v30:557`). FW:822 (ED-503) groups Spirit's uses as *"metaphysical grounding"*:
    Resolve, the contact wound-disruption check, the Thread-Read pool, Dissonance checks and the
    Sincerity Gate.
  - *Cognition* splits into `reasoning`, `observation`, `spatial-sense`, `land-sense` and
    `tactical-read`, by the fieldwork design's own *Reasoning* column (FW:90, :93), HIST:314 and
    Command's gloss (`exchange.py:59-60`).
  - *Recall* splits into `memory`, `learning` (HIST:35), `breadth` (HIST:34, :521) and
    `practice-ceiling` (HIST:517, :522).
  - *Agility* stays split three ways, `balance`, `quickness` and `reflexes`, because the bout computes
    three distinct formulas (`combat_systems.py:113`, `:172`, `:184-188`).
  - *Self-coherence* stays distinct from `will`: it is resilience against the Coherence cost
    (`operations.py:249-274`), not a pool term.
  - *Perception*, the registry's alias for Attunement, is an umbrella word and is not a slug.

**The command that reproduces columns 3–8, the order and the totals** from this proposal's own
evidence tables, run from the repository root. A draw is written
`` `slug` (role, [key] NAMED Tn: … `` (with `, overridden for dice by the <cause>` after the tier when
overridden) or `` `slug` (role, [key] INFERRED: … ``, in exactly one cell of one evidence row. It
prints, per aptitude in list order: domains, verbs [resolvers], subsystems, total, distinct reasons,
and the evidence by tier and cause; then the totals.

```sh
python3 - <<'EOF'
import re, collections
base = 'proposals/2026-10-16-attribute-derivation'
t = open(base + '.md').read() + open(base + '_part2.md').read()
rows = [l for l in t.splitlines() if re.match(r'\| (P\d\d|S\d\d|\d+) \|', l) and l.count(' | ') >= 6]
D = re.compile(r'`([a-z-]+)` \((odds|difficulty/cost|eligibility|effect size|resists another), \[([a-z0-9-]+)\] '
               r'(?:NAMED (T\d)(?:, overridden for dice by the (kernel|2026-09-05 gloss|T3 row))?|(INFERRED))')
A = collections.defaultdict(lambda: dict(P=0, V=0, S=0, res=set(), keys=set(), ev=collections.Counter()))
for l in rows:
    i = l.split(' | ')[0][2:]
    lv = i[0] if i[0] in 'PS' else 'V'
    for s, role, key, tier, cause, inf in D.findall(l):
        a = A[s]; a[lv] += 1; a['keys'].add(key)
        if lv == 'V': a['res'].add('thread' if 58 <= int(i) <= 64 else 'bout' if i in ('18', '20') else i)
        a['ev']['inferred' if inf else ('overridden ' + cause if cause else 'named ' + tier)] += 1
tot = lambda a: a['P'] + a['V'] + a['S']
src = lambda a: tot(a) - a['ev']['inferred']
nam = lambda a: sum(v for k, v in a['ev'].items() if k.startswith('named'))
for s in sorted(A, key=lambda s: (-src(A[s]), -nam(A[s]), -tot(A[s]), s)):
    a = A[s]
    print(s, a['P'], f"{a['V']} [{len(a['res'])}]", a['S'], tot(a), len(a['keys']), dict(sorted(a['ev'].items())))
ev = sum((a['ev'] for a in A.values()), collections.Counter())
print(len(A), 'aptitudes;', sum(tot(a) for a in A.values()), 'draws;', dict(sorted(ev.items())))
EOF
```

Its last line, at this writing: `46 aptitudes; 297 draws; {'inferred': 101, 'named T2': 80,
'named T3': 2, 'named T4': 84, 'overridden 2026-09-05 gloss': 14, 'overridden T3 row': 1,
'overridden kernel': 15}`.

---

## 2. STAGE 1: EVERY PRACTICE DOMAIN

**Where a practice can live in code today.**

- `Person.capability: dict` (`carriers.py:651`).
- `rosters.yaml: verb_capability` maps `tell` and `speak` to the one key `copying`
  (`engine/season/rosters.yaml:1082-1107`). Its note: *"WHICH capability key each verb draws on is
  stated nowhere"*.
- `pool_default=2` is what everyone without a key draws (`engine/season/data/fixtures.py:381`).
- One corpus person carries a key: NPC-088, `{copying: 3}`
  (`engine/season/cases/exercises/NPC-088.yaml:30-33`).
- **No `practice_roster` exists in code.** It is the character template's proposed roster (its §6).
- `engine/season/data/cast.py` does not mention `capability`: `git grep -n capability
  engine/season/data/cast.py` printed nothing.

**Where practice lives in stubs and designs.**

- Combat's `history`, `skills`, `tradition` and `equipped` (`modules/combat/combatant.py:93-97`).
- Threadwork's `history` (`operations.py:235-247`) and the knot's `history_relationships`
  (`knots.py:212-222`).
- The contest kernel's `faculty` (`resolver.py:184-195`).
- The 2026-08-15 practice table (AUG:170), whose columns read *"investigative practice | tradecraft
  practice | forensic practice | command practice | administrative practice"* beside combat's History.
- The lifepath Histories (HIST), whose skill *Domain* column uses Scene Battle, Mass Battle, Debate,
  Investigation, Faction Play, Scene Battle (Thread), Medicine and Craft.
- The settlement actions' *"Governance History"*, *"Wealth-relevant History"*, *"Military-relevant
  History"* and *"local History"* (settlement_layer_v30.md:560-563).
- The fieldwork design's one History per action (FW:73).

**The domains, one row each.** Verb numbers are the rows of the template's master verb table
(`2026-10-16-character-template_part2.md` §A.2, 1–65).

| P | domain | sources (tier) | verbs it serves |
|---|---|---|---|
| P01 | copying (repeated copying of a text) | `rosters.yaml:1106-1107` (T1); NPC-088.yaml:19-33 (T1, corpus) | #35 `tell` (read, T1); #32 `speak` (mapped, never reached) |
| P02 | standing and the matter: argument, oratory, forensic practice, the proceeding faculty | `resolver.py:184-195`, `:300-301` (T2); `sigma.py:82-129` for contested social rows (T1/T3); AUG:170 *"forensic practice"* (T4); `10_verbs_and_attributes.md:144` (T4); SCV:129-135, :155, :197-199, :246-267 (T4, superseded for dice); HIST Debate skills, e.g. :228, :310, :349 (T4) | #8, #35, #50, #54, #56 (sigma-routed, T3); #32 (open); #5, #26, #27, #28, #44 |
| P03 | arms: personal combat (`history`; the six `skills` sub-keys bind, parry, dodge, balance, technique, grab; `tradition`; `equipped` techniques; weapon specialization) | `combatant.py:93-97` (T2); AUG §1.3, :84-92, and §10.3, :465-480 (T4); HIST:266, :311 (T4) | #18, #20; #19 |
| P04 | command: leading a field side | `Officer.command` accepts a given value (`units.py:2700-2722`, T2); AUG:145, :170 *"command practice"* (T4); HIST:267, :369, :177 (T4); officers' practice gates troop types, *"named officer with Cavalry History"* (`military_layer_v30.md:132-133`, T4) | #22; #57, #65 |
| P05 | threadwork: the Leap and the seven operations; `thread_read` is a Leap (FW:351) | `operations.py:235-247` (T2); threadwork_v30:163, :195-229 (T4); HIST:279 (T4) | #58–#64; #40 |
| P06 | relationships (the knot-forming practice) | `knots.py:212-222` (T2); FW:470-490 (T4) | #42 |
| P07 | inquiry (investigative practice) | `proposals/2026-09-05-proceedings-subsystem/04_VERBS.md:473-476` (T3, contestable); AUG:170 (T4); FW:296-317 (T4); the interview Lattice, `investigation_systems_v30.md:243-255` (T4); HIST:253, :380 (T4) | #36–#39, #41; #34 |
| P08 | tradecraft: cover, concealment, deception, counter-intelligence | AUG:170 *"tradecraft practice"* (T4); FW:361, :575, :620 (T4); HIST:339 (T4); K-SC-6, the spoken lie (`research/by_lane/SC_social_contest.md:710`, T4) | #52; the concealer's obstacle on #36–#41 (open); #13 |
| P09 | administration and domain actions (governance; HIST's "Faction Play") | AUG:147, :170 *"administrative practice"* (T4); settlement_layer_v30.md:560-563 and governance_play_redesign_v1.md:61-68, :87 (T4); HIST:75, :94, :313-314 (T4) | #4, #9, #10, #17, #21, #31, #46, #47, #55, #65 (each eligible by an office) |
| P10 | trade: bargaining, valuing goods, networks | HIST:242, :312, :379 (T4); M-SE-2 (`research/by_lane/SE_settlements_territory_economy.md` §8, T4) | #12, #43 |
| P11 | craft: making and repairing things, scribal forgery included | HIST:241 *"+2D on any roll involving your specific craft"*, :350 (T4) | #15, #30, #45, #13 |
| P12 | medicine: healing bodies, stabilizing the wounded | HIST:362 *"+1D Medicine"*, :378 *"−1 Ob stabilise"* (T4); MB:328 *"Medicine Ob 2"* (T4); MB:925 *Tend the wounded*, *"Endurance or Attunement check"* (T4) | #49 |
| P13 | scholarship and lore: doctrine, Einhir lore, records, precedent | HIST:129, :141, :294, :313, :341, :381 (T4); FW:95 (T4) | #38, #41; #6 |
| P14 | literacy (Full / Trade / Functional / Illiterate) | HIST:44-55, :215 (T4) | #6, #13, #38 (INFERRED applicability) |
| P15 | travel, navigation and survival | FW:90, :92, :239 (T4); HIST:92, :178, :314, :322, :340 (T4) | #24, #34, #23 |
| P16 | socializing (scene-scale rapport: Read, Converse, Connect, Impress, Rumour, Negotiate) | FW:97-101, :401-438 (T4); HIST:310 (T4) | none at season scale (the template's §A.1 excludes them as scene-scale) |
| P17 | labour and husbandry | HIST:314 Crown Farmer (T4); M-SE-5, *"labour as an input to production"* (SE lane §8, T4) | #45 |
| P18 | physical stealth and evasion | HIST:165 *"+1D on Agility concealment"*, :382 *"Escape −1 Ob"*, :370 (T4) | none named at season scale |
| P19 | economic stewardship (*"Wealth-relevant History"*) | settlement_layer_v30.md:560; governance_play_redesign_v1.md:61 (T4) | #15 |

**19 domains: one at T1, five at T2, one at T3 (P07, contestable), twelve at T4.**

**Dropped, because no source names a practice:**

- *Politician* and *leader*. AUG:146 and :148 list them as **position** roles, carried by *"Standing
  ladder + Mandate/votes"* and *"Standing 7 / faction emergence"*, not by a practice.
- *Logistics* as a domain of its own. It appears only inside HIST:75's Heartland Roots, so it is
  folded into P09.
- *Horsemanship*, *seamanship* and *hunting* as domains of their own. Seamanship appears only as
  terrain bonuses (HIST:340 and the Fjord Sailor's defence on water), folded into P15 and P03.
- *Circles*: the network dice of the NPC designs (`npc_behavior_system_v1.md:176`, :197). It is a
  person-held quantity, who one knows, not a practice.

**The sigma-routed verbs' keys** (`determine`, `argue`, `arrest`, `interrogate`) are folded into P02:
*"the key is content"* (`2026-10-16-character-template_part2.md:169-170`), and no source names one.

---

## 3. STAGE 2a: WHAT EACH PRACTICE DOMAIN REQUIRES

**Fixed form.** For each domain:

- (a) what doing it well requires **physically**;
- (b) **cognitively**;
- (c) **perceptually**;
- (d) **socially or volitionally**;
- (e) what the sources name against what is inferred, as a count (named / overridden / inferred).

Each cell gives the aptitude, its role and its basis.

**Notes that bind the table.**

1. **The 2026-09-05 ruling, and the gloss.** Jordan's words are *"ignore their use of attributes"*
   (`04_VERBS.md:465-466`), and they are about the proceedings design's own pool column. The
   proceedings author glosses them for the five inquiry acts: *"`capability` supplies the dice"*
   (`:473-476`, T3, contestable; template head §3.1.1). The template notes that the fieldwork §4.2
   column *"is a different source table, and Jordan's words do not name it"*
   (`2026-10-16-character-template.md:297`). So the fieldwork *"Primary Attribute"* column is tagged
   *overridden for dice by the 2026-09-05 gloss* for `examine`, `interview`, `research`, `surveil` and
   `reconstruct`, and the tag is **contestable**. The column is kept as what the design's author held
   the act to require. The gloss does not reach `thread_read`. It does not reach a gate either: the
   template keeps TS gates on the ground that a gate is not a pool term
   (`2026-10-16-character-template.md:324-328`), and the same ground keeps the interview Lattice's
   attribute gates (`investigation_systems_v30.md:254-255`) and the Exploration Cognition gates
   (FW:84, :446) NAMED.
   - ⚠ **The Cognition depth gate is the Exploration row's, not Investigation's.** FW:446 gates
     Exploration on Cognition ≥ 2 / ≥ 3; Investigation (FW:447) has only Ob and TS gates. The earlier
     coding put that gate on inquiry (P07) and `examine` (#36). It now sits only at S04, which holds
     exploration.
2. **V-2 and V-3** (`10_verbs_and_attributes.md:198-199`) limit what CODE may read. They do not limit
   what an act requires, so they are applied in the recommendation (`_part3` §7), not here.
3. **J-13** (`workplans/valoria_master_workplan_v9_part5.md:433`) records two constraints of
   Jordan's, and both bind:
   - *"a social figure is derived, not stored"*. That is about the subsystem's score, not the
     person's aptitude. Nothing here proposes storing a score.
   - the row's *"latitude enters through the pool only"*, recording Jordan's 2026-09-06 words *"pool
     only it is, but ensure you don't go so far as to deprive player of a chance at winning"*. A
     person's difference may enter a proceeding only through the pool. So the SCV draws that put a person on the **cost** side of a
     proceeding (the Concentration tracker and the Focus defence: `concentration` at P02, #50 and
     S03, *difficulty/cost*) are doubly overridden: by the kernel, and by J-13. They stay in the
     list as what SCV held the act to require. They are not a reading any proceedings resolver may
     take, and each of those three cells says so.

| P | domain (best tier) | verbs it serves | (a) physical | (b) cognitive | (c) perceptual | (d) social / volitional | (e) named / overridden / inferred |
|---|---|---|---|---|---|---|---|
| P01 | copying (T1) | #35, #32 | `precision` (effect size, [copy-fidelity] INFERRED: a copy is only as good as its fidelity); `dexterity` (effect size, [copy-hand] INFERRED: hand-copying is hand work) | `concentration` (effect size, [long-work] INFERRED: repeated copying is long, sustained work) | — | — | 0 / 0 / 3 |
| P02 | standing and the matter (argument, oratory, forensic practice) (T2) | #8, #35, #50, #54, #56, #32 | — | `reasoning` (odds, [scv-judge] NAMED T4, overridden for dice by the kernel: SCV:133 expert judge, Cognition: "evaluates logical structure"); `memory` (odds, [scv-appraise-recall] NAMED T4, overridden for dice by the kernel: SCV:155 Appraise rolls Attunement + Recall); `concentration` (difficulty/cost, [scv-conc] NAMED T4, overridden for dice by the kernel: SCV:246, :267 Concentration = 3·Focus + 2·Spirit; SCV:197-199 Focus defence absorbs strain; J-13 also puts a person's latitude in the pool only (v9 _part5.md:433)); `verbal-fluency` (odds, [argument-words] INFERRED: argument is made of words); `quick-thinking` (odds, [rebut] INFERRED: the rebut move kind (resolver.py:34) answers in the moment) | `reading-people` (odds, [scv-appraise] NAMED T4, overridden for dice by the kernel: SCV:135 no adjudicator, Attunement: "read the other party and calibrate"; :147 Appraise is "empathetic perception") | `presence` (odds, [scv-crowd] NAMED T4, overridden for dice by the kernel: SCV:134 crowd, Charisma: "delivery and authority") | 0 / 5 / 2 |
| P03 | arms (personal combat: history, skills, tradition, techniques) (T2) | #18, #20, #19 | `strength` (effect size, [combat-str] NAMED T2: Impact, balance, health (AUG:86, :88; combatant.py:40-42)); `quickness` (odds, [combat-tempo] NAMED T2: tempo (combat_systems.py:113); Agility in the initiative emphasis (:1416-1421)); `reflexes` (odds, [combat-reflex] NAMED T2: reflex (combat_systems.py:172)); `balance` (odds, [combat-balance] NAMED T2: balance (combat_systems.py:184-188)); `stamina` (difficulty/cost, [combat-stamina] NAMED T2: `stamina_max` (combatant.py:45-47)); `toughness` (difficulty/cost, [combat-health] NAMED T2: `wound_interval`, `health_full` (combatant.py:30-42)) | `concentration` (difficulty/cost, [combat-conc] NAMED T2: the Concentration tracker, 3·Focus + 2·Spirit (combatant.py:147), drained on hits and per bout (wrapper.py:186, :427, :523), sets consistency and mental fatigue (combat_systems.py:1423-1431); disruption resistance is "Concentration disruption-resistance" (:1449-1452); poise regathers on Focus (:1433-1436), filed under Concentration by AUG:90) | `anticipation` (odds, [combat-reading] NAMED T2: reading (combat_systems.py:171), also in the initiative emphasis (:1416-1421)) | `boldness` (odds, [combat-disp] NAMED T2: `disp` aggression lean (combat_systems.py:181-183)) | 9 / 0 / 0 |
| P04 | command (leading a field side) (T2) | #22, #65, #57 | — | `spatial-sense` (odds, [hist-terrain] NAMED T4: HIST:177 Cognition to "identify terrain advantage"); `tactical-read` (odds, [command-cog] NAMED T2: Command's Cognition term is the "tactical read" (exchange.py:59-60); tactic execution is a Command roll (MB:312)); `judgment` (odds, [command-decisions] INFERRED: when to pursue, recall or commit is decided under uncertainty; the recall itself is a Command roll (orchestration.py:2585-2590)) | `anticipation` (odds, [feint-roll] NAMED T2: feint recognition `roll_pool(command)` (orchestration.py:2593-2599)); `situational-awareness` (eligibility, [span] NAMED T2: Command is "the span-of-control governor" (engine.py:93; MB:309)); `observation` (odds, [hist-ambush] NAMED T4: HIST:177 Border Vigilance, Cognition to detect ambush, assess enemy strength; HIST:369 Eagle Eyes) | `leadership` (eligibility, [command-cha] NAMED T2: Command, Charisma primary "inspire/hold the line" (exchange.py:57-66) → reform gate, morale start, re-establishing command (MB:209-210, :230, :343-344)) | 6 / 0 / 1 |
| P05 | threadwork (the Leap, the seven operations, thread_read) (T2) | #58, #59, #60, #61, #62, #63, #64, #40 | — | `concentration` (eligibility, [ops-per-contact] NAMED T4: Focus sets max operations per contact (threadwork_v30:199)) | `thread-sensitivity` (odds, [ts-pool] NAMED T2: `ts // 10` (operations.py:235-247)) | `will` (odds, [thread-pool] NAMED T2: `spirit × 2` (operations.py:235-247); threadwork_v30:163); `self-coherence` (difficulty/cost, [coherence-cost] NAMED T2: `resilience` resists the Coherence cost (operations.py:249-274), dark at gain 0); `contact-endurance` (eligibility, [thread-fatigue] NAMED T4: Thread Fatigue threshold = Spirit × 5 (threadwork_v30:195), cleared by meditation by Spirit (:203)) | 5 / 0 / 0 |
| P06 | relationships (knot-forming practice) (T2) | #42 | — | — | `thread-sensitivity` (eligibility, [knot-ts-gate] NAMED T2: either party `ts ≥ 30` (knots.py:195-198)) | `relational-depth` (eligibility, [knot-bonds-gate] NAMED T2: `bonds ≥ 5` gate and cap (knots.py:185-203); FW:477-479); `sincerity` (odds, [sincerity-check] NAMED T4: Sincerity Check before an instrumental approach (FW:430)); `will` (odds, [knot-roll] NAMED T2: formation roll `spirit × 2` (knots.py:212-222); FW:483; a sworn bond rolls Spirit too (npc_relational_graph_v30:277)) | 4 / 0 / 0 |
| P07 | inquiry (investigative practice) (T3) | #36, #37, #38, #39, #41, #34 | — | `reasoning` (eligibility, [lattice-cog-gate] NAMED T4: the interview Lattice's intellectual approaches need Cognition ≥ 3 (investigation_systems_v30:254)); `memory` (odds, [fw-research] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:95, :303 Research, Recall: "archives, oral histories … precedent"); `inference` (odds, [fw-reconstruct] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:306 Reconstruct rolls Recall to "assemble existing evidence into a coherent picture"); `concentration` (odds, [surveil-time] INFERRED: Surveil is observation "over extended time" (FW:304)) | `observation` (odds, [fw-examine] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:93, :301 Examine, Cognition: "examining objects … forensics"); `reading-people` (odds, [fw-interview] NAMED T4, overridden for dice by the 2026-09-05 gloss: FW:94, :302 Interview, Attunement: "reading people, sensing deception"); `thread-sensitivity` (eligibility, [fw-ts-gate] NAMED T4: depth gates TS ≥ 10 / ≥ 30 (FW:301, :447)) | `empathy` (eligibility, [lattice-att-gate] NAMED T4: the Lattice's emotional approaches ("I can see this is costing you something") need Attunement ≥ 4 (investigation_systems_v30:255)); `persuasiveness` (odds, [interview-cha] NAMED T4, overridden for dice by the 2026-09-05 gloss: the Interview action "roll[s] Charisma pool" (investigation_systems_v30:243), against FW:302's Attunement); `patience` (odds, [desperate-trail] INFERRED: three failures make a Desperate Trail (FW:337-345); persistence pays) | 3 / 5 / 2 |
| P08 | tradecraft (cover, concealment, deception, counter-intelligence) (T4) | #52, #36, #37, #38, #39, #40, #41, #13 | — | `reasoning` (resists another, [fw-cover] NAMED T4: Cover = Cognition + History "determines Exposure thresholds" (FW:575-577); the concealing party's pool, Cognition × 2, sets the investigator's Concealment Ob (FW:361)) | `observation` (odds, [counter-intel] INFERRED: HIST:339 Shadow Work (+1D surveillance / counter-intel) is practice) | `presence` (eligibility, [fw-cover-identity] NAMED T4: a cover identity needs a Charisma roll (FW:620)); `deception` (odds, [lying] INFERRED: HIST:339 Smooth Liar is a practice skill; the aptitude under it is unnamed) | 2 / 0 / 2 |
| P09 | administration and domain actions (governance; "Faction Play") (T4) | #4, #9, #10, #17, #21, #31, #46, #47, #55 | — | `reasoning` (odds, [settle-cog] NAMED T4: Develop and Survey roll Cognition + History (settlement_layer_v30:560; governance_play_redesign_v1:61, :87)); `judgment` (odds, [hold-court] NAMED T4: Hold Court adjudicates a dispute on Charisma/Cognition (governance_play_redesign_v1:64)); `numeracy` (odds, [ledger] INFERRED: the Governor role is "AP × compliance + Ledger" (AUG:147)); `planning` (odds, [works-over-seasons] INFERRED: administration sequences works over seasons) | `reading-people` (odds, [administer] NAMED T4: Administer rolls Attunement + Governance History (settlement_layer_v30:563)) | `presence` (odds, [pacify] NAMED T4: Pacify rolls Charisma + local History (settlement_layer_v30:562); Keep Order by Consent, Charisma (governance_play_redesign_v1:63)); `patience` (odds, [slow-admin] INFERRED: administration is slow work; no source states it) | 4 / 0 / 3 |
| P10 | trade (bargaining, valuing goods, networks) (T4) | #12, #43 | — | `numeracy` (odds, [price] INFERRED: valuation and price); `memory` (odds, [trade-memory] INFERRED: prices, routes, partners (HIST:379 Wide Network is practice)) | `reading-people` (odds, [negotiate] NAMED T4: Negotiate rolls Attunement (FW:413; a scene-scale analogue)) | `persuasiveness` (odds, [bargain] INFERRED: closing a bargain); `concentration` (difficulty/cost, [strain-nerve] INFERRED: HIST:312 Haggler's Nerve (−1 strain in private negotiation) is practice; strain is what the Focus defence absorbs (SCV:197-199)) | 1 / 0 / 4 |
| P11 | craft (making and repairing things; scribal forgery) (T4) | #15, #30, #45, #13 | `dexterity` (effect size, [craft-hand] INFERRED: HIST:241 Craft Expertise names the practice only); `precision` (effect size, [craft-quality] INFERRED: quality of the made thing); `strength` (effect size, [heavy-work] INFERRED: smithing, building, masonry) | `spatial-sense` (effect size, [build-to-plan] INFERRED: building to plan) | — | `patience` (effect size, [long-craft] INFERRED: long work) | 0 / 0 / 5 |
| P12 | medicine (healing bodies, stabilising the wounded) (T4) | #49 | `dexterity` (odds, [medicine-hand] INFERRED: HIST:378 Field Medicine (−1 Ob stabilise) and MB:328 (Medicine Ob 2) name the practice only; MB:925 Tend the wounded names "Endurance or Attunement", no function) | `memory` (odds, [remedies] INFERRED: remedies) | `observation` (odds, [diagnosis] INFERRED: diagnosis) | `concentration` (odds, [under-fire] INFERRED: working on the wounded under fire (MB:328, Phase 5)) | 0 / 0 / 4 |
| P13 | scholarship and lore (doctrine, Einhir lore, records, precedent) (T4) | #38, #41, #6 | — | `memory` (odds, [fw-research] NAMED T4: FW:95 lore research, Recall; HIST:294 Archive Access "+1D on Recall-based rolls"; HIST:381 Treaty Language "+1D Recall"; HIST:129 "knowledge as recognition, not intellect"); `reasoning` (odds, [interpret-doctrine] INFERRED: interpreting doctrine and precedent) | — | `patience` (odds, [archive-work] INFERRED: archive work) | 1 / 0 / 2 |
| P14 | literacy (Full / Trade / Functional / Illiterate) (T4) | #6, #13, #38 | — | `learning` (eligibility, [literacy-acquired] INFERRED: literacy is acquired (HIST:44-55); "available as spark" for the self-taught) | — | — | 0 / 0 / 1 |
| P15 | travel, navigation and survival (T4) | #24, #34, #23 | `stamina` (odds, [fw-endurance] NAMED T4: FW:92 Endurance-based exploration: "forced marches, exposure, harsh terrain"); `hardiness` (difficulty/cost, [calamity-travel] NAMED T4: FW:239 Endurance check per Calamity territory; HIST:92 Highland Toughness, :178 Cold Endurance) | `spatial-sense` (odds, [fw-pathfinding] NAMED T4: FW:90 Cognition: "pathfinding, cartography") | `land-sense` (odds, [seasons-reader] NAMED T4: HIST:314 Seasons Reader, "+1D Cognition for weather/terrain/agriculture"); `observation` (odds, [spot-route] INFERRED: spotting a route, a danger) | — | 4 / 0 / 1 |
| P16 | socializing (scene-scale rapport: Read, Converse, Connect, Impress, Rumour, Negotiate) (T4) | none at season scale | — | — | `reading-people` (odds, [fw-read] NAMED T4: Read and Negotiate roll Attunement (FW:97, :101, :408, :413)) | `presence` (odds, [fw-impress] NAMED T4: Impress and Rumour roll Charisma (FW:98, :100, :411-412)); `persuasiveness` (odds, [fw-converse] NAMED T4: Converse rolls Charisma: "shift Disposition" (FW:409)); `relational-depth` (odds, [fw-connect] NAMED T4: Connect rolls Bonds: "building genuine trust" (FW:99, :410)); `sincerity` (odds, [sincerity-check] NAMED T4: Sincerity Check, Spirit (FW:430)) | 5 / 0 / 0 |
| P17 | labour and husbandry (T4) | #45 | `stamina` (effect size, [labour] INFERRED: field and site work); `strength` (effect size, [labour] INFERRED: field and site work) | — | `land-sense` (effect size, [seasons-reader] NAMED T4: HIST:314 Seasons Reader (weather, agriculture)) | `patience` (effect size, [long-craft] INFERRED: seasonal work) | 1 / 0 / 3 |
| P18 | physical stealth and evasion (T4) | none at season scale | `balance` (odds, [hist-agility-conceal] INFERRED: HIST:165 Invisible names Agility ("+1D on Agility concealment" in crowds), not which of its functions; balance is this proposal's choice); `quickness` (odds, [escape] INFERRED: HIST:382 Slippery (Escape −1 Ob) names no attribute; combat's disengage rolls Agility (combat_reference_v1.md:598)) | — | — | `concentration` (odds, [hidden-steadiness] INFERRED: holding still under a searcher's eye) | 0 / 0 / 3 |
| P19 | economic stewardship ("Wealth History") (T4) | #15 | — | `reasoning` (odds, [settle-cog] NAMED T4: Develop rolls Cognition + Wealth-relevant History (settlement_layer_v30:560; governance_play_redesign_v1:61)); `numeracy` (odds, [ledger] INFERRED: accounts); `planning` (odds, [works-over-seasons] INFERRED: investment over seasons) | — | — | 1 / 0 / 2 |

**What the domain interrogation shows.**

- **Only P03 (arms), P04 (command), P05 (threadwork) and P06 (knots) have aptitudes named in code**
  (T2). Every other domain's aptitudes are named in designs (T4), overridden, or inferred.
- **P11 craft, P12 medicine, P14 literacy and P17 labour name only the practice.** Every aptitude under
  them is this proposal's.
- **The most-drawn aptitude across domains is `concentration`**, in 8 of 19 domains, but 5 of the 8
  are inferred (P01, P07, P10, P12, P18). **`reasoning`** is in 6, with 5 sourced.
  `reading-people`, `memory`, `observation` and `patience` are in 5 each (`patience` all inferred).
- **AUG:152-155 says the roles "are not distinguished by aptitude — they are distinguished by
  practice, instruments, and office".** The domain rows partly bear that out, and partly do not:
  - **Bearing it out:** reasoning, reading people and concentration recur across most domains, so
    they do not tell domains apart.
  - **Against it:** a minority of aptitudes is confined to one or two domains:
    - quickness, reflexes and balance: arms (T2), and stealth by inference only;
    - will and self-coherence: threadwork and knots;
    - thread sensitivity: threadwork, knots and inquiry;
    - relational depth: knots and socializing;
    - land sense: travel and husbandry.

    Those do mark a domain. **Judgment call:** AUG's sentence holds for the six roles it tabulates
    (AUG:168-177). It does not hold for the domains it leaves out (threadwork, knots, travel, stealth).
