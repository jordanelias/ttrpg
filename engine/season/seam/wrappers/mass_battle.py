"""THE MASS-BATTLE PROVIDER -- the host adapter and the host INPUT BUILDER for the `mass_battle` module's
entry, `modules/mass_battle/massbattle.py::resolve_field` (plan position `31c`, A-25).

PLAN POSITION `31c` SPLIT THIS MODULE AS `31a` SPLIT `sigma.py`. What stays here is the HOST: the input
builder `field_input` (`World` -> `queries/inputs.py::MassBattleInput`: each side's member weights, the
place, its fortification, each side's stance, the walls fixture) and the adapter `resolve`, which keeps
the PARTY-GAP refusals and the `Unopposed` branch, calls the module entry the prize row names
(`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its composition row, `entry: verb_call`,
`verb: march`) and lifts what comes back. The fight itself -- the Units, the terrain row, the battle and
its survivor-ratio grade -- is the module's, reached by string. `loop/sides.py` stays host too: it builds
the claimants the record's weights are read for. Below, `massbattle`'s functions are the ENTRY's
module's since `31c`.

Wired M3 of the driver-retirement plan
(`ED-IN-0279`); `rosters.yaml`'s "a field" row previously had a `module:` and NO `provider:`,
whose own comment said the absence WAS the row -- *"sides need `faction_q.resolve` (04 §C.5.1)"*.
M2 built `faction_q.resolve`; this is the call that reads it.

⚠ **THE `claimants`/`subject`/`rung` SPLIT BELOW IS SETTLED, AND WHAT STILL SUPPLIES IT IS NOT.**
`seam/contest.py`'s S39.1 is unconditional: *"claimant[] is PERSONS, ALWAYS. Not factions, not
units, not sides"*, and `seam/wrappers/sigma.py` already types `subject` as sometimes naming
something that is NOT a person, so this module's shape needed no new seam-level concept: it reuses
`subject` for the other side's faction Proposition id (as always) and, new at M4 (`ED-IN-0279`
clause (a)), reads `rung` -- ALREADY a parameter of `contest()`, already passed at every call site,
unused until now -- to scope that faction's `members` down to who is actually PRESENT at the
target, via `world_q.mustered` (`04 §C.5.1`'s own *"squad combat: the squad is
`members ∩ present-at-rung`"*). `claimants` stays one side's already-resolved `PersonId[]` per
§C.5.1's *"sides = (faction_q.resolve(proj,A), faction_q.resolve(proj,B)) -- ONCE, before
provider.run"*.
**M4 BUILD STEP 5 CLOSED THIS.** `loop/sides.py::sides_of`, dispatched on the PRIZE's own manifest
`module` (never on `a.verb`, and never on what the target looks like -- see that module's own
docstring for the corpus case that made a shape-based dispatch unsafe), now builds the REAL
`claimants`/`subject`/`rung` for this prize: the actor's own muster at the origin, the target
rung's holder faction (`queries/world_q.holder_faction_of`), and the target rung itself. `kill /
wound` and `tell` keep their pre-M4 two-claimant shape unchanged, through `sides_of`'s other
branch, which is what "generalizing without changing their behaviour" meant.

⚠ **WHO ATTACKS, WHO DEFENDS, AND WHAT AN EMPTY DEFENDING SIDE MEANS ARE `march`'s OWN eligibility
and effects, RULED AND BUILT (M4, `ED-IN-0279` clause (b), 2026-09-28)** -- an empty defending side
is `Unopposed` (the `Unopposed` branch in `resolve` below), never an auto-win manufactured here.

⚠⚠ **WHAT A GARRISON DOES TO THIS FIGHT IS NOW READ, AND THE READ IS ALL THIS MODULE ADDS (plan
position `20-iv`, `H-150`).** Jordan's ruling (planning round 2) fixed garrison STRENGTH as a Site's
`condition` field, and `queries/world_q.py::fortification_of` reads it. Until `20-iv` nothing called
that function: this module passed `terrain=None` unconditionally, so a garrisoned settlement fought
exactly like an undefended one. `resolve()` now reads three facts about the fight off the world and
hands them on as plain values -- it decides none of what they do:
  * the TERRITORY the target sits in, `_territory_of` below: the nearest `territory`-kind rung up
    the target's ancestry, turned back into its geography row by `data/rosters.territory_id_of`
    (the one owner of that id relation, which `harness/populated.py` mints through);
  * its FORTIFICATION, `world_q.fortification_of` at the target;
  * each side's MORALE source, `_side_stance` below;
and, since plan position `20-v`, one injected value: the `field_walls_dr` fixture (`H-150`). Since MB-05r
and MB-03, two more facts and one more value: the attacking side's ORIGIN territory (`_origin_of`), each
side's build-time LOYALTY row (`_side_stance` with `_creed_referent`), and the
`field_morale_loyalty_gain` fixture.
What a fortification DOES is `massbattle.resolve_field`'s and `terrain.py`'s: any positive value
makes the field A.9's `WALLS` row, whose one number (defender +3 DR) the engine applies to `Unit.dr`
1:1 (an ASSUMPTION about the unit, `H-150`). The number is canon's, not invented here -- `None` in the
fixture leaves it where `terrain.py` authors it, and an int sweeps it -- which is why this
module may carry the read without deciding anything -- `seam/wrappers/combat.py` derives a party the same way and calls the
engine without deciding who picked the fight.

⚠ **`degree_of` (`seam/ladder.py`) NOW GRADES THIS RESULT, THROUGH A THIRD BRANCH RATHER THAN BY
MANUFACTURING A MARGIN (M4, `ED-IN-0279` clause (a)).** It does NOT grade `massbattle.py`'s own
survivor-ratio classification, which is still disclosed as *"NOT the canonical degree ladder ... a
bespoke post-hoc classification"* by that module's own header -- reconciling the two stays open
MB-lane work. What it grades is the top-level `attacker_wins`/`unopposed` this function lifts,
onto the three bands `march` writes on (`seam/ladder.py::field_degree`). Manufacturing a `net`/`ob`
from the survivor-ratio classification would have been the second resolver S27.2 refuses; reading
a marker this function already derives is not that.

⚠ **NO NEW `sys.path` SEAM, AND NO IMPORT OF THE MODULE.** `resolve_field` is reached by STRING: the
composition row `mass_battle.resolve_field` (`references/module_contracts.yaml`) names it, the registrar
resolves it at driver construction into `MODULE_ENTRIES`, and `resolve` below looks it up there by the
role its prize row names -- `engine/` never imports module code. `PATH_SEAM_ALLOWED`
(`tests/valoria/test_engine_does_not_import_systems.py`) keeps its one entry: the moved closure's own
imports are dotted `modules.mass_battle.*`, a package, so it needs no path seam.
"""
from __future__ import annotations

