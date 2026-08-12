"""Being COMPILED is not being INVOKED — the orphan census must be able to see a dead tool.

WHY (G9, ED-IN-0159 §2.2, executed 2026-08-12).

`build_apparatus_registry.invoked_by()` tags a tool `ci:<workflow>` when its basename appears
anywhere in the workflow text, and `valoria-ci.yml`'s syntax-check job was a hand-maintained
`py_compile` list. So four tools — `atomizer`, `doc_index_gen`, `index_gen`, `valoria_rename` —
read as "Invoked by ci:valoria-ci.yml" while the registry's OWN row for that workflow listed none
of them. Orphans were undercounted and cull candidates hidden by the instrument that exists to
surface them. Measured here: 7 orphans before, 11 after, +4 exactly as predicted.

THE TWO HALVES SHIP TOGETHER OR THE CENSUS ZEROES. The other half of G9 globbed the compile
list, which covered 32 of 108 tools. The obvious alternative fix — name all 108 — would have
taken basename-in-workflow to 108/108 and driven the orphan count to a permanent silent zero.
`test_naming_every_tool_in_the_compile_gate_does_not_zero_the_census` is that scenario, run.

AND THE STRIP MUST NOT OVER-REACH. The first implementation was one multiline regex and it
swallowed the entire `validators-report` job, because that job's `run:` mentions `py_compile`
inside a comment. Two live validators were reported orphaned on that run. It is the trap
`test_gate_coverage.py::test_a_comment_mentioning_py_compile_does_not_zero_a_jobs_command_list`
already names, reproduced one file away from it — so the over-reach direction is tested here at
least as hard as the under-reach one.
"""
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WORKFLOW = os.path.join(ROOT, '.github', 'workflows', 'valoria-ci.yml')
sys.path.insert(0, os.path.join(ROOT, 'tools'))

pytest.importorskip('yaml')
import yaml  # noqa: E402
import build_apparatus_registry as bar  # noqa: E402


@pytest.fixture(scope='module')
def workflow_text():
    return open(WORKFLOW, encoding='utf-8').read()


@pytest.fixture(scope='module')
def registry():
    """A FRESH build, not the committed artifact.

    `references/apparatus_registry.yaml` is deliberately a single-writer, scheduled-wave
    artifact (ED-IN-0097) whose currency is `tools/audit_staleness.py`'s job, not a gate's —
    so asserting the committed file is current would contradict that convention and red on
    anyone who adds a tool. Building here tests the INSTRUMENT, which is what G9 changed, and
    cannot be fooled by a stale file either way.
    """
    return bar.build()


# ------------------------------------------------------------------------------------
# The census can see a dead tool — G9's required assertion
# ------------------------------------------------------------------------------------
@pytest.mark.slow
def test_a_known_dead_tool_still_reports_orphaned(registry):
    """`index_gen`/`doc_index_gen`/`atomizer` are dead (plan G2 retires them; its landing
    site is what is blocked, not its finding). If the census cannot see THEM it cannot see
    anything, because they are the four the compile list was hiding."""
    orphans = set(registry.get('orphaned_no_cli') or [])
    for dead in ('tools/index_gen.py', 'tools/doc_index_gen.py', 'tools/atomizer.py',
                 'tools/valoria_rename.py'):
        assert dead in orphans, (
            f'{dead} has no importer and no invoker but is not reported orphaned. '
            'If the compile gate started naming tools again, that is the cause.')


def test_the_compile_gate_names_no_individual_tool(workflow_text):
    """The recurrence guard on the workflow side. A named list is what rotted (32 of 108)
    and what would zero the census if it were completed."""
    kept = set(bar.strip_compile_only_steps(workflow_text).splitlines())
    compile_step = [ln for ln in workflow_text.splitlines() if ln not in kept]
    assert any('py_compile' in ln for ln in compile_step), \
        'no compile step was identified, so this test is asserting over nothing'
    named = [ln for ln in compile_step if ln.strip().startswith('tools/')]
    assert not named, (
        'the compile gate names individual tools again:\n  ' + '\n  '.join(named)
        + '\nUse the glob. A named list covers a subset that rots, and completing it '
          'silently zeroes the orphan census.')


