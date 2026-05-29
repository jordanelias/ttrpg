# A3 — SQL-Index Enshrinement

**Status:** STAGED for push. B6 (branch protection) blocks me committing to `main`, so you push the three repo files **and** apply the PI/architecture text edits below in the same change (migration discipline: code + text land together).
**Date:** 2026-05-28.

---

## What this does

Makes `references/valoria_index.sql` the **governing interface** for "what files does system X comprise" and "what system does file Y belong to." Bootstrap rebuilds the machine layer from HEAD every session (so it cannot drift), loads the curated manifest, and validates coverage loudly. The directory `.md` skeleton/`_index` routing is demoted to *within-doc* navigation; cross-file system membership is answered by the index, not by directory globbing.

The failure this fixes is the one from this session: the manifest already existed (82 concepts / 231 concept_files after A2) but was an **orphan** — `quick_bootstrap` never loaded it, so reads never benefited from it. Enshrinement closes that.

---

## Files to push (3)

1. **`references/valoria_index.sql`** — completed manifest. **49 → 82 concepts, 189 → 231 concept_files, 334 aliases.** Surgical completion: existing core sets unchanged (`threadwork`=10, `faction_layer`=19, `combat`=9), +33 concepts for previously-unregistered active design docs, +42 concept_files (each new concept = its own doc + same-`pair_id` index/infill + direct `params/{stem}.md` only — *not* every matching test). Residual uncovered active design docs = 2 (`combat_c4_draft_v0.md`, an audit `planning_v0.md`), both correctly excluded.
   *(Correction of record: my earlier "empty manifest / 0 rows" claim was a grep error — the dump uses `INSERT OR REPLACE INTO`, which an `INSERT INTO` grep missed. The manifest was never empty.)*

2. **`skills/valoria-orchestrator/scripts/regenerate_file_index.py`** — `open_db` **F2 fix**. `executescript()` on the dump fails with a deferred FK error (single implicit transaction + embedded `PRAGMA foreign_keys=ON` + FTS5 trigger/shadow-table creation). Replaced with a statement-by-statement autocommit loader (FK off during creation, triggers kept atomic, embedded pragmas ignored). The committed dump now round-trips. Adds `_split_sql()` helper.

3. **`skills/valoria-orchestrator/scripts/index_bootstrap.py`** — **NEW**. Enshrinement module:
   - `load_index(g)` → rebuild `files` from HEAD (`run_fast` SHA-diff), load curated, `validate()`. TTL-cached (600s) so per-subprocess bootstrap makes **zero** API calls on a cache hit (cc052aa cost discipline).
   - `validate(conn, strict=False)` → reports `dangling` (manifest paths at deleted/renamed files), `uncovered` (active design docs in no concept), `fk_violations`. **Raises on FK corruption**; raises on any drift when `strict=True`.
   - `concept_files(conn, name)` → the canonical reading set for a system.
   - `which_concepts(conn, path)` / `search(conn, term)` (alias-aware).

Plus test: **`tests/index/test_index_bootstrap.py`** (offline round-trip + query).

---

## PI change — replace `<bootstrap_script>` body with

```python
python3 - <<'BOOTSTRAP'
import os, sys, time, urllib.request, json, base64

PAT = open('/mnt/project/VALORIA_PAT').read().strip()
os.environ['GITHUB_PAT'] = PAT
open('/home/claude/.valoria_pat', 'w').write(PAT)
REPO = 'jordanelias/ttrpg'

SCRIPTS = [
    ('skills/valoria-orchestrator/scripts/github_ops.py',     '/home/claude/github_ops.py'),
    ('skills/valoria-orchestrator/scripts/valoria_hooks.py',  '/home/claude/valoria_hooks.py'),
    ('skills/valoria-orchestrator/scripts/index_bootstrap.py','/home/claude/index_bootstrap.py'),
]
for src, dst in SCRIPTS:
    if os.path.exists(dst) and (time.time() - os.path.getmtime(dst)) < 3600:
        continue
    req = urllib.request.Request(
        f'https://api.github.com/repos/{REPO}/contents/{src}?ref=main',
        headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github.v3+json'})
    with urllib.request.urlopen(req) as r:
        open(dst, 'w').write(base64.b64decode(json.loads(r.read())['content']).decode())

sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap
g, h, files, token = quick_bootstrap()

# SQL-index enshrinement: rebuild files from HEAD, load curated manifest, validate
import index_bootstrap as ix
conn, report = ix.load_index(g)
ix.print_index_summary(report)
BOOTSTRAP
```

