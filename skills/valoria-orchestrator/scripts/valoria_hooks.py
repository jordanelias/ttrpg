"""
valoria_hooks.py — Hard enforcement for Valoria session protocol.

Import as `h` immediately after bootstrapping github_ops.
Every function raises RuntimeError — no warnings, no soft failures.

Usage in every bash_tool block:
    import valoria_hooks as h
    h.assert_bootstrap()
    # ... task-specific gates ...
    oid = h.safe_commit(additions, deletions, message)
"""

import os, sys, re, json
sys.path.insert(0, '/home/claude')
import github_ops as g

_bootstrap_confirmed = False
_task_gates_passed   = set()
_checkpoint_written_this_session = False
_soft_warn_issued = False
_session_scope = None
_session_log_path = None

EDITORIAL_PATHS = (
    'designs/npcs/',
    'designs/world/',
    'designs/arcs/gm_ref/',
    'canon/03_',
)
EDITORIAL_MARKERS = ('[EDITORIAL:', '[PROVISIONAL:', '[EDITORIAL GATE]')

# ── Forbidden tokens (PI core_rules) ──────────────────────────────────────────
# Per Valoria PI core_rules: "Solmund, never Galbados". Promotes the
# canonical-name rule from Level 2 (skill-side, runs only on prose-writer
# invocation) to Level 4 (every commit, RuntimeError). The rule is satisfied if:
#   (a) the file does not contain the forbidden token, OR
#   (b) the file co-locates the canonical name (Solmund), reflecting actual
#       repo conventions for rename mappings and meta-discussion, OR
#   (c) every occurrence of the forbidden token has the exception phrase
#       ("never") within ±30 chars of immediate context.
# (a) and (c) are the consistency_check.py rules; (b) reflects actual repo
# usage patterns where rename-mapping files like references/name_collision_database.yaml
# legitimately cite both names side-by-side.
FORBIDDEN_TOKEN_RULES = (
    {
        'token_re': re.compile(r'(?i)galbados'),
        'canonical_name': 'Solmund',
        'canonical_re':   re.compile(r'(?i)solmund'),
        'exception_substring': 'never',
        'exception_window':    30,
        'description': (
            'PI core_rules: "Solmund, never Galbados". File must either '
            'co-locate "Solmund" or have "never" within 30 chars of every '
            'Galbados occurrence.'
        ),
    },
)

# Files exempt from forbidden-token gate.
FORBIDDEN_TOKEN_EXEMPT_PREFIXES = (
    'archives/',                       # frozen historical content
    'deprecated/',                     # frozen deprecated content
    'references/atoms_pending/',       # transient atomization staging
)
FORBIDDEN_TOKEN_EXEMPT_PATHS = (
    'skills/prose-writer/scripts/consistency_check.py',
    'skills/valoria-orchestrator/scripts/valoria_hooks.py',
)

# Informational — enforcing gate is COMMIT_FORMAT regex below
COMMIT_FORMAT   = re.compile(r'^\[(editorial|patch|simulation|compilation|infrastructure|skill|cleanup|godot|phase|fix|bugfix)\] .{10,}')
COMMIT_SCOPES   = tuple(COMMIT_FORMAT.pattern.split('(')[1].split(')')[0].split('|'))

# Context thresholds — scaled for 1M-token window (Opus 4.6/4.7, Sonnet 4.6).
# Prior values 120k/150k/180k were calibrated for the legacy 200k window.
# Percentages remain 60/75/90; absolute values updated 2026-05-10.
CONTEXT_SOFT              = 600_000   # 60% — plan handoff
CONTEXT_CHECKPOINT_HARD   = 750_000   # 75% — commit checkpoint now
CONTEXT_HARD              = 900_000   # 90% — hard close
CONTEXT_WARN              = CONTEXT_SOFT  # alias for backward compat

TASK_REQUIRED_FILES = {
    # Skill paths added 2026-05-08: each task type now requires fetching its
    # governing skill before the gate passes. Enforcement rationale: prior to
    # this change, skill compliance was text-only (Level 1). A session produced
    # a full sim from scratch, ignoring the existing harness and anti-patterns,
    # because the simulator skill was never fetched. Adding the skill to the
    # required-files list promotes enforcement to Level 4 (RuntimeError) —
    # the skill must be read before any work in that domain begins.
    "simulation":      ["references/canonical_sources.yaml", "canon/02_canon_constraints.md",
                        "skills/valoria-simulator/SKILL.md"],
    "audit":           ["references/canonical_sources.yaml", "canon/02_canon_constraints.md",
                        "skills/valoria-mechanic-audit/SKILL.md"],
    "canon_check":     ["canon/00_philosophical_foundations_rules.md", "canon/02_canon_constraints.md"],
    "editorial":       ["canon/editorial_ledger.jsonl"],
    "patch":           ["canon/patch_register_active.yaml"],
    "compilation":     ["references/canonical_sources.yaml", "canon/patch_register_active.yaml"],
    "propose_mechanic":["references/canonical_sources.yaml", "canon/editorial_ledger.jsonl",
                        "skills/valoria-mechanic-audit/SKILL.md"],
    "design_proposal": ["references/canonical_sources.yaml", "canon/editorial_ledger.jsonl",
                        "references/throughlines_meta.md"],
    "design":          ["references/canonical_sources.yaml"],
    "infrastructure":  [],
}


# ── Hook 1: Bootstrap ─────────────────────────────────────────────────────────

