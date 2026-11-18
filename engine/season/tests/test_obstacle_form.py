"""B05.14 -- THE ONE OBSTACLE FORM AT THE CONTROL ARM: one roster, one column, one composer, one record field
(OBS §1, §2, §4 step 1a; SC-B Edits A and B; CAP B5, B8; 29_DICE Item 29-4 steps 2 to 4; A-79, A-137).

THE FORM, `modules/social_contest/roll.py::obstacle(inp) -> (ob, terms)`:
    hard  = even + difficulty + opposed_ob(opposition if a person opposes else pool_default, opposition_rate) + sum(raw_i x step_i)
    ob    = max(OB_MIN, min(hard, cap(pool)))          # lane A's `forgery` step stays where it was, before the cap; the room is a roster member (B05.17)
    terms = ((name, value), ...) in `rosters.yaml: obstacle_terms` order, + ("forgery", q) and ("ceiling", -clip) and ("floor", +lift) where each acted

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * `terms` SUM TO `ob` and every name is a roster member (or lane A's `forgery`, or a bound): a term dropped, renamed or
    double-counted breaks the sum on the quarter-step lattice, where every figure is exact in binary (so `==` is an exactness claim
    that can fail, not an approximation).
  * NOTHING LOWERS THE OBSTACLE: a negative member raises `ValueError`.
  * EVERY ROSTER MEMBER HAS ONE HOST FUNCTION and every function a member (OBS gate 1), refused at import.
  * AT THE CONTROL A ROLLED ACT'S OBSTACLE IS TODAY'S: with no person opposite it is `routine` (1) + `opposed_ob(pool_default)` (1.0) =
    2.0, the stand-in the deleted `obstacle_default` was; with a person opposite the opposing ATTRIBUTE is in the opposition (A-137), so
    the obstacle moves by exactly `opposition_rate x` his held attribute, which is the declared mover.
  * A ROLLED ROW WITH NO `difficulty:` IS REFUSED at load, as is one a row nothing rolls carries, and a level outside the roster.
  * AN OPPONENT OF RANK 0 IS FLOORED at `OB_MIN`, and the lift is a named term.
"""
from __future__ import annotations

import itertools
import random
from types import SimpleNamespace

import pytest
import yaml

from engine.dice_engine.sigma_leverage import MU_PER_DIE, OB_MIN, band_odds, even_line, net_boost, opposed_ob
from engine.substrate import descriptors

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import roster
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..queries.inputs import Margin, SocialContestInput
from ..seam.wrappers import pool, sigma
from .test_sc01_obstacle_ceiling import _module

ROSTER = roster("obstacle_terms", ordered=True)
LANE_A_STEPS = ("forgery",)                        # outside the roster (U-6); lane A's `room` step left it at B05.17 (the hostile half is the `reception` member, the rest leverage)
BOUNDS = ("ceiling", "floor")
SHIPPED_TABLE = V.VERB_TABLE_YAML                 # read at import, before any test re-points the loader
ROLLED = ("tell", "lie", "argue", "speak", "determine", "arrest", "interrogate", "research", "examine", "surveil")


def _inp(**kw) -> SocialContestInput:
    """A record as the host builds one: the roster's `reception` operand (the hostile half of `reception`, times `reception_gain`) and `capability`
    (at 0 where no row applies) ride in `obstacle_operands` in roster order; `reception` and `reception_gain` themselves stay on the record, raw."""
    base = dict(pool=4, opposition=None, obstacle_ceiling=None, obstacle_refusal_multiple=2.0, leverage=0.0,
                difficulty=1.0, pool_default=2, pool_add=0, opposition_rate=0.5, ceiling_per_pool=False, reception=0.0, reception_gain=0.0)
    base.update(kw)
    base.setdefault("obstacle_operands", (("reception", max(0.0, -base["reception"]), base["reception_gain"]), ("capability", 0.0, 1.0)))
    return SocialContestInput(**base)


# ---------------------------------------------------------------------------------------------------------------------
# the lattice: terms sum to ob, every name is a roster member
# ---------------------------------------------------------------------------------------------------------------------

