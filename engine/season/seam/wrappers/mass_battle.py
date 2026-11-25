"""THE MASS-BATTLE PROVIDER -- the host adapter and the host INPUT BUILDER for the `mass_battle` module's
entry, `modules/mass_battle/massbattle.py::resolve_field` (plan position `31c`, A-25).

What is here is the HOST: the input builder `field_input` (`World` -> `queries/inputs.py::MassBattleInput`:
each side's member weights, the place, its fortification, each side's stance, the walls fixture) and the
adapter `resolve`, which keeps the PARTY-GAP refusals and the `Unopposed` branch, calls the module entry
the prize row names (`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its composition row,
`entry: verb_call`, `verb: march`) and lifts what comes back. The fight itself -- the Armies, the terrain
row, the battle and its survivor-ratio grade -- is the module's, reached by string. `resolve` also asks
`settlements.provision` (a `query` entry, through `composition.require`) how many of each side's troops
its treasury can field, shipped OFF (`field_provisioning`, `H-241`). `loop/sides.py` is host too: it builds
the claimants the record's weights are read for.

⚠ **THE `claimants`/`subject`/`rung` SPLIT.**
`seam/contest.py`'s S39.1 is unconditional: *"claimant[] is PERSONS, ALWAYS. Not factions, not
units, not sides"*, and `seam/wrappers/sigma.py` types `subject` as sometimes naming something that is
NOT a person, so this module's shape needs no new seam-level concept: it reuses `subject` for the other
side's faction Proposition id and reads `rung` to scope that faction's `members` down to who is actually
PRESENT at the target, via `world_q.mustered` (`04 §C.5.1`'s own *"squad combat: the squad is
`members ∩ present-at-rung`"*). `claimants` is one side's already-resolved `PersonId[]` per
§C.5.1's *"sides = (faction_q.resolve(proj,A), faction_q.resolve(proj,B)) -- ONCE, before
provider.run"*. `loop/sides.py::sides_of`, dispatched on the PRIZE's own manifest `module` (never on
`a.verb`, and never on what the target looks like -- see that module's own docstring), builds the
`claimants`/`subject`/`rung` for this prize: the actor's own muster at the origin, the target
rung's holder faction (`queries/world_q.holder_faction_of`), and the target rung itself. `kill /
wound` and `tell` keep their two-claimant shape, through `sides_of`'s other branch.

⚠ **WHO ATTACKS, WHO DEFENDS, AND WHAT AN EMPTY DEFENDING SIDE MEANS ARE `march`'s OWN eligibility
and effects (`ED-IN-0279` clause (b), 2026-09-28)** -- an empty defending side
is `Unopposed` (the `Unopposed` branch in `resolve` below), never an auto-win manufactured here.

⚠⚠ **WHAT A GARRISON DOES TO THIS FIGHT IS READ HERE, AND THE READ IS ALL THIS MODULE ADDS (plan
position `20-iv`, `H-150`).** Jordan's ruling (planning round 2) fixed garrison STRENGTH as a Site's
`condition` field, and `queries/world_q.py::fortification_of` reads it. `resolve()` reads three facts
about the fight off the world and hands them on as plain values -- it decides none of what they do:
  * the TERRITORY the target sits in, `_territory_of` below: the nearest `territory`-kind rung up
    the target's ancestry, turned back into its geography row by `data/rosters.territory_id_of`
    (the one owner of that id relation, which `boot/realm.py` mints through);
  * its FORTIFICATION, `world_q.fortification_of` at the target;
  * each side's MORALE source, `_side_stance` below;
and one injected value: the `field_walls_dr` fixture (`H-150`). Two more facts and one more value: the
attacking side's ORIGIN territory (`_origin_of`), each
side's build-time LOYALTY row (`_side_stance` with `_creed_referent`), and the
`field_morale_loyalty_gain` fixture.
What a fortification DOES is `massbattle.resolve_field`'s and `terrain.py`'s: any positive value
makes the field A.9's `WALLS` row, whose one number (defender +3 DR) the engine applies to `Army.dr`
1:1 (an ASSUMPTION about the unit, `H-150`). The number is canon's, not invented here -- `None` in the
fixture leaves it where `terrain.py` authors it, and an int sweeps it -- which is why this
module may carry the read without deciding anything -- `seam/wrappers/combat.py` derives a party the same way and calls the
engine without deciding who picked the fight.

⚠ **`degree_of` (`seam/ladder.py`) GRADES THIS RESULT THROUGH A THIRD BRANCH RATHER THAN BY
MANUFACTURING A MARGIN (`ED-IN-0279` clause (a)).** The module returns each side's survivor share and its
`routed`/`conceded` flags and no verdict. What it grades is the four top-level `seam/ladder.py::FIELD_FLAGS` (and `unopposed`)
this function lifts, onto the bands `march` writes on (Won, Lost, Drawn, Unopposed, and Invested under a besiege)
(`seam/ladder.py::field_degree`). Manufacturing a `net`/`ob` from the survivor shares would have been the second resolver
S27.2 refuses; reading flags the module already reports is not that.

⚠ **NO NEW `sys.path` SEAM, AND NO IMPORT OF THE MODULE.** `resolve_field` is reached by STRING: the
composition row `mass_battle.resolve_field` (`references/module_contracts.yaml`) names it, the registrar
resolves it at driver construction into `MODULE_ENTRIES`, and `resolve` below looks it up there by the
role its prize row names -- `engine/` never imports module code. `PATH_SEAM_ALLOWED`
(`tests/valoria/test_engine_does_not_import_systems.py`) is empty and gains no entry: the moved closure's own
imports are dotted `modules.mass_battle.*`, a package, so it needs no path seam.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any, Optional

from engine.dice_engine.draw import Draw

# `providers` is imported by module, as combat.py and sigma.py do (see their notes on the manifest
# import order); the entry lookup is `_entry.py`'s, which imports `registrar` and `registry` the same way.
from ...manifest.providers import provider
from ...data.geography import geography
from ...data.rosters import SUBTREE_OCCUPATION_KINDS, territory_id_of
from ...data import rosters
from ...data.rosters import BESIEGE, DRAWN, LOST, MARCH_POSTURE_KEY, ORDER_RETREAT_KEY, ORDER_ROLE_KEY, STORM, UNOPPOSED, WON, require_member
from ...loop.sides import sides_of
from ...queries.inputs import ArmyMuster, FieldOrder, MassBattleInput, ProvisionInput
from ...queries.person_q import stance_toward
from ...queries import world_q
from engine.substrate import composition
from ...state.carriers import Act
from ...state.gate import seat_faction
from ._entry import entry_for
from ._estimate import rng_of, samples_of
from ..ladder import FIELD_FLAGS, field_degree, field_flags

_PROVIDER = "mass_battle"
_PRIZE = "a field"      # the prize row this provider deals (`rosters.yaml`), `march`'s
# CP-T04-08: the bands `field_estimate` shares out, in `sigma.odds_of`'s order -- the four `field_degree` grades a
# fought or unopposed field into (`Declared` is the band RESOLVE writes before anything is fought, not an ending; `Invested`
# fights no field).
ESTIMATE_BANDS = (WON, LOST, DRAWN, UNOPPOSED)
# A result no field was fought for (an unopposed march, an invested garrison) carries the four flags all unset, so it is
# the field's shape for `degree_of` and `field_degree` reads its `unopposed`/`invested` marker first.
_NO_FLAGS = dict.fromkeys(FIELD_FLAGS, False)


def _territory_of(w: Any, rung: str) -> Optional[str]:
    """The geography territory id of the territory `rung` sits in, or `None`.

    The nearest `territory`-kind rung at or above `rung` (`world_q.enclosing_territory`, the one
    owner of that walk, over `world_q.ancestry`), read back to its geography row by
    `territory_id_of`. `None` -- no territory above, or one no geography row minted (a corpus
    fixture's) -- is `terrain_row_for_territory`'s no-modifier case, not a refusal."""
    return territory_id_of(world_q.enclosing_territory(w, rung))


def _creed_referent(w: Any, fac: str) -> Optional[str]:
    """Whom a member of faction `fac` holds their build-time LOYALTY row toward: the subject of the
    faction's creed Proposition when its mood is OUGHT (its authored leader), else `None` (MB-03).

    This is the writer's own rule read back, not a second one: `boot/realm.py::build_realm` appends the
    row `(prop.subject, *cast.stance_from_loyalty(...))` exactly when the creed's mood is OUGHT, and a
    HOLDS faction (`Guilds`, `Schoenland`: no leader or template in canon) gets no row and reads `None`
    here -- `cast.loyalty`'s *"`None` FOR A FACTION WITH NO TEMPLATE, NEVER A DEFAULT"*. ⚠ The row
    names a PERSON, the creed's utterer, not the faction: that is why the morale row (`_eff_march`,
    on the faction id) and this one are two referents and are read and handed on separately.

    ⚠ v11 CR-87 (5) BROKE THAT SEPARATION AT THE SHIPPED FIXTURE. With `loyalty_toward_creed` True (the default) the
    writer puts the build-time row on the creed PROPOSITION, which is the faction's own id, never on its utterer; so
    in a built realm this reads NO row (`H-256`), and the same row is read by `_side_stance`'s DEFAULT referent (the
    faction id), i.e. by the morale-start's `stance` term at one point per unit and no gain. Nothing here fixes it:
    it is H-256's recorded collision, to be settled by a decision on where loyalty is read, not by a patch."""
    prop = w.propositions.get(fac)
    return prop.subject if prop is not None and str(prop.mood).upper() == "OUGHT" else None


