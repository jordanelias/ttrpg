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

THE STRIP THIS FILE ONCE TESTED IS GONE (ED-IN-0169). G9 originally shipped a 54-line
indentation-aware line scanner in `build_apparatus_registry.py` to decide which workflow steps
only compile. `tools/ci_gate_coverage.py:63` states it is the SINGLE OWNER of workflow parsing —
"the only function in the tree that reads .github/workflows/valoria-ci.yml structurally… a
second list would be a second owner of the same rule… the exact §8 violation this repo keeps
finding" — and it already exposed `compiles_only` per job, computed over comment-stripped text.

The scanner therefore re-derived a rule that had an owner, AND re-derived its bug: its first cut
classified a job as compile-only because a COMMENT in its `run:` mentioned `py_compile`, falsely
orphaning two live validators. `ci_gate_coverage` had hit that exact defect and fixed it on
2026-08-01, and says so in its own comment. The registry now delegates; the orphan/prune figures
are unchanged at 11/2, which is the delta-none proof that the owner and the copy agreed.

Five tests were deleted with it — they existed only to test the re-implementation. What remains
is the guard that is actually about G9's subject: the compile gate must not name tools.
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
    import ci_gate_coverage
    compile_jobs = [j for j in ci_gate_coverage.jobs() if j.get('compiles_only')]
    assert compile_jobs, 'no compile-only job found, so this test asserts over nothing'
    named = [ln for j in compile_jobs for ln in j['runnable'].splitlines()
             if ln.strip().startswith('tools/')]
    assert not named, (
        'the compile gate names individual tools again:\n  ' + '\n  '.join(named)
        + '\nUse the glob. A named list covers a subset that rots, and completing it '
          'silently zeroes the orphan census.')







@pytest.mark.slow
def test_live_validators_are_not_orphaned(registry):
    """The false-positive control on the real tree, in registry terms rather than text."""
    orphans = set(registry.get('orphaned_no_cli') or [])
    for live in ('tools/mechanics_index_gen.py', 'tools/ci_workplan_pointer_check.py',
                 'tools/ci_naming_check.py', 'tools/canon_coverage_check.py'):
        assert live not in orphans, \
            f'{live} is invoked by a CI job but reports orphaned — the strip is over-reaching'

