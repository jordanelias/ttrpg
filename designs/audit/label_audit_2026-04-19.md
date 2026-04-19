<!-- [EDITORIAL: PP-670 — label accuracy audit 2026-04-19, user-directed] -->

# Label Accuracy Audit — 2026-04-19

**Patch:** PP-670
**Scope:** Verify `npc_roster_caste_annotations_deprecated.md` is actually deprecated; sweep repo for other mislabeled files (`_deprecated`, `_legacy`, `_historical`, `_superseded`, `_old`, `_obsolete`).

---

## §1 Primary target — npc_roster_caste_annotations_deprecated

**Path:** `designs/npcs/npc_roster_caste_annotations_deprecated.md`
**Status:** CORRECTLY LABELED (deprecated) — with one minor inconsistency

**Evidence:**
- File banner: `<!-- DEPRECATED -->` + `**DEPRECATED — 2026-04-11**` + "Do not use as a canonical source"
- Note: "Merged into designs/npcs/npc_roster.md as §14"
- `designs/npcs/npc_roster_v30.md` (the current canonical) contains `## 14. Caste System Impact on Roster NPCs` — confirmed the merge happened

**Minor inconsistency:** The internal "Companion to: designs/npcs/npc_roster.md" path is stale — canonical is `npc_roster_v30.md` (v30 suffix). Merge note in same file uses the same stale path. Not a reader-hazard since the deprecation banner is clear, but the path reference is pre-v30-rename.

**Recommendation:** no action. File stays. Internal path note is itself part of the deprecation artifact (it documents the historical state at deprecation time).

---

## §2 Label sweep findings

Scanned repo for filename suffixes `_deprecated`, `_legacy`, `_historical`, `_superseded`, `_old`, `_obsolete`. Total hits: 71 files (61 `_deprecated`, 6 `_legacy`, 3 `_historical`, 1 `_superseded`).

Files inside `deprecated/` or `archives/` directories: correctly organized — skipped from review.
Files outside those directories: 9 candidates reviewed.

### §2.1 Files outside deprecated/ with deprecation suffix

| File | Location | Label Analysis |
|-|-|-|
| `designs/npcs/npc_roster_caste_annotations_deprecated.md` | active `designs/` | ✓ Correctly labeled; see §1. |
| `tests/audit/audit_threadwork_v24_deprecated.md` | active `tests/` | ✓ Correctly labeled — DEPRECATED banner + superseded-by pointer. Location OK (tests/ is fine as audit artifact repository). |
| `tests/sim/sim_ttrpg_batch_legacy_02.md` | active `tests/sim/` | ⚠ Filename-only label. No internal DEPRECATED/LEGACY banner. See §2.2. |
| `tests/sim/sim_ttrpg_batch_legacy_03.md` | active `tests/sim/` | ⚠ Same as above. |
| `tests/sim/sim_ttrpg_batch_legacy_04.md` | active `tests/sim/` | ⚠ Same as above. |
| `designs/threadwork/threadwork_v25_historical.md` | active `designs/` | ⚠ Label partially correct — see §2.3. |
| `designs/threadwork/threadwork_v25_historical_skeleton.md` | active `designs/` | Auto-generated skeleton of above; inherits issue. |
| `params/threadwork_superseded.md` | active `params/` | ✓ Correct internal banner ("SUPERSEDED SECTIONS"). Location unconventional but intentional — threadwork references still resolve. |
| `deprecated/gm_ref/arcs_10_17_historical.md` | deprecated dir | ✓ Correctly placed; historical sim/arc record. |

### §2.2 sim_ttrpg_batch_legacy — FILENAME-ONLY LABEL

**Issue:** Three files (`_legacy_02`, `_03`, `_04`) have "legacy" only in the filename. No internal content banner warns the reader that these are historical simulation records.

**Context:** `tests/sim/sim_ttrpg_batch_02.md` ALSO exists (non-legacy) — they're distinct runs. The non-legacy is the later / re-run version. A reader opening the legacy file without seeing its filename would not know it's superseded.

**Recommendation:** Low priority. These are in `tests/sim/` (not in active design path), and sim records are historical-by-design. Adding a `<!-- LEGACY — superseded by non-legacy-named equivalent -->` banner at top would be correct but is minor infrastructure work. Defer.

### §2.3 threadwork_v25_historical — LABEL MISMATCH

**Path:** `designs/threadwork/threadwork_v25_historical.md` (96,661 chars)
**Canonical:** `designs/threadwork/threadwork_v30.md` (75,450 chars)

**Issue:** The "historical" suffix implies archived state, but:
- Content header reads `# THREADWORK MECHANICS — v2.6` + `## Version: v3.1` (same as canonical)
- File size is LARGER than canonical (96k vs 75k) because it retains pre-atomization prose and appendix content
- No internal DEPRECATED/HISTORICAL banner at top
- First line is just the content header, not a status marker

**True state:** This is the **pre-atomization** version of threadwork_v30. Canonical was atomized on 2026-04-13 (per canonical's `<!-- v30 baseline — renamed from designs/ttrpg/threadwork_redesign_v25.md on 2026-04-13 -->` comment). The historical file preserves the full prose/appendix form from before that atomization.

**Recommendation:** Add an internal banner to the historical file:
```
<!-- HISTORICAL — pre-atomization snapshot (2026-04-13) -->
<!-- Canonical is designs/threadwork/threadwork_v30.md -->
<!-- This file preserves prose/appendix content atomized out of canonical on 2026-04-13 -->
```

The skeleton (`threadwork_v25_historical_skeleton.md`) inherits the issue but correction on canonical flows through next skeleton regen. No direct edit needed to skeleton.

### §2.4 Other sweep findings — NO mislabels

Surveyed:
- `deprecated/*` — 57 files, all correctly placed per `deprecated/README.md` policy.
- `archives/session/session_log_legacy_migration.md` — legacy in name, appropriate for migration record.
- `deprecated/sim_coverage_matrix_legacy.md`, `deprecated/stage8_combat_legacy.md` — both in deprecated/.
- `params/threadwork_superseded.md` — internal banner correct, location intentional.

---

## §3 Summary

| Category | Count | Status |
|-|-|-|
| Correctly labeled + located | 66 | OK |
| Correctly labeled in content, minor path-staleness | 1 (`caste_annotations_deprecated`) | Accept as-is |
| Filename-only label, no internal banner | 3 (`sim_ttrpg_batch_legacy_*`) | Low priority — defer |
| Label mismatch (no internal banner) | 1 (`threadwork_v25_historical.md`) | Fix: add banner |
| Total reviewed | 71 | — |

**Action this commit:** Add HISTORICAL banner to `designs/threadwork/threadwork_v25_historical.md` to match its filename label.

**Deferred actions:** Add LEGACY banner to three `sim_ttrpg_batch_legacy_*` files — low priority infrastructure work, defer to next test-layer sweep.

**No false positives found** — the "_deprecated" suffix on `npc_roster_caste_annotations_deprecated.md` is genuinely accurate; all directory-based deprecation placements are correct.
