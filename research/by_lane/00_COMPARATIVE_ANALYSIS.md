# Comparative analysis: how the ten lane evaluations interact

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · resolves nothing at runtime · recommendations here enter no plan or ledger until Jordan so rules
## Date: 2026-10-16 · Lane: IN (cross-cutting) · read at HEAD `bd8105b`, code-equal to `5445e34` (`git diff --stat 5445e34 bd8105b -- engine modules systems workplans architecture references CURRENT.md` is empty)

**What this is.** Jordan asked for "a comparative analysis as its own section that weaves together and
reconciles how this work may interact", in a session whose goal is "to identify all the missing areas of the game
as it exists in code/workplanv9". The ten lane files in this directory each ran NERS and closed on
recommendations by primitives, verbs, mechanics, texture and surface. This file does not restate them. It
joins them: shared causes (C2), dependencies and collisions (C3), adjudication by a stated rule (C4), the
evidence the lanes share (C5), one deduplicated register of missing areas (C6), one register of Jordan's
decisions (C7), and one consolidated set of recommendations (C8). If this file were deleted the game would
behave identically.

**Locators.** `[CHECKED path:line]` = opened by this pass. `[LANE <lane> <id>]` = relayed from a lane file or
its digest at that id (where digest and lane file disagreed, the lane file was opened and governs; C9 lists
those). `[AUDIT <id>, <lines>]` = the uploaded NERS audit `9d5d80bf` (the tracked copy
`references/ners_audit_2026-10-14.md` differs from the upload only in its four header lines and two ED
renders, [CHECKED `diff`]). `vt` = `engine/season/verb_table.yaml`; `req` = `engine/season/requirements.yaml`;
`p2`..`p8` = `workplans/valoria_master_workplan_v9_part2.md`..`_part8.md`; `L1-01`, `L1-04` =
`architecture/meta/01_AXIOMS.md`, `04_CODE_ARCHITECTURE.md`; `20G` = the uploaded *Twenty Games, One Frame*
(`6039edcc`). Lane-row handles without their own id are written `<lane>:<position>(H|B)` for HOLLOW or BLOCKED.

---

## C0. VERDICT

**The ten lanes describe one game with one structural absence seen from ten sides: the season loop resolves
acts by persons who differ in what they want but not in what they hold, can do or know, so every seam where
one scale hands a magnitude to the next (a fight, a contest, an inquiry, a levy, a field army, the player's
view) is fed a default or nothing, and most of the lanes' missing areas are that seam left without a
person-held carrier.**

The five interactions that matter most, worst first:

| # | interaction | joins | why it ranks here |
|---|---|---|---|
| 1 | **The troop chain.** Jordan's four 2026-10-16 statements demand troops levied from settlements as their own resource, graded by equipment, experience and commander, assembled by factions into subunits with subformations; the tree sizes every season side as one `Line` of summed `Person.weight` at power 4, command 4 [CHECKED `modules/mass_battle/massbattle.py:170-232`], and the verb named `levy` moves `Rung.stores` into the seat's treasury [CHECKED vt:629-653; `loop/effects_governance.py:374-400`]. v9 schedules the opposite reading: IN-52 "`levy` moves stores, not troops", LF-1 delegated-ruled "[ASSUMPTION; medium; Jordan to correct]" [CHECKED p4:134-139; p5:533]. | MB, SE, FA, NPC, IN, PC | Jordan's own demand, contradicted by the plan; every downstream army, commander, experience and conquest row waits on it (C3 D-1..D-6). |
| 2 | **The per-person source.** `Person.capability` is empty on 429 of 430 corpus persons [CHECKED req:1244-1247]; the combat seam builds `Combatant(a_id, end=a_end)` and nothing else [CHECKED `modules/combat/fight.py:45`]; competence is a constant and H-200 has zero plan mentions [CHECKED grep]. The source is J-13's remainder, J.2 rank 1 [CHECKED p5:514]. | PC, SC, MB, NPC, FI, IN, WR, GO | One unruled source starves the body, the contest, the commander, the witness and the creation screen at once; R-09 cannot be met without it. |
| 3 | **Acts that carry no content.** Six inquiry rows write nothing [LANE FI T-FI-1; BASELINE B3]; act-minted Propositions carry empty predicates and an authored OUGHT's predicate is read by nothing (H-185, zero plan mentions [CHECKED]); every computed `utter` mints an OUGHT, so war is never uttered [LANE FA M-FA-1]. | FI, WR, IN, SC, FA, NPC, PC | The chronicle (IN-37), the investigator's record, deception, war and the ambition each need a predicate that is not written. |
| 4 | **No player surface and no pause.** IN-46 and IN-47 carry landed designs and "no build batch"; R-04, hence M1, "cannot read `met` until a build batch exists for IN-46 and IN-47" [CHECKED p4:32-37]. Every lane's SURFACE recommendation lands on that one unbatched surface, and what it may show is split inside ratified Layer 1 (AX-7's gloss "No state is hidden from the player" [CHECKED L1-01:301-302] against §C.11). | GO, IN, PC, MB, SC, FI, FA, SE, NPC, WR | It is the M1 blocker and the place where nine lanes' legibility findings converge. |
| 5 | **Population that only shrinks.** The cast is closed "for now" (ED-WR-0011, ruled 2026-09-13 [CHECKED `registers/editorial_ledger_wr_archive.jsonl`]); "the birth-side consumer of `capacity`" — "no position builds one" [CHECKED p8:134]; hunger, ageing, illness and weather ship at the control [LANE WR T-WR-8; BASELINE B5]. Any troop levy drawn from cohorts (interaction 1) and any forcing switched on (WR K-WR-9) draws down a population with no producer. | SE, WR, NPC, MB | It decides whether the troop chain and the forcing handles make a world that runs for more than a few seasons. |

