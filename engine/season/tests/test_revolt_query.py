"""`queries/world_q.py::uncontrolled` -- THE REVOLT QUERY, plan position `24h` P5.

Its oracle is retired code, recoverable with
`git show 5c5d8ec6:systems/world/sim/insurgency_pipeline.py`: `check_insurgency_triggers` started
from every territory with `owner is None`. The season stand-in for that test is
`holder_faction_of(w, r) is None`, and the Query's docstring says which of the oracle's other
conditions (contiguity, the two-season streak, promotion) have no stand-in and are left out.

What each test proves, and the control that stops it passing vacuously:

  1. PRECONDITIONS HOLD -> AT LEAST ONE. `build_realm(0)` as built has an unheld territory under
     its realm. The answer equals a set RE-DERIVED from `w.tenures` directly, not through
     `holder_faction_of`/`faction_holding`, so a misreading shared by the Query and its owner
     cannot cancel out.
  2. PRECONDITIONS FAIL -> ZERO, AS A CONTROL PAIR. The same world plus one live `hold` on each
     uncontrolled territory, by a person committed to exactly one rostered faction. The two
     worlds differ in exactly those edges, so the move from >= 1 to 0 is theirs.
  3. THE FACTION LIMB. A hold by a person committed to NO rostered faction leaves the territory
     uncontrolled; a second rostered commitment by a faction holder makes every territory he
     holds uncontrolled. Faction is read off the holder's live edges, when asked.
  4. THE ANCESTRY LIMB. A faction-held rung above an unheld territory governs it: the nearest
     held title decides, which is `holder_faction_of`'s own walk.
  5. IT WRITES NOTHING (`04 §A.2`: `world_q` owns nothing and takes no token; AX-4's one write
     path). Over the realm, every territory and the root territory outside the realm:
     the content hash and the log length are unchanged, the write gate stays closed, and the
     calls succeed with `World.write` replaced by a function that fails the test.
  6. ARM 5 CAN SEE A WRITE. A store write planted inside the read path (in `holder_faction_of`,
     which `uncontrolled` resolves by module name) moves the content hash; a draw bump planted there
     leaves the hash alone and moves `_unhashed`. Without this, arm 5 could be a hash that never
     moves for any reason, or blind to state the hash does not fold.
  7. THE CENSUS ROW IS THE QUERY'S CALLER (r2 `05` §A.1.5 RULED (d), `establishment_of`'s
     precedent: a Query with no consumer is a false N-line). `populated.census(w)["uncontrolled_territories"]` equals the Query's answer
     over the realm, and the same world with every territory UNDER THE REALM held reads 0 in the same row
     (`terr_T16` is outside it), so the row
     moves with the Query and is not a constant.
"""
from engine.season.data.rosters import FACTION_BY_PROP
from engine.season.harness.populated import build_realm
from engine.season.queries import world_q
from engine.season.state.carriers import Tenure
from engine.season.state.containment import descendants


def _realm(w) -> str:
    realms = [r for r in w.rungs if w.rungs[r].kind == "realm"]
    assert len(realms) == 1, f"fixture: expected one realm rung, found {realms}"
    return realms[0]


def _territories(w) -> list:
    return sorted(r for r in w.rungs if w.rungs[r].kind == "territory")


def _rostered_factions_of(w, pid) -> set:
    return {t.object for t in w.persons[pid].tenures
            if t.kind == "commit" and t.live and t.object in FACTION_BY_PROP}


def _faction_holder(w) -> str:
    """A person who holds a territory and is committed to exactly one rostered faction."""
    for t in w.tenures:
        if (t.kind == "hold" and t.live and t.object in w.rungs
                and w.rungs[t.object].kind == "territory" and t.subject in w.persons
                and len(_rostered_factions_of(w, t.subject)) == 1):
            return t.subject
    raise AssertionError("fixture: no territory is held by a single-faction person")


def _independent(w, root) -> list:
    """Uncontrolled territories under `root`, re-derived from `w.tenures` without the Query's
    owner. It leans on one fixture fact, asserted: no rung other than a territory is held, so
    no title above a territory can govern it."""
    held = {t.object: t.subject for t in w.tenures if t.kind == "hold" and t.live
            and t.object in w.rungs}
    assert all(w.rungs[r].kind == "territory" for r in held), (
        "fixture: a non-territory rung is held, so this derivation would need the ancestry walk")
    out = []
    for r in sorted({root, *descendants(w, root)}):
        if r not in w.rungs or w.rungs[r].kind != "territory":
            continue
        if r not in held or len(_rostered_factions_of(w, held[r])) != 1:
            out.append(r)
    return out


