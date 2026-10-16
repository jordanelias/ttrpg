# Attributes from scratch — part 3: flatten and collate

## Status: PROPOSED

Continues `2026-10-16-attributes-from-scratch_part2.md`. Verb ids `V001`…`V179` are in part 1, §2.

---

## 5. Flatten and collate

### 5.1 Totals

| | count |
|---|---|
| verbs | 179 (code 45 rows · plan 18 · plan refused/cut 7 · lane rec 23 · designed here 86) |
| demand statements | 536 (root sense 171 · subsystem 208 · ordinary sense 110 · patient-side 47, on 36 contested verbs) |
| atomic demands after flattening | 67 |
| clusters | 27: 20 that measure a person's body, senses, mind, will or manner; 7 that measure something else (skills, values, holdings, credibility, situation) |
| demand instances falling in the 20 personal clusters | 355 of 536 (66%) |
| access draws falling in the 7 non-personal clusters | 108 of 129 (84%) |

**The plainest result here: the personal clusters move odds, cost and effect, and the holdings move
access.** Of the 129 demands that decide whether a person may (or will) attempt an act at all, 108 are
met by a seat, a rank, a claim, means, a following or a value, not by a capacity. Personal clusters
draw odds 158, effect 117, cost 59, access 21. Non-personal clusters draw access 108, effect 50, odds
21, cost 2. Most of the personal-cluster access draws are nerve (§5.3).

### 5.2 Flattening, and the merge log