def _side_stance(w: Any, pids: list, referent=lambda w, fac: fac) -> float:
    """A side's weight-mean stance toward a referent its members' OWN faction names -- by default the
    faction itself, the season's morale carrier (`massbattle._morale_start`'s docstring says why it is
    this one); with `referent=_creed_referent`, the creed's utterer, the build-time loyalty row (MB-03).

    Each member's faction is `world_q.faction_holding`, the one owner of *which faction a person
    coheres under*, and the stance is `queries.person_q.stance_toward`, the one reader of a stance row
    (valence x weight, summed over the rows naming that referent). A member committed to no faction
    or to two reads `None` there and contributes zero -- `faction_holding`'s own *"NONE AND MANY BOTH
    RETURN None, AND NEITHER IS A DEFAULT"* -- and so does a member whose faction names no referent.
    Weighted by `Person.weight` because `resolve_field` sizes the side by the same weights: a cohort
    of ten carries ten men's morale. An empty side reads 0."""
    total = 0
    acc = 0.0
    for pid in pids:
        p = w.persons.get(pid)
        if p is None:
            continue
        fac = world_q.faction_holding(w, pid)
        ref = referent(w, fac) if fac is not None else None
        acc += p.weight * (stance_toward(p, ref) if ref is not None else 0.0)
        total += p.weight
    return acc / total if total else 0.0


