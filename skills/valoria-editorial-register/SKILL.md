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

# VALORIA EDITORIAL REGISTER SKILL

## Input Validation (MANDATORY BEFORE ANY WORKFLOW)

Read the following from the working tree before running any workflow. Do not use memory.

- `registers/editorial_ledger.jsonl` — the frozen flat-ID legacy store (read-only for new
  entries; still live for resolving/striking/citing pre-cutover `ED-NNN` items).
- Every `registers/editorial_ledger_<lane>.jsonl` that exists (`ls registers/editorial_ledger_*.jsonl`
  — currently `_mb`, `_pc`, `_fi`, `_sc`, `_fa`, `_wr`, `_se`, `_in`, plus the overflow
  `_archive`; a lane file only exists once that lane has allocated its first ED, so `_go`
  may be absent — that is expected, not an error).
- `references/id_reservations.yaml` — the ID allocation source of truth (§ below).
- `references/glossary.md` — term definitions.

**If any path is missing:** STOP for that path — except a missing `registers/editorial_ledger_<lane>.jsonl`
lane file, which is expected for a lane that has never allocated (do not treat as a failure;
just note the lane has no entries yet). For any other missing path, report the failure and do
not proceed using memory.

**Note:** there is no `references/file_index.md` — it does not exist in this repo. Do not cite
it. Propagation targets are discovered by reading the design doc(s) named in an entry's
`source` field and by grepping the corpus for the term/mechanic under discussion (see
`ED-WR-0001`'s explicit precedent: "derive sweep targets by grep, not by [a hand-maintained]
list").

**Additional reads:** Any workflow that touches a specific design file must read that file from the working tree before reading or modifying it. Never work from memory of a design file's contents.

## ED Number Collision Guard (MANDATORY — re-read before every ID assignment)

An earlier read of `references/id_reservations.yaml` is **not sufficient** for safe ID
assignment. Another session may have written new items since then. Always re-read it from
the working tree immediately before assigning:

1. Re-read `references/id_reservations.yaml` from the working tree right now, not at session
   start. Find `lane_ids.lanes.<LANE>.next_free` for the lane your work belongs to (see "ID
   Law" below for the lane roster).
2. That value IS the next ID to assign — form the entry as `ED-<LANE>-NNNN` (4-digit
   zero-padded, e.g. `next_free: 8` → `ED-MB-0008`).
3. After assigning, increment `next_free` by the count of IDs you allocated and co-commit
   `references/id_reservations.yaml` (a one-line change to the lane's `next_free` value, plus
   a short comment recording what the new ID covers — follow the existing comment style
   already present for that lane) in the **same commit** as the ledger entry/entries.

**There is no `# next_id:` header anywhere in this system — that mechanism does not exist.**
Do not look for one. Allocation is exclusively via `id_reservations.yaml`'s per-lane
`next_free` counters, described there as the "ALLOCATION PROTOCOL": read `next_free` → form
the entry with that ID → increment `next_free` → co-commit both files in the same commit.

**Worked examples (this repo's own history, follow this shape):** the audit-ecosystem
consolidation batch that produced this rewrite allocated `ED-IN-0032`, `ED-IN-0033`, and
`ED-IN-0034` in sequence, each by reading `lane_ids.lanes.IN.next_free`, forming the ledger
entry with that ID in `registers/editorial_ledger_in.jsonl`, bumping `next_free` in
`id_reservations.yaml`, and committing both files together (or, for a doc-only phase, filing
the ledger entry as a small follow-up commit — either is fine, the protocol doesn't require a
single atomic commit, just that the ledger entry and the `next_free` bump land together).

**The same batch is also a worked example of the collision guard's whole point.** These three
entries were originally allocated as `ED-IN-0031`/`0032`/`0033` — but a concurrent PR on `main`
independently read the same `next_free=31` and also claimed `ED-IN-0031` (for unrelated work),
merging first. Reconciling onto that PR meant renumbering all three of this batch's entries up
by one (see `id_reservations.yaml`'s IN-lane comment for the full incident). This is exactly
what the Collision Guard above is for: `next_free` is a live counter another session can move at
any time, and "renumber the later-merging side, one step at a time, keep both entries" is the
correct response — not a special case, the normal one.

**Two ID formats coexist (do not confuse them):**
- **`ED-<LANE>-NNNN`** (lane-tagged, 4-digit zero-padded) — the format for **all new
  allocations**, since 2026-07-02 (`ED-IN-0001`, the cutover entry). Lanes: `MB` mass battle,
  `PC` personal combat, `FI` field investigation, `SC` social contest, `FA` faction actions,
  `WR` world, `IN` infrastructure/cross-cutting, `GO` godot, `SE` settlements. A session should
  scope its own commits to the one lane whose `ED-<LANE>` ids it is allocating (CLAUDE.md §3),
  except genuinely cross-cutting `IN` work.
- **`ED-NNN`** (flat, no lane tag) — the **frozen legacy sequence**, stopped permanently at
  `ED-1096` (two more flat IDs landed the same 2026-07-02 cutover day before the sequence fully
  stopped — `ED-1094` is the ruling that established the freeze, not the last ID actually issued
  under it). No new flat IDs are ever allocated. Existing flat IDs remain permanently valid to
  cite, resolve, strike, or supersede (via a NEW lane-tagged ID) — they live in
  `registers/editorial_ledger.jsonl` (active) or `registers/editorial_ledger_archive.jsonl` (older,
  size-overflow-driven split of settled entries — see that file's own header/the ledger's
  `_split_from` fields for provenance).

## PP Number Collision Guard (MANDATORY — re-read before every PP assignment)

`PP-NNN` mechanical patches use the exact same `id_reservations.yaml` allocation discipline as
`ED-<LANE>-NNNN` above — read `next_free`, form the entry, bump, co-commit. They are a separate
counter (patches, not editorial decisions) but share the file and the protocol:

1. Re-read `references/id_reservations.yaml` from the working tree right now. PP blocks are
   per-round, not per-lane (unlike ED): find the active round's `PP: { block, next_free }` (as
   of this writing, round D's `next_free: 810`, with the `contest_rebuild` sub-block's own PP
   range separately tracked — check `reservations` for the current live block, not a cached
   value).
2. That `next_free` value IS the next PP to assign — form the entry as `PP-NNN` (no lane tag;
   `PP-NNN` predates the ED lane split and was never split the same way).
3. Append the entry to `registers/patch_register_active.yaml` (see that file's own header for its
   schema — `id`, `date`, `severity`, `description`, `affects`, `status`).
4. Increment the round's `PP.next_free` by the count allocated and co-commit
   `references/id_reservations.yaml` in the **same commit** as the patch-register entry.

Do not invent a variant format (e.g. a skill-specific `PP-SIM-NNN` prefix) — `canon/
patch_register_active.yaml` uses plain `PP-NNN` throughout; a non-conforming prefix will not
match `references/id_reservations.yaml`'s counters or any tooling that scans for `PP-\d+`.

## Term Reference

Use `references/glossary.md` (read above) for all term definitions and permitted abbreviations before using any game-specific term or abbreviation.

## Purpose

Maintain the editorial register — `registers/editorial_ledger.jsonl` (frozen legacy) plus the
lane-split `registers/editorial_ledger_<lane>.jsonl` files (live, where all new work is filed) —
as the source of truth for editorial decisions. Present unresolved items to the user, record
decisions, propagate changes across the working tree and commit, and keep the register clean.

---

## Store Format (observed, not invented)

**Format:** JSONL — one JSON object per line, NOT a single YAML file, NOT a
`editorial_decisions:` top-level list. Append a new line to add an entry; never rewrite the
whole file wholesale (git-diffability is the entire point of this format — see
`registers/editorial_ledger_migration_2026-05-28.md` for why it replaced the old fragmented-YAML
scheme).

**Files:**
- `registers/editorial_ledger.jsonl` — flat, pre-cutover `ED-NNN` entries. Read-only for new
  entries; existing entries may still transition `status` (e.g. `open` → `resolved`/`struck`).
- `registers/editorial_ledger_archive.jsonl` — an overflow split of the flat file's own older,
  terminal-status entries (token-cap driven, mirrors `patch_register_active`/`_archive`). Same
  rules as the flat file.
- `registers/editorial_ledger_<lane>.jsonl` (`mb`, `pc`, `fi`, `sc`, `fa`, `wr`, `se`, `in`, and
  `go` once GO allocates) — where every NEW entry is filed, one file per lane.

**Field vocabulary — observed-descriptive, not an enforced schema.** This is a practiced
convention, not a rigid schema: not every entry uses every field, and the legacy/archive
files in particular carry many one-off or migration-era fields no longer used by new entries.
Fields actually seen in live lane files (the pattern to follow for new entries):

| Field | Meaning |
|---|---|
| `id` | `ED-<LANE>-NNNN` (new) or `ED-NNN` (legacy) |
| `status` | free-text status word: `open`, `resolved`, `ratified`, `struck`, `deprecated`, etc. (see "Status values" below) |
| `date` | date the item was filed/flagged, `YYYY-MM-DD` |
| `resolution` / `date_resolved` | date the item was resolved — used by some lanes (e.g. every `ED-MB-*` entry) but not others (e.g. `ED-FI-0003`/`0004` resolve with neither field, folding the date into `description` prose instead); check the target lane's recent entries rather than assuming |
| `description` | the substantive text — often long, includes what was found, what was ruled, what was executed, and citations to the audit/PR that produced it, all in prose |
| `source` | path(s) to the design doc / audit doc / code file the item concerns |
| `confidence` | `high` / `medium` / `low` — how confident the filer is in the finding |
| `needs_jordan` | boolean — true if the item requires Jordan's explicit ruling before it can close |
| `system` | free-text subsystem tag, e.g. `"field_investigation/threadwork"` |
| `citations` | array of other `ED-*` ids this entry depends on or was ratified alongside |
| `severity` / `priority` | legacy-file fields for urgency (`P1-BLOCKER`, `P1`, `P2`, `P3` — see Priority Definitions below); rare in new lane entries, which usually fold urgency into `description` prose instead |
| `stale_reason` / `superseded_by` | used when striking an entry as a duplicate/superseded |
| `tags` | array of free-text tags (legacy/archive files only in practice) |

Do not treat this table as a contract to enforce on every new entry — match the style of
recent entries in the target lane file (read the last few lines of that lane's `.jsonl`
before writing a new one) over any fixed field list.

**Status values observed in practice:** `open`, `resolved`, `ratified`, `struck`, `deprecated`.
`provisional`, `applied`, `confirmed`, `deferred` also appear and are treated as "live" (not yet
settled) by CI tooling (see "Enforcement reality" below) — treat any status other than
`resolved`/`struck`/`ratified`/`deprecated` as still-open work.

---

## Workflow A — Resolve Items

1. From every `registers/editorial_ledger_<lane>.jsonl` that exists, plus
   `registers/editorial_ledger.jsonl` for any still-open legacy items (read each from the working
   tree): filter to non-terminal `status` values (`open`, `provisional`, `deferred`, etc. — not
   `resolved`/`struck`/`ratified`/`deprecated`), sorted with `needs_jordan: true` and any
   `P1-BLOCKER`/`P1` items first.
2. Present one item at a time: `id`, `description`, `source`, and any `citations`/related IDs.
3. Record the user's decision. Append the decision text to `description` (most entries fold
   the ruling into an updated/extended `description` string rather than a separate `decision`
   field — follow that pattern for lane files) or set a `decision` field if the target lane
   file already uses one for similar entries.
4. Set `status` to `resolved` (or `ratified`, if the item was a proposal Jordan approved
   in-principle). Whether to also add a separate `resolution`/`date_resolved` field is
   lane-dependent, not universal — check the target lane's own recent entries first (e.g. every
   `ED-MB-*` entry adds `resolution`, but `ED-FI-0003`/`ED-FI-0004` resolve with no such field at
   all, folding "RESOLVED YYYY-MM-DD ..." into `description` prose instead). Match whichever
   convention that lane already uses rather than adding the field by default.
5. Identify propagation targets by reading the file(s) named in `source` and by grepping the
   corpus for the mechanic/term under discussion — there is no `references/file_index.md` or
   other target-lookup registry to consult (see the Input Validation note above).
6. Read each propagation target from the working tree, apply the decision, commit.
7. Atomic commit: the lane ledger file + all target files edited (+ `id_reservations.yaml` only
   if this resolution also allocates a new ID, e.g. for a superseding entry).

---

## Workflow B — Add New Items

Triggered when a design file contains `[EDITORIAL: ...]` or `[PROVISIONAL: ...]` flags not yet
in the ledger. (This marker convention is independently enforced by
`tools/ci_editorial_checker.py` — see "Enforcement reality" below — for commits touching
`designs/npcs/`, `designs/world/`, `arcs/simulated/`, or `canon/03_canonical_timeline.md`:
substantive new/changed content in those paths must carry an `[EDITORIAL:` or `[PROVISIONAL:`
marker or CI fails. This workflow is how a flag placed in-doc gets a matching ledger entry.)

1. Read the source file from the working tree.
2. Extract all `[EDITORIAL: ...]` / `[PROVISIONAL: ...]` instances.
3. For each: check whether it is already registered — search the relevant lane's `.jsonl` (and
   the flat/archive files, for older material) by description/source similarity. An in-doc flag
   may already cite an existing `ED-NNN`/`ED-<LANE>-NNNN`; if so, this is not a new item.
