"""
compliance_dryrun.py — Dry-run the compliance auto-fix logic against current repo state.

Fetches current state, runs check_all, runs auto_fix with session_commit=False,
writes proposed additions to /tmp/dryrun_output/, generates report.

Usage:
    python3 tools/compliance_dryrun.py
"""

import sys, os, json
sys.path.insert(0, '/home/claude')
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import github_ops as g
import compliance_check as cc


def main():
    print("=" * 60)
    print("COMPLIANCE DRY-RUN")
    print("=" * 60)

    # Step 1: Run check_all
    print("\n[1/4] Scanning repo for violations...")
    violations = cc.check_all()

    if not violations:
        print("[DRY-RUN ✓] No violations found. Repo is compliant.")
        return

    print(f"\n[2/4] Found {len(violations)} violation(s):")
    print(cc.report(violations))

    auto_fixable = [v for v in violations if v.auto_fixable]
    manual = [v for v in violations if not v.auto_fixable]

    print(f"  Auto-fixable: {len(auto_fixable)}")
    print(f"  Manual:       {len(manual)}")

    if not auto_fixable:
        print("\n[DRY-RUN] No auto-fixable violations. Manual intervention required.")
        return

    # Step 3: Run auto_fix
    print(f"\n[3/4] Running auto_fix (dry-run, no commit)...")
    additions, msg = cc.auto_fix(auto_fixable, session_commit=False)

    print(f"  Commit message: {msg}")
    print(f"  Files to create/update: {len(additions)}")

    # Step 4: Write to output directory
    output_dir = '/tmp/dryrun_output'
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n[4/4] Writing proposed changes to {output_dir}/")

    manifest = []
    for path, content in additions:
        safe_path = path.replace('/', '_')
        out_file = os.path.join(output_dir, safe_path)
        with open(out_file, 'w') as f:
            f.write(content)
        tokens = len(content) // 4
        manifest.append({
            'repo_path': path,
            'local_file': safe_path,
            'tokens': tokens,
            'chars': len(content),
        })
        print(f"  {path} ({tokens:,} tokens)")

    # Write manifest
    manifest_path = os.path.join(output_dir, '_manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump({
            'violations_found': len(violations),
            'auto_fixed': len(auto_fixable),
            'manual_remaining': len(manual),
            'commit_message': msg,
            'files': manifest,
        }, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"DRY-RUN COMPLETE")
    print(f"{'=' * 60}")
    print(f"  Violations: {len(violations)}")
    print(f"  Auto-fixed: {len(auto_fixable)} → {len(additions)} file(s)")
    print(f"  Manual:     {len(manual)}")
    print(f"  Output:     {output_dir}/")
    print(f"  Manifest:   {manifest_path}")
    print(f"\nReview output files before running Phase 1.")

    if manual:
        print(f"\n⚠ MANUAL VIOLATIONS ({len(manual)}):")
        for v in manual:
            print(f"  {v}")


if __name__ == "__main__":
    main()
