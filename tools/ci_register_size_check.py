#!/usr/bin/env python3
"""
ci_register_size_check.py
Runs in CI (GitHub Actions) against the checked-out repo.
Fails if any governed file exceeds its token threshold.
This is the external enforcement gate — runs outside Claude, cannot be bypassed.
"""
import os, sys

THRESHOLDS = {
    # ── Active registers (strict limits — must chunk before exceeding) ──────
    "session_log_current.md":                  2_000,
    "session_logs/index.md":                   2_000,
    # editorial store + file index moved to JSONL/SQL (2026-05-28 cutover);
    # editorial_ledger.jsonl is checked soft below; valoria_index.sql is generated.
    # Interim: bumped 5_000 -> 12_000 to match the sanctioned interim cap in
    # g.TOKEN_THRESHOLDS (633f5e57; canonical_sources rode 9k->12k pending the
    # freshness SHA-split, roadmap K-2 / workplan LB-6). Returns to 5_000 when
    # the 115 canonical_sha fields move to references/canonical_freshness.yaml.
    "references/canonical_sources.yaml":      12_000,
    "skills/valoria-orchestrator/SKILL.md":    8_000,
    "canon/patch_register_active.yaml":       20_000,
    "tests/coverage_matrix.md":               5_000,
    "references/arc_register.md":            20_000,
    "references/propagation_map.md":         15_000,
    "references/design_registry.yaml":        8_000,
    # ── Archives (soft limits — warn when approaching split threshold) ──────
    # These are large by design; alert when year-split is needed
    "canon/patch_register_archive.yaml":     100_000,
    "canon/editorial_ledger.jsonl":         150_000,  # live append-only editorial store (post-2026-05-28 cutover); large by design
    "archives/session/session_log_archive_part_7.md": 100_000,
    "canon/patch_register_index.md":         20_000,
}

violations = []
checked = 0

for path, threshold in sorted(THRESHOLDS.items()):
    if not os.path.exists(path):
        print(f"SKIP {path}: not present in repo")
        continue
    try:
        with open(path, encoding='utf-8', errors='strict') as f:
            content = f.read()
    except UnicodeDecodeError as e:
        print(f'FAIL {path}: encoding error — {e}')
        violations.append((path, -1, threshold))
        checked += 1
        continue
    tokens = len(content) // 4
    checked += 1
    if tokens > threshold:
        violations.append((path, tokens, threshold))
        print(f"FAIL {path}: {tokens:,} tokens (limit {threshold:,})")
    else:
        print(f"OK   {path}: {tokens:,} / {threshold:,} tokens")

print(f"\nChecked {checked} files.")
if violations:
    print(f"\n[REGISTER SIZE VIOLATIONS: {len(violations)}]")
    for path, tokens, limit in violations:
        print(f"  {path}: {tokens:,} tokens exceeds {limit:,} limit")
        print(f"    Action: archive resolved/applied/struck content to the _archive file")
        print(f"    Ref: register chunking protocol in orchestrator SKILL.md")
    sys.exit(1)
else:
    print("All register sizes within limits.")
    sys.exit(0)
