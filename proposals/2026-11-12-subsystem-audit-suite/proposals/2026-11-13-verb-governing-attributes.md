# VERBS · DICE — each verb names the attributes its everyday meaning relies on, or the seat that authorises it, or the subsystem it calls

Written: 2026-11-13, on Jordan's rulings of the same day, relayed in four messages: (1) *every verb's dice amount is set by
the character's attributes, skill (if relevant) and office (if relevant)*, and *"you should be able to logically
interrogate each verb based upon its everyday meaning for what 1-2 attributes are most reasonably applied"*; (2) a verb
whose act calls a subsystem into being does not roll the generic pool: the subsystem resolves it by its own rule; (3) a
verb may name one to three attributes, and they are AVERAGED (an attribute he does not hold counts at the untrained
score); (4) a verb that is a brute function (authorised, gated or recorded; its efficacy not in question) names no
attribute at all: attributes apply only where the act can succeed, partly succeed or fail by the doer's ability. Read at
the working tree of 2026-11-13.

**Depends on:** B04 (the skill definition rows, `references/descriptor_registry.yaml: capabilities`, U1 §2); B05.09
(`pool.py::governing_attribute`, the skill score with no attribute in it); the plan's verb-row `capability:` and
`difficulty:` columns (`10_DICE_one_score_two_roles.md` Edit C; D-U1-04, `workplan_v12_part18_cont.md:37`).
**Lands in batch:** folded into workplan v12 on 2026-11-13: B05.24 (DESIGN-FIRST) and B05.25 (BUILD) after B05.09
(`master/workplan_v12/workplan_v12_part8.md`); BA1.13 (CONTENT, Jordan's per-verb cells,
`workplan_v12_part18_cont.md`); B28.34 (DESIGN-FIRST) and B28.35 (BUILD), the persuasion terms and the self-plea
(`workplan_v12_part35_cont.md`).

## Status: PROPOSED

