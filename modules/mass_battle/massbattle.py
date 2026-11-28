"""Season-facing adapter: `resolve_field`, the one battle path the season reaches, over `run_battle`.

`run_battle(unit_a, unit_b, max_ticks=18)` takes constructed Armies; the season's edge is strategic. `resolve_field`
builds each side (from an order of battle when either side carries one, `_oob_unit`; one unit per commanding person
when `field_units` is `'person'`, `_person_unit`; else one Line unit, `_weighted_unit`), sizes every headcount side by
`under_arms_cap(weight)`, takes each side's morale-start from season state (`_morale_start`) and the terrain from the
target's territory and garrison (`terrain_row_for_territory`), fights it in `_run_and_grade`, and `_grade`s the finished
battle into a frozen `FieldOutcome`: the two survivor shares, each side's `routed` / `conceded` flags, the parts of
each side and the part that broke first.
"""
from __future__ import annotations

import math
from dataclasses import asdict

from engine.season.queries.inputs import FieldOutcome, PartOutcome, SideOutcome
from modules.mass_battle import rngsource
from modules.mass_battle import config as _config
from modules.mass_battle.config import (CELL_CAP, MAX_TROOPS_PER_UNIT, MIN_ARMY_TROOPS, MIN_UNITS_PER_ARMY,
                                        ROLE_SPEC)
from modules.mass_battle.armies import UNIT_CAP
from modules.mass_battle.hierarchy.units import Order, Unit, Army, unit_conceded
from modules.mass_battle.orchestration import run_battle
from modules.mass_battle.orderofbattle import (OrderOfBattle, UnitRow, _SIDE_DIR, _place, class_of,
                                               build_unit as _build_oob_unit)
from modules.mass_battle.troop_types.recruitment import under_arms_cap
from modules.mass_battle.terrain import (FOREST_BROKEN, RIVER_CROSSING, RIVER_CROSSING_OFF_D,
                                             SPEED_TIERS, UPHILL, UPHILL_ATTACKER_OFF_D,
                                             UPHILL_DEFENDER_DEF_D, WALLS, WALLS_DEFENDER_DR,
                                             river_crossed, terrain_row_for_territory)

#: [d.1, ED-MB-0068] Canon's Morale ladder, the range a morale-start must land in:
#: `mass_battle_v30.md:230-231` states it directly ("Morale (1-7)"). The floor is 1, not 0: rout fires at
#: morale <= 0, so a side cannot START already routed -- this implementation's own reading, Jordan-vetoable.
_MORALE_FLOOR = 1  # [JUSTIFIED: mass_battle_v30.md:230-231 states canon's Morale range directly ("Morale (1-7)") — this is the direct citation, not an inference from the separate in-battle erosion floor at :254]
_MORALE_CEIL = 7  # [JUSTIFIED: Morale's canon ceiling, mass_battle_v30.md:230-231, "Morale (1-7)"]

#: The morale-start of a side whose members' stance toward their own faction is zero -- no field lost,
#: nothing written. It is the flat value (`morale=5`) every unit started at before d.1: the control arm.
#: ⚠ Not the shipped world: with `loyalty_toward_creed` True, `boot/realm.py` seeds each member's loyalty row
#: on the creed id `_side_stance` reads as morale (`H-256`; `_morale_start`).
_MORALE_START_BASE = 5  # [canonical: inherited default — the pre-port adapter's flat morale-start, carried by _faction_to_unit until d.1 and by _weighted_unit since; see GAP above]


def _round_half_up(x):
    """Round half UP (toward +inf), not Python's builtin `round()` (round-half-to-even / banker's
    rounding). Its input is `_MORALE_START_BASE` plus a side's mean stance, which can be negative;
    every value below 0.5 then clamps to `_MORALE_FLOOR` in `_morale_start`, so how a NEGATIVE half
    rounds never reaches a result, and half-up and half-away-from-zero agree on every input that does.

    WHY THIS EXISTS, NOT bare `round()`: a side's mean stance lands on an exact .5 in ordinary play --
    half the side lost a field at `field_morale_weight` 1 and half did not -- and `round()` at those
    boundaries is asymmetric in a way that has nothing to do with game state: `round(4.5) == 4` but
    `round(3.5) == 4` too, so one loss across half a side would cost a point of morale at one level
    and nothing at the next. `_round_half_up` treats every .5 boundary the same way."""
    return math.floor(x + 0.5)


