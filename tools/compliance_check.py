"""
compliance_check.py — Valoria compliance orchestrator.

Called by hooks. Reads atomization_rules.yaml, checks repo state, dispatches fixes.
Two modes:
  1. CI mode: `--check-only --repo-state .` — local working-tree size caps (the BLOCKING gate)

Dependencies: PyYAML.

ORCHESTRATOR HALF EXCISED 2026-08-05 (ED-IN-0145). This module used to carry check_all /
validate_commit / auto_fix / find_index_for, every one of which required `/home/claude` on
sys.path plus a GITHUB_PAT, and whose only callers lived under `deprecated/`. Its `import
github_ops` was the LAST live reference from the non-deprecated tree into the retired
orchestrator, and it made a BLOCKING CI gate transitively depend on four files in `deprecated/` —
which is what the W3 deletion rehearsal surfaced. The CI path (`--check-only --repo-state .`)
never called any of it. Removing it cost zero live functionality and unanchored `deprecated/`.
"""

import sys, os, re, fnmatch

import yaml

# ONE OWNER for the repo root, the 9-lane roster, token estimation and the id
# regexes: tools/ci_common.py (plan G7, ED-IN-0159 §8.3). The two lines below are
# the irreducible bootstrap — a module cannot import its owner without first
# knowing where the owner is — and they anchor on THIS FILE's directory, never on
# the repo root, so they are not the duplication they replace.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

from dataclasses import dataclass, field

@dataclass
class Violation:
    path: str
    rule: dict
    kind: str           # 'size_exceeded' | 'missing_index' | 'stale_index' |
                        # 'missing_index' | 'archive_needed' | 'unknown_pattern'
    current_tokens: int
    threshold: int
    auto_fixable: bool
    fix_action: str     # 'atomizer.atomize' | 'doc_index_gen.generate_index' | etc.
    fix_args: dict = field(default_factory=dict)
    severity: str = 'error'  # 'error' | 'warn' | 'info'

    def __str__(self):
        return (f"[{self.severity.upper()}] {self.kind}: {self.path} "
                f"({self.current_tokens:,} tokens, threshold {self.threshold:,})")


# ── Rules loading ────────────────────────────────────────────────────────────

def _match_rule(path: str, rules: dict) -> dict | None:
    """First-match policy lookup using fnmatch patterns."""
    policies = rules.get('policies', [])
    for policy in policies:
        pattern = policy.get('match', '')
        # Check exclude_suffix
        excludes = policy.get('exclude_suffix', [])
        if any(path.endswith(suffix) for suffix in excludes):
            continue
        if fnmatch.fnmatch(path, pattern):
            return policy
        # fnmatch is not path-aware: "*" and "**" both translate to ".*", so a
        # leading "**/" pattern requires a literal "/" somewhere in the candidate
        # to match. That silently exempts every root-level file (HANDOFF.md,
        # CURRENT.md, README.md, ...) from any "**/*.ext" catch-all. Also try the
        # pattern with the leading "**/" stripped so root files reach the same policy.
        if pattern.startswith('**/') and fnmatch.fnmatch(path, pattern[3:]):
            return policy
    return None


# ── Check functions ──────────────────────────────────────────────────────────

# ── on_exceed severity vocabulary — the SINGLE owner (ED-IN-0098, 2026-07-30) ───────────────
#
# WHY THIS EXISTS. The severity used to be computed inline as
#     severity = 'warn' if on_exceed.startswith('flag') else 'error'
# which silently graded EVERY token outside the `flag*` family as a blocking error — including
# `warn_only`, which references/atomization_rules.yaml declares on 12 files and whose whole
# purpose is to NOT block, and `chunk_by_quarter`, which is a split strategy rather than a
# severity at all. Neither had ever worked. It surfaced in W4 (ED-IN-0097) when a legitimate
# growth in module_contracts.yaml tripped a blocking gate that its own policy entry had already
# declared non-blocking; that wave raised the cap to route around it and filed this defect
# instead of fixing it, because the vocabulary sits adjacent to another program's scope.
#
# The fix is a CLOSED vocabulary. An unrecognised token is now a LOUD error naming itself,
# rather than a silent demotion to 'error' that is indistinguishable from a deliberate block.
# That is the §0.1 #5 shape: one owner, every site through it, and a guard that fails on
# recurrence (tests/valoria/test_compliance_on_exceed_vocabulary.py).
ON_EXCEED_BLOCKING = frozenset({
    'error',          # explicit: exceeding this cap is a hard failure
    'block_commit',   # explicit: block the commit (auto-fixable path)
})
ON_EXCEED_ADVISORY = frozenset({
    'warn_only',              # declared on 12 files; report but never block
    'flag_for_split',         # the flag* family: surface for a human/atomizer decision
    'flag_unknown_pattern',
    'flag_for_next_session',
    'flag_for_manual_archive',
    'chunk_by_quarter',       # a SPLIT STRATEGY, not a severity — advisory, never blocking
})
# 'skip' is handled before severity is computed (it produces no violation at all).
ON_EXCEED_KNOWN = ON_EXCEED_BLOCKING | ON_EXCEED_ADVISORY | frozenset({'skip'})


class UnknownOnExceedToken(ValueError):
    """Raised when atomization_rules.yaml declares an on_exceed value nothing implements."""