Design input, reference under CLAUDE.md §0.05. Lanes that own the files the plan items edit: IN
(`engine/season/verb_table.yaml`, `data/verbs.py`, `data/rosters.py`, `rosters.yaml`, `seam/wrappers/pool.py`,
`engine/dice_engine/sigma_leverage.py`), SC (B28's persuasion terms), with PC, MB, FA and FI owning the rows of their verbs.

## 0. The rule, and the method

**The rule, in one sentence an ordinary reader gets:** *a verb names one to three attributes; a person's governing score
for it is the average of his scores in them, rounded to the nearest tenth, a fraction like 2.5 staying a fraction (an
attribute he does not hold counts at the untrained score); his rank in the verb's skill, if the verb names one, is added; that number
plus the base, and never below the floor, is the dice he rolls (A-6); a verb that is a brute function of a seat, of his
own standing or of another's decision names no attribute and rolls nothing; and a verb that hands its act to a subsystem
(a fight, a field) names none either, because the subsystem reads him by its own rule.*

- **Three kinds.** Every row is one of: **(a) brute function** — the act is authorised, gated or recorded and cannot be
  done well or badly; the row names what authorises it, one of `seat` (a seat's remit, purview or conferral basis: the
  row's eligibility is `remit:` or its referent is an Office), `own` (an act on his own state or what he holds), or
  `counterparty` (another person's own decision completes it, drawn in that person's choice). **A brute row does not
  roll at all** (Jordan's clarification, 2026-11-13): not an empty pool, not a flat `pool_default` roll. It resolves by
  its gate: when the seat's purview and any standing the row names are met the act happens, and when they are not it is
  refused at formation (or, for a hand-built act, at the fold's `requires`). It never reaches `pool.faculty`, `pool.score`,
  `seam/wrappers/sigma.py` or the roll's stream (`loop/resolve.py:833`, `:893`, minted through `state/ids.py::draw_factory`;
  the keyed draw owner `engine/dice_engine/draw.py` is B06's, after B05; `engine/season/state/draw.py` does not exist at
  HEAD). **(b) efficacy-relevant** —
  the act can succeed, partly succeed or fail by the doer's ability: one to three attributes, a skill where one applies,
  the office modifier where it is done through a seat; **(c) hands off to a subsystem** — the row's `contests:` prize names
  a module that reads the person by its own rule.
- **An office act whose carrying out can be botched is (b), with the office modifier**, not (a): the seat makes it
  eligible, the doer's ability decides how well it is done (`arrest`, `interrogate`, `requisition`, `seize`, `raze`,
  `marshal`, `determine`; §3 item 5).
- **The mean and its rounding (Jordan, 2026-11-13).** The verb's governing score is the mean of the character's scores on
  its 1 to 3 attributes (an attribute he does not hold reads at the untrained score `pool_default`), rounded to the
  nearest tenth (a value halfway between two tenths rounds up); the result is a fractional number (`2.5`, not `3`) and
  feeds the dice as a fractional pool, as the engine already takes one (A-5; `sigma_leverage.py`'s continuous path). It is
  NOT rounded to a whole number and does not use `round_half_up`, which stays B38.55's, for integer counts. Attribute scores
  are integers on 1 to 7 (`descriptors.ATTRIBUTE_FLOOR`, `ATTRIBUTE_CEILING`), so the sum is exact and
  `governing_mean(scores) = (20 * sum(scores) + n) // (2 * n) / 10`, in integers until the last division. For `n` of 1 to
  3 the mean of integers is a multiple of a third, so a true half-tenth never occurs and the half-up clause is vacuous at
  this input; it is kept for the rule's completeness. Worked: Presence 6, Attunement 2, Reason 5 → 13 / 3 = 4.33 → 4.3;
  Perception 4, Reason 5 → 4.5; Spirit 3 held alone → 3.0.
- **The skill rank adds to the mean**, 0 where he holds none or the verb names no skill: an untrained man rolls on his
  attributes alone, and a first rank always adds a die `[ASSUMPTION: basis: ruling (1), "dice amount set by attributes,
  skill (if relevant)"; the plan's earlier form, the skill score as the only dice (B05.09 as first written), is what the
  ruling replaces]`. At control (`pool_add` 0, `pool_floor` 0) an unauthored person reads every attribute at
  `pool_default` and no rank, so his pool is `pool_default`, as before.
- **The office modifier** is the plan's one named level for an act through a seat (B05.20, U1-D), not a die: one channel
  already carries every seat effect, and a level and a die move the same roll (ladder step 5; ruling (1)'s "office (if
  relevant)" is honoured by the level, whose size is calibration's).
- **The opposition is unchanged in form**: the defender's skill score (A-79, B05.11) and his `opposed_attribute` as
  levels (A-79's *"aptitude … as named levels"*, B05.10's subject-side row). The column below names that attribute.
- **Method.** For each of the 67 rows of `engine/season/verb_table.yaml` (counted by `yaml.safe_load(...)['verbs']`), in
  the table's own strata: the everyday meaning first, in one sentence (a term of art named as such, with the ordinary word
  it is close to); then whether the doer's ability decides it; then the attributes most reasonably applied, each with one
  clause read from the attribute's own definition (§1). The tree's mapping was read only after, for the comparison column.

## 1. The ten attributes, in their own definitions

The roster is `engine/substrate/descriptors.py:50` (`ATTRIBUTES`), ten keys on 1 to 7
(`references/descriptor_registry.yaml:38-53`). The registry comments three of them only (`:48-53`); the definitions below
are Jordan's words, from the ruling that named the ten (`ED-IN-0328`, `registers/editorial_ledger_in.jsonl:107`) and the
rulings of 2026-11-05 by subject (`ED-IN-0347`, `:126`; verbatim in `proposals/2026-11-05-attribute-rulings-by-subject.md:36-105`).

| key | name | its own definition (verbatim) |
|---|---|---|
| `attr.body.strength` | Strength | *"the amount of damage a weapon can do … the ability to manage weapon heft, the ability to wear armour, the ability to leverage weapons, to push and force the opponent"* (AR-10); health and muscle mass (AR-11) |
| `attr.body.agility` | Coordination | *"coordination (agility and dexterity)"* (ED-IN-0328); *"accuracy with weapons and stable footing and dodging without losing balance and precise manoeuvres"* (AR-15); *"the quality of a forgery or ability to pick a lock"* (AR-16) |
| `attr.body.endurance` | Endurance | *"stamina, the ability to recover your breath, the likelihood of becoming tired which can impact concentration, and it contributes to someone's health/wounds"* (AR-20) |
| `attr.mind.focus` | Focus | *"focus (concentration, avoiding errors)"* (ED-IN-0328); *"less likely to be distracted as well as less likely to have irrelevant information impact their choices"* (AR-23) |
| `attr.mind.acuity` | Reason | *"reason (acuity, faculty, forecasting, predicting)"* (ED-IN-0328); *"mental acuity, logic, understanding of concepts/facts, forecasting, understanding what a choice entails"* (AR-21) |
| `attr.mind.will` | Spirit | *"the ability to stay true to yourself and be free of external influence or compulsion, the capacity to tolerate harm and strain and stress, the likelihood to perform threadwork without losing coherence, the ability to get good results despite poor circumstances, to overcome an obstacle"* (AR-44) |
| `attr.mind.perception` | Perception | *"awareness of surroundings, noticing information"* (ED-IN-0328; `descriptor_registry.yaml:48`); *"surveillance and fieldwork and noticing things out of place"* (AR-24); *"it concerns FACTUAL matters"* (AR-26) |
| `attr.social.attunement` | Attunement | *"attunement (reading people)"* (ED-IN-0328); *"understanding other characters in terms of their intentions in a given moment as well as their pursuits convictions ambitions goals desires"* (AR-30); *"the likelihood of forming knots/bonds"* (AR-31) |
| `attr.social.charisma` | Presence | *"charisma magnetism social impact"* (AR-29, governing AR-27 and AR-28) |
| `attr.social.grace` | Grace | *"composure (ability to remain calm under pressure, nerve)"*, *"composure and remaining calm and etiquette and manners"* (ED-IN-0328); *"being seen as respectable/dignified"* (AR-33); *"different kinds of social contests and venues may prioritize grace"* (AR-36) |

## 2. The table, by the verb table's strata

Legend. **kind**: (a) brute function, with its authoriser; (b) efficacy-relevant, with how it rolls (`contest` on a
`contests:` prize; `graded` on the inquiry route; `task` on the draw `18_DETERMINISM_task_draw_for_uncontested_verbs.md`
proposes, inert until B07); (c) subsystem. **attributes** are averaged. **current**: the tree's mapping today —
`verb_capability` skill → `vocation_attribute` attribute (`rosters.yaml:1550-1571`, `:1665-1668`); the opposing attribute
(`opposed_by: {}` ships empty, `:1676`, so a person opposes with the row's own attribute, `pool.py:68-75`); the roll today
(the social roll's `task_difficulty` rows, `rosters.yaml:1598-1607`; the prize rows; else the flat fold, no roll). A verb
with no `verb_capability` row pools at `pool_default` for everyone (`pool.py:112-117`). Row numbers are the `verb:` lines
of `engine/season/verb_table.yaml`.

### 2.1 Social (21 rows)

| verb (row) | everyday meaning | kind | attributes (averaged), or what authorises it | skill | office modifier | opposed by | calls a subsystem? | current | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `carry` (`:108`) | to take a petition up and put it before a forum (term of art, close to "present" or "sponsor") | (b) task | **Presence**, getting a forum to take a matter up is social impact (AR-29); **Grace**, done properly for the venue (AR-36) | `law` (P) | no (`own`) | nobody: the difficulty | none | no skill; no roll | **disagree**: can fail, rolls nothing |
| `argue` (`:133`) | to give someone reasons meant to change his mind | (b) contest | **Presence**, ruled the main component (ED-IN-0350, `editorial_ledger_in.jsonl:129`); **Attunement**, how the other is receiving it (same ruling; Jordan 2026-11-13 puts it in the roll); **Reason**, the case's logic (AR-21; Jordan's teller points) | `argue` | no (`own`); the seat gap is a hearer-side term (§2.6) | the hearer's **Spirit**, *"free of external influence"* (AR-44; CR-96's reading, `rosters.yaml:1669-1670`) | social contest (`social_contest.roll`, `a proposition`): its input is the generic pool, so not exempt | `argue` → Presence; opposed by Presence; social roll | **disagree**: opposition, and two attributes added |
| `commit` (`:209`) | to bind oneself publicly to a statement or cause | (a) `own`; roll: none | his own pledge: the row writes only his own `Tenure.since` | — | — | — | none | none; no roll | agree |
| `comply` (`:227`) | to do what an order requires | (a) `own`; roll: none | his decision on a writ he holds (`requires`); what compliance performs is the separate act the writ names (row `writes_note`), which rolls on its own row | — | — | — | none | none; no roll | agree |
| `conceal` (`:251`) | to take on a cover (a false identity about oneself) | (b) task | **Grace**, a calm, correct face under scrutiny (*"composure … nerve"*); **Focus**, not slipping out of the part (*"avoiding errors"*) | `deception` (P) | no | nobody when cast; the band is the examiner's obstacle later (18_DET item 4) | none | none; no roll | **disagree** |
| `covenant` (`:300`) | to offer another party a formal binding agreement | (a) `seat`; roll: none | `remit:issue`; acceptance is the counterparty's own act | — | — | — | none | none; no roll | agree |
| `lie` (`:534`) | to say what one knows is false so another believes it | (b) contest | **Attunement**, what this hearer will believe (AR-30); **Reason**, a consistent, plausible story (AR-21; Jordan's "knowledge of plausibility"); **Grace**, the liar's nerve (*"composure … nerve"*; U1 §2's `deception.base`, `U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:129`) | `deception` (P) | no | the hearer's **Attunement**, seeing intention in the moment (AR-30); U1 §2 says Perception, ruled *"FACTUAL matters"* (AR-26): the content's fit is an engine fact (§2.6) | social contest (`a standing`) | no skill row: pool and opposition at `pool_default` (`rosters.yaml:1563-1567`) | **disagree**: no attribute on either side |
| `forgive` (`:573`) | to stop holding a wrong against someone | (a) `own`; roll: none | his own stance rows (row `writes_note`) | — | — | — | none | none; no roll | agree |
| `give` (`:657`) | to hand something one holds to another | (a) `own`; roll: none | he holds it and the receiver is present (`requires`) | — | — | — | none | none; no roll | agree |
| `oblige` (`:1217`) | to take on a duty to a seat (term of art, close to "pledge service") | (a) `seat`; roll: none | the seat's `binds` admits the joiner (`requires`; referent an Office) | — | — | — | none | none; no roll | agree |
| `open_case` (`:1239`) | to begin formal proceedings on a matter | (a) `seat`; roll: none | `remit:determine`; the act declares the stages (`requires`); how the matter is judged is `determine`'s | — | — | — | none | none; no roll | agree (18_DET's `task` class disagreed with) |
| `petition` (`:1294`) | to ask an authority formally for something | (a) `counterparty`; roll: none | filing; the addressee's answer is his own act (18_DET `bookkeeping`); the persuasion is where the matter is heard (`speak`) | — | — | — | none | none; no roll | agree |
| `construe` (`:1320`) | to interpret terms, here to one's own advantage | (a) `own`; roll: none | his own reading, a belief (row `writes_note`) | — | — | — | none | none; no roll | agree |
| `speak` (`:1475`) | to address a hearing on a matter before it (to plead, when it is one's own) | (b) contest | **Presence**, moving a room (AR-29); **Reason**, the case (AR-21; Jordan's teller points); **Grace**, a venue penalizes one *"not doing it right"* (AR-36a) | `argue` (U1, `:139`) | yes where he speaks from a seat in the body that hears him (U1-D `heard_by`); else the gap is a hearer-side term | the matter's party: his **Spirit** (AR-44); the self-plea, §2.7 | social contest (`a matter`, `heard_by: bench`, `rosters.yaml:1786-1790`); the hearing's nested run is unbuilt (`:1379`) | `copying` → Focus; opposed by Focus | **disagree**: a copyist's attribute |
| `tell` (`:1582`) | to pass on to someone something one knows | (b) contest | **Reason**, knowing the matter and making it hang together (AR-21; "knowledge of plausibility"); **Attunement**, putting it to this hearer (AR-30) | none: attribute only (`copying` is a faithful reproduction of a text, `rosters.yaml:1629-1631`) | no | the hearer's **Spirit** (AR-44) | social contest (`a standing`) | `copying` → Focus; opposed by Focus | **disagree**: attribute and skill |
| `interview` (`:1767`) | to question someone to learn what he knows | (a) `counterparty`; roll: none | a prompt: the questioned person answers by his own `tell`, which is drawn (`rosters.yaml:1433-1434`, K-36) | — | — | — | none (`finding.made` reaches `fieldwork.find`) | none; no roll | agree (18_DET's contest class disagreed with) |
| `interrogate` (`:1783`) | to question a prisoner hard to get a confession | (b) contest, an office act that can be botched | **Attunement**, how near he is to breaking (AR-30; AR-42); **Presence**, the questioner's force (AR-29) | `inquiry` (U1 §5, `:300`) | yes: `remit:determine` | the prisoner's **Spirit**, *"free of … compulsion, the capacity to tolerate harm and strain"* (AR-44) | social contest (`a proposition`) | `inquiry` → Reason; opposed by Reason | **disagree**: both attributes |
| `tie / knot` (`:1896`) | to form a close personal bond with someone | (b) task | **Attunement**, ruled to govern *"the likelihood of forming knots/bonds"* (AR-31) | none | no | nobody's attribute: the other's regard is the term (`person_q.regard`) | none | none; no roll | **disagree**: AR-31 says *likelihood* |
| `utter` (`:2090`) | to put something into words | (a) `own`; roll: none | it makes a Proposition exist; belief in it is a later `tell` or `argue` | — | — | — | none | none; no roll | agree |
| `evade / defy` (`:457`) | to dodge an order quietly, or refuse it openly | (a) `own`; roll: none | his decision; *"disobedience others see or miss"* is the witnesses' noticing (row `writes_note`) | — | — | — | none | none; no roll | agree |
| `challenge` (`:925`) | to call someone out to fight | (a) `counterparty`; roll: none | a declaration (a `challenge` Record); the answer is the other man's `accept` | — | — | — | none (the fight is `accept`'s) | none; no roll | agree |

### 2.2 Contested physical (9 rows)

| verb (row) | everyday meaning | kind | attributes (averaged), or what authorises it, or the subsystem's inputs | skill | office modifier | opposed by | calls a subsystem? | current | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `arrest` (`:171`) | to seize a person by authority and take him into custody | (b) contest, an office act that can be botched | **Strength**, *"to push and force the opponent"* (AR-10); **Presence**, men submit to the bearing of authority (AR-29) | `arms` (U1 §5, `:303`) | yes: `remit:dispatch` | the subject's **Strength** (Coordination the competitor) | social contest today (`a standing`); the row's own question, standing or body: §6 Q1 | `arms` → Coordination; opposed by Coordination | **disagree**: Coordination → Strength, Presence |
| `fight` (`:733`) | to try to hurt or overcome someone by force | (c) | none of the verb's own: combat reads the martial skill `arms` (pool `max(5, skill + 6)`, the six base dice, `modules/combat/core.py:51-52`) and six attributes mapped from `Person.attributes`: Strength, Coordination, Endurance, Perception, Spirit, Focus (`modules/combat/attributes.py:45-50`) | `arms` (input) | no | combat's rule (A-71, A-79) | **personal combat** (`combat.fight`, `module_contracts.yaml:58-62`; `the body`); declared at RESOLVE, fought at ENCOUNTER (`rosters.yaml:1740-1741`): no roll before the hand-off | `arms` → Coordination through `faculty`, passed as `faculties` (`seam/wrappers/combat.py:215-229`) | **disagree: a duplicate.** An authored Coordination reaches the fight twice: in `faculty`'s `max(attr, have)` (`pool.py:107-108`) and as combat's `agi` (`attributes.py:46`; `fight.py:46-52`; passed at `combat.py:231-232`); the roster note that `agi` is the class default (`rosters.yaml:1660-1663`) predates PC-06 K-1 |
| `capture` (`:866`) | to take someone prisoner by force | (c) | as `fight` | `arms` (input) | yes: `remit:dispatch` | combat's rule, `yield` terms | **personal combat** (`the body`) | as `fight` | **disagree**: the same duplicate |
| `accept` (`:961`) | to take up a challenge, and fight it | (c) | as `fight` | `arms` (input) | no | combat's rule | **personal combat** (`the body`) | as `fight` | **disagree**: the same duplicate |
| `march` (`:1057`) | to lead an army to a place, and fight what meets it there | (c) | none of the verb's own: the field reads the commander's **command** (P; A-59, `DECISIONS_ANSWERED.md:73`) and each unit's prowess; today no person attribute (no `attributes` read in `seam/wrappers/mass_battle.py`) | `command` (P, input) | yes: `remit:dispatch` | the field's rule | **mass battle** (`mass_battle.resolve_field`, `module_contracts.yaml:64-68`; `a field`) | none (U1 §5 `none`, `:304`) | agree |
| `raze` (`:1426`) | to destroy a captured town utterly | (b) task, an office act that can be botched | **Presence**, an ugly order carried out is obedience to command (A-59; AR-29) | `command` (P) | yes: `remit:dispatch` | nobody | none (the field was `march`'s, row `writes_note`) | none; no roll | **disagree** |
| `examine` (`:1738`) | to look closely at a place to find out what happened there | (b) graded | **Perception**, *"noticing things out of place"* (AR-24), *"FACTUAL matters"* (AR-26); **Reason**, what the traces mean (AR-21) | `inquiry` | no | nobody (difficulty); a forger's or concealer's band | graded social roll (`rosters.yaml:1442`), then **field investigation** (`fieldwork.find`, `module_contracts.yaml:120-123`) on the grade: not exempt | `inquiry` → Reason | **disagree**: Perception added; CR-96 named the clash and stopped (`rosters.yaml:1650-1654`) |
| `surveil` (`:1838`) | to watch a place or person secretly over time | (b) graded | **Perception**, ruled for *"surveillance"* (AR-24); **Focus**, watching without lapses (AR-23) | `inquiry` | no | nobody; a watched person's **Perception** once the Person case is built (`rosters.yaml:1436-1437`) | graded social roll, then field investigation | `inquiry` → Reason | **disagree** |
| `thread_read` (`:1863`) | to sense the Thread at a site (term of art, close to "divine") | (b) task | **Spirit**, *"the likelihood to perform threadwork without losing coherence"* (AR-44) | none: Thread Sensitivity is the gate, not a skill (glossary `:84`, A-11) | no | nobody | none | none; no roll (waits, `rosters.yaml:1435-1436`) | **disagree** |

### 2.3 Uncontested material (23 rows)

| verb (row) | everyday meaning | kind | attributes (averaged), or what authorises it | skill | office modifier | opposed by | calls a subsystem? | current | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `create_record` (`:327`) | to write a document | (a) `own`; roll: none | his own paper (18_DET `bookkeeping`); a false one is `forge` | — | — | — | none | none; no roll | agree |
| `destroy_record` (`:338`) | to destroy a document one holds | (a) `own`; roll: none | he holds it (`requires`); what it leaves is a witness question | — | — | — | none | none; no roll | agree (18_DET's `task` disagreed with) |
| `exchange` (`:480`) | to trade goods with another | (a) `counterparty`; roll: none | both stores cover the terms or it is refused; each side's consent is his own choice | — | — | — | none | none; no roll | agree |
| `forge` (`:508`) | to make a false document | (b) task | **Coordination**, ruled for *"the quality of a forgery"* (AR-16); **Focus**, *"avoiding errors"* | `copying` (a faithful reproduction of a hand) | no | nobody when made; its band is the examiner's obstacle | none | none (`rosters.yaml:1651`); no roll | **disagree** |
| `found` (`:607`) | to found a settlement from a planned works | (b) task | **Reason**, planning and *"forecasting"* (AR-21); **Presence**, drawing settlers (AR-29) | none yet (U1 §5, `:307`) | no | nobody | none | none; no roll | **disagree** |
| `build` (`:632`) | to have a building put up at a site | (b) task | **Reason**, planning the works; **Focus**, without errors | none yet | no | nobody | none | none; no roll | **disagree** |
| `requisition` (`:1020`) | to take supplies from a place by official demand | (b) task, an office act that can be botched | **Presence**, being obeyed (AR-29) | `command` (P; glossary `:83`) | yes: `remit:issue` | nobody; short stores refuse | none | none; no roll | **disagree** |
| `restore` (`:1362`) | to repair a place's fabric | (b) task | **Coordination**, *"precise manoeuvres"* (AR-15); **Strength**, heavy work (AR-10) | none yet (craft) | no | nobody | none | none; no roll | **disagree** |
| `sabotage` (`:1403`) | to damage a place in secret | (b) task | **Coordination**, quiet, precise hands (AR-16); **Reason**, where it will hurt (AR-21) | none | no | nobody in the row | none | none; no roll | **disagree** |
| `seize` (`:1449`) | to confiscate something by authority | (b) contest, an office act that can be botched | **Presence**, authority's force on the holder (AR-29) | `law` (P) | yes: `remit:issue` | the holder's **Spirit**, refusing to yield (AR-44) | none | none; no roll | **disagree** |
| `survey` (`:1538`) | to compile an account of what a faction holds | (b) task | **Reason**, putting known facts in order (AR-21); **Perception**, noticing what is missing (AR-26a) | `inquiry` | no | nobody | none | none; no roll | **disagree** |
| `tend` (`:1557`) | to care for a sick or wounded person | (b) task | **Focus**, care without errors; **Coordination**, dressing a wound (AR-15) | `healing` (P; U1 §2 `:133`) | no | nobody | none | none; no roll | **disagree** |
| `research` (`:1815`) | to consult records to learn something | (b) graded | **Reason**, *"understanding of concepts/facts"* (AR-21); **Focus**, filtering the irrelevant (AR-23) | `inquiry` | no | nobody | graded social roll (`rosters.yaml:1441`), then field investigation | `inquiry` → Reason | agree (Focus added) |
| `reconstruct` (`:1881`) | to work out from what one knows what happened | (b) task | **Reason**, logic and forecasting (AR-21); **Focus**, *"filter and prioritize correctly"* (AR-21) | `inquiry` | no | nobody | none | none; no roll (waits, K-37) | **disagree** |
| `train` (`:1908`) | to teach someone a skill | (b) task | **Attunement**, understanding the learner (AR-30) | the skill taught (the `kind` operand), the trainer's own rank in it | no | nobody | none | none; a certain +1 (row `writes_note`) | **disagree** |
| `recruit` (`:1932`) | to raise troops from a population | (b) task | **Presence**, drawing men to the banner (AR-29); **Grace**, being seen as apt (AR-35) | `command` (P; U1 §5 `:305`) | no (`own`) | nobody | mass battle's army record (`mass_battle.army`, a query that rolls nothing, `module_contracts.yaml:99-102`): not exempt | none; no roll | **disagree** |
| `form_unit` (`:1955`) | to create a new, empty unit in an army | (a) `own`; roll: none | his own army record | — | — | — | army record (query) | none; no roll | agree |
| `assign_troops` (`:1978`) | to move troops into or out of a unit | (a) `own`; roll: none | as `form_unit` | — | — | — | the same | none; no roll | agree |
| `disband_unit` (`:2001`) | to break up a unit | (a) `own`; roll: none | as `form_unit` | — | — | — | the same | none; no roll | agree |
| `discharge_troops` (`:2024`) | to send unassigned troops home | (a) `own`; roll: none | as `form_unit` | — | — | — | the same | none; no roll | agree |
| `order_unit` (`:2047`) | to set a unit's role, stance and target | (a) `own`; roll: none | his own army record; whether it is obeyed in the field is the field's order-friction draw on `command` (A-59 (1)) | — | — | — | the same | none; no roll | agree |
| `transfer` (`:2070`) | to move goods from one's store to another's | (a) `own`; roll: none | his store covers it (`requires`) | — | — | — | none | none; no roll | agree |
| `work` (`:2101`) | to labour at a site to keep or raise it | (b) task | **Endurance**, *"the likelihood of becoming tired"* (AR-20); **Strength**, the labour's force (AR-10) | none yet (craft) | no | nobody | none | none; no roll | **disagree** |

### 2.4 Binding decision (12 rows)

| verb (row) | everyday meaning | kind | attributes (averaged), or what authorises it | skill | office modifier | opposed by | calls a subsystem? | current | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `confer` (`:267`) | to appoint someone to an office | (a) `seat`; roll: none | the conferral basis and 1-per-object (`requires`); Grace's pull on who is chosen (AR-35) weighs the choice (AR-04), not a roll | — | — | — | none | none; no roll | agree |
| `convene` (`:287`) | to call a body to meet on a date | (a) `seat`; roll: none | `remit:convene` | — | — | — | none | none; no roll | agree |
| `determine` (`:360`) | to judge a matter and decide it | (b) contest, an office act that can be botched | **Reason**, weighing facts and logic (AR-21); **Focus**, keeping the irrelevant out (AR-23) | `law` (P; U1 §5 `:302`; interim `argue`) | yes: `remit:determine` | the party's **Spirit** (AR-44) | social contest (`a proposition`) | `argue` → Presence; opposed by Presence | **disagree**: a judge is not an arguer |
| `dispatch` (`:424`) | to order a person to go or act | (a) `seat`; roll: none | `remit:dispatch`; *"their own choose decides"* (row `writes_note`) | — | — | — | none | none; no roll | agree |
| `establish` (`:441`) | to create a new office | (a) `seat`; roll: none | the conferral basis and a rung (`requires`) | — | — | — | none | none; no roll | agree |
| `issue` (`:682`) | to send out a written order | (a) `seat`; roll: none | `remit:issue`; execution is each executor's own act | — | — | — | none | none; no roll | agree (18_DET's `task` disagreed with) |
| `marshal` (`:1095`) | to draw up an army's order of battle | (b) task, an office act that can be botched | **Reason**, arranging and forecasting (AR-21); **Presence**, the command that makes it hold (A-59) | `command` (P) | yes: `remit:dispatch` | nobody | none at the act (the field reads the Record, `module_contracts.yaml:103-106`) | none; no roll | **disagree** |
| `surrender` (`:1128`) | to give a place up to another | (a) `seat`; roll: none | the seat's purview (`requires`) | — | — | — | none | none; no roll | agree |
| `pardon` (`:1266`) | to free someone from a punishment | (a) `seat`; roll: none | the bench seat over him (`requires`) | — | — | — | none | none; no roll | agree |
| `release` (`:1345`) | to let go a bond or hold one owns | (a) `own`; roll: none | his own tenure (`requires`) | — | — | — | none | none; no roll | agree |
| `revoke` (`:1386`) | to take an office back from its holder | (a) `seat`; roll: none | the revocation basis and a live hold (`requires`); a holder who resists answers by his own acts | — | — | — | none | none; no roll | agree (18_DET's contest class disagreed with) |
| `succeed` (`:1505`) | to take up a vacant seat by right of title | (a) `seat`; roll: none | no live hold and the title its `successions` names (`requires`); rival claims are other men's acts | — | — | — | none | none; no roll | agree |

### 2.5 Movement (2 rows)

| verb (row) | everyday meaning | kind | attributes (averaged) | skill | office modifier | opposed by | calls a subsystem? | current | agree? |
|---|---|---|---|---|---|---|---|---|---|
| `move` (`:1198`) | to travel from one place to another | (b) task | **Endurance**, stamina on the road (AR-20) | none | no | nobody | none | none; no roll | **disagree** |
| `migrate` (`:1163`) | to move one's household to live elsewhere | (b) task | **Endurance** (AR-20) | none | no | nobody; room at the destination refuses | none | none; no roll | **disagree** |

**Count:** 21 + 9 + 23 + 12 + 2 = 67 rows. Kinds: (a) 32, (b) 31, (c) 4. Against the tree: 33 disagree, 34 agree.

### 2.6 Persuasion: what the teller brings and what the hearer weighs

Jordan's points (2026-11-13): the teller's roll is affected by his reason, his attunement, his knowledge of the other
person and his knowledge of plausibility; the hearer's side (the obstacle) by faction, opinion of the teller, fit with the
hearer's understanding of the world, benefit to the hearer, the hearer's pursuits and axes, and the relative rung of the
teller's seat. The two attributes are in the rows above. The rest are facts the engine reads or does not; B28.34 designs
their terms, B28.35 builds them.

| point | side | engine fact today | how it would enter |
|---|---|---|---|
| reason | teller | `attr.mind.acuity` in `Person.attributes` | one of the averaged attributes |
| attunement | teller | `attr.social.attunement`; the tree already reads it on the RECEIVER's side, as his competence at weighing told claims (`decision/options.py:1690`, `competence`) | one of the averaged attributes |
| knowledge of the other person | teller | partial: `person_q.attributed_deeds(ledger, referent)` (`queries/person_q.py:158`) over the teller's own ledger; `world_q.proofs` already counts it against an opponent (`queries/world_q.py:852`) | a level for the roller per deed claim held `[ASSUMPTION]` |
| knowledge of plausibility | teller | no fact yet: the teller may not read the hearer's ledger (AX-2); `person_q.lie_said_of` (`:1236`) picks the false value and scores nothing | no fact yet |
| faction | hearer | `world_q.faction_of(w, subject)` (`queries/world_q.py:2550`) for both sides | an obstacle term when the two cohere under different factions `[ASSUMPTION]` |
| opinion of the teller | hearer | `person_q.regard(p, referent, fx)` (`queries/person_q.py:424`); of his faction, `world_q.opinion_of(w, p, faction)` (`queries/world_q.py:3029`); a bench's, `world_q.reception` (`:792`, already an obstacle term, `rosters.yaml:1584-1586`) | hostile an obstacle term, favourable a level (U1 §4's situation row, `:263`) |
| fit with his understanding of the world | hearer | `decision/options.py::agreement(told, own)` (`:1521`), agreements and disagreements over two claim sets | an obstacle term per disagreement `[ASSUMPTION]` |
| benefit to the hearer | hearer | partial: `person_q.pursuit_lean(verb, e)` (`:684`) scores a VERB along a pursuit; nothing scores what accepting a Proposition gains him | no fact yet for a Proposition |
| the hearer's pursuits and axes | hearer | `Person.pursuits`; `descriptors.AXES` (`engine/substrate/descriptors.py:133`); `person_q.argued_pursuits` (`:723`) writes the result; no reader turns them into an obstacle term | no fact yet as a term |
| relative rung of the teller's seat | hearer | the `rank` stem, `RUNG_KINDS.index(r.kind)` (`queries/world_q.py:4694-4703`); `rank_gap` is proposed (OBS member 6, glossary `:86`) | `rank_gap` |

### 2.7 The self-plea: who stands opposite

Only `speak` has a form whose subject is the actor (`subject_may_be_self: True`, row `:1475`). Today nobody opposes it:
`seam/wrappers/sigma.py:220` reads no opposition for a subject who is the actor, and the plea rolls at the stand-in under
the room's terms (row `contests_note`). An accused man pleads TO someone. Proposed: the opposition of a self-plea is **the
accuser where there is one** (the holder of the petition that docketed the matter, `DocketItem.petition`), resisting with
his **Spirit**; **else the bench** (`heard_by: bench`, `rosters.yaml:1790`), the presiding seat-holder's Spirit, with
`reception` staying the room's term `[ASSUMPTION: an accusatorial hearing has an accuser; a hearing on the court's own
motion has only the bench — basis: `interrogate`'s note, the Church Tribunal is accusatorial, row `:1783`]`. No other row
has a self-subject form (`confer`'s `counterparty_may_be_self` is a self-appointment, kind (a)). Built at B28.35.

### 2.8 The verbs that call a subsystem (kind c)

- **Exempt from the generic pool**: `fight`, `accept`, `capture` (personal combat), `march` (mass battle). Each rolls nothing
  of its own before the hand-off. Combat reads the martial skill as `faculties` and six mapped attributes; mass battle reads
  no person attribute today.
- **Not exempt, though they reach a module**: the social roll's verbs and the graded inquiries reach
  `social_contest.roll`, which takes the pool the generic rule builds (`seam/wrappers/sigma.py:225`, `contest_input` passes
  `faculty`), so the verb's attributes ARE the module's input. When the hearing scene's nested run is built and reads its
  own inputs (`rosters.yaml:1379`), `speak` moves to (c) by its prize row, with no verb edit. The army verbs reach
  `mass_battle.army`, a query that rolls nothing.
- **The tree's attribute on a (c) verb** (`fight`, `accept`, `capture`: `arms` → Coordination) is the hand-off's input in
  intent (CR-85) and a **duplicate** in effect (§2.2). B05.09 ends it by removing `max(attr, have)` from the score; B05.25
  makes (c) rows name no attribute, so it cannot return.

## 3. Disagreements with the tree, ranked by how much the game changes

33 of 67 rows disagree. Most game-changing first:

1. **The persuasion and judging verbs roll on the wrong attribute, or on none** (`tell`, `speak`, `lie`, `argue`'s
   opposition, `determine`, `interrogate`). These are the season's most frequent rolls. `tell` and `speak` read Focus
   because their skill is `copying` (`rosters.yaml:1550-1551`, `:1665`); a lie reads no attribute on either side
   (`:1563-1567`); every opposition reads the roller's own attribute because `opposed_by` ships empty (`:1676`).
2. **The governing attribute lives on the skill, and one skill serves verbs that rely on different attributes**:
   `inquiry` serves `examine`, `surveil` (Perception, AR-24) and `research` (Reason); `argue` serves `argue` and `speak`;
   `arms` serves `arrest` and the fight. CR-96 found it and stopped (*"one row cannot serve both"*,
   `rosters.yaml:1652-1654`); U1 §2 lands the same shape again as the skill row's `base:`
   (`U1_CAPABILITY_AUTHORING_ARCHITECTURE.md:95, 123-133`). Ladder step 4 answers it: the plan already put the verb's
   skill and difficulty on the verb row, and B05.10's level row is keyed `verb.base`. The verb row owns its attributes;
   `vocation_attribute` and the skill row's `base:`/`opposed_by:` retire (B05.25).
3. **Personal combat reads an authored Coordination twice** (`fight`, `accept`, `capture`: §2.2).
4. **Seventeen efficacy rows roll nothing** (`carry`, `conceal`, `tie / knot`, `raze`, `thread_read`, `forge`, `found`,
   `build`, `requisition`, `restore`, `sabotage`, `seize`, `survey`, `tend`, `reconstruct`, `train`, `recruit`, `work`,
   `marshal`, `move`, `migrate`, as the table marks them). 18_DET gives most a draw; without attributes that draw varies by
   seed alone, every person alike.
5. **Office acts with a hidden efficacy, made (b) with the office modifier**: `arrest`, `interrogate`, `requisition`,
   `seize`, `raze`, `marshal`, `determine`. Each is made eligible by a seat (`remit:`) but carried out well or badly by the
   man who holds it: a warrant served clumsily, a confession not got, a levy that falls short, a seizure the holder hides
   from, a town half-razed, an order of battle badly drawn, a judgement that does not hold.
6. **Rows the tree sends through a roll that are really brute functions**: none, so no row loses a roll at this tree. The
   tree rolls ten verbs on the social roll (`rosters.yaml:1598-1607`) and four through modules; all ten are efficacy acts.
   Later batches would roll some (a) rows: B07's task class (18_DET: `open_case`, `destroy_record`, `issue`) and B28's
   drawn bands on `give` (B28.02), `forgive` (B28.05), `challenge` (B28.06), `commit` (B28.08), `covenant` (B28.09): §6 Q2. The nearest is `determine` (a judge's word binds by his seat);
   it stays (b) by precedent (step 4: SC-03b made it a contested act with band-keyed writes, row `contests_note`), and its
   one `pool_default` reading is its skill's, not its kind.
7. **The self-plea is opposed by nobody** (§2.7); **`tie / knot` is certain** where AR-31 rules a likelihood; smaller
   opposition choices: `lie` opposed by Attunement (U1 §2 says Perception), `arrest` on Strength.

**Disagreements with proposals, not the tree** (for their lanes): 18_DET's class for `covenant`, `challenge`, `interview`,
`confer`, `establish`, `pardon`, `release`, `revoke`, `succeed` (contest owed → (a): the contested part is another
person's answer or a precondition), `open_case`, `destroy_record`, `issue` (task → (a)), and `tie / knot` (bookkeeping →
(b), AR-31); U1 §2's `deception` row (Grace, opposed by Perception → the verb rows: three averaged for `lie`, opposed by
Attunement).

## 4. What a test would assert

The loader refuses, the test shows it. `engine/season/tests/test_verb_governing_attributes.py` (B05.25):

- **`test_every_verb_row_names_its_attributes_or_its_authority_or_its_subsystem`**: each row of `data/verbs.py::VERB_TABLE`
  takes exactly one of (a) `brute:` one of `seat`, `own`, `counterparty`, with a non-empty `brute_note`, and `seat` only
  on a row whose eligibility carries a `remit:` or whose referent class is `Office`; (b) `governing:` one to three distinct
  members of `descriptors.ATTRIBUTES`, plus `opposed_attribute:` where the row is contested against a person; (c) the
  exemption: its `contests:` prize row says `person_inputs: own`, and then it names neither of the others. A row contested
  on a `person_inputs: pool` prize must take (b). The loop asserts `checked == len(VERB_TABLE)` (67 at writing).
- **`test_a_brute_row_carrying_governing_or_a_difficulty_is_refused`**: a `brute:` row given `governing:`, a
  `difficulty:` cell or a `task_difficulty` row → the loader raises, naming the verb.
- **`test_a_brute_verb_twice_on_one_state_is_one_outcome_and_no_draw`**: on two deep copies of one built world, one hand-built
  act of each brute verb the realm can form (at least `give`, `confer`, `dispatch`) is resolved; the two Event lists and
  `content_hash()` are equal, and a counting wrapper on `state/ids.py::draw_factory`'s returned `draw` (the stream the roll
  is minted from, `loop/resolve.py:833`, `:893`) records zero calls whose purpose begins `roll:` for those acts, with
  `pool.faculty` and `pool.score` patched to raise; the test asserts it asserted (`checked >= 3`). At B06 the counter moves
  to the keyed draw owner's own count.
- **`test_a_row_naming_none_is_refused_at_load`**: one row's columns removed → the loader raises, naming the verb. The
  falsifier: without it a new verb ships on `pool_default` for everyone, which is how `lie` shipped.
- **`test_a_verb_is_exempt_only_by_its_prize`**: `person_inputs: pool` planted on `the body` refuses `fight`.
- **`test_the_governing_score_is_the_mean_rounded_to_the_tenth`**: `governing_mean` equals the exact mean rounded to the
  nearest tenth over every one to three scores on 1 to 7 (`[2, 3]` → 2.5, not 3; `[2, 2, 3]` → 2.3; `[2, 3, 3]` → 2.7;
  `[5]` → 5.0), is a `float`, and refuses four scores, none and a negative.

## 5. Where the plan carries it

- **B05.24** (DESIGN-FIRST) — the rule of §0 and the row shape; one `ED-IN` row.
- **B05.25** (BUILD, behaviour mover) — the `governing:` / `brute:` / `opposed_attribute:` columns with §2's cells as
  interim, `person_inputs:` on the prize rows, the loader's closure, `sigma_leverage.governing_mean`,
  `pool.governing_score` (a float) and `rank`, `faculty` on their sum, with the `int` casts in `pool.py` removed (B05.25's
  WHERE); `vocation_attribute` deleted. B05.09, B05.10 and B05.16 carry
  a reconciliation line.
- **BA1.13** (CONTENT) — Jordan's corrections of the per-verb cells, through B05.25's loader.
- **B28.34** (DESIGN-FIRST) and **B28.35** (BUILD) — the persuasion terms of §2.6 and the self-plea's opposition (§2.7).

## 6. Questions that survive the ladder

**Q1. Is resisting arrest a contest of standing or of the body?** The row asks it itself (`contests_note`, `:171`:
*"[CONFIDENCE: medium -- whether resisting arrest is a contest of standing or of the body]"*). (A) Standing: the social
roll, as shipped; an arrest is submission to authority and cannot wound. (B) Body: a resisted arrest is `capture` (same
act by force, the yield terms, personal combat): arrests can wound and kill and draw on martial skill, and the row moves to
kind (c). The worlds differ in how often officers and the arrested die. The table's `arrest` row serves (A); by precedent
(step 4) (A) for the arrest, with a man who refuses free to answer by `fight`, his own act; Jordan's to confirm.

**Q2. Do acts on one's own state roll?** Jordan's brute ruling names *"a function of an office"*; this table extends
kind (a) to acts authorised by his own standing (`commit`, `forgive`, `give`, `challenge`) or completed by another's
decision (`covenant`), which the ruling's own list of authorisers ("a standing, a counterparty's own decision") reaches.
The SC lane's B28 makes five of them draws: `give` (B28.02, a drawn hand-over), `forgive` (B28.05, *"a drawn mark"*),
`challenge` (B28.06), `commit` (B28.08, *"its band is its strength"*), `covenant` (B28.09). (A) No roll: a pledge, a
pardon of a wrong, a gift are what the man decides, and B05.25's loader refuses their draws. (B) Drawn: how firmly a man
commits or forgives varies, and those rows become (b) with attributes (Spirit for a commitment, Grace for a forgiveness
`[ASSUMPTION]`). The worlds differ: under (A) a commitment is as strong as the chooser made it; under (B) the same choice
holds or breaks by a draw. Recommendation by ruling (step 1): (A), with B28's draws re-read by their lane; Jordan's to
confirm before B28 lands.

Decided by the ladder, not escalated: the office modifier as a level, not a die (§0, step 5); `determine` as (b) (step 4,
SC-03b); the skill rank added to the mean (ruling (1), marked); an unheld attribute at `pool_default` in the dice and at
the mid-point in the opposition's levels (ruling (3) for the dice; A-79 and U1 §4 for the levels: two roles, each read
once).

## 7. What was not checked

- `proposals/2026-11-05-verb-attribute-map.md` (and `_part2`, and the adjudication) is an earlier per-verb map against the
  same rulings; deliberately not read before the table was written, and not compared after. Its findings F1 to F27 should
  be diffed against §2 at BA1.13.
- The 14_VERBS_* lane proposals were not read row by row; where they set a verb's skill or roll differently, the lane's
  later text governs its row (U1 §5's rule, `:295`).
- Nothing was executed but the naming check; no hash claim was observed. B05.25's control claim (an unauthored realm reads
  `pool_default` and moves nothing) is the item's own gate to observe.
