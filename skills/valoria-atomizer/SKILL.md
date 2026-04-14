---
name: valoria-atomizer
description: >
  Split a v30 Valoria design document into two files:
  (1) a skeleton — mechanical specification only (tables, formulas, procedures, edge case rulings, cross-references);
  (2) a content infill — all prose, rationale, examples, design history, and explanatory text.
  Updates references/design_registry.yaml atomized field on completion.
  Trigger on: "atomize", "skeleton", "infill", "split design doc", "extract skeleton",
  "extract prose", "separate mechanics from prose", or when a design doc fails the
  Skeleton Ruleset Principle (doc > 400 lines with explanatory content).
---

# VALORIA ATOMIZER SKILL

**Model:** Sonnet 4.6.

## Purpose

Apply the Skeleton Ruleset Principle to every v30 design doc. After atomization:
- `{name}_v30.md` becomes the skeleton (mechanical spec only — the source of truth for mechanical values)
- `{name}_v30_infill.md` is created (all extracted non-skeleton content)
- `references/design_registry.yaml` is updated: `atomized: in_progress` (one file done) → `atomized: complete` (both done)

## What Goes in Skeleton vs Infill

### Skeleton — KEEP in `_v30.md`
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
- All content flagged `[SKELETON-DEBT: ...]`

### Rule of thumb
> If it answers "what/how" → skeleton. If it answers "why" → infill.

## Input Validation (MANDATORY)

```python
import os, sys, re
os.environ["GITHUB_PAT"] = "<PAT>"
sys.path.insert(0, "/home/claude")
import github_ops as g

# 1. Fetch design_registry.yaml to find canonical_v30 path
registry_files = g.read_files_graphql(["references/design_registry.yaml"])
# 2. Identify the target system entry
# 3. Confirm canonical_v30 path exists; atomized == not_started
# 4. Fetch the design doc
target_files = g.read_files_graphql([canonical_v30_path])
```

**If `atomized: complete`:** skip — already done. Report and stop.
**If `atomized: in_progress`:** check which file is missing, complete it.
**If `canonical_v30: null`:** cannot atomize — source is unverified. Report blocker and stop.

## Fetch Log (emit before any work)

```
## FETCH LOG
session token: [from g.assert_fetched()]
references/design_registry.yaml: ✓ fetched ([N] lines)
[canonical_v30_path]: ✓ fetched ([N] lines)
```

## Workflow

### Step 1 — Section Inventory
Parse the fetched design doc into sections (by `##` headers).
For each section, classify:
- `skeleton-only` — all content is tables, formulas, or one-sentence rulings
- `infill-only` — all content is prose, rationale, or examples
- `mixed` — contains both

Output a classification table (do not skip this step):
```
| Section | Lines | Classification | Notes |
|---------|-------|----------------|-------|
| § N — Title | N–N | skeleton-only | — |
| § N — Title | N–N | mixed | lines M–M are rationale |
```

### Step 2 — Extract Skeleton
Build `{name}_v30_skeleton.md` (or update `{name}_v30.md` in-place if replacing the canonical):

Header block:
```markdown
<!-- SKELETON — mechanical spec only — generated {date} from {predecessor} -->
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
<!-- Skeleton: {name}_v30.md (or {name}_v30_skeleton.md) -->
<!-- This file does not contain mechanical values. Reference the skeleton for all values. -->
```

Content rules:
- Each extracted section prefixed with its original section header
- Add `[→ skeleton §N.N]` backlink after each header
- Preserve all prose verbatim
- If the skeleton has an edge case that was truncated, include the full text here

### Step 4 — Update Registry
Fetch `references/design_registry.yaml` immediately before write (collision guard).
Update the target entry:
```yaml
  skeleton: designs/{system}/{name}_v30_skeleton.md  # or _v30.md if replacing in-place
  infill: designs/{system}/{name}_v30_infill.md
  atomized: complete
```

### Step 5 — Atomic Commit
Files in commit:
1. Skeleton file (`{name}_v30_skeleton.md` or updated `{name}_v30.md`)
2. Infill file (`{name}_v30_infill.md`) — NEW
3. `references/design_registry.yaml` — updated
4. Run freshness_gate if canonical changed: `python3 tools/freshness_gate.py --update`

Commit message: `[infrastructure] atomize {system}: skeleton + infill extracted — {date}`

## In-Place vs Side-by-Side Atomization

Two strategies — choose based on doc size and disruption:

**In-place** (preferred for docs ≤ 300 lines after extraction):
- `{name}_v30.md` becomes the skeleton (replace content)
- `{name}_v30_infill.md` is the new infill file
- canonical_sources.yaml does not change (path unchanged)

**Side-by-side** (for large docs where in-place would lose too much context):
- `{name}_v30.md` remains full doc (untouched)
- `{name}_v30_skeleton.md` is the extracted skeleton
- `{name}_v30_infill.md` is the extracted infill
- `design_registry.yaml`: set `skeleton: {name}_v30_skeleton.md`
- canonical_sources.yaml: if canonical is changing to skeleton path, update it

**Decision rule:** If removing infill content reduces doc by > 40%, use side-by-side.

## SKELETON-DEBT Handling

While atomizing, if a section is flagged `[SKELETON-DEBT: ...]` anywhere in the doc:
1. Record in the infill file header: `## SKELETON-DEBT ITEMS RESOLVED`
2. Extract all flagged content to infill
3. Remove flag from skeleton

## Pre-Commit Checks

```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```

Exit 0 required. On non-zero: fix before committing.

## Post-Commit Verification

After `atomic_commit()` returns SHA: re-fetch both output files. Confirm:
- Skeleton file contains NO prose paragraphs > 1 sentence
- Infill file contains NO mechanical formula tables
- `design_registry.yaml` shows `atomized: complete`

## Priority Order for Atomization

Work through in this order (highest mechanical value / most cross-referenced first):
1. `designs/ttrpg/threadwork_v30.md` (856 lines — highest complexity)
2. `designs/combat/combat_v30.md`
3. `designs/board_game/board_game_v30.md`
4. `designs/fieldwork/fieldwork_v30.md`
5. `designs/mass_combat/mass_battle_v30.md`
6. `designs/contest/social_contest_v30.md`
7. `designs/hybrid/scale_transitions_v30.md`
8. `designs/systems/npc_behavior_v30.md`
9. `designs/systems/clock_registry_v30.md`
10. All others from `references/design_registry.yaml`

## Collision Prevention

Before every `atomic_commit()` call, re-fetch all files being written and compare SHA to session-start fetch. If changed: STOP, report collision. See valoria-orchestrator skill §Collision Prevention.
