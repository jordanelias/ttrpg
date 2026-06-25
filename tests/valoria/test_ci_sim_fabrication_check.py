"""
Unit tests for the pure cores of ci_sim_fabrication_check.

extract_uncited_constants and genuine_violations are I/O-free. These tests pin
the ported heuristics: exempt numbers, range/len/enumerate/slice idiom skipping,
string-literal stripping, inline `# [canonical: ...]` citations, and ledger-value
filtering. Also covers the is_sim_file path classifier.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_sim_fabrication_check  # noqa: E402


def _numbers(violations):
    """Helper: the set of flagged number strings from a violations list."""
    return {n for _ln, _txt, n in violations}


# (a) An uncited mechanical constant is flagged.
def test_uncited_constant_flagged():
    content = "SPEED = 7\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert len(violations) == 1
    ln, txt, n = violations[0]
    assert ln == 1
    assert n == '7'
    assert 'SPEED = 7' in txt


# (b) The same line with a canonical citation is NOT flagged.
def test_inline_canonical_citation_not_flagged():
    content = "SPEED = 7  # [canonical: params/core.md §X]\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


def test_prior_line_canonical_citation_not_flagged():
    content = "# [canonical: params/core.md §X]\nSPEED = 7\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


# (c) Exempt numbers and idiom-wrapped numbers are NOT flagged.
def test_exempt_numbers_and_range_idiom_not_flagged():
    content = "for i in range(10):\n    x = 0\n    y = 1\n    z = 2\n    pct = 100\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


def test_range_with_nonexempt_bound_not_flagged():
    # 7 is non-exempt but sits inside a range() idiom -> structural, skipped.
    content = "for i in range(7):\n    pass\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


def test_len_idiom_skips_number_inside_parens():
    # The idiom heuristic only skips numbers that sit INSIDE range/len/etc parens.
    content = "chunk = data[: len(other) + 7]\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    # 7 is OUTSIDE len(...) -> not idiom-protected -> flagged (faithful to the port).
    assert _numbers(violations) == {'7'}
    # But a number INSIDE len(...) is skipped as structural.
    content2 = "chunk = data[len(other[7]):]\n"
    violations2 = ci_sim_fabrication_check.extract_uncited_constants(content2)
    assert violations2 == []


# (d) genuine_violations filters out a number present in the ledger.
def test_genuine_violations_filters_ledger_value():
    content = "DAMAGE = 7\nARMOR = 9\n"
    # Without a ledger, both are flagged.
    none_filtered = ci_sim_fabrication_check.genuine_violations(content, set())
    assert _numbers(none_filtered) == {'7', '9'}
    # With '7' in the ledger, only '9' survives.
    filtered = ci_sim_fabrication_check.genuine_violations(content, {'7'})
    assert _numbers(filtered) == {'9'}


def test_genuine_violations_none_ledger_safe():
    content = "DAMAGE = 7\n"
    assert _numbers(ci_sim_fabrication_check.genuine_violations(content, None)) == {'7'}


# (e) A number inside a string literal is NOT flagged.
def test_number_in_string_literal_not_flagged():
    content = 'name = "agent 7"\n'
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


def test_number_in_single_quoted_string_not_flagged():
    content = "label = 'tier 7 unit'\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


def test_number_in_inline_comment_not_flagged():
    content = "speed = base  # bump to 7 later\n"
    violations = ci_sim_fabrication_check.extract_uncited_constants(content)
    assert violations == []


# is_sim_file path classifier.
def test_is_sim_file_classification():
    assert ci_sim_fabrication_check.is_sim_file('tests/sim/foo/bar.py') is True
    assert ci_sim_fabrication_check.is_sim_file('engine/combat_sim.py') is True
    assert ci_sim_fabrication_check.is_sim_file('engine/simulation_core.py') is True
    # Non-.py is never a sim file, even under tests/sim/.
    assert ci_sim_fabrication_check.is_sim_file('tests/sim/foo/report.md') is False
    # Plain code with no 'sim' in the basename and not under tests/sim/.
    assert ci_sim_fabrication_check.is_sim_file('tools/ci_common.py') is False
    # Windows-style separators are normalized.
    assert ci_sim_fabrication_check.is_sim_file('tests\\sim\\foo\\bar.py') is True


if __name__ == '__main__':
    # Lightweight driver so the suite is runnable without pytest installed.
    funcs = [v for k, v in sorted(globals().items())
             if k.startswith('test_') and callable(v)]
    passed = failed = 0
    for fn in funcs:
        try:
            fn()
            passed += 1
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"ERROR {fn.__name__}: {type(exc).__name__}: {exc}")
    print(f"{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
