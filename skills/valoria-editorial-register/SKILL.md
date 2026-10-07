---
name: valoria-editorial-register
description: >
  Manage the Valoria editorial decisions register. Use when asked to: review
  editorial decisions, resolve EDITORIAL flags, propagate approved decisions across
  the tree, audit editorial debt, de-duplicate editorial items, strike stale items,
  or add new flags from design files. Trigger on: "resolve editorials", "address
  editorial flags", "editorial register", "propagate decisions", "editorial review",
  "what editorials are pending", "dedup editorials", "consolidate editorials",
  "strike stale items", or any request to systematically process [EDITORIAL: ...]
  items. Also triggers at session close when editorial_decisions_pending is non-empty.
  This skill owns all editorial register work — never process editorials inline.
---

# VALORIA EDITORIAL REGISTER SKILL

## Input Validation (MANDATORY BEFORE ANY WORKFLOW)

Read from the working tree, never from memory:

- every ledger file (Store Format; `ls registers/editorial_ledger*.jsonl`);
- `references/id_reservations.yaml`;
- `references/glossary.md`, before using any game term or abbreviation;
- any design file a workflow touches, before reading or modifying it.

**A missing path:** report it and stop. Exception: `registers/editorial_ledger_<lane>.jsonl`
exists only after the lane's first ED — note that the lane has no entries and continue.

**Propagation targets** are the files in an entry's `source` field plus a corpus grep for the
term or mechanic. There is no target registry and no `references/file_index.md`.

## ED Number Collision Guard (MANDATORY — re-read before every ID assignment)

Immediately before assigning — an earlier read is stale:

1. Re-read `references/id_reservations.yaml`; take `lane_ids.lanes.<LANE>.next_free` (lane:
   ID Law).
2. That value is the ID: `ED-<LANE>-NNNN`, zero-padded (`next_free: 8` → `ED-MB-0008`).
3. Increment `next_free` by the count allocated, with a short comment on what the ID covers in
   the lane's existing comment style; co-commit with the ledger entry — one commit, never two.

There is no `# next_id:` header; allocation is only the per-lane `next_free` counters.

**On collision** (a concurrent PR merged the same number first): renumber the later-merging side
one step at a time and keep both entries.

### ID Law

Roster, format, flat freeze and lane-scoping: CLAUDE.md §4. Roster code owner:
`tools/ci_common.py`'s `LANE_CODES`.

- **`ED-<LANE>-NNNN`** — every new allocation.
- **`ED-NNN`** (flat) — frozen, last issued `ED-1096`. Never allocate one. Existing flat IDs may
  be cited, resolved, struck, or superseded by a new lane-tagged ID; they live in
  `registers/editorial_ledger.jsonl` or `registers/editorial_ledger_archive.jsonl`.

## PP Number Collision Guard (MANDATORY — re-read before every PP assignment)

`PP-NNN` is a separate counter in the same file, under the same protocol:

1. Re-read `references/id_reservations.yaml`. PP blocks are per round, not per lane: take the
   active round's `PP: { block, next_free }` under `reservations` (`contest_rebuild` has its own
   PP range).
2. That value is the ID: plain `PP-NNN` — no lane tag, no variant prefix (`PP-SIM-NNN` matches no
   counter and no `PP-\d+` scan).
3. Append to `registers/patch_register_active.yaml` (schema in its header: `id`, `date`,
   `severity`, `description`, `affects`, `status`).
4. Increment the round's `PP.next_free` by the count allocated; co-commit with the
   patch-register entry.

## Store Format (observed, not invented)

JSONL, one object per line — not YAML, no `editorial_decisions:` list. Append to add; edit only
the line you change; never rewrite a file.

| File | Holds | Rule |
|---|---|---|
| `registers/editorial_ledger.jsonl` | flat `ED-NNN` | no new entries; `status` may still change |
| `registers/editorial_ledger_archive.jsonl` | older terminal flat entries | same |
| `registers/editorial_ledger_<lane>.jsonl` | every new entry, one file per lane | append |
| `registers/editorial_ledger_<lane>_archive.jsonl` | per-lane overflow split by date; may hold `open`/`deferred` rows | search it too |