def _origin_of(w: Any, pids: list) -> Optional[str]:
    """The geography territory id the attacking side marched FROM, or `None` (MB-05r).

    `contest()` hands this provider the target rung and never the origin, and no seam parameter is
    added for it: on the season path `loop/sides.py::sides_of` musters `claimants` at the actor's
    origin settlement (`world_q.mustered`, the settlement's subtree), so every claimant's home
    (`world_q.home_of`, read once) sits under that settlement and `_territory_of` reads the same
    territory for each. A side whose homes name no territory, or more than one (a caller passing a
    faction's whole membership), has no one origin and reads `None` -- the default, under which no
    crossing is derived."""
    homes = world_q.home_of(w)
    by_home: dict = {}                      # one `_territory_of` walk per distinct home, this call only
    found = set()
    for pid in pids:
        if pid not in homes:
            found.add(None)
            continue
        home = homes[pid]
        if home not in by_home:
            by_home[home] = _territory_of(w, home)
        found.add(by_home[home])
    return found.pop() if len(found) == 1 else None


def _order_of_battle(w: Any, faction: Optional[str], side: list) -> Any:
    """ED-IN-0306 phases 3 and 5. The order of battle `faction`'s army Record fights this field with, or `None` -- the
    side as it always fought, one headcount line. `None` for no faction, a faction with no army Record, an army whose
    commander is not here, and an army none of whose troops has a body left.

    AN ARMY IS WHERE ITS COMMANDER IS. The Record's holder is its commander; when he is among `side` (the persons the
    adapter already mustered at the place: the attacker's at its origin, the defender's at the target) the whole army
    takes the field, its troops drawn from cohorts wherever they live -- a cohort is a place's population and does not
    march, so requiring it to stand on the field capped every army at one town's levy (20 troops). A commander
    elsewhere leaves this side to fight as it always did. HOW FIT each cohort is = its `body` over `condition_scale`,
    the scale a person is built at (`Person.body`); that is the whole casualty loop -- `march` scales the bodies of the
    cohorts a losing army drew from by the engine's survivor fraction (`_eff_march`, `parties["fielded"]`), so the
    next field this army fights is that much smaller, and `tend` restores it. What the Record turns into is the
    module's (`mass_battle.army_order`, by role string): this reads facts off the world and decides nothing."""
    rid = world_q.army_of(w, faction) if faction is not None else None
    if rid is None:
        return None
    commander = world_q.hold_force(w, rid)
    if commander is None or commander.subject not in side:
        return None
    full = w.fixtures.get("condition_scale")
    fit = tuple((pid, max(0.0, min(1.0, p.body / full))) for pid, p in w.persons.items() if p.is_cohort)
    return composition.require(world_q.ARMY_ORDER)(ArmyMuster(w.records[rid].subject_matter, fit))


