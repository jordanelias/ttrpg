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
PATCH_REGISTER_LIMIT = yaml_max_tokens("registers/patch_register_active.yaml") or 15_000
# Third instance of the SAME defect this file already fixed twice above (ED-IN-0097, W4):
# module_contracts.yaml's cap was hardcoded 18_000 here while the policy file declared its own
# — two gates, one file, two limits. The W4 OI-54 join raised the policy cap to 24_000 and this
# hardcoded copy kept failing, which is exactly how the drift announces itself. Single-sourced.
MODULE_CONTRACTS_LIMIT = yaml_max_tokens("references/module_contracts.yaml") or 18_000

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
    "registers/patch_register_active.yaml":   PATCH_REGISTER_LIMIT,
    # Single-sourced from references/atomization_rules.yaml (COVERAGE_MATRIX_LIMIT).
    # coverage_matrix grows naturally as test coverage expands; adjust the cap in
    # the policy file (one place) and this validator follows. Drift between the two
    # is caught by tests/valoria/test_coverage_matrix_threshold.py.
    "tests/coverage_matrix.md":   COVERAGE_MATRIX_LIMIT,
    "arcs/registers/arc_register.md":            20_000,
    "references/propagation_map.md":         15_000,
    "references/names_index.yaml":            8_000,  # unified names index (the one place a name lives)
    # ── Previously-uncapped large registers (added 2026-07-20, ED-IN-0077 data-mgmt review) ──
    # Growth caps with headroom over current size; values_master is known-stale (do not grow it).
    "references/values_master.yaml":         40_000,  # quarantined stale snapshot (ED-IN-0029) — cap so it can't grow
    "references/id_reservations.yaml":       15_000,  # the ID-allocation source of truth
    # Single-sourced from references/atomization_rules.yaml (MODULE_CONTRACTS_LIMIT) — see above.
    "references/module_contracts.yaml":      MODULE_CONTRACTS_LIMIT,  # the 27-module I/O spine
    "references/definitions/definitions.yaml": 8_000,  # generated unified definitions store (ED-IN-0077)
    # ── Archives (soft limits — warn when approaching split threshold) ──────
    # These are large by design; alert when year-split is needed
    "registers/patch_register_archive.yaml":     100_000,
    "registers/editorial_ledger.jsonl":         150_000,  # live append-only editorial store (post-2026-05-28 cutover); large by design
    # Overflow chunk for registers/editorial_ledger.jsonl (2026-07-02, first split — settled
    # resolved/struck/superseded/applied entries ED-001..ED-330; 2026-07-07 second split,
    # user-approved during the Key & Echo armature ratification pass — the active ledger had
    # drifted to 152,202 tokens against the 150,000 cap, so the next batch of terminal-status
    # flat entries, ED-331..ED-759, moved here to restore headroom). Mirrors the
    # patch_register_active/archive co-location convention. Recognized by
    # tools/validate_ed_citations.py ARCHIVE_JSONL_PATHS so archived-ED citations still
    # resolve. Soft limit matches the active ledger's own cap.
    "registers/editorial_ledger_archive.jsonl": 150_000,
    # Per-lane active ledgers (2026-07-08 atomization pass): ED-<LANE>-NNNN entries split
    # out of registers/editorial_ledger.jsonl by lane, mirroring registers/handoffs/HANDOFF_<LANE>.md.
    # Generous headroom — each lane starts small (largest today, IN, is ~34 entries) but
    # this is a live append-only store like its parent, not a fixed-size snapshot.
    "registers/editorial_ledger_mb.jsonl": 50_000,
    "registers/editorial_ledger_pc.jsonl": 50_000,
    "registers/editorial_ledger_fi.jsonl": 50_000,
    "registers/editorial_ledger_sc.jsonl": 50_000,
    "registers/editorial_ledger_fa.jsonl": 50_000,
    "registers/editorial_ledger_wr.jsonl": 50_000,
    "registers/editorial_ledger_in.jsonl": 50_000,
    "registers/editorial_ledger_go.jsonl": 50_000,
    "registers/editorial_ledger_se.jsonl": 50_000,
    # Per-lane ARCHIVE overflow (ED-IN-0075, IN was the first lane to reach its 50k cap):
    # resolved/superseded entries move here from the live lane ledger; still loaded into the
    # ED universe by tools/validate_ed_citations.py (globs editorial_ledger_*_archive.jsonl),
    # so archived-ED citations keep resolving. Large cap like the flat editorial archive.
    "registers/editorial_ledger_in_archive.jsonl": 150_000,
    # [ED-MB-0051, 2026-07-29] MB lane archive — same 150k overflow ceiling as the IN sibling.
    "registers/editorial_ledger_mb_archive.jsonl": 150_000,
    # PC was the THIRD lane to reach its 50k cap (ED-PC-0050, 2026-07-29), during the E0-E3
    # combat-correctness arc. Same convention as the IN archive above: settled entries
    # (status resolved/ratified, needs_jordan not True) move here; anything open, deferred,
    # or still awaiting Jordan stays in the live lane ledger.
    # NOTE the MB sibling above landed independently on main the same day — three lanes crossed
    # the 50k cap within a week, so this is now a recurring pattern rather than a one-off. Adding
    # the cap by hand each time is the manual step; a per-lane default would retire it.
    "registers/editorial_ledger_pc_archive.jsonl": 150_000,
    # Audit/simulation-run verdict registry (added with the GitHub Pages dashboard,
    # 2026-07-11): one JSONL line per completed audit/simulation-balance run, appended
    # by 8 skills (valoria-canon-guard, -mechanic-audit, -resolution-diagnostic,
    # -module-adjudicator, -vector-audit, -editorial-register, -combat-simulator,
    # -simulator). Same append-only shape as the editorial ledger; generous headroom
    # since audit cadence is far lower than editorial-decision cadence.
    "references/audit_registry.jsonl": 50_000,
    "deprecated/archives/session/session_log_archive_part_7.md": 100_000,
    "registers/patch_register_index.md":         20_000,
}

