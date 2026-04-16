---
name: valoria-editorial-register
description: >
  Manage the Valoria editorial decisions register. Use when asked to: review
  editorial decisions, resolve EDITORIAL flags, propagate approved decisions to
  GitHub, audit editorial debt, de-duplicate editorial items, strike stale items,
  or add new flags from design files. Trigger on: "resolve editorials", "address
  editorial flags", "editorial register", "propagate decisions", "editorial review",
  "what editorials are pending", "dedup editorials", "consolidate editorials",
  "strike stale items", or any request to systematically process [EDITORIAL: ...]
  items. Also triggers at session close when editorial_decisions_pending is non-empty.
  This skill owns all editorial register work — never process editorials inline.
---

**Prerequisite:** Bootstrap must be complete — `assert_bootstrap()` called by orchestrator or via `quick_bootstrap()` before invoking this skill.


# VALORIA EDITORIAL REGISTER SKILL

**Model:** Sonnet 4.6.

## Input Validation (MANDATORY BEFORE ANY WORKFLOW)

Fetch the following from GitHub before running any workflow. Do not use memory or local copies.

```python
required = [
    'canon/editorial_ledger.yaml',     # the register itself
    'references/file_index.md',        # for propagation target resolution
    'references/glossary.md',          # term definitions
]
files = g.read_files_graphql(required)
# Verify nothing returned None before proceeding
for path, content in files.items():
    if content is None:
        raise RuntimeError(f"GitHub fetch failed: {path} — cannot proceed")
```

**If any fetch fails:** STOP. Report the failure. Do not proceed using memory.

**Additional reads:** Any workflow that touches a specific design file must fetch that file from GitHub before reading or modifying it. Never work from memory of a design file's contents.

## ED Number Collision Guard (MANDATORY — re-read before every ID assignment)

The session-start fetch of `canon/editorial_ledger.yaml` is **not sufficient** for safe ID assignment.
Another session may have written new items since then. Always re-fetch immediately before assigning:

```python
# Re-fetch the ledger RIGHT NOW, not at session start
fresh_ledger_files = g.read_files_graphql(["canon/editorial_ledger.yaml"])
raw = fresh_ledger_files["canon/editorial_ledger.yaml"]
if raw is None:
    raise RuntimeError("Failed to re-fetch editorial ledger — cannot assign IDs safely")

import re
nid_match = re.search(r"# next_id:\s*(\d+)", raw)
if not nid_match:
    raise RuntimeError("next_id header missing from ledger — do not proceed")

next_id = int(nid_match.group(1))
# SAFETY: also scan for highest ED-NNN actually present in the file
all_ids = [int(m) for m in re.findall(r"ED-(\d+)", raw)]
highest_present = max(all_ids) if all_ids else 0
safe_next = max(next_id, highest_present + 1)

# Use safe_next for assignment. Increment per item.
print(f"Safe next ED ID: {safe_next}")
```

**Assign IDs starting from `safe_next`.** After committing, verify the committed file's `# next_id:` equals the batch-end + 1.

**Known state (2026-04-13):** `# next_id: 486` in header is stale. Items up to ED-489 exist. Safe next = **490**. The guard above will compute this correctly.


## Term Reference

Use `references/glossary.md` (fetched above) for all term definitions and permitted abbreviations before using any game-specific term or abbreviation.

## Purpose

Maintain `canon/editorial_ledger.yaml` as the single source of truth for all
editorial decisions. Present unresolved items to the user, record decisions,
propagate changes to GitHub, and keep the register clean.

---

## Ledger Schema

`canon/editorial_ledger.yaml` format:

```yaml
editorial_decisions:
  - id: ED-NNN
    date_flagged: YYYY-MM-DD HH:MM
    date_resolved: YYYY-MM-DD HH:MM   # null if unresolved
    source: "session | simulation | design-file | arc-generation"
    source_file: "path/to/file.md"
    description: "Short description of the decision required"
    full_flag_text: "[EDITORIAL: ...]"
    status: "open | resolved | provisional | deferred | struck"
    priority: "P1-BLOCKER | P1 | P2 | P3"
    decision: null
    propagation_targets: []
    propagation_status: "pending | complete | N/A"
    related_ids: []
    supersedes: []
    superseded_by: null
    stale_reason: null
    provisional_assumption: null
    tags: []
```

