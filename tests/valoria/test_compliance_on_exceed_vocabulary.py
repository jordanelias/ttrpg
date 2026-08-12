"""Guard for the `on_exceed` severity vocabulary in tools/compliance_check.py (ED-IN-0098).

WHY THIS EXISTS (§0.1 #5 — the guard is what makes a sweep a sweep). The severity was computed
inline as `'warn' if on_exceed.startswith('flag') else 'error'`, which silently graded every
token outside the `flag*` family as a BLOCKING error. Two declared tokens fell through it:

  * `warn_only`        — declared on 12 files, whose entire purpose is to not block
  * `chunk_by_quarter` — a split strategy, not a severity at all

Neither had ever worked. It surfaced only when a legitimate growth in module_contracts.yaml
tripped a blocking gate its own policy entry had already declared non-blocking (W4/ED-IN-0097),
and that wave raised the cap to route around it rather than fixing the vocabulary.

The tests below pin two things a comment cannot enforce: that every token actually declared in
the policy file is implemented, and that an unimplemented token fails LOUDLY instead of
defaulting to a blocking error indistinguishable from an intentional one.
"""
import ast
import os
import re
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import compliance_check as cc  # noqa: E402

RULES = os.path.join(ROOT, 'references', 'atomization_rules.yaml')


def declared_tokens():
    """Every distinct on_exceed value in the policy file."""
    text = open(RULES, encoding='utf-8', errors='replace').read()
    return sorted(set(re.findall(r'on_exceed:\s*"([a-z_]+)"', text)))


def test_every_declared_token_is_implemented():
    """The failure this whole module exists for: a declared token nothing implements."""
    declared = declared_tokens()
    assert declared, 'no on_exceed tokens found in atomization_rules.yaml — parser drifted'
    unimplemented = [t for t in declared if t not in cc.ON_EXCEED_KNOWN]
    assert not unimplemented, (
        f'atomization_rules.yaml declares on_exceed token(s) that compliance_check.py does not '
        f'implement: {unimplemented}. They would grade as blocking errors by accident.')


def test_warn_only_is_advisory_not_blocking():
    """The specific regression: `warn_only` must never block. 12 files depend on it."""
    assert cc._on_exceed_severity('warn_only', 'references/module_contracts.yaml') == 'warn'
    assert 'warn_only' not in cc.ON_EXCEED_BLOCKING


def test_chunk_by_quarter_is_advisory():
    """A split strategy is not a severity — it must not block."""
    assert cc._on_exceed_severity('chunk_by_quarter', 'x.md') == 'warn'


@pytest.mark.parametrize('token', ['error', 'block_commit'])
def test_blocking_tokens_still_block(token):
    """The fix must not loosen the tokens that are SUPPOSED to block (no over-correction)."""
    assert cc._on_exceed_severity(token, 'x.md') == 'error'


@pytest.mark.parametrize('token', [
    'flag_for_split', 'flag_unknown_pattern', 'flag_for_next_session', 'flag_for_manual_archive',
])
def test_flag_family_remains_advisory(token):
    """Behaviour preserved for the family the old inline rule DID handle correctly."""
    assert cc._on_exceed_severity(token, 'x.md') == 'warn'


def test_unknown_token_fails_loudly_and_names_itself():
    """A typo must be a loud error, not a silent blocking default.

    This is the assertion that makes the fix a sweep rather than a patch: the next unimplemented
    token cannot repeat `warn_only`'s history of failing silently for weeks.
    """
    with pytest.raises(cc.UnknownOnExceedToken) as exc:
        cc._on_exceed_severity('warn_onlyy', 'references/some_file.yaml')
    msg = str(exc.value)
    assert 'warn_onlyy' in msg, 'the exception must name the offending token'
    assert 'references/some_file.yaml' in msg, 'the exception must name the file that declared it'


def test_severity_is_single_owned_no_inline_copy_remains():
    """No site may recompute the rule. The `startswith('flag')` idiom must be gone from live code.

    It appears once more in this file — inside the owner's own explanatory comment, quoting the
    defect — so the assertion counts occurrences outside comment lines rather than banning the
    string outright.
    """
    src = open(os.path.join(ROOT, 'tools', 'compliance_check.py'),
               encoding='utf-8', errors='replace').read()
    live = [ln.strip() for ln in src.splitlines()
            if "startswith('flag')" in ln and not ln.strip().startswith('#')]
    assert not live, f'an inline on_exceed severity copy survives outside the owner: {live}'

    # And every consumer must call the owner.
    #
    # CO-CHANGED 2026-08-12 by plan step G1 (ED-IN-0159 §1.5), which the plan
    # required to land in the same commit as the excision. This assertion used to
    # read `count(...) >= 3` — the owner's definition plus TWO call sites,
    # `_check_size` and the CI-mode path. `_check_size` is gone: its only caller
    # was `check_all()`, excised with the orchestrator on 2026-08-05, so it had
    # been unreachable for a week. One consumer now remains.
    #
    # The count is replaced rather than decremented. A literal `>= N` re-breaks on
    # every future edit and says nothing about the property it stands for; what the
    # test actually means is "no site computes a severity except through the
    # owner", so assert THAT: every assignment to a `severity` variable is either
    # a call to the owner or a read of a Violation's field.
    # AST, not a regex over lines. The regex first written here (`^severity\\s*=`)
    # flagged `severity=severity,` — a KEYWORD ARGUMENT inside a `Violation(...)`
    # call, not an assignment at all. A textual proxy for a syntactic property
    # reports the property it can see, not the one it means; the parser knows the
    # difference between `ast.Assign` and `ast.keyword` and cannot be fooled by
    # indentation or line breaks.
    assert '_on_exceed_severity(' in src, 'the owner itself is gone'
    strays = []
    for node in ast.walk(ast.parse(src)):
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == 'severity' for t in node.targets):
            continue
        v = node.value
        via_owner = (isinstance(v, ast.Call) and isinstance(v.func, ast.Name)
                     and v.func.id == '_on_exceed_severity')
        if not via_owner:
            strays.append(f'{node.lineno}: severity = {ast.unparse(v)}')
    assert not strays, f'a severity is computed without the owner: {strays}'

    # ...and the one surviving consumer really is wired to it, so the assertion
    # above cannot pass vacuously by there being no consumers at all.
    assert src.count('_on_exceed_severity(') >= 2, (
        'expected the owner definition plus at least one live call site; if this '
        'drops to 1 the gate has no consumer and the vocabulary is unenforced')
