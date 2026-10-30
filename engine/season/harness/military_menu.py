"""THE HEADLESS MILITARY MENU -- what a person who commands a faction's army may ask of it, as data, and the acts that ask
(ED-IN-0305 phase 5b).

    from engine.season.harness.military_menu import menu, act_for, callback, describe
    m = menu(w, "p_npc_033")                                   # a MilitaryMenu: legal army acts, with bounds, and advisories
    print(describe(m))                                         # the same, in plain words
    act = act_for(w, "p_npc_033", "recruit", cohort=c, troop_type="spearmen", count=40)
    choose = dispatching_chooser(auto, {"p_npc_033": callback(w, lambda m: [act_for(w, m.actor, ...)])})

The army verbs (`recruit`, `form_unit`, `assign_troops`, `order_unit`, `disband_unit`, `discharge_troops`) carry their command
in the act's PAYLOAD, which no Candidate carries, so nobody forms them for themselves (`Fixtures withheld_verbs`): this is
the surface a client uses to give them. A client is a player, or the preset installer (`harness/army_presets.py`) for a
faction nobody plays. There is no Godot screen: Jordan ruled the menu an engine-side Python API.

⚠ THE MENU ADDS NO RULE. The recruiting bound and the vocabulary are the module's own, asked through the
`mass_battle.army_options` row (`recruit_limit`, the registry's role menus); the assign, release and discharge amounts are
read straight off the record's counts; its refusals are the verbs'. A listed act can still be refused (the fold
checks who holds what); an act built by hand and not listed is refused for the reason the menu leaves it out. It reads the
world and writes nothing. `callback` returns the Acts a client chose; DELIBERATE refuses a return over the person's budget.

NAMED LIMIT: the menu covers the army record, not WHERE the army goes -- `march` is an ordinary verb a person already forms,
and the general who decides it is MB-08's.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any, Callable, Optional

from engine.substrate import composition

from ..data.rosters import ARMY_VERBS, FACTION_BY_PROP
from ..loop.effects_information import _army_mintable
from ..queries import world_q
from ..queries.inputs import ArmyOptionsQuery
from ..queries.world_q import faction_holding, hold_force
from ..state.carriers import Act

#: How many "can raise" rows `describe` spells out before saying "and N more". [canonical: none -- a display length]
SHOWN = 12  # [canonical: ED-IN-0305 -- display length only, no game meaning]

__all__ = ["MilitaryMenu", "menu", "act_for", "callback", "describe", "cohorts_raisable"]


@dataclass(frozen=True)
class MilitaryMenu:
    """What `actor` may do with the army of the faction they are committed to.
      * `faction`/`army`  -- the faction Proposition id and the army Record id, or None for each that does not exist
      * `commands`        -- True when `actor` holds the army and so can give it orders; False for a mere member
      * `mint`            -- True when `actor` may mint the faction's (empty) army now
      * `raise_`          -- ((cohort, troop type, most that may be raised now), ...)
      * `assign`/`release` -- ((subformation, cohort, most that may be moved), ...)
      * `discharge`       -- ((cohort, troop type, most that may be sent home), ...)
      * `disband`         -- (subformation name, ...)
      * `orders`          -- ((subformation, the roles its type allows), ...)
      * `vocabulary`      -- the module's own: strategies, stances, targets, troop_types (type, roles, site kind)
      * `advisories`      -- ((kind, subject, have, floor), ...), what is wrong with the army as it stands"""
    actor: str
    faction: Optional[str]
    army: Optional[str]
    commands: bool
    mint: bool
    raise_: tuple = ()
    assign: tuple = ()
    release: tuple = ()
    discharge: tuple = ()
    disband: tuple = ()
    orders: tuple = ()
    vocabulary: Optional[dict] = None
    advisories: tuple = ()


def cohorts_raisable(w, faction: str) -> tuple:
    """`((cohort id, weight, {site kind: best condition}), ...)` for each cohort `faction` may raise
    (`world_q.raisable_by`), in id order -- the fact the module's `recruit_limit` needs about a place."""
    return tuple((p.id, p.weight, world_q.training_sites(w, p.id))
                 for _id, p in sorted(w.persons.items())
                 if p.is_cohort and p.weight > 1 and world_q.raisable_by(w, p.id, faction))


def _empty_army(faction: str, strategy: str = "line") -> dict:
    """The content an army is minted with (`_army_mintable` checks it is well formed and empty). The key set is
    `rosters.yaml: record_kinds.army`; `line` is the neutral strategy, which `order_unit` changes."""
    return {"faction": faction, "strategy": strategy, "trained": (), "subformations": ()}


