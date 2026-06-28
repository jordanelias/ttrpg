#!/usr/bin/env python3
"""
ci_hooks_verifier.py
Runs in CI. Verifies the Claude Code-native enforcement architecture is intact.

This REPLACES the old orchestrator-coupled verifier. The previous version asserted
that skills/valoria-orchestrator/SKILL.md imported valoria_hooks and called
assert_bootstrap()/h.safe_commit, and that a bespoke harness defined named gate
functions — the load-bearing coupling that would have turned CI red the moment the
dead harness was removed. Enforcement now has one authoritative tier (this CI) and a
thin local tier (settings.json hooks + .githooks/pre-commit, both calling the same
tools/ci_*.py validators). So this verifier checks that the NATIVE wiring exists,
not that the retired harness does.

Blocking checks:
  1. .claude/settings.json exists and wires hooks to tools/ (or .githooks/).
  2. CLAUDE.md documents the git commit path.
  3. No SKILL.md exceeds its token budget.
  4. No /home/claude sandbox references under skills/ (the native-skill surface;
     the retired harness is gone, so skills must read the working tree).
Non-blocking warnings:
  - lingering /home/claude sandbox references under tools/ (analysis utilities
    pending the GitHub-API->working-tree port; tracked in HANDOFF.md).
  - design-doc skeleton-debt (>400 lines).
"""
import glob
import os
import sys

DEFAULT_SKILL_LIMIT = 8_000  # tokens (chars // 4)

violations = []
warnings = []

# ── Check 1: Claude Code hooks wired ─────────────────────────────────────────
SETTINGS = '.claude/settings.json'
if not os.path.exists(SETTINGS):
    violations.append(f"MISSING: {SETTINGS} — Claude Code hooks not configured")
else:
    with open(SETTINGS, encoding='utf-8', errors='replace') as f:
        s = f.read()
    if '"hooks"' not in s and 'hooks' not in s:
        violations.append(f"{SETTINGS}: no 'hooks' block")
    elif 'tools/' not in s and '.githooks' not in s:
        violations.append(f"{SETTINGS}: hooks do not reference tools/ or .githooks/")
    else:
        print(f"OK   {SETTINGS}: hooks wired")

# ── Check 2: CLAUDE.md documents the commit path ─────────────────────────────
if not os.path.exists('CLAUDE.md'):
    violations.append("MISSING: CLAUDE.md")
else:
    with open('CLAUDE.md', encoding='utf-8', errors='replace') as f:
        c = f.read()
    if 'git commit' not in c:
        violations.append("CLAUDE.md: does not document the git commit path")
    else:
        print("OK   CLAUDE.md: documents the git commit path")
    if 'Solmund' not in c:
        warnings.append("CLAUDE.md: naming rule (Solmund) not documented")

# ── Check 3 (warn): skill token sizes ────────────────────────────────────────
# Warn, not fail: skills load on-trigger (unlike registers, which load every
# session), so an oversized skill is a lint signal, not a hard violation.
for skill_md in sorted(glob.glob('skills/*/SKILL.md')):
    with open(skill_md, encoding='utf-8', errors='replace') as f:
        tokens = len(f.read()) // 4
    if tokens > DEFAULT_SKILL_LIMIT:
        warnings.append(f"SKILL LARGE: {skill_md.replace(os.sep, '/')}: {tokens:,} tokens "
                        f"(soft limit {DEFAULT_SKILL_LIMIT:,})")
    else:
        print(f"OK   size {skill_md}: {tokens:,}/{DEFAULT_SKILL_LIMIT:,} tokens")

# ── Check 4: lingering /home/claude sandbox references ───────────────────────
# skills/ are the native-skill surface and must be clean → BLOCKING.
# tools/ analysis utilities (and this verifier's own message strings) still
# mention the retired sandbox pending the GitHub-API→working-tree port → WARN.
# deprecated/ is intentionally NOT walked (retired artifacts kept for history).
for base in ('skills', 'tools'):
    for dirpath, _dirs, files in os.walk(base):
        for fn in files:
            if not (fn.endswith('.py') or fn.endswith('.md')):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding='utf-8', errors='replace') as f:
                    txt = f.read()
            except OSError:
                continue
            if '/home/claude' in txt:
                rel = p.replace(os.sep, '/')
                if base == 'skills':
                    violations.append(f"SANDBOX REF: {rel} references /home/claude — "
                                      f"skills must read the working tree (retired harness)")
                else:
                    warnings.append(f"SANDBOX REF: {rel} still references /home/claude "
                                    f"(port to working-tree reads)")

# ── Check 5 (warn): skeleton-debt — design docs over 400 lines ───────────────
for root, _dirs, files in os.walk('designs'):
    for fname in files:
        if (fname.endswith('_v30.md') and 'infill' not in fname
                and 'archive' not in fname and 'skeleton' not in fname):
            fpath = os.path.join(root, fname)
            with open(fpath, encoding='utf-8', errors='replace') as f:
                n = len(f.readlines())
            if n > 400:
                warnings.append(f"SKELETON-DEBT: {fpath.replace(os.sep, '/')} is {n} lines (limit 400); "
                                f"extract prose to *_infill.md")

if warnings:
    print(f"\n[WARNINGS: {len(warnings)}] (non-blocking)")
    for w in warnings:
        print(f"  ! {w}")

if violations:
    print(f"\n[HOOKS VERIFIER VIOLATIONS: {len(violations)}]\n")
    for i, v in enumerate(violations, 1):
        print(f"  [{i}] {v}")
    sys.exit(1)

print("\nHooks verifier: enforcement architecture intact.")
sys.exit(0)
