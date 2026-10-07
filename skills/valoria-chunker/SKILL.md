---
name: valoria-chunker
description: >
  Pre-process Valoria ruleset documents into indexed, token-efficient chunks for analysis skills.
  ALWAYS use this skill when a full Valoria document (>500 lines) is provided and needs to be
  analyzed by any analysis skill. Trigger on: full document provided to any Valoria skill,
  "chunk the ruleset", "prepare for analysis", "build section map", "extract mechanics",
  "build cross-reference map", or when any Valoria skill receives >500 lines of input.
  This skill MUST run before canon-guard or mechanic-audit receives input.
---

Structural extraction only — no content judgment.

## Commit Protocol (MANDATORY)

- Chunk outputs go under `references/` or `tests/`, never root.
- One atomic commit per document, e.g. `[infrastructure] chunk <document> — section map + extractions`.

## Input Validation (MANDATORY)

Read the target from the working tree; if the path does not exist, stop. Take its version label
(for file naming) from `references/canonical_sources.yaml`.

## Modes

### A — Section Map
All headings, with hierarchy → `valoria_section_map.md`:
`| Part | Section | Heading | Level | Lines | Est. Tokens |`. Regenerate only on version change.

### B — Section Extraction
Sections by heading or line range → one `chunk_[part]_[section_slug].md` each, 200–500 lines.
Over 500: split at sub-heading boundaries; still over 500: at the next sub-heading level.
Header per chunk:
```
# Chunk: [Part].[Section] — [Title]
Source: [repo-relative document path], Lines [N–M], Version: [label]
```

### C — Mechanic Extraction
All mechanical rules (formulas, tables, resolution procedures, tracks) → `mechanics_index.md`,
numbered M-001, M-002, …:
`| ID | Mechanic | Location | Formula/Procedure | Input Variables | Output | Dependencies |`

### D — Cross-Reference Map
All inter-section references (§ citations, "see above", implicit dependencies) → `xref_map.md`:
`| Source Section | References Section | Type | Note |`; Type = uses / modifies / conflicts / undefined.

### E — Canon Constraint Extract
The Foundations' philosophical constraints → `canon_constraints.md`:
`| ID | Constraint | Foundations Ref | Mechanical Implication | Violation Test |`. Run once per
project; update only when the Foundations version in `canonical_sources.yaml` changes.

## Rules
- Chunk at heading boundaries; never split mid-section.
- Report on completion: sections found · chunk count · estimated tokens/chunk.
