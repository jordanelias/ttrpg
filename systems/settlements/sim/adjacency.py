"""
systems/settlements/sim/adjacency.py — Territory adjacency map

Canon source: m1_church_infrastructure.py L276-293; settlement_layer_v30 + valoria_geography
Status: [CANONICAL — Phase 2 implementation 2026-05-17]
"""
from __future__ import annotations

ADJACENCY: dict[str, set[str]] = {
    'T1':  {'T2', 'T5', 'T14', 'T16'},
    'T2':  {'T1', 'T3', 'T9', 'T14'},
    'T3':  {'T2', 'T9', 'T17'},
    'T4':  {'T7', 'T12', 'T14'},
    'T5':  {'T1', 'T6', 'T14'},
    'T6':  {'T5', 'T13', 'T15'},
    'T7':  {'T4', 'T8'},
    'T8':  {'T7', 'T9', 'T10', 'T17'},
    'T9':  {'T2', 'T3', 'T8', 'T14', 'T17'},
    'T10': {'T8', 'T11'},
    'T11': {'T10', 'T12'},
    'T12': {'T4', 'T11', 'T13'},
    'T13': {'T6', 'T12', 'T15'},
    'T14': {'T1', 'T2', 'T4', 'T5', 'T9'},
    'T15': {'T6', 'T13'},
    'T17': {'T3', 'T8', 'T9'},
}