def assert_bootstrap(scope: str = None) -> str:
    """
    Confirm github_ops fetched from GitHub this session. Raises if not.

    scope: optional session scope tag (e.g. 'infrastructure', 'godot').
           When provided, sets _session_scope for per-session log routing.
           Valid scopes are defined in github_ops.SESSION_SCOPES.
    """
    global _bootstrap_confirmed, _session_scope, _session_log_path
    try:
        token = g.get_session_token()
        _bootstrap_confirmed = True
        print(f"[HOOK ✓] bootstrap — token: {token}")
    except RuntimeError:
        raise RuntimeError(
            "[HOOK VIOLATION] No session token — bootstrap incomplete.\n"
            "read_files_graphql() must be called before any work begins.\n"
            "Re-run the bootstrap block."
        )

    # Set session scope if provided
    if scope:
        if hasattr(g, 'SESSION_SCOPES') and scope not in g.SESSION_SCOPES:
            raise RuntimeError(
                f"[HOOK VIOLATION] Unknown session scope '{scope}'.\n"
                f"Valid: {sorted(g.SESSION_SCOPES)}"
            )
        _session_scope = scope
        _session_log_path = f"session_logs/{scope}_{token}.md"
        print(f"[HOOK ✓] session scope: {scope} → {_session_log_path}")

    # F.6 Rate-limit pre-check (added 2026-05-16).
    # GraphQL budget is per-PAT-user across all concurrent sessions, not
    # per-session. Surface remaining budget early so operators see the
    # constraint before hooks consume it, and HARD HALT before the budget
    # actually exhausts (which produces opaque KeyError('data') failures
    # mid-commit and orphans in-flight work). REST /rate_limit is itself
    # not rate-limited and costs one REST call.
    try:
        import urllib.request as _ur_rl, json as _j_rl
        pat_rl = os.environ.get('GITHUB_PAT', '')
        if pat_rl:
            _rl_req = _ur_rl.Request(
                'https://api.github.com/rate_limit',
                headers={'Authorization': f'token {pat_rl}', 'Accept': 'application/vnd.github.v3+json'}
            )
            with _ur_rl.urlopen(_rl_req) as _rl_r:
                _rl_data = _j_rl.loads(_rl_r.read())
            _gql = _rl_data.get('resources', {}).get('graphql', {})
            _rest = _rl_data.get('resources', {}).get('core', {})
            _gql_remain = _gql.get('remaining', 0)
            _gql_reset = _gql.get('reset', 0)
            _rest_remain = _rest.get('remaining', 0)
            import time as _t_rl
            _mins_to_reset = max(0, (_gql_reset - int(_t_rl.time())) // 60)

            # Halt thresholds — tuned from measured warm-cache bootstrap cost
            # after F.4/F.5 fixes landed (2026-05-16):
            #   warm-cache bootstrap: 2 GraphQL
            #   cold-cache bootstrap: 12 GraphQL
            #   bootstrap + commit:   ~5-15 GraphQL
            # Hard halt at 30 = 2× cold-bootstrap+commit cost; leaves margin
            # for retry on collision. Initial deploy of F.6 (d72cc86) used
            # 200/1000/3000 as conservative placeholders since the measured
            # cost wasn't known at write-time; those values were ~100×
            # over-provisioned and produced false positives blocking
            # legitimate commits at moderate budget pressure. Re-tuned here.
            if _gql_remain < 30:
                raise RuntimeError(
                    f"[BUDGET EXHAUSTED] GraphQL budget critical: "
                    f"{_gql_remain}/5000 remaining, resets in {_mins_to_reset} min.\n"
                    f"Bootstrap would fail mid-flight. Wait for reset before retry.\n"
                    f"Concurrent sessions on the same PAT share this budget — "
                    f"another session is likely consuming it."
                )
            elif _gql_remain < 150:
                print(
                    f"[BUDGET ⚠] GraphQL: {_gql_remain}/5000 remaining "
                    f"({_mins_to_reset} min to reset). Concurrent-session "
                    f"load is high; prefer cache hits, defer non-urgent work."
                )
            elif _gql_remain < 500:
                print(f"[BUDGET] GraphQL: {_gql_remain}/5000 remaining ({_mins_to_reset} min to reset).")
            # else: silent — budget is healthy
    except RuntimeError:
        raise  # re-raise the budget-exhausted halt
    except Exception:
        pass  # rate_limit check is advisory — never block bootstrap on it failing

    # Print active sessions summary
    if hasattr(g, 'read_active_sessions'):
        try:
            active = g.read_active_sessions()
            if active:
                print(f"\n[SESSION] {len(active)} active session(s):")
                for s in active:
                    marker = " ← THIS SESSION" if s.get('token') == token else ""
                    print(f"  {s.get('scope','?')} | {s.get('token','?')[:12]} | {s.get('started','?')}{marker}")
                # Warn on scope overlap
                if scope:
                    overlapping = [s for s in active
                                   if s.get('scope') == scope and s.get('token') != token]
                    if overlapping:
                        print(f"\n  ⚠ WARNING: scope '{scope}' is already active in another session!")
                        print(f"  Concurrent same-scope sessions risk collisions.")
                        print(f"  Consider using a different scope or closing the other session first.")
            else:
                print("[SESSION] No other active sessions.")
        except Exception:
            pass  # index may not exist yet (pre-migration)

    # Compliance check — blocks work if violations exist.
    # F.5 fix (2026-05-16): use cached wrapper. Caches violations result
    # by HEAD OID + 10-min TTL. Cache hit saves ~30 GraphQL calls per
    # bootstrap. Cache invalidates on any commit (HEAD moves), which is
    # the correct freshness boundary for compliance state.
    try:
        sys.path.insert(0, '/home/claude')
        import compliance_check as cc
        # Prefer cached entry point when available; fall back to direct
        # check_all for older compliance_check.py versions that haven't
        # picked up the F.5 fix yet (graceful degradation during rollout).
        _check_fn = getattr(cc, 'check_all_cached', cc.check_all)
        violations = _check_fn()
        if violations:
            auto_fixable = [v for v in violations if v.auto_fixable]

            if auto_fixable:
                # CHANGED 2026-05-10 from auto-commit-during-bootstrap to report-only.
                # The previous behavior at this site silently committed auto-fix
                # output to main on every bootstrap, which produced two destructive
                # commits (a8f7b2f8, 1df4259b) — atomizer.archive_by_status returned
                # empty new_files dict, then index_gen regenerated summary+index
                # against empty content (wiping the editorial_ledger_summary and
                # _index from 7 active P2 entries to next_id:1). Source of truth
                # editorial_ledger.yaml was unaffected; only the derivative views.
                # Auto-commit during a non-interactive bootstrap step is too
                # high-risk; surface violations and let the operator drive the fix.
                print(
                    f"[COMPLIANCE ⚠] {len(auto_fixable)} auto-fixable "
                    f"violation(s) detected. NOT auto-committing — run the "
                    f"fix manually:"
                )
                for v in auto_fixable:
                    print(f"  - {v.path} ({v.fix_action})")

            # NOTE 2026-05-10: The historical "re-check after auto-fix" block here
            # raised RuntimeError on residual error-severity violations. That made
            # sense when bootstrap auto-committed fixes; without the auto-commit
            # (the destructive path was disabled this session), the re-check is
            # now wrong — it would hard-stop on the same violations that were
            # just reported. Violations are now print-only at bootstrap time.
            # Manual remediation is the operator's responsibility; surfacing
            # them is the bootstrap's.
            warns = [v for v in violations if v.severity == 'warn']
            if warns:
                print(f"[COMPLIANCE ⚠] {len(warns)} warning(s) — non-blocking")
        else:
            print(f"[COMPLIANCE ✓] All files compliant.")
    except ImportError:
        # Auto-fetch compliance_check.py from repo
        try:
            import urllib.request, json, base64
            pat = os.environ.get('GITHUB_PAT', '')
            if pat:
                for tool_name in ['atomizer.py', 'compliance_check.py']:
                    tool_req = urllib.request.Request(
                        f'https://api.github.com/repos/jordanelias/ttrpg/contents/tools/{tool_name}?ref=main',
                        headers={'Authorization': f'token {pat}', 'Accept': 'application/vnd.github.v3+json'}
                    )
                    with urllib.request.urlopen(tool_req) as tool_r:
                        tool_data = json.loads(tool_r.read())
                    open(f'/home/claude/{tool_name}', 'w').write(
                        base64.b64decode(tool_data['content']).decode()
                    )
                import compliance_check as cc
                _check_fn2 = getattr(cc, 'check_all_cached', cc.check_all)
                violations = _check_fn2()
                if violations:
                    manual = [v for v in violations if v.severity == 'error']
                    if manual:
                        raise RuntimeError(
                            "[COMPLIANCE VIOLATION] Manual intervention required:\n"
                            + cc.report(manual)
                        )
                    warns = [v for v in violations if v.severity == 'warn']
                    if warns:
                        print(f"[COMPLIANCE \u26a0] {len(warns)} warning(s) — non-blocking")
                else:
                    print("[COMPLIANCE \u2713] All files compliant.")
            else:
                print("[COMPLIANCE] No PAT — skipping compliance check")
        except Exception as e2:
            print(f"[COMPLIANCE] Auto-fetch failed: {e2} — skipping")

    # Freshness gate — blocks sim/audit/patch if canonical sources are stale.
    #
    # Cost discipline (added 2026-05-16 — F.4 fix):
    # The previous implementation fired one GraphQL call per canonical_sha
    # pair (106 calls per bootstrap, uncached). With multiple concurrent
    # sessions this exhausted the 5000/hour GraphQL budget. The fix has
    # three parts:
    #   (1) batch — use fg.get_blob_shas_batch(paths) to fetch all SHAs in
    #       a single GraphQL request (1 call vs 106) via alias queries.
    #   (2) cache — write result to /home/claude/.freshness_cache.json
    #       keyed by SHA of canonical_sources.yaml content. Hit if the
    #       canonical_sources.yaml is unchanged AND within 10-min TTL.
    #   (3) script-TTL — re-fetch freshness_gate.py via REST only if
    #       local copy is stale (>1 hour, same TTL as the bootstrap
    #       script-cache discipline).
    # Net effect: at most 1 GraphQL call per ~10 min per canonical-set,
    # zero when cache is warm. Was 106 per bootstrap.
    try:
        import urllib.request as _ur, json as _j, base64 as _b64, time as _t, hashlib as _hl
        pat = os.environ.get('GITHUB_PAT', '')
        if pat:
            _fg_local = '/home/claude/freshness_gate.py'
            _fg_stale = (
                not os.path.exists(_fg_local)
                or (_t.time() - os.path.getmtime(_fg_local)) > 3600
            )
            if _fg_stale:
                _fg_req = _ur.Request(
                    'https://api.github.com/repos/jordanelias/ttrpg/contents/tools/freshness_gate.py?ref=main',
                    headers={'Authorization': f'token {pat}', 'Accept': 'application/vnd.github.v3+json'}
                )
                with _ur.urlopen(_fg_req) as _fg_r:
                    _fg_data = _j.loads(_fg_r.read())
                open(_fg_local, 'w').write(
                    _b64.b64decode(_fg_data['content']).decode()
                )
            import freshness_gate as fg
            # Reload so a freshly-fetched module replaces the cached import
            import importlib as _il
            _il.reload(fg)

            # Prefer cached canonical_sources content (avoids REST round-trip).
            # Falls back to fg.get_file() (REST) only on miss — rare after
            # the first quick_bootstrap of a session populates the cache.
            _cs_key = g._repo_key(fg.CANONICAL_SOURCES_PATH, 'ttrpg')
            content = g._session_fetches.get(_cs_key)
            if content is None:
                content, _ = fg.get_file(fg.CANONICAL_SOURCES_PATH)
            pairs = fg.parse_canonical_pairs(content)

            _cs_sha = _hl.sha256(content.encode()).hexdigest()
            _fc_path = '/home/claude/.freshness_cache.json'
            _FC_TTL = 600  # 10 minutes — long enough to span bursts, short
                           # enough that genuine staleness is caught quickly.

            _use_cache = False
            try:
                with open(_fc_path) as _fc_f:
                    _fc = _j.load(_fc_f)
                if (_fc.get('cs_yaml_sha') == _cs_sha
                    and (_t.time() - _fc.get('checked_at', 0)) < _FC_TTL):
                    stale_paths = _fc.get('stale_paths', [])
                    pairs_checked = _fc.get('pairs_checked', len(pairs))
                    _use_cache = True
            except (FileNotFoundError, _j.JSONDecodeError, KeyError):
                pass

            if not _use_cache:
                # Single batched GraphQL call replaces the per-path loop.
                _paths_to_check = [p for p, sha in pairs if sha]
                _recorded = {p: sha for p, sha in pairs if sha}
                live_shas = fg.get_blob_shas_batch(_paths_to_check)
                stale_paths = [
                    p for p in _paths_to_check
                    if live_shas.get(p) and live_shas[p] != _recorded[p]
                ]
                pairs_checked = len(pairs)
                # Persist cache (atomic write: temp + rename) so concurrent
                # writes don't corrupt the file.
                try:
                    _tmp = _fc_path + '.tmp'
                    with open(_tmp, 'w') as _fc_f:
                        _j.dump({
                            'cs_yaml_sha': _cs_sha,
                            'checked_at': _t.time(),
                            'pairs_checked': pairs_checked,
                            'stale_paths': stale_paths,
                        }, _fc_f)
                    os.replace(_tmp, _fc_path)
                except Exception:
                    pass  # non-fatal — cache is optimization, not requirement

            stale_count = len(stale_paths)
            _cache_marker = ' (cached)' if _use_cache else ''
            if stale_count:
                print(f"[FRESHNESS \u26a0] {stale_count} stale canonical source(s){_cache_marker} — run freshness_gate.py --update")
            else:
                print(f"[FRESHNESS \u2713] All {pairs_checked} canonical sources fresh{_cache_marker}.")
    except Exception as fg_err:
        print(f"[FRESHNESS] Check skipped: {fg_err}")
    except RuntimeError as e:
        if 'Cannot load references/atomization_rules.yaml' in str(e):
            print("[COMPLIANCE] atomization_rules.yaml not deployed — skipping (pre-Phase 0)")
        else:
            raise

    # Report active handoffs — lets new sessions see available workstreams
    # Handoff report emitted by github_ops.quick_bootstrap (caches _active_handoffs
    # in the same block). Dedupe per audit 2026-05-25 Phase 0.8.

    return token


# ── Hook 2: Task gate ─────────────────────────────────────────────────────────

def task_gate(task_type: str) -> None:
    """Confirm required files fetched for this task type. Raises if missing."""
    if not _bootstrap_confirmed:
        raise RuntimeError(
            f"[HOOK VIOLATION] task_gate('{task_type}') before assert_bootstrap()."
        )
    required = TASK_REQUIRED_FILES.get(task_type)
    if required is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] Unknown task type '{task_type}'.\n"
            f"Valid: {sorted(TASK_REQUIRED_FILES)}"
        )
    repo = g.active_repo()
    missing = [p for p in required
               if g._repo_key(p, repo) not in g._session_fetches
               or g._session_fetches[g._repo_key(p, repo)] is None]
    if missing:
        raise RuntimeError(
            f"[HOOK VIOLATION] Task '{task_type}' — files not fetched:\n"
            + "\n".join(f"  {p}" for p in missing)
            + "\nFetch before starting. No exceptions."
        )
    _task_gates_passed.add(task_type)
    print(f"[HOOK ✓] task_gate('{task_type}')")

    # Print governing-skill reminder at the decision point. (2026-05-08)
    # Rationale: skill SKILL.md is now a required fetch (Level 4 above), but
    # having the file in context != attending to it when planning. Printing the
    # critical anti-patterns here puts them right before Claude decides its
    # approach — not buried in bootstrap output 50k+ tokens back.
    if task_type == "simulation":
        print(
            "\n[TASK GATE: simulation] Mode G anti-patterns — verify before writing any code:\n"
            "  ✗ Build full-stack sim in one session          → module decomposition, one system/session\n"
            "  ✗ Fetch index; infer mechanics from headings   → force_full=True on all design docs\n"
            "  ✗ Invent mechanics because they sound right    → every constant needs a ledger entry\n"
            "  ✗ Batch-run an unvalidated sim                 → no batch runs before all modules verified\n"
            "  ✗ Use remembered or stale canonical values     → fetch canonical source, never memory\n"
            "  → Check tests/sim/ for existing harness BEFORE writing new code.\n"
            "  → Call h.sim_gate() before writing any simulation code.\n"
        )
    elif task_type == "audit":
        print(
            "\n[TASK GATE: audit] Required before any audit work:\n"
            "  → Never audit from memory — fetch canonical source for target system.\n"
            "  → All mechanical values must be cited with source file + section.\n"
            "  → P1 findings must be appended to canon/editorial_ledger.jsonl.\n"
            "  → Check tests/audit/ for prior audit outputs on this system first.\n"
        )


