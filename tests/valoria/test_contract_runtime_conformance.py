"""The runtime-conformance instrument measures the ENGINE, and does not perturb it.

WHY THIS EXISTS. CI's existing "Module-Contract Conformance (report-only)" job compares
DECLARATIONS AGAINST DECLARATIONS — contracts vs the Key Type Registry vs canonical_sources. Nothing
had ever asked the engine what it actually emits, so a module declaring `emits: [scene.dialogue]` and
emitting nothing was indistinguishable from one emitting it every season. That distinction IS the
hub-and-bus question (Jordan, 2026-08-24), and CLAUDE.md §0.2 says a juncture is done when the
behaviour EXECUTES — so the instrument runs a seeded campaign.

THE CONTROL IS THE LOAD-BEARING TEST HERE, not the counts. The instrument WRAPS
`TickScheduler._emit_at_depth`; if that wrapper changed campaign behaviour, every number it produces
would describe a system that does not ship. `test_instrumentation_does_not_move_the_key_log` is the
falsifier: same seed, same n, instrumented vs not, byte-identical `KeyLog.content_hash()`.

WHAT IT MEASURED ON 2026-08-24, recorded so a later reader can see whether it moved:
  397 emissions across 2 seeded campaigns, from exactly THREE call sites, and no contract claims
  any of the three files. 60 declared emit edges, 0 observed. 82 declared consume edges, 13
  observed — all `articulation_layer`, all stub-wire no-ops, and NONE of the 13 declared by it.
"""
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, ROOT)


@pytest.fixture(scope='module')
def measured():
    os.environ.setdefault('ECHO_TRANSPORT', '1')
    import contract_runtime_conformance as C
    return C, C.report(n=1, base_seed=0)


def test_the_campaign_actually_emitted_something(measured):
    """A conformance verdict computed over zero emissions is vacuous, and would read as 'clean'."""
    _, r = measured
    assert r['emission_volume'] > 0, (
        'no Keys were emitted, so every conformance number below is vacuous. Check ECHO_TRANSPORT '
        '— with the bus off there is no scheduler and nothing to observe.'
    )


def test_instrumentation_does_not_move_the_key_log():
    """THE CONTROL. Instrumented and uninstrumented runs must produce the same key-log hash.

    Without this the instrument's numbers describe whatever the wrapper turned the engine into.
    """
    os.environ.setdefault('ECHO_TRANSPORT', '1')
    import contract_runtime_conformance as C
    from engine import mc_v18
    from engine.substrate import keys as K

    _, _, instrumented_hash, _, _ = C.observe(n=1, base_seed=0)

    plain = []
    orig = K.TickScheduler.__init__
    def init(self, *a, **kw):
        orig(self, *a, **kw); plain.append(self)
    K.TickScheduler.__init__ = init
    try:
        mc_v18.run_batch(n=1, base_seed=0)
    finally:
        K.TickScheduler.__init__ = orig
    plain_hashes = [s.log.content_hash() for s in plain if getattr(s, 'log', None) is not None]

    assert plain_hashes, 'no scheduler was constructed in the uninstrumented run'
    assert instrumented_hash == plain_hashes[0], (
        'the instrument MOVED the key log — its measurements describe a system that does not ship. '
        f'instrumented={instrumented_hash} plain={plain_hashes[0]}'
    )


def test_the_bus_is_never_scored_as_an_emitter(measured):
    """`engine/substrate/` is the transport. If it were attributed, every Key would look like the
    substrate's own and no subsystem would ever appear."""
    C, r = measured
    _, p2m, _ = C._load_contracts()
    for prefix, module in p2m:
        assert not prefix.startswith('engine/substrate'), f'{module} binds the bus itself'
    for k in r['unclaimed_emitters']:
        assert not k.startswith('engine/substrate/'), k


def test_a_caller_is_not_credited_as_the_emitter(measured):
    """MUTATION-VERIFIED REGRESSION. The first version walked the stack until SOME frame matched a
    contract, so an unclaimed emitter was laundered onto whichever ancestor happened to be claimed —
    it attributed `scene.battle_concluded` to `peninsular_strain`, whose files never emit.

    ⚠ THE OBVIOUS ASSERTION DOES NOT CATCH THAT BUG, and an earlier draft of this test made exactly
    that mistake. "the attributed module binds a path" is TRUE of `peninsular_strain`, so the weak
    form was green over the defect it was written for (§0.1 pt 2 — an assertion must be able to
    observe the failure it excludes). The real check is that the FILE that emitted lives under the
    attributed module's own path prefix, which is why `observe` records the sites at all.
    """
    C, r = measured
    _, p2m, _ = C._load_contracts()
    by_module = dict((m, p) for p, m in p2m)
    for edge, files in r['attributed_sites'].items():
        module = edge.rsplit(':', 1)[0]
        prefix = by_module.get(module)
        assert prefix, f'attributed to {module}, which binds no path'
        for f in files:
            assert f == prefix or f.startswith(prefix.rstrip('/') + '/'), (
                f'{edge} was attributed to {module} (path {prefix!r}) but the emitting file is '
                f'{f!r} — a CALLER is being credited as the emitter.'
            )


def test_unclaimed_emitters_are_reported_not_swallowed(measured):
    """An emitting file no contract claims is a REGISTRY GAP and must be visible. Today all three
    production emitters are unclaimed; a version that hid them would report a clean interface."""
    _, r = measured
    assert r['unclaimed_emitters'], (
        'no unclaimed emitters reported. Either the registry now claims every emitting file — '
        'genuinely good, update this test and say so — or the reporting path broke.'
    )
    for key, count in r['unclaimed_emitters'].items():
        assert '::' in key and count > 0, key
