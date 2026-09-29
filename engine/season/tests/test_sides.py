"""`loop/sides.py` -- `sides_of`, and `queries/world_q.holder_faction_of` it depends on
(M4, `ED-IN-0279` clause (a)).

What each test proves, and the control that stops it passing vacuously:

  1. THE NON-`mass_battle` BRANCH IS BYTE-IDENTICAL TO THE PRE-M4 FOLD. `loop/resolve.py`'s own
     `_target`/`_parties` construction, before this module existed, built exactly
     `[a.actor] + ([_target] if _target and _target != a.actor else [])` with `subject=_target`
     and `rung` from the bare-string placeholder. Extracting the rule must move no golden.
  2. DISPATCH IS ON THE PRIZE'S OWN MANIFEST MODULE, NEVER ON WHAT `target` LOOKS LIKE. This
     module's first writing dispatched on whether `target` resolved to a person or a rung, and
     the corpus suite (`ARC-40`, a `tell` whose Candidate subject binds to `r_realm`, the
     campaign root RUNG) found it first: a rung-shaped subject is not unique to `march`, so that
     dispatch routed a `tell` into the army-muster branch and produced `claimants=[]`, which
     `seam/contest.py` correctly refuses (`Forbidden: contest with no claimants`). Test 2 is that
     exact case, run through `sides_of` directly rather than the full corpus, and test 3 confirms
     `a standing`/`a proposition` (the other two contested prizes) take the same non-`mass_battle`
     path a rung-shaped subject would have broken.
  3. THE `mass_battle` BRANCH DERIVES A REAL ARMY AND A REAL DEFENDER, not an empty shape that
     happens to type-check. Caught the same way as (2): `Office.faction` is a display value
     (`'Crown'`), not the proposition id `mustered`/`members` key on -- an untested version of
     this module would have shipped an always-empty army silently. `holder_faction_of` needed
     its own correction the same way: `faction_holding` takes a PERSON (the holder), not a rung,
     and a settlement is never itself the object of a `hold` in this corpus.
  4. AN UNHELD TARGET (`r_valoria`, the realm root -- nothing holds a realm) gives `subject=None`
     for a REAL reason, not a bug indistinguishable from one: contrasted against test 3's real
     holder at a real settlement.
  5. AN ACTOR WITH NO SEAT MUSTERS AN EMPTY ARMY -- never raises. `contest()`'s own PARTY-GAP
     discipline is the caller's to apply downstream.
"""

from engine.season.harness.populated import build_realm
from engine.season.loop.sides import sides_of
from engine.season.queries import world_q
from engine.season.state.carriers import Act


def test_non_mass_battle_branch_matches_the_pre_m4_fold_exactly():
    w = build_realm(0)
    a = Act(id="a1", actor="p_npc_008", verb="fight", payload={"subject": "p_npc_009"})
    claimants, subject, rung = sides_of(w, a, "p_npc_009", "the body")
    assert claimants == ["p_npc_008", "p_npc_009"]
    assert subject == "p_npc_009"
    assert rung == "R"          # the pre-M4 placeholder: a.payload is a dict, not a bare string


def test_non_mass_battle_branch_does_not_duplicate_the_actor_as_their_own_target():
    w = build_realm(0)
    a = Act(id="a1", actor="p_npc_008", verb="tell", payload={"subject": "p_npc_008"})
    claimants, subject, rung = sides_of(w, a, "p_npc_008", "a standing")
    assert claimants == ["p_npc_008"], "an actor named as their own subject must not appear twice"
    assert subject == "p_npc_008"


