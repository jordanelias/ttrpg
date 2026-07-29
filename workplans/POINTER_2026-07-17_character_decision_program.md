# Pointer — Character-decision remediation program (IN lane)

**target:** `audit/2026-07-17-character-decision-adversarial-audit/03_remediation_program.md`
**lane:** IN · **ED:** ED-IN-0073
**liveness:** LIVE — `## Status: PROPOSED — Jordan-gated`; Phase-0 docket D1 ruled, D2–D4 awaiting
**scope:** The program wrapper. **Phase 1 relocates `systems/characters/` →
`systems/character/{generation,conviction,beliefs}/`**, repoints 5 `descriptor_registry` entries and
`module_contracts`' `piety_track` `doc:`, and updates CURRENT.md / CLAUDE.md §3 / HANDOFF_IN.

> ⚠️ **Sequencing hazard.** A lane-ownership table cannot be authored against paths that are about to
> move. The centralization program (ED-IN-0103) must either wait on this Phase 1 or exclude
> `systems/characters/**` with a stated reason. See its §0.1 interlock 4.