def test_preconditions_hold_returns_at_least_one_and_matches_an_independent_derivation():
    w = build_realm(0)
    realm = _realm(w)
    got = world_q.uncontrolled(w, realm)
    assert len(got) >= 1, "build_realm(0) has an unheld territory under its realm; the Query saw none"
    assert got == _independent(w, realm)
    # Every answer is a territory INSIDE the subtree asked about, never outside it.
    inside = {realm, *descendants(w, realm)}
    assert all(r in inside and w.rungs[r].kind == "territory" for r in got)
    # Variation across input: a held territory answers [] and an unheld one answers itself.
    held_terr = next(r for r in _territories(w) if r not in got and r in inside)
    assert world_q.uncontrolled(w, held_terr) == []
    assert world_q.uncontrolled(w, got[0]) == [got[0]]


def test_control_pair_one_faction_hold_per_territory_turns_the_answer_to_zero():
    built = build_realm(0)
    planted = build_realm(0)
    realm = _realm(planted)
    assert built.content_hash() == planted.content_hash(), "fixture: two builds of seed 0 differ"
    targets = world_q.uncontrolled(planted, realm)
    assert targets, "the treatment arm is degenerate: nothing to hold"
    head = _faction_holder(planted)
    for i, r in enumerate(targets):
        planted.add_tenure(Tenure(f"t_test_revolt_hold_{i}", head, r, "hold", 0))
    # The pair differs in exactly the planted edges, and nothing else.
    assert len(planted.tenures) - len(built.tenures) == len(targets)
    assert world_q.uncontrolled(built, realm) == targets
    assert world_q.uncontrolled(planted, realm) == []


def test_a_holder_of_no_faction_or_of_two_leaves_the_land_uncontrolled():
    w = build_realm(0)
    realm = _realm(w)
    target = world_q.uncontrolled(w, realm)[0]
    loner = next((pid for pid in sorted(w.persons) if not _rostered_factions_of(w, pid)), None)
    assert loner is not None, "fixture: every person is committed to a rostered faction"
    w.add_tenure(Tenure("t_test_revolt_loner_hold", loner, target, "hold", 0))
    assert world_q.hold_force(w, target).subject == loner
    assert target in world_q.uncontrolled(w, realm), "a holder of no faction made the land controlled"

    w2 = build_realm(0)
    target2 = world_q.uncontrolled(w2, realm)[0]
    head = _faction_holder(w2)
    w2.add_tenure(Tenure("t_test_revolt_head_hold", head, target2, "hold", 0))
    assert target2 not in world_q.uncontrolled(w2, realm)
    (first,) = _rostered_factions_of(w2, head)
    second = next(p for p in sorted(FACTION_BY_PROP) if p != first and p in w2.propositions)
    w2.add_tenure(Tenure("t_test_revolt_second_commit", head, second, "commit", 0))
    his = sorted(t.object for t in w2.persons[head].tenures
                 if t.kind == "hold" and t.live and t.object in w2.rungs
                 and w2.rungs[t.object].kind == "territory"
                 and t.object in {realm, *descendants(w2, realm)})
    assert len(his) >= 2, f"fixture: the head holds {his}"
    got = world_q.uncontrolled(w2, realm)
    assert set(his) <= set(got), "divided allegiance did not read as uncontrolled on every holding"


def test_a_faction_held_rung_above_governs_an_unheld_territory_beneath_it():
    w = build_realm(0)
    realm = _realm(w)
    before = world_q.uncontrolled(w, realm)
    assert before
    assert world_q.hold_force(w, realm) is None, "fixture: the realm rung is already held"
    w.add_tenure(Tenure("t_test_revolt_realm_hold", _faction_holder(w), realm, "hold", 0))
    assert world_q.uncontrolled(w, realm) == []


def _every_call(w) -> list:
    """The realm, every territory (inside the realm and the root one outside it)."""
    return [_realm(w), *_territories(w)]


