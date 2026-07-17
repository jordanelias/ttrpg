#!/usr/bin/env python3
"""
ci_module_shape_check.py — container/shape hygiene guard (ED-1085; doctrine ED-1083 §3).

Enforces the holonic container rules on ENGINE/SIM RUNTIME code
(systems/_architecture/holonic_container_doctrine_v1.md §3):

  1. NO cross-container reach-ins: runtime modules must not manipulate sys.path to point
     into a tests/ tree (the ED-1085 failure class: combat_engine_v1/core.py importing its
     sigma kernel from the frozen tests/sim/v32-combat-balance station, dragging numpy into
     the engine runtime).
  2. NO imports from tests/ trees in runtime code (`from tests...` / `import tests...`).
  3. INFO-tier: module-scope numeric-literal constants in combat_engine_v1 runtime modules
     (outside config.py, the declared Class-C container) that carry no provenance tag.
     Constant-VALUE provenance is ci_sim_fabrication_check.py's job (changed-lines, ledger-
     backed) — this only surfaces untagged module-scope literals as drift candidates. It
     never fails the run.

DECLARED EXCLUSIONS (measurement/dev harnesses are not runtime containers):
  * anything under a tests/ tree itself,
  * designs/scene/combat_engine_v1/workbench/ (the measurement workbench reaches into the
    frozen v32 validation station BY DESIGN — tagged at each insert),
  * deprecated/archives/, deprecated/.

Scope: full working tree (deterministic; cheap). Exit 1 on any category-1/2 violation.
Wired report-only in CI first (same graduation lane as names-drift).

CLI:
    python tools/ci_module_shape_check.py
"""
import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# Runtime container roots this guard patrols.
RUNTIME_ROOTS = (
    'sim',
    'designs/scene/combat_engine_v1',
    'engine',
)

EXCLUDE_PARTS = ('tests', 'workbench', 'archives', 'deprecated', '__pycache__')

SYS_PATH_RE = re.compile(r'sys\.path\.(?:insert|append)\s*\(.*?["\']([^"\']+)["\']', re.S)
TESTS_IMPORT_RE = re.compile(r'^\s*(?:from|import)\s+tests[.\s]', re.M)
# module-scope NAME = <numeric literal>  (INFO tier, combat engine only)
CONST_RE = re.compile(r'^([A-Z][A-Z0-9_]*)\s*=\s*[-+]?\d+(?:\.\d+)?(?:e-?\d+)?\s*(#.*)?$')
PROVENANCE_TAGS = ('[canonical', '[class-c', '[d-a', '[damage_model', '[assumption', '[ci —', '[ci -', 'ed-')


def _runtime_files():
    for root in RUNTIME_ROOTS:
        base = os.path.join(REPO_ROOT, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            rel_dir = os.path.relpath(dirpath, REPO_ROOT).replace(os.sep, '/')
            parts = rel_dir.split('/')
            if any(p in EXCLUDE_PARTS for p in parts):
                dirnames[:] = []
                continue
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_PARTS]
            for name in filenames:
                if name.endswith('.py'):
                    yield os.path.join(dirpath, name), f"{rel_dir}/{name}"


def check(verbose=True):
    violations = []
    infos = []
    for path, rel in _runtime_files():
        try:
            with open(path, encoding='utf-8') as f:
                src = f.read()
        except OSError:
            continue

        for m in SYS_PATH_RE.finditer(src):
            target = m.group(1)
            if 'tests/' in target.replace('\\', '/') or target.startswith('tests'):
                line = src[:m.start()].count('\n') + 1
                violations.append(f"{rel}:{line}: sys.path reach-in to a tests/ tree ({target!r})")

        for m in TESTS_IMPORT_RE.finditer(src):
            line = src[:m.start()].count('\n') + 1
            violations.append(f"{rel}:{line}: runtime import from tests/ package")

        if rel.startswith('designs/scene/combat_engine_v1/') and not rel.endswith('/config.py'):
            for i, raw in enumerate(src.splitlines(), 1):
                cm = CONST_RE.match(raw)
                if cm:
                    comment = (cm.group(2) or '').lower()
                    if not any(t in comment for t in PROVENANCE_TAGS):
                        infos.append(f"{rel}:{i}: module-scope constant {cm.group(1)} without provenance tag")

    if verbose:
        for note in infos:
            print(f"  [INFO] {note}")
        if violations:
            print(f"[MODULE SHAPE VIOLATIONS: {len(violations)}]")
            print("  Runtime containers must not reach into tests/ trees "
                  "(holonic_container_doctrine_v1.md §3; ED-1085):")
            for v in violations:
                print(f"  {v}")
        else:
            print(f"Module shape: no container reach-ins in runtime code "
                  f"({len(infos)} INFO constant note(s)).")
    return violations


def main():
    return 1 if check() else 0


if __name__ == '__main__':
    sys.exit(main())
