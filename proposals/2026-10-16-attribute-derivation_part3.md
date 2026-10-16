# Attribute derivation — part 3 (SECONDARY): §6 clusters, §7 what should be an attribute, §8 meta-rule, §9 NERS, §10 limits

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. **Secondary to §1's list.** It recommends; J-T1 (stored or derived) and J-T2 (the tenth) stay Jordan's.
## Parts, in reading order: [head](2026-10-16-attribute-derivation.md) (head, §1–§3) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§4–§5) · **this file** (§6–§10).

---

## 6. STAGE 3: COLLATION

### 6.1 The rule

Every one of §1's 45 aptitudes goes into exactly one cluster, by **what it would measure about a
person**. **The clustering is a judgment call.** The aptitudes are fine. The clusters are this
proposal's reading, and §1 is kept unmerged so Jordan can cluster differently.

The columns:

- **PRA domains**, **verbs** (with distinct resolvers in brackets) and **subsystems** count the items
  that draw at least one member of the cluster.
- **draws as** counts roles over all the cluster's draws.
- **maps to the nine today** follows §1 column 8.

| K | cluster: what it measures | aptitudes | PRA domains | verbs [distinct resolvers] | subsystems | draws as | named (best tier) vs inferred | maps to the nine today |
|---|---|---|---|---|---|---|---|---|
| K1 | Force | `strength` | 3: P03, P11, P17 | 3 [2]: #18, #20, #45 | 2: S01, S08 | effect size 8 | named 4 (best T2); inferred 4 | STR |
| K2 | Agility | `quickness`, `reflexes`, `balance` | 2: P03, P18 | 2 [1]: #18, #20 | 1: S01 | odds 14 | named 14 (best T2); inferred 0 | AGI |
| K3 | Hand | `dexterity`, `precision` | 3: P01, P11, P12 | 4 [4]: #13, #30, #48, #49 | 1: S08 | effect size 11, odds 1 | named 0; inferred 12 | none (AGI only by the registry's Dexterity alias; no code) |
| K4 | Constitution | `stamina`, `toughness`, `hardiness`, `recovery` | 4: P03, P05, P15, P17 | 6 [5]: #18, #20, #24, #30, #39, #45 | 6: S01, S02, S04, S05, S08, S09 | difficulty/cost 19, effect size 4, odds 2, resists another 1 | named 19 (best T2); inferred 7 | END (WIL at low weight in stamina and toughness) |
| K5 | Intellect | `reasoning`, `inference`, `spatial-sense`, `numeracy` | 10: P02, P04, P07, P08, P09, P10, P11, P13, P15, P19 | 7 [7]: #8, #12, #28, #34, #36, #41, #50 | 5: S03, S04, S06, S08, S09 | odds 20, effect size 4, eligibility 3, resists another 1 | named 18 (best T4); inferred 10 | ACU, through the Cognition alias the registry marks [ASSUMPTION]; numeracy and inference none |
| K6 | Strategy | `planning`, `judgment` | 3: P04, P09, P19 | 1 [1]: #22 | 4: S02, S06, S07, S10 | odds 13 | named 2 (best T4); inferred 11 | none |
| K7 | Retention | `memory`, `learning`, `breadth` | 6: P02, P07, P10, P12, P13, P14 | 3 [3]: #38, #41, #51 | 3: S03, S04, S07 | odds 9, eligibility 2, effect size 2 | named 9 (best T4); inferred 4 | none (Recall, not on the registry) |
| K8 | Application | `concentration`, `discipline`, `patience` | 8: P01, P02, P05, P07, P09, P11, P13, P17 | 11 [5]: #38, #39, #50, #51, #58, #59, #60, #61, #62, #63, #64 | 6: S02, S03, S04, S05, S06, S08 | eligibility 12, odds 9, effect size 5, difficulty/cost 3 | named 15 (best T4); inferred 14 | FOC (concentration, discipline); patience none |
| K9 | Noticing | `observation`, `land-sense`, `situational-awareness`, `anticipation` | 7: P03, P04, P07, P08, P12, P15, P17 | 7 [6]: #18, #20, #22, #34, #36, #39, #49 | 4: S01, S02, S04, S09 | odds 18, effect size 3, eligibility 3 | named 18 (best T2); inferred 6 | split: ACU (observation, land sense), ACU + ATT (anticipation), CHA + ACU through Command (situational awareness) |
| K10 | Reading others | `reading-people`, `empathy`, `discernment` | 6: P02, P06, P07, P09, P10, P16 | 6 [6]: #8, #12, #35, #37, #50, #56 | 6: S03, S04, S06, S07, S08, S10 | odds 19, resists another 3, effect size 1 | named 13 (best T3); inferred 10 | ATT (discernment none) |
| K11 | Presence | `presence`, `leadership`, `intimidation` | 5: P02, P04, P08, P09, P16 | 6 [6]: #22, #32, #50, #52, #54, #56 | 5: S02, S03, S04, S06, S07 | odds 14, eligibility 5 | named 13 (best T2); inferred 6 | CHA |
| K12 | Persuasion | `persuasiveness`, `verbal-fluency`, `quick-thinking`, `deception` | 4: P02, P08, P10, P16 | 7 [7]: #27, #28, #32, #35, #37, #52, #56 | 3: S03, S04, S07 | odds 15, effect size 4 | named 2 (best T4); inferred 17 | CHA for persuasiveness only (FW:409); the rest none |
| K13 | Bonds | `relational-depth`, `sincerity` | 2: P06, P16 | 2 [2]: #35, #42 | 1: S04 | odds 6, eligibility 2 | named 7 (best T2); inferred 1 | BON (but FW:430 rolls sincerity on WIL) |
| K14 | Will | `will`, `contact-endurance`, `self-coherence` | 2: P05, P06 | 9 [3]: #40, #42, #58, #59, #60, #61, #62, #63, #64 | 3: S04, S05, S09 | odds 13, eligibility 9, difficulty/cost 9 | named 31 (best T2); inferred 0 | WIL (self-coherence is RES; contact endurance is Spirit × 5) |
| K15 | Nerve | `composure`, `courage`, `boldness` | 7: P02, P03, P04, P08, P10, P12, P18 | 4 [3]: #18, #20, #48, #50 | 5: S01, S02, S03, S04, S10 | difficulty/cost 12, odds 8 | named 11 (best T2); inferred 9 | FOC (composure); courage none; boldness is TMP, off the registry |
| K16 | Thread sensitivity | `thread-sensitivity` | 3: P05, P06, P07 | 10 [4]: #36, #40, #42, #58, #59, #60, #61, #62, #63, #64 | 3: S04, S05, S09 | odds 9, eligibility 7 | named 16 (best T2); inferred 0 | none (TS, its own stat) |

