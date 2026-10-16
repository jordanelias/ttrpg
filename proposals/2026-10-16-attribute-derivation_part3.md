# Attribute derivation — part 3 (SECONDARY): §6 the one grouping, §7 what should be an attribute (layer 1 only), §8 meta-rule, §9 NERS, §10 limits, §11–§12 the critic reconciliations

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. **Secondary to the head's §1.** It recommends; J-T1 (stored or derived) and J-T2 (the tenth) stay Jordan's.
## Parts, in reading order: [head](2026-10-16-attribute-derivation.md) (words, §1 the stack, the command) · [`_part2`](2026-10-16-attribute-derivation_part2.md) (§2–§5, the evidence) · **this file** (§6–§12).

Every count here is the head's command's output (head §1.7) or a re-cut of the same parse, and the
totals are the head's: 46 terms; 355 draw entries over 19 domains, 34 graded verbs and 16 subsystems;
171 term-statements (79 named, 12 overridden, 80 inferred); a stack of 14 base inputs, 41 derived
scores, 58 learned-skill rows and 64 sourced uses.

---

## 6. THE ONE GROUPING

### 6.1 The rule

**There is one grouping, and it is the stack's bottom layer: each term goes to the base input it
hangs off** (head §1.5, *group*). It replaces the first pass's sixteen clusters (K1–K16), and the word
study's twelve classes and ten families, which assigned the same rows three different ways.

- A **BASE INPUT** term goes to that input (`observation` → ACU).
- A **DERIVED SCORE**, **USE OF A DERIVED SCORE** or **LIMIT** term goes to the input with the
  largest weight in the score's formula: `concentration` → FOC (3·FOC + 2·WIL); `stamina` → END
  (3·END + 2·WIL); `reflexes` → AGI (REFLEX_AGI 2.0 against REFLEX_ATT 1.0, `config.py:122`);
  `anticipation` → ACU (2·Cog + Att); the three Command uses → CHA (2·Cha + Cog).
- **Ties** go to the input the source rules on or names first: `balance` → AGI (½Agi + ½Str, and
  *"GOVERNED BY AGILITY"*, `combat_systems.py:185`); `judgment` → CHA (*"Charisma/Cognition"*,
  governance_play_redesign_v1:64).
- A **LEARNED SKILL** term goes to the input the skill enters on (`land-sense` → ACU, Seasons Reader),
  else to *practice*. A **TEMPERAMENT** term goes to TMP.
- **Two placements are this proposal's reading, not a formula:** `judgment`'s tie, and `patience`
  as a lean (no source names it at all).

| group | terms | PRA domains | verbs [resolvers] | subsystems | draw entries | statements named / overridden / inferred | roles over all draws |
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
| RES | self-coherence | 1 | 6 [1] | 3 | 10 | 3 / 0 / 0 | difficulty/cost 10 |
| TMP | boldness, patience | 6 | 3 [2] | 5 | 14 | 1 / 0 / 5 | odds 11, effect size 3 |
| practice | deception, discipline, intimidation, numeracy, planning, precision, quick-thinking, verbal-fluency | 7 | 9 [9] | 6 | 28 | 0 / 0 / 15 | odds 19, effect size 9 |

Statements are the distinct keys of the group's terms at best basis, so a statement two terms of one
group share counts once. **Roles carry no magnitude** (head, Words): STR's four odds draws and its
four cost draws are the bout's bind term and a labelled noise term in Health, not four capacities.

### 6.2 Cross-tabs

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
| RES |   |   |   |   | ● |   |   |   |   |   |   |   |   |   |   |   |   |   |   | 1 |
| TMP |   |   | ● |   |   |   | ○ |   | ○ |   | ○ |   | ○ |   |   |   | ○ |   |   | 6 |
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
| RES | ● |   |   |   | ● |   |   |   | ● |   |   |   |   |   |   |   | 3 |
| TMP | ● |   |   | ○ |   | ○ |   | ○ |   | ○ |   |   |   |   |   |   | 5 |
| practice |   |   | ○ | ○ |   | ○ |   | ○ |   |   | ○ |   |   |   |   | ○ | 6 |

S14's ACU cell is blank because the Miraculous Event's Cognition check is coded to `steadfastness`,
which is in the WIL group; the ACU reading of that check is U19 in the head and S-defect 4 below.

### 6.3 Driven by acts, by learned skills, or by sustained play

The same rule as the first pass, on distinct verb resolvers (the seven thread rows count once):
**sustained play** if subsystems exceed both other counts; **learned skills** if domains exceed both by
at least 2; **acts** if resolvers exceed both; otherwise **even**.

| driven by | groups (PRA / verb resolvers / subsystems) | reading |
|---|---|---|
| **learned skills** | ACU (13 / 10 / 9), FOC (8 / 5 / 5) | drawn under many practices. ⚠ FOC's lead is mostly inference: 6 of its 8 domains reach it by inferred draws only (§6.2) |
| **sustained play** | END (4 / 5 / 7), WIL (3 / 5 / 7), ATT (6 / 6 / 8), TS (4 / 4 / 6), RES (1 / 1 / 3) | requirements the subsystems call for that few single acts carry: the march, the thread, belief under shock, the reading of a room |
| **acts** | practice (7 / 9 / 6) | what single acts ask for, every draw inferred |
| even | STR (3 / 2 / 2), AGI (5 / 5 / 4), CHA (7 / 9 / 9), BON (2 / 2 / 2), REC (6 / 4 / 6), TMP (6 / 2 / 5) | — |