def _standing_order(w: Any, faction: Optional[str], place: Optional[str]) -> Optional[FieldOrder]:
    """CP-T04-02: the standing order `faction`'s line fights `place` under, as the module reads it, or `None`.
    Which Record is `world_q.standing_order`'s (the newest holder edge among the faction's seats' orders about the place);
    this lifts its content into the typed `FieldOrder` and decides nothing."""
    rec = world_q.standing_order(w, faction, place)
    return None if rec is None else FieldOrder(rec.subject_matter[ORDER_ROLE_KEY], rec.subject_matter[ORDER_RETREAT_KEY])


def field_input(w: Any, claimants: list, other: list, rung: str,
                factions: tuple = (None, None), origin_place: Optional[str] = None) -> MassBattleInput:
    """THE HOST INPUT BUILDER (plan position `31c`, A-25): `World` -> the frozen record the field reads.

    Reads `w.persons` (each side member's `weight`, and the stances `_side_stance` reads), the rung
    ancestry (`_territory_of`, at the target and at the claimants' homes for `_origin_of`), the
    target's fortification, the creeds' Propositions (`_creed_referent`) and `w.fixtures`, and nothing
    else; the module that consumes the record never sees `World`. Its precondition is the adapter's
    PARTY-GAP checks and a non-empty defending side (`resolve`, below). A member id `World` does not
    hold contributes no weight, as `resolve_field` read it before the split.

    MB-05r: `origin` is the World half of the river-crossing fact; whether the line from it to the
    target crosses a river is the geography's, which the module reads (`terrain.py::river_crossed`) off
    the record's `geography` -- the file `data/geography.py` reads once per process; the module opens none.
    MB-03: `loyalties` and `loyalty_gain` are the build-time loyalty rows and the fixture gain; what
    they do to the morale-start is `massbattle._morale_start`'s.
    CP-T04-05: `walls_dr` is the `field_walls_dr` fixture times `fort_level`, floored; `None` stays `None`.
    CP-T04-01: `members` are the person ids beside `weights` (the same test, so they align) and `units` is the
    `field_units` fixture (`H-359`), handed on unread; the module reads them only on its `person` arm.
    ED-IN-0306 phase 3: `factions` is `(attacker, defender)`, each side's faction Proposition id or `None`;
    each side whose faction holds an army Record fights as that Record's order of battle
    (`_order_of_battle`). Neither side having one leaves `orders_of_battle` `None`, the record exactly as it was.
    B17.03: `condition_scale` is the `condition_scale` fixture, the body scale the module quantises each survivor share onto.
    CP-T04-02 (`H-361`): `orders` is each side's STANDING ORDER (`_standing_order`): the attacker's about
    `origin_place` (the settlement it marched from, `world_q.march_origin`), the defender's about `rung` (the target). A
    side whose faction's seats hold no order about its place reads `None`; neither side having one leaves `orders` `None`,
    the record exactly as it was."""
    def members(side: list) -> tuple:
        return tuple(pid for pid in side if pid in w.persons)

    def weights(side: list) -> tuple:
        return tuple(w.persons[pid].weight for pid in members(side))    # the two align by construction
    oobs = (_order_of_battle(w, factions[0], claimants), _order_of_battle(w, factions[1], other))
    orders = (_standing_order(w, factions[0], origin_place), _standing_order(w, factions[1], rung))
    fort = world_q.fortification_of(w, rung) if w.rungs[rung].kind in SUBTREE_OCCUPATION_KINDS else 0.0
    return MassBattleInput(
        weights=(weights(claimants), weights(other)),
        territory=_territory_of(w, rung),
        # Walls are a settlement's: a field fought AT a territory is a field battle in the territory's own terrain
        # (`fortification_of` averages every garrison in a subtree and any value above 0 is WALLS, which overrides
        # terrain), ED-IN-0306 phase 5.
        fort_level=fort,
        stances=(_side_stance(w, claimants), _side_stance(w, other)),
        # CP-T04-05: graded walls. `None` (shipped) is today's flat row; else the fixture's value scaled by the garrison's
        # condition, FLOORED (`int`, never `round`: banker's rounding gives 3 x 0.5 -> 2 and 1 x 0.5 -> 0).
        walls_dr=None if (dr := w.fixtures.get("field_walls_dr")) is None else int(dr * fort),
        origin=_origin_of(w, claimants),
        loyalties=(_side_stance(w, claimants, _creed_referent), _side_stance(w, other, _creed_referent)),
        loyalty_gain=w.fixtures.get("field_morale_loyalty_gain"),
        geography=geography(),
        condition_scale=w.fixtures.get("condition_scale"),
        orders_of_battle=None if oobs == (None, None) else oobs,
        members=(members(claimants), members(other)),
        units=w.fixtures.get("field_units"),
        orders=None if orders == (None, None) else orders)


