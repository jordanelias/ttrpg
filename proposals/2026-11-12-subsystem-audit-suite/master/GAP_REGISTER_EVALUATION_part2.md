# Evaluation of the gap register, part 2: the settlement ledger and the one-disposition-per-id table

## Status: EVALUATION RECORD, generated (stage 5 of `STAGES.md`; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted when workplan v12 is adopted)

**What this part is.** Every row of lanes E6 to E8 whose disposition this settle pass changed or re-cited, keyed by lane file and line (the verbatim copies in parts 3 to 5 keep the lane's call), then every register id (H-) that lane E3 (v11 parts 8 and 9, which list hole rows) and a register lane dispositioned differently, with the settled call. The register lane governs a register row (E3's own convention 6 defers it), except where the ledger rows of `V11_EVALUATION_part2.md` §1 (E3 rows, kind RECON) or of §1 below say otherwise.

**Kinds.** ANSWER: re-dispositioned or re-cited by a Jordan answer (A-100 to A-114). LADDER: a for-Jordan item settled by the five-step ladder (CLAUDE.md §0). MBA: the A-100 supersession table (`master/mb_abstraction/MBA_DESIGN_part3.md` §8) applied. WRONG-R: a WRONG call reversed after its evidence was opened. REREAD: an E7 extract-only row re-read in full and changed. RECON: one disposition per id across the lane files. A row whose settled disposition equals its lane disposition was re-cited only. The table is generated from `overrides.py`/`recon.py` (the settle record, scratch) by script; the rule each RECON row follows is in the head file §4.

## 1. Settlement ledger, lanes E6 to E8