### 6.2 Cross-tabs

**Legend.** ● at least one NAMED draw (T1–T4). ◐ overridden draws only. ○ inferred draws only. A blank
cell means no draw.

**Cluster × practice domain.**

| K \ P | P01 | P02 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P17 | P18 | P19 | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| K1 Force |  |  | ● |  |  |  |  |  |  |  | ○ |  |  |  |  |  | ○ |  |  | 3 |
| K2 Agility |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |  | 2 |
| K3 Hand | ○ |  |  |  |  |  |  |  |  |  | ○ | ○ |  |  |  |  |  |  |  | 3 |
| K4 Constitution |  |  | ● |  | ● |  |  |  |  |  |  |  |  |  | ● |  | ○ |  |  | 4 |
| K5 Intellect |  | ◐ |  | ● |  |  | ◐ | ● | ● | ○ | ○ |  | ○ |  | ● |  |  |  | ● | 10 |
| K6 Strategy |  |  |  | ○ |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ○ | 3 |
| K7 Retention |  | ◐ |  |  |  |  | ◐ |  |  | ○ |  | ○ | ● | ○ |  |  |  |  |  | 6 |
| K8 Application | ○ | ◐ |  |  | ● |  | ○ |  | ○ |  | ○ |  | ○ |  |  |  | ○ |  |  | 8 |
| K9 Noticing |  |  | ● | ● |  |  | ◐ | ○ |  |  |  | ○ |  |  | ● |  | ● |  |  | 7 |
| K10 Reading others |  | ◐ |  |  |  | ○ | ◐ |  | ● | ● |  |  |  |  |  | ● |  |  |  | 6 |
| K11 Presence |  | ◐ |  | ● |  |  |  | ● | ● |  |  |  |  |  |  | ● |  |  |  | 5 |
| K12 Persuasion |  | ○ |  |  |  |  |  | ○ |  | ○ |  |  |  |  |  | ● |  |  |  | 4 |
| K13 Bonds |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |  |  |  | 2 |
| K14 Will |  |  |  |  | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  | 2 |
| K15 Nerve |  | ◐ | ● | ○ |  |  |  | ○ |  | ○ |  | ○ |  |  |  |  |  | ○ |  | 7 |
| K16 Thread sensitivity |  |  |  |  | ● | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  | 3 |

