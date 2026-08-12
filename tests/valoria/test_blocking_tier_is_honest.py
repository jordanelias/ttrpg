"""A tool in the blocking job must be capable of failing, and the ghost hook tier must stay dead.

WHY (G3, ED-IN-0159 §1.9/§1.10, executed 2026-08-12).

`ci_supersession_check.py` documents "ALWAYS return 0 (WARN-ONLY)" at :66 and every return in
its `main()` is 0. `ci_audit_registry_check.py`'s own registry row says "Always exits 0 by
design". Both sat in `validators`, the BLOCKING job. Neither could ever have failed a build.

That is not a harmless mislabel. `validators` is the job whose membership answers "what blocks a
merge", and two of its nineteen entries answered it falsely — while `valoria_local.py:162,172`
had them right as report-only the whole time, so the two tiers disagreed and the stricter-looking
one was the wrong one. The cost is paid by a reader who trusts the list.

THE GUARD IS THE POINT, NOT THE MOVE. Moving two tools is a one-off; §0.1 point 5 asks for the
thing that fails on recurrence. `test_no_blocking_validator_is_incapable_of_failing` is it: add a
third always-exit-0 tool to the blocking job and this reds. It needs no allowlist, because when
it was written the invariant held with zero exceptions — 17 of 17 blocking tools can fail, and
all six that cannot are in `validators-report`.

AND THE GHOST TIER. `valoria_hooks.py` — the whole "level 4, in-session hook with RuntimeError"
rung — lived only at `deprecated/skills/valoria-orchestrator/scripts/` and went with the
2026-08-05 evacuation (`cadf9c7`). It left ~90 lines of registry describing it as live, six
`paired_hook:` values naming functions in it, and a check (d) in a BLOCKING gate that walked the
entire repo on every run to discover the file was absent and then reported that as an error.
Deleted, under the rule ED-IN-0163 had to state for the opposite case: an absent path is dead
only if its SUBJECT was retired, never merely because it is absent. Here the subject was retired
on purpose.
"""
import ast
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REGISTRY = os.path.join(ROOT, 'references', 'ci_checks_registry.yaml')
sys.path.insert(0, os.path.join(ROOT, 'tools'))

pytest.importorskip('yaml')
import yaml  # noqa: E402


def _jobs():
    import ci_gate_coverage
    return ci_gate_coverage.jobs()


def _can_fail(path: str) -> bool:
    """Is there any code path by which this module exits non-zero?

    Deliberately GENEROUS — it says yes on the mere presence of a non-zero return or exit
    anywhere in the module, without proving reachability. A generous detector makes the
    assertion below hard to trip, so when it DOES trip the finding is real. The failure mode
    it cannot see is a tool that gates by letting an exception escape; that is itself worth
    finding, and the assertion message says so rather than pretending otherwise.
    """
    tree = ast.parse(open(path, encoding='utf-8').read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Constant):
            if node.value.value not in (0, None, False):
                return True
        # sys.exit(N) / exit(N) / raise SystemExit(N)
        target = None
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr == 'exit':
                target = node
            elif isinstance(f, ast.Name) and f.id in ('exit', 'SystemExit'):
                target = node
        if target is not None and target.args:
            a = target.args[0]
            if not isinstance(a, ast.Constant):
                continue          # sys.exit(main()) — value comes from main's returns
            if a.value not in (0, None, False):
                return True
    return False


# --------------------------------------------------------------------------------------
# §1.9 — the blocking tier tells the truth about itself
# --------------------------------------------------------------------------------------
def test_no_blocking_validator_is_incapable_of_failing():
    """THE RECURRENCE GUARD. A tool that cannot exit non-zero cannot gate anything."""
    offenders = []
    for job in _jobs():
        if not job.get('blocking') or job['id'] == 'syntax-check':
            continue
        for cmd in job.get('tool_commands') or []:
            path = os.path.join(ROOT, cmd['script'])
            if not os.path.exists(path) or not path.endswith('.py'):
                continue
            if not _can_fail(path):
                offenders.append(f"{cmd['script']} (in blocking job {job['id']})")
    assert not offenders, (
        'these tools sit in a BLOCKING CI job but have no non-zero exit anywhere in them, so '
        'they can never fail a build and their presence misreports what gates a merge:\n  '
        + '\n  '.join(sorted(offenders))
        + '\n\nMove them to `validators-report` AND flip their `ci_job:` row in '
          'references/ci_checks_registry.yaml in the SAME commit (broken_dependency_checker '
          'joins the two and reds if they disagree). If one of them really does gate by '
          'raising an uncaught exception, that is the finding — give it an explicit exit code.')