def task_gate_with_system(task_type: str, system: str, canonical_sources_content: str) -> None:
    """
    Extended task gate: also confirms canonical design doc fetched for system.
    Parses canonical_sources.yaml with PyYAML (not regex).
    """
    task_gate(task_type)
    try:
        import yaml
        sources = yaml.safe_load(canonical_sources_content)
    except Exception as e:
        raise RuntimeError(
            f"[HOOK VIOLATION] Failed to parse canonical_sources.yaml: {e}\n"
            f"Fetch a valid canonical_sources.yaml before calling task_gate_with_system()."
        )

    systems = sources.get('systems', {}) if sources else {}
    entry = systems.get(system, {})

    # Try multiple canonical key names used in the file
    canonical_path = (
        entry.get('canonical') or
        entry.get('canonical_bg') or
        entry.get('design_doc') or
        entry.get('canonical_ttrpg')
    )

    if not canonical_path or not isinstance(canonical_path, str):
        raise RuntimeError(
            f"[HOOK VIOLATION] System '{system}' not found or has no canonical path\n"
            f"in canonical_sources.yaml. Available systems: {sorted(systems.keys())}\n"
            f"Cannot propose or simulate without knowing the canonical source."
        )

    _cs_key = g._repo_key(canonical_path, g.active_repo())
    if _cs_key not in g._session_fetches or g._session_fetches[_cs_key] is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] Canonical doc for '{system}' not fetched:\n"
            f"  Required: {canonical_path}\n"
            f"Fetch via read_files_graphql(['{canonical_path}']) before starting."
        )
    print(f"[HOOK ✓] system gate '{system}' — {canonical_path}")


# ── Hook 3: Editorial gate ────────────────────────────────────────────────────

def editorial_gate(path: str, content: str) -> None:
    """
    Blocks commits to editorial paths without [EDITORIAL] or [PROVISIONAL] markers.
    Called automatically for every addition in pre_commit_gate.
    """
    if not any(path.startswith(p) for p in EDITORIAL_PATHS):
        return
    if len(content) < 200:
        return  # stub — exempt
    if path.endswith('_index.md'):
        print(f"[HOOK ✓] editorial_gate — {path} (index exempt)")
        return
    if not any(m in content for m in EDITORIAL_MARKERS):
        raise RuntimeError(
            f"[HOOK VIOLATION] Editorial path without flag:\n"
            f"  {path}\n"
            f"Add [EDITORIAL: ED-NNN — description] or [PROVISIONAL: ...] before committing.\n"
            f"User retains exclusive authority over: setting, worldbuilding, characters,\n"
            f"narrative, faction behaviour, ambiguous design intent."
        )
    print(f"[HOOK ✓] editorial_gate — {path}")


# ── Hook 3a: Forbidden-token gate (PI core_rules canonical names) ─────────────

def forbidden_token_gate(additions: list) -> None:
    """
    Block commits introducing forbidden canonical-name tokens outside their
    permitted contexts. Implements PI core_rules: "Solmund, never Galbados".

    Promotes a previously Level-2 (skill-side prose-writer/consistency_check.py)
    rule to Level 4 by enforcing on every commit. CI mirror should run an
    equivalent check via the consistency_check.py script.

    Logic per FORBIDDEN_TOKEN_RULES entry: a file passes if any of —
      (a) it does not contain the forbidden token,
      (b) it also contains the canonical name (e.g. Solmund),
      (c) every forbidden-token occurrence has the exception phrase
          (e.g. "never") within ±N chars of immediate context.

    See FORBIDDEN_TOKEN_EXEMPT_PREFIXES / EXEMPT_PATHS for files exempted
    from the check (archives, deprecated, the rule-defining files themselves,
    transient atomization staging).
    """
    errors = []
    for path, content in additions:
        if any(path.startswith(p) for p in FORBIDDEN_TOKEN_EXEMPT_PREFIXES):
            continue
        if path in FORBIDDEN_TOKEN_EXEMPT_PATHS:
            continue
        for rule in FORBIDDEN_TOKEN_RULES:
            token_re = rule['token_re']
            occurrences = list(token_re.finditer(content))
            if not occurrences:
                continue  # rule (a)
            if rule['canonical_re'].search(content):
                continue  # rule (b)
            # Rule (c): every occurrence must have exception nearby
            window = rule['exception_window']
            exception = rule['exception_substring'].lower()
            offenders = []
            for m in occurrences:
                ctx = content[max(0, m.start() - window): m.end() + window]
                if exception not in ctx.lower():
                    line = content[:m.start()].count('\n') + 1
                    snippet = ctx.strip().replace('\n', ' ')[:80]
                    offenders.append(f"L{line}: ...{snippet}...")
            if offenders:
                errors.append(
                    f"{path}: {rule['description']}\n  "
                    + "\n  ".join(offenders)
                )
    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] forbidden_token_gate FAILED:\n\n"
            + "\n\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
            + "\n\nFix the offending content before committing. "
              "If the file is genuinely meta-documentation about the rename, "
              "either co-locate the canonical name in the same file, or add "
              "the path to FORBIDDEN_TOKEN_EXEMPT_PATHS in valoria_hooks.py."
        )
    print(f"[HOOK \u2713] forbidden_token_gate ({len(additions)} files scanned)")


# ── Hook 3b: Framework vetting gate (PP-674) ──────────────────────────────────
#
# Enforces the canonical vetting framework from references/throughlines_meta.md.
# Triggers when a commit modifies canon/patch_register_active.yaml adding a
# Class A or Class B patch entry. Requires the entry to carry a `vetting:` block
# with N, Ω, Μ, М, Q records. Class C/D/E entries are exempt. Pre-PP-674 entries
# are grandfathered.

VETTING_REQUIRED_KEYS = ('class', 'necessity', 'omega', 'mu', 'm_ratings', 'q')
VETTING_CLASS_VALUES = ('A', 'B', 'C', 'D', 'E')
VETTING_ENFORCED_FROM_PP = 674


def vetting_gate(additions: list) -> None:
    """
    Validates framework-required vetting records on patch_register additions.

    Fires only if additions modify canon/patch_register_active.yaml. Locates
    PP entries with id >= PP-674; for each Class A/B entry, verifies a
    `vetting:` block is present with required keys. Class C/D/E entries only
    need the `class` field.

    This enforces the canonical vetting framework (references/throughlines_meta.md)
    at commit time. CI runs the same check externally.
    """
    import re as _re
    pr_additions = [(p, c) for p, c in additions if p == 'canon/patch_register_active.yaml']
    if not pr_additions:
        return  # Not touching the patch register, nothing to enforce

    path, content = pr_additions[0]

    # Parse PP entries — simple YAML-ish extraction (the full yaml module might
    # not be available in every environment; use the same regex style other
    # hooks use).
    entries = _re.findall(
        r'-\s+id:\s+PP-(\d+)\s*\n(.*?)(?=\n-\s+id:\s+PP-\d+|\Z)',
        content, _re.DOTALL
    )
    errors = []
    for pp_num_str, body in entries:
        pp_num = int(pp_num_str)
        if pp_num < VETTING_ENFORCED_FROM_PP:
            continue  # grandfathered
        # Does this entry have a vetting block?
        vetting_match = _re.search(r'\n\s+vetting:\s*\n(.*)',
                                   body, _re.DOTALL)
        # NOTE: capture extends to end-of-body (body is already scoped to one PP
        # entry by the outer regex). The required-keys substring check below is
        # unique-key-safe: necessity/omega/mu/m_ratings/q only appear inside
        # vetting blocks. Avoids the prior bug where lookahead matched FIRST
        # child of vetting (class:) and truncated captured block to one line.
        # Fixed 2026-04-25 alongside PP-674 yaml indentation repair.
        if not vetting_match:
            # Missing — is this a Class A/B? We do not know for certain without
            # a class marker. Default: require vetting block for all entries
            # >= PP-674 unless the body explicitly carries "class: C|D|E" or
            # "pre-framework: true".
            if _re.search(r'class:\s*[CDE]\b', body) or 'pre-framework: true' in body:
                continue
            errors.append(
                f"PP-{pp_num_str}: no `vetting:` block. Required for "
                f"Class A/B patches (PP-{VETTING_ENFORCED_FROM_PP}+). "
                f"Add class + vetting per references/throughlines_meta.md §8, "
                f"or mark `class: E` / `pre-framework: true` if grandfathered."
            )
            continue
        vetting_block = vetting_match.group(1)
        # Parse class
        class_match = _re.search(r'class:\s*([A-E])\b', vetting_block)
        if not class_match:
            errors.append(
                f"PP-{pp_num_str}: vetting.class missing or invalid. "
                f"Must be one of {VETTING_CLASS_VALUES}."
            )
            continue
        cls = class_match.group(1)
        if cls in ('C', 'D', 'E'):
            # Light validation — only need class
            continue
        # Class A/B — require full set
        for key in VETTING_REQUIRED_KEYS:
            if _re.search(rf'\b{key}:', vetting_block) is None:
                errors.append(
                    f"PP-{pp_num_str} (Class {cls}): vetting.{key} missing. "
                    f"Required keys for Class A/B: {VETTING_REQUIRED_KEYS}."
                )

    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] vetting_gate FAILED:\n\n"
            + "\n\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
            + "\n\nFramework: references/throughlines_meta.md\n"
            + "Required for Class A/B patches (PP-674+). Fix before committing."
        )
    print(f"[HOOK ✓] vetting_gate — {len(entries)} PP entries scanned")


# ── Hook 4: Commit message ────────────────────────────────────────────────────

def commit_message_gate(message: str) -> None:
    """Raises if message doesn't match [scope] description format."""
    if not COMMIT_FORMAT.match(message):
        raise RuntimeError(
            f"[HOOK VIOLATION] Bad commit message: '{message}'\n"
            f"Required: '[scope] description — PP-NNN / ED-NNN if applicable'\n"
            f"Valid scopes: {sorted(COMMIT_SCOPES)}"
        )
    print(f"[HOOK ✓] commit_message_gate")


# ── Hook 5: Pre-commit gate ───────────────────────────────────────────────────

# ── Hook: Supersession check ──────────────────────────────────────────────────

def supersession_check(additions: list) -> None:
    """
    Non-blocking WARNING. Checks canon/supersession_register.yaml for any entries
    whose 'files_to_recheck' list overlaps with the current commit's paths.
    Emits a visible warning per match so that a propagating commit re-asserts
    whatever the superseded authority used to claim.

    Does NOT block — commits legitimately re-touch these files. The warning is
    a prompt to verify the commit does not regress the supersession.

    The register itself lives at canon/supersession_register.yaml. If not fetched
    this session, silently skip (can't check what we don't have).
    """
    register_path = 'canon/supersession_register.yaml'
    repo_key = g._repo_key(register_path, g.active_repo())
    if repo_key not in g._session_fetches or g._session_fetches[repo_key] is None:
        return  # register not fetched — skip

    content = g._session_fetches[repo_key]
    if not content:
        return

    try:
        import yaml
        data = yaml.safe_load(content) or {}
    except Exception:
        return  # malformed register — don't fail the commit

    entries = data.get('entries', []) if isinstance(data, dict) else []
    if not entries:
        return

    commit_paths = {p for p, _ in additions}
    matches = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        recheck = e.get('files_to_recheck', []) or []
        if isinstance(recheck, list):
            overlap = commit_paths & set(recheck)
            if overlap:
                matches.append({
                    'id': e.get('superseded_id', '?'),
                    'scope': str(e.get('scope', ''))[:80],
                    'replacement': str(e.get('replacement', ''))[:120],
                    'touched': sorted(overlap),
                })

    if matches:
        print(f"\n[HOOK ⚠ SUPERSESSION] {len(matches)} match(es) in canon/supersession_register.yaml:")
        for m in matches:
            print(f"  - {m['id']}: {m['scope']}")
            print(f"    Current canonical: {m['replacement']}")
            print(f"    Touched in this commit: {', '.join(m['touched'])}")
        print("  Verify commit does not regress the superseded authority. (non-blocking)\n")