| source row | id | lane disposition | settled | kind | reason / cite |
|---|---|---|---|---|---|
| E6:42 | H-11 | DONE-IN-CODE | **STILL-NEEDED** | RECON | H-11: the register row's fixture is shipped, but its closure is v11 CR-22's MEASURE-then-BUILD (E3 Block 16); one item with CR-22 (SE, B12). |
| E6:71 | H-47 | MISSING-DEP | **STILL-NEEDED** | RECON | H-47: not MISSING-DEP: U3 §6.3 names v11 CP-T07-02 as the one carrier of a `Person.coherence` writer (E1:101, E5 head finding (a)); one item with CP-T07-02 (WR, B35). |
| E6:87 | H-62 | MISSING-DEP | **STILL-NEEDED** | RECON | H-62: as H-47. |
| E6:103 | H-125 | DONE-IN-CODE | **STILL-NEEDED** | RECON | H-125: as H-11 (CR-22 re-derives `body_step`). |
| E6:119 | H-89 | STILL-NEEDED | **MISSING-DEP** | RECON | H-89: one item with CR-07; IS-B2-CORE-06 records it BLOCKED (DEP-v11): `off_npc_084`'s rung is content the plan may not author. |
| E6:120 | H-90 | MISSING-DEP | **STILL-NEEDED** | RECON | H-90: the Court Parliament's working state is v11 CR-38 (design-first bench, A-76 interim) with CR-35..CR-37 and IN-48 (`U5_FINDINGS_CLOSURE_U5d.md:75`); carried in B21c, not a missing dependency. |
| E6:145 | H-132 | STILL-NEEDED | **STILL-NEEDED** | ANSWER | re-cited, A-105 (H-132): a reduction of a sitting holder's grant is judged as a revocation, and its odds read the power relation between the two factions (A-35's resistible draw with relative faction power as a term); FA, B21b, `state/gate.py::may_fill`; a declared hash mover. |
| E7:69 | H-171 | STILL-NEEDED | **STILL-NEEDED** | REREAD | re-cited after the full `cite:`: H-171's limit (2) (`Rung.envelope` declared, no writer) is SUPERSEDED by C3-C4 (keep the field) with `07_SE_population_regrowth_B.md` (:124-133, births and deaths of envelope weight at MATTER, B12); limit (3) closed by REM-44; limit (1) (no eater in corpus worlds) stays carried, design-first, SE B12. |
| E7:71 | H-173 | DONE-IN-CODE | **STILL-NEEDED** | REREAD | H-173: the delegated ruling (no distinct reading) closes the design; v11's measurement of the four consequences, whose trigger has fired (`determine` executes), is owed and nothing supersedes it (E3 Block 12); SC, B27. |
| E7:79 | H-181 | MISSING-DEP | **STILL-NEEDED** | REREAD | H-181: not MISSING-DEP: its producer is v11 CR-32 ('rank reads one scale (H-181's producer)', E3 Block 18), carried in B21c; one item with CR-32. |
| E7:83 | H-185 | STILL-NEEDED | **DONE-IN-CODE** | REREAD | H-185: the full `cite:` records ladder step 4's precedent (`harness/corpus_run.py::build_at`, 2026-09-13: `Proposition.predicate` kept as a declared non-causal label) and IN-43's hold ('nothing planned needs it'); no session item needs a reader; nothing is owed. |
| E7:97 | H-199 | DONE-IN-CODE | **STILL-NEEDED** | REREAD | H-199: the full `cite:` (B-P Phase 1) records two functions of one ordinal (`world_q.remove_weight` `(K-k)/K` against `refracted_confidence` `k/(K-1)`): two ladders for one quantity, an S defect (CLAUDE.md §0.06); ladder step 5 picks one spacing; E3 Block 12 carries it. |
| E7:107 | H-209 | WRONG | **SUPERSEDED** | WRONG-R | H-209: the measurement is unreproducible at its seed but the mechanism claim is unfalsified; `09_WR_B_pointer_text_for_the_orchestrator.md:101` (opened) carries the re-measure at seed 2 or under the illness arm after the duel path executes (B03). |
| E7:115 | H-217 | SUPERSEDED | **STILL-NEEDED** | REREAD | H-217: its closure says 'RESOLVED-BY plan CR-35', a v11 position, not a session item; carried with CR-35 in B21c, amended by A-14/A-19 and `22_HAPPENINGS_B` (E3 Block 13). |
| E7:120 | H-222 | DONE-IN-CODE | **STILL-NEEDED** | REREAD | H-222: E7's own evidence names the missing producer ('irrelevant until a `person_predicates` producer exists'); v11 A1-87's writer through the channels is owed (E3 Block 9). |
| E7:122 | H-224 | DONE-IN-CODE | **STILL-NEEDED** | REREAD | H-224: the window-arm measurement rides CR-29's exit (E3 Block 11); the chooser reader is `02_CHAR_voices_and_the_room.md` Edit 5 (B10). |
| E7:123 | H-225 | WRONG | **SUPERSEDED** | WRONG-R | H-225: as H-209 (`09_WR_B_pointer_text_for_the_orchestrator.md:102`, opened). |
| E8:117 | H-325 | MISSING-DEP | **MISSING-DEP** | ANSWER | re-cited, A-109: no general exploration act (the exploration-act part is SUPERSEDED: travel and inquiry cover ordinary discovery; H-327's arrival-teaches lands in B12). STILL owed: a way to find what is hidden (a concealment rating or withheld claim; a drawn find under the one opposed rule; what finding yields; exposure at depth). The dependency is A-109's design, owner SE+FI lanes (a design proposal first); no Jordan decision remains. |
| E8:119 | H-326r | MISSING-DEP | **MISSING-DEP** | ANSWER | re-cited, A-109: the depth axis, exposure and cover tracks fold into A-109's find-the-hidden design (`surveil`'s Exposure effect gets its carrier there). |
| E8:154 | H-361 | SUPERSEDED | **SUPERSEDED** | MBA | re-cited, A-100: §8.2 NARROWS H-361: the friction re-read is on the contact draw with the multiplier at zero (`27_MB_C` 27C-3 (k)); the pair-rule part of the cite is superseded by MBA-04; PLAY §E and MIL-C Edit 5 stand. |

## 2. One disposition per register id (E3 against E6 to E8)

