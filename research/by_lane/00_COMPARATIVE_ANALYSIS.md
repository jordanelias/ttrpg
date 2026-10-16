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

---

## C4. RECONCILIATION

**The rule, in order of precedence:** (1) Jordan's statements and rulings (where two conflict, the later one
governs on the point it decides) > (2) ratified Layer 1 > (3) the v9 plan's recorded state (an entry over an
index row when the plan contradicts itself) > (4) measured behaviour in the tree > (5) proposals > (6) research
(tier 3, `engine/season/rosters.yaml:75-90` [CHECKED]). A tag "[ASSUMPTION; Jordan to correct]" leaves a
plan answer at rank (3) but marks it revertible alone (p8:193). Where the rule does not decide, the item goes
to C7.

### C4.1 Collisions and cross-lane disagreements

| item | sides | rank that decides | favours | why | C7 |
|---|---|---|---|---|---|
| X-1 `urgency` | IN K-IN-2 against v9 IN-62 | (3) | IN-62 first, then K-IN-2 | IN-62 is a scheduled hash-EQUAL refactor; deleting `urgency` afterwards shrinks its triple by one slot, which IN's own §10.7 calls "real but small". A sequence, not a conflict. | — |
| X-2 troops as persons or stock | MB, FA against SE, IN | (1) partly | a rung-held troop resource distinct from `Person.weight` | Statement 1: "troops levied from settlements as their own resource". It does not say whether raising the resource lowers a cohort's weight. | J-C-2 |
| X-3 felled actor | PC K-PC-2 against `march`'s loser-only write | (1) | PC, for the felled actor | Jordan 2026-09-04, "your code just has to accept the result" [LANE PC M-PC-2]; ED-IN-0279 writes the losing side and "is silent on the winner" [CHECKED `effects_combat.py:178-183`]. The standing winner's wounds: not decided. | J-C-4 |
| X-4 population | WR, MB, FA (down) against SE (up) | (1) | no new named persons; a cohort's weight may grow | ED-WR-0011 rules the NAMED cast closed "for now" [CHECKED]; it does not reach a cohort's `weight`. Growth or fixed stays Jordan's (SE K-SE-1). Order: decide before forcing (D-19). | J-C-9 |
| X-5 suspension sites | GO K-GO-3 against IN-46's design | (2) | GO | Layer 1: "for a player character the player IS the decision procedure" [CHECKED L1-04:844-846], and "serial and pooled runs produce the identical hash" [CHECKED L1-04:1118]. A seat at DELIBERATE and its exclusion from the pooled map follow; IN-46 (PROPOSED, held) covers ENCOUNTER only. The battle's internal yield (MB, IN): no rule decides which acts interrupt. | J-C-20 |
| X-6 `requires` grammar | FI against MB, FA, PC, NPC conjuncts | (4) | conjuncts within the seven forms: takeable; an eighth form: Jordan | `rosters.yaml:1782-1784` closes the forms ("a design change, not a table edit") [LANE FI §9 C3]. | J-C-15 (for `at_war`) |
| X-7 which act war gates | MB (`march`) against FA (`fight`) | none | — | F.33 leaves it open [LANE FA K-FA-1]. | J-C-15 |
| X-8 GD-2 | MB, WR (missing) against FA, IN (strike) | (1), later over earlier | the faction-level mandatory pass is superseded | Jordan's later "adopt in full" of Layer 1 (2026-09-05; AX-1, no faction-level actor) supersedes GD-2 on the actor. Whether a threatened holder bears a duty (WR K-WR-12) is not decided; MB M-MB-12 and WR M-WR-6 stay MISSING only under that reading. | J-C-14 |
| X-9 GD-1 | FA (strike thresholds) against WR (re-express) | (2), (3) | an ending as a Query over seats persons' acts produced | IN-27 schedules a Query-based ending; an omniscient evaluator is "acceptable only as presentation gating no act" [LANE FA §9 C3]. Whether the Accord and Stability terms survive, and 15 or 17 territories, is a canon edit. | J-C-13 |
| X-10 Mending | WR K-WR-3 against v9 IN-35 | (3), then sequence | IN-35 today; WR once a thread Mend verb exists | IN-35's `restore` arm and the roster's refusal are both "[ASSUMPTION; Jordan to correct]"; the roster declines only "until a Mending can be told from mending a wall" [LANE WR §0 #9]. R-C-18 creates that distinction; the restore reading then has no basis. | — (unless R-C-18 is refused) |
| X-11 top seat | FA K-FA-3 against the duchy ruling | (1) | abdication: yes; replacement: no | The 2026-10-12 ruling bars stripping a top seat; a holder resigning by his own `release` is not stripping. | J-C-5 (replacement only) |
| X-12 closing a petition | SC K-SC-3 against A-16, A-13 | (1) over (3) | the closer is owed | ED-IN-0210 Ruling 2 (a petition rises to the hand that may deny it) outranks the plan's "No new closer rows". Addressing to the seat above needs no new row (takeable); which closer is Jordan's. | J-C-7 |
| X-13 early dismissal | NPC K-NPC-8 against FA K-FA-11 | none | — | H-207 ruling (A) and IN-31's ban bound `revoke`; neither covers a same-rung deputy. | J-C-17 |
| X-14 capacity carrier | audit G1, PC, GO (new field) against NPC (existing field) | (3), provisionally | the existing `Person.capability` | v9 records K-2 "not ratified" and `capability` as the interim carrier (J-13 (iii)); the SOURCE remains Jordan's. | J-C-3 |
| X-15 actor self-reading | FI against IN, audit | (2) | not owed | AX-7 (2): self-understanding "may be wrong" — permitted. FI's inquiry half becomes a design choice. | J-C-3 (sub-question) |
| X-16 what is shown | GO, IN, SC | (2) against (2) | — | AX-7's gloss and §C.11 conflict inside Layer 1. Decided regardless: `explain` takes no `World`, so any odds shown are the actor's estimate [LANE GO §9 C2]. | J-C-12 |
| X-17 investigation's seam | FI-02 against FI-01's roller | (1) | FI: its own role | SM-3, "investigation is not a contest seam. it is its own thing" (P6:266), outranks the carried v8 line [LANE FI K-FI-9]. Using the one roller is RC-9's single owner, not a seam. | — |
| X-18 dedup filter | audit G4 against IN K-IN-3 | (2) against (2) | — | 03 §C.2 and §C.3 conflict inside Layer 1. | J-C-16 |
| `restore` executes? | SE (refused 25, executed 0, two seasons at HEAD) against `req:163-166` and older lane prose | (4) | refused | SE ran it [LANE SE §9 self-audit]; BASELINE B3's pin classes `restore` R. | — |
| `march` in the realm | `req:675` "16/16" against `req:1124` "all 11 refused" | (4), not run | unreconciled | Needs `aperture 4 0` (about 25 minutes); no lane ran it; p2:178 marks it [UNVERIFIED]. A measurement, not Jordan's. | — (C9) |
| inquiry verbs writing nothing | FI "six" against audit "five" | (4) | both | Scope: BASELINE B3 lists six rows with no writes; five if `thread_read` is counted as threadwork. | — |
| IN-14's state | index "ask-then, B-Z" against entry "STATE: B ... BATCH: B-J" | (3), entry over index | the entry (MORE ROUNDS, delegated-ruled 2026-10-12) | [CHECKED p4:25-27]. FA and IN both flagged it. | — |
| delegation's class | IN MISSING, NPC BLOCKED, FA and SE PLANNED | definitional | — | IN-48 is STATE B in a batch the plan calls "unscheduled". | J-C-10 |
| parity contract | Layer 1 hash against the PROPOSED strategy's statistics | (2) over (5) | hash equality, integer domain | [CHECKED L1-04:1119]; GO itself takes the hash at step 3 [LANE GO §9.5]. Remaining: the version (J-9) and the fixed-point table resolution. | J-C-11 (version only) |
| thread history term (audit G7) | audit: agent fix `min(3, history) + 3` against WR: Jordan | (4) and §0.05 | WR | Code reads `min(3, history + 3)` [CHECKED `systems/threadwork/sim/operations.py:246`]; the alternative rests on a comment's wording and PP-624 has no `registers/` row [LANE WR §8.4, "History term"]. Prose cannot decide. | J-C-23 |
| one substrate (audit G2d) | audit: agent [medium] against PC: Jordan | (1) | PC | Combat is exempt from the ladder's bands by ruling (T-PC-13), and the substrate choice moves every combat balance figure. | J-C-18 |

### C4.2 The lanes against the uploaded NERS audit

Test applied: IN's §10.7 (each finding re-opened at `5445e34`, [CHECKED `IN_infrastructure.md:1023-1052`])
for A2, A3, A4, A5, A9, T3-T6, G1-G9, X1-X8; the other lanes' own cites for A1, A6, A7, A8, T1, T2 and
R-WORLD. The audit assumed every v9 position built; a lane row that is MISSING under that assumption agrees
with it, and a row that is only unbuilt does not contradict it.

| audit id | lanes' verdict | relation | lane cites |
|---|---|---|---|
| A1 / T1 per-person difference | holds; reaches commanders, troops, competence and creation | agree, extend | MB M-MB-3, NPC M-NPC-13, FI M-FI-3, SC M-SC-8, GO M-GO-7 |
| A2 player as callback; §C.11 vs gloss; dead path; empty hooks | holds | agree, extend: DELIBERATE pause; mass→personal yield; thread→mass | IN §10.7; GO M-GO-4; MB M-MB-4; WR M-WR-3 |
| A3 / T3 one ladder, several roads; non-monotone odds | holds; sawtooth to c = 6 | agree, extend | IN §9.1; PC M-PC-7; MB M-MB-11; GO M-GO-10 |
| A4 (i)-(iv) inert chooser terms, dark knobs | holds | agree | IN §10.7; NPC M-NPC-3, M-NPC-4 |
| A4 (v) no term reads odds, cost or capability | not a missing area | **diverge** (but becomes a defect once capacity lands, AM-1) | IN §8.5; NPC §8.5; PC §9 C3 |
| A4 datum (439 of 1,318; 70.5 %) | not re-run | unverified (G9 unrun) | — |
| A5 (a) dedup contradicts §C.3 | the conflict is §C.2 against §C.3 | **diverge** in form | IN §10.7 |
| A5 S-UP petition | holds | agree | SC M-SC-2; IN §9.9 |
| A5 R-CHOICE `levy` unpriced | holds, but prices the misnamed store act | **re-labelled** by statement 5 | IN M-IN-13; SE H-SE-1 |
| A6 `doc: null` contracts; designed governance verbs; no births | holds | agree, extend: labour, exchange, adjacency | SE M-SE-1, M-SE-2, M-SE-4, M-SE-5 |
| A7 / T2 a season force cannot be resolved | holds | agree on defect; **repair superseded** (troop stock, not weight conversion) | MB M-MB-1, M-MB-15; IN §10.7 G3 |
| A8 thread history; coherence after crossing; Mending free; inquiries write nothing | holds; Mending cost 0 at all 16 cells, executed | agree, extend | WR M-WR-2, M-WR-4, M-WR-7; FI M-FI-1 |
| A9 AX-7 falsifier fires by its letter | holds; sites moved again | agree, extend (inquiry needs the actor's own reading, X-15) | IN §10.7; FI M-FI-3 |
| R-WORLD forcing dark, `at_war` false | holds | agree, extend: ages unauthored; drought arm stays in surplus | WR M-WR-8; SE §9 R-WORLD |
| S coverage | holds | agree, extend (DELIBERATE) | GO M-GO-4 |
| T2 seam keeps the band | holds, narrowed | agree | MB T-MB-2; PC T-PC-10 |
| T4 built ahead of readers | holds | agree | IN T-IN-3; NPC T-NPC-3; FA T-FA-5; SE T-SE-9; WR T-WR-8 |
| T5 acts record that, not what | holds; magnitude [CONFIDENCE: low], one seed | agree | IN T-IN-4; FI T-FI-1; WR T-WR-4 |
| T6 apparatus | holds; run output now 88,377 lines | agree, updated | IN §10.7 |
| G1 rule a capacity source | survives | agree; carrier contested (X-14) | K-IN-1, K-NPC-1, K-PC-1 |
| G2a one literal owner · G2b delete survivor degree · G2c margin (Jordan) | survive | agree | K-IN-5; K-MB-7; K-MB-8 |
| G2d one substrate, agent | Jordan | **diverge** (ladder) | K-PC-8 |
| G3 weight→troop conversion | superseded in form by statements 1, 3, 4, 5 | **overturned** | IN §10.7; K-MB-1 |
| G4 delete the dedup filter | not a free cut | **overturned** | K-IN-3 |
| G5 delete `urgency`, `benefits_me` | survives; after IN-62 (X-1); ED-IN-0261 Jordan's | agree | K-IN-2; NPC M-NPC-12 |
| G6 AX-7 falsifier and gloss | falsifier re-point survives; gloss route is Jordan's | partly **diverge** | K-IN-9; K-GO-6 |
| G7 thread history term | a ruling, not a repair | **diverge** (ladder) | K-WR-7 |
| G8 re-point head rows | survives; one head sits in `.audit/`, which `CURRENT.md:13`'s caveat does not cover | agree, extend | WR §0 #1 |
| G9 re-read candidate formation | survives, unrun | agree | — |
| X1-X7 apparatus | survive | agree | IN §10.7; K-IN-12 |
| X8 delete `tools/evacuation_plan.py` | precondition still unverified | open | IN §10.7 |

**Audit claims the lanes overturned:** G3 (the repair's form, by Jordan's statements); G4 (as a free cut);
G7 and G2d (their ladder results, to Jordan); A4 (v) (as a missing area); A5's `levy` finding (re-labelled
onto the store act). **Claims the lanes extended past the audit's frame:** RC-2 (the troop chain, which
post-dates the audit), the DELIBERATE pause, labour, adjacency, ages, and the actor's own reading.

