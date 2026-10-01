"""`seam/wrappers/mass_battle.py` -- the `@provider("contest", "mass_battle")` M3 wires
(`ED-IN-0279`). What each block proves, and the control that stops it passing vacuously:

  1. END TO END THROUGH `contest()`, not just the provider function in isolation -- proves the
     manifest row, the `@provider` registration, and the dispatch in `seam/contest.py` all agree,
     which a unit test calling `resolve()` directly could not.
  2. `PARTY-GAP` ON AN EMPTY CLAIMANT LIST, A MISSING `subject` AND A MISSING `rung`, mirroring
     `seam/wrappers/combat.py`'s own PARTY-GAP discipline -- the provider derives a gap rather
     than fabricating a side.
  3. AN UNRESOLVABLE `subject` DOES NOT CRASH OR REFUSE. `faction_q.resolve` (read through
     `world_q.mustered`) returns an empty membership for an unknown proposition id (§B.6.1's own
     -- membership is `commit`, and there is none to find), which is INDISTINGUISHABLE from a real
     faction that mustered nobody at this `rung` -- both take the `Unopposed` path (M4,
     `ED-IN-0279` clause (a)) rather than reaching `resolve_field`'s crash-avoidance floor. That
     collapse is deliberate: an honest "nobody defended" beats a fabricated fight against a
     floor-sized phantom unit, which is what the pre-M4 version of this test proved happened
     instead -- superseded, not merely re-passing.
  4. THE `rung` SCOPING (M4, `ED-IN-0279` clause (a)) GENUINELY NARROWS, RATHER THAN PASSING
     VACUOUSLY. At `r_valoria` every member of `fac_guilds` happens to be present, so asserting
     against `world_q.mustered` there would pass whether or not the intersection ran. `fac_crown`
     at `set_s_002` is the falsifying case: 11 members total, exactly one present -- proving the
     defending side is the mustered subset, not the full membership `faction_q.resolve` alone
     would give.

  5. A GARRISONED DEFENDER FIGHTS DIFFERENTLY FROM AN UNGARRISONED ONE (plan position `20-iv`,
     `H-150`'s falsifier): the same army, target and seeds, with and without the target's garrison
     Site, every field FOUGHT (not `Unopposed`) and at least one resolving differently. Before
     `20-iv` this provider passed `terrain=None` and never read `fortification_of`, so every pair
     was identical. ⚠ WHAT MOVES IS THE ENGINE'S RESULT, NOT THE BAND: at this fixture's weights the
     2-man attacker loses either way, so the garrison raises the DEFENDERS' survivor fraction, which
     the season writes only on a `Won` band this scale does not reach (`test_march.py`'s
     `test_a_won_field...` docstring measured that).

Block 6 (`resolve_field` sums `Person.weight` per side into army SIZE, not quality) lives in
`tests/valoria/test_mass_battle_resolve_field.py`, not here: it needs `from systems.mass_battle...`
at module scope to reach `massbattle` directly for monkeypatching, and
`tests/valoria/test_engine_does_not_import_systems.py`'s `NESTED_BASELINE`/`BASELINE_TOTAL` ratchet
(zero `systems.*` imports anywhere under `engine/`, top-level OR function-local) applies to
`engine/season/tests/` -- this file is under `engine/`. `tests/valoria/test_mass_battle_d1_morale_baseline.py`
already imports `massbattle` the same way from that location; this follows it rather than being new.
"""
import random

from engine.season.harness.populated import build_realm
from engine.season.queries import faction_q, world_q
from engine.season.seam.contest import contest


def test_resolves_end_to_end_through_contest():
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    r = contest(w, "r_valoria", "a field", crown.members, depth=0, max_depth=3,
                causes=["test_cause"], subject="fac_guilds", rng=random.Random(7))
    assert r["status"] == "RESOLVED"
    assert r["module"] == "mass_battle"
    assert r["resolver"] == "dice_pool"
    # `result['degree']` (nested) is `massbattle.py`'s own non-canonical classification, kept for
    # introspection only -- see the provider's docstring for why there is no top-level `degree`
    # key: that would look like the token `degree_of` grades with, and it is not one yet.
    assert r["result"]["degree"] in {"Overwhelming", "Success", "Partial", "Failure"}
    assert "degree" not in r
    assert set(r["parties"]["claimants"]) == set(crown.members)
    # `world_q.mustered`, not raw `faction_q.resolve(...).members` -- see test 4 below for why the
    # distinction is checked on a case that can actually tell the two apart.
    assert set(r["parties"]["subject_members"]) == set(world_q.mustered(w, "r_valoria", "fac_guilds"))


def test_party_gap_on_empty_claimants_missing_subject_and_missing_rung():
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    w = build_realm(0)
    empty = provider_resolve(w, [], ["c"], "a field", subject="fac_guilds", rung="r_valoria")
    assert empty["status"] == "PARTY-GAP"
    missing_subject = provider_resolve(w, ["p_npc_008"], ["c"], "a field", subject=None,
                                        rung="r_valoria")
    assert missing_subject["status"] == "PARTY-GAP"
    missing_rung = provider_resolve(w, ["p_npc_008"], ["c"], "a field", subject="fac_guilds")
    assert missing_rung["status"] == "PARTY-GAP"


