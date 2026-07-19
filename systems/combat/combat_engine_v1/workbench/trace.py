"""Run ONE fight with the engine's trace seam on, capturing the structured event stream.

A single run is n=1 by construction — a point sample, not a probability. The branch probabilities
the narrator/explorer show come from probabilities.py (the local distribution at each node), NOT from
repeating the fight. For win-rates over many fights use the montecarlo path (workbench server), never this."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
import random
import wrapper
import config


def run_traced_fight(A, B, cfg=None, seed=0, max_bouts=12):
    """Returns (result, events). result is -1/0/+1 (A's perspective). events is the ordered trace.
    Restores wrapper._TRACE afterward so concurrent callers are unaffected."""
    cfg = cfg or config.CFG
    events = []
    prev = wrapper._TRACE
    wrapper._TRACE = events.append
    try:
        rng = random.Random(seed)   # stdlib RNG (engine contract post ED-1085)
        result = wrapper.fight(A, B, cfg, rng, max_bouts=max_bouts)
    finally:
        wrapper._TRACE = prev
    return result, events
