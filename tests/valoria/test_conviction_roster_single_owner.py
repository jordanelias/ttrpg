"""The Conviction roster has ONE owner, and this fails if a second one appears.

WHY THIS GUARD EARNS ITS EXISTENCE (CLAUDE.md §0.1 pt 5, the load-bearing predicate). The artifact
it protects is game code, and the defect it caught was not hypothetical: three incompatible rosters
shipped simultaneously — nine names in `systems/characters/sim/conviction.py`, eight in
`systems/world/sim/npe.py`, thirteen registered in `references/descriptor_registry.yaml` — and the
disagreement silently disabled ED-912 §6.1's Close-Knot-break Conviction Scar for as long as both
modules existed. That is the signature §0.1 pt 5 describes: each roster was correct when written and
stopped being correct because the other changed.

So: one owner (`references/descriptor_registry.yaml:conviction_roster`), one exporter
(`tools/export_descriptors.py`), one leaf reader (`engine.substrate.descriptors`), every consumer
reads the leaf — and this fails on recurrence.

THE FALSIFIER for the guard itself: re-hardcode any two canonical Conviction names in a tuple or
list literal anywhere under `engine/` or `systems/` and `test_no_second_conviction_roster_in_code`
fails. Mutation-verified 2026-08-24.
"""
import ast
import os

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: The one module allowed to name Convictions as literals — because it is where they are cooked
#: from the registry, and even there they are read from the artifact, not typed.
_OWNER = os.path.join('engine', 'substrate', 'descriptors.py')

#: The alias map is allowed to name retired roster names against canonical ones.
_ALLOWED = {_OWNER}


def _canonical():
    from engine.substrate import descriptors
    return set(descriptors.CONVICTIONS)


def _py_files():
    for tree in ('engine', 'systems'):
        for dirpath, dirnames, filenames in os.walk(os.path.join(_ROOT, tree)):
            dirnames[:] = [d for d in dirnames if d != '__pycache__']
            for fn in filenames:
                if fn.endswith('.py'):
                    yield os.path.join(dirpath, fn)


def test_the_roster_comes_from_the_registry_not_a_literal():
    from engine.substrate import descriptors
    assert len(descriptors.CONVICTIONS) == 13
    # Every consumer is the SAME object, not a copy that can drift.
    from systems.characters.sim import conviction
    from systems.world.sim import npe
    assert conviction.CONVICTIONS is descriptors.CONVICTIONS
    assert npe.CONVICTIONS is descriptors.CONVICTIONS


def test_no_second_conviction_roster_in_code():
    """A literal holding 2+ canonical Conviction names is a re-hardcoded roster.

    DICT LITERALS ARE INCLUDED, AND THEY ARE WHY THIS DOCSTRING EXISTS. The first version checked
    only Tuple/List/Set, and a Dict slipped straight through: systems/world/sim/npe.py's
    deviation-flip carried {"Faith": "Reason", "Order": "Survival", ...} — eight names, six of them
    non-canonical — and survived the very commit that shipped this guard. Worse than a stale copy:
    once CONVICTIONS became canonical, that map could MINT a name resolve_conviction raises on.
    Keys AND values are inspected, because either half is a roster fragment.
    """
    canon = _canonical()
    offenders = []
    for path in _py_files():
        rel = os.path.relpath(path, _ROOT)
        if rel in _ALLOWED:
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
        'a second Conviction roster has been hardcoded. The roster is owned by '
        'references/descriptor_registry.yaml:conviction_roster and read via '
        'engine.substrate.descriptors.CONVICTIONS — read it, do not retype it:\n  '
        + '\n  '.join(offenders)
    )


def test_every_non_canonical_name_raises_and_nothing_is_silently_migrated():
    """No legacy name is translated — including the two that briefly WERE.

    `Reason` and `Autonomy` were aliased to Scholastic and Liberty for a few hours on 2026-08-24,
    justified as "a rename rather than a design call". Both conviction_taxonomy_v30.md:282 and
    references/alias_registry.yaml:658-663 route legacy tags to PER-CHARACTER migration under
    PP-685 and deliberately name no single target, so the alias decided a ruling by accident.
    This pins that no future edit quietly reintroduces one.
    """
    from engine.substrate import descriptors
    assert not hasattr(descriptors, 'CONVICTION_ALIASES'), (
        'an alias map is back. A legacy Conviction tag has no single canonical target — see '
        'conviction_taxonomy_v30.md §6 and references/alias_registry.yaml.')
    for dead in ('Justice', 'Survival', 'Loyalty', 'Truth', 'Power',
                 'Continuity', 'Reason', 'Autonomy'):
        with pytest.raises(ValueError):
            descriptors.resolve_conviction(dead)
    # A canonical name passes through unchanged — the function translates nothing.
    for good in descriptors.CONVICTIONS:
        assert descriptors.resolve_conviction(good) == good
