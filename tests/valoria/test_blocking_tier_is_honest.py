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
    """Can this module's PROCESS EXIT be non-zero? Analysed along the exit path only.

    REWRITTEN 2026-08-12 (ED-IN-0169) BECAUSE THE FIRST VERSION WAS HOLLOW. It walked the
    WHOLE module and returned True on any non-zero `Return` constant anywhere — so a helper
    like `def _is_thing(x): return True`, which is ordinary in any codebase, made a tool read
    as "can fail" regardless of its actual exit. Demonstrated, not theorised: appending one
    such helper to `ci_supersession_check.py` — a tool whose own line 66 says "ALWAYS return 0
    (WARN-ONLY)" — flipped it from CANNOT to CAN. The guard would then have passed the very
    tool it was written to catch.

    It gave the right answer for all 17 blocking tools ONLY BY LUCK: neither
    `ci_supersession_check` nor `ci_audit_registry_check` happens to contain `return True` or
    `return False`. And it was right about `validate_ed_citations` for the WRONG REASON — it
    matched a `return True` predicate at :206 while SKIPPING the real exit at :569,
    `sys.exit(1 if errors or over else 0)`, whose argument is an IfExp rather than a Constant.

    That is CLAUDE.md §0.1 point 2 — an assertion that cannot observe the failure it excludes
    — inside the guard written to prevent a recurrence, and the third instance of the class in
    three commits (ED-IN-0165's `owner_src.split` guard was the second).

    THE ANALYSIS NOW FOLLOWS THE EXIT PATH: find the `if __name__ == '__main__':` block, take
    every `sys.exit(...)` / `exit(...)` / `raise SystemExit(...)` in it, and resolve each
    argument — a non-zero constant is a failure path; a call to a local function means
    inspecting THAT function's returns (one level); anything non-constant (`IfExp`, a
    comparison, a computed count) is treated as capable, because it can evaluate non-zero.
    Returns in unrelated helpers are now invisible, which is the whole point.
    """
    tree = ast.parse(open(path, encoding='utf-8').read())
    funcs = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}

    def _nonzero_constant(node) -> bool:
        return isinstance(node, ast.Constant) and node.value not in (0, None, False)

    def _returns_can_be_nonzero(fn) -> bool:
        """Any return in `fn` that is non-zero, or that is not a constant at all."""
        for n in ast.walk(fn):
            if not isinstance(n, ast.Return) or n.value is None:
                continue
            if not isinstance(n.value, ast.Constant):
                return True           # computed — len(errors), 1 if x else 0, ...
            if _nonzero_constant(n.value):
                return True
        return False

    def _exit_value_can_be_nonzero(arg) -> bool:
        if arg is None:
            return False
        if isinstance(arg, ast.Constant):
            return _nonzero_constant(arg)
        if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) \
                and arg.func.id in funcs:
            return _returns_can_be_nonzero(funcs[arg.func.id])
        return True                   # IfExp / Compare / computed — capable

    def _scan(body, seen, depth=0) -> bool:
        """Any reachable non-zero exit from these statements, following local calls.

        THE ENTRY POINT IS NOT THE ONLY PLACE THE EXIT LIVES. Measured across the 17 blocking
        tools, three shapes are in use and an analyser that knows only one is wrong about the
        other two:
          A  `if __name__ == '__main__': main()`, with `sys.exit(...)` INSIDE main
             (ci_register_size_check, validate_ed_citations, broken_dependency_checker)
          B  no `__main__` guard at all — module-level `sys.exit(1)` / `sys.exit(0)`
             (ci_hooks_verifier, ci_co_file_checker, ci_editorial_checker)
          C  `sys.exit(main())`, with the code in main's return values (ci_naming_check, ...)
        A first cut of this rewrite handled only C and reported four live gates as unable to
        fail, which would have red-flagged them as offenders. Following calls fixes it.
        """
        if depth > 3:
            return False
        for stmt in body:
            for node in ast.walk(stmt):
                if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call) \
                        and isinstance(node.exc.func, ast.Name) \
                        and node.exc.func.id == 'SystemExit':
                    if _exit_value_can_be_nonzero(
                            node.exc.args[0] if node.exc.args else None):
                        return True
                if not isinstance(node, ast.Call):
                    continue
                f = node.func
                if (isinstance(f, ast.Attribute) and f.attr == 'exit') or \
                        (isinstance(f, ast.Name) and f.id == 'exit'):
                    if _exit_value_can_be_nonzero(node.args[0] if node.args else None):
                        return True
                # follow a call into a local function
                name = f.id if isinstance(f, ast.Name) else None
                if name and name in funcs and name not in seen:
                    seen.add(name)
                    if _scan(funcs[name].body, seen, depth + 1):
                        return True
        return False

    main_blocks = [n for n in tree.body if isinstance(n, ast.If) and _is_main_guard(n)]
    if main_blocks:
        entry = [s for b in main_blocks for s in b.body]
    else:
        # Shape B: no guard, the module body IS the entry. Function/class definitions are
        # skipped — defining a function is not running it; only an explicit call reaches it.
        entry = [s for s in tree.body
                 if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
        if not entry:
            return None
    return _scan(entry, set())


def _is_main_guard(node: ast.If) -> bool:
    """BOTH operand orders, because `ci_common.has_main_guard` — the ONE OWNER of this
    predicate (OI-52a, ED-IN-0097) — documents that it exists precisely because an earlier
    local copy "only matched the conventional operand order". The first version of this
    function reproduced that exact defect, in a file arguing for single ownership.

    The owner answers "does this tree have a guard", not "which node is it", so it cannot be
    called directly here. `test_main_guard_matcher_agrees_with_the_owner` pins the two
    together instead, so they cannot drift.
    """
    t = node.test
    if not isinstance(t, ast.Compare):
        return False
    operands = [t.left] + list(t.comparators)
    names = {o.id for o in operands if isinstance(o, ast.Name)}
    consts = {o.value for o in operands if isinstance(o, ast.Constant)}
    return '__name__' in names and '__main__' in consts


# --------------------------------------------------------------------------------------
# §1.9 — the blocking tier tells the truth about itself
# --------------------------------------------------------------------------------------
def test_no_blocking_validator_is_incapable_of_failing():
    """THE RECURRENCE GUARD. A tool that cannot exit non-zero cannot gate anything."""
    offenders, unjudgeable, checked = [], [], 0
    for job in _jobs():
        if not job.get('blocking'):
            continue
        for cmd in job.get('tool_commands') or []:
            path = os.path.join(ROOT, cmd['script'])
            if not os.path.exists(path) or not path.endswith('.py'):
                continue
            checked += 1
            verdict = _can_fail(path)
            if verdict is None:
                unjudgeable.append(f"{cmd['script']} (in {job['id']}): no __main__ guard")
            elif verdict is False:
                offenders.append(f"{cmd['script']} (in blocking job {job['id']})")

    # A LOOP THAT ASSERTS CONDITIONALLY MUST ASSERT THAT IT ASSERTED (§0.1 point 2).
    # `ci_gate_coverage.jobs()` returns [] if the workflow is absent, and its JOB_RE only
    # matches lowercase-hyphen job ids — rename a job with an underscore and it drops out
    # silently. Either way both lists below stay empty and this guard reports green over
    # nothing. Its sibling test_gate_coverage.py:151 already carries this assertion.
    assert checked >= 17, (
        f'only {checked} blocking tool invocations were examined; the workflow parse has '
        'collapsed and this guard is reporting green over nothing')

    # AN UNJUDGEABLE TOOL MUST REACH A HUMAN, not be silently counted as fine. The first
    # version of this test had no such bucket, so any shape the analyser could not read
    # would have passed as "can fail".
    assert not unjudgeable, (
        'these blocking tools have no `if __name__ == "__main__":` entry point, so whether '
        'they can fail cannot be determined by reading them:\n  ' + '\n  '.join(unjudgeable)
        + '\nGive them one, or teach _can_fail the shape deliberately.')
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


def test_an_ordinary_boolean_helper_does_not_fake_a_failure_path(tmp_path):
    """THE MUTATION THAT DEFEATED THE FIRST VERSION OF `_can_fail` (ED-IN-0169).

    That version walked the WHOLE module and returned True on any non-zero `Return` constant,
    so appending `def _t(x): return True` — ordinary in any codebase — to a tool documented
    "ALWAYS return 0 (WARN-ONLY)" flipped it to "can fail". The guard would then have waved
    through the exact tool it exists to catch. It was right about all 17 tools only because
    neither always-exit-0 tool happened to contain a boolean helper.

    Both directions are pinned: the decoys must not flip it, and a REAL added exit must.
    """
    base = open(os.path.join(ROOT, 'tools', 'ci_supersession_check.py'), encoding='utf-8').read()
    assert _can_fail(os.path.join(ROOT, 'tools', 'ci_supersession_check.py')) is False, \
        'the control tool is no longer always-exit-0; pick another'

    for label, decoy in (
            ('boolean helper', '\ndef _t(x):\n    if x:\n        return True\n    return False\n'),
            ('non-zero helper', '\ndef _n():\n    return 7\n'),
            ('uncalled exiting fn', '\ndef _never():\n    sys.exit(3)\n')):
        p = tmp_path / f'decoy_{label.split()[0]}.py'
        p.write_text(base + decoy, encoding='utf-8')
        assert _can_fail(str(p)) is False, \
            f'a {label} made an always-exit-0 tool read as able to fail — the guard is hollow'

    real = tmp_path / 'real.py'
    real.write_text(base.replace("if __name__ == '__main__':\n    sys.exit(main(sys.argv[1:]))",
                                 "if __name__ == '__main__':\n    sys.exit(1)"), encoding='utf-8')
    assert _can_fail(str(real)) is True, \
        'adding a genuine non-zero exit did not register — the detector now under-reports'


def test_main_guard_matcher_agrees_with_the_owner():
    """`ci_common.has_main_guard` is the ONE OWNER; this file needs the node, not the bool.
    Pin them together over the real blocking tools so the local matcher cannot drift from it."""
    import ci_common
    for job in _jobs():
        if not job.get('blocking'):
            continue
        for cmd in job.get('tool_commands') or []:
            path = os.path.join(ROOT, cmd['script'])
            if not os.path.exists(path) or not path.endswith('.py'):
                continue
            tree = ast.parse(open(path, encoding='utf-8').read())
            mine = any(isinstance(n, ast.If) and _is_main_guard(n) for n in tree.body)
            assert mine == ci_common.has_main_guard(tree), \
                f'{cmd["script"]}: local guard matcher disagrees with ci_common.has_main_guard'


def test_all_three_entry_shapes_are_understood():
    """`_can_fail` must handle every entry shape the blocking tier actually uses.

    A first cut of the rewrite understood only `sys.exit(main())` and reported four live
    gates as unable to fail. One representative of each measured shape is pinned here so a
    future simplification cannot quietly drop one.
    """
    shapes = {
        'tools/ci_register_size_check.py': 'A: __main__ calls main(), sys.exit inside main',
        'tools/ci_hooks_verifier.py': 'B: no __main__ guard, module-level sys.exit',
        'tools/ci_naming_check.py': 'C: sys.exit(main())',
        'tools/validate_ed_citations.py': 'A + computed code: sys.exit(1 if errors else 0)',
    }
    for rel, shape in shapes.items():
        assert _can_fail(os.path.join(ROOT, rel)) is True, \
            f'{rel} ({shape}) reads as unable to fail; the analyser lost this shape'


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