# ── Early warning (ED-MB-0063 residual, 2026-08-01) ───────────────────────────
# THE PATTERN THIS EXISTS FOR. Registers approach their caps SILENTLY: output was
# binary OK/FAIL, so a file at 99% of its cap printed the same "OK" as one at 10%.
# The first signal was therefore a BLOCKING failure on whichever PR happened to add
# the next entry — structurally, someone other than whoever grew the file.
#
# Measured 2026-08-01, all three found in one session and all three already over 95%:
#   registers/editorial_ledger_mb.jsonl   49,260 / 50,000   98.5%   (740 tokens left)
#   registers/editorial_ledger_in.jsonl   47,602 / 50,000   95.2%
#   tests/coverage_matrix.md              14,655 / 15,000   97.7%
#
# WARN is REPORT-ONLY and must stay that way. A blocking warn is just a lower cap,
# which re-creates the same cliff a few thousand tokens earlier; the point is to move
# the cost onto the session doing the growing, not to add a second wall.
WARN_FRACTION = 0.85


def main():
    violations = []
    warnings = []
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
        elif tokens >= threshold * WARN_FRACTION:
            warnings.append((path, tokens, threshold))
            print(f"WARN {path}: {tokens:,} / {threshold:,} tokens "
                  f"({tokens / threshold:.0%} of cap — archive settled entries soon)")
        else:
            print(f"OK   {path}: {tokens:,} / {threshold:,} tokens")

    print(f"\nChecked {checked} files.")
    if warnings:
        print(f"\n[APPROACHING CAP: {len(warnings)} file(s) at or above "
              f"{WARN_FRACTION:.0%}] — report-only, this does not fail the gate.")
        for path, tokens, limit in warnings:
            print(f"  {path}: {tokens:,} / {limit:,} ({limit - tokens:,} tokens of headroom)")
        print("    Action: archive WHOLE settled ids to the _archive file — never individual")
        print("    rows. The ledgers are append-only, so an id's effective status is its LAST")
        print("    row; moving only the resolved row silently reverts it (ED-IN-0112 incident,")
        print("    pinned by tests/valoria/test_ledger_hygiene.py).")
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