---

## C5. CROSS-LANE EVIDENCE

### C5.1 Convergence: independent lanes, one pattern

"Independent" asks whether the lanes reached the pattern from different evidence. Six lanes citing one
measurement is redundancy, not corroboration (CLAUDE.md §10).

| pattern | lanes | evidence base | independent? |
|---|---|---|---|
| persons differ in wants, not capacities | IN T-IN-1, PC T-PC-9, MB T-MB-15, SC T-SC-2, NPC T-NPC-4, FI T-FI-7 | one measurement (`req:1244-1247`), relayed, plus the audit's T1 | **no**: one source, six sites of the same absence |
| built ahead of readers; controls shipped off | IN T-IN-3, NPC T-NPC-3/-5, SE T-SE-9, WR T-WR-8, FA T-FA-5/-6, PC T-PC-7, GO T-GO-2 | different knobs and carriers, opened by each lane (BASELINE B5 lists 18) | **yes**: separate sites |
| acts record that, not what | IN T-IN-4, FI T-FI-1, NPC T-NPC-13, WR T-WR-4 | vt rows (FI); `storybar.py` and one uncommitted datum (WR, IN) | partly: the rows are independent; the 52-of-52 datum is one seed |
| a levy takes people, and so labour and the future | MB T-MB-5, SE T-SE-4, IN T-IN-14, FA T-FA-16 | historical (FASE), precedent (20G A3, Proposal F, X4), Jordan's statements | **yes**: three tiers agree, and the plan is the outlier |
| one resolver, several fidelities | MB T-MB-3, PC T-PC-8, IN T-IN-5 | the Total War auto-resolve precedent | no: one precedent |
| scale keeps attribution only through a named person | WR T-WR-12, FA T-FA-1, NPC | Layer 1 AX-1 plus surveys | partly |
| commitment cheap, binding at a price, breach punished | SC T-SC-13, FA (K-FA-2), NPC (K-NPC-5) | rhetoric corpus, governance research, Pax Pamir | partly |
| accrual without a closer runs away | NPC T-NPC-9, IN T-IN-6 | Guild 3 (TD:195) | no |
| conquest is priced by method | MB T-MB-14, SE T-SE-5 | memory-written history; SE's game leg CONTRADICTED | weak |

### C5.2 Shared nulls: the same gap in several lanes' research