4. If not registered: determine the correct lane (by subsystem — see the lane roster above),
   re-read `references/id_reservations.yaml`'s `lane_ids.lanes.<LANE>.next_free` **right now**
   (Collision Guard above), assign that ID, append one JSON line to
   `registers/editorial_ledger_<lane>.jsonl` (create the file if this lane has never allocated
   before), and bump `next_free` in `id_reservations.yaml`.
5. Run Workflow D (dedup) before committing.
6. Atomic commit: the lane ledger file(s) + `id_reservations.yaml`. If the in-doc
   `[EDITORIAL: ...]` text itself needs updating to cite the new ID, include that design-file
   edit in the same commit too.

---

## Workflow C — Propagation Pass

Run after any batch of resolved items whose decisions still need to reach other design files.

1. From the relevant lane ledger file(s): filter to entries whose `status` is `resolved` or
   `ratified` but whose `description` indicates propagation/execution is still pending (recent
   entries say this explicitly in prose, e.g. "decision ratified, execution pending" — there is
   no dedicated `propagation_status` field in live lane entries to filter on structurally,
   unlike the legacy/archive files, which do carry one; check both).
2. For each: read target files from the working tree (identified per Workflow A step 5), apply
   the decision text, and update the entry's `description` to record what was executed and
   when (recent entries append an "EXECUTED YYYY-MM-DD ..." clause rather than flipping a
   separate status field — follow that convention unless the entry already used
   `propagation_status`, in which case keep it consistent).