def _morale_start(stance, loyalty=0.0, gain=0):
    """A side's starting morale from its members' mean stance toward their own faction (`ED-MB-0067`:
    *faction state sets the morale baseline*).

    THE SOURCE, AND WHY IT IS THIS ONE. The season has no faction stat vector, by architecture
    (`04_CODE_ARCHITECTURE.md`, the faction view's list: *"NEVER: a member of `World` · a field of its own · ..."*), so faction state
    is what members hold toward the faction. Jordan's M4 ruling on a lost field (`ED-IN-0279` clause
    (b): *"casualties only, decrease in morale, and a grudge token"*) is already built as a stance row
    on each loser, `(own faction, -1.0, field_morale_weight)` (`loop/effects_combat.py::_eff_march`):
    that row IS the season's morale. The provider sums it through `queries.person_q.stance_toward`, the one
    reader of a stance row, and hands each side's weight-mean here.

    THE MAPPING, AND THE ONE THING IT ASSUMES. One stance unit toward one's own faction is one point
    of morale, added to `_MORALE_START_BASE` and clamped to canon's ladder. That identity is the
    assumption; it adds no knob, because the magnitude is already `field_morale_weight`'s (`H-148`,
    swept 0/1/3): `_eff_march` writes its row on a faction id, and `boot/realm.py`'s build-time loyalty rows land
    on the same id when `loyalty_toward_creed` is True (`H-256`), so a scale factor here would only multiply
    that weight. At weight 0 a lost field writes a zero row and this returns the base -- the control.
    ONE EXCEPTION (`H-151`): in a SAME-FACTION march winner and loser are one faction, so each loser also
    carries the grudge row `(faction, -1.0, field_grudge_weight)` and `stance_toward` sums both: the next
    morale-start is `5 - (morale_w + grudge_w)` (3 at the defaults 1/1), and at weight 0 the grudge still
    moves it. The control above holds for a cross-faction field only.

    THE BUILD-TIME LOYALTY ROW, BEHIND A GAIN (MB-03, `ED-MB-0078`'s superseding row, option (b)).
    `loyalty` is the side's weight-mean stance toward its faction creed's UTTERER -- the row
    `data/cast.py::stance_from_loyalty` seeds at build, `-5..+5` -- and it is added at `gain`, the
    season's `field_morale_loyalty_gain` fixture. It is a SECOND TERM, not merged into `stance`: with
    `loyalty_toward_creed` False the loyalty row names the faction's LEADER, a person, and the morale row
    names the faction, so the host reads and hands on the two referents apart; at the shipped True the row
    lands on the faction id and the `stance` term reads it instead (`H-256`;
    `seam/wrappers/mass_battle.py::_creed_referent`). Only their sum on the ladder is shared. AT `gain` 0
    THE TERM IS ZERO and the result is the shipped option (a), battle history only, exactly (the
    control, swept 0 / 0.4 / 1; `data/fixtures.py` says how each arm is derived). At 0.4 a side with
    loyalty >= 3.75 already reaches the ceiling, and the 1:1 arm saturates most creed-holding
    factions at the realm `boot/realm.py` builds (the row's own finding, with the per-side starts pinned in
    `tests/valoria/test_mass_battle_d1_morale_baseline.py`), which is why the magnitude is the gain's
    and is swept rather than chosen here."""
    return max(_MORALE_FLOOR, min(_MORALE_CEIL, _round_half_up(
        _MORALE_START_BASE + float(stance) + float(gain) * float(loyalty))))


#: [canonical: mass_battle_integration_v30.md §4.10 sub-step 3 — the strategic entry point. ⚠ THE
#:  VALUES BELOW ARE NOT CANON AND THIS COMMENT DOES NOT CLAIM THEY ARE. They are the pre-port
#:  adapter's minimum-viable defaults, carried over FIELD-FOR-FIELD so the engine swap is a
#:  single-variable experiment, and the [GAP] on both this module's construction paths is the
#:  honest status: no canonical spec exists for army -> Army construction of ANY kind. The
#:  fabrication gate is right to ask; the answer is "inherited, with a recorded gap", not
#:  "derived".] SHARED, until `29b` deleted `_faction_to_unit`, BY THAT FUNCTION AND `_weighted_unit` (§8:
#: one owner for the MVP shape); `_weighted_unit` is now the only user. `concentration` is deliberately
#: NOT here -- it is continuous-mode-only (`_weighted_unit` sets it; the deleted tier-sized Unit
#: did not).
_MVP_SUBUNIT_SHAPE = dict(
    shape='Line',
    troop_type='infantry',
    tier=2,                          # [canonical: inherited default — 200 troops, see GAP above]
    stance='balanced',
    unit_type='melee',
)

#: SAME SHARING, FOR THE UNIT SIDE. `power`/`morale`/`morale_start` are NOT here: they are set by
#: `_weighted_unit` itself (morale from `_morale_start`, since plan position `20-iv`).
_MVP_UNIT_COMMAND = dict(
    command=4,                       # [canonical: inherited default — see GAP above]
    discipline=5,                    # [canonical: inherited default — see GAP above]
    discipline_start=5,              # [canonical: inherited default — see GAP above]
)


#: A season `Person` carries no troop-density signal at all -- `power` is an Army-level QUALITY
#: stat (baseline for a subunit with no per-subunit override; `eff_power`'s own fallback, cited
#: there as "[canonical: sim_mb_06_v9_historical_spec.md -- P4 tier baseline default]"), not
#: something army headcount should feed. Re-used here rather than derived from weight -- headcount
#: is a SIZE fact (below), and conflating it with quality would let a Crown-sized force out-CLASS a
#: Guild-sized one on quality alone.
_SEASON_FORCE_POWER = 4  # [canonical: sim_mb_06_v9_historical_spec.md — P4 tier baseline default, eff_power's own fallback]

#: B17.01: THE ONE SCALE. A headcount side's troops are `under_arms_cap(weight)` (`troop_types/recruitment.py`), the
#: most the side's weight could put under arms and the size `_oob_unit` already gives a headcount side that meets an
#: order of battle; the `troops_per_weight` fixture is gone (`hole_register.yaml` H-250, closed). `_SEASON_FORCE_POWER`
#: is a quality stat and is not scaled.
_MIN_TROOPS = 1.0  # floor only -- `Army.total_troops() == 0` divides by zero deep in
                   # `orchestration.resolve_engagements`; this is the smallest value that avoids
                   # that crash, not a claim about what a minimal army is.