| null | lanes | standing |
|---|---|---|
| no precedent solves the hand-off above the bout (personal leverage from N=1 to N=1000+) | MB T-MB-4, PC T-PC-15, IN T-IN-7 | sound; and the built `Command=0 -> instant rout` contradicts the borrowed rule that a person moves a unit only by a fraction [LANE MB §0 #8] |
| no source for magnitudes: shape transfers, numbers do not | FA T-FA-14, IN T-IN-8, MB §0 #3, PC T-PC-4, WR T-WR-6 | sound in every lane; every value is `[OPEN — Jordan tuning]` or a fixture |
| no historical research for the lane | FI §0 #8, GO T-GO-4 | sound |
| no surveyed bout, magic or cost-to-self system | PC T-PC-6, WR T-WR-6 | sound |
| no game models argument content or attitude durability | SC T-SC-6 | sound, single source for durability |
| no game ships an NPC acting on knowingly false political information (PREC N-9) | FI T-FI-10, NPC T-NPC-15, IN T-IN-13 | **contradicted** in all three: The Guild 2's fabricated evidence and slander (TD:191) |
| allegiance never arrives late | IN T-IN-12, NPC T-NPC-2 (sound) against FA T-FA-9 (over-claimed), SE T-SE-7 (unverified) | adjudicated: "recomputed instantly" over-claims, since Tropico's opinion diffusion and Guild 2's evidence exist (20G A9); "no title schedules a lag on allegiance" holds inside the twenty (20G empty cell 3) |

### C5.3 Precedent applied correctly in one lane, incorrectly in another

| precedent | applied correctly | applied incorrectly |
|---|---|---|
| failure shape A: a mechanism tuned never to fire is absent (EU4, Imperator) | MB T-MB-13 to the dead `Won` branch; FA T-FA-5 to `head()`, `at_war`, `uncontrolled`, `levy` | — |
| The Guild 3's agent layer switched off (TD:195, the publisher's own account, T1) | FA T-FA-5, NPC T-NPC-3, PC T-PC-7 (layer built as one switch) | VCD's "at a popularity threshold" (relayed by IN and NPC): not in the teardown; it comes from the absent churn survey (F77) [UPLOAD_CHECKS] |
| 20G A5's "specify the half-strength setting" | NPC T-NPC-3 | none misapplied, but the lanes miss a nuance: Valoria's knobs DO have intermediate arms (`scar_weight_shift` arms 0.5 / 1, `confliction_weight` 0.2 / 1, BASELINE B5); the half-strength setting exists in code and is unchosen in data |
| Banished | SE: capacity gates births (TD:284) | SFP 02:116's "food-limited attrition" is CONTRADICTED (TD:21: starve with full granaries because deaths removed gatherers); Tropico's shack-squatting cited with causation inverted [UPLOAD_CHECKS] |
| du Picq on rout | — | MB: the 15-30 % band is a recorded Jordan value (ED-MB-0031) credited to du Picq in code and ledger [LANE MB §0 #7] |
| Total War auto-resolve as the second-resolver failure | PC T-PC-8 (honoured: the band is read off the scene) | MB T-MB-3: protection over-claimed (the structure is one engine, but the season path never reaches its depth) |
| a companion's survey counts | — | COMP "six of eight, Valoria owns the primitive", contradicted by its own table [LANE IN §7]; 13G convergence counts inflated (X1) [LANE NPC §0 #8] |

### C5.4 Research tiers across lanes: which tier reaches an owner code reads

| lane | historical research reaches | game precedent reaches | repository work rests on |
|---|---|---|---|
| MB | code comments, unverified constants | gauges that gate nothing (T-MB-10) | Jordan values; harness |
| PC | constants tagged `[FIAT]`/`[SIM-CALIBRATE]` | nothing | rulings |
| SC | the vendored study's gate half | nothing (scope ruling) | rulings; one source |
| SE | one name (Sen via SFP P1, shipped dark); H-100 | nothing (rosters built and deleted unread, `rosters.yaml:86-90` [CHECKED]) | Layer 1 axioms |
| FA | one hole row the loop does not read (H-100) | nothing | Layer 1, rulings |
| NPC | H-100 | `forgive`, via VCD | rulings, measurements |
| WR | nothing (HCC) | IN-37 as observer; forcing handles with controls | its own metaphysics |
| FI | — | nothing | its own archived prose |
| IN | nothing, by Layer 1's stated exclusion | VCD's name-level mapping (18 rows PARTLY) | Layer 1, measurements |
| GO | — | — | engine reference; its own audits |

The one research finding with a code-read owner in any lane is H-100 (seat provenance prices revocation),
and its owner (IN-31) keys cost on a different variable (`conferral`, not how the seat was won) [LANE NPC
§0 #3; H-NPC-2]. Research reaches the game by name and vocabulary, never by magnitude (T-IN-8).

### C5.5 The Twenty Games frame against the lane findings

**Corpus bound (the document's own):** the frame covers twenty titles; Dwarf Fortress, RimWorld, the Victoria
series, Frostpunk and Old World are unexamined, and every empty-cell and novelty claim inherits that bound
[CHECKED 20G:148, :446, :462].

**The seven axes, with Valoria's own cell (code today; v9 built in brackets):**

| axis (20G §2.1) | Valoria's cell | lane evidence | empty in Valoria's own design? |
|---|---|---|---|
| 1 population resolution | individual (46 named) plus cohort as one Person at `weight` (37 cohorts) | SE T-SE-10; NPC; p5:514 row 4 | no, but the cohort tier never changes size (RC-6) |
| 2 named-agent cardinality | 46, closed "for now" (ED-WR-0011) | WR T-WR-2; NPC T-NPC-10 | no |
| 3 contested object | seats and allegiance (commit edges); land (occupation, `seize`, planned IN-13); labour absent; time absent (no ending) | FA T-FA-1; SE M-SE-5; IN-27 | **labour and time empty** |
| 4 player position | embedded: the player IS the decision procedure for one person [CHECKED L1-04:844-846] | GO T-GO-8 | no |
| 5 control channel | rung 1 (own acts) only; rung 3 delegate built and reverted (IN-48, unscheduled); rung 4 lobby a body unbuilt (SC-01); rung 2 absent | IN M-IN-5; SC M-SC-1 | **rungs 2, 3 and 4 empty today; 2 empty planned** |
| 6 coupling latency | belief carried by telling (lagged, thin: 4 of 1,270 claims [LANE NPC T-NPC-2]); scars accrue; lagged-cohort absent | NPC T-NPC-1/-2; SE M-SE-1 | **lagged-cohort empty** |
| 7 durability | persistent; no ending (H-176) [IN-27 Query ending] | FA T-FA-4 | ending empty today |
| clock count | two clocks by design (season; 18-tick battle and duel), auto-resolve only | MB T-MB-12; IN-46 | the second clock buys nothing a player touches (20G directive 6) |
| legibility strategy | none | RC-5 | **empty** |

**The four empty cells of 20G §2.3, against Valoria:** cell 1 (finely modelled populace × scarce named
agents) is occupied in structure (cohorts plus 46 named persons) but its loop is not, since no named person
can be placed over a populace (IN-48); cell 2 (labour contested between players) is empty (SE M-SE-5, WEAK);
cell 3 (lagged allegiance) is crossed in shape by the telling transport and thin in delivery; cell 4 (rungs
2 and 3 together) is empty.

**The asymmetry map A1-A9 (20G Part 4):**

| # | transfer | Valoria | lane ids |
|---|---|---|---|
| A1 | give allegiance a delay | **crossed in shape**: claims arrive by telling, regard at read; the stored loyalty seed is static | NPC T-NPC-1, -2; IN T-IN-12; IN-69, IN-70 |
| A2 | zone plus delegate; risk in the delegation | **not crossed**: no zone; delegation reverted; "usefulness breeds threat" WEAK | IN M-IN-5; NPC M-NPC-11; FA T-FA-15 |
| A3 | conscription that removes a cohort, not a number | **not crossed, and refused by v9** (IN-52 LF-1); exactly Jordan's statements 1 and 5; Proposal F ("The Levy", B+) is its fullest form, and its lag needs births (RC-6) | MB T-MB-5, M-MB-15; SE T-SE-4, M-SE-9; FA M-FA-10; IN M-IN-12 |
| A4 | relational victory | **partly**: IN-27 plans a Query over who holds seats; GD-1's territorial thresholds unresolved | FA T-FA-4, K-FA-6; WR K-WR-10 |
| A5 | a graduated agent layer | **crossed in mechanism, not in data**: intermediate arms exist, every one ships at 0 | NPC T-NPC-3, -5; IN T-IN-3; FA T-FA-5 |
| A6 | ephemerality with meta-progression | not applicable: Valoria is persistent; no lane addressed it | — |
| A7 | a dual-use political currency | **not crossed**; no lane addressed it | — |
| A8 | scarce named agents over an anonymous many | **structure crossed**, loop not (no steward over a populace) | NPC T-NPC-10; SE T-SE-6 |
| A9 | belief with provenance | **crossed**, where Valoria is ahead of the twenty (source, chain, `seen.who`); deceit and fabrication absent (H-198; `forge` unbuilt) | IN T-IN-13; FI T-FI-4; NPC §0 "solid" |

Read together: Valoria has crossed the epistemic asymmetries (A1, A9) that the political corpus lacks and has
not crossed the demographic ones (A3, the lagged-cohort axis, labour) that the settlement corpus supplies.
Jordan's 2026-10-16 statements point at A3.

---

## C6. CONSOLIDATED MISSING-AREAS REGISTER

**Count rule.** Every MISSING row and every HOLLOW or BLOCKED row of the ten lanes' §8.2 and §8.3 enters once.
Rows describing one game area (one object, one absent behaviour) merge into one consolidated row whatever
their lane or class. In the *merges* column an unsuffixed id was filed MISSING; `(H)` HOLLOW, `(B)` BLOCKED.
*Demand* is the strongest among the merged rows, coded as the lanes code it: D1 THE NINE or a Jordan
statement · D2 canon · D3 a ruling or Layer 1 needing a carrier · D4 a hole row or plan text · D5 the audit ·
D6 research alone; strength S/M/W. *Code* and *v9* are the merged rows' cells, reconciled by C4.

**Arithmetic.** Lane rows: MISSING 99 (MB 17, PC 9, FI 7, SC 9, FA 5, WR 8, IN 14, GO 10, SE 8, NPC 12) +
HOLLOW or BLOCKED 65 (MB 5, PC 3, FI 7, SC 9, FA 6, WR 6, IN 10, GO 4, SE 5, NPC 10) = **164**. They merge into
**84** consolidated rows (persons 3, armies 15, settlements 6, factions 13, knowledge 10, proceedings 9,
world 7, surface 6, port 8, decision layer 7); 164 − 84 = 80 lane rows merged away; 30 of the 84 rows join
two or more lanes. Per-lane placements re-add to the lane totals (MB 22, PC 12, FI 14, SC 18, FA 11, WR 14,
IN 24, GO 14, SE 13, NPC 22).

### Persons and capacity

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-PER-1 | per-person capacity (attributes, skill, kit) that the pool, the `Combatant` and the commander read | PC M-PC-1, M-PC-9(H) · IN M-IN-1, H-IN-2(H), H-IN-4(B) · NPC M-NPC-1, H-NPC-1(H), B-NPC-4(B) · SC 8.3-a(B) · FI FI-01 by person(B) | D1 R-09; statement 1 · S | empty on 429 of 430; `Combatant` takes `end` only | J-13 remainder (J.2 rank 1); `train` (B-Q) writes `copying` only; K-2 not ratified | R-VARIETY; S vertical |
| C-PER-2 | a reader's competence, and the actor's reading of his own act | FI M-FI-3 · SC M-SC-8 · NPC M-NPC-2 · IN M-IN-7 | D3 AX-7 · S | competence fixed; actor exempt (`witness.py:495`) | none; H-200 zero mentions | R-VARIETY; R-COMPLETE |
| C-PER-3 | values and body that change in shipped play (scar shift, strain, conscience, age, illness) | NPC M-NPC-3, B-NPC-3(B) | D1 R-06 · S | built, shipped at the control | none arms them; IN-65 conditional | R-WORLD; N bottom-up |

### Combat and armies

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-ARM-1 | a season force scale: sides that clear the rout floor | MB M-MB-1, IN-13(H), MB-07r(H/B) | D1 R-04, R-07 c3; statement 3 · S | troops = weight sum (largest 6) against floor 80 | none; IN-52 can only lower troops | R-COMPLETE; R-CHOICE |
| C-ARM-2 | a troop stock held by a settlement, raised by a levy, fielded by `march`, drawn down by loss | MB M-MB-15, M-MB-6, IN-52(H) · SE M-SE-9 · FA M-FA-10 · IN M-IN-12, H-IN-10(H) | D1 statements 1, 4, 5 · S | absent: no troop kind; cohorts have no `commit` | opposite reading scheduled (IN-49 B-K; IN-52 LF-1, B-T) | R-CHOICE; R-WORLD; S vertical |
| C-ARM-3 | the store act under its own name, and priced | IN M-IN-13 · SE H-SE-1(H) | D1 statement 5 · S | `levy` moves `Rung.stores`, unpriced | IN-49 builds it under the wrong name | E-LEGIBILITY; R-CHOICE |
| C-ARM-4 | composition: several subunits of different kinds and subformations, chosen by the faction | MB M-MB-2, M-MB-17, J-19(B) | D1 statements 3, 4 · S | `build_army` harness-only; season one `Line` | MB-08 LEAVE | R-VARIETY; R-CHOICE |
| C-ARM-5 | a commander whose person reaches the field | MB M-MB-3 · NPC M-NPC-13 | D1 statement 1 · S | `command=4` fixed; `Officer` harness-only | U-4, K-6 LEAVE | R-PLAYER; S lateral |
| C-ARM-6 | experience as a troop quality | MB M-MB-16 | D1 statement 1 · S | absent (two comments) | none | R-VARIETY |
| C-ARM-7 | a decision at the field (formation, stance, commitment) | MB M-MB-5 | D1 R-04 · S | `resolve_field` takes no choice | none | R-CHOICE; S pause |
| C-ARM-8 | a battle that yields to a person (commander's duel, champion, capture) | MB M-MB-4 · PC M-PC-5 · IN M-IN-6 | D5 A2; R-04 · M | one atomic 18-tick call | M-6 LEAVE | S vertical; S pause |
| C-ARM-9 | death in battle | MB M-MB-14 | D3 ED-IN-0279 · M | `max(1, …)` floor; `total` arm emits no death | none | R-WORLD |
| C-ARM-10 | the actor's own outcome written | PC M-PC-2 | D1 Jordan 2026-09-04 · S | lifted, never read; false `contest.undecided` | none | R-COMPLETE; S methodology |
| C-ARM-11 | fights with more than two persons | PC M-PC-3 | D3 Layer 1 §E.2.1; R-04 · S | the seam reads two claimants | PC-08, WS-7 LEAVE | S vertical |
| C-ARM-12 | a cohort fought as one body | PC M-PC-12 | D3 "a cohort is a person at weight > 1" · S | `weight` unread at the seam | none (H-49 zero mentions) | R-COMPLETE |
| C-ARM-13 | the occupying army's consumption | MB M-MB-8 | D4 IN-13 [GAP] · M | absent | none | R-COMPLETE |
| C-ARM-14 | the authored cast marches | MB M-MB-13 | D4 H-175 · M | never attempted in the corpus | none (remainder unowned) | R-WORLD |
| C-ARM-15 | an access gate whose premise holds (heads housed at their seats) | NPC H-NPC-5(H) | D4 IN-59 · M | five of six heads off-seat | IN-59 (B-Y) | R-COMPLETE |

### Settlements, population and the economy

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-SET-1 | births and growth | SE M-SE-1, H-SE-3(H) | D3 RR-2; D5 A6 · S | absent | none ("no position builds one") | R-WORLD; N bottom-up |
| C-SET-2 | exchange between places; a trading act | SE M-SE-2 · SC M-SC-6 · FA FA-01 trade(B) | D1 R-05 · S | no `_eff_exchange` (reverted) | IN-33 B, no batch | R-VARIETY; R-CHOICE |
| C-SET-3 | adjacency between territories | SE M-SE-4 | D2 GD-3 · S | geography parsed, read by no season module | none | S lateral |
| C-SET-4 | labour as an input to production | SE M-SE-5 | D6 · W | yield ignores headcount | none | R-COMPLETE |
| C-SET-5 | terms of taking a place | SE M-SE-7 | D6 · W | absent | none | R-CHOICE |
| C-SET-6 | regional difference in production | SE M-SE-8 | D6 · W | every settlement has every site | none | R-VARIETY |

### Factions, war, treaty, succession and the ending

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-FAC-1 | war as a state persons enter and leave | FA M-FA-1 · MB M-MB-7 | D3 Layer 1 04:451, D-48; D1 IN-36 · S | `at_war` built, read by nothing | none ("waits on a `mood` source") | R-WORLD; S lateral |
| C-FAC-2 | forcing a top-rung holder out | FA M-FA-3 | contested: D6 against a D1 ruling | strippable by nobody | none | R-WORLD |
| C-FAC-3 | a change of sides priced as its own deed, and the bloc it carries | NPC M-NPC-5 · FA M-FA-8 | D4 H-205 · S | vow-break judged at `release` cells | none | R-CHOICE; R-WORLD |
| C-FAC-4 | an ending reached by choices | FA IN-27(H/B) · WR IN-27(H/B) | D2 GD-1; H-176 · S | absent | IN-27 (B-U), BLK IN-37 | R-COMPLETE |
| C-FAC-5 | treaties that bind | FA covenant(H) | D2 GD-1 · M | unbuilt | IN-12 step 7 (B-Q), readers deferred | R-CHOICE |
| C-FAC-6 | insurgency that forms a faction over contiguous ground | FA IN-30(H) · SE H-SE-2(H) | D2 GD-3 · S | `uncontrolled` report-only, drops contiguity | IN-30 (B-U): exit is any caller | R-WORLD; S lateral |
| C-FAC-7 | grand-strategy acts that do something | FA FA-01 flip(H) | D1 R-04 · S | `dispatch` writes nothing | FA-01 (B-V) | R-CHOICE |
| C-FAC-8 | succession | FA IN-61(B) · IN H-IN-5(B) · NPC B-NPC-1(B) · SC 8.3-f(H) | D1 RS-27 · S | heads die; `succeed` declined | IN-61 (B-R), BLK SC-04, ED-IN-0292 (2) | R-WORLD |
| C-FAC-9 | delegation and regency | IN M-IN-5 · NPC B-NPC-5(B) | D1 Jordan 2026-09-03 · S | built, reverted | IN-48, B-JR unscheduled | R-WORLD; R-CHOICE |
| C-FAC-10 | offices made and emptied by persons, and what that costs | IN M-IN-4, H-IN-7(B), H-IN-11(B) · NPC H-NPC-2(H) | D1 R-04 (1), R-05 · S | `revoke` hand-forced only | IN-31 (B-Q), exit against H-207 | R-WORLD; R-CHOICE |
| C-FAC-11 | a threatened holder's response (GD-2) | MB M-MB-12 · WR M-WR-6 | D2 GD-2 · S, form unruled (C4 X-8) | absent | none | S methodology |
| C-FAC-12 | recruitment | NPC M-NPC-10 | D6 · W | membership is the person's own `commit` | none | R-CHOICE |
| C-FAC-13 | usefulness breeds threat | NPC M-NPC-11 | D6 · W | absent | none | R-CHOICE |

### Knowledge, testimony, inquiry and findings

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-KNO-1 | an inquiry that yields content, graded, with failure distinct from refusal | FI M-FI-1, FI-01 vs S-6(H), vs scales(H), vs R-05(H), vs Q1(H), SKIP scope(B) | D1 R-04 (3); D3 AX-7 · S | six rows write nothing | FI-01 (B-O) grades a content-free kind | R-COMPLETE; N bottom-up |
| C-KNO-2 | the honest misreading | FI M-FI-2 | D3 AX-2; R-07, R-08 · S | refraction moves confidence only | none (reader side) | R-WORLD |
| C-KNO-3 | the concealer's score as the obstacle | FI M-FI-4 | D1 Jordan 2026-08-18 Q1 · M | non-person default obstacle | none | R-CHOICE |
| C-KNO-4 | testimony from questioning | FI M-FI-6 | D1 Jordan Q4 · M | `interview` content-free | none | R-COMPLETE |
| C-KNO-5 | covert watching of a person | FI M-FI-7 | D4 · W | grammar cannot bind it | none | R-VARIETY |
| C-KNO-6 | an investigation role with a provider | FI FI-02(H) | D1 SM-3 · M | role registered, no provider | FI-02 (B-O); FI-03 (B-S) | N |
| C-KNO-7 | a spoken lie that can be caught | SC M-SC-7 · IN M-IN-14 | D4 H-198 (a ruling) · M | `said_of` passes a held claim | G7 recorded only | R-COMPLETE; R-VARIETY |
| C-KNO-8 | a hearer's credibility inputs: intent kept, stake, rank | IN M-IN-8 · NPC M-NPC-9 · SC M-SC-4 | D1 R-07 · M | `rank_gain` dormant | none (H-191 zero mentions) | R-WORLD |
| C-KNO-9 | who holds a place, knowable | SE M-SE-3 | D2 GD-1, GD-3; H-195 · S | 0 of 80 persons hold a `held_by` claim | none (zero mentions) | S diagonal; R-CHOICE |
| C-KNO-10 | a vacancy delivered by claim | PC M-PC-8 · WR M-WR-9 · NPC M-NPC-6 | D4 H-206 · M | a dead holder's edges are deleted with him | none (holder half landed) | S-DOWN; R-WORLD |

### Contests and proceedings

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-PRO-1 | the game a computed case is heard under | SC M-SC-1 | D1 R-04; D3 THE BAR · S | `DOCKET_ARRANGEMENT: None` | none; IN-10 reverted | N; R-VARIETY |
| C-PRO-2 | a petition that rises; a receiver who may deny | SC M-SC-2, 8.3-g(H) | D3 ED-IN-0210 Ruling 2 · S | addressed to its own subject | contested (A-16) | S-UP |
| C-PRO-3 | the stasis issue ladder | SC M-SC-3 | D3 `PS/04_VERBS.md:249` · S | the charge ladder mislabelled | none | S methodology |
| C-PRO-4 | procedure before the vote: agenda, recorded defeat, `carry` | SC M-SC-5 · IN H-IN-6(B) | D4 SC-07 · M | `carry` declined | IN-45 (B-K); its gate would amend Layer 1 | R-WORLD |
| C-PRO-5 | a compromise scaled to the loss | SC 8.3-b(H) | D1 R-05 · M | no disposal reader | SC-03b (B-O) | R-COMPLETE |
| C-PRO-6 | arrangement data read in production | SC 8.3-c(H) | D4 · W | six keys read by nothing | SC-08: exit already met | E-OVERHEAD |
| C-PRO-7 | an obstacle ceiling that does not deprive | SC 8.3-d(H) | D1 Jordan 2026-09-06 · M | p = 0.0006 at ceiling 3 | SC-01 falsifier | R-COMPLETE |
| C-PRO-8 | a vote over the bench's commitments | SC 8.3-e(B) | D2 GD-3(b) · M | `commit` always refused | SC-01 step 11; J-4 | R-CHOICE |
| C-PRO-9 | the held questions: `scale:` column, nested deliberation, a common-fact store | SC 8.3-h(B), 8.3-i(B) · IN H-IN-8(B) | D1 Jordan 2026-09-02 · M | `scale:` read by nothing | HELD (J.2 rows 5-7) | S pause |

### The world, threadwork and the crossing

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-WLD-1 | thread operations as persons' acts | WR M-WR-1, IN-06(H), PC-06 K-3(H) | D3 #457 D1 · S | module runs; no verb; no `coherence` field | none builds it | N; S vertical |
| C-WLD-2 | what follows the crossing | WR M-WR-2 | D2 P-15 · S | no carrier | none | R-COMPLETE |
| C-WLD-3 | thread hand-offs to the field and the faction; Domain Echo | WR M-WR-3 · MB M-MB-9 | D5 A2 · M | empty `threadwork_check` hook | none | S diagonal |
| C-WLD-4 | a cost on Mending oneself; Mending by another | WR M-WR-4, M-WR-7 | D3 RULINGS C-1, E-1 · M | cost 0 at all 16 cells; not routed | none | R-CHOICE; R-COMPLETE |
| C-WLD-5 | the Calamity coupled to acts | WR IN-35(H/B) | D1 #457 answer · S | wear only | IN-35 (B-S), BLK IN-06 | N; S |
| C-WLD-6 | practitioner resilience (R-14) | WR WR-01(B) | D4 · M | built dark, gain 0 | WR-01 (B-S) | R-VARIETY |
| C-WLD-7 | authored ages for the body hazard | WR M-WR-8 | D3 #457 D2 · M | `age_at_build` 0 | none | R-WORLD |

### The player surface and pause

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-SUR-1 | the playable fight: suspension at ENCOUNTER, in-fight decisions | PC M-PC-4 · IN M-IN-2 · MB IN-46(B) | D1 R-04 c3 · S | callback only | IN-46, no build batch | R-PLAYER; S pause |
| C-SUR-2 | character spaces: creation, development, chronicle | GO M-GO-7 · IN H-IN-3(H) · NPC M-NPC-7 · WR IN-37(H) · PC M-PC-10(H) | D1 R-04 c3 · S | cast entry seated by the builder; `storybar.py` measures only | IN-47 no batch; IN-37 (B-U) | E-LEGIBILITY; R-VARIETY |
| C-SUR-3 | `explain(p, v)`, the derivation Layer 1 owes | IN M-IN-3 · GO M-GO-5 | D3 §C.11 · S | absent | none | E-LEGIBILITY |
| C-SUR-4 | odds shown before an act | GO M-GO-6 · MB M-MB-10 · PC M-PC-6 | D5 A3 · M | `eff_ob` display-only, no caller | none | E-LEGIBILITY; R-CHOICE |
| C-SUR-5 | the player's seat at DELIBERATE and at the duel yield | GO M-GO-4 | D3 L1-04:844-846 · S | serial loop; seat unspecified | none (IN-46: ENCOUNTER only) | S pause |
| C-SUR-6 | subsystem views: investigator's record, contest room, faction | FI M-FI-5 · SC M-SC-9 · FA M-FA-4 | D1 R-04 · M | carriers built, no surface | none | E-LEGIBILITY |

### Parity, the resolution kernel and the port

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-POR-1 | one die and one ladder for every scale | PC M-PC-7 · MB M-MB-11 | D3 Layer 1 03 · M | continuous Normal; three-band field result | none | S methodology |
| C-POR-2 | a canonical integer encoding of state | GO M-GO-1 | D3 L1-04:1119 · S | `repr()`; floats | none | S methodology |
| C-POR-3 | a portable draw primitive | GO M-GO-2 | D3 L1-04:916 · S | CPython `random.Random` | none | S methodology |
| C-POR-4 | port-readable fixtures | GO M-GO-3, GO-05(H/B) | D3 L1-04:913 · M | a Python literal | GO-05 lists paths only | S vertical |
| C-POR-5 | fixed-point resolution arithmetic | GO M-GO-10 | D3 L1-04:1119 · S | libm floats at the listed sites | none | S methodology |
| C-POR-6 | refusal as a typed value | GO M-GO-8 | D3 L1-04 rejection 5 · S | about 120 in-loop raises | none | R-COMPLETE |
| C-POR-7 | save by replay | GO M-GO-9 | D6 · W | no path | none | R-COMPLETE |
| C-POR-8 | a version and a slice that runs | GO GO-01(H/B), GO-06(B), PC-05(H/B) · PC M-PC-11(B) | D3 step 13 · M | skeleton extends an undefined base | B-Z; J-9 | N |

### The decision layer

| id | area | merges | demand | code | v9 | NERS |
|---|---|---|---|---|---|---|
| C-DEC-1 | what an ambition demands (an OUGHT's predicate) | NPC M-NPC-4 · IN M-IN-9 | D1 R-06; H-185 · S | read by nothing | none (zero mentions) | R-COMPLETE |
| C-DEC-2 | self-interest weighting | NPC M-NPC-12 | D3 ED-IN-0261 · M | `benefits_me` has no caller [CHECKED] | none | R-VARIETY |
| C-DEC-3 | a damping bound on self-feeding loops | IN M-IN-11 | D4 H-25, H-106 · M | no cap, decay or closer | `forgive` (B-Q) | R-COMPLETE |
| C-DEC-4 | a controlled multi-season reading | IN M-IN-10 | CLAUDE.md §7 gap · M | `arms` sweeps one mechanic | none | R (every verdict's denominator) |
| C-DEC-5 | R-05 owned by a position | IN H-IN-1(H) | D1 R-05 · S | relaxed exit reads DONE-test | none | — |
| C-DEC-6 | cohorts with pursuits and an internal spread | SE B-SE-1(B), B-SE-2(B) · NPC B-NPC-2(B) | D1 R-06 · M | pursuit term 0 | SE-06 ask-then; SE-04 (c) HELD | R-CHOICE |
| C-DEC-7 | loyalty and grievance that move choice | NPC H-NPC-3(H), H-NPC-4(H) | D1 R-07 · M | hash EQUAL at `legacy`; alignment fixed at build | IN-58, IN-69, IN-70 | R-WORLD |

### PLANNED-UNBUILT and BUILT-DARK (second table)

The lanes file 149 such rows (MB 11, PC 8, FI 15, SC 17, FA 18, WR 8, IN 30, GO 9, SE 19, NPC 14). They are not
missing under the v9-built assumption; they are unbuilt or unarmed in code. Grouped by what builds or arms them
(families, not a row-by-row merge):

| family | what builds or arms it | lanes |
|---|---|---|
| IN-12's twelve verbs (seize, covenant, sabotage, tend, argue, train, conceal, forgive, arrest, pardon, interrogate, raze) | B-K, B-M, B-Q, B-R | IN, MB, PC, FI, SC, FA, SE, NPC |
| arrival, occupation, foreign march | IN-13 (B-M), IN-36 (B-V) | MB, FA, WR, NPC, IN |
| goals, salience, opinion, scar re-read, doctrine pull | IN-62..72, FA-04..06 (B-X) | FA, NPC, IN |
| proceedings core and tail | SC-01..04, SC-07, SC-08 (B-N..B-P) | SC, FI, IN |
| inquiry degree, role, counter-espionage, knots, `thread_read` operand | FI-01..03, IN-32, PC-06 K-3 | FI, WR, PC, NPC |
| `forge`, `work`, `migrate`, `carry`, `found`, `build`, the levy referent | IN-45, IN-28, IN-49 (B-K) | FI, SE, SC, IN |
| levied stores to the field (`field_provisioning` absent from code) | IN-52 (B-T) | MB, SE, FA, IN |
| legitimacy and stability, ending, insurgency | IN-23, IN-27, IN-30 (B-U) | FA, SE, GO, IN |
| Calamity coupling | IN-35 (B-S) | WR, SE, IN |
| chronicle render, character space | IN-37 (B-U), IN-47 (no batch) | FI, WR, GO, NPC, IN |
| duel terms, co-location, access gate | PC-10, IN-59, IN-60 (B-Y) | PC, NPC |
| delegation, revocation cost, succession | IN-48 (B-JR), IN-31 (B-Q), IN-61 (B-R) | FA, SE, NPC |
| `exchange`; `comply`, `evade / defy`, `construe` | IN-33, IN-09 (restorable, no batch) | SE, FA, IN |
| cast overlays; act budget | IN-38 (B-V); IN-14 (B-J by its entry) | NPC, FA, IN |
| forcing knobs: `age_step`, `illness_rate`, `age_at_build`, `body_step`, `season_factor_draw` | no position; values Jordan's (H-208, J-6) | WR, SE, NPC, IN |
| person knobs: `scar_weight_shift`, `confliction_weight`, `scar_excludes_actor`, `refusal_axis`, `intent_disclosure`, `said_slant`, `telling_privacy`, `stance_polarity` | none, IN-65 (conditional), ED-IN-0296 (ask-then) | NPC, PC, SC, FI, IN |
| field knobs: `field_morale_loyalty_gain`, `MB_SUPPORT_RANK_CAP` | none; MB-07r (J) | MB, SE, FA, NPC, IN |
| built carriers with no reader: `urgency`, `benefits_me`, σ-leverage, `head()`, `at_war`, `faction_sheet`, `uncontrolled`, `proofs`, D-6/D-7, `bench_quorum`, `destroy_record`, `confer` via seat, `View`, the play-surface seam, the combat trace, `eff_ob`, module traditions and weapons | various; most none | all ten |
| the contest kernel's retirement | SC-05, HELD | SC |
| thread pricing, authored TS, the history term | IN-06, K-3, a ruling | WR |

---

## C7. DECISIONS FOR JORDAN

Every choice the lanes leave to Jordan, deduplicated, after CLAUDE.md §0's five-step ladder and C4's rule
removed those a source already decides (the parity contract, X-5's DELIBERATE seat, X-17, the faction-level
GD-2 pass, the felled actor). Parameter values marked `[OPEN — Jordan tuning]` are not listed one by one; they
ride the decision whose form they fill.

| id | question | (a) | (b) | what each does to the game | hinges | blocked until decided |
|---|---|---|---|---|---|---|
| J-C-1 | the store act's name (statement 5 already rules `levy` wrong for it) | a new name, Jordan's; `levy` becomes the troop verb | — | (a) is the only option the statement leaves; the name is his | MB, SE, FA, IN | R-C-2, R-C-10; IN-49, IN-52, H-163 re-statement |
| J-C-2 | troops: persons or a stock | a levy lowers cohort `weight` and raises a stock by the same headcount (persons) | a non-person troop kind in `matter_kinds`, uncoupled from population | (a) casualties are population losses, so war has a demographic price (20G A3, Proposal F); (b) simpler, separable, war costs no labour | MB, SE, FA, IN, NPC, PC | R-C-2, R-C-11, R-C-13's cohort half; also the men-per-weight scale |
| J-C-3 | the source of per-person capacity, and J-13's reading | one stored source read by pool, `Combatant`, command and competence | identical capacities are intended; withdraw the claim that personal resolution varies by person | (a) persons differ in what they can do; R-09 can be met; (b) a game of wants alone. Sub-questions: new `Person.attributes` (K-2) or existing `capability` (X-14); the actor's own fallible reading, owed or not (X-15) | PC, SC, MB, NPC, IN, FI, WR, GO | R-C-1, R-C-23's competence half, R-C-37's attribute half |
| J-C-4 | a standing winner's wounds | written | not written | (a) every fight costs both sides; (b) the winner walks away whole, as `march`'s loser-only rule already reads | PC | the rest of R-C-13 |
| J-C-5 | the top seat replaced by others | allowed (a third revocation basis) | not allowed; abdication only | (a) overwrites the 2026-10-12 duchy ruling and SC-04; (b) keeps it | FA, SC, NPC | R-C-30's replaced arm |
| J-C-6 | do persons lie | yes: a lie is a deed claim a witness can hold False | no: close deception and intent-keeping; credit rests on cell agreement | (a) testimony, interrogation and the mirror test have something to catch; (b) cuts G7, H-198, H-191 | SC, IN, FI, NPC | R-C-35, R-C-14's "withheld or false" |
| J-C-7 | how a petition closes | `destroy_record` (blocked by A-13) | a new `deny` row (against A-16) | either delivers ED-IN-0210 Ruling 2; they differ in what a denial leaves in the log | SC, IN | R-C-16's closer |
| J-C-8 | a failed or refused inquiry | failure as error, refusal witnessable (K-FI-7, K-FI-8) | failure as ignorance, refusal silent (the SKIP arm) | (a) a confidently wrong finding and a visible attempt; (b) today's silence; H-111 records both as defensible | FI | R-C-23's second half; FI-01's exit |
| J-C-9 | population | grows at CENSUS until `capacity` refuses (RR-2) | fixed; delete `Rung.envelope` | (a) a lagged population (20G axis 6); (b) a closed world that only shrinks under forcing | SE, WR, NPC, MB | R-C-9, R-C-32's forcing half |
| J-C-10 | what counts as MISSING | strict: no position at all | wide: no position that delivers the behaviour (LEAVE, unscheduled batch, a hollow exit) | changes the counts, not the game; this file uses wide for C6 entry and keeps the lanes' own classes | all | nothing in the game; the next count |
| J-C-11 | the Godot version (J-9) and the fixed-point table resolution | — | — | parity itself is decided by Layer 1 (C4) | GO, PC | GO-01, GO-05, PC-05 |
| J-C-12 | what the player sees: AX-7's gloss or §C.11 | the gloss: no state hidden | §C.11: the arithmetic of what the character holds | (a) admits true odds; (b) odds only as the actor's estimate. Sub-question: is a band shown (PS 15 against COMP S6) | GO, IN, SC, MB | R-C-38 |
| J-C-13 | the ending | a Query over seats persons' acts hold, GD-1's thresholds struck | GD-1 kept, its stability term read from a seat-holder's estimate and Accord given a carrier | threshold victory against choice-only victory; 15 or 17 territories | FA, WR, SE | R-C-31; IN-27 |
| J-C-14 | GD-2's threat response | a duty on the threatened holder | retired | (a) a person's question names the threatened territory; (b) removes a canon row | MB, WR, FA, IN | C-FAC-11 |
| J-C-15 | war's gate | declare-then-march: `march` requires `at_war` | `fight` is the gated act; or march freely | which act a war licenses; F.33 open | MB, FA | R-C-12's gating half |
| J-C-16 | repetition in a season | 03 §C.2: triage is the mechanism (keep the dedup filter) | 03 §C.3: no dedup (delete it, re-measure the monoculture) | overwrites ratified Layer 1 either way | IN | the dedup filter |
| J-C-17 | offices in computed play | `revoke` and `establish` must execute through a general motive | they read DONE-test | (a) offices change hands by persons' choice; (b) by hand-built test only. Includes a delegate's early dismissal (X-13) | IN, FA, NPC, SE | R-C-19's dismissal half; IN-31's exit |
| J-C-18 | one substrate and the field's margin | combat and mass battle roll the season's die and grade on `degree_from_net` | combat keeps its continuous roll and the field its three bands, stated in Layer 1 | (a) one ladder (S methodology); (b) moves no balance figure; (a) rewrites ED-IN-0279's writes | PC, MB, IN | R-C-3's substrate half |
| J-C-19 | death in battle | a lost field kills | wounds only | two games of war | MB | R-C-34 |
| J-C-20 | a commander's fate in a field | a duel scene at ENCOUNTER | scaled by the side's fraction | which acts may interrupt a battle | MB, PC, IN, GO | R-C-24's interrupting acts |
| J-C-21 | experience on a stock | one averaged grade | separate entries per grade | legibility against fidelity | MB | R-C-2's experience half |
| J-C-22 | the crossing | removal from play | continued play as an altered being | P-15's consequence | WR | R-C-26's crossing half |
| J-C-23 | the thread pool's History term (PP-624) | the code's reading: `min(3, history + 3)`, inert at history ≥ 0 | `min(3, history) + 3`, worth up to +3D | whether History matters to a thread roll | WR | the term |
| J-C-24 | Coherence's elastic return | a licensed clock on the being | the effect of a rest a person chooses | a fourth clock against an act | WR | `coherence.recover()` |
| J-C-25 | forcing values (ages, illness, hunger, weather) | Jordan's values (#457 D2's gate; J-6) | — | unwatched seasons carry dearth and death, or do not | WR, SE, NPC | R-C-32 |
| J-C-26 | kin | a tie kind the heir title reads | the heir stays a title | dynastic against title game | NPC | IN-61's eligibility |
| J-C-27 | a creed after its head dies | binds the man (schism) | binds the seat (vacancy) | regicide splits or transfers | NPC | dead-referent state |
| J-C-28 | self-interest | build ED-IN-0261's weighting on `benefits_me` | delete `benefits_me` | persons who weigh self-interest against those who do not | NPC, IN | R-C-8's `benefits_me` cut |
| J-C-29 | proceedings | a disposal's `degree` read as term length, or as release price (K-SC-5); a nested deliberation inside RESOLVE, yes or no (H-56) | — | how hard a narrow win binds; whether a contest reacts mid-fold | SC | R-C-28, SC-01 step 15 |
| J-C-30 | settlements | production authored by place (K-SE-10); persisting dearth deposited every season (K-SE-7, re-opens H-160 (3)) | — | interdependent towns; neglect known at the seat | SE | the two rows |
| J-C-31 | played fidelity | the duel decision set (J-15); whether a player commands a field once it starts; creation as an act or a selection | — | how much of a fight or a battle a player touches | PC, MB, IN | R-C-37 |

---

## C8. CONSOLIDATED KEY RECOMMENDATIONS

Forty, distilled from the lanes' 112 K-rows (MB 12, PC 9, FI 8, SC 12, FA 12, WR 12, IN 12, GO 11, SE 12,
NPC 12, withdrawn rows excluded). *Ladder* is CLAUDE.md §0's: a takeable step number, or Jordan with the C7 id.
Meta-rule: a row that adds a system names what it removes. None is entered in the plan or a ledger until
Jordan so rules.

**Top ten, and why this order.** R-C-2 (troop stock) first because it is Jordan's own demand, contradicted by
the plan, and six lanes wait on it; R-C-1 (capacity) second, because it is the one source whose absence
starves the most seams; R-C-3 (one die, monotone) third, because R-C-1 wakes the latent sawtooth (D-26);
R-C-11 (order of battle) fourth, because it turns the stock into the subunits statement 4 asks for; R-C-37
(the surface batch) fifth, because M1 cannot be met without it and its designs exist; R-C-23 (inquiry yield)
sixth, because it puts content into the chronicle's thinnest input; R-C-12 (war) seventh, because the
strategic layer has no conflict without it; R-C-8 (deletions) eighth, cheap and shortening every later read;
R-C-29 (vacancy by claim) ninth, because it unblocks succession; R-C-4 (integer hash) tenth, because every
golden re-pin after it is the last of its kind.

### PRIMITIVES

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-1 | Rule one source of per-person capacity, stored once and derived at read by the contest pool, the `Combatant`, a commander's command and a witness's competence. | K-IN-1, K-NPC-1, K-PC-1, K-SC-2, K-FI-1, K-GO-8 (attributes), audit G1 | Jordan (J-C-3) | adds four readers; cuts `pool_default`, `obstacle_default`, `competence = 1`, `command=4`, the unread `stats`/`ts` | J-C-3; R-C-3 | two persons differing only in capacity resolve differently over the same seeds; equal capacities reproduce today's `content_hash` |
| R-C-2 | Give each settlement a troop stock by kind, raised by `levy`, fielded by `march`, drawn down by a lost field and graded by equipment, experience and commander. | K-MB-1, K-MB-3, K-SE-13, K-FA-13 (stock), K-IN-13 | Jordan (J-C-1, J-C-2, J-C-21) for form; direction is statement 1 | adds a count per kind and one write on `levy`; cuts `_weighted_unit`'s weight feed, `_SEASON_FORCE_POWER`, IN-52's stores bound, the planned `field_provisioning` | J-C-1, J-C-2 | a seeded levy raises the stock by the headcount drawn; a march fields it; a lost field lowers the next levy; arm off reproduces the hash |
| R-C-3 | Put every per-die figure in one owner, adopt an obstacle rule under which a more capable equal pair never has worse odds, and rule one substrate and one field margin. | K-IN-5, K-PC-8, K-MB-8, audit G2a, G2c, G2d | owner: step 4; substrate and margin: Jordan (J-C-18) | adds nothing; cuts three literal owners, then the losing substrate or a Layer 1 sentence | — | grep finds the per-die pair defined once; the odds table is monotone in capacity |
| R-C-4 | Fold state into `content_hash` through one integer encoder with declared field order, and move the baseline fixtures into authored YAML a port can read. | K-GO-1, K-GO-4, K-GO-5 | step 3 (L1-04:1119, :913) | adds an encoder; cuts the `repr()` path, floats in `Person.pursuits`, the Python literal as head | — | an independent encoder prints the same seed-0 hash; a planted float is refused; a YAML edit moves the hash |
| R-C-5 | Own the draw primitive behind `H(seed, tick, subject, purpose)` and resolve every draw in fixed point. | K-GO-2, K-GO-11 | step 3; table resolution Jordan (J-C-11) | adds tables under one owner; cuts `random.Random`, the stdlib fallback, libm calls | R-C-4 | a second implementation from the tables alone reproduces 10,000 seeded outcomes |
| R-C-6 | Let a person hold a `held_by` claim when he witnesses a seat over a place conferred, revoked or vacated, and let regard reach a place through its holder. | K-SE-2 | step 5 | adds a deposit occasion; cuts the ABSENT H-195 marker | — | after one realm season some persons hold `held_by` (0 of 80 today); a hostile person scores `march` on that rung above zero |
| R-C-7 | Read adjacency from the geography already parsed, as one Query, for contiguity, spread and distance; and have Jordan rule whether production follows the map. | K-SE-3, K-SE-10 | step 3/4; map production Jordan (J-C-30) | adds one Query, no state | — | two non-adjacent uncontrolled territories form no group; two adjacent do |
| R-C-8 | Delete what the season carries and nothing reads: `urgency` (after IN-62), `benefits_me` (unless J-C-28 builds it), mass battle's survivor-ratio degree, the empty `rally_check` and `threadwork_check` hooks, D-6/D-7 and three unread arrangement keys, the seam's `winner`, the skeleton's Key-type resources. | K-IN-2, K-MB-7, K-MB-11, K-SC-10, K-PC-3, K-GO-10, audit G2b, G5 | steps 2-3 | cuts only | X-1 order | `content_hash` at seed 0 equal before and after each deletion |
| R-C-9 | Give each settlement's population one carrier, cohort `weight`, and let it grow at CENSUS until `capacity` refuses, or rule it fixed and delete `Rung.envelope`; let `work` scale with that weight. | K-SE-1, K-SE-8 | Jordan (J-C-9); `work` half step 5 | adds one CENSUS term or nothing; cuts two of three population carriers | J-C-9 | over ten fed seasons a cohort's weight rises and stops at `capacity` |

### VERBS

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-10 | Give the store act its own name and row, price it by the hunger it leaves, and let the person taxed comply, evade or defy before it runs. | K-SE-5, K-FA-5, K-IN-13 (name) | name Jordan (J-C-1); price step 5; answer step 3 | renames, no new act; cuts the misnaming across IN-49, IN-52, H-163 | J-C-1; D-20, D-21 | after the rename `levy` writes no goods; with `body_step` > 0 a taxed cohort's body falls |
| R-C-11 | Let `march` carry an order of battle chosen by the marching seat (which stock kinds, how many subunits, each role) and build every season side through `build_army` moved into `modules/mass_battle/`. | K-MB-2, K-MB-4, K-FA-13 (composition) | step 5 | adds one operand; cuts `_MVP_SUBUNIT_SHAPE`, the fixed `Line`, `make_mixed_unit` | R-C-2 | equal stocks under different orders of battle give different outcome distributions |
| R-C-12 | Let a person whose goal holds stance −1 toward a rival seat utter WAR, and let one act read `at_war`. | K-FA-1, K-MB-5 | producer step 3; gate Jordan (J-C-15) | one payload read and one conjunct; no object | the own-echo precondition (D-7) | seed 0 yields a WAR Proposition with a live `commit`; a march without one refuses (if gated) |
| R-C-13 | When a fight fells its actor, write it as the subject's felling is written; refuse a fight one of whose parties is a cohort until a cohort can be fought at its weight; require co-location for every lethal act. | K-PC-2, K-PC-12, K-NPC-12 | felled actor step 4; refusal step 5; co-location step 3; standing winner Jordan (J-C-4) | adds a second subject write and two conjuncts; cuts the false `contest.undecided` and the free remote kill | heads housed at seats (D-25) | a seeded fight that fells its actor removes him; no death joins persons in different places |
| R-C-14 | Let `interview` yield testimony: the questioned person's own `tell` to the asker about the matter, true, mistaken or withheld. | K-FI-3 | step 4 | adds the matter as the Event's subject | J-C-6 for "false" | B, holding a claim about C, holds a `tell` to A about C in his next opening set |
| R-C-15 | Let a concealer's own score set what an inquiry into what he concealed faces. | K-FI-5 | step 3 | adds a branch to `_obstacle_of` | `forge` executing (D-12) | inquiries into a forged and a true Record face obstacles differing by `forgery_quality`/2 |
| R-C-16 | Address a computed petition to the holder of the seat above its subject, and give the receiver a way to close it. | K-SC-3 | address step 4; closer Jordan (J-C-7) | no new verb for the address | — | a petition about a person reaches a different person above him |
| R-C-17 | Let the person who opens a case name the game it is heard under, from a writ or remit he holds. | K-SC-1 | step 5, after IN-10 | one operand binding; cuts `UNDECLARED_DISPOSAL` as the computed path | IN-10 restored (D-13) | ≥ 1 computed `determine` opens a `detain`, `ban` or `succession` hold; disabled operand gives 0 |
| R-C-18 | Make the thread operations persons' acts resolved by `operations.py` and writing Coherence through the seam; keep `restore` for fabric; seed Thread Sensitivity from authored values once a writer exists. | K-WR-2, K-WR-3, K-WR-1 | step 3-4 | verb rows on an existing resolver; cuts the module's Coherence store, the empty hook, IN-35's `restore`-as-Mending | IN-06 (D-18) | a working writes `(Person, coherence)`; deleting the rows returns today's hash |
| R-C-19 | Let a ruler delegate by establishing and conferring a termed second seat over his domain, ended by its term or the delegate's `release`. | K-FA-11, K-SE-6, K-NPC-8, K-IN-4 | step 3; early dismissal and computed `revoke` Jordan (J-C-17) | one seat row per delegation; cuts the reverted `delegate` kind | — | a deputy acts `via` the seat while the principal keeps his hold; after the term the act refuses |
| R-C-20 | Give a broken vow its own deed, and end a covenant party's `commit` when he acts against its terms. | K-NPC-5, K-FA-2 | step 3-4 | one cell pair, one reader; no new Event kind | — | witnesses of a vow-break and of a plain `release` judge different valences |
| R-C-21 | Publish an edict as an `issue`d Record addressed to everyone in the seat's purview, instead of building `proclaim`. | K-FA-12 | step 4 | one addressee form; cuts the deferred `proclaim` row | — | the edict deposits claims in persons in purview and none outside |
| R-C-22 | When IN-33 restores `exchange`, let seat-holders trade rungs' stores through it, and seed no `negotiation` game before then. | K-SE-4, K-SC-11 | step 4-5 | a seat-treasury reading of operands; no price object | IN-33 | two rungs with complementary surpluses trade, conserved |

### MECHANICS

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-23 | Give every inquiry a yield on the content-deposit model, starting with Records, without widening `requires_typed`; keep refusal distinct from Failure; land investigation's role only with a provider. | K-FI-6, K-FI-9, K-FI-7, K-FI-8 | Records step 4; role step 3/5; error and refusal Jordan (J-C-8) | one trigger on an existing deposit; cuts `research`'s content-free yield | — | a Success `research` on another's Record leaves its content in the actor's ledger, no `hold` |
| R-C-24 | Let a battle stop at a phase boundary for a present person's act (a commander's duel, a thread act) and resume with the result, reading a duel only as a fraction of the side. | K-IN-6, K-MB-10, K-PC-5 | form step 4; which acts Jordan (J-C-20) | one yield point; cuts the flat `Command=0` rout, the empty hook, M-6's LEAVE | R-C-37 | a field whose commanders duel differs from a control where the duel is forbidden |
| R-C-25 | Bound the troops a side fields by the smaller of its stock and what its treasury can ration. | K-MB-6 | step 3 | IN-52's input becomes the stock | R-C-2 | a full stock with an empty treasury fields no more than the bound |
| R-C-26 | Feed the Calamity's coupling from the strain thread acts leave; price Mending one's own configuration in its Ob and route a Mending aimed at another; give the crossing a consequence. | K-WR-4, K-WR-6, K-WR-5 | step 3; crossing Jordan (J-C-22) | one coupling input, one Ob term, one branch; cuts `ms_track.py` | R-C-18 | Menders stabilize and workers destabilize against a no-acts arm; repeated own-aim casts cost more |
| R-C-27 | Let allegiance move with deeds done to oneself (revoked, passed over, bound), a hearer learn whether a told intent was kept, and a teller's word weigh by the hearer's claims about his seat. | K-NPC-7, K-NPC-10, K-SC-7 | step 5 | kinds in `PAIRED_KINDS`, a reconciliation at read, a producer for `rank_gain` | — | a person whose seat his head revokes reads lower regard toward him than a matched control |
| R-C-28 | Give the contest the stasis `issue` ladder, a reader for a disposal's `degree` (or stop writing it), and a recorded defeat a later speaker can cite. | K-SC-4, K-SC-5, K-SC-8 | steps 3-5; reader Jordan (J-C-29) | four roster members, one reader, one write; cuts the mislabel and `records_dissent` | SC-03b | a `Partial` and a `Success` determination differ later on the disposal edge |
| R-C-29 | Keep a dead seat-holder's ended edges so witnesses name his office and the vacancy reaches every person who holds a claim of it. | K-NPC-3, K-PC-10 | step 3/5 | no carrier; cuts `World._departed` | — | after a seeded regicide, a non-conferrer holds a claim naming the office |
| R-C-30 | Found an insurgent faction only when persons utter a creed and two commit; let a crisis offer a top holder his own resignation; make the highest seat-holder the faction's head; let the Church's appetite rise with its holdings. | K-FA-7, K-FA-3, K-FA-4, K-FA-8 | steps 3; head and replacement Jordan (Layer 1 B.6.1; J-C-5) | cuts the `Tenure.degree` derivation, a third revocation basis, FA-07's planned Church Query | own-echo precondition | sustained `uncontrolled` yields a creed with ≥ 2 commits; a control does not |
| R-C-31 | End the realm on a Query over seats held through persons' acts, and re-express or strike GD-1's terms and GD-2's pass. | K-FA-6, K-WR-10, K-WR-12, K-IN-12 (GD-2) | Jordan (J-C-13, J-C-14) | cuts canon clauses; adds nothing | — | every hold the ending reads traces to an act in `w.log` |
| R-C-32 | Arm or delete every dark person and world knob; author an age for each named person and ship weather, hunger, ageing and illness at Jordan's values. | K-NPC-2, K-WR-9 | step 3 (arm-or-delete); values Jordan (J-C-25) | cuts each knob not armed with its hole row | R-C-9 (D-19) | a four-season realm in which pursuit weights and bodies move, the hash declared |
| R-C-33 | When `seize` lands, let the taker's terms be what he does with the place's seats (confirm, or revoke and confer). | K-SE-9 | step 5 | no terms object | R-C-6; IN-12 step 6 | a seated person left in place and one revoked hold different stance toward the taker |

### TEXTURE

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-34 | Let a lost field kill and emit `person.died`. | K-MB-9 | Jordan (J-C-19) | one emission; cuts the `max(1, …)` floor | R-C-2 | a seeded field kills a named loser |
| R-C-35 | Let a teller speak a lie at `said_of`, a deed claim a witness can hold False. | K-SC-6, K-IN-7 | Jordan (J-C-6) | one value rule; cuts the ABSENT H-198 marker | — | a hearer holds a value differing from the teller's, not from a `Partial` |
| R-C-36 | Read an ambition's predicate, so it is achieved or thwarted. | K-NPC-9 (with K-IN-2's predicate half) | step 5 | one reader at Q4, or the field's deletion | IN-66 | a person whose OUGHT's predicate holds stops receiving its question |

### SURFACE

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-37 | Batch IN-46 and IN-47; seat the player at DELIBERATE and at the duel yield, excluded from the pooled map; let creation write a cast entry in the shape world-gen seats; fight a played person's fight one engagement per act. | K-IN-10, K-GO-3, K-GO-8, K-PC-4, K-GO-9 | step 3-4; decision set and creation Jordan (J-C-31) | one batch, one exclusion clause; cuts `fight`'s separate RESOLVE-time path for played persons | — | AUTOMATED and PLAYABLE with the chooser's choices end at one hash; a differing choice moves it |
| R-C-38 | Build `explain(p, v)` from the holder's own claims as the one owner of every derivation shown; show odds only as the character believes them. | K-GO-6, K-GO-7, K-IN-9, K-SC-9, K-MB-12 | Jordan (J-C-12) | one function; cuts the losing Layer 1 sentence | J-C-12 | `explain` takes no `World`; two persons with different claims see different odds |
| R-C-39 | Render the chronicle and every view (character, investigator's record, faction, settlement) as projections of what the person holds, carrying each act's decisive content. | K-WR-11, K-NPC-11, K-FI-11, K-FA-9, K-SE-12, K-PC-9 | step 3-5 | no store; one renderer, several inputs; cuts the trace key and a second render path | R-C-23, R-C-37 | two persons read different chronicles; none shows an unwitnessed event |

### APPARATUS (IN only)

| id | recommendation | merges | ladder | adds / cuts | depends | falsifier |
|---|---|---|---|---|---|---|
| R-C-40 | Make `arms` sweep any fixture knob over N seasons, and untrack run output, fork-delete `params_tables.yaml`, re-point the dead CANONICAL path and AX-7's stale sites. | K-IN-11, K-IN-12, audit X1, X3, G6 (sites), G8 | steps 1-4 | two arguments; cuts about 87,000 tracked lines | — | a planted difference is detected over N seasons; a clean checkout gives the same deltas |

<!-- APPEND -->
