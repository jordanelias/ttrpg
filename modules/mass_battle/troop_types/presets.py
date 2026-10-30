"""modules.mass_battle.troop_types.presets -- the order of battle a faction raises for itself (ED-IN-0305, phase 5c).

A faction the player does not play still needs an army. This is the rule for the one it raises: a PURE PLAN from what a
faction's cohorts can raise to the commands that mint-fill-organise an army, as the commands a player would give
(`recruit`, `form_unit`, `assign_troops`; the army's strategy is set when it is minted). It reads no `World` and draws nothing, so the same facts give
the same army. The engine side (`engine/season/harness/army_presets.py`) turns the plan into acts for the faction's
leader; the verbs refuse what the world does not allow, so this plan adds no rule of its own beyond WHAT TO ASK FOR.

THE DOCTRINE (ASSUMPTION; medium; Jordan to correct -- it is the common shape of the Romance of the Three Kingdoms and
Total War armies Jordan named): a battle line of the best heavy foot the faction can train, missile troops behind it,
horse for the flanks, and levy filling whatever room is left, as the reserve.

    melee    heavy_infantry, spearmen, pike, light_infantry   (the first the faction can train)    45% of each cohort's cap
    missile  crossbow, archers, sling, skirmishers                                                    a quarter of it
    mounted  cavalry, knights_templar, light_cavalry                                                  a fifth of it
    levy     the rest of every cohort's room (a tenth where every Site exists), held back as the reserve

Each cohort gives each class its share of its own cap, in the best type of that class its Sites allow. A
type the faction has no Site for is skipped (`recruitment.recruit_limit` reads 0), so a realm without a barracks, a
range or a stable fields levy alone -- which holds a line and cannot press an attack (a named limit, HANDOFF_MB).
An army that would come to fewer than `BLOCK_SIZE` troops is not raised at all (it routs at once). A group of fewer than `SUBUNIT_ROUT_FLOOR` troops is not raised: it would rout at the first check, and
its room goes to the levy.

[canonical: none -- every share and the type order are this module's; the troop types, their roles and the floors are
the registry's and `config.py`'s. Revert: a faction's army is whatever its leader orders.]
"""
from __future__ import annotations

from modules.mass_battle.armyrecord import cohort_claims
from modules.mass_battle.config import BLOCK_SIZE, SUBUNIT_ROUT_FLOOR
from modules.mass_battle.troop_types.recruitment import recruit_limit, under_arms_cap

__all__ = ['DOCTRINE', 'ROLE_OF', 'plan']

#: class -> (share of each cohort's under-arms cap, the types in order of preference). [ASSUMPTION; medium;
#: Jordan to correct; the order is heaviest and most disciplined first.]
DOCTRINE = (
    ('melee',   0.45, ('heavy_infantry', 'spearmen', 'pike', 'light_infantry')),  # [canonical: ED-IN-0305 -- ASSUMPTION: the doctrine's share of a cohort's cap; Jordan to correct]
    ('missile', 0.25, ('crossbow', 'archers', 'sling', 'skirmishers')),  # [canonical: ED-IN-0305 -- ASSUMPTION: the doctrine's share of a cohort's cap; Jordan to correct]
    ('mounted', 0.20, ('cavalry', 'knights_templar', 'light_cavalry')),  # [canonical: ED-IN-0305 -- ASSUMPTION: the doctrine's share of a cohort's cap; Jordan to correct]
)

#: type -> the role its subformation takes, from `roles_for(type)`: a plain line for the heavy foot, volleys for the
#: bows, the flank for the horse, the reserve for the levy. None is a plain Line.
ROLE_OF = {
    'heavy_infantry': None, 'spearmen': None, 'pike': None, 'light_infantry': None,
    'crossbow': 'Support', 'archers': 'VolleyLine', 'sling': 'Support', 'skirmishers': 'Skirmish',
    'knights_templar': 'Support', 'cavalry': 'Flanker', 'light_cavalry': 'Flanker',
    'levy': 'Reserve',
}


def plan(q) -> tuple:
    """THE ENTRY (`mass_battle.army_preset`, a `query` composition row): `((verb, payload), ...)` that raise and organise
    an army for `q.faction`, in the order they must be given. `payload` carries everything but the army's `subject`,
    which the host adds. `q` is `engine/season/queries/inputs.py::ArmyPresetQuery`: `faction`, `cohorts`
    (`((cohort id, weight, {site kind: condition}), ...)`, those the faction may raise), `full` (the condition scale)
    and `others` (the other armies' records, whose claims on a cohort count against it). An empty plan means the
    faction can raise nobody."""
    cohorts = sorted(q.cohorts)
    given = {c: cohort_claims(None, q.others, c) for c, _w, _s in cohorts}
    raised: list = []                                   # (cohort, type, count) in the order asked for

    def room(c, w, sites, t):
        return recruit_limit(t, w, sites, given[c], q.full)

    def take(c, t, n):
        given[c][t] = given[c].get(t, 0) + n
        raised.append((c, t, n))

    # Each class in turn, and from EVERY cohort its share of that cohort's cap (a cohort's people are split across the
    # arms, so a class filled from the first cohorts alone would leave the later classes nothing to stand on). A trial pass
    # sees what the class WOULD raise; a type that comes to less than a subformation can stand on is dropped, then the real
    # pass. `given` is restored between, so both passes see the same rooms.
    for _cls, share, types in DOCTRINE:
        trial = []
        snapshot = {c: dict(g) for c, g in given.items()}
        for c, w, sites in cohorts:
            want = int(under_arms_cap(w) * share)
            for t in types:
                n = min(want, room(c, w, sites, t))
                if n > 0:
                    trial.append((c, t, n))
                    given[c][t] = given[c].get(t, 0) + n
                    break
        for c, snap in snapshot.items():
            given[c].clear()
            given[c].update(snap)
        by_t: dict = {}
        for _c, t, n in trial:
            by_t[t] = by_t.get(t, 0) + n
        for c, t, n in trial:
            if by_t[t] >= SUBUNIT_ROUT_FLOOR:
                take(c, t, n)
    # The levy takes the rest of every cohort's room, as the reserve, if it comes to a standing subformation.
    levy = []
    for c, w, sites in cohorts:
        n = room(c, w, sites, 'levy')
        if n > 0:
            levy.append((c, 'levy', n))
    if sum(n for _c, _t, n in levy) >= SUBUNIT_ROUT_FLOOR:
        for c, t, n in levy:
            take(c, t, n)
    if not raised:
        return ()
    if sum(n for _c, _t, n in raised) < BLOCK_SIZE:       # `armyrecord.options` calls this `army_routs`: not worth raising
        return ()
    order = [x for _k, _s, ts in DOCTRINE for x in ts] + ['levy']        # the doctrine's order, the reserve last
    types = sorted({t for _c, t, _n in raised}, key=order.index)
    cmds = [('recruit', {'cohort': c, 'troop_type': t, 'count': n}) for c, t, n in raised]
    for t in types:
        role = ROLE_OF[t]
        cmds.append(('form_unit', {'name': t, 'troop_type': t, **({'role': role} if role else {})}))
    cmds += [('assign_troops', {'name': t, 'cohort': c, 'count': n}) for c, t, n in raised]
    return tuple(cmds)
