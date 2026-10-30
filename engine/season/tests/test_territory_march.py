"""ED-IN-0304 phase 4 -- A TERRITORY IS MARCHED ON, OCCUPIED AND SEIZED; A DEFENDED ONE IS NOT.

Jordan: if a faction's army defends its territory successfully there is no occupation and potential seizure of it by
the attacker; if it does not defend, the attacking army occupies the territory alongside its settlements and may seize
it. What the position built (`rosters.yaml`: `march_target_kinds` gained `territory`, `subtree_occupation_kinds`,
`raze_target_kinds`; `world_q.occupies`; `effects_shared.occupying_faction` reads it): the field is the same field, the
arrival is the same arrival, and the licence `seize` asks is OCCUPATION -- which a lost march never gives.

Fixture: `build_realm(0)` and `test_march.py`'s helpers. The Crown (`p_npc_033`, seat `off_npc_033`) marches on
`terr_T7` (Hafenmark's, nobody of Hafenmark's mustered under it: unopposed) and on `terr_T9` (the Church's, defended).
`p_npc_020` / `off_npc_020` is the Crown seat that seizes.
"""

from __future__ import annotations

from engine.season.data.rosters import MARCH_TARGET_KINDS, RAZE_TARGET_KINDS, SUBTREE_OCCUPATION_KINDS
from engine.season.harness.populated import build_realm
from engine.season.queries import world_q
from engine.season.state.carriers import Act, Tenure

from engine.season.loop.effects_combat import _not_yet_under

from .test_march import (CHURCH, CROWN, _fold_one, _march_act, _no_resident_crown, _resolve_one, _seize_kinds)

ACTOR, SEAT = "p_npc_033", "off_npc_033"
UNDEFENDED, DEFENDED, TOWN = "terr_T7", "terr_T9", "set_s_016"      # TOWN is under UNDEFENDED, held by Hafenmark


def _march(w, target, act_id="m1"):
    return [e.kind for e in _fold_one(w, _march_act(ACTOR, target, SEAT, act_id=act_id))]


def test_the_rosters_say_a_territory_is_marched_on_occupied_by_arrival_and_never_razed():
    assert "territory" in MARCH_TARGET_KINDS and "settlement" in MARCH_TARGET_KINDS
    assert SUBTREE_OCCUPATION_KINDS == {"settlement"} and SUBTREE_OCCUPATION_KINDS <= MARCH_TARGET_KINDS
    assert RAZE_TARGET_KINDS == {"settlement"}


def test_a_defended_territory_is_not_occupied_and_cannot_be_seized():
    w = _no_resident_crown(build_realm(0))
    assert world_q.holder_faction_of(w, DEFENDED) == CHURCH
    assert world_q.mustered(w, DEFENDED, CHURCH), "fixture: the Church has people under its territory to defend it"
    kinds = _march(w, DEFENDED)
    assert "field.lost" in kinds and "army.arrived" not in kinds, kinds
    assert not world_q.occupies(w, DEFENDED, CROWN), "a routed army occupies nothing"
    assert _seize_kinds(w, DEFENDED, act_id="s_def") == ["seize.refused"]
    assert world_q.holder_faction_of(w, DEFENDED) == CHURCH, "the defended territory changed hands"


def test_an_undefended_territory_is_occupied_by_the_arrival_and_the_attacker_may_seize_it():
    w = build_realm(0)
    # CONTROL, one change from the admitted seizure below: before the march the Crown occupies nothing there
    assert not world_q.occupies(w, UNDEFENDED, CROWN)
    assert _seize_kinds(w, UNDEFENDED, act_id="s_pre") == ["seize.refused"]
    kinds = _march(w, UNDEFENDED)
    assert "army.arrived" in kinds, kinds
    assert world_q.occupies(w, UNDEFENDED, CROWN)
    assert world_q.holder_faction_of(w, UNDEFENDED) == "fac_hafenmark", "an arrival wrote a title (R-6)"
    assert _seize_kinds(w, UNDEFENDED, act_id="s_post") == ["rung.seized"]
    assert world_q.holder_faction_of(w, UNDEFENDED) == CROWN


def test_the_settlements_in_an_occupied_territory_are_occupied_with_it():
    w = build_realm(0)
    assert world_q.holder_faction_of(w, TOWN) == "fac_hafenmark"
    _march(w, UNDEFENDED)
    assert not world_q.mustered(w, TOWN, CROWN), "vacuous if the army stands in the town itself"
    assert world_q.occupies(w, TOWN, CROWN), "the territory's settlements ride with it"
    assert _seize_kinds(w, TOWN, act_id="s_town") == ["rung.seized"]
    assert world_q.holder_faction_of(w, TOWN) == CROWN


