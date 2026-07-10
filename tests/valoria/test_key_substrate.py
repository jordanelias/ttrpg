"""Tests for sim/substrate/keys.py — the executable Key substrate v1 (ED-IN-0018).

Covers: registry loading against the live key_type_registry_v30.md; the §2.3
universal invariants; SSI append-order assignment; KeyLog replay determinism
(byte-identical serialization across two identically-seeded constructions);
the Theorem-B termination guard (cascade-depth cap, emissions-per-tick cap,
fan-out width NOT counting as depth); B1 no-synchronous-re-entry; and OF-7
deferred-apply at ACCOUNTING_BOUNDARY. Caps in these tests are explicit
arbitrary values — OF-CAP is an open fork and the substrate takes caps as
required parameters (no canonical constants exist to assert against).
"""

import random

import pytest

from sim.substrate import (
    EmittedAt,
    Key,
    KeyLog,
    KeyValidationError,
    Target,
    TerminationBreach,
    TickScheduler,
    TypeRegistry,
    Visibility,
)

REGISTRY_PATH = "designs/architecture/key_type_registry_v30.md"


@pytest.fixture(scope="module")
def registry():
    return TypeRegistry.load(REGISTRY_PATH)


def make_key(kid, ktype="scene.dialogue", season=0, payload=None, **kw):
    payload = payload if payload is not None else {
        "exchange_count": 1, "initiator_id": "npc_a", "topic": "harvest",
    }
    defaults = dict(
        emitted_at=EmittedAt(season_index=season),
        scale_signature=["personal"],
        visibility=Visibility(public=True),
    )
    defaults.update(kw)
    return Key(id=kid, type=ktype, payload=payload, **defaults)


# -- registry ---------------------------------------------------------------

def test_registry_loads_full_roster(registry):
    # §9 counts 44 types; the file physically carries 48 ### type headings
    # (44 + combat STUB entries counted with personal_combat). Assert the
    # parse found at least the §9 roster and the entries the substrate needs.
    assert len(registry.types) >= 44
    for tid in ("scene.dialogue", "scene.contest_resolved", "env.crisis",
                "meta.miraculous_event", "mechanical.accounting"):
        assert tid in registry.types, tid


def test_registry_required_fields_scene_dialogue(registry):
    entry = registry.require("scene.dialogue")
    names = [str(f).split("#", 1)[0].strip() for f in entry["required_payload_fields"]]
    assert names == ["exchange_count", "initiator_id", "topic"]


def test_unknown_type_rejected(registry):
    log = KeyLog(registry)
    with pytest.raises(KeyValidationError, match="not registered"):
        log.append(make_key("k1", ktype="scene.not_a_type"))


def test_missing_required_payload_rejected(registry):
    log = KeyLog(registry)
    with pytest.raises(KeyValidationError, match="missing required payload"):
        log.append(make_key("k1", payload={"exchange_count": 1}))


# -- §2.3 universal invariants ----------------------------------------------

def test_duplicate_id_rejected(registry):
    log = KeyLog(registry)
    log.append(make_key("k1"))
    with pytest.raises(KeyValidationError, match="duplicate"):
        log.append(make_key("k1"))


def test_unknown_cause_rejected(registry):
    log = KeyLog(registry)
    with pytest.raises(KeyValidationError, match="unknown cause"):
        log.append(make_key("k1", causes=["ghost"]))


def test_known_cause_accepted(registry):
    log = KeyLog(registry)
    log.append(make_key("k1"))
    log.append(make_key("k2", causes=["k1"]))
    assert log.lookup("k2").causes == ["k1"]


def test_season_regression_rejected(registry):
    log = KeyLog(registry)
    log.append(make_key("k1", season=3))
    with pytest.raises(KeyValidationError, match="regresses"):
        log.append(make_key("k2", season=2))


def test_non_canonical_axis_rejected(registry):
    log = KeyLog(registry)
    bad = make_key("k1", symbolic_dimensions={"vibes": 1.0})
    with pytest.raises(KeyValidationError, match="non-canonical axis"):
        log.append(bad)


def test_invalid_target_role_rejected(registry):
    log = KeyLog(registry)
    bad = make_key("k1", targets=[Target(actor_id="a", role="protagonist")])
    with pytest.raises(KeyValidationError, match="invalid role"):
        log.append(bad)


def test_empty_scale_signature_rejected(registry):
    log = KeyLog(registry)
    with pytest.raises(KeyValidationError, match="empty scale_signature"):
        log.append(make_key("k1", scale_signature=[]))