def _refusal(army_a, army_b):
    """B17.04: THE TWO SHAPES THE CELL ENGINE CANNOT HOLD, as a typed refusal beside the typed outcome, or `None` for a field it can.
    A dict on `PARTY-GAP`'s shape (`status`, `why`), which `seam/wrappers/mass_battle.py::resolve` hands on and `seam/contest.py::
    REFUSAL_STATUSES` reads as the game's refusal. Read off the Armies as built, so the headcount arms and an order of battle are one
    rule. `SCALE-GAP`: a unit past `config.MAX_TROOPS_PER_UNIT`, the module's stated ceiling, or an army of more than `armies.UNIT_CAP` units. `PARTY-GAP`: BOTH sides are nobody, every
    unit of each at or below `_MIN_TROOPS`, the crash floor, which is a floor-sized phantom and not a block (a field of nobody
    against nobody, or one man a side, is the host's no-party branch, not a battle that the attacker `loses`). One side of nobody
    against a real side is fought as it was."""
    sizes = [[u._start_troops for u in army.units] for army in (army_a, army_b)]
    big = max(max(side) for side in sizes)
    if max(len(army.units) for army in (army_a, army_b)) > UNIT_CAP:
        return dict(status="SCALE-GAP", why=f"an army of more than {UNIT_CAP} units is past the module's ceiling "
                    f"(armies.UNIT_CAP)")
    if big > MAX_TROOPS_PER_UNIT:
        return dict(status="SCALE-GAP", why=f"a unit of {big:g} troops is past the module's ceiling of "
                    f"{MAX_TROOPS_PER_UNIT} (config.MAX_TROOPS_PER_UNIT)")
    if all(n <= _MIN_TROOPS for side in sizes for n in side):
        return dict(status="PARTY-GAP", why="a field battle needs a block of troops on a side; both sides are nobody "
                    "or one man (the crash floor)")
    return None


#: CP-T04-02 (`H-361`): THE STANDING ORDER'S VOCABULARY, owned HERE and read by the season through
#: `tools/export_battle_orders.py` -> `engine/engine_params/battle_orders.json` (`engine/substrate/battle_orders.py`),
#: never from a second list. `ORDER_ROLES` is `config.ROLE_SPEC`'s names, the whole set: a standing order is the
#: commander's, so it is NOT gated by `registry.role_allowed` for the line's stand-in troop type ('infantry', whose
#: menu is Hold/Push/ShieldWall and moves a field by under 3 points, `H-361`). [ASSUMPTION; medium; Jordan to correct;
#: revert: gate `role` on `registry.role_allowed` for the stand-in troop type in `_role_fields`.]
#: `ORDER_RETREAT_AT` is the closed set of the order's second key, `none` or the share of its starting strength at
#: which a subunit of the side falls back (`_retreat_orders`; CP-T04-03).
ORDER_ROLES = tuple(ROLE_SPEC)
ORDER_RETREAT_AT = ('none', '0.5', '0.25')

#: One line of text per member of `ORDER_ROLES` and `ORDER_RETREAT_AT`, for the client to show a named order
#: (`tools/export_battle_orders.py` refuses a member with none and a line for a non-member).
#: [ASSUMPTION: drafted wording, listed for Jordan's correction (B34.07, D-19); the text sits beside the tuples it describes.]
ORDER_ROLE_TEXT = {
    'ShieldWall': "Close shields in a line, brace against shock and hold the ground.",
    'Hold': "Stand the line and do not give ground.",
    'Anvil': "Brace and take the blow so that another body can strike.",
    'Push': "Press forward in an aggressive line.",
    'Skirmish': "Fight in open order, with gaps in the line.",
    'Screen': "Cover the front of the main body.",
    'Pursue': "Run down a broken enemy.",
    'Shock': "Strike in an arrowhead and charge.",
    'Flanker': "Go around the enemy's flank and envelop it.",
    'Feint': "Show weakness to lure the enemy forward.",
    'VolleyLine': "Stand in a line and shoot volleys.",
    'Harass': "Harry the enemy in loose order from a distance.",
    'Kite': "Shoot, then keep out of the enemy's reach.",
    'Support': "Stay behind the line, holding strength to commit where it is needed.",
    'Reserve': "Hold back uncommitted until called.",
}
ORDER_RETREAT_AT_TEXT = {
    'none': "Never fall back: stand to the end.",
    '0.5': "Fall back once the side is down to half its starting strength.",
    '0.25': "Fall back once the side is down to a quarter of its starting strength.",
}


def _role_fields(role):
    """CP-T04-02: the `Unit` fields a standing order's `role` sets, from `config.ROLE_SPEC` (shape and instruction
    package, as `armies.build_army` takes them), at CONSTRUCTION -- the footprint is generated from the shape, so a
    shape written afterwards would change nothing. `None` is `{}`: the subunit exactly as it was. A role outside
    `ROLE_SPEC` is refused here, naming the set."""
    if role is None:
        return {}
    if role not in ROLE_SPEC:
        raise ValueError(f"order role {role!r} is not one of {ORDER_ROLES}")
    spec = ROLE_SPEC[role]
    return dict(shape=spec['shape'], role=role, instructions=spec['instructions'])


def _retreat_orders(retreat_at):
    """CP-T04-03: a standing order's `retreat_at` as the Orders each of the side's units carries -- one
    `own_strength:FRAC` Order whose action is the `retreat` stance (the primitive `orderofbattle`'s `fall_back_at` writes,
    `hierarchy/units.py::Order`) AND the order's own mark `conceded` (which `fall_back_at` and a DG-2 withdrawal do not set):
    once THIS subunit is down to FRAC of its starting troops it turns and gives ground. A
    subunit retreats on its OWN strength, not the side's, and `unit_conceded` is what makes a side whose every subunit has
    retreated or routed give up the field. `None` and `'none'` are no order (`()`, the subunit exactly as it was); a
    value outside `ORDER_RETREAT_AT` is refused here, naming the set."""
    if retreat_at is None or retreat_at == 'none':
        return ()
    if retreat_at not in ORDER_RETREAT_AT:
        raise ValueError(f"order retreat_at {retreat_at!r} is not one of {ORDER_RETREAT_AT}")
    return (Order(f'own_strength:{float(retreat_at)}', {'stance': 'retreat', 'conceded': True}),)


def _line_spec(role, troops):
    """The one headcount line's spec, as `orderofbattle._place` reads it: the MVP shape with the standing order's
    `role` fields, its troops and the densest packing (`config.CELL_CAP`), no position yet."""
    return {**_MVP_SUBUNIT_SHAPE, **_role_fields(role), 'troops': troops, 'concentration': float(CELL_CAP)}


