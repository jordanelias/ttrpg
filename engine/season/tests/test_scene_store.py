"""B09.16 -- THE SCENE IS KEPT BESIDE ITS ACTS (`ActStore.add_scene` / `scene_of` / `scenes`).

The question an act answered used to live in `SeasonDriver.scenes`, a dict that died with the driver. It now lives in
`World.acts`, written by RESOLVE (which holds the ACTS token) and by nobody else. Four claims, each able to fail:

  1. THE DRIVER HOLDS NO SCENES -- no attribute, and nothing a season leaves on it, is a Scene map. DELIBERATE returns
     the map it built and stores nothing (`test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route` is the
     other half: a store write inside DELIBERATE reddens it).
  2. EVERY STORED ACT ANSWERS `scene_of`, and the Scene it answers is the one that carried the act (not any Scene).
  3. A FRESH DRIVER ANSWERS A SEASON-0 ACT'S QUESTION: `chronicle.occasion_line(w, act_id)` on a world the first driver
     has gone from. `None`/an unrecorded line falsifies edit 1-2.
  4. THE CONTENT HASH DOES NOT FOLD THE STORE (edit 3, `[ASSUMPTION; medium; Jordan to correct; revert: fold it]`):
     adding a Scene moves no hash (`test_hash_equal_with_the_scene_store_unfolded`, the falsifier of this claim). The
     realm's two-season hash is also read against the shipped realm pin (`test_the_realm_two_season_hash_is_the_shipped_pin_and_the_run_stores_scenes`):
     that is the realm pin, which B09.99 re-recorded, and not a reading taken at B09.15.
"""
from __future__ import annotations

import pytest

from ..gaps import Unspecified
from ..harness import chronicle as CHR
from ..harness import headless as HL
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.carriers import Act, Question, Scene

# The realm pin at seed 0, two seasons: `build_realm(0)` played by `populated.run`'s composition (`test_choose_watch._play`).
# It is `_realm_goldens.SHIPPED[(0, 2)]` (B09.99 re-recorded it with the other realm pins; B09.15 took the first reading of
# this world), the same world, held here as a literal.
REALM_PIN_SEED_0_TWO_SEASONS = "f313e280bd3836abeccf660a5ae71f4b"        # B24p merge with B21 re-record: c9bba3fa.. -> f313e280..; B24p merge re-record: e6466cf7.. -> c9bba3fa..; B15.99 re-record: aea26494.. -> e6466cf7..; BA1.99 re-pin, second time, manner rows held back (the cast's content, `_realm_goldens.SHIPPED[(0, 2)]`): was e66b5058.. with them; before: f18fd036..; B10.99 re-pin: was e03202af..


def _play_headless(seasons: int = 2):
    w = HL.build_world(0)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs())
    for _ in range(seasons):
        d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


@pytest.fixture(scope="module")
def played():
    return _play_headless(2)


def test_the_driver_holds_no_scenes(played):
    w, d = played
    assert len(w.acts) >= 30, "the season released too few acts for the claim to mean anything"
    # No attribute of the driver is a Scene map, however it is named (a rename would not escape this).
    holders = [k for k, v in vars(d).items()
               if (isinstance(v, dict) and any(isinstance(x, Scene) for x in v.values()))
               or (isinstance(v, (list, tuple, set, frozenset)) and any(isinstance(x, Scene) for x in v))]
    assert not holders, f"the driver holds Scenes in {holders}"
    assert not hasattr(d, "scenes")
    # ...and the store is where they went, in release order, with the acts they carried.
    assert len(w.acts.scenes()) >= 10
    assert all(isinstance(sc, Scene) for sc in w.acts.scenes())


def test_every_stored_act_answers_scene_of(played):
    w, _d = played
    checked = 0
    for a in w.acts:
        sc = w.acts.scene_of(a.id)
        assert sc is not None, f"{a.id} ({a.verb}) answers no Scene"
        assert sc.id == a.scene and any(x.id == a.id for x in sc.acts), (a.id, a.scene, sc.id)
        assert sc.actor == a.actor
        checked += 1
    assert checked >= 30, f"only {checked} acts checked: the claim is vacuous"
    assert checked == len(w.acts)
    # CONTROL: an id the store never held answers nothing, and the accessor does not raise.
    assert w.acts.scene_of("act_never_stored") is None


def test_the_store_refuses_a_repeated_scene_id_and_holds_release_order():
    w, _d = _play_headless(1)
    scenes = w.acts.scenes()
    assert isinstance(scenes, tuple) and len({sc.id for sc in scenes}) == len(scenes)
    with pytest.raises(Unspecified):
        w.acts.add_scene(Scene(scenes[0].id, scenes[0].actor, []))
    assert w.acts.scenes() == scenes, "a refused scene was stored anyway"
    # Release order: the first scene stored is the one the first stored act rode (RESOLVE adds the lap's scenes in
    # release order, before folding any of them).
    assert w.acts.scene_of(next(iter(w.acts)).id) in scenes[:5]


