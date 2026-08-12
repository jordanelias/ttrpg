#!/usr/bin/env python3
"""
ci_common.py — shared helpers for the Valoria validators.

Single source of truth for "what changed" so every caller (GitHub Actions CI,
the local .githooks/pre-commit hook, the Claude Code PreToolUse runner, and the
unit tests) computes the changeset the same way. Previously get_changed_files()
was copy-pasted byte-for-byte into ci_co_file_checker.py and ci_editorial_checker.py;
this module collapses that duplication.

Modes:
  'ci'      — use GitHub Actions event context (push / pull_request); the
              authoritative path. Falls back to HEAD~1 then the empty tree.
  'staged'  — the index (git diff --cached): what a `git commit` is about to record.
              Used by the local pre-commit hook and the PreToolUse runner.
  'local'   — HEAD~1..HEAD (or empty tree for the first commit): ad-hoc local runs.

All functions are pure wrappers over `git`; no network, no PAT, no cache.

────────────────────────────────────────────────────────────────────────────────
THE SINGLE IMPORT SURFACE FOR `tools/` (plan step G7, ED-IN-0159 §8.3)
────────────────────────────────────────────────────────────────────────────────
Jordan's centralization directive (2026-08-11): *"We want to centralize as much
information as possible through injectable code, dictionaries, glossaries,
masters, etc such that we can maximize code uniformity and prevent duplication."*

`00_code_leanness.md` §1.2 measured what that directive targets in this tier:
the repo root re-derived **53 times in 15 distinct spellings**, YAML register
load **44 times**, the 9-lane roster **8 times**, token estimation **6**, the
PP/ED id regex **6**. Every one of those copies AGREES today, so collapsing them
is mechanical and the expected delta is *none* — which is what
`tests/valoria/test_ci_common_primitives.py` asserts, site by site.

WHY THE PRIMITIVES LAND HERE AND NOT IN `observability/obs_core.py`.
§8.3 names `ci_common` as the import surface, and the layering falls out of the
dependency graph rather than from taste: `obs_core` imports `build_decisions`,
which requires PyYAML and sweeps the corpus at import time. Several BLOCKING
gates (`validate_ed_citations`, `currency_consistency_check`,
`ci_workplan_pointer_check`) need only the 9-code tuple. Routing them through
`obs_core` to get it would make a stdlib-only gate depend on the observability
tier — a real regression bought for a tuple.

So the rule is: **dependency-free primitives are owned here and re-exported by
`obs_core`** (which keeps every one of its 9 consumers working unchanged), and
`obs_core`'s genuinely heavier primitives — the ledger reader, the JS-bundle
writer — are re-exported *lazily* from here via module `__getattr__`, so
`import ci_common` never pulls PyYAML in. One definition either way; the import
cost is paid only by callers that actually want the heavy thing.

This is NOT a fourth library. §1.1 measured `ci_common` at 11/118 and `obs_core`
at 9/118 adoption: the abstractions already exist and are correct. The work here
is adoption, not authorship.
"""
import ast
import glob
import os
import re
import subprocess
from pathlib import Path

# git's well-known empty-tree object — diff against this == "everything is new".
EMPTY_TREE = '4b825dc642cb6eb9a060e54bf8d69288fbee4904'

# ── one owner: the repository root ────────────────────────────────────────────
# Exposed in BOTH shapes because the tier is split between the two idioms and a
# call site should never have to convert. They are one definition — REPO_PATH is
# derived from REPO — so they cannot drift.
#   REPO      (str)  — the `os.path.join(REPO, ...)` / `subprocess(cwd=REPO)` idiom
#   REPO_PATH (Path) — the `REPO_PATH / 'references' / 'x.yaml'` idiom
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_PATH = Path(REPO)

# Pre-G7 private name, kept so nothing that already imported it breaks. New code
# uses REPO.
_REPO = REPO