def test_standing_in_one_town_does_not_occupy_the_territory_around_it():
    """THE CONTROL OF THE ABOVE, one change: the army arrives at the town and not at the territory. Reading a
    territory as occupied by subtree presence would let one won settlement seize the land round it."""
    w = build_realm(0)
    kinds = _march(w, TOWN)
    assert "army.arrived" in kinds and world_q.mustered(w, TOWN, CROWN), kinds
    assert world_q.occupies(w, TOWN, CROWN) and not world_q.occupies(w, UNDEFENDED, CROWN)
    assert _seize_kinds(w, UNDEFENDED, act_id="s_terr") == ["seize.refused"]
    assert world_q.holder_faction_of(w, UNDEFENDED) == "fac_hafenmark"


def _raze(w, target, act_id):
    return [e.kind for e in _resolve_one(w, Act(id=act_id, actor=ACTOR, verb="raze",
                                                payload={"subject": target}, via=SEAT))]


def test_an_occupied_territory_is_never_razed_but_an_occupied_settlement_still_is():
    taken = build_realm(0)
    _march(taken, UNDEFENDED)
    assert world_q.occupies(taken, UNDEFENDED, CROWN)
    assert _raze(taken, UNDEFENDED, "rz_t") == ["raze.refused"] and UNDEFENDED in taken.rungs
    # CONTROL, the same raze act on a settlement the army stands in
    town = build_realm(0)
    _march(town, TOWN)
    assert world_q.mustered(town, TOWN, CROWN)
    assert _raze(town, TOWN, "rz_s") == ["rung.razed"] and TOWN not in town.rungs


def test_an_army_housed_inside_the_territory_still_has_to_arrive_at_it():
    """`_not_yet_under` and `occupies` read the same fact: beneath a settlement is there, but a territory is occupied
    only AT it. An attacker housed in one of its towns therefore makes the journey (and so occupies), where it was
    skipped as "already there" and left the territory unoccupied. CONTROL, one change: the same man, the town as the
    target, needs no journey."""
    w = build_realm(0)
    for t in w.tenures:
        if t.subject == ACTOR and t.kind == "contain" and t.live:
            t.until = w.tick
    inside = sorted(world_q.descendants(w, TOWN))[0]
    w.add_tenure(Tenure("t_d1_inside", ACTOR, inside, "contain", w.tick))
    assert UNDEFENDED in world_q.ancestry(w, world_q.home_of(w)[ACTOR]), "fixture: the actor lives under the territory"
    assert _not_yet_under(w, [ACTOR], UNDEFENDED, ACTOR, SEAT) == [ACTOR]
    assert _not_yet_under(w, [ACTOR], TOWN, ACTOR, SEAT) == [], "control: under a settlement is already there"


def test_a_settlement_with_a_hold_of_its_own_does_not_ride_with_an_occupied_territory():
    """The settlements an occupied territory carries are the ones held THROUGH it. CONTROL first: the town is held
    through the territory and is occupied with it; then a third faction takes a hold of its own on the town and it
    stands alone, so the army on the territory does not reach it (and cannot seize it without a field)."""
    w = build_realm(0)
    _march(w, UNDEFENDED)
    assert world_q.governing_hold(w, TOWN).object == UNDEFENDED and world_q.occupies(w, TOWN, CROWN)
    churchman = world_q.members(w, CHURCH)[0]
    w.add_tenure(Tenure("t_d2_own_hold", churchman, TOWN, "hold", w.tick))
    assert world_q.governing_hold(w, TOWN).object == TOWN and world_q.holder_faction_of(w, TOWN) == CHURCH
    assert not world_q.mustered(w, TOWN, CROWN) and not world_q.occupies(w, TOWN, CROWN)
    assert world_q.occupies(w, UNDEFENDED, CROWN), "the territory itself is still occupied"


def test_a_territorys_occupation_carries_a_settlements_seizure_but_not_its_razing():
    """`raze` stays the act of the army IN the town. CONTROL: the same town, the army standing in it, is razed (the
    test above); here the army only holds the territory above it and the razing is refused."""
    w = build_realm(0)
    _march(w, UNDEFENDED)
    assert world_q.occupies(w, TOWN, CROWN) and not world_q.mustered(w, TOWN, CROWN)
    assert _raze(w, TOWN, "rz_t2") == ["raze.refused"] and TOWN in w.rungs