---

## C1. LANE COMPARISON MATRIX

**Comparison rule.** Each cell is the lane's own finding at the cited section, not a new reading. *Research*
and *precedent* strength grade the evidence each lane's §0 and §7 judged sound (strong · moderate · thin ·
none); *grounding* is what the lane says its running code rests on; *code reach* is the dominant value in the
lane's throughline table (executes · built-inert · absent); *v9 reach* names the positions that touch the lane.
Counts are the lane file's §8.1, reconciled against the digest (SC's §8.4 has 17 rows, as its §8.1 says; the
digest's "14" is wrong, [CHECKED `SC_social_contest.md:394-415`]; SE's §8.4 has 19 rows [CHECKED]).
*Outrun rank* orders the lanes by how far their research and precedent reach beyond what their code delivers
(1 = evidence furthest ahead of code).

| lane | research | precedent | grounding of running code | code reach | v9 reach | NERS verdict (one phrase) | MISS · H/B · P-D | top recommendation | outrun rank |
|---|---|---|---|---|---|---|---|---|---|
| MB | large but self-authored from memory, unverified (PFF 16 files) [LANE MB §0 #5] | moderate (13G, 20G, COMP) | research cited in code comments; Jordan values | harness depth built-inert; season path one Line executes | IN-13, IN-52 (opposite reading), MB-07r BLK:J, MB-08 LEAVE | R-CHOICE, R-VARIETY, E-LEGIBILITY fail on the season path [LANE MB §9] | 17 · 5 · 11 | K-MB-1 troop stock | 1 |
| SC | best-ranked vendored study reaches the live design; SC-SRC, RHET unreached [LANE SC §0] | companion excluded by scope ruling | the study's gate half; rulings | `tell` executes; gate hand-built-tests-only | SC-01..08 (B-N..B-P), SC-05/06 HELD | holds as shape on four objects, fails as a game on N, R-VARIETY, S-UP, E-OVERHEAD [LANE SC §9] | 9 · 9 · 17 | K-SC-1 case names its game | 2 |
| PC | thin: one self-authored HEMA run, secondary sources, no verifier [LANE PC §0 #2] | null for the bout (T-PC-6) | constants tied to cited sources; rulings | module depth executes; every season fight two default fighters | PC-10 (B-Y), PC-06 (B-S), PC-08 LEAVE, PC-05 BLK | `fight` holds narrowed; actor's felling unwritten [LANE PC §9.8] | 9 · 3 · 8 | K-PC-1 combat inputs | 3 |
| SE | written for a retired target (`sim/provincial`, `sim/territory`) [LANE SE §0 #1] | teardown now in hand, partly confirmed, partly contradicted [UPLOAD_CHECKS] | Layer 1 axioms, rulings | larder, wear, `transfer` execute; `levy`, `found`, `build`, `work` refused | IN-07, IN-28, IN-45, IN-49, SE-03/04/06 | R-WORLD not observed for scarcity; S-DOWN fails today [LANE SE §9] | 8 · 5 · 19 | K-SE-13 troop stock | 4 |
| FA | governance research unauditable, Key-idiom hooks [LANE FA §0 #1-2] | mostly judged against a retired driver | Layer 1, rulings; no v9 FA row cites research | `dispatch` executes and writes nothing; `head()`, `at_war` built-inert | B-X goals, IN-27, IN-30, IN-36, FA-07 LEAVE | the code holds the discipline, canon does not [LANE FA §9.5] | 5 · 6 · 18 | K-FA-13 faction levies and composes | 5 |
| NPC | one research file (RTP), weakly delivered [LANE NPC §0 #4] | degrades downstream (dropped marks, contradicted N-9) | rulings, own measurements | claim ledger and pursuit cells execute; capacity, values, body dark | B-X (IN-62..72), IN-61, IN-48 | "small because capacity and change were amputated, not distilled" [LANE NPC §9] | 12 · 10 · 14 | K-NPC-1 one capacity source | 6 |
| WR | historical catalogue (HCC) reaches no code [LANE WR §0 #3] | none for magic (T-WR-6); strong on narrative failure shapes | its own metaphysics; stipulated numbers | threadwork runs in its own tests, no verb; wear executes; forcing dark | IN-35, IN-06, WR-01, IN-37, IN-27 | Calamity implementable as wear, expressible as threadwork [LANE WR §9] | 8 · 6 · 8 | K-WR-2 thread acts as verbs | 7 |
| FI | none historical [LANE FI §0 #8] | unattributed, self-graded survey | its own archived prose | six rows execute content-free | FI-01/02 (B-O), FI-03 (B-S) | investigation executes and yields no content [LANE FI §9] | 7 · 7 · 15 | K-FI-6 inquiry yield | 8 |
| IN | excluded by Layer 1's stated rule; 0 of 45 verb rows GROUNDED [LANE IN §0] | weaker than its verdicts | Layer 1, rulings, own measurement | loop executes: 17 of 45 verbs in the corpus pin | most positions | four false N-lines; S-UP fails on the petition [LANE IN §9.9] | 14 · 10 · 30 | K-IN-1 capacity source | 9 (code ahead of evidence) |
| GO | none | almost none | engine-reference reading, own audits | six constants bridged; parity Python-only | GO-01/05/06, PC-05 all B-Z | Godot shell expressible, not implementable [LANE GO §9.2] | 10 · 4 · 9 | K-GO-1 integer hash | 10 (no evidence) |
| **total** | | | | | | | **99 · 65 · 149** | | |

Reading: the ranking inverts the lanes' code maturity. MB and SC carry the most cited research and the deepest
built module (`build_army`, the arrangement table) and deliver least of it to the season; IN and GO have
almost no research and the most executing or bridged code. The lanes whose evidence most outruns their code
are the ones Jordan's 2026-10-16 statements address (MB, SE, FA): their research already named the levied,
population-costed army (T-MB-5, T-SE-4, T-FA-16) that the plan declined.

---

## C2. SHARED ROOT CAUSES

A root cause enters here when at least three lanes file different M-, T- or H-rows for it and one sentence
explains all of them. "Agree?" records whether the lanes agree on what code and v9 hold; disagreements are
adjudicated in C4.

| id | the cause, in one sentence | rows covered, by lane | agree on code and plan? | NERS axis failed |
|---|---|---|---|---|
| RC-1 | **No per-person source of capacity:** no ruled source for per-person magnitudes exists (J-13's remainder [CHECKED p5:514]; K-2 "not ratified" [LANE PC M-PC-1]), so each resolver reads a fixture default. | PC M-PC-1, M-PC-9, T-PC-9 · MB M-MB-3, M-MB-16, T-MB-15 · SC 8.3-a, M-SC-8, T-SC-2 · NPC M-NPC-1, M-NPC-2, M-NPC-13, H-NPC-1, B-NPC-4, T-NPC-4 · IN M-IN-1, M-IN-7, H-IN-2, H-IN-4, T-IN-1 · FI M-FI-3, FI:FI-01 by person(B), T-FI-7 · WR authored `ts:` unread (§8.4) · GO M-GO-7 | Agree it is absent. Disagree on the carrier: a new `Person.attributes` (K-2; audit G1; PC K-PC-1; GO K-GO-8) or the existing `Person.capability`, derived at read (NPC K-NPC-1). FI also needs AX-7's layer (2), the actor's reading of his own act [CHECKED `loop/witness.py:490-497`]; IN calls that "permitted-or-owed, unruled, not recommended" [LANE IN M-IN-7]. | R-VARIETY; S vertical; N bottom-up |
| RC-2 | **No troop stock, and a misnamed levy:** the season force is sized from summed `Person.weight` because no carrier for troops exists, and the one verb named for raising them moves stores. | MB M-MB-1, -2, -6, -15, -16, -17, MB:IN-52(H), T-MB-5, T-MB-19 · SE M-SE-9, H-SE-1, T-SE-4 · FA M-FA-10, T-FA-16 · NPC M-NPC-13 · IN M-IN-12, M-IN-13, H-IN-10, T-IN-14 · PC M-PC-12 | Agree on code [CHECKED as C0 #1] and plan (IN-52 LF-1 [CHECKED p4:136]). Disagree on form: troops as persons drawn from cohort weight (FA K-FA-13 "a `Person.weight` writer"; MB K-MB-1 lowers cohort weight and raises a per-kind count by the same headcount) or a non-person stock kind (SE K-SE-13; IN K-IN-13 leaves both open). | R-CHOICE; R-VARIETY; S vertical; N bottom-up |
| RC-3 | **Knowledge only by claim, with no deposit occasion:** AX-2 makes a claim the only route to knowing, and several facts a person must act on have no occasion on which anyone deposits them. | SE M-SE-3 (H-195 holder) · PC M-PC-8, WR M-WR-9, NPC M-NPC-6 (H-206 vacancy) · SC M-SC-4, IN M-IN-8 (H-180, H-181 rank and stake) · NPC M-NPC-9 (H-191 intent kept) · FA M-FA-4 (sheet read by no decision) · SC M-SC-7, IN M-IN-14, FI M-FI-2 (no false claim can be held) | Agree on absence: H-195, H-191 zero plan mentions [CHECKED grep of the eight plan files]; H-206 once (p3:213, its holder half). NPC dropped H-180, H-181 and H-195 as covered elsewhere [LANE NPC §8.5]; SC, IN and SE carry them. Not a disagreement about the tree: a placement difference. | S-DOWN; R-WORLD; R-COMPLETE |
| RC-4 | **Acts and findings carry no content:** verb rows record an event kind rather than a predicate, and the instruments count the event, so content-free execution passes every exit. | FI M-FI-1, M-FI-6, FI:FI-01 ×4(H), T-FI-1, T-FI-6 · WR T-WR-4, WR:IN-37(H) · IN M-IN-9, T-IN-4 · SC M-SC-1 (`DOCKET_ARRANGEMENT: None`), M-SC-5 · FA M-FA-1, T-FA-12 · NPC M-NPC-4, T-NPC-13 · PC M-PC-10 | Agree. Count difference only: FI counts six inquiry rows with no writes (BASELINE B3 lists six: `examine`, `interview`, `research`, `surveil`, `thread_read`, `reconstruct`); the audit corrected itself to "five investigation verbs" [AUDIT 498], plausibly excluding `thread_read`. Both hold under their scopes. | R-COMPLETE; N bottom-up; S-DOWN |
| RC-5 | **No player surface and no pause:** IN-46 and IN-47 have designs and no build batch [CHECKED p4:32-37], and the derivation half of §C.11 (`explain`) has no position. | GO M-GO-4, -5, -6, -7, -9 · IN M-IN-2, M-IN-3, H-IN-3 · PC M-PC-4, M-PC-6 · MB M-MB-5, M-MB-10, MB:IN-46(B) · SC M-SC-9 · FI M-FI-5 · FA M-FA-4 · NPC M-NPC-7 · WR chronicle (§8.4) | Agree on absence. Disagree on what may be shown: AX-7's gloss against §C.11 (GO K-GO-6 calls the cut "arguably takeable"; IN K-IN-9 and the audit's G6 route it differently); whether a band of odds is shown (SC K-SC-9: PS 15 against COMP S6); PC withdrew its odds surface (K-PC-11). | E-LEGIBILITY; S pause; R-PLAYER |
| RC-6 | **No births or growth:** the closed cast (ED-WR-0011) and the missing birth-side consumer of `capacity` leave every population carrier with writers only downward, and the downward writers ship dark. | SE M-SE-1, H-SE-3, T-SE-9, T-SE-10 · NPC M-NPC-3, T-NPC-5 · WR M-WR-8, T-WR-8 · IN §8.4-21, -25 · MB M-MB-14 | Disagree on scope: NPC dropped "births and new persons" [LANE NPC §8.5]; SE carries births STRONG on RR-2 [LANE SE M-SE-1]. Different objects: new named persons (ruled out "for now") against a cohort's `weight` growing. | R-WORLD; R-COMPLETE; S vertical |
| RC-7 | **War, endings and the top seat:** strategic outcomes are person-level Propositions with no producer for the mood or payload that would start them, and canon's faction-level terms (GD-1, GD-2) were never re-expressed after Layer 1. | FA M-FA-1, M-FA-3, FA:IN-27(H), FA:covenant(H), FA:IN-30(H), FA:FA-01 flip(H) · WR M-WR-6, WR:IN-27(H) · MB M-MB-7, M-MB-8, M-MB-12 · SE H-SE-2, M-SE-4, M-SE-7 | Agree that `at_war` has no game reader [CHECKED grep: only `queries/faction_q.py:219` and docstrings outside tests]. Disagree on GD-2: MB M-MB-12 and WR M-WR-6 file its threat response as MISSING; FA K-FA-6 and IN K-IN-12 strike or supersede it. Disagree on GD-1's thresholds (FA strikes; WR re-expresses through a seat-holder's estimate). | R-WORLD; S lateral; R-COMPLETE |
| RC-8 | **Offices are not made or emptied by persons:** the chooser has no general motive that produces `revoke` or `establish`, and delegation was built and reverted against Layer 1 §E.2.4. | IN M-IN-4, M-IN-5, H-IN-5, H-IN-7, H-IN-11 · FA FA:IN-61(B), M-FA-2 (planned) · NPC B-NPC-1, B-NPC-5, H-NPC-2 · SC 8.3-f · SE delegation (§8.4) | Disagree on class: IN files delegation MISSING (M-IN-5); NPC moved it to BLOCKED (B-NPC-5); FA and SE file it PLANNED-UNBUILT (IN-48 STATE B, batch B-JR "unscheduled" [CHECKED BASELINE B1.1]). Same tree reading, different definitions of MISSING (C7 J-C-10). | R-WORLD; R-CHOICE |
| RC-9 | **One ladder, several roads:** the season, the contest and mass battle reach the one margin ladder by discrete dice while combat draws a continuous Normal with a logistic side-channel, and mass battle grades on its own three-band vocabulary. | PC M-PC-7, T-PC-13 · MB M-MB-11 · IN T-IN-2 · GO M-GO-10 (float arithmetic in resolution) | Agree [AUDIT A3, 80-103]. IN extends: the odds lattice is non-monotone up to c = 6 (a sawtooth), latent only because capability is empty [LANE IN §9.1]. | S methodology |
| RC-10 | **Hash parity:** `World.content_hash` folds `repr()` and floats and draws come from CPython `random.Random`, where ratified Layer 1 asks for "a headless run [that] prints the Python oracle's hash in the integer domain" [CHECKED L1-04:1119]. | GO M-GO-1, -2, -3, -10, T-GO-3 · IN T-IN-2 (literals) · PC T-PC-13 | Agree on code. Disagree on the contract: Layer 1 says hash equality; the PROPOSED strategy says statistical parity [LANE GO §7.2]. | S methodology; R-COMPLETE |
| RC-11 | **Inert-at-ship controls:** a carrier is built with its control arm as the shipped value and no position owns the flip, so a measurement's apparatus stays as dead state. | IN T-IN-3, §8.4-21..30 · NPC M-NPC-3, T-NPC-3, T-NPC-5 · SE T-SE-9 · WR T-WR-8 · PC §8.4-d, f, g · MB loyalty to morale, `MB_SUPPORT_RANK_CAP` · FA T-FA-5 · SC 8.4 `bench_quorum`, D-6/D-7 | Agree (BASELINE B5: 18 knobs). Disagree on repair: arm (WR K-WR-9, values Jordan's) or delete (IN K-IN-2, SC K-SC-10) or "arm or delete each" (NPC K-NPC-2). | R-WORLD; E-OVERHEAD; N (false N-lines) |

**The order the causes sit in.** RC-1 and RC-2 are the two ruled-source gaps; RC-4 is their consequence at the
act (with nothing person-specific going in, an act has little to record); RC-3 and RC-5 are the same gap at
the reader (no deposit, no view); RC-6, RC-7 and RC-8 are the world's motion left without producers; RC-9,
RC-10 and RC-11 are methodology defects that each of the others inherits. This matches the audit's own causal
order (T1 upstream of T2 and T5, [AUDIT 413-415]) and adds RC-2, which Jordan's statements created after the
audit was written.

---

## C3. INTERACTION MAP

### C3 (a) Dependencies: X needs Y first

| id | X (needs) | Y (first) | reason |
|---|---|---|---|
| D-1 | a composite season army (MB M-MB-2, M-MB-17, K-MB-2, K-MB-4; FA M-FA-10, K-FA-13 composition half) | a troop stock by kind (MB K-MB-1; SE K-SE-13; IN K-IN-13) | `build_army` takes a spec list per subunit [LANE MB K-MB-2]; with no count per kind, every spec is the one default. |
| D-2 | a troop stock | the levy name and the persons-or-stock ruling (C7 J-C-1, J-C-2) | the verb that raises troops is named `levy`, and the row of that name writes `Rung.stores` [CHECKED vt:629-653]; SE, FA, NPC, MB and IN each name a different carrier. |
| D-3 | the stock entering the plan | IN-49 and IN-52 re-stated, and LF-1..LF-3 withdrawn | IN-52 states the opposite reading and its LF rows are delegated assumptions [CHECKED p4:136; p5:533]. |
| D-4 | commander quality reaching a field (MB M-MB-3; NPC M-NPC-13; K-NPC-1's fourth reader) | the per-person source (RC-1, C7 J-C-3) | `Officer`'s command is derived from a person's figures; no person carries one. |
| D-5 | troop experience (MB K-MB-3) | the stock, and fields actually fought (IN-13) | experience is earned in a fought field; none is fought in the realm (H-150) [LANE MB §0 #2]. |
| D-6 | a fought field with any outcome but `Lost` (MB:IN-13(H)) | a force scale (MB M-MB-1) | the largest season side is 6, the rout floor 80 [CHECKED `config.py:117`]; "0 of 20 at <=80 troops" won [LANE MB T-MB-13]. |
| D-7 | war as a state (FA M-FA-1, K-FA-1) | a mood source for computed `utter`, and the `attention_key` own-echo precondition | every computed `utter` mints an OUGHT [LANE FA M-FA-1]; the own-act screen is "a design point for the user" [LANE FA K-FA-1, citing req:901-904]. |
| D-8 | a march that requires war (MB K-MB-5) | war utterable (D-7) | otherwise every inter-faction march refuses and the R-07 conjunct 3 field (IN-13) can never be fought. Order hazard. |
| D-9 | insurgency emerging as a faction (FA K-FA-7; SE H-SE-2) | the same own-echo precondition; IN-27 (IN-30 is BLK on it) | IN-30's exit is any caller of `uncontrolled(` [LANE FA, SE]. |
| D-10 | a reader's competence (FI K-FI-1; NPC M-NPC-2; SC M-SC-8) | RC-1's source, and, for an inquiry, AX-7's layer (2) | every inquiry deposits to its own actor, who is exempt from refraction [CHECKED `loop/witness.py:490-497`]. |
| D-11 | the confidently wrong finding (FI K-FI-7) | an inquiry that yields content (K-FI-6) and a competence (K-FI-1) | a wrong value needs a value; error is decided at the reader [LANE FI §9 C3]. |
| D-12 | the concealer's score as obstacle (FI K-FI-5) | a concealing act that executes (`forge`, IN-45, BLK IN-10) | K-FI-5's own ladder: "once a concealing act executes" [LANE FI K-FI-5]. |
| D-13 | a computed case heard under its game (SC K-SC-1) | IN-10's record-sourced operand channel (built and reverted at B-I) | the arrangement is read from a held writ [LANE SC K-SC-1]; IN-10 restorable under the relaxed exit [CHECKED BASELINE B2.1]. |
| D-14 | succession (IN-61; FA, NPC B-NPC-1, SC 8.3-f) | the vacancy delivered by claim (H-206; PC K-PC-10, NPC K-NPC-3) and a case that can award (D-13) | IN-61 "rests on the same missing claim" [LANE NPC M-NPC-6]; a tribunal hears every computed case as `oblige` [LANE SC 8.3-f]. |
| D-15 | a chronicle a reader can follow (IN-37; WR K-WR-11; NPC K-NPC-11; FI K-FI-11) | acts with content (RC-4) and IN-47 batched | the render's input is "thin" [LANE WR T-WR-4]; IN-37 is BLK SC-01 step 16. |
| D-16 | odds or a derivation shown (GO K-GO-6, -7; IN K-IN-9; SC K-SC-9; MB K-MB-12) | the AX-7 gloss vs §C.11 ruling (C7 J-C-12) | the view's admissible content is what the ruling decides. |
| D-17 | a played fight (PC K-PC-4), a battle that yields to a duel (MB K-MB-10; IN K-IN-6; PC K-PC-5), the port's seat (GO K-GO-3) | IN-46 batched | all three extend IN-46's one call-out [CHECKED p4:32]. |
| D-18 | thread acts (WR K-WR-2), Calamity from strain (K-WR-4), TS seeding (K-WR-1) | a writer of `(Person, coherence)` and IN-06's re-plug | K-3 types `thread_read` but names no writer [LANE WR M-WR-1]. |
| D-19 | forcing switched on (WR K-WR-9) | authored ages (WR M-WR-8) and the births ruling (SE K-SE-1) | `age_at_build` is 0 [LANE WR M-WR-8]; with no producer, forcing only shrinks the realm (X-4). |
| D-20 | a priced store act (SE K-SE-5, price half) | `body_step` above 0 (J-6) | the price is "the hunger it leaves" [LANE SE K-SE-5]; hunger ships at 0. |
| D-21 | the levied person's answer (FA K-FA-5) | IN-09 restored and the store act executing (IN-49) | `comply` never attempted; `evade / defy` has no effect [LANE FA M-FA-5]. |
| D-22 | terms of taking a place (SE K-SE-9) | `seize` (IN-12 step 6) and `held_by` claims (SE K-SE-2) | the falsifier reads stance toward the taker, which needs a known holder. |
| D-23 | hostility aimed at a place (SE K-SE-2's falsifier; FA IN-70) | `held_by` claims | `stance_term` reads a rung, not its holder (H-195) [LANE SE M-SE-3]. |
| D-24 | R-04 conjunct (3), hence M1 | IN-46, IN-47 batched, plus FA-01, IN-07, FI-01, SC-01 rows `in_loop` | [CHECKED p4:36; BASELINE B2 R-04]. |
| D-25 | co-location for lethal acts (NPC K-NPC-12; IN-59) | leaders housed at their seats | five of six faction heads live off-seat; 0 of 10 season-0 kills co-located [LANE NPC H-NPC-5]. |
| D-26 | any person-varying pool going live (RC-1) | a monotone odds rule (IN K-IN-5) | the sawtooth is latent only because capability is empty [LANE IN §9.1]. |

### C3 (b) Collisions: recommendations that touch one object incompatibly

| id | object | side A | side B | incompatibility |
|---|---|---|---|---|
| X-1 | the chooser's `urgency` term | IN K-IN-2: delete `urgency` and `benefits_me` | v9 IN-62: `score_terms(p, c, fx, memo) -> (pursuit, stance, urgency)`, "a refactor, hash EQUAL" [CHECKED p5:255] | IN-62 preserves the slot K-IN-2 removes. |
| X-2 | `Person.weight` as the troop source | MB K-MB-1 (count per kind on the rung, cohort weight lowered by the same headcount); FA K-FA-13 (a `Person.weight` writer) | SE K-SE-13 (a carrier, kind or weight writer: Jordan); IN K-IN-13 (persons or non-person: Jordan); PC K-PC-12 (refuse fights at weight > 1 until a cohort can be fought at weight) | Persons-as-troops makes casualties population losses; a stock does not. MB's form is a hybrid and presupposes the answer. |
| X-3 | the felled actor's write | PC K-PC-2: write the felling of a `fight`'s or `accept`'s actor, on `march`'s precedent | `_eff_march` writes "ON THE LOSING SIDE ONLY ... the ruling is silent on the winner" [CHECKED `loop/effects_combat.py:178-183`] | None for a felled actor (he is the losing side). A standing actor's wounds are unruled on both sides. |
| X-4 | population over time | WR K-WR-9: ship weather, hunger, ageing and illness on; MB K-MB-1 and FA K-FA-13: levies draw cohort weight down | SE K-SE-1: growth at CENSUS or a fixed population; ED-WR-0011: the cast "only shrinks" | Three lanes write population down; one writes it up, behind a Jordan ruling. A cohort's death is final [AUDIT A6 (iii)]. |
| X-5 | the suspension sites | GO K-GO-3: seat the player at DELIBERATE and at the mass-to-personal duel; MB K-MB-10, IN K-IN-6: a battle yields at phase boundaries inside the 18-tick call | IN-46's design: the driver suspends at ENCOUNTER "and only at the engine call" [CHECKED p4:32] | Each extends IN-46 beyond its designed site. |
| X-6 | the closed `requires` grammar | FI: do not widen `requires_typed`; "each added read is a refusal condition", the forms are closed at seven, and K-FI-6's Sites and Rungs half needs an eighth form [CHECKED `FI_fieldwork_investigation.md:374, :455-462`] | MB K-MB-5 (`at_war` conjunct on `march`); FA K-FA-1 (an act gated on `at_war`); PC K-PC-12 (a weight conjunct); NPC K-NPC-12 (co-location) | Not incompatible in intent (these lanes want the refusal), but all draw on one grammar; F.33 leaves open whether `at_war` may gate a `requires` [LANE FA K-FA-1]. |
| X-7 | which act war gates | MB K-MB-5: `march` | FA K-FA-1: "real removal of `at_war` only if Jordan makes `fight` the gated act" | Two different acts proposed for one gate. |
| X-8 | GD-2's threat response | MB M-MB-12, WR M-WR-6: MISSING (canon demand) | FA K-FA-6: strike GD-2's mandatory pass; IN K-IN-12: mark it superseded; WR K-WR-12: a duty on the holder, or retire | Missing area against deletion. |
| X-9 | GD-1's ending terms | FA K-FA-6: an ending Query over seats acts produced; strike the Accord and Stability thresholds | WR K-WR-10: read stability from a named seat-holder's estimate; give Accord a carrier or drop it | Strike against re-express. SE adds 15 against 17 territories [LANE SE §8.4]. |
| X-10 | what Mending is | WR K-WR-3: the thread Mend is the Mending; `restore` stays fabric repair | v9 IN-35: "Mending as persons' acts (the `restore` arm)" [LANE WR §0 #9] | One verb for two acts against two verbs. |
| X-11 | the top seat | FA K-FA-3: a crisis offers the top holder resignation; the replaced arm is Jordan's | Jordan's 2026-10-12 duchy ruling ("strippable by nobody") and SC-04 "awards, never unseats" [LANE FA M-FA-3] | Abdication is compatible; replacement is not. |
| X-12 | closing a petition | SC K-SC-3: close by `destroy_record`; (b) a separate `deny` row | plan A-16 "No new closer rows"; A-13 (`destroy_record` unformable) [LANE SC M-SC-2] | (a) is blocked by A-13; (b) contradicts A-16. |
| X-13 | ending a delegate's tenure early | NPC K-NPC-8's falsifier: "revoking deputy ends his acts that season" | FA K-FA-11: early dismissal is Jordan's (IN-31's ban; H-207); SE K-SE-6 ends at term only | NPC's falsifier assumes the ruling FA leaves open. |
| X-14 | the capacity carrier | audit G1, PC K-PC-1, GO K-GO-8: `Person.attributes` (K-2), "one field and one reader" | NPC K-NPC-1: "adds no field", stored on `Person.capability`, derived at read | New field against existing field. |
| X-15 | AX-7's actor exemption | FI K-FI-1 needs the actor's own fallible reading (layer 2) | IN M-IN-7: "permitted-or-owed unruled ... not recommended"; audit G6: "permitted, not owed"; NPC dropped it [LANE NPC §8.5] | FI treats as needed what three others treat as optional. |
| X-16 | what the player may see | GO K-GO-6: cut the gloss to Jordan's verbatim ("arguably takeable"); K-GO-7 odds from held claims | IN K-IN-9: Jordan rules which sentence; SC K-SC-9: whether a band is shown; PC withdrew odds | One Layer 1 conflict, three proposed routes. |
| X-17 | investigation's seam | FI-02 and K-FI-9: investigation keeps its own role ("not a contest seam", SM-3) | FI-01 pins the social contest's roller (`modules/social_contest/roll.py`); K-FI-3 routes testimony through `tell`, SC's contested verb [LANE FI §X] | Own seam against the contest's roller and verb. |
| X-18 | the dedup filter `_drop_what_was_already_done` | audit G4: delete it, Layer 1 03 §C.3 forbids it | IN K-IN-3: the conflict is 03 §C.2 against §C.3 and a measured monoculture; Jordan [LANE IN §10.7] | Free cut against a ruling inside Layer 1. |

### C3 (c) Amplifications: one lane's fix makes another lane's gap bite or eases it

| id | fix | effect on another lane | direction |
|---|---|---|---|
| AM-1 | RC-1's capacity source (K-IN-1, K-NPC-1, K-PC-1) | wakes IN's latent sawtooth (D-26); makes PC's C3 defect live ("harmless while opponents identical, a defect once K-1 lands", [LANE PC §9 C3]); raises the stakes of RC-5 (a varying pool nobody can see) | bites |
| AM-2 | the troop stock (K-MB-1, K-SE-13) | eases MB M-MB-1 and IN-13's hollow exit; makes SE M-SE-1 (no births) bite: a levy drains a population with no producer | both |
| AM-3 | forcing on (K-WR-9) | multiplies deaths; with NPC B-NPC-1 ("five of six heads die in two seasons" [LANE NPC]) and H-206 open, more vacancies nobody learns of | bites |
| AM-4 | a case names its game (K-SC-1) | eases IN-61's tribunal (SC 8.3-f) and FI T-FI-3 (inquiry lands on proceedings) | eases |
| AM-5 | an inquiry yield (K-FI-6) | eases IN-37's thin input and SC-02 `22a`'s "investigation products" | eases |
| AM-6 | war utterable (K-FA-1) | makes MB M-MB-1 and M-MB-14 bite: wars are fought by 4/4 Lines that always lose and never kill | bites |
| AM-7 | co-location (NPC K-NPC-12; IN-59) | makes H-NPC-5 bite: the access gate's premise (where leaders live) is wrong in data | bites |
| AM-8 | renaming the store act (K-SE-5; K-IN-13) | eases SE H-SE-1 and IN M-IN-13; FA K-FA-5 still needs the renamed act to execute | eases |
| AM-9 | `held_by` claims (K-SE-2) | eases FA and MB targeting, IN-70's opinion of a faction, and SE K-SE-9 | eases |
| AM-10 | arming dark person knobs (K-NPC-2) | makes RC-5 bite: values change unwatched with no surface (T-NPC-8) | bites |
| AM-11 | thread acts as verbs (K-WR-2) | makes WR M-WR-4 bite: free own-aim Mending becomes a strictly dominant option at a playable seat (T-WR-9) | bites |
| AM-12 | the integer hash and fixed-point draws (K-GO-1, K-GO-2, K-GO-11) | every golden moves once; every other hash-moving repair (K-PC-2, K-MB-9, K-NPC-3, K-SE-1) moves them again | ordering cost |

### C3 (d) Dependency order of the consolidated recommendations (C8 ids)

| layer | contents | why here |
|---|---|---|
| L0 rulings | C7 J-C-1, -2, -3, -9, -12 first; the rest as their dependants arrive | each blocks a primitive below |
| L1 cuts and owners (no ruling) | R-C-8 (deletions), R-C-3 (one per-die owner, monotone rule's owner half), R-C-4 (integer hash, typed fixtures), R-C-5 (draw primitive) | shorten what every later step reads; fix methodology before depth is wired through it |
| L2 primitives | R-C-1 (capacity), R-C-2 (troop stock), R-C-6 (`held_by`), R-C-7 (adjacency), R-C-9 (population carrier), R-C-29 (vacancy by claim) | each is a carrier a verb below reads |
| L3 verbs | R-C-10 (store act), R-C-11 (order of battle), R-C-12 (war), R-C-13 (felled actor, cohort refusal), R-C-14..R-C-22 | each needs an L2 carrier or an L0 ruling |
| L4 mechanics and texture | R-C-23..R-C-36 | read what L3 writes |
| L5 surface | R-C-37..R-C-39 | renders what L2-L4 produce; R-C-37 (the batch) can start in parallel because its designs exist |
| L6 apparatus | R-C-40 | measures the others |

<!-- APPEND -->