def sim_reference_roots(repo_root=None):
    """Every directory the 1:1 Python sim reference now lives under. ONE OWNER (ED-IN-0087).

    `sim/` was RETIRED 2026-07-21 (ED-IN-0071 P4): the core moved to `engine/` and the
    per-subsystem sims to `systems/<subsystem>/sim/`. Two tools still walked the old flat tree, and
    because `os.walk` on a missing directory yields nothing rather than raising, both went SILENTLY
    HALF-DEAD — `ci_quantity_vocabulary_check` kept reporting its contract-side findings and looked
    like a working gate while its entire code-side scan returned zero files.

    That is the §0.1 point-5 pattern-defect signature (correct when written; broken because
    something else moved), so the answer is the standard shape: one owner for the question, every
    site routed through it, and a guard that fails on recurrence
    (tests/valoria/test_sim_reference_roots.py). The glob is deliberate — a NEW subsystem gains its
    sim automatically, which is the property the hardcoded list never had.
    """
    root = repo_root or _REPO
    roots = [os.path.join(root, 'engine')]
    roots += sorted(glob.glob(os.path.join(root, 'systems', '*', 'sim')))
    return [p for p in roots if os.path.isdir(p)]


def sim_reference_prefixes(repo_root=None):
    """Like `sim_reference_roots()`, but as repo-relative path PREFIXES (POSIX '/'
    separators, trailing '/') for callers that filter a changed-file list or build a
    git-pathspec / `str.startswith()` scope tuple, rather than walking the filesystem.
    ONE OWNER (OI-53a, ED-IN-0097, 2026-07-29-code-shape-open-items plan §3 Wave 4 item 3).

    Three more sites were found still keyed on the retired `designs/`/`sim/` roots this way
    — `tools/audit_staleness.py`'s `scope_prefixes` tuples (git-log pathspecs),
    `tools/observability/build_decisions.py`'s `SWEEP_DIRS` (a directory-name list —
    already fully covered by its existing `systems`/`engine` entries, so no new prefix is
    needed there), and `tools/workplan_status.py`'s `RELEVANT_PREFIXES`
    (`str.startswith()` tuple). `sim_reference_roots()` itself returns absolute filesystem
    paths meant for `os.walk`, the wrong shape for any of the three — hence this sibling,
    not a re-derivation of the root list (CLAUDE.md §8: one rule, one home; this restates
    the SAME roots in the shape each caller needs).
    """
    root = repo_root or _REPO
    return tuple(sorted(
        os.path.relpath(p, root).replace(os.sep, '/') + '/'
        for p in sim_reference_roots(root)
    ))


def _git(args):
    """Run a git command, returning stdout on success and '' on failure.

    Decodes as UTF-8 explicitly (errors='replace'). This is REQUIRED on Windows:
    text=True would decode with the cp1252 locale, which fails on the UTF-8 bytes
    in the design corpus (em-dashes, minus signs) and silently yields stdout=None.
    The repo is UTF-8; CI (Linux) is UTF-8 too, so this is consistent everywhere.
    """
    r = subprocess.run(['git'] + args, capture_output=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '') if r.returncode == 0 else ''


def _has_parent():
    return bool(_git(['rev-parse', '--verify', '-q', 'HEAD~1']).strip())


def _diff_args(mode):
    """Return the git-diff revision args for `mode` (excluding 'diff' itself)."""
    if mode == 'staged':
        return ['--cached']
    if mode == 'local':
        return ['HEAD~1', 'HEAD'] if _has_parent() else [EMPTY_TREE, 'HEAD']

    # mode == 'ci'
    event = os.environ.get('GITHUB_EVENT_NAME', '')
    before = os.environ.get('GITHUB_EVENT_BEFORE', '')
    sha = os.environ.get('GITHUB_SHA', '')
    base = os.environ.get('GITHUB_BASE_REF', '')
    if event == 'push' and before and sha and before != '0' * 40:
        return [before, sha]
    if event == 'pull_request' and base:
        return [f'origin/{base}...HEAD']
    return ['HEAD~1', 'HEAD'] if _has_parent() else [EMPTY_TREE, 'HEAD']


def get_changed_files(mode='ci'):
    """Set of repo-relative paths changed in the given mode (added/modified/deleted)."""
    out = _git(['diff', '--name-only'] + _diff_args(mode))
    return {line for line in out.splitlines() if line.strip()}


def get_changed_files_filtered(mode='ci', diff_filter=None):
    """Like get_changed_files but with a git --diff-filter (e.g. 'd' to drop deletions)."""
    args = ['diff', '--name-only']
    if diff_filter:
        args.append(f'--diff-filter={diff_filter}')
    out = _git(args + _diff_args(mode))
    return {line for line in out.splitlines() if line.strip()}