The only changes from the V2.2 script: `index_bootstrap.py` added to `SCRIPTS`, and the three `ix.*` lines after `quick_bootstrap()`. Heavy logic stays in the scripts; PI script still just loads → caches → imports → delegates.

Add to PI `<post_bootstrap_calls>`: *"Route system reads through `ix.concept_files(conn, name)` rather than directory globbing; `ix.which_concepts(conn, path)` for reverse lookup. The manifest is the canonical design+params reading set per system."*

---

## Architecture changes (project knowledge — `project-architecture-valoria-v2_4.md`)

- **`<reference_files_pattern>`** — add: *"`references/valoria_index.sql` (SQLite) is the governing file index. `files` (machine) is rebuilt from HEAD each session; `concepts`/`concept_files`/`aliases` (curated) declare per-system canonical reading sets. `concept_files` granularity is **design + params docs**, not test/sim/audit artifacts (those live in `files`, queryable by `domain`). The `file_index_summary.md` markdown remains a human-readable digest; the SQL index is authoritative."*
- **Demote skeleton/`_index` routing** — in `<surface>`/PI `<canon_terms><skeleton>`: clarify `_index.md` sidecars are for heading-level navigation *within* a document; *which files comprise a system* is answered by `ix.concept_files`, not directory walks.
- **`<enforcement_spectrum>`** — new Level-4 row: *"Index load + validate at bootstrap (`index_bootstrap.validate`) — `files` rebuilt from HEAD (drift-proof); FK corruption raises; `strict=True` raises on dangling/uncovered. Loud `[INDEX DRIFT]` warnings otherwise."*

---

## Validation evidence (this session)

```
A) repo's CURRENTLY-committed index:  49 concepts / 189 concept_files / 1712 active files
   [INDEX DRIFT] 33 active design docs registered to no concept   ← exactly what A2 fixes
B) staged completed index:            82 concepts / 231 concept_files / 1713 active files
   [INDEX] coverage clean — every active design doc maps to a concept.

   concept_files('threadwork') → 10 docs incl params/threadwork.md (the MS chart)
   which_concepts('params/threadwork.md') → ['params_threadwork','threadwork']
   search('faction') → faction_canon, faction_layer, faction_systems_overview, params_factions, proper_noun_registry

   build (HEAD rebuild) 3.2s · cache hit 0.00s (zero API) · both modules compile · committed dump round-trips
```

---

## Companion change needed in `safe_commit` (one line)

The index cache (`/home/claude/.index_cache.json`, TTL 600s) must be invalidated on commits that change the file tree, the same way the bootstrap data cache is invalidated. On any `safe_commit` whose `additions`/`deletions` add, move, or delete a file: `os.remove('/home/claude/.index_cache.json')` (guarded). Until added, staleness is bounded to 10 minutes after a tree-changing commit.

---

## Resume-from-here (if interrupted)

Done & staged: `valoria_index.sql` (82/231), `regenerate_file_index.py` (F2 fix), `index_bootstrap.py` (tested), this package, smoke test.
Remaining: (a) you push the 3 files + apply PI/architecture edits + the `safe_commit` one-liner; (b) **Pass B** — traverse each system via its `concept_files` set to completeness (coverage ledger = `concept_files` − `g._session_fetches`), ~3–5 systems/turn; (c) **Pass C** — rebuild loop map + per-system NERS on complete info (fold DC-1..12, add the 5 omitted loop classes, re-anchor the scale ladder to canon's 5 named scales) + the MS two-force model + Force-3 bound (threadwork multiplier + Gap-bleed sized so MS reaches 0 at the civil-war→Altonian-invasion→unification beat, winnable on the maintain path).
