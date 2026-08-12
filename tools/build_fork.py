#!/usr/bin/env python3
"""Assemble the code-first fork tree, then prove it runs standalone.

WHY A SCRIPT AND NOT A COPIED DIRECTORY. A hand-copied fork is a snapshot that starts rotting the
moment it exists and doubles the repo. This declares the carry list as DATA, assembles from it, and
ends by running a seeded campaign inside the assembled tree with the source repo removed from
`sys.path`. If the fork cannot run on its own, the build FAILS -- so "self-contained" is a test
result, not a claim.

WHAT THE FORK IS FOR (plan of record §0.1, Jordan's principles): a Python-runnable, code-first game
engine that ports to Godot. Values live in code and typed tables; Keys carry inter-subsystem state;
prose stays behind. So the carry list is deliberately narrow, and everything left out is left out
ON PURPOSE rather than forgotten -- LEAVE below is as load-bearing as CARRY.

THE MASS-BATTLE TREES -- RULED 2026-08-03 (J2), REGISTERED 2026-08-04 as ED-MB-0064.
`systems/mass_battle/sim/` (5 modules) is what the campaign actually calls; `tests/sim/mass_battle/`
(28 modules) is CANON. The live 5-module tree is RETIRED, not kept alongside.
  CORRECTION (ED-IN-0125): the API line below was WRONG in every copy of it. `{winner, turns, phases}`
  is the `kind='single'` path; the caller uses `kind='multi'`, which returns
  `{winner, battle_turns, log, a_loss_final, b_loss_final}` -- see audit/2026-08-03-session-oddities.md
  section H. Three of the caller's four fields map mechanically.
  `degree` still has no canon mapping and must be AUTHORED, but it is partially unblocked: Jordan
  ruled 2026-08-04 (C2) that mass battle occurs ON A MAP and the loser of the scene is whoever loses
  more units or has their settlement captured. That supplies `attacker_wins` and constrains the ladder;
  the four band edges remain unruled, so `degree_map` stays a required arg with no default.
  ⚠ STATUS OF THIS TOOL. The repository direction was INVERTED 2026-08-04 (ED-IN-0125): `main` is the
  code-first go-forward repo and the fork/archive receives the outdated prose. This script's
  copy-into-an-empty-tree operation is therefore NO LONGER the executor. Both trees are still carried
  below because the carry list doubles as the keep-set draft, but the canon re-home is now an in-repo
  `git mv` (history survives via --follow), not a copy. Do NOT run CARRY/LEAVE backwards to produce a
  deletion list: CARRY union LEAVE does not partition the tree, and the neither-set -- .github/,
  .githooks/, .claude/, tools/, tests/valoria/, most of references/, research/, skills/, CLAUDE.md,
  CURRENT.md, HANDOFF.md -- would be DELETED, taking the enforcement tier and the shipping gate with
  it. The authored keep-set is systems/_architecture/repository_keep_set_v1.md.

Usage:
    python3 tools/build_fork.py --out /path/to/fork      # assemble + verify
    python3 tools/build_fork.py --out /tmp/fork --verify-only
"""
from __future__ import annotations

import argparse
import ast
import collections
import json
import os
import shutil
import subprocess
import sys

try:
    import yaml
except ImportError:
    yaml = None

# ONE OWNER for the repo root, the 9-lane roster, token estimation and the id
# regexes: tools/ci_common.py (plan G7, ED-IN-0159 §8.3). The two lines below are
# the irreducible bootstrap — a module cannot import its owner without first
# knowing where the owner is — and they anchor on THIS FILE's directory, never on
# the repo root, so they are not the duplication they replace.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO

