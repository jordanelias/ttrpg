# Attribute derivation — part 3: §6 the principles, §7 pool, selection and coverage, §8 the one grouping, §9 meta-rule, §10 NERS, §11 limits, §12–§13 the critic reconciliations

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. It recommends a set of primaries and two alternatives; the choice is Jordan's.
## Parts, in reading order: [head](2026-10-16-attribute-derivation.md) (words, §1 the evidence, the command) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§2–§5, the interrogation) · **this file** (§6–§13).

**The frame for this part (Jordan, 2026-10-16).** *"ANY of these can be an attribute. ignore all
prior rulings for this exercise"*, and *"there are no derived scores when we don't even know our
primaries."* So every demand, every source formula, every ingredient and every learned skill is a
candidate; no ruling excludes one (the head's *What the tree currently says* paragraph records them
as history); the number of attributes is open; and nothing is called *derived* until §7.6, after the
primaries are chosen.

Every count is the head's command's output (head §1.7). The totals: 46 demands; 355 draw entries over
19 domains, 34 graded verbs and 16 subsystems; 171 demand-statements (79 named, 12 overridden, 80
inferred); the evidence tables hold 14 ingredients, 41 source formulas, 58 learned-skill rows and 64
sourced uses.

---

## 6. THE SELECTION PRINCIPLES (derived from the evidence, stated before they are applied)

Each principle is a test a candidate passes or fails, with the evidence that suggested it. **ID-13 is
used as a quality test (P1), never as a ruling.**

| P | principle | the test | evidence it comes from |
|---|---|---|---|
| **P1** | **READ** | something reads it: **strong** if T1/T2 code reads a per-person value; **weak** if only designs (T4) do; **fails** if nothing does | an attribute nothing reads moves no outcome (ID-13, as quality); head §1.6's *best tier* column shows the spread, from BODY at T1 to Recall at T4 |
| **P2** | **INDEPENDENT** | two persons can differ in it without differing in another primary. A candidate the sources compute wholly from two or more other candidates is not independent of them; choose the compound or its ingredients, not both | 14 of the 46 demands are computed by the sources from other quantities (head §1.5); the one place a source argues independence directly: *"Spirit 6 / Focus 2 … endurance without skill. Spirit 2 / Focus 6 … skill without staying power"* (`derived_stats_v30.md:267`) |
| **P3** | **ABSORBS** | between a candidate and another that carries a superset of its demands, formulas, skills and uses (each source statement once), prefer the one that carries more | head §1.6: Agility carries Tempo, Reflex, Balance, initiative and the counter, while Tempo carries one demand |
| **P4** | **STABLE TO CARRY** | carried between scenes: not a resource that drains in play, not a relational state, not kit. A resource's **maximum** may be stable while the resource drains | *"Stats are what your faction/character CAN do. Derived values are what they HAVE right now"* (`derived_stats_v30.md:14`); the Combatant keeps `stamina` (current) beside `stamina_max` (combatant.py:45-47, :150-151) |
| **P5** | **MONOTONE** | more is better wherever it is read: a capacity, not a lean | `disp` is neutral at 4 and read as `(disp − 4)/3`, aggressive or cautious (combatant.py:99; combat_systems.py:180-182) |
| **P6** | **DOMAIN-GENERAL** | it applies across domains; what grows by use within one domain is practice | the 2026-08-15 role table puts practice in the Pool row per role and *"Faculties — modulate, don't select"* across all roles (AUG:168-176); Histories skills spark per History (HIST:41) |
| **P7** | **LEGIBLE** | a plain word a player can predict outcomes from | NERS *Elegant*: *"allows the player to intuit complex outcomes from simple choices"* (`CLAUDE.md` §0.06); the registry's own *"[ASSUMPTION]"* on folding Cognition into Acuity (`descriptor_registry.yaml:42`) is a legibility cost |
| **COVERAGE** | **the main test of a set** | the set must express every CAPACITY, COMPUTED QUANTITY and LIMIT demand and every source formula through the ingredients the sources use; anything else is **UNCOVERED**, or needs a re-expression that is stated as a new choice | head §1.5's ingredients column and §1.2's formulas; the command checks each set |

**How they are applied.** P4, P5 and P6 sort the pool by kind (resources, leans, practice); P1
grades what is left; P2 and P3 choose between a compound and its ingredients; coverage decides how
many primaries a set needs. ⚠ **Coverage is measured against the ingredients the sources use today.**
That favours a set built from today's ingredient vocabulary. A set built of other quantities (for
example, Concentration in place of Focus) can express the same demands only by rewriting formulas;
§7.5 states each such rewrite as a new choice rather than counting it as covered.

---

## 7. POOL, SELECTION AND COVERAGE

### 7.1 The candidate pool (step 2)

**Every item is a candidate:** the 46 demands (19 CAPACITY, 14 COMPUTED QUANTITY, 9 PRACTICE, 2 LIMIT,
2 TEMPERAMENT); the 41 source formulas (head §1.2) as quantities in their own right; the 14
ingredients the formulas and rolls name (head §1.1); the 58 learned-skill rows (head §1.3); and what
else a person carries: KIT, Disposition, the Coherence and Truth tracks, Inspiration.

### 7.2 Screening (step 3, by principle)