def _unit_counts(troops):
    """B17.16 (ED-MB-0101): HOW MANY UNITS EACH OF A SIDE'S PERSONS' TROOPS IS CUT INTO, `troops` being each person's (a `side`
    arm and an order's headcount line are one). Each is the fewest equal units none of which passes `MAX_TROOPS_PER_UNIT` (unless that would be more than `UNIT_CAP` units, and then `_refusal` refuses the field); and a
    side that raises at least `MIN_ARMY_TROOPS` is at least `MIN_UNITS_PER_ARMY` units in all, the extra cuts going to the largest
    unit first (the tie to the earlier person). A side below the army's floor is not cut further: it is under the ruled minimum
    and `armyrecord`'s form-time warning is where that is said, as `geometry.footprint_for` leaves a unit below its own."""
    counts = [max(1, math.ceil(t / MAX_TROOPS_PER_UNIT)) for t in troops]
    if sum(troops) >= MIN_ARMY_TROOPS:
        while sum(counts) < MIN_UNITS_PER_ARMY:
            counts[max(range(len(counts)), key=lambda i: (troops[i] / counts[i], -i))] += 1
    while sum(counts) > UNIT_CAP and max(counts) > 1:      # an army holds at most `UNIT_CAP` units: past it a unit passes the
        counts[max(range(len(counts)), key=lambda i: (counts[i], -i))] -= 1       # ceiling and `_refusal` reads it (`SCALE-GAP`)
    return counts


def _cut(troops):
    """B17.16: `troops`, one value per person, as the specs' troops and the index of the person owning each: `(sizes, owners)`.
    A person's units are equal, so his troops are what they were (to the float)."""
    sizes, owners = [], []
    for i, (t, n) in enumerate(zip(troops, _unit_counts(troops))):
        sizes += [t / n] * n
        owners += [i] * n
    return sizes, owners


def _weighted_unit(name, weight, side, morale_start=_MORALE_START_BASE, role=None, retreat_at=None):
    """One `Army`, its troops cut into units by `_cut` (B17.16: at least `MIN_UNITS_PER_ARMY` once the side is at the army's
    floor, none past `MAX_TROOPS_PER_UNIT`), each sized by `troops=` (the Jordan-directed continuous-scale field,
    `hierarchy/units.py`: "when `troops` is set the footprint is generated from (troops,
    concentration) ... `tier` becomes vestigial") rather than by `tier`'s fixed lookup table.

    B17.01: `troops = max(under_arms_cap(weight), _MIN_TROOPS)`, the one weight -> troops owner (`_oob_unit`'s size
    too). It is built with `faction` `side` ('A' the attacker, 'B' the defender) and placed by `orderofbattle._place`
    as an order of battle's line is, so a headcount field starts `_APPROACH_ROWS` apart as an army field does.

    `_MVP_SUBUNIT_SHAPE`'s `tier=2` is still passed because `Unit.__post_init__` requires SOME
    tier even in continuous mode; it is inert here (troops overrides it). `concentration` is set
    to `config.CELL_CAP` -- pack as densely as the engine allows before it would open a second
    cell, the smallest-footprint reading available and not a claim about real troop density.
    `morale_start` is `_morale_start`'s value for this side (the base when omitted); `morale` starts
    equal to it, and the Unit sets neither, so its `eff_morale` falls through to the Army's.
    Every other Unit/Army field is the non-canonical inherited default of the pre-port adapter, carried
    via `_MVP_SUBUNIT_SHAPE`/`_MVP_UNIT_COMMAND`.

    CP-T04-02: `role`, the side's standing order (`_role_fields`); `None` is the side as it was. CP-T04-03: `retreat_at`,
    the order's second key (`_retreat_orders`); `None` or `'none'` is the side as it was."""
    return _line_army(name, _cut([max(float(under_arms_cap(weight)), _MIN_TROOPS)])[0], side, morale_start, role, retreat_at)


def _line_army(name, sizes, side, morale_start, role, retreat_at):
    """The one Army a headcount side is: a line unit of each of `sizes` troops, placed by `orderofbattle._place` for `side`, every
    unit with the side's standing order (`role`) and retreat order (`retreat_at`), the Army with its command and morale.
    `_weighted_unit` and `_person_unit` differ only in where `sizes` comes from."""
    specs = [_line_spec(role, t) for t in sizes]
    _place(specs, [class_of(sp['troop_type']) for sp in specs], side)
    subs = [Unit(**spec, advance_dir=_SIDE_DIR[side], orders=_retreat_orders(retreat_at)) for spec in specs]
    return Army(name=name, faction=side, power=_SEASON_FORCE_POWER, **_MVP_UNIT_COMMAND,
                morale=morale_start, morale_start=morale_start,
                units=subs)


#: CP-T04-01 (`H-359`): the two shapes a headcount side takes, the fixture `field_units`' closed set. `side` is the
#: side as it was, ONE subunit sized by Σ weight; `person` is one subunit per commanding person, sized by his own weight.
SUBUNIT_ARMS = ('side', 'person')


def _person_troops(weights, fed):
    """CP-T04-01: each commanding person's troops, `under_arms_cap` of his own weight (B17.01's one scale), floored at `_MIN_TROOPS`
    as `_weighted_unit` floors the side. `fed`, when the host provisioned the field (v9 IN-52), is the side's fielded troops
    standing in for Σ weight, spread over the persons in proportion to their weights, so the side's total is what it was."""
    total = float(sum(weights))
    share = (float(fed) / total) if (fed is not None and total > 0) else 1.0
    return [max(float(under_arms_cap(float(wt) * share)), _MIN_TROOPS) for wt in weights]


def _person_owners(weights, fed=None):
    """B17.16: which person owns each unit of the side `_person_unit` builds, the person's index per unit in unit order
    (`_cut`'s owners): a person's troops are one or several units, kept together and named as one part (`_person_namer`)."""
    return tuple(_cut(_person_troops(weights, fed))[1])