# ── CARRY: (source, destination, why) ────────────────────────────────────────
CARRY = [
    # The executable core. `engine/` is the Key substrate + autoload singletons + cross-scale
    # adapters + the campaign driver. Everything else depends UPWARD on it (acyclic).
    ("engine", "engine", "the executable core: substrate, autoload, cross_scale, mc_v18, tests"),
    # Per-subsystem sims and their design docs. One subsystem = one folder (ED-IN-0071 P4).
    ("systems", "systems", "per-subsystem sims + combat_engine_v1 + subsystem design docs"),
    # CANON mass battle, re-homed out of tests/ (ED-MB-0043). Carried alongside the live tree,
    # not instead of it -- see the module docstring.
    ("tests/sim/mass_battle", "systems/mass_battle/canon",
     "ED-MB-0043 canon MB engine, 28 modules, misfiled under tests/ in the source repo"),
    # The numpy-free parity oracle the sigma kernel validates against.
    ("tests/sim/v32-combat-balance", "engine/reference/v32-combat-balance",
     "sigma-kernel parity oracle (m1_dice_sigma_core)"),
    # The machine-readable spine. These are DATA, not prose: the fork reads them.
    ("references/module_contracts.yaml", "references/module_contracts.yaml",
     "Key IN -> resolver -> OUT contracts + owned state"),
    ("references/wiring_manifest.yaml", "references/wiring_manifest.yaml",
     "build state / godot state / port rank / parity per unit"),
    ("references/key_graph.json", "references/key_graph.json", "merged producer/consumer key graph"),
    ("references/execution_map.json", "references/execution_map.json", "boot->termination spine"),
    ("references/EXECUTION_MAP.md", "references/EXECUTION_MAP.md", "the same map, readable"),
    ("references/execution_trace.json", "references/execution_trace.json",
     "measured per-phase execution"),
    # The Godot target.
    ("godot", "godot", "the eventual res:// root: strategy, architecture spec, skeleton"),
]

# ── LEAVE: (path, why) — stated, because a silent omission is indistinguishable from a mistake ──
LEAVE = [
    ("registers/", "editorial ledgers, patch register, handoffs — process, not game"),
    ("audit/", "the audit corpus; cite back by repo@SHA"),
    ("arcs/", "generated narrative content"),
    ("workplans/", "the progress board"),
    ("dashboard/", "the published status site"),
    ("proposals/", "unratified proposals incl. the fork plan itself"),
    ("canon/", "philosophical foundations — prose with no code pair; revisit per principle 7"),
    ("engine/params/", "43 prose param tables with ZERO readers in engine/ or systems/"),
    ("tools/", "the source repo's gates; the fork re-derives what it needs"),
    ("deprecated/", "history"),
    ("tests/valoria/", "the source repo's validator suite; engine/tests comes instead"),
]

VERIFY_SEED = 20260803
VERIFY_SEASONS = 3


def assemble(out: str) -> list[str]:
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    carried = []
    for src, dst, _why in CARRY:
        s = os.path.join(REPO, src)
        d = os.path.join(out, dst)
        if not os.path.exists(s):
            raise SystemExit(f"carry source missing: {src}")
        os.makedirs(os.path.dirname(d), exist_ok=True)
        if os.path.isdir(s):
            # LEAVE IS SUBTRACTED HERE, not merely documented. It used to be consulted only by the
            # escape scan, so `engine/params/` sat in LEAVE with its reason -- 43 prose tables with
            # ZERO readers in engine/ or systems/ -- and shipped anyway, because CARRY takes
            # `engine/` wholesale. A LEAVE list that does not subtract is a comment.
            def _prune(dirpath, names):
                out_names = set(shutil.ignore_patterns(
                    '__pycache__', '*.pyc', '.pytest_cache')(dirpath, names))
                for n in names:
                    rel = os.path.relpath(os.path.join(dirpath, n), os.path.join(REPO, src))
                    full = os.path.normpath(os.path.join(dst, rel))
                    if any(full == L.rstrip('/') or full.startswith(L.rstrip('/') + os.sep)
                           for L in (x.strip('/') for x, _ in LEAVE)):
                        out_names.add(n)
                return out_names
            shutil.copytree(s, d, ignore=_prune)
        else:
            shutil.copy2(s, d)
        carried.append(dst)
    # A package marker for the re-homed canon tree, so it imports as
    # systems.mass_battle.canon.* rather than needing a sys.path entry.
    init = os.path.join(out, 'systems', 'mass_battle', 'canon', '__init__.py')
    if not os.path.exists(init):
        with open(init, 'w', encoding='utf-8') as fh:
            fh.write('"""ED-MB-0043 canon mass-battle engine, re-homed out of tests/sim/.\n\n'
                     'Carried ALONGSIDE systems/mass_battle/sim (the tree the campaign calls),\n'
                     'not instead of it: the APIs differ and the swap needs a `degree` mapping\n'
                     'that has no canon. See tools/build_fork.py.\n"""\n')
    return carried


