# VERBS · DICE — each verb names the one or two attributes its everyday meaning relies on

Written: 2026-11-13, on Jordan's instruction of the same day: *every verb's dice amount is set by the character's
attributes, skill (if relevant) and office (if relevant)*, and *"you should be able to logically interrogate each verb
based upon its everyday meaning for what 1-2 attributes are most reasonably applied"*; with his added rule, relayed the
same day: a verb whose act calls a subsystem into being does not roll the generic pool, the subsystem resolves it by its
own rule. Read at the working tree of 2026-11-13.

**Depends on:** B04 (the skill definition rows, `references/descriptor_registry.yaml: capabilities`, U1 §2); B05.09
(`pool.py::governing_attribute`, the skill score with no attribute in it); the plan's verb-row `capability:` and
`difficulty:` columns (`10_DICE_one_score_two_roles.md` Edit C; D-U1-04, `workplan_v12_part18_cont.md:37`).
**Lands in batch:** B05, as two items after B05.09 (§5 below): one DESIGN-FIRST, one BUILD.

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05: nothing here edits code, data or the plan; the plan items in §5 are for
the orchestrator to insert. Lanes that own the files the items edit: IN (`engine/season/verb_table.yaml`,
`engine/season/data/verbs.py`, `engine/season/data/rosters.py`, `engine/season/rosters.yaml`,
`engine/season/seam/wrappers/pool.py`, `sigma.py`), with SC, PC, MB, FA and FI owning the rows of their verbs.

## 0. The method, and what "governing attribute" means here

For each of the 67 rows of `engine/season/verb_table.yaml` (counted by the loader's own parse, `yaml.safe_load(...)['verbs']`,
67 entries), in the table's own strata (`stratum:` column): the everyday meaning first, in one sentence, as a person
outside this repository uses the word (a term of art is named as such, with the ordinary word it is close to); then what a
person doing it is mainly relying on; then the one or two attributes of the ten most reasonably applied, each with one
clause read from the attribute's own definition (§1). The tree's current mapping was read only after, for the comparison
column.

- **The first attribute named is the verb's governing attribute** (glossary *governing attribute*, `unified/U1_GLOSSARY.md:64`,
  A-98 (1)). How it enters the roll, as dice or as levels, is §6 Q1; the table does not depend on the answer.
- **A second attribute** is named only where the everyday act plainly needs both. It enters as one named level for the
  roller, by the level reader the plan already builds (B05.10's `edge` row, `per: mid`,
  `workplan_v12_part8.md:294-295`) `[ASSUMPTION: the second attribute is a level, never a second pool — basis: U1 §4's
  rule that two inputs are never added into one number, U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:269-271]`.
- **Skill**: an existing tree key (`copying`, `argue`, `inquiry`, `arms`: `engine/season/rosters.yaml:1550-1571`), a
  proposed skill row of U1 §2 marked (P) (`law`, `deception`, `command`, `healing`, `insight`:
  `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:125-133`), or "none: attribute only".
- **Office modifier**: yes where the act is done through a seat's standing (a `remit:` eligibility, so `Act.via` names
  the seat), the plan's seat `modifier:` (A-12; U1-D, `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:525-528`). It is derived
  from the row's eligibility, so no new column carries it. The relative rung of a seat against a hearer is a different
  thing, a hearer-side term (§2.6).