---

## Workflow A — Resolve Items

1. From fetched `canon/editorial_ledger.yaml`: filter `status: open`, sorted by priority (P1-BLOCKER first).
2. Present one item at a time: ID, description, flag text, source file, related IDs.
3. Record user's decision in `decision` field.
4. Set `status: resolved`, `date_resolved: today`.
5. Set `propagation_targets` based on fetched `references/file_index.md`.
6. Fetch each propagation target from GitHub, apply decision, commit.
7. Set `propagation_status: complete`.
8. Atomic commit: ledger + all target files.

---

## Workflow B — Add New Items

Triggered when a design file contains `[EDITORIAL: ...]` flags not yet in the ledger.

1. Fetch source file from GitHub.
2. Extract all `[EDITORIAL: ...]` instances.
3. For each: check if already registered (search fetched ledger by description similarity).
4. If not registered: assign next ED-NNN id, populate schema, append to ledger.
5. Run Workflow D (dedup) before committing.
6. Atomic commit: ledger only.

---

## Workflow C — Propagation Pass

Run after any batch of resolved items.

1. From fetched ledger: filter `status: resolved` AND `propagation_status: pending`.
2. For each: fetch target files from GitHub, apply decision text, mark `propagation_status: complete`.
3. Atomic commit: all modified files + ledger.

---

## Workflow D — Dedup, Consolidate, and Strike

**Run:** at session start (after fetching ledger) and whenever new items are added.

### Step 1 — Deduplication
Identify pairs of items that describe the same decision:
- Same description (exact or near-exact)
- Same source_file with same flag text
- Same tags AND same systems with overlapping decisions

For each duplicate pair:
- Keep the item with the lower ED number (or the one with more detail).
- Set the other's `status: struck`, `stale_reason: "Duplicate of ED-NNN"`, `superseded_by: ED-NNN`.
- Add the struck ID to the survivor's `supersedes` list.

**Do not silently delete.** Struck items remain in the ledger with their status.

### Step 2 — Consolidation
Identify items that should be merged because they represent the same underlying decision:

**Consolidation triggers:**
- Same system + same mechanical area + decisions that cannot differ
- Items explicitly marked `related_ids` pointing to each other

**Consolidation procedure:**
1. Create a new consolidated item (or designate the most complete existing item as primary).
2. Merge all `full_flag_text` fields into a consolidated description.
3. Union all `propagation_targets`.
4. Mark superseded items as `status: struck`, `stale_reason: "Consolidated into ED-NNN"`.


### Step 3 — Stale Striking
Mark items as `status: struck` with `stale_reason` when:

**Automatic strike criteria:**
- Decision was resolved via simulation — mark `status: resolved` with decision text citing the test finding.
- Feature the item refers to has been CUT — mark `struck`, `stale_reason: "Feature cut — [cut decision]"`.
- A later item supersedes this one and the earlier item's decision would conflict — mark `struck`, `stale_reason: "Superseded by ED-NNN"`.
- Item refers to a document that no longer exists or was deprecated — mark `struck`, `stale_reason: "Source document deprecated"`.

**Do not auto-strike:**
- Items that are merely low-priority (P3).
- Items where the answer is known but not yet propagated (use `resolved` + `propagation_status: pending`).
- Blockers, regardless of age.

### Step 4 — Report
After running dedup/consolidate/strike, output a table:

| Action | Count | IDs |
|--------|-------|-----|
| Deduped (struck as duplicate) | N | ED-NNN, ... |
| Consolidated | N | ED-NNN → ED-NNN |
| Struck (stale/cut) | N | ED-NNN, ... |
| Remaining open | N | — |
| Remaining P1-BLOCKER | N | — |

