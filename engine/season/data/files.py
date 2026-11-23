"""THE ONE ANCHOR. Every path this package derives is named here, once.

⚠ THIS IS THE ONLY MODULE IN `season/` THAT MAY ANCHOR ITSELF ON ITS OWN MODULE LOCATION -- a
checkable property, though not by a bare grep for the dunder spelling of the module-location name:
a comment discussing the invariant necessarily matches it too (`harness/governance_spine.py` names
this paradox at its own site). The narrower, actually-true claim: this module owns every path to a
REGISTRY the package loads; `tests/test_season_shape.py` legitimately resolves its own `.py` for an
AST walk, and neither of those is a second anchor. An anchor climbing its own chain of `.parent`s
makes the length of that chain a fact about where the file happens to sit rather than about the
tree. A path anchor fails silently by construction -- the degradation each
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
`test_jordan_no_definition_is_hardcoded_in_a_body` (retired), which reads any collection of three or more
short string constants as a definition that belongs in a data file. These are locations, not
definitions, and they are not spelled as a collection.)
"""

from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------
# THE ANCHOR ITSELF. `engine/season/data/files.py` -> data -> season -> engine -> repo.
#
# ⚠ A MOVE OF THE PACKAGE MOVES EVERY PATH IN IT IN ONE EDIT HERE, and the self-check below is
# what turns a wrong depth into an import-time refusal instead of silently skipped seam tests.
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
# ⚠ THE YAML REGISTRIES BELOW ARE CO-LOCATED WITH THE CODE THAT READS THEM (ED-IN-0204): files
# this package owns.
# ---------------------------------------------------------------------------
RUNS_DIR = PACKAGE_DIR / "runs"
CASES_DIR = PACKAGE_DIR / "cases"
EXERCISES_DIR = CASES_DIR / "exercises"
CHAIN_CASES_DIR = CASES_DIR / "chain"
RESULTS_JSON = RUNS_DIR / "results.json"

# The same artifact as a REPO-RELATIVE string, because `harness/delta.py` reads it out of git
# (`git show <rev>:<path>`) rather than off the disk, and git speaks repo-relative paths only.
RESULTS_REPO_REL = RESULTS_JSON.relative_to(REPO_ROOT).as_posix()

# ⚠ AND THE SAME ARTIFACT AT ITS PRE-ADOPTION PATH. `delta.py` reads a COMMITTED REVISION, so it
# must be able to name where the file lived AT THAT REVISION -- before the adoption commit it
# existed only under `proposals/`, and naming one path alone would make `delta.py <any earlier
# rev>` a hard refusal (this lane's declared `G11` carrier). It lives here, beside its sibling,
# which is where a second path for one artifact belongs.
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
# `governance_spine.yaml` declares the 13-seat generic ladder, read by `harness/governance_spine.py`.
# A local `Path(__file__).resolve().parents[1]` there would be a SECOND anchor in the package
# whose whole point is to have one. The invariant that catches it is this module's own --
# narrower than a bare grep for `__file__` (see the module docstring above): this module owns
# every path to a registry the package loads.
GOVERNANCE_SPINE_YAML = PACKAGE_DIR / "governance_spine.yaml"
# `offices.yaml` -- the governance ladder's titles and the authored seats. Anchored here for the
# same reason `GOVERNANCE_SPINE_YAML` is: one path owner, never a local `__file__` a house move rots.
OFFICES_YAML = PACKAGE_DIR / "offices.yaml"
# `arrangements.yaml` -- PROC-A, `21_RECONCILIATION.md` PHASE 2 step 6 /
# `03_PARAMETERS.md` PART D: THE CLOSED SET of proceeding shapes (`ID-12` -- "changing one is a
# data edit"), read through `data/arrangements.py`, the ONE loader. Anchored here for the same
# reason every sibling registry above is: one path owner, never a local `__file__`.
ARRANGEMENTS_YAML = PACKAGE_DIR / "arrangements.yaml"
# `cohorts.yaml` -- SUBSISTENCE IS TERRITORIAL (`ED-IN-0255`): the AUTHORED
# population synecdoches, one `weight > 1` `Person` per populated rung, read once at world-gen by
# `boot/realm.py::build_realm` beside the case-derived cast. Anchored here for the same
# reason every sibling registry above is: one path owner, never a local `__file__`.
COHORTS_YAML = PACKAGE_DIR / "cohorts.yaml"
# `goals.yaml` -- v9 IN-66 (ED-IN-0293 (8)): the AUTHORED goals of the organizations (faction, body,
# seat), each an OUGHT Proposition `boot/realm.py` mints at world-gen.
# Read through `data/goals.py`, the ONE loader. Anchored here for the same reason every sibling
# registry above is: one path owner, never a local `__file__`.
GOALS_YAML = PACKAGE_DIR / "goals.yaml"

# The degree sweep's two arm modules (plus their shared `sweep_core`), once imported by source in two
# tests, both retired (nothing reads this path now). Moved out of `proposals/2026-09-04-degree-sweep` to `engine/reference/degree-sweep/` so
# the blocking test suite depends on no unratified tree (ED-IN-0231 precedent); the measurement
# record (runs/, README.md, EXECUTION_PLAN.md, the other arms) stays in the proposal.
DEGREE_SWEEP_DIR = ENGINE_DIR / "reference" / "degree-sweep"