3. Atomic commit: all modified target files + the ledger file(s).

---

## Workflow D — Dedup, Consolidate, and Strike

**Run:** at session start (after reading the ledger files) and whenever new items are added.

### Step 1 — Deduplication
Identify pairs of items that describe the same decision:
- Same or near-exact `description`
- Same `source` with overlapping subject matter
- Same `system`/tags with overlapping decisions

For each duplicate pair:
- Keep the item with the lower/older ED number, or the one with more detail.
- Set the other's `status: struck`, add `stale_reason: "Duplicate of ED-<LANE>-NNNN"` (or
  `ED-NNN` for a legacy duplicate), and `superseded_by: "ED-<LANE>-NNNN"`.

**Do not silently delete.** Struck items remain in the ledger with their status. Never rewrite
or remove another line in the JSONL file except the one being struck — this format is
append/edit-in-place per line, not a rewritten whole-file document.

### Step 2 — Consolidation
Identify items that should be merged because they represent the same underlying decision:

**Consolidation triggers:**
- Same system + same mechanical area + decisions that cannot differ
- Items that explicitly cite each other via `citations`

**Consolidation procedure:**
1. Designate the most complete existing item as primary (or open a new one, allocated per the
   Collision Guard, if neither existing item is a clean primary).
2. Fold the other's substance into the primary's `description`.
3. Mark the folded-in items `status: struck`, `stale_reason: "Consolidated into ED-<LANE>-NNNN"`.