**Fields are observed practice, not a validated schema.** Legacy/archive files carry fields new
entries no longer use. Before writing, read the target lane's last few lines and match them.

| Field | Meaning |
|---|---|
| `id` | `ED-<LANE>-NNNN` (new) or `ED-NNN` (legacy) |
| `status` | free-text status word (Status values below) |
| `date` | date filed, `YYYY-MM-DD` |
| `resolution` / `date_resolved` | resolution date — some lanes only (every `ED-MB-*`); others (`ED-FI-0003`/`0004`) fold "RESOLVED YYYY-MM-DD ..." into `description`. Check the lane's recent entries |
| `description` | the substantive text: finding, ruling, execution, citations |
| `source` | path(s) to the design, audit or code file concerned |
| `confidence` | `high` / `medium` / `low` |
| `needs_jordan` | `true` if the item needs Jordan's ruling to close |
| `system` | free-text subsystem tag, e.g. `"field_investigation/threadwork"` |
| `citations` | array of `ED-*` ids this entry depends on or was ratified with |
| `severity` / `priority` | legacy urgency (Priority Definitions); new entries fold it into `description` |
| `stale_reason` / `superseded_by` | set when striking as duplicate or superseded |
| `tags` | free-text array (legacy/archive only) |

**Status values.** Terminal: `resolved`, `ratified`, `struck`, `deprecated`. Anything else
(`open`, `provisional`, `applied`, `confirmed`, `deferred`, …) is open work.

## Workflow A — Resolve Items

1. Filter every lane file and lane archive, plus the flat file for legacy items, to non-terminal
   `status`; `needs_jordan: true` and `P1-BLOCKER`/`P1` first.
2. Present one item at a time: `id`, `description`, `source`, `citations`.
3. Record the ruling by extending `description` — or in a `decision` field if the lane already
   uses one for similar entries.
4. Set `status: resolved` (`ratified` for an approved proposal). Add `resolution`/`date_resolved`
   only if the lane's recent entries do.
5. Find the propagation targets (Input Validation); read each and apply the ruling.
6. Atomic commit: lane ledger + every target edited (+ `id_reservations.yaml` if an ID was
   allocated, e.g. for a superseding entry).

## Workflow B — Add New Items

Trigger: a design file carries `[EDITORIAL: ...]` or `[PROVISIONAL: ...]` flags not yet in the
ledger.

1. Read the source file and extract every flag.
2. Skip any already registered: search every lane file and lane archive, then the flat/archive
   files, by description and source. A flag citing an existing ED id is registered.
3. Otherwise: pick the lane by subsystem, allocate per the ED Number Collision Guard, and append
   one line to `registers/editorial_ledger_<lane>.jsonl` (create it if absent).
4. Run Workflow D.
5. Atomic commit: lane ledger(s) + `id_reservations.yaml` + any design-file edit making the
   in-doc flag cite the new ID.

## Workflow C — Propagation Pass

Run after resolutions whose rulings have not yet reached other design files.

1. Filter to `resolved`/`ratified` entries whose `description` says execution is pending. Lane
   files have no `propagation_status` field; legacy/archive files do — check both.
2. For each: read the targets (Workflow A step 5), apply the ruling, and append
   "EXECUTED YYYY-MM-DD ..." to `description` — or update `propagation_status` where the entry
   uses it.
3. Atomic commit: targets + ledger file(s).

## Workflow D — Dedup, Consolidate, and Strike

**Run:** at session start, after reading the ledgers, and whenever items are added. Never delete
a line; touch only the line being changed.

### Step 1 — Deduplication
Duplicates: same or near-identical `description`; same `source` with overlapping subject; same
`system`/`tags` with overlapping decisions.

Keep the older ID or the more detailed item. On the other set `status: struck`,
`stale_reason: "Duplicate of ED-<LANE>-NNNN"` (or `ED-NNN`), `superseded_by: "ED-<LANE>-NNNN"`.

