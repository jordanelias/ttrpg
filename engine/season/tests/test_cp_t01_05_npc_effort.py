"""CP-T01-05, THE NPC HALF (B10-10; `H-249`) -- THE COMPUTED CHOOSER FORMS `effort` (`decision/choose.py::settle_efforts`).

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * WHERE THE PERSON'S BELIEVED CHANCE RISES WITH THE EFFORT (the View's query answers per the act's own `effort`),
    the chooser puts the variant on the act; WHERE IT IS FLAT IN EFFORT it never does, however many slots it could
    take. Through `make_chooser`'s real ranking and packing, the payload read off the scenes' acts.
  * EFFORT IS PRICED BY THE ACTS IT DISPLACES: with a strong rival ranked below, the same rising chance no longer
    pays for the slots and the base stays; with nothing below it, effort displaces nothing and is formed.
  * NO SCENE IS EVER OVERSPENT: `make_chooser`'s scenes, priced by `Scene.cost`, total no more than the budget, and no
    scene fills more than `interactions_per_scene` slots. PLANTED FAILURE (d): the price of a scene taken as one
    slot per act (`len(acts) > 1`, the second owner `take()` used to be) overspends, so (c) is red under it.
  * THE CONTROL: `npc_effort` `off` forms no effort on the same case, and returns its arguments untouched.
  * THE ARM IS A ROSTER: an arm outside `rosters.yaml: npc_efforts` raises.
  * THE ODDS ARE ASKED ABOUT THE ACT WITH ITS EFFORT: on a real world, `sigma.believed_chance` rises with the
    `effort` in the payload (the chooser's variant reaches `odds_of` as `_payload_of` hands it).
There is NO realm-level pin of the `off` arm in the tree: `test_go07_canonical_digest.py` pins the SHIPPED arm (`on`), and
`on` and `off` read the same hash at every measured horizon, so that pin cannot tell a working `off` from a no-op `off`
(the Phase 1 close of B10-10). The `off` control above is the chooser-level one.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from engine.substrate.descriptors import PURSUITS

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..queries import person_q
from ..seam.wrappers import sigma
from ..data.verbs import VERB_CAPABILITY
from ..state.carriers import EFFORT, Act, Candidate, Claim, Person, effort_of

AXIS = "grandiose_humble"
RIVAL = "carry"                  # an uncontested verb: its pursuit term is never weighted by a chance
HEARER = "p_other"


def _fx(npc="on", per=None):
    fx = DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("odds_weighting", "believed").sweep("npc_effort", npc)
    return fx if per is None else fx.sweep("interactions_per_scene", per)


def _person(pid="p_a"):
    p = Person(id=pid, name=pid)
    # roster-exempt: TEST FIXTURE pursuits -- one vector, so only the believed chance and the displaced acts part the scores.
    p.pursuits = {n: 1.0 for n in PURSUITS}
    return p


@pytest.fixture
def cells(monkeypatch):
    """`argue` carries no alignment cell in the shipped table, so one is planted on the rebound binding
    (`test_cr17_odds_weighting.py`'s seam): `argue` 1.0 on AXIS; the uncontested rival's cell is set per case."""
    table = {ax: dict(row) for ax, row in V.ALIGNMENT.items()}
    table.setdefault(AXIS, {}).update({"argue": 1.0, RIVAL: 0.0})
    monkeypatch.setattr(V, "ALIGNMENT", table)
    return table


def _curve(by_effort):
    """A believed-odds query reading the chance off the asked act's own `effort` (0 when it carries none)."""
    asked = []

    def odds(act, bands):
        e = effort_of(act)
        asked.append(e)
        return by_effort[e] if e in by_effort else by_effort[max(by_effort)]
    odds.asked = asked
    return odds


def _choose(cands, odds, budget=5, fx=None, person=None):
    """`make_chooser`'s real ranking AND packing over the planted option set, the View carrying `odds`."""
    p = person or _person()
    ch = CH.make_chooser(fx or _fx(), lambda pid, verb, key: f"{pid}:{verb}:{key}")
    return ch(p, SimpleNamespace(question=None, odds=odds), SimpleNamespace(), lambda: budget)


def _plant(monkeypatch, cands):
    monkeypatch.setattr(CH, "opening_set", lambda p, view, q, fx: list(cands))


def _run(monkeypatch, cands, odds, budget=5, fx=None):
    _plant(monkeypatch, cands)
    p = _person()
    ch = CH.make_chooser(fx or _fx(), lambda pid, verb, key: f"{pid}:{verb}:{key}")
    return ch(p, SimpleNamespace(question=object(), odds=odds), SimpleNamespace(), lambda: budget)


def _argue(subject="prop_x"):
    return Candidate("argue", subject, operands={"to": HEARER})


def _efforts(scenes):
    return [effort_of(a) for sc in scenes for a in sc.acts]


RISING = {0: 0.1, 1: 0.5, 2: 0.9}
FLAT = {0: 0.5, 1: 0.5, 2: 0.5}


# ---------------------------------------------------------------------------------------------
# (b) the chooser forms effort where the believed chance rises with it, and never where it is flat
# ---------------------------------------------------------------------------------------------

def test_a_believed_chance_that_rises_with_effort_forms_the_effort_variant(cells, monkeypatch):
    odds = _curve(RISING)
    scenes = _run(monkeypatch, [_argue()], odds)
    assert _efforts(scenes) == [2], "the chance rises 0.1 -> 0.5 -> 0.9 with nothing to displace: the top effort pays"
    assert set(odds.asked) == {0, 1, 2}, f"the variants were never asked about WITH their effort: {sorted(set(odds.asked))}"
    assert scenes[0].acts[0].payload[EFFORT] == 2


def test_a_believed_chance_flat_in_effort_never_forms_it(cells, monkeypatch):
    odds = _curve(FLAT)
    scenes = _run(monkeypatch, [_argue(f"prop_{i}") for i in range(4)], odds)
    assert len(_efforts(scenes)) == 4 and set(_efforts(scenes)) == {0}, _efforts(scenes)
    assert set(odds.asked) == {0, 1, 2}, "the control must have asked about the variants, or flat proves nothing"


def test_a_chance_of_none_leaves_the_base(cells, monkeypatch):
    scenes = _run(monkeypatch, [_argue()], lambda act, bands: None)
    assert _efforts(scenes) == [0]


def test_a_view_with_no_query_forms_no_effort(cells, monkeypatch):
    scenes = _run(monkeypatch, [_argue()], None)
    assert _efforts(scenes) == [0]


def test_an_uncontested_verb_forms_no_variant_whatever_the_query_says(cells, monkeypatch):
    cells[AXIS][RIVAL] = 1.0
    odds = _curve(RISING)
    scenes = _run(monkeypatch, [Candidate(RIVAL, "prop_x")], odds)
    assert _efforts(scenes) == [0] and odds.asked == [], odds.asked


# ---------------------------------------------------------------------------------------------
# the price: the acts it displaces
# ---------------------------------------------------------------------------------------------

def test_a_strong_rival_beneath_it_keeps_the_base_and_nothing_beneath_it_forms_effort(cells, monkeypatch):
    # The base `argue` scores W * 0.1; effort 2 scores W * 0.9, a gain of 0.8 W. Two rivals scored 0.5 W each
    # (the cell W * 0.5) would fill the two slots effort takes: net 0.9 W - 1.0 W < 0.1 W, so the base stays.
    cells[AXIS][RIVAL] = 0.5
    rivals = [Candidate(RIVAL, f"prop_r{i}") for i in range(2)]
    scenes = _run(monkeypatch, [_argue()] + rivals, _curve(RISING))
    assert set(_efforts(scenes)) == {0}, _efforts(scenes)
    # the control one clause away: the same rivals scored at a tenth of that, and the gain pays for the slots
    cells[AXIS][RIVAL] = 0.05
    scenes = _run(monkeypatch, [_argue()] + rivals, _curve(RISING))
    assert max(_efforts(scenes)) == 2, _efforts(scenes)


def test_off_forms_no_effort_on_the_same_case_and_returns_its_arguments_untouched(cells, monkeypatch):
    scenes = _run(monkeypatch, [_argue()], _curve(RISING), fx=_fx("off"))
    assert _efforts(scenes) == [0]
    cands, scores = [_argue()], {}
    scores[id(cands[0])] = 0.1
    assert CH.settle_efforts(cands, scores, lambda c: 0.1, _fx("off")) == (cands, scores)


def test_an_arm_outside_the_roster_raises(cells, monkeypatch):
    with pytest.raises(Unspecified):
        _run(monkeypatch, [_argue()], _curve(RISING), fx=_fx("maybe"))


def test_no_room_for_a_second_slot_forms_no_effort(cells, monkeypatch):
    scenes = _run(monkeypatch, [_argue()], _curve(RISING), fx=_fx(per=1))
    assert _efforts(scenes) == [0]
    # and a bound of 2 caps the top effort at 1 (an effort-2 act needs 3 slots)
    scenes = _run(monkeypatch, [_argue()], _curve(RISING), fx=_fx(per=2))
    assert _efforts(scenes) == [1]


# ---------------------------------------------------------------------------------------------
# (c) / (d) a scene holding an effort Candidate is never overspent, asserted through Scene.cost
# ---------------------------------------------------------------------------------------------

def _spent(scenes, ext):
    return sum(sc.cost(ext) for sc in scenes)


def _six(monkeypatch, budget, fx=None):
    cands = [_argue(f"prop_{i}") for i in range(6)]
    return _run(monkeypatch, cands, _curve(RISING), budget=budget, fx=fx)


def test_c_a_scene_with_an_effort_candidate_is_never_overspent(cells, monkeypatch):
    ext = DEFAULT_FIXTURES.get("extended_scene_cost")
    per = DEFAULT_FIXTURES.get("interactions_per_scene")
    formed = 0
    for budget in (1, 2, 3, 4, 5, 6):
        scenes = _six(monkeypatch, budget)
        assert _spent(scenes, ext) <= budget, (budget, _spent(scenes, ext), [sc.slots for sc in scenes])
        assert all(sc.slots <= per for sc in scenes), [sc.slots for sc in scenes]
        formed += sum(1 for e in _efforts(scenes) if e)
    assert formed >= 1, "no effort was formed in any case: the overspend check observed nothing"


def test_c_the_budget_that_cannot_carry_an_effort_scene_does_it_plain(cells, monkeypatch):
    # budget 3: the first scene is an effort-2 act alone (slots 3, cost 2), leaving 1; the next cannot afford an
    # extended scene, so its act is taken at effort 0 (a plain scene), not skipped
    scenes = _six(monkeypatch, 3)
    assert [effort_of(sc.acts[0]) for sc in scenes] == [2, 0], [effort_of(a) for sc in scenes for a in sc.acts]
    assert _spent(scenes, DEFAULT_FIXTURES.get("extended_scene_cost")) == 3


def test_effort_scenes_are_packed_by_slots_not_by_count(cells, monkeypatch):
    # no budget pressure: every scene fits `interactions_per_scene` slots, whatever efforts are in it
    per = DEFAULT_FIXTURES.get("interactions_per_scene")
    scenes = _run(monkeypatch, [_argue(f"prop_{i}") for i in range(5)], _curve({0: 0.1, 1: 0.5, 2: 0.5}), budget=50)
    assert any(e for e in _efforts(scenes))
    assert all(sc.slots <= per for sc in scenes), [sc.slots for sc in scenes]
    assert sum(len(sc.acts) for sc in scenes) == 5, "an act was lost or doubled by the packing"


# ---------------------------------------------------------------------------------------------
# the odds the chooser reads are for the act WITH its effort, on a real world
# ---------------------------------------------------------------------------------------------

def test_the_believed_chance_on_a_real_world_rises_with_the_acts_effort():
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)                                   # the registrar fills MODULE_ENTRIES
    p = w.persons["p_low"]
    # REM-30's `verb_capability` row makes `argue` draw on the `argue` key, so a person hearer's opposition is a belief the
    # roller must hold (none held -> no figure) and nothing deposits one in a built realm: the believer is handed it (score 4,
    # an obstacle of 2.0, the module's own default for a hearer who holds no key).
    p.ledger.append(Claim(id=f"c:{p.id}:{HEARER}", holder=p.id, subject=HEARER,
                          predicate=person_q.CAPABILITY_CLAIM + VERB_CAPABILITY["argue"], value=4, when=0,
                          source="told", confidence=5, visibility="own"))
    row = VERB_TABLE["argue"]
    bands = tuple(b for b, written in row.writes_by_degree.items() if written)
    got = []
    for e in (0, 1, 2):
        payload = {"subject": "prop_x", "to": HEARER, **({EFFORT: e} if e else {})}
        got.append(sigma.believed_chance(w, p, Act(f"a:{e}", p.id, "argue", payload=payload), bands))
    assert None not in got, got
    assert got[0] < got[1] < got[2], got