### 6.4 What each group moves

From §6.1's role column. **END is mostly cost** (18 of 27 draws: wounds, fatigue, exposure). **AGI
is odds and effect size**; its effect-size draws are all `dexterity`'s, inferred. **STR is the one
group spread over odds, cost and effect size** in code (D03, D07–D10), so the first pass's *"all
effect size"* was wrong. **FOC is cost and eligibility** (the tracker, the defence, the operations
cap). **WIL is odds, then eligibility** (the thread pool, the fatigue threshold, the Inspiration cap).
**ACU, CHA and ATT are mostly odds**: in a contest-shaped game they are what makes a pool bigger.
**RES is cost alone**, and dark.

---

## 7. WHAT SHOULD BE AN ATTRIBUTE (secondary; answered from layer 1 only)

### 7.1 The rule, and the count per base input

**By J-13, applied uniformly (head, Words), only a base input can be an attribute.** A derived score,
a use of one, a limit, a lean and a learned skill are not candidates, whatever their draws. So the
question becomes: **which base inputs do the derived scores, the learned skills and the sourced uses
require?** Each count below is of distinct source statements, from the head's stack tables, never of
items at the domain, verb or subsystem level.

| base input | distinct derived scores (named / overridden) | distinct learned skills (named / overridden / inferred / retired) | distinct sourced uses (named / overridden / inferred) | best tier with a per-person value | derivable from another input? | N cut test (§9) |
|---|---|---|---|---|---|---|
| STR | 5 (5 / 0) | 1 (1 / 0 / 0 / 0) | 0 | T2 | no: an independent term in D03, D07–D10 | holds, narrowed to combat |
| AGI | 5 (5 / 0) | 6 (5 / 0 / 1 / 0) | 3 (3 / 0 / 0) | T2 | no | holds, narrowed: combat, plus three world uses at T4 |
| END | 4 (4 / 0) | 2 (2 / 0 / 0 / 0) | 4 (4 / 0 / 0) | T2; BODY stands in at T1 | no | holds |
| FOC | 5 (4 / 1) | 3 (0 / 0 / 1 / 2) | 0 | T2 | no; derived_stats_v30:267 keeps it apart from Spirit | holds, through derived scores alone |
| ACU | 5 (5 / 0) | 13 (9 / 1 / 3 / 0) | 15 (11 / 3 / 1) | T2 | no | holds, conditional on the Cognition alias |
| WIL | 8 (8 / 0) | 6 (6 / 0 / 0 / 0) | 12 (12 / 0 / 0) | T2 | no | holds |
| ATT | 5 (4 / 1) | 15 (10 / 5 / 0 / 0) | 9 (7 / 2 / 0) | T2 | no | holds |
| CHA | 5 (3 / 2) | 4 (2 / 2 / 0 / 0) | 11 (8 / 2 / 1) | T2 (through Command and Face) | no | narrowed at T2, holds at T4 |
| BON | 1 (1 / 0) | 0 | 3 (3 / 0 / 0) | T2 | no | narrowed: the knot gate also needs Disposition |
| REC | 5 (4 / 1), all T4 | 10 (4 / 6 / 0 / 0) | 3 (1 / 2 / 0) | T4 | not by any formula; the designs give it its own column | **false today** |
| TS | 2 (2 / 0) | 2 (2 / 0 / 0 / 0) | 5 (5 / 0 / 0) | T2 (a T3 gate) | no; but a growing Track | holds, as its own field |
| RES | 1 (1 / 0), dark | 0 | 2 (0 / 0 / 2) | T2, dark | canon names Spirit: *"how resilient their spirit is"* (operations.py:144) | **false today** |
| BODY | 1 (1 / 0) | 0 | 0 | **T1** | — (a state) | holds at T1, as a state |
| TMP | 1 (1 / 0) | 0 | 0 | T2 | — (a lean) | holds, narrowed to combat |

**Named against inferred.** Every derived score is source-written by definition (head, Words); the
inferred share lives in the terms, and §6.1 gives it per group. **Where the named support sits:** WIL
16 named statements and ACU 15 lead; TS 9, CHA 7, REC 7, END 6, ATT 4, AGI 3, FOC 3, BON 3, RES 3,
STR 1, TMP 1. *practice* has none.

### 7.2 One by one

- **The nine are each required.** Every one feeds at least one source-written derived score at T2
  (STR: D03, D07–D10; AGI: D01–D05; END: D10, D11; FOC: D14–D16; ACU: D04, D06, D18; WIL: D10, D11,
  D14, D32; ATT: D02, D04–D06; CHA: D18, D22; BON: D36), and none is computed from another in any
  formula. That is the support for keeping the nine the first pass never stated: **once derived scores
  are counted, every named requirement in the corpus reaches one of the nine, Recall or TS** (head
  §1.6); the first pass's twelve "homeless" named draws all reduce to the nine.