| id | rows (lane disposition → settled) | settled for the id |
|---|---|---|
| H-10 | E3:448 H-10 STILL-NEEDED→SUPERSEDED; E6:40 H-10a DONE-IN-CODE→DONE-IN-CODE; E6:41 H-10b SUPERSEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| H-11 | E3:449 H-11 STILL-NEEDED→STILL-NEEDED; E6:42 H-11 DONE-IN-CODE→STILL-NEEDED | one: STILL-NEEDED |
| H-25 | E3:456 H-25 DONE-IN-CODE→STILL-NEEDED; E6:49 H-25 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-30 | E3:461 H-30 DONE-IN-CODE→SUPERSEDED; E6:54 H-30 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-37 | E3:468 H-37 SUPERSEDED→DONE-IN-CODE; E6:61 H-37 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-39 | E3:470 H-39 DONE-IN-CODE→STILL-NEEDED; E6:63 H-39 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-40 | E3:471 H-40 DONE-IN-CODE→SUPERSEDED; E6:64 H-40 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-47 | E3:478 H-47 SUPERSEDED→STILL-NEEDED; E6:71 H-47 MISSING-DEP→STILL-NEEDED | one: STILL-NEEDED |
| H-48 | E3:479 H-48 DONE-IN-CODE→SUPERSEDED; E6:72 H-48 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-52 | E3:483 H-52 DONE-IN-CODE→WRONG; E6:76 H-52 WRONG→WRONG | one: WRONG |
| H-56 | E3:487 H-56 SUPERSEDED→SUPERSEDED; E6:80 H-56a DONE-IN-CODE→DONE-IN-CODE; E6:81 H-56b SUPERSEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| H-59 | E3:490 H-59 DONE-IN-CODE→SUPERSEDED; E6:84 H-59 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-62 | E3:493 H-62 SUPERSEDED→STILL-NEEDED; E6:87 H-62 MISSING-DEP→STILL-NEEDED | one: STILL-NEEDED |
| H-63 | E3:494 H-63 DONE-IN-CODE→SUPERSEDED; E6:88 H-63 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-70 | E3:498 H-70 DONE-IN-CODE→DONE-IN-CODE; E6:92 H-70a SUPERSEDED→SUPERSEDED; E6:93 H-70b DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / SUPERSEDED |
| H-86 | E3:513 H-86 DONE-IN-CODE→SUPERSEDED; E6:116 H-86 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-87 | E3:514 H-87 DONE-IN-CODE→WRONG; E6:117 H-87 WRONG→WRONG | one: WRONG |
| H-90 | E3:517 H-90 SUPERSEDED→STILL-NEEDED; E4:572 §2 H-90 sovereign pow… STILL-NEEDED→STILL-NEEDED; E6:120 H-90 MISSING-DEP→STILL-NEEDED | one: STILL-NEEDED |
| H-92 | E3:519 H-92 STILL-NEEDED→SUPERSEDED; E6:122 H-92 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-97 | E3:524 H-97 DONE-IN-CODE→SUPERSEDED; E6:127 H-97 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-98 | E3:525 H-98 DONE-IN-CODE→SUPERSEDED; E6:128 H-98 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-103 | E3:530 H-103 DONE-IN-CODE→SUPERSEDED; E6:131 H-103 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-106 | E3:533 H-106 DONE-IN-CODE→STILL-NEEDED; E6:134 H-106 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-108 | E3:535 H-108 SUPERSEDED→STILL-NEEDED; E6:136 H-108a DONE-IN-CODE→DONE-IN-CODE; E6:137 H-108b STILL-NEEDED→STILL-NEEDED | in parts: DONE-IN-CODE / STILL-NEEDED |
| H-111 | E3:538 H-111 DONE-IN-CODE→SUPERSEDED; E6:140 H-111 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-119 | E3:546 H-119 DONE-IN-CODE→SUPERSEDED; E7:40 H-119 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-125 | E3:552 H-125 STILL-NEEDED→STILL-NEEDED; E6:103 H-125 DONE-IN-CODE→STILL-NEEDED | one: STILL-NEEDED |
| H-126 | E3:553 H-126 DONE-IN-CODE→DONE-IN-CODE; E6:104 H-126a SUPERSEDED→SUPERSEDED; E6:105 H-126b DONE-IN-CODE→DONE-IN-CODE | in parts: DONE-IN-CODE / SUPERSEDED |
| H-127 | E3:554 H-127 DONE-IN-CODE→SUPERSEDED; E6:106 H-127 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-130 | E3:557 H-130 DONE-IN-CODE→STILL-NEEDED; E6:143 H-130 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-132 | E3:559 H-132 DONE-IN-CODE→STILL-NEEDED; E6:145 H-132 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-133 | E3:560 H-133 DONE-IN-CODE→STILL-NEEDED; E6:146 H-133 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-135 | E3:562 H-135 DONE-IN-CODE→STILL-NEEDED; E6:148 H-135 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-137 | E3:564 H-137 DONE-IN-CODE→STILL-NEEDED; E6:150 H-137 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-138 | E3:565 H-138 DONE-IN-CODE→STILL-NEEDED; E6:151 H-138 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-139 | E3:566 H-139 DONE-IN-CODE→STILL-NEEDED; E6:152 H-139 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-141 | E3:568 H-141 DONE-IN-CODE→STILL-NEEDED; E7:26 H-141 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-142 | E3:569 H-142 DONE-IN-CODE→STILL-NEEDED; E7:27 H-142 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-143 | E3:570 H-143 DONE-IN-CODE→STILL-NEEDED; E7:28 H-143 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-145 | E3:572 H-145 DONE-IN-CODE→STILL-NEEDED; E7:30 H-145 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-146 | E3:573 H-146 DONE-IN-CODE→SUPERSEDED; E6:108 H-146 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-153 | E3:580 H-153 DONE-IN-CODE→STILL-NEEDED; E7:50 H-153 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-154 | E3:581 H-154 DONE-IN-CODE→STILL-NEEDED; E7:51 H-154 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-156 | E3:583 H-156 DONE-IN-CODE→SUPERSEDED; E7:53 H-156 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-158 | E3:585 H-158 SUPERSEDED→DONE-IN-CODE; E7:55 H-158 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-160 | E3:587 H-160 SUPERSEDED→DONE-IN-CODE; E7:57 H-160 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-162 | E3:589 H-162 DONE-IN-CODE→DONE-IN-CODE; E7:59 H-162 DONE-IN-CODE→DONE-IN-CODE; E7:60 H-162 (c) SUPERSEDED→SUPERSEDED | in parts: DONE-IN-CODE / SUPERSEDED |
| H-164 | E3:591 H-164 DONE-IN-CODE→SUPERSEDED; E7:62 H-164 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-168 | E3:594 H-168 SUPERSEDED→WRONG; E7:66 H-168 WRONG→WRONG | one: WRONG |
| H-169 | E3:595 H-169 DONE-IN-CODE→STILL-NEEDED; E7:67 H-169 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-170 | E3:596 H-170 DONE-IN-CODE→SUPERSEDED; E7:68 H-170 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-171 | E3:597 H-171 SUPERSEDED→STILL-NEEDED; E7:69 H-171 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-173 | E3:599 H-173 STILL-NEEDED→STILL-NEEDED; E7:71 H-173 DONE-IN-CODE→STILL-NEEDED | one: STILL-NEEDED |
| H-175 | E3:601 H-175 SUPERSEDED→DONE-IN-CODE; E7:73 H-175 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-180 | E3:605 H-180 DONE-IN-CODE→STILL-NEEDED; E7:78 H-180 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-181 | E3:606 H-181 STILL-NEEDED→STILL-NEEDED; E7:79 H-181 MISSING-DEP→STILL-NEEDED | one: STILL-NEEDED |
| H-185 | E3:609 H-185 DONE-IN-CODE→DONE-IN-CODE; E7:83 H-185 STILL-NEEDED→DONE-IN-CODE | one: DONE-IN-CODE |
| H-187 | E3:258 H-187 DONE-IN-CODE→SUPERSEDED; E7:85 H-187 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-189 | E3:260 H-189 SUPERSEDED→DONE-IN-CODE; E7:87 H-189 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-191 | E3:262 H-191 DONE-IN-CODE→MISSING-DEP; E7:89 H-191 MISSING-DEP→MISSING-DEP | one: MISSING-DEP |
| H-192 | E3:263 H-192 DONE-IN-CODE→SUPERSEDED; E7:90 H-192 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-193 | E3:264 H-193 DONE-IN-CODE→SUPERSEDED; E7:91 H-193 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-195 | E3:266 H-195 STILL-NEEDED→SUPERSEDED; E7:93 H-195 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-197 | E3:268 H-197 SUPERSEDED→DONE-IN-CODE; E7:95 H-197 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-198 | E3:269 H-198 DONE-IN-CODE→MISSING-DEP; E7:96 H-198 MISSING-DEP→MISSING-DEP | one: MISSING-DEP |
| H-199 | E3:270 H-199 STILL-NEEDED→STILL-NEEDED; E7:97 H-199 DONE-IN-CODE→STILL-NEEDED | one: STILL-NEEDED |
| H-200 | E3:271 H-200 DONE-IN-CODE→SUPERSEDED; E7:98 H-200 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-203 | E3:274 H-203 DONE-IN-CODE→SUPERSEDED; E7:101 H-203 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-206 | E3:277 H-206 SUPERSEDED→DONE-IN-CODE; E7:104 H-206 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-207 | E3:278 H-207 SUPERSEDED→SUPERSEDED; E4:575 §2 H-207's vacancy mo… STILL-NEEDED→SUPERSEDED; E7:105 H-207 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-209 | E3:280 H-209 SUPERSEDED→SUPERSEDED; E7:107 H-209 WRONG→SUPERSEDED | one: SUPERSEDED |
| H-215 | E3:286 H-215 DONE-IN-CODE→SUPERSEDED; E7:113 H-215 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-217 | E3:288 H-217 STILL-NEEDED→STILL-NEEDED; E7:115 H-217 SUPERSEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-218 | E3:289 H-218 DONE-IN-CODE→SUPERSEDED; E7:116 H-218 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-219 | E3:290 H-219 SUPERSEDED→STILL-NEEDED; E7:117 H-219 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-221 | E3:292 H-221 SUPERSEDED→DONE-IN-CODE; E7:119 H-221 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-222 | E3:293 H-222 STILL-NEEDED→STILL-NEEDED; E7:120 H-222 DONE-IN-CODE→STILL-NEEDED | one: STILL-NEEDED |
| H-224 | E3:295 H-224 STILL-NEEDED→STILL-NEEDED; E7:122 H-224 DONE-IN-CODE→STILL-NEEDED | one: STILL-NEEDED |
| H-225 | E3:296 H-225 STILL-NEEDED→SUPERSEDED; E7:123 H-225 WRONG→SUPERSEDED | one: SUPERSEDED |
| H-229 | E3:300 H-229 SUPERSEDED→STILL-NEEDED; E7:127 H-229 STILL-NEEDED→STILL-NEEDED | one: STILL-NEEDED |
| H-234 | E3:305 H-234 STILL-NEEDED→SUPERSEDED; E7:132 H-234 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
| H-235 | E3:306 H-235 SUPERSEDED→DONE-IN-CODE; E7:133 H-235 DONE-IN-CODE→DONE-IN-CODE | one: DONE-IN-CODE |
| H-237 | E3:308 H-237 SUPERSEDED→WRONG; E7:135 H-237 WRONG→WRONG | one: WRONG |
| H-239 | E3:310 H-239 DONE-IN-CODE→SUPERSEDED; E7:137 H-239 SUPERSEDED→SUPERSEDED | one: SUPERSEDED |
