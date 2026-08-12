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
  6. The self-scheduling deny-list is intact in .claude/settings.json, and
     CLAUDE.md still documents the no-polling rule (ED-IN-0084). This is the
     recurrence guard for the measured 2026-07-19..26 incident: 116 hourly
     `send_later` self check-ins re-entered persistent sessions to re-confirm
     already-green PRs. Deleting a deny entry silently restores an ~23k-token
     floor per wake-up, so the deny-list gets a gate rather than a convention.
Non-blocking warnings:
  - lingering /home/claude sandbox references under tools/ (analysis utilities
    pending the GitHub-API->working-tree port; tracked in HANDOFF.md).
  - design-doc skeleton-debt (>400 lines).
"""
import glob
import os
import sys

# ONE OWNER for the repo root, the 9-lane roster, token estimation and the id
# regexes: tools/ci_common.py (plan G7, ED-IN-0159 §8.3). The two lines below are
# the irreducible bootstrap — a module cannot import its owner without first
# knowing where the owner is — and they anchor on THIS FILE's directory, never on
# the repo root, so they are not the duplication they replace.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

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
        tokens = ci_common.tokens(f.read())
    if tokens > DEFAULT_SKILL_LIMIT:
        warnings.append(f"SKILL LARGE: {skill_md.replace(os.sep, '/')}: {tokens:,} tokens "
                        f"(soft limit {DEFAULT_SKILL_LIMIT:,})")
    else:
        print(f"OK   size {skill_md}: {tokens:,}/{DEFAULT_SKILL_LIMIT:,} tokens")

# ── Check 4: lingering /home/claude sandbox references ───────────────────────
# SUBSTRING MATCHING MADE THIS CHECK 4/4 FALSE (fixed 2026-08-01). It flagged any file
# CONTAINING the literal path, so it fired on:
#   - ci_hooks_verifier.py — ITSELF, on its own comments describing this very check
#   - freshness_gate.py    — a comment recording that it USED to use the path and no longer does
#   - ci_sim_fabrication_check.py — the line "No GitHub API, no PAT, no /home/claude, no network",
#                            i.e. flagged for explicitly declaring it does not use it
#   - build_apparatus_registry.py — `not w["dest"].startswith("/home/claude")`, a filter that
#                            EXCLUDES the path
# Zero were live dependencies, and the warning had therefore been permanently on. A signal that is
# always red is a signal nobody reads — the same defect as the binary register-size check fixed the
# same day, and the same shape as retired Check 5, which scanned a deleted directory and reported
# clean for months.
#
# The check now asks the question it always meant: WOULD THIS FILE BREAK OUTSIDE THE SANDBOX?
# Comments and docstrings cannot break, so they are stripped before matching. A reference that
# appears only inside a negated guard is an exclusion, not a dependency, and is also not a break.
def _live_sandbox_ref(txt, fn, rel):
    """True only if `/home/claude` survives as EXECUTABLE, non-negated code.

    STRUCTURE, NOT LINE TEXT. The first version of this fix matched on the raw source line:
    it dropped a hit when the line started with a quote (assumed docstring) or contained
    `'not '` (assumed exclusion filter). An adversarial pass found both to be FALSE
    NEGATIVES, which is strictly worse than the false positives being fixed — a false
    positive is noise, a false negative is a live sandbox dependency reported clean:

      CACHE = "/home/claude/x.json"   # note: not portable    -> dropped by the 'not ' rule
      MSG = (\n    "prefix "\n    "/home/claude/tail"\n)      -> continuation line starts
                                                                 with a quote, read as a docstring

    Both are decidable from the AST and neither is decidable from the line. Comments do not
    appear in the AST at all, so they need no rule. A docstring is structurally the first
    statement of a module/def/class. An exclusion is structurally a string under a `not`
    (or a `NotIn` comparison), not a string on a line containing the letters n-o-t.

    Fails CLOSED on unparseable Python: an unparseable file is not evidence of cleanliness.
    """
    if '/home/claude' not in txt:
        return False
    if fn.endswith('.md'):
        # MARKDOWN KEEPS THE OLD SUBSTRING RULE, and that is deliberate. An earlier version of
        # this fix returned False for every `.md` on the reasoning that markdown "has no
        # executable surface". That silently gutted the BLOCKING half of the check: the rule at
        # the top of this file is "no /home/claude under skills/", and a skill's primary surface
        # IS its SKILL.md — prose that instructs an agent to read a retired sandbox path is
        # exactly the violation, and it is the instruction that executes. skills/ happens to be
        # clean today, so nothing broke; the GUARD would have been gone.
        return True
    if rel == 'tools/ci_hooks_verifier.py':
        # This file necessarily contains the literal it searches for — in the WARNING TEXT it
        # prints. A checker that reports itself for quoting its own error message is a false
        # positive by construction, not a dependency; it cannot be fixed by editing the file,
        # only by not asking. Scoped to this exact path so the exemption cannot silently
        # generalise to another tool.
        return False
    import ast
    try:
        tree = ast.parse(txt)
    except (SyntaxError, ValueError):
        return True   # fail CLOSED

    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, 'body', None)
            if body and isinstance(body[0], ast.Expr) and \
                    isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
                docstrings.add(id(body[0].value))

    # NEGATION ALONE IS NOT EXCLUSION. An earlier version dropped every string under any `not`,
    # which reported these LIVE dependencies clean:
    #     if not os.path.exists('/home/claude/cache'): sys.exit(1)
    #     while not os.path.isdir('/home/claude/x'): ...
    # Both negate a FILESYSTEM ACCESS to the path — the strongest possible dependency on it.
    # An exclusion negates a CLASSIFICATION of some other value: `not dest.startswith(PATH)` or
    # `PATH not in dest` ask "is that thing under the sandbox", and work fine with the sandbox
    # absent. So the test is what the negation wraps, not that a negation exists.
    _CLASSIFIERS = {'startswith', 'endswith'}
    excluded = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare) and any(isinstance(o, ast.NotIn) for o in node.ops):
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                    excluded.add(id(sub))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            for call in ast.walk(node):
                if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) \
                        and call.func.attr in _CLASSIFIERS:
                    for sub in ast.walk(call):
                        if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                            excluded.add(id(sub))
    negated = excluded

    for node in ast.walk(tree):
        if not (isinstance(node, ast.Constant) and isinstance(node.value, str)):
            continue
        if '/home/claude' not in node.value:
            continue
        if id(node) in docstrings or id(node) in negated:
            continue
        return True
    return False


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
            rel = p.replace(os.sep, '/')
            if not _live_sandbox_ref(txt, fn, rel):
                continue
            if base == 'skills':
                violations.append(f"SANDBOX REF: {rel} references /home/claude — "
                                  f"skills must read the working tree (retired harness)")
            else:
                warnings.append(f"SANDBOX REF: {rel} still references /home/claude "
                                f"(port to working-tree reads)")

# ── Check 5: RETIRED 2026-07-28 (ED-IN-0088) — the rule already lives once, elsewhere ─────
# It walked `designs/`, retired 2026-07-19, so it had scanned nothing since PR #191 and reported
# clean. The obvious repair was to repoint it at `systems/`. That would have been WRONG twice over:
#
#   1. Its rule was superseded. Both its advice ("extract prose to *_infill.md") and its threshold
#      (400 lines) encode the index+infill convention CLAUDE.md §4 RETIRED on 2026-07-26 in favour
#      of sequential `_partN` splits at ~15k tokens. Repointing as-is would have emitted 29 warnings
#      recommending a practice the repo had just abandoned.
#   2. Its rule is not its own. `tools/compliance_check.py` reads `references/atomization_rules.yaml`
#      — the single owner of the threshold — applies the live 15,000-token cap, and already reports
#      every oversized doc under `systems/`. Verified by hand: all 8 actionable docs the correct rule
#      identifies (41.7k faction_politics_v30 down to 15.3k integration_proposal_v30) appear in
#      compliance_check's 55 size warnings. Reviving a second implementation would be a fresh §8
#      violation ("Never re-implement a rule") committed while cleaning up after other ones.
#
# So the check is GONE, not repointed and not left inert. `compliance_check --check-only
# --repo-state .` is the owner and is already a blocking CI job.
# Falsifier: tests/valoria/test_retired_tree_apparatus.py asserts compliance_check still reports the
# oversized systems/ docs, so the coverage this deletion relies on cannot vanish unnoticed.

# ── Check 6: self-scheduling deny-list intact ────────────────────────────────
# ED-IN-0084. The waste class is a session that re-arms its own wake-up: each
# firing re-sends the whole conversation, and CLAUDE.md alone is ~12k tokens, so
# an empty-conversation wake-up still costs ~23k. The deny-list in
# .claude/settings.json is the single owner of "this repo does not self-schedule";
# this check is the guard that fails if an entry is dropped.
REQUIRED_DENY = (
    'send_later',      # claude-code-remote: the PR self-check-in primitive
    'create_trigger',  # claude-code-remote: send_later's underlying Routine API
    'ScheduleWakeup',  # /loop dynamic self-pacing
    'CronCreate',      # /loop fixed-interval scheduling
    # --- widened 2026-07-28 (ED-IN-0087) ---------------------------------------------
    # ED-IN-0084 pinned the four primitives that were *known* then, and wrote its own
    # falsifier as: "if a session ever schedules a wake-up while these pass, find the new
    # primitive and add it to REQUIRED_DENY." That is exactly what happened — ED-IN-0085
    # found three live route-arounds still reachable in-session:
    'update_trigger',  # re-enables / re-crons an EXISTING Routine, so a session that cannot
                       # create one can still arm a disabled one — create_trigger's twin
    'fire_trigger',    # fires a Routine on demand; the Routine's own prompt can re-arm, so
                       # this is a one-hop path back into the chain create_trigger blocks
    'Skill(loop)',     # the /loop skill runs a prompt on a recurring interval in-session —
                       # the same polling behaviour, reached through the skill surface rather
                       # than a scheduling tool. ScheduleWakeup/CronCreate deny /loop's
                       # pacing primitives; this denies its entry point.
)
if os.path.exists(SETTINGS):
    import json
    try:
        with open(SETTINGS, encoding='utf-8') as f:
            cfg = json.load(f)
    except (OSError, ValueError) as e:
        violations.append(f"{SETTINGS}: unparseable JSON ({e})")
        cfg = None
    if cfg is not None:
        deny = cfg.get('permissions', {}).get('deny', [])
        if not isinstance(deny, list):
            violations.append(f"{SETTINGS}: permissions.deny is not a list")
            deny = []
        blob = '\n'.join(str(d) for d in deny)
        missing = [t for t in REQUIRED_DENY if t not in blob]
        if missing:
            violations.append(
                f"{SETTINGS}: permissions.deny is missing self-scheduling "
                f"primitive(s): {', '.join(missing)} — ED-IN-0084 forbids "
                f"sessions arming their own wake-ups (CLAUDE.md §11)")
        else:
            print(f"OK   {SETTINGS}: self-scheduling deny-list intact "
                  f"({len(REQUIRED_DENY)} primitives)")

if os.path.exists('CLAUDE.md'):
    if 'does not self-schedule' not in c:
        violations.append("CLAUDE.md: §11 no-polling rule missing "
                          "(expected the 'does not self-schedule' statement) — ED-IN-0084")
    else:
        print("OK   CLAUDE.md: documents the no-polling rule (§11)")

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
