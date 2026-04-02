---
name: valoria-editorial-register
description: >
  Manage the Valoria editorial decisions register. Use when asked to: review
  editorial decisions, resolve EDITORIAL flags, propagate approved decisions to
  GitHub, audit editorial debt, de-duplicate editorial items, or strike resolved
  items. Trigger on: "resolve editorials", "address editorial flags", "editorial
  register", "propagate decisions", "editorial review", "what editorials are
  pending", or any request to systematically process [EDITORIAL: ...] items.
  Also triggers at session close when editorial_decisions_pending is non-empty.
  This skill owns all editorial register work — never process editorials inline.
---

# VALORIA EDITORIAL REGISTER SKILL

## Purpose

Maintain `canon/editorial_ledger.yaml` as the single source of truth for all
editorial decisions in the project. Present unresolved items to the user
one-by-one, record decisions, propagate changes to GitHub, and keep the register
clean (deduplicated, consolidated, stale items struck).

**Model:** Sonnet 4.6.

---

## Ledger Schema

`canon/editorial_ledger.yaml` format:

```yaml
editorial_decisions:
  - id: ED-NNN
    date_flagged: YYYY-MM-DD
    date_resolved: YYYY-MM-DD   # null if unresolved
    source: "session | simulation | design-file | arc-generation"
    source_file: "path/to/file.md"   # where the flag originated
    description: "Short description of the decision required"
    full_flag_text: "[EDITORIAL: ...]"   # verbatim flag text
    status: "open | resolved | deferred | struck"
    decision: null   # populated on resolution
    propagation_targets: []   # files to update on approval
    propagation_status: "pending | complete | N/A"
    related_ids: []   # IDs of similar/duplicate items
    supersedes: []    # IDs this item replaces
    tags: []          # e.g. [faction, threadwork, debate, combat, npc, worldbuilding]
```

---

## Protocol

### Step 1 — Ingest

Read ALL of the following and extract every `[EDITORIAL: ...]` flag found:

1. `canon/editorial_ledger.yaml` — existing register (current state)
2. `session_log_current.md` → `editorial_decisions_pending` block
3. `valoria_gap_register_consolidated.md` → EDITORIAL-tagged rows only
4. `canon/patch_register.yaml` → any patch with `[EDITORIAL]` in description
5. Any output files passed as input by the calling skill (arc outputs, simulation
   findings, design proposals)

**Deduplication rule:** Before adding a new item, check `editorial_ledger.yaml`
for semantic equivalents. Two items are duplicates if they require the same
user decision on the same mechanic or content element, even if phrased
differently. When duplicates exist: keep the most complete description,
add `related_ids` cross-references, strike the lesser item.

**Consolidation rule:** Items that concern the same mechanic subsystem and
could be resolved by a single user decision must be grouped. Present them
together as a single prompt with sub-points. Assign one ED-NNN to the group;
sub-points are lettered (ED-042a, ED-042b, etc.).

**Strike rule:** An item is struck (status: struck) when:
- A higher-priority decision has rendered it irrelevant
- The mechanic it concerns was cut
- A subsequent canonical document answers it definitively
- The user explicitly dismisses it

Never delete struck items — set status: struck and populate `decision` with
the reason.

---

### Step 2 — Sort and Prioritise

Sort unresolved items:

| Priority | Criteria |
|----------|----------|
| P1-BLOCKER | Explicitly marked BLOCKER in session log or blocks compilation |
| P1 | Affects currently compiled stage; mechanical dependency |
| P2 | Design-adjacent; affects a stage not yet compiled |
| P3 | Flavour, naming, tone — no mechanical dependency |

Within each tier, sort by `date_flagged` ascending (oldest first).

---

### Step 3 — Present (One at a Time)

For each unresolved item, present to the user:

```
══════════════════════════════════════════════════
EDITORIAL DECISION [ED-NNN] — [STATUS TAG]
Source: [file] | Flagged: [date]
Tags: [tags]
──────────────────────────────────────────────────
[Full description of what needs deciding]

Context:
[1–3 sentences of relevant mechanical context from source file]

Propagation targets if approved:
[list of files that will be updated]

Related items: [ED-NNN, ...] (resolved together if applicable)
══════════════════════════════════════════════════
Decision? (approve / reject / defer / strike / rephrase):
```