def get_added_lines(mode='ci'):
    """
    Map {path: [added_line, ...]} containing only the ADDED ('+') lines of the diff.

    This is what makes the naming guard diff-aware: it inspects only newly-introduced
    text, so the ~28 files that legitimately contain the forbidden token (registries,
    tests, archives, the matcher itself) are never re-flagged for content they already had.
    """
    out = _git(['diff', '--unified=0', '--no-color'] + _diff_args(mode))
    result = {}
    current = None
    for line in out.splitlines():
        if line.startswith('+++ '):
            target = line[4:].strip()
            if target == '/dev/null':
                current = None
            else:
                current = target[2:] if target.startswith('b/') else target
                result.setdefault(current, [])
        elif line.startswith('+') and not line.startswith('+++') and current is not None:
            result[current].append(line[1:])
    return result


def get_removed_lines(mode='ci'):
    """Map {path: [removed_line, ...]} containing only the DELETED ('-') lines of the diff.

    The mirror of get_added_lines, and it exists because added lines alone cannot answer "did this
    changeset invalidate something?". Deleting a `# [canonical: ...]` citation leaves the constant
    it justified uncited without touching that constant's line — so an added-lines-only gate sees a
    diff with no `+` lines at all and reports clean over a newly-fabricated value
    (ci_sim_fabrication_check, ED-IN-0119). A guard that only looks at what arrived cannot see what
    left.
    """
    out = _git(['diff', '--unified=0', '--no-color'] + _diff_args(mode))
    result = {}
    current = None
    for line in out.splitlines():
        if line.startswith('--- '):
            continue  # the a/ header; the b/ header below establishes the path
        if line.startswith('+++ '):
            target = line[4:].strip()
            current = None if target == '/dev/null' else (
                target[2:] if target.startswith('b/') else target)
            if current is not None:
                result.setdefault(current, [])
        elif line.startswith('-') and current is not None:
            result[current].append(line[1:])
    return result


def read_text(path):
    """Read a working-tree file as UTF-8; return None if missing or undecodable."""
    try:
        with open(path, encoding='utf-8', errors='strict') as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError, UnicodeDecodeError):
        return None


def has_main_guard(tree):
    """True iff `tree` (an `ast.parse`d module) contains an
    `if __name__ == '__main__':` guard anywhere in its body — including the
    reversed operand order `if '__main__' == __name__:`. ONE OWNER (OI-52a,
    ED-IN-0097, 2026-07-29-code-shape-open-items plan §3 Wave 4 item 2).

    Moved here from `skills/valoria-vector-audit/scripts/structure_audit.py`
    (the AST-based, both-operand-order predicate — the stricter of two
    independent implementations found live: `tools/build_apparatus_registry.py`
    carried a second, regex-over-raw-source check that (a) matched only the
    conventional operand order and (b) had no defense against a comment or
    string literal that merely CONTAINS the guard text — a real false-positive
    class, not a hypothetical one (see `tests/valoria/test_ci_common.py`).
    `structure_audit.py` adopts this function too this same wave (a
    same-name-divergent-value duplicate is the exact defect class CLAUDE.md §8
    exists to prevent); `build_apparatus_registry.py`'s `analyze_py()` now
    calls this instead of its old regex.

    AST-based, not text-based: it only recognizes a real `if` statement whose
    test is `__name__ == '__main__'` or `'__main__' == __name__` — a comment or
    a string literal containing that text is never in the parsed statement
    tree, so it cannot false-positive on either.
    """
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        test = node.test
        if not (isinstance(test, ast.Compare) and len(test.ops) == 1
                and isinstance(test.ops[0], ast.Eq) and len(test.comparators) == 1):
            continue
        left, right = test.left, test.comparators[0]

        def _is_dunder_name(n):
            return isinstance(n, ast.Name) and n.id == '__name__'

        def _is_main_const(n):
            return isinstance(n, ast.Constant) and n.value == '__main__'

        if (_is_dunder_name(left) and _is_main_const(right)) or \
           (_is_dunder_name(right) and _is_main_const(left)):
            return True
    return False


# ══════════════════════════════════════════════════════════════════════════════
# G7 — the mechanical one-owner primitives (ED-IN-0159 §8.1)
#
# Every constant and function below replaces a set of copies that AGREE today.
# The expected delta of each migration is therefore *none*, and any behaviour
# change is a bug rather than a finding — which is exactly what
# tests/valoria/test_ci_common_primitives.py exists to establish, by recomputing
# each primitive the way its call sites used to and asserting equality.
# ══════════════════════════════════════════════════════════════════════════════

