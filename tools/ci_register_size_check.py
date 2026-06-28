#!/usr/bin/env python3
"""
ci_register_size_check.py
Runs in CI (GitHub Actions) against the checked-out repo.
Fails if any governed file exceeds its token threshold.
This is the external enforcement gate — runs outside Claude, cannot be bypassed.
"""
import os, sys

# Single source of truth for the coverage-matrix cap: references/atomization_rules.yaml
# (the declarative atomizer spec the local compliance gate already reads). Sourcing it
# here removes the duplicated literal that drifted once (8000 vs 10000, 2026-06-24).
# Falls back to a hardcoded value so this unbypassable CI gate never crashes on a
# missing/unparseable rules file.
_COVERAGE_MATRIX_FALLBACK = 10_000


def _coverage_matrix_threshold(
    rules_path="references/atomization_rules.yaml",
    match="tests/coverage_matrix.md",
    fallback=_COVERAGE_MATRIX_FALLBACK,
):
    """Read the coverage_matrix max_tokens from atomization_rules.yaml; fall back on any error."""
    try:
        import yaml
        with open(rules_path, encoding="utf-8") as f:
            rules = yaml.safe_load(f)
        for policy in (rules or {}).get("policies", []):
            if policy.get("match") == match:
                mt = policy.get("max_tokens")
                if isinstance(mt, int):
                    return mt
    except Exception as e:
        print(f"NOTE: coverage_matrix threshold falling back to {fallback:,} ({type(e).__name__}: {e})")
    return fallback


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
    "canon/patch_register_active.yaml":       20_000,
    # coverage_matrix cap sourced from references/atomization_rules.yaml (single source —
    # 2026-06-28 consolidation). Was independently set 10_000 here AND in the yaml; the
    # literal drifted once (8000 vs 10000). To change it, edit the yaml policy only.
    "tests/coverage_matrix.md":              _coverage_matrix_threshold(),
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
