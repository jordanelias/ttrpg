# Valoria Tools Directory

## CI Tools (run on every push to main)
| Tool | Purpose |
|---|---|
| `ci_register_size_check.py` | Enforces token thresholds on governed files |
| `ci_co_file_checker.py` | Verifies co-file requirements (design→canonical_sources, patch→propagation_map, sim→coverage_matrix) |
| `ci_editorial_checker.py` | Checks editorial paths have [EDITORIAL]/[PROVISIONAL] markers |
| `ci_hooks_verifier.py` | Verifies hooks wired, skills clean, skeleton limits |

## Integrity Tools (run in CI integrity job)
| Tool | Purpose |
|---|---|
| `broken_dependency_checker.py` | Scans propagation_map + canonical_sources for refs to nonexistent files |
| `patch_propagation_checker.py` | Verifies patches listed in patch_register are reflected in params file headers |
| `freshness_gate.py` | Detects drift between canonical docs and their SHA records in canonical_sources |

## Utility Tools (manual use)
| Tool | Purpose |
|---|---|
| `coverage_matrix.py` | Generates/updates coverage matrix from test files |
| `find_references.py` | Find all references to a given file path across the repo |
| `propagator.py` | Propagate patch changes to affected files |
| `verify_cuts.py` | Verify content was properly cut during skeleton/infill splits |
| `model_router.html` | UI for model routing decisions |
| `editorial_review/valoria-editorial-review.jsx` | React component for editorial review workflow |
