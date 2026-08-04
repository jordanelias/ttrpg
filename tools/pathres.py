#!/usr/bin/env python3
"""THE path-reference owner: extract path tokens, resolve them through the alias map, once.

WHY THIS EXISTS — three confirmed instances of ONE defect, each of which looked plausible.

A path-shaped string in this corpus is a *fuzzy pointer*: it can be relocated (the restructure
alias map), constructed from segments at runtime, and it is substring-ambiguous. Every naive
comparison against one has failed, silently, in one of three directions:

1. **Unanchored substring OVER-match (ED-IN-0133).** A scan for `audit/[a-z0-9./_-]+\\.py`
   reported a phantom `audit/scripts/` directory. The regex matched *inside*
   `skills/valoria-vector-audit/scripts/…`. A nonexistent path was reported as a finding.
2. **Split/constructed path UNDER-match (ED-IN-0128).** `gen_sigma_parity_goldens.py` builds
   `os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py')`. A literal scan
   for `audit/` *cannot* see it. A deletion planner reported the file as unread while a kept CI
   test depended on it; the AST scan added in response found 45 readers the substring scan missed.
3. **Alias/relocation UNDER-match (2026-08-04).** A census of provenance citations reported **0**
   pointing at evacuating docs. True answer: **58 of 112**. The citations say `params/core.md`,
   which reaches `engine/params/core.md` only through the alias map. The single largest affected
   group scored zero.

WHY AN OWNER RATHER THAN A FOURTH FIX. Measurement before writing this: the alias ledger already
had **four** independent parsers — `broken_dependency_checker` (single-hop, longest-dir-prefix),
`ci_claude_workflow_paths` (chained, existence-checked, glob-aware — the richest, and the one this
module is extracted from), and `skills/valoria-vector-audit/scripts/{vector_audit,workbench}.py`
(each re-parsing the table locally). The anchored token grammar existed three more times. That is
CLAUDE.md §8's "every rule lives once" violated four deep, and it is why the same defect keeps
arriving: there was no one place where the lesson could be applied.

So this module is NET REMOVAL, not new machinery: four parsers, two resolvers and three roster
copies come out as it lands.

WHY `Resolution` IS AN OBJECT AND NOT A STRING. All three failures are the same *silent
substitution of the question*: "does this string occur" for "does this file exist"; "does this
substring occur" for "is this file read"; "does this literal path exist" for "does this reference
resolve". A returned string lets that substitution stay invisible. `Resolution` has no
path-yielding `__str__` and comparing it to a raw path is `False` by type, so the caller must say
which question they meant — `r.live_path == x` ("the post-alias file") or `r.status == 'LIVE'`
("literal existence IS my semantics", which is correct at some sites: `currency_consistency_check`
detects drift precisely by NOT resolving). `hops` carries the provenance, so a census can report
"58 of 112, all via the `params/` row" instead of a bare number.

Stdlib only, deliberately: the `integrity` CI job installs no PyYAML and
`broken_dependency_checker` must be able to import this.

CLI — and it matters more than it looks. Two of the three instances were UNCOMMITTED scratch
scans, and no CI guard can fail code that never enters the tree. The only real lever on that class
is making the correct scan cheaper than `grep`:

    python3 tools/pathres.py resolve params/core.md
    python3 tools/pathres.py scan tools/ --json
"""
from __future__ import annotations

import ast
import dataclasses
import glob as _glob
import json
import os
import re
import sys
from typing import Iterator

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER_REL = os.path.join('references', 'restructure_ledger.md')

# THE tree roster. Previously duplicated in ci_claude_workflow_paths.TREES,
# test_tool_input_paths_resolve.TREES and broken_dependency_checker.extract_file_refs.
# `designs/` and `sim/` are retired and included DELIBERATELY — a reference to them is the
# failure a scan looks for, not an omission.
TREES: tuple[str, ...] = (
    "designs", "sim", "systems", "engine", "references", "params", "tests",
    "registers", "canon", "audit", "arcs", "godot", "tools", "skills", "proposals",
    "workplans", "deprecated", "dashboard", "research",
)