def test_unresolvable_subject_is_not_a_crash_or_a_second_refusal():
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    from engine.season.seam.ladder import field_degree
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    r = provider_resolve(w, crown.members, ["c"], "a field", subject="fac_this_does_not_exist",
                          rung="r_valoria", rng=random.Random(3))
    assert r["status"] == "RESOLVED"
    assert r["parties"]["subject_members"] == []
    # An unresolvable subject musters nobody, which is `Unopposed`, not a fought-and-won battle:
    # the pre-M4 version of this test asserted this reached `resolve_field`'s crash-avoidance
    # floor instead, which the `Unopposed` short-circuit now pre-empts (M4, `ED-IN-0279` clause
    # (a)) -- checked here rather than only in the dedicated unopposed test, since this is the
    # case that used to exercise the floor and must be shown to no longer need it.
    assert r["attacker_wins"] is True and r["unopposed"] is True
    assert field_degree(r) == "Unopposed"


def test_rung_scoping_excludes_members_not_present_at_the_target():
    """M4 (`ED-IN-0279` clause (a)), F6 of the planning pass, closed. `fac_crown` has 11 members
    and exactly one -- `p_npc_020` -- is present at `set_s_002`'s subtree; asserting the defending
    side equals the FULL faction would fail here where it would pass silently at `r_valoria` (test
    1 above), which is why this case exists rather than reusing that one."""
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    assert len(crown.members) > 1, "the fixture no longer gives fac_crown more than one member"
    mustered = world_q.mustered(w, "set_s_002", "fac_crown")
    assert 0 < len(mustered) < len(crown.members), (
        f"set_s_002 no longer gives a strict subset of fac_crown's {len(crown.members)} members "
        f"({mustered}); pick a rung/faction pair that still does")
    r = provider_resolve(w, ["p_npc_008"], ["c"], "a field", subject="fac_crown",
                          rung="set_s_002", rng=random.Random(11))
    assert r["status"] == "RESOLVED"
    assert set(r["parties"]["subject_members"]) == set(mustered)
    assert set(r["parties"]["subject_members"]) != set(crown.members)


def test_a_real_faction_that_musters_nobody_at_the_rung_is_unopposed():
    """M4 (`ED-IN-0279` clause (a)). Distinct from the unresolvable-subject test above: `fac_crown`
    genuinely exists and has members, but none is present at `set_s_003`'s subtree, so this is the
    case a settlement-defence read actually meets -- a real holder faction whose people are
    elsewhere, not a typo'd faction id."""
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    from engine.season.seam.ladder import field_degree
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    assert crown.members, "fac_crown has no members at all; pick a faction that does"
    mustered = world_q.mustered(w, "set_s_003", "fac_crown")
    assert not mustered, (
        f"set_s_003 no longer gives fac_crown zero mustered ({mustered}); pick a rung that does")
    r = provider_resolve(w, ["p_npc_008"], ["c"], "a field", subject="fac_crown",
                          rung="set_s_003", rng=random.Random(13))
    assert r["status"] == "RESOLVED"
    assert r["attacker_wins"] is True and r["unopposed"] is True
    assert field_degree(r) == "Unopposed"
    assert r["parties"]["subject_members"] == []


def test_a_garrisoned_defender_resolves_differently_from_an_ungarrisoned_one():
    """PLAN POSITION `20-iv` -- `H-150`'s falsifier. `set_s_036` (Church of Solmund, territory T9)
    carries the one garrison Site `build_realm` seeds per settlement; the bare world deletes it, so
    `fortification_of` reads 1.0 against 0.0. Eight seeds, both worlds, the same 2-man Crown army.
    Every one is a FOUGHT field (asserted, so this cannot pass on `Unopposed` short-circuits), and
    the garrison changes at least one result and never leaves the defenders with fewer survivors.
    Pre-`20-iv`, `differs` was 0: the provider never read the garrison."""
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    target = "set_s_036"
    garrisoned, bare = build_realm(0), build_realm(0)
    for sid in [sid for sid, s in bare.sites.items() if s.kind == "garrison" and s.rung == target]:
        del bare.sites[sid]
    assert world_q.fortification_of(garrisoned, target) > 0.0, "the fixture no longer garrisons the target"
    assert world_q.fortification_of(bare, target) == 0.0, "deleting the garrison left a fortification"
    attackers = world_q.mustered(garrisoned, "set_s_014", "fac_crown")
    assert attackers and attackers == world_q.mustered(bare, "set_s_014", "fac_crown")
    fought = differs = 0
    for seed in range(8):
        walled = provider_resolve(garrisoned, attackers, ["c"], "a field",
                                  subject="fac_church_of_solmund", rung=target,
                                  rng=random.Random(seed))
        open_ = provider_resolve(bare, attackers, ["c"], "a field",
                                 subject="fac_church_of_solmund", rung=target,
                                 rng=random.Random(seed))
        for r in (walled, open_):
            assert r["status"] == "RESOLVED" and r["unopposed"] is False, f"seed {seed}: not fought: {r}"
        fought += 1
        differs += walled["result"] != open_["result"]
        assert walled["result"]["defender_size_pct"] >= open_["result"]["defender_size_pct"], (
            f"seed {seed}: the walls left the defenders FEWER survivors: {walled} vs {open_}")
    assert fought >= 8, f"only {fought} fields were fought"
    assert differs >= 1, "a garrisoned target fought identically to a bare one on every seed (H-150)"
