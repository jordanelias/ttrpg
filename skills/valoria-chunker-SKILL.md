# valoria-chunker

Pre-process Valoria documents into indexed chunks for analysis skills. Must run before canon-guard, mechanic-audit, or simulator receive >500 lines of input.

**Model:** Haiku 4.5. Structural extraction only.

## Term Reference

Read `references/glossary.md` for all term definitions and permitted abbreviations before using any game-specific term or abbreviation.

## Modes

**A — Section Map:** Extract headings with hierarchy → `valoria_section_map.md`
```
| Part | Section | Heading | Level | Lines | Est. Tokens |
```
Regenerate only on version change.

**B — Section Extraction:** Extract sections into chunk files → `chunk_[part]_[section_slug].md`
Target 200–500 lines/chunk. Split at sub-heading boundaries if >500. Header per chunk: `# Chunk: [Part].[Section] — [Title] | Source: [doc], Lines [N–M], Version: [label]`

**C — Mechanic Extraction:** Extract all formulas, tables, resolution procedures, tracks → `mechanics_index.md`
```
| ID | Mechanic | Location | Formula/Procedure | Input Variables | Output | Dependencies |
```
Number sequentially: M-001, M-002, ...

**D — Cross-Reference Map:** Extract inter-section references → `xref_map.md`
```
| Source Section | References Section | Type | Note |
```
Type: uses / modifies / conflicts / undefined

**E — Canon Constraint Extract:** Extract philosophical constraints from Foundations → `canon/canon_constraints.md`
```
| ID | Constraint | Foundations Ref | Mechanical Implication | Violation Test |
```
Run once per project. Update only when Foundations changes.

## Rules
- Chunk at heading boundaries — never mid-section
- No content judgment
- Report: sections found · chunk count · tokens/chunk