def test_a_rung_shaped_subject_on_a_non_mass_battle_prize_does_not_route_to_the_army_branch():
    """THE FALSIFYING CASE FOR THE DEFECT THIS MODULE SHIPPED FIRST (found on `ARC-40`'s `tell`,
    whose Candidate subject bound to that fixture's campaign-root rung, reproduced here against
    `build_realm`'s own root): `tell`'s prize is `a standing`, not `a field`, so a Candidate
    subject binding to `r_valoria` -- a real Rung -- must still take the two-person shape. Before
    the fix this produced `claimants=[]` and `seam/contest.py` raised `Forbidden`; now it must
    not."""
    w = build_realm(0)
    assert "r_valoria" in w.rungs and "r_valoria" not in w.persons, (
        "the fixture no longer names r_valoria as a rung distinct from every person")
    a = Act(id="a1", actor="p_npc_008", verb="tell", payload={"subject": "r_valoria"})
    claimants, subject, rung = sides_of(w, a, "r_valoria", "a standing")
    assert claimants == ["p_npc_008", "r_valoria"], (
        "a standing's sides are the pre-M4 two-person shape whatever `target` looks like")
    assert subject == "r_valoria"


def test_mass_battle_branch_derives_a_real_army_and_a_real_defender():
    """`p_npc_033` holds `off_npc_033` (`fac_crown`, display value `'Crown'`), lives at
    `set_s_014`, and `set_s_014` musters exactly `p_npc_033`/`p_npc_035` under `fac_crown` --
    verified against the live fixture, not assumed from the office's own `remit_acts`.
    `set_s_002` is held (via `terr_T1`) by `p_npc_020`, who commits to `fac_crown` alone -- a
    DIFFERENT settlement's holder, so this is not the same faction answering by coincidence."""
    w = build_realm(0)
    actor = "p_npc_033"
    office = w.offices["off_npc_033"]
    assert "dispatch" in office.remit_acts
    assert office.faction == "Crown", "the fixture's office no longer carries this display value"
    origin_army = world_q.mustered(w, "set_s_014", "fac_crown")
    assert origin_army, "set_s_014 no longer musters anyone under fac_crown"
    a = Act(id="a1", actor=actor, verb="march", payload={"subject": "set_s_002"}, via="off_npc_033")
    claimants, subject, rung = sides_of(w, a, "set_s_002", "a field")
    assert set(claimants) == set(origin_army)
    assert subject == "fac_crown"
    assert rung == "set_s_002"


def test_holder_faction_of_walks_to_the_nearest_held_ancestor():
    """A settlement is never itself the object of a `hold` in this corpus -- `hold_force`
    returns `None` for one directly -- so `holder_faction_of` must climb to `set_s_002`'s
    containing territory (`terr_T1`) before it finds a holder. Asserted at both ends: the
    settlement's own `hold_force` is empty, and the walk still resolves."""
    w = build_realm(0)
    assert world_q.hold_force(w, "set_s_002") is None
    assert world_q.holder_faction_of(w, "set_s_002") == "fac_crown"


def test_an_unheld_target_gives_no_defending_faction():
    """`r_valoria`, the realm root: nothing holds a realm. Contrasted with the real holder in
    the test above, so `None` here is checked against a case that DOES resolve, not merely
    asserted in isolation."""
    w = build_realm(0)
    assert world_q.holder_faction_of(w, "r_valoria") is None
    a = Act(id="a1", actor="p_npc_033", verb="march", payload={"subject": "r_valoria"},
            via="off_npc_033")
    claimants, subject, rung = sides_of(w, a, "r_valoria", "a field")
    assert subject is None
    assert rung == "r_valoria"


def test_an_actor_with_no_seat_musters_an_empty_army_not_a_raise():
    w = build_realm(0)
    a = Act(id="a1", actor="p_npc_033", verb="march", payload={"subject": "set_s_002"}, via=None)
    claimants, subject, rung = sides_of(w, a, "set_s_002", "a field")
    assert claimants == [], "no via means no office, no faction, and so no army to muster"
    assert subject == "fac_crown", "the DEFENDING side is unaffected by the actor's own gap"
    assert rung == "set_s_002"


def test_no_target_falls_through_to_the_non_mass_battle_default():
    """`target=None`: an uncontested verb's payload, or a hand-built act naming no subject."""
    w = build_realm(0)
    a = Act(id="a1", actor="p_npc_008", verb="work", payload=None)
    claimants, subject, rung = sides_of(w, a, None, "the body")
    assert claimants == ["p_npc_008"]
    assert subject is None
    assert rung == "R"