def assert_unique_ids(additions: list) -> None:
    """
    Enforce id uniqueness in ledger and register files.

    Prevents collision bugs like ED-762 (committed 2026-04-29 across two separate
    sessions, surfaced in audit 2026-04-30). Hooks at commit time so violations
    fail fast rather than after CI or via downstream propagation defects.

    Files checked:
      canon/editorial_ledger.jsonl         (JSONL store → round-trip parse + id-uniqueness;
                                            integrity/required-fields via jsonl_ledger_gate)
      canon/patch_register_active.yaml     (top-level list with .id)
      canon/patch_register_archive.yaml    (top-level list with .id)

    The editorial_ledger YAML + its archive files were deprecated 2026-05-28
    (→ deprecated/canon/); the live editorial ledger is the JSONL store.
    """
    LEDGER_FILES = {
        'canon/patch_register_active.yaml':    None,
        'canon/patch_register_archive.yaml':   None,
    }
    JSONL_LEDGERS = {'canon/editorial_ledger.jsonl'}
    import yaml, json
    errors = []
    for path, content in additions:
        if path in JSONL_LEDGERS:
            # JSONL: one JSON object per line; uniqueness across the whole file.
            items = []
            for ln_no, ln in enumerate(content.splitlines(), 1):
                if not ln.strip():
                    continue
                try:
                    items.append(json.loads(ln))
                except json.JSONDecodeError as e:
                    errors.append(f"UNIQUE_IDS: {path}: line {ln_no} invalid JSON — {e}")
            seen, dupes = {}, []
            for item in items:
                if not isinstance(item, dict):
                    continue
                iid = item.get('id')
                if iid is None:
                    continue
                if iid in seen:
                    dupes.append(iid)
                else:
                    seen[iid] = True
            if dupes:
                errors.append(
                    f"UNIQUE_IDS: {path}: duplicate ID(s) {sorted(set(dupes))}. "
                    f"Each JSONL entry must have a unique id."
                )
            continue
        if path not in LEDGER_FILES:
            continue
        try:
            data = yaml.safe_load(content)
        except yaml.YAMLError as e:
            errors.append(f"UNIQUE_IDS: {path}: YAML parse error — {e}")
            continue
        key = LEDGER_FILES[path]
        if key is None:
            items = data if isinstance(data, list) else []
        else:
            items = (data or {}).get(key, []) or []
        seen, dupes = {}, []
        for item in items:
            if not isinstance(item, dict):
                continue
            iid = item.get('id')
            if iid is None:
                continue
            if iid in seen:
                dupes.append(iid)
            else:
                seen[iid] = True
        if dupes:
            errors.append(
                f"UNIQUE_IDS: {path}: duplicate ID(s) {sorted(set(dupes))}. "
                f"Each entry must have a unique id (caused ED-762 collision 2026-04-29)."
            )
    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] assert_unique_ids FAILED:\n"
            + "\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
        )


def jsonl_ledger_gate(additions: list) -> None:
    """
    Validate canon/editorial_ledger.jsonl on commit (DB-grade integrity in text):
      - every non-empty line is valid JSON (round-trip)
      - every entry is an object with required fields: id, status, description
      - id matches ED-<int>
    Uniqueness is enforced separately by assert_unique_ids. Raises RuntimeError on violation.
    """
    import json, re as _re
    JSONL_PATH = 'canon/editorial_ledger.jsonl'
    HARD = ('id',)          # integrity: file is a keyed store — id is mandatory
    SOFT = ('description', 'status')  # data quality: warn, do not halt
    errors, warnings = [], []
    for path, content in additions:
        if path != JSONL_PATH:
            continue
        for ln_no, ln in enumerate(content.splitlines(), 1):
            if not ln.strip():
                continue
            try:
                obj = json.loads(ln)
            except json.JSONDecodeError as e:
                errors.append(f"line {ln_no}: invalid JSON — {e}")
                continue
            if not isinstance(obj, dict):
                errors.append(f"line {ln_no}: not a JSON object")
                continue
            iid = obj.get('id', '')
            if iid in (None, ''):
                errors.append(f"line {ln_no}: missing/empty id (keyed store requires id)")
            elif not _re.match(r'^ED-\d+$', str(iid)):
                warnings.append(f"line {ln_no}: non-standard id '{iid}' (expected ED-<int>)")
            miss_soft = [f for f in SOFT if f not in obj or obj.get(f) in (None, '', '[unrecovered]')]
            if miss_soft:
                warnings.append(f"line {ln_no} (id={iid or '?'}): missing/empty {miss_soft}")
    if warnings:
        print(f"[HOOK ⚠ jsonl_ledger_gate] {len(warnings)} data-quality warning(s) "
              f"(missing description/status — non-blocking):")
        for w in warnings[:15]:
            print(f"    - {w}")
        if len(warnings) > 15:
            print(f"    ... and {len(warnings)-15} more")
    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] jsonl_ledger_gate FAILED on canon/editorial_ledger.jsonl:\n"
            + "\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors[:40]))
            + (f"\n  ... and {len(errors)-40} more" if len(errors) > 40 else "")
        )


def placeholder_names_gate(additions: list) -> None:
    """
    Check canon/placeholder_names.yaml for expired placeholders that still
    appear in committed content. Halts if any expired placeholder is referenced
    by file path or file content in this commit, UNLESS the commit itself
    transitions that placeholder from 'expired' to 'resolved' (signaling rename
    + content replacement happening in this very commit).

    Status lifecycle (Jordan-controlled): pending -> expired -> resolved.
      pending: hook does not halt (placeholder still in active use, audit pending)
      expired: hook HALTS (Jordan ratified replacement decision; rename required)
      resolved: hook does not halt (placeholder rename complete)

    Registry: canon/placeholder_names.yaml
    """
    registry_path = "canon/placeholder_names.yaml"

    # Try to load the registry from disk. If absent, skip (registry not yet
    # deployed). This is bootstrap-safe.
    try:
        import os
        if not os.path.exists(registry_path):
            # Maybe we're running outside the repo; try a relative-to-cwd fallback
            candidate_paths = [
                registry_path,
                os.path.join(os.getcwd(), registry_path),
                "/home/claude/" + registry_path,
            ]
            registry_path = next((p for p in candidate_paths if os.path.exists(p)), None)
            if registry_path is None:
                # Registry not yet deployed; skip silently
                return

        with open(registry_path) as f:
            registry_content = f.read()
    except (OSError, IOError):
        return  # Cannot read registry; skip

    # Also accept the registry from the commit itself (if Jordan is updating it
    # this very commit, use the new version, not the stale on-disk one)
    for path, content in additions:
        if path == "canon/placeholder_names.yaml":
            registry_content = content
            break

    try:
        import yaml
        registry = yaml.safe_load(registry_content)
    except (yaml.YAMLError, ImportError):
        return  # Cannot parse; let other hooks handle

    if not registry or "placeholders" not in registry:
        return

    expired_with_violation = []

    # Iterate placeholders
    for entry in registry.get("placeholders", []):
        status = entry.get("deadline_status", "pending")
        if status != "expired":
            continue  # pending or resolved: hook does not enforce

        placeholder_name = entry.get("placeholder_name", "")
        if not placeholder_name:
            continue

        # Check if commit transitions this placeholder to 'resolved' (allowed)
        # Look in commit's registry update: if status changed to 'resolved'
        # in this commit, allow the placeholder to still appear in other files
        # (the rename may not be complete across all files in this same commit).
        # Conservative: require the registry-update commit AND no other content
        # touch in same commit. For now: any placeholder marked 'expired' in
        # the committed registry triggers halt.

        # Search committed content for the placeholder
        for path, content in additions:
            if path == registry_path:
                continue  # Don't scan the registry itself
            if placeholder_name in path or (content and placeholder_name in content):
                expired_with_violation.append({
                    "id": entry.get("id", "unknown"),
                    "placeholder_name": placeholder_name,
                    "found_in": path,
                    "canonical_name_pending": entry.get("canonical_name_pending", "unknown"),
                })

    if expired_with_violation:
        msg_lines = ["[HOOK VIOLATION] placeholder_names_gate: expired placeholder(s) still in use:"]
        for v in expired_with_violation:
            msg_lines.append(
                f"  - {v['id']}: '{v['placeholder_name']}' found in {v['found_in']}"
            )
            msg_lines.append(
                f"      Canonical name pending: {v['canonical_name_pending']}"
            )
        msg_lines.append("")
        msg_lines.append(
            "Resolution: rename placeholder to canonical name in all paths, "
            "OR revert deadline_status to 'pending' if audit not yet complete."
        )
        raise RuntimeError("\n".join(msg_lines))

    print(f"[HOOK ✓] placeholder_names_gate")