- **Opposed by**: A-71's one opposed rule (`unified/DECISIONS_ANSWERED.md:94`, completed by A-79 at `:105`): the
  defender's skill score and his attribute. The column names the attribute a person opposite resists with; "nobody" where
  no person stands opposite (the task's difficulty alone).
- **Calls a subsystem**: read from the row's `contests:` prize and its `module_entry:` (`rosters.yaml:1736-1791`), the
  graded-inquiry route (`rosters.yaml:1441-1443`) and the composition rows that name a verb or a verb's effect
  (`references/module_contracts.yaml:52-68, 99-110, 120-123`).
- **Roll?**: "contest" (a `contests:` prize), "task" (a draw against a difficulty, the class
  `18_DETERMINISM_task_draw_for_uncontested_verbs.md:133-137` proposes), "subsystem" (the called module resolves it), or
  "no roll" with the reason from the row. No row here is made certain: where the act does not roll, what follows from it
  is drawn in another act or another person's choice, named in the cell.

## 1. The ten attributes, in their own definitions

The roster is `engine/substrate/descriptors.py:50` (`ATTRIBUTES`, read from the cooked registry), ten keys on the scale
1 to 7 (`references/descriptor_registry.yaml:38-53`). The registry carries a one-line comment for three of them only
(Perception, Attunement, Grace, `:48-53`); the definitions below are Jordan's own words, from the ruling that named the ten
(`ED-IN-0328`, `registers/editorial_ledger_in.jsonl:107`) and the rulings of 2026-11-05 by subject (`ED-IN-0347`, `:126`;
the verbatim text `proposals/2026-11-05-attribute-rulings-by-subject.md:36-105`, AR numbers below). The display name is
used in prose; the key in data.

| key | name | its own definition (verbatim) |
|---|---|---|
| `attr.body.strength` | Strength | *"the amount of damage a weapon can do … the ability to manage weapon heft, the ability to wear armour, the ability to leverage weapons, to push and force the opponent"* (AR-10); health and muscle mass (AR-11) |
| `attr.body.agility` | Coordination | *"coordination (agility and dexterity)"* (ED-IN-0328); *"accuracy with weapons and stable footing and dodging without losing balance and precise manoeuvres"* (AR-15); *"the quality of a forgery or ability to pick a lock"* (AR-16) |
| `attr.body.endurance` | Endurance | *"stamina, the ability to recover your breath, the likelihood of becoming tired which can impact concentration, and it contributes to someone's health/wounds"* (AR-20) |
| `attr.mind.focus` | Focus | *"focus (concentration, avoiding errors)"* (ED-IN-0328); *"less likely to be distracted as well as less likely to have irrelevant information impact their choices"* (AR-23) |
| `attr.mind.acuity` | Reason | *"reason (acuity, faculty, forecasting, predicting)"* (ED-IN-0328); *"mental acuity, logic, understanding of concepts/facts, forecasting, understanding what a choice entails"* (AR-21) |
| `attr.mind.will` | Spirit | *"spirit/willpower"* (ED-IN-0328); *"the ability to stay true to yourself and be free of external influence or compulsion, the capacity to tolerate harm and strain and stress, the likelihood to perform threadwork without losing coherence, the ability to get good results despite poor circumstances, to overcome an obstacle"* (AR-44) |
| `attr.mind.perception` | Perception | *"awareness of surroundings, noticing information"* (ED-IN-0328; the registry comment, `descriptor_registry.yaml:48`); *"surveillance and fieldwork and noticing things out of place"* (AR-24); *"it concerns FACTUAL matters"* (AR-26) |
| `attr.social.attunement` | Attunement | *"attunement (reading people)"* (ED-IN-0328); *"understanding other characters in terms of their intentions in a given moment as well as their pursuits convictions ambitions goals desires"* (AR-30); *"the likelihood of forming knots/bonds"* (AR-31) |
| `attr.social.charisma` | Presence | *"charisma magnetism social impact"* (AR-29, which governs AR-27 and AR-28) |
| `attr.social.grace` | Grace | *"composure (ability to remain calm under pressure, nerve)"* and *"grace … composure and remaining calm and etiquette and manners"* (ED-IN-0328); *"being seen as respectable/dignified"* (AR-33); *"different kinds of social contests and venues may prioritize grace"* (AR-36) |

## 2. The table, by the verb table's strata

Legend for the "current" column: the tree's mapping as it runs today — `verb_capability` skill → `vocation_attribute`
attribute (`rosters.yaml:1550-1571`, `:1665-1668`); the opposing attribute (`opposed_by: {}` ships empty, `:1676`, so a
person opposes with the row's own attribute, `seam/wrappers/pool.py:68-75`); and the roll the verb gets today (the social
roll's `task_difficulty` rows, `rosters.yaml:1598-1607`; the prize rows; else the flat fold, no roll). A verb with no
`verb_capability` row pools at `pool_default` for everyone (`pool.py:112-117`).

### 2.1 Social (21 rows)

| verb (row) | everyday meaning | governing attribute(s), with reason | skill | office modifier | opposed by | calls a subsystem? | roll? | current mapping | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `carry` (`verb_table.yaml:108`) | to take a petition up and put it before a forum (term of art, close to "present" or "sponsor" a petition) | **Presence**: getting a forum to take a matter up is social impact (AR-29); **Grace**: it must be done properly for the venue (AR-36) | `law` (P) | no: eligibility `own` | nobody: the task's difficulty | none | task (18_DET `task`) | no skill; no roll (flat fold) | **disagree**: the act can fail and rolls nothing |
| `argue` (`:133`) | to give someone reasons meant to change his mind | **Presence**: ruled the argument's main component (ED-IN-0350, `editorial_ledger_in.jsonl:129`); **Attunement**: how the other is receiving it and which style to deliver (same ruling), which Jordan's persuasion points of 2026-11-13 put into the teller's roll | `argue` | no (`own`); the hearer's seat against the arguer's is a hearer-side term (§2.6) | the hearer's **Spirit**: *"free of external influence"* (AR-44; CR-96's own reading, `rosters.yaml:1669-1670`; U1 §2 `argue.opposed_by`, `:126`) | social contest (`social_contest.roll`, prize `a proposition`); the module's input is the generic pool, so the attributes are its input, not a second roll | contest | `argue` → Presence; opposed by Presence; social roll, difficulty 1.0 | **disagree**: opposition (Presence → Spirit) and the second attribute |
| `commit` (`:209`) | to bind oneself publicly to a statement or cause | — | — | — | — | none | **no roll**: a pledge of one's own; the row writes only the actor's own `Tenure.since` | none; no roll | agree |
| `comply` (`:227`) | to do what an order requires | — | — | — | — | none | **no roll**: emission-only (`writes: []`); what compliance performs is the separate act the writ names (row `writes_note`) | none; no roll | agree |
| `conceal` (`:251`) | to hide; here, to take on a cover (a false identity about oneself) | **Grace**: keeping a calm, correct face under scrutiny (*"composure … nerve"*, ED-IN-0328); **Focus**: not slipping out of the part (*"avoiding errors"*) | `deception` (P) | no | nobody when cast; the cover's band is read later as the obstacle of whoever examines it (18_DET item 4) | none | task | none; no roll | **disagree**: a cover is made well or badly and nothing draws it |
| `covenant` (`:300`) | to offer another party a formal binding agreement | — (if lane 13 makes the offer a contest: **Attunement**, what the other side wants, AR-30; **Reason**, what the terms entail, AR-21) | `law` (P) | yes: `remit:issue`, the seat's standing behind the terms | — | none | **no roll**: the row offers (`covenant.offered`); acceptance is the counterparty's own act, drawn in his choice. 18_DET lists it as a contest owed; I find the contested part is the other man's answer | none; no roll | agree |
| `lie` (`:534`) | to say what one knows is false so another believes it | **Attunement**: knowing what this hearer will believe (AR-30); **Reason**: keeping the story consistent and plausible (AR-21; Jordan's "knowledge of plausibility"). Competitor: Grace, the liar's composure, U1 §2's `deception.base` (`:129`); not taken, because Jordan's 2026-11-13 points name reason and attunement for the teller | `deception` (P) | no | the hearer's **Attunement**: seeing another's intention in the moment (AR-30). U1 §2 says Perception (`:129`); Perception is ruled to concern *"FACTUAL matters"* (AR-26), and the fit of the content with what the hearer knows is an engine fact (§2.6), not an attribute | social contest (`a standing`) | contest | no skill row: pool and opposition both at `pool_default` (`rosters.yaml:1563-1567`); social roll, difficulty 1.0 | **disagree**: no attribute at all on either side |
| `forgive` (`:573`) | to stop holding a wrong against someone | — | — | — | — | none | **no roll**: a change of one's own stance (`Person.stance` rows of the actor's own, row `writes_note`) | none; no roll | agree |
| `give` (`:657`) | to hand something one holds to another | — | — | — | — | none | **no roll**: a transfer of a held thing to a present receiver | none; no roll | agree |
| `oblige` (`:1217`) | to take on a duty to a seat (term of art, close to "pledge service" or "enlist") | — | — | — | — | none | **no roll**: the seat's `binds` admits the joiner or refuses (precondition) | none; no roll | agree |
| `open_case` (`:1239`) | to begin formal proceedings on a matter | **Reason**: framing the matter and its stages is understanding facts and what they entail (AR-21) | `law` (P) | yes: `remit:determine`, done from the bench seat | nobody | none | task (18_DET `task`) | none; no roll | **disagree**: no roll where 18_DET proposes a task |
| `petition` (`:1294`) | to ask an authority formally for something | — | — | — | — | none | **no roll** at filing: the addressee's answer is his own act (18_DET `bookkeeping`); the persuasion happens where the matter is heard (`speak`) | none; no roll | agree |
| `construe` (`:1320`) | to interpret terms; here, to read them to one's own advantage | — | — | — | — | none | **no roll**: emission-only, the construal is the holder's own belief (row `writes_note`) | none; no roll | agree |
| `speak` (`:1475`) | to address a hearing on a matter before it (to plead, when the matter is one's own) | **Presence**: moving a room is social impact (AR-29); **Grace**: a venue penalizes the speaker who is persuasive but *"not doing it right"* (AR-36a) | `argue` (U1: the hearing's argue moves draw on `argue`, `:139`) | yes where he speaks from a seat in the body that hears him (U1-D's `heard_by`); else the rung gap is a hearer-side term | the matter's party, a person: his **Spirit** (AR-44); the self-plea: §2.7 | social contest (`a matter`, `heard_by: bench`, `rosters.yaml:1786-1790`): the hearing scene; its nested run is unbuilt (`:1379`), so today the generic pool is its input | contest | `copying` → Focus; opposed by Focus; social roll, difficulty 1.0 | **disagree**: Focus is a copyist's attribute, not a speaker's |
| `tell` (`:1582`) | to pass on to someone something one knows | **Reason**: knowing the matter and making it hang together (AR-21; Jordan's "knowledge of plausibility"); **Attunement**: putting it to this hearer (AR-30) | none: attribute only. `copying` fails the word test for telling (a copy is a faithful reproduction of a text, `rosters.yaml:1629-1631`) | no (`own`) | the hearer's **Spirit**: resisting being told what to believe (AR-44) | social contest (`a standing`) | contest | `copying` → Focus; opposed by Focus; social roll, difficulty 1.0 | **disagree**: attribute (Focus → Reason) and skill |
| `interview` (`:1767`) | to question someone to learn what he knows | — (if made a contest: **Attunement**, what he holds back, AR-30) | `inquiry` if rolled | no | — | none (`finding.made` reaches `fieldwork.find` after) | **no roll** on the asker: the row is a prompt; the questioned person answers by his own `tell`, which is drawn (`rosters.yaml:1433-1434`, K-36). 18_DET lists it as a contest owed | none; no roll | agree |
| `interrogate` (`:1783`) | to question a prisoner hard to get a confession | **Attunement**: judging how near he is to breaking (AR-30; AR-42's *"how close the opponent may be to admitting defeat"*); **Presence**: the questioner's force of personality (AR-29) | `inquiry` (U1 §5, unanimous, `:300`) | yes: `remit:determine`, done from the bench | the prisoner's **Spirit**: *"free of external influence or compulsion, the capacity to tolerate harm and strain"* (AR-44) | social contest (`a proposition`) | contest | `inquiry` → Reason; opposed by Reason; social roll, difficulty 1.0 | **disagree**: both attributes |
| `tie / knot` (`:1896`) | to form a close personal bond with someone | **Attunement**: ruled to govern *"the likelihood of forming knots/bonds"* (AR-31) | none: attribute only | no | nobody's attribute: the other's regard of him is the term (`person_q.regard`, §2.6) | none | task: AR-31 says *likelihood*, which is a draw. 18_DET puts it in `bookkeeping` | none; no roll | **disagree**: AR-31 asks for a draw |
| `utter` (`:2090`) | to put something into words | — | — | — | — | none | **no roll**: it makes a Proposition exist; whether anyone believes it is a later `tell` or `argue` | none; no roll | agree |
| `evade / defy` (`:457`) | to dodge an order quietly, or refuse it openly | — | — | — | — | none | **no roll** on the actor: emission-only; *"disobedience others see or miss"* is the witnesses' noticing (row `writes_note`) | none; no roll | agree |
| `challenge` (`:925`) | to call someone out to fight | — | — | — | — | none (the fight is `accept`'s) | **no roll**: issuing it is a declaration (a `challenge` Record); the answer is the other man's `accept` or refusal. 18_DET lists it as a contest owed | none; no roll | agree |

### 2.2 Contested physical (9 rows)

| verb (row) | everyday meaning | governing attribute(s), with reason | skill | office modifier | opposed by | calls a subsystem? | roll? | current mapping | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `arrest` (`:171`) | to seize a person by authority and take him into custody | **Strength**: laying hands on a man is *"to push and force the opponent"* (AR-10); **Presence**: most men submit to the bearing of authority before force is needed (AR-29) | `arms` (U1 §5, `:303`) | yes: `remit:dispatch`, the warrant's seat | the subject's **Strength** (breaking a hold); Coordination (slipping it) is the competitor | social contest today (prize `a standing`); the row's own open question is whether resisting arrest is a contest of the body (row `contests_note`): §6 Q2 | contest | `arms` → Coordination; opposed by Coordination; social roll, difficulty 1.0 | **disagree**: attribute (Coordination → Strength) |
| `fight` (`:733`) | to try to hurt or overcome someone by force | none of the verb's own: the subsystem's inputs are the **martial skill** `arms` (combat's pool `max(5, skill + 6)`, the six base dice, `modules/combat/core.py:51-52`) and the six attributes combat maps from `Person.attributes`: Strength, Coordination, Endurance, Perception, Spirit, Focus (`modules/combat/attributes.py:45-50`) | `arms` (the subsystem's input) | no (`own`) | combat's own rule (A-71, A-79) | **personal combat** (`combat.fight`, `module_contracts.yaml:58-62`; prize `the body`) | subsystem. The row rolls nothing before the hand-off: it is declared at RESOLVE (band `Declared`) and fought at ENCOUNTER (`rosters.yaml:1740-1741`) | `arms` → Coordination through `faculty`, which `combat_input` passes as `faculties` (`seam/wrappers/combat.py:215-229`) | **disagree: a duplicate.** An authored Coordination reaches the fight twice: in `faculty`'s `max(attr, have)` (`pool.py:107-108`) and as combat's `agi` by `registry_key` (`attributes.py:46`, `fight.py:46-52`, passed at `combat.py:231-232`). The roster note saying `agi` is the class default (`rosters.yaml:1660-1663`) predates PC-06 K-1 |
| `capture` (`:866`) | to take someone prisoner by force | as `fight` (the subsystem's inputs) | `arms` (input) | yes: `remit:dispatch`, the seat the custody goes to | combat's rule, under the `yield` terms | **personal combat** (prize `the body`, reached through the prize row) | subsystem; declared, then fought | `arms` → Coordination, as `fight` | **disagree**: the same duplicate |
| `accept` (`:961`) | to take up a challenge, and fight it | as `fight` | `arms` (input) | no | combat's rule | **personal combat** (prize `the body`) | subsystem; accepting is the choice, the fight is the module's | `arms` → Coordination, as `fight` | **disagree**: the same duplicate |
| `march` (`:1057`) | to lead an army to a place, and fight what meets it there | none of the verb's own: the field's inputs are the commander's **command** (P; A-59, `DECISIONS_ANSWERED.md:73`: *"a learned skill … and social/mental attributes"*; U1 §2 `command.base` Presence, `:132`) and each unit's prowess (A-59 (2)); today the field adapter reads no person attribute (no `attributes` read in `seam/wrappers/mass_battle.py`) | `command` (P, the subsystem's input) | yes: `remit:dispatch` | the field's rule | **mass battle** (`mass_battle.resolve_field`, `module_contracts.yaml:64-68`; prize `a field`) | subsystem; declared at RESOLVE, fought at ENCOUNTER (`rosters.yaml:1747-1748`) | none (U1 §5: `none`, noted, `:304`) | agree |
| `raze` (`:1426`) | to destroy a captured town utterly | **Presence**: an ugly order carried out by troops is obedience to command (A-59's social attribute; AR-29) | `command` (P) | yes: `remit:dispatch` | nobody | none: the field was `march`'s (row `writes_note`: *"contests: none"*) | task (18_DET): how thoroughly it is done is drawn | none; no roll | **disagree**: the act can be done thoroughly or not and rolls nothing |
| `examine` (`:1738`) | to look closely at a place to find out what happened there | **Perception**: *"noticing things out of place"* (AR-24) about *"FACTUAL matters"* (AR-26); **Reason**: working out what the traces mean (AR-21) | `inquiry` | no | nobody (difficulty 2.0); a forger's or concealer's band where the thing examined carries one | the social roll by the graded route (`rosters.yaml:1442`), then **field investigation** (`fieldwork.find`, `module_contracts.yaml:120-123`) on its `finding.made`: the find module takes the grade, so the attributes are the roll's, not a second roll | task (graded) | `inquiry` → Reason | **disagree**: the order (Reason first → Perception first). CR-96 named the clash and left it (`rosters.yaml:1650-1654`): one skill row cannot carry two attributes, which §3 item 2 answers |
| `surveil` (`:1838`) | to watch a place or person secretly over time | **Perception**: ruled to concern *"surveillance"* (AR-24); **Focus**: watching for long without lapses (AR-23) | `inquiry` | no | nobody (difficulty 2.0); a watched person's **Perception** where the Person case is built (absent, `rosters.yaml:1436-1437`) | graded social roll, then **field investigation** | task (graded) | `inquiry` → Reason | **disagree**: attribute (Reason → Perception) |
| `thread_read` (`:1863`) | to sense the Thread at a site (term of art, close to "divine" or "sense") | **Spirit**: *"the likelihood to perform threadwork without losing coherence"* (AR-44) | none: Thread Sensitivity is the gate (`requires`), not a skill (glossary `:84`, A-11) | no | nobody | none (`finding.made` to field investigation after) | task: it waits today on a value space (`rosters.yaml:1435-1436`) | none; no roll | **disagree**: no roll and no attribute |

### 2.3 Uncontested material (23 rows)

| verb (row) | everyday meaning | governing attribute(s), with reason | skill | office modifier | opposed by | calls a subsystem? | roll? | current mapping | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `create_record` (`:327`) | to write a document | — | — | — | — | none | **no roll**: writing one's own paper (18_DET `bookkeeping`); a false one is `forge` | none; no roll | agree |
| `destroy_record` (`:338`) | to destroy a document one holds | — | — | — | — | none | **no roll**: burning a paper in one's hand fails in no ordinary way; what it leaves behind is a witness question. 18_DET lists it as `task` | none; no roll | agree |
| `exchange` (`:480`) | to trade goods with another | — | — | — | — | none | **no roll**: both sides' stores cover the terms or it is refused; each side's consent is his own sampled choice (18_DET) | none; no roll | agree |
| `forge` (`:508`) | to make a false document | **Coordination**: ruled to concern *"the quality of a forgery"* (AR-16); **Focus**: exactness, *"avoiding errors"* | `copying` (a faithful reproduction of a hand is what the word means; `rosters.yaml:1629-1631`) | no | nobody when made; its band is the examiner's obstacle later (`Record.forgery_quality`) | none | task (18_DET item 4: the band is the quality) | none (AR-16 note: `forge` draws on no skill, `rosters.yaml:1651`); no roll | **disagree**: no roll and no attribute |
| `found` (`:607`) | to found a new settlement from a planned works | **Reason**: planning and *"forecasting"* what a place needs (AR-21); **Presence**: drawing people to settle (AR-29) | none yet: a craft or stewardship skill is Jordan's content (U1 §5, `:307`) | no (`own`; the maker's standing) | nobody | none (settlements are reached at MATTER, not by this verb) | task (18_DET) | none; no roll | **disagree** |
| `build` (`:632`) | to have a building put up at a site | **Reason**: planning the works (AR-21); **Focus**: carrying it out without errors | none yet (U1 §5, `:307`) | no | nobody | none | task | none; no roll | **disagree** |
| `requisition` (`:1020`) | to take supplies from a place by official demand | **Presence**: being obeyed is social impact (AR-29) | `command` (P): *"the skill by which an order takes effect"* (glossary `:83`) | yes: `remit:issue`, the seat's authority | nobody: the stores refuse by precondition | none | task (18_DET) | none; no roll | **disagree** |
| `restore` (`:1362`) | to repair a place's fabric | **Coordination**: careful handwork, *"precise manoeuvres"* (AR-15); **Strength**: heavy work (AR-10's force) | none yet: a craft skill (U1 §5, `:307`) | no | nobody | none | task | none; no roll | **disagree** |
| `sabotage` (`:1403`) | to damage a place in secret | **Coordination**: quiet, precise hands, the lock-picker's attribute (AR-16); **Reason**: knowing where it will hurt (AR-21) | none: attribute only | no | nobody in the row; discovery is a later `examine` | none | task | none; no roll | **disagree** |
| `seize` (`:1449`) | to confiscate something by authority | **Presence**: authority's force on the holder (AR-29) | `law` (P): a seizure stands on its warrant | yes: `remit:issue` | the dispossessed holder's **Spirit**, refusing to yield (AR-44) | none | contest (18_DET: owed to the binding lane) | none; no roll | **disagree** |
| `survey` (`:1538`) | to compile an account of what a faction holds | **Reason**: putting known facts in order (AR-21); **Perception**: noticing what is missing (AR-24, AR-26a) | `inquiry` | no | nobody | none | task (18_DET) | none; no roll | **disagree** |
| `tend` (`:1557`) | to care for a sick or wounded person | **Focus**: attentive care without errors; **Coordination**: dressing a wound is precise handwork (AR-15) | `healing` (P; U1 §2 base Focus, `:133`) | no | nobody | none | task (18_DET) | none; no roll | **disagree** |
| `research` (`:1815`) | to consult records to learn something | **Reason**: *"understanding of concepts/facts"* (AR-21); **Focus**: filtering what is irrelevant (AR-21's caveat, AR-23) | `inquiry` | no | nobody (difficulty 2.0) | graded social roll (`rosters.yaml:1441`), then **field investigation** | task (graded) | `inquiry` → Reason | agree (the second attribute is new) |
| `reconstruct` (`:1881`) | to work out from what one knows what happened | **Reason**: logic and forecasting (AR-21); **Focus**: *"fail to filter and prioritize correctly"* is low Focus (AR-21) | `inquiry` | no | nobody | none (field investigation after its finding) | task; it waits today (K-37, `rosters.yaml:1435`) | none; no roll | **disagree** |
| `train` (`:1908`) | to teach someone a skill | **Attunement**: understanding the learner (AR-30) | the skill taught (the `kind` operand, `rosters.yaml: vocation_sourced`): the trainer's own score in it | no | nobody; the learner's own governing attribute of the skill taught is a level for the draw `[ASSUMPTION: the learner's aptitude helps the lesson take — basis: A-98 (1), an aptitude is an attribute]` | none | task (18_DET): today it raises by one, certain (row `writes_note`) | none; no roll | **disagree**: a certain gain |
| `recruit` (`:1932`) | to raise troops from a population | **Presence**: drawing men to the banner (AR-29); **Grace**: being seen as respectable and apt (AR-35) | `command` (P; U1 §5, `:305`) | no (`own`; the commander's standing) | nobody: the cohort's limit is the module's | mass battle's army record (`mass_battle.army`, a query, `module_contracts.yaml:99-102`): it computes limits and rolls nothing, so the turnout draw is the verb's | task (18_DET: turnout) | none; no roll | **disagree** |
| `form_unit` (`:1955`) | to create a new, empty unit in an army | — | — | — | — | mass battle's army record (query; no roll) | **no roll**: an administrative act on one's own army record | none; no roll | agree |
| `assign_troops` (`:1978`) | to move troops into or out of a unit | — | — | — | — | the same | **no roll** | none; no roll | agree |
| `disband_unit` (`:2001`) | to break up a unit, its men returning to the pool | — | — | — | — | the same | **no roll** | none; no roll | agree |
| `discharge_troops` (`:2024`) | to send unassigned troops home | — | — | — | — | the same | **no roll** | none; no roll | agree |
| `order_unit` (`:2047`) | to set a unit's role, stance and target | — | — | — | — | the same | **no roll** at the order: whether it is obeyed in the field is the field's order-friction draw on the commander's `command` (A-59 (1)) | none; no roll | agree |
| `transfer` (`:2070`) | to move goods from one's store to another's | — | — | — | — | none | **no roll** (18_DET `bookkeeping`) | none; no roll | agree |
| `work` (`:2101`) | to labour at a site to keep or raise it | **Endurance**: stamina, *"the likelihood of becoming tired"* (AR-20); **Strength**: the force of the labour (AR-10) | none yet: a craft skill (U1 §5, `:307`) | no | nobody | none | task (18_DET) | none; no roll | **disagree** |

### 2.4 Binding decision (12 rows)

| verb (row) | everyday meaning | governing attribute(s), with reason | skill | office modifier | opposed by | calls a subsystem? | roll? | current mapping | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `confer` (`:267`) | to appoint someone to an office | — | — | — | — | none | **no roll**: an appointment is the conferrer's to make; the world refuses it by precondition (conferral basis, 1-per-object). Grace's pull on who is chosen (AR-35) is a weight in the conferrer's choice (AR-04), not a roll. 18_DET lists it as a contest owed | none; no roll | agree |
| `convene` (`:287`) | to call a body to meet on a date | — | — | — | — | none | **no roll**: scheduling (18_DET `bookkeeping`) | none; no roll | agree |
| `determine` (`:360`) | to judge a matter and decide it | **Reason**: weighing facts and logic (AR-21); **Focus**: keeping irrelevant matter out of the judgement (AR-23) | `law` (P; U1 §5, `:302`; interim `argue`) | yes: `remit:determine`, the bench seat | the party's **Spirit**, resisting a binding finding (AR-44) | social contest (`a proposition`) | contest | `argue` → Presence; opposed by Presence; social roll, difficulty 1.0 | **disagree**: a judge is not an arguer (Presence → Reason) |
| `dispatch` (`:424`) | to order a person to go somewhere or do something | — | — | — | — | none | **no roll** at the order: *"their own choose decides"* (row `writes_note`) | none; no roll | agree |
| `establish` (`:441`) | to create a new office | — | — | — | — | none | **no roll**: a seat with the conferral basis creates it or is refused. 18_DET lists it as a contest owed | none; no roll | agree |
| `issue` (`:682`) | to send out a written order to those who must carry it out | — | — | — | — | none | **no roll** at issue: execution is each executor's `comply` or `evade / defy`, drawn in his choice. 18_DET lists it as `task` | none; no roll | agree |
| `marshal` (`:1095`) | to draw up an army's order of battle | **Reason**: arranging and forecasting (AR-21); **Presence**: the command that makes an order of battle hold (A-59's social attribute) | `command` (P) | yes: `remit:dispatch` | nobody | none at the act (the Record is read by mass battle at the field, `module_contracts.yaml:103-106`) | task (18_DET): the band is the order's quality carried into the field `[ASSUMPTION: 18_DET's task rows write a band; the field reading it is MB's to design]` | none; no roll | **disagree** |
| `surrender` (`:1128`) | to give a place up to another | — | — | — | — | none | **no roll**: a seat's decision, refused by precondition (purview) | none; no roll | agree |
| `pardon` (`:1266`) | to free someone from a punishment | — | — | — | — | none | **no roll**: the bench's act of grace on its own restraints. 18_DET lists it as a contest owed | none; no roll | agree |
| `release` (`:1345`) | to let go a bond or hold one owns | — | — | — | — | none | **no roll**: it closes the actor's own tenure. 18_DET lists it as a contest owed | none; no roll | agree |
| `revoke` (`:1386`) | to take an office back from its holder | **Presence**: the force of authority (AR-29) | `law` (P) | yes: `remit:revoke` | the holder's **Grace**: *"someone can occupy an office of low standing but have high grace, which will make people think well of them"* (AR-34) | none | contest (18_DET; `16_PESSIMIST_FA_A`: a dismissal can fail) | none; no roll | **disagree** |
| `succeed` (`:1505`) | to take up a vacant seat by right of title | — (where rival claims meet: **Grace**, *"the likelihood of … receiving an office"*, AR-35; **Presence**) | — | — | a rival claimant's **Grace** (if contested) | none | **no roll** on an uncontested title: the row requires no live hold and the title; rival claims are other men's acts. 18_DET lists it as a contest owed | none; no roll | agree |

### 2.5 Movement (2 rows)

| verb (row) | everyday meaning | governing attribute(s), with reason | skill | office modifier | opposed by | calls a subsystem? | roll? | current mapping | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `move` (`:1198`) | to travel from one place to another | **Endurance**: stamina on the road (AR-20) | none: attribute only | no | nobody | none | task (18_DET: Partial arrives a leg short) | none; no roll | **disagree** |
| `migrate` (`:1163`) | to move one's household to live elsewhere | **Endurance** (AR-20) | none | no | nobody; room at the destination refuses by precondition | none (housing is read by `world_q`, not called by the verb) | task (18_DET) | none; no roll | **disagree** |

**Count:** 21 + 9 + 23 + 12 + 2 = 67 rows; 35 disagree with the tree, 32 agree (§3).

### 2.6 Persuasion: what the teller brings and what the hearer weighs

Jordan's points (2026-11-13): the teller's roll is affected by his reason, his attunement, his knowledge of the other
person and his knowledge of plausibility; the hearer's side (the obstacle) by faction, opinion of the teller, fit with the
hearer's understanding of the world, benefit to the hearer, the hearer's pursuits and axes, and the relative rung of the
teller's seat. The two attributes are in the table (`tell`, `lie`; `argue` keeps the ruled Presence first). The rest are
facts the engine reads or does not:

| point | side | engine fact today | how it would enter |
|---|---|---|---|
| reason | teller | `attr.mind.acuity` in `Person.attributes` | the table's first or second attribute |
| attunement | teller | `attr.social.attunement`; note the tree already reads it on the RECEIVER's side, as his competence at weighing told claims (`decision/options.py:1690`, `competence`) | the table's first or second attribute |
| knowledge of the other person | teller | partial: `person_q.attributed_deeds(ledger, referent)` (`queries/person_q.py:158`) over the teller's own ledger; `world_q.proofs` already counts it against an opponent (`queries/world_q.py:852`) | a level for the roller per deed claim held, through B05.10's `edge` reader `[ASSUMPTION]` |
| knowledge of plausibility | teller | no fact yet: the teller may not read the hearer's ledger (AX-2); `person_q.lie_said_of` (`:1236`) picks the false value and scores nothing | no fact yet |
| faction | hearer | `world_q.faction_of(w, subject)` (`queries/world_q.py:2550`) for both sides | an obstacle term when the two cohere under different factions `[ASSUMPTION]` |
| opinion of the teller | hearer | `person_q.regard(p, referent, fx)` (`queries/person_q.py:424`); of his faction, `world_q.opinion_of(w, p, faction)` (`queries/world_q.py:3029`); a bench's, `world_q.reception` (`:792`, already an obstacle term, `rosters.yaml:1584-1586`) | hostile regard an obstacle term, favourable a level (U1 §4's situation row, `:263`) |
| fit with his understanding of the world | hearer | `decision/options.py::agreement(told, own)` (`:1521`): agreements and disagreements over two claim sets | an obstacle term per disagreement `[ASSUMPTION]` |
| benefit to the hearer | hearer | partial: `person_q.pursuit_lean(verb, e)` (`:684`) scores how a VERB points along a pursuit; no reader scores what accepting a Proposition gains the hearer | no fact yet for a Proposition |
| the hearer's pursuits and axes | hearer | `Person.pursuits`; the axis roster `descriptors.AXES` (`engine/substrate/descriptors.py:133`); `person_q.argued_pursuits` (`:723`) writes the result, no reader turns them into an obstacle term | no fact yet as an obstacle term |
| relative rung of the teller's seat | hearer | the `rank` stem, `RUNG_KINDS.index(r.kind)` (`queries/world_q.py:4694-4703`); `rank_gap` is proposed (OBS member 6, glossary `:86`) | `rank_gap`, the proposed obstacle term |

### 2.7 The self-plea: who stands opposite

Only `speak` has a form whose subject is the actor (`subject_may_be_self: True`, row `:1475`; the accused answers his own
matter). Today nobody opposes it: `seam/wrappers/sigma.py:220` reads no opposition for a subject who is the actor, and the
plea rolls at the stand-in under the room's terms (row `contests_note`). An accused man pleads TO someone. Proposed: the
opposition of a self-plea is **the accuser where there is one** (the holder of the petition that docketed the matter,
`DocketItem.petition`), resisting with his **Spirit**; **else the bench** (`heard_by: bench`, `rosters.yaml:1790`), read as
the presiding seat-holder's Spirit, with `reception` staying the room's term `[ASSUMPTION: an accusatorial hearing has an
accuser; a hearing on the court's own motion has only the bench — basis: `interrogate`'s note, the Church Tribunal is
accusatorial, row `:1783`]`. No other row has a self-subject form (`confer`'s `counterparty_may_be_self` is a self-appointment,
which does not roll).

### 2.8 The verbs that call a subsystem (Jordan's exception)

- **Exempt from the generic pool**: `fight`, `accept`, `capture` (personal combat), `march` (mass battle). Each rolls nothing
  of its own before the hand-off (declared at RESOLVE, fought at ENCOUNTER). Their inputs are the module's: combat reads the
  martial skill as `faculties` and six mapped attributes; mass battle reads no person attribute today.
- **Not exempt, though they reach a module**: the social roll's verbs (`tell`, `lie`, `argue`, `speak`, `arrest`,
  `determine`, `interrogate`) and the graded inquiries (`examine`, `research`, `surveil`). The module they reach,
  `social_contest.roll`, takes the pool the generic rule builds (`seam/wrappers/sigma.py:225`, `contest_input` passes
  `faculty`), so the verb's governing attributes ARE the module's input. When the hearing scene's nested run is built and
  reads its own inputs (`rosters.yaml:1379`), `speak` moves to the exempt class by its prize row, with no verb edit.
- **A module that rolls nothing**: the army verbs reach `mass_battle.army`, a query that edits the army record and computes
  limits; `recruit`'s turnout is therefore the verb's own task draw.
- **The tree's vocation attribute on an exempt verb** (`fight`, `accept`, `capture`: `arms` → Coordination) is the
  hand-off's input in intent (CR-85: `faculties` replaces `history`) and a **duplicate** in effect, since the module maps
  Coordination again as `agi` (§2.2). B05.09 removes `max(attr, have)` from the score, which ends the duplicate; the
  item in §5 makes the exempt rows name no attribute so it cannot return.

<!-- APPEND: 3 onward -->
