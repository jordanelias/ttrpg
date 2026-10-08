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
  5b. THE WALLS' DR IS AN INJECTABLE FIXTURE (plan position `20-v`, `H-150`): `field_walls_dr` swept
     3 / 0 / 1 on block 5's fixture -- 0 reproduces the open field exactly (the control), 3 and 1
     differ from it and from each other, and 3 equals the unset default. Its open arm is fought with
     the territory read made `None` (`_fight_open`): since MB-05 the bare target's own territory, T9,
     is a live UPHILL field, so "no garrison" alone is no longer "open ground".
  7. AN UPHILL FIELD RESOLVES DIFFERENTLY FROM THE SAME FIELD ON OPEN GROUND (MB-05, A.9's Uphill row):
     block 5's bare fixture as found (T9 -> UPHILL) against itself with the territory read made `None`
     (OPEN_FLAT). The other two MB-05 rows have no provider test, and why is a finding, not an
     omission: RIVER_CROSSING needs a signal this provider cannot derive (it holds the target rung,
     not the march's origin) -- `resolve_field`'s own test is in `tests/valoria/test_mass_battle_terrain.py`;
     NARROW_PASS is not applied (`massbattle._run_and_grade`'s docstring says why it would change nothing).

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


def _bare(target):
    """`build_realm(0)` with `target`'s garrison Site deleted -- `fortification_of` reads 0, so the
    field is whatever row the target's territory resolves to (blocks 5 and 7). Block 5 fights it through
    `_fight_open` for the open-ground arm; block 7 reads the real territory."""
    w = build_realm(0)
    for sid in [sid for sid, s in w.sites.items() if s.kind == "garrison" and s.rung == target]:
        del w.sites[sid]
    assert world_q.fortification_of(w, target) == 0.0, "deleting the garrison left a fortification"
    return w


def _fight_open(monkeypatch, w, attackers, subject, target, seed):
    """The same fight with the provider's territory read made `None` -- `terrain_row_for_territory`'s
    no-modifier case, OPEN_FLAT, whatever the territory and fortification. Patched for this one call
    only, so a sibling arm in the same test reads the real territory."""
    from engine.season.seam.wrappers import mass_battle as wrapper
    with monkeypatch.context() as m:
        m.setattr(wrapper, "_territory_of", lambda _w, _rung: None)
        return wrapper.resolve(w, attackers, ["c"], "a field", subject=subject, rung=target,
                               rng=random.Random(seed))


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


def test_a_garrisoned_defender_resolves_differently_from_an_ungarrisoned_one(monkeypatch):
    """PLAN POSITION `20-iv` -- `H-150`'s falsifier. `set_s_036` (Church of Solmund, territory T9)
    carries the one garrison Site `build_realm` seeds per settlement; the bare world deletes it, so
    `fortification_of` reads 1.0 against 0.0. The bare arm is fought through `_fight_open`: T9 is UPHILL
    since MB-05, so a bare world on its real territory would compare WALLS against a hill, not walls
    against open ground. Eight seeds, both worlds, the same 2-man Crown army.
    Every one is a FOUGHT field (asserted, so this cannot pass on `Unopposed` short-circuits), and
    the garrison changes at least one result and never leaves the defenders with fewer survivors.
    Pre-`20-iv`, `differs` was 0: the provider never read the garrison."""
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    target = "set_s_036"
    garrisoned, bare = build_realm(0), _bare(target)
    assert world_q.fortification_of(garrisoned, target) > 0.0, "the fixture no longer garrisons the target"
    attackers = world_q.mustered(garrisoned, "set_s_014", "fac_crown")
    assert attackers and attackers == world_q.mustered(bare, "set_s_014", "fac_crown")
    fought = differs = 0
    for seed in range(8):
        walled = provider_resolve(garrisoned, attackers, ["c"], "a field",
                                  subject="fac_church_of_solmund", rung=target,
                                  rng=random.Random(seed))
        open_ = _fight_open(monkeypatch, bare, attackers, "fac_church_of_solmund", target, seed)
        for r in (walled, open_):
            assert r["status"] == "RESOLVED" and r["unopposed"] is False, f"seed {seed}: not fought: {r}"
        fought += 1
        differs += walled["result"] != open_["result"]
        assert walled["result"]["defender_size_pct"] >= open_["result"]["defender_size_pct"], (
            f"seed {seed}: the walls left the defenders FEWER survivors: {walled} vs {open_}")
    assert fought >= 8, f"only {fought} fields were fought"
    assert differs >= 1, "a garrisoned target fought identically to a bare one on every seed (H-150)"


def test_field_walls_dr_sweep_zero_is_the_open_field_and_three_and_one_differ(monkeypatch):
    """PLAN POSITION `20-v` -- `H-150`'s three-point sweep of the `field_walls_dr` fixture, on the
    `20-iv` fixture (`set_s_036`, the 2-man Crown army, garrisoned vs the garrison deleted).

      * `0` IS THE CONTROL: with no DR bonus the garrisoned field resolves IDENTICALLY to the bare
        one on OPEN GROUND on every seed -- DR is the only live difference between a walled and an
        open field, and the sweep removes it exactly (`==`, not `approx`). The bare arm is fought with
        the territory read made `None` (`_fight_open`): since MB-05 applies UPHILL, the bare target's
        own territory (T9) is no longer open ground, and comparing against it would test the hill.
      * `3` (A.9) AND `1` DIFFER from that control and from each other, and the defenders' survivors
        rise monotonically 0 -> 1 -> 3 on every seed -- so the fixture reaches the engine and its
        magnitude is what moves the result, rather than the sweep being three spellings of one run.
      * `3` EQUALS THE UNSET DEFAULT on every seed: the default is `None`, A.9's number read from
        `terrain.py`, and this is what shows the sentinel resolves to 3 (it would break the day the
        owner's literal moved off the 3 this test spells; H-150's `sweep: [3, 0, 1]` is a separate
        record, which this test does not read).

    Seeds 0..15, measured: the three arms differ on seeds 0, 2, 4, 10 (a one-off figure, not
    asserted -- the other twelve end identically at this scale, which `>= 1` tolerates and `checked`
    keeps honest). Pre-`20-v` `field_walls_dr` did not exist and the arm could not be set."""
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    target = "set_s_036"
    default, bare = build_realm(0), build_realm(0)
    for sid in [sid for sid, s in bare.sites.items() if s.kind == "garrison" and s.rung == target]:
        del bare.sites[sid]
    assert world_q.fortification_of(default, target) > 0.0, "the fixture no longer garrisons the target"
    assert world_q.fortification_of(bare, target) == 0.0, "deleting the garrison left a fortification"
    assert default.fixtures.get("field_walls_dr") is None, "the shipped default moved off A.9's own number"
    arms = {}
    for dr in (3, 0, 1):
        arms[dr] = build_realm(0)
        arms[dr].fixtures = arms[dr].fixtures.sweep("field_walls_dr", dr)
        assert arms[dr].fixtures.get("field_walls_dr") == dr
    attackers = world_q.mustered(default, "set_s_014", "fac_crown")
    assert attackers and attackers == world_q.mustered(bare, "set_s_014", "fac_crown")

    def fight(w, seed):
        r = provider_resolve(w, attackers, ["c"], "a field", subject="fac_church_of_solmund",
                             rung=target, rng=random.Random(seed))
        assert r["status"] == "RESOLVED" and r["unopposed"] is False, f"seed {seed}: not fought: {r}"
        return r["result"]

    checked = zero_differs_from_3 = zero_differs_from_1 = three_differs_from_1 = 0
    for seed in range(16):
        open_ = _fight_open(monkeypatch, bare, attackers, "fac_church_of_solmund", target, seed)
        assert open_["status"] == "RESOLVED" and open_["unopposed"] is False, f"seed {seed}: not fought"
        open_, dflt = open_["result"], fight(default, seed)
        r3, r0, r1 = fight(arms[3], seed), fight(arms[0], seed), fight(arms[1], seed)
        assert r0 == open_, f"seed {seed}: walls at DR 0 still differ from the open field: {r0} vs {open_}"
        assert r3 == dflt, f"seed {seed}: DR 3 is not the unset default: {r3} vs {dflt}"
        assert (r0["defender_size_pct"] <= r1["defender_size_pct"] <= r3["defender_size_pct"]), (
            f"seed {seed}: defender survivors are not monotone in the DR: {r0} {r1} {r3}")
        checked += 1
        zero_differs_from_3 += r3 != r0
        zero_differs_from_1 += r1 != r0
        three_differs_from_1 += r3 != r1
    assert checked == 16
    assert zero_differs_from_3 >= 1, "DR 3 resolved identically to the control on every seed"
    assert zero_differs_from_1 >= 1, "DR 1 resolved identically to the control on every seed"
    assert three_differs_from_1 >= 1, "DR 3 and DR 1 resolved identically on every seed"


def test_an_uphill_field_resolves_differently_from_the_same_field_on_open_ground(monkeypatch):
    """MB-05 -- A.9's Uphill row ("Defender +1D Def; attacker −1D Off"), through the provider.

    `set_s_036` sits in T9, whose anchor resolves UPHILL once its garrison is deleted
    (`tests/valoria/test_mass_battle_terrain.py` pins T9 -> UPHILL; this file may not import the lookup).
    The SAME bare world, army and seeds are fought twice: as found, and with the territory read made
    `None` (`_fight_open`, OPEN_FLAT) -- the row is the only difference between the arms.

    THE FALSIFIER, BOTH WAYS. Before MB-05 the row was identified and not applied, and the two arms were
    EQUAL on all 16 seeds (measured 2026-10-08, CI's Python 3.11); after, they differ on seeds 0, 4 and
    10 (a one-off figure, not asserted -- `>= 1` is, and `checked` keeps it honest). The DIRECTION is
    asserted per seed: uphill, the attacker is the weaker party, so the defenders never end with fewer
    survivors than on open ground -- a sign error in the Def dice would break this first."""
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve, _territory_of
    target, subject = "set_s_036", "fac_church_of_solmund"
    w = _bare(target)
    assert _territory_of(w, target) == "T9", "the target moved off T9; re-pin it to an UPHILL territory"
    attackers = world_q.mustered(w, "set_s_014", "fac_crown")
    assert attackers, "the fixture no longer musters a Crown army at set_s_014"
    checked = differs = 0
    for seed in range(16):
        uphill = provider_resolve(w, attackers, ["c"], "a field", subject=subject, rung=target,
                                  rng=random.Random(seed))
        open_ = _fight_open(monkeypatch, w, attackers, subject, target, seed)
        for r in (uphill, open_):
            assert r["status"] == "RESOLVED" and r["unopposed"] is False, f"seed {seed}: not fought: {r}"
        assert uphill["result"]["defender_size_pct"] >= open_["result"]["defender_size_pct"], (
            f"seed {seed}: uphill left the defenders FEWER survivors: {uphill} vs {open_}")
        checked += 1
        differs += uphill["result"] != open_["result"]
    assert checked == 16
    assert differs >= 1, "an uphill field fought identically to open ground on every seed (MB-05)"
