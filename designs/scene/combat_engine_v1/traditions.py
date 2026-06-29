"""traditions.py — the TRADITIONS DICTIONARY: each tradition as an AGGREGATE of ability primitives + a reading bias.

The data half of the tradition split (the atoms are in ability_primitives.py). Symmetric to the weapon split: a
weapon is a bundle of physical primitives (weapons.py); a tradition is a bundle of ABILITY primitives (the kit it
teaches) plus its preferred-node bias and familiarity profile. A tradition is a COGNITIVE MODE — a way of reading
the same shared physics — NOT a separate rule-set; it biases HOW its fighter reads/selects, never new physics.

Differentiation is BOTTOM-UP only: the learned ABILITIES it grants (ability_primitives.py), the IMPOSITION gate
(the preferred node it fights to impose), and FAMILIARITY (how well it reads an unfamiliar style). The scalar
7-channel weight vector was REMOVED 2026-06-29 (Jordan) — proven a degenerate "who-bought-balance" contest; the
raw numbers below survive only as `set`/`mode`/provenance metadata, read by nothing as weights.
"""

# Each tradition: the named-set it expresses (bridge mapping) + vestigial channel/mode metadata (NOT read as weights).
TRADITIONS = {
    'german':   dict(visual=0.95, tactile=1.35, precommit=1.00, leverage=1.30, tempo=1.10, measure=1.05, balance=1.00,
                     set='Bind Fighter', mode='tactile'),
    'italian':  dict(visual=1.20, tactile=1.00, precommit=1.00, leverage=0.95, tempo=1.30, measure=1.25, balance=1.05,
                     set='Thrust Duelist', mode='temporal-spatial'),
    'spanish':  dict(visual=1.15, tactile=0.95, precommit=1.00, leverage=0.95, tempo=1.05, measure=1.35, balance=1.30,
                     set='Thrust Duelist', mode='geometric'),
    'japanese': dict(visual=1.05, tactile=1.15, precommit=1.35, leverage=1.05, tempo=1.20, measure=1.10, balance=1.10,
                     set='Counter-time', mode='intentional'),
    'chinese':  dict(visual=1.05, tactile=1.20, precommit=1.05, leverage=1.15, tempo=1.05, measure=1.20, balance=1.15,
                     set='Burst', mode='kinetic-rhythmic'),
    'filipino': dict(visual=1.00, tactile=1.25, precommit=1.05, leverage=1.00, tempo=1.15, measure=1.05, balance=1.25,
                     set='Continuous-flow', mode='kinetic-rhythmic'),
    'english':  dict(visual=1.10, tactile=1.05, precommit=1.00, leverage=1.05, tempo=1.15, measure=1.15, balance=1.10,
                     set='Counter-time', mode='biomechanical'),
    'none':     dict(visual=1.00, tactile=1.00, precommit=1.00, leverage=1.00, tempo=1.00, measure=1.00, balance=1.00,
                     set=None, mode=None),
}

# Knowledge-of-others: how well a tradition READS an unfamiliar one (the imposition/read edge against a novel style).
FAMILIARITY_DEFAULT = 0.85          # baseline read of any unfamiliar tradition
FAMILIARITY_ADJACENT = 0.93         # adjacent/cross-pollinated traditions
ADJACENT = {                        # pairs that historically exchanged (read each other better)
    frozenset({'german', 'italian'}), frozenset({'italian', 'spanish'}), frozenset({'german', 'english'}),
    frozenset({'italian', 'english'}), frozenset({'chinese', 'japanese'}), frozenset({'chinese', 'filipino'}),
    frozenset({'japanese', 'filipino'}),
}

# Each tradition's PREFERRED node — the part of the state graph it fights to impose (the imposition gate, decoupled
# from any channel magnitude). 'bind'=German (the crossing); 'counter'=Italian/Japanese/English (refuse the bind);
# 'measure'=Spanish (the círculo); 'burst'=Chinese; 'flow'=Filipino. Read only when cfg['IMPOSITION_GATE'] is on.
PREFERRED = {'german': 'bind', 'italian': 'counter', 'spanish': 'measure', 'japanese': 'counter',
             'english': 'counter', 'chinese': 'burst', 'filipino': 'flow', 'none': None}


def preferred(trad):
    return PREFERRED.get(trad)


def familiarity(reader_trad, opponent_trad):
    """How well `reader_trad` reads `opponent_trad`. 1.0 if same or either is 'none' (no tradition to misread)."""
    if reader_trad == opponent_trad:
        return 1.0
    if reader_trad == 'none' or opponent_trad == 'none':
        return 1.0
    if frozenset({reader_trad, opponent_trad}) in ADJACENT:
        return FAMILIARITY_ADJACENT
    return FAMILIARITY_DEFAULT


def profile(trad):
    return TRADITIONS.get(trad, TRADITIONS['none'])
