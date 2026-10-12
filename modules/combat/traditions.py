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

# Each tradition: the named-set it expresses (bridge mapping) + the cognitive-mode label. The old 7-dim channel-weight
# vector was REMOVED 2026-06-29 (degenerate top-down tuning) and its vestigial numbers deleted 2026-06-29 (read by
# nothing). Differentiation is bottom-up: the abilities it grants (ability_primitives) + the imposition gate
# familiarity. `mode` is flavour metadata (the governing-analogue label); not read at resolution.
TRADITIONS = {
    'german':   dict(set='Bind Fighter',    mode='tactile'),
    'italian':  dict(set='Thrust Duelist',  mode='temporal-spatial'),
    'spanish':  dict(set='Thrust Duelist',  mode='geometric'),
    'japanese': dict(set='Counter-time',    mode='intentional'),
    'chinese':  dict(set='Burst',           mode='kinetic-rhythmic'),
    'filipino': dict(set='Continuous-flow', mode='kinetic-rhythmic'),
    'english':  dict(set='Counter-time',    mode='biomechanical'),
    'none':     dict(set=None,              mode=None),
}

# Knowledge-of-others: how well a tradition READS an unfamiliar one (the imposition/read edge against a novel style).
FAMILIARITY_DEFAULT = 0.85          # baseline read of any unfamiliar tradition
FAMILIARITY_ADJACENT = 0.93         # adjacent/cross-pollinated traditions
ADJACENT = {                        # pairs that historically exchanged (read each other better)
    frozenset({'german', 'italian'}), frozenset({'italian', 'spanish'}), frozenset({'german', 'english'}),
    frozenset({'italian', 'english'}), frozenset({'chinese', 'japanese'}), frozenset({'chinese', 'filipino'}),
    frozenset({'japanese', 'filipino'}),
}

# ED-PC-0035: PREFERRED / preferred() are GONE. They were the IMPOSITION GATE's data — the node a tradition "fights to
# impose" — and that gate was retired as top-down scripting by Jordan's ED-PC-0023 ruling. They then sat here with ZERO
# live readers while three comments (this module's header, tradition.py's, ability_primitives.eff_cw's) still described
# the gate as a live differentiation mechanism, and the config's own note claimed PREFERRED was "read only when
# IMPOSITION_GATE is on" — false even then, since the retired impose_node read neither. Tradition preference now EMERGES
# from BUILD (skill('bind') + weapon wind affinity + learned abilities + disposition, all live in mode_sigma/bind_sigma);
# a future EMERGENT selection-bias must be derived from those, not restored from a label table.


def familiarity(reader_trad, opponent_trad):
    """How well `reader_trad` reads `opponent_trad`. 1.0 if same or either is 'none' (no tradition to misread)."""
    if reader_trad == opponent_trad:
        return 1.0
    if reader_trad == 'none' or opponent_trad == 'none':
        return 1.0
    if frozenset({reader_trad, opponent_trad}) in ADJACENT:
        return FAMILIARITY_ADJACENT
    return FAMILIARITY_DEFAULT


# `profile(trad)` REMOVED (ED-PC-0042): a bare TRADITIONS.get() wrapper with zero call sites in engine,
# workbench or tests — verified by AST (definition + facade re-export only) as well as by grep. Every live
# consumer reads the TRADITIONS dict directly or goes through familiarity(); a lookup helper that nothing
# looks up is a trap for a future caller who assumes it does more than `.get`.
