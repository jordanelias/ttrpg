# Part 4 — Acquisition and growth: what raises a technique, what it costs, and how it differs from Concentration

## Status: PROPOSED. Reference only. Every number marked `[ASSUMPTION; low]` is a placeholder for calibration and Jordan's correction.

## 4.1 Three things grow, and each has one writer

| what grows | what it means in a fight | who writes it | where it is stored | ceiling | status |
|---|---|---|---|---|---|
| **a technique's level** (depth) | how strongly that technique acts (`value ** level` or `value * level`, `ability_primitives.py:185-207`) | **instruction only**: a teacher, a school, a story event (§4.2) | on the person (Part 5) | 8 (`MAX_INVESTMENT_LEVEL`, `:151`); and the teacher's own level | proposed |
| **attention** (breadth) | how many techniques the fighter can bring (Part 2 §2.3.3) | derived from **Concentration**, which fight experience and sparring write (PC-22, Jordan 2026-11-07) | nothing stored: a function of Focus, Spirit and experience "derived from the log" (PC-22, as carried in the brief §3.7) | Concentration's own; sparring's lower ceiling | proposed; the experience term is PC-22's and unbuilt |
| **the `arms` skill score** | the fighter's pool and the obstacle his opponent rolls against (`fight.py:172-177`; `attributes.py:28-31`) | `train` (`engine/season/loop/effects_combat.py:909-931`) and build-by-doing, `_grown`: a survivor of a fight that drew blood gains one point (`:271-277`) | `Person.capability` | the row's ceiling | **live** |

**Why three and not one.** Jordan's ruling separates them: experience from fights "should write moreso" to composure, Concentration, and "not increased technique and martial prowess itself" (as recorded at `00_tradition_sets.md:135`; the brief paraphrases "moreso" as "mainly"). A design where fighting raised technique levels would contradict it; a design where nothing but fighting raised anything would leave technique with no writer. So depth comes from being *taught*, breadth from having *fought*. **A tension this proposal does not resolve and does not widen:** `_grown` already raises `arms` for a fight survivor (v11 CP-T03-04), which reads like "martial prowess" growing from a fight. That is PC-22's to reconcile with its own ruling; nothing here adds a second fight-driven writer.

## 4.2 What raises a technique level

1. **Being taught (the main route).** The season verb `train` already has the right shape: an *actor* who trains a *subject*, and the actor's own capability is not read today ("The ACTOR's own capability is NOT read: capability gates nothing", `effects_combat.py:918-919`). Proposed: when the actor knows a technique that comes next on the subject's **path** (Part 1, J-D) at a higher level than the subject holds it, a `train` raises the subject's level in it by one. **The path supplies which technique, so the act needs no new operand** (the act already carries `kind` for a vocation, `:912-913`; H-94 records that acts carry few operands, which this avoids). **This changes one principle**: the teacher's own level would gate the raise, where today the actor's capability gates nothing. That is decision D-7 in Part 9.
2. **A school.** A place (a fencing hall in a settlement) acting as a standing teacher, with a curriculum stocked to a level. Content; the mechanism is the same as (1) with a place as the actor.
3. **Self-study.** Without a teacher, a person may raise a technique already on their path to level 2 and no further `[ASSUMPTION; low]`. A manual is a teacher whose level is 2.
4. **A story event.** An authored event may teach a technique at level 1, or reveal a set (Troubleshooter grants masteries for story choices and achievements: "some case-scenario choices determine which mastery you get" [FAN: Steam thread, `troubleshooter_combat_reception.md:78`]).
5. **Not by fighting, not by sparring.** Sparring (PC-22, designed, unbuilt) pays Concentration up to its own ceiling, pairwise familiarity, and a marginal capability raise. In this proposal it raises *attention* through Concentration and never a technique level. That keeps the 2026-11-07 ruling exact.

**Cost of a level `[ASSUMPTION; low]`.** One `train` act per level for levels 1–3, two for 4–5, three for 6–8; a full mastery of one technique is therefore 3 + 4 + 9 = 16 acts of a teacher who has it. The price is time (the subject's and the teacher's), and the scarcity of teachers at high levels. There is no currency: Troubleshooter's Training Manuals and the Bravely Default and FFT job-point economies are the precedents for a currency, and both drew grinding complaints (§4.4).

**Growth stage, derived, never stored `[ASSUMPTION; low]`:** *novice* until three techniques reach level 3; *practised* until three reach level 6; *veteran* after. Slots per board column: 1, 2, 3 by stage. A person's stage is printed on the sheet (Part 8) and computed by `sheets.py` from their levels.

