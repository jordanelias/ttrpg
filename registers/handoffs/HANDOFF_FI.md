# Handoff — FI (Field Investigation)

Lane-scoped continuity for the `FI` (field investigation) lane, per the `ED-<LANE>-NNNN`
namespace (`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md`
is the index; see it for cross-lane/global items.

No active work tracked in this lane as of the 2026-07-02 HANDOFF split. Canonical heads:
`designs/scene/fieldwork_v30.md` (+ co-files), `designs/scene/fieldwork_bg_v30.md`,
`designs/scene/investigation_systems_v30.md`.

## Pending

- **ED-FI-0004 (RESOLVED 2026-07-08) — pessimist-audit FI verdicts EXECUTED** (FI-lane follow-up to
  ED-IN-0027). **Interview MERGE:** the `fieldwork_v30 §4.2` bare-roll Interview object is annotated as
  superseded by the Dialogue Lattice (`investigation_systems_v30` S14 — its own Cross-System table already
  says the Interview routes through the Lattice "instead of single Charisma roll"); the Lattice is now the
  single canonical Interview home. Bare-roll row retained as baseline until **ED-921** (schedule/attribute
  reconciliation) + a `CURRENT.md` fieldwork row settle governance — this MERGE retires ED-921 + the fieldwork
  half of ED-IN-0016/EP-8 to one ruling. **Dialogue Lattice REFINE:** the five-filter Response-Matrix chain
  gets a build-gating requirement for a compact "why this NPC responded" readout (composed-system Q-elegant
  strain); the Lattice design + Certainty Gate are KEPT (ordinary finding, not a scope cut). `params/fieldwork.md`
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