# ---------------------------------------------------------------------------------------------
# B05.60 -- the advantage channel is signed, and `wounds` is its member (ADV Edits A to D; A-8)
# ---------------------------------------------------------------------------------------------
# A wound is a named LEVEL on the roll its bearer makes (one `wound_level` per `wound_step` of body lost below his ceiling, at most
# `wound_levels_max`), AGAINST him; and the roller's FOR where the bearer is the person he acts on. Never an obstacle term (A-8).
# Gate 2: the same `tell` by the same person at full body and at one third lost deals what `odds_of` reads, `record_odds(<his pool>, ob, 0.0)`
# and `record_odds(<his pool>, ob, -0.25)`, within three standard errors over 200,000 seeded rolls.
from dataclasses import asdict                                                    # noqa: E402

from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, record_odds            # noqa: E402

from .test_odds_of import _assert_dealt, _tell, _world as _tell_world             # noqa: E402
from .test_sc01_obstacle_ceiling import _module                                   # noqa: E402

N_WOUND = 200_000


def _wound_world(**sweeps):
    """`test_odds_of`'s world (a strong hearer `p_mid`, the speaker `p_low`), the fixtures swept as named."""
    w = _tell_world()
    for name, value in sweeps.items():
        w.fixtures = w.fixtures.sweep(name, value)
    return w