# ---------------------------------------------------------------------------
# THE REPOSITORY. The personal-combat module is NOT anchored here: it is the package `modules.combat`,
# reached by the composition rows `combat.fight` and `combat.duel_terms` (seam/wrappers/combat.py).
# ---------------------------------------------------------------------------
SYSTEMS_DIR = REPO_ROOT / "systems"
# The world map: `provinces:` (territories, their `anchor`s), `terrain:` polygons and `water:`.
# CANON, not this package's own. Read at world-gen by `boot/realm.py` and, for the battle
# field, by `data/geography.py`, which hands it to the `mass_battle` module on its input record --
# the module does not name the file.
GEOGRAPHY_YAML = SYSTEMS_DIR / "settlements" / "valoria_geography_v30.yaml"
REFERENCES_DIR = REPO_ROOT / "references"
MODULE_CONTRACTS_YAML = REFERENCES_DIR / "module_contracts.yaml"
CLAUDE_MD = REPO_ROOT / "CLAUDE.md"

# ⚠ THE CAST, AND IT IS CANON RATHER THAN THIS PACKAGE'S OWN. Character rows whose ids match
# `load_cases("NPC")` 1:1, carrying an authored `faction`, `role`, weighted `convictions` over the
# canonical roster, and a `title` on some. Named here because `files.py` is the one anchor; read
# through `data/cast.py`, which is the one reader.
NPC_REGISTRY_YAML = REFERENCES_DIR / "npc_registry.yaml"


def subsystem_sim_dir(name: str) -> Path:
    """`systems/<name>/sim/` — asked of the tree directly where a module contract carries no
    `sim_module:`. A function rather than a constant because the subsystem is not known here."""
    return SYSTEMS_DIR / name / "sim"


# ---------------------------------------------------------------------------
# THIS PACKAGE'S OWN SOURCES. Several guards read the instrument's source rather than importing it
# -- an AST walk over the write call sites, the roster scan, the margin-producer scan.
# ---------------------------------------------------------------------------
LOOP_DIR = PACKAGE_DIR / "loop"
DRIVER_PY = LOOP_DIR / "driver.py"


def loop_modules() -> tuple:
    """EVERY `.py` UNDER `loop/`, DISCOVERED. The season loop's source corpus.

    ⚠ **`DRIVER_PY` ALONE IS NOT THE LOOP (ED-IN-0206).** `04_CODE_ARCHITECTURE.md` §A.2:134 makes
    `loop/` *"driver + six steps"*, so the six step bodies live in their own modules, and a guard
    reading `files.DRIVER_PY` by fixed path would NARROW IN SILENCE over every write site the six
    steps took with them. The fix is the one `package_modules` states below: **compute the
    corpus, never list it.**

    A caller that scans this for a property must also pin a FLOOR or a SUPERSET, because a
    discovery that stops matching passes by finding nothing (`CLAUDE.md` §0.1 pt 2)."""
    return tuple(sorted(LOOP_DIR.rglob("*.py"),
                        key=lambda p: p.relative_to(LOOP_DIR).as_posix()))


def loop_source() -> str:
    """Every `loop/` module's text, concatenated in path order -- for the guards that grep the
    season loop for a literal rather than walking it."""
    return "\n".join(p.read_text(encoding="utf-8") for p in loop_modules())


def effects_modules() -> tuple:
    """EVERY `.py` under `loop/` NAMED `effects*`, DISCOVERED: the aggregator (`effects.py`) plus its
    flat siblings (`effects_shared.py`, `effects_governance.py`, ...), no package and no
    `__init__.py` barrel, matched by name rather than hand-listed.
    `data/verbs.py::_derive_openers_from_effects` is the one reader: every `@effect_for(...)`-
    decorated function and every `Tenure(...)` construction site it walks lives in one of the
    siblings, none in the aggregator itself (which only imports them), so a walk confined to
    `effects.py` alone finds nothing -- `loop_modules`'s lesson (`compute the corpus, never list
    it`) rather than hand-listing names that go stale the day another lands.

    A caller that scans this for a property must also pin a FLOOR or a SUPERSET, `loop_modules`'s
    own warning (`CLAUDE.md` §0.1 pt 2), checked at `_derive_openers_from_effects`'s own call site
    rather than here, since this function has no opinion on what a caller expects."""
    return tuple(p for p in loop_modules() if p.name.startswith("effects"))

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
    A caller must also assert a FLOOR on the length -- `04_CODE_ARCHITECTURE.md` §A.2 (the `decision/` row) names four
    members, so a scan that finds fewer has stopped matching and is passing vacuously (`CLAUDE.md`
    §0.1 pt 2)."""
    return tuple(sorted(DECISION_DIR.rglob("*.py"),
                        key=lambda p: p.relative_to(DECISION_DIR).as_posix()))
TEST_PY = TESTS_DIR / "test_season_shape.py"

PROBES_PY = HARNESS_DIR / "probes.py"
HEADLESS_PY = HARNESS_DIR / "headless.py"

# THE REALM BUILDER'S HOME (A-102): `boot/` builds the World and imports no instrument. It is not a
# step of the season, so `loop_modules()` does not list it; `package_modules()` finds it by `rglob`.
BOOT_DIR = PACKAGE_DIR / "boot"
REALM_PY = BOOT_DIR / "realm.py"
BOOT_CHOOSER_PY = BOOT_DIR / "chooser.py"


def package_modules() -> tuple:
    """EVERY `.py` IN THIS PACKAGE, DISCOVERED AND NEVER LISTED, sorted by package-relative path.

    ⚠ THE DISCOVERY IS THE POINT. Three guards need *every module in the instrument*: the roster
    scan, the need-taint scan and the margin-producer scan. A hardcoded filename tuple goes
    unscanned BY CONSTRUCTION when a module is added -- `G2` forbids the shape (a filename roster is
    a router), so the set is computed. Recursive, because the harness modules live one directory
    down and a flat `glob` would silently drop them."""
    return tuple(sorted(PACKAGE_DIR.rglob("*.py"),
                        key=lambda p: p.relative_to(PACKAGE_DIR).as_posix()))