- **WIL** carries the most derived scores (8) and the most named statements (16): the thread pool,
  the knot roll, the fatigue threshold, the Inspiration cap, and five belief-under-shock checks.
- **ACU** carries the most uses (15) and, with ATT, the most learned skills (13 and 15). ⚠ Much of it
  reaches ACU only through the *Cognition* alias the registry marks *"[ASSUMPTION] … Jordan veto"*
  (`descriptor_registry.yaml:42`).
- **ATT** carries 15 learned skills, five of them Appraise bonuses overridden by the kernel.
- **CHA**: at T2 its only readers are Command (2:1 with ACU) and Face (outcome-inert). Cut CHA and
  `derive_command` still runs on Cognition; what dies is the 2:1 weighting and Face's ceiling. At T4 it
  has 8 named uses (Impress, Rumour, Converse, the cover identity, Pacify, Keep Order by Consent,
  Address the population, Hold Court). **Narrowed at T2, holds at T4.**
- **END** reaches T1 only through BODY (D13). The END attribute a person would carry is, on the
  season path, the class default 4 minus body bands.
- **FOC has no sourced use.** Every Focus requirement is through a derived score (D14–D16, D20, D31).
  Its two Histories skills are retired rules (L32, L33). It stays distinct from WIL by the source's
  own statement: *"Spirit 6 / Focus 2 … endurance without skill … Spirit 2 / Focus 6 … skill without
  staying power"* (`derived_stats_v30.md:267`).
- **AGI** is combat at T2 and three world uses at T4 (U01–U03); the first pass's *"all combat at T2"*
  missed the uses. Dexterity reaches it by alias only.
- **STR** has no sourced use and one learned skill; its five derived scores are all in the bout.
- **BON** is the narrowest of the nine: one derived score (the knot cap), three uses, no skill. The
  knot gate also needs Disposition (`knots.py:189-193`), a relational state.

### 7.3 The tenth (ID-13 read honestly)

**No candidate for the tenth has a reader above T4.** By ID-13 none is a candidate until Jordan gives
it one, so **the tenth stays unnamed by evidence**, and J-T2 is Jordan's. The evidence for each:

| candidate | for | against | reading |
|---|---|---|---|
| **REC: Recall** | the broadest design footprint of the non-nine: 5 derived scores (D25, D37–D40), 10 learned skills (4 named), 3 uses; the designs give it its own column (FW:95, :306; SCV:155) and a Memory check (threadwork_v30:688) | **no code field** (`git grep -i recall -- '*.py'`); every derived score T4; 2 of its 3 uses and 6 of its 10 skills overridden; **two contrary sources**: *"It is evidence for D2, not a candidate for it"* (`10_verbs_and_attributes.md:152-156`), and the 2026-08-15 proposal calls Recall's *"triple-gate (breadth + depth + learning rate)"* *"a mandatory tax stat"* and rules *"capacities govern breadth, never depth"* (AUG:202-205). The first pass's recommended Recall bundled exactly that triple gate (D38, D39, D40) plus memory | the strongest design case, and a false N-line today. Its natural reader, `train`, is barred by V-2 (`2026-10-16-character-template_part2.md:179`); see the question in §8 |
| **TS** | 2 derived scores and 5 uses, at T2 and a T3 gate | 0–100, not 1–7 (registry :64); a Track that grows by exposure (derived_stats_v30:578; HIST:127, :324; FW:254) | **its own field** (J-T1a), not the tenth |
| **RES: resilience** | a stub slot exists (operations.py:142-147) and the plan names *"'spirit' (resilience, R-14)"* a candidate input (v9 _part5.md:444) | its one derived score is the identity at gain 0; its two uses map to it only by inference; canon defines it as *"how resilient their spirit is"* (operations.py:144) | **not the tenth**: what fills the slot is Spirit by canon's own words, a choice of filler, not a new input |
| **a split of WIL or FOC** | WIL carries eight derived scores and five kinds of check | J-13: a base input is not split by its uses; no source writes two inputs inside either; the one source that separates them separates WIL **from** FOC (derived_stats_v30:267), which argues against merging, not for splitting | **not a candidate** |

**Recommendation on the tenth: none, by evidence.** The first pass recommended Recall while conceding
it had no reader above T4 and a false N-line; that was the producer's preference, not the evidence's.

### 7.4 Leave as practice, or cut

- **Leave as practice:** every P-domain; every LEARNED SKILL term (`numeracy`, `verbal-fluency`,
  `precision`, `deception`, `planning`, `intimidation`, `quick-thinking`, `discipline`, `land-sense`).
  `precision`'s one source is craft practice (HIST:241); *Precision Hands* is a perceptual examination
  (+1D examining crafted objects, HIST:350), so it is not evidence for precision at all. `deception`
  and `intimidation` meet sources only as skills on the contest's Obscuring move (HIST:339, :349).
  `numeracy` is practice because no source names it as a person's input and ledger work sits under
  administrative practice (AUG:147, :170), not because of its coinage.
- **Leave as derived scores** (never stored, by J-13): every DERIVED SCORE, USE and LIMIT term.
- **Cut from the nine: nothing.** BON and STR are nearest the line (§7.2).

### 7.5 THE RECOMMENDATION (secondary; a judgment; Jordan's under J-T1 and J-T2)

