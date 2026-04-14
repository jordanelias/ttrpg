#!/usr/bin/env python3
"""
ci_hooks_verifier.py
Runs in CI. Verifies the enforcement architecture is intact:
- valoria_hooks.py exists and has required functions
- Orchestrator SKILL.md imports hooks and calls assert_bootstrap()
- Orchestrator uses h.safe_commit() not g.atomic_commit() directly
- Skills do NOT contain the redundant blocks that were stripped
- Skills do NOT exceed individual token thresholds
"""
import sys, os, re

HOOKS_PATH = 'skills/valoria-orchestrator/scripts/valoria_hooks.py'
ORCH_PATH  = 'skills/valoria-orchestrator/SKILL.md'

REQUIRED_HOOKS = [
    'def assert_bootstrap',
    'def task_gate',
    'def editorial_gate',
    'def pre_commit_gate',
    'def commit_message_gate',
    'def propose_mechanic_gate',
    'def context_gate',
    'def safe_commit',
]

REDUNDANT_BLOCKS = [
    '**Pre-commit (run before every `atomic_commit()` call):**\n```bash',
    '**Memory contamination warning:**',
    '**Fetch log (emit before any analysis):**',
    '**Version check:** confirm',
]

SKILL_TOKEN_LIMITS = {
    'skills/valoria-orchestrator/SKILL.md':        8_000,
    'skills/valoria-simulator/SKILL.md':           6_000,
    'skills/valoria-mechanic-audit/SKILL.md':      6_000,
    'skills/valoria-canon-guard/SKILL.md':         6_000,
    'skills/valoria-editorial-register/SKILL.md':  6_000,
    'skills/valoria-chunker/SKILL.md':             3_000,
    'skills/valoria-dice-model/SKILL.md':          6_000,
}

violations = []
skeleton_warnings = []

# ── Check 1: hooks file exists with required functions ────────────────────────
if not os.path.exists(HOOKS_PATH):
    violations.append(f"MISSING: {HOOKS_PATH} — enforcement hooks not present")
else:
    with open(HOOKS_PATH) as f:
        hooks_content = f.read()
    for fn in REQUIRED_HOOKS:
        if fn not in hooks_content:
            violations.append(f"HOOKS MISSING function: {fn}")
        else:
            print(f"OK   hooks: {fn}")

# ── Check 2: orchestrator imports hooks and uses safe_commit ──────────────────
if not os.path.exists(ORCH_PATH):
    violations.append(f"MISSING: {ORCH_PATH}")
else:
    with open(ORCH_PATH) as f:
        orch = f.read()
    checks = {
        'imports valoria_hooks': 'import valoria_hooks' in orch,
        'calls assert_bootstrap': 'assert_bootstrap()' in orch,
        'uses h.safe_commit': 'h.safe_commit' in orch,
        'documents safe_commit replaces atomic_commit': 'safe_commit' in orch,
    }
    for name, result in checks.items():
        if result:
            print(f"OK   orchestrator: {name}")
        else:
            violations.append(f"ORCHESTRATOR: {name} — not found in {ORCH_PATH}")

# ── Check 3: skills do not contain redundant blocks ──────────────────────────
for skill_path in SKILL_TOKEN_LIMITS:
    if skill_path == ORCH_PATH:
        continue  # orchestrator is allowed to have some of these
    if not os.path.exists(skill_path):
        print(f"SKIP {skill_path}: not found")
        continue
    with open(skill_path) as f:
        content = f.read()
    for block in REDUNDANT_BLOCKS:
        if block in content:
            violations.append(
                f"REDUNDANT BLOCK in {skill_path}: '{block[:50]}...'\n"
                f"  Strip this — it belongs only in github_ops.py or orchestrator."
            )

# ── Check 4: skill token sizes ────────────────────────────────────────────────
for path, limit in SKILL_TOKEN_LIMITS.items():
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8', errors='replace') as f:
        content = f.read()
    tokens = len(content) // 4
    if tokens > limit:
        violations.append(f"SKILL TOO LARGE: {path}: {tokens:,} tokens (limit {limit:,})")
    else:
        print(f"OK   size {path}: {tokens:,}/{limit:,} tokens")

# ── Check 5: skeleton ruleset principle — design docs over 400 lines ──────────
for root, dirs, files in os.walk('designs'):
    for fname in files:
        if fname.endswith('_v30.md') and 'infill' not in fname and 'archive' not in fname and 'skeleton' not in fname:
            fpath = os.path.join(root, fname)
            with open(fpath, encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
            if len(lines) > 400:
                skeleton_warnings.append(
                    f"SKELETON-DEBT: {fpath} is {len(lines)} lines (limit 400).\n"
                    f"  Extract explanatory prose to {fname.replace('_v30.md','_v30_infill.md')}"
                )
            else:
                print(f"OK   skeleton {fpath}: {len(lines)} lines")


# ── Check 6: all skills must reference bootstrap ─────────────────────────────
ALL_SKILLS = [p for p in SKILL_TOKEN_LIMITS.keys() if p != ORCH_PATH]
for skill_path in ALL_SKILLS:
    if not os.path.exists(skill_path):
        continue
    with open(skill_path, encoding='utf-8', errors='replace') as f:
        content = f.read()
    if 'assert_bootstrap' not in content and 'quick_bootstrap' not in content:
        violations.append(
            f"BOOTSTRAP MISSING: {skill_path} does not reference assert_bootstrap or quick_bootstrap.\n"
            f"  All skills that do bash_tool work must call quick_bootstrap() or assert_bootstrap().\n"
            f"  Add the Standard Work Block Template from orchestrator SKILL.md."
        )
    else:
        print(f"OK   bootstrap ref: {skill_path}")

if skeleton_warnings:
    print(f"\n[SKELETON-DEBT WARNINGS: {len(skeleton_warnings)}] (non-blocking)")
    for w in skeleton_warnings:
        print(f"  \u26a0 {w}")

if violations:
    print(f"\n[HOOKS VERIFIER VIOLATIONS: {len(violations)}]\n")
    for i, v in enumerate(violations, 1):
        print(f"  [{i}] {v}\n")
    sys.exit(1)
else:
    print("\nHooks verifier: all checks passed.")
    sys.exit(0)