KNOWN_EXT: tuple[str, ...] = (
    ".md", ".py", ".yaml", ".yml", ".json", ".jsonl", ".js", ".gd", ".txt", ".html",
)

# The MOVES table of references/restructure_ledger.md: | `old` | `new` | STATUS |
_ROW_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", re.M)

MAX_ALIAS_HOPS = 6

LIVE, ALIASED, DEAD = 'LIVE', 'ALIASED', 'DEAD'


@dataclasses.dataclass(frozen=True)
class Resolution:
    """What a path reference actually points at. Deliberately not a string — see the module docstring."""
    query: str
    status: str                       # LIVE | ALIASED | DEAD
    live_path: str | None             # existing repo-relative path; None iff DEAD
    hops: tuple[tuple[str, str], ...] = ()

    def __str__(self) -> str:
        # NOT the path. A path-yielding __str__ is how a Resolution silently becomes a string again
        # and the caller stops declaring which question they are asking.
        return f'<Resolution {self.status} {self.query!r} -> {self.live_path!r}>'

    def __bool__(self) -> bool:
        raise TypeError(
            'Resolution has no truth value: `if resolve(x):` hides which question you are asking. '
            "Write `if r.status != 'DEAD':` (does it point anywhere) or `if r.status == 'LIVE':` "
            '(is the literal path current — the right test when detecting drift).')

    def same_file(self, other: str, root: str = REPO) -> bool:
        """Do this reference and `other` name the same file AFTER alias resolution?"""
        if self.live_path is None:
            return False
        return self.live_path == resolve(other, root=root).live_path


# --------------------------------------------------------------------------------------------
# The alias map — SOLE PARSER of references/restructure_ledger.md
# --------------------------------------------------------------------------------------------
_MAP_CACHE: dict = {}


def load_alias_map(root: str = REPO) -> tuple[dict[str, str], list[tuple[str, str]]]:
    """(exact rows, dir-prefix rows sorted longest-first). Cached per root.

    Longest-prefix-first is load-bearing: one `designs/X/ -> systems/.../` pointer row must resolve
    every file moved under it, which is the convention the P4 restructure relies on.
    """
    if root in _MAP_CACHE:
        return _MAP_CACHE[root]
    path = os.path.join(root, LEDGER_REL)
    if not os.path.exists(path):
        result: tuple[dict, list] = ({}, [])
    else:
        with open(path, encoding='utf-8') as fh:
            rows = _ROW_RE.findall(fh.read())
        exact = {old: new for old, new in rows if not old.endswith('/')}
        prefix = sorted(((old, new) for old, new in rows if old.endswith('/')),
                        key=lambda pair: -len(pair[0]))
        result = (exact, prefix)
    _MAP_CACHE[root] = result
    return result


def resolve(ref: str, root: str = REPO, max_hops: int = MAX_ALIAS_HOPS) -> Resolution:
    """Resolve a repo-relative reference through the alias map to a file that exists.

    `max_hops=1` reproduces `broken_dependency_checker`'s historical single-hop behaviour exactly;
    the default chases chains (the ledger contains a real 2-hop chain:
    `references/params_core.md` -> `params/core.md` -> `engine/params/core.md`).
    """
    ref = ref.strip()
    if os.path.exists(os.path.join(root, ref)):
        return Resolution(ref, LIVE, ref, ())
    exact, prefix = load_alias_map(root)
    seen: set[str] = set()
    hops: list[tuple[str, str]] = []
    current = ref
    for _ in range(max_hops):
        if current in seen:
            return Resolution(ref, DEAD, None, tuple(hops))   # cycle in the ledger
        seen.add(current)
        nxt = None
        if current in exact:
            nxt = exact[current]
            hops.append((current, nxt))
        else:
            for old, new in prefix:
                if current.startswith(old):
                    nxt = new + current[len(old):]
                    hops.append((old, new))
                    break
        if nxt is None:
            return Resolution(ref, DEAD, None, tuple(hops))
        if os.path.exists(os.path.join(root, nxt)):
            return Resolution(ref, ALIASED, nxt, tuple(hops))
        current = nxt
    return Resolution(ref, DEAD, None, tuple(hops))