def test_naming_every_tool_in_the_compile_gate_does_not_zero_the_census(workflow_text):
    """THE SCENARIO THE TWO HALVES EXIST TO SURVIVE, actually executed.

    Simulate someone 'fixing' the 32-of-108 coverage gap the obvious way. Without the strip
    this tags every tool as CI-invoked; with it, nothing changes.
    """
    import glob
    import re
    names = sorted(os.path.basename(p) for p in
                   glob.glob(os.path.join(ROOT, 'tools', '**', '*.py'), recursive=True))
    assert len(names) > 100, f'expected ~108 tools, found {len(names)}'
    hypothetical = workflow_text.replace(
        '          python -m py_compile $files',
        '          python -m py_compile \\\n'
        + ' \\\n'.join(f'            tools/{n}' for n in names))

    raw_hits = [n for n in names if re.search(rf'\b{re.escape(n)}\b', hypothetical)]
    assert len(raw_hits) == len(names), \
        'the simulation did not actually inject the names; the test proves nothing'

    stripped = bar.strip_compile_only_steps(hypothetical)
    surviving = [n for n in ('atomizer.py', 'doc_index_gen.py', 'index_gen.py',
                             'valoria_rename.py')
                 if re.search(rf'\b{re.escape(n)}\b', stripped)]
    assert not surviving, (
        f'naming all {len(names)} tools in the compile gate re-tagged {surviving} as '
        'CI-invoked. The strip is not covering the compile step.')


# ------------------------------------------------------------------------------------
# The strip must not over-reach — the direction that produced a false finding
# ------------------------------------------------------------------------------------
def test_the_strip_removes_only_the_compile_step(workflow_text):
    """AN INDEX-ACCURATE DIFF, not set membership.

    The first version computed `[ln for ln in original if ln not in set(stripped)]`, which
    UNDERCOUNTS: `        run: |` is removed with the compile step but appears verbatim in
    five other steps, so it tested as "kept" and the removal read as 5 lines instead of 7.
    An over-reach test that undercounts removals is weaker than it looks — the §0.1 point 2
    shape, in the test written to catch an over-reach.
    """
    import difflib
    stripped = bar.strip_compile_only_steps(workflow_text)
    removed = [ln[1:] for ln in difflib.unified_diff(
        workflow_text.splitlines(), stripped.splitlines(), lineterm='', n=0)
        if ln.startswith('-') and not ln.startswith('---')]
    assert any('py_compile' in ln for ln in removed), 'the compile step was not removed at all'
    assert len(removed) <= 10, (
        f'the strip removed {len(removed)} lines; the compile step is 7 including its blank '
        'separator. It is eating neighbouring content:\n  ' + '\n  '.join(removed[:25]))


def test_a_step_that_compiles_AND_invokes_is_not_stripped():
    """`_INVOKES` is the guard that keeps a mixed step. Without it, a job that compiled and
    then ran validators would have its validators erased from the invocation index."""
    wf = (
        'jobs:\n'
        '  mixed:\n'
        '    steps:\n'
        '      - name: compile then run\n'
        '        run: |\n'
        '          python -m py_compile tools/foo.py\n'
        '          python3 tools/ci_naming_check.py\n'
    )
    out = bar.strip_compile_only_steps(wf)
    assert 'ci_naming_check.py' in out, 'a real invocation was stripped as if it were a compile'


def test_an_UNNAMED_compile_step_is_still_stripped():
    """Found by attacking this function, not by a test failing.

    SIX steps in valoria-ci.yml carry `run:` with no `name:`. The scanner originally keyed
    step starts on `- name:` alone, so it was correct only because none of those six happens
    to be a compile step — an unnamed one would have slipped past the guard entirely and
    restored the undercount by a side door.
    """
    wf = (
        'jobs:\n'
        '  j:\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - run: python -m py_compile tools/atomizer.py\n'
        '      - name: real\n'
        '        run: python3 tools/ci_naming_check.py\n'
    )
    out = bar.strip_compile_only_steps(wf)
    assert 'atomizer.py' not in out, 'an UNNAMED compile step was not stripped'
    assert 'ci_naming_check.py' in out, 'the neighbouring real invocation was eaten'


def test_a_comment_mentioning_py_compile_does_not_strip_the_step():
    """THE INCIDENT. The report-only job's run block says 'only py_compile on it' in a
    comment; the first implementation deleted the whole job and orphaned two live validators."""
    wf = (
        'jobs:\n'
        '  report:\n'
        '    steps:\n'
        '      - name: Every report-only validator\n'
        '        run: |\n'
        '          # nothing runs valoria_local (only py_compile on it)\n'
        '          w python3 tools/mechanics_index_gen.py --strict\n'
        '          w python3 tools/ci_workplan_pointer_check.py\n'
    )
    out = bar.strip_compile_only_steps(wf)
    for tool in ('mechanics_index_gen.py', 'ci_workplan_pointer_check.py'):
        assert tool in out, f'{tool} was stripped because a COMMENT mentioned py_compile'


@pytest.mark.slow
def test_live_validators_are_not_orphaned(registry):
    """The false-positive control on the real tree, in registry terms rather than text."""
    orphans = set(registry.get('orphaned_no_cli') or [])
    for live in ('tools/mechanics_index_gen.py', 'tools/ci_workplan_pointer_check.py',
                 'tools/ci_naming_check.py', 'tools/canon_coverage_check.py'):
        assert live not in orphans, \
            f'{live} is invoked by a CI job but reports orphaned — the strip is over-reaching'

