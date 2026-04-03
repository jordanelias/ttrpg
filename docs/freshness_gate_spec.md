# Freshness Gate — Design Spec and Protocol
## Version: 2026-04-02
## Status: IMPLEMENTED — pending SHA population pass

---

## Problem

Params files and canonical docs drift apart. Simulations, audits, and patches
have used stale params values because nothing enforced that params files were
current before use. The only existing check (`STALE CHECK` comment in params headers)
was advisory and model-enforced — trivially bypassed.

---

## Solution: Hard-Tier SHA Tracking

Every canonical document has a commit-level SHA (Git blob OID). This SHA changes
every time the file is modified. If the SHA of the canonical doc on GitHub differs
from the SHA recorded in `canonical_sources.yaml` at the time the params file was
last synced, the params file is stale.

This is code-enforced, not model-enforced.

---

## Components

### 1. `tools/freshness_gate.py`

Standalone Python tool. Three modes:

| Mode | Command | What it does |
|------|---------|--------------|
| Check all | `python3 tools/freshness_gate.py` | Compare live SHA vs recorded SHA for every system. Exit 1 if any stale. |
| Check one | `python3 tools/freshness_gate.py --system combat` | Same, single system. |
| Update | `python3 tools/freshness_gate.py --update` | Fetch live SHAs and write them back to `canonical_sources.yaml`. Run after any canonical doc commit. |

Exit codes:
- `0` = all fresh → proceed
- `1` = stale detected → **BLOCK**
- `2` = `canonical_sha` fields missing → run `--update` first

### 2. `canonical_sources.yaml` Schema Extension

Each system entry gains per-canonical-doc SHA fields. Format:

```yaml
combat:
  canonical: designs/combat/combat_design_v1.md
  canonical_sha__designs__combat__combat_design_v1_md: "abc123def456..."
  params: references/params_combat.md
  ...
```

Key format: `canonical_sha__` + path with `/` → `__` and `.` → `_`.

This keeps SHAs adjacent to the canonical path they track, readable without
any code, and unambiguous when a system has multiple canonical paths.

### 3. Session Start Protocol Addition (orchestrator SKILL.md)

Insert as **Step 2** of Session Start Protocol (before any task work):

```
2. FRESHNESS GATE
   python3 tools/freshness_gate.py
   Exit 0 → proceed.
   Exit 1 → report stale systems. Do not begin any simulation, audit,
             or patch on a stale system until user authorises the
             canonical doc re-read and --update is run.
   Exit 2 → run --update first, then re-check.
```

### 4. Commit Protocol Addition

After every commit that modifies a canonical doc, the committer MUST run:
```
python3 tools/freshness_gate.py --update
```
This is added to the Commit Protocol checklist in the Project Instructions and
in the orchestrator SKILL.md Atomic Commit Discipline section.

---

## Enforcement Points

| When | What runs | Blocks what |
|------|-----------|-------------|
| Session start | `freshness_gate.py` (check mode) | Everything on stale systems |
| After any canonical doc commit | `freshness_gate.py --update` | Next session will gate-pass |
| Pre-simulation | `freshness_gate.py --system <X>` | That simulation |
| Pre-audit | `freshness_gate.py --system <X>` | That audit |
| Pre-patch | `freshness_gate.py --system <X>` | That patch |
| Pre-commit (broken_dependency_checker) | existing tool | Broken file refs |

The freshness gate and broken dependency checker are **both** mandatory pre-commit.

---

## Bootstrap (One-Time)

Run once to populate all SHA fields in `canonical_sources.yaml`:

```bash
export GITHUB_PAT=<pat>
python3 tools/freshness_gate.py --update
```

Then verify:

```bash
python3 tools/freshness_gate.py
# Expected: [GATE PASSED] All systems fresh.
```

After this, every canonical doc commit must re-run `--update` to keep SHAs current.

---

## What This Does NOT Solve

- Params file content accuracy (a params file could have the right SHA but
  contain wrong extracted values). This is a separate problem — the params
  audit pass addresses it.
- Drift within a session if a canonical doc is committed mid-session.
  Mitigation: run `--system <X>` before each simulation even within a session.

---

## Files Modified by This Feature

| File | Change |
|------|--------|
| `tools/freshness_gate.py` | New tool |
| `references/canonical_sources.yaml` | `canonical_sha__*` fields added per system |
| `skills/valoria-orchestrator/SKILL.md` | Session Start step 2 + Commit Protocol addition |
| Project Instructions | Commit Protocol bullet: run `freshness_gate.py --update` |