| candidates | P1 read | P2 independent | P3 absorbs | P4 stable | P5 monotone | P6 general | P7 legible | verdict |
|---|---|---|---|---|---|---|---|---|
| STR, AGI, END, ACU, WIL, ATT, CHA | strong (T2; END T1 through BODY) | yes: no source computes any of them | each carries 3–11 demands and 4–8 formulas | yes | yes | yes | yes (ACU's *"Cognition"* alias is a cost) | **select** |
| FOC | strong (T2) | yes (derived_stats_v30:267) | 1 demand, 5 formulas, no sourced use | yes | yes | yes | yes | **select** (P3 is its weakest) |
| BON | strong (T2: the knot gate and cap) | yes | 1 demand, 1 formula, 3 uses | yes | yes | yes | yes | **select** (narrowest that passes) |
| TS | strong (T2: the thread pool, the knot gate) | yes | 1 demand with 9 named statements, 2 formulas, 2 skills, 5 uses, in 6 subsystems | yes, and it grows by exposure (HIST:127, :324; FW:254) | yes | yes: the thread reaches fieldwork, the world, belief, perception gates and progression | yes | **select** |
| REC | **weak** (designs only; no code field) | yes | 5 demands, 5 formulas, 10 skills, 3 uses | yes | yes | yes | yes | **select, on coverage** (§7.3) |
| RES | weak (a dark stub, gain 0) | **no**: canon defines it as *"how resilient their spirit is"* (operations.py:144) | 1 demand, 1 formula, 2 inferred uses | yes | yes | yes | low (a coined term) | not selected; larger set only |
| TMP | strong (T2) | yes | 1 demand (`patience` adds an unsourced one) | yes | **no**: a lean | yes | yes | not selected as an attribute; larger set only |
| BODY | strong (**T1**) | yes | 2 demands through F13 | **no**: a condition that changes in play | yes | yes | yes | a state the loop carries, never a missing primary |
| the 19 CAPACITY demands as primaries in place of their ingredient (`observation`, `spatial-sense` … ) | as their ingredient | each is a use of one ingredient | **loses** to its ingredient: `observation` carries itself; Acuity carries 11 demands | yes | yes | yes | yes | not selected: the ingredient absorbs them. Where a demand IS the ingredient (`strength`, `will`, `thread-sensitivity`, `memory` for Recall, `relational-depth` for Bonds) it is selected under the ingredient's name |
| Command (F18) | strong (T2) | **no**: the sources compute it from CHA and ACU, which carry 6 and 11 demands | 3 demands | yes | yes | no: command only | **yes**: players of mass battle think in Command (MB:306) | not selected; a variant of the larger set (§7.5) |
| Concentration (F14), the stamina reserve (F11), Durability (F10), Reading (F06), Reflex (F02), Balance (F03), Tempo (F01) | strong (T2/T1) | no: each is computed from one or two candidates that carry more | 1 demand each | a maximum is stable; the tracker drains | yes | yes | yes | not selected: each ingredient absorbs it (Focus also carries F15, F16, F20, F31, which Concentration does not) |
| Resolve cap (F29), Thread Fatigue threshold (F30), operations cap (F31), knot cap (F36), equip slots (F39), depth ceiling (F40), effective Recall (F37), spark (F38) | T2–T4 | no: each is one ingredient times a constant | 1 demand each | yes | yes | yes | yes | not selected: the ingredient absorbs it |
| Face (F22), Composure (F24), kernel trackers (F23), obstacles (F26, F27, F35, F41), pools (F19, F25, F32, F33), Cover (F28), Coherence resistance (F34), Take a Breath (F12), strain modifier (F21), handling (F08), Impact (F07), bind (F09), counter (F05), initiative (F04), disruption (F15), poise (F16), lean (F17), season `end` (F13) | various | no: each is computed from candidates | ≤ 2 demands each | several are resources or obstacles | — | — | — | not selected |
| learned skills: History, `capability`, `faculty`, Combatant skills, techniques, tradition, tactic cards, the Histories skills, Mentor dice | strong to none | — | each enters one or a few pools | yes | yes | **no**: each grows by use, or is held, within a domain | yes | not selected: practice, sitting on primaries (§7.6) |
| KIT; Disposition; Coherence, Truth, Inspiration | — | — | — | **no**: held kit, a relational state, tracks and a resource | — | — | — | not selected |

### 7.3 The candidate sets and the coverage test (the main test)

| K | set | primaries |
|---|---|---|
| K01 | recommended | `STR` `AGI` `END` `FOC` `ACU` `WIL` `ATT` `CHA` `BON` `REC` `TS` |
| K02 | smaller | `STR` `AGI` `END` `ACU` `WIL` `ATT` `CHA` `TS` |
| K03 | larger | `STR` `AGI` `END` `FOC` `ACU` `WIL` `ATT` `CHA` `BON` `REC` `TS` `RES` `TMP` |
| K04 | today's nine (the baseline, for comparison) | `STR` `AGI` `END` `FOC` `ACU` `WIL` `ATT` `CHA` `BON` |

**The coverage, as the command prints it** (BODY counts as a state every person has; PRACTICE demands
sit on primaries and are not counted as uncovered):

```
K01 recommended 11 primaries | demands {'UNCOVERED': 2, 'expressed': 34, 'practice': 9, 'unsourced temperament': 1} | formulas {'UNCOVERED': 2, 'expressed': 36, 'no person ingredient': 3}
   uncovered: boldness (needs TMP); self-coherence (needs RES); F17 (needs TMP); F34 (needs RES)
K02 smaller 8 primaries | demands {'UNCOVERED': 9, 'expressed': 27, 'practice': 9, 'unsourced temperament': 1} | formulas {'UNCOVERED': 13, 'expressed': 25, 'no person ingredient': 3}
   uncovered: boldness (needs TMP); breadth (needs REC); concentration (needs FOC); inference (needs REC); learning (needs REC); memory (needs REC); practice-ceiling (needs REC); relational-depth (needs BON); self-coherence (needs RES); F14 (needs FOC); F15 (needs FOC); F16 (needs FOC); F17 (needs TMP); F20 (needs FOC); F25 (needs REC); F31 (needs FOC); F34 (needs RES); F36 (needs BON); F37 (needs REC); F38 (needs REC); F39 (needs REC); F40 (needs REC)
K03 larger 13 primaries | demands {'expressed': 36, 'practice': 9, 'unsourced temperament': 1} | formulas {'expressed': 38, 'no person ingredient': 3}
   uncovered: none
K04 today's nine (the baseline, for comparison) 9 primaries | demands {'UNCOVERED': 8, 'expressed': 28, 'practice': 9, 'unsourced temperament': 1} | formulas {'UNCOVERED': 9, 'expressed': 29, 'no person ingredient': 3}
   uncovered: boldness (needs TMP); breadth (needs REC); inference (needs REC); learning (needs REC); memory (needs REC); practice-ceiling (needs REC); self-coherence (needs RES); thread-sensitivity (needs TS); F17 (needs TMP); F25 (needs REC); F32 (needs TS); F33 (needs TS); F34 (needs RES); F37 (needs REC); F38 (needs REC); F39 (needs REC); F40 (needs REC)
```

**Reading it.**

- **Today's nine (K04) leave 8 demands and 9 source formulas uncovered**: thread sensitivity and its two
  formulas; the whole Recall family (memory, inference, learning, breadth, the practice ceiling, and
  five formulas); self-coherence; boldness.
- **The recommended eleven (K01) leave 2 demands and 2 formulas uncovered**: `self-coherence` and its
  formula F34 (the dark resilience slot), and `boldness` and F17 (the temperament lean). Both are
  answered without a new primary in §7.6.
- **The smaller eight (K02) leave 9 demands and 13 formulas uncovered**: everything the nine leave
  except the thread family, plus Focus's and Bonds's demands and formulas.
- **The larger thirteen (K03) leave nothing uncovered.**

### 7.4 THE RECOMMENDATION: eleven primaries

**STR · AGI · END · FOC · ACU · WIL · ATT · CHA · BON · REC (Recall) · TS (Thread Sensitivity).**

Per primary: what it absorbs (the formulas, learned skills and demands that hang off it in head
§1.2–§1.5), the evidence (each source statement once), what it moves, what reads it, and the cut test
(propose cutting it and name what dies; an N-line whose producer moves no outcome is false).

| primary | absorbs (formulas; demands) | evidence: formulas / skills / uses / demand statements named-overridden-inferred | moves | readers | cut test |
|---|---|---|---|---|---|
| **STR** Strength | F03, F07–F10; `strength` | 5 / 1 / 0 / 1-0-2 | odds, cost, effect size (Impact, handling, bind, half of Balance, a Health noise term) | `core.strike_impact`; `combat_systems.handling_penalty`, bind and wind σ, `balance_eff` (T2) | Impact, handling and the bind lose their person term; Balance becomes Agility alone. **Holds, narrowed to combat**; no use outside it |
| **AGI** Agility | F01–F05; `quickness`, `reflexes`, `balance`, `dexterity` | 5 / 6 / 3 / 3-0-9 | odds (tempo, reflex, initiative, counter), effect size (inferred hand work) | `combat_systems.weapon_tempo`, `reflex`, `init_emphasis_sigma`, `counter_success_prob` (T2); three T4 world rolls | combat tempo, reflex and initiative lose their person term; three world hazards lose their roll. **Holds** |
| **END** Endurance | F10–F12, F35; `stamina`, `toughness`, `hardiness` | 4 / 2 / 4 / 6-0-8 | cost (wounds, fatigue, exposure), resists another | `combatant.health_full`, `stamina_max` (T1 through BODY); fieldwork and travel (T4) | Health, Max Wounds and the stamina reserve lose their person term; travel and exploration checks lose their roll. **Holds** |
| **FOC** Focus | F14–F16, F20, F31; `concentration` | 5 / 3 (2 retired, 1 inferred) / 0 / 3-1-5 | cost and eligibility (the tracker, the operations cap), odds (consistency) | `combatant.derive_stats` (`conc_max`), `disrupt_resist_p`, `poise_regen` (T2) | the Concentration tracker becomes Spirit alone, and disruption, poise and the operations cap lose their input. **Holds, through formulas alone**; no sourced use |
| **ACU** Acuity | F04, F06, F18 (with CHA), F27, F28; `reasoning`, `observation`, `spatial-sense`, `land-sense`, `anticipation` | 5 / 13 / 15 / 15-3-8 | odds (36 of 53 draws), eligibility (gates), resists another | `reading` (2:1), `derive_command` (secondary) (T2); 11 named T4 uses | Reading and Command lose a term; 15 sourced uses lose their roll. **Holds**, conditional on folding Cognition into Acuity |
| **WIL** Will (Spirit) | F10, F11, F14 (minor terms), F29, F30, F32, F35, F38; `will`, `steadfastness`, `sincerity`, `devotion`, `contact-endurance` | 8 / 6 / 12 / 16-0-1 | odds (the thread pool, the knot roll), eligibility (fatigue threshold, Inspiration cap), cost | `operations._actor_pool`, `knots` formation roll (T2) | the thread pool and the knot roll lose their main term; five belief-under-shock checks lose their roll. **Holds** |
| **ATT** Attunement | F02, F04–F06 (minor terms), F25; `reading-people`, `empathy`, `discernment` | 5 / 15 / 9 / 4-2-6 | odds, eligibility (the Lattice gate), resists another | `reflex`, `reading` (minor terms, T2); 7 named T4 uses | Reflex and Reading lose a minor term; reading people, the Lattice gate and 10 named skills lose their input. **Holds** |
| **CHA** Charisma | F18 (with ACU), F21, F22, F24, F26; `presence`, `persuasiveness`, `judgment`, `leadership`, `situational-awareness`, `tactical-read` | 5 / 4 / 11 / 7-3-17 | odds (34 of 48 draws), eligibility (Command's reform gate) | `derive_command` (primary, 2:1), Face (outcome-inert) (T2); 8 named T4 uses | at T2, Command still runs on Acuity alone and Face moves nothing; at T4, eight social and governance rolls lose their input. **Narrowed at T2, holds at T4** |
| **BON** Bonds | F36; `relational-depth` | 1 / 0 / 3 / 3-0-0 | eligibility (the knot gate and cap), odds (Connect) | `knots` gate and cap (T2) | the knot loses its ≥ 5 gate and its cap, but still gates on Disposition (knots.py:189-193); Connect and Anchoring lose their roll. **Narrowed** |
| **REC** Recall | F25, F37–F40; `memory`, `inference`, `learning`, `breadth`, `practice-ceiling` | 5 / 10 (4 named, 6 overridden) / 3 (1 named, 2 overridden) / 7-3-3 | odds (research, appraisal), eligibility (equip slots, depth ceiling), the learning rate | **no code reader**; designs: FW:95, :306; SCV:155; threadwork_v30:688; HIST:34-43, :517-522 | nothing at T1–T3. **A false N-line today**: it becomes live only when a progression or inquiry resolver reads it |
| **TS** Thread Sensitivity | F32 (with WIL), F33; `thread-sensitivity` | 2 / 2 / 5 / 9-0-1 | odds (the thread pool's TPS), eligibility (knot, depth and visibility gates) | `operations._actor_pool` (`ts // 10`), the knot gate (T2); a T3 gate (K-3) | the thread pool loses TPS; the knot gate and every depth and visibility gate lose their input. **Holds** |

**Why eleven, not nine.** On the coverage test today's nine leave the thread family and the Recall
family uncovered (§7.3). TS passes every principle with strong readers. Recall passes every principle
except P1, where it is weak; it is selected **on coverage**: without it five demands and five
formulas need a new home, and the only candidate home, Acuity, contradicts the source that separates
them (*"Knowledge as recognition, not intellect"*, HIST:129).

**Contrary sources on Recall, stated in full.** *"It is evidence for D2, not a candidate for it"*
(`10_verbs_and_attributes.md:152-156`); and the 2026-08-15 proposal calls Recall's *"triple-gate
(breadth + depth + learning rate)"* *"a mandatory tax stat"* and rules *"capacities govern breadth,
never depth"* (AUG:202-205). The recommendation carries that triple gate (F38, F39, F40). The first
is a judgement about the D2 slot, which this exercise sets aside; the second is a design objection
that stands: if Recall is selected, the depth ceiling (F40) is the formula to reconsider first.

**Confidence.** Medium that WIL, ACU, ATT and END are each needed and distinct; medium for AGI, STR and
FOC (each needed, almost all in the bout; FOC and STR have no sourced use); medium for TS; low to
medium for CHA (T2 only through a 2:1 weighting and an inert view) and BON (one formula); **low for
REC** (no reader in code).

### 7.5 Two alternatives, for comparison

| | **smaller (K02): eight** | **larger (K03): thirteen** |
|---|---|---|
| primaries | STR · AGI · END · ACU · WIL · ATT · CHA · TS | the recommended eleven + RES · TMP |
| changes from the recommendation | drops FOC, BON and REC | adds resilience and temperament |
| coverage | 9 demands and 13 formulas uncovered (§7.3) | none uncovered |
| the new choices it needs | **FOC → WIL**: Concentration on Spirit alone and the operations cap on Spirit, which erases the one distinction a source argues for (`derived_stats_v30.md:267`); **BON → CHA or ATT**: Connect and Anchoring re-rolled, the knot gate left on Disposition, which it already needs; **REC → ACU**: research, reconstruct and learning on Acuity, against HIST:129 | none for coverage; it carries a slot (RES) that canon defines by Spirit, so it keeps a second ladder for one quantity |
| what it buys | fewer numbers, each broad (every primary carries at least two formulas or five uses) | every demand and formula has a home without rewriting a formula |
| what it costs | three rewrites, each against a stated source; FOC's and BON's T2 readers lose their input | RES has no live reader (gain 0) and fails P2; TMP is a lean (fails P5), so *more* stops meaning *better* on the sheet |
| a variant | — | **Command carried as its own primary**, not computed from CHA and ACU: the code already accepts a given value (`Officer.command`, units.py:2700-2722). Coverage is unchanged; it buys a commander who leads without charm or tactics, and costs a second ladder against CHA and ACU |

### 7.6 Relative to the recommended set: what each remaining item is (step 4, only now)

- **Derived (expressed by a formula over the eleven).** Of the 41 source formulas, 36 use only the
  eleven and are derived relative to K01, **by the formula the source already writes** (head §1.2):
  F01–F16, F18, F20–F22, F24–F33, F35–F40 (F13 reads BODY, a state). Of the demands, the 13
  COMPUTED QUANTITY demands other than `self-coherence` are expressed by those formulas, and the 2
  LIMIT demands by F39 and F40; with the 19 CAPACITY demands that makes the 34 the command reports.
- **Uses of a primary.** The 19 CAPACITY demands are each a use of one primary (head §1.5,
  *ingredients*); `judgment` and `steadfastness` are each a use of one of two (S-defect 4 for the
  second).
- **Learned skills, sitting on primaries.** The 9 PRACTICE demands and the 58 learned-skill rows. Of
  those rows, 44 name the ingredient they enter on, and every such ingredient is in the eleven except
  in L33 and L32, whose rules are retired.
- **Resources and tracks.** The current levels of the stamina reserve, Health, the Concentration
  tracker, Face, Composure, the kernel trackers, Thread Fatigue, Inspiration, Coherence and Truth.
  Their maxima are the formulas above.
- **No person ingredient.** F19 (the resolution pool reads History only), F23 (the kernel trackers),
  F41 (the Negotiate Ob names no ingredient).
- **UNCOVERED, and the answer without a new primary.** `self-coherence` and F34: re-express
  resilience as a function of Spirit, which is canon's own definition (*"how resilient their spirit
  is"*, operations.py:144) — a new choice, and Jordan's. `boldness` and F17: carry `disp` as a
  **temperament field beside the attributes**, not among them (P5); or drop the lean. `patience` has
  no source at all.

### 7.7 What the critic's "the homeless draws reduce to the nine" does and does not show

The second critic found that the first pass's twelve "homeless" named draws reduce to the nine
through formulas (Hold Court rolls Charisma or Cognition; anticipation is Reading; situational
awareness is Command). **That shows the current nine can express those named demands. It does not
show the nine are right**: the same coverage test, run on the nine as a set (K04), leaves the thread
family and the Recall family uncovered, and run on other sets gives the comparison in §7.3.

---

## 8. THE ONE GROUPING (relative to the recommended set)

### 8.1 The rule

**There is one grouping: each demand goes to the recommended primary that expresses it** (head §1.5,
*group*). It replaces the first pass's sixteen clusters, and the word study's twelve classes and ten
families, which assigned the same rows three different ways.

- A **CAPACITY** demand goes to the primary it is a use of (`observation` → ACU).
- A **COMPUTED QUANTITY** or **LIMIT** demand goes to the primary with the largest weight in the
  source's formula: `concentration` → FOC (3·FOC + 2·WIL); `stamina` → END; `reflexes` → AGI (2 : 1,
  `config.py:122`); `anticipation` → ACU (2·Cog + Att); the three uses of Command → CHA (2·Cha + Cog).
- **Ties** go to the ingredient the source writes first: `balance` → AGI (½Agi + ½Str); `judgment` →
  CHA (*"Charisma/Cognition"*). Two placements are this proposal's reading, not a formula: `judgment`'s
  tie, and `patience` as a lean.
- A **PRACTICE** demand goes to the primary its skill enters on (`land-sense` → ACU), else to
  *practice*. A **TEMPERAMENT** demand goes to *temperament*. A demand the set does not express goes
  to *uncovered*.

| group | demands | PRA domains | verbs [resolvers] | subsystems | draw entries | statements named / overridden / inferred | roles over all draws |
|---|---|---|---|---|---|---|---|
| STR | strength | 3 | 3 [2] | 2 | 8 | 1 / 0 / 2 | effect size 8, odds 4, difficulty/cost 4 |
| AGI | balance, dexterity, quickness, reflexes | 5 | 6 [5] | 4 | 25 | 3 / 0 / 9 | odds 18, effect size 7 |
| END | hardiness, stamina, toughness | 4 | 6 [5] | 7 | 27 | 6 / 0 / 8 | difficulty/cost 18, odds 4, effect size 4, resists another 1 |
| FOC | concentration | 8 | 12 [5] | 5 | 26 | 3 / 1 / 5 | difficulty/cost 9, eligibility 9, odds 7, effect size 1 |
| ACU | anticipation, land-sense, observation, reasoning, spatial-sense | 13 | 11 [10] | 9 | 53 | 15 / 3 / 8 | odds 36, eligibility 6, resists another 6, effect size 5 |
| WIL | contact-endurance, devotion, sincerity, steadfastness, will | 3 | 11 [5] | 7 | 39 | 16 / 0 / 1 | odds 22, eligibility 10, difficulty/cost 7 |
| ATT | discernment, empathy, reading-people | 6 | 6 [6] | 8 | 24 | 4 / 2 / 6 | odds 17, eligibility 3, resists another 3, effect size 1 |
| CHA | judgment, leadership, persuasiveness, presence, situational-awareness, tactical-read | 7 | 9 [9] | 9 | 48 | 7 / 3 / 17 | odds 34, eligibility 10, resists another 3, effect size 1 |
| BON | relational-depth | 2 | 2 [2] | 2 | 6 | 3 / 0 / 0 | eligibility 3, odds 3 |
| REC | breadth, inference, learning, memory, practice-ceiling | 6 | 4 [4] | 6 | 24 | 7 / 3 / 3 | odds 18, eligibility 5, difficulty/cost 1 |
| TS | thread-sensitivity | 4 | 10 [4] | 6 | 23 | 9 / 0 / 1 | odds 12, eligibility 9, difficulty/cost 1, effect size 1 |
| uncovered | self-coherence | 1 | 6 [1] | 3 | 10 | 3 / 0 / 0 | difficulty/cost 10 |
| temperament | boldness, patience | 6 | 3 [2] | 5 | 14 | 1 / 0 / 5 | odds 11, effect size 3 |
| practice | deception, discipline, intimidation, numeracy, planning, precision, quick-thinking, verbal-fluency | 7 | 9 [9] | 6 | 28 | 0 / 0 / 15 | odds 19, effect size 9 |

Statements are the distinct keys of the group's demands at best basis. **Roles carry no magnitude**:
STR's odds and cost draws are the bind term and a labelled noise term in Health.

### 8.2 Cross-tabs

**Legend.** ● at least one NAMED draw. ◐ overridden draws only. ○ inferred draws only. Blank: no draw.

**Group × practice domain.**

| group \ P | P01 | P02 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P17 | P18 | P19 | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STR |   |   | ● |   |   |   |   |   |   |   | ○ |   |   |   |   |   | ○ |   |   | 3 |
| AGI | ○ |   | ● |   |   |   |   |   |   |   | ○ | ○ |   |   |   |   |   | ○ |   | 5 |
| END |   |   | ● |   |   |   |   |   |   |   |   | ○ |   |   | ● |   | ○ |   |   | 4 |
| FOC | ○ | ◐ | ● |   | ● |   | ○ |   |   | ○ |   | ○ |   |   |   |   |   | ○ |   | 8 |
| ACU |   | ◐ | ● | ● |   |   | ● | ● | ● |   | ○ | ○ | ○ |   | ● | ● | ● |   | ● | 13 |
| WIL |   |   |   |   | ● | ● |   |   |   |   |   |   |   |   |   | ● |   |   |   | 3 |
| ATT |   | ◐ |   |   |   |   | ● |   | ● | ● |   | ○ |   |   |   | ● |   |   |   | 6 |
| CHA |   | ◐ |   | ○ |   |   | ◐ | ● | ● | ○ |   |   |   |   |   | ● |   |   |   | 7 |
| BON |   |   |   |   |   | ● |   |   |   |   |   |   |   |   |   | ● |   |   |   | 2 |
| REC |   | ◐ |   |   |   |   | ◐ |   |   | ○ |   | ○ | ● | ○ |   |   |   |   |   | 6 |
| TS |   |   |   |   | ● | ● | ● |   |   |   |   |   |   |   | ● |   |   |   |   | 4 |
| uncovered |   |   |   |   | ● |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 1 |
| temperament |   |   | ● |   |   |   | ○ |   | ○ |   | ○ |   | ○ |   |   |   | ○ |   |   | 6 |
| practice | ○ | ○ |   |   |   |   |   | ○ | ○ | ○ | ○ |   |   |   |   |   |   |   | ○ | 7 |

**Group × subsystem.**

| group \ S | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 | S10 | S11 | S12 | S13 | S14 | S15 | S16 | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STR | ● |   |   |   |   |   |   | ○ |   |   |   |   |   |   |   |   | 2 |
| AGI | ● |   |   |   |   |   |   | ○ | ○ |   |   | ○ |   |   |   |   | 4 |
| END | ● | ○ |   | ● | ● |   |   | ○ | ● |   |   | ○ |   |   |   |   | 7 |
| FOC | ● |   | ◐ | ○ | ● |   |   |   |   |   |   | ○ |   |   |   |   | 5 |
| ACU | ● | ● | ◐ | ● |   | ● |   |   | ● |   | ● | ○ |   |   | ● |   | 9 |
| WIL |   |   |   | ● | ● |   | ● |   | ● | ● |   |   |   | ● |   | ● | 7 |
| ATT |   |   | ◐ | ● |   | ● | ○ | ○ |   | ○ |   | ○ | ○ |   |   |   | 8 |
| CHA | ○ | ● | ◐ | ● |   | ● | ○ |   |   | ○ | ● |   | ○ |   |   |   | 9 |
| BON |   |   |   | ● | ● |   |   |   |   |   |   |   |   |   |   |   | 2 |
| REC |   |   | ◐ | ◐ | ● |   |   |   |   |   |   | ○ | ● |   |   | ● | 6 |
| TS |   |   |   | ● | ● |   |   |   | ● |   |   |   |   | ○ | ● | ● | 6 |
| uncovered | ● |   |   |   | ● |   |   |   | ● |   |   |   |   |   |   |   | 3 |
| temperament | ● |   |   | ○ |   | ○ |   | ○ |   | ○ |   |   |   |   |   |   | 5 |
| practice |   |   | ○ | ○ |   | ○ |   | ○ |   |   | ○ |   |   |   |   | ○ | 6 |

S14's ACU cell is blank because the Miraculous Event's Cognition check is coded to `steadfastness`,
in the WIL group; the Cognition reading of that check is head U19 and S-defect 4.

### 8.3 Driven by acts, by learned skills, or by sustained play

The first pass's rule, on distinct verb resolvers: **sustained play** if subsystems exceed both other
counts; **learned skills** if domains exceed both by at least 2; **acts** if resolvers exceed both;
otherwise **even**.

| driven by | groups (PRA / verb resolvers / subsystems) | reading |
|---|---|---|
| **learned skills** | ACU (13 / 10 / 9), FOC (8 / 5 / 5) | drawn under many practices. ⚠ FOC's lead is mostly inference: 6 of its 8 domains reach it by inferred draws only |
| **sustained play** | END (4 / 5 / 7), WIL (3 / 5 / 7), ATT (6 / 6 / 8), TS (4 / 4 / 6), uncovered (1 / 1 / 3) | what the subsystems call for that few single acts carry: the march, the thread, belief under shock, the reading of a room |
| **acts** | practice (7 / 9 / 6) | single acts, every draw inferred |
| even | STR (3 / 2 / 2), AGI (5 / 5 / 4), CHA (7 / 9 / 9), BON (2 / 2 / 2), REC (6 / 4 / 6), temperament (6 / 2 / 5) | — |

---

## 9. WHAT IT ADDS AND CUTS (the meta-rule, relative to today's registry)

| | object | removes or adds something that exists? |
|---|---|---|
| **adds** | two primaries: Recall and Thread Sensitivity | Recall exists only in designs (no code field); TS exists as a practitioner field (`ts`, registry :64) and would become an attribute |
| **keeps** | the registry's nine | no change |
| **re-expresses** | resilience as a function of Spirit (canon's definition), if it is ever lit | changes what fills an existing stub slot (operations.py:142-147); removes no attribute |
| **sets beside** | temperament (`disp`) as a field beside the attributes, not among them | the field exists in combat (combatant.py:99) |
| **leaves** | every formula, use, limit, lean, resource and learned skill off the attribute list, each expressed by or sitting on a primary (§7.6) | no |
| **asks** | if Recall is selected: should a writer's increment (`train`) read an attribute? Today's V-2 says no (`10_verbs_and_attributes.md:198`) — history, recorded as a question | no |

**Net effect on the roster: two added, none removed.** This proposal edits no code, no registry and
no ledger, allocates no ID, and touches five files under `proposals/`.

---

## 10. NERS, IN BRIEF (`skills/ners/SKILL.md`)

`[SELF-AUTHORED — bias risk]`. Grade: **paper**. No outcome was measured.

**N** is the cut-test column of §7.4: nine of the eleven hold (STR and AGI narrowed to combat, CHA
narrowed at T2, BON narrowed by Disposition); **REC is a false N-line today**; TS holds. Of the
larger set's additions, RES is false today (F34 is the identity at gain 0) and TMP holds only in
combat, as a lean.

**S: six "two ladders for one quantity" defects** (`CLAUDE.md` §0.06, *"calculations consistent in
methodology"*). None is repaired here; each is named for whoever writes the formulas.

1. **Steadiness under strain.** Focus carries it in the combat tracker (combatant.py:147) and the
   contest's Focus defence (SCV:199); Charisma carries it as *Composure* (Charisma × 3,
   derived_stats_v30:554; Cha + 6, FW:640), retired as the contest tracker only (SCV:242), still
   charged by threadwork (threadwork_v30:177), and named in the monster-hex *"Composure check"*
   (valoria_ui_ux_v4_1:916).
2. **Sincerity.** The registry aliases it to Bonds (`descriptor_registry.yaml:48`); the fieldwork
   Sincerity Check rolls Spirit (FW:430), and ED-503 assigns the Sincerity Gate to Spirit (FW:822).
3. **Initiative.** The stub's initiative emphasis reads Agility, Reading and History
   (`combat_systems.py:1416-1421`); the designs roll initiative by Attunement (FW:106;
   `combat_c4_draft_v0.md:127`, not opened); Combat Reflexes breaks Attunement ties by Agility
   (HIST:463).
4. **Holding one's framework under shock.** Five statements roll Spirit (npc_behavior_v30:1054;
   faction_politics_v30:741, :752; conviction_track_v1.md:95; southernmost_v30:105); the Miraculous
   Event's witness rolls Cognition vs Truth (miraculous_event_v30.md:132).
5. **Perceiving the thread.** TS gates and feeds the pool (operations.py:244; FW:84); thread-aware
   exploration rolls Attunement (FW:91), and five Histories skills add Attunement dice to perceive
   Thread phenomena (HIST:105, :121, :280, :362, :450); for the Leap itself Attunement was struck
   (threadwork_v30:163). Selecting TS as a primary is the natural repair: perception of the thread
   becomes TS's.
6. **Concentration's formula.** `3·Focus + 2·Spirit` everywhere live (combatant.py:147;
   derived_stats_v30:159; SCV:267), but the Trained Memory skill still names *"Concentration (Focus +
   Recall)"* (HIST:217), a formula derived_stats_v30:166 removed.