def _causing_act(w: Any, causes: list) -> Any:
    """The marching act, or `None`. `contest()` hands this provider `causes = [a.id]`, never the act: the act is
    found in `w.acts` by `state/attribution.py::causing_act`'s first-match rule over those ids (the fold appends the
    act before it folds it, `loop/resolve.py::resolve`)."""
    return next((w.acts.get(c) for c in causes if w.acts.get(c) is not None), None)


def _seat_treasury(w: Any, via: Optional[str]) -> Optional[str]:
    """v9 IN-52: THE ATTACKER'S TREASURY -- the rung of the office a marching act is exercised through (`Act.via`),
    the treasury `requisition` fills (`loop/effects_governance.py::_eff_requisition`'s `seat.rung`), or
    `None` for an act exercising no seat or a rungless seat."""
    office = w.offices.get(via) if via else None
    rid = office.rung if office is not None else None
    return rid if rid in w.rungs else None


def _defender_treasury(w: Any, rung: str) -> Optional[str]:
    """v9 IN-52 [ASSUMPTION LF-2, delegated-ruled]: THE DEFENDER'S TREASURY -- the nearest held rung at or
    above the target, the walk `world_q.holder_faction_of` makes (`world_q.governing_hold`, its one owner;
    it traces nothing), or `None` where nothing up the chain is held."""
    t = world_q.governing_hold(w, rung)
    return t.object if t is not None and t.object in w.rungs else None


def provision_input(w: Any, weight: int, treasury: Optional[str], eaten: tuple = ()) -> ProvisionInput:
    """THE PROJECTION `settlements.provision` reads (v9 IN-52), for one side: its Σ weight, its treasury's
    `Rung.stores` in their own order (`()` for no treasury rung), the `subsistence_weight` ration sorted by
    kind, and the `field_provisioning` fixture (`H-241`; `False`, shipped, is the control arm). Read-only.

    `eaten`: `((kind, units), ...)` another side has already consumed from THIS treasury in the same field
    (the defender's treasury when it is the attacker's own rung), subtracted from the projected stores so one
    store is never eaten twice. No floor is applied (the entry fields 0 on a non-positive store); `()` leaves
    the projection exactly as it was."""
    stores = tuple((w.rungs[treasury].stores or {}).items()) if treasury is not None else ()
    if eaten:
        less = dict(eaten)
        stores = tuple((kind, units - less.get(kind, 0)) for kind, units in stores)
    ration = tuple(sorted((w.fixtures.get("subsistence_weight") or {}).items()))
    return ProvisionInput(weight, stores, ration, bool(w.fixtures.get("field_provisioning")))


def _fielded_by(inp: MassBattleInput) -> tuple:
    """WHO FOUGHT, per side: the cohorts a side fought as an order of battle drew its troops from, else `None`
    (everybody mustered, as it always did). `(None, None)` when neither side has an order of battle."""
    if inp.orders_of_battle is None:
        return (None, None)
    return tuple(None if o is None else o.cohorts for o in inp.orders_of_battle)