def _on_exceed_severity(on_exceed: str, path: str) -> str:
    """Map an `on_exceed` token to 'warn' | 'error'. Unknown tokens fail LOUDLY.

    A typo previously became a blocking error indistinguishable from an intentional one, which
    is how `warn_only` went unimplemented for weeks across 12 files.
    """
    if on_exceed in ON_EXCEED_BLOCKING:
        return 'error'
    if on_exceed in ON_EXCEED_ADVISORY:
        return 'warn'
    raise UnknownOnExceedToken(
        f"references/atomization_rules.yaml declares on_exceed: {on_exceed!r} for {path!r}, but "
        f"tools/compliance_check.py implements no such token. Known: "
        f"{sorted(ON_EXCEED_KNOWN)}. Add it to ON_EXCEED_BLOCKING or ON_EXCEED_ADVISORY (with a "
        f"reason) rather than letting it default — an unimplemented token silently graded as a "
        f"blocking error is the ED-IN-0098 defect this exception exists to prevent.")


# ── Check functions ──────────────────────────────────────────────────────────
#
# THE REST OF THIS SECTION WAS EXCISED 2026-08-12 (plan step G1, ED-IN-0159 §1.5).
#
# `_check_size`, `_check_index`, `_check_archive_pressure` and `report` were the
# check/report half of the orchestrator removed on 2026-08-05 (ED-IN-0145). Their
# only caller was `check_all()`, which went with it — so for a week this BLOCKING
# GATE'S FILE carried four functions nothing could reach, two of which could not
# even run:
#
#   $ python3 tools/compliance_check.py
#     NameError: name 'check_all' is not defined
#
# `_check_index` was the worse of the two. It called `_lazy_import()` and
# `_doc_index_gen`, NEITHER OF WHICH IS DEFINED ANYWHERE IN THE TREE, and it
# branched on `require_index_above` — a key that does not exist in
# `references/atomization_rules.yaml`, whose rule uses `require_skeleton_above`
# (§1.6). Dead code reading a policy key that was never written.
#
# WHAT SURVIVES IS THE WHOLE LIVE GATE. The CI mode (`--check-only --repo-state .`)
# is fully inline below and called none of this; that is precisely why the rot went
# unnoticed. `_match_rule`, `_on_exceed_severity`, the `on_exceed` vocabulary and
# `Violation` are all still here because the live path uses every one of them.
#
# Expected delta: none. `tests/valoria/test_gate_coverage.py:131` pins the gate's
# invocation, and the working-tree scan reports the same 48 warnings / 0 errors
# before and after.


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Valoria compliance checker")
    parser.add_argument('--check-only', action='store_true',
                        help="Check and report, exit nonzero on violations")
    parser.add_argument('--repo-state', default=None,
                        help="Path to local repo checkout (for CI)")
    args = parser.parse_args()

    if args.repo_state:
        # CI mode: check local files instead of GitHub API
        print("[COMPLIANCE] CI mode — checking local repo state")
        # Load rules from local file
        rules_path = os.path.join(args.repo_state, 'references', 'atomization_rules.yaml')
        if not os.path.isfile(rules_path):
            print("[COMPLIANCE] No atomization_rules.yaml found — skipping")
            sys.exit(0)

        rules = ci_common.load_yaml(rules_path)

        violations = []
        # Walk local files
        for root, dirs, files in os.walk(args.repo_state):
            for fname in files:
                if not (fname.endswith('.md') or fname.endswith('.yaml')):
                    continue
                full_path = os.path.join(root, fname)
                rel_path = os.path.relpath(full_path, args.repo_state)
                rule = _match_rule(rel_path, rules)
                if not rule:
                    continue
                with open(full_path) as f:
                    content = f.read()
                max_tokens = rule.get('max_tokens')
                if max_tokens and ci_common.tokens(content) > max_tokens:
                    on_exceed = rule.get('on_exceed', 'error')
                    # ED-IN-0098: this CI-mode path carried its OWN copy of the severity rule and
                    # had DIVERGED from _check_size above — it never honoured 'skip', so an
                    # explicitly-exempted file over its cap graded as a blocking error here while
                    # the same file was exempt on the other path. Both now route through the single
                    # owner, _on_exceed_severity, and 'skip' is honoured identically.
                    if on_exceed == 'skip':
                        continue
                    severity = _on_exceed_severity(on_exceed, rel_path)
                    violations.append(Violation(
                        path=rel_path, rule=rule, kind='size_exceeded',
                        current_tokens=ci_common.tokens(content), threshold=max_tokens,
                        auto_fixable=False, fix_action='',
                        severity=severity,
                    ))

        if violations:
            errors = [v for v in violations if v.severity == 'error']
            warns = [v for v in violations if v.severity == 'warn']
            if warns:
                print(f"[COMPLIANCE ⚠] {len(warns)} warning(s):")
                for v in warns:
                    print(f"  {v}")
            if errors:
                print(f"[COMPLIANCE ✗] {len(errors)} error(s):")
                for v in errors:
                    print(f"  {v}")
                sys.exit(1)
            else:
                print(f"[COMPLIANCE ✓] {len(warns)} warning(s), 0 errors")
                sys.exit(0)
        else:
            print("[COMPLIANCE ✓] All files within thresholds")
            sys.exit(0)
    else:
        # There is no second mode. The interactive path called `check_all()` and
        # `report()`, both excised with the orchestrator (ED-IN-0145) — so running
        # this file without --repo-state raised NameError rather than doing
        # anything. Say so and exit cleanly instead of pretending.
        print("[COMPLIANCE] --repo-state is required; the interactive/orchestrator "
              "mode was excised 2026-08-05 (ED-IN-0145). "
              "Use: compliance_check.py --check-only --repo-state .", file=sys.stderr)
        sys.exit(2)
