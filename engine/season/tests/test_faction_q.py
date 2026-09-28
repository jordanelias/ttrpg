"""`queries/faction_q.py` -- `resolve(w, prop) -> Faction`, §B.6.1's one constructor.

What each block proves, and the control that stops it passing vacuously:

  1. THE FIVE FIELDS, AND `proposition` IS THE INPUT ECHOED BACK -- not re-derived, not dropped.
  2. `members` IS THE SAME RULE AS `world_q.members`, NOT A SECOND DEFINITION OF MEMBERSHIP
     (`CLAUDE.md` §8, "every rule lives once"). Asserted by identity, not by equal output --
     two functions that happen to agree today can drift; the same object cannot.
  3. `holdings`/`seats` MATCH AN INDEPENDENTLY-COMPUTED SET, not merely "non-empty". The control
     re-derives membership DIRECTLY from `w.tenures` (`kind == "commit"`), not by calling
     `world_q.members` -- test 2 already proves `faction_q.members IS world_q.members`, so calling
     it again here would make the "independent" control share the exact function whose correctness
     is in question, and a misreading of §14.2 shared by both would cancel out rather than be seen.
  4. VARIATION ACROSS INPUT: two real factions with different membership return different
     `holdings`/`seats`, which a stub returning a fixed list could not do.
  5. `head` IS ALWAYS `None`, CITING `F.4`. `Tenure.degree` (§B.6.1's cited derivation input) is a
     real field -- default `None` -- but has no GAME-LOGIC reader anywhere in the tree; the only
     touches are the gate's generic before/after diff and `World`'s hash/snapshot machinery, which
     treat it exactly as they treat every other field and read no game meaning from it
     (`harness/populated.py:551-556`, measured by grep, 2026-09-14). This does not re-run that
     grep as a standing guard -- `CLAUDE.md` §0.1 pt 3's "absence" row is the cheapest claim to
     make and this repo does not mint a guard whose subject is another module's citation
     (§0.1 pt 5) -- it only asserts the one thing `resolve()` actually promises.
"""
from engine.season.harness.populated import build_realm
from engine.season.queries import faction_q, world_q


def test_resolve_returns_the_five_fields_with_proposition_echoed():
    w = build_realm(0)
    f = faction_q.resolve(w, "fac_crown")
    assert f.proposition == "fac_crown"
    assert set(vars(f)) == {"proposition", "members", "holdings", "seats", "head"}


def test_members_is_world_q_members_not_a_second_definition():
    # Identity, not equality -- `faction_q.py` imports the function object directly.
    assert faction_q.members is world_q.members


def test_holdings_and_seats_match_an_independently_computed_set():
    w = build_realm(0)
    f = faction_q.resolve(w, "fac_crown")
    # ⚠ RE-DERIVED FROM `w.tenures` DIRECTLY, NOT VIA `world_q.members` -- test 2 proves
    # `faction_q.members is world_q.members`, so calling it here would test the code against
    # itself. §14.2: "Membership is `commit`."
    inside = {t.subject for t in w.tenures
              if t.kind == "commit" and t.object == "fac_crown" and t.live
              and t.subject in w.persons}
    assert inside, "fac_crown has no live members in this corpus -- the fixture changed"

    held = [t for t in w.tenures if t.kind == "hold" and t.live and t.subject in inside]
    expect_holdings = sorted({t.object for t in held if t.object in w.rungs})
    expect_seats = sorted({t.object for t in held if t.object in w.offices})

    assert f.holdings == expect_holdings
    assert f.seats == expect_seats
    assert f.holdings, "control is vacuous if Crown holds no territory in this corpus"
    assert f.seats, "control is vacuous if Crown holds no seat in this corpus"


def test_holdings_and_seats_vary_with_membership_not_a_fixed_stub():
    w = build_realm(0)
    crown = faction_q.resolve(w, "fac_crown")
    guilds = faction_q.resolve(w, "fac_guilds")
    assert crown.members != guilds.members
    assert (crown.holdings, crown.seats) != (guilds.holdings, guilds.seats)


def test_head_is_always_none_citing_f4():
    w = build_realm(0)
    for prop in ("fac_crown", "fac_schoenland", "fac_guilds"):
        assert faction_q.resolve(w, prop).head is None