def _lose(w, who, steps):
    """`who` has lost `steps` of `wound_step` below his ceiling."""
    w.persons[who].body = w.persons[who].body_ceiling - steps * w.fixtures.get("wound_step")


def _contest(w):
    """The record the fold would build for `p_low` telling `p_mid`, and the obstacle the module composes for it."""
    inp = sigma.contest_input(w, ["p_low", "p_mid"], verb="tell", subject="p_mid")
    return inp, _module().obstacle(inp)[0]


def test_the_wound_step_is_a_third_of_the_scale_read_from_the_fixtures():
    fx = DEFAULT_FIXTURES
    assert fx.get("wound_step") == fx.get("condition_scale") // 3
    assert (fx.get("wound_level"), fx.get("wound_levels_max")) == ("minor", 2)


def test_a_wounded_actor_rolls_with_a_level_against():
    w = _wound_world()
    whole, ob = _contest(w)
    assert whole.leverage == 0.0, "a man at full body brings no wound level"
    _lose(w, "p_low", 1)
    hurt, ob_hurt = _contest(w)
    assert ob_hurt == ob and hurt.pool == whole.pool, "a wound is never an obstacle term and never a die (A-8)"
    assert hurt.leverage == -LEVEL_SIGMA["minor"] == -0.25
    odds_whole, odds_hurt = record_odds(whole.pool, ob, 0.0), record_odds(hurt.pool, ob, -0.25)
    assert odds_hurt[0] > odds_whole[0], "the wound makes Failure likelier"
    assert sigma.odds_of(w, _tell("p_mid")) == odds_hurt, "`odds_of` reads the same record the fold deals"
    _assert_dealt(odds_hurt, hurt, N_WOUND)
    fresh = _wound_world()
    assert sigma.odds_of(fresh, _tell("p_mid")) == odds_whole
    _assert_dealt(odds_whole, _contest(fresh)[0], N_WOUND)