**E, scored last, as a ratio against N and R.** Eleven plain words, each with its formulas beneath it;
a player predicting an outcome reads one primary and the formula that uses it. The costs are two new
words on the sheet (one, TS, with a 0–100 scale unlike the others), a primary (Recall) whose readers
do not yet exist, and one widened definition (WIL takes sincerity and belief under shock).

---

## 11. LIMITS, DISAGREEMENTS AND WHAT COULD NOT BE SOURCED

**Method limits.**

- **No subagent was spawned in any pass** (head, Method). The interrogations, the kinds, the
  principles and the selection are one producer's. An independent Opus critic read the first two
  passes (§12, §13); nobody has re-derived this pass's selection.
- **The coverage test is relative to today's ingredients** (§6, *How they are applied*). It cannot
  reward a set built of other quantities unless its formulas are rewritten; §7.5 states the rewrites.
- **The principles are this proposal's reading of the evidence**, and their order (kind first, then
  read, then independence and absorption, then coverage) is a choice. A different order (for example,
  P7 before P3) could select Command over Charisma.
- **Not opened** (cited by grep line, or carried from an earlier pass): `combat_c4_draft_v0.md:127`;
  AUG:192; `sigma.py:82-129`; `world_q.py:778-790`; `person_q.py:468-469`; `verb_table.yaml` rows;
  `fixtures.py:251`, `:381`, `:542-544`; the lane files under `research/by_lane/` beyond the §8 row
  heads; the bodies of `npc_behavior_system_v1.md`, `military_layer_v30.md`, `settlement_layer_v30.md`
  and `governance_play_redesign_v1.md` beyond the lines cited; `knots_v30.md:250`.