def _person_unit(name, weights, members, side, morale_start=_MORALE_START_BASE, fed=None, role=None,
                 retreat_at=None):
    """CP-T04-01: the `person` arm of a headcount side -- ONE `Army`, its units CUT PER COMMANDING PERSON (`_cut`: one unit,
    or the several his troops need under `MAX_TROOPS_PER_UNIT`, and a side at the army's floor is at least `MIN_UNITS_PER_ARMY` in all),
    each person's troops `_person_troops` and the line placed by `orderofbattle._place` for `side`. Every unit has `_weighted_unit`'s
    shape and the Army its command and morale. The unit at index `i` is `members[_person_owners(...)[i]]`'s (B17.03:
    `_person_namer` and the engine's order of breaking name him by that index; the unit carries no person of its own).
    CP-T04-02: `role`, the side's standing order, is every unit's (`_role_fields`). CP-T04-03: so is `retreat_at`
    (`_retreat_orders`): each unit retreats on its OWN strength."""
    return _line_army(name, _cut(_person_troops(weights, fed))[0], side, morale_start, role, retreat_at)


def _share(left, start, scale):
    """B17.03: THE ONE QUANTISER, a survivor count as an integer on the body scale: `round(scale x left / start)`, `start` floored at
    1 as `_grade`'s ratio always was, clamped to `0..scale`. It is where the engine's floats meet the host's integers, so a side
    the battle never touched reads EXACTLY `scale` (a ratio one part in 10^15 short of 1 rounds to it), and a share never exceeds
    it. Quantised at the seam, not an integer-state commitment (A-29)."""
    return max(0, min(scale, round(scale * left / max(1.0, start))))


def _cohort_share(drawn, left, cohort, scale):
    """B17.03: a cohort's survivors on the body scale. `drawn` is `OrderOfBattle.drawn`, `((unit, cohort, troops), ...)`; `left` maps a
    unit's name to the fraction of it that survived. Each unit's surviving fraction is applied to the troops this cohort gave
    that unit, summed over the units it fed, over what it gave in all."""
    gave = [(unit, troops) for unit, c, troops in drawn if c == cohort]
    return _share(sum(troops * left[unit] for unit, troops in gave), sum(troops for _unit, troops in gave), scale)


def _person_namer(members, owners):
    """B17.03: how the `person` arm names the parts of its side, for `_run_and_grade`. A part is one member and his unit or units
    (B17.16: `owners[i]` is the index into `members` of the person the unit at index `i` is), named by the cohort rule
    (`_cohort_namer`): his share is his units' survivors over his units' start, and he is routed when every unit of his routed.
    `(parts, credit)`, the parts in `members`' order and the id the engine's `(side, unit index)` order of breaking credits for each
    unit index."""
    def name(army, scale):
        parts = []
        for k, pid in enumerate(members):
            mine = [sub for sub, o in zip(army.units, owners) if o == k]
            parts.append(PartOutcome(pid, _share(sum(sub.cur_troops for sub in mine), sum(sub._start_troops for sub in mine), scale),
                                     all(bool(sub.routed) for sub in mine)))
        return tuple(parts), tuple(members[o] for o in owners)
    return name


def _cohort_namer(oob):
    """B17.03: how an army (an order of battle) names the parts of its side. A part is a COHORT: each of the order's units
    surviving fraction (`cur_troops / _start_troops`) is applied to the troops each cohort gave it (`OrderOfBattle.drawn`) and
    summed per cohort (`_cohort_share`); a cohort is routed when every unit it fed routed. A unit's break is credited to the cohort
    that gave it the most troops (the first, on a tie): the part that broke the line, by the engine's order of breaking."""
    def name(army, scale):
        left = {row.name: sub.cur_troops / max(1.0, sub._start_troops) for row, sub in zip(oob.units, army.units)}
        out = {row.name: bool(sub.routed) for row, sub in zip(oob.units, army.units)}
        parts = tuple(PartOutcome(c, _cohort_share(oob.drawn, left, c, scale),
                                  all(out[unit] for unit, cohort, _t in oob.drawn if cohort == c))
                      for c in oob.cohorts)
        credit = tuple(max((r for r in oob.drawn if r[0] == row.name), key=lambda r: r[2], default=(None, None, 0))[1]
                       for row in oob.units)
        return parts, credit
    return name


#: The troop type a side with no order of battle fights as, once the OTHER side has one. It is the nearest canonical
#: stand-in for `_MVP_SUBUNIT_SHAPE`'s bare 'infantry' (which has no stat preset): one line of light infantry, sized by
#: the side's headcount. NOT `levy`, though a levy is what a side that raised nothing could call up: measured at 300 a
#: side over twelve seeds, a levy line closes to contact in 0 of them and every other infantry or mounted type in 11-12
#: (`Army` discipline 1), so a levy fallback would make a field against a headcount side a standing-still draw. [ASSUMPTION; medium; Jordan to correct -- ED-IN-0306 phase 5 gives every faction a real
#: preset order of battle, after which this fallback is reached only by a hand-built record.]
_HEADCOUNT_LINE_TYPE = 'light_infantry'


def _oob_unit(oob, weight, side, morale_start):
    """The Army for a side when the field carries orders of battle (ED-IN-0306). `oob` None -> a single
    `_HEADCOUNT_LINE_TYPE` `UnitRow`, so both sides deploy by the same rule. Its size is the most the side's
    `weight` could put under arms, `under_arms_cap(weight)` (`troop_types/recruitment.py`), NOT the bare weight:
    an order of battle counts troops (a weight-12 cohort raises up to 12,000) and a season weight counts households,
    so a side left at its weight would meet a hundred troops with twelve. [ASSUMPTION; medium; Jordan to correct;
    revert: `max(float(weight), _MIN_TROOPS)`, and a headcount side is a tenth the army it could muster.]
    Built with `faction` 'A'/'B', the engine's deployment convention, rather than `_weighted_unit`'s side names:
    the sides must start on opposite rows, which the single-line path's shared (8, 12) never needed."""
    if oob is None:
        # B17.16: the headcount line is cut into units as every headcount side is (`_cut`), named `line`, `line_2`, ...
        sizes, _owners = _cut([max(float(under_arms_cap(weight)), _MIN_TROOPS)])
        oob = OrderOfBattle(tuple(UnitRow('line' if i == 0 else f'line_{i + 1}', _HEADCOUNT_LINE_TYPE, t)
                                  for i, t in enumerate(sizes)))
    return _build_oob_unit(oob, f'side_{side.lower()}', side, morale_start=morale_start)