def _unhashed(w) -> tuple:
    """World state `content_hash` does NOT fold (it folds the state collections, the docket, the
    tenures and the log): the draw ordinal that mints later Event ids, the tick, the act store, the
    barrier cache, the staged deltas and the write-emission list. `uncontrolled` says it is recomputed
    on every call, so none of these may move across one. Without this the writes-nothing arm was blind
    to a `w.new_draw()` in the body, which would have passed every other assertion here."""
    return (w.tick, w.draw, len(w.acts), frozenset(w._barrier_cache),
            {k: list(v) for k, v in w._staged.items()}, len(w._emitted_by_write))


def test_the_query_writes_nothing_and_never_needs_the_write_gate(monkeypatch):
    w = build_realm(0)
    calls = _every_call(w)
    assert not w.gate.is_open, "fixture: a fresh world opened with a write window"
    hash_before = w.content_hash()
    log_before = sum(1 for _ in w.log)
    writes_before = len(w.writes)
    unhashed_before = _unhashed(w)

    def refuse(*a, **k):
        raise AssertionError("`uncontrolled` called `World.write`; a Query takes no token")

    monkeypatch.setattr(w, "write", refuse)
    answered = 0
    found = 0
    for r in calls:
        found += len(world_q.uncontrolled(w, r))
        answered += 1
        assert not w.gate.is_open
    assert answered == len(calls) >= 18, f"only {answered} calls ran"
    assert found >= 2, "every call answered []: this arm observed a degenerate read"
    assert w.content_hash() == hash_before
    assert sum(1 for _ in w.log) == log_before
    assert len(w.writes) == writes_before
    assert _unhashed(w) == unhashed_before, "the Query moved World state that content_hash does not fold"


def test_the_writes_nothing_arm_sees_a_write_planted_in_the_read_path(monkeypatch):
    w = build_realm(0)
    realm = _realm(w)
    expected = world_q.uncontrolled(w, realm)
    hash_before = w.content_hash()
    real = world_q.holder_faction_of
    fired = []

    def writing(w_, rung_id):
        fired.append(rung_id)
        w_.docket.append({"planted_by_test": rung_id})   # a store write that bypasses the gate
        return real(w_, rung_id)

    monkeypatch.setattr(world_q, "holder_faction_of", writing)
    got = world_q.uncontrolled(w, realm)
    assert fired, "the plant never ran: `uncontrolled` does not read through `holder_faction_of`"
    assert got == expected
    assert w.content_hash() != hash_before, "a planted store write left the content hash unmoved"

    # THE SECOND PLANT: a write the content hash cannot see. `new_draw` bumps `w.draw`, which mints later
    # Event ids (world.py `new_draw`), and `content_hash` does not fold it; the control is that the hash
    # stays put while `_unhashed` moves, so arm 5's extra snapshot is what catches this class.
    w2 = build_realm(0)
    realm2 = _realm(w2)
    hash2, unhashed2 = w2.content_hash(), _unhashed(w2)
    fired2 = []

    def drawing(w_, rung_id):
        fired2.append(rung_id)
        w_.new_draw()
        return real(w_, rung_id)

    monkeypatch.setattr(world_q, "holder_faction_of", drawing)
    world_q.uncontrolled(w2, realm2)
    assert fired2, "the draw plant never ran"
    assert w2.content_hash() == hash2, "fixture: the content hash was expected to be blind to a draw bump"
    assert _unhashed(w2) != unhashed2, "a planted draw bump left the unhashed snapshot unmoved"


def test_the_census_reports_the_revolt_query_and_moves_with_it():
    from engine.season.harness.populated import census

    w = build_realm(0)
    realm = _realm(w)
    expected = len(world_q.uncontrolled(w, realm))
    assert expected >= 1, "fixture: build_realm(0) has no uncontrolled territory to report"
    assert census(w)["uncontrolled_territories"] == expected

    # the control: hold every uncontrolled territory (a single-faction holder), as arm 2 does
    holder = _faction_holder(w)
    for i, tid in enumerate(world_q.uncontrolled(w, realm)):
        w.add_tenure(Tenure(f"t_test_census_hold_{i}", holder, tid, "hold", 0))
    assert world_q.uncontrolled(w, realm) == []
    assert census(w)["uncontrolled_territories"] == 0