**A set needs depth, too `[ASSUMPTION; low]`.** A set's gate opens only when each member is at level 3 or more. So a set is a goal of depth as well as breadth, the way Tactics Ogre gates finishing moves on weapon-skill ranks 2, 4, 6 and 8 [V: S15, `tactics_ogre_bravely_default.md:73`].

## 4.3 How this differs from the Concentration growth of the 2026-11-07 rulings

| | technique level | Concentration (and attention from it) |
|---|---|---|
| source | a teacher, a school, self-study to a cap, a story event | fights (mainly), sparring (capped) |
| stored? | yes, per technique, on the person | no: derived from the log (PC-22) |
| how often | as often as a teacher is available and the act is chosen | sparring once per season per person (PC-22) |
| what it changes in a fight | the factor on one lever | how many techniques are on the board; and, already today, the in-bout Concentration pool (`conc_max`, `combatant.py:172`) |
| who decides | the player or the NPC's chooser picks `train` and the teacher; the path picks the technique | nobody: it follows from what happened |
| ceiling | 8, and the teacher's level | PC-22's; sparring's own |

## 4.4 Precedents, adjudicated for growth

| game | how a unit grows (tagged) | transfers? | why |
|---|---|---|---|
| **Troubleshooter** | masteries cannot be levelled; they drop from enemies, are crafted by "research" from other masteries, are granted by class level 1/4/8/12/16, by story choice and achievement [FAN: Steam threads; TroubleMaster data, `troubleshooter_characters.md:46,92-93`]; Training Points = character level + 0/2/3 [V: 26 sheets, `guide_1349483727_images.md:751-781`] | **with change** | masteries are found, not levelled; Valoria's techniques *are* levelled (0–8, the live model, ED-PC-0024). What transfers is "class level unlocks the next class masteries", as `requires` levels down a curriculum line |
| **Tactics Ogre** | PSP: classes level, not units ("never a point where one unit can be the dominate force") [V: S13], "the 2nd most problematic aspect of the game" by one FAQ author's account [FAN: S16]; ranked skills 1–8 rising *by use*, finishers at ranks 2/4/6/8 [V: S15, S16]; Reborn: unit levels return, four skill slots, training battles where units cannot die [V: S1, S3, S4] | **the ladder shape transfers; growth by use does not** | a 1–8 rank ladder matches Valoria's 0–8 exactly; but rank by use is "SaGa-style growth of technique by use", flagged as conflicting with Jordan's ruling (brief §2). Reborn's no-death training battles are the shape of `spar` |
| **Final Fantasy Tactics** | JP per job, earned only by a *successful* action; job levels unlock jobs in a prerequisite DAG; documented JP exploits and a developer nerf [V: FF wiki, `precedents_other.md` §1.1–1.2, FFT block] | **the DAG transfers as `requires`; JP does not** | JP is growth by use again, and its economy was exploited (the JP scroll glitch, Accrue JP stacking) |
| **Bravely Default** | JP only to the current job; one ability per job level, cap 14; reviewers: the job system "necessitated grinding to unlock its full value" [V: B1, B2, B12] | **no** | a currency that only one job earns at a time forces grinding; Valoria has no "current job" to starve |
| **Triangle Strategy** | promotion at level 10 + a Medal of Bravery and level 20 + a second medal (Valor or Honor; the name is unresolved across sources); medals come from chapter and battle rewards and are also sold at the encampment, and "There does not appear to be a way to farm these items" [V: S10, S9]; weapon trees with either/or nodes [V: S3] | **with change** | a gate item of limited supply is what a *teacher* already is in Valoria: a master who knows a technique at 8 is rare, so no item is needed |
| **Fire Emblem: Three Houses** | class mastery permanently teaches an ability usable in any class [V: `precedents_other.md` FE3H block] | **yes** | a technique, once learned, is the person's regardless of the board they bring |
| **Divinity: Original Sin 2** | skillbooks plus school points plus Memory slots (4 at Memory 10, skills cost 1–3) [V: `precedents_other.md` DOS2 block] | **with change** | Memory is the closest precedent to attention: a capacity from an attribute that skills cost against. Valoria reads it from Concentration instead of a dedicated attribute |

## 4.4b Two things the generated sheets show about the ladder (run this session; Part 8)

