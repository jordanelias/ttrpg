# Handoff — FI (Field Investigation)

Lane-scoped continuity for the `FI` (field investigation) lane, per the `ED-<LANE>-NNNN`
namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md`
is the index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical heads:
`systems/fieldwork/reference/fieldwork_v30.md` (+ co-files),
`systems/fieldwork/reference/fieldwork_bg_v30.md`,
`systems/fieldwork/reference/investigation_systems_v30.md`. (The `designs/` tree was dissolved; every
old path resolves through `references/restructure_ledger.md` via `tools/pathres.py`.)

## Pending

- **ED-FI-0009 (open, `needs_jordan: FALSE`, 2026-09-10) — THE SIX INVESTIGATION ACTS ARE ROWS, AND
  WHAT IS LEFT IS WORK ITEM 4.5, NOT A RULING.** Jordan: *"'the six investigation acts' is not a verb"* and *"you must
  ensure you build the six from investigation systems"*. `engine/season/verb_table.yaml`'s single
  placeholder row is now `examine` · `interview` · `research` · `surveil` · `thread_read` ·
  `reconstruct`, each with a typed `requires` built from the existing closed grammar. Measured:
  verbs 32 -> 37, resolvable 12 -> 17, **executing in the corpus 6 -> 10**, distinct corpus
  behaviours 2 -> 16 (of which the six alone carry 2 -> 10 and the new `alignment` cells 10 -> 16),
  §F1 clause-4 drops **25** (all `move`) -> **1,104 decision-affecting across five verbs** (1,491
  raw, less `restore`'s 387 — `restore` is not in `resolvable_verbs()`, so those cannot move a
  decision), both sides measured by one script over the same 89 worlds (`move` itself falls,
  25 -> 18). NPC-086 moved
  BLOCKED -> DEGRADED; NPC-010 lost one of three blockers.
  **What is NOT built:** nothing resolves a DEGREE for an investigation act, so their `emits:` is
  flat while `fieldwork_v30.md` §4.2 grades all six on four bands.
  ⚠ **I FILED THAT AS A JORDAN QUESTION AND WITHDREW IT THE SAME DAY.** All four parts are answered
  inside the tree, and an adversarial pass on the delivered work found the first two:
  - **the seam** — `workplans/2026-09-06-season-loop-execution-plan.md:647` ran this blank through
    §0's five tests four days earlier and closed it at test 3: *"NOT A SEAM. The loop IS the
    mechanism"*, attaching RESOLVE → WITNESS, out = *"Claims graded by degree; Failure emits
    `finding.none` and deposits nothing"*, **work item 4.5**. The six rows already ship that
    refusal half verbatim.
  - **the attribute gate** — my *"canon contradicts canon"* was an equivocation.
    `fieldwork_v30.md:76` is the *Perception gates* paragraph and governs DEPTH ACCESS (its
    examples are the Depth-1/Depth-2 gates at `:34-35`; Depth 0's gate is *None*). `#353 §9.2`
    forbids gating a VERB. Compatible.
  - **Exposure** — answered by precedent at `01_AXIOMS.md:1001-1002`: *"secrecy is the empty
    observer set."* Conspicuousness is the size of the observer set, which WITNESS already
    computes. `04:237` is not the blocker; it is why a per-territory meter was the wrong shape.
  **Next actions — work, not a ruling.** Item 4.5, the degree producer at RESOLVE → WITNESS. Its
  own blockers: no attribute values on any corpus person (`W27`'s cast), no Depth carrier, and
  §27.4's refusal to route an uncontested attempt to an `Ob = 0` roll. Then: `examine` stays
  refused until some question source names a Site (`H-04`); the Dialogue Lattice replaces the
  `interview` row rather than sitting beside it (ED-FI-0004).
- **Housekeeping, unowned:** `workplans/2026-09-09-r-execution-plan_part2.md` is ~30k tokens against
  `compliance_check`'s 15k cap — a pre-existing WARN that this session added ~1.2k to. §4's remedy
  is a `_part3` in reading order.


- **ED-FI-0004 (RESOLVED 2026-07-08) — pessimist-audit FI verdicts EXECUTED** (FI-lane follow-up to
  ED-IN-0027). **Interview MERGE:** the `fieldwork_v30 §4.2` bare-roll Interview object is annotated as
  superseded by the Dialogue Lattice (`investigation_systems_v30` S14 — its own Cross-System table already
  says the Interview routes through the Lattice "instead of single Charisma roll"); the Lattice is now the
  single canonical Interview home. Bare-roll row retained as baseline until **ED-921** (schedule/attribute
  reconciliation) + a `CURRENT.md` fieldwork row settle governance — this MERGE retires ED-921 + the fieldwork
  half of ED-IN-0016/EP-8 to one ruling. **Dialogue Lattice REFINE:** the five-filter Response-Matrix chain
  gets a build-gating requirement for a compact "why this NPC responded" readout (composed-system Q-elegant
  strain); the Lattice design + Truth Gate are KEPT (ordinary finding, not a scope cut). `params/fieldwork.md`
  carries a doc-side co-file note (no values changed). No sim edits (investigation.py/fieldwork.py are stubs).
  **Decision packet available** for the canonical-head governance question (which file's Status line
  binds, Option B full-port vs Option C split-head):
  `designs/audit/2026-07-08-pessimist-action-audit/decision_packets/DP-4_FI_interview_canonical_head.md`.

- **ED-FI-0002 (open) — counter-espionage loop.** Filed 2026-07-05 from the ratified
  edge-playability audit (PR #81, "Ratify all"; finding EP-6): enemy `da.covert_betrayal` reaches
  the player only as a non-interactive cut scene when `exposed==true`; antinomian/economic covert
  action produces no signal at all; no detection/response verb exists. Design the loop with
  fieldwork as host (Exposure is the symmetric mechanic): investigable trail, exposure-flip path,
  response surface. The one ratified §7 item that is new design, not wiring. Composes with
  ED-FI-0001 (investigation-lane audit) and the audit's EP-8 (investigation_systems_v30
  canonical-in-name-only; head conflict settles via ED-IN-0016's CURRENT.md row). See the audit
  report §1 EP-6/EP-8 / §7 item 7.

## Decisions

(none logged under this lane split.)

## Next actions

- **ED-914 residual (from `registers/handoffs/HANDOFF_IN.md`'s LA-23 ledger-status reconciliation):**
  left `open`; mechanical parts remain — PP-719 record-or-strike; dead `fieldwork_design_v1`
  parent-path refs in `params/bg/core.md`, `designs/scene/fieldwork_v30.md`,
  `designs/scene/fieldwork_godot.md`.