def resolve_glob(pattern: str, root: str = REPO) -> Resolution:
    """Alias-resolve a GLOB. `resolve()` cannot be reused: it tests os.path.exists, always False
    for a pattern, so a legitimate glob (`registers/editorial_ledger*.jsonl`) reports a false DEAD.
    Rewrite through the dir-prefix rows and re-glob instead."""
    if _glob.glob(os.path.join(root, pattern)):
        return Resolution(pattern, LIVE, pattern, ())
    _exact, prefix = load_alias_map(root)
    for old, new in prefix:
        if pattern.startswith(old):
            candidate = new + pattern[len(old):]
            if _glob.glob(os.path.join(root, candidate)):
                return Resolution(pattern, ALIASED, candidate, ((old, new),))
    return Resolution(pattern, DEAD, None, ())


# --------------------------------------------------------------------------------------------
# Extraction — the ANCHORED grammar (the ED-IN-0133 fix, owned once)
# --------------------------------------------------------------------------------------------
def path_token_re(trees: tuple[str, ...] = TREES,
                  exts: tuple[str, ...] = KNOWN_EXT) -> re.Pattern:
    """The one anchored path-token pattern.

    THE LEFT LOOKBEHIND IS THE WHOLE POINT. Without `(?<![\\w/.-])`, `audit/` matches inside
    `skills/valoria-vector-audit/scripts/` and the scan invents a directory that does not exist
    (ED-IN-0133). `*` sits inside the character class so a glob is captured whole — truncating at
    the `*` yields a path that never exists and reports a false DEAD.
    """
    _ = exts  # extension filtering is `is_dependency`'s job; kept in the signature for callers
    return re.compile(r'(?<![\w/.-])(?:%s)/[A-Za-z0-9_.*/-]+' % '|'.join(trees))


@dataclasses.dataclass(frozen=True)
class PathRef:
    raw: str
    line_no: int
    line: str


def iter_path_refs(text: str, trees: tuple[str, ...] = TREES) -> Iterator[PathRef]:
    """Every anchored path token in `text`, with the line it came from."""
    pat = path_token_re(trees)
    for i, line in enumerate(text.splitlines(), 1):
        for m in pat.finditer(line):
            yield PathRef(m.group(0), i, line)