def _run_and_grade(unit_a, unit_b, terrain, rng, scale, walls_dr=None, namers=(None, None)):
    """`run_battle` plus the finished field's typed outcome (`_grade`; `resolve_field` is its only caller).

    `walls_dr` (plan position `20-v`, `H-150`): the defender DR the WALLS row adds. `None` -- the
    default -- is A.9's own number, `terrain.WALLS_DEFENDER_DR`, read here and never copied; an int
    overrides it for the one call (the season's `field_walls_dr` fixture, swept 3 / 0 / 1).

    ⚠ CAVEATS THAT BIND THIS PATH.
    DETERMINISM: `rng` is scoped over the battle by `rngsource.using`; the canon engine drew from the
    global `random` module at seven sites, so without that holder a seeded run is unpinnable.
    TERRAIN: UPHILL, RIVER_CROSSING and WALLS are applied (UPHILL's two A.9 clauses fully; NARROW_PASS
    is identified and applies nothing, see below); the attacker is `unit_a`, the defender `unit_b`.
    FOREST_BROKEN's speed half is INERT -- `run_battle` never reads `.speed` (only
    `orchestration.pursuit_damage` and the multi-unit loop of `systems/mass_battle/sim/multi.py` do, and neither is reachable from here).
    WALLS (plan position `20-iv`, the garrisoned march target) adds `terrain.WALLS_DEFENDER_DR` to the
    DEFENDER's `dr`, read live at every melee and rout hit (`eff_dr` falls through to the Army;
    `h_per_size`, the one field derived from `dr` at construction, has no reader), so mutating it here is
    the same in-place shape the speed half uses. WALLS' other clauses, "no flanking; Slow cannot
    advance", are NOT applied: this engine's one-subunit season units have no flank or advance order to
    forbid. UPHILL and RIVER_CROSSING (MB-05) are dice rows: their A.9 dice go onto
    `Army.terrain_off_d`/`terrain_def_d` (`terrain.py`'s constants, which say how a die reaches the
    engine -- `config.SIGMA_PER_D`, calibrated debt); RIVER_CROSSING also steps the crosser one
    `SPEED_TIERS` slower (inert, as forest's is). NARROW_PASS is identified and NOT applied, and it is
    not a deferral: "1 engagement per side; Fibonacci impossible" restricts how many units engage and
    the Concentration tactic, and a season unit is ONE subunit with no tactic -- both clauses already
    hold on every field this function fights, so applying them would change nothing. NO VERDICT: this returns
    the typed outcome (each side's share and flags) and decides nothing; the host's `field_degree` reads it.

    Takes `rng` directly rather than a `world`-shaped object -- this is the only thing either
    caller ever reads off `world`, so narrowing the parameter to what is actually used means
    `resolve_field` (which has no `World`, only a bare `rng`) needs no adapter object to satisfy
    an attribute it does not otherwise have.

    B17.03: `scale` is the body scale each share is quantised onto (`_share`). `namers` is `(attacker's, defender's)`, each `None`
    (a headcount side, which names no part) or the side's namer (`_person_namer`, `_cohort_namer`), read off the units AFTER the
    battle; `run_battle`'s `broke` (its order of breaking) names the part that broke first on each side."""
    if terrain == FOREST_BROKEN:
        if unit_a.speed == 'Fast':
            unit_a.speed = 'Standard'
        if unit_b.speed == 'Fast':
            unit_b.speed = 'Standard'
    elif terrain == WALLS:
        unit_b.dr += WALLS_DEFENDER_DR if walls_dr is None else walls_dr
    elif terrain == UPHILL:
        unit_a.terrain_off_d += UPHILL_ATTACKER_OFF_D
        unit_b.terrain_def_d += UPHILL_DEFENDER_DEF_D
    elif terrain == RIVER_CROSSING:
        unit_a.terrain_off_d += RIVER_CROSSING_OFF_D
        unit_a.speed = SPEED_TIERS[max(0, SPEED_TIERS.index(unit_a.speed) - 1)]

    with rngsource.using(rng):
        # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6), the canon engine's own default]
        ran = run_battle(unit_a, unit_b, max_ticks=18)

    named = [((), ()) if namer is None else namer(army, scale) for namer, army in zip(namers, (unit_a, unit_b))]
    first = tuple(next((credit[i] for who, i in ran['broke'] if who == side and i < len(credit)), None)
                  for side, (_parts, credit) in zip('AB', named))
    return _grade(unit_a, unit_b, scale, ran['turns'], tuple(parts for parts, _credit in named), first)


def _grade(unit_a, unit_b, scale, ticks, parts=((), ()), broke_first=(None, None)):
    """A FINISHED battle's typed outcome (B17.03; B17.01's one reading, split out of `_run_and_grade` so it has one owner -- the walkthrough
    harness reads a run it has already fought through this, not a copy), and NO verdict. `unit_a` is the attacker. A side's share is its
    troops left over its troops at the start, `hp / hp_max`, quantised onto `scale` (`_share`: a side that took no casualty reads
    exactly `scale` and none reads above it). `ended` is `rout` when either army routed, else `concession` when a side gave the
    field up, else `time`. The band is the host's: `engine/season/seam/ladder.py::field_degree` reads `a_out = routed or conceded`
    (CP-T04-03: a side every one of whose units retreated or routed has given the field up, `unit_conceded`) and the same for the
    defender, and a side that is out with the other standing is lost; both out, or neither out when the ticks ran down, is
    drawn. `parts` and `broke_first` are `(attacker's, defender's)`."""
    ended = 'rout' if unit_a.routed or unit_b.routed else (
        'concession' if unit_conceded(unit_a) or unit_conceded(unit_b) else 'time')
    return FieldOutcome(ended=ended, ticks=int(ticks), attacker=_side_outcome(unit_a, scale, parts[0], broke_first[0]),
                        defender=_side_outcome(unit_b, scale, parts[1], broke_first[1]))