# ── the 9-lane roster (§1.3b: 8 sites, agreeing today, diverged before) ───────
# The lane tag makes cross-lane ED collision impossible by construction
# (CLAUDE.md §4). Verbatim copies previously lived in ci_workplan_pointer_check,
# broken_dependency_checker, handoff_atomize, validate_ed_citations,
# currency_consistency_check and obs_core, plus two derived spellings.
#
# The reason this is a defect and not merely repetition is on the record:
# obs_core's own header notes that one of the prior rosters silently OMITTED
# 'GO', undercounting a whole lane. Adding a tenth lane used to be 8 edits.
LANE_CODES: tuple = ("MB", "PC", "FI", "SC", "FA", "WR", "IN", "GO", "SE")

# Ledger filenames use the lowercase code: registers/editorial_ledger_<xx>.jsonl
LEDGER_LANE_CODES: tuple = tuple(c.lower() for c in LANE_CODES)


# ── id regexes (§1.2: 6 sites) ───────────────────────────────────────────────
# Exposed as PATTERN STRINGS, not only as compiled objects, because half the
# call sites embed them in a larger expression (`-\s+id:\s+PP-(\d+)`) and a
# compiled object cannot be composed. The compiled forms below cover the rest.
#
# Both ED formats are permanently valid (CLAUDE.md §4): the flat ED-NNNN
# sequence is FROZEN at ED-1096 but never retired, and all new items are
# lane-tagged ED-<LANE>-NNNN. A pattern that matches only one of the two is the
# recurring bug here — `index_gen.py:129` documents its own r'ED-\d+' as
# predating the lane format and never updated.
PP_ID_PAT = r'PP-\d+'

# ── ONLY ONE ID PATTERN IS EXPORTED, and that is the honest state ────────────
# This block first shipped SEVEN names — ED_FLAT_ID_PAT, ED_LANE_ID_PAT,
# ED_ID_PAT, ANY_ID_PAT and compiled PP_ID_RE / ED_ID_RE / ANY_ID_RE — labelled
# "ONE OWNER (§1.2: 6 sites)". An adversarial pass established that NONE of them
# had a single caller: the six copies they claimed to own were all still live,
# including two in `ci_vetting_check`, a BLOCKING gate that did not import
# ci_common at all. That is ED-IN-0149's build-then-disconnect defect, shipped
# inside the commit that cites it — and CLAUDE.md §8's named anti-pattern, "a
# single-owner comment asserting a property the tree lacks is worse than no
# comment", re-earned one section after §2.3 withdrew the same charge against
# `pathres`.
#
# `PP_ID_PAT` survives because its call sites were migrated in the same commit:
# `ci_vetting_check.py` (both patterns) and `export_sim_params.py`. It is exported
# as a PATTERN STRING, not a compiled object, because every one of those sites
# embeds it in a larger expression (`-\s+id:\s+` + PP_ID_PAT) — which a compiled
# object cannot do, and which is why a compiled export had no takers.
#
# THE ED PATTERNS ARE DELIBERATELY NOT EXPORTED. The two live ED readers must NOT
# be collapsed onto a shared pattern, and that is a finding rather than an
# omission: `validate_ed_citations.py:304` matches flat `ED-\d+` ONLY BY DESIGN
# (the archives it salvages predate the lane-tagged format), and
# `ci_claim_provenance_check.py:84` parses `^(ED-[A-Z]+)-(\d+)$` into two capture
# groups. They mean different things. Giving them one owner would be §8.2's
# "merging two concepts that share a name", which the mission forbids.
#
# `tests/valoria/test_ci_common_primitives.py::test_every_ci_common_primitive_has_a_caller`
# is the guard: a primitive exported here with no consumer fails the suite.


# Sentinel: "no default was given". Distinguishes load_yaml(p) — which must RAISE
# on a missing file, exactly as the bare `open()` it replaced did — from
# load_yaml(p, None), which asks for None. Without it the helper silently absorbed
# a missing input, which is the failure `tests/valoria/test_engine_atlas.py::
# test_missing_input_is_reported_not_silently_absorbed` exists to prevent, and
# which it CAUGHT on this migration.
_RAISE = object()