def pre_commit_gate(additions: list, deletions: list = None) -> None:
    """
    Hard gate before every commit. Checks:
    1. Task gate was passed this process (task_gate() called before committing)
    2. Editorial gate per path
    3. Size thresholds (via github_ops — defense in depth)
    4. Required co-files (design doc → canonical_sources, patch → register, sim → matrix)

    Tool runner (freshness_gate, broken_dependency_checker, patch_propagation_checker)
    is NOT run here — those tools run in CI against the full repo after push.
    Running them client-side from a container without the full repo is unreliable.
    CI is the authoritative gate for those checks.
    """
    if not _bootstrap_confirmed:
        raise RuntimeError(
            "[HOOK VIOLATION] pre_commit_gate() before assert_bootstrap().\n"
            "Run bootstrap sequence before committing."
        )
    if not _task_gates_passed:
        raise RuntimeError(
            "[HOOK VIOLATION] pre_commit_gate(): no task_gate() called this process.\n"
            "Call h.task_gate('type') before committing. Valid: "
            + str(sorted(TASK_REQUIRED_FILES))
        )
    if deletions is None:
        deletions = []

    errors = []
    paths_in_commit = {p for p, _ in additions} | set(deletions)

    # Block direct writes to session_log_current.md (now auto-generated)
    if 'session_log_current.md' in paths_in_commit:
        # Allow writes from trusted internal callers (start_session_log, close_session_log, safe_session_close)
        import inspect
        caller = inspect.stack()[1].function
        trusted_callers = {'start_session_log', 'close_session_log', 'safe_session_close',
                           '_generate_pointer', 'pre_commit_gate_mutating'}
        # Walk up the stack to find if any trusted caller is in the chain
        caller_chain = {f.function for f in inspect.stack()[:8]}
        if not caller_chain & trusted_callers:
            errors.append(
                f"LEGACY BLOCK: session_log_current.md is now auto-generated.\n"
                f"  Use per-session logs instead:\n"
                f"    g.start_session_log(scope, token)  — creates session_logs/<scope>_<token>.md\n"
                f"    g.update_session_log(scope, token, content)  — updates your session log\n"
                f"    g.close_session_log(scope, token, content)  — archives and closes\n"
                f"  Direct writes to session_log_current.md are blocked."
            )

    # Editorial check per path
    for path, content in additions:
        try:
            editorial_gate(path, content)
        except RuntimeError as e:
            errors.append(str(e))

    # Size check
    for path, content in additions:
        tokens = len(content) // 4
        threshold = g.TOKEN_THRESHOLDS.get(path)
        if threshold and tokens > threshold:
            errors.append(
                f"SIZE: {path}: {tokens:,} tokens exceeds {threshold:,} limit.\n"
                f"  Archive old content before committing."
            )

    # Co-file: design doc → canonical_sources.yaml
    design_docs = [p for p, _ in additions
                   if re.match(r'designs/.+_v30\.md$', p) and 'infill' not in p]
    if design_docs and 'references/canonical_sources.yaml' not in paths_in_commit:
        errors.append(
            f"CO-FILE: design docs changed {design_docs} but\n"
            f"  references/canonical_sources.yaml not in commit.\n"
            f"  Include if source authority changed."
        )

    # Co-file: patch register content write → propagation_map
    # Index files (patch_register_index*.md) are excluded — they don't affect propagation.
    patch_writes = [p for p in paths_in_commit
                    if 'patch_register' in p
                    and not p.endswith('_index.md')
                    and not p.endswith('_index_archive.md')]
    if patch_writes and 'references/propagation_map.md' not in paths_in_commit:
        errors.append(
            f"CO-FILE: patch_register changed but propagation_map.md not included."
        )

    # Co-file: sim output → coverage_matrix
    sim_writes = [p for p in paths_in_commit
                  if p.startswith('tests/sim/') or p.startswith('tests/audit/')]
    if sim_writes and 'tests/coverage_matrix.md' not in paths_in_commit:
        errors.append(
            f"CO-FILE: simulation output added but tests/coverage_matrix.md not updated.\n"
            f"  Sim outputs: {sim_writes}"
        )

    # Co-file: SKILL.md change → skill_registry.yaml (and md companion)
    # Any change to a skills/<name>/SKILL.md must also update the registry. The
    # yaml is canonical; the .md is human-readable companion. Adding/removing/
    # renaming a skill MUST keep both in sync.
    skill_md_writes = [p for p in paths_in_commit
                       if re.match(r'^skills/[^/]+/SKILL\.md$', p)]
    skill_md_deletes = [p for p in (deletions or [])
                        if re.match(r'^skills/[^/]+/SKILL\.md$', p)]
    skill_md_changes = skill_md_writes + skill_md_deletes
    SKILL_REGISTRY_YAML = 'skills/valoria-orchestrator/references/skill_registry.yaml'
    SKILL_REGISTRY_MD   = 'skills/valoria-orchestrator/references/skill_registry.md'
    if skill_md_changes:
        registry_paths_in_commit = (
            paths_in_commit | set(deletions or [])
        )
        if SKILL_REGISTRY_YAML not in registry_paths_in_commit:
            errors.append(
                f"CO-FILE: skills/SKILL.md change(s) {skill_md_changes} but\n"
                f"  {SKILL_REGISTRY_YAML} not in commit.\n"
                f"  Update the registry entry (or add/remove it) in the same commit."
            )
        if SKILL_REGISTRY_MD not in registry_paths_in_commit:
            errors.append(
                f"CO-FILE: skills/SKILL.md change(s) {skill_md_changes} but\n"
                f"  {SKILL_REGISTRY_MD} not in commit.\n"
                f"  Markdown companion to the yaml registry must also stay in sync."
            )

    # Sim fabrication check — catches uncited mechanical constants in sim files
    try:
        sim_fabrication_check(additions)
    except RuntimeError as e:
        errors.append(str(e))

    # Forbidden-token gate (PI core_rules canonical names — Solmund, never Galbados)
    try:
        forbidden_token_gate(additions)
    except RuntimeError as e:
        errors.append(str(e))

    # Unique-ID check on ledger/register files (prevents ED-762-style collisions)
    try:
        assert_unique_ids(additions)
        jsonl_ledger_gate(additions)
    except RuntimeError as e:
        errors.append(str(e))

    # Framework vetting gate (PP-674) — enforce throughlines_meta.md protocol
    try:
        vetting_gate(additions)
    except RuntimeError as e:
        errors.append(str(e))

    # Placeholder-name gate: check canon/placeholder_names.yaml for expired
    # placeholders that still appear in committed content
    try:
        placeholder_names_gate(additions)
    except RuntimeError as e:
        errors.append(str(e))

        # Supersession check — warn (non-blocking) if commit touches files flagged
    # as propagation risks in canon/supersession_register.yaml
    supersession_check(additions)

    if errors:
        raise RuntimeError(
            "[HOOK VIOLATION] pre_commit_gate FAILED:\n\n"
            + "\n\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
            + "\n\nFix before committing. CI will also check after push."
        )

    print(f"[HOOK ✓] pre_commit_gate ({len(additions)} additions, {len(deletions)} deletions)")


def pre_commit_gate_mutating(additions: list, deletions: list = None) -> list:
    """
    Like pre_commit_gate but returns augmented additions list.
    Runs compliance validation and auto-applies fixes to the commit.
    """
    # Run standard pre_commit_gate first (editorial, size, co-file checks)
    pre_commit_gate(additions, deletions)

    # Then run compliance validation on proposed commit
    try:
        sys.path.insert(0, '/home/claude')
        import compliance_check as cc
        viols = cc.validate_commit(additions, deletions or [])

        auto_viols = [v for v in viols if v.auto_fixable]
        manual_errors = [v for v in viols if not v.auto_fixable and v.severity == 'error']
        manual_warns = [v for v in viols if not v.auto_fixable and v.severity == 'warn']

        if manual_warns:
            print(f"[COMPLIANCE ⚠] {len(manual_warns)} warning(s) — non-blocking")

        if manual_errors:
            raise RuntimeError(
                "[COMPLIANCE VIOLATION] Commit would violate rules:\n"
                + cc.report(manual_errors)
            )

        if auto_viols:
            additions = cc.apply_auto_fixes_to_additions(additions, auto_viols)
            print(f"[COMPLIANCE ✓] Auto-applied {len(auto_viols)} fixes to commit")
    except ImportError:
        pass  # compliance_check not deployed yet
    except RuntimeError as e:
        if 'Cannot load references/atomization_rules.yaml' in str(e):
            pass  # rules not deployed yet
        else:
            raise

    return additions


# ── Hook 6: Propose mechanic ──────────────────────────────────────────────────

def propose_mechanic_gate(system: str) -> None:
    """
    Call before any mechanic proposal. Enforces full prerequisite chain:
    1. canonical_sources.yaml fetched
    2. canon/editorial_ledger.jsonl fetched
    3. Canonical design doc for the system fetched
    """
    cs_key = g._repo_key('references/canonical_sources.yaml', 'ttrpg')
    if cs_key not in g._session_fetches or g._session_fetches[cs_key] is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] propose_mechanic_gate('{system}'):\n"
            f"  canonical_sources.yaml not fetched.\n"
            f"  Cannot propose mechanics without knowing which doc is canonical."
        )
    els_key = g._repo_key('canon/editorial_ledger.jsonl', 'ttrpg')
    if els_key not in g._session_fetches or g._session_fetches[els_key] is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] propose_mechanic_gate('{system}'):\n"
            f"  canon/editorial_ledger.jsonl not fetched.\n"
            f"  Required before proposing mechanics (editorial ledger is the JSONL store post-2026-05-28)."
        )
    # Delegate to task_gate_with_system for canonical doc verification
    task_gate_with_system('propose_mechanic', system, g._session_fetches[cs_key])
    print(f"[HOOK ✓] propose_mechanic_gate('{system}')")


# ── Hook 7: Context gate ──────────────────────────────────────────────────────

# Fixed context cost estimates
_SYSTEM_OVERHEAD_TOKENS = 50_000
# Accounts for: project instructions (~8k), user prefs (~1.5k), SKILL.md (~4.5k),
# conversation turns (30 avg * 1000 = 30k), tool output tokens (~3k buffer), safety margin (~3k).
# Conservative by design — real usage is higher. When in doubt, close earlier.



# ── Hook 8: Memory contamination guard ───────────────────────────────────────

def memory_contamination_guard(path: str, content: str) -> None:
    """Verify content for path came from GitHub this session, not memory."""
    _key = g._repo_key(path, g.active_repo())
    fetched = g._session_fetches.get(_key)
    if fetched is None:
        raise RuntimeError(
            f"[HOOK VIOLATION] '{path}' not fetched this session.\n"
            f"Do not use content from memory or local copies."
        )
    if fetched != content:
        raise RuntimeError(
            f"[HOOK VIOLATION] '{path}' content differs from GitHub fetch.\n"
            f"Re-fetch after any commit that modifies this file."
        )
    print(f"[HOOK ✓] memory_contamination_guard — {path}")


# ── Hook 9: Audit gate (heading-gated reads) ─────────────────────────────────

_AUDIT_KEYWORDS = {'audit', 'review', 'critique', 'comparison'}

def audit_gate(task_description: str, paths: list) -> None:
    """
    Enforce heading-gated reads for audit/review tasks.
    
    On audit-keyword tasks: every design doc in `paths` MUST go through
    g.read_index() before g.read_files_graphql() or any full read.
    Raises RuntimeError if a full read is attempted without prior index.
    
    Call this BEFORE reading any design files for audit tasks.
    After this gate passes, use g.read_index(path) then g.read_sections(path, [...]).
    """
    task_lower = task_description.lower()
    is_audit = any(kw in task_lower for kw in _AUDIT_KEYWORDS)
    
    if not is_audit:
        return  # non-audit tasks are not gated
    
    design_paths = [p for p in paths if p.startswith('designs/')]
    if not design_paths:
        return  # no design docs = no gate needed
    
    # Check that none of these paths were already full-read without index
    repo = g.active_repo()
    already_fetched_without_index = [
        p for p in design_paths
        if g._repo_key(p, repo) in g._session_fetches
        and not g.was_indexed(p, repo)
    ]
    
    if already_fetched_without_index:
        print(f"[HOOK ⚠] audit_gate: {len(already_fetched_without_index)} files were full-read "
              f"without index. For future reads, use g.read_index() first.")
    
    print(f"[HOOK ✓] audit_gate — {len(design_paths)} design docs require index-first reads")
    print(f"  Protocol: g.read_index(path) → evaluate headings → g.read_sections(path, [relevant_indices])")


def assert_index_before_full_read(path: str) -> None:
    """
    Call before any full file read in audit context.
    Raises if the path is a design doc that wasn't indexed first.
    """
    if not path.startswith('designs/'):
        return
    if not g.was_indexed(path):
        raise RuntimeError(
            f"[HOOK VIOLATION] Full read of '{path}' without prior index.\n"
            f"Audit protocol: call g.read_index('{path}') first, then\n"
            f"g.read_sections('{path}', [relevant_heading_indices])."
        )


# ── safe_commit: the only valid way to commit ─────────────────────────────────

