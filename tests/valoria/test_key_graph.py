"""The Key graph must be a graph — every key produced by someone and consumed by someone.

WHY. The architecture says subsystems communicate by emitting typed Keys. MEASURED 2026-08-02:
**55 key types declared, 1 emitted anywhere in the codebase** (`scene.accord_echo`, in
`engine/cross_scale/echo_transport.py`), while the real inter-subsystem traffic is 16 direct
Python imports. The contracts reference 47 dotted key names; implemented coverage is ~2%.

Nothing noticed because nothing could: the graph was authored TWICE, in two formats, and no tool
ever joined them. `systems/_architecture/key_type_registry_v30.md` carries
`emitting_systems`/`consuming_systems` as FREE PROSE (values include `'all subscribing systems'`
and `'npc_behavior / Procedure E'`); `references/module_contracts.yaml` carries typed
`emits`/`consumes`. A prose field cannot be joined to a typed one, so the two drifted in public
for months while both looked authoritative.

`tools/build_key_graph.py` merges them into `references/key_graph.json`. This file is the guard
on the merged result.

THE INVARIANT THAT MATTERS is `test_every_key_has_a_producer` / `..._a_consumer`. A key type with
no producer is a schema nobody fills; with no consumer it is a message nobody reads. Either way it
is a declaration masquerading as a system, and **this invariant firing on day one is what would
have stopped 54-of-55 from accumulating**. It is therefore expressed as a BASELINE that may only
shrink, not a report: the known gaps are enumerated below, and a NEW one fails the build.

WHAT THE MERGE FOUND, recorded because the headline number was wrong in the alarming direction:
a first pass reported 20 producer and 42 consumer "conflicts" — an apparently intractable 62
decisions. After six evidence-backed aliases and distinguishing DISAGREEMENT from INCOMPLETENESS,
the genuine conflict count is **ZERO**. The two views agree everywhere they both speak; they
simply speak at different completeness. That distinction is load-bearing: a subset is a filing
task, a conflict is a design decision, and collapsing them made a tractable backlog read as a
crisis.
"""
import json
import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
GRAPH = os.path.join(ROOT, 'references', 'key_graph.json')

KEY_RE = re.compile(r'^[a-z_]+\.[a-z_]+$')

# Keys with no declared PRODUCER, as measured at introduction. This set may shrink, never grow.
# `*` is not a key at all — a wildcard that leaked into module_contracts' `emits`/`consumes`.
KNOWN_NO_PRODUCER = {'*', 'meta.legacy_event'}

# Keys with no declared CONSUMER. Every one is a real declaration nobody listens to; several are
# terminal world-events (era_transition, second_calamity, theocracy_unification_declared) where a
# consumer may genuinely not exist yet. Enumerated rather than waived so the number is visible and
# can be driven down deliberately.
KNOWN_NO_CONSUMER = {
    'env.crisis', 'mechanical.era_transition', 'mechanical.season_change',
    'mechanical.second_calamity', 'mechanical.settlement_captured',
    'mechanical.theocracy_unification_declared', 'meta.legacy_event',
    'state.settlement_revolt',
}

# Registry prose that names no module. Left unresolved ON PURPOSE — mapping `player_input` or
# `all subscribing systems` to a module is a design decision, and guessing one is exactly the
# fabrication this repo's no-fabrication rule forbids.
KNOWN_UNRESOLVED = {'all', 'all subscribing systems', 'echo_transport',
                    'legacy-aware consumers only', 'player_input', 'substrate (auto)'}


@pytest.fixture(scope='module')
def graph():
    if not os.path.exists(GRAPH):
        pytest.fail('references/key_graph.json missing — run tools/build_key_graph.py')
    with open(GRAPH, encoding='utf-8') as f:
        return json.load(f)


def test_graph_is_not_vacuous(graph):
    """Guards the guard: an empty graph would make every assertion below trivially true."""
    assert len(graph['keys']) >= 50, f"only {len(graph['keys'])} key types — the merge is broken"
    assert len(graph['modules']) >= 25, f"only {len(graph['modules'])} modules"