**Keep the registry's nine: STR · AGI · END · FOC · ACU · WIL · ATT · CHA · BON. Leave the tenth
unnamed: no candidate has a reader above T4.** Within the nine:

- **WIL's definition names what the sources roll on Spirit**: the thread, the knot, belief under shock
  (`steadfastness`), the Inspiration cap (`devotion`), and the Sincerity Check (FW:430; ED-503 at
  FW:822), with the registry's *Sincerity* alias on Bonds flagged (S-defect 2).
- **RES's slot is filled from WIL**, if it is ever lit (§7.3).
- **ATT's definition takes discernment** (FW:94, *"calibrating trust"*); AX-7's reader input stays
  J-T9's.

**Confidence.**

- **Medium** that WIL, ACU, ATT and END are each required and distinct: each feeds several T2 derived
  scores and has named uses.
- **Medium** for AGI, STR and FOC: required by T2 derived scores, almost all in the bout; FOC and STR
  have no sourced use.
- **Low to medium** for CHA (T2 only through a 2:1 weighting and an inert view) and BON (one derived
  score).
- **Low** that the tenth should be any of the four candidates.

**This is close to the 2026-08-15 proposal's option A-2, *"Ratify the 10 unchanged"*** (AUG:192, read
in the first pass, not re-opened here), with the tenth left open rather than filled.

**Read under the template's two options.**

- **Option B (stored: the attributes on `Person.attributes`).** Each base input is stored; every
  derived score is computed where it is read. As V-2 stands, an attribute reaches only rows declaring
  `contests:`: four shipped (`fight`, `accept`, `march`, `tell`) and four sigma-routed (`determine`,
  `argue`, `arrest`, `interrogate`). The thread operations, the knot, the inquiry acts, `train` and the
  open effect cells cannot read one. The Spirit checks of belief under shock sit outside any verb row.
- **Option A (derived: nothing attribute-shaped is stored).** Every requirement is carried inside the
  practice keys of the domains that draw it. The cost is one copy per domain for a base input drawn by
  many: ACU (13 domains), FOC (8, 6 inferred-only), ATT (6), REC (6), CHA (7). Two ladders for one
  quantity is the S defect `CLAUDE.md` §0.06 names. Recall's learning rate and WIL's belief checks
  have no practice key to live in.
- **The evidence narrows J-T1 without deciding it.** B fits the base inputs many domains draw; A fits
  the narrow ones (STR, BON, TMP). **Judgment call.**

---

## 8. WHAT IT ADDS AND CUTS (the meta-rule, relative to the registry's nine)

| | object | removes or adds something that exists? |
|---|---|---|
| **adds** | nothing to the roster: the tenth stays unnamed (§7.3) | no |
| **asks** | **a question, not an amendment:** if Jordan wants Recall to have a reader, would a writer's increment (`train`) be allowed to read an attribute? V-2 says no (`10_verbs_and_attributes.md:198`); the first pass called the yes-answer *V-2b*. It is raised for Jordan and drafted into no rule file | no |
| **widens** | WIL's definition (belief under shock, the Inspiration cap, the Sincerity Check); ATT's (discernment) | no new slot |
| **fills** | RES's existing stub slot from WIL, if it is ever lit | changes what fills a slot that exists (operations.py:142-147); removes no attribute, because RES is on no roster |
| **declines** | REC, TS and RES for the tenth; every derived score, use, limit, lean and skill as an attribute (J-13) | no: none is on the roster |
| **flags** | BON and STR as the narrowest of the nine; CHA as narrowed at T2 | no: nothing is cut |

**Net effect on the roster: zero new slots, zero removals.** This proposal edits no code, no registry
and no ledger, allocates no ID, and touches five files under `proposals/`.

---

## 9. NERS, IN BRIEF (`skills/ners/SKILL.md`)

`[SELF-AUTHORED — bias risk]`. Grade: **paper**. No outcome was measured.