def test_terms_sum_to_ob():
    mod = _module()
    checked = bounds_seen = 0
    for pool_add, diff, opp, rate, room, fq, ceil in itertools.product(
            (0, 5, 10), (0.0, 0.5, 1.0, 2.25, 3.0), (None, 0.0, 1.25, 2.0, 4.5, 8.0), (0.25, 0.5),
            (0.0, 0.75, -0.75), (0.0, 0.5), (None, 2.0, 3.0)):
        inp = _inp(pool_add=pool_add, difficulty=diff, opposition=opp, opposition_rate=rate,
                   reception=room, reception_gain=1.0, forgery_quality=fq, obstacle_ceiling=ceil)
        ob, terms = mod.obstacle(inp)
        names = [n for n, _ in terms]
        assert set(names) <= set(ROSTER) | set(LANE_A_STEPS) | set(BOUNDS), names
        assert names[:len(ROSTER)] == list(ROSTER), names                       # every member, in roster order, first
        assert sum(v for _, v in terms) == ob, (inp, ob, terms)                # exact: the lattice is dyadic
        assert ob >= OB_MIN, (inp, ob)                                         # the floor
        bounds_seen += sum(n in BOUNDS for n in names)
        checked += 1
    assert checked == 3 * 5 * 6 * 2 * 3 * 2 * 3 and bounds_seen > 100, (checked, bounds_seen)   # the bounds acted: the clip and the lift are in the sum


def test_every_term_is_non_negative_but_the_ceiling():
    mod = _module()
    negative = set()
    for diff, opp, room in itertools.product((0.0, 1.0, 3.0), (None, 0.0, 2.0, 8.0), (0.0, 1.0, -1.0)):
        _, terms = mod.obstacle(_inp(difficulty=diff, opposition=opp, reception=room, reception_gain=1.0, obstacle_ceiling=2.0))
        negative |= {n for n, v in terms if v < 0}
    assert negative == {"ceiling"}, negative               # nothing lowers the obstacle but the clip: a favourable room is leverage (B05.17)


def test_a_negative_term_raises():
    mod = _module()
    mod.obstacle(_inp(opposition=4.0))                                           # CONTROL: the same record, non-negative, composes
    for planted in (dict(difficulty=-1.0), dict(pool_add=-1), dict(opposition=4.0, opposition_rate=-0.5),
                    dict(obstacle_operands=(("x", -1.0, 1.0),)), dict(obstacle_operands=(("x", 1.0, -1.0),))):
        with pytest.raises(ValueError, match="negative"):
            mod.obstacle(_inp(**planted))


def test_opposition_is_never_absent():
    """PES-DICE (a): with nobody opposite the term is `opposed_ob(pool_default)`, with a person it is `opposed_ob(opposition)`."""
    mod = _module()
    for pd in (0, 2, 3):
        _, terms = mod.obstacle(_inp(opposition=None, pool_default=pd))
        assert dict(terms)["opposition"] == opposed_ob(pd, 0.5), terms
    _, terms = mod.obstacle(_inp(opposition=7.0, pool_default=2))
    assert dict(terms)["opposition"] == 3.5, terms
    _, terms = mod.obstacle(_inp(opposition=0.0, pool_default=2))
    assert dict(terms)["opposition"] == 0.0, terms                                # a held 0 is a person, not "nobody"


def test_the_even_line_is_the_owners_and_reads_pool_add():
    mod = _module()
    ob0, t0 = mod.obstacle(_inp())
    ob5, t5 = mod.obstacle(_inp(pool_add=5))
    assert dict(t0)["even"] == 0.0 and dict(t5)["even"] == even_line(5) == MU_PER_DIE * 5, (t0, t5)
    assert ob5 - ob0 == even_line(5)


# ---------------------------------------------------------------------------------------------------------------------
# the binding: roster member <-> host function
# ---------------------------------------------------------------------------------------------------------------------

def test_every_roster_member_has_a_host_function():
    assert tuple(sigma.OBSTACLE_TERMS) == ROSTER, (tuple(sigma.OBSTACLE_TERMS), ROSTER)          # the count is read, never typed
    assert all(callable(fn) for fn in sigma.OBSTACLE_TERMS.values())
    # `even`'s is the function that carries `pool_add` onto the record (OBS §1)
    fields = sigma.OBSTACLE_TERMS["even"](DEFAULT_FIXTURES, {})
    assert fields == {"pool_add": DEFAULT_FIXTURES.get("pool_add")}, fields
    # the refusal at import, in both directions, on planted bindings (the import-time call is `sigma._bound_to`)
    sigma._bound_to(dict(sigma.OBSTACLE_TERMS), "obstacle_terms")                                 # CONTROL: the shipped binding passes
    members = dict(sigma.OBSTACLE_TERMS)
    gone = members.pop("difficulty")
    with pytest.raises(Unspecified, match="difficulty"):                                         # a member with no function
        sigma._bound_to(members, "obstacle_terms")
    with pytest.raises(Unspecified, match="zebra"):                                              # a function with no member
        sigma._bound_to({**sigma.OBSTACLE_TERMS, "zebra": gone}, "obstacle_terms")