def py_joined_paths(source: str) -> list[str]:
    """Repo-relative paths a Python source builds OUT OF SEGMENTS.

    THE FALSE NEGATIVE THIS EXISTS FOR (ED-IN-0128), and it was a real one:

        os.path.join(REPO_ROOT, 'audit', '2026-06-03-contest-groundup', 'engine.py')

    contains no `audit/` substring, so a text scan reported that file as having no readers while a
    kept tool loaded it to regenerate a committed golden a kept CI test asserts on. A substring
    scan cannot see a split path — not "did not", *cannot*.

    Non-constant segments (variables) are SKIPPED rather than guessed: guessing is the fabrication
    this repo forbids, and a skipped segment yields a shorter path that still matches on its root,
    which is the level a slice decision cares about. Extracted verbatim from
    `evacuation_plan.const_segments`.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    roots = set(TREES)
    out: list[str] = []

    def const_segments(node):
        segs = []
        if isinstance(node, ast.Call):
            f = node.func
            name = getattr(f, 'attr', None) or getattr(f, 'id', None)
            if name in ('join', 'Path'):
                for a in node.args:
                    segs.extend(const_segments(a))
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            segs.extend(const_segments(node.left))
            segs.extend(const_segments(node.right))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            segs.append(node.value)
        return segs

    for node in ast.walk(tree):
        if not isinstance(node, (ast.Call, ast.BinOp)):
            continue
        segs = [s for s in const_segments(node) if s and '/' not in s and s not in ('.', '..')]
        if len(segs) < 2:
            continue
        for i, s in enumerate(segs):
            if s in roots and i + 1 < len(segs):
                out.append('/'.join(segs[i:]))
                break
    return sorted(set(out))


# --------------------------------------------------------------------------------------------
# I/O tracing — because a REFERENCE is not a DEPENDENCY
# --------------------------------------------------------------------------------------------
# Jordan, 2026-08-04: "you need to trace pipelines or I/O for stuff."
#
# Everything above answers "does this string point at a real file". That is the wrong question for
# a deletion. `evacuation_plan.readers()` calls a kept file a "blocking reader" if the evacuating
# path appears ANYWHERE in it — which is why the engine/params slice reported 30 blocking readers
# that are mostly mentions in comments and docstrings. A mention is not a dependency; an `open()`
# is. Conflating them inflates the blocking count until nobody reads it, which is how a slice
# report loses its ability to stop a bad deletion.
#
# So: classify each reconstructed path by what the code DOES with it. read/write/scan/delete are
# pipeline edges; everything else is prose. Nothing here guesses — a non-constant segment is
# skipped, exactly as in `py_joined_paths`.
#
# Nothing in the tree does this today: `build_apparatus_registry` records a tool's DECLARED output
# destination and `structure_audit` graphs MODULE IMPORTS. Neither sees file-level I/O.
_READ_FUNCS = {'read_text', 'read_bytes', 'load', 'safe_load', 'read_csv'}
_SCAN_FUNCS = {'glob', 'iglob', 'walk', 'rglob', 'listdir', 'scandir'}
_DEL_FUNCS = {'remove', 'unlink', 'rmdir', 'removedirs', 'rmtree'}
_WRITE_FUNCS = {'write_text', 'write_bytes', 'mkdir', 'makedirs'}


@dataclasses.dataclass(frozen=True)
class IORef:
    path: str          # reconstructed repo-relative path (constant segments only)
    mode: str          # read | write | scan | delete | mention
    line: int


def py_path_io(source: str) -> list[IORef]:
    """What a Python source READS, WRITES, SCANS or DELETES — not merely mentions.

    `open(p)` vs `open(p, 'w')` is the distinction that matters for a deletion plan: the first
    breaks when the file goes, the second recreates it. A bare string in a comment does neither.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    roots = set(TREES)

    def const_segments(node):
        segs = []
        if isinstance(node, ast.Call):
            f = node.func
            name = getattr(f, 'attr', None) or getattr(f, 'id', None)
            if name in ('join', 'Path'):
                for a in node.args:
                    segs.extend(const_segments(a))
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            segs.extend(const_segments(node.left))
            segs.extend(const_segments(node.right))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            segs.append(node.value)
        return segs

    # MODULE-LEVEL CONSTANT ENVIRONMENT. Without this the tracer sees 24 paths in the whole repo,
    # because the dominant idiom is `LEDGER = os.path.join(ROOT, "references", "x.md")` followed by
    # `open(LEDGER)` — the I/O site holds a Name, not a path. Missing those would be the SAME
    # under-report-by-indirection this module exists to end, one level up: a tracer that only sees
    # inlined literals is a substring scan wearing an AST.
    # Deliberately one level and constants only — no dataflow analysis, no guessing. A name that
    # cannot be resolved to a constant path is skipped, exactly like a non-constant join segment.
    env: dict[str, str] = {}

    def as_repo_path(node) -> str | None:
        """A repo-relative path from a constant, a bound name, a join, or a `/`-chain."""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            v = node.value
            return v if v.split('/')[0] in roots else None
        if isinstance(node, ast.Name):
            return env.get(node.id)
        segs = [s for s in const_segments(node) if s and '/' not in s and s not in ('.', '..')]
        for i, s in enumerate(segs):
            if s in roots and i + 1 < len(segs):
                return '/'.join(segs[i:])
        # a join whose first constant already carries slashes: os.path.join(REPO, 'engine/params')
        flat = [s for s in const_segments(node) if s]
        for s in flat:
            if s.split('/')[0] in roots and '/' in s:
                return s
        return None

    # populate the environment first: module-level NAME = <path expr>, in source order so a later
    # constant may be built from an earlier one.
    for stmt in tree.body:
        targets, value = [], None
        if isinstance(stmt, ast.Assign):
            targets, value = stmt.targets, stmt.value
        elif isinstance(stmt, ast.AnnAssign) and stmt.value is not None:
            targets, value = [stmt.target], stmt.value
        if value is None:
            continue
        p = as_repo_path(value)
        if p:
            for t in targets:
                name = getattr(t, 'id', None)
                if name:
                    env[name] = p

    out: list[IORef] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not node.args:
            continue
        fname = getattr(node.func, 'attr', None) or getattr(node.func, 'id', None)
        target = as_repo_path(node.args[0])
        if fname == 'Path' and len(node.args) == 1:
            continue                      # Path(x) alone is construction, not I/O
        if target is None:
            # Path(...).read_text() — the path is on the receiver, not in the args
            recv = getattr(node.func, 'value', None)
            if recv is not None and fname in (_READ_FUNCS | _WRITE_FUNCS | _SCAN_FUNCS):
                target = as_repo_path(recv)
            if target is None:
                continue
        if fname == 'open':
            mode = 'read'
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                m = str(node.args[1].value)
                mode = 'write' if any(c in m for c in 'wax') else 'read'
            for kw in node.keywords:
                if kw.arg == 'mode' and isinstance(kw.value, ast.Constant):
                    mode = 'write' if any(c in str(kw.value.value) for c in 'wax') else 'read'
            out.append(IORef(target, mode, node.lineno))
        elif fname in _DEL_FUNCS:
            out.append(IORef(target, 'delete', node.lineno))
        elif fname in _SCAN_FUNCS:
            out.append(IORef(target, 'scan', node.lineno))
        elif fname in _WRITE_FUNCS:
            out.append(IORef(target, 'write', node.lineno))
        elif fname in _READ_FUNCS:
            out.append(IORef(target, 'read', node.lineno))
    return out


