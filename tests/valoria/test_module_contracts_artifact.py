"""The cooked module-contract artifact tracks the registry, and its path binding has one owner.

WHY THIS EXISTS. `references/module_contracts.yaml` declares 27 modules' Key interface and TEN tools
parsed it independently (`test_engine_params_bridge.py`'s `AUTHORED_PARSERS`). It now has an
exporter and a cooked artifact, on the same authored-surface / one-exporter / one-artifact pattern as
descriptors, key_types, composition and world_initial_state.

THE `path_to_module` BINDING IS THE PART WORTH GUARDING, and the reason is a measured failure rather
than a principle. A contract module name is LOGICAL (`domain_actions`, `social_contest`); the tree is
organised by DIRECTORY. Nothing owned the map, so the first run of
`tools/contract_runtime_conformance.py` invented one from directory names and reported "0 of 60
declared emissions happen" — a number that was true of its own attribution scheme and false of the
engine. Two further attribution defects followed (a directory prefix that swallowed a sibling, and a
stack walk that scored a CALLER as the emitter). Every one of them produced a plausible finding.
"""
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTIFACT = os.path.join(ROOT, 'engine', 'engine_params', 'module_contracts.json')
EXPORTER = os.path.join(ROOT, 'tools', 'export_module_contracts.py')


@pytest.fixture(scope='module')
def art():
    with open(ARTIFACT, encoding='utf-8') as fh:
        return json.load(fh)


def test_the_artifact_is_not_stale():
    """The exporter's own --check is the gate; this makes it a test failure too."""
    r = subprocess.run([sys.executable, EXPORTER, '--check'], capture_output=True, text=True,
                       cwd=ROOT)
    assert r.returncode == 0, f'module_contracts.json is stale:\n{r.stdout}{r.stderr}'


def test_every_module_declares_its_interface_shape(art):
    assert art['module_count'] == len(art['modules']) == 27
    for name, m in art['modules'].items():
        assert set(m) == {'impl_path', 'doc', 'emits', 'consumes',
                          'emits_any', 'consumes_any'}, name
        assert isinstance(m['emits'], list) and isinstance(m['consumes'], list), name


def test_path_bindings_are_longest_prefix_first(art):
    """Ordering is load-bearing: `systems/social_contest/sim/contest` must win over a shorter
    sibling, or a subdirectory resolves to the wrong module. A sorted-by-name artifact would
    silently mis-attribute."""
    lengths = [len(p) for p, _ in art['path_to_module']]
    assert lengths == sorted(lengths, reverse=True), art['path_to_module']


def test_no_binding_is_a_bare_tree_root(art):
    """A prefix of `systems` or `engine` would claim the whole tree and make every attribution
    meaningless. Nothing may bind above the subsystem level."""
    for prefix, module in art['path_to_module']:
        assert prefix.count('/') >= 1, f'{module} binds the tree root: {prefix!r}'
        assert prefix not in ('systems', 'engine', 'systems/', 'engine/'), module


def test_unattributable_means_no_path_not_a_guessed_one(art):
    """`sim_module: none` must normalise to None, never to the literal string.

    A consumer treating 'none' as a path would build the prefix `none/` and match nothing, which
    looks identical to a module that genuinely emits nothing — the exact confusion this artifact
    exists to remove."""
    for name in art['unattributable']:
        assert art['modules'][name]['impl_path'] is None, name
    bound = {m for _, m in art['path_to_module']}
    assert bound.isdisjoint(set(art['unattributable']))
    # This is a real, currently-large number. Recorded, not asserted at zero: it is the ED-1051
    # backlog (contract modules with no implementation), and pinning it at 0 would be a lie.
    assert 0 < len(art['unattributable']) < art['module_count']


def test_edge_counts_match_the_declared_lists(art):
    assert art['emit_edge_count'] == sum(len(m['emits']) for m in art['modules'].values())
    assert art['consume_edge_count'] == sum(len(m['consumes']) for m in art['modules'].values())


def test_the_wildcard_survives_the_cook(art):
    """`{type: "*"}` must reach the artifact as a FLAG, not be filtered out as a non-dotted string.

    ⚠ THIS IS THE GUARD FOR A MEASURED, NEARLY-SHIPPED FALSE FINDING. The first exporter kept only
    entries containing a '.', which silently dropped both wildcard declarations.
    `articulation_layer` — a universal reader of the full Key stream (key_substrate §8.7) — cooked as
    `consumes: []`, and the runtime-conformance instrument then reported all THIRTEEN of its live
    subscriptions as undeclared, two of them as types NO contract declares. Every one of those was
    an artifact of this filter. The next step would have been transcribing thirteen type names into
    a contract that already declared a superset — creating the exact drifting twin the centralization
    work exists to remove.
    """
    assert art['wildcard_consumers'], (
        'no wildcard consumer in the artifact. Either the registry dropped both `{type: "*"}` '
        'declarations — say so and update this test — or the exporter is filtering them out again, '
        'which reads as 13 phantom drift findings downstream.'
    )
    for name in art['wildcard_consumers']:
        assert art['modules'][name]['consumes_any'] is True, name
    # Every module carries both flags, so a consumer cannot silently miss the field on one module.
    for name, m in art['modules'].items():
        assert isinstance(m['emits_any'], bool) and isinstance(m['consumes_any'], bool), name