- **Not settled by reading:** what HIST's § mark means; whether *"Intellect"* (npc_behavior_v30:350)
  means Cognition; what ingredient a *"Coherence check"* or a *"Composure check"* reads (head U62–U64).
- **The Histories sweep** found skills whose effect names an ingredient, a pool or a formula; a skill
  written in a form the pattern misses could be absent.

**Where this proposal disagrees with the character template, with evidence.** (1) *"Charisma is the
thinnest"* is true of T2 readers, and this pass agrees CHA is narrowed there; by named T4 uses and
formulas BON is narrower. (2) The template's *"TS … Not an attribute"* and its reading of Recall by
ID-13 follow today's rulings; this exercise sets them aside, and the evidence selects both. (3) FOC is
not combat-only: it feeds a threadwork formula (F31) and a contest one (F20, overridden), and
`derived_stats_v30.md:267` keeps it apart from Spirit.

**Falsifiers.**

- **The head's §1.5–§1.7 and §7.3 here.** The command must print §1.5 row for row and the quoted
  blocks line for line; both were diffed against a fresh run in this pass.
- **The coverage claim.** A demand or formula the command reports expressed whose source actually
  names an ingredient outside the set would break it; the ingredients column is the thing to audit.
- **The recommendation.** If a set of fewer primaries covers as much without a rewrite against a
  stated source, it beats K01 on the principles; §7.5's smaller set does not.

