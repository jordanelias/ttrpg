"""modules.mass_battle.orderofbattle -- a faction's ORDER OF BATTLE as a typed input, and the builder that turns
it into the multi-subunit `Unit` the engine fights with (ED-IN-0306, phase 1).

WHAT THIS IS. `massbattle._weighted_unit` builds every season army as ONE 'infantry' subunit sized by headcount.
An `OrderOfBattle` says what the army actually is: named SUBFORMATIONS, each of one troop type (spearmen, archers,
light cavalry, ...), one size, one role, and optionally a stance and a fall-back point; plus one STRATEGY for the
whole army. `build_unit` constructs the Unit through `armies.build_army`, the engine's one multi-subunit
constructor, so troop-type stats, reach, density, the role -> shape/instruction menu and the SUBUNIT_CAP all come
from their existing owners: nothing is re-implemented here.

WHAT IT DECIDES AND WHAT IT DOES NOT. It decides placement (where on the field each subformation starts) and which
fields it hands `build_army`. It resolves nothing: the fight is `run_battle`'s. It reads no `World`: the host
(`engine/season/seam/wrappers/mass_battle.py`) builds the record from season state and hands it on.

THE DEPLOYMENT RULE (ASSUMPTION; medium; Jordan to correct): melee in the front line, centred; ranged and artillery in
a line behind it; mounted subformations on the two flanks, alternating left and right. A battle line is the common
shape of RTK and Total War deployments and of the engine's own `build_army` default; the rear offset is the front
line's own depth plus one row, so nothing is placed inside another subformation. If the army cannot fit that layout on
the field, it degrades to one centred line on the front row rather than raising.

STRATEGY is a named stance policy applied to each class of subformation unless the subformation sets its own stance
(`STRATEGIES`, below). Three are built; the envelopment presets in `systems/mass_battle/sim/engine.py` are the next
ones and are not folded in here.

[canonical: none -- the strategy table and the deployment rule are this module's, marked ASSUMPTION; the troop types,
stats, reach and roles they refer to are `troop_types/registry.py` and `config.py`'s.]
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from modules.mass_battle.armies import DEPLOY_GAP, SUBUNIT_CAP, _centered_line_cols, _spec_span, build_army
from modules.mass_battle.config import BATTLEFIELD_SIZE, ROLE_SPEC, cell_cap_for
from modules.mass_battle.geometry import footprint_for
from modules.mass_battle.hierarchy.units import Order, _INSTRUCTION_STANCE
from modules.mass_battle.troop_types.registry import is_mounted, roles_for, stats_for, unit_type_for

__all__ = ['Subformation', 'OrderOfBattle', 'STRATEGIES', 'STANCES', 'TARGETINGS', 'class_of', 'build_unit',
           'validate']

#: Stances a subformation may be set to (`config.STANCE_SPEED_MOD`'s keys; 'retreat' is reachable only through
#: `fall_back_at`, since a subformation that STARTS retreating is not a deployment).
STANCES = ('balanced', 'aggressive', 'hold')

#: Targeting a subformation may be told to prefer (`Subunit.target_condition`; None is the engine's 'nearest').
TARGETINGS = (None, 'nearest', 'weakest')

#: Strategy -> the stance each CLASS of subformation takes unless it sets its own. `class_of` names the classes.
#: ASSUMPTION; medium; Jordan to correct. 'line' is the engine's neutral default; 'advance' presses the melee and the
#: horse; 'defend' holds them and lets the missile troops work. Ranged stay 'balanced' in all three: a held archer
#: is frozen (`STANCE_SPEED_MOD['hold']` is -99) and braced against shock, which is not what holding means for them.
STRATEGIES = {
    'line':    {'melee': 'balanced',   'ranged': 'balanced', 'mounted': 'balanced'},
    'advance': {'melee': 'aggressive', 'ranged': 'balanced', 'mounted': 'aggressive'},
    'defend':  {'melee': 'hold',       'ranged': 'balanced', 'mounted': 'hold'},
}

# Rows. Side 'A' (the attacker) advances toward -row, side 'B' toward +row (`armies.build_army`'s convention), and a
# footprint extends toward +row from its start row on BOTH sides, so A's front face is its start row and B's is its
# last row. THE TWO FRONT FACES START `_APPROACH_ROWS` APART, NOT THE ENGINE'S OWN 15-ROW APPROACH: the season runs ONE
# 18-tick engagement (`massbattle._run_and_grade`), not a multi-turn battle, and lines 19 rows apart never closed in
# that time (a levy line took no casualties at all). The single headcount line it replaces started on the same cells --
# a battle already joined -- so this keeps the field a fight and leaves room for the missile troops' opening volley.
# [ASSUMPTION; medium; Jordan to correct: 3 rows is the smallest gap measured to join every melee type in one turn.]
_A_FRONT_ROW = 27   # [canonical: ED-IN-0306 -- a deployment ASSUMPTION of this module, not canon; Jordan to correct]
_APPROACH_ROWS = 3  # [canonical: ED-IN-0306 -- an ASSUMPTION, not canon: the smallest gap measured to join every melee type in one turn]
_SIDE_DIR = {'A': -1, 'B': 1}
_ANCHOR_COL = 25            # [canonical: armies.build_army's anchor_col default, ED-MB-0017] the field's centre column
_MIN_COL, _MAX_COL = 1, BATTLEFIELD_SIZE - 2    # keep a 1-cell margin, as `_centered_line_cols` does

#: The Unit-level baseline the subformations inherit where a troop type sets nothing: the season adapter's own
#: (`massbattle._SEASON_FORCE_POWER`, `_MVP_UNIT_COMMAND`). Duplicated as three literals rather than imported:
#: `massbattle` imports THIS module, and a cycle is the worse of the two. A test pins them equal.
_UNIT_POWER, _UNIT_COMMAND, _UNIT_DISCIPLINE = 4, 4, 5  # [canonical: sim_mb_06_v9_historical_spec.md -- T3 baseline P4/C4/D5 defaults, as massbattle._SEASON_FORCE_POWER and _MVP_UNIT_COMMAND carry them]


@dataclass(frozen=True)
class Subformation:
    """One body of troops of ONE type, with how it fights.

    `troops` is a headcount (the engine sizes the footprint from it). `role` is a `config.ROLE_SPEC` key from the troop
    type's gated menu (`roles_for`); None is a plain Line with no instructions. `stance` None takes the strategy's. `target`
    is `TARGETINGS`. `fall_back_at`, if set, is a fraction in (0, 1) of its own starting strength at which it
    withdraws (an `own_strength` Order setting stance 'retreat'); None never does. [ASSUMPTION; medium; Jordan to
    correct: a "fall-back point" is read as a strength, since the record holds no position and a season field is one
    18-tick engagement; revert: an `enemy_within:` or position trigger, which needs a position on the record.]"""
    name: str
    troop_type: str
    troops: float
    role: Optional[str] = None
    stance: Optional[str] = None
    target: Optional[str] = None
    fall_back_at: Optional[float] = None


@dataclass(frozen=True)
class OrderOfBattle:
    """An army: its subformations, in line order, and one strategy for the whole. `drawn_from` is the host's, not the
    battle's: the ids of the cohorts the troops were drawn from, so the host writes a fight's casualties to the people
    who fought and not to everybody standing nearby. The battle never reads it."""
    subformations: Tuple[Subformation, ...]
    strategy: str = 'line'
    drawn_from: Tuple[str, ...] = ()


def class_of(troop_type: str) -> str:
    """'mounted' | 'ranged' | 'melee' -- how deployment and strategy treat a troop type. Derived from the registry
    (`is_mounted`, and the assigned weapon's reach via `unit_type_for`), never listed here."""
    if is_mounted(troop_type):
        return 'mounted'
    return 'ranged' if unit_type_for(troop_type) == 'ranged' else 'melee'


def validate(oob: OrderOfBattle) -> None:
    """Refuse an order of battle the engine could not build, loudly and at the boundary. Raises ValueError."""
    if oob.strategy not in STRATEGIES:
        raise ValueError(f"unknown strategy {oob.strategy!r} (known: {sorted(STRATEGIES)})")
    if not oob.subformations:
        raise ValueError("an order of battle needs at least one subformation")
    if len(oob.subformations) > SUBUNIT_CAP:
        raise ValueError(f"{len(oob.subformations)} subformations exceeds the cap of {SUBUNIT_CAP}")
    seen = set()
    for sf in oob.subformations:
        if sf.name in seen:
            raise ValueError(f"duplicate subformation name {sf.name!r}")
        seen.add(sf.name)
        if stats_for(sf.troop_type) is None:
            raise ValueError(f"{sf.name!r}: troop type {sf.troop_type!r} has no stat preset")
        if not sf.troops > 0:
            raise ValueError(f"{sf.name!r}: troops must be positive, got {sf.troops!r}")
        if sf.role is not None and sf.role not in roles_for(sf.troop_type):
            raise ValueError(f"{sf.name!r}: role {sf.role!r} is not in {sf.troop_type!r}'s menu {roles_for(sf.troop_type)}")
        if sf.stance is not None and sf.stance not in STANCES:
            raise ValueError(f"{sf.name!r}: stance {sf.stance!r} not in {STANCES}")
        if sf.target not in TARGETINGS:
            raise ValueError(f"{sf.name!r}: target {sf.target!r} not in {TARGETINGS}")
        if sf.fall_back_at is not None and not 0.0 < sf.fall_back_at < 1.0:
            raise ValueError(f"{sf.name!r}: fall_back_at must be strictly between 0 and 1, got {sf.fall_back_at!r}")


def _spec_for(sf: Subformation, strategy: str) -> dict:
    """The `build_army` spec dict for one subformation (placement is added by `_place`)."""
    cls = class_of(sf.troop_type)
    # No role named -> a plain Line with no instruction package, the shape the headcount line has always fought as.
    # The type's first menu entry is NOT a safe default: a levy's menu is the 'any' fallback (Support, Reserve), and a
    # Reserve body does not advance. Roles are chosen on purpose, by the host or the menu. THE ONE RULED EXCEPTION is
    # `build_army`'s (ED-1095, Jordan: mounted archers "shouldn't be closing in on the enemy"): a mounted_archers body
    # with no role stands off as Kite, and naming a shape here would opt it out of that.
    role = sf.role or ('Kite' if sf.troop_type == 'mounted_archers' else None)
    spec = dict(troop_type=sf.troop_type, troops=float(sf.troops),
                concentration=float(cell_cap_for(sf.troop_type)))
    # STANCE PRECEDENCE: the subformation's own, then the one its role's instructions set (ShieldWall and Hold hold,
    # Push presses -- `Subunit.eff_stance` reads them only while the stance was never written on purpose), then the
    # strategy's for its class. Always writing the strategy's stance made a role unable to set it.
    role_stance = role is not None and any(k in _INSTRUCTION_STANCE for k in ROLE_SPEC[role]['instructions'])
    if sf.stance is not None:
        spec['stance'] = sf.stance
    elif not role_stance:
        spec['stance'] = STRATEGIES[strategy][cls]
    if role is not None:
        spec['role'] = role
    else:
        spec['shape'] = 'Line'
    if sf.target is not None:
        spec['target_condition'] = sf.target
    if sf.fall_back_at is not None:
        spec['orders'] = [Order(f'own_strength:{sf.fall_back_at}', {'stance': 'retreat'})]
    return spec


def _rows_of(spec: dict) -> int:
    """Depth in rows of a spec's footprint, computed before construction (as `_spec_span` does for columns)."""
    shape = spec['shape'] if 'shape' in spec else ROLE_SPEC[spec['role']]['shape']
    pat = footprint_for(shape, spec['troops'], spec['concentration'], spec['troop_type'])
    rs = [r for r, _c in pat]
    return (max(rs) - min(rs) + 1) if rs else 1


def _place(specs: list, classes: list, side: str) -> None:
    """Write `starting_position` into each spec, in place, by the deployment rule in the module docstring. Leaves a
    spec without one (so `build_army` centres the lot) if the layout does not fit the field."""
    front = [i for i, c in enumerate(classes) if c == 'melee']
    rear = [i for i, c in enumerate(classes) if c == 'ranged']
    flank = [i for i, c in enumerate(classes) if c == 'mounted']
    if not front and not rear:                       # a horse-only army: one centred line of its own
        front, flank = flank, []
    elif not front:                                  # missile troops with nothing to screen them: they stand at the front
        front, rear = rear, []
    depth = max(_rows_of(specs[i]) for i in front)
    rear_depth = max((_rows_of(specs[i]) for i in rear), default=0)
    if side == 'A':
        row = _A_FRONT_ROW
        rear_row = row + depth + 1                    # footprints run toward +row: the rear line starts past the front's last row
    else:
        # B's front face is its LAST row: put the deepest front subformation's face `_APPROACH_ROWS` short of A's.
        row = (_A_FRONT_ROW - _APPROACH_ROWS - 1) - (depth - 1)
        rear_row = row - 1 - rear_depth               # and its rear line ends one clear row before the front's first
    pos = {}
    cols = _centered_line_cols([specs[i] for i in front], _ANCHOR_COL)
    for i, c in zip(front, cols):
        pos[i] = (row, c)
    lo = min(c + _spec_span(specs[i])[0] for i, c in zip(front, cols))
    hi = max(c + _spec_span(specs[i])[1] for i, c in zip(front, cols))
    if rear:
        for i, c in zip(rear, _centered_line_cols([specs[i] for i in rear], _ANCHOR_COL)):
            pos[i] = (rear_row, c)
    left_edge, right_edge = lo - DEPLOY_GAP, hi + DEPLOY_GAP
    for n, i in enumerate(flank):
        cmin, cmax = _spec_span(specs[i])
        if n % 2 == 0:                                # even: left of the line, abutting its edge outward
            col = left_edge - cmax - 1
            left_edge = col + cmin - DEPLOY_GAP
        else:
            col = right_edge - cmin + 1
            right_edge = col + cmax + DEPLOY_GAP
        pos[i] = (row, col)
    for i, (r, c) in pos.items():
        cmin, cmax = _spec_span(specs[i])
        if c + cmin < _MIN_COL or c + cmax > _MAX_COL:
            # Does not fit the layout: degrade to ONE centred line on the front row (`_centered_line_cols` fits or
            # compresses it to the field), keeping the approach rule, rather than raise.
            pos = {i: (row, c) for i, c in enumerate(_centered_line_cols(specs, _ANCHOR_COL))}
            break
    for i, p in pos.items():
        specs[i]['starting_position'] = p


def build_unit(oob: OrderOfBattle, name: str, side: str, *, morale_start: int):
    """The `Unit` for `oob` on `side` ('A' attacker, 'B' defender): `armies.build_army` over one spec per
    subformation, placed by `_place`. `morale_start` is the side's season morale, applied to every subunit
    (`build_army` gives each its own copy). Unit-level power/command/discipline are the season adapter's baseline;
    the TROOP TYPE's own stats override them per subunit (`Subunit.of_type`). [ASSUMPTION; medium; Jordan to correct:
    the side's morale is every subunit's start, so a troop type's own morale preset (levy 2, knights 6) does not apply
    -- in the season morale is a fact about the SIDE (stance, loyalty, battle history, `massbattle._morale_start`);
    revert: pass no `morale` here so `Subunit.of_type`'s preset applies.]"""
    if side not in _SIDE_DIR:
        raise ValueError(f"side must be 'A' or 'B', got {side!r}")
    validate(oob)
    specs = [_spec_for(sf, oob.strategy) for sf in oob.subformations]
    classes = [class_of(sf.troop_type) for sf in oob.subformations]
    _place(specs, classes, side)
    return build_army(specs, name, side, power=_UNIT_POWER, command=_UNIT_COMMAND, discipline=_UNIT_DISCIPLINE,
                      morale=morale_start, morale_start=morale_start)