def test_the_difficulty_levels_are_sized_and_closed():
    levels = roster("difficulty_levels", ordered=True)
    sizes = DEFAULT_FIXTURES.get("difficulty_ob")
    assert tuple(sizes) == levels, (sizes, levels)
    assert list(sizes.values()) == sorted(sizes.values()) and min(sizes.values()) == 0 and len(set(sizes.values())) == len(levels)
    assert {r.difficulty for v, r in V.VERB_TABLE.items() if v in ROLLED} == {"routine"}          # the control: every rolled row `routine`


# ---------------------------------------------------------------------------------------------------------------------
# the column: a rolled row names a level, a row nothing rolls names none
# ---------------------------------------------------------------------------------------------------------------------

def _load_with(monkeypatch, tmp_path, verb, **cell):
    """`_load_verb_table` over the shipped yaml with `cell` set on (None: removed from) `verb`'s row."""
    doc = yaml.safe_load(SHIPPED_TABLE.read_text())
    row = next(r for r in doc["verbs"] if r["verb"] == verb)
    for k, v in cell.items():
        row.pop(k, None) if v is None else row.__setitem__(k, v)
    path = tmp_path / "verb_table.yaml"
    path.write_text(yaml.safe_dump(doc))
    monkeypatch.setattr(V, "VERB_TABLE_YAML", path)
    return V._load_verb_table()


def test_a_rolled_row_with_no_difficulty_is_refused(monkeypatch, tmp_path):
    assert set(V.social_roll_verbs()) == set(ROLLED), sorted(V.social_roll_verbs())              # the ten rows, derived from the prizes and routes
    assert _load_with(monkeypatch, tmp_path, "tell", difficulty="routine")["tell"].difficulty == "routine"       # CONTROL: the shipped cell loads
    for verb in ROLLED:                                                                           # contested rows and graded rows both
        with pytest.raises(SystemExit, match=f"{verb!r} is dealt by the social roll and declares no `difficulty:`"):
            _load_with(monkeypatch, tmp_path, verb, difficulty=None)
    with pytest.raises(SystemExit, match="not a member of `rosters.yaml: difficulty_levels`"):
        _load_with(monkeypatch, tmp_path, "tell", difficulty="easy")
    assert V.GRADED_INQUIRIES and set(V.GRADED_INQUIRIES) <= set(ROLLED)             # the graded rows are among the ten, and were refused above
    unrolled = next(v for v, r in V.VERB_TABLE.items() if v not in ROLLED and r.brute)
    with pytest.raises(SystemExit, match=f"{unrolled!r} declares `difficulty: 'routine'` and the social roll does not deal it"):
        _load_with(monkeypatch, tmp_path, unrolled, difficulty="routine")


# ---------------------------------------------------------------------------------------------------------------------
# the floor
# ---------------------------------------------------------------------------------------------------------------------

def test_an_opponent_of_rank_0_is_floored_at_ob_min():
    """DOE §3 row 11. At `plain` (difficulty 0) and no stand-in (`pool_default` 0), and at `plain` against a person scoring 0,
    nothing stands against the act, the floor lifts it to `OB_MIN` and the lift is the LAST term, named."""
    mod = _module()
    for planted in (dict(difficulty=0.0, opposition=None, pool_default=0), dict(difficulty=0.0, opposition=0.0)):
        ob, terms = mod.obstacle(_inp(**planted))
        assert ob == OB_MIN and terms[-1] == ("floor", float(OB_MIN)), (planted, ob, terms)
        assert sum(v for _, v in terms) == ob
    ob, terms = mod.obstacle(_inp(difficulty=0.0, opposition=0.0, obstacle_ceiling=3.0))          # CONTROL: nothing to lift, no floor term
    assert ob == OB_MIN
    ob, terms = mod.obstacle(_inp(difficulty=1.0, opposition=0.0))                                 # `routine` against a score of 0: at OB_MIN already
    assert ob == OB_MIN and "floor" not in dict(terms), terms