def _local_blocking_flags() -> dict:
    """{script basename: blocking bool} read out of valoria_local's `checks` table.

    AST, not a line match. The first version of this asserted the source line ENDED in
    `False),` and was defeated by a trailing `# comment` — a proxy for the property instead
    of the property, which is the ED-IN-0165 `severity=severity` lesson repeated. A parser
    can tell a tuple element from a comment; indentation and punctuation cannot.
    """
    tree = ast.parse(open(os.path.join(ROOT, 'tools', 'valoria_local.py'), encoding='utf-8').read())
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Assign) and isinstance(node.value, ast.List)):
            continue
        if not any(getattr(t, 'id', None) == 'checks' for t in node.targets):
            continue
        out = {}
        for elt in node.value.elts:
            if isinstance(elt, ast.Tuple) and len(elt.elts) == 3 \
                    and isinstance(elt.elts[0], ast.Constant) \
                    and isinstance(elt.elts[2], ast.Constant):
                out[elt.elts[0].value] = elt.elts[2].value
        return out
    raise AssertionError('valoria_local.py no longer defines a `checks = [...]` table')


def test_the_two_moved_tools_are_report_only_in_both_tiers():
    """CI and `valoria_local` disagreed about these two for months; pin the agreement."""
    local = _local_blocking_flags()
    assert len(local) > 10, f'the checks table parsed to only {len(local)} rows — parser is wrong'
    registry = yaml.safe_load(open(REGISTRY, encoding='utf-8'))
    rows = {e['path']: e for e in registry['ci_checks']}
    for tool in ('tools/ci_supersession_check.py', 'tools/ci_audit_registry_check.py'):
        assert rows[tool]['ci_job'] == 'validators-report', \
            f'{tool} claims ci_job {rows[tool]["ci_job"]!r}; it cannot fail, so it cannot block'
        base = os.path.basename(tool)
        assert local[base] is False, \
            f'{base} is blocking in valoria_local.py but cannot fail — the tiers disagree again'


# --------------------------------------------------------------------------------------
# §1.10 — the ghost hook tier stays dead
# --------------------------------------------------------------------------------------
def test_the_registry_declares_no_in_session_hook_apparatus():
    registry = yaml.safe_load(open(REGISTRY, encoding='utf-8'))
    assert 'in_session_hooks' not in registry, (
        'the in_session_hooks section is back. It described 19 hooks in valoria_hooks.py, a '
        'file removed by the 2026-08-05 evacuation. Nothing reads this section.')
    assert not any(e.get('paired_hook') for e in registry['ci_checks']), \
        'a paired_hook: value is back; it names a function in an evacuated file'
    assert not any(e.get('level') == 4 for e in registry['ci_checks']), \
        'level 4 is the retired in-session hook rung — see this file\'s header'


def test_valoria_hooks_is_only_ever_mentioned_as_history():
    """Provenance is fine ("Ports valoria_hooks.vetting_gate"); a live claim is not.

    The distinction is the whole of §1.10: the registry may record where a tool CAME from,
    but must not describe the hook tier as a present-tense enforcement mechanism.
    """
    text = open(REGISTRY, encoding='utf-8').read()
    for i, line in enumerate(text.splitlines(), 1):
        if 'valoria_hooks' not in line:
            continue
        historical = ('Ports valoria_hooks' in line          # provenance on a notes: field
                      or 'RETIRED' in text.split(line)[0][-400:]  # inside the tombstone block
                      or line.lstrip().startswith('#'))       # a comment, i.e. the tombstone
        assert historical, f'{REGISTRY}:{i} states a live valoria_hooks mechanism: {line.strip()}'


def test_the_dead_paired_hook_check_is_gone_from_the_blocking_gate():
    """Check (d) walked the WHOLE repo on every run of a blocking gate to find a deleted file."""
    src = open(os.path.join(ROOT, 'tools', 'broken_dependency_checker.py'),
               encoding='utf-8').read()
    tree = ast.parse(src)
    fns = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    assert '_find_valoria_hooks_path' not in fns, \
        'the repo-wide os.walk for an evacuated file is back in a blocking gate'
    assert "'paired_hook'" not in src and '"paired_hook"' not in src, \
        'broken_dependency_checker reads paired_hook again; the field no longer exists'