### Step 3 — Stale Striking
Mark items as `status: struck` (with `stale_reason`) or `status: deprecated` (with a
`deprecation` note, the legacy-file convention for "superseded by a different canonical
source entirely" — see `ED-107`'s `deprecation` field for a worked example) when:

**Automatic strike/deprecate criteria:**
- Decision was resolved via simulation or direct code verification — mark `status: resolved`
  with the finding cited in `description` (see e.g. `ED-MB-0007`'s pattern of citing exact
  measured values).
- Feature the item refers to has been CUT — mark `struck`, `stale_reason: "Feature cut — ..."`.
- A later item supersedes this one and the earlier item's decision would conflict — mark
  `struck`, `stale_reason: "Superseded by ED-..."`.
- Item refers to a document that no longer exists or was deprecated — mark `struck`,
  `stale_reason: "Source document deprecated"`.

**Do not auto-strike:**
- Items that are merely low-priority.
- Items where the answer is known but not yet propagated — leave `status: resolved` with the
  propagation-pending state recorded in `description` (Workflow C).
- Blockers (`needs_jordan: true` or anything explicitly marked `P1-BLOCKER`), regardless of age.

### Step 4 — Report
After running dedup/consolidate/strike, output a table:

| Action | Count | IDs |
|--------|-------|-----|
| Deduped (struck as duplicate) | N | ED-..., ... |
| Consolidated | N | ED-... → ED-... |
| Struck (stale/cut) | N | ED-..., ... |
| Remaining open | N | — |
| Remaining `needs_jordan: true` | N | — |

---

## Workflow E — Harvest New Editorials from Session

After any session where design work was done:

1. Read all files modified in the session from the working tree.
2. Extract all `[EDITORIAL: ...]` / `[PROVISIONAL: ...]` flags from those files (see
   `tools/ci_editorial_checker.py` — this is what CI actually enforces on
   `designs/npcs/`, `designs/world/`, `arcs/simulated/`, `canon/03_canonical_timeline.md`
   commits; harvesting keeps the ledger in sync with what CI already requires to exist in-doc).
3. Cross-reference against the relevant lane ledger file(s) (by description/ID match).
4. Add unregistered items via Workflow B (correct lane, real `next_free` allocation).
5. Run Workflow D (dedup/consolidate/strike).
6. Report: N new items added, N consolidated, N struck.

---

## Enforcement reality (what CI actually checks — read before assuming a rule)

Two separate, unrelated CI mechanisms touch this system. Do not conflate them:

- **`tools/ci_editorial_checker.py`** (CI job `editorial-check`) does **not** parse or
  validate the JSONL ledger files at all. It checks that commits touching
  `designs/npcs/`, `designs/world/`, `arcs/simulated/`, or `canon/03_canonical_timeline.md`
  carry an `[EDITORIAL:`, `[PROVISIONAL:`, or `[EDITORIAL GATE]` marker somewhere in the
  changed content (stubs under 200 chars are exempt; auto-generated `_skeleton.md` files are
  exempt). Deleting a file from those paths requires the marker in the commit message instead,
  since deleted content can't be scanned. This is the mechanism Workflow B/E's "flags in
  design files" language is grounded in.
- **`tools/broken_dependency_checker.py::check_editorial_ledger`** (part of the BLOCKING
  `repository-integrity` CI job) is the check that actually reads
  `registers/editorial_ledger.jsonl` and every `registers/editorial_ledger_<lane>.jsonl`. For every
  entry whose `status` is one of the "live" values (`open`, `provisional`, `applied`,
  `confirmed`, `deferred` — resolved/struck/ratified/deprecated entries are historical record
  and exempt), it extracts file-path references from the JSON line and fails the build if any
  of them don't exist on disk (with a remap through `references/restructure_ledger.md` for
  pre-restructure paths). **Practical implication: an entry left `open` with a `source` or
  `description` citing a path that later moves or is deleted will break CI** — either update
  the entry's path reference or resolve/strike it when the file it names goes away.