def test_a_wounded_defender_gives_the_roller_a_level():
    w = _wound_world()
    whole, ob = _contest(w)
    _lose(w, "p_mid", 1)
    hurt, ob_hurt = _contest(w)
    assert ob_hurt == ob and hurt.pool == whole.pool
    assert hurt.leverage == LEVEL_SIGMA["minor"] == 0.25, "the bearer's wound helps the roller when the bearer defends"
    odds_hurt = record_odds(hurt.pool, ob, 0.25)
    assert odds_hurt[0] < record_odds(whole.pool, ob, 0.0)[0], "the wound makes Failure less likely for the roller"
    assert sigma.odds_of(w, _tell("p_mid")) == odds_hurt
    _assert_dealt(odds_hurt, hurt, N_WOUND)


def test_wound_level_none_is_todays_bytes():
    """THE CONTROL: with `wound_level` None a wounded actor's leverage is exactly 0 and his record is the unwounded man's, field for field."""
    w = _wound_world(wound_level=None)
    whole, _ = _contest(w)
    for who in ("p_low", "p_mid"):                           # both lost two thirds of the scale (green before `wounds` existed, and after)
        w.persons[who].body = w.persons[who].body_ceiling - 2 * w.fixtures.get("condition_scale") // 3
    hurt, _ = _contest(w)
    assert hurt.leverage == 0.0 and asdict(hurt) == asdict(whole)
    assert sigma.odds_of(w, _tell("p_mid")) == sigma.odds_of(_wound_world(wound_level=None), _tell("p_mid"))