Each demand phrase in §4 was written as an atomic phrase plus an optional gloss in parentheses.
Flattening strips the gloss. **Merges of exact synonyms happened when the §4 phrases were written**,
not afterwards, so the log below lists the root-sense wordings in §2 (column "what the root sense
implies") that were judged to be the same demand and given one atomic phrase. Wordings that were *not*
synonyms but were re-read as another kind of demand are logged separately: these are interpretations,
not merges.

**Exact-synonym merges (root-sense wording → atomic demand):**

| atomic demand | root-sense wordings merged into it (verb) |
|---|---|
| vigilance over time | "keep awake over" (surveil) · "watch over" (guard) · "keep watch over" (ward) · "attention that stays" (tend) |
| holding to a course over time | "stand against" (withstand) · "sit down before and outlast" (besiege) · "follow on without stopping" (pursue) · "follow through to the end" (execute) · "keep it shut" (lock) · "lay claim to redress" kept over time (avenge) |
| patient application | "go round again and again" (research) · "go round, missing nothing" (search) · "apply oneself with zeal" (study) · "turn round and round" (drill) · "draw along, again and again" (train) · "till and tend over seasons" (cultivate) |
| assembling meaning from parts | "pile together" (construe) · "build again" (reconstruct) · "make shine clear" (argue) · "undo a cipher" (decipher) · "interpret" (thread_read) |
| fine discrimination | "weigh" (examine) · "find the fault" (mend) |
| foresight and planning | "see ahead" (provision) · "lay a foundation" (found) · "make a thing stand" (establish) · "deliberate well" (counsel) · "clear the hindrances" (dispatch) |
| reckoning in numbers | "reckon out shares" (ration) · "assess" (tax) · "a count" (survey) |
| carrying voice and bearing | "cry out" (proclaim) · "proclaim" (ban, preach) · "put outward into circulation" (utter) · "make clear in public" (declare) · "show forces" (muster) |
| being liked | "make sweet" (persuade) · "attend at court" (court) |
| menace | "press on another" (threaten) |
| readiness to let go | "give away a debt" (forgive) · "give wholly" (pardon) · "let go a right" (waive) · "loose" (release) |
| hiding things | "cover wholly" (conceal) · "hide a store" (hoard) · "sneak goods past" (smuggle) |
| moving unseen | "be another's shade" (shadow) · "stand unseen under the eaves" (eavesdrop) · "put oneself in the wood" (ambush) |
| judgement of value | "set a price" (appraise) · "haggle" (bargain) · "barter" (exchange) |

**Re-readings: a bodily root sense read as a positional demand. These are not merges.** *bear
together* (confer), *come together* (convene), *bind* (oblige), *call back* (revoke), *make stay*
(arrest), *raise* (levy), *load* (charge), *set the boundary* (determine). Each root names a physical
act, and the act's present-day demand is a seat or a rank. They flatten to "a seat's remit" or "rank or
office that others recognize". §3.6 explains why. **These re-readings are the most consequential
judgement in this section.** Read the other way, they would put 40 verbs' worth of demand into a
"standing" attribute.

**What was NOT merged, and why:**

- *Quick bodily reaction* and *quick judgement* are kept apart: a fast body and a fast decision are
  different people.
- *Fluent speech* and *trained rhetoric*: a gift and a training.
- *Keeping one's word* and *being believed*: the first is a disposition the person has; the second is
  others' belief, which a liar can also enjoy.
- *Perceiving the threads* and *handling the threads*: a seer and a weaver.
- *Bearing grief and strain* and *keeping one's shape under the threads*: emotional resilience, and an
  [INFERRED] setting-specific integrity.

### 5.3 The atomic demands

Sorted by cluster. "tags R/S/O/P" counts the source of each demand instance. The draws columns count
odds/cost/access/effect.

| atomic demand | cluster | verbs | subsystems | tags R/S/O/P | odds/cost/access/effect | verb ids |
|---|---|---|---|---|---|---|
| raw bodily force | K01 | 18 | 5 (PC MB GV EC WT) | 7/2/5/4 | 5/0/0/13 | V018, V020, V045, V054, V066, V067, V084, V094, V099, V100, V101, V102, V154, V159, V165 |
| quick bodily reaction | K02 | 14 | 4 (PC MB GV WT) | 2/4/4/4 | 14/0/0/0 | V018, V020, V054, V083, V084, V094, V095, V096, V097, V100, V101, V102 |
| whole-body balance and agility | K02 | 6 | 4 (PC MB TW WT) | 1/0/4/1 | 6/0/0/0 | V082, V097, V099, V163, V165 |
| fine control of the hands | K03 | 9 | 9 (PC MB FI TW GV FA EC WT NP) | 3/2/4/0 | 5/0/0/4 | V006, V013, V048, V064, V076, V079, V100, V154, V169 |
| steady aim at range | K03 | 2 | 5 (PC MB EC WT NP) | 1/1/0/0 | 2/0/0/0 | V101, V167 |
| sustained exertion | K04 | 17 | 8 (PC MB SC FI GV FA EC WT) | 6/3/8/0 | 0/17/0/0 | V001, V003, V015, V022, V024, V030, V045, V058, V099, V110, V114, V134, V146, V155, V159, V164, V166 |
| taking harm and recovering | K04 | 9 | 5 (PC MB FA WT NP) | 1/3/1/4 | 0/4/0/5 | V018, V083, V094, V101, V106, V118, V168, V178 |
| bearing privation | K04 | 2 | 3 (MB WT NP) | 2/0/0/0 | 0/2/0/0 | V023, V168 |
| keen senses | K05 | 12 | 8 (PC MB FI GV FA EC WT NP) | 3/0/4/5 | 12/0/0/0 | V034, V036, V039, V105, V107, V133, V135, V139, V141, V161 |
| vigilance over time | K05 | 11 | 8 (PC MB FI TW GV FA EC NP) | 4/3/0/4 | 5/6/0/0 | V039, V049, V064, V095, V105, V106, V137, V142, V146 |
| reading terrain | K06 | 8 | 6 (PC MB FI FA EC WT) | 4/4/0/0 | 6/0/0/2 | V022, V024, V105, V107, V108, V110, V161, V162 |
| reading signs and traces | K06 | 5 | 7 (PC MB FI TW EC WT NP) | 2/3/0/0 | 4/0/1/0 | V041, V114, V134, V144, V167 |
| reading a person's face and intent | K07 | 23 | 7 (PC SC FI GV FA EC NP) | 4/11/1/7 | 22/0/0/1 | V012, V025, V037, V056, V075, V093, V096, V098, V119, V122, V123, V129, V132, V138, V140, V151, V153, V157, V170 |
| judgement of people's worth | K07 | 4 | 5 (MB GV FA EC NP) | 0/3/1/0 | 0/0/0/4 | V004, V069, V072, V158 |
| assembling meaning from parts | K08 | 9 | 3 (SC FI TW) | 4/3/0/2 | 8/0/0/1 | V028, V038, V040, V041, V050, V124, V136 |
| fine discrimination | K08 | 5 | 6 (SC FI TW GV EC NP) | 2/2/0/1 | 5/0/0/0 | V008, V013, V036, V081, V156 |
| memory for particulars | K09 | 11 | 7 (PC SC FI GV FA EC NP) | 3/0/7/1 | 3/1/1/6 | V006, V035, V038, V041, V056, V075, V124, V126, V139, V175, V177 |
| foresight and planning | K10 | 12 | 5 (MB SC GV FA EC) | 5/3/4/0 | 3/0/0/9 | V005, V009, V010, V014, V073, V089, V092, V109, V111, V112, V131, V147 |
| judgement of value | K10 | 10 | 7 (PC MB SC FI GV FA EC) | 4/3/1/2 | 4/0/0/6 | V012, V086, V104, V123, V145, V152, V153, V156 |
| reckoning in numbers | K10 | 8 | 4 (MB FI GV EC) | 2/6/0/0 | 1/0/0/7 | V021, V034, V043, V111, V141, V145, V147, V148 |
| invention under pressure | K11 | 3 | 4 (PC SC FI GV) | 3/0/0/0 | 3/0/0/0 | V011, V075, V098 |
| quick judgement | K11 | 3 | 5 (PC MB SC GV FA) | 0/2/1/0 | 3/0/0/0 | V103, V116, V125 |
| nerve in danger | K12 | 20 | 10 (PC MB SC FI TW GV FA EC WT NP) | 9/3/6/2 | 3/1/16/0 | V011, V019, V020, V064, V068, V074, V082, V083, V084, V085, V087, V102, V106, V113, V118, V121, V129, V165, V176 |
| holding to a course over time | K13 | 12 | 10 (PC MB SC FI TW GV FA EC WT NP) | 6/1/3/2 | 4/7/1/0 | V056, V065, V078, V112, V114, V118, V119, V123, V143, V153, V168, V175 |
| patient application | K13 | 10 | 6 (MB FI GV EC WT NP) | 6/0/4/0 | 0/10/0/0 | V038, V051, V117, V133, V136, V141, V155, V167, V172, V177 |
| keeping one's word | K13 | 7 | 7 (SC FI TW GV FA EC NP) | 4/0/1/2 | 2/1/1/3 | V002, V042, V047, V140, V147, V151, V171 |
| bearing grief and strain | K13 | 1 | 1 (NP) | 1/0/0/0 | 0/1/0/0 | V173 |
| self-command under scrutiny | K14 | 14 | 8 (PC MB SC FI GV FA EC NP) | 1/4/6/3 | 11/1/0/2 | V037, V052, V056, V075, V093, V104, V115, V121, V125, V129, V138, V139, V161 |
| taking another's guise | K14 | 2 | 3 (FI FA NP) | 1/1/0/0 | 2/0/0/0 | V138, V139 |
| carrying voice and bearing | K15 | 15 | 7 (PC MB SC GV FA EC NP) | 7/3/5/0 | 1/0/0/14 | V019, V032, V044, V051, V060, V061, V063, V071, V072, V087, V091, V113, V116, V117, V128 |
| menace | K15 | 5 | 6 (MB SC FI GV FA EC) | 1/0/4/0 | 5/0/0/0 | V021, V046, V054, V056, V121 |
| rousing a crowd | K15 | 2 | 4 (PC MB SC NP) | 1/1/0/0 | 0/0/0/2 | V113, V128 |
| ordering many hands | K16 | 9 | 6 (PC MB GV FA EC WT) | 2/7/0/0 | 0/2/0/7 | V009, V022, V061, V071, V092, V103, V108, V115, V147 |
| being liked | K17 | 8 | 8 (MB SC FI TW GV FA EC NP) | 2/5/1/0 | 1/0/1/6 | V016, V037, V042, V061, V072, V119, V122, V170 |
| care for another's needs | K17 | 6 | 6 (MB TW GV EC WT NP) | 4/1/1/0 | 0/0/0/6 | V049, V081, V149, V169, V172, V173 |
| moving unseen | K18 | 9 | 5 (PC MB FI FA EC) | 4/5/0/0 | 8/1/0/0 | V007, V039, V048, V064, V105, V106, V107, V135, V137 |
| hiding things | K18 | 6 | 4 (FI FA EC NP) | 3/1/2/0 | 6/0/0/0 | V013, V052, V150, V151, V160, V161 |
| handling the threads | K19 | 8 | 4 (PC TW EC NP) | 2/6/0/0 | 0/0/0/8 | V042, V076, V077, V078, V079, V080, V081, V142 |
| keeping one's shape under the threads | K19 | 8 | 5 (PC FI TW WT NP) | 1/5/0/2 | 0/5/0/3 | V040, V076, V077, V080, V082, V143 |
| perceiving the threads | K19 | 2 | 2 (FI TW) | 1/1/0/0 | 2/0/0/0 | V040, V144 |
| fluent speech | K20 | 10 | 6 (PC MB SC GV FA NP) | 1/1/8/0 | 2/0/0/8 | V027, V032, V035, V050, V086, V119, V120, V129, V130, V132 |
| knowledge of a craft | K21 | 11 | 7 (MB FI GV FA EC WT NP) | 4/7/0/0 | 0/0/1/10 | V013, V015, V030, V036, V045, V048, V051, V109, V154, V155, V162 |
| knowledge of law and custom | K21 | 8 | 4 (SC FI GV NP) | 0/6/2/0 | 1/0/1/6 | V008, V017, V026, V027, V028, V120, V131, V170 |
| letters | K21 | 8 | 5 (SC FI GV EC NP) | 0/7/1/0 | 0/0/7/1 | V006, V013, V017, V028, V034, V038, V136, V177 |
| weapon craft | K21 | 8 | 4 (PC MB SC GV) | 0/8/0/0 | 7/0/0/1 | V018, V067, V085, V094, V095, V096, V098, V100 |
| knowledge of war | K21 | 5 | 4 (MB GV FA WT) | 0/5/0/0 | 0/0/0/5 | V092, V108, V112, V116, V117 |
| knowledge of doctrine and rite | K21 | 3 | 4 (SC TW GV NP) | 0/3/0/0 | 0/0/0/3 | V128, V174, V179 |
| trained rhetoric | K21 | 3 | 2 (SC GV) | 0/3/0/0 | 1/0/0/2 | V050, V120, V124 |
| knowledge of the body and its cures | K21 | 2 | 4 (MB EC WT NP) | 0/2/0/0 | 0/0/0/2 | V049, V169 |
| thread lore | K21 | 2 | 2 (FI TW) | 0/2/0/0 | 0/0/0/2 | V040, V144 |
| watercraft | K21 | 2 | 2 (EC WT) | 1/0/1/0 | 2/0/0/0 | V164, V166 |
| horsemanship | K21 | 1 | 3 (PC MB WT) | 1/0/0/0 | 1/0/0/0 | V163 |
| conviction | K22 | 8 | 5 (SC TW GV FA NP) | 3/2/3/0 | 4/0/1/3 | V002, V044, V091, V127, V128, V174, V176, V179 |
| ruthlessness | K22 | 8 | 6 (PC MB TW GV FA NP) | 0/0/8/0 | 0/0/8/0 | V058, V065, V066, V080, V088, V093, V106, V175 |
| readiness to let go | K22 | 4 | 2 (GV NP) | 2/0/2/0 | 0/0/4/0 | V029, V053, V055, V070 |
| restraint | K22 | 1 | 1 (EC) | 0/0/1/0 | 0/0/1/0 | V160 |
| a seat's remit | K23 | 20 | 7 (MB SC FI GV FA EC NP) | 10/10/0/0 | 0/0/20/0 | V004, V008, V009, V010, V017, V021, V029, V031, V054, V055, V056, V059, V060, V061, V062, V065, V069, V074, V089, V145 |
| rank or office that others recognize | K23 | 16 | 7 (PC MB SC TW GV FA NP) | 5/11/0/0 | 0/0/14/2 | V005, V019, V025, V044, V047, V057, V063, V068, V085, V086, V091, V116, V127, V130, V171, V179 |
| a lawful claim | K23 | 4 | 4 (MB GV FA NP) | 3/0/1/0 | 1/0/3/0 | V033, V046, V070, V090 |
| means to spend | K24 | 18 | 8 (MB SC FI GV FA EC WT NP) | 11/6/1/0 | 0/1/17/0 | V003, V010, V012, V014, V015, V016, V023, V025, V030, V043, V072, V111, V140, V149, V151, V152, V157, V158 |
| arms and kit | K24 | 2 | 3 (PC MB WT) | 0/2/0/0 | 0/0/1/1 | V018, V101 |
| a place held | K24 | 1 | 1 (GV) | 1/0/0/0 | 0/0/1/0 | V059 |
| people who answer one's call | K25 | 18 | 5 (MB SC GV FA EC) | 0/17/1/0 | 2/1/12/3 | V011, V014, V022, V031, V033, V046, V054, V058, V059, V062, V071, V087, V088, V090, V109, V112, V121, V146 |
| connections | K25 | 8 | 6 (PC SC FI GV FA NP) | 1/7/0/0 | 0/0/7/1 | V001, V005, V027, V090, V106, V138, V150, V171 |
| being believed | K26 | 14 | 7 (MB SC FI GV FA EC NP) | 4/6/3/1 | 2/0/4/8 | V001, V033, V035, V047, V057, V075, V093, V126, V131, V132, V148, V150, V153 |
| knowledge of the matter | K27 | 5 | 5 (MB SC FI GV NP) | 4/1/0/0 | 0/0/5/0 | V026, V035, V057, V073, V126 |
| presence at the place | K27 | 1 | 1 (FI) | 1/0/0/0 | 0/0/1/0 | V007 |

### 5.4 The clusters

| cluster | measures | atomic demands | verbs | subsystems | draws o/c/a/e | R-tagged | root-sense families shared by ≥2 of its verbs | verb ids |
|---|---|---|---|---|---|---|---|---|
| K01 | bodily force | raw bodily force | 15 | 5 (PC MB GV EC WT) | 5/0/0/13 | 7 | strike (4: fight, kill, strike, wound), make (2: craft, work) | V018, V020, V045, V054, V066, V067, V084, V094, V099, V100, V101, V102, V154, V159, V165 |
| K02 | bodily quickness | quick bodily reaction; whole-body balance and agility | 16 | 5 (PC MB TW GV WT) | 20/0/0/0 | 3 | strike (2: fight, strike) | V018, V020, V054, V082, V083, V084, V094, V095, V096, V097, V099, V100, V101, V102, V163, V165 |
| K03 | fine hand and aim | fine control of the hands; steady aim at range | 11 | 9 (PC MB FI TW GV FA EC WT NP) | 7/0/0/4 | 4 | make (3: craft, forge, heal), take (2: hunt, steal) | V006, V013, V048, V064, V076, V079, V100, V101, V154, V167, V169 |
| K04 | bodily toughness | bearing privation; sustained exertion; taking harm and recovering | 26 | 9 (PC MB SC FI GV FA EC WT NP) | 0/23/0/5 | 9 | strike (3: fight, raze, strike), build (2: build, restore), tread (2: march, patrol), follow (2: pursue, track) | V001, V003, V015, V018, V022, V023, V024, V030, V045, V058, V083, V094, V099, V101, V106, V110, V114, V118, V134, V146, V155, V159, V164, V166, V168, V178 |
| K05 | watchfulness | keen senses; vigilance over time | 17 | 9 (PC MB FI TW GV FA EC WT NP) | 17/6/0/0 | 7 | hide (4: ambush, eavesdrop, shadow, smuggle), watch (3: guard, surveil, ward) | V034, V036, V039, V049, V064, V095, V105, V106, V107, V133, V135, V137, V139, V141, V142, V146, V161 |
| K06 | field sense | reading signs and traces; reading terrain | 13 | 8 (PC MB FI TW FA EC WT NP) | 10/0/1/2 | 6 | hide (2: ambush, smuggle), follow (2: pursue, track) | V022, V024, V041, V105, V107, V108, V110, V114, V134, V144, V161, V162, V167 |
| K07 | reading people | judgement of people's worth; reading a person's face and intent | 23 | 8 (PC MB SC FI GV FA EC NP) | 22/0/0/5 | 4 | give (4: betray, bribe, lend, suborn) | V004, V012, V025, V037, V056, V069, V072, V075, V093, V096, V098, V119, V122, V123, V129, V132, V138, V140, V151, V153, V157, V158, V170 |
| K08 | reasoning | assembling meaning from parts; fine discrimination | 12 | 6 (SC FI TW GV EC NP) | 13/0/0/1 | 6 | make (2: forge, mend), build (2: construe, reconstruct) | V008, V013, V028, V036, V038, V040, V041, V050, V081, V124, V136, V156 |
| K09 | memory | memory for particulars | 11 | 7 (PC SC FI GV FA EC NP) | 3/1/1/6 | 3 | seek (2: interrogate, research) | V006, V035, V038, V041, V056, V075, V124, V126, V139, V175, V177 |
| K10 | reckoning and forethought | foresight and planning; judgement of value; reckoning in numbers | 25 | 7 (PC MB SC FI GV FA EC) | 8/0/0/22 | 11 | see (2: provision, survey), give (2: surrender, yield), price (2: appraise, tax) | V005, V009, V010, V012, V014, V021, V034, V043, V073, V086, V089, V092, V104, V109, V111, V112, V123, V131, V141, V145, V147, V148, V152, V153, V156 |
| K11 | quick wits | invention under pressure; quick judgement | 6 | 6 (PC MB SC FI GV FA) | 6/0/0/0 | 3 | go (2: concede, evade / defy) | V011, V075, V098, V103, V116, V125 |
| K12 | nerve | nerve in danger | 19 | 10 (PC MB SC FI TW GV FA EC WT NP) | 3/1/16/0 | 9 | take (2: accept, steal), loosen (2: repudiate, rescue), jump (2: insult, leap) | V011, V019, V020, V064, V068, V074, V082, V083, V084, V085, V087, V102, V106, V113, V118, V121, V129, V165, V176 |
| K13 | constancy | bearing grief and strain; holding to a course over time; keeping one's word; patient application | 30 | 10 (PC MB SC FI TW GV FA EC WT NP) | 6/19/2/3 | 17 | bind (3: lock, marry, tie / knot), seek (3: interrogate, research, search), give (2: bribe, suborn), follow (2: execute, pursue) | V002, V038, V042, V047, V051, V056, V065, V078, V112, V114, V117, V118, V119, V123, V133, V136, V140, V141, V143, V147, V151, V153, V155, V167, V168, V171, V172, V173, V175, V177 |
| K14 | self-command | self-command under scrutiny; taking another's guise | 13 | 8 (PC MB SC FI GV FA EC NP) | 13/1/0/2 | 2 | hide (2: conceal, smuggle), give (2: betray, yield) | V037, V052, V056, V075, V093, V104, V115, V121, V125, V129, V138, V139, V161 |
| K15 | presence | carrying voice and bearing; menace; rousing a crowd | 20 | 8 (PC MB SC FI GV FA EC NP) | 6/0/0/16 | 9 | proclaim (3: ban, preach, proclaim), speak (2: speak, utter), seek (2: interrogate, requisition) | V019, V021, V032, V044, V046, V051, V054, V056, V060, V061, V063, V071, V072, V087, V091, V113, V116, V117, V121, V128 |
| K16 | ordering many | ordering many hands | 9 | 6 (PC MB GV FA EC WT) | 0/2/0/7 | 2 | — | V009, V022, V061, V071, V092, V103, V108, V115, V147 |
| K17 | warmth | being liked; care for another's needs | 14 | 9 (MB SC FI TW GV FA EC WT NP) | 1/0/1/12 | 6 | raise (3: levy, rear, relieve), make (2: heal, mend) | V016, V037, V042, V049, V061, V072, V081, V119, V122, V149, V169, V170, V172, V173 |
| K18 | stealth | hiding things; moving unseen | 15 | 6 (PC MB FI FA EC NP) | 14/1/0/0 | 7 | hide (6: ambush, conceal, eavesdrop, hoard, shadow, smuggle) | V007, V013, V039, V048, V052, V064, V105, V106, V107, V135, V137, V150, V151, V160, V161 |
| K19 | the threads | handling the threads; keeping one's shape under the threads; perceiving the threads | 12 | 6 (PC FI TW EC WT NP) | 2/5/0/11 | 4 | bind (3: lock, tie / knot, weave), draw (2: pull, trace), loosen (2: loosen, sever) | V040, V042, V076, V077, V078, V079, V080, V081, V082, V142, V143, V144 |
| K20 | fluency | fluent speech | 10 | 6 (PC MB SC GV FA NP) | 2/0/0/8 | 1 | — | V027, V032, V035, V050, V086, V119, V120, V129, V130, V132 |
| K21 | learned knowledge (skills) | horsemanship; knowledge of a craft; knowledge of doctrine and rite; knowledge of law and custom; knowledge of the body and its cures; knowledge of war; letters; thread lore; trained rhetoric; watercraft; weapon craft | 49 | 10 (PC MB SC FI TW GV FA EC WT NP) | 12/0/9/32 | 6 | make (5: craft, forge, fortify, heal, work), build (3: build, construe, restore), seek (3: petition, pray, research), strike (3: fight, strike, wound), draw (2: trace, train), drive (2: navigate, refute), field (2: champion, encamp) | V006, V008, V013, V015, V017, V018, V026, V027, V028, V030, V034, V036, V038, V040, V045, V048, V049, V050, V051, V067, V085, V092, V094, V095, V096, V098, V100, V108, V109, V112, V116, V117, V120, V124, V128, V131, V136, V144, V154, V155, V162, V163, V164, V166, V169, V170, V174, V177, V179 |
| K22 | disposition (values) | conviction; readiness to let go; restraint; ruthlessness | 21 | 8 (PC MB SC TW GV FA EC NP) | 4/0/14/3 | 5 | loosen (3: release, sever, waive), give (3: betray, forgive, pardon), strike (2: kill, raze) | V002, V029, V044, V053, V055, V058, V065, V066, V070, V080, V088, V091, V093, V106, V127, V128, V160, V174, V175, V176, V179 |
| K23 | standing and authority | a lawful claim; a seat's remit; rank or office that others recognize | 40 | 9 (PC MB SC FI TW GV FA EC NP) | 1/0/37/2 | 18 | loosen (3: release, repudiate, waive), give (3: command, pardon, surrender), proclaim (3: abdicate, ban, proclaim), carry (2: charge (accuse), confer), stand (2: arrest, establish), go (2: issue, succeed), seek (2: interrogate, requisition), speak (2: deny, utter), price (2: praise, tax), come (2: convene, covenant), bind (2: marry, oblige) | V004, V005, V008, V009, V010, V017, V019, V021, V025, V029, V031, V033, V044, V046, V047, V054, V055, V056, V057, V059, V060, V061, V062, V063, V065, V068, V069, V070, V074, V085, V086, V089, V090, V091, V116, V127, V130, V145, V171, V179 |
| K24 | means and holdings | a place held; arms and kit; means to spend | 21 | 9 (PC MB SC FI GV FA EC WT NP) | 0/1/19/1 | 12 | give (4: bribe, give, lend, suborn), build (2: build, restore) | V003, V010, V012, V014, V015, V016, V018, V023, V025, V030, V043, V059, V072, V101, V111, V140, V149, V151, V152, V157, V158 |
| K25 | following and connections | connections; people who answer one's call | 25 | 8 (PC MB SC FI GV FA EC NP) | 2/1/19/4 | 1 | come (2: conspire, convene), go (2: evade / defy, succeed), tread (2: march, patrol), take (2: sack, seize), strike (2: raze, storm) | V001, V005, V011, V014, V022, V027, V031, V033, V046, V054, V058, V059, V062, V071, V087, V088, V090, V106, V109, V112, V121, V138, V146, V150, V171 |
| K26 | credibility | being believed | 13 | 7 (MB SC FI GV FA EC NP) | 2/0/4/8 | 4 | carry (2: carry, charge (accuse)), count (2: ration, tell), come (2: conspire, covenant) | V001, V033, V035, V047, V057, V075, V093, V126, V131, V132, V148, V150, V153 |
| K27 | situational access | knowledge of the matter; presence at the place | 6 | 5 (MB SC FI GV NP) | 0/0/6/0 | 5 | — | V007, V026, V035, V057, V073, V126 |

**Notes on the clusters:**

- **Learned knowledge (K21) is the largest cluster** (49 verbs, all ten subsystems). Skills carry
  more of the game's demand than any single capacity. A sheet built only of attributes would explain
  too little.
- **Standing and authority (K23) is second** (40 verbs; 37 of its 40 draws are access). Following
  and connections (K25, 25 verbs) and means and holdings (K24, 21) follow. Together the holdings are
  the dominant gate on what a person may do.
- **Among the personal clusters, constancy (K13) is the broadest**: 30 verbs, all ten subsystems, and
  **the highest root-sense count, 17 R tags**. Its verbs' root senses *are* holding a course: commit,
  covenant, besiege ("sit before"), withstand, pursue ("follow on"), execute ("follow out"), research
  and search ("go round"), study ("be eager"), drill ("bore round"), train ("draw along").
  Next come bodily toughness (K04, 28 instances on 26 verbs, nine subsystems), reckoning and
  forethought (K10, 25 verbs) and reading people (K07, 23 verbs).
- **Draw types separate cleanly.** Bodily quickness moves **odds only** (20 of 20). Bodily toughness
  moves **cost** (23 of 28). Reckoning and forethought moves **effect** (22 of 30). Presence moves
  effect (16 of 22). Warmth moves effect (12 of 14). **Nerve moves access** (16 of 20): nerve decides
  *whether* a person attempts the act, not how well he does it. That is a property of the chooser more
  than of the dice (§6.3, attribute 9).
- **Disposition (K22, 21 verbs) is mostly access (14 of 21).** Values gate choices. They do not move
  odds.

### 5.5 Root-sense families and what they show

Families with three or more verbs. "Clusters their demands fall in" counts demand instances, patient-side
included.

| root sense | verbs | subsystems spanned | clusters their demands fall in (count) |
|---|---|---|---|
| give | give, forgive, pardon, surrender, betray, yield, command, bribe, suborn, lend (10) | PC MB SC FI GV FA EC NP | K24 means and holdings 4, K07 reading people 4, K22 disposition (values) 3, K23 standing and authority 3 |
| loosen | release, repudiate, waive, loosen, sever, rescue, disengage (7) | PC MB SC TW GV NP | K19 the threads 4, K23 standing and authority 3, K22 disposition (values) 3, K12 nerve 2 |
| make | forge, work, mend, fortify, craft, heal (6) | MB FI TW GV EC WT NP | K21 learned knowledge (skills) 6, K03 fine hand and aim 3, K08 reasoning 2, K01 bodily force 2 |
| strike | fight, raze, kill, wound, storm, strike (6) | PC MB FA | K01 bodily force 5, K02 bodily quickness 4, K04 bodily toughness 4, K21 learned knowledge (skills) 3 |
| seek | requisition, petition, research, interrogate, search, pray (6) | SC FI TW GV EC WT NP | K21 learned knowledge (skills) 3, K13 constancy 3, K23 standing and authority 2, K15 presence 2 |
| bind | oblige, tie / knot, weave, lock, rally, marry (6) | PC MB SC TW GV FA NP | K19 the threads 4, K13 constancy 3, K23 standing and authority 2, K15 presence 2 |
| draw | train, withdraw, pull, retreat, trace, haul (6) | MB SC FI TW EC WT NP | K19 the threads 4, K21 learned knowledge (skills) 2, K13 constancy 1, K15 presence 1 |
| hide | conceal, ambush, eavesdrop, shadow, hoard, smuggle (6) | PC MB FI FA EC NP | K05 watchfulness 8, K18 stealth 6, K14 self-command 2, K06 field sense 2 |
| build | destroy_record, build, construe, restore, reconstruct (5) | SC FI EC | K21 learned knowledge (skills) 4, K04 bodily toughness 2, K24 means and holdings 2, K08 reasoning 2 |
| go | evade / defy, issue, migrate, succeed, concede (5) | SC GV FA WT NP | K11 quick wits 2, K25 following and connections 2, K23 standing and authority 2, K21 learned knowledge (skills) 2 |
| take | accept, seize, steal, sack, hunt (5) | PC MB FI GV FA EC WT NP | K12 nerve 2, K25 following and connections 2, K03 fine hand and aim 2, K01 bodily force 1 |
| carry | carry, confer, transfer, charge (accuse) (4) | SC GV EC | K26 credibility 3, K23 standing and authority 2, K25 following and connections 1, K04 bodily toughness 1 |
| stand | establish, arrest, withstand, testify (4) | PC MB SC FI GV | K23 standing and authority 2, K01 bodily force 2, K24 means and holdings 1, K10 reckoning and forethought 1 |
| watch | surveil, guard, ward, steward (4) | PC MB FI TW GV EC | K05 watchfulness 5, K10 reckoning and forethought 2, K18 stealth 1, K02 bodily quickness 1 |
| proclaim | ban, proclaim, abdicate, preach (4) | SC GV FA NP | K15 presence 4, K23 standing and authority 3, K10 reckoning and forethought 1, K21 learned knowledge (skills) 1 |
| come | convene, covenant, conspire (3) | SC GV FA NP | K23 standing and authority 2, K25 following and connections 2, K26 credibility 2, K10 reckoning and forethought 1 |
| speak | speak, utter, deny (3) | SC GV FA | K15 presence 2, K23 standing and authority 2, K20 fluency 1, K22 disposition (values) 1 |
| see | survey, interview, provision (3) | MB SC FI GV EC | K10 reckoning and forethought 3, K14 self-command 2, K05 watchfulness 1, K21 learned knowledge (skills) 1 |
| hold | detain, grapple, anchor (3) | PC TW GV NP | K01 bodily force 2, K02 bodily quickness 2, K23 standing and authority 1, K24 means and holdings 1 |
| raise | levy, relieve, rear (3) | MB GV FA NP | K17 warmth 3, K23 standing and authority 1, K15 presence 1, K16 ordering many 1 |
| follow | execute, pursue, track (3) | PC MB FI GV WT | K13 constancy 2, K04 bodily toughness 2, K06 field sense 2, K23 standing and authority 1 |
| drive | rush, refute, navigate (3) | PC MB SC WT | K08 reasoning 2, K21 learned knowledge (skills) 2, K01 bodily force 1, K12 nerve 1 |
| price | praise, tax, appraise (3) | SC FI GV EC NP | K10 reckoning and forethought 3, K23 standing and authority 2, K20 fluency 1, K08 reasoning 1 |

**Reading the families:**

1. **Families that land in one cluster are evidence for that cluster as a natural kind:**
   - *hide* (conceal, ambush, eavesdrop, shadow, hoard, smuggle) → stealth, 6 of 6 on the performer
     side; the patient side adds watchfulness (8), its opposite.
   - *watch* (surveil, guard, ward, steward) → watchfulness, 4 of 4.
   - *proclaim* (ban, proclaim, abdicate, preach) → presence, 4 of 4.
   - *price* (praise, tax, appraise) → reckoning and judgement of value, 3 of 3.
   - *see* (survey, interview, provision) → reckoning and forethought, 3 of 3.
   - *strike* (fight, raze, kill, wound, storm, strike) → bodily force, 5 of 6.

   English, and the Latin and French behind it, has long named watching, hiding, proclaiming, valuing
   and striking as separate acts. That is weak but independent support for watchfulness, a hiding
   capacity, presence, forethought and force as separate properties. The *see* family is worth a note:
   Latin *pro-videre* "see ahead" gave both *provision* and *providence*. Language files
   quartermastering under foresight, not under arithmetic.
2. **Families that scatter are evidence that the demand is not a capacity:**
   - *give* (give, forgive, pardon, surrender, betray, yield, command, bribe, suborn, lend; ten verbs,
     eight subsystems) lands in means, values, standing and reading people. To give you must **have**
     (means), have **the right** (standing), and be **willing** (values). No capacity "to give" exists.
     *forgive* is an Old English calque of Latin *perdonare*, from which *pardon* also comes. One root
     sense split into a private act and an official one, and the demand split with it: the private act
     wants a temperament (readiness to let go), the official act wants a seat.
   - *loosen* (release, repudiate, waive, loosen, sever, rescue, disengage) and *carry*/*stand*/*go*
     scatter the same way.
3. **The thread verbs share root senses with the social binding verbs, but not their demands.** The
   *bind* family (oblige, tie, weave, lock, rally, marry) lands mostly in the threads cluster (4) and
   constancy (3). The social members want standing and constancy. The thread members want the threads
   cluster. Together with *draw* (pull, trace) and *loosen* (loosen, sever), **the setting's threadwork
   literalizes the vocabulary of obligation, but performing it asks for different things.** One
   "binding" attribute serving oaths and knots would be a metaphor turned into a mechanic. The demands
   do not support it.
4. **Register.** The verbs whose demands are bodily and personal are overwhelmingly Germanic: fight,
   strike, work, build, ride, swim, climb, leap, steal, hunt, give, tell, speak, heal. The verbs whose
   demands are positional are overwhelmingly Latinate or Norman French: confer, establish, determine,
   requisition, revoke, pardon, detain, abolish, abdicate, depose. English took its law and
   administration from the Normans. In this list **the etymological register predicts the kind of
   demand**: a Latinate verb of rule has a bodily root sense and a positional demand (§3.6).

### 5.6 Does the result stand on the code's verbs alone?

| cluster | measures | code | plan | plan (refused/cut) | lane rec | designed here | rank among clusters, code verbs only |
|---|---|---|---|---|---|---|---|
| K01 | bodily force | 3 | 1 | 2 | 1 | 8 | 18 |
| K02 | bodily quickness | 2 | 1 | 0 | 3 | 10 | 24 |
| K03 | fine hand and aim | 2 | 1 | 1 | 2 | 5 | 22 |
| K04 | bodily toughness | 9 | 1 | 0 | 1 | 15 | 4 |
| K05 | watchfulness | 3 | 1 | 1 | 0 | 12 | 21 |
| K06 | field sense | 3 | 0 | 0 | 0 | 10 | 19 |
| K07 | reading people | 4 | 1 | 1 | 3 | 14 | 8 |
| K08 | reasoning | 7 | 1 | 0 | 1 | 3 | 7 |
| K09 | memory | 4 | 1 | 0 | 1 | 5 | 9 |
| K10 | reckoning and forethought | 8 | 0 | 0 | 4 | 13 | 6 |
| K11 | quick wits | 1 | 0 | 0 | 1 | 4 | 26 |
| K12 | nerve | 3 | 0 | 2 | 6 | 8 | 16 |
| K13 | constancy | 3 | 3 | 1 | 1 | 22 | 12 |
| K14 | self-command | 1 | 2 | 0 | 2 | 8 | 27 |
| K15 | presence | 4 | 7 | 0 | 4 | 5 | 10 |
| K16 | ordering many | 2 | 1 | 0 | 2 | 4 | 23 |
| K17 | warmth | 3 | 2 | 0 | 2 | 7 | 17 |
| K18 | stealth | 3 | 2 | 1 | 0 | 9 | 15 |
| K19 | the threads | 2 | 0 | 0 | 7 | 3 | 25 |
| K20 | fluency | 3 | 1 | 0 | 1 | 5 | 20 |
| K21 | learned knowledge (skills) | 15 | 4 | 1 | 2 | 27 | 1 |
| K22 | disposition (values) | 3 | 3 | 3 | 4 | 8 | 13 |
| K23 | standing and authority | 13 | 11 | 4 | 6 | 6 | 2 |
| K24 | means and holdings | 11 | 1 | 0 | 1 | 8 | 3 |
| K25 | following and connections | 8 | 5 | 0 | 4 | 8 | 5 |
| K26 | credibility | 3 | 2 | 0 | 2 | 6 | 11 |
| K27 | situational access | 3 | 1 | 0 | 1 | 1 | 14 |

**Not entirely, and the dependence is named here.** Ranked on the 45 code rows alone, the clusters run:
skills 1, standing 2, means 3, bodily toughness 4, following 5, forethought 6, reasoning 7, reading
people 8, memory 9, presence 10. **The body barely shows:** force ranks 18th, quickness 24th, and
self-command 27th (last). The code's personal combat sits behind one `fight` row, and the code has no
stealth, travel-skill or care acts. **Quickness, fine hand, stealth, composure and constancy owe most
of their breadth to verbs I added** (9 of 14, 5 of 11, 9 of 15, 7 of 11 and 19 of 26 respectively;
performer side). Code, plan and lane alone would give a governance-heavy set: forethought, reasoning,
reading people, toughness and presence, with standing and means on the sheet as holdings.

### 5.7 Do the verbs tell the clusters apart?

How often two personal clusters are drawn on by the same verb (performer side). Jaccard overlap is the
verbs drawing on both, divided by the verbs drawing on either. The table shows the top 16 pairs.

| cluster pair | verbs drawing on both | Jaccard overlap |
|---|---|---|
| bodily force + bodily quickness | 7 | 0.33 |
| bodily quickness + nerve | 6 | 0.23 |
| watchfulness + stealth | 5 | 0.22 |
| reading people + warmth | 5 | 0.17 |
| reasoning + memory | 3 | 0.17 |
| bodily toughness + field sense | 5 | 0.16 |
| bodily force + nerve | 4 | 0.14 |
| quick wits + self-command | 2 | 0.13 |
| fine hand and aim + stealth | 3 | 0.13 |
| bodily force + bodily toughness | 4 | 0.12 |
| field sense + stealth | 3 | 0.12 |
| reading people + fluency | 3 | 0.11 |
| reckoning and forethought + constancy | 5 | 0.11 |
| field sense + ordering many | 2 | 0.10 |
| reckoning and forethought + ordering many | 3 | 0.10 |
| reasoning + the threads | 2 | 0.10 |

The highest overlap is 0.33, between force and quickness (the fighting verbs use both). **No pair of
clusters is drawn on by the same verbs.** The verbs distinguish all twenty personal clusters. This
measures whether the *acts* separate the properties. It cannot measure whether the properties vary
separately among *persons*. §6's independence test is the judgement that does that, and it is not a
measurement.