- **`tools/ci_register_size_check.py`** enforces soft token caps per ledger file (150,000 for
  `registers/editorial_ledger.jsonl` and `_archive.jsonl`; 50,000 per lane file, including
  not-yet-created `_go.jsonl`). Approaching a cap is a split signal (as already happened once
  for the flat file, 2026-07-02 and 2026-07-07), not an emergency — but don't ignore a warning.
- **`tools/validate_ed_citations.py`** scans canon/design docs (not the ledger files
  themselves, which are excluded as source-of-truth registers) for `ED-` citations only (v1 scope
  — `PP-` citations are not validated by this tool) and
  fails if a citation claims ratified/canonical authority (`canonical`, `ratified`, `applied`,
  `closes`, etc. near the citation) while the cited entry is actually still `open` in the
  ledger universe. This is the guard against a design doc asserting an editorial decision that
  was never actually made.

None of the above enforces the field-vocabulary table above as a schema — that table is
descriptive of practice, not something any CI job validates line-by-line.

---

## Commit Convention

All editorial register commits use scope `[editorial]`:

```
[editorial] Resolve ED-FI-0005 (Knot Pool formula) — ED-FI-0005
[editorial] Propagate ED-WR-0002 MS/RS decision to params/threadwork.md — ED-WR-0002
[editorial] Harvest session items, dedup ED-SC-0009/0011 — ED-SC-0012, ED-SC-0013
```