class EmptyScanError(RuntimeError):
    """A scan was asked to walk a tree with no Python in it.

    See `_scanned_py` for why this is an error rather than an empty result.
    """


def _scanned_py(out: str) -> list[str]:
    """THE SINGLE OWNER of "which .py files does a tree-scan see", and it refuses to see none.

    CLAUDE.md 0.1 point 2: an assertion must be able to observe the failure it excludes. Both
    scanners below (`escapes`, `classify`) walked `out` directly with `os.walk`, which yields
    NOTHING for a path that does not exist -- it does not raise. A scan over a missing tree
    therefore reported "no path literal reaches an uncarried tree", which is textually identical
    to the clean result and carries none of its meaning. That is the gate-reporting-clean-over-
    nothing class (#283/#284, and `tests/valoria/test_tool_input_paths_resolve.py` names it).

    The concrete defect this closes: `--verify-only` skips `assemble()`, so on a fresh `--out`
    the tree never existed; the run printed a green escape line over zero files and then died at
    the FORK_MANIFEST write with a bare FileNotFoundError. Both halves were wrong -- the green
    line was meaningless and the failure was illegible.

    NOT fixed by having `--verify-only` assemble into a temp dir: that silently verifies a
    different tree than the one the caller named, and collapses the two documented modes into one.
    `--verify-only` re-verifies an EXISTING assembled tree; if there isn't one, say so.
    """
    if not os.path.isdir(out):
        raise EmptyScanError(
            f"{out!r} does not exist. `--verify-only` re-verifies an ALREADY-ASSEMBLED tree; "
            f"run without --verify-only first to build it."
        )
    files = []
    for dirpath, dirnames, filenames in os.walk(out):
        dirnames[:] = [d for d in dirnames if d != '__pycache__']
        files.extend(os.path.join(dirpath, fn) for fn in filenames if fn.endswith('.py'))
    if not files:
        raise EmptyScanError(
            f"{out!r} contains no .py files, so every scan over it is vacuously clean. "
            f"Refusing to report a green result that means nothing."
        )
    return files