**N: cut each base input and name what dies** (head §1.2–§1.4). A line that holds in one direction
only is narrowed; a line whose producer moves no outcome is false (the skill's disqualifier 2).

| cut | what dies | direction | verdict |
|---|---|---|---|
| STR | Impact (D07), the handling penalty (D08), the bind and wind term (D09), half of Balance (D03); Health's STR term is labelled noise (combatant.py:21) | bottom-up (person → bout) | **holds, narrowed to combat** |
| AGI | Tempo, Reflex, Balance, initiative, the counter (D01–D05); three T4 world uses (U01–U03) | bottom-up, lateral (person → world) | **holds, narrowed** |
| END | Durability and the Stamina reserve (D10, D11), Take a Breath (D12), the Dissolution Ob (D35); four T4 uses | bottom-up, lateral (person vs thread) | **holds** |
| FOC | the Concentration tracker, disruption, poise (D14–D16); the operations cap (D31); the Focus defence (D20, overridden) | bottom-up, horizontal (bout, thread, contest) | **holds**, through derived scores alone |
| ACU | Reading's 2:1 term (D06), Command's secondary term (D18), Cover (D28), the Impress Ob (D27); 11 named T4 uses | vertical (field → command), horizontal | **holds**, conditional on the Cognition alias |
| WIL | the thread pool, the knot roll, the fatigue threshold, the Inspiration cap, the spark check, part of Stamina and Concentration; 12 named uses | bottom-up, top-down (faction layer and world → person) | **holds** |
| ATT | Reflex and Reading's minor terms (D02, D06); 7 named T4 uses; 10 named skills | lateral (person vs person) | **holds** |
| CHA | at T2, Command's 2:1 weighting and Face's ceiling (Command still runs on ACU; Face moves nothing); at T4, 8 named uses | top-down (commander → field) | **narrowed at T2**, holds at T4 |
| BON | the knot cap and the ≥ 5 gate (D36, U51); Connect, the Anchoring Scene | lateral | **narrowed**: the gate also needs Disposition (knots.py:189-193) |
| REC | nothing at T1–T3. Its derived scores and uses are T4 | vertical (practice → growth) | **FALSE N-LINE TODAY** |
| TS | the thread pool's TPS term, the knot and depth gates | bottom-up | **holds**, as its own field |
| RES | D34, the identity at gain 0 | bottom-up | **FALSE TODAY** |
| BODY | `end` on the season path (D13), so every per-person difference in the loop's fight | bottom-up | **holds at T1**, as a state |
| TMP | the aggression lean (D17) | bottom-up | **holds, narrowed to combat**; a lean |

**S: six "two ladders for one quantity" defects** (`CLAUDE.md` §0.06, *"calculations consistent in
methodology"*). None is repaired here; each is named for whoever defines the attribute.

1. **Steadiness under strain.** Focus carries it in the combat tracker (combatant.py:147) and the
   contest's Focus defence (SCV:199); Charisma carries it as *Composure* (Charisma × 3,
   derived_stats_v30:554; Cha + 6, FW:640), retired as the contest tracker only (SCV:242), still
   charged by threadwork (threadwork_v30:177), and named in the monster-hex *"Composure check"*
   (valoria_ui_ux_v4_1:916).
2. **Sincerity.** The registry aliases it to Bonds (`descriptor_registry.yaml:48`); the fieldwork
   Sincerity Check rolls Spirit (FW:430), and ED-503 assigns the Sincerity Gate to Spirit (FW:822).
3. **Initiative.** The stub's initiative emphasis reads Agility, Reading and History
   (`combat_systems.py:1416-1421`); the designs roll initiative by Attunement (FW:106;
   `combat_c4_draft_v0.md:127`, not opened); the Combat Reflexes skill breaks Attunement ties by Agility
   (HIST:463).
4. **Holding one's framework under shock.** Five statements roll Spirit (npc_behavior_v30:1054;
   faction_politics_v30:741, :752; conviction_track_v1.md:95; southernmost_v30:105); the Miraculous
   Event's witness rolls Cognition vs Truth (miraculous_event_v30.md:132).
5. **Perceiving the thread.** TS gates and feeds the pool (operations.py:244; FW:84); thread-aware
   exploration rolls Attunement (FW:91), and five Histories skills add Attunement dice to perceive
   Thread phenomena (HIST:105, :121, :280, :362, :450); for the Leap itself Attunement was struck
   (threadwork_v30:163).
6. **Concentration's formula.** `3·Focus + 2·Spirit` everywhere live (combatant.py:147;
   derived_stats_v30:159; SCV:267), but the Trained Memory skill still names *"Concentration (Focus +
   Recall)"* (HIST:217), a formula derived_stats_v30:166 removed.

**E, scored last, as a ratio against N and R.** The stack is the legible form: fourteen inputs, each
with its scores beneath it, and a player predicting an outcome reads one input and the formula that
uses it. What it costs is two widened definitions (WIL, ATT) and the acknowledgment that four of the
fourteen inputs (REC, RES, BODY, TMP) are not attributes.

---

## 10. LIMITS, DISAGREEMENTS AND WHAT COULD NOT BE SOURCED

**Method limits.**

- **No subagent was spawned in any pass** (head, Method). The interrogations, the classification and
  the grouping are one producer's. An independent Opus critic read the first two passes (§11, §12);
  nobody has re-derived this pass's classification.
- **Not opened** (cited by grep line, or carried from an earlier pass): `combat_c4_draft_v0.md:127`;
  AUG:192 (option A-2); `sigma.py:82-129`; `world_q.py:778-790`; `person_q.py:468-469`;
  `verb_table.yaml` rows; `fixtures.py:251`, `:381`, `:542-544`; the lane files under
  `research/by_lane/` beyond the §8 row heads; the bodies of `npc_behavior_system_v1.md`,
  `military_layer_v30.md`, `settlement_layer_v30.md` and `governance_play_redesign_v1.md` beyond the
  lines cited; `knots_v30.md:250`.
- **Not settled by reading:** what HIST's § mark means (the file does not define it); whether
  *"Intellect"* (npc_behavior_v30:350) means Cognition; what input a *"Coherence check"* or a
  *"Composure check"* reads (U62–U64).
- **The Histories sweep** found skills whose effect names an input, a pool or a derived score. A
  skill that names none is not in §1.3; a skill whose name is written in a form the pattern misses
  could be absent.

**Where this proposal disagrees with the character template, with evidence.**