import random
from typing import Any, Optional

# `providers` is imported by module, as combat.py and sigma.py do (see their notes on the manifest
# import order); the entry lookup is `_entry.py`'s, which imports `registrar` and `registry` the same way.
from ...manifest.providers import provider
from ...data.geography import geography
from ...data.rosters import territory_id_of
from ...queries.inputs import MassBattleInput, ProvisionInput
from ...queries.person_q import stance_toward
from ...queries import world_q
from engine.substrate import composition
from ._entry import entry_for

_PROVIDER = "mass_battle"


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

    This is the writer's own rule read back, not a second one: `harness/populated.py` appends the
    row `(prop.subject, *cast.stance_from_loyalty(...))` exactly when the creed's mood is OUGHT, and a
    HOLDS faction (`Guilds`, `Schoenland`: no leader or template in canon) gets no row and reads `None`
    here -- `cast.loyalty`'s *"`None` FOR A FACTION WITH NO TEMPLATE, NEVER A DEFAULT"*. ⚠ The row
    names a PERSON, the creed's utterer, not the faction: that is why the morale row (`_eff_march`,
    on the faction id) and this one are two referents and are read and handed on separately."""
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
    crossing is derived and the field is what it was before MB-05r."""
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


def field_input(w: Any, claimants: list, other: list, rung: str) -> MassBattleInput:
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
    they do to the morale-start is `massbattle._morale_start`'s."""
    def weights(side: list) -> tuple:
        return tuple(w.persons[pid].weight for pid in side if pid in w.persons)
    return MassBattleInput(
        weights=(weights(claimants), weights(other)),
        territory=_territory_of(w, rung),
        fort_level=world_q.fortification_of(w, rung),
        stances=(_side_stance(w, claimants), _side_stance(w, other)),
        walls_dr=w.fixtures.get("field_walls_dr"),
        origin=_origin_of(w, claimants),
        loyalties=(_side_stance(w, claimants, _creed_referent), _side_stance(w, other, _creed_referent)),
        loyalty_gain=w.fixtures.get("field_morale_loyalty_gain"),
        geography=geography())