# ---------------------------------------------------------------------------------------------------------------------
# step 1a at the control, through the host
# ---------------------------------------------------------------------------------------------------------------------

def _world(**fixtures):
    fx = DEFAULT_FIXTURES
    for name, value in fixtures.items():
        fx = fx.sweep(name, value)
    w = P.tiny_world(fx)
    SeasonDriver(w)                                                             # the registrar fills the module entries
    return w


def test_step_1a_composes_todays_obstacle_at_control():
    """OBS gate 3, as a test: at the control arm (`pool_add` 0, `opposition_rate` 0.5, every rolled row `routine`) an act with NO person
    opposite -- a site, a Record, nobody -- composes `1 + opposed_ob(pool_default)` = 2.0, the obstacle the deleted `obstacle_default`
    gave; an act against a person composes `1 + 0.5 x (his opposing attribute + his skill score)`: the stand-in's 2.0 for a person
    opposite at the untrained score on an UNHELD attribute no longer exists, so the move is exactly the attribute's half. FALSIFIER: the
    attribute dropped from the opposition (a person's term would equal `0.5 x score`), or a non-person act off 2.0."""
    w = _world()
    default = float(w.fixtures.get("pool_default"))
    checked = moved = 0
    for verb in ROLLED:
        row = V.VERB_TABLE[verb]
        for subject in ("site_harbour", None):                                   # nobody opposite
            inp = sigma.contest_input(w, ["p_low"], verb=verb, subject=subject)
            ob, terms = _module().obstacle(inp)
            assert (ob, dict(terms)["even"], dict(terms)["difficulty"], dict(terms)["opposition"]) == (2.0, 0.0, 1.0, 1.0), (verb, subject, terms)
            checked += 1
        inp = sigma.contest_input(w, ["p_low"], verb=verb, subject="p_low")
        assert inp.opposition is None and _module().obstacle(inp)[0] == 2.0, (verb, inp)        # a self-plea is the stand-in too
        # a person opposite, his attribute held at 5 and his skill unheld: attribute + the untrained score
        other = w.persons["p_other"]
        other.capability = {}
        other.attributes = {row.opposed_attribute: 5} if row.opposed_attribute else {}
        inp = sigma.contest_input(w, ["p_low"], verb=verb, subject="p_other")
        ob, terms = _module().obstacle(inp)
        held = 5 if row.opposed_attribute else 0
        assert inp.opposition == held + default, (verb, inp.opposition)
        assert dict(terms)["opposition"] == 0.5 * (held + default), (verb, terms)
        moved += held > 0
    assert checked == 2 * len(ROLLED) and moved >= 7, (checked, moved)


def test_a_resolved_roll_carries_margin_terms_and_no_ob_terms():
    """The record key lane A added (`ob_terms`, a dict) is replaced by `Margin.terms` (C3-L5): the host's result carries the pair the
    module returned, summing to `ob`, in roster order; the refusal's too."""
    w = _world()
    w.persons["p_mid"].capability = {"copying": 3}
    out = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid", rng=random.Random(0))
    assert out["status"] == "RESOLVED" and "ob_terms" not in out, sorted(out)
    assert tuple(n for n, _ in out["terms"])[:len(ROSTER)] == ROSTER and sum(v for _, v in out["terms"]) == out["ob"], out["terms"]
    out = sigma.resolve(_world(), ["p_low"], ["c"], "a standing", verb="tell", subject="site_harbour", rng=random.Random(0))
    assert out["terms"] and sum(v for _, v in out["terms"]) == out["ob"]
    assert isinstance(Margin(net=0.0, ob=1.0).terms, tuple)