def _fed(w: Any, inp: MassBattleInput, treasuries: tuple) -> list:
    """v9 IN-52, THE LEVY-TO-FIELD FEED [LF-1..LF-3]: each side's fielded troops are `settlements.provision`'s
    answer on its treasury, reached by role string; `resolve_field` sizes each Army by them, and
    `_eff_march` debits each side's `consumed` from the treasury named beside it. With `field_provisioning`
    off (shipped) the entry returns `troops = Σ weight` and `consumed = ()`: the field and the world as
    they were. An unprovisioned side fields 0, which `resolve_field`'s crash floor lifts (A16).
    ONE TREASURY FOR BOTH SIDES (the defender's held rung is the attacker's seat rung): the attacker eats
    first, attacker-then-defender being the order `_ration_debits` writes, and each side is provisioned
    NET of what its treasury has already had eaten this field, so the debit never exceeds the store. A
    side with no treasury (`None`) projects no stores and consumes `()`, so it nets nothing.
    `treasuries` is `(attacker's, defender's)`. `field_estimate` sizes the sides the way the fold does through
    this; read-only."""
    prov = composition.require(world_q.PROVISION)
    fed, eaten = [], {}
    for t, side, drawn in zip(treasuries, inp.weights, _fielded_by(inp)):
        # An army eats what it drew its troops from (the cohorts' weight), not everyone mustered beside it.
        weight = sum(w.persons[pid].weight for pid in drawn if pid in w.persons) if drawn is not None else sum(side)
        p = prov(provision_input(w, weight, t, eaten.get(t, ())))
        eaten[t] = p.consumed
        fed.append(p)
    return fed


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[Draw] = None, rung: Optional[str] = None,
            effort: int = 0, host: Any = None, via: Optional[str] = None, seat: Optional[str] = None) -> dict:
    """CALL the mass-battle engine. Returns what it said; decides nothing itself. `seat` (B21.61) is accepted and NOT USED HERE: the seam's
    call is uniform.

    `effort` (CP-T01-05) is accepted and NOT USED HERE: the seam's call is uniform, and a field battle has no
    scene slots to spend. `host` (v10 REM-31) is accepted
    and NOT USED HERE either: mass battle's PLAYABLE mode would read this same keyword, not a second shape.

    `claimants`: one side's `PersonId[]`, expected already resolved (§C.5.1) by whoever called
    `contest()`: `loop/sides.py::sides_of` builds them for a `march`.
    `subject`: the OTHER side's faction Proposition id, or `None` for no opposing side (v9 IN-13:
    a relocation or an arrival at unheld land), which resolves `Unopposed`.
    `rung`: where the defence is scoped (`ED-IN-0279` clause (a)) -- `subject`'s faction is
    resolved to its `members` (`faction_q.resolve`) and THEN
    INTERSECTED with presence at `rung`'s subtree (`queries/world_q.mustered`), per `04 §C.5.1`'s
    own pseudocode: *"squad combat: the squad is `members ∩ present-at-rung`"*. Without the
    intersection a field battle would defend with a faction's ENTIRE membership wherever it
    stands. REQUIRED: a caller with no rung has no
    place to defend, which is a PARTY-GAP exactly like a caller with no claimants.

    `result` is the module's frozen `FieldOutcome` (B17.03), or `None` where no field was fought (`Unopposed`, `Invested`); the
    four `FIELD_FLAGS` are lifted from its two sides to the top level for `degree_of`, and `field_degree` grades the outcome.
    B17.04: a field the module refuses (`resolve_field` returns a dict: `SCALE-GAP`, or `PARTY-GAP` for two sides of nobody) is
    that dict with this provider named, a refusal `seam/contest.py` folds and not a result."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a field battle needs at least one claimant",
                    module=_PROVIDER)
    if not rung:
        return dict(status="PARTY-GAP", why="a field battle needs a place to scope the "
                    "defending side to (rung); none given", module=_PROVIDER)
    # NO OPPOSING FACTION IS `Unopposed`, NOT A PARTY GAP (v9 IN-13). `loop/sides.py::sides_of` names
    # `subject = None` for ONE case only -- the target's
    # holder is the marcher's own faction, or nobody holds it -- and H-149's refusal rides an empty
    # `claimants` instead (above). With claimants and a rung given, an absent opposing faction has
    # nobody to muster, which is this function's empty-defence shape, read as such.
    other = world_q.mustered(w, rung, subject) if subject is not None else []
    parties = {"claimants": claimants, "subject_members": other}
    # CP-T04-06: THE POSTURE THE MARCH DECLARED (`rosters.yaml: march_postures`), a payload key read off the marching act, `storm`
    # for an act that declares none. Checked against the roster BEFORE anything is answered, so an unrostered posture (a
    # `besiege` while the roster ships `[storm]`) is a refusal to run and not a storm in disguise.
    act = _causing_act(w, causes)
    declared = act.payload.get(MARCH_POSTURE_KEY, STORM) if act is not None and isinstance(act.payload, dict) else STORM
    require_member(declared, rosters.MARCH_POSTURES, f"march posture {declared!r} is not in the roster", "CP-T04-06",
                   law="`field_casualty_model`'s own precedent -- an unrecognised posture silently falling back to a storm "
                       "would make every measurement of `besiege` read the control")
    if not other:
        # ⚠ AN EMPTY DEFENDING SIDE IS `Unopposed`, NOT A CALL TO `resolve_field`
        # (`ED-IN-0279` clause (a)). `resolve_field`'s own docstring: *"AN EMPTY `side_b` gets
        # `_MIN_TROOPS`' crash-avoidance floor, not an invented auto-win... what an empty
        # defending force MEANS is eligibility policy for whichever verb calls this."* This
        # wrapper is that caller's derivation half: it does not decide what an unopposed march
        # means for the game, but it does not launder "nobody mustered" into a fabricated fight
        # against a floor-sized phantom unit either. `unopposed` (B17.01 deleted `attacker_wins`) is top-level so
        # `seam/ladder.py::field_degree` can grade this without opening `result`.
        return dict(status="RESOLVED", module=_PROVIDER, resolver="d_sigma",
                    **_NO_FLAGS, unopposed=True,
                    result=None,
                    winner=claimants, parties=parties)
    if declared == BESIEGE:
        # CP-T04-06, AN OPPOSED SIEGE: THE ARMY SITS BEFORE THE WALLS AND NO BATTLE IS RUN -- no engine call, so no draw is
        # consumed and nobody is hurt or moved. Graded `Invested` (`seam/ladder.py::field_degree`, off the lifted `invested`
        # marker); `_eff_march` wears the garrison. An empty defence never reaches here: it answered `Unopposed` above, as a storm.
        return dict(status="RESOLVED", module=_PROVIDER, resolver="d_sigma",
                    **_NO_FLAGS, unopposed=False, invested=True,
                    result=None,
                    winner=[], parties=parties)
    # ⚠ THE ENTRY IS LOOKED UP BY THE ROLE THE PRIZE ROW NAMES (`module_entry:`), IN `MODULE_ENTRIES`,
    # as `sigma.py` and `combat.py` look theirs up: a call reaching here with the role
    # unregistered (no driver constructed in the process) is the typed `ENGINE-UNAVAILABLE`.
    entry, refusal = entry_for(prize, _PROVIDER)
    if entry is None:
        return refusal
    # The place and the two sides' morale are read here (`field_input`) and decided
    # there (`H-150` -- `fortification_of`'s caller on the battle path).
    # The walls' DR is the `field_walls_dr` fixture (`H-150`), `None` = A.9's
    # own number, which the module reads from its terrain table -- this adapter decides none of it.
    # ED-IN-0306 phase 3: the attacker's faction is the seat the marching act was exercised through (the one
    # `loop/sides.py::sides_of` mustered `claimants` under), the defender's is `subject`.
    inp = field_input(w, claimants, other, rung,
                      factions=(seat_faction(w, act.via) if act is not None else None, subject),
                      origin_place=world_q.march_origin(w, act.actor) if act is not None else None)
    if inp.orders_of_battle is not None:
        # WHO FOUGHT, for `_eff_march` to write casualties to (ED-IN-0306): a side fought as an order of battle drew
        # its troops from the cohorts it names, and the fight is theirs alone; a side with none (None) fought as
        # everybody mustered, as it always did.
        parties = {**parties, "fielded": _fielded_by(inp)}
    # v9 IN-52, THE LEVY-TO-FIELD FEED: `_fed` (above), the one place a side's fielded troops are read.
    treasuries = (_seat_treasury(w, act.via if act is not None else None), _defender_treasury(w, rung))
    fed = _fed(w, inp, treasuries)
    result = entry.fn(inp, rng, troops_a=fed[0].troops, troops_b=fed[1].troops)
    if isinstance(result, dict):
        # B17.04: the module's typed refusal (`SCALE-GAP`, or `PARTY-GAP` for two sides of nobody), on `PARTY-GAP`'s shape: handed on
        # whole with this provider named, so `seam/contest.py` folds it as the verb's refusal and no fight was run.
        return dict(result, module=_PROVIDER)
    return dict(status="RESOLVED", module=_PROVIDER, resolver="d_sigma",
                # v9 IN-52: `((treasury rung, consumed), ...)`, attacker then defender -- what `_eff_march`
                # debits (LF-3). Empty `consumed` on both sides while the arm is off.
                provision=tuple((t, p.consumed) for t, p in zip(treasuries, fed)),
                # ⚠ LIFTED TO TOP LEVEL, NOT LEFT NESTED UNDER `result`. `degree_of`
                # (`seam/ladder.py`) reads a provider's return directly -- `wound_state` and
                # `net`/`ob` are already top-level for the other two providers -- so a third,
                # nested-only shape would be the one branch `degree_of` could not reach without
                # a special case. The four flags are the module's own (`massbattle._grade`); the winner is the band's:
                # the claimants on `Won`, the defending side on `Lost`, nobody on `Drawn`.
                **field_flags(result), unopposed=False,
                result=result,
                winner={WON: claimants, LOST: other}.get(field_degree(result), []),
                parties=parties)


def field_estimate(w: Any, actor: str, via: Optional[str], target: Optional[str],
                   order: Optional[FieldOrder] = None) -> dict:
    """THE ODDS A FIELD WOULD DEAL, SAMPLED LIVE (CP-T04-08; `-08` AM-C-02's shape, `fight_estimate`'s sibling; MODE (a),
    THE PLAYER'S DISPLAY ONLY -- no NPC reads it, AQ-X1, and DELIBERATE never calls it).

    Builds the `MassBattleInput` `resolve` would build for `actor` marching on `target` through the seat `via` (the sides are
    `loop/sides.py::sides_of`'s, the same function the fold uses; the input is `field_input`'s; the troops are `_fed`'s),
    runs the module entry `resolve_field` `estimate_samples` times on the private stream `_estimate.rng_of` keys
    `(world_seed, tick, actor, "estimate")`, grades each result with `ladder.field_degree` (the one grader, so no second
    odds function and no band mapped here), and returns the SHARES `Won`, `Lost`, `Drawn` and `Unopposed` (`ESTIMATE_BANDS`; they
    sum to 1) beside `status` `ESTIMATED` and the `samples` run. An empty defending side is `Unopposed` with share 1 and
    `samples` 0: `resolve` deals it with no battle, so nothing is sampled. A refusal is `resolve`'s own dict
    (`PARTY-GAP`, `SCALE-GAP`, `ENGINE-UNAVAILABLE`).

    THE ORDER. `order` None reads the standing order as `field_input` reads it (`world_q.standing_order`, both
    sides'); a `FieldOrder` given is the ATTACKER's order for this estimate in the standing one's place (the defender's
    standing order stays), so the player can ask what a role or a retreat line would change before he issues it.

    ⚠ THE RNG IS PRIVATE AND IS NOT A SEASON DRAW (`_estimate.py`): `content_hash` and the draw counter are those of a
    world that never asked, and the shares are the distribution the field is drawn from, not a forecast of the battle the
    fold deals (it seeds its own from the causing act). Reads `World`; writes nothing."""
    if w.persons.get(actor) is None:
        return dict(status="PARTY-GAP", why=f"a march needs an actor who is a person; got {actor!r}", module=_PROVIDER)
    n = samples_of(w)
    claimants, subject, rung = sides_of(w, Act(id="estimate", actor=actor, verb="march", via=via), target, _PRIZE)
    if not claimants:
        return dict(status="PARTY-GAP", why="a field battle needs at least one claimant", module=_PROVIDER)
    other = world_q.mustered(w, rung, subject) if subject is not None else []
    if not other:
        return dict(status="ESTIMATED", module=_PROVIDER, samples=0, **{b: float(b == UNOPPOSED) for b in ESTIMATE_BANDS})
    entry, refusal = entry_for(_PRIZE, _PROVIDER)
    if entry is None:
        return refusal
    inp = field_input(w, claimants, other, rung, factions=(seat_faction(w, via), subject),
                      origin_place=world_q.march_origin(w, actor))
    if order is not None:
        inp = replace(inp, orders=(order, inp.orders[1] if inp.orders is not None else None))
    fed = _fed(w, inp, (_seat_treasury(w, via), _defender_treasury(w, rung)))
    rng = rng_of(w, actor)
    tally = dict.fromkeys(ESTIMATE_BANDS, 0)
    for _ in range(n):
        got = entry.fn(inp, rng, troops_a=fed[0].troops, troops_b=fed[1].troops)
        if isinstance(got, dict):
            # B17.04: a field the module refuses is refused every sample alike; `resolve`'s dict, as for any refusal here.
            return dict(got, module=_PROVIDER)
        tally[field_degree(got)] += 1
    return dict(status="ESTIMATED", module=_PROVIDER, samples=n, **{b: c / n for b, c in tally.items()})


@provider("estimate", _PROVIDER)
def estimate(w: Any, act: Any, claimants: list, target: Optional[str]) -> Optional[tuple]:
    """THIS PROVIDER'S CASE FOR `sigma.odds_of`, MODE (a): `field_estimate`'s shares as `(Won, Lost, Drawn, Unopposed)`
    (`ESTIMATE_BANDS`' order), or `None` for a refusal. `claimants` is `odds_of`'s own derivation of the act's parties,
    unused here beyond being non-empty (`field_estimate` derives the sides itself, from the act's actor, seat and target)."""
    got = field_estimate(w, act.actor, act.via, target)
    return tuple(got[b] for b in ESTIMATE_BANDS) if got["status"] == "ESTIMATED" else None