# --------------------------------------------------------------------------------------------
# CLI — the mitigation for the class no CI check can reach (uncommitted scratch scans)
# --------------------------------------------------------------------------------------------
def _cli(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__.strip().splitlines()[0])
        print('usage: pathres.py resolve <ref>... | pathres.py scan <file-or-dir> [--json]')
        return 0
    cmd, rest = argv[0], argv[1:]
    as_json = '--json' in rest
    rest = [a for a in rest if a != '--json']

    if cmd == 'resolve':
        rows = [resolve(r) for r in rest]
        if as_json:
            print(json.dumps([dataclasses.asdict(r) for r in rows], indent=1))
        else:
            for r in rows:
                via = f'  via {" -> ".join(a + "=>" + b for a, b in r.hops)}' if r.hops else ''
                print(f'  {r.status:8s} {r.query}  ->  {r.live_path}{via}')
        return 0 if all(r.status != DEAD for r in rows) else 1

    if cmd == 'scan':
        targets = []
        for t in rest:
            full = os.path.join(REPO, t) if not os.path.isabs(t) else t
            if os.path.isdir(full):
                for dirpath, _d, names in os.walk(full):
                    targets += [os.path.join(dirpath, n) for n in names
                                if n.endswith(KNOWN_EXT)]
            elif os.path.isfile(full):
                targets.append(full)
        seen: dict[str, Resolution] = {}
        where: dict[str, list[str]] = {}
        for full in targets:
            try:
                with open(full, encoding='utf-8', errors='ignore') as fh:
                    text = fh.read()
            except OSError:
                continue
            rel_src = os.path.relpath(full, REPO).replace(os.sep, '/')
            for ref in iter_path_refs(text):
                if ref.raw not in seen:
                    seen[ref.raw] = resolve(ref.raw)
                where.setdefault(ref.raw, []).append(f'{rel_src}:{ref.line_no}')
            for built in py_joined_paths(text) if full.endswith('.py') else []:
                if built not in seen:
                    seen[built] = resolve(built)
                where.setdefault(built, []).append(f'{rel_src} (constructed)')
        counts = {LIVE: 0, ALIASED: 0, DEAD: 0}
        for r in seen.values():
            counts[r.status] += 1
        if as_json:
            print(json.dumps({'counts': counts,
                              'refs': {k: dataclasses.asdict(v) for k, v in sorted(seen.items())},
                              'sites': where}, indent=1, sort_keys=True))
        else:
            print(f'{len(targets)} file(s), {len(seen)} distinct reference(s): '
                  f'{counts[LIVE]} LIVE, {counts[ALIASED]} ALIASED, {counts[DEAD]} DEAD')
            for k, r in sorted(seen.items()):
                if r.status != LIVE:
                    print(f'  {r.status:8s} {k}  ->  {r.live_path}   [{where[k][0]}]')
        return 0
    if cmd == 'pipeline':
        # WHO READS AND WHO WRITES each path, across every .py in the given trees.
        # A path with writers and no readers is a generated artefact nobody consumes; a path with
        # readers and no writers is an input that must survive a cut. Both are cutting decisions
        # that a reference count cannot make.
        scope = rest or ['tools', 'engine', 'systems', 'tests']
        edges: dict[str, dict[str, set]] = {}
        for t in scope:
            base = os.path.join(REPO, t)
            for dirpath, _d, names in os.walk(base):
                for n in names:
                    if not n.endswith('.py'):
                        continue
                    full = os.path.join(dirpath, n)
                    src_rel = os.path.relpath(full, REPO).replace(os.sep, '/')
                    try:
                        with open(full, encoding='utf-8', errors='ignore') as fh:
                            code = fh.read()
                    except OSError:
                        continue
                    for io in py_path_io(code):
                        r = resolve(io.path)
                        key = r.live_path or io.path
                        e = edges.setdefault(key, {'read': set(), 'write': set(),
                                                   'scan': set(), 'delete': set()})
                        e.setdefault(io.mode, set()).add(f'{src_rel}:{io.line}')
        if as_json:
            print(json.dumps({k: {m: sorted(v) for m, v in d.items()}
                              for k, d in sorted(edges.items())}, indent=1, sort_keys=True))
            return 0
        produced = {k for k, d in edges.items() if d['write']}
        consumed = {k for k, d in edges.items() if d['read'] or d['scan']}
        print(f'{len(edges)} path(s) with traced I/O across {", ".join(scope)}')
        print('  NOTE: a LOWER BOUND. Dynamic paths (open(os.path.join(REPO, rel)) for a loop')
        print('  variable) are invisible without dataflow analysis, and guessing is forbidden.')
        print('  This is a candidate-finder, not a census. Pinned by')
        print('  tests/valoria/test_pathres.py::test_the_known_blind_spot_is_a_blind_spot.')
        print(f'  written and read : {len(produced & consumed)}')
        print(f'  WRITTEN, NEVER READ (generated, unconsumed): {len(produced - consumed)}')
        for k in sorted(produced - consumed):
            print(f'      {k}   <- {sorted(edges[k]["write"])[0]}')
        print(f'  READ, NEVER WRITTEN (inputs that must survive a cut): '
              f'{len(consumed - produced)}')
        return 0
    print(f'unknown command {cmd!r}', file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(_cli(sys.argv[1:]))