---

## 12. CRITIC RECONCILIATION (first pass)

Kept as the record of the first reconciliation. ⚠ **Its counts and locations are that pass's:** §2–§3
have since moved to `_part2`, every count is superseded by the head's §1.7, and several of its choices
are reversed by §13.

| finding | applied / rebutted / narrowed | where (as of the first reconciliation) |
|---|---|---|
| **1. Combat Concentration omitted** | **applied, then narrowed on the count.** `composure` merged into `concentration` | head §1, §3 P03; `_part2` #18, #20, S01 |
| **2. "Overridden … almost always the 2026-09-05 ruling" is false** | **applied.** Every overridden draw names its cause | head tiers, §3 note 1 |
| **3. Command's Cognition term is glossed** | **applied** as a new term `tactical-read`, NAMED T2 (reversed in §13, finding 4) | head §3 P04; `_part2` #22, S02 |
| **4. A Spirit aptitude named in sources is absent** | **applied.** `steadfastness` and `devotion` added | head §1; `_part2` S04, S07, S09, S10 |
| **5. Some "named T4" draws rest on practice skills or flavour** | **applied** | head §3 P05, P18; `_part2` S02, S05 |
| **6. One source cell counted as two aptitudes** | **applied** | head §3 P02, P07; `_part2` #41, S03 |
| **7. Inferred draws a source contradicts** | **applied** | head §3 P04, P06, P08, P16; `_part2` #37, #52, S02, S04 |
| **8. Verbs graded on a shared word** | **applied.** #34 `survey` is *book*; #24 INFERRED | `_part2` #24, #34 |
| **9. Internal inconsistencies** | **applied, except FW:620, narrowed** | head §3 note 1; `_part2` #36, #52, S04 |
| **10. Rank inflated by re-counted inference** | **applied** (reworked in §13, finding 2) | head §1 |
| **11. Fine grain** | **applied, except Affability, rebutted** | head §1 |
| **12. Word choice** | **applied for Retention, narrowed for "aptitude"** (reworked in §13) | head, Words |
| **13. J-13 half read** | **applied** (superseded in §13: no ruling binds this exercise) | head §3 note 3 |
| **14. Locators** | **applied** | evidence tables |

