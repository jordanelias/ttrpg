# 08 · PROVENANCE — where every claim came from, and what the method could not see

## Status: reference. This document exists so that a later session can check this suite rather than
## trust it, and can see the shape of what it missed.

---

## §1 · THE METHOD

Jordan directed: trace every instance of code architecture across PRs #337–#344; sweep the repository
for the corresponding design and code; adjudicate; produce one authoritative suite.

**Three stages, structurally independent by construction.**

1. **Fourteen tracing and sweeping agents**, read-only, **none able to see any other's output.** Eight
   traced one pull request each; six swept one repository lane each.
2. **Five adjudicators**, each given the logs *and* pointed at the working tree, with instructions to
   verify rather than inherit — because a trace log is a secondary source.
3. **This suite**, written on the adjudications.

**Why the independence matters.** The head's own diagnosis of its process was that *every audit was
derivative-facing, and agreement between derivative documents read as corroboration when it was
correlated error with one root.* The counter-measure is not more review; it is **review pointed at a
different object.** Six of the fourteen lanes read code and registries rather than proposals, and
that is the only reason the central ruling in `04` §1 could be made at all.

**Where the relay worked, visibly.** An adjudicator overturned its own lane's sweep: the sweep
reported the fixed-point fix as absent, having grepped a range that stopped five lines short of where
it was adopted. A producer and a critic that share a reading share its errors; these did not.

---

## §2 · THE EVIDENCE BASE

All fourteen logs are committed at
`proposals/_session_provenance/2026-08-31-architecture-reconciliation/`.

| log | what it traced | scale |
|---|---|---|
| `pr_logs/PR337.md` | systems integration master + precedent companion | 255 architecture rows |
| `pr_logs/PR338.md` | the precedent matrix, slice decomposition, unified imports | 165 rows |
| `pr_logs/PR339.md` | the archived greenfield suite | 130 rows |
| `pr_logs/PR340.md` | greenfield v2 — the content quarry | 214 rows |
| `pr_logs/PR341.md` | the nine-throughline critique | 103 rows |
| `pr_logs/PR342.md` | Valoria from scratch | 195 rows |
| `pr_logs/PR343.md` | coverage, arcs, integration, the superseding document | 239 rows |
| `pr_logs/PR344.md` | the current head and its adversarial review | 317 rows |
| `repo_logs/R1_engine.md` | what executes | — |
| `repo_logs/R2_systems.md` | the design source of truth | — |
| `repo_logs/R3_godot.md` | the port, the contracts, the version | — |
| `repo_logs/R4_registries.md` | registries, vocabulary, ledgers | — |
| `repo_logs/R5_corpus_coverage.md` | the coverage re-measurement | — |
| `repo_logs/R6_execution.md` | tests, tools, CI, the board | — |

**~1,600 logged architecture items.** The adjudications are in the session scratch and their rulings
are reproduced, with grounds, in `06_ADJUDICATIONS.md`.

---

## §3 · FINDINGS BY INDEPENDENT REDISCOVERY

Per `CLAUDE.md` §10, a finding rediscovered by lanes that could not see each other is the strongest
signal available. **Ranked by how many independent lanes reached it:**

| finding | lanes |
|---|---|
| Nothing in the #337–#344 line executes; every core object is absent from the code | R1, R6, and the M1 board |
| **The running campaign resolves with zero people in it**, and the population guard is blind to a direct loader | PR337, PR338, R6 |
| ED-IN-0200 and ED-IN-0201 are open, unexecuted, and uncited by the design line | PR338, R4, R5 |
| The `Derived → Query` rename was forced by live registries with the opposite meaning | R1, R4 |
| The coverage confession is itself stale | R5, independently re-measured |
| `Faction.L` is written by code at ~31 sites and ratified as derived-with-no-setter | PR337, PR338 |
| Correct machinery exists with no caller — the closed Key-driven write loop that has never fired | PR337, PR338 |

---

## §4 · WHAT THIS METHOD COULD NOT SEE

Stated plainly, because a method's limits are part of its result.

1. **This suite has not read the other 103 uncited documents either.** Its "there is no X" claims carry
   the same scope limit as the head's. `05` §5 ranks what to read.
2. **Nothing was executed.** No campaign was run to test a claim; no Godot project was opened. Every
   claim about engine behaviour is marked `[engine]` and is published semantics, not measurement.
3. **The tracing agents are fallible in a specific, demonstrated way.** One fabricated a `PP-` citation
   that appears nowhere in the repository. It was caught by a blocking CI gate, corrected in `63192f0`,
   and **recorded rather than deleted** — it is a worked instance of the leaky-provenance hazard
   `CLAUDE.md` §7 names, and the value of keeping it is that the gate caught it.
4. **Two lanes produced opposite headlines from the same tree.** Both were competent and both cited
   code; the conflict was real and was ruled, not averaged. **A reader who takes either headline whole
   will be wrong.**
5. **The `valoria-game` implementation repository is not in this checkout.** Every claim about
   `project.godot`, the CI pin and the 84-error ratchet is quoted from this repo's records of runs
   made elsewhere. **Nobody has run Godot 4.6 against it, and this suite could not.**
6. **The adjudicators wrote no code.** They ruled on what should be built. The first honest test of any
   of it is step 1 of `07_EXECUTION_PATH.md`.

---

## §5 · HOW TO CHECK THIS SUITE

- **Every factual claim about the repository carries a path.** Read the path, not the claim.
- **Every ruling in `06` carries a falsifier.** Run it against the tree.
- **Where this suite and the code disagree, the code wins** (`CLAUDE.md` §0.05) — and the disagreement
  is a defect in one of them, resolved by deciding and then changing the code.
- **Where this suite and a `## Status:` line disagree, neither wins automatically.** Ask what executes.
