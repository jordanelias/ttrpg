"""Run ONE fight with the engine's trace seam on, capturing the structured event stream.

A single run is n=1 by construction — a point sample, not a probability. The branch probabilities
the narrator/explorer show come from probabilities.py (the local distribution at each node), NOT from
repeating the fight. For win-rates over many fights use the montecarlo path (workbench server), never this.

The fight is the entry's (B14.11): the Combatants are read into a `PersonalCombatInput` (`fight_record.py`) and fought by
`modules.combat.fight:fight`, whose `trace` is the event list; nothing here binds `wrapper._TRACE`."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `modules.combat` is a package
sys.path.insert(0, os.path.dirname(__file__))
import random
from modules.combat import wrapper
from modules.combat import fight as entry
import fight_record as FR


def trace_record(rec, cfg=None, seed=0, max_bouts=12, decide=None):
    """Returns (result, events) for the record `rec`, fought through the entry at `seed`. `decide(turn)` takes the turn number."""
    out = entry.fight(rec, random.Random(seed),   # stdlib RNG (engine contract post ED-1085)
                      decide=None if decide is None else (lambda view: decide(view.turn)), cfg=cfg, max_bouts=max_bouts)
    return FR.result_of(out), list(out.trace)


def run_traced_fight(A, B, cfg=None, seed=0, max_bouts=12, **fight_kw):
    """Returns (result, events). result is -1/0/+1 (A's perspective). events is the ordered trace. A and B are Combatants,
    read into a record (`fight_record.party_of_combatant`). `fight_kw` is `terms=` and `decide=` (both ride the record and the
    entry) and `yield_decl=`: a declared Yield names a Combatant by identity and the record has no field for it, so a call that
    passes one is this file's one direct `wrapper.fight` call (`armour_participation.py`, `build_levers.py` and `calibrate_generics.py` still call it on Combatants, outside B14.11's WHERE) (its `trace=` argument; the hook is not touched)."""
    terms = fight_kw.pop('terms', wrapper.LETHAL_TERMS)
    decide = fight_kw.pop('decide', None)
    yield_decl = fight_kw.pop('yield_decl', None)
    if fight_kw:
        raise TypeError(f"run_traced_fight() got unexpected keyword argument(s) {sorted(fight_kw)}")
    if yield_decl is not None:
        events = []
        result = wrapper.fight(A, B, cfg, random.Random(seed), max_bouts=max_bouts, yield_decl=yield_decl, terms=terms,
                               decide=decide, trace=events.append)
        return result, events
    rec = FR.record_of(FR.party_of_combatant(A), FR.party_of_combatant(B), terms=terms)
    return trace_record(rec, cfg=cfg, seed=seed, max_bouts=max_bouts, decide=decide)
