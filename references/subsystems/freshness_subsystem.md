# Freshness Subsystem
**Status:** built · documented 2026-05-31 (Lane B, roadmap 2.4)
**Source:** `tools/freshness_gate.py` + `references/canonical_sources.yaml` (the `canonical_sha__*` fields) + `/home/claude/.freshness_cache.json` (10-min disk cache)

## Purpose
Detects drift between a derived `params` file and the canonical design document it was synced from. Each canonical source in `references/canonical_sources.yaml` carries a recorded `canonical_sha`; freshness compares that against the **live HEAD blob SHA** of the doc. If they differ, the params file is stale and simulation / audit / patch work is BLOCKED until re-sync. Bootstrap reports `[FRESHNESS ✓] All 115 canonical sources fresh` or the stale set.

## Public API (`tools/freshness_gate.py`)
- `run_check(system_filter=None)` — compare declared vs live SHAs (all sources, or one system). Exit semantics below.
- `run_update()` — recompute and re-inject every `canonical_sha`. The `--update` path; run after a commit changes a canonical doc.
- `parse_canonical_pairs(content) -> [(path, recorded_sha)]` — extract the declared pairs from `canonical_sources.yaml`.
- `get_blob_shas_batch(paths) -> {path: live_sha}` — batched GraphQL blob-SHA lookup against `main`.
- `inject_shas(content, path_to_sha) -> new_content` — rewrite the `canonical_sha` fields in place (SHA-only diff).
- `get_blob_sha`, `get_file`, `put_file`, `sha_key` — single-file helpers.

## CLI / exit codes
```
python3 tools/freshness_gate.py            # check all
python3 tools/freshness_gate.py --system combat
python3 tools/freshness_gate.py --update   # re-sync all SHAs after a commit
```
`0` = all fresh · `1` = one or more stale (BLOCK sim/audit/patch) · `2` = `canonical_sha` fields missing (run `--update` first). Requires `GITHUB_PAT`.

## Re-sync the correct way (precedent: 5.5, commit `ad98144d`)
To refresh stale SHAs, use the pure functions (`parse_canonical_pairs` → `get_blob_shas_batch` → `inject_shas`) and commit the result through **`h.safe_commit`** — *not* the tool's own `put_file`/update path, which bypasses the commit gates. The diff must be SHA-only.

## Artifacts
- `references/canonical_sources.yaml` — declares the ~115 canonical paths + their `canonical_sha` fields (the freshness source of truth). Currently at an interim 12k-token cap.
- `/home/claude/.freshness_cache.json` — freshness SHA results, 10-minute TTL (avoids re-querying every subprocess).

## Queued refactor (roadmap 2.4 — do *with/after* this doc, not blind)
Move the 115 `canonical_sha` fields out of `canonical_sources.yaml` into a dedicated `references/canonical_freshness.yaml` (writer = `tools/freshness_gate.py`), dropping `canonical_sources.yaml` to ~5k of pure declarations on the hot bootstrap path. This is Lane B item 5.3 — **not** to be run during a parallel window (the file is co-claimed via the co-file SHA hook).

## Gotchas
- Stale freshness BLOCKS sim/audit/patch (exit 1) — it is a hard gate for those task types, unlike compliance (advisory).
- The 10-min cache means a just-committed canonical change may read fresh until the cache expires or is invalidated.