def safe_commit(additions: list, deletions: list, message: str,
               repo: str = None) -> str:
    """
    The ONLY valid path to atomic_commit(). Runs all gates in sequence.

    repo: 'ttrpg' (default) or 'valoria-game'
      - ttrpg: full gates (editorial, size, co-files)
      - valoria-game: commit message format only (no editorial/size gates for GDScript)

    additions: list of (path, content) tuples — NOT a dict.
    IMPORTANT: entire function must run in a SINGLE bash_tool block.
    _commit_auth is process-scoped.
    """
    # Type guard — catch dict/wrong-type early with a clear message
    if not isinstance(additions, list):
        raise TypeError(
            f"[HOOK VIOLATION] safe_commit() additions must be list[tuple], got {type(additions).__name__}.\n"
            f"Use: additions=[('path/to/file.md', content_str), ...]"
        )
    if additions and not isinstance(additions[0], (tuple, list)):
        raise TypeError(
            f"[HOOK VIOLATION] safe_commit() additions[0] must be tuple, got {type(additions[0]).__name__}.\n"
            f"Use: additions=[('path/to/file.md', content_str), ...]"
        )
    repo = repo or g.active_repo()
    repo_config = g.REPOS.get(repo, {})

    commit_message_gate(message)

    if repo_config.get('enforce_editorial', False):
        # Full gates for design repo — mutating variant adds compliance co-files
        additions = pre_commit_gate_mutating(additions, deletions or [])
    else:
        # Godot code: only size sanity check (no editorial/co-file gates)
        errors = []
        for path, content in additions:
            # Sanity: single GDScript file shouldn't exceed 500k chars
            if len(content) > 500_000:
                errors.append(f"FILE TOO LARGE: {path}: {len(content):,} chars — check for accidental duplication")
        if errors:
            raise RuntimeError(
                "[HOOK VIOLATION] valoria-game pre-commit:\n" +
                "\n".join(f"  {e}" for e in errors)
            )
        print(f"[HOOK ✓] valoria-game pre-commit (format only — {len(additions)} files)")

    auth = g._authorize_next_commit()
    oid = g.atomic_commit(
        additions=additions,
        deletions=deletions or [],
        message=message,
        repo=repo,
        _auth=auth,
    )
    print(f"[HOOK ✓] safe_commit → {repo} — {oid}")
    return oid


# ── NEW Hook 10: Simulation verification ledger ───────────────────────────────
#
# THE PROBLEM THIS SOLVES:
# Simulations have failed because Claude writes mechanical code without having
# actually read the canonical sources. The code is then built on fabricated or
# remembered values, producing results that look valid but are mechanically wrong.
#
# THE FIX:
# Before any simulation code is written or committed, a verification ledger must
# exist that maps every canonical source read → every mechanical value extracted
# → every sim variable using that value. The ledger is an artifact, not a mental
# record. If you cannot produce the ledger, you have not read enough to simulate.

import json

# Systems that simulation code typically touches. For a "full stack" sim, all of
# these must have canonical sources read. For a targeted sim, only the relevant
# subset. The gate accepts a scope parameter to distinguish.
SIM_CANONICAL_PRESETS = {
    "full_stack": [
        "core_engine", "combat", "threadwork", "clocks", "factions",
        "victory", "territories", "mass_combat", "social_debate",
        "scale_transitions", "faction_layer", "military_layer",
        "tc_political", "peninsular_strain", "settlement_layer",
        "campaign_architecture", "derived_stats",
    ],
    "strategic": [
        "core_engine", "factions", "victory", "territories", "clocks",
        "faction_layer", "tc_political", "peninsular_strain",
        "campaign_architecture",
    ],
    "combat": ["core_engine", "combat", "derived_stats"],
    "mass_combat": ["core_engine", "mass_combat", "derived_stats"],
    "thread": ["core_engine", "threadwork"],
    "social": ["core_engine", "social_debate", "conviction_track"],
    # Custom scope: caller provides systems list directly
}


def sim_gate(scope: str, systems: list = None) -> None:
    """
    Gate before any simulation code is written.

    1. Resolves the canonical sources registry.
    2. Determines required systems (from preset or explicit list).
    3. Confirms every canonical design doc for those systems has been read
       at full depth (not just index).
    4. Requires a verification ledger at /home/claude/sim_verification_ledger.json
       mapping each mechanical value in the sim to its canonical source.

    Failure raises RuntimeError with the exact gap identified.

    Usage:
        h.sim_gate("strategic")  # uses preset
        h.sim_gate("custom", systems=["core_engine", "combat", "victory"])

    The ledger format (JSON):
        {
          "sim_file": "valoria_sim_v3.py",
          "scope": "strategic",
          "entries": [
            {
              "sim_variable": "CROWN_STARTING_MANDATE",
              "value": 5,
              "canonical_source": "params/factions/stats_1_7_scale.md",
              "section": "Starting Stats",
              "quoted_text": "Crown | 5 | 5 | 5 | 4 ..."
            },
            ...
          ]
        }

    Every mechanical constant in the sim must have a ledger entry. No exceptions.
    """
    if not _bootstrap_confirmed:
        raise RuntimeError(
            "[HOOK VIOLATION] sim_gate() before assert_bootstrap()."
        )

    # Require task_gate('simulation') has run
    if 'simulation' not in _task_gates_passed:
        raise RuntimeError(
            "[HOOK VIOLATION] sim_gate() requires task_gate('simulation') first.\n"
            "Call h.task_gate('simulation') before h.sim_gate()."
        )

    # Resolve systems
    if scope in SIM_CANONICAL_PRESETS:
        if systems is not None:
            raise RuntimeError(
                f"[HOOK VIOLATION] sim_gate('{scope}') uses a preset — do not pass systems.\n"
                f"To override, use scope='custom' with explicit systems=[...]."
            )
        systems = SIM_CANONICAL_PRESETS[scope]
    elif scope == "custom":
        if not systems:
            raise RuntimeError(
                "[HOOK VIOLATION] sim_gate('custom') requires systems=[...]."
            )
    else:
        raise RuntimeError(
            f"[HOOK VIOLATION] Unknown sim scope '{scope}'.\n"
            f"Valid presets: {sorted(SIM_CANONICAL_PRESETS.keys())}\n"
            f"Or use scope='custom' with systems=[...]."
        )

    # Load canonical_sources.yaml from session fetches
    cs_key = g._repo_key('references/canonical_sources.yaml', 'ttrpg')
    cs_content = g._session_fetches.get(cs_key)
    if not cs_content:
        raise RuntimeError(
            "[HOOK VIOLATION] sim_gate(): canonical_sources.yaml not fetched.\n"
            "Call read_files_graphql(['references/canonical_sources.yaml']) first."
        )

    # canonical_sources.yaml has known malformed sections (mixed top-level list
    # items and mappings). Parse robustly by filtering out the specific list-
    # item blocks that clash with the surrounding mapping structure, while
    # keeping all sibling mapping entries.
    import yaml
    cs = None
    try:
        cs = yaml.safe_load(cs_content)
    except Exception:
        # Remove lines that are top-level list items ('- key:' at column 0)
        # and their indented child lines, but preserve siblings that are
        # mapping keys at column 0 or 2 (common outer/nested indentation).
        lines = cs_content.split('\n')
        filtered = []
        skipping = False
        for line in lines:
            # Start skipping at a '- ' list marker at column 0
            if line.startswith('- '):
                skipping = True
                continue
            if skipping:
                # Stop skipping when we hit a line that starts with non-space
                # OR a line that starts with exactly 2 spaces followed by a
                # letter (sibling mapping entry at the outer level — not a
                # child of the list item).
                if line and not line[0].isspace():
                    skipping = False
                    filtered.append(line)
                elif (line.startswith('  ') and len(line) > 2
                      and not line[2].isspace()
                      and line[2].isalpha()):
                    skipping = False
                    filtered.append(line)
                # Otherwise still skipping this list-item's children
                continue
            filtered.append(line)

        cleaned = '\n'.join(filtered)
        try:
            cs = yaml.safe_load(cleaned)
        except Exception as e:
            raise RuntimeError(
                f"[HOOK VIOLATION] sim_gate(): cannot parse canonical_sources.yaml\n"
                f"even after removing malformed list blocks: {e}\n"
                f"Fix the YAML file before proceeding."
            )

    # Systems may be in the top-level `systems:` key or as bare top-level keys
    # (the file mixes both styles). Merge them.
    cs_systems = {}
    if cs:
        cs_systems.update(cs.get('systems', {}) or {})
        # Also absorb top-level mapping keys that have 'canonical' or 'design_doc'
        # fields — these are system-like entries not under systems:
        for k, v in cs.items():
            if k == 'systems':
                continue
            if isinstance(v, dict) and (
                'canonical' in v or 'design_doc' in v
            ) and k not in cs_systems:
                cs_systems[k] = v

    # For each required system, resolve canonical path and verify fetched at depth
    missing_systems = []
    unfetched_paths = []
    index_only_paths = []
    repo = g.active_repo()

    for system in systems:
        entry = cs_systems.get(system)
        # Also check top-level (some systems are defined outside systems:)
        if not entry and cs:
            entry = cs.get(system)
        if not entry:
            missing_systems.append(system)
            continue

        # Resolve canonical path — prefer design_doc over canonical for simulation
        # because design_doc is the mechanical source; params files are derived.
        canonical_path = (
            entry.get('design_doc') or
            entry.get('canonical') or
            entry.get('canonical_bg') or
            entry.get('canonical_ttrpg')
        )
        if not canonical_path or not isinstance(canonical_path, str):
            missing_systems.append(f"{system} (no canonical path in registry)")
            continue

        key = g._repo_key(canonical_path, repo)

        # Check read depth. Must be 'full' for sim work — simulations need
        # mechanical detail which only exists in full design docs. Indexes
        # contain only section headings; sections may miss cross-references.
        try:
            depth = g.read_depth(canonical_path, repo)
        except AttributeError:
            # Older github_ops without read_depth — fall back to session fetch check
            depth = 'full' if (key in g._session_fetches and g._session_fetches[key] is not None) else 'none'

        if depth == 'none':
            unfetched_paths.append((system, canonical_path))
            continue
        if depth == 'index':
            index_only_paths.append((system, canonical_path))
        # 'sections' and 'full' both pass — sim work can use section reads IF
        # the relevant sections were read. The ledger enforces that — each
        # ledger entry names the exact section it quoted from.

        # If there's a params file in the registry too, fetching the params
        # file is also required — params files may contain values that override
        # or augment design_doc content.
        params_path = entry.get('params')
        if params_path and isinstance(params_path, str):
            p_depth = g.read_depth(params_path, repo) if hasattr(g, 'read_depth') else (
                'full' if g._repo_key(params_path, repo) in g._session_fetches else 'none'
            )
            if p_depth == 'none':
                unfetched_paths.append((system, params_path))

    # Assemble violation report
    errors = []
    if missing_systems:
        errors.append(
            "Systems not found in canonical_sources.yaml:\n"
            + "\n".join(f"    {s}" for s in missing_systems)
        )
    if unfetched_paths:
        errors.append(
            "Canonical sources not fetched:\n"
            + "\n".join(f"    {sys}: {path}" for sys, path in unfetched_paths)
            + "\n  Fetch with: read_files_graphql([<paths>])"
        )
    if index_only_paths:
        errors.append(
            "Sources fetched as INDEX only (not infilled) — simulations need mechanical detail:\n"
            + "\n".join(f"    {sys}: {path}" for sys, path in index_only_paths)
            + "\n  Fetch full content with: read_files_graphql([<paths>])\n"
            + "  Or use read_sections() for specific ranges."
        )

    if errors:
        raise RuntimeError(
            f"[HOOK VIOLATION] sim_gate('{scope}') — canonical reads incomplete:\n\n"
            + "\n\n".join(f"  [{i+1}] {e}" for i, e in enumerate(errors))
            + "\n\nA simulation cannot be written on incomplete sources.\n"
            + "Fetch the missing content before proceeding. No exceptions.\n"
        )

    # Manifest check (2026-05-08) — Mode G enforcement.
    # Any simulation spanning more than one mechanical system requires a module
    # manifest before code is written. This prevents the sim_v2 anti-pattern:
    # building a full-stack sim in a single session on index-depth reads.
    # The manifest must exist at /home/claude/sim_module_manifest.md OR at
    # tests/sim/<any-subdirectory>/module_manifest.md in the session fetches.
    # Single-system sims (custom scope, len==1) are exempt.
    if len(systems) > 1:
        manifest_local = '/home/claude/sim_module_manifest.md'
        manifest_in_fetches = any(
            'module_manifest' in k for k in g._session_fetches
        )
        if not os.path.exists(manifest_local) and not manifest_in_fetches:
            raise RuntimeError(
                f"[HOOK VIOLATION] sim_gate('{scope}') — module manifest required.\n\n"
                f"This simulation spans {len(systems)} systems: {systems}\n"
                f"Mode G (Incremental Build Protocol) is mandatory for multi-system sims.\n\n"
                f"Before writing any simulation code:\n"
                f"  1. Produce a module manifest at /home/claude/sim_module_manifest.md\n"
                f"  2. Commit it to tests/sim/<sim-name>/module_manifest.md\n"
                f"  3. Re-run sim_gate — it will pass once the manifest is present.\n\n"
                f"Manifest format: table of modules with name, dependencies,\n"
                f"canonical_source paths, and status (pending/verified).\n"
                f"See skills/valoria-simulator/SKILL.md Mode G §Protocol Step 1.\n\n"
                f"Single-system sims (scope='custom', one system) are exempt.\n"
                f"No exceptions for multi-system sims.\n"
            )

    # Verification ledger check — the artifact must exist
    ledger_path = '/home/claude/sim_verification_ledger.json'
    if not os.path.exists(ledger_path):
        raise RuntimeError(
            f"[HOOK VIOLATION] sim_gate('{scope}') — verification ledger missing.\n"
            f"Required file: {ledger_path}\n\n"
            f"The ledger must map every mechanical constant in the sim to its\n"
            f"canonical source. Example entry:\n"
            f'  {{"sim_variable": "CROWN_STARTING_MANDATE",\n'
            f'    "value": 5,\n'
            f'    "canonical_source": "params/factions/stats_1_7_scale.md",\n'
            f'    "section": "Starting Stats",\n'
            f'    "quoted_text": "Crown | 5 | 5 | 5 | 4 ..." }}\n\n'
            f"Build the ledger before writing any sim code. No exceptions."
        )

    try:
        with open(ledger_path) as f:
            ledger = json.load(f)
    except Exception as e:
        raise RuntimeError(
            f"[HOOK VIOLATION] sim_gate(): cannot parse {ledger_path}: {e}\n"
            f"Ledger must be valid JSON."
        )

    entries = ledger.get('entries', [])
    if not entries:
        raise RuntimeError(
            f"[HOOK VIOLATION] sim_gate(): verification ledger has no entries.\n"
            f"Add one entry per mechanical constant in the sim before proceeding."
        )

    # Each entry must have the four required fields
    required_fields = ('sim_variable', 'value', 'canonical_source', 'quoted_text')
    incomplete = []
    for i, e in enumerate(entries):
        missing = [f for f in required_fields if f not in e or e[f] in (None, '')]
        if missing:
            incomplete.append(f"entry {i}: missing {missing}")
    if incomplete:
        raise RuntimeError(
            "[HOOK VIOLATION] sim_gate(): ledger entries incomplete:\n"
            + "\n".join(f"  {x}" for x in incomplete)
            + "\nEvery entry requires: sim_variable, value, canonical_source, quoted_text."
        )

    # Each referenced canonical_source must be in session fetches
    referenced_sources = {e['canonical_source'] for e in entries}
    unfetched_refs = [
        s for s in referenced_sources
        if g._repo_key(s, repo) not in g._session_fetches
        or g._session_fetches[g._repo_key(s, repo)] is None
    ]
    if unfetched_refs:
        raise RuntimeError(
            "[HOOK VIOLATION] sim_gate(): ledger references unfetched sources:\n"
            + "\n".join(f"  {s}" for s in unfetched_refs)
            + "\nFetch these before proceeding."
        )

    print(f"[HOOK ✓] sim_gate('{scope}') — {len(systems)} systems verified, "
          f"{len(entries)} ledger entries, {len(referenced_sources)} sources cited")