def escapes(out: str) -> list[tuple[str, int, str]]:
    """Path literals in the assembled tree naming a directory the fork did NOT carry.

    The same join-aware discriminator the source repo's scan uses: a bare 'tests' is only an
    escape when it is an argument to a path-joining call, and a multi-segment literal always is.
    A value-only scan over-reports dict keys; a separator-only scan misses os.path.join(REPO,
    'tests'). Both mistakes were made and corrected upstream.
    """
    # FULL PREFIXES, not first segments. Taking `p.split('/')[0]` turned `engine/params/` into
    # `engine` and `tests/valoria/` into `tests`, blacklisting the entire carried engine tree and
    # every reference to it -- 8 of the first run's 11 "escapes" were that, plus docstrings.
    left = tuple(p.strip('/') for p, _ in LEAVE)
    found = []

    def _is_left(v):
        n = v.replace('\\', '/').strip('/')
        return any(n == L or n.startswith(L + '/') for L in left)

    class V(ast.NodeVisitor):
        def __init__(self, rel, tree):
            self.rel = rel
            # DOCSTRINGS ARE PROSE. A module/class/function docstring is an ast.Constant, so a
            # bare Constant visitor reads every path MENTIONED in documentation as a path USED by
            # the code. That is the same prose-vs-code proxy error corrected twice already
            # upstream; collected here so the scan reports usage only.
            self.docstrings = set()
            for n in ast.walk(tree):
                if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                    body = getattr(n, 'body', None)
                    if body and isinstance(body[0], ast.Expr) and \
                            isinstance(body[0].value, ast.Constant) and \
                            isinstance(body[0].value.value, str):
                        self.docstrings.add(id(body[0].value))
        def _chk(self, node, joined):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                if id(node) in self.docstrings:
                    return          # prose, not a path the code uses
                if _is_left(node.value) and ('/' in node.value or joined):
                    found.append((self.rel, node.lineno, node.value))
        def visit_Call(self, node):
            fn = getattr(node.func, 'attr', None) or getattr(node.func, 'id', None)
            if fn in ('join', 'Path', 'open', 'walk', 'spec_from_file_location', 'abspath'):
                for a in node.args:
                    self._chk(a, True)
            self.generic_visit(node)
        def visit_Constant(self, node):
            self._chk(node, False)

    for p in _scanned_py(out):          # guarded: refuses to scan an empty/missing tree
        try:
            tree = ast.parse(open(p, encoding='utf-8').read())
        except (SyntaxError, UnicodeDecodeError):
            continue
        V(os.path.relpath(p, out), tree).visit(tree)
    return found


def contract_coverage() -> list[str]:
    """RULE (Jordan, 2026-08-03): anything that needs a contract, or is a stub for something,
    gets forked over.

    Enforced at build time rather than trusted. Every unit in module_contracts must have its
    declared `doc` and `sim_module` inside the carry set. It passes today only because
    `systems/` and `engine/` are carried WHOLESALE -- which is exactly why it is a guard: the
    tempting next move is a "minimal fork" of just the 58 runtime files, and that would silently
    drop 14 units that have a contract but no code yet, plus all three `build: stub` units. A
    contract with no code is the fork's backlog; dropping it loses the backlog, not dead weight.
    """
    if yaml is None:
        return ["pyyaml missing — cannot verify contract coverage"]
    roots = [dst for _src, dst, _why in CARRY]

    def inside(path):
        if not isinstance(path, str) or path.strip().lower() in ('none', 'null', 'n/a', ''):
            return True                      # nothing declared is nothing to carry
        q = path.strip().rstrip('/')
        return any(q == r or q.startswith(r.rstrip('/') + '/') for r in roots)

    with open(os.path.join(REPO, 'references', 'module_contracts.yaml'), encoding='utf-8') as fh:
        contracts = yaml.safe_load(fh) or {}
    bad = []
    for c in contracts.get('modules') or []:
        for field in ('doc', 'sim_module'):
            if not inside(c.get(field)):
                bad.append(f"{c['module']}.{field} = {c.get(field)!r} is outside the carry set")
    return bad