def test_visibility_shapes(registry):
    log = KeyLog(registry)
    # public with observer lists -> invalid
    with pytest.raises(KeyValidationError, match="invariant 8"):
        log.append(make_key("k1", visibility=Visibility(public=True, private_observers=["a"])))
    # non-public with no lists -> invalid
    with pytest.raises(KeyValidationError, match="invariant 8"):
        log.append(make_key("k2", visibility=Visibility(public=False)))
    # non-public with both lists -> invalid
    with pytest.raises(KeyValidationError, match="invariant 8"):
        log.append(make_key("k3", visibility=Visibility(
            public=False, semi_public_observers=["a"], private_observers=["b"])))
    # each valid shape
    log.append(make_key("k4", visibility=Visibility(public=False, private_observers=["a"])))
    log.append(make_key("k5", visibility=Visibility(public=False, semi_public_observers=["a", "b"])))


# -- OPT-AV-16 stat-vocabulary hook (extension §3.1, ED-IN-0029; candidate
# invariant 9 — WARN-tier, collects, never raises) --------------------------

def test_stat_vocabulary_default_none_is_unchanged(registry):
    # Default behavior must be byte-for-byte what it was before this hook
    # existed: no vocabulary check performed, no warnings list populated,
    # and an unresolvable stat_deltas key does not raise.
    log = KeyLog(registry)
    log.append(make_key("k1", targets=[
        Target(actor_id="a", role="witness", stat_deltas={"NotARegisteredStat": 1}),
    ]))
    assert log.stat_vocabulary is None
    assert log.stat_vocabulary_warnings == []


def test_stat_vocabulary_warns_but_never_raises(registry):
    known = {"Strength", "Wealth"}
    log = KeyLog(registry, stat_vocabulary=known)
    log.append(make_key("k1", targets=[
        Target(actor_id="a", role="witness",
               stat_deltas={"Strength": 1, "TotallyMadeUp": 2}),
    ]))
    assert len(log.stat_vocabulary_warnings) == 1
    assert "TotallyMadeUp" in log.stat_vocabulary_warnings[0]
    assert "Strength" not in log.stat_vocabulary_warnings[0]


def test_stat_vocabulary_accepts_callable_resolver(registry):
    resolver = lambda name: name == "Wealth"  # noqa: E731
    log = KeyLog(registry, stat_vocabulary=resolver)
    log.append(make_key("k1", targets=[
        Target(actor_id="a", role="witness", stat_deltas={"Wealth": 1, "Other": 1}),
    ]))
    assert len(log.stat_vocabulary_warnings) == 1
    assert "Other" in log.stat_vocabulary_warnings[0]


# -- SSI append order + determinism ------------------------------------------

def test_sub_step_index_append_order(registry):
    log = KeyLog(registry)
    a = log.append(make_key("k1", season=0))
    b = log.append(make_key("k2", season=0))
    c = log.append(make_key("k3", season=1))
    assert (a.emitted_at.sub_step_index, b.emitted_at.sub_step_index) == (0, 1)
    assert c.emitted_at.sub_step_index == 0  # counter is per-season


def _build_seeded_log(registry, seed):
    rng = random.Random(seed)
    log = KeyLog(registry)
    for i in range(25):
        log.append(make_key(
            f"k{i}", season=i // 7,
            payload={"exchange_count": rng.randint(1, 5),
                     "initiator_id": f"npc_{rng.randint(0, 3)}", "topic": "t"},
            targets=[Target(actor_id=f"a{rng.randint(0, 2)}", role="witness",
                            impact_vector={"sacred": rng.random()})],
        ))
    return log


def test_keylog_replay_byte_identical(registry):
    log1 = _build_seeded_log(registry, seed=99)
    log2 = _build_seeded_log(registry, seed=99)
    assert log1.serialize() == log2.serialize()
    assert log1.content_hash() == log2.content_hash()
    log3 = _build_seeded_log(registry, seed=100)
    assert log1.content_hash() != log3.content_hash()


# -- Theorem-B termination guard ----------------------------------------------

def _sched(registry, **kw):
    kw.setdefault("cascade_depth_max", 3)
    kw.setdefault("emissions_per_tick_max", 10)
    # OF-7/OF-B1 are RATIFIED (Jordan's 2026-07-07 consolidated "ratify all"
    # ruling pass, ED-IN-0026 — armature §5.3/5.4) and default True on
    # TickScheduler itself; restated explicitly here so these tests keep
    # exercising them even if the class default ever changes.
    # test_defaults_are_authoritative_canon pins the class default directly.
    kw.setdefault("no_sync_reentry", True)
    kw.setdefault("defer_apply", True)
    return TickScheduler(KeyLog(registry), **kw)