def _attacker_treasury(w: Any, causes: list) -> Optional[str]:
    """v9 IN-52: THE ATTACKER'S TREASURY -- the rung of the office the marching act exercised (`Act.via`),
    the treasury `requisition` fills (`loop/effects_governance.py::_eff_requisition`'s `seat.rung`), or
    `None` for an act exercising no seat, a rungless seat, or no act among `causes`.

    `contest()` hands this provider `causes = [a.id]`, never the act: the act is found in `w.acts` by
    `state/attribution.py::causing_act`'s first-match rule over those ids (the fold appends the act
    before it folds it, `loop/resolve.py::resolve`)."""
    act = next((w.acts.get(c) for c in causes if w.acts.get(c) is not None), None)
    office = w.offices.get(act.via) if act is not None and act.via else None
    rid = office.rung if office is not None else None
    return rid if rid in w.rungs else None


def _defender_treasury(w: Any, rung: str) -> Optional[str]:
    """v9 IN-52 [ASSUMPTION LF-2, delegated-ruled]: THE DEFENDER'S TREASURY -- the nearest held rung at or
    above the target, the walk `world_q.holder_faction_of` makes (`world_q.governing_hold`, its one owner;
    it traces nothing), or `None` where nothing up the chain is held."""
    t = world_q.governing_hold(w, rung)
    return t.object if t is not None and t.object in w.rungs else None