def test_the_opposing_attribute_joins_the_skill_score_in_the_opposition():
    """A-137 (the later ruling): the person opposite resists with his opposing ATTRIBUTE plus his SKILL SCORE. Two opponents differing
    only in the attribute read oppositions that differ by it; two differing only in the skill likewise; an UNHELD attribute reads the
    untrained score (`pool.untrained`, until B05.16 says the mid-point)."""
    w = _world()
    verb = "tell"
    opposed = V.VERB_TABLE[verb].opposed_attribute
    assert opposed in descriptors.ATTRIBUTES
    key = V.VERB_CAPABILITY[verb]
    default = int(w.fixtures.get("pool_default"))
    read = {}
    for label, attr, rank in (("lo", 3, 0), ("hi", 6, 0), ("skilled", 3, 5), ("unheld", None, 0)):
        p = w.persons["p_other"]
        p.attributes = {} if attr is None else {opposed: attr}
        p.capability = {key: rank} if rank else {}
        read[label] = sigma.contest_input(w, ["p_low"], verb=verb, subject="p_other").opposition
    assert read == {"lo": 3 + default, "hi": 6 + default, "skilled": 3 + 5, "unheld": default + default}, read
    assert pool.opposing_attribute(w.fixtures, w.persons["p_other"], verb) == default           # the reader: untrained where unheld


# ---------------------------------------------------------------------------------------------------------------------
# member `capability`: a hostile circumstance reaches the obstacle as data (B05.15; MAP §G edits 6, 7 and its falsifier; OBS §2 member 9)
# ---------------------------------------------------------------------------------------------------------------------

def _plant_circumstance(monkeypatch, key, *, when=None, side="actor", gain="reception_gain"):
    """Rebind `capability_uses()` to the shipped rows plus one `circumstance` row on the social roll's site, loaded by the real loader."""
    from .test_u1_capability_surface import _rebound
    row = dict(use=sigma.SOCIAL_ROLL_SITE, role="circumstance", key=key, side=side, gain=gain)
    if when is not None:
        row["when"] = when
    _rebound(monkeypatch, lambda rows: rows.append(row))


def test_a_circumstance_row_raises_the_obstacle_by_its_gain(monkeypatch):
    """MAP's falsifier, copied: a `circumstance` row with a gain of 0.25 on an attribute the actor holds at 4, on the uncapped arm
    (`obstacle_ceiling` None): the composed obstacle rises by exactly 1.0, and `fed_by` names the row. On the shipped arm the rise is
    clipped at the pool's cap, as a hostile room's is. No `circumstance` row ships, so the control is the same act with the table as shipped.
    FALSIFIER: a roster member with no row-reading function adds 0.0 whatever the table says; a row that needed Python to take effect
    would show here as a rise of 0.0."""
    attribute = descriptors.attribute_key("grace")
    outcomes = {}
    for arm, ceiling, gain in (("uncapped", None, 0.25), ("shipped", DEFAULT_FIXTURES.get("obstacle_ceiling"), 1.0)):   # the shipped arm's gain overshoots its cap
        w = _world(reception_gain=gain, obstacle_ceiling=ceiling)
        w.persons["p_low"].attributes = {attribute: 4}
        before = _module().obstacle(sigma.contest_input(w, ["p_low"], verb="tell", subject="site_harbour"))
        assert dict(before[1])["capability"] == 0.0, before                              # CONTROL: nothing ships, the member stands at 0
        with monkeypatch.context() as m:
            _plant_circumstance(m, attribute)
            inp = sigma.contest_input(w, ["p_low"], verb="tell", subject="site_harbour")
            after = _module().obstacle(inp)
            out = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="site_harbour", rng=random.Random(0))
        assert dict(after[1])["capability"] == 4 * gain, (arm, after)                    # 4 held x the gain, one operand (name, raw, 1.0)
        assert sum(v for _, v in after[1]) == after[0], after
        named = [f for f in out["fed_by"] if f[1] == "circumstance"]
        assert named == [(sigma.SOCIAL_ROLL_SITE, "circumstance", attribute, "actor", 4, 4 * gain)], out["fed_by"]    # `fed_by` names the row
        outcomes[arm] = (before[0], after[0], dict(after[1]))
    low, high, terms = outcomes["uncapped"]
    assert high - low == 1.0 and "ceiling" not in terms, outcomes                       # exactly the gain's worth, nothing clipped
    low, high, terms = outcomes["shipped"]
    assert high - low < 4.0 and terms["capability"] == 4.0 and terms["ceiling"] < 0, outcomes   # the cap bites: the rise is clipped, as a room's is


