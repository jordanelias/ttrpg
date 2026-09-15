"""The ethical-axis set has ONE owner, and this fails if a second one appears.

WHY THIS GUARD EARNS ITS EXISTENCE (CLAUDE.md §0.1 pt 5, the load-bearing predicate). The artifact
it protects is game code: `engine/season/decision/choose.py` sums a candidate's score over this set
once per deliberation, and `engine/substrate/keys.py` invariant 6 rejects any Key naming an axis
outside it. Both were reading their own literal.

THE DEFECT IT CLOSES, MEASURED RATHER THAN FEARED (2026-09-14, ED-IN-0229). `keys.py::AXES` was a
tuple literal and `engine/season/rosters.yaml: conviction_axes` was a `values:` list, and NOTHING
compared them — while that roster's own note asserted that *"the engine substrate already
single-owns this tuple, so a fifth axis or a rename is one edit there and a loader refusal here
rather than two rosters drifting apart."* AST sweep of the whole tree: **exactly one module imports
`AXES`, and it is `engine/substrate/__init__.py` re-exporting it.** Nothing under `engine/season/`
read it. Both arms were run:

  * a fifth axis in `keys.py` alone -> the season engine goes on scoring over four, in silence;
  * a fifth axis in the roster alone -> the season engine scores over five while `keys.py`
    invariant 6 rejects every Key that names it.

Two failures in opposite directions, neither side able to observe the other. That is §0.1 pt 5's
signature exactly — each literal was correct when written and stopped being correct because the
other changed — and it is the same defect, one level up, that put the 13 Convictions in the
registry in 2026-08-24 after nine-vs-eight-vs-thirteen silently disabled a ratified mechanic.

So: one owner (`references/descriptor_registry.yaml: axis_roster`), one exporter
(`tools/export_descriptors.py`), one leaf reader (`engine.substrate.descriptors`), every consumer
reads the leaf — and this fails on recurrence.

A NOTE ASSERTING A GUARD THAT IS NOT THERE IS WORSE THAN NO NOTE, because it is trusted. That is
what `test_the_roster_row_points_at_the_owner_and_carries_no_literal` is for: it fails if the
`values:` list comes back, which is how the false claim would return.
"""
import ast
import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: The one module allowed to name the axes, and even there they are read from the artifact.
_OWNER = os.path.join('engine', 'substrate', 'descriptors.py')


def _canonical():
    from engine.substrate import descriptors
    return set(descriptors.AXES)


def _py_files():
    for tree in ('engine', 'systems'):
        for dirpath, dirnames, filenames in os.walk(os.path.join(_ROOT, tree)):
            dirnames[:] = [d for d in dirnames if d != '__pycache__']
            for fn in filenames:
                if fn.endswith('.py'):
                    yield os.path.join(dirpath, fn)


def test_both_readers_resolve_to_the_same_object():
    """`is`, not `==`. Equal-but-separate is exactly the state this guard exists to end."""
    from engine.substrate import descriptors, keys
    from engine.season.data import rosters
    assert keys.AXES is descriptors.AXES, (
        'engine/substrate/keys.py::AXES is no longer the registry object. It was a literal until '
        '2026-09-14 and a second literal is how the two axis lists drifted — read '
        'engine.substrate.descriptors.AXES, do not retype it')
    assert set(rosters.CONVICTION_AXES) == set(descriptors.AXES), (
        f'the season engine scores over {sorted(rosters.CONVICTION_AXES)} while the Key substrate '
        f'validates against {sorted(descriptors.AXES)}. A Key naming an axis only one side knows '
        'is rejected by keys.py invariant 6 while choose.py has already scored on it')
    assert len(descriptors.AXES) == 4, (
        f'{len(descriptors.AXES)} axes. key_substrate_v30.md §2.4 permits a 5th as a Class B '
        'extension "if Stage 10 calibration finds the simplification load-bearing; treat as '
        'deferred unless required" — if that ruling has been taken, update this line WITH its '
        'citation rather than loosening it')


def test_the_roster_row_points_at_the_owner_and_carries_no_literal():
    """The `values:` list must not come back — that IS the second roster, in YAML."""
    from engine.season.data.rosters import _ROSTERS
    row = _ROSTERS.get('conviction_axes') or {}
    assert 'values' not in row, (
        'engine/season/rosters.yaml: conviction_axes has a `values:` list again. That is the '
        'second axis roster restored, in the file the Python-scanning guard below does not read. '
        'Use `from_descriptor: axis_roster`')
    assert row.get('from_descriptor') == 'axis_roster', (
        'conviction_axes must point at `axis_roster` in the descriptor registry')
    # And the pointer is load-bearing rather than decorative: the `forbidden:` bar still fires.
    assert 'exposure' in (row.get('forbidden') or []), (
        "conviction_axes' `forbidden: [exposure]` bar is gone. #353 `:1897` names the Exposure "
        'collision — three senses of one word — and routing through `roster()` rather than '
        'importing AXES directly is what keeps that data-side bar alive')


def test_no_second_axis_roster_in_code():
    """A literal holding 2+ canonical axis names is a re-hardcoded roster.

    Dict literals are inspected on BOTH halves, for the reason the Conviction guard records: a
    mapping keyed on axis names is a roster fragment that can mint a name the validator raises on.
    """
    canon = _canonical()
    offenders = []
    for path in _py_files():
        rel = os.path.relpath(path, _ROOT)
        if rel == _OWNER:
            continue
        try:
            tree = ast.parse(open(path, encoding='utf-8').read())
        except SyntaxError:                                  # pragma: no cover - not our problem
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Dict):
                elts = [e for e in list(node.keys) + list(node.values) if e is not None]
            elif isinstance(node, (ast.Tuple, ast.List, ast.Set)):
                elts = node.elts
            else:
                continue
            names = {e.value for e in elts
                     if isinstance(e, ast.Constant) and isinstance(e.value, str)}
            hits = names & canon
            if len(hits) >= 2:
                offenders.append(f'{rel}:{node.lineno} -> {sorted(hits)}')
    assert not offenders, (
        'a second ethical-axis roster has been hardcoded. The set is owned by '
        'references/descriptor_registry.yaml:axis_roster and read via '
        'engine.substrate.descriptors.AXES — read it, do not retype it:\n  '
        + '\n  '.join(offenders)
    )
