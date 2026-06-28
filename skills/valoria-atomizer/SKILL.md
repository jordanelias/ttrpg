---
name: valoria-atomizer
description: >
  Split a v30 Valoria design document into two files:
  (1) a index — mechanical specification only (tables, formulas, procedures, edge case rulings, cross-references);
  (2) a content infill — all prose, rationale, examples, design history, and explanatory text.
  Updates references/design_registry.yaml atomized field on completion.
  Trigger on: "atomize", "index", "infill", "split design doc", "extract index",
  "extract prose", "separate mechanics from prose", or when a design doc fails the
  Index Ruleset Principle (doc > 400 lines with explanatory content).
---

# VALORIA ATOMIZER SKILL

## Purpose

Apply the Index Ruleset Principle to every v30 design doc. After atomization:
- `{name}_v30.md` becomes the index (mechanical spec only — the source of truth for mechanical values)
- `{name}_v30_infill.md` is created (all extracted non-index content)
- `references/design_registry.yaml` is updated: `atomized: in_progress` (one file done) → `atomized: complete` (both done)

## What Goes in Index vs Infill

### Index — KEEP in `_v30.md`
- All tables (stat tables, formula tables, procedure tables, degree tables)
- All explicit formulas and mathematical expressions
- Numbered/bulleted procedure steps (the mechanical sequence itself)
- Edge case rulings — ONE sentence each. Format: `**Edge:** [condition] → [outcome].`
- Cross-references: `See {other_doc} §N.N`
- Section headers (retain for structure)
- One-line system summary at the top of each section (maximum 1 sentence)

### Infill — MOVE to `_v30_infill.md`
- Any prose paragraph > 1 sentence that explains *why* a mechanic works that way
- Design rationale ("This ensures that...", "The intent is...", "Because...")
- Historical context ("Prior to PP-NNN...", "Originally...", "In v24...")
- Worked examples (narrative walkthroughs)
- Flavor text, in-world framing
- Philosophical justification
- All content flagged `[INDEX-DEBT: ...]`

### Rule of thumb
> If it answers "what/how" → index. If it answers "why" → infill.

## Input Validation (MANDATORY)

Read the following files from the working tree (use the Read tool) before proceeding. The checkout is authoritative — do not fetch from GitHub and do not work from memory. If a listed file is absent from the working tree, stop and report it.

- `references/design_registry.yaml`  # find canonical_v30 path for the target system entry
- `<canonical_v30_path>`  # the design doc to atomize (resolved from the registry)

Then:
1. Identify the target system entry in the registry.
2. Confirm the `canonical_v30` path exists and `atomized == not_started`.
3. Read the design doc at that path.

**If `atomized: complete`:** skip — already done. Report and stop.
**If `atomized: in_progress`:** check which file is missing, complete it.
**If `canonical_v30: null`:** cannot atomize — source is unverified. Report blocker and stop.

## Workflow

### Step 1 — Section Inventory
Parse the design doc into sections (by `##` headers).
For each section, classify:
- `index-only` — all content is tables, formulas, or one-sentence rulings
- `infill-only` — all content is prose, rationale, or examples
- `mixed` — contains both

Output a classification table (do not skip this step):
```
| Section | Lines | Classification | Notes |
|---------|-------|----------------|-------|
| § N — Title | N–N | index-only | — |
| § N — Title | N–N | mixed | lines M–M are rationale |
```

### Step 2 — Extract Index
Build `{name}_v30_index.md` (or update `{name}_v30.md` in-place if replacing the canonical):

Header block:
```markdown
<!-- INDEX — mechanical spec only — generated {date} from {predecessor} -->
<!-- Infill: {name}_v30_infill.md -->
<!-- DO NOT add prose to this file. Edit {name}_v30_infill.md for rationale/examples. -->
```

