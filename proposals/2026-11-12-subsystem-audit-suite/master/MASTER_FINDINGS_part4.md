# The master findings — part 4: the findings by subsystem (PC, MB, SC)

## Status: REFERENCE (part 4 of `master/MASTER_FINDINGS.md`; the row tables are generated from the closure tables `unified/U5_FINDINGS_CLOSURE_U5a.md`..`_U5d.md` by the lane's scratch extract, the syntheses written by lane MF; resolves nothing at runtime; dies with the suite)

Columns and order are the head part's §0. **evidence**: the closure row (`U5a:66` = `unified/U5_FINDINGS_CLOSURE_U5a.md` line 66), then the audit line that defines the finding where the extract found it (`audits/` implied), then the closure row's own evidence, cut to one line. **sev**: B blocks a requirement · D degrades narrative · C code matter · M design matter · H hygiene · — ungraded. **carrier**: the closure row's carrier cell, cut to one line (its short names are the closure table's, defined at the head of that table's section). **batch**: v12's handle; `→` before it on a SUPERSEDED row (the successor's batch); `— (stale)`, `— (disputed)`, `— (answered …)` where no fix is owed. Claims are the closure tables' one-liners, cut at about a hundred characters.


---

## PC — personal combat

<!-- SYNTHESIS:PC -->

**Rows: 169** (RESOLVED-BY 117 · SUPERSEDED 48 · STALE/FP 4 · DISPUTED 0 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-PC-13 | the duel and the grid round are not one path: no round entry, no approach | B | R-04 | `U5b:82` · `03_PC_audit.md:258` · `mc/wrapper.py:576-615`; addendum §B3 | RESOLVED-BY | PB as reconciled (§2 the round, §3 the approach, §7 the order), with RUL-PC §1 (the nesting ca… | B16, B15 | PC |
| 2 | F-PES-PC-01 | a fight is two blows | B | R-04, R-09 | `U5b:216` · `16_PESSIMIST_PC.md:650` · pessimist `pF_story.py` F1, `pK_scale2.py` | RESOLVED-BY | RUL-PC §4 (A-31: the damage scale lowered so a Success is one Wound Interval; obstacle left al… | B15 | PC |
| 3 | F-PC-01 | computed play almost never reaches personal combat, and never by a duel | B | R-05, R-09 | `U5b:67` · `03_PC_audit.md:124` · audit E7, E7b, E12 (`aperture 2 0`: `challenge` 84 of 84 refused, `fight` forme… | RESOLVED-BY | P1 (Exact edits: `referent_class: Person`, the person-side `dispute` decline, Record-kind form… | B37, B01, B21b | IN |
| 4 | F-PC-02 | every person is the same fighter | B | R-06, R-09 | `U5b:68` · `03_PC_audit.md:150` · audit E8 (83 of 83 default) | RESOLVED-BY | P4 Parts A–D as reconciled (home and schema are U1 §1–§3; the pool slot is two inputs, A-7); R… | B18, B15 | PC |
| 5 | F-PC-03 | a fight's consequences reach other subsystems only as a death and a body | D | R-01, R-07 | `U5b:69` · `03_PC_audit.md:163` · audit E3 (0 stance rows in 400 fights), E11 | RESOLVED-BY | P2 Part A (`DecisiveBeat`, `fell_to`); PES-C (the scene's shape, `fell_to_hand`); the survivor… | B10, B14 | IN |
| 6 | F-PES-PC-05 | the world keeps a verdict, not a fight | D | R-01, R-07 | `U5b:220` · `16_PESSIMIST_PC.md:682` · pessimist `pS_season.py` S1 | RESOLVED-BY | PES-C part 1 | B14 | PC |
| 7 | F-PC-14 | inside a fight an NPC is not an agent | D | R-06, R-08 | `U5b:83` · `03_PC_audit.md:278` · `mc/wrapper.py:586-592` (`decide=None`) | RESOLVED-BY | PB §5 (`choose.approach_of`, one decider per claimant); PES-A (the concession); P3 Part A (the… | B16, B15 | PC |
| 8 | F-PES-PC-06 | a killing in self-defence has no killer | D | R-07, R-08 | `U5b:221` · `16_PESSIMIST_PC.md:687` · pessimist `pS2.py` S7 | RESOLVED-BY | PES-C part 2 | B14 | PC |
| 9 | F-PC-04 | a plain `fight` is binary for its loser; the roll is top-heavy | D | R-09 | `U5b:70` · `03_PC_audit.md:177` · audit E3 (a death in 200 of 200), E5 | RESOLVED-BY | P3 Part B as reconciled (adopts PHY-A A3, the mortal-wound draw and `context_terms`); PES-A (t… | B16, B15 | PC |
| 10 | U5a F-DICE-14 Edit C | the fight's believed estimate | D |  | `U5b:254` · `10_DICE_audit.md:252` | RESOLVED-BY | RES-PC §8 | B14 | PC |
| 11 | F-PC-05 | the one in-fight choice is free, and only a played person has it | D |  | `U5b:71` · `03_PC_audit.md:186` · audit E6 (52.0% → 14.3%) | RESOLVED-BY | P3 Part A (the contested withdrawal); PB §4–§5 (every party has a decider) | B16 | PC |
| 12 | F-PC-12 | no unarmed fighter; "holds no arms" means an arming sword | D |  | `U5b:81` · `03_PC_audit.md:253` · audit E2 | RESOLVED-BY | P4 Part C | B18 | PC |
| 13 | F-PC-08 (c) | the Ob a person is attacked against reads the fallback and practice; SC's opposition reader excludes both | H |  | `U5b:76` · `03_PC_audit.md:215` · `mc/core.py:102-124` | RESOLVED-BY | CAP Part B row B5 (`opposed_ob`, one owner, one `opposition_rate`); RUL-PC §2 (what the combat… | B04, B15 | IN |
| 14 | F-PC-06 | the module returns an untyped dict; the seam returns twelve keys, the fold reads two; `winner` contradic… | H |  | `U5b:72` · `03_PC_audit.md:196` · audit E3 (11 of 200), E11 | RESOLVED-BY | P2 Part A as reconciled (the flip is replaced by 18-D's tracked riposte, so `result` and the t… | B14 | PC |
| 15 | F-PC-08 (a) | `core.resolve` inlines `net_boost` | H |  | `U5b:74` · `03_PC_audit.md:215` · audit E10 | RESOLVED-BY | P2 Part C, R-PC-17 | B14 | PC |
| 16 | F-PC-10 | 18 engine constants outside `CFG` and the export | H |  | `U5b:79` · `03_PC_audit.md:235` · addendum E-B1, E-B3 | SUPERSEDED | by F-PC-15 (addendum C-8: 64 constants and every weapon field); carried by PX and P2 Part C R-… | → B14 | PC |
| 17 | F-PC-11 | flat-module and prose debt (path inserts, dead citations, handoff pointers, CR-85 Status, the tempo flat… | H |  | `U5b:80` · `03_PC_audit.md:243` · audit E10 (16 dead citations) | RESOLVED-BY | P2 Part C (R-PC-15, R-PC-16); RES-PC §6 (the flat-top named on plan PC-08's Phase-C row; the w… | B14, held | PC |
| 18 | F-PC-15 | the export carries the weapons' names and nothing else | H |  | `U5b:185` · `03_PC_audit_addendum_B.md:75` · addendum E-B1 | RESOLVED-BY | PX | B14 | PC |
| 19 | F-PC-22 | six stale texts in instruments and comments | H |  | `U5b:192` · `03_PC_audit_addendum_B.md:150` · addendum E-B15 | RESOLVED-BY | RES-PC §5 (R-PC-39's edits, which no file carried) | B14 | PC |
| 20 | F-PC-23 | the workbench owns a third copy of the roll | H |  | `U5b:193` · `03_PC_audit_addendum_B.md:161` · `workbench/probabilities.py::degree_distribution` | RESOLVED-BY | P2 Part C as reconciled (R-PC-42 added beside R-PC-17) | B14 | PC |
| 21 | F-PES-PC-13 | extremes: same-id fight, fractional and negative faculty, a form as a kit | H |  | `U5b:228` · `16_PESSIMIST_PC.md:727` · `es/seam/wrappers/combat.py:257` | RESOLVED-BY | RES-PC §4 (the `PARTY-GAP` refusal); RUL-PC §2 edit 3 (the raw pool and its floor); PX item 4… | B14, B15 | PC |
| 22 | F-PC-08 (b) | nine bespoke Bernoulli or logistic gates beside the ladder | H |  | `U5b:75` · `03_PC_audit.md:215` · `mc/wrapper.py:344-357`, `:434`, `:622` | SUPERSEDED | the bands are ruled exempt (audit §5); the one gate that decided an outcome by fiat, the upset… | → B15 | PC |
| 23 | F-PC-08 (d) | `core.py:58` rounds the pool to an integer | H |  | `U5b:77` · `03_PC_audit.md:215` · `mc/core.py:58` (`int(round(faculty))`, re-read at HEAD) | RESOLVED-BY | RUL-PC §2 edit 3 (the pool is carried raw; A-5's bell curve takes a fractional pool) | B15 | PC |
| 24 | R-PC-01 | close H-98; re-point R-09's `blocks:` | — | R-09 | `U5b:117` | RESOLVED-BY | P2 Part C | B14 | PC |
| 25 | H-240 | `accept` binds a challenge: closed in mechanism, unreached | — |  | `U5b:106` · audit E7 | RESOLVED-BY | P1 edit 4 | B01 | IN |
| 26 | R-PC-06, R-PC-07, R-PC-08 | `challenge` on persons with a dispute; `accept` on challenge Records | — |  | `U5b:122` | RESOLVED-BY | P1 | B01 | IN |
| 27 | §13 NPC-010, NPC-035 (killable) | yes by hand | — |  | `U5b:160` · audit E3 | RESOLVED-BY | P1; `22_HAPPENINGS_C_*` (the context) | B01 | IN |
| 28 | U5c `challenge` | forms but is refused | — |  | `U5b:260` | RESOLVED-BY | P1 | B01 | IN |
| 29 | §11 item 2 | the one input to a combat pool and its obstacle | — |  | `U5b:143` · `DECISIONS_ANSWERED.md` A-6, A-7, A-8 | SUPERSEDED | answered: A-7 (two numbers), A-6 (score plus a base, floor five), A-8 (the wound); carried by… | → B04, B15 | IN |
| 30 | §13 ARC-53 (the wound degrades faction-… | in part | — |  | `U5b:152` · `es/seam/wrappers/pool.py:38-50` | RESOLVED-BY | CAP Part B row B6 and `10_DICE_advantage_sources_for_the_arcs.md` Edits B–D (A-8: a level agai… | B05, B04 | IN |
| 31 | §14 (a)–(e) the capability surface for… | slots; rule in code; doubled Ob; no carriers | — |  | `U5b:167` · audit §14 table | RESOLVED-BY | U1 §2–§4 and §8 (the home, the roles, the reader); P4 Part A; CAP Part B row B7 specified by R… | B18, B04, B15 | PC |
| 32 | §1.6 S (i) | one ladder centred at two places | — |  | `U5b:230` · pessimist `pJ_roll.py` | RESOLVED-BY | CAP Part B (one pool rule, one opposed divisor across combat and everything else, A-5/A-6/A-26… | B04, B15 | IN |
| 33 | PC-21, PC-22, CR-95 | design-first positions | — |  | `U5b:113` | SUPERSEDED | plan positions stand; CR-95's adverse body modifier is answered by A-8 (`10_DICE_advantage_sou… | → B05, B10 | IN |
| 34 | C-9 | a fight is never priced by believed odds in the chooser | — |  | `U5b:183` · `es/seam/wrappers/sigma.py` | RESOLVED-BY | RES-PC §8 (the `believed_chance` answer for the `personal_combat` band: the resolver sampled o… | B05, B14 | IN |
| 35 | F-PC-07 | one engine, two doors; the registered door is the narrower | — |  | `U5b:73` · `workbench/server.py:15-37`; `mc/fight.py:55-56` | RESOLVED-BY | P2 Part B | B14 | PC |
| 36 | F-PC-09 | the tradition, ability and lever layer is unreachable from the season and near-silent in the module | — |  | `U5b:78` · audit E5 (47.8% against a 46.1–49.3 band) | RESOLVED-BY | P4 Part A (the layer becomes authoring data composed host-side into `lever` and `skill` slots,… | B18, B14 | PC |
| 37 | H-98 | the fourth band | — |  | `U5b:95` · audit E3 (90 untouched, 110 wounded) | RESOLVED-BY | P2 Part C, R-PC-01 (register edit) | B14 | PC |
| 38 | H-119 | two degree surfaces | — |  | `U5b:96` · audit E3 | RESOLVED-BY | P2 Part A (the deleted keys); 18-D | B14 | PC |
| 39 | H-123 | wound magnitude; stale `site:` | — |  | `U5b:97` | RESOLVED-BY | P2 Part C, R-PC-15 | B14 | PC |
| 40 | H-184, H-258 | the Wounded edge; the lasting mark, closed as assumptions | — |  | `U5b:98` · `es/loop/effects_combat.py:394-424` | SUPERSEDED | H-258 by `audits/25_GROUNDING_ENGINE.md` G-22 (the mark is a certainty at the gate) and RES-PC… | → B14 | PC |
| 41 | H-251 | odds sample size; clients not opened | — |  | `U5b:99` · `seam/wrappers/sigma.py` (`believed_chance`) | SUPERSEDED | by addendum C-9 (opened: a fight is never priced by believed odds); carried by RES-PC §8 | → B14 | PC |
| 42 | H-266 | the log's gaps | — |  | `U5b:102` · audit E4 | RESOLVED-BY | P2 Part A, R-PC-05; PES-C | B14 | PC |
| 43 | H-348 | the victor reads `undecided` | — |  | `U5b:103` · audit E3 | RESOLVED-BY | P2 Part A (`standing`) | B14 | PC |
| 44 | H-64 | the probe corpus invented `fight` | — |  | `U5b:107` · audit §6.1 | STALE/FP | `fight` is a table row (`es/verb_table.yaml:733`); the row's own text marks the stale symbol;… | — (stale) | PC |
| 45 | CP-T03-06 | the survivor's grudge | — |  | `U5b:110` · pessimist `pS2.py` S7 | RESOLVED-BY | PES-C part 2 (the killer's name, which the regard needs first); the regard side is CHAR's (U5a) | B14 | PC |
| 46 | PC-06 K-5, PC-08 | leave | — |  | `U5b:115` | SUPERSEDED | accepted; PC-08 gains the flat-top by name (RES-PC §6) | → B14, held | PC |
| 47 | CR-85 build | built on an unratified design | — |  | `U5b:116` · `mc/attributes.py:29-37` | RESOLVED-BY | P2 Part C, R-PC-16 (Status line); the design question itself is answered by A-6, A-7, A-8 (RUL… | B14, B15 | PC |
| 48 | R-PC-02 | delete `winner`, `result`, `unresolved` from the seam | — |  | `U5b:118` · audit E11 | RESOLVED-BY | P2 Part A | B14 | PC |
| 49 | R-PC-04 | `standing` in `fight_endings` | — |  | `U5b:120` | RESOLVED-BY | P2 Part A | B14 | PC |
| 50 | R-PC-05 | H-266 corrected; carry the decisive beat | — |  | `U5b:121` | RESOLVED-BY | P2 Part A | B14 | PC |
| 51 | R-PC-09 | a frozen `CombatOutcome` | — |  | `U5b:123` | RESOLVED-BY | P2 Part A | B14 | PC |
| 52 | R-PC-10 | widen the record; workbench through the entry; trace sink a parameter | — |  | `U5b:124` | RESOLVED-BY | P2 Part B | B14 | PC |
| 53 | R-PC-12 | a starter inventory and seeding | — |  | `U5b:126` | RESOLVED-BY | P4 Parts B, D (content `[ASSUMPTION]`, Jordan's to correct; admitted only with RES-PC §3's cen… | B18, B14 | PC |
| 54 | R-PC-15, R-PC-16, R-PC-17, R-PC-18, R-P… | stale locators; CR-85 Status; `net_boost`; constants into `CFG`; `state_graph.py` docstring | — |  | `U5b:129` | RESOLVED-BY | P2 Part C | B14 | PC |
| 55 | R-PC-19 | the tradition layer recorded as oracle-side; no edit | — |  | `U5b:130` | RESOLVED-BY | P4 Part A (the slot interface makes the layer authoring data); plan PC-21 | B18, B14 | PC |
| 56 | R-PC-21 | the tempo flat-top folded into PC-08 by name | — |  | `U5b:131` · `mc/combat_systems.py:107-113` | RESOLVED-BY | RES-PC §6 (the plan-row edit, which no file carried) | B14 | PC |
| 57 | §11 item 3 | is any matchup certain? | — |  | `U5b:144` · 18-D | SUPERSEDED | answered by the standing rule (sweep D-11, C-13); carried by 18-D (decided fights), PES-D (arm… | → B14, B15 | PC |
| 58 | C-7 | `DuelState` has a fifth field; an adapter holds nothing | — |  | `U5b:181` · addendum E-B7 | RESOLVED-BY | PB §2; PF (which removes the fifth field if it lands first) | B16, B14 | PC |
| 59 | C-8 | 64 constants and every weapon field are outside the export | — |  | `U5b:182` · addendum E-B1, E-B3 | RESOLVED-BY | PX | B14 | PC |
| 60 | F-PC-16 | the half-sword form persists across engagements | — |  | `U5b:186` · addendum E-B7, E-B8 | RESOLVED-BY | PF | B14 | PC |
| 61 | F-PC-20 | the roster MB proposes as the only one is melee only | — |  | `U5b:190` · addendum E-B1 | RESOLVED-BY | PX item 6 (pike as content; ranged classes carry `mass` only until a ranged resolution exists) | B14 | PC |
| 62 | F-PC-21 | four skill axes are real, two are not; the weapon erases the build | — |  | `U5b:191` · addendum E-B5 | RESOLVED-BY | P4 Part A as reconciled (R-PC-43: `technique` and `grab` are not exposed as slots until a swee… | B18, B14 | PC |
| 63 | §B7 | the loadout rule's individual side: three amendments | — |  | `U5b:199` · addendum E-B1 | RESOLVED-BY | PL as reconciled; PX item 6 | B14, B18 | PC |
| 64 | R-PC-36, R-PC-37, R-PC-38 | the export's sections; forms; ranged | — |  | `U5b:203` | RESOLVED-BY | PX | B14 | PC |
| 65 | R-PC-39 | six stale texts | — |  | `U5b:204` | RESOLVED-BY | RES-PC §5 | B14 | PC |
| 66 | R-PC-42 | the workbench re-derives the roll | — |  | `U5b:207` | RESOLVED-BY | P2 Part C as reconciled | B14 | PC |
| 67 | R-PC-43 | two skill axes move nothing; skills uncapped | — |  | `U5b:208` | RESOLVED-BY | P4 Part A as reconciled; RES-PC §1 | B18, B14 | PC |
| 68 | F-PES-PC-08 | one attribute outweighs the levers the intent names | — |  | `U5b:223` · pessimist `pN_att.py` | RESOLVED-BY | RES-PC §1 (R-7: isolate the term, lift the read's literal scale into `CFG`, the slope bound as… | B14 | PC |
| 69 | F-PES-PC-09 | eight false or narrowed N-lines | — |  | `U5b:224` · pessimist `pE_cuts2.py`, `pE3_default.py` | RESOLVED-BY | no edit of its own; it is the evidence for the order (RUL-PC §5) and for what the port does no… | B15, B14 | PC |
| 70 | F-PES-PC-10 | names that promise events the engine does not have | — |  | `U5b:225` · pessimist §1.3 | RESOLVED-BY | RES-PC §2 (the grapple's names); P2 Part A (`standing`); "first blood" is restated by PES-A's… | B14, B15 | PC |
| 71 | F-PES-PC-12 | a spear against a sword is 99.2 to 99.8% | — |  | `U5b:227` · pessimist `pE_cuts_base800.txt` | RESOLVED-BY | RES-PC §3 (R-9: the census gates each weapon's admission to `arms_kinds`) | B14 | PC |
| 72 | §3.7 stories that cannot happen | twelve rows | — |  | `U5b:233` | SUPERSEDED | each row is closed by the finding it cites (ambush: RUL-PC §6; yield: PES-A; refused surrender… | → B16, B18, B14, B15 | PC |
| 73 | §5 standing-rule table | ten fixed functions of state | — |  | `U5b:234` | SUPERSEDED | each row by its named carrier above; the lasting mark by RES-PC §7; one point of `arms` per fi… | → B14 | PC |
| 74 | R-5 | the scene's shape and `fell_to_hand` | — |  | `U5b:238` | RESOLVED-BY | PES-C | B14 | PC |
| 75 | R-7 | a slope bound; the read's scale into `CFG` | — |  | `U5b:240` · `mc/combat_systems.py:1145` | RESOLVED-BY | RES-PC §1 | B14 | PC |
| 76 | R-8 | the grapple's names | — |  | `U5b:241` · `mc/contact.py:60-77` | RESOLVED-BY | RES-PC §2 | B14 | PC |
| 77 | R-9 | a census before `arms_kinds` is populated | — |  | `U5b:242` | RESOLVED-BY | RES-PC §3; P4 Part B as reconciled | B18, B14 | PC |
| 78 | R-10 | `resolve` takes the same-id refusal | — |  | `U5b:243` · `es/seam/wrappers/combat.py:257` | RESOLVED-BY | RES-PC §4 | B14 | PC |
| 79 | U5a C5 | a second unseeded-generator fallback at `mc/wrapper.py:565` | — |  | `U5b:252` | RESOLVED-BY | RES-PC §4 edit 2 (`rng` required; re-read at HEAD: `rng=rng or random.Random()`) | B14 | PC |
| 80 | U5a H-264 | (PC's) | — |  | `U5b:257` | RESOLVED-BY | RES-PC §9 (register rows this family owns, by id) | B14 | PC |
| 81 | U5a tests §4 | PC's ten all-conditional loops | — |  | `U5b:258` | RESOLVED-BY | RES-PC §10 | B14 | PC |
| 82 | R-PC-26 | one `carry_demand` leaf; `in_hand`; `switch` | — |  | `U5b:136` | RESOLVED-BY | PL as reconciled (addendum §B7's three amendments; the unit side is `04_MB_unit_loadout_and_we… | B17, B18 | MB |
| 83 | §B6 | what the chooser must do to pick an approach | — |  | `U5b:198` · `es/decision/choose.py:193-197`, `:441-454` | RESOLVED-BY | PB §5, step 4; the CHAR loader-rule sentence ("refuse a key outside `CHOICE_RANGES`") is CHAR'… | B10, B16 | IN |
| 84 | §5 a wound's persistence | `party_end` cuts Endurance by band; the tracker starts clean | — |  | `U5b:90` · `es/seam/wrappers/combat.py:143-152` | RESOLVED-BY | RUL-PC §3 (A-8: the carried wound is a level against the wounded fighter's rolls, the Enduranc… | B15 | PC |
| 85 | §5 the beaten yield, flee or die | plain `fight` is lethal | — |  | `U5b:91` · audit E3 | RESOLVED-BY | P3 Part B as reconciled; PES-A | B16, B15 | PC |
| 86 | H-97 | body lands on `end` (assumption) | — |  | `U5b:94` · `combat.py:143-152` | RESOLVED-BY | RUL-PC §3 (A-8 answers what the CR-85 §4 step 2 question was waiting on) | B15, B39 | PC |
| 87 | H-263 | no exit but death | — |  | `U5b:100` · audit E3 | RESOLVED-BY | P3 Part B as reconciled; PES-A | B16, B15 | PC |
| 88 | H-349 | none against light armour, not re-measured | — |  | `U5b:104` · pessimist `pC_armour.py` | SUPERSEDED | by `16_PESSIMIST_PC.md` §2.3 (re-measured: light is worth 1.5 points; plate is a certainty), c… | → B15 | PC |
| 89 | CL-SLICE | ratified design, no client | — |  | `U5b:112` · `PlayHost(` constructed only at `es/tests/test_rem31_grid_suspension.py:80` | RESOLVED-BY | audit §8 step 4 on the round entry (PB step 1), ordered in RUL-PC §5 | B16, B15 | PC |
| 90 | R-PC-25 | the field's adapter calls `combat.round` on a contact | — |  | `U5b:135` · addendum F-PC-19 | SUPERSEDED | by R-PC-30 and A-4: the field module is handed a `duel` callable and the call is a nested cont… | → B16, B15 | PC |
| 91 | §11 item 1 | does a beaten fighter in a plain `fight` have an exit? | — |  | `U5b:142` · P3:102-117 | SUPERSEDED | answered by the standing rule (`audits/18_DETERMINISM_SWEEP.md` D-04) and A-16; carried by P3… | → B16, B15 | PC |
| 92 | named: the suspension and the grid map | a grid battle cannot run inside one decider | — |  | `U5b:145` · `architecture/meta/04_CODE_ARCHITECTURE.md:811` | SUPERSEDED | by addendum C-4/R-PC-33 (one build: the cell field at weight 1, one provider call) and A-9 (a… | → B16, B15 | PC |
| 93 | named: CR-85 §4 step 2 | a round entry needs carried damage, which is held | — |  | `U5b:147` | SUPERSEDED | A-4 took nesting (the state stays in the calling frame, no carrier in the world); between scen… | → B15 | PC |
| 94 | named: NPC-088, ARC-31 against ED-IN-03… | a killing with no institutional context | — |  | `U5b:150` · `DECISIONS_ANSWERED.md` A-16 | SUPERSEDED | by A-16 (yes, rarely; lifts the conflict for criminal contexts); carried by `22_HAPPENINGS_C_a… | → B37, B15 | IN |
| 95 | §13 ARC-23 (capture over death) | yes at personal scale | — |  | `U5b:157` · audit E4 | RESOLVED-BY | PHY-A A1–A3; P3 Part B; inside a battle PB step 5 | B16, B15 | PC |
| 96 | §13 SCN-14 (a personal action inside a… | no | — |  | `U5b:165` | RESOLVED-BY | PB step 5; RUL-PC §1; RUL-MB | B16, B15, B19 | PC |
| 97 | §15 (a)–(e) NPCs and the chooser in a f… | hard-coded NPC rules in module and seam | — |  | `U5b:169` · audit §15 (c) | RESOLVED-BY | PB §5; PES-A; P3 Part A | B16, B15 | PC |
| 98 | F-PC-17 | the monotone advantage of aggression is the initiative drift | — |  | `U5b:187` · addendum E-B10 | RESOLVED-BY | PB §3, step 3e; composed with PES-B (the deep tier) in RUL-PC §5 | B16, B15 | PC |
| 99 | §B4 row 1 | the adapter row: person-supplied callables | — |  | `U5b:194` · `es/seam/wrappers/combat.py:331-332` | SUPERSEDED | by A-4 (read as one declared class of adapter input); the declaration is RUL-PC §1 edit 3 | → B15 | PC |
| 100 | §B4 row 2 | nested resolution under §39.3 | — |  | `U5b:195` · `holonic_ARCHITECTURE.md:1397-1402` | SUPERSEDED | by A-4 (option (a): a nested contest, counted against the cap); the cap's default is RUL-PC §1… | → B15 | PC |
| 101 | §B10 item 4 | is intensity a declared term or only a lean? | — |  | `U5b:209` · `DECISIONS_ANSWERED.md` ladder table | SUPERSEDED | by the ladder (D-40: A now; B behind a dial at zero, set after D-39); PB step 3c; RUL-PC §5 | → B16, B15 | PC |
| 102 | F-PES-PC-02 | the per-phase approach has nothing to decide | — |  | `U5b:217` · pessimist `pP_window.py`, `pI_approach2.py` | RESOLVED-BY | PES-B, then RUL-PC §4, then PB step 3 with the added gate (R-6), in the order RUL-PC §5 fixes | B16, B15 | PC |
| 103 | F-PES-PC-03 | whether a wounded man gives up is a threshold | — |  | `U5b:218` · pessimist `pB_yield.py` | RESOLVED-BY | PES-A | B15 | PC |
| 104 | F-PES-PC-04 | the commit window is [2, 4.03]; the deep tier sits at 4.0 | — |  | `U5b:219` · pessimist `pF_story.py` F3 | RESOLVED-BY | PES-B | B15 | PC |
| 105 | F-PES-PC-07 | armour is an average; its top step is a certainty | — |  | `U5b:222` · pessimist `pC_armour.py`, `pQ2_gap.py` | RESOLVED-BY | PES-D | B15 | PC |
| 106 | F-PES-PC-11 | the opener has no edge, and neither does the watch | — |  | `U5b:226` · pessimist `pL_misc.py`, `pS_season.py` S2 | RESOLVED-BY | RUL-PC §6 (D-41 B: a first-exchange level on an opener the target did not expect); the watch:… | B15 | PC |
| 107 | §1.6 S (ii)–(v) | armour an average; the yield a threshold; "deep" an absolute; two verbs for taking a man | — |  | `U5b:231` | RESOLVED-BY | PES-D; PES-A; PES-B; PHY-A A1–A2 | B15 | PC |
| 108 | R-1, R-2 | the yield is a draw; NPC concession no longer Jordan's | — |  | `U5b:235` | RESOLVED-BY | PES-A | B15 | PC |
| 109 | R-3 | the tier follows the window | — |  | `U5b:236` | RESOLVED-BY | PES-B | B15 | PC |
| 110 | R-4 | the bare zone drawn per blow | — |  | `U5b:237` | RESOLVED-BY | PES-D | B15 | PC |
| 111 | R-6 | the approach is built after PES-B and J-1 | — |  | `U5b:239` | RESOLVED-BY | PB §7 as reconciled (the order and the added gate); RUL-PC §5 | B16, B15 | PC |
| 112 | R-11 | the twelve-turn cap kept | — |  | `U5b:244` | SUPERSEDED | by the 2026-06-02 ruling (an undecided fight is legitimate); PES-D makes it rarer | → B15 | PC |
| 113 | J-1 | how long is a fight? | — |  | `U5b:245` · `DECISIONS_ANSWERED.md` A-31 | SUPERSEDED | answered: A-31 (B, longer); RUL-PC §4 | → B15 | PC |
| 114 | J-2 | does opening a fight give an edge? | — |  | `U5b:246` · `DECISIONS_ANSWERED.md` ladder table | SUPERSEDED | answered by the ladder: D-41 B, following A-16; RUL-PC §6 | → B15 | PC |
| 115 | U5a CAP row B7 | combat's pool and attribute terms as the same two inputs | — |  | `U5b:253` | RESOLVED-BY | RUL-PC §2 | B15 | PC |
| 116 | U5a sweep C-12 | a felling is a death | — |  | `U5b:259` | RESOLVED-BY | PHY-A A3 (adopted by P3 Part B) | B16, B15 | PC |
| 117 | §5 the player decides once per engageme… | one binary choice per turn | — |  | `U5b:93` · addendum §B3 | SUPERSEDED | by the 2026-11-12 intent and R-PC-27/R-PC-40 (three approaches over three phases); carried by… | → B16 | PC |
| 118 | H-304, H-338, H-340 | filed under PC by path; `_eff_tend`, `_eff_forgive` | — |  | `U5b:109` | SUPERSEDED | H-304 by P3 Part C as reconciled (`tend` a graded draw); H-338 and H-340 by CHAR's closure (U5… | → B16 | PC |
| 119 | R-PC-11 | the turn-level withdrawal through `disengage_clean_p` and the pursuit strike | — |  | `U5b:125` | RESOLVED-BY | P3 Part A | B16 | PC |
| 120 | R-PC-14 | `tend` restores a body whole | — |  | `U5b:128` · `effects_combat.py:766-790` | RESOLVED-BY | P3 Part C as reconciled (D-05: a graded draw through 18-A's route) | B16 | PC |
| 121 | R-PC-22 | expose the engagement as `fight.round` with a `DuelState` | — |  | `U5b:132` | RESOLVED-BY | PB §2, step 1 (state in the calling loop's frame, R-PC-30) | B16 | PC |
| 122 | R-PC-23 | three approaches as a lean on the disposition hooks | — |  | `U5b:133` · addendum F-PC-17 | SUPERSEDED | by R-PC-28 (own coefficients; the drift never moved); PB §3 | → B16 | PC |
| 123 | R-PC-24 | per-party deciders | — |  | `U5b:134` | RESOLVED-BY | PB §5, step 4 | B16 | PC |
| 124 | named: ED-PC-0007's reopen condition | three approaches are a menu | — |  | `U5b:148` · `DECISIONS_ANSWERED.md` ladder table, D-40 | SUPERSEDED | the condition is met by Jordan's own intent of 2026-11-12 and D-40 (leans first, the transfer… | → B16 | PC |
| 125 | §13 SCN-03 (two recoveries) | no | — |  | `U5b:154` | RESOLVED-BY | P3 Part C as reconciled | B16 | PC |
| 126 | §13 SCN-03, SCN-01 (channelled action;… | no; design-first with WR | — |  | `U5b:156` | SUPERSEDED | WR's closure (U5d) owns the mechanism; PC's precondition (round state) is PB §2 | → B16 | PC |
| 127 | §13 ARC-23 (a commander's incapacitatio… | no | — |  | `U5b:158` | RESOLVED-BY | PB step 5 (the contact result) with RUL-MB (what the field does with it); see Part 2 | B16, B19 | PC |
| 128 | C-1 | the off-hand slot is a closed scope call, not a gap | — |  | `U5b:175` · `mc/core.py:217-220` | SUPERSEDED | by ED-PC-0055's last row (R-PC-35); no edit; P5 §1's "no off-hand or shield slot" is marked in… | → B16 | PC |
| 129 | C-2 | the test is exact equality, not agreement in expectation | — |  | `U5b:176` · `architecture/meta/03_VERBS_AND_LOOPS.md:146-153` | RESOLVED-BY | PB step 4 (R-PC-32); A-1 confirms Layer 1 §27.2 and §C.4 unchanged | B16 | PC |
| 130 | C-3 | the free withdrawal is a one-agent-kind breach | — |  | `U5b:177` | RESOLVED-BY | P3 Part A as reconciled (its ground restated) | B16 | PC |
| 131 | C-4 | the grid is one build | — |  | `U5b:178` · `04_CODE_ARCHITECTURE.md:811` | RESOLVED-BY | PB §4 (the cell field at weight 1) | B16 | PC |
| 132 | C-6 | disposition is monotone because of one hook | — |  | `U5b:180` · addendum E-B4, E-B10 | RESOLVED-BY | PB step 3e (`DISP_INIT_K = 0`) | B16 | PC |
| 133 | F-PC-18 | "phase" is the engagement's own phase | — |  | `U5b:188` · `systems/combat/combat_engine_v1/state_graph.py::INJECTION_POINTS` | RESOLVED-BY | PB §3–§4 (R-PC-27) | B16 | PC |
| 134 | F-PC-19 | round state on an adapter cannot be built | — |  | `U5b:189` · `architecture/holonic_ARCHITECTURE.md:1679-1686` | RESOLVED-BY | PB §2, §4 (R-PC-30); A-4 | B16 | PC |
| 135 | R-PC-27 … R-PC-34 | phase, own coefficients, drift, state in the frame, form, exact gate, one grid, the person's decider | — |  | `U5b:201` | RESOLVED-BY | PB §2–§5, §7 | B16 | PC |
| 136 | R-PC-40 | cadence and "is disposition a trade" | — |  | `U5b:205` | SUPERSEDED | answered by the 2026-11-12 intent; PB | → B16 | PC |
| 137 | §B10 named: ED-IN-0304, J-15 | risk appetite as the temperament carrier; one act or scenes | — |  | `U5b:210` | SUPERSEDED | ED-IN-0304 stays CHAR's open ask (no new carrier, PB §8.6); J-15 is answered for the nested ca… | → B16 | PC |
| 138 | U5a DICE addendum §5.2 | the duel round from the dice side (an approach is an `edge` row, never a pool rule) | — |  | `U5b:255` | RESOLVED-BY | PB §3 (a lean is a prior on a gate; no pool term) | B16 | PC |
| 139 | §5 every fighter differs | mechanisms present, sources empty | — |  | `U5b:92` · audit E8 | RESOLVED-BY | P4 | B18 | PC |
| 140 | H-265 | no unarmed fighter | — |  | `U5b:101` · audit E2 | RESOLVED-BY | P4 Part C | B18 | PC |
| 141 | H-350 | one kit for all | — |  | `U5b:105` · audit E8 | RESOLVED-BY | P4 Part B | B18 | PC |
| 142 | PC-06 K-1 | landed, unreached | — |  | `U5b:114` · audit E8 | RESOLVED-BY | P4 Part D | B18 | PC |
| 143 | R-PC-13 | an `unarmed` record | — |  | `U5b:127` | RESOLVED-BY | P4 Part C | B18 | PC |
| 144 | §13 SCN-03 (incapacitation varies by at… | in the module; unreached | — |  | `U5b:153` · audit E5, E8 | RESOLVED-BY | P4 Part D | B18 | PC |
| 145 | §13 NPC-006 (high combat stats, no numb… | wrongly stated | — |  | `U5b:162` | RESOLVED-BY | P4 Part D (authored attributes and an `arms` key on his cast entry; values are content) | B18 | PC |
| 146 | U5a DICE addendum §5.3 | the carry cost is the `threshold` role, one leaf | — |  | `U5b:256` | RESOLVED-BY | PL | B18 | PC |
| 147 | §5 "no matchup is ever certain" | the cap moves `result`; the fold reads trackers | — |  | `U5b:89` · `mc/wrapper.py:618-624` (re-read at HEAD) | RESOLVED-BY | 18-D (the riposte through the one damage site) | — | PC |
| 148 | H-147, H-212, H-342, H-355, H-360 | filed under PC by path; subject is `_eff_march` | — |  | `U5b:108` | SUPERSEDED | closed in Part 2 (MB) of this file | — | PC |
| 149 | CP-T03-10, CP-T03-11 | rescue parked; guards cut | — |  | `U5b:111` · plan card | SUPERSEDED | accepted as the plan records them; no edit | — | PC |
| 150 | R-PC-03 | keep the flip as the workbench's rule; a comment | — |  | `U5b:119` · 18-D "Exact edits" 3 | SUPERSEDED | by 18-D edit 3 (the flip is deleted; the comment edit is replaced) and survivor 3's closure be… | — | PC |
| 151 | named: R-04's grid reading | two builds | — |  | `U5b:146` · `04_CODE_ARCHITECTURE.md:811` | STALE/FP | Layer 1 names it one build (addendum C-4) | — (stale) | PC |
| 152 | named: `videogame_mode_spec.md` zones,… | no grid; a simplified formula | — |  | `U5b:149` | SUPERSEDED | by Layer 1 §27.2 and `04:811` (R-PC-41), and A-1 | — | PC |
| 153 | §13 ARC-53 (persisting injury; recovery… | represented | — |  | `U5b:151` · audit E3, E7 | STALE/FP | not a defect: the audit's own "yes" rows; no edit | — (stale) | PC |
| 154 | §13 SCN-03 (a second depleting resource) | inside a fight only | — |  | `U5b:155` · `mc/wrapper.py:286-288` | STALE/FP | represented for the fight; the case's season reading is not PC's need (audit's own row) | — (stale) | PC |
| 155 | §13 ARC-23 (a skill gates an attempt) | wrongly stated against Layer 1 | — |  | `U5b:159` · `DECISIONS_ANSWERED.md` A-11 | SUPERSEDED | by A-11 (training never gates; the need is re-read as "far likelier") | — | PC |
| 156 | §13 NPC-088 (found and killed with no i… | conflicts with a ruling | — |  | `U5b:161` | SUPERSEDED | by A-16 | — | PC |
| 157 | §13 NPC-040, ARC-16, NPC-081/020/031/00… | not PC's mechanism | — |  | `U5b:163` | SUPERSEDED | CHAR (U5a), FA (U5d), SC (U5c) closures | — | PC |
| 158 | §13 ARC-31 (a covert lethal attempt in… | no | — |  | `U5b:164` | SUPERSEDED | A-16 supplies the attempt (`22_HAPPENINGS_C_*`); the interruption of a proceeding is SC's (U5c) | — | PC |
| 159 | §13 ARC-07 | not PC | — |  | `U5b:166` | SUPERSEDED | Part 2 (MB) of this file; A-2 | — | PC |
| 160 | §14 (d) item 10 | "a capability may gate an attempt" is refused by Layer 1 | — |  | `U5b:168` | SUPERSEDED | A-11 confirms the refusal | — | PC |
| 161 | C-5 | `videogame_mode_spec.md` is superseded on both points | — |  | `U5b:179` | SUPERSEDED | Layer 1; A-1; no edit (R-PC-41) | — | PC |
| 162 | C-10 | the FFT precedent is in the held proposal's Appendix A, unsurveyed | — |  | `U5b:184` | SUPERSEDED | recorded as a null; nothing is built from it (addendum §B3 "Against the research") | — | PC |
| 163 | §B4 row 3 | the upset flip after the engagement | — |  | `U5b:196` | RESOLVED-BY | 18-D | — | PC |
| 164 | §B4 row 4 | the quarantined auto-resolve formula | — |  | `U5b:197` | SUPERSEDED | Layer 1 §27.2; A-1 | — | PC |
| 165 | §B7 fourth matter | which weapons may be carried where (carry context) | — |  | `U5b:200` | SUPERSEDED | held with `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` §12… | — | PC |
| 166 | R-PC-35 | off-hand closed | — |  | `U5b:202` | SUPERSEDED | ED-PC-0055 | — | PC |
| 167 | R-PC-41 | `videogame_mode_spec.md` | — |  | `U5b:206` | SUPERSEDED | Layer 1; A-1 | — | PC |
| 168 | §1.4 N-lines 1–8 | each quoted necessity, cut | — |  | `U5b:229` | SUPERSEDED | by F-PES-PC-09's closure | — | PC |
| 169 | §2.5 premises nobody asked for | the opener; disarm/throw/pin; the watch; `undecided`; first blood | — |  | `U5b:232` | SUPERSEDED | by F-PES-PC-10 and F-PES-PC-11's closures | — | PC |

---

## MB — mass battle

<!-- SYNTHESIS:MB -->

**Rows: 146** (RESOLVED-BY 104 · SUPERSEDED 39 · STALE/FP 3 · DISPUTED 0 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-GO-02 | the float contract | B |  | `U5b:447` · `11_GO_audit.md:142` | SUPERSEDED | A-29; `11_GO_float_contract.md` (U5d's); TO §1 quantises the field's shares at the seam | → B06, B17 | IN |
| 2 | F-GO-03 | draws are built in two places | B |  | `U5b:448` · `11_GO_audit.md:176` | SUPERSEDED | A-30; `11_GO_one_draw_owner.md` (U5d's); this family's streams (the per-round stream, the nest… | → B06 | IN |
| 3 | F-MB-01 | the shipped scale does not resolve a battle | B |  | `U5b:285` · `04_MB_audit.md:182` · audit §12 (attacker loses 60 of 60 below a block) | RESOLVED-BY | HG (one scale owner, `under_arms_cap`; R-01, R-16); a field of named persons only goes to the… | B19, B17 | MB |
| 4 | F-MB-02 | the headcount path's survivor ratio is not a ratio | B |  | `U5b:286` · `04_MB_audit.md:205` · audit §12 (70 of 289 losers above 1.0; bodies 1000 → 20) | RESOLVED-BY | HG (`hp / hp_max`; the loser's write capped) | B17 | MB |
| 5 | F-MB-03 | nothing in natural play reaches the engine; no choice surface is on | B |  | `U5b:287` · `04_MB_audit.md:229` · `aperture 2 0` (`field.won`, `field.lost` never emitted) | RESOLVED-BY | PLAY §E as reconciled (one fixture, `armies_at_build`); MIL-C and MIL-D (a commander forms the… | B07, B20, B22 | IN |
| 6 | F-MB-05 | the standalone and the season battle are two code paths | B |  | `U5b:289` · `04_MB_audit.md:268` · reach probe (16 of 48 functions entered by no season arm) | RESOLVED-BY | TO §2; confirmed as Layer 1 §27.2 conformance by A-1 | B17 | MB |
| 7 | F-MB-19 | loadout is not read; no second weapon; the weapon in hand is not a state | B |  | `U5b:303` · `04_MB_audit.md:492` · audit §12 (byte-identical under three loadouts) | RESOLVED-BY | LOAD-B (stages 1–4) with PL on the person's side | B18, B17 | PC |
| 8 | F-GO-04 | 91 mass-battle tunables read from the environment | B |  | `U5b:449` · `11_GO_audit.md:204` | SUPERSEDED | the same finding as F-MB-09; TO §3 | → B17 | MB |
| 9 | `audits/11_GO_audit.md` F-GO-01 | the pinned slices barely enter combat and mass battle | B |  | `U5b:446` · `11_GO_audit.md:115` | SUPERSEDED | U5d's closure owns GO; this family's part is the two calibration batches' re-records (RUL-PC §… | → B15, B19 | PC |
| 10 | F-GO-08, F-GO-18 | PLAYABLE exists at one seam | B |  | `U5b:450` · `11_GO_audit.md:310` | SUPERSEDED | U5d's closure; this family's carriers are PB §4 (the duel), MGR §4 (the field) and SQD (the sq… | → B16, B20, B30 | PC |
| 11 | F-MB-20 | at season scale the cell grid is not the battlefield | B |  | `U5b:370` · `04_MB_audit_addendum_B.md:155` · addendum `generators_probe`, `density_probe` | RESOLVED-BY | HIER §2 (R-32) with 26-SCALE §1–§2 | B19 | MB |
| 12 | F-MB-21 | two of the three army strategies lose to the third | B |  | `U5b:371` · `04_MB_audit_addendum_B.md:200` · addendum `lever_probe` (20 to 77; 30 to 56) | RESOLVED-BY | MGR §3 (R-34); the cause is PART's (the pair rule read through three strategies) | B20, B19 | MB |
| 13 | F-PES-MB-01 | an army divided into units loses to the same men in one block | B |  | `U5b:408` · `16_PESSIMIST_MB.md:605` · pessimist `p15_shape.py` (0 of 60 against 36) | RESOLVED-BY | PART (edits 1–4; the PARTITION row), as CR12's step 3 | B19 | MB |
| 14 | F-PES-MB-02 | the field is decided by one draw made before it, over a rule that is a cliff | B |  | `U5b:409` · `16_PESSIMIST_MB.md:634` · pessimist `p1_size.py` | SUPERSEDED | the rule under the draw: PART; the draw itself is answered by A-59 (lowered, and tested for re… | → B19 | MB |
| 15 | F-PES-MB-03 | a rout has no exit | B |  | `U5b:410` · `16_PESSIMIST_MB.md:648` · pessimist `p6_rout.py` | RESOLVED-BY | ROUT as reconciled; 26-ROUT §3–§5 | B19 | MB |
| 16 | F-MB-14 | individuals' attributes do not reach the battle | B |  | `U5b:298` · `04_MB_audit.md:400` · `mb/massbattle.py:184-188` | RESOLVED-BY | 27-MB (A-59: command from a learned skill and social and mental attributes; each unit's own pr… | B20, B22 | MB |
| 17 | F-MB-15 | no intervention during a battle and no account afterwards | B |  | `U5b:299` · `04_MB_audit.md:417` · `mb/massbattle.py:425-427` | RESOLVED-BY | MGR §4–§6 (it supersedes PLAY §B's decider return); bouts and lulls: 26-SCALE §3 | B20 | MB |
| 18 | F-MB-26 | the manager's vocabulary has no carrier in the season | B |  | `U5b:376` · `04_MB_audit_addendum_B.md:323` · `mb/armyrecord.py:13-19` | RESOLVED-BY | MGR §2 (R-39); 26-MAN | B20 | MB |
| 19 | U5a F-DICE-18 (C-7) | a field battle reads no person | B |  | `U5b:437` · `10_DICE_audit_addendum_B.md:224` | RESOLVED-BY | 27-MB (A-59) | — | MB |
| 20 | F-MB-04 | a field neither side wins is written as the attacker's defeat | D |  | `U5b:288` · `04_MB_audit.md:253` · audit §12 (10 `Failure`, 14 `Partial`, all `Lost` at the seam) | RESOLVED-BY | HG (the `Drawn` band) with MGR §1 (A-3: the host reads the end state) | B17, B20 | MB |
| 21 | F-MB-06 | the seam drops what the battle knows; the outcome is an untyped dict | D |  | `U5b:290` · `04_MB_audit.md:288` · `mb/massbattle.py:465-470` | RESOLVED-BY | TO §1 as reconciled (no `verdict`); the report: MGR §6, PLAY §D | B17, B20 | MB |
| 22 | F-MB-16 | the non-player commander is a script; the player sees what no NPC may | D |  | `U5b:300` · `04_MB_audit.md:433` · `harness/army_presets.py:17-20` | RESOLVED-BY | MIL-C, MIL-D (he forms the six verbs through the one chooser); doctrines as data: LOAD-B's tro… | B17, B22 | MB |
| 23 | F-MB-18 | two role shapes do not survive the first tick; per-cell morale comes loose | D |  | `U5b:302` · `04_MB_audit.md:472` · audit §12 (the one-tick probe) | RESOLVED-BY | RES-MB §9 (R-24; R-25, which 26-MOVE §4 carries in fact) | B17 | MB |
| 24 | F-MB-22 | troop types that differ only by weapon are one type | D |  | `U5b:372` · `04_MB_audit_addendum_B.md:248` · addendum `pike_probe` (440 of 440) | RESOLVED-BY | LOAD-B §2 (reach and support depth from the arm in hand) after HIER §2 | B19, B17 | MB |
| 25 | F-PES-MB-07 | the pike is a name | D |  | `U5b:414` · `16_PESSIMIST_MB.md:699` · pessimist `p4_pike.py` (60 of 60 identical) | RESOLVED-BY | LOAD-B (its falsifier with depth added) after HIER and PART | B19, B17 | MB |
| 26 | F-PES-MB-09 | the people a field touches are ground to a thousandth | D |  | `U5b:416` · `16_PESSIMIST_MB.md:718` · pessimist `p8_season.py` | RESOLVED-BY | HG; TO; SQD (their own rounds, not a headcount share) | B17, B30 | MB |
| 27 | U5a F-DICE-14 Edit C | the field's believed estimate | D |  | `U5b:441` · `10_DICE_audit.md:252` | RESOLVED-BY | RES-MB §5 | B17 | MB |
| 28 | F-MB-07 | CR-12 is parked on a question the ledger answered, behind an instrument that cannot read its exit | D |  | `U5b:291` · `04_MB_audit.md:307` · `registers/editorial_ledger_mb_archive.jsonl:73` | RESOLVED-BY | CR12 (steps 1–3) with PART as its step 3. The question it turns on (D-35) is answered: A-60, n… | B19 | MB |
| 29 | F-MB-17 | the hierarchy is three levels, not four | D |  | `U5b:301` · `04_MB_audit.md:449` · `proposals/2026-09-25-squad-engagement-concept-v5.md:7` | SUPERSEDED | by addendum C-1 (three containers and an arrangement; no level is missing); HIER §1 (R-30); A-2 | → B19 | MB |
| 30 | F-PES-MB-04 | integer armour against integer power makes whole match-ups certain | D |  | `U5b:411` · `16_PESSIMIST_MB.md:657` · pessimist `p10_edges.py` (60 of 60) | RESOLVED-BY | PART edit 3 | B19 | MB |
| 31 | F-PES-MB-05 | a flanked line breaks no sooner; an encircled one never | D |  | `U5b:412` · `16_PESSIMIST_MB.md:685` · pessimist `p2_flank.py` | RESOLVED-BY | PART gate 4; 26-ROUT §1 (the stand draw on a body struck in flank or rear; A-61 confirms it be… | B19 | MB |
| 32 | F-PES-MB-06 | two stamina ledgers | D |  | `U5b:413` · `16_PESSIMIST_MB.md:692` · pessimist `p5_tired.py` | RESOLVED-BY | STAM | B19 | MB |
| 33 | F-MB-11 | after a won field the loser stays and the winner stands beside him | D |  | `U5b:295` · `04_MB_audit.md:376` · `es/loop/effects_combat.py:532-536` | SUPERSEDED | by A-57 and A-58: on land another holds, an aggressor's win passes the land and its seats (LAN… | → B20, B23 | MB |
| 34 | F-MB-08 | a ruled magnitude (friction) swamps every choice | D |  | `U5b:292` · `04_MB_audit.md:325` · pessimist `p1_size.py` (the higher draw wins 275 of 287) | SUPERSEDED | answered: A-59 (D-34): the day's luck is lowered once order friction exists, and a static side… | — | MB |
| 35 | F-MB-09 | hidden inputs and held state in a registered module | H |  | `U5b:293` · `04_MB_audit.md:340` · 91 `os.environ` reads (addendum §B7, confirmed) | RESOLVED-BY | TO §3 (one frozen `EngineConfig`; the unused registry mutators deleted); the float half is A-2… | B06, B17 | IN |
| 36 | F-MB-10 | dead and unreached code | H |  | `U5b:294` · `04_MB_audit.md:355` · audit §3 | RESOLVED-BY | TO §2 (stubs, no-ops, the second pool owner); RES-MB §1 (the one role list); `rally_check` is… | B17, B19 | MB |
| 37 | F-MB-12 | surfaces that disagree with the code | H |  | `U5b:296` · `04_MB_audit.md:384` | RESOLVED-BY | RES-MB §2 (R-12, R-13, R-14); TO (R-15); HG (R-16) | B17 | MB |
| 38 | F-MB-23 | troop behaviour is keyed on type names | H |  | `U5b:373` · `04_MB_audit_addendum_B.md:272` · `mb/hierarchy/units.py:943`, `:1491` | RESOLVED-BY | LOAD-B stage 2 (four columns) | B17 | MB |
| 39 | F-MB-25 | reference surfaces that say the opposite of the code | H |  | `U5b:375` · `04_MB_audit_addendum_B.md:311` · `mb/config.py:262-272` | RESOLVED-BY | RES-MB §2 (R-37, R-38, R-43) | B17 | MB |
| 40 | F-PES-MB-08 | nine role rows do nothing, two do harm, one name is false | H |  | `U5b:415` · `16_PESSIMIST_MB.md:706` · pessimist `p10_edges.py` (b) | RESOLVED-BY | RES-MB §1 | B17 | MB |
| 41 | U5a F-DICE-21 (C-8) | the field speaks sigma in die-equivalents and tires twice | H |  | `U5b:438` · `10_DICE_audit_addendum_B.md:285` | RESOLVED-BY | RUL-MB §1 edit 1; STAM | B19 | MB |
| 42 | U5a F-PES-DICE-09 | the field's four stat checks are bare binaries | H |  | `U5b:440` · `16_PESSIMIST_DICE.md:562` | RESOLVED-BY | ROUT (rally graded; recall); 26-ROUT §1 (the stand draw); 26-MAN (the feint's three draws); ea… | B19 | MB |
| 43 | F-MB-13 | the choice surfaces are priced wrongly for the chooser | H |  | `U5b:297` · `04_MB_audit.md:392` · H-361 | RESOLVED-BY | PLAY §E (`marshal` fans `retreat_at` only); MIL-C Edit 5 (the one opportunity-key edit) | B20, B22 | MB |
| 44 | C-5 | the two ladders differ at 6 of 10,000 cells | — |  | `U5b:365` · `audits/10_DICE_audit.md` F-DICE-07 (by title) | RESOLVED-BY | RUL-MB §1 edit 1 (the module calls the owner; A-5); DOE §1 (U5a's) | B05, B19 | IN |
| 45 | §5.2 the stub is the shipped path | `_weighted_unit` at one troop a weight | — |  | `U5b:310` | RESOLVED-BY | HG | B17 | MB |
| 46 | §5.2 M11 against CR-24 | winners never depleted (design) against `engine` shipped | — |  | `U5b:311` | RESOLVED-BY | RES-MB §2 (R-13) | B17 | MB |
| 47 | §5.4 NERS cuts | `_weighted_unit` at k 1 dies; the `marshal` role dies on a headcount line; `run_multi_unit_battle` moves… | — |  | `U5b:314` | RESOLVED-BY | HG; PLAY §E; TO §2; HG | B17, B20 | MB |
| 48 | §5.5 design that is only prose | pursuit, captives, march supply, the troop stock, a general who decides, terrain choice, tactic cards, m… | — |  | `U5b:315` | RESOLVED-BY | ROUT and 26-ROUT (pursuit; the dead and the taken; captives through PHY-A's custody); 26-MOVE… | B17, B19, B15 | MB |
| 49 | H-151 | same-faction march | — |  | `U5b:317` · audit §6.1 | STALE/FP | closed at HEAD (`es/loop/sides.py:159-160`); register edit RES-MB §2 | — (stale) | MB |
| 50 | H-250 | the scale | — |  | `U5b:318` | RESOLVED-BY | HG | B17 | MB |
| 51 | H-308 | fortification is a step as shipped | — |  | `U5b:319` · audit `walls_probe.py` | RESOLVED-BY | HG (`field_walls_dr=3`); its unit becomes dice with PART edit 3 | B17, B19 | MB |
| 52 | H-354 | mutual rout graded a loss | — |  | `U5b:320` | RESOLVED-BY | HG; MGR §1 | B17, B20 | MB |
| 53 | H-359 | one body or commanding persons | — |  | `U5b:321` | RESOLVED-BY | HG (`person` shipped); SQD for a field of persons only | B17, B30 | MB |
| 54 | H-361 | a role against its orderer | — |  | `U5b:323` | RESOLVED-BY | PLAY §E; RES-MB §1; PART (the pair rule is why the levers invert) | B17, B20, B19 | MB |
| 55 | H-355, H-360 | where the beaten side goes; the shipped winner write unseen by a test | — |  | `U5b:324` | RESOLVED-BY | H-355: LAND with PLAY §G (A-57, A-58); H-360: TO gate 4 | B17, B20, B23 | MB |
| 56 | CL-TROOP, MB-08, CR-52, CP-T04-04, CP-T… | plan rows | — |  | `U5b:325` | RESOLVED-BY | RES-MB §7; R-23 in RES-MB §2 | B17 | MB |
| 57 | R-01, R-02, R-03, R-16, R-18, R-19 | one scale; one share; `Drawn`; one deployment; graded walls; `person` | — |  | `U5b:327` | RESOLVED-BY | HG as reconciled (R-03's verdict is read host-side) | B17 | MB |
| 58 | R-04, R-05, R-08, R-09, R-15, R-21, R-26 | the typed outcome; one path; `EngineConfig`; stubs; the resolver label; the docstring; `rally_check` kept | — |  | `U5b:328` | RESOLVED-BY | TO as reconciled | B17 | MB |
| 59 | R-07 | presets at build; a training Site a seat; levy as a line | — |  | `U5b:330` | RESOLVED-BY | PLAY §E as reconciled; RES-MB §3 (R-44: Sites where the venues are) | B17, B20 | MB |
| 60 | R-10 | roles with no primitive leave the menu | — |  | `U5b:331` | RESOLVED-BY | RES-MB §1 (merged with F-PES-MB-08) | B17 | MB |
| 61 | R-12, R-13, R-14, R-23, R-28 | pointer and status edits | — |  | `U5b:333` | RESOLVED-BY | RES-MB §2 | B17 | MB |
| 62 | R-24, R-25, R-29 | `GappedLine`'s minimum; the morale maps re-keyed; the truncated-troops figure | — |  | `U5b:335` | RESOLVED-BY | RES-MB §9 | B17 | MB |
| 63 | R-27 | one weapon roster, personal combat's | — |  | `U5b:336` · addendum §B7 (no missile weapon, pike or lance in the personal roster) | SUPERSEDED | by addendum C-3 and R-36 (one owner a fact, not one file); LOAD-B §2 | → B17 | MB |
| 64 | §13 ARC-07 (five needs) | a rare sub-outcome persists; a condition on a unit; the reason for staying; a distinct resolving act; a… | — |  | `U5b:340` | RESOLVED-BY | TO §1 (parts, `broke_first`); A-2 (the condition is claims in the men's ledgers); PLAY §G and… | B17, B20, B31, B23, B22 | MB |
| 65 | §13 ARC-43, ARC-20, ARC-45, ARC-11, NPC… | fields that arise from persons' acts; commanders whose command is material | — |  | `U5b:342` | RESOLVED-BY | PLAY §E; MIL-C, MIL-D; TO (per-cohort shares) | B17, B20, B22 | MB |
| 66 | §14 (a)–(e) capability surface | Command a literal; troop tables in Python; two stat systems; the roller re-implemented | — |  | `U5b:346` | RESOLVED-BY | 27-MB (command; a unit's prowess from its own row); LOAD-B stage 1 (the troop file); RUL-MB §1… | B19, B17 | MB |
| 67 | §16 (a)–(e) the NPC surface | who decides; the estimate is the player's; doctrine a script | — |  | `U5b:350` | RESOLVED-BY | MIL-C, MIL-D; RES-MB §5; CHAR's cells on fanned payload values (U5a) | B17, B22 | MB |
| 68 | §16 named: AQ-X1 | "no NPC reads" the estimate | — |  | `U5b:351` · `es/seam/wrappers/mass_battle.py:465-466` | RESOLVED-BY | RES-MB §5 (an NPC reckons on what he believes, never on the world) | B17 | MB |
| 69 | §18.2 "no character death from mass bat… | the `total` casualty arm kills | — |  | `U5b:353` | RESOLVED-BY | RES-MB §2 is extended at landing by one roster note (the `total` arm labelled a control that c… | B17 | MB |
| 70 | C-3 | the roster merge has nowhere to go | — |  | `U5b:363` · addendum §B7 | RESOLVED-BY | LOAD-B §2 (R-36) | B17 | MB |
| 71 | §B2.3 "armour is unwired; `dr` a free s… | still true | — |  | `U5b:378` · `mb/orchestration.py:1360-1366` | RESOLVED-BY | PART edit 3 (armour and walls shift the roll); LOAD-B (`armour` on the troop row) | B17, B19 | MB |
| 72 | §B2.3 "the shipped default has no regre… | `[UNVERIFIED]` | — |  | `U5b:379` | SUPERSEDED | by the first audit §4.5 (disclosed by design: the golden modes pin flags off; the seed-2 pin i… | → B17 | MB |
| 73 | §B5.1 rows | the duel in a field; what a duel does to the field; squads; the carry rule; the weapon in hand; the appr… | — |  | `U5b:385` | RESOLVED-BY | MGR §7 as reconciled; SQD; PL as reconciled (`carry_demand_of`); LOAD-B §4; the approach roste… | B18, B20, B17, B30 | PC |
| 74 | §B5.2 rows | a reason for war; training Sites; supply; upkeep; veterancy; the march's cost; captives | — |  | `U5b:386` | RESOLVED-BY | PHY-B B1 and FA (U5d); RES-MB §3; ECON as reconciled (RUL-MB §5); 26-MOVE §3; 26-ROUT §4 with… | B19, B17, B31, B22, B15 | MB |
| 75 | R-35, R-36 | columns for the name tests; one owner a fact | — |  | `U5b:395` | RESOLVED-BY | LOAD-B | B17 | MB |
| 76 | R-37, R-38, R-43 | stale surfaces; the Layer 1 pointer (IN's); the dead skeleton | — |  | `U5b:396` | RESOLVED-BY | RES-MB §2 | B17 | MB |
| 77 | R-44 | Sites where the venues are | — |  | `U5b:399` | RESOLVED-BY | RES-MB §3 | B17 | MB |
| 78 | §1.1 false N-lines (seven rows) | each cut, executed | — |  | `U5b:417` | SUPERSEDED | by the findings that carry them (the unit ledger: STAM; the pike: LOAD-B; nine role rows: RES-… | → B17, B20, B19 | MB |
| 79 | §1.3 the resolution diagnostic (P-i to… | two live bands; reachable zeros; leverage falling with pool; no legible odds; an undamped loop | — |  | `U5b:418` · pessimist `t2.py` | RESOLVED-BY | PART edits 2–3; RUL-MB §1; RES-MB §5 (odds a commander can state) | B19, B17 | MB |
| 80 | §3.3 extremes | nobody against nobody; past the ceiling | — |  | `U5b:422` · pessimist `p11_extremes.py` | RESOLVED-BY | RES-MB §6 | B17 | MB |
| 81 | §3.4 stories that cannot happen | ten rows | — |  | `U5b:423` | SUPERSEDED | each by the finding its missing link names (PART; MGR; LOAD-B; STAM and 26-MOVE; ROUT; ECON) | → B20, B17, B31, B19 | MB |
| 82 | res. 7 | inert roles off the menu | — |  | `U5b:427` | RESOLVED-BY | RES-MB §1 | B17 | MB |
| 83 | res. 9 | pike and heavy infantry identical at depth | — |  | `U5b:429` | RESOLVED-BY | LOAD-B | B17 | MB |
| 84 | U5a res. 22 | the survivor-ratio labels use the ladder's four names | — |  | `U5b:439` | RESOLVED-BY | HG (the four-way `degree` is deleted) | B17 | MB |
| 85 | U5a sweep C-06 | a defended field is lost by the attacker 60 of 60 | — |  | `U5b:442` | RESOLVED-BY | HG | B17 | MB |
| 86 | U5a F-TEST-10 row 6; tests §4 | the standing `xfail`; `approx` on conservation | — |  | `U5b:443` | RESOLVED-BY | RES-MB §4 | B17 | MB |
| 87 | §15 duels in and around a field | no edge; the squad scale; between engagements; at the end | — |  | `U5b:347` | RESOLVED-BY | SQD as reconciled; RUL-MB §3; `capture` on `field.won` through PHY-A | B19, B30, B15 | MB |
| 88 | §5.3 CR-12 judged | the diagnosis is right; the build is not ready | — |  | `U5b:313` | RESOLVED-BY | CR12 step 1 (the instrument first) | B19 | MB |
| 89 | §5.7 the cell approach judged | "army → subformation → cell, the officer makes a subformation a unit" | — |  | `U5b:316` | SUPERSEDED | by addendum C-1; HIER §1; MGR §7 | → B20, B19 | MB |
| 90 | R-06 | CR-12: numbers out of the melee dice | — |  | `U5b:329` | RESOLVED-BY | CR12 (A-60) | B19 | MB |
| 91 | §11 item 1 | CR-12: do numbers stay in the melee dice | — |  | `U5b:339` | SUPERSEDED | answered: A-60 (option (a)); CR12 is the carrier | → B19 | MB |
| 92 | §13 ARC-23, SCN-14 | phases within a battle; a commander's incapacitation; a personal act inside a battle | — |  | `U5b:341` | RESOLVED-BY | 26-SCALE §3 (bouts and lulls); MGR §7 as reconciled with RUL-MB §3 (the nested duel; an office… | B19, B20 | MB |
| 93 | §15 shared geometry | may one module import another | — |  | `U5b:349` | SUPERSEDED | no module imports another: the squad entry is handed a callable (RUL-MB §3); the engine leaf i… | → B19 | MB |
| 94 | C-1 | the four words are three containers and an arrangement | — |  | `U5b:361` · addendum §B3.1 | RESOLVED-BY | HIER §1 (R-30); A-2 | B19 | MB |
| 95 | C-7 | on every season constructor the cell is filled to the cap | — |  | `U5b:367` · addendum `cells_probe` | RESOLVED-BY | HIER §2 with 26-SCALE §1 | B19 | MB |
| 96 | C-9 | `rally_check` is the commander's hook, with more than a rally | — |  | `U5b:369` | RESOLVED-BY | MGR §4 (`rally` as a general's action); ROUT (the end-of-field draw) | B20, B19 | MB |
| 97 | §B2.3 re-verified old findings (17 rows… | each "still true" or "now false" | — |  | `U5b:377` · addendum §B2.3 | SUPERSEDED | each by the finding or resolution its row names (F-MB-18, -20, -23, -26; R-29; ROUT for pursui… | → B19 | MB |
| 98 | §B2.3 "two contradictory ranged DR tabl… | `[UNVERIFIED]` | — |  | `U5b:380` | SUPERSEDED | by PART edit 3 (no table is subtracted from damage); the two tables were opened by no lane and… | → B19 | MB |
| 99 | §B3.4 | a minimum cells floor, or a UI | — |  | `U5b:381` | RESOLVED-BY | HIER §2 (neither: an explicit grid at the calibrated density) | B19 | MB |
| 100 | §B3.6 | more than one troop kind in a unit | — |  | `U5b:382` | RESOLVED-BY | HIER §4 (`bands`, staged last) | B19 | MB |
| 101 | §B4.6 | the squad of named characters | — |  | `U5b:384` | RESOLVED-BY | SQD as reconciled (a registered entry, RUL-MB §3) | B19, B30 | MB |
| 102 | §B5.3 | the shared roller: three notes | — |  | `U5b:387` | RESOLVED-BY | RUL-MB §1 and §6 row 4 (the sampler lands first in the batch; one re-record) | B19 | MB |
| 103 | R-30 | "unit" and "subformation" | — |  | `U5b:391` | RESOLVED-BY | HIER §1 | B19 | MB |
| 104 | R-32, R-33 | ranks-by-files bodies; formations as rows | — |  | `U5b:393` | RESOLVED-BY | HIER §2, §3 | B19 | MB |
| 105 | R-42 | veterancy and upkeep | — |  | `U5b:398` | RESOLVED-BY | ECON as reconciled (RUL-MB §5) | B19, B31 | MB |
| 106 | §1.4 S | walls as armour; the opposed-roll obstacle; a LogNormal where siblings use capped levels | — |  | `U5b:419` | RESOLVED-BY | PART edit 3 and edit 2; the multiplier is A-59's (27-MB) | B19 | MB |
| 107 | res. 1–4 | the partition requirement; pay by own net; armour shifts the roll; a cell's strength divided among its p… | — |  | `U5b:424` | RESOLVED-BY | PART as reconciled (the net is the one sampler's) | B19 | MB |
| 108 | res. 5 | rally and pursuit as two draws | — |  | `U5b:425` | RESOLVED-BY | ROUT as reconciled | B19 | MB |
| 109 | res. 6 | one ledger | — |  | `U5b:426` | RESOLVED-BY | STAM | B19 | MB |
| 110 | res. 8 | CR-12's exit gains the partition row | — |  | `U5b:428` | RESOLVED-BY | PART; CR12 as reconciled | B19 | MB |
| 111 | U5a DOE §1 row 4 | the module's sampler becomes the owner's | — |  | `U5b:436` | RESOLVED-BY | RUL-MB §1 | B19 | MB |
| 112 | §3.A "one cell resolver" | yes for the resolver, no for the battle | — |  | `U5b:304` | RESOLVED-BY | MGR §5 (delegated, commanded and replayed are one call); A-1 | B20 | MB |
| 113 | R-11 | where the beaten side goes | — |  | `U5b:332` | SUPERSEDED | in part by A-57 and A-58 (title now moves on an aggressor's win: LAND); its third clause (a ro… | → B20, B23 | MB |
| 114 | R-17, R-20, R-22 | the `marshal` fan and the army-verb key; MB-08's march half; a win clears a morale row | — |  | `U5b:334` | RESOLVED-BY | PLAY §E, §G; MIL-C Edit 5; PHY-B B1 | B20, B22 | MB |
| 115 | §13 NPC-089 | three graduated postures | — |  | `U5b:343` | RESOLVED-BY | PHY-B B1 (one Candidate a posture); `besiege` un-withheld by PLAY A/C; a probing posture is FA… | B20, B22 | MB |
| 116 | §17 named conflicts | attributes against the 2026-07-08 directive; intervention against ED-IN-0301; legible cause against fric… | — |  | `U5b:352` | SUPERSEDED | (1) A-59: command sets the odds of an order taking effect; whether an officer's command also r… | → B20 | MB |
| 117 | C-2 | an even engagement is decisive for one body, drawn for an army | — |  | `U5b:362` · addendum `mirror_probe` | RESOLVED-BY | PLAY as reconciled (its evidence is corrected by A26 R-5); 26-SCALE §3 | B20 | MB |
| 118 | C-4 | two of the three strategies a decider would choose are traps | — |  | `U5b:364` · addendum `lever_probe` | RESOLVED-BY | MGR §3, §4 | B20 | MB |
| 119 | C-6 | Layer 1 does not accept a returned winner | — |  | `U5b:366` | SUPERSEDED | answered by A-3 (an end state, read by the host); MGR §1 | → B20 | MB |
| 120 | F-MB-24 | the field returns a winner | — |  | `U5b:374` · `es/seam/ladder.py:198-222` | SUPERSEDED | answered by A-3; MGR §1 (R-31) | → B20 | MB |
| 121 | §B4.3–§B4.5 | standing orders; the general's action; the report | — |  | `U5b:383` | RESOLVED-BY | MGR §2, §4, §6 as reconciled; 26-MAN §1 (an order takes effect by a draw) | B20 | MB |
| 122 | R-31 | the end state in place of a winner | — |  | `U5b:392` | RESOLVED-BY | MGR §1 | B20 | MB |
| 123 | R-34, R-39, R-40, R-45 | strategy off the choice surface; standing orders; officers; the estimate | — |  | `U5b:394` | RESOLVED-BY | MGR §3, §2, §7, §8 | B20 | MB |
| 124 | §3.2 a dead-end loop | one person forms the same refused march 15 times in a season | — |  | `U5b:421` · pessimist `p8_s0_k30.txt` | RESOLVED-BY | PHY-B B1 (the `Field` class makes the wrong-kind target unformable); MIL-A Edit 6's shape for… | B22 | MB |
| 125 | U5a CHAR §10; NPC-089 | the officer's keys on the input; more than one posture | — |  | `U5b:444` | RESOLVED-BY | 27-MB; PHY-B B1 | B22 | MB |
| 126 | U5d H-158; C-2; C-3 | upkeep; the withheld verbs; the FA→MB interface | — |  | `U5b:445` | RESOLVED-BY | ECON; MIL-C Edit 7 and MIL-D Edit 6; ECON | B31, B22 | MB |
| 127 | R-41 | where the squad lives | — |  | `U5b:397` | RESOLVED-BY | SQD as reconciled | B30 | MB |
| 128 | §5.2 a field graded on the one ladder | "acceptable: `field_degree` is one owner" | — |  | `U5b:312` · `04_CODE_ARCHITECTURE.md:786` | SUPERSEDED | by addendum C-6 / F-MB-24 and A-3 | — | MB |
| 129 | H-150, H-256 | garrison strength; the loyalty row | — |  | `U5b:322` | SUPERSEDED | H-150 closed in mechanism; H-256 is CHAR's (U5a) | — | MB |
| 130 | CP-T04-02/05/06/07 | repairs, closed | — |  | `U5b:326` · audit §6.1 | STALE/FP | closed at HEAD per the audit's reading of the code paths; no edit | — (stale) | MB |
| 131 | §9 conflict 1; §11 item 2 | friction at sigma 1.1 against "choices change what happens" | — |  | `U5b:337` | SUPERSEDED | answered: A-59 (the audit's option (b), taken further); 27-MB | — | MB |
| 132 | §9 conflict 2 | same-round resolution against a defender's turn | — |  | `U5b:338` | SUPERSEDED | no conflict once `Drawn` exists (the audit's own reading); bouts inside the scene: 26-SCALE §3… | — | MB |
| 133 | §13 NPC-070, ARC-47, ARC-43 (the fixed… | not MB's mechanism | — |  | `U5b:344` | SUPERSEDED | CHAR (U5a), FA and WR (U5d) closures | — | MB |
| 134 | §13 "needs wrongly stated" | SCN-14's suspended command; ARC-07's unit condition; three UNCLEAR needs | — |  | `U5b:345` | SUPERSEDED | read as the audit reads them (a commander's attention is spent or not per bout; claims in ledg… | — | MB |
| 135 | §15 named conflicts | one engine against a dispatch by scale; §C.5.1 against a squad | — |  | `U5b:348` | SUPERSEDED | A-1 (the ruling is about played and delegated resolution of one contest); A-4; the squad is th… | — | MB |
| 136 | §18.2 levy cannot campaign | the design confines levy to its home territory; the code does not | — |  | `U5b:354` | SUPERSEDED | not adopted by the audit (R-07 keeps levy as a line); named for FA (U5d); no ruling orders it | — | MB |
| 137 | §18.3 earlier audits | five entries, re-verified where relied on | — |  | `U5b:355` | SUPERSEDED | by addendum §B2.3's fuller re-verification, closed in 2.3 | — | MB |
| 138 | C-8 | Ogre Battle unsourced; more of Bannerlord sourced | — |  | `U5b:368` · the audit's own Grounded note | STALE/FP | sourced since (`audits/24_GROUNDING_GAMES.md` GM-01 to GM-03; `research/game_precedent_suite/g… | — (stale) | MB |
| 139 | §B5.4 (a) | "no second resolver" against "fight or auto-resolve" | — |  | `U5b:388` | SUPERSEDED | answered by A-1 | — | MB |
| 140 | §B5.4 (b) | "no unit class" against the nested structure | — |  | `U5b:389` | SUPERSEDED | answered by A-2 | — | MB |
| 141 | §B5.4 (c) | the field returns a winner | — |  | `U5b:390` | SUPERSEDED | answered by A-3 | — | MB |
| 142 | §B11 item 1 | auto-resolve: a mode or a calculation | — |  | `U5b:400` | SUPERSEDED | answered: A-1 | — | MB |
| 143 | §B11 item 2 | a unit: a row or a thing | — |  | `U5b:401` | SUPERSEDED | answered: A-2 | — | MB |
| 144 | §B11 item 3 | what a field returns | — |  | `U5b:402` | SUPERSEDED | answered: A-3 | — | MB |
| 145 | §2.8 the five premises | larger usually wins; a flanked line breaks; pikes hold; tired fights worse; rallied or pursued | — |  | `U5b:420` | SUPERSEDED | by F-PES-MB-01 to -07, each closed above | — | MB |
| 146 | §5 survivor | friction: keep it, or move its seat | — |  | `U5b:430` | SUPERSEDED | answered: A-59 (option (b): its seat moves to the named draws) | — | MB |

---

## SC — social contest and proceedings

<!-- SYNTHESIS:SC -->

**Rows: 154** (RESOLVED-BY 135 · SUPERSEDED 14 · STALE/FP 3 · DISPUTED 2 · JORDAN 0).

| # | id | claim | sev | R | evidence | disposition | carrier | batch | owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F-PES-SC-05 | the verdict reads nothing of the hearing | B | R-02, R-05, R-09 | `U5c:203` · `16_PESSIMIST_SC.md:653` · `p1_petitioner.py` | RESOLVED-BY | OBS; EVID with ADM; `05_SC_acquittal.md`; HEAR | B27, B05, B24 | SC |
| 2 | F-PES-SC-07 | a hearing ends by exhaustion only | B | R-02, R-04 | `U5c:205` · `16_PESSIMIST_SC.md:667` · `p3_hearing_ends.py` | RESOLVED-BY | `05_SC_acquittal.md` (C-08); RES §4 (one asking per sitting; the re-opening rule; the `lapsed`… | B27 | SC |
| 3 | F-SC-01 | a proceeding rarely closes; nothing said in it decides it | B | R-04, R-05 | `U5c:51` · `05_SC_audit.md:153` · audit §1 runs (3 determined of 27 opened, seeds 0–1); re-executed with controls… | RESOLVED-BY | plan B10-18c (CR-57…CR-64) for intake; `05_SC_acquittal.md` as reconciled (C-08) for the losin… | B27, B05, B24, B24a | SC |
| 4 | F-SC-02 | two owners of one subsystem; the played one is not run | B |  | `U5c:52` · `05_SC_audit.md:175` · audit §12 run 9 (four test importers, no engine importer) | RESOLVED-BY | KERN (supersedes `05_SC_sc05_kernel_retirement.md`, whose edits 1–6 it keeps) | B24 | SC |
| 5 | F-SC-07 | no decision inside a social contest | B |  | `U5c:57` · `05_SC_audit.md:235` · `sigma.py:459-460` | RESOLVED-BY | HEAR (six moves, one decider interface); EVID edit 6 (`cites` variants) | B24 | SC |
| 6 | F-SC-15 | the proposed played hearing is on the wrong side of a ruled boundary | B |  | `U5c:123` · `05_SC_audit_addendum_B.md:144` · `ED-IN-0285`, `ED-IN-0349` | RESOLVED-BY | HEAR | B24 | SC |
| 7 | F-SC-04 | the roll that decided a contest is not in the log | D | R-01, R-02 | `U5c:54` · `05_SC_audit.md:204` · `loop/resolve.py:406, :866`; H-284 | RESOLVED-BY | `05_SC_contest_record_on_event.md` as reconciled (C-06: `terms` and `levels` replace `room`) | B05 | IN |
| 8 | F-PES-SC-11 | proceedings begin without a readable reason | D | R-01, R-07 | `U5c:209` · `16_PESSIMIST_SC.md:699` · `e1_reasons.py` | RESOLVED-BY | `16_PESSIMIST_GAME_standing_occasions_carry_their_cause.md` and `02_CHAR_offer_what_can_be_don… | B09, B10 | IN |
| 9 | F-PES-SC-03 | a verdict names the judge, not the party | D | R-01, R-02, R-07 | `U5c:201` · `16_PESSIMIST_SC.md:638` · `p4_verdict.py` | RESOLVED-BY | PES-C | B27 | SC |
| 10 | F-SC-16 | at the shipped arm, evidence is inert against a strong opponent | D | R-02, R-06 | `U5c:124` · `05_SC_audit_addendum_B.md:149` · addendum §B7 run 3; PES-SC §1.5 | RESOLVED-BY | OBS §3 (evidence as levels: no ceiling clip, no floor saturation); gate reproduced from PES-A'… | B05 | IN |
| 11 | F-SC-08 | most social acts die before the roll; a failed one costs nothing | D | R-02, R-08 | `U5c:58` · `05_SC_audit.md:242` · aperture 2 0 (31 of 41 `argue` refused) | RESOLVED-BY | formation: `02_CHAR_offer_what_can_be_done.md` (U5a's family; cited, not re-closed); failure e… | B10, B27, B24, B11 | IN |
| 12 | F-SC-05 | one terminal state; speech does not reach it; `Tenure.degree` unread | D | R-02 | `U5c:55` · `05_SC_audit.md:212` · H-162 (c); `faction_q.py:146` | RESOLVED-BY | (a) `05_SC_acquittal.md` (C-08); (b) HEAR edit 7 and EVID edit 4 (filed stages); (c) `05_SC_ar… | B27, B24 | SC |
| 13 | F-SC-14 | evidence is typed where held and a scalar where used | D | R-02, R-07 | `U5c:64` · `05_SC_audit.md:269` · `world_q.py:852-879` | RESOLVED-BY | EVID (supersedes `05_SC_evidence_and_rebuttal.md`) with ADM and `08_FI_05_evidence-interface_B… | B24 | SC |
| 14 | F-PES-SC-08 | only an accusation can be granted; the grant is the judge's; the accused is the addressee | D | R-02, R-04 | `U5c:206` · `16_PESSIMIST_SC.md:675` · 14 of 14 petitions `terms == to` | RESOLVED-BY | RES §5 | B27 | SC |
| 15 | F-SC-13 | the chooser does not weigh a speech; the verdict does not read the judge | D | R-06, R-08 | `U5c:63` · `05_SC_audit.md:254` · `choose.py:154-162` | RESOLVED-BY | EVID/ADM (a `speak` writes stages at every band, so `_writing_bands` prices it); CAPS (`determ… | B05, B24, B04 | IN |
| 16 | F-PES-SC-10 | the lie's roll reads neither party; its content is a fixed function | D | R-06, R-09 | `U5c:208` · `16_PESSIMIST_SC.md:690` · `p2e_roll_check.py` | RESOLVED-BY | CAPS (`deception`, opposed by perception); PES-E edit 2 (two directions, the liar's sampled ch… | B05, B04, B11 | IN |
| 17 | F-SC-03 | every realm roll is 2 dice against Ob 2; equal opponents drift | D | R-06, R-09 | `U5c:53` · `05_SC_audit.md:189` · audit §12 run 8; 13 §3.2 (270 of 284 one cell) | RESOLVED-BY | OBS (difficulty, opposition through `opposed_ob`, the stand-in); `02_CHAR_*` cast seating is C… | B05 | IN |
| 18 | F-PES-SC-04 | what the speaker brings rides two ladders | D | R-06, R-09 | `U5c:202` · `16_PESSIMIST_SC.md:646` · `n1_favour_two_ladders.py` | RESOLVED-BY | PES-A, generalised by OBS §3 to every favourable term | B05 | IN |
| 19 | F-SC-20 | every design on file averages the bench | D | R-06 | `U5c:128` · `05_SC_audit_addendum_B.md:190` · `declared_votes` | RESOLVED-BY | HEAR (`Seat`, `ballots`); RES §6 (the ballot has one owner, the module's close; C-11) | B27, B24 | SC |
| 20 | F-PES-SC-06 | an argument moves somebody 0.07 of the time; repetition is free | D | R-06, R-07, R-09 | `U5c:204` · `16_PESSIMIST_SC.md:661` · `p5_argue.py` | RESOLVED-BY | PES-D; the Proposition's content is `02_CHAR_which_ground_moves_whom.md` and FA's `utter` form… | B24, B27 | SC |
| 21 | F-PES-SC-01 | one ledger, two beliefs | D | R-07, R-08 | `U5c:199` · `16_PESSIMIST_SC.md:621` · `p2c_two_readers.py` | RESOLVED-BY | PES-B | B09 | IN |
| 22 | F-PES-SC-02 | an honest teller is marked a liar | D | R-07, R-08, R-09 | `U5c:200` · `16_PESSIMIST_SC.md:631` · `p2_lie.py` | RESOLVED-BY | PES-E edit 1 | B11 | FI |
| 23 | F-SC-06 | arrangement rows are read by the loader and by nothing that plays | D |  | `U5c:56` · `05_SC_audit.md:226` · audit §12 runs 10–11 | RESOLVED-BY | plan CR-60/CR-61 (a computed case names its row); `05_SC_arrangement_rows_that_bind.md` edit 5… | B27, B05, B24, B24a | SC |
| 24 | F-SC-17 | Layer 1's named fault and issue ladder are absent | D |  | `U5c:125` · `05_SC_audit_addendum_B.md:161` · `holonic` §2 T7, §54.3 | RESOLVED-BY | HEAR edits 1, 3 (`issue_rungs`, `hearing_faults`) | B24 | SC |
| 25 | F-PES-SC-09 | the room is necessary to nothing | D |  | `U5c:207` · `16_PESSIMIST_SC.md:683` · `n2_cuts.py` | RESOLVED-BY | HEAR edit 7; EVID edit 4; ADM | B24 | SC |
| 26 | F-PES-SC-12 | words that do not mean what they say | H |  | `U5c:210` · `16_PESSIMIST_SC.md:704` · PES-SC §2.5 | RESOLVED-BY | PES-D (`argument.held`); `argument.refused` at Success: RES §7; `release` offered under `detai… | B27, B24, B21 | SC |
| 27 | F-SC-09 | `reception` and `proofs` read other persons' ledgers at RESOLVE (F8) | H |  | `U5c:59` · `05_SC_audit.md:277` · `world_q.py:833-848, :877-879`; `04` §B.2 F8 | RESOLVED-BY | plan SC-02 (design `proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md`, `ED-SC-0… | B27, B24 | SC |
| 28 | F-SC-10 | SC-05's carried block forwards an extension the live path never applied | H |  | `U5c:60` · `05_SC_audit.md:284` · `ladder.py:262-264` | RESOLVED-BY | KERN (keeps `05_SC_sc05_kernel_retirement.md` edit 5) | B24 | SC |
| 29 | F-SC-11 | registry and export surfaces describe the kernel | H |  | `U5c:61` · `05_SC_audit.md:289` · `module_contracts.yaml:464-486`; `sim_params.json` | RESOLVED-BY | KERN (keeps retirement edits 3–4); the `requirements.yaml` row: RES §1 | B27, B24 | SC |
| 30 | F-SC-12 | THE BAR passes only off the sweep; kernel checks assert a model the game does not run | H |  | `U5c:62` · `05_SC_audit.md:296` · `test_sc01_the_bar.py:63-69` | RESOLVED-BY | RES §2 (the BAR re-pinned on `build_hearing` at shipped fixtures; `BAR_FIXTURES` deleted); ker… | B27, B24 | SC |
| 31 | F-SC-18 | the kernel's menu is solved by a constant policy | H |  | `U5c:126` · `05_SC_audit_addendum_B.md:172` · addendum §B7 runs 1–2 | RESOLVED-BY | KERN (dead list); HEAR gate 5 (the stationary-menu run) | B24 | SC |
| 32 | F-SC-19 | H-56's held half does not block a hearing | H |  | `U5c:127` · `05_SC_audit_addendum_B.md:184` · `ED-IN-0349` | RESOLVED-BY | KERN edit 5 | B24 | SC |
| 33 | G-21 | which faculty a judge, arrester, liar and interrogator roll | — |  | `U5c:90` · CAPS table | SUPERSEDED | by G-53/G-67 (CAPS): `lie` → `deception`, `determine` → `law`, `interrogate` → `inquiry`; `arr… | → B04, B24 | IN |
| 34 | G-23 | a trait cannot reach the roll without code | — |  | `U5c:92` · `sigma.py:151-157` | RESOLVED-BY | `05_SC_capability_surface.md` edits 3–4, as one member of the leverage channel (OBS §3; the ta… | B04, B05 | IN |
| 35 | §13 arcs table | ARC-04, -05, -06, -10, -21, -31, -42, R18; EMG-C4, -X6; NPC-001, -071, -085; SCN-04, -12 | — |  | `U5c:109` · audit §13; addendum §B6 | RESOLVED-BY | as the addendum's amended table reads, with: ARC-04 `05_SC_acquittal.md` + VERD; ARC-10/-21 `0… | B27, B04, B05, B24, B21c | SC |
| 36 | G-52 | the social capabilities as rows | — |  | `U5c:145` · CAPS edits | RESOLVED-BY | CAPS (rows on the surface U1 decides) | B04 | IN |
| 37 | G-53 | `lie` → `deception` | — |  | `U5c:146` · CAPS | RESOLVED-BY | CAPS edit 2; `05_SC_capability_surface.md` Reconciled | B04 | IN |
| 38 | G-59 | `score/2` kept, the divisor in `opposed_ob` | — |  | `U5c:152` · 2026-08-14 ruling; A-26 | SUPERSEDED | in its first half by Jordan's answer A-26 (the rate is 0.4 per point; C-33). Its second half s… | → B04, B05 | IN |
| 39 | G-67 | CORE's edit 8 against `deception` and `law` | — |  | `U5c:160` · CAPS | RESOLVED-BY | CAPS "Sequencing" | B04 | IN |
| 40 | §B5 items 1–6 | capability consequences | — |  | `U5c:163` | RESOLVED-BY | CAPS; office weight is FA's `06_FA_office_capabilities.md` | B04 | IN |
| 41 | cell 1 | `lie`, `arrest`, `determine`, `interrogate` cannot be opposed | — |  | `U5c:170` · 13 §3.3 control | RESOLVED-BY | CAPS edit 2 and `05_SC_capability_surface.md` edit 2 (rows); OBS §2 | B04, B05 | IN |
| 42 | cell 10 | a verdict with no spread | — |  | `U5c:179` · 13 §3.3 | RESOLVED-BY | OBS; T13; CAPS | B05, B04 | IN |
| 43 | G-10 | the roll's operands are dropped: `Event.ending` | — |  | `U5c:79` · H-266 precedent | RESOLVED-BY | `05_SC_contest_record_on_event.md` (C-06) | B05 | IN |
| 44 | G-13 | an equal opponent is a rising disadvantage (held for Jordan) | — |  | `U5c:82` · addendum §B7 run 7; A-26 | RESOLVED-BY | `05_SC_opposed_obstacle_parity.md`, un-held by Jordan's answer A-26 (0.4 per point); the rate'… | B05 | IN |
| 45 | G-14 | H-127: no floor | — |  | `U5c:83` · `10_DICE_one_score_two_roles.md` E-07 | SUPERSEDED | by OBS §2 (a person without a score opposes at `opposed_ob(pool_default)`; `obstacle_default`… | → B05 | IN |
| 46 | G-19 | no person's skill varies | — |  | `U5c:88` · aperture pools `[2]` | RESOLVED-BY | CHAR's cast seating (U5a's family); SC's reader is OBS | B05 | IN |
| 47 | G-33 | archived dice per Finding against the obstacle placement | — |  | `U5c:102` · `ED-884`, `ED-1037` | SUPERSEDED | by OBS §3: evidence rides the leverage channel as named levels (never dice, never an obstacle… | → B05 | IN |
| 48 | G-34 | the player sees what his character believes and his own roll | — |  | `U5c:103` · `View.odds` | RESOLVED-BY | `05_SC_contest_record_on_event.md`; HEAR "What a player sees" | B05, B24 | IN |
| 49 | §11 item 1 | what an equal opponent costs (H-288; SC-P5) | — |  | `U5c:105` · `unified/DECISIONS_ANSWERED.md` A-26 | RESOLVED-BY | answered by Jordan, A-26 (D-30: 0.4 per point; an even contest is even). `05_SC_opposed_obstac… | B05 | IN |
| 50 | §6.1 hole rows | H-131, H-113, H-120, H-276 closed in code; H-226 superseded in part; H-132, H-137, H-141, H-142, H-143,… | — |  | `U5c:107` · audit §6.1 | RESOLVED-BY | RES §1 (the register edits and the re-filings, by row); H-126/H-321 CHAR; H-127/H-288/H-296 OB… | B05, B27 | IN |
| 51 | G-41 | proofs clipped by the ceiling: subtract after it | — |  | `U5c:134` · `ED-884`, `ED-934`, `ED-1037`; `rosters.yaml: advantage_sources` source line; P… | SUPERSEDED | by C-01 (OBS §3): what a party brings is a named level on the leverage channel, so there is no… | → B05 | IN |
| 52 | G-57 | the obstacle is the task's difficulty plus named modifiers | — |  | `U5c:150` · relayed clarification, 2026-11-12 | RESOLVED-BY | OBS (the reconciled form; SC-B's hard terms kept) | B05 | IN |
| 53 | G-58 | a `difficulty:` column | — |  | `U5c:151` · PES-DICE (a)–(b) | RESOLVED-BY | OBS §2 and §4 (row values: all ten `routine` at the control arm; C-04) | B05 | IN |
| 54 | G-60 | a hearer's regard reaches the roll | — |  | `U5c:153` · `person_q.py:73-82`, `:424-453` | RESOLVED-BY | OBS §2–§3 (reader `stance_toward`; unit per full `STANCE_MAX`; hostile half an obstacle term,… | B05 | IN |
| 55 | G-61 | `Margin.terms` | — |  | `U5c:154` · SC-B | RESOLVED-BY | OBS §5; `05_SC_contest_record_on_event.md` (C-06) | B05 | IN |
| 56 | G-62 | NPC against NPC by the same builder | — |  | `U5c:155` · SC-B | RESOLVED-BY | OBS §2 | B05 | IN |
| 57 | G-63 | SC-P5 option B not adopted | — |  | `U5c:156` · addendum §B7 run 7; A-26 | SUPERSEDED | by Jordan's answer A-26: option B is adopted. Run 7 stands as the measurement of what moves; O… | → B05 | IN |
| 58 | G-64 | two rosters named `obstacle_terms` | — |  | `U5c:157` · DICE map §G edit 1 | RESOLVED-BY | OBS §1 (one roster, one binding table, the merged members; C-02) | B05 | IN |
| 59 | G-68 | SC-B1 folded | — |  | `U5c:161` | RESOLVED-BY | OBS (the bound has one statement) | B05 | IN |
| 60 | §B8 | the obstacle, decision-ready | — |  | `U5c:164` · C-01 to C-04 | SUPERSEDED | by OBS (the favourable halves leave the obstacle; row values; regard's reader and unit) | → B05 | IN |
| 61 | cell 2 | no dimension but score and bench reaches a roll | — |  | `U5c:171` · 270 of 284 | RESOLVED-BY | OBS; T13 (as reconciled) | B05 | IN |
| 62 | cell 3 | a held score of 0 composes Ob 0.0 | — |  | `U5c:172` · 13 §3.1 | RESOLVED-BY | OBS §2 (floor after every term) | B05 | IN |
| 63 | cell 4 | the room has three states | — |  | `U5c:173` · PES-A table | RESOLVED-BY | OBS §3 (favour as levels: monotone at every pool) | B05 | IN |
| 64 | cell 5 | opposition stops mattering above the cap | — |  | `U5c:174` · 13 §4 | DISPUTED | none: the chance floor (CP-T01-06) doing its job; stated in OBS §2 | — (disputed) | IN |
| 65 | cell 6 | SC-B's sizes merge `demanding` and `hard` | — |  | `U5c:175` · 13 §3.4 | RESOLVED-BY | T13 commit 2 (half-step sizes) with CAL (C1, C8) | B05 | IN |
| 66 | cell 7 | no roll lands Overwhelming at pool 2 | — |  | `U5c:176` · 0 of 284 | RESOLVED-BY | recorded as a constraint in OBS §6 (no band map hangs a sole effect on Overwhelming at the shi… | B05 | IN |
| 67 | R-1 | SC-B's sizes as the control arm; half-step as the calibrated arm | — |  | `U5c:181` · 13 §3.4 | RESOLVED-BY | T13 commits 1–2 | B05 | IN |
| 68 | R-2 | floor at `OB_MIN` | — |  | `U5c:182` · PP-232 | RESOLVED-BY | OBS §2 | B05 | IN |
| 69 | R-3 | venue is the row and the bench, not the building | — |  | `U5c:183` | RESOLVED-BY | T13 T2 | B05 | IN |
| 70 | R-4 | affiliation enters through regard only | — |  | `U5c:184` · `person_q.py:424-453`, `:468-482` | DISPUTED | OBS §2: no second affiliation term (kept); but the obstacle may read only the counterparty's s… | — (disputed) | IN |
| 71 | R-5 | publicity authored into `standard` | — |  | `U5c:185` | RESOLVED-BY | T13 T2 | B05 | IN |
| 72 | R-6 | no season or territory modifier | — |  | `U5c:186` · `04` §B.3 | RESOLVED-BY | T13 "not a table" | B05 | IN |
| 73 | R-9 | temperament is advantage | — |  | `U5c:189` | RESOLVED-BY | `02_CHAR_which_ground_moves_whom.md` on the leverage channel (OBS §3) | B24, B05 | SC |
| 74 | R-10 | office standing is dice | — |  | `U5c:190` · `verb_capability` source line | RESOLVED-BY | T13 T4 (`standing_dice` through `register_pool_addend`); a `standing` obstacle member is refus… | B05 | IN |
| 75 | R-11 | two cited SC files do not exist | — |  | `U5c:191` · `ls proposals/` at `6cbc712` | STALE/FP | none: `05_SC_negotiation_scene.md` and `05_SC_evidence_and_rebuttal_B.md` exist at HEAD; T13's… | — (stale) | SC |
| 76 | res. 1 | favour and proofs as levels | — |  | `U5c:211` · ladder 1 | RESOLVED-BY | PES-A; OBS §3 | B05 | IN |
| 77 | res. 3 | `tell` is opposed by the hearer's skill | — |  | `U5c:213` · PES-SC §2.2 table | RESOLVED-BY | OBS §2: the opposing score is the capability row's `opposed_by`; `copying.opposed_by: none` gi… | B05 | IN |
| 78 | Jordan 1 | is a favourable modifier part of the obstacle? | — |  | `U5c:221` · ledger rows read at HEAD | RESOLVED-BY | PES-A; OBS §3. Answered by Jordan (A-25, D-29: they raise the speaker; hostile ones raise the… | B05 | IN |
| 79 | G-51 | negotiation under `disposal: mutual`; acceptance is the accepter's own act | — |  | `U5c:144` · `04` PART D row 10a | RESOLVED-BY | NEG (as reconciled, D-06: the choice is sampled); C-07 keeps it against DRAW13's row | B24, B07 | SC |
| 80 | cell 8 | `interview` has no roll | — |  | `U5c:177` · sweep C-03 | RESOLVED-BY | DRAW13 (questioning row) with QUES and plan CP-T06-05 (C-12 orders them) | B26, B07, B25 | FI |
| 81 | cell 9 | contests that resolve as a fixed function of state | — |  | `U5c:178` · sweep C-07, C-10, C-14 | RESOLVED-BY | DRAW13 as reconciled (C-07) for docketing, the ballot, the appeal; NEG for negotiation; the bi… | B24, B07 | SC |
| 82 | R-7 | `interview` draws | — |  | `U5c:187` · standing rule | RESOLVED-BY | DRAW13; QUES | B26, B07 | FI |
| 83 | R-8 | negotiation: an offer is a draw graded into accepted / countered / refused | — |  | `U5c:188` · `04` PART D row 10a; sweep §3 | SUPERSEDED | by C-07: the offer's hearing is a draw; acceptance is the accepter's own sampled act (NEG). DR… | → B24, B07 | SC |
| 84 | standing-rule list | five things that do not draw in this scope | — |  | `U5c:225` · PES-SC §0 | RESOLVED-BY | C-10 (the four) and DRAW13 (docketing) | B07 | IN |
| 85 | res. 2 | one comparator | — |  | `U5c:212` | RESOLVED-BY | PES-B | B09 | IN |
| 86 | res. 9 | the garble and the lie are one rule | — |  | `U5c:219` | RESOLVED-BY | PES-E | B11 | FI |
| 87 | Jordan 2 | may a convicted man discharge his own sentence? | — |  | `U5c:222` · `effects_information.py:531-535`; A-37 | RESOLVED-BY | answered by Jordan, A-37 (D-54: no): an imposed service ends by the bench's `pardon` or its te… | B27, B21 | SC |
| 88 | false N-lines 1–6 | the room; the Proposition; the verdict as a wait; "a hearing ends"; the record; the band as data | — |  | `U5c:224` · PES-SC §6 | RESOLVED-BY | 1: HEAR/EVID; 2: PES-D's named residue; 3–4: C-08, RES §4; 5: PES-E; 6: the band maps above | B27, B24, B11 | SC |
| 89 | G-01 | retire `K/` whole | — |  | `U5c:70` · `ED-SC-0033` cl. 2 | RESOLVED-BY | KERN | B24 | SC |
| 90 | G-02 | forward no extension | — |  | `U5c:71` · `ladder.py:262-264` | RESOLVED-BY | KERN (retirement edit 5 kept) | B24 | SC |
| 91 | G-03 | repoint the `social_contest` contract row | — |  | `U5c:72` · `module_contracts.yaml:464-486` | RESOLVED-BY | KERN (retirement edit 3; KERN edit 2) | B24 | SC |
| 92 | G-04 | re-derive `sim_params.json` by its exporter | — |  | `U5c:73` · exporter `--check` | RESOLVED-BY | KERN (retirement edit 4) | B24 | SC |
| 93 | G-11 | speech does not reach the verdict | — |  | `U5c:80` · addendum C-1 | SUPERSEDED | by G-36/G-40 (HEAR) and EVID: the filing writes; the sitting reads the board. CP-T05-01 and CP… | → B24 | SC |
| 94 | G-24 | do the Gate-C ratifications lapse (survivor) | — |  | `U5c:93` · addendum C-2 | SUPERSEDED | by G-38 (KERN's table: closed item by item at ladder steps 1–3) | → B24 | SC |
| 95 | G-27 | a speech writes nothing, so the chooser does not price it | — |  | `U5c:96` · `choose.py:154-162` | RESOLVED-BY | EVID edit 4 with ADM edit 3 (`speak.writes` gains `Record.stages` at all four bands) | B24 | SC |
| 96 | G-28 | the hearing's carrier is the case file | — |  | `U5c:97` · CR-61 | RESOLVED-BY | HEAR edit 7; EVID edit 4 | B24 | SC |
| 97 | G-29 | a choice inside a hearing is the same for player and NPC | — |  | `U5c:98` · `settle_efforts` precedent | RESOLVED-BY | HEAR "Who decides" (one `decide`); EVID edit 6 | B24 | SC |
| 98 | G-30 | cited, typed entries admitted by the row | — |  | `U5c:99` · `08_FI_05_evidence-interface_B.md` E-1 | SUPERSEDED | by G-42 (EVID: `cites`, ids only; kind derived) | → B24 | SC |
| 99 | G-31 | rebuttal by a held contradiction strikes | — |  | `U5c:100` · `18_DETERMINISM_SWEEP.md` D-01 | SUPERSEDED | by G-65 as reconciled (D-01): the answering act's graded draw (EVID rules 1–2) | → B24 | SC |
| 100 | G-32 | a forged Record counts until an `examine` finding strikes it | — |  | `U5c:101` · FI R-43 | SUPERSEDED | by EVID rule 1 (an impeaching answer, drawn; the found deposit's `(record, record.forged, True… | → B24 | SC |
| 101 | G-35 | `ED-SC-0013` names the kernel as the one engine | — |  | `U5c:104` · `ED-SC-0033`, `ED-IN-0285` | RESOLVED-BY | KERN (the doctrine becomes true of the module's two modes) | B24 | SC |
| 102 | §11 item 2 | whether anything ratified for the kernel is kept | — |  | `U5c:106` · addendum C-2 | SUPERSEDED | by G-38 (KERN) | → B24 | SC |
| 103 | §6.2 workplan rows | B10-18c proceeds; SC-02 released by merge; SC-05 decided; SC-07 waits on CR-36/37 | — |  | `U5c:108` · audit §6.2 | RESOLVED-BY | RES §1 (order); KERN | B27, B24 | SC |
| 104 | C-1 | SC-P3 conflicts with `ED-IN-0285` (13), (16) | — |  | `U5c:116` · ledger row `ED-IN-0285` | RESOLVED-BY | HEAR; `05_SC_playable_hearing.md` carries a Reconciled line | B24 | SC |
| 105 | C-2 | audit §11 item 2 is answered by the ladder | — |  | `U5c:117` · addendum §B7 run 1 | RESOLVED-BY | KERN "The Gate ratifications" | B24 | SC |
| 106 | C-3 | the carry list is short by seven | — |  | `U5c:118` · addendum §B3 | RESOLVED-BY | KERN's carry table (ten checks), corrected by this lane where it still conceded a rung or stru… | B24 | SC |
| 107 | C-4 | SC-P8 names the wrong owner of "contradicts" | — |  | `U5c:119` · `options.py:1491-1521` | RESOLVED-BY | EVID edit 2 (`decision/options.py::contradicts`, exposed from `_pair`) | B24 | SC |
| 108 | C-6 | the target specification is P4 as cut by its critic | — |  | `U5c:121` · P4 §9 | RESOLVED-BY | HEAR (the in-room gap); G-40's division | B24 | SC |
| 109 | G-36 | the sitting is `social_contest.hearing` | — |  | `U5c:129` · `ED-IN-0285` | RESOLVED-BY | HEAR | B24 | SC |
| 110 | G-37 | H-56's held half | — |  | `U5c:130` · `ED-IN-0349` | RESOLVED-BY | KERN edit 5 | B24 | SC |
| 111 | G-38 | the Gate ratifications lapse item by item | — |  | `U5c:131` · C-2 | RESOLVED-BY | KERN | B24 | SC |
| 112 | G-39 | SC-05: retire the code, carry the exchange game | — |  | `U5c:132` · addendum §B3 | RESOLVED-BY | KERN | B24 | SC |
| 113 | G-40 | verb rows around the room, move rows in it | — |  | `U5c:133` · P4's critic | RESOLVED-BY | HEAR | B24 | SC |
| 114 | G-42 | `cites`, ids only | — |  | `U5c:135` · FI R-41 | RESOLVED-BY | EVID; `08_FI_05_evidence-interface_B.md` E-1 | B24 | SC |
| 115 | G-43 | the owner of "contradicts" | — |  | `U5c:136` · C-4 | RESOLVED-BY | EVID edit 2 | B24 | SC |
| 116 | G-44 | filing is each party's own act; the room reads the case file | — |  | `U5c:137` · `04` §B.2 | RESOLVED-BY | EVID edits 4–5 | B24 | SC |
| 117 | G-45 | mirror, contradiction, corroboration | — |  | `U5c:138` · `ED-IN-0322` | RESOLVED-BY | EVID `standing` rules 2–4 | B24 | SC |
| 118 | G-46 | the issue ladder | — |  | `U5c:139` · `PS/03` | RESOLVED-BY | HEAR edit 1 | B24 | SC |
| 119 | G-47 | named faults | — |  | `U5c:140` · T7 | RESOLVED-BY | HEAR edits 1, 3 | B24 | SC |
| 120 | G-48 | an NPC's choice inside the room | — |  | `U5c:141` · `_sample_order` | RESOLVED-BY | HEAR "Who decides" (sampled, D-06) | B24 | SC |
| 121 | G-49 | the bound on a sitting is the attendee's `effort` | — |  | `U5c:142` · `PS/05` B.1 | RESOLVED-BY | HEAR | B24 | SC |
| 122 | G-50 | a `Seat` per member, a ballot per seat | — |  | `U5c:143` · `ED-1057` behaviour | RESOLVED-BY | HEAR; RES §6 (C-11) | B27, B24 | SC |
| 123 | G-54 | the Griftlands objection assessed | — |  | `U5c:147` · §B4.6 | RESOLVED-BY | HEAR gate 5 | B24 | SC |
| 124 | G-56 | chronicle shapes from `HearingOutcome.exchanges` | — |  | `U5c:149` · `narrative.py` | RESOLVED-BY | KERN carry table (last row) | B24 | SC |
| 125 | G-65 | entry and strike of evidence | — |  | `U5c:158` · sweep D-01; LACUNA C-1 | RESOLVED-BY | ADM for entry (the citing `speak`'s band; applied to EVID's text by this lane, C-05); EVID rul… | B24 | SC |
| 126 | G-66 | the module cannot import the owner of "contradicts" | — |  | `U5c:159` · `04` §A.2 seam row | RESOLVED-BY | EVID edit 3 (`pairs` handed as data) | B24 | SC |
| 127 | cell 11 | deterministic entry and strike in SC's played hearing | — |  | `U5c:180` · EVID header | RESOLVED-BY | already reconciled by sweep D-01/D-02; entry by ADM (C-05) | B24 | SC |
| 128 | §7 catalogue | one automatic round per contest type | — |  | `U5c:192` | RESOLVED-BY | HEAR and NEG own the sitting; the catalogue's negotiation and vote rows read as C-07 and C-11… | B24 | SC |
| 129 | G-07 | a computed case names no arrangement | — |  | `U5c:76` · 14 of 14 `None` | RESOLVED-BY | plan CR-60, CR-61 | B24a | SC |
| 130 | G-25 | `ED-SC-0038`'s per-matter vector is ruled and unbuilt | — |  | `U5c:94` · `ED-SC-0038` | RESOLVED-BY | RES §3 (a bundle is several docket items opened by one act; design-first on CR-61) | B27, B24a | SC |
| 131 | G-05 | `requirements.yaml` scale row says the seam is unbuilt | — |  | `U5c:74` · audit §12 run 3 (11 rows contest) | RESOLVED-BY | RES §1 | B27 | SC |
| 132 | G-06 | ten arrangement keys and `speech_kinds` unread | — |  | `U5c:75` · audit §12 run 10 | RESOLVED-BY | `05_SC_arrangement_rows_that_bind.md` edit 5 | B27 | SC |
| 133 | G-08 | a verdict's band changes nothing a reader sees | — |  | `U5c:77` · `_eff_determine` | RESOLVED-BY | `05_SC_arrangement_rows_that_bind.md` edits 1–3 | B27 | SC |
| 134 | G-09 | no acquittal: Failure dismisses | — |  | `U5c:78` · H-162 (c) | RESOLVED-BY | `05_SC_acquittal.md` as reconciled (C-08) | B27 | SC |
| 135 | G-12 | F8 breach: build the re-source | — |  | `U5c:81` · `ED-SC-0040` | RESOLVED-BY | plan SC-02; RES §1 | B27 | SC |
| 136 | G-15 | close H-276 | — |  | `U5c:84` · `sigma.py:210` | RESOLVED-BY | RES §1 | B27 | SC |
| 137 | G-16 | close H-120 | — |  | `U5c:85` · audit §12 run 3 | RESOLVED-BY | RES §1 | B27 | SC |
| 138 | G-17 | rewrite H-226 to its residue | — |  | `U5c:86` · aperture: `interrogate` formed 0 | RESOLVED-BY | RES §1 | B27 | SC |
| 139 | G-18 | close H-131's open half | — |  | `U5c:87` · `state/world.py` `finally: self.gate.close()` | RESOLVED-BY | RES §1 | B27 | SC |
| 140 | G-20 | `PS/README.md` Status clause is stale | — |  | `U5c:89` · the built `es/` path | RESOLVED-BY | RES §1 | B27 | SC |
| 141 | G-22 | THE BAR passes only off the sweep | — |  | `U5c:91` · `test_sc01_the_bar.py` | RESOLVED-BY | RES §2 | B27 | SC |
| 142 | C-5 | Victoria 3's shape transfers (a stage held to the next sitting) | — |  | `U5c:120` · P4 §3.5 | RESOLVED-BY | `05_SC_acquittal.md` as reconciled (C-08: the row key `ballots`) | B27 | SC |
| 143 | C-7 | R-31 to R-41 are quoted, not ledgered | — |  | `U5c:122` · addendum §B7 run 5 | RESOLVED-BY | RES §1 (a ledger row is the orchestrator's; no game fact depends on it) | B27 | SC |
| 144 | G-55 | the count that dismisses is a row key | — |  | `U5c:148` · `ED-IN-0288` (#453 §9.6 as intent); P4 §3.5 (proposed) | RESOLVED-BY | `05_SC_acquittal.md` as reconciled (C-08): key `ballots`, default 1; a row may author 3 | B27 | SC |
| 145 | res. 4 | the same matter re-opened at once | — |  | `U5c:214` · LACUNA §3 ladder | RESOLVED-BY | RES §4 | B27 | SC |
| 146 | res. 5 | every computed petition names its addressee as its matter | — |  | `U5c:215` · `realm_s1_k4.txt` | RESOLVED-BY | RES §5 | B27 | SC |
| 147 | res. 6 | a judge opens a case on himself | — |  | `U5c:216` | RESOLVED-BY | RES §5 | B27 | SC |
| 148 | res. 7 | a verdict's claims name the judge and an edge id | — |  | `U5c:217` · `epistemic.py::_hold_tenure_ends` | RESOLVED-BY | PES-C edits 1–2 | B27 | SC |
| 149 | res. 8 | Failure moves the arguer; Partial is `argument.held` | — |  | `U5c:218` · H-221 intent | RESOLVED-BY | PES-D | B27 | SC |
| 150 | res. 10 | "obligee" names the bound party | — |  | `U5c:220` · `establishment_of` | STALE/FP | none: one person, two words; VERD's table reads "by the bound party" after this lane's edit | — (stale) | SC |
| 151 | Jordan 3 | who is a verdict for? | — |  | `U5c:223` · PES-SC §2.1 P1.6; A-38 | RESOLVED-BY | answered by Jordan, A-38 (D-55: the petitioner, or a seat he names). PES-C carries the party o… | B27 | SC |
| 152 | G-26 | the lane research file is stale on `speak`/`argue` | — |  | `U5c:95` · audit §17 | STALE/FP | none needed: dated reference; D_T05 rows 71–73 already say so | — (stale) | SC |
| 153 | §13 wrongly stated needs | ARC-03, NPC-071/-085 `UNCLEAR:` rows, SCN-04's faction resource, EMG-C4's champion | — |  | `U5c:110` · `04` PART D rows 1, 8, 14 | RESOLVED-BY | the audit's own restatements stand (no edit to a case file is proposed; `12_ARCS_*` owns the c… | — | SC |
| 154 | §B4.7 | six conflicts with ruled items, named | — |  | `U5c:162` · HEAR NERS-N | RESOLVED-BY | each kept as the addendum names it: one sitting is one provider call (ARC-31 between sittings… | — | SC |
