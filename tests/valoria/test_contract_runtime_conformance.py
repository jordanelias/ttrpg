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


def test_a_wildcard_does_not_suppress_an_undeclared_type(measured):
    """A wildcard grants a MODULE permission to consume. It does not DECLARE that a type exists.

    ⚠ THIS TEST ASSERTED THE OPPOSITE FOR A FEW HOURS ON 2026-08-24, AND THAT IS WHY THE FLOOR WAS
    UNFAILABLE. It read "a module declaring `{type: "*"}` declares every type on that side, so its
    subscriptions can never be undeclared drift" — and `_triage` implemented it as
    `declared_by.get(t) or list(wildcards)`, which cannot return empty while any wildcard consumer
    exists. `undeclared_type` was unreachable on the consume side and the tool reported the floor
    MET. CLAUDE.md §0.1 pt 2: an assertion that cannot observe the failure it excludes.

    Two real gaps were hiding behind it. `scene.accord_echo` and `meta.cascade_cluster_event` are
    both in the Key vocabulary (`engine/engine_params/key_types.json`) and NO module contract names
    either, on either side — while `engine/cross_scale/articulation.py:125,129` subscribes to both.
    """
    C, r = measured
    modules, _, _ = C._load_contracts()
    wildcard_consumers = {m for m, d in modules.items() if d.get('consumes_any')}
    assert wildcard_consumers, 'no wildcard consumer — this test no longer has a subject'
    explicit = {t for d in modules.values() for t in d['consumes']}
    for edge in r['consumes']['observed_only']:
        module, _, type_id = edge.rpartition(':')
        if type_id in explicit:
            continue
        flagged = any(edge in x for x in r['consumes']['triage']['undeclared_type'])
        assert flagged, (
            f'{edge} is consumed at runtime, no contract declares the type, and the triage did not '
            f'flag it — the wildcard is suppressing a real gap again.'
        )


def test_matched_never_counts_a_wildcard_edge(measured):
    """`matched` must mean "explicitly declared AND observed", or it measures nothing.

    Folding wildcard expansion into `declared` makes `matched == observed` for that module BY
    CONSTRUCTION — the number cannot fail. It shipped that way for a few hours as "108 declared /
    13 matched"; every one of the 13 was `articulation_layer`, which declares `consumes: []` and so
    matched only itself. The honest numbers are 82 declared / 13 observed / 0 matched.
    """
    C, r = measured
    modules, _, _ = C._load_contracts()
    explicit_c = {f'{m}:{t}' for m, d in modules.items() for t in d['consumes']}
    explicit_e = {f'{m}:{t}' for m, d in modules.items() for t in d['emits']}
    for edge in r['consumes']['matched']:
        assert edge in explicit_c, f'{edge} counted as matched but is only wildcard-covered'
    for edge in r['emits']['matched']:
        assert edge in explicit_e, f'{edge} counted as matched but is only wildcard-covered'
    # Wildcard coverage is reported, just never as conformance.
    assert 'wildcard_covered' in r['consumes']


def test_check_mode_gates_only_genuinely_undeclared_types(measured):
    """The HARD FLOOR is narrow on purpose: gating the wide "observed but not declared" measure
    would block on registry holes (a declared owner with no `sim_module`) and on ownership
    questions — including the deliberate cross-scale carrier pattern. Those are reported, never
    gated. But narrow must not mean UNFAILABLE, which is what the wildcard fallback made it."""
    C, r = measured
    assert C.UNDECLARED_TYPE_MAX == 0
    for side in ('emits', 'consumes'):
        tri = r[side]['triage']
        wide = set(r[side]['observed_only'])
        n = len(tri['undeclared_type']) + len(tri['ownership_mismatch']) + len(tri['unobservable'])
        assert n == len(wide), f'{side}: triage lost or duplicated an edge ({n} vs {len(wide)})'


def test_the_floor_is_currently_RED_and_says_so(measured):
    """Records the honest state rather than a green claim.

    Two Key types flow that no contract declares, so `--check` exits 1 today. This test exists so
    that fixing them is a DELIBERATE act with a visible diff, not something that drifts to green —
    and so that a future reader cannot mistake the earlier "floor MET" claim (produced by the
    vacuous fallback) for a measurement. When the two are declared or accepted, delete this test
    and say which in the commit.
    """
    _, r = measured
    undeclared = (r['emits']['triage']['undeclared_type']
                  + r['consumes']['triage']['undeclared_type'])
    assert len(undeclared) == 2, (
        f'the undeclared-type count moved to {len(undeclared)}: {undeclared}. If it went DOWN, the '
        f'gap was closed — update or delete this test in the same commit and name what changed. If '
        f'it went UP, a new Key type is flowing that no contract declares.'
    )
    joined = ' '.join(undeclared)
    assert 'scene.accord_echo' in joined and 'meta.cascade_cluster_event' in joined
