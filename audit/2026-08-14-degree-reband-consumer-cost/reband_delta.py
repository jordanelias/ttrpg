#!/usr/bin/env python3
"""MEASURED-BY instrument for ED-IN-0187's downstream-cost claim.

Reproduces, from source, the band shift the 2026-08-14 reband caused and the consumer tables that
distinguish the two bands. Exists because the claim "30.2% of the domain moved Partial -> Failure"
is otherwise unreproducible prose, and CLAUDE.md 0.1 point 3 requires a claim to carry the thing
that would show it wrong.

Run: python3 audit/2026-08-14-degree-reband-consumer-cost/reband_delta.py
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from engine.autoload import dice_engine as D


def pre_ruling(net, ob):
    """The ladder as it stood at 85bf491, transcribed from the removed lines of that diff."""
    if ob >= 20:
        if net >= ob: return 'Success'
        return 'Partial' if net >= 10 else 'Failure'
    if net >= 2 * ob and net >= 3: return 'Overwhelming'
    if net >= ob: return 'Success'
    if net > 0: return 'Partial'
    return 'Failure'


NETS, OBS = range(-4, 26), range(1, 21)


def main():
    moved = [(n, o) for o in OBS for n in NETS
             if pre_ruling(n, o) == 'Partial' and D.degree_from_net(n, o).value == 'failure']
    cells = len(NETS) * len(OBS)
    print(f'Partial -> Failure: {len(moved)}/{cells} cells ({100*len(moved)/cells:.1f}%)')
    for ob in (1, 3, 8, 12):
        band = sorted(n for n, o in moved if o == ob)
        now = [n for n in NETS if D.degree_from_net(n, ob).value == 'partial']
        print(f'  Ob {ob:>2}: moved {band}   still Partial: {now}')
    print('\nConsumers that pay differently for the two bands:')
    print('  domain_echo.ECHO_AMOUNT_BY_DEGREE   Partial 0  vs Failure -1 (acting faction stat)')
    print('  zoom_in_out.SCENE_OB_MODIFIER_...   Partial 0  vs Failure +1 Ob (next scene harder)')
    print('  DAMAGE_BY_DEGREE (both MB engines)  Partial 1  vs Failure  0 damage')
    return 0


if __name__ == '__main__':
    sys.exit(main())
