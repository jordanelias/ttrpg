# Instruction suite IS-B3 — FA, SE, WR and GO as standalone playable games

## Status: PROPOSED (stage 4 of `STAGES.md`, lane IS-B3; batch-shaped instructions for workplan v12; nothing here is applied; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: `b07fc1c` (working tree of branch `ccr-62958c70-0kjhsw`, 2026-11-12). Producer: Fable, lane IS-B3. Work order: `master/INSTRUCTION_SUITE_ORDER.md`. Parts: this file (head, FA, SE), `IS_B3_FA_SE_WR_GO_part2.md` (WR, GO, the tables v12 takes, limits).

## 0. What this file is, and how to read an item

**What it is.** For each of four subsystems (faction and governance FA, settlements SE, the world WR, the player surface and port GO): the standalone-playable test of the work order, read against the tree at this SHA and against the suite's proposals; the batch sequence of `unified/U3_DEPENDENCY_ORDER.md` that gets the subsystem to that test; and one `Item:` for each thing the existing proposals do not carry. It does not restate a proposal's edits. An item that points at a proposal says so and adds only what is missing.

**What it is not.** It is not v12 and it moves no requirement row. Every reading quoted as "today" was taken by a command named beside it, at this SHA, on `main`'s tree as checked out (implementation lane A's two commits are not in it, `README.md` §6). No proposal is landed, so every "after B-nn" statement is a statement about a document's gate, not about behaviour (CLAUDE.md §0.2).

**The item form** (work order, "The item form"), in this order:

- `Item: <handle>` — handles are `IS-B3-FA-nn`, `-SE-nn`, `-WR-nn`, `-GO-nn`, `-X-nn` (crosses the four).
- **Advances** — the subsystem and the requirement rows of `engine/season/requirements.yaml`.
- **INSTRUCTION** — ordered edits at the single owner: file, symbol, schema, call sites.
- **WHERE** — the edit set (what the file census of U3 §5.1 gains).
- **FALSIFIER and control.**
- **GATE** — an execution artifact and its expected reading; never a document.
- **Hash movers.**
- **Depends on** — batch handles and item handles, each EXISTS-IN-TREE / PROPOSED / MISSING.
- **Lane · batch · cost class · tier · what lands it.**

**Marks.** `[ASSUMPTION: … — basis]` is a reading this lane took and a later lane may reverse. `[UNVERIFIED]` is a claim this lane did not open and does not rely on. `[BLOCKED: reason — owner]` is a missing part not decidable from the repository.

**Words.** `unified/U1_GLOSSARY.md` governs. "Scenario" is a world (a loader that builds a `World`), never a code path (`11_GO_fidelity_and_campaign_modes.md`: "a scenario is a world"). "Stub" below means the neighbour's declared interface answered by fixture data or by the neighbour's own registered module at a fixed input, never a second implementation.

## 1. The standalone-playable test, as this lane applies it

The work order's test has seven parts. Each subsystem section opens with a table of exactly these rows, each marked against the tree today (T) and against the suite's proposals as ordered (P):

| # | part | what counts as met |
|---|---|---|
| S1 | **entry** | one command or harness call that builds the scenario's world and runs it, with choices able to come from outside (a `--pick` or a decider) and from the chooser |
| S2 | **scenario** | a named world or generator seed that exercises this subsystem and no other more than its stub contract requires |
| S3 | **player-facing surface** | the readings the GO proposals name for it (what is offered, what is held, what happened, why) |
| S4 | **stub contract** | for each neighbour, the declared interface (composition row, query, effect) and what stands in for it |
| S5 | **stop conditions** | the ending kinds (win, lose, draw), each reachable, none a dead end (A-81) and a held position still moving the world (A-80) |
| S6 | **execution artifact** | a named test or a run with its expected reading, per ending and per stub |
| S7 | **integrated check** | the same subsystem inside the season loop through its registered seam (`04` §A.2, composition rows), with no change of code path |

A part is marked **met** only where a command this lane ran shows it, **carried** where a proposal with a gate carries it (the batch is named), **owed** where an item below carries it, and **blocked** with the reason and owner otherwise.

**GO is not a module.** `unified/U4_TRACEABILITY.md` §3 records it and the tree agrees (no `modules/go`, no composition row). For GO the test is read as: can a client that holds no engine state start a game, be offered choices, send one, be shown the result and its reason, reach an ending, save, and resume, through the one host the other three subsystems' scenarios run on. Its S7 is the port gate (B41).

**WR is three things.** The world's clocks (weather, harvest, wear, strife, eras) are "not a game and not meant to be one" (`audits/09_WR_audit.md` §9.1, as `U4_TRACEABILITY.md` §3 quotes it); threadwork is a registered-module candidate with a session; the story instruments are observers. The WR section applies the test to threadwork and to the era as a playable arc, and applies only S6 and S7 to the clocks.