**Cluster × subsystem.**

| K \ S | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 | S10 | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K1 Force | ● |  |  |  |  |  |  | ○ |  |  | 2 |
| K2 Agility | ● |  |  |  |  |  |  |  |  |  | 1 |
| K3 Hand |  |  |  |  |  |  |  | ○ |  |  | 1 |
| K4 Constitution | ● | ○ |  | ● | ● |  |  | ○ | ● |  | 6 |
| K5 Intellect |  |  | ◐ | ● |  | ● |  | ○ | ● |  | 5 |
| K6 Strategy |  | ○ |  |  |  | ● | ○ |  |  | ○ | 4 |
| K7 Retention |  |  | ◐ | ◐ |  |  | ○ |  |  |  | 3 |
| K8 Application |  | ● | ◐ | ○ | ● | ○ |  | ○ |  |  | 6 |
| K9 Noticing | ● | ● |  | ◐ |  |  |  |  | ● |  | 4 |
| K10 Reading others |  |  | ◐ | ◐ |  | ● | ○ | ○ |  | ● | 6 |
| K11 Presence |  | ● | ◐ | ● |  | ● | ○ |  |  |  | 5 |
| K12 Persuasion |  |  | ○ | ● |  |  | ○ |  |  |  | 3 |
| K13 Bonds |  |  |  | ● |  |  |  |  |  |  | 1 |
| K14 Will |  |  |  | ● | ● |  |  |  | ● |  | 3 |
| K15 Nerve | ● | ○ | ◐ | ○ |  |  |  |  |  | ○ | 5 |
| K16 Thread sensitivity |  |  |  | ● | ● |  |  |  | ● |  | 3 |

### 6.3 Driven by acts, by learned skills, or by sustained play

Jordan asked to see which clusters are driven by acts and which by learned skills. The comparison
uses distinct verb resolvers (the bracket), so the seven thread rows count once.

| driven by | clusters (PRA / verb resolvers / subsystems) | reading |
|---|---|---|
| **learned skills**: many practice domains, few acts | K5 Intellect (10 / 7 / 5), K8 Application (8 / 5 / 6), K15 Nerve (7 / 3 / 5), K7 Retention (6 / 3 / 3) | capacities under MANY practices. A per-domain practice key cannot carry them without one copy per domain |
| **acts**: more resolvers than domains | K12 Persuasion (4 / 7 / 3), K3 Hand (3 / 4 / 1), K16 Thread sensitivity (3 / 4 / 3), K14 Will (2 / 3 / 3, over 9 rows) | what single acts ask for in the moment. K12 and K3 are almost wholly INFERRED; K14 and K16 are named at T2 |
| **sustained play**: subsystems at least equal to the larger of the other two | K6 Strategy (3 / 1 / 4), K4 Constitution (4 / 5 / 6) | the subsystem-level requirements Jordan predicted, *"endurance of a march, judgment under uncertainty of command"*. They appear in few verb rows because no single act carries them |
| even | K9 Noticing (7 / 6 / 4), K10 Reading others (6 / 6 / 6), K11 Presence (5 / 6 / 5), K1 Force (3 / 2 / 2), K2 Agility (2 / 1 / 1), K13 Bonds (2 / 2 / 1) | — |

### 6.4 What each cluster moves

The *draws as* column of §6.1 gives the role mix.

