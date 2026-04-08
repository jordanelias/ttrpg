---
name: valoria-chunker
description: >
  Pre-process Valoria ruleset documents into indexed, token-efficient chunks for analysis skills.
  ALWAYS use this skill when a full Valoria document (>500 lines) is provided and needs to be
  analyzed by any analysis skill. Trigger on: full document provided to any Valoria skill,
  "chunk the ruleset", "prepare for analysis", "build section map", "extract mechanics",
  "build cross-reference map", or when any Valoria skill receives >500 lines of input.
  This skill MUST run before canon-guard, mechanic-audit, or simulator receive input.
---

**Model:** Haiku 4.5. Structural extraction only — no content judgment.

## Input Validation (MANDATORY)

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

The document to be chunked must be fetched from GitHub this session. Do not chunk a document from memory or a local copy.

```python
# Fetch target document from GitHub before chunking
files = g.read_files_graphql(['<path to document on GitHub>'])
content = files['<path to document on GitHub>']
if content is None:
    raise RuntimeError("Document not found on GitHub — cannot chunk")
```

**Fetch log (emit before any analysis):**
```
## FETCH LOG
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, stop — the analysis is invalid.

**Requires:** Document version label for file naming (read from `references/canonical_sources.yaml`).

## Modes

### A — Section Map
Extract all headings with hierarchy.
**Output:** `valoria_section_map.md`
**Format:**
```
| Part | Section | Heading | Level | Lines | Est. Tokens |
```
Regenerate only on version change. Reuse across sessions.

### B — Section Extraction
Extract sections by heading or line range into individual chunk files.
**Output:** `chunk_[part]_[section_slug].md` per section
**Target:** 200–500 lines/chunk. Split at sub-heading boundaries if >500 lines.
**Header per chunk:**
```
# Chunk: [Part].[Section] — [Title]
Source: [document path on GitHub], Lines [N–M], Version: [label]
```

### C — Mechanic Extraction
Extract all mechanical rules: formulas, tables, resolution procedures, tracks.
**Output:** `mechanics_index.md`
**Format:**
```
| ID | Mechanic | Location | Formula/Procedure | Input Variables | Output | Dependencies |
```
Number each mechanic sequentially (M-001, M-002, ...).

### D — Cross-Reference Map
Extract all inter-section references (§ citations, "see above", implicit dependencies).
**Output:** `xref_map.md`
**Format:**
```
| Source Section | References Section | Type | Note |
```
Type = uses / modifies / conflicts / undefined

### E — Canon Constraint Extract
Extract philosophical constraints from Foundations into structured checklist.
**Output:** `canon_constraints.md`
**Format:**
```
| ID | Constraint | Foundations Ref | Mechanical Implication | Violation Test |
```
Run once per project. Update only when Foundations changes (check `canonical_sources.yaml` version).

## Rules
- Chunk boundaries at heading level — never split mid-section
- No content judgment — extraction and indexing only
- Report after completion: sections found · chunk count · estimated tokens/chunk
- If a chunk exceeds 500 lines after heading-level split, split at next sub-heading level
- Source path in every chunk header must be the GitHub path, not a local path