**Wait for user response before presenting the next item.**

User response handling:

| Response | Action |
|----------|--------|
| `approve [text]` | Record decision, set status: resolved, queue propagation |
| `reject` | Record as resolved (rejected), no propagation |
| `defer` | Set status: deferred, move to end of queue |
| `strike` | Set status: struck with reason, remove from active queue |
| `rephrase [text]` | Update description, re-present |
| `group with ED-NNN` | Consolidate into named item, re-present as group |
| Any free text | Treat as the decision text for `approve` |

---

### Step 4 — Propagate

After each approval (or at user's instruction to batch-propagate):

1. **Read** the target file(s) from GitHub
2. **Identify** the exact location(s) requiring update:
   - Locate the `[EDITORIAL: ...]` flag text verbatim
   - Locate any stub or placeholder it guards
3. **Apply** the decision:
   - Replace the flag with the decided text
   - If the flag guards stub content, expand stub with the approved decision
   - If the flag is a warning only (no content to replace), remove the flag
     and append a design note: `*Decision [ED-NNN]: [summary]. Applied [date].*`
4. **Commit** to GitHub via PUT to the file's API endpoint
5. **Update** `canon/editorial_ledger.yaml`:
   - Set `propagation_status: complete`
   - Record `applied_commit` hash

**Commit message format:**
`[ED-NNN] [short description] — editorial decision applied`

**Multi-file propagation:** If the same decision affects multiple files,
apply all in a single session. List all committed files in the ledger entry.

---

### Step 5 — Register Maintenance

After processing a batch (end of session or when called explicitly):

1. **Re-check for supersession:** Any newly resolved items may render open
   items irrelevant. Run a pass and propose strikes with explanation.

2. **Consolidate:** Look for open items that share a tag cluster and could
   be resolved together. Propose grouping to the user before merging.

3. **Ledger commit:** Push updated `canon/editorial_ledger.yaml` to GitHub.
   Commit message: `[editorial-ledger] batch update — [N] resolved, [N] struck, [N] added`

4. **Session log update:** Remove resolved items from
   `session_log_current.md → editorial_decisions_pending`.

5. **Gap register sync:** For any ED item sourced from the gap register,
   update the gap register row (mark resolved or struck).

---

## ID Assignment

IDs are assigned sequentially: ED-001, ED-002, etc. Read the current highest
ID from `editorial_ledger.yaml` before assigning new ones.

Items from `session_log_current.md → editorial_decisions_pending` that use
BG-E-NNN notation retain their legacy IDs as aliases: record both
(`id: ED-NNN`, `legacy_id: BG-E-30`).

---

## Scope Constraints

**In scope (Claude decides format, user decides content):**
- Faction names, NPC names, character details
- Mechanical ambiguities requiring design intent confirmation
- Worldbuilding elements (locations, factions, tone)
- Proceeding types, asymmetric structures
- Named abilities, Unique Actions, thresholds

**Out of scope (Claude executes without this skill):**
- Formula corrections (go through patch_register)
- Formatting and structural repairs
- Simulation findings without editorial content

---

## Output

- Present decisions inline during review session
- Final register state: always `canon/editorial_ledger.yaml` on GitHub
- Summary report after batch: inline table (ID | Decision | Propagated To)
- If >10 items processed: produce `.md` summary file to outputs

---

## Error Conditions

| Condition | Handling |
|-----------|----------|
| Target file not found on GitHub | Flag `[PROPAGATION-BLOCKED: file not found]`, set propagation_status: pending, continue |
| Flag text not found verbatim in target file | Flag `[PROPAGATION-BLOCKED: flag text not located]`, present context to user |
| Conflicting decisions on same mechanic | Surface conflict, do not resolve — present both to user |
| Ledger missing (empty YAML) | Initialise with schema header, proceed with ingest |
