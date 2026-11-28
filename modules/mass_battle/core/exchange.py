"""modules.mass_battle.core.exchange — the Command clamp and derivation, and which men of a body are engaged.
Pure: depends on config + the support falloff + the geometry's abs-to-orig map + duck-typed unit/atom attributes only; imports
nothing from orchestration (no cycle). Re-imported by orchestration via `from modules.mass_battle.core.exchange import *`.

B19.12 (MBA-04 step 4): the combat pool left the melee pair, and with it the per-subunit pool, its per-pair share, the
Command-only base pool and the yield malus: the contact draw (`core/contact_draw.py`) replaces them. Their
routed/broken/disordered tests moved to the draw's vector builder (`contact_draw.fights`: a body with no fighting men contributes
`m = 0`), and a yielding body's malus became the posture `retreat` (`contact_draw.commitment`). `derive_command` and `clamp_command`
stay for whatever still reads Command (morale, formation-hold speed, order-issuing, derive_rout); `derive_command` retires with
27A-5. `_pair_engaged_troops` stays the one owner of "which men of a body are engaged" and feeds the draw's `support_a`."""
from modules.mass_battle.config import *
from modules.mass_battle.troop_types.registry import support_weight
from modules.mass_battle.geometry import cells_to_orig_coords

__all__ = ['derive_command', 'clamp_command', '_pair_engaged_troops', '_pair_troops', 'D_YIELD']


def clamp_command(value):
    """[A3, ED-MB-0067 Part A / ED-MB-0073] SINGLE OWNER of the Command
    1-7 clamp (`FORK:c451bcb:engine/params/factions/stats_1_7_scale.md`) — so `Officer` and the general's own
    `command` share ONE clamp instead of each re-implementing it (§8: never re-implement a rule). Both sides of
    every Command comparison in `build_army` go through this one function — see `build_army`'s own note."""
    return max(1, min(7, int(value)))  # [canonical: FORK:c451bcb:engine/params/factions/stats_1_7_scale.md — Command clamped 1-7]


def derive_command(charisma, cognition):
    """Command DERIVED from Charisma (primary weight) + Cognition (secondary weight).
    [canonical: Jordan canon-structure directive] Command = leadership leverage:
    Charisma primary (inspire/hold the line), Cognition secondary (tactical read).
    Weighted mean on the 1-7 scale, rounded and clamped to 1-7 (derived_stats weighting convention).
    """
    w = CMD_CHA_WEIGHT + CMD_COG_WEIGHT
    val = round((CMD_CHA_WEIGHT * charisma + CMD_COG_WEIGHT * cognition) / w)
    return clamp_command(val)


def _pair_troops(atom, contact_abs_cells):
    """`(front, engaged)` for ONE atom in ONE pair: the troops in its contact cells, and those plus the depth-weighted troops of its
    ranks behind the contact line (`registry.support_weight`, capped at the ranks the troop type's weapon reaches, MB-07), summed in
    the walk's own order (so `_pair_engaged_troops` reads to the bit what it read before B19.12). The one walk of a body's
    `cell_troops` against a contact; `_pair_engaged_troops` is `engaged`, and the contact draw's `support_a` is `engaged / front`.

    Iterates the atom's ACTUAL `cell_troops` directly, not a freshly recomputed CELL_PATTERN_FN[shape](tier): today the only real
    per-cell signal (troop_type, discipline and power are still subunit-uniform)."""
    contact_orig = set(cells_to_orig_coords(atom, set(contact_abs_cells)))
    if not contact_orig:
        return 0.0, 0.0
    front_r = min(r for r, c in contact_orig)
    front = weighted = 0.0
    cell_troops = getattr(atom, 'cell_troops', None) or {}
    _broken = getattr(atom, 'cell_broken', None)
    for pid, troops in cell_troops.items():
        if troops <= 0:
            continue
        # [ED-MB-0041 phase 2] A broken cell stops FIGHTING. This is the one place per-cell troops
        # become emitted combat weight, so excluding them here is the whole of "a section that has
        # given way no longer contributes" -- no other emission path needs to know. The men are still
        # there (cell_troops is untouched, so they can still be killed and still count as casualties);
        # they have simply stopped being a fighting part of the line, which is what a local break IS.
        if _broken is not None and _broken(pid):
            continue
        orig_r, orig_c = pid
        if pid in contact_orig:
            front += troops
            weighted += troops
        elif SUPPORT_STACK_ENABLED and orig_r > front_r:
            depth = orig_r - front_r
            weighted += troops * support_weight(depth, getattr(atom, 'troop_type', None))
    return front, weighted


def _pair_engaged_troops(atom, contact_abs_cells):
    """Troop-weighted engagement magnitude for ONE atom in ONE pair: the actual troops in contact plus depth-weighted support from
    ranks behind (`_pair_troops`' second value). Read by the cascade's truncation counter (`resolve_engagements_cascading`)."""
    return _pair_troops(atom, contact_abs_cells)[1]