1. **Depth is a real lever at the module, not a near-zero one.** Each sheet fights its own person with an empty board on 400 keyed seeds (`sheets.py`, `measure`). The control arm (empty board against itself) sits at 47.8–51.7%. With the board: the novice (two techniques at level 1) wins 53.5%; the practised German 59.8%; the cross-trained Spaniard 62.3%; the veteran Japanese 66.2%; the bespoke Italian 72.5%. **Caveat on the two cross-trained sheets:** the run passes one tradition name per fighter (`sheets.py`, `measure`; the record's own limit, `fight.py:58-63`), so the Spaniard's Italian techniques and the bespoke Italian's German ones act on nothing in it; those two figures measure each one's primary school only, not the board the sheet shows. At n = 400 the 95% half-width is about 5 points, so every board above level 1 moves the mirror by more than noise. The earlier finding of a near-zero aggregate (ED-PC-0023; the 2-point band in the agency proposal §6.2) was measured one technique at level 1; it does not describe a practised board. This is what the fiat audit allows ("some builds are stronger and that is fine"), and it is what makes teaching worth a season: but **the 2-point band cannot be the acceptance test for a board** (decision D-5).
2. **The top of the ladder is dead on a probability lever.** The counter's reach is `0.45 × tempo × (1 − 0.5·lean) × factor` (`combat_systems.py:1029`; `COUNTER_SELECT_BASE = 0.45`, `config.py:247`). With lean = (disposition − 4) ÷ 3 (`combat_systems.py:171-174`), a full `tempo` factor of 1, and one technique at ×1.4 per level, the product first reaches 1 at level 3 for a neutral fighter (0.88 at level 2, so level 3 still lifts it to certainty and **levels 4 to 8** change nothing at that site); at level 2 for a cautious fighter (disposition 3); at level 4 for disposition 6; at level 5 for the most aggressive (disposition 7). Any `tempo` factor other than 1 moves the point again [arithmetic from the code; not run separately]. The live ladder is bounded for overflow (`ability_primitives.py:144-153`), not for saturation. The repo's own remedy for a signed site is a log-odds edge (`lever_log_edge`, ED-PC-0045, `combat_systems.py:15`); a probability site would take the same form. That is a lever-form question for the PC lane (the B15.13 sweep), named here because a growth design that sells eight levels must not sell dead ones.

## 4.5 Proposals on growth, ranked

### G-1. Taught depth, fought breadth (RECOMMENDED)

- **What it is.** §4.2 and §4.3: technique levels from `train` with a teacher who knows more, along the person's path; attention from Concentration.
- **N-line.** Cut the teacher rule and levels need another source, which must be fighting (against the ruling) or a currency (§4.4's grinding precedents). Cut attention-from-Concentration and fight experience has nothing to buy in personal combat besides the in-bout pool.
- **Runtime change in `engine/season/`.** `_eff_train` gains one branch: when the actor and subject share a path entry the actor knows better, raise the subject's level (written to the carrier, Part 5). The seam composes attention from Concentration once PC-22's function exists.
- **Falsifier.** (1) Over a seeded multi-season run, no technique level rises in a season in which the person took no `train` and had no story event (a level that moves on its own is a hidden writer). (2) A level never exceeds the teacher's. Both are counts over the run, `assert checked >= 1`.
- **Build order, with gates.** (1) The carrier (Part 5). (2) The `train` branch, behind a fixture switch defaulting off; gate: seed-2 one-season hash EQUAL with it off. (3) Switch on; gate: falsifiers (1)–(2); MOVER(behaviour) declared and recorded. (4) Attention from Concentration, after PC-22 lands its function.
- **Hash movers.** (3) moves the season hash wherever a `train` of a technique fires; fights still do not form (H-264), so the fight outcomes do not move.
- **Cost.** Small in code; the content (who teaches what, where) is Jordan's.
- **Decision it leaves Jordan.** D-7 (may a teacher's level gate `train`?).
- **Lessons.** Tactics Ogre's 1–8 ladder and training battles; FFT's prerequisite DAG; FE3H's permanent learning; DOS2's Memory (tags in §4.4).

### G-2. A technique-point currency (Troubleshooter's Training Points or FFT's JP, ported)

- Points earned per act or per fight, spent on levels. **Dies on two counts:** points per fight are growth by use (the ruling), and a currency invites the grind every precedent above reports. Ranked third.

### G-3. Growth by use (Tactics Ogre ranks, SaGa)

- **Dies on Jordan's 2026-11-07 ruling.** Listed so it is not re-proposed.

### G-4. Fixed at creation (the lifepath sets the levels; nothing grows)

- **N-line.** The cheapest path to a varied realm: B18.05 already gives martial lifepaths an `arms` key; the same lifepath would set a starting path and levels. **What dies:** growth. **Ranked second, and recommended as G-1's first increment**: it makes persons differ before anyone can grow them, and it needs only the carrier.