def classify(out: str) -> dict:
    """Every carried .py file, classified by its relation to the EXECUTABLE.

    This is the structure the fork is for. A flat copy of 206 files says nothing; the graph does.
    `runtime` is the transitive import closure from `engine.mc_v18` -- boot to termination, the
    thing that actually runs. Everything else is carried for a stated reason, and being outside
    the closure is a FACT about wiring, not a defect: `systems/combat` is 28 files of tested
    engine the campaign never calls (personal_combat is `build: unwired`), which is exactly what
    the fork exists to fix.
    """
    def mod_to_path(m):
        for cand in (m.replace('.', '/') + '.py', m.replace('.', '/') + '/__init__.py'):
            q = os.path.join(out, cand)
            if os.path.exists(q):
                return q
        return None

    def imports_of(q):
        try:
            t = ast.parse(open(q, encoding='utf-8').read())
        except (SyntaxError, UnicodeDecodeError):
            return set()
        acc = set()
        for n in ast.walk(t):
            if isinstance(n, ast.ImportFrom) and n.module:
                acc.add(n.module)
                for a in n.names:
                    acc.add(f"{n.module}.{a.name}")
            elif isinstance(n, ast.Import):
                for a in n.names:
                    acc.add(a.name)
        return {m for m in acc if m.split('.')[0] in ('engine', 'systems')}

    runtime, frontier = set(), {'engine.mc_v18'}
    while frontier:
        m = frontier.pop()
        q = mod_to_path(m)
        if not q or q in runtime:
            continue
        runtime.add(q)
        for dep in imports_of(q):
            dq = mod_to_path(dep)
            if dq and dq not in runtime:
                frontier.add(dep)

    buckets = collections.defaultdict(list)
    for q in _scanned_py(out):          # guarded: refuses to scan an empty/missing tree
        rel = os.path.relpath(q, out)
        if q in runtime:
            buckets['runtime'].append(rel)
        elif rel.startswith(os.path.join('engine', 'tests')):
            buckets['test'].append(rel)
        elif rel.startswith(os.path.join('engine', 'reference')):
            buckets['oracle'].append(rel)
        elif rel.startswith(os.path.join('systems', 'mass_battle', 'canon')):
            buckets['canon_unwired'].append(rel)
        elif os.sep + 'workbench' + os.sep in rel:
            buckets['workbench'].append(rel)
        else:
            buckets['subsystem_unwired'].append(rel)
    return {k: sorted(v) for k, v in buckets.items()}


