"""CI-tier static integrity for the scene-combat engagement state graph (WS-1).

Fast, deterministic checks over systems/combat/combat_engine_v1/state_graph.py — the declarative graph that is
the source of truth for "the state graph flows correctly" (requirement 1). The heavier dynamic coverage sweep
+ dead-branch scan lives in state_graph.py's __main__ (it runs fights); here we keep CI fast: the static
graph properties plus one small live smoke that the trace actually visits the core states.
"""
import os
import sys

import pytest

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)
sys.path.insert(0, os.path.join(ENGINE, 'workbench'))

import state_graph as G  # noqa: E402


def test_edge_closure():
    """Every transition target is a defined state (no dangling edges)."""
    valid = set(G.STATES)
    for s, v in G.STATES.items():
        for t in v['to']:
            assert t in valid, f"{s} -> {t}: undefined target"


def test_terminal_reachable_from_entry():
    """At least one terminal exists and is reachable from every entry node."""
    assert G.TERMINAL_STATES
    assert G.ENTRY_STATES
    for e in G.ENTRY_STATES:
        assert G.TERMINAL_STATES & G.reachable_from(e), f"no terminal reachable from {e}"


def test_no_islands():
    """Every state is reachable from some entry node (no unreachable islands)."""
    cover = set().union(*[G.reachable_from(e) for e in G.ENTRY_STATES])
    assert set(G.STATES) - cover == set(), f"islands: {set(G.STATES) - cover}"


def test_emit_legality():
    """Every declared emit is a known trace-event kind the engine actually fires."""
    for s, v in G.STATES.items():
        for em in v['emits']:
            assert em in G.TRACE_KINDS, f"{s} declares unknown emit '{em}'"


def test_terminals_have_no_outgoing_edges():
    for t in G.TERMINAL_STATES:
        assert G.STATES[t]['to'] == [], f"terminal {t} has outgoing edges"


def test_live_trace_visits_core_states():
    """A small live sweep: the engine's trace must visit the core path states (proves the graph is live, not
    just well-formed). Kept tiny + seeded for CI speed/determinism."""
    pytest.importorskip("numpy")  # this smoke runs a live fight (-> r8 -> numpy); skip where numpy is absent (the 7 static graph tests above still run)
    from combatant import Combatant
    from trace import run_traced_fight
    fired = set()
    for wa, wb in (('arming', 'arming'), ('spear', 'dagger')):
        for s in range(8):
            A = Combatant('A', weapon=wa); B = Combatant('B', weapon=wb)
            _, ev = run_traced_fight(A, B, seed=s)
            fired |= G.fired_states_from_events(ev)
    for core in ('FightInit', 'EngagementInit', 'Exchange', 'Separation', 'FinalResult'):
        assert core in fired, f"core state {core} never fired in the smoke sweep"


def test_injection_points_reference_defined_states():
    """The WS-1 tradition injection-point bridge stays synced with the graph — every point names a real state."""
    valid = set(G.STATES)
    for k, v in G.INJECTION_POINTS.items():
        assert v['node'] in valid, f"injection point {k} -> undefined state {v['node']}"


def test_injection_points_carry_no_stale_site_string():
    """D12b (I8): the per-point 'site' line-range strings were DROPPED (had already drifted across I2..I7b) —
    pin their absence so a future edit can't silently reintroduce an unread, driftable line reference."""
    for k, v in G.INJECTION_POINTS.items():
        assert 'site' not in v, f"injection point {k} carries a dropped 'site' key"


def test_known_dead_branch_is_documented():
    """The collapse (stamina<=-4) separation reason is empirically dead — assert it's a DECLARED reason (so the
    harness can flag it) rather than silently absent. This pins the finding; a future fix can remove it from
    SEPARATION_REASONS once the guard is demoted/deleted."""
    assert 'collapse' in G.SEPARATION_REASONS


# ── I7b CONTACT AXIS (D8/D9, M-11, 2026-07-03) ───────────────────────────────────────────────────
# designs/audit/2026-07-02-scene-combat-closing-distance-redesign/plan_r1_RATIFIED.md
def test_contact_node_is_real_not_activation():
    """M-11: the Contact state + 'contact' TRACE_KIND are a real BUILD (verified absent pre-I7b: 15 STATES,
    no Contact node, no 'contact' kind) — pins that this stays built."""
    assert 'Contact' in G.STATES
    assert 'contact' in G.TRACE_KINDS
    assert 'contact' in G.STATES['Contact']['emits']
    assert not G.STATES['Contact'].get('terminal')


def test_contact_reachable_from_all_three_precondition_sites():
    """D8: Contact is reachable from Exchange directly (the deep-commit reopen precondition needs neither
    Bind nor Riposte nor a landed hit) as well as from Bind/Riposte/HitLanded (the other two precondition
    sites can co-occur with any of those three outcomes)."""
    for s in ('Exchange', 'Bind', 'Riposte', 'HitLanded'):
        assert 'Contact' in G.STATES[s]['to'], f"{s} -> Contact edge missing"


def test_contact_node_live_trace_fires():
    """A live sweep including a short-reach (dagger) matchup must actually visit Contact — the open-contact
    exemption fires it on essentially every closed beat for that wielder, so this is not a rare branch."""
    pytest.importorskip("numpy")
    from combatant import Combatant
    from trace import run_traced_fight
    fired = set()
    for s in range(20):
        A = Combatant('A', weapon='spear'); B = Combatant('B', weapon='dagger')
        _, ev = run_traced_fight(A, B, seed=s)
        fired |= G.fired_states_from_events(ev)
    assert 'Contact' in fired