def test_wounds_is_the_channels_last_member_and_a_stack_is_capped_at_the_maximum():
    from ..data.rosters import roster
    assert roster("advantage_sources", ordered=True)[-1] == "wounds" and set(sigma.ADVANTAGE_SOURCES) == set(roster("advantage_sources"))
    fx = DEFAULT_FIXTURES
    ceiling, step = fx.get("condition_scale"), fx.get("wound_step")
    ops = lambda lost, other=0: {"body": ceiling - lost, "body_ceiling": ceiling, "subject_body": ceiling - other, "subject_body_ceiling": ceiling}
    assert sigma._wound_levels(fx, ops(step - 1)) == ([], [])                     # short of one step: none
    assert sigma._wound_levels(fx, ops(step)) == ([], ["minor"])
    assert sigma._wound_levels(fx, ops(step, 2 * step)) == (["minor"] * 2, ["minor"])
    assert sigma._wound_levels(fx, ops(ceiling)) == ([], ["minor"] * 2)           # dead on his feet: still `wound_levels_max`
    assert sigma._wound_levels(fx, {}) == ([], [])                                # operands absent: nothing lost


def test_a_wound_level_that_is_no_level_raises_at_the_owner_never_scores_zero():
    w = _wound_world(wound_level="grievous")
    assert _contest(w)[0].leverage == 0.0, "no wound, no level to name"
    _lose(w, "p_low", 1)
    with pytest.raises(KeyError):
        _contest(w)


def test_the_believer_passes_his_own_body_and_leaves_the_subjects_out():
    w = _wound_world(regard_step=0)                          # at a live `regard_step` a person counterparty's stance is unknown to him (B05.21): no record at all
    p = w.persons["p_low"]
    for key in ("copying", VERB_TABLE["tell"].opposed_attribute):     # his belief of the hearer's skill and of the attribute that resists
        p.ledger.append(Claim(id=f"c:p_low:p_mid:{key}", holder="p_low", subject="p_mid", predicate=person_q.CAPABILITY_CLAIM + key,
                              value=10, when=0, source="told", confidence=5, visibility="own"))
    _lose(w, "p_mid", 2)                                    # the subject's wound is not the believer's to know
    args = dict(pool=4.0, person_subject=True)
    sound = sigma.believed_input(p, "tell", "p_mid", w.fixtures, **args)
    assert sound is not None and sound.leverage == 0.0
    _lose(w, "p_low", 1)
    assert sigma.believed_input(p, "tell", "p_mid", w.fixtures, **args).leverage == -0.25, "his own wound is his to know"


def test_the_largest_stack_against_still_leaves_a_chance_of_partial_or_better():
    """U5a closure: at `wound_levels_max` levels against, at the strongest level a sweep names, the chance of Partial or better is not zero."""
    w = _wound_world(wound_level="moderate")
    _lose(w, "p_low", 5)                                     # past the maximum: two levels, not five
    inp, ob = _contest(w)
    assert inp.leverage == -2 * LEVEL_SIGMA["moderate"]
    failure = sigma.odds_of(w, _tell("p_mid"))[0]
    assert 0.0 < 1.0 - failure < 1.0, failure
