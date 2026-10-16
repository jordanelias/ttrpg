# The flattened list, re-issued: the recommended primaries, what hangs off each, and the 46 demands mapped into them (from `2026-10-16-attribute-derivation.md` §1 and `_part3` §7)

## Status: PROPOSED (2026-10-16). An extract, for showing on its own. The evidence is the head's §1 and `_part2`; the principles, the selection and the coverage test are `_part3` §6–§7. The choice is Jordan's.

**Key.**

1. **Demand**: one of the 46 words for what an act or a subsystem asks of a person (the first pass
   called them *aptitudes*; that word has three other senses in the tree, head Words). Each is marked
   by **kind**, independent of any roster: CAPACITY 19, COMPUTED QUANTITY 14, PRACTICE 9, LIMIT 2,
   TEMPERAMENT 2.
2. **Primary**: a quantity selected to be carried as an attribute. Per Jordan (2026-10-16), *"ANY of
   these can be an attribute. ignore all prior rulings for this exercise"* and *"there are no derived
   scores when we don't even know our primaries"*: every demand, formula, ingredient and learned
   skill was a candidate, and a formula is called **derived** only relative to the chosen set.
3. **The selection principles** (`_part3` §6): a reader (P1, ID-13 as quality), independence (P2),
   absorption (P3), stable to carry (P4), monotone (P5), domain-general (P6), legible (P7), and
   **coverage**, the main test: the set must express every demand and every source formula.
4. Evidence counts each source statement once. *Formulas* are those the sources write (head §1.2),
   derived relative to this set by the formula the source already writes; *skills* are the learned
   skills that enter on the primary (head §1.3); *uses* are the sourced rolls of it alone (head §1.4);
   *statements* are the distinct statements of the demands grouped under it (named / overridden /
   inferred). Totals: 46 demands; 355 draw entries over 19 domains, 34 graded verbs and 16 subsystems;
   171 demand-statements (79 named, 12 overridden, 80 inferred).

## The recommended set: eleven primaries

**STR · AGI · END · FOC · ACU · WIL · ATT · CHA · BON · REC (Recall) · TS (Thread Sensitivity).**
Coverage: 34 of the 36 non-practice demands with a source ingredient and 36 of the 38 formulas with a
person ingredient are expressed; uncovered: `self-coherence` (F34) and `boldness` (F17).

| primary | formulas hanging off it | skills | uses | demands that hang off it | statements n / o / i | moves | cut test |
|---|---|---|---|---|---|---|---|
| **STR** Strength | 5: Balance F03 (half), Impact F07, Handling F08, Bind and wind F09, Durability F10 (a noise term) | 1 | 0 | strength | 1 / 0 / 2 | odds, cost, effect size | holds, narrowed to combat |
| **AGI** Agility | 5: Tempo F01, Reflex F02, Balance F03, Initiative F04, Counter F05 | 6 | 3 | quickness, reflexes, balance, dexterity | 3 / 0 / 9 | odds, effect size | holds |
| **END** Endurance | 4: Durability F10, Stamina reserve F11, Take a Breath F12, Dissolution Ob F35 | 2 | 4 | stamina, toughness, hardiness | 6 / 0 / 8 | cost | holds |
| **FOC** Focus | 5: Concentration F14, Disruption F15, Poise F16, Focus defence F20, Operations cap F31 | 3 (2 retired) | 0 | concentration | 3 / 1 / 5 | cost, eligibility, odds | holds, through formulas alone |
| **ACU** Acuity (Cognition) | 5: Initiative F04, Reading F06, Command F18 (with CHA), Impress Ob F27, Cover F28 | 13 | 15 | reasoning, observation, spatial-sense, land-sense, anticipation | 15 / 3 / 8 | odds, eligibility, resists another | holds, conditional on the Cognition alias |
| **WIL** Will (Spirit) | 8: F10, F11, F14 (minor terms), Resolve cap F29, Thread Fatigue F30, Thread pool F32, F35, Spark check F38 | 6 | 12 | will, steadfastness, sincerity, devotion, contact-endurance | 16 / 0 / 1 | odds, eligibility, cost | holds |
| **ATT** Attunement | 5: F02, F04, F05, F06 (minor terms), Appraise pool F25 | 15 | 9 | reading-people, empathy, discernment | 4 / 2 / 6 | odds, eligibility | holds |
| **CHA** Charisma | 5: Command F18, Strain modifier F21, Face F22, Composure F24, Appraise Ob F26 | 4 | 11 | presence, persuasiveness, judgment, leadership, situational-awareness, tactical-read | 7 / 3 / 17 | odds, eligibility | narrowed at T2 (Command runs on ACU alone; Face moves nothing), holds at T4 |
| **BON** Bonds | 1: Knot cap F36 | 0 | 3 | relational-depth | 3 / 0 / 0 | eligibility, odds | narrowed: the knot gate also needs Disposition |
| **REC** Recall | 5: Appraise pool F25, Effective Recall F37, Spark F38, Equip slots F39, Depth ceiling F40 | 10 (6 overridden) | 3 (2 overridden) | memory, inference, learning, breadth, practice-ceiling | 7 / 3 / 3 | odds, eligibility, the learning rate | **false today**: no code reads it |
| **TS** Thread Sensitivity | 2: Thread pool F32 (with WIL), Thread Pool Score F33 | 2 | 5 | thread-sensitivity | 9 / 0 / 1 | odds, eligibility (gates) | holds |

