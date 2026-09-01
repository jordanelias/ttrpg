# Session provenance — 2026-09-01, the holonic architecture

## What this is

**The working material behind `proposals/2026-09-01-holonic-architecture/`.** It is **evidence, not
findings**: raw lane output, transcribed from the session, kept so that every retraction in
`ARCHITECTURE.md` §0.2 can be checked against the thing that forced it.

⚠ **A NOTE ON THE CONVENTION, STATED RATHER THAN GLOSSED.** `CLAUDE.md` §0's 2026-08-19 amendment
says an adversarial pass *"does not create a directory or a document."* **This directory exists
because Jordan asked for the session's working material to be committed**, and because the chain's own
practice differs — #343, #344, #345, #350 and #351 each landed `_session_provenance/`. The distinction
that makes this compatible rather than a violation: **these are raw lane transcripts, not a new prose
findings surface.** The findings went where the amendment says they should — into edits to the thing
under review, and into the commit messages.

## What ran, in order

| # | lane | model | tools | scope |
|---|---|---|---|---|
| 1 | **Context sweep** — PRs #337–#352 | Fable 5.1 | GitHub MCP + local reads | the whole chain: bodies, changed files, comments, commits |
| 2 | **Dropped-rulings census** | Fable 5.1 (same agent, resumed) | local reads | 27 items, each required to name the later section that lost it |
| 3 | **Lane A** — chain fidelity, factuality | Fable 5.1, `valoria-critic` | **Read/Grep/Glob only** | every quotation in the proposal, checked against source |
| 4 | **Lane B** — architecture: keys, wrappers, modularity, ownership, primitives | Fable 5.1, `valoria-critic` | **Read/Grep/Glob only** | the wrapper rule, the key system, C4's boundary, the descent |
| 5 | **Lane C** — logic, sequence, flexibility, emergence | Fable 5.1, `valoria-critic` | **Read/Grep/Glob only** | the step partition, termination, scripting drift, self-consistency |
| 6 | **Lane D** — adjudicate the dropped rulings for fold-in | Fable 5.1, `valoria-critic` | **Read/Grep/Glob only** | 27 verdicts + set-level conflicts, order, budget |

**Independence is structural, not declared.** Lanes A–D were dispatched as `valoria-critic`, whose
agent definition carries `tools: Read, Grep, Glob` — **no Write, no Edit, no Bash** — so a critic
*cannot* write whatever its prompt says. None of the four saw the author's reasoning; each received
the finished documents only.

**All four were instructed to withhold corrections until the end** and present them as one set with
(a) every correction, (b) which interact, (c) ranked by whether each changes conclusions / evidence /
wording, (d) what they would NOT correct and why. **That instruction was Jordan's**, and it is the
reason the retractions in §0.2 could be judged holistically rather than patched one at a time.

## The result, in one line

**Three lanes independently killed the first revision's central proposal** — the wrapper — and the
convergence is what makes it bankable rather than one reviewer's opinion.

| finding | A | B | C | D |
|---|---|---|---|---|
| the wrapper has nothing to check (`Event` has no target) | — | ✅ F3 | ✅ F7 | ✅ |
| its direction rule contradicts T6 / containerless venues | — | ✅ F1 | ✅ F8 | — |
| wrapper placed on the code tree, rule on the world tree | — | ✅ F2 | ✅ F11 | — |
| MATTER is not rung-local → "two of six" is wrong | ✅ F7 | ✅ F5 | ✅ F1 | — |
| the act budget is RULED in chain and was missed | ✅ F4 | — | — | — |
| L3 needs a third clause (ended edges) | — | ✅ F11 | ✅ F14 | — |
| the spine is not a tree at two edges | — | ✅ F8 | — | — |
| `phase:`'s N-line is false / it must be a set | — | ✅ F10 | ✅ F17-18 | — |
| the census miscounts itself (27, not 24) | ✅ F1 | — | — | ✅ |
| item 16 is a STRIKE | — | — | — | ✅ |

## What each lane got wrong, or could not settle

**Recorded because a lane's limits are part of its evidence.**

- **Lane A** could not check two PR-body claims — **the bodies are not on disk in this checkout** — and
  correctly reported them UNVERIFIED rather than false. The census now says so.
- **Lane B** left the ROLE↔SUBSYSTEM ordering **UNVERIFIED**: whether one role (`contest`) has three
  providers, or each deferred system is its own role, is not settled in the chain. `ARCHITECTURE.md`
  §41.2 states it as unresolved rather than picking.
- **Lane C** flagged the `(#340)` PR-number attribution as UNVERIFIED without git and **declined to
  guess** — *"a guess is worse than the possible error."*
- **Lane D** could not verify item 19's `U-1` attribution (#338's body not on disk) and said so.

## Files

| file | what it is |
|---|---|
| `01_SWEEP_337_352.md` | the chain sweep — the arc, the shape as of #350/#351, what #352 found |
| `02_CENSUS_BRIEF.md` | the brief the census ran under, and why its fourth field is the whole test |
| `03_LANE_A_fidelity.md` | quotations and scope, checked |
| `04_LANE_B_architecture.md` | the lane that killed the wrapper first |
| `05_LANE_C_logic.md` | the lane that found the self-contradiction |
| `06_LANE_D_foldin.md` | 27 verdicts, and the dependency order |

⚠ **These are transcriptions of lane output made during the session, not machine-captured logs.** They
are faithful to the findings and the corrections; they are not byte-exact transcripts, and nothing in
them should be cited as a measurement without re-running the check it names. **Every load-bearing
claim they carry was independently re-verified by hand before it changed the proposal** — those
verifications are named in `ARCHITECTURE.md` §0.2 and in `03_DROPPED_IN_CHAIN.md` §1.1.