def test_a_circumstance_row_whose_when_fails_adds_nothing(monkeypatch):
    """The row's `when` selects it (`rosters.when_holds`): `rank_at_least` on the row's own skill, read on the holder the row's side names.
    The actor holds `copying` at 3 over a bar of 2 (the row applies: 3 x 0.25) and at 1 under it (the row is left out)."""
    w = _world(reception_gain=0.25, obstacle_ceiling=None)
    _plant_circumstance(monkeypatch, "copying", when=dict(rank_at_least=2))
    read = {}
    for rank in (3, 1):
        w.persons["p_low"].capability = {"copying": rank}
        read[rank] = dict(_module().obstacle(sigma.contest_input(w, ["p_low"], verb="tell", subject="site_harbour"))[1])["capability"]
    assert read == {3: 0.75, 1: 0.0}, read


# ---------------------------------------------------------------------------------------------------------------------
# what the speaker brings is leverage (B05.17; PES-A; OBS gate 2)
# ---------------------------------------------------------------------------------------------------------------------

def test_favour_and_proof_levels_change_odds_at_every_pool():
    """OBS gate 2 (F-SC-16's rows, PES-DICE's gate 2): against a person scoring 8 (`opposition` 8) at a shipped-arm obstacle, holding 0, 1, 2 and
    4 proofs (and, separately, 0, 1, 2 and 4 units of a friendly bench's favour) gives four DIFFERENT, strictly increasing Success-or-better
    shares on the closed form of the one sampler, at every pool from `pool_floor` (the control, 0) to `pool_floor + 10`. `!=`, no `approx`: a
    cell where adding one leaves the odds unchanged (the dead zone the subtracting form had, four of six cells) is a failure.
    From a pool of 1: a pool of nothing rolls nothing and the boost is `sqrt(pool)` of its shift, so no leverage moves pool 0, which is
    observed in the last line, not skipped silently (B05.23 sets `pool_floor` 5, above it)."""
    fx = DEFAULT_FIXTURES
    assert fx.get("proof_level") is not None and fx.get("favour_level") is not None       # the control arms are None; these are the shipped ones
    floor = fx.get("pool_floor")
    checked = 0
    for source, operand in (("proofs", "proofs"), ("favour", "reception")):
        for pool in range(max(1, floor), floor + 11):
            shares = []
            for held in (0, 1, 2, 4):
                inp = _inp(pool=pool, opposition=8.0, obstacle_ceiling=fx.get("obstacle_ceiling"), ceiling_per_pool=True,
                           leverage=sigma.advantage_sigma(fx, {operand: held}))
                ob, _terms = _module().obstacle(inp)
                failure, partial, success, overwhelming = band_odds(pool, ob, net_boost(inp.leverage, pool))
                shares.append(success + overwhelming)
            assert len(set(shares)) == 4 and all(a != b for a, b in itertools.combinations(shares, 2)), (source, pool, shares)
            assert shares[0] < shares[1] < shares[2] < shares[3], (source, pool, shares)
            checked += 1
    assert checked == 2 * len(range(max(1, floor), floor + 11)) and checked >= 20, checked
    assert net_boost(sigma.advantage_sigma(fx, {"proofs": 4}), 0) == 0.0                   # the one cell not in the range, observed


def test_the_levels_are_the_sources_the_leverage_sums():
    """OBS §5: the `levels` a roll records are the very lists `leverage` is the sum of -- one per `advantage_sources` member, roster order, whole
    units, each FOR the roller (the defender list is empty for proofs and favour until B24's cited items)."""
    fx = DEFAULT_FIXTURES
    operands = {"proofs": 2.5, "reception": 1.4}
    levels = sigma.advantage_levels(fx, operands)
    assert tuple(n for n, _, _ in levels) == roster("advantage_sources", ordered=True) and [n for n, _, _ in levels][-3:] == ["proofs", "favour", "office"], levels
    by = {n: (f, a) for n, f, a in levels}
    assert by["proofs"] == (["minor"] * 3, []) and by["favour"] == (["major"] * 1, []), by                  # 2.5 and 1.4 round half up
    assert sigma.advantage_sigma(fx, operands) == 3 * 0.25 + 1.0
    assert sigma._levels_count(levels)[-3:] == (("proofs", 3, 0), ("favour", 1, 0), ("office", 0, 0))
    none = DEFAULT_FIXTURES.sweep("proof_level", None).sweep("favour_level", None)
    assert sigma.advantage_sigma(none, operands) == 0.0                                                      # the control: None brings no level
    assert sigma.advantage_sigma(fx, {"reception": -3.0}) == 0.0                                             # a hostile bench is no favour
