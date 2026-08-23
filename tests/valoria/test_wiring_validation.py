"""Unit tests for `tools/export_composition.py`'s `validate_wiring` — the wiring gate
(ED-IN-0074) after plan S5c folded `references/wiring_manifest.yaml` into
`references/module_contracts.yaml`.

WHY THIS FILE EXISTS, stated plainly because its absence was a real defect for one commit.
S5c deleted `tests/valoria/test_wiring_map_check.py` along with the tool it pinned, and moved
three of that tool's five rules into `export_composition.py`. The rules therefore travelled
from a tool WITH a falsifier to a tool WITHOUT one, while `references/ci_checks_registry.yaml`
asserted they were "mutation-verified" — a result claim with no artifact in the tree, which is
exactly what CLAUDE.md §0.1 point 3 forbids. An adversarial pass caught it. This is the
artifact; the claim is now falsifiable rather than merely true.

It earns its existence under §0.1 point 5's load-bearing predicate: the `wiring:` facts are the
Godot port work-list, so their subject is the port, not this repository's process. It is also
not net-new apparatus — it restores a falsifier the same step removed, and the tool count is
still down by one.

HERMETIC, and for the same reason the deleted file was: every case runs `validate_wiring` over
synthetic in-memory structures, never the live registry. A legitimate adapter rename should red
the BLOCKING `export_composition --check` CI gate, not this suite. These pin the gate's LOGIC so
it cannot silently stop gating.

The one rule that CANNOT be tested here is the one the fold discharged: "every wiring tag
resolves to a module contract" has no test because it has no way to fail — the facts are a
sub-map of the contract row. That absence is the fold's whole result, so it is named rather
than quietly missing.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import export_composition as ec  # noqa: E402

REAL_ADAPTERS = sorted(
    f[:-3] for f in os.listdir(os.path.join(ec.REPO, 'engine', 'cross_scale'))
    if f.endswith('.py') and not f.startswith('__')
)


def _contracts(**over):
    """A tiny, internally-consistent registry: 2 modules + every real adapter, full coverage."""
    doc = {
        'wiring_vocabularies': {
            'build_states': ['live', 'gated', 'deferred', 'unwired', 'stub', 'design'],
            'godot_states': ['gd-ported', 'typed-exported', 'python-oracle', 'no-oracle', 'retire'],
        },
        'modules': [
            {'module': 'alpha', 'wiring': {'build': 'live', 'godot': 'gd-ported', 'port_rank': 0}},
            {'module': 'beta', 'wiring': {'build': 'design', 'godot': 'no-oracle', 'port_rank': 8}},
        ],
        'adapters': {n: {'build': 'gated', 'godot': 'python-oracle'} for n in REAL_ADAPTERS},
    }
    doc.update(over)
    return doc


def test_a_consistent_registry_is_green():
    """The control. Without it every failure below could be a broken fixture."""
    assert ec.validate_wiring(_contracts()) == []


def test_a_module_row_without_wiring_is_caught():
    c = _contracts()
    del c['modules'][1]['wiring']
    fails = ec.validate_wiring(c)
    assert any('beta' in f and 'wiring' in f for f in fails), fails


def test_an_unnamed_module_row_is_caught():
    """A row with no `module:` key vanishes into every consumer that keys the list by name."""
    c = _contracts()
    del c['modules'][0]['module']
    assert any('modules[0]' in f and 'name' in f for f in ec.validate_wiring(c)), ec.validate_wiring(c)


def test_a_duplicated_module_name_is_caught():
    """`modules:` is a LIST. The retired manifest was a MAP, where this could not happen; the
    fold did not inherit that guarantee, and consumers silently keep the last row."""
    c = _contracts()
    c['modules'].append({'module': 'alpha', 'wiring': {'build': 'live', 'godot': 'retire'}})
    assert any('declared twice' in f for f in ec.validate_wiring(c)), ec.validate_wiring(c)


def test_an_adapter_tag_that_names_no_file_is_caught():
    c = _contracts()
    c['adapters']['not_a_real_adapter'] = {'build': 'gated', 'godot': 'python-oracle'}
    assert any('not_a_real_adapter' in f and 'does not resolve' in f
               for f in ec.validate_wiring(c)), ec.validate_wiring(c)


def test_an_undeclared_adapter_on_disk_is_caught():
    """Coverage runs the other way too: a new cross_scale seam must be declared."""
    c = _contracts()
    c['adapters'].pop(REAL_ADAPTERS[0])
    fails = ec.validate_wiring(c)
    assert any('coverage' in f and REAL_ADAPTERS[0] in f for f in fails), fails


def test_coverage_counts_tags_that_RESOLVE_not_tags_that_exist():
    """A rename keeps the declared count at 8 and must not print '8/8' while failing."""
    c = _contracts()
    c['adapters']['renamed_seam'] = c['adapters'].pop(REAL_ADAPTERS[0])
    cov = [f for f in ec.validate_wiring(c) if 'coverage' in f]
    assert cov and f'{len(REAL_ADAPTERS) - 1}/{len(REAL_ADAPTERS)}' in cov[0], cov


def test_a_bad_build_or_godot_value_is_caught_on_modules_and_adapters():
    c = _contracts()
    c['modules'][0]['wiring']['build'] = 'mostly-live'
    c['adapters'][REAL_ADAPTERS[0]]['godot'] = 'half-ported'
    fails = ec.validate_wiring(c)
    assert any('bad build state' in f for f in fails), fails
    assert any('bad godot state' in f for f in fails), fails


def test_a_missing_vocabulary_fails_loudly_rather_than_vacuously_passing():
    """Without vocabularies every value is unvalidatable, so this must not read as green —
    the failure mode CLAUDE.md §0.1 point 2 is about."""
    c = _contracts()
    del c['wiring_vocabularies']
    fails = ec.validate_wiring(c)
    assert fails and 'unvalidatable' in fails[0], fails


def test_the_live_registry_passes_its_own_gate():
    """One non-hermetic case, deliberately: the rules above are worthless if the shipped
    registry does not satisfy them. This is the only test here that reads the real file."""
    live = ec.ci_common.load_yaml(ec.SRC, default=None)
    assert live, 'references/module_contracts.yaml did not load'
    assert ec.validate_wiring(live) == []