# ── the `## Status:` reader (plan G8 — the one intended behaviour change) ────
# ONE OWNER for BOTH axes of the question, because the finding conflated them and
# only one of the two was doing the damage:
#
#   axis 1, THE REGEX  — how many hashes, how much whitespace, bold or not
#   axis 2, THE WINDOW — head-only or whole-document
#
# 00_code_leanness.md §1.3a measured axis 1 by running five regexes over whole
# documents. Three of the five are not used that way: ci_generation_consistency
# reads the first 12 lines, dashboard_data read the first 4,000 CHARACTERS,
# build_identifier_census the whole file. Measured properly, axis 1 is nearly a
# non-event — ci_generation_consistency's regex is *equivalent* to this one (206
# docs, 0 gained, 0 lost) and build_incompleteness composes on it with no change
# (25 -> 25). Axis 2 is where the behaviour lives, and it is where the false
# positives come from: over a WHOLE document this pattern matches a schema
# template (`  status : IN_FORCE | VETOED | SUPERSEDED`) and a legend
# (`## Status: NOT STARTED / IN PROGRESS / COMPLETE`).
#
# ⚠ CORRECTED 2026-08-12 (ED-IN-0164). This comment first claimed 80 was "the
# window dashboard_data already used". It was not — dashboard_data read 4,000
# CHARACTERS, a per-caller literal, so after G8 four different windows still
# existed and the one thing the plan calls "where the behaviour lives" had no
# owner. An adversarial pass caught it. dashboard_data now uses
# STATUS_HEAD_LINES; the delta on its corpus was 114 -> 114, i.e. the divergence
# was latent rather than firing, and unifying the window closes it before it does.
STATUS_RE = re.compile(r'^#{0,3}\s*Status\s*:\s*(.+)$', re.I)

# A document's status is its HEAD's status. Chosen BY MEASUREMENT against the
# SUPERSEDED classification that consumes it: at 12 lines two genuinely-superseded
# docs stop being recognised, at the whole document a schema template starts being
# read as one, and 40 and 80 give the same answer — that stability is what the
# choice rests on.
STATUS_HEAD_LINES = 80


def first_status(text, head_lines=None):
    """The first `## Status:` value in `text`, or None.

    `head_lines=None` scans everything it is given — the behaviour obs_core's
    `first_status` has always had, since its callers slice the head themselves.
    Pass an integer to apply the window here instead.

    Lines are stripped before matching, so leading indentation is tolerated; that
    was already true of every reader this replaces.
    """
    lines = text.splitlines()
    if head_lines is not None:
        lines = lines[:head_lines]
    for line in lines:
        m = STATUS_RE.match(line.strip())
        if m:
            return m.group(1).strip()
    return None


def doc_status(text):
    """A document's status: `first_status` over its head. The shape a caller
    asking "what is this doc's status" wants, with the window not left to it."""
    return first_status(text, head_lines=STATUS_HEAD_LINES)


def tokens(text) -> int:
    """The repo's token estimate: characters // 4. ONE OWNER (§1.2, 6 sites).

    This is the number every size cap in the repo is denominated in —
    `references/atomization_rules.yaml`, `ci_register_size_check`,
    `compliance_check`, `ci_hooks_verifier`, `handoff_atomize` — so it is not a
    convenience wrapper but the definition the caps mean. Two gates checking the
    same file against caps computed by two different estimators is a class of
    disagreement this repo has already paid for once (ED-IN-0097).

    Six inline `len(x) // 4` sites survive, ALL of them in atomizer /
    doc_index_gen / index_gen, which plan step G2 retires — migrating a module
    scheduled for retirement is work done twice. `test_inline_token_estimation_is
    _confined_to_the_modules_being_retired` pins that residue, so a new inline
    estimator anywhere else fails and this exemption cannot outlive its retirement.

    Accepts str or bytes; `None` counts as 0 so a missing file is not a crash in
    a size sweep.
    """
    if text is None:
        return 0
    return len(text) // 4


