# Governance corpus — decomposition and rebuild (2026-09-03)

**Status: PROPOSAL.** Nothing here is ratified, no subsystem head moves, and no `CURRENT.md` row
changes. This is analysis and design, offered for review.

## Provenance — read this first

The subject of this work is a **33-document corpus uploaded to the session as a zip**
(`governance_play_redesign_v1.zip`, 810,408 bytes, ~115,000 words). The analysis was deliberately
scoped to those uploaded files **and nothing else**: no repository file was read as a source, and no
claim in these documents is grounded in the working tree.

That scoping was a standing instruction from Jordan during the session and it is load-bearing on how
these documents should be read: where they say "the corpus", they mean the upload, not `systems/`.
Several of the uploaded documents share filenames with files under `systems/` — they are **not**
verified to be identical, and no such comparison was performed after the scoping instruction was
given. **Do not assume a statement here describes the corresponding file on `main`.**

## Contents, in reading order

| file | what it is |
|---|---|
| `01-design-v1.md` | The first rebuild. 33 documents sorted into sets, flattened, decomposed, reconciled, and stated as one model: single ownership, pure derivation, one outcome type, one cross-scale carrier, a twelve-phase season. |
| `02-critique-and-precedents.md` | The critique of v1 along six axes — hierarchical shape, ownership, nesting, dependencies, state changes, emergence — plus a precedent analysis asking of each acclaimed game *what object exists there that does not exist here*. |
| `03-design-v2.md` | The rewrite. **Read this one if you read one.** Restores two dropped tiers, introduces titles and claims, splits acceptance by grain, and replaces "everything is capped" with a named instability budget. Its Part 0 states the organizing principles as tests; its Audit records the sixteen places the design failed one. |
| `annex-a-decomposition.md` | Full decomposition: 14 overlapping sets, 318 primitives, 293 derivatives, 129 pipelines, 18 throughlines, 79 indexed contradictions, 37 referee dependencies, 196 gaps. Formulas verbatim. |
| `annex-b-state-graphs.md` | The executable model: 12 sets of typed state with graph diagrams, single-writer primitives, expressions for derivatives, machine-evaluable pipeline predicates, the tick, and the code shape. **◆** marks each of 105 authored choices. |
| `annex-c-gaps-and-numbers.md` | 30 entries naming, per non-executable rule, the *specific missing decision*; plus 362 verbatim numeric constants and formulas. |

## Method

Two independent full readings of the corpus; a design synthesis; an adversarial fidelity pass that
overturned seven claims in v1 (all corrected in place, listed in that document's Verification
section); then for v2, a critique, a precedent study, an extraction of the design's own principles
into failable tests, a self-audit against them (7 findings), and an independent structural critique
(9 more, including three behavioural bugs the self-audit could not have found).

The most transferable result is in `03-design-v2.md` § Audit: **principles catch contradiction; only
tracing the mechanics catches error.** A design that is internally consistent and does the wrong thing
passes every test it can write about itself.

## What is NOT claimed

- No verification against `main`. See Provenance.
- No ED or PP identifiers are allocated; none were needed and none should be inferred.
- The numeric parameters proposed in v2 — regime entry conditions, scaling exponents, `Π_world` band
  edges — are **unvalidated**. v2 says so in its closing section and names campaign length as the
  question that must be settled before any of them can be tuned.