1. **On "Charisma is the thinnest".** True of READERS at T2, and this pass agrees it is narrowed there.
   By named T4 uses (8) and derived scores (5), CHA is not the narrowest; BON is.
2. **On Recall.** Agreed: by ID-13 it is not a candidate unless Jordan gives it a reader, and this pass
   now says so in its recommendation.
3. **On FOC as a combat-only merge candidate.** At the verb-READ level, yes. In the stack FOC feeds a
   threadwork derived score (D31) and a contest one (D20, overridden), and derived_stats_v30:267 keeps
   it apart from WIL.

**Falsifiers.**

- **For the head's §1.5–§1.7.** The command must print §1.5 row for row and the quoted block line for
  line. Run in this pass: the quoted block diffed clean against a fresh run, and a parse of §1.5's 46
  rows matched the command's 46 lines in count and order.
- **For §6.1's grouping.** A term whose derived score's largest weight is on another input, or a
  Histories skill entering on a different input than its row says, moves a term between groups.
- **For §7.2's "every named requirement reaches a base input".** One named statement that reads none
  of the fourteen inputs and is not a learned skill would break it. The *practice* row has none
  (§6.1).
- **For §7.3.** If code gains a Recall field that an outcome reads, or Jordan rules that V-2 does not
  bind writers, Recall gains a reader and the table's verdict for it changes.

---

## 11. CRITIC RECONCILIATION (first pass)

Kept as the record of the first reconciliation. ⚠ **Its counts and locations are that pass's:** §2–§3
have since moved to `_part2`, every count is superseded by the head's §1.7, and several of its
choices (Command's draws NAMED T2; Agility, Cognition and Spirit split into separate terms as
candidate attributes) are reversed by §12.

| finding | applied / rebutted / narrowed | where (as of the first reconciliation) |
|---|---|---|
| **1. Combat Concentration omitted** | **applied, then narrowed on the count.** P03, #18, #20 and S01 draw `concentration` (T2). `composure` is merged into it. FOC's *"two jobs"* is retracted | head §1, §3 P03; `_part2` #18, #20, S01 |
| **2. "Overridden … almost always the 2026-09-05 ruling" is false** | **applied.** Every overridden draw names its cause; the gloss is contestable | head tiers, §3 note 1 |
| **3. Command's Cognition term is glossed** | **applied** as a new term `tactical-read`, NAMED T2 (reversed in §12, finding 4) | head §3 P04; `_part2` #22, S02 |
| **4. A Spirit aptitude named in sources is absent** | **applied.** `steadfastness` and `devotion` added; `will` at #51; *"WIL narrowed to the substrate"* retracted | head §1; `_part2` S04, S07, S09, S10 |
| **5. Some "named T4" draws rest on practice skills or flavour** | **applied.** P18 INFERRED; `discipline` withdrawn at P05, S05, S02 | head §3 P05, P18; `_part2` S02, S05 |
| **6. One source cell counted as two aptitudes** | **applied.** SCV:147 is one draw; FW:306 is one draw | head §3 P02, P07; `_part2` #41, S03 |
| **7. Inferred draws a source contradicts** | **applied.** #52 to `reasoning`; `composure` and `courage` removed where a source names Cover or Command; empathy re-based on the Lattice gate | head §3 P04, P06, P08, P16; `_part2` #37, #52, S02, S04 |
| **8. Verbs graded on a shared word** | **applied.** #34 `survey` is *book*; #24 INFERRED | `_part2` #24, #34 |
| **9. Internal inconsistencies** | **applied, except FW:620, narrowed** (the cause differs by item) | head §3 note 1; `_part2` #36, #52, S04 |
| **10. Rank inflated by re-counted inference** | **applied** with reason keys and an order by source-stated draws (reworked in §12, finding 2) | head §1 |
| **11. Fine grain** | **applied, except Affability, rebutted** | head §1 |
| **12. Word choice** | **applied for Retention, narrowed for "aptitude"** (reworked in §12) | head, Words |
| **13. J-13 half read** | **applied** (read further in §12, finding 1) | head §3 note 3 |
| **14. Locators** | **applied** | evidence tables |

---

## 12. CRITIC RECONCILIATION (OPUS, SECOND PASS)

The Opus critic read the four derivation files and the word study after the first reconciliation. Its
verdict: the arithmetic held; two structural defects (derived scores listed as aptitudes; an order key
that re-counted named evidence); the word study contradicted its sources in places; the recommended
nine survive. Every locator below was re-opened before the edit it supports. Jordan's instruction of
2026-10-16, *"Learned skills and derived scores etc all need to be folded in to this"*, is applied
through finding 1.