def test_every_key_has_a_producer(graph):
    orphans = {k for k, v in graph['keys'].items() if not v['producers']}
    new = orphans - KNOWN_NO_PRODUCER
    assert not new, (
        f'key type(s) with NO producer: {sorted(new)}.\n'
        f'A key nobody emits is a schema nobody fills. Either declare an emitter in '
        f'module_contracts.yaml / key_type_registry_v30.md, or delete the key type.')


def test_every_key_has_a_consumer(graph):
    orphans = {k for k, v in graph['keys'].items() if not v['consumers']}
    new = orphans - KNOWN_NO_CONSUMER
    assert not new, (
        f'key type(s) with NO consumer: {sorted(new)}.\n'
        f'A key nobody reads is a message into the void — the exact shape that let 54 of 55 key '
        f'types sit unimplemented. Declare a consumer or delete the key type.')


def test_known_gaps_only_shrink(graph):
    """The ratchet. Fixing a gap without updating the baseline should fail, so the baseline stays
    honest rather than drifting into a permanent waiver nobody rereads."""
    no_prod = {k for k, v in graph['keys'].items() if not v['producers']}
    no_cons = {k for k, v in graph['keys'].items() if not v['consumers']}
    stale_p = KNOWN_NO_PRODUCER - no_prod
    stale_c = KNOWN_NO_CONSUMER - no_cons
    assert not stale_p, f'KNOWN_NO_PRODUCER lists fixed key(s) {sorted(stale_p)} — remove them'
    assert not stale_c, f'KNOWN_NO_CONSUMER lists fixed key(s) {sorted(stale_c)} — remove them'


@pytest.mark.parametrize('field', ['producers', 'consumers'])
def test_participants_are_real_modules(graph, field):
    """Every producer/consumer must name a module that exists in the contracts."""
    modules = set(graph['modules'])
    bad = {}
    for kt, v in graph['keys'].items():
        for name in v[field]:
            if name not in modules and name not in KNOWN_UNRESOLVED:
                bad.setdefault(name, []).append(kt)
    assert not bad, (
        f'{field} naming non-existent module(s): '
        f'{ {k: v[:3] for k, v in bad.items()} }.\n'
        f'Either add an alias in build_key_graph.ALIASES (with the EVIDENCE that justifies it) '
        f'or add the module to module_contracts.yaml.')


def test_no_genuine_conflicts(graph):
    """The two authored views must not contradict each other.

    A `conflict` means each side asserts a participant the other omits — a real design decision.
    Subsets are fine (one view under-declared); disagreement is not. Measured at introduction: 0.
    """
    conflicts = [k for k, v in graph['keys'].items()
                 if 'conflict' in (v['reconciliation']['producer_status'],
                                   v['reconciliation']['consumer_status'])]
    assert not conflicts, (
        f'{len(conflicts)} key type(s) where the registry and the contracts CONTRADICT each other: '
        f'{conflicts[:8]}.\nThis needs a human decision, not a merge rule — the builder deliberately '
        f'takes the union rather than picking a winner.')


def test_key_names_are_well_formed(graph):
    bad = {k for k in graph['keys'] if not KEY_RE.match(k)} - KNOWN_NO_PRODUCER
    assert not bad, f'malformed key type name(s): {sorted(bad)} (expected `namespace.name`)'


def test_graph_is_current(graph):
    """The committed graph must equal a fresh rebuild — it is generated, so drift means a hand-edit
    or a stale commit, and either makes every assertion above describe the wrong tree."""
    import subprocess
    import sys
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'build_key_graph.py'), '--check'],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, f'build_key_graph.py --check failed:\n{r.stdout}\n{r.stderr}'
    with open(GRAPH, encoding='utf-8') as f:
        committed = json.load(f)
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'bkg', os.path.join(ROOT, 'tools', 'build_key_graph.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert committed == mod.build(), (
        'references/key_graph.json differs from a fresh build — regenerate with '
        '`python3 tools/build_key_graph.py` and commit.')
