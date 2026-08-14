"""Expected-delta test for `tools/ci_co_file_checker.py` (plan step G2, ED-IN-0164).

WHY THIS FILE EXISTS. G2 removed Rule 4 from a BLOCKING gate, and an adversarial
pass established that **the gate had no test at all** — `test_gate_coverage.py:112`
pins only its command string, so nothing asserted that Rules 1-3 still fire after
the edit. `01_plan.md:28-29` is explicit that every migration of a blocking gate
ships its own expected-delta test; that requirement was met for G7 and G8 and
missed for G2. This closes it.

Rule 4 required a design-doc change to co-change `engine/params/{system}.md`. That
tree was EVACUATED 2026-08-05 (ED-IN-0145), so the rule examined zero items for a
week before removal. Its retirement is therefore expected-delta-NONE by
construction — but "by construction" is the claim, and the claim is what a test
exists to establish.

ONE CORRECTION TO THE RETIREMENT'S OWN JUSTIFICATION, recorded here because the
tombstone in the gate stated it too strongly. It said six `--check` gates "now
carry" Rule 4's mechanism and are "strictly stronger". Both halves overreach:
those six run **code -> generated artifact**, Rule 4 ran **design doc -> params
prose**, and all six pre-existed the retirement, so nothing was transferred. The
accurate statement is that Rule 4's SUBJECT was evacuated, leaving the rule with
nothing to check — and that the corpus retains strong code-to-artifact freshness
gating independently. The tombstone is corrected to say that.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, 'tools', 'ci_co_file_checker.py')


def _src():
    return Path(GATE).read_text(encoding='utf-8')


def test_rules_1_to_3_are_still_present_and_rule_4_is_gone():
    """The direct expected-delta assertion: three rules in, one out."""
    src = _src()
    for n, subject in ((1, 'canonical_sources'), (2, 'propagation_map'), (3, 'coverage_matrix')):
        assert re.search(rf'^# ── Rule {n}:', src, re.M), f'Rule {n} disappeared'
        assert subject in src, f"Rule {n}'s subject ({subject}) is no longer referenced"
    live = [ln for ln in src.splitlines()
            if re.match(r'^# ── Rule 4:', ln) and 'RETIRED' not in ln]
    assert not live, 'Rule 4 came back without a decision'


def test_rule_4s_subject_really_is_absent_from_the_tree():
    """The whole basis for the retirement. If `engine/params/` ever returns — its
    disposition is one of the surfaces CLAUDE.md §5-7 HOLDS for Jordan — this fails,
    which is the correct signal to reconsider rather than to leave the gate silently
    unable to resume."""
    assert not os.path.isdir(os.path.join(ROOT, 'engine', 'params')), (
        'engine/params/ is back — Rule 4 was retired because its subject was '
        'evacuated, so its retirement needs re-deciding, not ignoring')


def test_the_gate_still_runs_and_still_reports():
    """Non-vacuity: the gate executes and produces its report line. A gate that
    crashed after the edit would also 'not report violations'.

    ⚠ REWRITTEN 2026-08-14 (ED-IN-0186). The first version ran the gate in `--local`
    mode against the AMBIENT WORKING TREE, so its input was "whatever the author
    happened to have uncommitted". On a clean tree the gate correctly prints
    "No changed files detected. Skipping co-file check." and the assertion failed —
    **the test passed or failed based on whether you had unsaved work**, which is the
    one thing it was not trying to measure.

    It went unnoticed because a session almost always runs the suite mid-change. It
    surfaced only when the suite was run against a fully committed and pushed tree,
    which is the state CI is closest to.

    A test whose verdict depends on ambient environment measures the environment, not
    the subject. So this now builds a deterministic COMPLIANT changeset — the same
    temp-repo technique `test_rule_1_actually_REJECTS_a_changeset_it_must_reject`
    below already uses — and requires the gate to run it and report. The non-vacuity
    intent is unchanged; only its input is now controlled instead of borrowed.
    """
    import subprocess as sp
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        def git(*a):
            return sp.run(['git', *a], cwd=td, capture_output=True, text=True)
        git('init', '-q')
        git('config', 'user.email', 't@t')
        git('config', 'user.name', 't')
        doc = Path(td) / 'systems' / 'combat' / 'thing_v30.md'
        doc.parent.mkdir(parents=True)
        doc.write_text('# seed\n', encoding='utf-8')
        (Path(td) / 'references').mkdir()
        cs = Path(td) / 'references' / 'canonical_sources.yaml'
        cs.write_text('a: 1\n', encoding='utf-8')
        git('add', '-A')
        git('commit', '-qm', 'seed')

        # A COMPLIANT change: the design doc AND its co-file move together, so the
        # gate has real work, finds no violation, and must say so.
        doc.write_text('# seed\nchanged\n', encoding='utf-8')
        cs.write_text('a: 2\n', encoding='utf-8')
        git('add', '-A')
        r = sp.run([sys.executable, GATE, '--staged'], cwd=td,
                   capture_output=True, text=True, timeout=300)

    assert r.returncode in (0, 1), f'gate crashed: {r.returncode}\n{r.stderr[-2000:]}'
    assert 'Skipping' not in r.stdout, (
        'the gate skipped a changeset that HAS changed files — its change detection '
        f'broke, which is the defect this test exists to catch.\n{r.stdout[-2000:]}')
    assert 'Co-file check' in r.stdout or 'CO-FILE VIOLATIONS' in r.stdout, r.stdout[-2000:]


def test_rule_1_actually_REJECTS_a_changeset_it_must_reject():
    """The assertion with real teeth — it EXECUTES the gate (ED-IN-0165).

    The first version of this test claimed in its docstring to "construct a
    changeset that Rule 1 must reject" and then grepped the gate's source for the
    string `violations.append`. Two independent adversarial passes caught it, and
    the objection is exact: Rule 4 was retired precisely because it contained
    `violations.append` and was UNREACHABLE. A source-grep is blind to the defect
    class this whole step exists to remove.

    So this builds a real git repo, stages a design-doc change WITHOUT its co-file,
    runs the gate in `--staged` mode, and requires a non-zero exit. If Rule 1's
    scope ever goes dead the way Rule 4's did, this fails.
    """
    import subprocess as sp
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        def git(*a):
            return sp.run(['git', *a], cwd=td, capture_output=True, text=True)
        git('init', '-q')
        git('config', 'user.email', 't@t')
        git('config', 'user.name', 't')
        # the gate reads paths relative to the repo it runs in
        doc = Path(td) / 'systems' / 'combat' / 'thing_v30.md'
        doc.parent.mkdir(parents=True)
        doc.write_text('# seed\n', encoding='utf-8')
        (Path(td) / 'references').mkdir()
        (Path(td) / 'references' / 'canonical_sources.yaml').write_text('a: 1\n', encoding='utf-8')
        git('add', '-A')
        git('commit', '-qm', 'seed')

        # change the design doc ONLY — Rule 1 must reject this
        doc.write_text('# seed\nchanged\n', encoding='utf-8')
        git('add', '-A')
        r = sp.run([sys.executable, GATE, '--staged'], cwd=td,
                   capture_output=True, text=True, timeout=300)
        assert r.returncode == 1, (
            'Rule 1 did NOT reject a design-doc change with no canonical_sources '
            f'co-change — its scope may have gone dead like Rule 4\'s.\n'
            f'rc={r.returncode}\n{r.stdout}\n{r.stderr}')
        assert 'canonical_sources' in r.stdout, r.stdout

        # ...and the CONTROL: add the co-file and it must pass. Without this the
        # test above could pass because the gate rejects everything.
        (Path(td) / 'references' / 'canonical_sources.yaml').write_text('a: 2\n', encoding='utf-8')
        git('add', '-A')
        r2 = sp.run([sys.executable, GATE, '--staged'], cwd=td,
                    capture_output=True, text=True, timeout=300)
        assert r2.returncode == 0, f'the co-changed case must pass\n{r2.stdout}\n{r2.stderr}'


def test_rule_1s_scope_has_no_dead_alternation():
    """Rule 4 went inert because its scope named an evacuated tree. Rule 1 carried
    the same latent defect — `(?:designs|systems)/` — for three weeks, in the file
    this programme edited, and the sweep read the line without seeing it.

    `designs/` was retired 2026-07-19 (CLAUDE.md §3, "do not recreate"), so the
    alternation was half-dead. This asserts no surviving rule scopes on a tree that
    is not in the repository.
    """
    import ast as _ast
    src = _src()
    # CODE ONLY. The first version scanned raw lines and flagged the gate's own
    # module docstring, where the retired rule is legitimately NAMED as retired —
    # a prose mention read as a live scope. Collect string literals and comparison
    # operands from the parsed tree instead, so only what the gate actually
    # MATCHES ON is examined.
    # Identify docstrings by NODE, not by value: ast.get_docstring() returns the
    # cleaned text while the raw Constant carries the original leading newline and
    # indentation, so a value-set comparison never matched and the module docstring
    # leaked through. (Third textual-proxy false positive in this branch; the
    # parser knows which node is a docstring, so ask it.)
    tree_ = _ast.parse(src)
    doc_nodes = set()
    for n in _ast.walk(tree_):
        if isinstance(n, (_ast.Module, _ast.FunctionDef, _ast.ClassDef)) and n.body:
            first = n.body[0]
            if isinstance(first, _ast.Expr) and isinstance(first.value, _ast.Constant) \
                    and isinstance(first.value.value, str):
                doc_nodes.add(id(first.value))
    literals = [n.value for n in _ast.walk(tree_)
                if isinstance(n, _ast.Constant) and isinstance(n.value, str)
                and id(n) not in doc_nodes]
    for tree in ('designs/', 'arcs/', 'engine/params/'):
        live = [x for x in literals if tree in x]
        assert not live, f'a rule still scopes on the retired tree {tree!r}: {live}'


def test_the_retirement_note_does_not_overclaim():
    """§0.1 point 3 applied to a tombstone.

    The first version of Rule 4's retirement note said six gates "now carry" its
    mechanism and were "strictly stronger". An adversarial pass refuted both: those
    gates run code->artifact, Rule 4 ran doc->doc, and all six PRE-EXISTED the
    retirement, so nothing was transferred. A tombstone that misstates why a gate
    was removed is how a removal gets re-litigated from the wrong premise.
    """
    note = _src()
    note = note[note.index('# ── Rule 4:'):note.index('if violations:')]
    # The phrase legitimately survives INSIDE the retraction that quotes it — the
    # same shape `test_compliance_on_exceed_vocabulary` already handles, where the
    # banned idiom appears once more in the owner's comment quoting the defect. So
    # require every occurrence to sit on a line that also marks it as retracted,
    # rather than banning the string outright.
    for i, ln in enumerate(note.splitlines(), 1):
        if 'strictly stronger' in ln:
            assert 'overreach' in ln or 'overclaim' in ln, (
                f'the overclaim is back at note line {i}: code->artifact gates are '
                f'not a stronger form of a doc->doc co-change rule, they are a '
                f'different mechanism — {ln.strip()}')
    assert 'overreached' in note, 'the correction itself was removed'
    assert 'EVACUATED' in note or 'evacuated' in note, (
        'the tombstone must state the actual reason — the subject left the tree')


@pytest.mark.parametrize('rule_subject', ['canonical_sources', 'propagation_map', 'coverage_matrix'])
def test_each_surviving_rules_subject_still_exists(rule_subject):
    """The vitality check #304's C4 generalises, applied to this gate now.

    Rule 4 went inert because its subject was evacuated and nothing noticed for a
    week. The same thing can happen to Rules 1-3. This is the cheap local version
    of the meta-guard plan step G5 owns.
    """
    matches = list(Path(ROOT).rglob(f'*{rule_subject}*'))
    matches = [m for m in matches
               if 'deprecated' not in m.parts and '__pycache__' not in m.parts]
    assert matches, (
        f"Rule's subject {rule_subject!r} matches nothing in the tree — this rule "
        f'has gone inert exactly as Rule 4 did')