def test_defaults_are_authoritative_canon(registry):
    # OF-7 / OF-B1 are RATIFIED amendments (2026-07-07 ruling pass): the
    # oracle's defaults now follow the amended canon — synchronous re-entry
    # during a drain is forbidden, and apply callbacks defer to
    # accounting_boundary() rather than running live.
    s = TickScheduler(KeyLog(registry), cascade_depth_max=3, emissions_per_tick_max=10)
    assert s.no_sync_reentry is True and s.defer_apply is True
    applied = []
    s.emit(make_key("k0"), apply=lambda k: applied.append(k.id))
    assert applied == []  # deferred, not live
    ran = s.accounting_boundary()
    assert ran == 1 and applied == ["k0"]


def test_emissions_per_tick_cap_fires(registry):
    s = _sched(registry, emissions_per_tick_max=3)
    for i in range(3):
        s.emit(make_key(f"k{i}"))
    with pytest.raises(TerminationBreach, match="emissions this tick"):
        s.emit(make_key("k_overflow"))
    s.next_tick()
    s.emit(make_key("k_next_tick_ok"))  # counter resets


def test_cascade_depth_cap_fires(registry):
    s = _sched(registry, cascade_depth_max=1, emissions_per_tick_max=100)

    def reemit(key, sched):
        # every consumed dialogue key spawns another -> runaway cascade
        sched.schedule_emission(make_key("re_" + key.id))

    s.subscribe("scene.dialogue", reemit)
    s.schedule_emission(make_key("k0"))
    with pytest.raises(TerminationBreach, match="cascade_depth"):
        s.drain_tick()


def test_fanout_width_does_not_increment_depth(registry):
    # One Key, N targets is a SINGLE emission at one depth (propagation_spec
    # §3 D.1) — a wide targets[] array must not trip the depth cap.
    s = _sched(registry, cascade_depth_max=0, emissions_per_tick_max=5)
    wide = make_key("kw", targets=[
        Target(actor_id=f"a{i}", role="bystander") for i in range(50)
    ])
    s.emit(wide)  # must not raise
    assert len(s.log) == 1


def test_bounded_cascade_drains_clean(registry):
    s = _sched(registry, cascade_depth_max=2, emissions_per_tick_max=10)
    fired = []

    def once(key, sched):
        if not key.id.startswith("child_"):
            sched.schedule_emission(make_key("child_" + key.id))
        fired.append(key.id)

    s.subscribe("scene.dialogue", once)
    s.schedule_emission(make_key("k0"))
    drained = s.drain_tick()
    assert drained == 2 and fired == ["k0", "child_k0"]


# -- B1 no-synchronous-re-entry ------------------------------------------------

def test_sync_reentry_raises_under_b1(registry):
    s = _sched(registry)

    def bad_consumer(key, sched):
        sched.emit(make_key("sync_" + key.id))  # forbidden under B1

    s.subscribe("scene.dialogue", bad_consumer)
    s.schedule_emission(make_key("k0"))
    with pytest.raises(TerminationBreach, match="synchronous re-entry"):
        s.drain_tick()


def test_sync_reentry_allowed_when_flag_off(registry):
    s = _sched(registry, no_sync_reentry=False, emissions_per_tick_max=10)

    def consumer(key, sched):
        if key.id == "k0":
            sched.emit(make_key("sync_child"))

    s.subscribe("scene.dialogue", consumer)
    s.schedule_emission(make_key("k0"))
    s.drain_tick()
    assert len(s.log) == 2


# -- OF-7 deferred-apply --------------------------------------------------------

def test_deferred_apply_waits_for_accounting_boundary(registry):
    s = _sched(registry)
    applied = []
    s.emit(make_key("k0"), apply=lambda k: applied.append(k.id))
    # AU-3.2: the Key is logged LIVE, its settlement effect is deferred.
    assert len(s.log) == 1 and applied == []
    ran = s.accounting_boundary()
    assert ran == 1 and applied == ["k0"]


def test_apply_immediate_when_defer_flag_off(registry):
    s = _sched(registry, defer_apply=False)
    applied = []
    s.emit(make_key("k0"), apply=lambda k: applied.append(k.id))
    assert applied == ["k0"]


def test_undrained_queue_blocks_tick_advance(registry):
    s = _sched(registry)
    s.schedule_emission(make_key("k0"))
    with pytest.raises(TerminationBreach, match="undrained"):
        s.next_tick()


# -- registry defaults ----------------------------------------------------------

def test_registry_defaults_applied_on_emit(registry):
    s = _sched(registry)
    k = Key(id="kd", type="scene.dialogue",
            emitted_at=EmittedAt(season_index=0),
            scale_signature=[],  # empty -> registry default [personal]
            payload={"exchange_count": 1, "initiator_id": "n", "topic": "t"})
    s.emit(k)
    assert k.scale_signature == ["personal"]
    # scene.dialogue: default_permanence=persistent, default_time_horizon=near
    assert k.permanence == "persistent" and k.time_horizon == "near"
