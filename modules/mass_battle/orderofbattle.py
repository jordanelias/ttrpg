"""modules.mass_battle.orderofbattle -- a faction's ORDER OF BATTLE as a typed input, and the builder that turns
it into the multi-subunit `Army` the engine fights with (ED-IN-0306, phase 1).

WHAT THIS IS. `massbattle._weighted_unit` builds every season army as ONE 'infantry' subunit sized by headcount.
An `OrderOfBattle` says what the army actually is: named UNITS (one `UnitRow` each), each of one troop type (spearmen, archers,
light cavalry, ...), one size, one role, and optionally a posture and a fall-back point; plus one STRATEGY for the
whole army. `build_unit` constructs the Army through `armies.build_army`, the engine's one multi-subunit
constructor, so troop-type stats, reach, density, the role -> shape/instruction menu and the UNIT_CAP all come
from their existing owners: nothing is re-implemented here.

WHAT IT DECIDES AND WHAT IT DOES NOT. It decides placement (where on the field each unit starts) and which
fields it hands `build_army`. It resolves nothing: the fight is `run_battle`'s. It reads no `World`: the host
(`engine/season/seam/wrappers/mass_battle.py`) builds the record from season state and hands it on.

THE DEPLOYMENT RULE (ASSUMPTION; medium; Jordan to correct): melee in the front line, centred; ranged and artillery in
a line behind it; mounted units on the two flanks, alternating left and right. A battle line is the common
shape of RTK and Total War deployments and of the engine's own `build_army` default; the rear offset is the front
line's own depth plus one row, so nothing is placed inside another unit. If the army cannot fit that layout on
the field, it degrades to one centred line on the front row rather than raising.

STRATEGY is a named posture policy applied to each class of unit unless the unit sets its own posture
(`STRATEGIES`, below). Three are built.

[canonical: none -- the strategy table and the deployment rule are this module's, marked ASSUMPTION; the troop types,
stats, reach and roles they refer to are `troop_types/registry.py` and `config.py`'s.]
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from modules.mass_battle.armies import DEPLOY_GAP, ENVELOP_WING_GAP, UNIT_CAP, _centered_line_cols, _spec_span, build_army
from modules.mass_battle.config import BATTLEFIELD_SIZE, COMMAND_DEFAULT, ROLE_SPEC, cell_cap_for
from modules.mass_battle.geometry import footprint_for
from modules.mass_battle.hierarchy.units import Order, _INSTRUCTION_STANCE
from modules.mass_battle.troop_types import table as _troops
from modules.mass_battle.troop_types.registry import default_role_for, is_mounted, roles_for, stats_for, unit_type_for

__all__ = ['UnitRow', 'OrderOfBattle', 'STRATEGIES', 'POSTURES', 'TARGETINGS', 'class_of', 'build_unit',
           'validate', 'cells_for', 'place_posts', 'formation_of', 'subformations']

#: Postures a unit may be set to (the engine's stances, `config.STANCE_SPEED_MOD`'s keys; 'retreat' is reachable only through
#: `fall_back_at`, since a unit that STARTS retreating is not a deployment).
POSTURES = ('balanced', 'aggressive', 'hold')

#: Targeting a unit may be told to prefer (`Unit.target_condition`; None is the engine's 'nearest').
TARGETINGS = (None, 'nearest', 'weakest')

#: Strategy -> the posture each CLASS of unit takes unless it sets its own. `class_of` names the classes.
#: ASSUMPTION; medium; Jordan to correct. 'line' is the engine's neutral default; 'advance' presses the melee and the
#: horse; 'defend' holds them and lets the missile troops work. Ranged stay 'balanced' in all three: a held archer
#: is frozen (`STANCE_SPEED_MOD['hold']` is -99) and braced against shock, which is not what holding means for them.
STRATEGIES = {
    'line':    {'melee': 'balanced',   'ranged': 'balanced', 'mounted': 'balanced'},
    'advance': {'melee': 'aggressive', 'ranged': 'balanced', 'mounted': 'aggressive'},
    'defend':  {'melee': 'hold',       'ranged': 'balanced', 'mounted': 'hold'},
}
#: B19.18: an army's strategy names its formation (`formation_of`), so every other formation row of the troop file is a strategy too, with
#: `line`'s postures (the wings' timed release and the refused wing's trigger are standing orders, not a posture of the strategy).
STRATEGIES.update({name: dict(STRATEGIES['line']) for name in _troops.formations() if name not in STRATEGIES})


def formation_of(strategy: str) -> str:
    """The formation row an army's `strategy` names: the strategy itself where it is a row of `references/troops.yaml: formations`, else `line`
    (`advance` and `defend` are postures of the one line)."""
    return strategy if strategy in _troops.formations() else _troops.DEFAULT_FORMATION

# Rows. Side 'A' (the attacker) advances toward -row, side 'B' toward +row (`armies.build_army`'s convention), and a
# footprint extends toward +row from its start row on BOTH sides, so A's front face is its start row and B's is its
# last row. THE TWO FRONT FACES START THE FORMATION'S `opening_rows` APART (`references/troops.yaml: formations.<name>.opening_rows`,
# 3 for `line`, was `_APPROACH_ROWS`), NOT THE ENGINE'S OWN 15-ROW APPROACH: the season runs ONE
# 18-tick engagement (`massbattle._run_and_grade`), not a multi-turn battle, and lines 19 rows apart never closed in
# that time (a levy line took no casualties at all). The single headcount line it replaces started on the same cells --
# a battle already joined -- so this keeps the field a fight and leaves room for the missile troops' opening volley.
# [ASSUMPTION; medium; Jordan to correct: 3 rows is the smallest gap measured to join every melee type in one turn.]
_A_FRONT_ROW = 27   # [canonical: ED-IN-0306 -- a deployment ASSUMPTION of this module, not canon; Jordan to correct]
_SIDE_DIR = {'A': -1, 'B': 1}
_ANCHOR_COL = 25            # [canonical: armies.build_army's anchor_col default, ED-MB-0017] the field's centre column
_MIN_COL, _MAX_COL = 1, BATTLEFIELD_SIZE - 2    # keep a 1-cell margin, as `_centered_line_cols` does

#: The Army-level baseline the units inherit where a troop type sets nothing: the season adapter's own
#: (`massbattle._SEASON_FORCE_POWER`, `_MVP_UNIT_COMMAND`). Power and discipline are duplicated as literals rather than imported
#: (`massbattle` imports THIS module, and a cycle is the worse of the two); command is `config.COMMAND_DEFAULT`, which
#: both read. A test pins them equal.
_UNIT_POWER, _UNIT_COMMAND, _UNIT_DISCIPLINE = 4, COMMAND_DEFAULT, 5  # (command: `config.COMMAND_DEFAULT`, 27A-2) [canonical: sim_mb_06_v9_historical_spec.md -- T3 baseline P4/C4/D5 defaults, as massbattle._SEASON_FORCE_POWER and _MVP_UNIT_COMMAND carry them]


@dataclass(frozen=True)
class UnitRow:
    """One unit of the order of battle: a body of troops of ONE type, with how it fights.

    `troops` is a headcount (the engine sizes the footprint from it). `role` is a `config.ROLE_SPEC` key from the troop
    type's gated menu (`roles_for`); None is a plain Line with no instructions. `posture` None takes the strategy's. `target`
    is `TARGETINGS`. `fall_back_at`, if set, is a fraction in (0, 1) of its own starting strength at which it
    withdraws (an `own_strength` Order setting stance 'retreat'); None never does. [ASSUMPTION; medium; Jordan to
    correct: a "fall-back point" is read as a strength, since the record holds no position and a season field is one
    18-tick engagement; revert: an `enemy_within:` or position trigger, which needs a position on the record.]"""
    name: str
    troop_type: str
    troops: float
    role: Optional[str] = None
    posture: Optional[str] = None
    target: Optional[str] = None
    fall_back_at: Optional[float] = None
    officer: Optional[object] = None          # [27A-3] the unit's officer as a typed record (`CommandRecord`), built by the host; None -> none
    depth: Optional[int] = None               # [B19.17] the unit formation's depth in cells (rows); None -> the troop type's `depth` (`cells_for`)
    width: Optional[int] = None               # [B19.17] its width in cells (files); None -> from the troops, the depth and `deployment.cell_troops`
    post: Optional[str] = None                # [B19.18] the post it stands at in the army's formation (a key of `formations.<name>.posts`); None -> its class's `default_post`


@dataclass(frozen=True)
class OrderOfBattle:
    """An army: its units, in line order, and one strategy for the whole. `drawn` is the host's, not the battle's:
    `((unit name, cohort id, troops), ...)`, the troops each cohort gave each unit (its assigned count scaled by how fit the
    cohort was), so a fight's casualties are written to the people who fought, each cohort by the unit it fed, and not to
    everybody standing nearby (B17.03). The battle never reads it; `massbattle.resolve_field` reads it to cut each cohort."""
    units: Tuple[UnitRow, ...]
    strategy: str = 'line'
    drawn: Tuple[Tuple[str, str, float], ...] = ()
    commander: Optional[object] = None        # [27A-3] the commander as a typed record (`CommandRecord`), built by the host; None -> none
    commander_post: Optional[str] = None      # [27A-3] the name of the unit he rides with; None is the army's rear centre
    formation: str = 'line'                   # [B19.18] a row of `references/troops.yaml: formations`: where each unit starts (`place_posts`); the record's `strategy` names it (`formation_of`)

    @property
    def cohorts(self) -> Tuple[str, ...]:
        """The cohorts the troops were drawn from, each once, in the order `drawn` first names them."""
        return tuple(dict.fromkeys(cohort for _unit, cohort, _troops in self.drawn))


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
    if oob.formation not in _troops.formations():
        raise ValueError(f"unknown formation {oob.formation!r} (known: {sorted(_troops.formations())})")
    if not oob.units:
        raise ValueError("an order of battle needs at least one unit")
    if len(oob.units) > UNIT_CAP:
        raise ValueError(f"{len(oob.units)} units exceeds the cap of {UNIT_CAP}")
    if oob.commander_post is not None and oob.commander_post not in {sf.name for sf in oob.units}:
        raise ValueError(f"commander_post {oob.commander_post!r} names no unit of the order of battle")
    seen = set()
    for sf in oob.units:
        if sf.name in seen:
            raise ValueError(f"duplicate unit name {sf.name!r}")
        seen.add(sf.name)
        if stats_for(sf.troop_type) is None:
            raise ValueError(f"{sf.name!r}: troop type {sf.troop_type!r} has no stat preset")
        if not sf.troops > 0:
            raise ValueError(f"{sf.name!r}: troops must be positive, got {sf.troops!r}")
        if sf.role is not None and sf.role not in roles_for(sf.troop_type):
            raise ValueError(f"{sf.name!r}: role {sf.role!r} is not in {sf.troop_type!r}'s menu {roles_for(sf.troop_type)}")
        if sf.posture is not None and sf.posture not in POSTURES:
            raise ValueError(f"{sf.name!r}: posture {sf.posture!r} not in {POSTURES}")
        if sf.target not in TARGETINGS:
            raise ValueError(f"{sf.name!r}: target {sf.target!r} not in {TARGETINGS}")
        if sf.fall_back_at is not None and not 0.0 < sf.fall_back_at < 1.0:
            raise ValueError(f"{sf.name!r}: fall_back_at must be strictly between 0 and 1, got {sf.fall_back_at!r}")
        if sf.post is not None and sf.post not in _troops.formation(oob.formation)['posts']:
            raise ValueError(f"{sf.name!r}: post {sf.post!r} is not a post of the {oob.formation!r} formation "
                             f"(known: {sorted(_troops.formation(oob.formation)['posts'])})")
        for col in ('depth', 'width'):
            v = getattr(sf, col)
            if v is not None and (isinstance(v, bool) or not isinstance(v, int) or v < 1):
                raise ValueError(f"{sf.name!r}: {col} must be a whole number of at least 1 (cells), got {v!r}")


def cells_for(troop_type: str, troops: float, depth: Optional[int] = None, width: Optional[int] = None,
              arm: Optional[str] = None) -> dict:
    """B19.17: how a body of `troops` of `troop_type` is laid into cells, as the footprint keys of a `build_army` spec or a `Unit`:
    THE ONE FUNCTION `_spec_for` AND BOTH HEADCOUNT CONSTRUCTORS (`massbattle._line_spec`) CALL. A unit formation is a grid, `depth`
    rows by `width` files of cells (`footprint_for`'s explicit arm, which ignores the floor and the cap by design):

        depth = unit's depth or the troop type's `depth`
        width = unit's width or max(1, round(troops / (depth * deployment.cell_troops)))

    `arm` (default `deployment.arm` of the troop file) is `cap`, today's packing and the control: a body that names no depth and no
    width is passed as the densest packing its type allows (`concentration`), exactly as before; or `grid`, which lays every body
    on the grid. A unit that names its own `depth` or `width` is laid on the grid under either arm (the unit's own formation is a
    choice, the arm only the default for a body that makes none)."""
    dep = _troops.deployment()
    if (arm or dep['arm']) == 'cap' and depth is None and width is None:
        return {'concentration': float(cell_cap_for(troop_type))}
    d = depth or _troops.depth_of(troop_type)
    return {'width': width or max(1, round(troops / (d * dep['cell_troops']))), 'depth': d}


def _spec_for(sf: UnitRow, strategy: str) -> dict:
    """The `build_army` spec dict for one unit (placement is added by `_place`)."""
    cls = class_of(sf.troop_type)
    # No role named -> a plain Line with no instruction package, the shape the headcount line has always fought as.
    # The type's first menu entry is NOT a safe default: a levy's menu is the 'any' fallback (Support, Reserve), and a
    # Reserve body does not advance. Roles are chosen on purpose, by the host or the menu. THE ONE RULED EXCEPTION is
    # `build_army`'s (ED-1095, Jordan: mounted archers "shouldn't be closing in on the enemy"): a mounted_archers body
    # with no role stands off as Kite, and naming a shape here would opt it out of that.
    role = sf.role or default_role_for(sf.troop_type)   # [B17.11] the troop file's `default_role` (`Kite` for `mounted_archers`)
    spec = dict(troop_type=sf.troop_type, troops=float(sf.troops),
                **cells_for(sf.troop_type, float(sf.troops), sf.depth, sf.width))
    # POSTURE PRECEDENCE: the unit's own, then the one its role's instructions set (ShieldWall and Hold hold,
    # Push presses -- `Unit.eff_stance` reads them only while the engine stance was never written on purpose), then
    # the strategy's for its class. Always writing the strategy's posture made a role unable to set it.
    role_stance = role is not None and any(k in _INSTRUCTION_STANCE for k in ROLE_SPEC[role]['instructions'])
    if sf.posture is not None:
        spec['stance'] = sf.posture  # D-9: `build_army`'s spec key is the engine attribute `Unit.stance`, which keeps its name (an Order sets it by name, `_ORDER_SAFE_FIELDS`)
    elif not role_stance:
        spec['stance'] = STRATEGIES[strategy][cls]
    if role is not None:
        spec['role'] = role
    else:
        spec['shape'] = 'Line'
    if sf.target is not None:
        spec['target_condition'] = sf.target
    if sf.officer is not None:
        spec['officer_record'] = sf.officer
    if sf.fall_back_at is not None:
        spec['orders'] = [Order(f'own_strength:{sf.fall_back_at}', {'stance': 'retreat'})]
    return spec


def _rows_of(spec: dict) -> int:
    """Depth in rows of a spec's footprint, computed before construction (as `_spec_span` does for columns)."""
    shape = spec['shape'] if 'shape' in spec else ROLE_SPEC[spec['role']]['shape']
    pat = footprint_for(shape, spec['troops'], spec.get('concentration'), spec['troop_type'],
                        width=spec.get('width'), depth=spec.get('depth'))
    rs = [r for r, _c in pat]
    return (max(rs) - min(rs) + 1) if rs else 1


_ACROSS_SIDE = {'left': -1, 'wide_left': -1, 'right': 1, 'wide_right': 1}   # which side of the centre line an `across` term stands on


def _is_centre(post: dict) -> bool:
    return post['across'] == 'centre'


def place_posts(specs: list, posts: list, formation: str, side: str, row: int, anchor_col: int = _ANCHOR_COL) -> dict:
    """B19.18, THE ONE READER OF A FORMATION ROW (`references/troops.yaml: formations`): `{spec index: (row, col)}` for each spec that names no
    `starting_position`, where `posts[i]` is the name of the post spec `i` stands at and `row` is the row of the first line. THE SEASON'S
    `_place` AND THE HARNESS'S `build_envelopment` / `build_refused_flank` BOTH CALL IT: an army deploys by one rule wherever it is built.
    A spec that names a `starting_position` stands where it says, and the posts beside it are laid against where it is, not where the rule
    would have put it. It reads no field and resolves nothing; it does not check that the layout fits (`_place` does, and degrades).

    Each line (`rank_line`) is laid on its own: its units across the centre are centred on `anchor_col` (the whole line, side posts included,
    when the row's `frontage` is `whole`), and its side posts stand outside that, clear of it by the post's `gap` or else the deploy gap
    (`left`, `right`) or the wing gap (`wide_*`), each outward from the one before. A line stands one clear row behind the depth of the line
    in front of it (a line's depth is its centre units'; footprints run toward +row, so A's later lines are at larger rows and B's at smaller);
    a post's `forward` then moves it that many rows toward the enemy (A advances toward -row, B toward +row)."""
    f = _troops.formation(formation)
    frame, whole = f['posts'], f['frontage'] == 'whole'
    adir = _SIDE_DIR[side]
    lines: dict = {}
    for i, name in enumerate(posts):
        lines.setdefault(frame[name]['rank_line'], []).append(i)
    rows, prev = {}, None
    for k in sorted(lines):
        if prev is None:
            rows[k] = row
        else:
            centre = [i for i in lines[k] if _is_centre(frame[posts[i]])] or lines[k]
            pcentre = [i for i in lines[prev] if _is_centre(frame[posts[i]])] or lines[prev]
            rows[k] = (rows[prev] + max(_rows_of(specs[i]) for i in pcentre) + 1 if adir < 0
                       else rows[prev] - 1 - max(_rows_of(specs[i]) for i in centre))
        prev = k
    out, extent = {}, None
    for k in sorted(lines):
        laid = [i for i in lines[k] if whole or _is_centre(frame[posts[i]])]
        cols = dict(zip(laid, _centered_line_cols([specs[i] for i in laid], anchor_col))) if laid else {}
        sited = {}                                    # spec index -> the column it stands at, where it stands across the centre or names its own
        for i in lines[k]:
            post = frame[posts[i]]
            if 'starting_position' in specs[i]:
                sited[i] = specs[i]['starting_position'][1]
            elif _is_centre(post):
                sited[i] = cols[i]
                out[i] = (rows[k] + post.get('forward', 0) * adir, cols[i])
        centred = [i for i in lines[k] if _is_centre(frame[posts[i]])]
        if centred:
            extent = (min(sited[i] + _spec_span(specs[i])[0] for i in centred), max(sited[i] + _spec_span(specs[i])[1] for i in centred))
        lo, hi = extent if extent is not None else (anchor_col, anchor_col)
        edge = {-1: lo, 1: hi}                        # the inner edge of each side's last unit: the next stands outside it
        for i in lines[k]:
            post = frame[posts[i]]
            if _is_centre(post) or 'starting_position' in specs[i]:
                continue
            cmin, cmax = _spec_span(specs[i])
            way = _ACROSS_SIDE[post['across']]
            empty = post['gap'] if 'gap' in post else (DEPLOY_GAP if post['across'] in ('left', 'right') else ENVELOP_WING_GAP - 1)
            if way < 0:
                col = edge[-1] - 1 - empty - cmax
                edge[-1] = col + cmin
            else:
                col = edge[1] + 1 + empty - cmin
                edge[1] = col + cmax
            out[i] = (rows[k] + post.get('forward', 0) * adir, col)
    return out


def _posts_for(classes: list, explicit: list, formation: str) -> list:
    """The post each unit stands at: its own where it names one, else the formation's `default_post` for its class (a list of posts is
    taken in turn by the units of that class that name none). If nothing then stands across the centre of the first line, the units behind
    it step up to it (missile troops with nothing to screen them stand at the front), or, with none behind, every unit does (a horse-only
    army is one centred line of its own)."""
    f = _troops.formation(formation)
    frame, taken = f['posts'], {}
    names = []
    for cls, own in zip(classes, explicit):
        if own is not None:
            names.append(own)
            continue
        given = f['default_post'][cls]
        n = taken.get(cls, 0)
        taken[cls] = n + 1
        names.append(given[n % len(given)] if isinstance(given, list) else given)
    first = next(name for name, p in frame.items() if p['rank_line'] == 0 and _is_centre(p))
    if first not in names:
        behind = [i for i, n in enumerate(names) if frame[n]['rank_line'] > 0]
        for i in (behind or range(len(names))):
            names[i] = first
    return names


def subformations(oob: OrderOfBattle) -> Tuple[Tuple[str, Tuple[str, ...]], ...]:
    """B19.19: `((post, (unit name, ...)), ...)`, a SUBFORMATION per post of the army formation that has a unit, the posts in the order of the
    formation row's `posts`, the units at each in line order. READ over the unit rows (a unit is a row; nothing is stored): each unit's post is
    the one it names, else its class's `default_post`, exactly as `_posts_for` deploys it. Units at one post that name different officers are
    still one subformation. [ASSUMPTION, reversible: D-1 of the lexicon]"""
    if not oob.units:
        return ()
    posts = _posts_for([class_of(u.troop_type) for u in oob.units], [u.post for u in oob.units], oob.formation)
    return tuple((post, tuple(u.name for u, p in zip(oob.units, posts) if p == post))
                 for post in _troops.formation(oob.formation)['posts'] if post in posts)


def _place(specs: list, classes: list, side: str, explicit: Optional[list] = None, formation: str = 'line') -> None:
    """Write `starting_position` into each spec, in place, by the army's formation row (`place_posts`; the rule in the module docstring is the
    `line` row). Leaves the layout one centred line on the first row (`build_army` places the lot) if it does not fit the field.
    `explicit[i]` is the post unit `i` names, or None for its class's default."""
    names = _posts_for(classes, explicit or [None] * len(specs), formation)
    f = _troops.formation(formation)
    frame = f['posts']
    first = [i for i, n in enumerate(names) if frame[n]['rank_line'] == 0 and _is_centre(frame[n])]
    depth = max(_rows_of(specs[i]) for i in first)
    ahead = max([0] + [frame[n].get('forward', 0) for n in names])    # the first face stands where the opening puts it: a post forward of it moves the line back
    if side == 'A':
        row = _A_FRONT_ROW + ahead
    else:
        # B's front face is its LAST row: put the deepest front unit's face `opening_rows` short of A's.
        row = (_A_FRONT_ROW - f['opening_rows'] - 1) - (depth - 1) - ahead
    pos = place_posts(specs, names, formation, side, row)
    for i, (r, c) in pos.items():
        cmin, cmax = _spec_span(specs[i])
        if c + cmin < _MIN_COL or c + cmax > _MAX_COL:
            # Does not fit the layout: degrade to ONE centred line on the front row (`_centered_line_cols` fits or
            # compresses it to the field), keeping the opening distance, rather than raise.
            pos = {i: (row, c) for i, c in enumerate(_centered_line_cols(specs, _ANCHOR_COL))}
            break
    for i, p in pos.items():
        specs[i]['starting_position'] = p


def build_unit(oob: OrderOfBattle, name: str, side: str, *, morale_start: int):
    """The `Army` for `oob` on `side` ('A' attacker, 'B' defender): `armies.build_army` over one spec per
    unit, placed by `_place`. `morale_start` is the side's season morale, applied to every subunit
    (`build_army` gives each its own copy). Army-level power/command/discipline are the season adapter's baseline;
    the TROOP TYPE's own stats override them per subunit (`Unit.of_type`). [ASSUMPTION; medium; Jordan to correct:
    the side's morale is every subunit's start, so a troop type's own morale preset (levy 2, knights 6) does not apply
    -- in the season morale is a fact about the SIDE (stance, loyalty, battle history, `massbattle._morale_start`);
    revert: pass no `morale` here so `Unit.of_type`'s preset applies.]"""
    if side not in _SIDE_DIR:
        raise ValueError(f"side must be 'A' or 'B', got {side!r}")
    validate(oob)
    specs = [_spec_for(sf, oob.strategy) for sf in oob.units]
    classes = [class_of(sf.troop_type) for sf in oob.units]
    _place(specs, classes, side, [sf.post for sf in oob.units], oob.formation)
    army = build_army(specs, name, side, power=_UNIT_POWER, command=_UNIT_COMMAND, discipline=_UNIT_DISCIPLINE,
                      morale=morale_start, morale_start=morale_start,
                      commander=oob.commander, commander_post=oob.commander_post)
    for unit, sf in zip(army.units, oob.units):   # [27A-4, B19.05] the row's name rides on the unit `commander_post` names
        unit.name = sf.name
    return army
