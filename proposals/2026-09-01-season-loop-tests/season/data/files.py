"""THE ONE ANCHOR. Every path this package derives is named here, once.

⚠ THIS IS THE ONLY MODULE IN `season/` THAT MAY ANCHOR ITSELF ON ITS OWN MODULE LOCATION, and that
is a checkable property rather than a convention: with `D` standing for the dunder spelling of the
module-location name, `grep -rln D season/` must print this file and nothing else. Before this
module the package carried 29 independent anchors across 10 files, each climbing its own chain of
`.parent`s, and the length of that chain was a fact about where the file happened to sit rather
than about the tree. `combat_seam.py` is the worked case for why that is dangerous rather than
merely untidy: it climbed four levels, so moving the file one directory changes which directory
`_PC` names, `engine()` returns `None`, `resolve()` answers `ENGINE-UNAVAILABLE`, six seam tests
SKIP, and the run stays GREEN. A path anchor fails silently by construction -- the degradation each
seam performs on purpose (a named gap rather than an ImportError) is exactly what hides a wrong
anchor -- so the anchor has to be checked at import, in one place, or not at all.

WHAT THE SELF-CHECK BUYS. It fires on import, before any caller can read a constant, and it names
the directory it computed. Two of its three clauses are about the REPOSITORY (`CLAUDE.md` and
`engine/` are at the root and nowhere else on the way up), and the third is about THIS PROPOSAL, so
a wrong depth in either direction is caught: too shallow and the proposal name does not match, too
deep and the repo markers are absent.

THE PATHS ARE FLAT CONSTANTS, DELIBERATELY. No dict, no tuple, no lookup by string key -- a caller
names the thing it wants and a typo is an `AttributeError` at the call site rather than a `None`
that travels. (It is also what keeps this module clear of the roster gate in
`test_jordan_no_definition_is_hardcoded_in_a_body`, which reads any collection of three or more
short string constants as a definition that belongs in a data file. These are locations, not
definitions, and they are not spelled as a collection.)
"""

from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------
# THE ANCHOR ITSELF. `season/data/files.py` -> data -> season -> the proposal -> proposals -> repo.
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = DATA_DIR.parent
HARNESS_DIR = PACKAGE_DIR / "harness"
PROPOSAL_DIR = PACKAGE_DIR.parent
PROPOSALS_DIR = PROPOSAL_DIR.parent
REPO_ROOT = PROPOSALS_DIR.parent

# ⚠ LOUD AT IMPORT, NAMING WHAT IT COMPUTED. See the module docstring: every consumer of a path in
# this package degrades gracefully on a missing file, so a wrong anchor is invisible downstream.
assert (REPO_ROOT / "CLAUDE.md").is_file() and (REPO_ROOT / "engine").is_dir() \
    and PROPOSAL_DIR.name == "2026-09-01-season-loop-tests", REPO_ROOT

# ---------------------------------------------------------------------------
# THIS PROPOSAL. `runs/` is written by `harness/report.py` alone (`W15`, guardrail `G7`).
# ---------------------------------------------------------------------------
RUNS_DIR = PROPOSAL_DIR / "runs"
CASES_DIR = PROPOSAL_DIR / "cases"
EXERCISES_DIR = CASES_DIR / "exercises"
RESULTS_JSON = RUNS_DIR / "results.json"
TRACE_TXT = RUNS_DIR / "TRACE.txt"

# The same artifact as a REPO-RELATIVE string, because `harness/delta.py` reads it out of git
# (`git show <rev>:<path>`) rather than off the disk, and git speaks repo-relative paths only.
RESULTS_REPO_REL = RESULTS_JSON.relative_to(REPO_ROOT).as_posix()