**Not primaries, and where the remaining demands go.**

| demands | why | where they sit |
|---|---|---|
| self-coherence | its ingredient, `resilience`, is a dark stub slot (gain 0) that canon defines as *"how resilient their spirit is"* (operations.py:144) | **uncovered**; the canon-suggested re-expression on Will is a new choice, Jordan's |
| boldness, patience | leans, not capacities (P5); `patience` has no source at all | temperament: `disp` carried beside the attributes, not among them |
| numeracy, verbal-fluency, precision, deception, planning, intimidation, quick-thinking, discipline | they grow by use within a domain (P6); every draw is inferred | practice, sitting on primaries through History and the learned skills |

## The two alternatives

| | primaries | coverage (uncovered demands / formulas) | trade-off |
|---|---|---|---|
| **smaller: eight** | STR · AGI · END · ACU · WIL · ATT · CHA · TS | 9 / 13 | fewer numbers, each broad; needs three rewrites, each against a source: Focus onto Will (against `derived_stats_v30.md:267`), Bonds onto Charisma or Attunement, Recall onto Acuity (against HIST:129) |
| **larger: thirteen** | the eleven + RES · TMP | 0 / 0 | every demand and formula has a home; RES has no live reader and canon defines it by Spirit; TMP is a lean, so *more* stops meaning *better*. Variant: Command carried as its own primary (`Officer.command` already accepts a value) |
| *today's nine, for comparison* | STR · AGI · END · FOC · ACU · WIL · ATT · CHA · BON | 8 / 9 | the thread family and the Recall family have no home |

## The 46 demands, mapped

Kind is the head's §1.5; the group is the recommended primary that expresses the demand.

| demand | kind | group | | demand | kind | group |
|---|---|---|---|---|---|---|
| reasoning | CAPACITY | ACU | | strength | CAPACITY | STR |
| thread-sensitivity | CAPACITY | TS | | boldness | TEMPERAMENT | temperament |
| steadfastness | CAPACITY | WIL | | contact-endurance | COMPUTED QUANTITY | WIL |
| will | CAPACITY | WIL | | empathy | CAPACITY | ATT |
| presence | CAPACITY | CHA | | hardiness | CAPACITY | END |
| concentration | COMPUTED QUANTITY | FOC | | judgment | CAPACITY | CHA |
| memory | CAPACITY | REC | | land-sense | PRACTICE | ACU |
| reading-people | CAPACITY | ATT | | learning | COMPUTED QUANTITY | REC |
| relational-depth | CAPACITY | BON | | practice-ceiling | LIMIT | REC |
| self-coherence | COMPUTED QUANTITY | uncovered | | quickness | COMPUTED QUANTITY | AGI |
| stamina | COMPUTED QUANTITY | END | | reflexes | COMPUTED QUANTITY | AGI |
| breadth | LIMIT | REC | | sincerity | CAPACITY | WIL |
| devotion | COMPUTED QUANTITY | WIL | | dexterity | CAPACITY | AGI |
| observation | CAPACITY | ACU | | discernment | CAPACITY | ATT |
| persuasiveness | CAPACITY | CHA | | inference | CAPACITY | REC |
| spatial-sense | CAPACITY | ACU | | leadership | COMPUTED QUANTITY | CHA |
| toughness | COMPUTED QUANTITY | END | | situational-awareness | COMPUTED QUANTITY | CHA |
| anticipation | COMPUTED QUANTITY | ACU | | tactical-read | COMPUTED QUANTITY | CHA |
| balance | COMPUTED QUANTITY | AGI | | patience | TEMPERAMENT | temperament |
| numeracy, verbal-fluency, precision, deception, planning, intimidation, quick-thinking, discipline | PRACTICE | practice | | | | |
