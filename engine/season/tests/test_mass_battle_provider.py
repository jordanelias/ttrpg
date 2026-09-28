"""`seam/wrappers/mass_battle.py` -- the `@provider("contest", "mass_battle")` M3 wires
(`ED-IN-0279`). What each block proves, and the control that stops it passing vacuously:

  1. END TO END THROUGH `contest()`, not just the provider function in isolation -- proves the
     manifest row, the `@provider` registration, and the dispatch in `seam/contest.py` all agree,
     which a unit test calling `resolve()` directly could not.
  2. `PARTY-GAP` ON AN EMPTY CLAIMANT LIST AND ON A MISSING `subject`, mirroring
     `seam/wrappers/combat.py`'s own PARTY-GAP discipline -- the provider derives a gap rather
     than fabricating a side.
  3. AN UNRESOLVABLE `subject` DOES NOT CRASH OR REFUSE. `faction_q.resolve` returns an empty
     `Faction` for an unknown proposition id (§B.6.1's own -- membership is `commit`, and there is
     none to find); the provider does not special-case that into an auto-win or a second refusal
     -- it is one more input to the battle math, exactly as this module's own docstring commits to.

Block 4 (`resolve_field` sums `Person.weight` per side into army SIZE, not quality) lives in
`tests/valoria/test_mass_battle_resolve_field.py`, not here: it needs `from systems.mass_battle...`
at module scope to reach `massbattle` directly for monkeypatching, and
`tests/valoria/test_engine_does_not_import_systems.py`'s `NESTED_BASELINE`/`BASELINE_TOTAL` ratchet
(zero `systems.*` imports anywhere under `engine/`, top-level OR function-local) applies to
`engine/season/tests/` -- this file is under `engine/`. `tests/valoria/test_mass_battle_d1_morale_baseline.py`
already imports `massbattle` the same way from that location; this follows it rather than being new.
"""
import random

from engine.season.harness.populated import build_realm
from engine.season.queries import faction_q
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
    assert set(r["parties"]["subject_members"]) == set(faction_q.resolve(w, "fac_guilds").members)


def test_party_gap_on_empty_claimants_and_missing_subject():
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    w = build_realm(0)
    empty = provider_resolve(w, [], ["c"], "a field", subject="fac_guilds")
    assert empty["status"] == "PARTY-GAP"
    missing_subject = provider_resolve(w, ["p_npc_008"], ["c"], "a field", subject=None)
    assert missing_subject["status"] == "PARTY-GAP"


def test_unresolvable_subject_is_not_a_crash_or_a_second_refusal():
    from engine.season.seam.wrappers.mass_battle import resolve as provider_resolve
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    r = provider_resolve(w, crown.members, ["c"], "a field", subject="fac_this_does_not_exist",
                          rng=random.Random(3))
    assert r["status"] == "RESOLVED"
    assert r["parties"]["subject_members"] == []