def menu(w, actor: str) -> MilitaryMenu:
    """The military menu for `actor`. Empty (nothing legal, no faction) for a person committed to no faction that has
    an army, and for an unknown person. Read-only."""
    faction = faction_holding(w, actor) if actor in w.persons else None
    if faction is None or faction not in FACTION_BY_PROP:
        return MilitaryMenu(actor, faction, None, False, False)
    rid = world_q.army_of(w, faction)
    if rid is None:
        return MilitaryMenu(actor, faction, None, False, _army_mintable(w, actor, _empty_army(faction)))
    held = hold_force(w, rid)
    rec = w.records[rid].subject_matter
    commands = held is not None and held.subject == actor
    if not commands:
        return MilitaryMenu(actor, faction, rid, False, False)
    opts = composition.require(world_q.ARMY_OPTIONS)(
        ArmyOptionsQuery(rec, cohorts_raisable(w, faction), w.fixtures.get("condition_scale"),
                         world_q.other_army_records(w, rid)))
    roles = {t: r for t, r, _site in opts["troop_types"]}
    sfs = rec["subformations"]
    assign = tuple((sf["name"], c, n) for sf in sfs for c, t, n in rec["trained"] if t == sf["troop_type"])
    release = tuple((sf["name"], c, n) for sf in sfs for c, n in sf["assigned"])
    return MilitaryMenu(
        actor, faction, rid, True, False, raise_=opts["raise"], assign=assign, release=release,
        discharge=tuple((c, t, n) for c, t, n in rec["trained"]), disband=tuple(sf["name"] for sf in sfs),
        orders=tuple((sf["name"], roles[sf["troop_type"]]) for sf in sfs),
        vocabulary={k: opts[k] for k in ("strategies", "stances", "targets", "troop_types")},
        advisories=opts["advisories"])


def act_for(w, actor: str, verb: str, **payload: Any) -> Act:
    """The Act that gives one army command. `verb` is `create_record` (mint the faction's empty army; the payload may name its
    `strategy`) or one of the six army verbs, whose payload is the command (`recruit`: cohort, troop_type, count;
    `form_unit`: name, troop_type, role?; `assign_troops`: name, cohort, count (negative releases); `order_unit`: name and
    any of role, stance, target, fall_back_at, or strategy alone; `disband_unit`: name; `discharge_troops`: cohort,
    troop_type, count). The army is the actor's faction's. The id is derived from the tick, the actor, the verb and the
    payload (the same command gives the same id; folding it twice applies it twice). Builds, does not check: the fold's refusals are the check."""
    faction = faction_holding(w, actor)
    if verb == "create_record":
        home = world_q.home_of(w).get(actor)
        rid = f"army_{faction}_{w.tick}"
        while rid in w.records:                       # a dead holder's army is still a Record; never overwrite it
            rid += "_"
        body = {"record": rid, "kind": "army", "rung": home,
                "subject_matter": _empty_army(faction, payload.get("strategy", "line"))}
    elif verb in ARMY_VERBS:
        rid = world_q.army_of(w, faction)
        if rid is None:
            raise ValueError(f"{faction!r} has no army to {verb}: mint one first")
        body = {"subject": rid, **payload}
    else:
        raise ValueError(f"{verb!r} is not an army command (known: create_record, {', '.join(sorted(ARMY_VERBS))})")
    key = hashlib.sha1(repr((w.tick, actor, verb, sorted(body.items(), key=lambda kv: kv[0]))).encode()).hexdigest()[:10]
    return Act(id=f"mil_{key}", actor=actor, verb=verb, payload=body)


def callback(w, select: Callable[[MilitaryMenu], list]) -> Callable[..., list]:
    """A `play_surface.dispatching_chooser` callback for one person: it shows `select` that person's menu and returns the
    Acts `select` chose (built with `act_for`). `auto`, the shipped policy, is ignored: a person given a menu decides
    for themselves. Build one per person and pass `{person id: callback(...)}`. The acts are cut to the person's scene
    budget (`ask_budget()`), since DELIBERATE raises on a return over it.

    ⚠ NAMED LIMIT OF THE IN-SEASON PATH: DELIBERATE drops an act whose `(verb, subject)` an earlier round already realised
    (`data/verbs.py::opportunity_key`), and an army verb's subject is the army, so a person can give each army verb ONCE
    PER SEASON through a callback (one `recruit`, not one per cohort). The menu still lists every cohort. Bulk organising
    is the fold's: hand-built acts between seasons (`harness/army_presets.py::install` does so)."""
    def cb(p: Any, v: Any, s: Any, ask_budget: Callable[[], int], auto: Callable[..., list]) -> list:
        return list(select(menu(w, p.id)))[:max(0, int(ask_budget()))]
    return cb


def describe(m: MilitaryMenu) -> str:
    """The menu in plain words."""
    if m.faction is None:
        return f"{m.actor} serves no faction with an army."
    if m.army is None:
        return (f"{m.faction} has no army. {m.actor} may raise one (mint)." if m.mint
                else f"{m.faction} has no army, and {m.actor} may not raise one.")
    if not m.commands:
        return f"{m.faction} has an army ({m.army}); {m.actor} does not command it."
    out = [f"{m.actor} commands {m.faction}'s army ({m.army})."]
    if m.raise_:
        out.append("Can raise: " + "; ".join(f"{n} {t} from {c}" for c, t, n in m.raise_[:SHOWN])
                   + (f"; and {len(m.raise_) - SHOWN} more" if len(m.raise_) > SHOWN else "") + ".")
    else:
        out.append("Can raise nobody more.")
    if m.disband:
        out.append("Subformations: " + ", ".join(m.disband) + ".")
    if m.discharge:
        out.append("Trained, in no subformation: " + "; ".join(f"{n} {t} of {c}" for c, t, n in m.discharge) + ".")
    for kind, subject, have, floor in m.advisories:
        out.append({"subformation_routs": f"Warning: {subject} has {have} troops; under {floor} it routs at the first check.",
                    "army_routs": f"Warning: the army fields {have} troops; under {floor} it routs at once.",
                    "unassigned": f"{have} trained troops are in no subformation and will not fight.",
                    "levy_never_closes": f"{subject} is levy and will not close to contact."}.get(kind, f"{kind}: {subject}"))
    return " ".join(out)