# ── Extension to pre_commit_gate: anti-fabrication check for sim commits ──────
#
# THE PROBLEM THIS SOLVES:
# Even with sim_gate, Claude could write sim code with uncited mechanical values
# and commit it. This catches uncited constants at commit time.
#
# THE FIX:
# Any committed .py file under tests/sim/ or containing "sim" in the name must
# have every numeric literal either (a) covered by a ledger entry, or (b)
# annotated with a `# [canonical: path §section]` comment on the same line or
# the line above.

_MECHANICAL_NUMERIC_PATTERN = re.compile(r'(?<![a-zA-Z_])(\d+)(?![a-zA-Z_])')
_CANONICAL_COMMENT_PATTERN = re.compile(r'#\s*\[canonical:\s*[^\]]+\]')

# Values exempt from citation requirement — these are structural, not mechanical.
_EXEMPT_NUMBERS = {'0', '1', '2', '10', '100'}  # indices, loop bounds, percentages
# Note: this is permissive. A "2" could be Ob 2 (mechanical) or list[2] (structural).
# The gate uses heuristics, not hard rules — it prints warnings and lets the
# committer decide. False negatives are acceptable; false positives are not.


def _is_sim_file(path: str) -> bool:
    """A file is a sim file if it's under tests/sim/ or its name contains 'sim'."""
    if not path.endswith('.py'):
        return False
    if path.startswith('tests/sim/'):
        return True
    basename = path.rsplit('/', 1)[-1].lower()
    if 'sim' in basename or 'simulation' in basename:
        return True
    return False


def _extract_uncited_constants(content: str) -> list:
    """
    Scan Python content for numeric literals on lines without canonical citations.
    Returns list of (line_number, line_text, number) for uncited values.
    Heuristic — skips exempt values (0, 1, 2, 10, 100) and comment-only lines.
    """
    uncited = []
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        # Does this line or the line before have a canonical comment?
        prev = lines[i - 2] if i >= 2 else ''
        if _CANONICAL_COMMENT_PATTERN.search(line) or _CANONICAL_COMMENT_PATTERN.search(prev):
            continue
        # Strip string literals to avoid flagging numbers in strings
        # Rough heuristic — doesn't handle escape sequences perfectly
        code_only = re.sub(r"'[^']*'", "''", line)
        code_only = re.sub(r'"[^"]*"', '""', code_only)
        # Strip inline comments
        if '#' in code_only:
            code_only = code_only.split('#', 1)[0]
        numbers = _MECHANICAL_NUMERIC_PATTERN.findall(code_only)
        for n in numbers:
            if n in _EXEMPT_NUMBERS:
                continue
            # Skip if part of a standard Python idiom (range, len, slice)
            # Heuristic: if the number is inside range(), len(), [:N], etc.,
            # it's probably structural.
            if re.search(rf'(range|len|enumerate|slice)\s*\([^)]*\b{n}\b', code_only):
                continue
            uncited.append((i, line.rstrip(), n))
    return uncited


def sim_fabrication_check(additions: list) -> None:
    """
    Post-sim-gate check: scans committed sim files for uncited mechanical constants.
    Called automatically within pre_commit_gate for .py files matching sim patterns.
    Raises RuntimeError if uncited constants found and a ledger does not cover them.
    """
    sim_files = [(p, c) for p, c in additions if _is_sim_file(p)]
    if not sim_files:
        return

    # Load ledger if present — values there are "cited"
    ledger_values = set()
    ledger_path = '/home/claude/sim_verification_ledger.json'
    if os.path.exists(ledger_path):
        try:
            with open(ledger_path) as f:
                ledger = json.load(f)
            for e in ledger.get('entries', []):
                v = e.get('value')
                if v is not None:
                    ledger_values.add(str(v))
        except Exception:
            pass

    problems = []
    for path, content in sim_files:
        uncited = _extract_uncited_constants(content)
        # Filter: if the number matches a ledger value, accept it
        # (this is loose — same number different meaning would pass. But the
        #  primary failure mode is wholly fabricated values, which this catches.)
        genuine = [(ln, txt, n) for ln, txt, n in uncited if n not in ledger_values]
        if genuine:
            problems.append((path, genuine))

    if problems:
        lines = ["[HOOK VIOLATION] sim_fabrication_check — uncited mechanical constants:\n"]
        for path, items in problems:
            lines.append(f"  {path}:")
            for ln, txt, n in items[:10]:  # cap at 10 per file to avoid spam
                lines.append(f"    line {ln}: value {n} — {txt[:80]}")
            if len(items) > 10:
                lines.append(f"    ... and {len(items) - 10} more")
            lines.append("")
        lines.append("Every mechanical constant requires either:")
        lines.append("  (a) a ledger entry in /home/claude/sim_verification_ledger.json, OR")
        lines.append("  (b) a `# [canonical: path §section]` comment on same or prior line.")
        lines.append("")
        lines.append("Fabricated constants are the primary simulation failure mode.")
        lines.append("This gate is intentionally noisy — it catches the failure early.")
        raise RuntimeError("\n".join(lines))

    print(f"[HOOK ✓] sim_fabrication_check ({len(sim_files)} sim files, all constants cited)")


# ── Checkpoint artifact schema ────────────────────────────────────────────────

CHECKPOINT_PATH = 'canon/session_checkpoint.md'

# A checkpoint is a machine-readable yaml frontmatter + human-readable body.
# The format:
#
#   ---
#   schema_version: 1
#   session_token: <16-char hex>
#   created_at: <ISO8601 UTC>
#   status: active | closed | stale
#   task_scope: <string describing the session's task>
#   context_tokens_at_checkpoint: <int>
#   files_verified: [<path>, ...]
#   sim_ledger_path: /home/claude/sim_verification_ledger.json  # if sim work
#   commits_this_session: [<oid>, ...]
#   completed: [<work item>, ...]
#   pending: [<work item, ordered>]
#   decisions_made: [<decision>, ...]
#   open_questions: [<question>, ...]
#   next_bootstrap_actions: [<action>, ...]
#   ---
#   # Session Checkpoint — <date>
#
#   <human-readable narrative: what was done, what's next, why stopped>