def test_a_fresh_driver_answers_a_season_0_acts_question(played):
    w, d = played
    # The act the first driver released first, in season 0 (acts are stored in resolution order).
    with_question = [a for a in w.acts
                     if getattr(w.acts.scene_of(a.id), "occasion", None) is not None]
    assert with_question, "no stored act answers a question: the claim is vacuous"
    act = with_question[0]
    line = CHR.occasion_line(w, act.id)
    assert line.startswith("for: ") and "(no scene)" not in line, line
    del d
    d2 = SeasonDriver(w)                       # a second driver on the same world: it has held nothing
    assert not hasattr(d2, "scenes")
    assert CHR.occasion_line(w, act.id) == line
    sc = w.acts.scene_of(act.id)
    assert sc is not None and sc.occasion is not None, "a fresh driver cannot say why the act was taken"
    assert line == f"for: {sc.occasion.source} {sc.occasion.about}"


def test_an_act_with_no_scene_prints_no_question():
    w = HL.build_world(0)
    bare = Act(id="act_bare_b0916", actor=next(iter(w.persons)), verb="work")
    assert CHR.occasion_line(w, bare.id) == "for: (no scene)"            # not stored: nothing is claimed
    w.acts.append(bare)
    assert w.acts.scene_of(bare.id) is None
    assert CHR.occasion_line(w, bare.id) == "for: (no scene)"


def test_hash_equal_with_the_scene_store_unfolded():
    w, _d = _play_headless(1)
    before = w.content_hash()
    n = len(w.acts.scenes())
    w.acts.add_scene(Scene("sc_b0916_extra", next(iter(w.persons)), [],
                           occasion=Question("q_b0916", "need", (), about="x")))
    assert len(w.acts.scenes()) == n + 1, "the plant did not reach the store"
    assert w.content_hash() == before, "the content hash folds the Scene store (edit 3 says it is left out)"


def test_the_realm_two_season_hash_is_the_shipped_pin_and_the_run_stores_scenes():
    """What this observes at HEAD: the seed-0 two-season realm hash equals the realm pin, and that run stores Scenes
    (so the store is populated while the pin holds). It does NOT show the store is unfolded -- the planted
    `test_hash_equal_with_the_scene_store_unfolded` is that falsifier; this is the realm pin read from this file."""
    from .test_choose_watch import _play
    w, d = _play(0, 2)
    assert not hasattr(d, "scenes")
    assert len(w.acts.scenes()) > 100, "the realm run stored too few Scenes for this to mean anything"
    assert w.content_hash() == REALM_PIN_SEED_0_TWO_SEASONS


def test_scene_decided_counts_equal_decision_spread():
    """B10.05: the stamp on each Scene's first act and `decision_spread --decisions` count ONE rule (`choose.deciding_term`).
    The `--decisions` reading is taken as it takes it (`read_decisions`: `attribute_top` over each person's common set);
    the stamp is read off the chooser's own Scenes (`make_chooser`, the opening set narrowed to that same common set, the
    same draw and the same believed-odds query), so a second owner of the rule on either side makes the two counts differ."""
    from collections import Counter

    from ..boot.realm import build_realm
    from ..decision import assemble, choose as CH
    from ..harness import decision_spread as DS
    from ..seam.wrappers.sigma import believed_odds_query
    from ..state.ids import draw_factory

    w = build_realm(0)
    spread: Counter = Counter()
    for row in DS.read_decisions(w)["rows"]:                 # also `w._rehome()`s, as the reading does
        spread.update(row["deciders"])
    fx, draw, foldable = w.fixtures, draw_factory(w.world_seed, lambda: w.tick), resolvable_verbs()
    held: dict = {}
    stamped: Counter = Counter()
    chooser = CH.make_chooser(fx, lambda *a: "|".join(a), verbs=foldable, draw=draw)
    real_opening_set = CH.opening_set
    CH.opening_set = lambda p, view, q, fx_: list(held[p.id])
    try:
        for _label, ref in DS.common_referents(w):
            q = DS.decision_question(ref)
            formed = {pid: DS.formed_set(w, p, q, foldable) for pid, p in sorted(w.persons.items())}
            keyed = {pid: {(c.verb, c.subject, DS.is_self_plea(c, pid)): c for c in cs} for pid, cs in formed.items() if cs}
            common = set.intersection(*(set(k) for k in keyed.values())) if keyed else set()
            order = sorted(common, key=lambda k: (k[0], k[1] or ""))
            for pid in keyed:
                held[pid] = [keyed[pid][k] for k in order]
                p = w.persons[pid]
                view = assemble(p, q, fx.get("view_k"), odds=believed_odds_query(w, p))
                scenes = chooser(p, view, None, lambda: 99)
                stamped[scenes[0].decided if scenes else "none"] += 1
    finally:
        CH.opening_set = real_opening_set
    assert sum(spread.values()) >= 200, f"only {sum(spread.values())} readings: the claim is vacuous"
    assert len(spread) >= 2 and "" not in stamped, (spread, stamped)       # the stamp was set, and it says more than one thing
    assert stamped == spread, f"two owners of the rule: stamp {dict(stamped)} against decision_spread {dict(spread)}"