def provision_input(w: Any, weight: int, treasury: Optional[str]) -> ProvisionInput:
    """THE PROJECTION `settlements.provision` reads (v9 IN-52), for one side: its Σ weight, its treasury's
    `Rung.stores` in their own order (`()` for no treasury rung), the `subsistence_weight` ration sorted by
    kind, and the `field_provisioning` fixture (`H-241`; `False`, shipped, is the control arm). Read-only."""
    stores = tuple((w.rungs[treasury].stores or {}).items()) if treasury is not None else ()
    ration = tuple(sorted((w.fixtures.get("subsistence_weight") or {}).items()))
    return ProvisionInput(weight, stores, ration, bool(w.fixtures.get("field_provisioning")))


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None, rung: Optional[str] = None) -> dict:
    """CALL the mass-battle engine. Returns what it said; decides nothing itself.

    `claimants`: one side's `PersonId[]`, expected already resolved (§C.5.1) by whoever called
    `contest()`: `loop/sides.py::sides_of` builds them for a `march`.
    `subject`: the OTHER side's faction Proposition id, or `None` for no opposing side (v9 IN-13:
    a relocation or an arrival at unheld land), which resolves `Unopposed`.
    `rung`: where the defence is scoped (M4, `ED-IN-0279` clause (a)) -- `subject`'s faction is
    resolved to its `members` (`faction_q.resolve`, the same function M2 built) and THEN
    INTERSECTED with presence at `rung`'s subtree (`queries/world_q.mustered`), per `04 §C.5.1`'s
    own pseudocode: *"squad combat: the squad is `members ∩ present-at-rung`"*. Without the
    intersection a field battle would defend with a faction's ENTIRE membership wherever it
    stands -- the M4 planning pass's F6, closed here. REQUIRED: a caller with no rung has no
    place to defend, which is a PARTY-GAP exactly like a caller with no claimants.

    `result` carries `massbattle.py`'s own non-canonical survivor-ratio classification under
    `result['degree']`, kept for introspection; it is NOT the token `degree_of` grades with (see
    this module's docstring) and callers should not read it as one."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a field battle needs at least one claimant",
                    module=_PROVIDER)
    if not rung:
        return dict(status="PARTY-GAP", why="a field battle needs a place to scope the "
                    "defending side to (rung); none given", module=_PROVIDER)
    # v9 IN-13 (#453 §9.6 code edit (ii)): NO OPPOSING FACTION IS `Unopposed`, NOT A PARTY GAP. Since
    # the arrival, `loop/sides.py::sides_of` names `subject = None` for ONE case only -- the target's
    # holder is the marcher's own faction, or nobody holds it -- and H-149's refusal rides an empty
    # `claimants` instead (above). With claimants and a rung given, an absent opposing faction has
    # nobody to muster, which is this function's existing empty-defence shape, read as such.
    other = world_q.mustered(w, rung, subject) if subject is not None else []
    parties = {"claimants": claimants, "subject_members": other}
    if not other:
        # ⚠ AN EMPTY DEFENDING SIDE IS `Unopposed`, NOT A CALL TO `resolve_field` (M4,
        # `ED-IN-0279` clause (a)). `resolve_field`'s own docstring: *"AN EMPTY `side_b` gets
        # `_MIN_TROOPS`' crash-avoidance floor, not an invented auto-win... what an empty
        # defending force MEANS is eligibility policy for whichever verb calls this."* This
        # wrapper is that caller's derivation half: it does not decide what an unopposed march
        # means for the game, but it does not launder "nobody mustered" into a fabricated fight
        # against a floor-sized phantom unit either. `attacker_wins`/`unopposed` are top-level so
        # `seam/ladder.py::field_degree` can grade this without opening `result`.
        return dict(status="RESOLVED", module=_PROVIDER, resolver="dice_pool",
                    attacker_wins=True, unopposed=True,
                    result=dict(attacker_wins=True, degree="Unopposed",
                                attacker_size_pct=1.0, defender_size_pct=0.0),
                    winner=claimants, parties=parties)
    # ⚠ THE ENTRY IS LOOKED UP BY THE ROLE THE PRIZE ROW NAMES (`module_entry:`), IN `MODULE_ENTRIES`,
    # as `sigma.py` and `combat.py` look theirs up (`31a`, `31b`): a call reaching here with the role
    # unregistered (no driver constructed in the process) is the typed `ENGINE-UNAVAILABLE`.
    entry, refusal = entry_for(prize, _PROVIDER)
    if entry is None:
        return refusal
    # PLAN POSITION `20-iv`: the place and the two sides' morale, read here (`field_input`) and decided
    # there (`H-150` -- `fortification_of`'s caller on the battle path).
    # PLAN POSITION `20-v`: the walls' DR is the `field_walls_dr` fixture (`H-150`), `None` = A.9's
    # own number, which the module reads from its terrain table -- this adapter decides none of it.
    inp = field_input(w, claimants, other, rung)
    # v9 IN-52, THE LEVY-TO-FIELD FEED [LF-1..LF-3]: each side's fielded troops are `settlements.provision`'s
    # answer on its treasury, reached by role string; `resolve_field` sizes each Unit by them, and
    # `_eff_march` debits each side's `consumed` from the treasury named beside it. With `field_provisioning`
    # off (shipped) the entry returns `troops = Σ weight` and `consumed = ()`: the field and the world as
    # they were. An unprovisioned side fields 0, which `resolve_field`'s crash floor lifts (A16).
    prov = composition.require(world_q.PROVISION)
    treasuries = (_attacker_treasury(w, causes), _defender_treasury(w, rung))
    fed = tuple(prov(provision_input(w, sum(side), t)) for side, t in zip(inp.weights, treasuries))
    result = entry.fn(inp, rng, troops_a=fed[0].troops, troops_b=fed[1].troops)
    return dict(status="RESOLVED", module=_PROVIDER, resolver="dice_pool",
                # v9 IN-52: `((treasury rung, consumed), ...)`, attacker then defender -- what `_eff_march`
                # debits (LF-3). Empty `consumed` on both sides while the arm is off.
                provision=tuple((t, p.consumed) for t, p in zip(treasuries, fed)),
                # ⚠ LIFTED TO TOP LEVEL, NOT LEFT NESTED UNDER `result` (M4). `degree_of`
                # (`seam/ladder.py`) reads a provider's return directly -- `wound_state` and
                # `net`/`ob` are already top-level for the other two providers -- so a third,
                # nested-only shape would be the one branch `degree_of` could not reach without
                # a special case. `result['degree']` stays as `massbattle.py`'s own
                # non-canonical classification, kept for introspection only; it is NOT this.
                attacker_wins=result.get("attacker_wins"), unopposed=False,
                result=result,
                winner=(claimants if result.get("attacker_wins") else other),
                parties=parties)