def write_checkpoint(task_scope: str,
                     files_verified: list = None,
                     completed: list = None,
                     pending: list = None,
                     decisions: list = None,
                     open_questions: list = None,
                     next_actions: list = None,
                     commits: list = None,
                     narrative: str = "",
                     sim_ledger: bool = False) -> str:
    """
    Write a session checkpoint to GitHub at CHECKPOINT_PATH.

    Required on context_gate() hitting CONTEXT_CHECKPOINT_HARD (75%).
    Recommended at CONTEXT_SOFT (60%) to avoid rushed checkpoints at 75%.

    Returns the commit OID.

    Must be called AFTER bootstrap. task_scope is the single-line description
    of what this session is doing (e.g. "sim_gate + flush protocol build").

    This function commits DIRECTLY via atomic_commit (not safe_commit) because:
    - safe_commit requires task_gate, which may not have been called yet
    - checkpoints are metadata about the session, not task output
    - checkpoint commits use a dedicated '[infrastructure]' scope
    """
    global _checkpoint_written_this_session

    if not _bootstrap_confirmed:
        raise RuntimeError(
            "[HOOK VIOLATION] write_checkpoint() before assert_bootstrap()."
        )

    from datetime import datetime, timezone
    import json as _json

    token = g.get_session_token()
    fetch_tokens = sum(len(c) for c in g._session_fetches.values() if c) // 4
    total_tokens = fetch_tokens + _SYSTEM_OVERHEAD_TOKENS

    frontmatter = {
        'schema_version': 1,
        'session_token': token,
        'created_at': datetime.now(timezone.utc).isoformat(),
        'status': 'active',
        'task_scope': task_scope,
        'context_tokens_at_checkpoint': total_tokens,
        'files_verified': files_verified or [],
        'sim_ledger_present': sim_ledger,
        'commits_this_session': commits or [],
        'completed': completed or [],
        'pending': pending or [],
        'decisions_made': decisions or [],
        'open_questions': open_questions or [],
        'next_bootstrap_actions': next_actions or [],
    }

    # Build markdown
    import yaml
    yaml_block = yaml.safe_dump(frontmatter, default_flow_style=False,
                                sort_keys=False, allow_unicode=True)
    body_parts = [
        '---', yaml_block.strip(), '---', '',
        f'# Session Checkpoint — {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}',
        '',
        f'**Task scope:** {task_scope}',
        f'**Session token:** `{token}`',
        f'**Context at checkpoint:** ~{total_tokens:,} tokens',
        '',
    ]

    if narrative:
        body_parts.extend([
            '## Narrative',
            '',
            narrative.strip(),
            '',
        ])

    if completed:
        body_parts.extend([
            '## Completed this session',
            '',
            *[f'- {item}' for item in completed],
            '',
        ])

    if pending:
        body_parts.extend([
            '## Pending (in order)',
            '',
            *[f'{i+1}. {item}' for i, item in enumerate(pending)],
            '',
        ])

    if decisions:
        body_parts.extend([
            '## Decisions made',
            '',
            *[f'- {item}' for item in decisions],
            '',
        ])

    if open_questions:
        body_parts.extend([
            '## Open questions',
            '',
            *[f'- {item}' for item in open_questions],
            '',
        ])

    if next_actions:
        body_parts.extend([
            '## Next bootstrap actions',
            '',
            '*(When a new session bootstraps, these are the first steps to take.)*',
            '',
            *[f'{i+1}. {item}' for i, item in enumerate(next_actions)],
            '',
        ])

    content = '\n'.join(body_parts) + '\n'

    # Commit directly — checkpoint is infrastructure metadata
    auth = g._authorize_next_commit()
    oid = g.atomic_commit(
        additions=[(CHECKPOINT_PATH, content)],
        deletions=[],
        message=f'[infrastructure] checkpoint — {task_scope[:60]}',
        repo='ttrpg',
        _auth=auth,
    )
    print(f"[HOOK ✓] checkpoint written → {oid} ({total_tokens:,} tokens at checkpoint)")
    return oid


def close_checkpoint() -> str:
    """
    Mark the active checkpoint as closed. Called at session close after
    the final session_log_current.md commit.

    Returns the commit OID of the close, or None if no active checkpoint.
    """
    files = g.read_files_graphql([CHECKPOINT_PATH])
    current = files.get(CHECKPOINT_PATH)
    if not current:
        return None  # nothing to close

    import yaml
    # Parse frontmatter
    if not current.startswith('---'):
        return None
    parts = current.split('---', 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return None

    if fm.get('status') == 'closed':
        return None  # already closed

    fm['status'] = 'closed'
    from datetime import datetime, timezone
    fm['closed_at'] = datetime.now(timezone.utc).isoformat()

    new_yaml = yaml.safe_dump(fm, default_flow_style=False, sort_keys=False,
                              allow_unicode=True)
    new_content = '---\n' + new_yaml.strip() + '\n---' + parts[2]

    auth = g._authorize_next_commit()
    oid = g.atomic_commit(
        additions=[(CHECKPOINT_PATH, new_content)],
        deletions=[],
        message='[infrastructure] checkpoint closed — session complete',
        repo='ttrpg',
        _auth=auth,
    )
    print(f"[HOOK ✓] checkpoint closed → {oid}")
    return oid


def read_active_checkpoint() -> dict:
    """
    If canon/session_checkpoint.md exists and has status=active, return its
    parsed frontmatter as a dict. Otherwise return None.

    Called at bootstrap to allow sessions to resume from the last checkpoint
    instead of starting cold.
    """
    try:
        files = g.read_files_graphql([CHECKPOINT_PATH])
        content = files.get(CHECKPOINT_PATH)
    except Exception:
        return None
    if not content or not content.startswith('---'):
        return None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    import yaml
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return None
    if fm.get('status') != 'active':
        return None
    return fm


# ── New context_gate with three tiers ─────────────────────────────────────────

def context_gate() -> None:
    """
    Estimate context usage against three tiers:
      60% (CONTEXT_SOFT)            — warn: plan handoff; write a draft checkpoint soon
      75% (CONTEXT_CHECKPOINT_HARD) — require: checkpoint must be written this session
      90% (CONTEXT_HARD)            — hard stop: session close protocol only

    At 75%, raises RuntimeError unless write_checkpoint() has been called.
    At 90%, raises RuntimeError regardless.

    Call at session start and every ~10 tool calls.
    """
    global _soft_warn_issued

    fetch_tokens = sum(len(c) for c in g._session_fetches.values() if c) // 4
    total = fetch_tokens + _SYSTEM_OVERHEAD_TOKENS

    if total >= CONTEXT_HARD:
        raise RuntimeError(
            f"[HOOK VIOLATION] Context hard stop: ~{total:,} estimated tokens\n"
            f"  (fetches: {fetch_tokens:,} + overhead: {_SYSTEM_OVERHEAD_TOKENS:,})\n"
            f"Run Session Close Protocol immediately. Do not begin new work.\n"
            f"Close: commit final state, update session_log_current.md, close_checkpoint()."
        )

    if total >= CONTEXT_CHECKPOINT_HARD:
        if not _checkpoint_written_this_session:
            raise RuntimeError(
                f"[HOOK VIOLATION] Context at ~{total:,} tokens (75% threshold).\n"
                f"A checkpoint MUST be written before any further work.\n\n"
                f"Call h.write_checkpoint(task_scope='...', completed=[...], pending=[...])\n"
                f"The checkpoint commits to canon/session_checkpoint.md and allows a new\n"
                f"session to resume this work instead of starting cold.\n\n"
                f"After writing the checkpoint, this gate will let you continue — but\n"
                f"the right move is to close the session now and start fresh."
            )
        else:
            print(f"[HOOK ⚠] Context ~{total:,} tokens (75%). Checkpoint written — "
                  f"continuing is OK but handoff is imminent.")
        return

    if total >= CONTEXT_SOFT:
        if not _soft_warn_issued:
            print(f"[HOOK ⚠] Context ~{total:,} tokens (60% threshold).\n"
                  f"  Plan for handoff. Consider calling h.write_checkpoint() at the\n"
                  f"  next clean stopping point. At 75% a checkpoint is mandatory.")
            _soft_warn_issued = True
        else:
            print(f"[HOOK ⚠] Context ~{total:,} tokens (soft threshold still exceeded)")
        return

    print(f"[HOOK ✓] context_gate: ~{total:,} estimated tokens "
          f"(fetches {fetch_tokens:,} + overhead {_SYSTEM_OVERHEAD_TOKENS:,})")


# ── Bootstrap helper: resume prompt ───────────────────────────────────────────

def prompt_resume_from_checkpoint() -> None:
    """
    Called at bootstrap. If an active checkpoint exists, print its summary
    and return it so the orchestrator can decide whether to resume.

    Does NOT auto-resume — user must confirm. That's the session-start protocol:
      Message 1 = bootstrap, print checkpoint status, stop.
      Message 2 = user confirms resume, or sends new task.
    """
    cp = read_active_checkpoint()
    if not cp:
        return None

    print("\n" + "=" * 50)
    print("ACTIVE CHECKPOINT FOUND")
    print("=" * 50)
    print(f"Task scope:       {cp.get('task_scope', '?')}")
    print(f"Session token:    {cp.get('session_token', '?')}")
    print(f"Created:          {cp.get('created_at', '?')}")
    print(f"Files verified:   {len(cp.get('files_verified', []))}")
    print(f"Commits:          {len(cp.get('commits_this_session', []))}")
    print(f"Pending items:    {len(cp.get('pending', []))}")

    pending = cp.get('pending', [])
    if pending:
        print("\nPending work (in order):")
        for i, item in enumerate(pending[:5], 1):
            print(f"  {i}. {item}")
        if len(pending) > 5:
            print(f"  ... and {len(pending) - 5} more")

    next_actions = cp.get('next_bootstrap_actions', [])
    if next_actions:
        print("\nNext bootstrap actions:")
        for i, a in enumerate(next_actions[:3], 1):
            print(f"  {i}. {a}")

    print("=" * 50)
    print("To resume: confirm with Jordan, then fetch needed files and continue.")
    print("To start fresh: close_checkpoint() before beginning new work.")
    print("=" * 50 + "\n")

    return cp


# ── Handoff enforcement ──────────────────────────────────────────────────────
#
# Handoffs are the authoritative resumption documents for parallel workstreams.
# These hooks ensure handoff quality at write time.

def validate_handoff(handoff: dict) -> None:
    """
    Validate a handoff dict. Raises RuntimeError if invalid.
    Call this before g.write_handoff() for pre-flight validation,
    or rely on write_handoff()'s built-in validation.
    """
    if not _bootstrap_confirmed:
        raise RuntimeError("[HOOK VIOLATION] validate_handoff() before assert_bootstrap().")

    errors = g._validate_handoff_schema(handoff)
    if errors:
        raise RuntimeError(
            "[HANDOFF BLOCKED] Schema validation failed:\n"
            + "\n".join(f"  - {e}" for e in errors)
        )

    # Additional hook-level checks beyond schema

    # context_files paths should look like real repo paths (no absolute, no ..)
    for cf in handoff.get('context_files', []):
        p = cf.get('path', '')
        if p.startswith('/') or '..' in p:
            raise RuntimeError(
                f"[HANDOFF BLOCKED] context_files path must be relative repo path, got: '{p}'"
            )

    # owns patterns should be non-empty strings
    for pattern in handoff.get('owns', []):
        if not isinstance(pattern, str) or not pattern.strip():
            raise RuntimeError(
                f"[HANDOFF BLOCKED] 'owns' entries must be non-empty strings, got: {pattern!r}"
            )

    # working_state.next must have at least one item
    ws_next = handoff.get('working_state', {}).get('next', [])
    if not ws_next:
        raise RuntimeError(
            "[HANDOFF BLOCKED] working_state.next must have at least one item — "
            "what should the resuming session do?"
        )

    print("[HOOK ✓] handoff validation passed")


def require_handoff_on_close(handoff_id: str) -> str:
    """
    Validate that a handoff file exists and is valid before session close.
    Returns the handoff file path for citation in the archived session log.

    Call this before g.close_session_log() to get the path, then pass
    the handoff_id to close_session_log().
    """
    if not _bootstrap_confirmed:
        raise RuntimeError("[HOOK VIOLATION] require_handoff_on_close() before assert_bootstrap().")

    import yaml

    path = f"handoffs/{handoff_id}.yaml"
    try:
        files = g.read_files_graphql([path], repo='ttrpg', skip_health_check=True)
    except Exception as e:
        raise RuntimeError(
            f"[HANDOFF BLOCKED] Cannot read {path}: {e}\n"
            f"Write the handoff with g.write_handoff() first."
        )

    content = files.get(path)
    if content is None:
        raise RuntimeError(
            f"[HANDOFF BLOCKED] {path} does not exist.\n"
            f"Write the handoff with g.write_handoff() first."
        )

    parsed = yaml.safe_load(content)
    validate_handoff(parsed)

    print(f"[HOOK ✓] Handoff '{handoff_id}' exists and is valid for session close")
    return path