| finding | applied / rebutted / narrowed | where |
|---|---|---|
| **1. Derived scores presented as atomic aptitudes; J-13 read too narrowly; omitted derived scores and learned-skill layers** | **applied.** The flat list is now a four-layer stack. 41 derived scores, each re-opened, including every one the critic named as omitted (handling penalty D08, counter D05, resolution pool D19, Take a Breath D12, strain modifier D21, kernel trackers D23, Cover D28, effective Recall D37). 58 learned-skill rows, including Instruments, School and Techniques (L07–L09), the Investment and Record slots (L58), Combatant skills (L06), Histories levels and sparking (L10), tactic cards (L09) and a sweep of every Histories skill that names its input. J-13 is the controlling split rule, applied uniformly: Agility is not split by derived score, Command not by use, and Balance follows Jordan's *"NOT a stat"* (combat_systems.py:185). Each of the 46 is classified as one of six classes | head Words, §1.1–§1.6; `_part2` §3 note 3 |
| **2. The order key re-counts one named statement at several levels; "not re-counted" is false** | **applied.** A key is one source statement; §1.5 counts distinct statements per term at best basis and orders by **named statements only**; overridden statements are shown and not weighted; draw entries are shown and called re-counts. The first pass's claim that the ACT column is not re-counted against DOMAIN is retracted in `_part2` §4. Totals recomputed and the printed command rewritten; its output is quoted and was diffed against a fresh run. The new top is `reasoning` (10 named), not the seven thread rows | head §1.5, §1.7; `_part2` §4 |
| **3. The twelve named "homeless" draws reduce to the nine** | **applied.** `judgment` is Hold Court, CHA or ACU (U15; its §1 mapping now follows its own P09 cell); `anticipation` is Reading (D06) with its feint draws as uses of Command; `situational-awareness` is Command (D18). The head now says every named requirement reaches a base input | head §1.5, §1.6; §7.2 |
| **4. Command-derived draws coded NAMED T2 against the head's own rule; a docstring treated as mechanism** | **applied.** As terms, `leadership`, `tactical-read`, `situational-awareness` and `anticipation`'s feint draws are INFERRED; Command itself is NAMED T2 at D18. *"Tactical read"* (exchange.py:60) is called a docstring gloss, and the span is cited to MB:309 and units.py:2700-2722, not the engine.py:93 comment | `_part2` P04, #22, S02; head Words, D18 |
| **5. The Recall recommendation ignores contrary sources; FW:95 coded two ways; overridden draws weighted as named** | **applied.** Both contrary sources are quoted (10_verbs_and_attributes.md:152-156; AUG:202-205), and the recommendation is restated per ID-13: no candidate has a reader above T4, and the tenth stays unnamed by evidence. `[fw-research]` is overridden everywhere; the Histories Recall skills are a separate key. HIST:36 is now D37 and an S16 draw. **Rebutted in part:** the +2D citation bonus is binary (*"Binary"*, SCV:177) and reads no person's Recall, so it is not coded as support | §7.3, §7.5; `_part2` P13, S16 |
| **6. "Force is all effect size" contradicted** | **applied.** `strength` carries odds, cost and effect size (Impact, handling, bind and wind, half of Balance); the Health term is cited as the noise term the code labels it (combatant.py:21) | `_part2` P03, #18, #20, S01; head D07–D10; §6.4 |
| **7. Pattern-matching on the word: Precision, Deception** | **applied.** `precision` is re-justified from what the source does (craft quality sits in the practice, HIST:241); *Precision Hands* is a perceptual examination and is an ACU learned skill (L49). `deception`'s skills are *Smooth Liar* and *Intimidation* on the Obscuring move (L45, L46). The *practice-named* flag is dropped | `_part2` P01, P08, P11, #13; head §1.3, §1.5 |
| **8. Named draws never coded** | **applied, each:** the monster-hex Composure check (valoria_ui_ux_v4_1:916, S01; *"courage is gone"* narrowed); Attunement for sensing the thread (FW:91 at P15 and S04; HIST:105 as L16; HIST:362 as L21 and in P05's `[hist-thread-att]`), with the Leap's struck Attunement noted (threadwork_v30:163); southernmost_v30:103 at S09 (*"AGI … all combat at T2"* corrected), and the sweep found southernmost_v30:123 too; npc_behavior_v30:350, :352 at S11; threadwork_v30:688 at S05; SCV:155's Appraise Ob (P02, #50, S03) and FW:411's Impress Ob (P16, S04) as *resists another* | `_part2` §3, §4, §5; head §1.4 |
| **9. "T1 is 0" overstated** | **applied.** T1 is defined as loop-run code on a per-person value; the season loop's BODY-derived `end` (seam/wrappers/combat.py:130-138) makes `stamina` and `toughness` NAMED T1; BODY is a base input (B13) and `end` a derived score (D13) | head tiers, B13, D13; `_part2` P03, #18, #20, S01 |
| **10. "The kernel binds only faculty" overstated** | **applied.** It binds `faculty` and `charisma`; `charisma` sets only Face's outcome-inert ceiling (resolver.py:184-195, :226-236) | head tiers; `_part2` S03 note |
| **11. Discernment as a T3 statement overstated** | **applied.** AX-7's *"competence"* may be practice; every `[ax7]` draw is INFERRED | `_part2` #8, #35, S10 |
| **12. Draws are not commensurable; roles carry no magnitude; Mentor coded as learning; the gloss extended beyond note 1** | **applied** for the weighting (distinct statements, named only), roles (stated to carry no magnitude) and Mentor (now L56, a held bonus die; the S07 `learning` draw is removed). **Narrowed** for the gloss: note 1 now states that it reads the gloss as about the inquiry acts' dice in any design, so it reaches investigation_systems_v30:243 explicitly, and remains contestable | head Words; `_part2` §3 note 1, S07 |
| **13. Missing subsystems** | **applied.** S11 espionage and intelligence, S12 medicine, S13 diplomacy and treaties, S14 religion and the Truth track, S15 information and perception gates, S16 progression and advancement, each in the fixed template. They surfaced S-defect 4 (Cognition vs Spirit) and that faction Intel, Spy, Diplomacy and Treat roll faction stats, not a person's | `_part2` §5 |
| **Word study: Devotion and Sincerity in Bonds** | **applied.** Both are in the WIL group (Spirit × 1, derived_stats_v30:557; FW:822; FW:430); the registry's Sincerity alias is S-defect 2 | `_equivalences` §1, §2 |
| **Word study: §3.2 mapping errors** | **applied.** Contact endurance → WIL; inference → REC; judgment → CHA or ACU; anticipation → ACU (Reading, Cognition-primary); tactical read → a use of Command | `_equivalences` §3 |
| **Word study: Concentration ≈ Will** | **applied.** 3F + 2S is a blend of two inputs, and derived_stats_v30:267 separates Spirit from Focus; Concentration is in the FOC group, a derived score | `_equivalences` §2 |
| **Word study: the definition of D fails for Tactical read** | **applied.** Tactical read reads a field, not a person; it is a use of Command in the CHA group | `_equivalences` §2 |
| **Word study: Quickness and Reflexes "stay two"; the semantic test cannot observe its failure** | **applied.** They are two derived scores of one input. The word study now says plainly that groups whose members derive from one input are **identical by code**, and that the divergence test applies to base inputs and derived scores, not to words | `_equivalences` §3 |
| **Word study: six, not seven, typed as not a capacity** | **applied, and the column is replaced:** the type column is now the head's class; the count follows the classes (19 / 11 / 3 / 9 / 2 / 2) | `_equivalences` §1 |
| **Word study: Numeracy argued from its coinage** | **applied.** The argument is dropped; numeracy is practice because no source names it as a person's input (§7.4) | `_equivalences` §2; §7.4 |
| **Word study: upheld items** (Discipline, Deception, Intimidation not inputs; Boldness a lean; Breadth and Practice ceiling limits) | **agreed**, and kept as LEARNED SKILL, TEMPERAMENT and LIMIT | head §1.5 |
| **Word study: Leadership and Persuasiveness typed "cap/skl"** | **applied.** Leadership is a use of Command; Persuasiveness is a use of CHA (Converse, FW:409) | head §1.5; `_equivalences` §1 |
| **Word study: "equivalence class"; non-symmetric relations; the "Domain" column; three groupings** | **applied.** *Group* replaces *equivalence class*; relation labels are defined, with the non-symmetric ones marked; the column is renamed *faculty family*; the three groupings are one, §6.1's | `_equivalences` §0, §2; §6.1 |
| **Etymologies** | **applied.** Empathy: 1908 is attested, Titchener's 1909 use is the usual citation (medium); numeracy, 1959 (Crowther), high, the ‡ dropped; *learn* from PIE *\*leis-* (cognates *lore*, *last*), medium; *plan* low (French *plan* blends *planum* and Italian *pianta*); *discipulus* < *discere* is itself debated | `_equivalences` §1, §4 |
| **Rule compliance: ID-13 (Recall recommended without a reader)** | **applied** (finding 5) | §7.3 |
| **Rule compliance: the meta-rule's "cut of RES removes nothing that exists"** | **applied.** Reworded: RES is an existing stub slot; filling it from WIL changes its filler and removes no attribute | §8 |
| **Rule compliance: V-2b offered as a loosening** | **applied (softened).** It is now a question for Jordan, not a proposed amendment | §8 |
| **Rule compliance: the 2026-09-05 ruling's overridden draws weighted in full** | **applied** (finding 2) | head §1.5 |
| **Rule compliance: "aptitude" has a third sense** | **applied.** The 46 are *requirement terms*, a phrase `git grep -i` finds nowhere; all three senses of "aptitude" are named (core.py:106-107; faction_politics_v30:541; 10_verbs_and_attributes.md:140, :199; AUG:1288); BASE INPUT, DERIVED SCORE and LEARNED SKILL are defined in the head | head Words |
| **NERS: CHA, ACU, STR and BON N-lines** | **applied.** CHA narrowed at T2 (Command runs on ACU alone; Face moves nothing); ACU holds without the docstring, through Reading and 11 named uses; STR's real lines are Impact, bind and wind, handling and half of Balance, with the Health term labelled noise; BON narrowed by Disposition. WIL, END, AGI and FOC hold, as the critic found | §9 |
| **Not checked by the critic** | **checked here:** the command now runs and its quoted output diffs clean; knots_v30:149, npc_relational_graph_v30:277, fieldwork_v30_infill:48, combat_reference_v1:598, FW:446-447, :477-483, units.py:2700-2712 and military_layer_v30:132-133 hold. **One locator corrected:** TS +1 at a Breach is FW:254, not :255. Still not checked: the lane files; combat_c4_draft_v0:127; sigma.py:82-129; world_q.py:778-790; person_q.py:468-469; verb_table rows; whether ED-IN-0185 Q7 says "10 attributes" verbatim | §10 |
