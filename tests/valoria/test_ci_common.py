"""
Known-answer tests for ci_common.has_main_guard (OI-52a, ED-IN-0097,
audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md §3 Wave 4 item 2).

has_main_guard is the single-owner replacement for TWO independent, divergent
implementations that both existed live before this wave:

  1. skills/valoria-vector-audit/scripts/structure_audit.py's `has_main_guard` — AST-based,
     recognized both operand orders (`__name__ == '__main__'` and the reversed
     `'__main__' == __name__`). The stricter of the two; this is the one that moved here.
  2. tools/build_apparatus_registry.py's `analyze_py()` — a regex over RAW SOURCE TEXT
     (`re.search(r'if\\s+__name__\\s*==\\s*["\\']__main__["\\']', src)`): only the conventional
     operand order, and — because it never parses the source, only pattern-matches its text —
     it cannot tell a real `if __name__ == '__main__':` statement from the same text sitting
     inside a comment or a string literal. That is a real false-positive class, not a
     hypothetical one: any docstring or example comment that shows the idiom (several exist in
     this very corpus, e.g. skill docs quoting the guard as an example) would have made a module
     with NO real CLI entry point read as one.

These tests pin the single owner's behavior directly (conventional order, reversed order,
unguarded, string/comment false-positive rejection) and — since build_apparatus_registry.py is
the ONE consumer this lane (L-cycle) owns and rewires this wave — that its `analyze_py()` now
calls through to ci_common.has_main_guard and no longer regex-false-positives on the planted
comment/string case. (The SECOND consumer, structure_audit.py, is the join lane's edit this same
wave per the file-ownership split in .claude/wf_wave4_central.js's header — not touched here; the
cross-consumer "perturb the owner, both fail" mutation reasoning is the Adjudicate phase's job
once both lanes have landed, per the wave's ADJ_SCHEMA item 1. What IS documented here, per §0.1
point 3 ("name the falsifier"): perturbing ci_common.has_main_guard (e.g. deleting the reversed-
operand branch, or making it always return False) breaks
test_has_main_guard_conventional_and_reversed_forms below AND
test_build_apparatus_registry_analyze_py_uses_the_shared_predicate below — the one owner, two
consumers this lane can independently verify.)
"""
import ast
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_common  # noqa: E402


# ── the owner: ci_common.has_main_guard — known answers ─────────────────────────────────────────

def test_has_main_guard_conventional_and_reversed_forms():
    conventional = ast.parse("if __name__ == '__main__':\n    pass\n")
    assert ci_common.has_main_guard(conventional) is True

    reversed_form = ast.parse("if '__main__' == __name__:\n    pass\n")
    assert ci_common.has_main_guard(reversed_form) is True


def test_has_main_guard_absent_on_unguarded_and_empty_modules():
    unguarded = ast.parse("X = 1\nif X == 2:\n    pass\n")
    assert ci_common.has_main_guard(unguarded) is False

    empty = ast.parse("")
    assert ci_common.has_main_guard(empty) is False


def test_has_main_guard_rejects_comment_false_positive():
    # A regex over raw text (the OLD build_apparatus_registry.py implementation) matches this
    # line; the AST never sees a comment at all, so the real predicate must not.
    src = "# if __name__ == '__main__':\n#     pass\nX = 1\n"
    tree = ast.parse(src)
    assert ci_common.has_main_guard(tree) is False


def test_has_main_guard_rejects_string_literal_false_positive():
    # Same hazard, inside a string literal (e.g. a docstring/example quoting the idiom) rather
    # than a comment — also invisible to the AST's statement structure.
    src = 'DOC = "if __name__ == \'__main__\':\\n    pass"\n'
    tree = ast.parse(src)
    assert ci_common.has_main_guard(tree) is False


def test_has_main_guard_rejects_non_dunder_equality():
    # Same shape (an `if X == Y:` comparison), neither operand is the real __name__/__main__
    # pair — must not match on comparison shape alone.
    src = "if some_name == 'main':\n    pass\n"
    tree = ast.parse(src)
    assert ci_common.has_main_guard(tree) is False


# ── the consumer this lane owns: build_apparatus_registry.analyze_py ────────────────────────────

def _load_apparatus_registry():
    import importlib.util
    root = os.path.join(os.path.dirname(__file__), '..', '..')
    path = os.path.join(root, 'tools', 'build_apparatus_registry.py')
    spec = importlib.util.spec_from_file_location('build_apparatus_registry', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_build_apparatus_registry_analyze_py_uses_the_shared_predicate(tmp_path):
    bar = _load_apparatus_registry()

    real_guard = tmp_path / "real_cli.py"
    real_guard.write_text("if __name__ == '__main__':\n    pass\n", encoding="utf-8")
    assert bar.analyze_py(real_guard)["has_main"] is True

    reversed_guard = tmp_path / "reversed_cli.py"
    reversed_guard.write_text("if '__main__' == __name__:\n    pass\n", encoding="utf-8")
    assert bar.analyze_py(reversed_guard)["has_main"] is True


def test_build_apparatus_registry_no_longer_false_positives_on_a_comment(tmp_path):
    # The exact regression the OLD regex-over-raw-text implementation was exposed to: a module
    # with no real CLI entry point, whose only trace of the guard text is a comment.
    bar = _load_apparatus_registry()
    fake = tmp_path / "not_a_cli.py"
    fake.write_text(
        "# Example: if __name__ == '__main__':\n"
        "#     run()\n"
        "def helper():\n"
        "    return 1\n",
        encoding="utf-8",
    )
    assert bar.analyze_py(fake)["has_main"] is False


def test_build_apparatus_registry_imports_ci_common_not_a_local_regex():
    # Single-owner check: the module must consume the SAME function object (not a re-implemented
    # copy), and must not carry its own re.search-based guard predicate any more.
    bar = _load_apparatus_registry()
    assert bar.ci_common.has_main_guard is ci_common.has_main_guard
    src_path = os.path.join(os.path.dirname(__file__), '..', '..', 'tools',
                             'build_apparatus_registry.py')
    src = open(src_path, encoding='utf-8').read()
    # Check the live executable line, not the module's own doc comment describing the old
    # implementation (which quotes the pattern verbatim as a citation, per §0.1's own provenance
    # discipline — matching on that text would be exactly the comment/string false-positive class
    # this consolidation exists to fix).
    assert 'has_main = bool(re.search(' not in src, (
        "build_apparatus_registry.py still carries the old regex-based __main__-guard assignment — "
        "the single-owner consolidation was supposed to delete it"
    )
    assert 'has_main = ci_common.has_main_guard(tree)' in src, (
        "build_apparatus_registry.py's analyze_py() no longer calls the single-owner predicate"
    )