def load_yaml(path, default=_RAISE):
    """`yaml.safe_load` a file, returning `default` when it is missing or empty.

    THE INTENDED OWNER OF YAML REGISTER LOAD — **not yet the only one**, and this
    docstring says so because the alternative has a name in this repo. It first
    read "ONE OWNER (§1.2, 44 sites)" while having ZERO CALLERS, which is CLAUDE.md
    §8's named anti-pattern ("a single-owner comment asserting a property the tree
    lacks is worse than no comment") and the exact charge `00_code_leanness.md`
    §2.3 withdrew against `pathres` once `pathres` started stating its own status
    honestly. An adversarial pass re-earned it here within one commit.

    Migrated: 12 call sites, both idioms — `yaml.safe_load(open(x))` and
    `with open(x) as f: y = yaml.safe_load(f)`. **52 bare `yaml.safe_load` calls
    remain in `tools/`**, each of which does something this helper does not (loads
    a stream, a string, a StringIO, or wants the exception on a missing file).
    `tests/valoria/test_ci_common_primitives.py` pins that count, so it can only
    go down.

    PyYAML is imported INSIDE the function, deliberately. `ci_common` is
    imported by stdlib-only blocking gates, and a module-level `import yaml`
    would make PyYAML a hard requirement of every one of them for the benefit of
    the subset that reads registers.

    The `default` contract is the one the call sites already had: a register
    that does not exist reads as empty rather than raising, because several
    gates legitimately run against trees where an optional register is absent
    (a lane file exists only once that lane has allocated an ED — CLAUDE.md §4).
    Call sites that WANT the exception should keep calling yaml.safe_load
    directly; this helper does not take that choice away from them.
    """
    import yaml
    try:
        with open(path, encoding='utf-8') as fh:
            data = yaml.safe_load(fh)
    except FileNotFoundError:
        if default is _RAISE:
            raise
        return default
    if data is None:
        return None if default is _RAISE else default
    return data


# `load_register()` WAS HERE AND IS NOT SHIPPED (ED-IN-0164). It resolved a name
# against registers/ then references/, and it had ZERO callers — which makes it the
# same defect as the id_reservations reader refused below. Caught by an adversarial
# pass that noticed this file refusing one speculative helper while shipping two
# more fifty lines above it. `load_yaml` survives only because call sites were
# migrated onto it in the same commit; had they not been, it would have gone too.


# ── NOT provided: an `id_reservations` reader ────────────────────────────────
# The plan's §8.1 table lists "id_reservations read | 8 | 1 | removed 7". Executing
# it found nothing to collapse: measured across the whole tree
# (`grep -rn id_reservations --include=*.py . | grep -E 'safe_load|yaml.load'`),
# **zero** modules load that file. The census's detector for this row is the bare
# pattern `id_reservations`, so its 8 are mostly MENTIONS — prose comments
# explaining the ID rules, a `ci_register_size_check` size-cap row keyed by
# path string, a `build_decisions` source tuple.
#
# ⚠ CORRECTED 2026-08-12 by an adversarial pass (ED-IN-0164). This comment used to
# end "Nothing parses it." THAT IS FALSE, and it was the only justification given
# for striking a plan row. `tools/currency_consistency_check.py:280` reads the file
# and genuinely PARSES it — four fields extracted by regex (`verified_live_max.ED`,
# per-block `next_free`, `lane_ids.<lane>.next_free`) driving a BLOCKING currency
# gate. `duplication_census.py` reads it too.
#
# The true statement is narrower and still sufficient: nothing loads it with
# PyYAML, and a text-plus-regex reader is not served by `load_yaml`. The decision
# now rests on what the tree does rather than on an overstatement.
#
# Shipping a `read_id_reservations()` here anyway would have added an abstraction
# with no caller — the precise defect ED-IN-0149 named and the consolidation sweep
# ranked (build-then-disconnect). Callers that need the file can use load_yaml();
# when the first real reader appears, THAT is the moment to give it an owner.
# Recorded rather than silently skipped: §0.1 point 3.


# ── lazy re-exports of obs_core's heavier primitives ──────────────────────────
# PEP 562 module __getattr__. `ci_common.read_ledger_entries(...)` works and is
# the single import surface §8.3 asks for, but `import ci_common` still costs
# nothing: obs_core (and through it build_decisions, and through that PyYAML) is
# imported only if one of these names is actually touched.
_LAZY_FROM_OBS_CORE = (
    'read_ledger_entries',      # registers/editorial_ledger*.jsonl, normalized
    'open_ledger_entries',
    'is_unratified_status',
    'text_needs_jordan',
    'write_js_bundle',
    'infer_lane',
    'LANE_NAMES',
    'DECISION_MARKERS',
)


def __getattr__(name):
    if name in _LAZY_FROM_OBS_CORE:
        import sys
        obs_dir = os.path.join(REPO, 'tools', 'observability')
        if obs_dir not in sys.path:
            sys.path.insert(0, obs_dir)
        import obs_core
        return getattr(obs_core, name)
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