def verify_runs(out: str):
    """THE FALSIFIER: run a seeded campaign INSIDE the fork, with the source repo off sys.path.

    Subprocess with a scrubbed PYTHONPATH and cwd=out, so an accidental import of the source repo
    fails loudly instead of silently succeeding because this process already has it loaded.
    """
    script = (
        "import sys, json\n"
        "sys.path.insert(0, '.')\n"
        f"bad = [p for p in sys.path if {REPO!r} in p]\n"
        "assert not bad, f'source repo leaked onto sys.path: {bad}'\n"
        "from engine import mc_v18\n"
        f"r = mc_v18.run_campaign(seed={VERIFY_SEED}, "
        f"params={{'ECHO_TRANSPORT': True, 'CAMPAIGN_SEASONS': {VERIFY_SEASONS}}})\n"
        "print(json.dumps({'winner': r.winner, 'keys': r.keys_emitted, "
        "'hash': r.key_log_hash[:16], 'battles': r.battle_count}))\n"
    )
    env = dict(os.environ)
    env.pop('PYTHONPATH', None)
    return subprocess.run([sys.executable, '-c', script], cwd=out, env=env,
                          capture_output=True, text=True)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--verify-only', action='store_true')
    args = ap.parse_args(argv)
    out = os.path.abspath(args.out)

    if not args.verify_only:
        carried = assemble(out)
        n_py = sum(len([f for f in fs if f.endswith('.py')]) for _, _, fs in os.walk(out))
        print(f"[FORK] assembled {len(carried)} carry roots -> {out}")
        print(f"[FORK] {n_py} .py files")
    else:
        # FAIL BEFORE PRINTING ANYTHING GREEN. `--verify-only` does not assemble, so on a fresh
        # --out there is no tree; the scanners would otherwise report a vacuous clean line and
        # only then die at the manifest write. Check first, exit legibly.
        try:
            _scanned_py(out)
        except EmptyScanError as e:
            print(f"[FORK] CANNOT VERIFY: {e}")
            return 2

    gaps = contract_coverage()
    if gaps:
        print(f"[FORK] {len(gaps)} contracted/stub unit(s) would be LEFT BEHIND:")
        for g in gaps:
            print(f"        {g}")
    else:
        print("[FORK] every contract unit's doc + code is inside the carry set")

    esc = escapes(out)
    if esc:
        print(f"[FORK] {len(esc)} path literal(s) reach a tree the fork does not carry:")
        for rel, line, v in esc[:20]:
            print(f"        {rel}:{line}  {v!r}")
    else:
        print("[FORK] no path literal reaches an uncarried tree")

    cls = classify(out)
    total = sum(len(v) for v in cls.values())
    print(f"[FORK] structure by relation to the executable ({total} .py):")
    for k in ('runtime', 'test', 'oracle', 'canon_unwired', 'workbench', 'subsystem_unwired'):
        if cls.get(k):
            print(f"        {k:20s} {len(cls[k]):>4}")
    # THE UNWIRED SUBSYSTEMS ARE THE BACKLOG, NOT NOISE -- 69 files in one bucket hides which
    # subsystem and how much of it is real. Crossed with wiring_manifest's build state so the
    # bucket reads as a work-list: `unwired` means tested code the loop never calls (the thing
    # the fork exists to fix), `design` means no code to wire yet.
    if cls.get('subsystem_unwired'):
        # JOIN THROUGH THE CONTRACTS, not by directory name. A first pass matched the directory
        # (`combat`) against module names (`personal_combat`) and returned '?' for 9 of 11 rows.
        # module_contracts' `sim_module` is the mapping, and it may be a FILE or a DIRECTORY.
        unit_of, states = {}, {}
        cpath = os.path.join(out, 'references', 'module_contracts.yaml')
        mpath = os.path.join(out, 'references', 'wiring_manifest.yaml')
        if yaml is not None and os.path.exists(cpath):
            with open(cpath, encoding='utf-8') as fh:
                contracts = yaml.safe_load(fh) or {}
            for c in contracts.get('modules') or []:
                code = c.get('sim_module')
                if not isinstance(code, str) or code.strip().lower() in ('none', 'null', ''):
                    continue
                unit_of[code.rstrip('/')] = c['module']
        if yaml is not None and os.path.exists(mpath):
            with open(mpath, encoding='utf-8') as fh:
                m = yaml.safe_load(fh) or {}
            for name, row in (m.get('modules') or {}).items():
                states[name] = row.get('build')

        def unit_for(rel):
            """Longest matching sim_module prefix -- a directory pointer owns everything under it."""
            best = None
            for path, unit in unit_of.items():
                if rel == path or rel.startswith(path.rstrip('/') + os.sep):
                    if best is None or len(path) > len(best[0]):
                        best = (path, unit)
            return best[1] if best else None

        rows = collections.defaultdict(int)
        for rel in cls['subsystem_unwired']:
            u = unit_for(rel)
            rows[(u or 'no contract', states.get(u) if u else None)] += 1
        print("        -- unwired files by CONTRACT unit and declared build state:")
        print("           (build != design means it is MEANT to be wired -- that is the backlog)")
        for (unit, st), n in sorted(rows.items(), key=lambda kv: -kv[1]):
            tag = {'unwired': '  <- tested code the loop never calls',
                   'stub': '  <- raises; needs building',
                   'gated': '  <- runs only under a condition',
                   'deferred': '  <- reached, resolves nothing'}.get(st, '')
            print(f"             {unit:22s} {n:>3} files   build={st}{tag}")

    with open(os.path.join(out, 'FORK_MANIFEST.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps({
            "_generated": ("GENERATED by tools/build_fork.py. `runtime` is the transitive import "
                           "closure from engine.mc_v18 -- boot to termination. Being outside it is "
                           "a fact about WIRING, not a defect: systems/combat is tested engine the "
                           "campaign never calls, which is what the fork exists to fix."),
            "carry": [{"from": a, "to": b, "why": c} for a, b, c in CARRY],
            "leave": [{"path": a, "why": b} for a, b in LEAVE],
            "counts": {k: len(v) for k, v in cls.items()},
            "files": cls,
        }, indent=1) + "\n")

    proc = verify_runs(out)
    if proc.returncode == 0:
        print(f"[FORK] RUNS STANDALONE: {proc.stdout.strip()}")
    else:
        print("[FORK] DOES NOT RUN STANDALONE:")
        print((proc.stderr or proc.stdout).strip()[-2500:])
    return 0 if (proc.returncode == 0 and not esc and not gaps) else 1


if __name__ == '__main__':
    sys.exit(main())
