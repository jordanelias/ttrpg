"""ability_primitives.py — the ABILITY PRIMITIVES: the atomic, learnable units a tradition is built from.

The atoms half of the tradition split (the traditions DICTIONARY that aggregates them is traditions.py). "Abilities
are basically tradition primitives" (Jordan): just as a weapon is a bundle of physical primitives, a tradition is a
bundle of ability primitives — the named techniques/concepts it teaches (Indes, Winden, mezzo tempo, atajo,
sen-no-sen, true-times…), grounded in the historical-combat-manuals corpus.

CURRENT MODEL (scaffold — the modulator form): an ability is a tradition-learned MODULATOR a fighter EQUIPS
(c.equipped, default empty -> no change -> invariant-safe). Each targets a named LEVER with op '+' (additive) or
'*' (multiplicative). TARGET MODEL (REARCHITECTURE_v1 Phase 4): an ability becomes learned ACCESS (permission to
attempt a graph transition), with the op extended to 'gate' and a phase-slot + prereq; effectiveness then EMERGES
from primitives rather than a hand-set value. This module is where that upgrade lands.

LEVER STATUS: the 7 channel levers + counter_success/counter_select/anti_overcommit are live (eff_cw consumed at
~9 sites). The 'seize' lever is DEAD (its pre-contact consumer was cut 2026-06-05): vorschlag/sen_no_sen do
nothing when equipped — slated for retire-or-reroute (Phase 4 / Jordan's call).
"""

ABILITIES = {
    # German (Liechtenauer; S1/S2)
    'indes':          dict(tradition='german',   grade='S1/S2', lever='counter_success', op='+', value=0.15,
                           desc="Indes / Fühlen — feeling the bind, the simultaneous counter in the same tempo"),
    'vorschlag':      dict(tradition='german',   grade='S1/S2', lever='seize',           op='+', value=4.0,
                           desc="Vorschlag — the first-strike that seizes the Vor [DEAD: 'seize' lever has no consumer since 2026-06-05]"),
    'staerke_schwaeche': dict(tradition='german', grade='S1/S2', lever='leverage',       op='*', value=1.20,
                           desc="Stärke-Schwäche — strong/weak leverage in the bind (channel lever)"),
    # Italian (Fiore -> rapier; S2)
    'mezzo_tempo':    dict(tradition='italian',  grade='S2',    lever='counter_select',  op='*', value=1.40,
                           desc="Mezzo tempo — the half-time counterattack; reaches for the in-tempo counter more readily"),
    'misura':         dict(tradition='italian',  grade='S2',    lever='measure',         op='*', value=1.15,
                           desc="Misura — distance / measure control (channel lever)"),
    # Japanese (koryū; S2)
    'sen_no_sen':     dict(tradition='japanese', grade='S2',    lever='seize',           op='+', value=4.0,
                           desc="Sen-no-sen — pre-emptive seizing as the opponent commits [DEAD: 'seize' lever has no consumer since 2026-06-05]"),
    # English (Silver; S2)
    'true_times':     dict(tradition='english',  grade='S2',    lever='anti_overcommit', op='+', value=0.25,
                           desc="True Times — Silver's true-vs-false times: commitment discipline, fewer over-commits"),
    # Iberian Destreza (S2/S3 — partly reliable; flagged)
    'atajo':          dict(tradition='spanish',  grade='S2/S3', lever='measure',         op='*', value=1.18,
                           desc="Atajo — Destreza blade-constraint / measure off the círculo (channel lever; S2/S3)"),
}


def ability_bonus(c, lever):
    """Sum of ADDITIVE ('+') modulations for `lever` across the fighter's equipped abilities. Default 0.0."""
    tot = 0.0
    for name in getattr(c, 'equipped', ()) or ():
        a = ABILITIES.get(name)
        if a and a['lever'] == lever and a['op'] == '+':
            tot += a['value']
    return tot


def ability_factor(c, lever):
    """Product of MULTIPLICATIVE ('*') modulations for `lever` across the fighter's equipped abilities. Default 1.0."""
    f = 1.0
    for name in getattr(c, 'equipped', ()) or ():
        a = ABILITIES.get(name)
        if a and a['lever'] == lever and a['op'] == '*':
            f *= a['value']
    return f


def eff_cw(c, channel):
    """Effective lever modulator for `channel`. The scalar channel WEIGHTS are removed: only a learned ABILITY hooked
    to that lever (ability_factor) moves this off 1.0. With no such ability — the default — this is exactly 1.0, so
    the channel has no intrinsic effect and traditions differ only via the imposition gate + familiarity. (Name kept
    so call-sites read as the lever they modulate; an authored ability on e.g. 'measure' goes live here.)"""
    return ability_factor(c, channel)
