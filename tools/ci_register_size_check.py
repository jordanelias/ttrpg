#!/usr/bin/env python3
"""
ci_register_size_check.py
Runs in CI (GitHub Actions) against the checked-out repo.
Fails if any governed file exceeds its token threshold.
This is the external enforcement gate — runs outside Claude, cannot be bypassed.
"""
import os, sys

ATOMIZATION_RULES = "references/atomization_rules.yaml"


def yaml_max_tokens(match_path, rules_file=ATOMIZATION_RULES):
    """Read the `max_tokens` for a `- match: "<match_path>"` block from the
    atomization-rules policy file, without a YAML dependency (consistent with the
    no-PyYAML-in-validators convention, cf. ci_vetting_check.py). Returns int or
    None if the file or entry is absent. This keeps a single source of truth for
    thresholds that are also declared in the policy file."""
    if not os.path.exists(rules_file):
        return None
    target = f'match: "{match_path}"'
    in_block = False
    with open(rules_file, encoding='utf-8', errors='replace') as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith('- match:'):
                in_block = target in stripped
                continue
            if in_block and stripped.startswith('max_tokens:'):
                try:
                    return int(stripped.split(':', 1)[1].split('#', 1)[0].strip())
                except ValueError:
                    return None
    return None


# Single-sourced from references/atomization_rules.yaml; falls back to the
# inline default only if the policy entry is missing.
COVERAGE_MATRIX_LIMIT = yaml_max_tokens("tests/coverage_matrix.md") or 10_000
# Same single-sourcing for the patch register. The old hardcoded 20_000 had drifted
# above the policy file's 15_000 — two gates, one file, two limits. Read the cap from
# the policy so they cannot diverge again. (Live register is ~5k tokens, well under both.)
PATCH_REGISTER_LIMIT = yaml_max_tokens("canon/patch_register_active.yaml") or 15_000

THRESHOLDS = {
    # ── Active registers (strict limits — must chunk before exceeding) ──────
    # session_log_current.md / session_logs/index.md entries removed 2026-07-01 (ED-1084):
    # the retired session-log machinery moved to deprecated/session_machinery/ and is frozen.
    # editorial store + file index moved to JSONL/SQL (2026-05-28 cutover);
    # editorial_ledger.jsonl is checked soft below; valoria_index.sql is generated.
    # Interim: bumped 5_000 -> 12_000 to match the sanctioned interim cap in
    # g.TOKEN_THRESHOLDS (633f5e57; canonical_sources rode 9k->12k pending the
    # freshness SHA-split, roadmap K-2 / workplan LB-6). Returns to 5_000 when
    # the 115 canonical_sha fields move to references/canonical_freshness.yaml.
    "references/canonical_sources.yaml":      12_000,
    # Single-sourced from references/atomization_rules.yaml (PATCH_REGISTER_LIMIT) so the
    # validator and the policy file can't drift (was hardcoded 20_000 vs policy 15_000).
    "canon/patch_register_active.yaml":   PATCH_REGISTER_LIMIT,
    # Single-sourced from references/atomization_rules.yaml (COVERAGE_MATRIX_LIMIT).
    # coverage_matrix grows naturally as test coverage expands; adjust the cap in
    # the policy file (one place) and this validator follows. Drift between the two
    # is caught by tests/valoria/test_coverage_matrix_threshold.py.
    "tests/coverage_matrix.md":   COVERAGE_MATRIX_LIMIT,
    "references/arc_register.md":            20_000,
    "references/propagation_map.md":         15_000,
    "references/design_registry.yaml":        8_000,
    "references/names_index.yaml":            8_000,  # unified names index (the one place a name lives)
    # ── Archives (soft limits — warn when approaching split threshold) ──────
    # These are large by design; alert when year-split is needed
    "canon/patch_register_archive.yaml":     100_000,
    "canon/editorial_ledger.jsonl":         150_000,  # live append-only editorial store (post-2026-05-28 cutover); large by design
    "archives/session/session_log_archive_part_7.md": 100_000,
    "canon/patch_register_index.md":         20_000,
}

def main():
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
            print(f"    Ref: register chunking protocol in CLAUDE.md")
        sys.exit(1)
    else:
        print("All register sizes within limits.")
        sys.exit(0)


if __name__ == '__main__':
    main()