---

## Workflow E — Harvest New Editorials from Session

After any session where design work was done:

1. Fetch all files modified in the session from GitHub.
2. Extract all `[EDITORIAL: ...]` flags from fetched files.
3. Cross-reference against fetched ledger (by description match).
4. Add unregistered items to ledger.
5. Run Workflow D (dedup/consolidate/strike).
6. Report: N new items added, N consolidated, N struck.

**New items from session 2026-04-02 to add:**

| Description | Source File | Priority | Tags |
|-------------|-------------|----------|------|
| ST-BG-01: Overwhelming threshold (Ob+1 vs 2×Ob) | bg_v05_simulation_and_patches.md | P1 | board_game, dice |
| ST-BG-05: Theocracy Counter (TC) 80 seizure scope | bg_v05_simulation_and_patches.md | P1 | board_game, church |
| ST-INT-02: Commander bonus formula (three conflicting formulas) | bg_v05, mass_battle_v3 | P1 | mass_combat, hybrid, commander |
| ST-INT-07: Ceiral Ritual Rendering Stability gain vs Co-Movement scale | bg_v05, mass_battle_v3 | P2 | threadwork, hybrid, scaling |
| ST-INT-08: Muster output in BG context (Str=2 off token scale) | bg_v05, mass_battle_v3 | P2 | board_game, hybrid, muster |
| ST-INT-12: Altonian invasion unit stats BLOCKER | bg_v05, mass_battle_v3 | P1-BLOCKER | hybrid, mass_combat, altonia |
| ST-MB-01: Volley TN 6 vs universal TN 7 | mass_battle_v3.md | P1 | mass_combat, volley |
| ST-MB-02: Coherence undefined as mass battle stat | mass_battle_v3.md | P1 | mass_combat, threadwork, coherence |
| ST-INT-04: Military seasonal cap pooled vs separate | bg_v05, mass_battle_v3 | P2 | board_game, hybrid, military |
| P2-B11-13: Artillery Balanced disposition lock (intentional?) | stage8_combat.md | P3 | mass_combat, artillery |
| P2-B11-19: Thread Tension (TT) 80+ effect in mass battle | stage8_combat.md | P2 | mass_combat, threadwork |
| Debate: Can accused have corroborators in Church Tribunal? | debate_system_redesign_v1.md | P2 | debate, church |
| Debate: Obscuring as pure denial/Doubt Marker — confirm design intent | debate_system_redesign_v1.md | P1 | debate, orientation |
| Debate: Niflhel social mode (what can they do if excluded?) | debate_system_redesign_v1.md | P2 | debate, niflhel |
| Debate: Genre pivot mid-debate — permitted? penalised? | debate_system_redesign_v1.md | P2 | debate, genre |
| ST-TW-01: W-24 Object scale under-costed | threadwork_redesign_v25.md | P2 | threadwork, combat |

Consolidate new Niflhel debate item with ED-008.
Consolidate ST-INT-02 commander bonus with ED-018.
Consolidate P2-B11-02 Grand Debate role alternation with ED-013.

---

## Commit Convention

All editorial register commits use scope `[editorial]`:

```
[editorial] Harvest session items ED-031–046, consolidate ED-011→ED-027, strike ED-005 — 2026-04-02
[editorial] Resolve ED-027 (Poise/Focus) — ED-027
[editorial] Propagate ED-027 decision to stage2, stage8 — ED-027
```

---

## Priority Definitions

| Priority | Definition |
|----------|-----------|
| provisional | Claude made a defensible design decision to unblock simulation. Requires user review. Text marked [PROVISIONAL]. |
| P1-BLOCKER | Blocks compilation or playtest of a system. Nothing downstream can proceed without this. |
| P1 | Must resolve before next playtest. Produces broken or undefined outcomes if unresolved. |
| P2 | Should resolve before distribution. Produces inconsistency or unclear rules if unresolved. |
| P3 | Low urgency. Cosmetic or edge-case. |
