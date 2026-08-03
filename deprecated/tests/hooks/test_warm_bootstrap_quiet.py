"""Regression test for the warm-quiet bootstrap fix (commit bd59441b).

quick_bootstrap() must print the verbose status block (handoffs / roadmap /
lane / index summary) only on the FIRST bootstrap of a session; warm
re-bootstraps print one terse line. This guards that gating from being
silently reverted by a future edit to quick_bootstrap.

Structural (AST/source) test: imports github_ops and inspects quick_bootstrap's
source. No network, no mocks, no call into quick_bootstrap — cannot be flaky.
"""
import ast
import inspect
import os
import sys
import textwrap

# Portable import: repo layout first, ad-hoc /home/claude fallback.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/claude")  # fallback for ad-hoc container runs
sys.path.insert(0, os.path.join(_HERE, "..", "..", "skills", "valoria-orchestrator", "scripts"))  # repo (authoritative)
import github_ops  # noqa: E402

GATED = {"report_handoffs", "report_roadmap", "report_lane", "print_index_summary"}


def _quick_bootstrap_funcdef():
    src = textwrap.dedent(inspect.getsource(github_ops.quick_bootstrap))
    return ast.parse(src).body[0]


def test_force_full_param_exists():
    params = inspect.signature(github_ops.quick_bootstrap).parameters
    assert "force_full" in params, "quick_bootstrap lost its force_full escape hatch"
    assert params["force_full"].default is False


def test_first_bootstrap_signal_defined():
    src = inspect.getsource(github_ops.quick_bootstrap)
    assert "first_bootstrap" in src, "first_bootstrap signal removed"
    assert "cache_hit" in src, "first_bootstrap must derive from cache_hit"


def test_terse_warm_path_present():
    src = inspect.getsource(github_ops.quick_bootstrap)
    assert "if not first_bootstrap" in src, "terse warm branch removed"
    assert "warm" in src.lower(), "terse warm line removed"


def test_reporters_gated_by_first_bootstrap():
    func = _quick_bootstrap_funcdef()
    parents = {}
    for node in ast.walk(func):
        for child in ast.iter_child_nodes(node):
            parents[child] = node

    def guarded(n):
        cur = n
        while cur in parents:
            cur = parents[cur]
            if isinstance(cur, ast.If):
                names = {x.id for x in ast.walk(cur.test) if isinstance(x, ast.Name)}
                if "first_bootstrap" in names:
                    return True
        return False

    found = set()
    for node in ast.walk(func):
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
            if name in GATED:
                found.add(name)
                assert guarded(node), f"{name}() is no longer guarded by first_bootstrap"
    assert found, "expected at least one gated reporter call in quick_bootstrap"


if __name__ == "__main__":
    test_force_full_param_exists()
    test_first_bootstrap_signal_defined()
    test_terse_warm_path_present()
    test_reporters_gated_by_first_bootstrap()
    print("ALL PASS")
