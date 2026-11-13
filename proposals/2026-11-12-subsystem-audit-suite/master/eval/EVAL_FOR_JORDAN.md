# Evaluation of workplan v11 and the gap register: what was for you, and how it was settled

## Status: REFERENCE (a decision register for stage 5 of `STAGES.md`; resolves nothing at runtime, CLAUDE.md §0.05; not canon; deleted when workplan v12 is adopted)

## Read at: the working tree of 2026-11-12. Lane: the evaluation's settle-and-merge pass, after your answers A-100 to A-114 (`unified/DECISIONS_ANSWERED.md`).

**What this is.** The eight evaluation lanes raised eleven items for you (three of them the same question asked three times). You have answered eight; the other three were settled by the five-step ladder (CLAUDE.md §0: superseded, irrelevant, design document, precedent, architecture), and each is recorded below with the reason, so you can reverse any of them in one line. Form as `unified/DECISIONS_FOR_JORDAN.md`.

**Open questions: none.** Nothing in the evaluation is waiting on you. Two things are worth your eye (end of this file); neither is a question.

## Answered by you

### EVAL-1 · How many seasons may the re-take of the nine run? · answered (A-114)

**Your answer.** No four-season re-take at each milestone: the plan's two-season cap (v11 P10, and P16 clause 1) governs every probe and every batch close; the longer re-take of the nine runs **once, as the plan's very last item, after M5**, as its closing gate. **What changed.** P10 and P16 (1) are carried into v12's head as standing rules with that one exception; the instruction suite's per-milestone re-take items (IS-A-13) stop at each milestone close; the four-season `measure:` strings of R-04, R-05 and R-09 are read at two seasons or left as they stand until the end. **Sources:** `master/eval/E1.md` EVAL-1; v11 `-00` P10, P16; `master/instructions/IS_A_NINE_part2.md` IS-A-13.

### EVAL-3 = J-E2-01 = J-E3-1 · May a march be refused for want of a claim? · answered (A-103)

**Your answer.** Option B: a claim is the occasion for a march, not a gate. **What changed.** v11's claim gate on `march` (CR-91 part 3) is retired; the claim carrier (CR-91 parts 1, 2, 4, 5) is built as occasion and as context for regard and legitimacy, first in the new faction batch so the battle verbs can read it; the cap of one march per season into a territory stays as your test limit; `30_WR_A_the_era_is_a_named_period.md` line 65 is corrected. **Sources:** E1 EVAL-3, E2 J-E2-01, E3 J-E3-1; v11 CR-91, IN-36, M10.

### E-3 (M31 (b)) · Do management orders cost scene budget? · answered (A-104)

**Your answer.** No: an order is not a scene; performing one may prompt a scene, which costs as any scene does. **What changed.** M31 (b) and E-3 are retired; the management surface (CL-MGMT) is no longer held on M31; the rule is a v12 item and a declared hash mover. **Sources:** E5 P15 M31, E-3.

### E-4 · May a person's manner differ from what his pursuits project? · answered (A-108)

**Your answer.** Yes, a stored offset on each manner axis. **What changed.** E-4 is retired; M34 and the personality layer (CL-PERSON) are built with offsets, behind a neutral-control gate that reproduces today's hashes at zero offset; CL-PERSON stays held on its other questions (M35 to M37, M40) as v11 states. **Sources:** E5 P15 E-4, M34; v11 CL-PERSON.

### H-1 · Your words of 2026-10-28 · answered (A-111)

**Your answer.** Let the relayed text stand. **What changed.** v12 carries the owed ledger rows (M31, M32) as relayed, marked as such; the menu-budget part is already A-104's. **Sources:** E5 P15 H-1.

### H-132 · May a territorial superior reduce a foreign faction's officer's grant? · answered (A-105)

**Your answer.** A reduction is judged as a revocation, and its odds read the power between the two factions: the host cannot strip a stronger faction's appointee unless that faction is persuaded; foreign officers are uncommon. **What changed.** H-132 is carried as one clause at `state/gate.py::may_fill`, in the first new faction batch. **Sources:** E6 H-132.

### H-325, H-326 (residue) · Does the game have exploration? · answered (A-109)

**Your answer.** No general exploration act (travel and inquiry cover ordinary discovery), but a way to find what is hidden. **What changed.** The exploration-act part is retired; the find-the-hidden design is a design-first item for the settlements and fieldwork lanes (how a place or event is hidden, how it is found by a drawn act under the one opposed rule, what finding yields, the exposure risk at depth, which gives `surveil`'s Exposure effect its carrier). **Sources:** E8 H-325, H-326r, CF-E8-5.

### J-E3-2 · `RemoteTrigger` in the deny-list · answered (A-110)

**Your answer.** Not now. **What changed.** v11 A1-80 is retired; CLAUDE.md §11's standing rule (add a primitive once one is seen arming a routine) is the only mechanism. **Sources:** E3 A1-80, Block 8 (a).

## Settled by the ladder (reversible: say so and it flips)

### EVAL-2 · Do the army verbs still count as built out through the preset menu? · settled: Option B

**What it was.** You ratified (2026-10-31, ED-IN-0307) a clause that `recruit`, `form_unit` and `assign_troops` count as built out when the harness's preset order of battle does them through the menu, because the chooser was barred from forming them; CR-52 would build that door. **How it was settled.** Ladder step 2 (irrelevant): the session takes the army verbs off the barred list so the chooser forms them (`14_VERBS_MILITARY_C_the_muster.md:210`, `_D:185`), and the requirement text counts only what the chooser forms (`IS_A_NINE.md` §6); the bridge has nothing left to cross, and keeping it would give one quantity two ladders. Option B was E1's lean and stated default. **Result.** CR-52 is not built; CR-46's menu clause is retired; the three verbs count once the chooser forms them (B22). **To reverse:** say "keep the menu door" and CR-52 returns ahead of B22.

### J-E3-3 · The "4.6" in v11 · settled: v11's 4.6 question is wrong at the ledger

**How it was settled.** Ladder step 1 (superseded): `registers/editorial_ledger_go.jsonl` ED-GO-0002 records your ruling of 2026-10-09 for the 4.7 series, given minutes after and superseding the 4.6 note; CLAUDE.md names that row as the one owner of the engine version. **Result.** v11 M13 and A1-44 are dispositioned WRONG (premise false); v12 writes no version number and points at ED-GO-0002; the GO early landing that reads the version reads it from there.

### J-E3-4 · A common-fact store beside RS-29 · settled: no store

**How it was settled.** Ladder step 3 (a design document: AX-7, no unmediated world truth) and step 4 (precedent: v11 took its option (a), the channels are the shared ledger; no session proposal builds a store); you excluded the store from RS-29's ratification and nothing since has asked for one. **Result.** v11 A1-48 is dispositioned DONE-IN-CODE (the decided state, channels and no store, is the tree's).

## Worth your eye (not questions)

- **Two things a lane flagged that were not asked of you and need no answer now.** (1) CR-105 (the flow-conditioning fold's last position) will need its AX-2 text when its gate opens; it is carried held at the end of the new flow batch (E5). (2) The instruction suite said nothing supersedes CR-94 (the forger's rule); two session proposals and A-26 do, so it is retired here, an `[ASSUMPTION]` the v12 author can reverse if the instruction lane meant otherwise.
- **A-101's consequence text** (initiative among the carried state; "round" for the season's lap in A-63/A-64) is listed for you by the round lane (`master/pc_round/PCR_FOR_JORDAN.md` item 1), not by this pass.