# ---------------------------------------------------------------------------
# SIBLING PROPOSALS IN THE CHAIN. Read, never written: `2026-08-31-shape-tracer/cases/` is a
# PREDECESSOR's committed corpus and this chain does not own it (`corpus_run.rescales`).
# ---------------------------------------------------------------------------
ARCH_DIR = PROPOSALS_DIR / "2026-09-02-executable-architecture"
WRITE_MATRIX_YAML = ARCH_DIR / "write_matrix.yaml"
ROSTERS_YAML = ARCH_DIR / "rosters.yaml"
VERB_TABLE_YAML = ARCH_DIR / "verb_table.yaml"
HOLE_REGISTER_YAML = ARCH_DIR / "hole_register.yaml"
ARCHITECTURE_V2_MD = ARCH_DIR / "ARCHITECTURE_V2.md"
ARCH_PLAN_MD = ARCH_DIR / "PLAN.md"

HOLONIC_DIR = PROPOSALS_DIR / "2026-09-01-holonic-architecture"
SOURCE_353_MD = HOLONIC_DIR / "ARCHITECTURE.md"

SHAPE_TRACER_DIR = PROPOSALS_DIR / "2026-08-31-shape-tracer"
CHAIN_CASES_DIR = SHAPE_TRACER_DIR / "cases"
ENDINGS_CLASSIFIED_YAML = CHAIN_CASES_DIR / "ENDINGS_CLASSIFIED.yaml"

DEGREE_SWEEP_DIR = PROPOSALS_DIR / "2026-09-04-degree-sweep"

# ---------------------------------------------------------------------------
# THE REPOSITORY. Two seams reach out of the proposal and both load BY PATH and ON FIRST USE:
# `combat_seam.engine()` (the flat personal-combat module set) and `shape.degree_ladder()`
# (`engine.autoload.dice_engine`). Each is deferred so the tracer still runs where the tree is
# absent, degrading to a NAMED gap rather than an ImportError at import.
# ---------------------------------------------------------------------------
SYSTEMS_DIR = REPO_ROOT / "systems"
PC_ENGINE_DIR = SYSTEMS_DIR / "combat" / "combat_engine_v1"
REFERENCES_DIR = REPO_ROOT / "references"
MODULE_CONTRACTS_YAML = REFERENCES_DIR / "module_contracts.yaml"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"


def subsystem_sim_dir(name: str) -> Path:
    """`systems/<name>/sim/` — asked of the tree directly where a module contract carries no
    `sim_module:`. A function rather than a constant because the subsystem is not known here."""
    return SYSTEMS_DIR / name / "sim"


# ---------------------------------------------------------------------------
# THIS PACKAGE'S OWN SOURCES. Several guards read the instrument's source rather than importing it
# -- an AST walk over the write call sites, the roster scan, the margin-producer scan.
# ---------------------------------------------------------------------------
SHAPE_PY = PACKAGE_DIR / "shape.py"
COMBAT_SEAM_PY = PACKAGE_DIR / "combat_seam.py"
TRACE_LOG_PY = PACKAGE_DIR / "trace_log.py"
TEST_PY = PACKAGE_DIR / "test_tracer_is_honest.py"

PROBES_PY = HARNESS_DIR / "probes.py"
RUN_CASES_PY = HARNESS_DIR / "run_cases.py"
CORPUS_RUN_PY = HARNESS_DIR / "corpus_run.py"
EXERCISES_PY = HARNESS_DIR / "exercises.py"
REGISTER_PY = HARNESS_DIR / "register.py"
REPORT_PY = HARNESS_DIR / "report.py"
DELTA_PY = HARNESS_DIR / "delta.py"
HEADLESS_PY = HARNESS_DIR / "headless.py"


def package_modules() -> tuple:
    """EVERY `.py` IN THIS PACKAGE, DISCOVERED AND NEVER LISTED, sorted by package-relative path.

    ⚠ THE DISCOVERY IS THE POINT, and it is this repository's own lesson rather than a preference.
    Three guards need *every module in the instrument*: the roster scan, the need-taint scan and
    the margin-producer scan. Each was first written against a hardcoded filename tuple, and each
    time a module was added it went unscanned BY CONSTRUCTION -- `G2` forbids the shape (a
    filename roster is a router), so the set is computed. Recursive, because the harness modules
    now live one directory down and a flat `glob` would silently drop eight of them, which is the
    same defect in a new spelling."""
    return tuple(sorted(PACKAGE_DIR.rglob("*.py"),
                        key=lambda p: p.relative_to(PACKAGE_DIR).as_posix()))
