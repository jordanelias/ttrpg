"""THE ONE ANCHOR. Every path this package derives is named here, once.

⚠ THIS IS THE ONLY MODULE IN `season/` THAT MAY ANCHOR ITSELF ON ITS OWN MODULE LOCATION -- a
checkable property, though not by a bare grep for the dunder spelling of the module-location name:
a comment discussing the invariant necessarily matches it too (`harness/governance_spine.py` names
this paradox at its own site). The narrower, actually-true claim: this module owns every path to a
REGISTRY the package loads; `tests/test_season_shape.py` legitimately resolves its own `.py` for an
AST walk, and neither of those is a second anchor. Before this
module the package carried 29 independent anchors across 10 files, each climbing its own chain of
`.parent`s, and the length of that chain was a fact about where the file happened to sit rather
than about the tree. A path anchor fails silently by construction -- the degradation each
seam performs on purpose (a named gap rather than an ImportError) is exactly what hides a wrong
anchor -- so the anchor has to be checked at import, in one place, or not at all.

WHAT THE SELF-CHECK BUYS. It fires on import, before any caller can read a constant, and it names
the directory it computed. Two of its three clauses are about the REPOSITORY (`CLAUDE.md` and
`engine/` are at the root and nowhere else on the way up), and two are about WHERE THIS PACKAGE
SITS IN IT, so a wrong depth in either direction is caught: too shallow and the package names do
not match, too deep and the repo markers are absent.

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
# THE ANCHOR ITSELF. `engine/season/data/files.py` -> data -> season -> engine -> repo.
#
# ⚠ THE CHAIN IS ONE LINK SHORTER THAN IT WAS, AND THAT IS THE WHOLE REASON THIS MODULE EXISTS.
# The package was decomposed while it lived at `proposals/2026-09-01-season-loop-tests/season/`,
# five levels below the repo root; it is now at `engine/season/`, four. Every path in the package
# moved by one level in one edit HERE, and the self-check below is what turns a wrong depth into an
# import-time refusal instead of six silently skipped seam tests.
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = DATA_DIR.parent
HARNESS_DIR = PACKAGE_DIR / "harness"
STATE_DIR = PACKAGE_DIR / "state"
TESTS_DIR = PACKAGE_DIR / "tests"
ENGINE_DIR = PACKAGE_DIR.parent
REPO_ROOT = ENGINE_DIR.parent

# ⚠ LOUD AT IMPORT, NAMING WHAT IT COMPUTED. See the module docstring: every consumer of a path in
# this package degrades gracefully on a missing file, so a wrong anchor is invisible downstream.
# Two clauses are about the REPOSITORY and two about THIS PACKAGE's position in it, so a wrong
# depth is caught in either direction: too shallow and the package names do not match, too deep
# and the repository markers are absent.
assert (REPO_ROOT / "CLAUDE.md").is_file() and (REPO_ROOT / "engine").is_dir() \
    and PACKAGE_DIR.name == "season" and ENGINE_DIR.name == "engine", REPO_ROOT

# ---------------------------------------------------------------------------
# THIS PACKAGE'S OWN DATA. `runs/` is written by `harness/report.py` alone (`W15`, guardrail `G7`).
# ⚠ THE FIVE YAML REGISTRIES BELOW USED TO LIVE IN A SIBLING PROPOSAL DIRECTORY AND NOW LIVE
# HERE, co-located with the code that reads them -- the adoption's doing (ED-IN-0204), not the
# decomposition's. They are listed in this section rather than under SIBLINGS because that is now
# what they are: files this package owns.
# ---------------------------------------------------------------------------
RUNS_DIR = PACKAGE_DIR / "runs"
CASES_DIR = PACKAGE_DIR / "cases"
EXERCISES_DIR = CASES_DIR / "exercises"
CHAIN_CASES_DIR = CASES_DIR / "chain"
RESULTS_JSON = RUNS_DIR / "results.json"
TRACE_TXT = RUNS_DIR / "TRACE.txt"

# The same artifact as a REPO-RELATIVE string, because `harness/delta.py` reads it out of git
# (`git show <rev>:<path>`) rather than off the disk, and git speaks repo-relative paths only.
RESULTS_REPO_REL = RESULTS_JSON.relative_to(REPO_ROOT).as_posix()

# ⚠ AND THE SAME ARTIFACT AT ITS PRE-ADOPTION PATH, WHICH IS NOT A HISTORICAL FOOTNOTE. `delta.py`
# reads a COMMITTED REVISION, so it must be able to name where the file lived AT THAT REVISION --
# before the adoption commit it existed only under `proposals/`, and naming one path alone made
# `delta.py <any earlier rev>` a hard refusal. That is this lane's declared `G11` carrier going
# silent at exactly the commit that needed it. ⚠ THE CONSTANT WAS DROPPED ONCE ALREADY, in the
# three-way merge that brought the decomposition onto the adopted tree: the DEFINITION sat inside
# a conflict hunk and the USE sat outside it, so taking one side left `delta.py` raising
# `NameError` on every `<rev>` argument while `delta.py` with no argument still worked. It lives
# here now, beside its sibling, which is where a second path for one artifact belongs.
RESULTS_BEFORE_ADOPTION_REPO_REL = "proposals/2026-09-01-season-loop-tests/runs/results.json"

# ---------------------------------------------------------------------------
# THE DOCTRINE THIS INSTRUMENT IS ABOUT. Read, never written. `architecture/` is LAYER 1 -- prose,
# and reference under `CLAUDE.md` §0.05; the mechanism is the YAML above and the code around it.
# ---------------------------------------------------------------------------
ARCH_DIR = REPO_ROOT / "architecture"
ARCHITECTURE_V2_MD = ARCH_DIR / "ARCHITECTURE_V2.md"
ARCH_PLAN_MD = ARCH_DIR / "PLAN.md"
SOURCE_353_MD = ARCH_DIR / "holonic_ARCHITECTURE.md"

# ---------------------------------------------------------------------------
# THE YAML REGISTRIES THIS PACKAGE READS, all co-located since the adoption.
# ---------------------------------------------------------------------------
WRITE_MATRIX_YAML = PACKAGE_DIR / "write_matrix.yaml"
ROSTERS_YAML = PACKAGE_DIR / "rosters.yaml"
VERB_TABLE_YAML = PACKAGE_DIR / "verb_table.yaml"
HOLE_REGISTER_YAML = PACKAGE_DIR / "hole_register.yaml"
REQUIREMENTS_YAML = PACKAGE_DIR / "requirements.yaml"
ENDINGS_CLASSIFIED_YAML = PACKAGE_DIR / "ENDINGS_CLASSIFIED.yaml"
# ⚠ A FIXTURE'S REGISTRY, AND IT IS ANCHORED HERE FOR THE SAME REASON THE OTHERS ABOVE ARE.
# `governance_spine.yaml` declares the 13-seat generic ladder. It was first written with a
# local `Path(__file__).resolve().parents[1]` inside `harness/governance_spine.py` — a
# SECOND anchor in the package whose whole point is to have one, and the exact defect
# `harness/populated.py` records having already removed once. The invariant that catches it
# is this module's own -- narrower than a bare grep for `__file__` (see the module docstring
# above): this module owns every path to a registry the package loads.
GOVERNANCE_SPINE_YAML = PACKAGE_DIR / "governance_spine.yaml"

# The degree sweep's two arm modules (plus their shared `sweep_core`), imported by source in two
# tests. Moved out of `proposals/2026-09-04-degree-sweep` to `engine/reference/degree-sweep/` so
# the blocking test suite depends on no unratified tree (ED-IN-0231 precedent); the measurement
# record (runs/, README.md, EXECUTION_PLAN.md, the other arms) stays in the proposal.
DEGREE_SWEEP_DIR = ENGINE_DIR / "reference" / "degree-sweep"

# ---------------------------------------------------------------------------
# THE REPOSITORY. The flat personal-combat module set is NOT anchored here: it is loaded by the
# one path seam, engine/substrate/pc_engine.py (2026-09-25), which seam/wrappers/combat.py calls.
# ---------------------------------------------------------------------------
SYSTEMS_DIR = REPO_ROOT / "systems"
REFERENCES_DIR = REPO_ROOT / "references"
MODULE_CONTRACTS_YAML = REFERENCES_DIR / "module_contracts.yaml"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"

# ⚠ THE CAST, AND IT IS CANON RATHER THAN THIS PACKAGE'S OWN. 46 character rows whose ids are an
# EXACT 1:1 MATCH with `load_cases("NPC")` — measured, zero symmetric difference — carrying an
# authored `faction`, `role`, weighted `convictions` over the canonical thirteen, and a `title` on
# seven. It sat unread by anything that executes while `run_cases.seed_pursuits` derived each
# person's convictions from `blake2b(seed, case_id, pid)`. Named here because `files.py` is the one
# anchor; read through `data/cast.py`, which is the one reader.
NPC_REGISTRY_YAML = REFERENCES_DIR / "npc_registry.yaml"
# `names_index.yaml` HAD A CONSTANT HERE AND NO LONGER NEEDS ONE (2026-09-16). `cast.py`
# opened it directly to build a faction alias map; it now reads `engine/substrate/names.py`,
# which is fed by `tools/export_names.py`. Nothing under `engine/season/` opens the YAML, so
# the constant was a declared-but-unread row -- `01_AXIOMS.md` ID-13's "mechanism that does
# not exist, wearing a schema's clothes". Deleted rather than kept for a caller that is gone.


def subsystem_sim_dir(name: str) -> Path:
    """`systems/<name>/sim/` — asked of the tree directly where a module contract carries no
    `sim_module:`. A function rather than a constant because the subsystem is not known here."""
    return SYSTEMS_DIR / name / "sim"


# ---------------------------------------------------------------------------
# THIS PACKAGE'S OWN SOURCES. Several guards read the instrument's source rather than importing it
# -- an AST walk over the write call sites, the roster scan, the margin-producer scan.
# ---------------------------------------------------------------------------
LOOP_DIR = PACKAGE_DIR / "loop"
# The season loop itself, extracted from `shape.py` at step 9. Source-scanning guards that
# used to read `SHAPE_PY` for `SeasonDriver` code read this instead -- `shape.py` was deleted at
# step 10, so a scan pointed there fails to open a file rather than passing by finding nothing.
DRIVER_PY = LOOP_DIR / "driver.py"


def loop_modules() -> tuple:
    """EVERY `.py` UNDER `loop/`, DISCOVERED. The season loop's source corpus.

    ⚠ **THIS EXISTS BECAUSE `DRIVER_PY` ALONE STOPPED BEING THE LOOP AT UNIT L5 (ED-IN-0206).**
    `04_CODE_ARCHITECTURE.md` §A.2:134 makes `loop/` *"driver + six steps"*, so the six step bodies
    left `driver.py` for their own modules -- and six guards read `files.DRIVER_PY` BY FIXED PATH.
    Four went loudly red on the move and one, `test_w2`'s write-call-site walk, would have NARROWED
    IN SILENCE: its only floor is `assert pairs`, which `probes.py` satisfies on its own, so it
    would have reported clean over every write site the six steps took with them. That is the fourth
    recurrence of one defect in this package (steps 2, 4, 5, now), and the fix is the same one
    `package_modules` states above: **compute the corpus, never list it.**

    A caller that scans this for a property must also pin a FLOOR or a SUPERSET, because a
    discovery that stops matching passes by finding nothing (`CLAUDE.md` §0.1 pt 2)."""
    return tuple(sorted(LOOP_DIR.rglob("*.py"),
                        key=lambda p: p.relative_to(LOOP_DIR).as_posix()))


def loop_source() -> str:
    """Every `loop/` module's text, concatenated in path order -- for the guards that grep the
    season loop for a literal rather than walking it."""
    return "\n".join(p.read_text(encoding="utf-8") for p in loop_modules())

# ---------------------------------------------------------------------------
# AX-2's ISLAND, AND THE ONLY DIRECTORY IN THIS PACKAGE WHOSE SHAPE IS AN ENFORCEMENT MECHANISM
# RATHER THAN A FILING CHOICE. `04_CODE_ARCHITECTURE.md:1046`: *"`decision/` is a directory from its
# first commit. The isolation scan matches BY PATH, so a `choose` drafted inside `loop/` and moved
# later would have been green while violating AX-2."* The scan that sentence names reads this
# anchor, and it reads the DIRECTORY rather than a file list -- a member added tomorrow is scanned
# by existing, which is `package_modules`'s own lesson one directory down.
# ---------------------------------------------------------------------------
DECISION_DIR = PACKAGE_DIR / "decision"


def decision_modules() -> tuple:
    """EVERY `.py` under `decision/`, discovered. The AX-2 scan's corpus.

    ⚠ Recursive and derived, for the reason `package_modules` states above it: three guards in this
    package were first written against a filename tuple and each went blind when a module was added.
    A caller must also assert a FLOOR on the length -- `04_CODE_ARCHITECTURE.md` §A.2:133 names four
    members, so a scan that finds fewer has stopped matching and is passing vacuously (`CLAUDE.md`
    §0.1 pt 2)."""
    return tuple(sorted(DECISION_DIR.rglob("*.py"),
                        key=lambda p: p.relative_to(DECISION_DIR).as_posix()))
SEAM_DIR = PACKAGE_DIR / "seam"
# ⚠ THE WRAPPER MOVED UNDER `seam/wrappers/` (L2, ED-IN-0206). `04:135` and §A.2's
# `seam/wrappers/*` row put one wrapper per deferred subsystem there; it sat at the package root
# because the step-8 plan read D5's COST as a reason not to perform the rename. The declared
# `sys.path` seam in `tests/valoria/test_engine_does_not_import_systems.py` is renamed with it.
COMBAT_SEAM_PY = SEAM_DIR / "wrappers" / "combat.py"
TRACE_LOG_PY = PACKAGE_DIR / "trace_log.py"
TEST_PY = TESTS_DIR / "test_season_shape.py"

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
