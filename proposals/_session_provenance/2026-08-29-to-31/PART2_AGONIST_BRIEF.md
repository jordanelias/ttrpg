# Part 2 — agonist brief (shared by both lanes)

## What Part 2 is

Jordan's instruction, verbatim:

> "Second, critically interpret your findings and propose how to integrate the following
> into the PR#342 design code proposals for (a) NPC matrix seasons and (b) arcs."

So the deliverable is **an integration proposal against PR #342's design code proposals**.
Not a review. Not a summary of findings. A proposal that says: *here is what changes in
the #342 suite, here is the exact shape of the change, here is why it is warranted, here
is what it costs.*

## Binding inputs (read these, in this order)

1. `proposals/2026-08-31-integration/03_corrected_findings.md` — **BINDING.** §A lists 12
   struck claims. **Any proposal built on a struck claim is void.** §B lists 7 survivors.
   §C lists 7 proposal-changing corrections (C-1..C-7) — these are the spine of your work.
   §D lists 4 standing methodological constraints you must respect in every claim you make.
2. `proposals/_session_provenance/2026-08-29-to-31/CODESHAPE_FORBIDDEN.md` — PR #342's
   §7 forbidden list and R-1/R-2 module rules, verbatim. **A proposal that violates one of
   these is dead on arrival**; if you believe a forbidden item must be relaxed, that is an
   *amendment request* and must be argued as one, separately and explicitly.
3. `proposals/2026-08-31-integration/00b_pessimistic_ners.md` — P-1..P-5. Every change you
   propose gets an N/E/R/S line under these rules. E is a RATIO against N and R, never a
   fourth averaged axis. R is structural: a dominant option at a seat a player occupies is
   a design failure, not a balance note.
4. `proposals/2026-08-29-valoria-from-scratch/11_code_shape.md` — the compliance target.
   §2 signatures, §3 ownership table, §7 forbidden list, §8 four structural tests.
5. Your lane's own review and source suite (named in your lane prompt).

## Hard rules for what you write

- **Cite by object, not by adjective.** Every claim names the file, the section, and where
  possible the line. "The design already handles this" is not a claim; it is a mood.
- **Every proposed change carries: (i) the exact #342 document and section it edits, (ii)
  the text or type change, (iii) the N/E/R/S line, (iv) what it costs, (v) the falsifier —
  what observation would show the change was wrong.**
- **Prefer the smallest change that closes the defect.** #342's §3 ownership table is
  deliberately narrow ("a container holds its stake, its judging set, its standing dates.
  Nothing else"). Adding a field to a container is expensive; adding a *place-scoped object*
  or a *derived read* is cheap. Argue the cost.
- **Do not propose a validator, a guard, a register, or a process document.** This is a game
  design exercise from scratch. If you find yourself proposing apparatus, you have drifted.
- **Do not remediate existing repo code.** #342 is a from-scratch proposal suite; existing
  `engine/`/`systems/` code is reference only, never ruling.
- **Separate what is SETTLED from what is a LIVE CHOICE.** Where two defensible shapes exist
  and they lead to materially different games, say so and present both with a recommendation
  — do not silently pick.
- **If a finding does not warrant a change, say so and close it.** A finding that survives
  review and still needs no integration is a legitimate outcome. Say which and why.

## Output format

A single markdown document. Sections:

- `## 0. What I am integrating` — the surviving findings this proposal acts on, by ID.
- `## 1. Findings that need NO change` — with the reason each closes.
- `## 2. The changes` — one subsection per change, numbered `I-N` (lane a) or `I-A-N`
  (lane b, arcs). Each carries the five items above.
- `## 3. Amendment requests` — anything that touches #342's forbidden list or ownership
  table, argued explicitly as an amendment with the cost of NOT making it.
- `## 4. Live choices` — where you refused to pick, with both options and a recommendation.
- `## 5. What this proposal does not do` — the honest boundary.

Length: as long as the material warrants, no longer. Prose, not bullet-soup.

## What happens next (so you write for it)

Your OUTPUT ONLY — not your reasoning, not this brief — goes to a cold adversarial critic
with read-only tools, which will try to break it against the working tree. Write so that a
reader with no memory of this session can check every claim you make. Unverifiable claims
will be struck, and a struck claim voids the change built on it.