Content rules:
- All tables → copied verbatim
- All formulas → copied verbatim
- Procedure steps → copied verbatim
- Edge case rulings → kept as one-liners; if multi-sentence, truncate to first sentence
- Section headers → kept
- One-sentence section summary → kept if it states a mechanical fact (e.g., "Pool = Agi + hist_pts + 3.")
- Everything else → replaced with `[→ infill §N.N]` cross-reference stub

### Step 3 — Extract Infill
Build `{name}_v30_infill.md`:

Header block:
```markdown
<!-- INFILL — prose, rationale, examples extracted from {canonical_v30_path} -->
<!-- Index: {name}_v30.md (or {name}_v30_index.md) -->
<!-- This file does not contain mechanical values. Reference the index for all values. -->
```

Content rules:
- Each extracted section prefixed with its original section header
- Add `[→ index §N.N]` backlink after each header
- Preserve all prose verbatim
- If the index has an edge case that was truncated, include the full text here

### Step 4 — Update Registry
Re-read `references/design_registry.yaml` from the working tree immediately before write (collision guard).
Update the target entry:
```yaml
  index: designs/{system}/{name}_v30_index.md  # or _v30.md if replacing in-place
  infill: designs/{system}/{name}_v30_infill.md
  atomized: complete
```

### Step 5 — Commit
Write all output files directly to their repo paths in the working tree, then `git commit`. Files in commit:
1. Index file (`{name}_v30_index.md` or updated `{name}_v30.md`)
2. Infill file (`{name}_v30_infill.md`) — NEW
3. `references/design_registry.yaml` — updated
4. Run freshness_gate if canonical changed: `python3 tools/freshness_gate.py --update`

Commit message: `[infrastructure] atomize {system}: index + infill extracted — {date}`

## In-Place vs Side-by-Side Atomization

Two strategies — choose based on doc size and disruption:

**In-place** (preferred for docs ≤ 300 lines after extraction):
- `{name}_v30.md` becomes the index (replace content)
- `{name}_v30_infill.md` is the new infill file
- canonical_sources.yaml does not change (path unchanged)

**Side-by-side** (for large docs where in-place would lose too much context):
- `{name}_v30.md` remains full doc (untouched)
- `{name}_v30_index.md` is the extracted index
- `{name}_v30_infill.md` is the extracted infill
- `design_registry.yaml`: set `index: {name}_v30_index.md`
- canonical_sources.yaml: if canonical is changing to index path, update it

**Decision rule:** If removing infill content reduces doc by > 40%, use side-by-side.

## INDEX-DEBT Handling

While atomizing, if a section is flagged `[INDEX-DEBT: ...]` anywhere in the doc:
1. Record in the infill file header: `## INDEX-DEBT ITEMS RESOLVED`
2. Extract all flagged content to infill
3. Remove flag from index

## Pre-Commit Checks

```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```

Exit 0 required. On non-zero: fix before committing.

## Post-Commit Verification

After the commit lands: re-read both output files from the working tree. Confirm:
- Index file contains NO prose paragraphs > 1 sentence
- Infill file contains NO mechanical formula tables
- `design_registry.yaml` shows `atomized: complete`

## Priority Order for Atomization

Work through in this order (highest mechanical value / most cross-referenced first):
1. `designs/threadwork/threadwork_v30.md` (856 lines — highest complexity)
2. `designs/scene/combat_v30.md`
3. `designs/provincial/strategic_layer_v30.md`
4. `designs/scene/fieldwork_v30.md`
5. `designs/provincial/mass_battle_v30.md`
6. `designs/scene/social_contest_v30.md`
7. `designs/architecture/scale_transitions_v30.md`
8. `designs/npcs/npc_behavior_v30.md`
9. `designs/provincial/clock_registry_v30.md`
10. All others from `references/design_registry.yaml`

## Collision Prevention

Before every commit, re-read all files being written from the working tree and compare to what you read at the start of the task. If changed underneath you: STOP, report collision. See valoria-orchestrator skill §Collision Prevention.