### Step 2 — Consolidation
Triggers: same system and mechanical area with decisions that cannot differ; items citing each
other via `citations`.

1. Primary: the most complete item, or a new one allocated per the Collision Guard if none is
   clean.
2. Fold the others' substance into the primary's `description`.
3. Mark the others `status: struck`, `stale_reason: "Consolidated into ED-<LANE>-NNNN"`.

### Step 3 — Stale Striking

| Condition | Mark |
|---|---|
| resolved by simulation or code verification | `status: resolved`, finding cited in `description` (e.g. `ED-MB-0007`) |
| feature cut | `struck`, `stale_reason: "Feature cut — ..."` |
| superseded by a later, conflicting item | `struck`, `stale_reason: "Superseded by ED-..."` |
| source document gone or deprecated | `struck`, `stale_reason: "Source document deprecated"` |
| superseded by a different canonical source entirely (legacy) | `deprecated`, with a `deprecation` note (e.g. `ED-107`) |

**Do not auto-strike:** low-priority items; resolved-but-unpropagated items (leave `resolved`,
pending state in `description` — Workflow C); blockers (`needs_jordan: true` or `P1-BLOCKER`),
whatever their age.

### Step 4 — Report

| Action | Count | IDs |
|--------|-------|-----|
| Deduped (struck as duplicate) | N | ED-..., ... |
| Consolidated | N | ED-... → ED-... |
| Struck (stale/cut) | N | ED-..., ... |
| Remaining open | N | — |
| Remaining `needs_jordan: true` | N | — |

## Workflow E — Harvest New Editorials from Session

After a session with design work:

1. Read every file the session modified and extract its `[EDITORIAL: ...]` /
   `[PROVISIONAL: ...]` flags.
2. Cross-reference the lane ledger(s) by description or ID.
3. Register the missing via Workflow B.
4. Run Workflow D.
5. Report: N added, N consolidated, N struck.

## Enforcement reality (what CI actually checks — read before assuming a rule)

Four separate checks; do not conflate them.

- **`tools/ci_editorial_checker.py`** (CI `editorial-check`) does not read the ledger. A commit
  touching its `EDITORIAL_PATHS` must carry `[EDITORIAL:`, `[PROVISIONAL:` or `[EDITORIAL GATE]`
  in the changed content (exempt: stubs under 200 chars, `_skeleton.md`); a deletion carries it in
  the commit message. Workflows B and E register those markers.
- **`tools/broken_dependency_checker.py::check_editorial_ledger`** (BLOCKING, CI
  `repository-integrity`) reads the flat ledger, every lane file and every lane `_archive`. For
  each entry whose `status` is in `LIVE_STATUSES` (`open`, `provisional`, `applied`, `confirmed`,
  `deferred`), it fails if a referenced path does not exist (old paths remapped through
  `references/restructure_ledger.md`). When a cited file moves or goes, update the path or close
  the entry.
- **`tools/ci_register_size_check.py`** — soft per-file token caps (table in the file). A warning
  is a split signal.
- **`tools/validate_ed_citations.py`** scans canon/design docs, not the ledgers, for `ED-`
  citations (not `PP-`); it fails when a citation claims authority (`canonical`, `ratified`,
  `applied`, `closes`, …) while the cited entry is `open`.

## Commit Convention

Scope `[editorial]`, citing every ED id touched — e.g.
`[editorial] Resolve ED-FI-0005 (Knot Pool formula) — ED-FI-0005`.

## Priority Definitions

| Priority | Definition |
|----------|-----------|
| provisional | A defensible design decision made to unblock work. Requires user review. Text marked `[PROVISIONAL]`. |
| P1-BLOCKER | Blocks compilation or playtest of a system. Nothing downstream can proceed without this. |
| P1 | Must resolve before next playtest. Produces broken or undefined outcomes if unresolved. |
| P2 | Should resolve before distribution. Produces inconsistency or unclear rules if unresolved. |
| P3 | Low urgency. Cosmetic or edge-case. |

Free text in `description` or legacy `priority`/`severity`, not an enum: match the lane's wording.
