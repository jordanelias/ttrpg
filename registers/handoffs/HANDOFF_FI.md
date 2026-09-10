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

- **ED-FI-0009 (open, `needs_jordan: true`, 2026-09-10) — THE SIX INVESTIGATION ACTS ARE ROWS, AND
  THE DEGREE IS THE RULING.** Jordan: *"'the six investigation acts' is not a verb"* and *"you must
  ensure you build the six from investigation systems"*. `engine/season/verb_table.yaml`'s single
  placeholder row is now `examine` · `interview` · `research` · `surveil` · `thread_read` ·
  `reconstruct`, each with a typed `requires` built from the existing closed grammar. Measured:
  verbs 32 -> 37, resolvable 12 -> 17, **executing in the corpus 6 -> 10**, distinct corpus
  behaviours 2 -> 16, §F1 clause-4 drops **25** (all `move`) -> 1,491 across six verbs, both sides
  measured by one script over the same 89 worlds (`move` itself falls, 25 -> 18). NPC-086 moved
  BLOCKED -> DEGRADED; NPC-010 lost one of three blockers.
  **What is NOT built and why:** nothing resolves a DEGREE for an investigation act, so their
  `emits:` is flat while `fieldwork_v30.md:302-309` grades all six on four bands.
  `engine/season/rosters.yaml:481` types investigation's seam UNRULED and `:487-491` rules that
  writing an IN/OUT for an unruled mode is inventing the architecture; `:505-508` forbids giving
  them a prize instead. The ruling request carries four questions that are one question — the seam,
  the pool (and whether `Person.capability` may gate, where `fieldwork_v30.md:76` and `#353 §9.2`
  contradict each other outright), the obstacle, and where Exposure lands given `04:237`.
  **Next actions once ruled:** the margin producer closes `H-98`'s second half and moves R-09;
  `examine` stays refused until some question source names a Site (`H-04`'s territory); the
  Dialogue Lattice replaces the `interview` row rather than sitting beside it (ED-FI-0004).


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