Cite the `ED-<LANE>-NNNN` (or legacy `ED-NNN`) id(s) touched. If the commit also allocates a
new ID via `id_reservations.yaml`, that file is part of the same commit (Collision Guard,
above) — do not split the ledger entry and the `next_free` bump across two commits.

---

## Priority Definitions

| Priority | Definition |
|----------|-----------|
| provisional | A defensible design decision made to unblock work. Requires user review. Text marked `[PROVISIONAL]`. |
| P1-BLOCKER | Blocks compilation or playtest of a system. Nothing downstream can proceed without this. |
| P1 | Must resolve before next playtest. Produces broken or undefined outcomes if unresolved. |
| P2 | Should resolve before distribution. Produces inconsistency or unclear rules if unresolved. |
| P3 | Low urgency. Cosmetic or edge-case. |

These labels appear as free-text inside `description`/legacy `priority`/`severity` fields, not
as an enforced enum — match the wording already used in the target lane file's recent entries.

---

## Dashboard registry logging (MANDATORY on completion)

When this skill's run concludes — pass, fail, or partial — append one record to the
Valoria audit/simulation-run registry (`references/audit_registry.jsonl`) so the
GitHub Pages dashboard and `tools/ci_audit_registry_check.py` can see it. Do this
every time, not only on request — a skipped append is what makes the dashboard's
verdict table go stale.

```bash
python tools/audit_registry.py append \
  --audit-type editorial_register \
  --subsystem <personal_combat|mass_battle|social_contest|faction_political|settlement_territory|threadwork|fieldwork_investigation|architecture|cross_cutting|corpus_wide> \
  --skill valoria-editorial-register \
  --date <YYYY-MM-DD> \
  --folder "<designs/audit/... path this run's output actually lives at>" \
  --scope "<one-line: what was audited>" \
  --verdict <this skill's own verdict, mapped to PASS|FAIL|PARTIAL|CONFORMANT|NON_CONFORMANT|OPEN|MIXED|CLOSED> \
  --verdict-detail "<one-line context, e.g. a PR number or ratification note>"
```

Pick `--subsystem` from what the run actually targeted (`cross_cutting` if it
genuinely spans several, `corpus_wide` only for a whole-corpus pass). See
`tools/audit_registry.py`'s module docstring for the full field/vocabulary
reference — this is the single source of truth for the schema, not this note.