- **Body clusters split by role.**
  - K4 Constitution is mostly **difficulty/cost**: 19 of 26 draws (wounds, fatigue, exposure).
  - K2 Agility is all **odds** (14 of 14).
  - K1 Force is all **effect size** (8 of 8).
- **K14 Will is the one cluster spread evenly over odds (13), eligibility (9) and cost (9).** It
  supplies the pool, a contact cap and a cost resistance in the same resolver.
- **K16 Thread sensitivity is odds and eligibility** (9 and 7). It is the cluster most often used as a
  **gate**, with K8 Application (12 eligibility draws, from Focus's operations-per-contact rule).
- **Social and perceptual clusters are overwhelmingly odds** (K10: 19 of 23; K11: 14 of 19; K9: 18 of
  24). In a contest-shaped game, they are what makes a pool bigger.

---

## 7. WHAT THE EVIDENCE SUPPORTS AS ATTRIBUTES (secondary)

### 7.1 The nine, and the template's four further candidates, against the evidence

Each code's row sums the draws of the aptitudes §1 column 8 maps to it. **The mapping uses only the
registry's names and aliases, or a source using that attribute for that function.** Fifteen aptitudes
map to none (§7.3).

| attribute | aptitudes mapped (§1 column 8) | draws | PRA domains | verbs [resolvers] | subsystems | what it moves | named / overridden / inferred |
|---|---|---|---|---|---|---|---|
| STR | strength | 8 | 3 | 3 [2] | 2 | effect size 8 | 4 / 0 / 4 |
| AGI | quickness, reflexes, balance | 14 | 2 | 2 [1] | 1 | odds 14 | 14 / 0 / 0 |
| END | stamina, toughness, hardiness | 24 | 3 | 6 [5] | 6 | difficulty/cost 17, effect size 4, odds 2, resists another 1 | 17 / 0 / 7 |
| FOC | concentration, composure, discipline | 34 | 10 | 13 [6] | 5 | difficulty/cost 14, eligibility 12, odds 6, effect size 2 | 16 / 6 / 12 |
| ACU | reasoning, observation, spatial-sense, land-sense | 32 | 11 | 7 [7] | 4 | odds 22, effect size 6, eligibility 3, resists another 1 | 13 / 10 / 9 |
| WIL | will, contact-endurance, recovery | 24 | 2 | 9 [3] | 2 | odds 13, eligibility 9, difficulty/cost 2 | 24 / 0 / 0 |
| ATT | reading-people, empathy | 19 | 6 | 4 [4] | 5 | odds 18, effect size 1 | 4 / 8 / 7 |
| CHA | presence, leadership, persuasiveness | 25 | 6 | 9 [9] | 5 | odds 19, eligibility 5, effect size 1 | 10 / 5 / 10 |
| BON | relational-depth, sincerity | 8 | 2 | 2 [2] | 1 | odds 6, eligibility 2 | 7 / 0 / 1 |
| REC (candidate) | memory, learning, breadth | 13 | 6 | 3 [3] | 3 | odds 9, eligibility 2, effect size 2 | 3 / 6 / 4 |
| TMP (candidate) | boldness | 5 | 1 | 2 [1] | 2 | odds 5 | 4 / 0 / 1 |
| RES (candidate) | self-coherence | 9 | 1 | 6 [1] | 2 | difficulty/cost 9 | 9 / 0 / 0 |
| TS (candidate) | thread-sensitivity | 16 | 3 | 10 [4] | 3 | odds 9, eligibility 7 | 16 / 0 / 0 |

### 7.2 One by one

- **Well-supported, broad and distinct** (drawn by at least five domains or five subsystems):
  - **END** (6 subsystems, named at T2 and T4). The broadest body attribute: wounds, fatigue,
    exposure, troop stamina, and a defence against the thread.
  - **ACU** (11 domains, the most of any). ⚠ 10 of its 32 draws are overridden, and much of the rest
    reaches ACU only through the Cognition alias the registry marks *"[ASSUMPTION] … Jordan veto"*
    (`descriptor_registry.yaml:42`). **Its support is broad, and it is conditional on that alias.**
  - **FOC** (10 domains). ⚠ The sources give it **two jobs**: concentration (SCV:267;
    threadwork_v30:199) and composure (SCV:199; AUG:90). That is a definitional question, not a
    merge.
  - **CHA** (9 verb resolvers, the most of any; 5 subsystems). Its one T2 reader is still
    `derive_command`; the rest is T4 or overridden.
  - **ATT** (6 domains, 5 subsystems). ⚠ 8 of its 19 draws are overridden (the inquiry column).
- **Named strongly, but narrow:**
  - **WIL** (24 draws, all named, but 2 domains: threadwork and knots).
  - **AGI** (14 named, but combat and stealth only).
  - **STR** (8 draws: combat at T2; craft and labour inferred).

  Each is what one resolver needs. Cutting any of them blinds a stub channel (§9).
- **Thin:** **BON** (8 draws, 2 domains, 1 subsystem). The thinnest of the nine on this test.

**Disagreement with the 2026-08-15 proposal** (AUG:191-195, :473-474). It ranks Focus *"CONTESTED"*
(+0.3pp) and Charisma *"CONTESTED"* (zero code). On the test of **what the designs REQUIRE**, FOC (10
domains) and CHA (5 subsystems, 9 verb resolvers) are among the most-drawn of the nine. **AUG measured
EFFECT in code. This proposal measures REQUIREMENT in design.** Both are true. A low measured effect
says the stubs under-use them, not that the game does not need them. **Judgment call.**

### 7.3 Merge candidates, and the clusters with no home

**Merge candidates (pairs, with the evidence).**

| pair | evidence for merging | evidence against | reading |
|---|---|---|---|
| **RES into WIL** | 8 of RES's 9 draws are the thread pool, beside `spirit × 2` (P05, S05 and §4 rows 58–63). The plan names *"'spirit' (resilience, R-14)"* a candidate input only (`_part5.md:444`) | S09's Coherence check at Depth 4 (FW:253) reads RES with no WIL | **merge**: RES is a sub-term of WIL. It is not a candidate for the tenth |
| **BON into ATT** | BON's two domains (P06, P16) are a subset of the domains drawing `empathy` (P02, P06, P16). By Jordan's co-occurrence test it is a sub-term candidate | the knot's T2 gate reads BON alone (`knots.py:185-203`). FW keeps Connect (Bonds, :410) apart from Read (Attunement, :408) | **candidate, not finding**: thin, and the one T2 reader is a gate |
| **STR and AGI** | both named only in combat at T2 (the template's §A.4.1) | the bout reads them in different channels (impact and health against tempo, reflex and balance) | **keep apart** |
| **TMP** | a lean, not a capacity: `disp` moves aggression, not ability (`combat_systems.py:183`) | — | **not an aptitude** under this proposal's definition. A chooser-side field, like values, if it is ever read outside combat |

**Clusters and aptitudes with no home among the nine.** Fifteen aptitudes map to none: 72 of 303
draws. Of those 72, only 16 are NAMED or overridden, and those 16 fall in four groups:

- `anticipation` (7, T2): the combat reading blend of ACU and ATT, and the command feint roll.
- `situational-awareness` (3 named, T2): Command as span of control.
- `inference` (3 overridden: FW:306).
- `judgment` (2, T4) and `discernment` (1, T3).

The other 56 are inferred. **So the nine cover most of what the sources NAME. What is homeless is
mostly what this proposal infers.**

| candidate for the tenth | cluster draws (§6.1) | named | an ID-13 reader in the tree? | reading |
|---|---|---|---|---|
| **REC: Retention** (memory, learning, breadth) | 13 | 3 T4, 6 overridden | **`train`** (#51, IN-12 step 9, T3) would read learning speed and breadth. ⚠ **V-2 bars an attribute from `train`**: its §9 row declares no `contests:` (`2026-10-16-character-template_part2.md:179`). So Recall needs a V-2 amendment, here called **V-2b**, *"a writer's increment may read an attribute"*, parallel to the template's V-2a for gates. Jordan's. The dice of `research` and `reconstruct` are overridden | **the best-supported homeless cluster**: 6 domains, 3 subsystems. **Low confidence**: no reader above T4 without V-2b |
| **K6: Strategy** (judgment, planning) | 13 | 2 T4 (Hold Court; the settlement actions) | Command's Cognition term exists and is never glossed. A per-person `choice_temperature` is proposed by no source | weak: 11 of 13 draws inferred |
| **K3: Hand** (dexterity, precision) | 12 | 0 | four **open** effect cells (`forgery_quality`; `× f(degree)` on `restore` and `work`; `tend`'s body raised) | weak: all inferred. A candidate only if those cells get readers |
| **discernment** | 4 | 1 T3 (AX-7) | `refracted_confidence`, the factor held at 1 (H-200) | strongest ID-13 case of any homeless aptitude, but it sits in the ATT cluster (K10). **Fold into ATT's definition**, which is one of J-T9's three options |
| **TS** (the template's candidate) | 16 | 16 (T2 11) | its own field, J-T1a (K-3, ratified as intent) | **leave on its own field.** It is 0–100, not 1–7 (`descriptor_registry.yaml:64`), and it **grows by exposure** like a practice: +5 inherited (HIST:127), +3 occupational (HIST:324), +1 at a Breach (FW:255) |
| **TMP**, **RES** (the template's candidates) | 5; 9 | 4 T2; 8 T2 and 1 T4 | `disp`; `resilience` | not the tenth: TMP is not an aptitude, and RES merges into WIL (above) |

### 7.4 Leave as practice, or cut

- **Leave as practice:** every P-domain. Also the aptitudes whose only evidence is a practice skill
  sitting on them:
  - `deception`, under HIST:339 Smooth Liar;
  - `intimidation`, under HIST:349;
  - `numeracy`, under trade and administration;
  - `verbal-fluency` and `quick-thinking`, under P02;
  - `precision` and `dexterity`, under craft.

  Under either option these enter play through `faculty(domain)`'s practice term, unless a reader asks
  for them by name.
- **Cut from the nine:** nothing, on this evidence. BON is the only member near the line (§7.3).

### 7.5 THE RECOMMENDATION (secondary; a judgment; Jordan's to rule under J-T1 and J-T2)

**STR · AGI · END · FOC · ACU · WIL · ATT · CHA · BON, plus Retention (REC: memory, learning speed,
breadth of practice) as the tenth.** Within that:

- **WIL absorbs RES.**
- **ATT's definition absorbs AX-7's discernment**, if J-T9 so rules.
- **FOC's definition names both of its jobs**, concentration and composure.

**Confidence.**

- **Medium** that the eight STR–CHA are each drawn on and distinct.
- **Low to medium** for BON.
- **Low** for the tenth: Retention has no reader above T4, and its natural reader, `train`, needs V-2b.

**This is the 2026-08-15 proposal's option A-2, *"Ratify the 10 unchanged"*** (AUG:192). The evidence
here reaches A-2 by a different route from the one AUG rejected it on (§7.2).

**The alternative, if Jordan merges BON into ATT:** the freed slot goes to **Strategy** (judgment,
planning). That rests on 2 named draws of 13, so its confidence is **low**.

**Read under the template's two options:**

- **Option B (stored: the ten on `Person.attributes`).** Each domain's `faculty(domain)` composes its
  attributes as §3's rows list them. As V-2 stands, an attribute reaches only rows declaring
  `contests:`:
  - four shipped: `fight` and `accept` (`verb_table.yaml:485`, `:610`), `march` (`:676`), `tell`
    (`:953`);
  - four planned and routed to the sigma roll: `determine`, `argue`, `arrest`, `interrogate`
    (template `_part2` rows 8, 50, 54, 56).

  **So 8 of the 35 graded verbs can read an attribute.** The other 27 cannot until they gain
  `contests:` or V-2 is amended. They include:
  - the seven thread operations and the knot;
  - the six inquiry acts, which `rosters.yaml:1074-1077` says must not be made contests;
  - `train`;
  - the open effect cells (`forge`, `restore`, `work`, `tend`).

  **Retention has no lawful reader under B without V-2b**, and the knot's BON gate none without V-2a.
- **Option A (derived: nothing attribute-shaped is stored; practice per domain).** Every aptitude is
  carried inside the practice keys of the domains that draw it. **The cost is the one-per-domain copy:**
  - a cluster drawn by N domains needs N consistent copies. That is K5 Intellect (10), K8 Application
    (8), K9 Noticing and K15 Nerve (7 each), K7 Retention and K10 Reading others (6 each). Two ladders
    for one quantity is the S defect `CLAUDE.md` §0.06 names.
  - **Retention cannot be a practice key at all.** Learning speed is a rate over every key, the thing
    `train` would scale, so under A it has no carrier.
  - Clusters drawn by one or two domains lose little under A: K2 Agility, K13 Bonds and K14 Will.
- **So the evidence narrows J-T1 without deciding it.** B fits the cross-domain clusters, and A fits
  the domain-local ones. The cross-domain clusters are the larger share: §6.3's *learned skills* row.
  **Judgment call.**

---

## 8. WHAT IT ADDS AND CUTS (the meta-rule, relative to the registry's nine)

| | object | removes or adds something that exists? |
|---|---|---|
| **adds** | one attribute, Retention, in the slot ED-IN-0185 ruled and ED-IN-0193 left unnamed | fills a ruled, empty slot. No count changes |
| **adds** | a named amendment, **V-2b** (a writer's increment may read an attribute), raised for Jordan, not drafted into any rule file | no: a question, not a rule |
| **widens** | FOC's definition (both jobs); ATT's (discernment, if J-T9 rules so) | no new slot |
| **cuts** | RES as a separate candidate (folded into WIL) | no: RES is on no roster |
| **declines** | TMP and TS for the tenth; Strategy and Hand as attributes (insufficient named evidence) | no: none is on the roster |
| **flags** | BON as the thinnest of the nine (merge candidate into ATT) | no: nothing is cut |

**Net effect on the roster: zero new slots beyond the ruled ten, and zero removals.** This proposal
edits no code, no registry and no ledger. It allocates no ID. It adds four files under `proposals/`.

---

## 9. NERS, IN BRIEF (`skills/ners/SKILL.md`)

`[SELF-AUTHORED — bias risk]`. Grade: **paper**. No outcome was measured.

**N: for each recommended attribute, propose cutting it and name what dies** (from §3–§5's tables).

| cut | what dies | direction | verdict |
|---|---|---|---|
| STR | combat's impact and health channel (T2); strength in labour and craft (inferred) | bottom-up (person → bout) | **holds, narrowed to combat at T2** |
| AGI | tempo, reflex and balance (T2); stealth (T4) | bottom-up | **holds, narrowed**: one resolver |
| END | wounds and fatigue in combat (T2); travel exposure (T4); the defence against Dissolution (T4); troop stamina (inferred) | bottom-up, lateral (person vs thread), top-down (field → troop) | **holds** |
| FOC | contest strain defence and Concentration (T4, overridden); operations per contact (T4); poise (T2) | bottom-up, horizontal (contest, thread, bout) | **holds** across three subsystems |
| ACU | the depth gates of inquiry (T4, overridden); settlement Develop and Survey (T4); pathfinding (T4); Command's secondary term (T2) | vertical (field → command), horizontal | **holds**, conditional on the Cognition alias |
| WIL | the thread pool, the knot roll, `thread_read`, contact endurance (T2/T4) | bottom-up | **holds, narrowed to the substrate** |
| ATT | reading people in administration, socializing and argument (T4); combat reading's 1/3 term (T2) | lateral (person vs person) | **holds**: 8 of 19 draws overridden |
| CHA | Command (T2), and with it the reform gate, morale erosion and span of control; presence in social acts (T4) | top-down (commander → field) | **holds at T2 through Command alone** |
| BON | the knot gate and cap (T2); Connect (T4) | lateral | **narrowed**: the gate would need a replacement input (the template's §3.3 shows the same under its Option A) |
| Retention | nothing at T1–T3 today. Learning speed and breadth are T4 (HIST:34-41) | vertical (practice → growth) | **FALSE N-LINE TODAY**, by the skill's disqualifier 2 (no producer moves an outcome). It becomes live only if `train` reads it (V-2b) |

**S: three "two ladders for one quantity" defects the interrogation exposed.** Each is one aptitude
computed from different attributes in two designs (`CLAUDE.md` §0.06, *"calculations consistent in
methodology"*):

1. `composure`: Focus defence (SCV:199) against *"Composure (Cha + 6)"* (FW:640). The latter was
   retired only as the contest tracker (SCV:242).
2. `sincerity`: the registry aliases it to Bonds (`:48`), while the fieldwork Sincerity Check rolls
   Spirit (FW:430).
3. `reflexes` and initiative: Agility plus History in the stub (`combat_systems.py:1419-1421`),
   against *"initiative by Attunement"* (FW:106).

None is repaired here: they are named for whoever defines the attribute.

**E, scored last.** The flat list is legible (45 plain words). The recommendation adds no slot. The
cost is two widened definitions (FOC, ATT), which a player must read to predict an outcome.

---

## 10. LIMITS, DISAGREEMENTS AND WHAT COULD NOT BE SOURCED

**Method limits.**

- **No reader was spawned.** This lane's toolset holds no agent-dispatch tool. All three interrogations
  and the collation are one producer's. **Owed:** a structurally independent critic (`valoria-critic`)
  on the 111 inferred draws and on §6's clustering, the two places a single reader is likeliest to be
  wrong.
- **Not opened** (cited only by grep line, or not at all):
  - `.designs/systems/combat/reference/combat_c4_draft_v0.md`;
  - `investigation_systems_v30.md`;
  - the bodies of `npc_behavior_system_v1.md`, `military_layer_v30.md`, `settlement_layer_v30.md` and
    `governance_play_redesign_v1.md` beyond the lines cited;
  - the persuasion-actor upload extracts (the template's PD3, scratch, T4);
  - the lane files beyond the §8 row heads cited.
- The template's verified code locators (`combat_systems.py`, `exchange.py`, `orchestration.py`,
  `engine.py`, `knots.py`, `operations.py`) were reused, not re-opened.

**Could not source, so dropped or kept inferred:**

- Practices for *politician*, *leader*, *logistics*, *horsemanship*, *seamanship* and *hunting* (§2).
- Any aptitude for the 24 choice-only verbs, beyond S10's chooser.
- Every draw of ten aptitudes (§1 Totals).

**Where this proposal disagrees with the character template, with evidence.**

1. **On "Charisma is the thinnest".** The template (§3.2) says CHA is *"the thinnest: one T2 reader,
   `derive_command`"*. True of READERS. By REQUIREMENT, CHA is drawn by the most verb resolvers of the
   nine (9) and by 5 subsystems; the thinnest is **BON** (§7.1). Different questions, both true.
2. **On Recall.** The template: *"by ID-13 it is not a candidate for the tenth unless Jordan gives it a
   reader"*. Agreed, with one addition. The natural reader is `train`, which the template classes
   *"a writer, not a reader"* (its row 51). A writer's increment can read an aptitude as effect size,
   but V-2 forbids it on a row without `contests:`. So giving Recall a reader is not only naming one:
   it needs V-2b (§7.3).
3. **On FOC as a combat-only merge candidate.** The template's §A.4.1 says *"STR, AGI, FOC and TMP
   co-occur only in `fight`/`accept`"*. That holds at the verb-READ level. By requirement, FOC is
   drawn by 10 practice domains and 5 subsystems (§7.1), so it is not a combat-only quantity. STR, AGI
   and TMP remain combat-centred.

**Falsifiers.**

- **For §1.** The command under §1 must print, for every aptitude, the PRA, verb and subsystem counts
  that §1's columns 3–5 give. If any differs, §1 is wrong. Run in this pass: see the receipt.
- **For §7.3's BON-into-ATT candidacy.** If a re-reading of §3 finds a domain drawing BON that draws no
  ATT-cluster aptitude, the subset claim fails.
- **For the Retention recommendation.** If `train` is given a `contests:` cell, or Jordan rules that
  V-2 does not bind writers, V-2b is moot and Retention has a reader. If Jordan rules learning speed
  is a property of the practice, not the person, Retention has none, and the tenth falls to §7.3's
  next row.
