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


## Bootstrap & Commit Protocol (MANDATORY)

Chunker writes files to GitHub. All writes go through hooks.

```python
import sys; sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap
g, h, files, token = quick_bootstrap(['references/canonical_sources.yaml'])
h.context_gate()
h.task_gate('design')

# Fetch target document
doc_files = g.read_files_graphql(['<path/to/document.md>'])
content = doc_files.get('<path/to/document.md>')
if not content:
    raise RuntimeError("Document not found — cannot chunk")

# ... perform chunking work ...

# Commit ALL chunk outputs atomically
oid = h.safe_commit(
    additions=[
        ('references/<chunk_output>.md', chunk_content),
        # add all chunk files here
    ],
    deletions=[],
    message='[infrastructure] chunk <document> — section map + extractions'
)
print(f"Chunks committed: {oid}")
```

**Rules:**
- Never write chunk files without going through `h.safe_commit()`
- Never use `g.atomic_commit()` directly
- All chunk output paths must be in `references/` or `tests/` — not root
- Commit all chunks for a document in one atomic commit

## Input Validation (MANDATORY)

The document to be chunked must be fetched from GitHub this session. Do not chunk a document from memory or a local copy.

```python
# Fetch target document from GitHub before chunking
files = g.read_files_graphql(['<path to document on GitHub>'])
content = files['<path to document on GitHub>']
if content is None:
    raise RuntimeError("Document not found on GitHub — cannot chunk")
```

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