def _side_outcome(unit, scale, parts, broke_first):
    return SideOutcome(share=_share(unit.hp, unit.hp_max, scale), routed=bool(unit.routed),
                       conceded=bool(unit_conceded(unit)), parts=parts, broke_first=broke_first)


def resolve_field(inp, rng=None, *, cfg=None, troops_a=None, troops_b=None, decide=None, duel=None):
    """THE SEASON-FACING ENTRY POINT, AND THE `mass_battle` MODULE'S ENTRY (A-25, plan position `31c`) --
    `04 §C.5.1`'s roster contract, reconciled with this module's OWN requirement for an `Army` to hand
    `run_battle`.

    THE ENTRY. The composition row `mass_battle.resolve_field` (`references/module_contracts.yaml`,
    `entry: verb_call`, `verb: march`) targets this function; the registrar resolves it by string into
    `manifest.MODULE_ENTRIES` at driver construction, and the host adapter
    `engine/season/seam/wrappers/mass_battle.py::resolve` -- the `@provider("contest", "mass_battle")` the
    prize row `a field` names -- calls it with the typed input record its builder `field_input` made
    (`engine/season/queries/inputs.py::MassBattleInput`) and the seeded `rng`. It never reads or writes
    `World`, holds no token, and keeps
    no state between calls: the draws are scoped to this call by `rngsource.using` (`_run_and_grade`), the
    geography arrives on the record (`inp.geography`, the host's read), and no trace block is opened.

    §C.5.1: *"units = PersonId[] at weight — one type. There is NO unit class, at any scale."* The
    record's `weights` are each side's `Person.weight`s (`state/carriers.py`: "A COHORT IS A PERSON AT
    weight > 1"); no `Army`/`Faction`-shaped object crosses this boundary. Internally, `run_battle` still
    needs an `Army` -- that requirement does not go away because the caller's contract changed -- and
    headcount is a SIZE fact, not a quality one (see `_weighted_unit` and `_SEASON_FORCE_POWER`'s note). "No unit
    class, at any scale" is honoured at the SEAM this function's signature draws; it does not reach inside an
    adapter whose whole job is to become an `Army` for the engine that only speaks one.

    ⚠ **AN EMPTY DEFENDING SIDE gets `_MIN_TROOPS`' crash-avoidance floor, not an invented auto-win.**
    What an empty defending force MEANS is eligibility policy for whichever verb calls this (open,
    per `ED-IN-0279` clause (a)'s live design fork on the season-side spatial join -- NOT yet
    Jordan's ruling on an auto-win specifically, which this function does not attribute to that row)
    -- the same discipline `seam/wrappers/*` already follows: derive what you can, decide nothing
    you were not asked to. See `_MIN_TROOPS`' own docstring for the SCALE gap this does not solve
    either -- a real corpus side's weight sum is nowhere near this engine's calibrated battle size,
    and this function does not invent the missing conversion.

    THE RECORD'S FIELDS (plan position `20-iv` and after), each a plain value the host read off the world:
      `weights` -- `(attacker, defender)`, each side's member weights, SUMMED here into its Army's troops.
      `territory`, `fort_level` -- the geography territory id of the place fought over and its
          fortification (`world_q.fortification_of`, `[0.0, 1.0]`), turned into ONE A.9 row by
          `terrain_row_for_territory` and applied in `_run_and_grade`. The second side is the DEFENDER,
          so walls stiffen it. `None` territory is the lookup's own no-modifier fallback, whatever the
          fortification, because that function asks "is this a known territory" first.
      `stances` -- `(attacker, defender)`: each side's weight-mean stance toward its own faction, which
          `_morale_start` turns into a morale-start. `0.0` is the base: the pre-`20-iv` flat 5.
      `walls_dr` -- plan position `20-v` (`H-150`): the defender DR a WALLS field adds, handed to
          `_run_and_grade` unchanged. `None` is A.9's number, `terrain.WALLS_DEFENDER_DR`; an int
          overrides it. Inert on a field `terrain_row_for_territory` does not call WALLS.
      `origin` -- MB-05r: the territory the attacking side marched from, or `None`. Whether the march
          crossed a river is `terrain.river_crossed(origin, territory)` (the geography's water, which
          the host never reads), handed to `terrain_row_for_territory` as its `river_crossing`, the
          one place RIVER_CROSSING can come from. `None` crosses nothing: the field as before MB-05r.
      `loyalties`, `loyalty_gain` -- MB-03: `(attacker, defender)` build-time loyalty rows and the
          gain `_morale_start` adds them at; gain `0` is the control, battle history only.
    The row is derived here from the facts that decide it (`territory`, `fort_level`, `origin`), so
    no caller can hand in a row that disagrees.
      `geography` -- the parsed geography file both lookups read, the HOST's (read once per process by
          `engine/season/data/geography.py`). This module opens no file and never writes into it.

    v9 IN-52 (the levy-to-field feed): `troops_a`/`troops_b` are each side's FIELDED troops when the host
    provisioned the field (`settlements.provision`, read by the adapter), `None` -- the default -- meaning
    the side's Σ weight, the field before the feed. They size the Army in the weight's place and nothing
    else; `_MIN_TROOPS`' floor still applies, so an unprovisioned side (`0`) fields the crash floor.

    B17.01: a headcount side is sized by `under_arms_cap` of whatever stands in the weight's place -- Σ weight or the fed
    troops (provision bounds in weight units, so the cap applies after the bound). A side with an order of battle is
    sized by that order's own headcounts; the headcount side facing it is sized by the same cap, so there is one scale.

    CP-T04-01 (`H-359`): `inp.units` is the `field_units` fixture. `side`, shipped, is the side as it was. `person`
    builds a headcount side as one unit per member of `inp.members` (`_person_unit`) and the return then names each
    person as a part of his side, with his own share and rout, and the person who broke first (`_person_namer`); a side that holds
    an order of battle, or faces one, is unchanged by it (its units are the order's, not persons': its parts are its cohorts,
    `_cohort_namer`).

    CP-T04-02 (`H-361`): `inp.orders` is `(attacker, defender)`, each a record with `role` (a `ROLE_SPEC` name) and
    `retreat_at`, or `None`. A side's `role` is the shape and instruction package of every subunit of its headcount line,
    on either `units` arm (`_role_fields`); a side with `None` is the line it always was, so no order held is today's
    field. A side that holds an army's order of battle, or faces one, fights as that order says and an order of battle
    here is not read. CP-T04-03: a side's `retreat_at` is each of its headcount line's units' `own_strength` retreat Order
    (`_retreat_orders`), on either `units` arm; `'none'`, or no order, is no Order. `_grade` reads the side's concession.

    B17.03: returns a frozen `FieldOutcome` on every arm (`_run_and_grade`'s), each share an integer on `inp.condition_scale`.
    B17.04: or a refusal dict (`_refusal`: `SCALE-GAP` past `MAX_TROOPS_PER_UNIT`, `PARTY-GAP` for two sides of nobody) on which
    `run_battle` is never entered.

    B17.12: `cfg` is the engine's `EngineConfig`, stated, never found: `None` is the shipped one (`config.DEFAULT`). The
    module's constants are read off the config this tree was built from, so a config that is not this tree's own is
    refused here by name, not run as if it were: a variant is a tree built from it
    (`systems/mass_battle/sim/variant.py`), whose own `resolve_field` accepts it. `decide` and `duel` are the seams
    for a decision hook and a duel resolver, `None` and passed by nothing yet (B20, B30)."""
    if cfg is not None and asdict(cfg) != asdict(_config.DEFAULT):
        raise ValueError("resolve_field: cfg is not this engine's config; build the engine from it "
                         "(systems/mass_battle/sim/variant.py) and call that engine's resolve_field")
    weight_a, weight_b = (sum(side) for side in inp.weights)
    if troops_a is not None:
        weight_a = troops_a
    if troops_b is not None:
        weight_b = troops_b
    stance_a, stance_b = inp.stances
    loyalty_a, loyalty_b = inp.loyalties
    morale_a = _morale_start(stance_a, loyalty_a, inp.loyalty_gain)
    morale_b = _morale_start(stance_b, loyalty_b, inp.loyalty_gain)
    oob_a, oob_b = inp.orders_of_battle or (None, None)
    armies = oob_a is not None or oob_b is not None
    # CP-T04-02: each side's standing order's role, `None` for a side holding none (`inp.orders` unset is both).
    order_a, order_b = inp.orders or (None, None)
    role_a = None if order_a is None else order_a.role
    role_b = None if order_b is None else order_b.role
    retreat_a = None if order_a is None else order_a.retreat_at
    retreat_b = None if order_b is None else order_b.retreat_at
    if inp.units not in SUBUNIT_ARMS:
        raise ValueError(f"field_units {inp.units!r} is not one of {SUBUNIT_ARMS}")
    namers = (None, None)
    if not armies and inp.units == 'person':
        # CP-T04-01: one unit per commanding person. `members` is `weights`' own order, so zip pairs a person with
        # his weight. A provisioned side (`troops_a`/`troops_b`) is spread over its persons by weight.
        unit_a = _person_unit("side_a", inp.weights[0], inp.members[0], 'A', morale_a, troops_a, role_a, retreat_a)
        unit_b = _person_unit("side_b", inp.weights[1], inp.members[1], 'B', morale_b, troops_b, role_b, retreat_b)
        namers = (_person_namer(inp.members[0], _person_owners(inp.weights[0], troops_a)),
                  _person_namer(inp.members[1], _person_owners(inp.weights[1], troops_b)))
    elif not armies:
        unit_a = _weighted_unit("side_a", weight_a, 'A', morale_a, role_a, retreat_a)
        unit_b = _weighted_unit("side_b", weight_b, 'B', morale_b, role_b, retreat_b)
    else:
        # ED-IN-0306: a side with an order of battle fights as that order says. Its headcounts are authoritative,
        # so `troops_a`/`troops_b` (the provisioning feed) are not applied to it -- recruiting is what bounds an
        # order of battle's size (phase 2), and scaling it here would silently overrule that.
        unit_a = _oob_unit(oob_a, weight_a, 'A', morale_a)
        unit_b = _oob_unit(oob_b, weight_b, 'B', morale_b)
        # B17.03: an army's parts are its cohorts; a headcount side facing one names none.
        namers = tuple(None if oob is None else _cohort_namer(oob) for oob in (oob_a, oob_b))
    refused = _refusal(unit_a, unit_b)
    if refused is not None:
        return refused
    # No territory: `river_crossed` answers False and the lookup OPEN_FLAT. WALLS outranks a crossing
    # (`terrain_row_for_territory`), so a fortified field does not derive one.
    crossing = inp.fort_level <= 0 and river_crossed(inp.origin, inp.territory, geography=inp.geography)
    return _run_and_grade(unit_a, unit_b,
                          terrain_row_for_territory(inp.territory, inp.fort_level, crossing,
                                                    geography=inp.geography),
                          rng, inp.condition_scale, walls_dr=inp.walls_dr, namers=namers)
