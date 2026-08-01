"""
Drift guard for the canonical scope vocabulary (Lane B item 5.8 / resolved-decision D6).

The three scope/type constructs — commit scopes, session scopes, task types — were
historically disjoint with no single source of truth (the D6 defect). This test makes
`references/scope_vocabulary.md` authoritative: it locks each construct's current
membership and asserts their union equals the documented canonical vocabulary.

Effect: any future change to a scope set (add/remove/rename) in valoria_hooks or
github_ops fails this test until `references/scope_vocabulary.md` AND the EXPECTED_*
sets below are updated in the same change. That co-update requirement is the
single-source-of-truth enforcement D6 asks for.

It is NON-BREAKING: it asserts the live sets as they are (2026-05-31); it does not
narrow any gate. The D6 reduction to ~10 (which removes live scopes and must wait for
a non-parallel window + Jordan's merge decisions) will update the EXPECTED_* sets here.

Convention matches tests/hooks/test_correctness_gates.py.
"""

import sys
sys.path.insert(0, '/home/claude')
import valoria_hooks   # noqa: E402  — COMMIT_SCOPES, TASK_REQUIRED_FILES
import github_ops       # noqa: E402  — SESSION_SCOPES


# ── Authoritative record (mirrors references/scope_vocabulary.md, verified 2026-05-31) ──

EXPECTED_COMMIT_SCOPES = {
    'editorial', 'patch', 'simulation', 'compilation', 'infrastructure',
    'skill', 'cleanup', 'godot', 'phase', 'fix', 'bugfix',
}
EXPECTED_SESSION_SCOPES = {
    'infrastructure', 'godot', 'editorial', 'design', 'simulation', 'audit', 'general',
}
EXPECTED_TASK_TYPES = {
    'simulation', 'audit', 'canon_check', 'editorial', 'patch', 'compilation',
    'propose_mechanic', 'design_proposal', 'design', 'infrastructure',
}
# Canonical vocabulary = the union of the three axes.
CANONICAL_VOCABULARY = EXPECTED_COMMIT_SCOPES | EXPECTED_SESSION_SCOPES | EXPECTED_TASK_TYPES


def _live_commit_scopes():
    return set(valoria_hooks.COMMIT_SCOPES)


def _live_session_scopes():
    return set(github_ops.SESSION_SCOPES)


def _live_task_types():
    return set(valoria_hooks.TASK_REQUIRED_FILES.keys())


# ── Per-construct membership locks (catch silent drift in any one set) ──

def test_commit_scopes_match_record():
    assert _live_commit_scopes() == EXPECTED_COMMIT_SCOPES, (
        "COMMIT_FORMAT scopes changed — update references/scope_vocabulary.md "
        "and EXPECTED_COMMIT_SCOPES together."
    )


def test_session_scopes_match_record():
    assert _live_session_scopes() == EXPECTED_SESSION_SCOPES, (
        "SESSION_SCOPES changed — update references/scope_vocabulary.md "
        "and EXPECTED_SESSION_SCOPES together."
    )


def test_task_types_match_record():
    assert _live_task_types() == EXPECTED_TASK_TYPES, (
        "TASK_REQUIRED_FILES keys changed — update references/scope_vocabulary.md "
        "and EXPECTED_TASK_TYPES together."
    )


# ── Vocabulary consistency (the D6 single-source assertion) ──

def test_union_equals_canonical_vocabulary():
    union = _live_commit_scopes() | _live_session_scopes() | _live_task_types()
    assert union == CANONICAL_VOCABULARY, (
        f"Scope vocabulary drift. Union={sorted(union)} "
        f"vs canonical={sorted(CANONICAL_VOCABULARY)}. "
        "A scope was added/removed in one construct — reconcile in scope_vocabulary.md."
    )


def test_each_construct_is_subset_of_vocabulary():
    assert _live_commit_scopes() <= CANONICAL_VOCABULARY
    assert _live_session_scopes() <= CANONICAL_VOCABULARY
    assert _live_task_types() <= CANONICAL_VOCABULARY


def test_commit_format_pattern_contains_all_scopes():
    # Guard the COMMIT_FORMAT regex actually encodes every commit scope
    # (COMMIT_SCOPES is parsed from this pattern at L74).
    pat = valoria_hooks.COMMIT_FORMAT.pattern
    for s in EXPECTED_COMMIT_SCOPES:
        assert s in pat, f"commit scope '{s}' missing from COMMIT_FORMAT regex"
