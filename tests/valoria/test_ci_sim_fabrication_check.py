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


# ── ED-1053 hardening: float tokenization (§4.2) ──────────────────────────────
def test_float_is_one_token_not_split():
    # `1.7` must scan as a single literal, not `1` (exempt) + `7`.
    violations = ci_sim_fabrication_check.extract_uncited_constants("LETHALITY = 1.7\n")
    assert _numbers(violations) == {'1.7'}


def test_fabricated_float_not_excused_by_integer_token_collision():
    # The §4.2 hole: `1.7` split to `7`, and `7` in the ledger excused it.
    # By-pair matcher with `7` as a loose value must STILL flag `1.7`.
    v = ci_sim_fabrication_check.genuine_violations_by_pair("LETHALITY = 1.7\n", {}, {'7'})
    assert _numbers(v) == {'1.7'}


def test_trivial_dot_zero_floats_are_exempt():
    content = "a = 1.0\nb = 2.0\nc = 100.0\n"
    assert ci_sim_fabrication_check.extract_uncited_constants(content) == []


# ── ED-1053 hardening: (variable, value) matching (§4.1) ───────────────────────
def test_by_pair_flags_value_collision_under_wrong_variable():
    # `25` is a ledger value but registered for BATTLEFIELD_SIZE, not FABRICATED_CRIT.
    pairs = {'BATTLEFIELD_SIZE': {'25'}}
    v = ci_sim_fabrication_check.genuine_violations_by_pair(
        "FABRICATED_CRIT = 25\n", pairs, {'25'})
    assert _numbers(v) == {'25'}


def test_by_pair_cites_registered_variable():
    pairs = {'BATTLEFIELD_SIZE': {'25'}}
    v = ci_sim_fabrication_check.genuine_violations_by_pair(
        "BATTLEFIELD_SIZE = 25\n", pairs, {'25'})
    assert v == []


def test_by_pair_unassigned_literal_keeps_loose_value_match():
    # No assignment target -> loose value-match against the flat ledger set.
    v = ci_sim_fabrication_check.genuine_violations_by_pair(
        "total = compute([25, 30])\n", {}, {'25'})
    assert _numbers(v) == {'30'}  # 25 excused loosely, 30 not in ledger -> flagged


def test_by_pair_numeric_normalization():
    # 0.60 (code) must match 0.6 (ledger JSON float) for the same variable.
    pairs = {'ADEF': {'0.6'}}
    v = ci_sim_fabrication_check.genuine_violations_by_pair("ADEF = 0.60\n", pairs, set())
    assert v == []


def test_num_match_int_float_equivalence():
    assert ci_sim_fabrication_check._num_match('25', {'25.0'}) is True
    assert ci_sim_fabrication_check._num_match('0.60', {'0.6'}) is True
    assert ci_sim_fabrication_check._num_match('7', {'8', '9'}) is False


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


# ── the FORK provenance vocabulary (ED-IN-0188) ────────────────────────────────────────────────
# These ship WITH the FORK addition rather than after it (CLAUDE.md §0.1 point 3). The first draft
# of that gate shipped with no test and two real defects — it accepted English words spelled in hex
# (`defaced`) and REJECTED the symbolic ref form `tests/valoria/test_forked_status.py` already pins
# as valid. Both are pinned below so neither can come back.

def test_fork_is_accepted_as_provenance_like_the_other_markers():
    """A FORK-tagged constant is CITED. Without this the marker is decoration."""
    assert ci_sim_fabrication_check._CANONICAL_COMMENT_PATTERN.search(
        'X = 3  # [FORK: mc_v17.py Muster Ob 1 — source at ref c451bcb]')


def test_a_fork_tag_must_name_a_ref():
    """The whole point of the marker: it says WHERE the source went."""
    assert ci_sim_fabrication_check._FORK_REF_PATTERN.search('mc_v17.py Muster Ob 1 — source at ref c451bcb')
    assert ci_sim_fabrication_check._FORK_REF_PATTERN.search('refs/tags/pre-evacuation-2026-08-05')
    assert not ci_sim_fabrication_check._FORK_REF_PATTERN.search('the old params tree, wherever that went')


def test_a_hex_looking_english_word_is_not_a_ref():
    """`[0-9a-f]{7,40}` alone matches ordinary words — the defect the digit requirement closes.

    Without this the tag `[FORK: the file was defaced]` would satisfy a gate whose entire job is to
    make provenance checkable.
    """
    for word in ('defaced', 'acceded', 'deadbeef', 'facade'):
        assert not ci_sim_fabrication_check._FORK_REF_PATTERN.search(word), word


def test_every_real_fork_tag_in_the_tree_is_visible_and_carries_a_ref():
    """Reads the ACTUAL tags on disk, not a hand-written example.

    ⚠ THIS TEST USED TO ASSERT AGAINST AN INVENTED STRING, and that made it worthless in the exact
    way it was written to prevent. Four of ED-IN-0188's FORK tags live in module DOCSTRINGS, and at
    the time they were written as bare `FORK: ...` with no brackets -- so `_FORK_TAG_PATTERN`
    (which requires `[FORK: ...]`) could not see any of them, while this test passed against a
    bracketed example no real site used. An adversarial pass caught it. The four sites are now
    bracketed so they are genuinely checkable, and this test reads them off disk so the two can
    never drift apart again.
    """
    import pathlib
    root = pathlib.Path(__file__).resolve().parents[2]
    tagged = []
    for rel in ('engine/autoload/game_state.py', 'engine/autoload/season_manager.py',
                'systems/factions/sim/absolution.py', 'systems/factions/sim/faction_action.py'):
        text = (root / rel).read_text(encoding='utf-8')
        for m in ci_sim_fabrication_check._FORK_TAG_PATTERN.finditer(text):
            tagged.append((rel, m.group(1)))
            assert ci_sim_fabrication_check._FORK_REF_PATTERN.search(m.group(1)), \
                f'{rel}: FORK tag names no ref -- {m.group(1)[:70]}'
    # The count guard is what stops this passing on an empty sweep (CLAUDE.md 0.1 point 2): if the
    # tags are ever unbracketed again, `tagged` empties and the assertion below fails loudly.
    assert len(tagged) >= 9, f'expected >=9 FORK tags across those four files, found {len(tagged)}'
    assert sum(1 for rel, _ in tagged if rel != 'systems/factions/sim/faction_action.py') >= 3, \
        'the DOCSTRING tags (game_state, season_manager, absolution) are not being seen'