---

## 13. CRITIC RECONCILIATION (OPUS, SECOND PASS)

The Opus critic read the four derivation files and the word study after the first reconciliation. Its
verdict: the arithmetic held; two structural defects (derived scores listed as aptitudes; an order key
that re-counted named evidence); the word study contradicted its sources in places; the nine survive.
Every locator below was re-opened before the edit it supports. **Three instructions of Jordan's,
2026-10-16, reshape how several findings are applied**, and are rows of their own.

| finding | applied / rebutted / narrowed | where |
|---|---|---|
| **Jordan: *"Learned skills and derived scores etc all need to be folded in to this."*** | **applied.** The evidence now holds the 41 formulas the sources compute (head §1.2), 58 learned-skill rows (§1.3) and 64 sourced uses (§1.4), all feeding the selection | head §1.2–§1.4 |
| **Jordan: *"ANY of these can be an attribute. ignore all prior rulings for this exercise."*** | **applied.** Every demand, formula, ingredient and skill is in the pool (§7.1); no ruling excludes a candidate; the rulings are one *what the tree currently says* paragraph; the number is open. J-13, the 2026-09-05 gloss, V-2/V-3, K-3, *"BALANCE is NOT a stat"* and the ten-attribute count are history only. ID-13 is a quality test (P1) | head Words; `_part2` §3 notes; §6, §7 |
| **Jordan: *"there are no derived scores when we don't even know our primaries."*** | **applied.** No item is called derived before selection; the 46 are marked by kind (CAPACITY, COMPUTED QUANTITY, PRACTICE, LIMIT, TEMPERAMENT; no RESOURCE); the sources' formulas are recorded with today's ingredients as history; derivation is assigned in §7.6, relative to the chosen set; coverage is the main test, run on four sets | head Words, §1.5; §7.3, §7.6 |
| **1. Derived scores presented as atomic aptitudes; J-13 read too narrowly; omitted formulas and learned-skill layers** | **applied, then reframed.** Every formula the critic named as omitted is in head §1.2 (handling F08, counter F05, resolution pool F19, Take a Breath F12, strain modifier F21, kernel trackers F23, Cover F28, effective Recall F37); the learned-skill layers are in §1.3 (Instruments, School, Techniques L07–L09; Investment and Record L58; Combatant skills L06; Histories levels L10; tactic cards L09; a sweep of the Histories skills). **Reframed:** the critic's remedy, *"a derived score is not an attribute"*, is not applied as a rule (Jordan's two later instructions); a formula is instead screened as a candidate by P2 and P3 (§7.2), and Agility, Command and the rest are kept whole because their ingredients absorb more, not because a ruling says so | head §1.2–§1.5; §7.2 |
| **2. The order key re-counts one named statement; "not re-counted" is false** | **applied.** A key is one statement; §1.5 counts distinct statements per demand at best basis and orders by named statements only; overridden statements are shown and not weighted; the *"not re-counted"* claim is retracted (`_part2` §4); totals recomputed; the command rewritten, its output quoted and diffed | head §1.5, §1.7; `_part2` §4 |
| **3. The twelve named "homeless" draws reduce to the nine** | **applied, and reframed (Jordan's instruction).** `judgment` is Hold Court, CHA or ACU (U15); `anticipation` is Reading (F06); `situational-awareness` is Command (F18). This shows the nine **express** those demands, not that the nine are right: on the coverage test the nine leave 8 demands and 9 formulas uncovered | §7.3, §7.7 |
| **4. Command-derived draws coded NAMED T2 against the head's own rule; a docstring treated as mechanism** | **applied.** As terms, the uses of Command are INFERRED; Command is a source formula NAMED T2 (F18); *"tactical read"* is called a docstring gloss; the span cites MB:309 and units.py:2700-2722 | `_part2` P04, #22, S02; head F18 |
| **5. Recall: contrary sources ignored; FW:95 coded two ways; overridden draws weighted as named** | **applied.** Both contrary sources are quoted in full (§7.4), and the AUG objection is kept as standing; `[fw-research]` is overridden everywhere, with the Histories Recall skills as a separate key; HIST:36 is F37 and an S16 draw. Recall is now **selected on coverage, with low confidence and a false N-line stated**, under Jordan's instruction that rulings (ID-13 as a ruling, the D2 slot) do not exclude. **Rebutted in part:** the +2D citation bonus is binary (SCV:177) and reads no person's Recall | §7.4; `_part2` P13, S16 |
| **6. "Force is all effect size" contradicted** | **applied.** `strength` carries odds, cost and effect size; the Health term is the code's labelled noise (combatant.py:21) | `_part2` P03, #18, #20, S01; head F07–F10; §8.1 |
| **7. Pattern-matching on the word: Precision, Deception** | **applied.** `precision` rests on craft practice (HIST:241); *Precision Hands* is perceptual (L49); `deception`'s skills are *Smooth Liar* and *Intimidation* on the Obscuring move (L45, L46); the *practice-named* flag is dropped | `_part2` P01, P08, P11, #13; head §1.3, §1.5 |
| **8. Named draws never coded** | **applied, each:** valoria_ui_ux_v4_1:916 (S01; *"courage is gone"* narrowed); FW:91 (P15, S04), HIST:105 (L16), HIST:362 (L21; P05 `[hist-thread-att]`), with the Leap's struck Attunement noted (threadwork_v30:163); southernmost_v30:103 (S09), and the sweep found :123 too; npc_behavior_v30:350, :352 (S11); threadwork_v30:688 (S05); SCV:155's Appraise Ob (P02, #50, S03) and FW:411's Impress Ob (P16, S04) | `_part2` §3–§5; head §1.4 |
| **9. "T1 is 0" overstated** | **applied.** The season loop's BODY-computed `end` makes `stamina` and `toughness` NAMED T1; BODY is an ingredient (C13), F13 its formula | head tiers, C13, F13 |
| **10. "The kernel binds only faculty" overstated** | **applied.** It binds `faculty` and `charisma`; `charisma` sets only Face's inert ceiling | head tiers; `_part2` S03 |
| **11. Discernment as a T3 statement overstated** | **applied.** Every `[ax7]` draw is INFERRED | `_part2` #8, #35, S10 |
| **12. Draws not commensurable; roles carry no magnitude; Mentor coded as learning; the gloss's reach** | **applied** for weighting, roles and Mentor (now L56; the S07 `learning` draw removed). **Narrowed** for the gloss: `_part2` §3 note 1 states the reach to investigation_systems_v30:243 explicitly; under Jordan's instruction the gloss binds nothing, and the selection counts its statements as source statements | head Words; `_part2` §3 note 1, S07 |
| **13. Missing subsystems** | **applied.** S11–S16 in the fixed template; they surfaced S-defect 4 and that faction Intel, Spy, Diplomacy and Treat roll faction stats | `_part2` §5 |
| **Word study: Devotion and Sincerity in Bonds** | **applied.** Both are in the WIL group (Spirit × 1, derived_stats_v30:557; FW:822; FW:430); the registry alias is S-defect 2 | `_equivalences` |
| **Word study: §3.2 mapping errors (A2, C/E, D)** | **applied.** Contact endurance → WIL; inference → REC; judgment → CHA or ACU; anticipation → ACU; tactical read → a use of Command | `_equivalences` |
| **Word study: Concentration ≈ Will** | **applied.** 3F + 2S is a blend of two ingredients; derived_stats_v30:267 separates them | `_equivalences` |
| **Word study: D's definition fails for Tactical read** | **applied.** Tactical read reads a field; it is a use of Command | `_equivalences` |
| **Word study: Quickness/Reflexes "stay two"; the semantic test cannot observe its failure** | **applied.** They are two formulas over one ingredient. Members that the sources compute from one ingredient are **identical by code** for the divergence test, which applies to candidate primaries and the formulas over them, not to words | `_equivalences` |
| **Word study: six, not seven, typed as not a capacity** | **applied; the column is replaced** by the head's kind (19 / 14 / 9 / 2 / 2) | `_equivalences` |
| **Word study: Numeracy argued from its coinage** | **applied.** Dropped; numeracy is practice because no source names it as a person's capacity | `_equivalences`; §7.2 |
| **Word study: upheld items** | **agreed**, as PRACTICE, TEMPERAMENT and LIMIT kinds | head §1.5 |
| **Word study: Leadership and Persuasiveness typed "cap/skl"** | **applied.** Leadership is a use of Command (COMPUTED QUANTITY); Persuasiveness is a use of Charisma (CAPACITY) | head §1.5 |
| **Word study: "equivalence class"; non-symmetric relations; the "Domain" column; three groupings** | **applied.** *Group*; relation labels defined, non-symmetric ones marked; the column renamed *faculty family*; one grouping, §8.1's | `_equivalences`; §8.1 |
| **Etymologies** | **applied.** Empathy medium (Titchener 1909 the usual citation); numeracy high (Crowther 1959, ‡ dropped); *learn* from PIE *\*leis-*, medium; *plan* low; *discipulus* < *discere* debated | `_equivalences` |
| **Rule compliance: ID-13; the meta-rule's RES cut; V-2b; the 2026-09-05 weighting; "aptitude"'s third sense** | **applied.** ID-13 is a quality test (P1), and Recall's weak reader is stated wherever it is selected; RES is re-expressed, not cut, with what exists named (§9); V-2b is a question (§9); overridden statements are not weighted as named; *demand* replaces *aptitude*, with all three senses named (head Words) | §6, §9; head Words |
| **NERS: CHA, ACU, STR, BON N-lines** | **applied.** CHA narrowed at T2; ACU holds without the docstring; STR's lines are Impact, bind, handling and half of Balance, with the Health term noise; BON narrowed by Disposition | §7.4, §10 |
| **Not checked by the critic** | **checked here:** the command runs and its quoted output diffs clean; knots_v30:149, npc_relational_graph_v30:277, fieldwork_v30_infill:48, combat_reference_v1:598, FW:446-447, :477-483, units.py:2700-2712 and military_layer_v30:132-133 hold. **Corrected:** TS +1 at a Breach is FW:254, not :255. Still not checked: the lane files; combat_c4_draft_v0:127; sigma.py:82-129; world_q.py:778-790; person_q.py:468-469; verb_table rows; whether ED-IN-0185 Q7 says "10 attributes" verbatim | §11 |
