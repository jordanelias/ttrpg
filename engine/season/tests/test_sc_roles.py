"""B24p.06 -- the bearing reading and what a person carries in (V2 p2 §A.2 to §A.4, §G).

Every reader here is person-side: it reads the person's OWN interior and the operands the host passes, never `World`,
another person's ledger or a true attribute of anyone else. Hand-built people only; `test_sc_roles.py` is shared with
the exchange's and the roles' tests (B24p.07, .18): the last two tests below are the exchange's (a Focus role and a Reason role)."""
from __future__ import annotations

import math
from dataclasses import replace

from engine.dice_engine import dice_engine

from ..data.affiliations import AFFILIATION_CEILING, AFFILIATIONS
from ..data.arrangements import GROUNDS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import STANCE_MAX
from ..queries import person_q as PQ
from ..queries.inputs import Choice, Cond
from ..state.carriers import Claim, Person, interior_of
from .test_sc_proceeding_module import P, _dials, _inp, _key, _p, _rite, _sit

FX = DEFAULT_FIXTURES
FULL = (("x", 5, 5),)        # one stance row at the row type's bound: a relationship of +1


def _person(pid="p", **kw):
    return Person(id=pid, **kw)


def test_bearing_reads_only_his_own_interior():
    """A pursuit the matter helps reads `want` above 0, the same matter against it below 0; a man with nothing at stake
    reads `(0, 0, bond)`. Read from `interior_of(p)`, the record that carries nothing but his own state."""
    lover = interior_of(_person(pursuits={"wealth": 0.8}, stance=[("x", 2, 5)]), 0, 0)
    helps = PQ.bearing(lover, {"wealth": 1.0}, for_party="x", against_party="y")
    against = PQ.bearing(lover, {"wealth": -1.0}, for_party="x", against_party="y")
    bare = PQ.bearing(interior_of(_person(stance=[("x", 2, 5)]), 0, 0), {"wealth": 1.0}, for_party="x", against_party="y")
    assert helps[0] > 0 > against[0]
    assert bare[:2] == (0, 0) and bare[2] == 10 / STANCE_MAX and bare[2] == helps[2]
    # a held conviction reads as `hold`, over the roster's own ceiling, and never as `want`
    name = sorted(AFFILIATIONS)[0]
    held = interior_of(_person(conviction={name: AFFILIATION_CEILING}), 0, 0)
    got = PQ.bearing(held, {name: 1.0}, for_party="x", against_party="y")
    assert got == (0, 1.0, 0)


def test_conflict_on_both_sides_never_cancels():
    """Interests and ties on both sides are a conflict, never a cancellation (V2 p4 §K B6, §L 13); a shared faction is
    a tie, never partiality (§L R1); a conviction alone is not partiality (§L 19)."""
    # a pursuit the matter helps and an office duty it hurts: opposed, equal
    wants = _person(pursuits={"wealth": 0.5})
    c, lean = PQ.conflict(wants, {"wealth": 1.0}, for_party="x", against_party="y", duty=(("wealth", -0.5),))
    assert round(c, 2) == 0.33 and lean == 0.0
    # a tie as strong to one party as to the other
    both = _person(stance=[("x", 5, 5), ("y", 5, 5)])
    c, lean = PQ.conflict(both, {}, for_party="x", against_party="y")
    assert round(c, 2) == 0.33 and lean == 0.0
    # a conviction the matter bears on, alone: it moves how he hears (hold), it makes him no partial
    name = sorted(AFFILIATIONS)[0]
    law = _person(conviction={name: AFFILIATION_CEILING})
    assert PQ.bearing(law, {name: 1.0}, for_party="x", against_party="y")[1] == 1.0
    assert PQ.conflict(law, {name: 1.0}, for_party="x", against_party="y") == (0.0, 0.0)
    # a shared faction with one party moves the bond he hears by and is not partiality
    judge = _person()
    assert PQ.bearing(judge, {}, for_party="x", against_party="y", shares=("x",))[2] > 0
    assert PQ.conflict(judge, {}, for_party="x", against_party="y") == (0.0, 0.0)


def test_bearing_gives_a_party_a_stake_in_his_own_case():
    """A flat matter: each party's `mean(stake)` is `PARTY_STAKE` toward his own side; a non-party's is 0; `party=False`
    reads the matter without the floor; a stake already above the floor is not lowered."""
    def mean(stake):
        return sum(stake) / len(stake)

    flat = {}
    pro = mean(PQ.bearing(_person("x"), flat, for_party="x", against_party="y"))
    con = mean(PQ.bearing(_person("y"), flat, for_party="x", against_party="y"))
    out = mean(PQ.bearing(_person("z"), flat, for_party="x", against_party="y"))
    assert pro > 0 > con and out == 0                 # being a party is a stake, toward his own side
    assert abs(pro - PQ.PARTY_STAKE) < 1e-12 and abs(con + PQ.PARTY_STAKE) < 1e-12
    assert mean(PQ.bearing(_person("x"), flat, for_party="x", against_party="y", party=False)) == 0
    keen = PQ.bearing(_person("x", pursuits={"wealth": 1.0}), {"wealth": 1.0}, for_party="x", against_party="y")
    assert mean(keen) > PQ.PARTY_STAKE and keen[2] == 0


def test_a_false_item_is_his_own_word_or_nothing():
    """A man whose own ledger holds the matter false and who speaks for it gets one insincere `testimony` of his own;
    one whose ledger agrees gets none; so does one who holds nothing (a forged `Record` is a `[HOOK]`)."""
    def knows(value, pid="p"):
        return _person(pid, ledger=[Claim("c", pid, "m", "held_by:q", value, 0, "firsthand", 80, "own")])

    liar = PQ.false_items(knows(False), "m", "for", FX)
    assert len(liar) == 1 and liar[0].kind == "testimony" and liar[0].sincere is False
    assert liar[0].source == "p" and liar[0].about == "m" and 0 < liar[0].weight <= 1
    assert PQ.false_items(knows(False), "m", "against", FX) == ()
    assert PQ.false_items(knows(True), "m", "for", FX) == ()
    assert len(PQ.false_items(knows(True), "m", "against", FX)) == 1
    assert PQ.false_items(_person(), "m", "for", FX) == ()
    assert PQ.believes(knows(False), "m", FX) < 0 < PQ.believes(knows(True), "m", FX)


def test_strain_carried_fades_and_is_bounded():
    """Each rattle fades on its own clock and the k-th freshest counts half the one before: any number of rattles stays
    under 1.0 and each further scene lowers the load. Control: with no fade the load does not drop."""
    assert PQ.strain_carried((), FX) == 0
    assert PQ.strain_carried((0,) * 1000, FX) < 1.0
    assert PQ.strain_carried((2,), FX) < PQ.strain_carried((1,), FX) < PQ.strain_carried((0,), FX)
    still = FX.sweep("strain_fade", 0.0)
    assert PQ.strain_carried((9,), still) == PQ.strain_carried((0,), still)
    assert PQ.strain_carried((3, 0), FX) == PQ.strain_carried((0, 3), FX)


def _speak(inp, mover, keyed, ground="consequence"):
    return P.exchange(inp, _sit(inp), mover, Choice("argue", ground, None, None), _key("roles", keyed))[1]


def test_drift_is_continuous_in_the_pull():
    """FOCUS (R1, B14): what pulls a man off the point (the times' `unrest`) moves him only as far as his hold fails to carry it: no pull,
    no drift; a pull of 0.0001 a drift of at most 0.0001 even at Focus 1 (it once read 0.67); a real pull sometimes carries him."""
    seen = {}
    for pull in (0.0, 0.0001, 0.5):
        inp = _inp([_p("a", "for", focus=1.0), _p("b", "against"), _p("j", decides=True)], _rite(unrest=pull))
        drifts = [_speak(inp, inp.room[0], i).drift for i in range(60)]
        assert all(0.0 <= d <= pull for d in drifts), (pull, max(drifts))
        seen[pull] = sum(d > 0 for d in drifts)
    assert seen[0.0] == 0 and seen[0.5] > 5, seen


def test_a_party_who_decides_hears_his_own_case_by_his_own_reason():
    """REASON, C2: a party who decides is moved by his own speech, heard by HIMSELF: his own Reason validates it (a sounder speaker moves
    his own track further, the dice held equal), his own Will resists it, and the other side's Reason and Will, which he is not hearing
    through, change nothing on his track (his own Reason is 7, off the middle, so that a validation read from anyone else would show)."""
    def own_move(a_reason=7.0, a_will=4.0, b_reason=4.0, b_will=4.0):
        dials = _dials(DEFAULT_FIXTURES.sweep("fit_level", "strong"))
        grounds = (("consequence", 0.0, 1.0),)                # Reason's share of the dice 0: only Presence rolls, so Reason acts by validating
        inp = _inp([_p("a", "for", True, reason=a_reason, will=a_will), _p("b", "against", reason=b_reason, will=b_will)], dials=dials, grounds=grounds)
        return dict(_speak(inp, inp.room[0], 7).moved)

    base = own_move()
    assert "a" in base
    assert own_move(a_reason=7.0)["a"] > own_move(a_reason=1.0)["a"]
    assert own_move(a_will=7.0)["a"] < own_move(a_will=1.0)["a"]
    assert own_move(b_reason=7.0)["a"] == own_move(b_reason=1.0)["a"] == base["a"]
    assert own_move(b_will=7.0)["a"] == own_move(b_will=1.0)["a"] == base["a"]


# ------------------------------------------------------------------------------------------------------------------ B24p.18: the six roles
# Each role is one test, on the module with hand-built inputs (no World, no driver). The settings are the SHIPPED column of V2 p2 §K, set in
# THIS file (the repo's Fixtures hold control values until B24p.23); a role's CONTROL ARM is the same scene with that operand's own setting off.
# An arm reads the same `KEYS` keys at attribute 1 and at 7 (common random numbers: a key's draws do not depend on the attribute), so the
# difference is paired; a POSITIVE arm asserts the ruled sign beyond two standard errors of that paired difference, a CONTROL arm asserts the
# per-key lists `==`. The outcome of a speech is its margin on the one ladder (carried = Success or better), not the sitting's close: the close's
# own draw would add noise and no operand. Each test asserts `checked == the arms it ran` (a loop that asserts conditionally must assert it asserted).
SHIPPED = dict(
    fit_level="strong", answer_level="moderate", repeat_step=0.35, sense_step=0.15, involve=0.3, esteem_step=0.2, show=1.0, off_step=1.0,
    admit_step=0.5, contempt_step=1.0, ploy_step=1.5, grain_strain=0.5, heard_step=0.05, heard_floor=0.5, gap_step=0.25, weary_step=0.5,
    stay_base=1.0, stay_per_will=0.5, awe_step=0.5, comfort_step=0.5, rel_gain=0.5, flop=0.5, invite=0.5, press_ob=1.25, press_pull=1.0,
    rattle_pull=0.5, wear=0.5, rattle_gain=1.5, rebound=1.0, reactance=0.75, room_level=0.5, heckle=1.0, concede_step=1.0, consent_at=2.5,
    crowd_at=12.0, crowd_lean=0.2, mood_scale=5.0, read_scale=1.0, read_blur=2.0, read_noise=0.3, bias_step=2.0, relevance=1, track_step=0.2,
    temper_step=0.5, temper_break=0.75, temper_cool=0.5, grain=2.0, grudge=2.0, pride=2.0, start_step=2.0, presume_step=2.0, power_scale=2.0,
    strain_fade=0.5, recuse_at=0.25)
GROUND_REASON = {"evidence": 0.8, "consequence": 0.7, "authority": 0.4, "solidarity": 0.2}      # each ground's Reason weight, the shipped column
KEYS = 1000      # the plan's 2,000 ran this file in 21 s (the weakest arm read z = 11.2 there; about 7.9 at 1,000), so 1,000 keys an arm
LO, HI = 1.0, 7.0
SPEECH_FIELDS = ("relevance", "frame", "heard", "esteem", "drift")
ARGUE = Choice("argue", "consequence", None, None)
PRESS = Choice("press", "consequence", None, None)


def _set(**over) -> dict:
    return _dials(**{**SHIPPED, **over})


def _grounds(col=None) -> tuple:
    """the grounds as the shipped column weighs them, or every ground's Reason weight at `col` (0: the dice are Presence's, 1: Reason's)."""
    return tuple((g, GROUND_REASON[g] if col is None else col, 1.0) for g in GROUNDS)


def _abridged(a, b, col=0.0, **over):
    """a tell: `a` speaks once to `b`, who is addressed, decides and has no side."""
    rite = _rite(close="exchange", turns=1, moves=(("for", ("argue",)),), difficulty=0.5)
    return _inp([_p("a", "for", **a), _p("b", None, True, **{"stake": (0.2, 0.0, 0.0), **b})], rite, _set(**over), _grounds(col))


def _trial(a, b, j, col=None, rite=None, **over):
    """a trial: `a` for, `b` against, one judge `j`; the rite leans to Reason (0.2) and asks Grace 5, as a trial does."""
    rite = rite or _rite(turns=5, standard=5.0, reason_lean=0.2)
    return _inp([_p("a", "for", **a), _p("b", "against", **b), _p("j", None, True, **{"stake": (0.2, 0.0, 0.0), **j})], rite, _set(**over), _grounds(col))


def _state(inp, **cond):
    """a sitting in which each person named has the `Cond` given (`a=Cond(heat=1.0)`), the rest fresh."""
    return _sit(inp, cond=tuple((p.id, cond.get(p.id, Cond())) for p in inp.room))


def _beats(inp, mover="a", choice=ARGUE, label="roles", st=None, n=KEYS) -> list:
    st = st or _sit(inp)
    who = next(p for p in inp.room if p.id == mover)
    return [P.exchange(inp, st, who, choice, _key(label, i))[1] for i in range(n)]


def _carried(beats) -> list:
    """1.0 where the speech's margin reaches Success on the one ladder (`degree_from_net`), else 0.0."""
    need = dice_engine.DEGREE_ORDINAL[dice_engine.Degree.SUCCESS]
    return [float(dice_engine.DEGREE_ORDINAL[dice_engine.degree_from_net(b.margin, 0.0)] >= need) for b in beats]


def _col(beats, f) -> list:
    return [f(b) for b in beats]


def _margin(beats) -> list:
    return [b.margin for b in beats]


def _term(beats, name) -> list:
    return [dict(b.terms).get(name, 0.0) for b in beats]


def _moved(beats, who) -> list:
    return [dict(b.moved)[who] for b in beats]


def _sign(hi, lo, sign, what) -> tuple:
    """a POSITIVE arm: the paired difference `hi - lo` has the ruled sign by more than two standard errors, and is not 0."""
    d = [h - l for h, l in zip(hi, lo)]
    n = len(d)
    mean = math.fsum(d) / n
    se = math.sqrt(math.fsum((x - mean) ** 2 for x in d) / (n - 1) / n)
    assert n == KEYS and sign * mean > 2 * se and sign * mean > 0, (what, mean, se)
    return mean, se


def _off(hi, lo, what) -> None:
    """a CONTROL arm: with the operand's own setting off, the per-key lists are equal, not nearly."""
    assert len(hi) == len(lo) == KEYS and hi == lo, (what, next((i, h, l) for i, (h, l) in enumerate(zip(hi, lo)) if h != l))


def _only(lo, hi, own) -> None:
    """the attribute changes its own beat field and no other of the five a speech writes (V2 p2 §C.6): the others are equal key by key."""
    for f in SPEECH_FIELDS:
        a, b = _col(lo, lambda x: getattr(x, f)), _col(hi, lambda x: getattr(x, f))
        assert (a != b) if f == own else (a == b), (own, f)


def _ends(build, **kw) -> tuple:
    """the same scene at the attribute's two ends, on the same keys: `build(level)` -> the beats."""
    return build(LO), build(HI)


def test_the_speakers_reason_moves_relevance_and_gap_and_nothing_else():
    """REASON (A-143, R1; V2 p2 §C.6): the content. With its share of the dice held off (the ground's `reason` 0, so only Presence rolls), a
    speaker's Reason 7 against 1 raises `relevance` and, before a power-6 respondent, lifts the `standing` term (`gap`) and with each the
    share carried; the other four beat fields are equal key by key. CONTROL: `relevance` off and `gap_step` 0 and the dice share off, the
    margins are equal on every key."""
    checked = 0
    tell = lambda r, power=0.0, **o: _beats(_abridged(dict(reason=r), dict(power=power), **o))
    lo, hi = _ends(tell)
    _sign(_carried(hi), _carried(lo), +1, "reason relevance carried"); checked += 1
    _sign(_col(hi, lambda b: b.relevance), _col(lo, lambda b: b.relevance), +1, "relevance"); checked += 1
    _only(lo, hi, "relevance"); checked += 1
    lo, hi = _ends(lambda v: tell(v, relevance=0, gap_step=0.0))
    _off(_margin(hi), _margin(lo), "reason: relevance and gap off"); checked += 1
    lo, hi = _ends(lambda v: tell(v, power=6.0, relevance=0))      # `gap`: the other side's circumstances, answered by Reason
    _sign(_carried(hi), _carried(lo), +1, "reason gap carried"); checked += 1
    _sign(_term(lo, "standing"), _term(hi, "standing"), +1, "gap: the standing term falls with Reason"); checked += 1
    lo, hi = _ends(lambda v: tell(v, power=6.0, relevance=0, gap_step=0.0))
    _off(_margin(hi), _margin(lo), "reason: gap_step 0"); checked += 1
    assert checked == 7


def _framed(level, **over):
    """a trial whose judge holds three wants (gold bears on the matter his way, kin against, faith not at all): the speaker frames a `want`
    ground on one of them from what he BELIEVES the judge holds (`view`), then speaks on it; `(beats, views, the frame a perfect reader picks)`."""
    holds = (("want", "gold", 0.9, 0.9), ("want", "kin", 0.6, -0.5), ("want", "faith", 0.5, 0.0))
    inp = replace(_trial(dict(attunement=level), {}, dict(holds=holds), **over), frames=tuple((c, t) for c, t, _, _ in holds))
    st, a = _sit(inp, tracks=(("a", 0.0), ("b", 0.0), ("j", 1.0))), inp.room[0]
    beats, views = [], []
    for i in range(KEYS):
        rng = _key("frame", i)
        v = P.view(inp, st, a, rng)
        o = next(o for o in v.options if (o.move, o.ground) == ("argue", "consequence"))
        beats.append(P.exchange(inp, st, a, Choice(o.move, o.ground, o.item, o.relation), rng, o.frame)[1])
        views.append(v)
    return beats, views, P.frame(inp, [inp.room[2]], "for", "consequence"), P.mood(inp, st, a)


def test_the_speakers_attunement_moves_the_frame_and_the_gauge():
    """ATTUNEMENT (A-141, A-142): the framing and the gauge. A speaker of Attunement 7 against 1 frames the ground on what the judge truly holds
    more often, so the share carried rises (and no other beat field of the five differs); and he reads the room truer: his view's mood is nearer the
    room's. CONTROL: a perfect reading (`read_blur` and `bias_step` 0): the frame is the true best at both ends and the margins and the views'
    moods are equal key by key."""
    checked = 0
    (lo, vlo, best, mood), (hi, vhi, _, _) = _framed(LO), _framed(HI)
    assert best == "gold" and 0 < mood < 1
    _sign([float(b.frame == best) for b in hi], [float(b.frame == best) for b in lo], +1, "frame is the true best"); checked += 1
    _sign(_carried(hi), _carried(lo), +1, "attunement carried"); checked += 1
    _only(lo, hi, "frame"); checked += 1
    _sign([abs(v.mood - mood) for v in vlo], [abs(v.mood - mood) for v in vhi], +1, "the gauge: the perceived mood's error falls"); checked += 1
    (lo, vlo, best, mood), (hi, vhi, _, _) = _framed(LO, read_blur=0.0, bias_step=0.0), _framed(HI, read_blur=0.0, bias_step=0.0)
    _off(_col(hi, lambda b: b.frame), _col(lo, lambda b: b.frame), "perfect reading: the frame"); checked += 1
    _off(_margin(hi), _margin(lo), "perfect reading: the margin"); checked += 1
    _off([v.mood for v in vhi], [v.mood for v in vlo], "perfect reading: the perceived mood"); checked += 1
    assert set(_col(lo, lambda b: b.frame)) == {best} and {v.mood for v in vlo} == {mood}
    assert checked == 7


def test_the_speakers_presence_moves_heard_and_its_share_of_the_dice():
    """PRESENCE (A-143): the delivery. Before a crowd (weight 30 against `crowd_at` 12) a speaker of Presence 7 against 1 is heard more whole
    (`heard`) and carries more, the dice held Reason's (the venue's lean cancels the crowd's pull, so `k` is 10) so that `heard` is the whole
    of it; no other beat field of the five differs. CONTROL: `heard_step` 0, the margins are equal on every key."""
    checked = 0

    def rally(presence, **o):
        rite = _rite(close="hearers", turns=3, moves=(("for", ("argue", "rest")), ("against", ())), reply=(("for", "raise"),), silence="free",
                     reason_lean=0.2)
        inp = _inp([_p("a", "for", presence=presence), _p("crowd", None, True, weight=30, stake=(0.2, 0.0, 0.0))], rite, _set(**o), _grounds(1.0))
        return _beats(inp)

    lo, hi = _ends(rally)
    _sign(_carried(hi), _carried(lo), +1, "presence carried"); checked += 1
    _sign(_col(hi, lambda b: b.heard), _col(lo, lambda b: b.heard), +1, "heard"); checked += 1
    _only(lo, hi, "heard"); checked += 1
    lo, hi = _ends(lambda v: rally(v, heard_step=0.0))
    _off(_margin(hi), _margin(lo), "presence: heard_step 0"); checked += 1
    assert checked == 4


def test_the_speakers_grace_moves_esteem_and_nothing_else():
    """GRACE (A-143): the conduct. In a trial that asks Grace 5, a speaker of Grace 7 against 1 stands better with the room than the man
    opposite (`esteem`) and carries more; no other beat field of the five differs. CONTROL: `esteem_step` 0, the margins are equal on every key."""
    checked = 0
    trial = lambda g, **o: _beats(_trial(dict(grace=g), {}, {}, **o))
    lo, hi = _ends(trial)
    _sign(_carried(hi), _carried(lo), +1, "grace carried"); checked += 1
    _sign(_col(hi, lambda b: b.esteem), _col(lo, lambda b: b.esteem), +1, "esteem"); checked += 1
    _only(lo, hi, "esteem"); checked += 1
    lo, hi = _ends(lambda v: trial(v, esteem_step=0.0))
    _off(_margin(hi), _margin(lo), "grace: esteem_step 0"); checked += 1
    assert checked == 4


def test_the_speakers_focus_acts_only_under_a_pull():
    """FOCUS (R1, B14): the hold. Pressed in a trial (his heat and a rattle, and the times' `unrest`) a speaker of Focus 7 against 1 is pulled less
    off the point (`drift`) and carries more, modestly; no other beat field of the five differs. CONTROL: no pull (no `unrest`, no heat, no
    rattle): `drift` is 0 at both ends and the margins are equal on every key; and with `off_step` 0 the drift still differs but moves nothing."""
    checked = 0

    def pressed(focus, pull=True, **o):
        inp = _trial(dict(focus=focus), {}, {}, rite=_rite(turns=5, standard=5.0, reason_lean=0.2, unrest=0.5 if pull else 0.0), **o)
        return _beats(inp, st=_state(inp, a=Cond(heat=1.0, rattles=1)) if pull else None)

    lo, hi = _ends(pressed)
    assert max(_col(lo, lambda b: b.drift)) > 0
    _sign(_carried(hi), _carried(lo), +1, "focus carried"); checked += 1
    _sign(_col(hi, lambda b: b.drift), _col(lo, lambda b: b.drift), -1, "drift falls with Focus"); checked += 1
    _only(lo, hi, "drift"); checked += 1
    lo, hi = _ends(lambda v: pressed(v, pull=False))
    assert set(_col(lo, lambda b: b.drift)) == set(_col(hi, lambda b: b.drift)) == {0.0}
    _off(_margin(hi), _margin(lo), "focus: pull 0"); checked += 1
    lo, hi = _ends(lambda v: pressed(v, off_step=0.0))
    assert _col(lo, lambda b: b.drift) != _col(hi, lambda b: b.drift)
    _off(_margin(hi), _margin(lo), "focus: off_step 0"); checked += 1
    assert checked == 5


def test_the_speakers_will_is_his_staying_power_and_silent_at_the_tell():
    """WILL (R1, A-138): `weary`. On his fifth turn at a trial a speaker of Will 7 against 1 has more staying power, so the `weary` term of the
    obstacle is less and he carries more; no other beat field of the five differs. CONTROL: `weary_step` 0, the margins are equal on every key.
    LIMIT (A-138): at a quiet tell nothing has been spent, and his Will moves nothing at all: the margins are equal."""
    checked = 0

    def fifth(will, **o):
        inp = _trial(dict(will=will), {}, {}, **o)
        return _beats(inp, st=_state(inp, a=Cond(spoken=4, spent=4.0)))

    lo, hi = _ends(fifth)
    _sign(_carried(hi), _carried(lo), +1, "will carried"); checked += 1
    _sign(_term(lo, "weary"), _term(hi, "weary"), +1, "the weary term falls with Will"); checked += 1
    _only(lo, hi, None); checked += 1
    lo, hi = _ends(lambda v: fifth(v, weary_step=0.0))
    _off(_margin(hi), _margin(lo), "will: weary_step 0"); checked += 1
    lo, hi = _ends(lambda v: _beats(_abridged(dict(will=v), {})))
    _off(_margin(hi), _margin(lo), "will: silent at the tell"); checked += 1
    assert checked == 5


def test_r11_the_dice_are_reason_and_presence_by_the_ground_and_the_venue():
    """R11: the dice a speech rolls are a blend of Reason and Presence, Reason's share `k` set by the ground's weight and the venue's lean.
    At `k` 10 Presence moves the pool not at all (the margins are equal on every key once `heard`, its other operand, is off) and Reason
    moves the share carried; at `k` 0 Reason moves it not at all (its other two operands off) and Presence moves the share carried; and a venue
    that leans to Reason (a trial, +0.2) gives Reason the steeper pool, one that leans to Presence (a rally, -0.3) gives Presence the steeper."""
    checked = 0
    one = lambda col, who, **o: (lambda v: _beats(_abridged({who: v}, {}, col=col, **o)))
    lo, hi = _ends(one(1.0, "presence", heard_step=0.0))
    _off(_margin(hi), _margin(lo), "k 10: Presence moves nothing"); checked += 1
    lo, hi = _ends(one(1.0, "reason"))
    _sign(_carried(hi), _carried(lo), +1, "k 10: Reason carried"); checked += 1
    lo, hi = _ends(one(0.0, "reason", relevance=0, gap_step=0.0))
    _off(_margin(hi), _margin(lo), "k 0: Reason moves nothing"); checked += 1
    lo, hi = _ends(one(0.0, "presence"))
    _sign(_carried(hi), _carried(lo), +1, "k 0: Presence carried"); checked += 1

    def slopes(lean):
        inp = _trial({}, {}, {}, col=0.5, rite=_rite(turns=5, standard=5.0, reason_lean=lean))
        a = inp.room[0]
        pool = lambda **kw: P.case_pool(inp, replace(a, **kw), "consequence")
        return pool(reason=HI) - pool(reason=LO), pool(presence=HI) - pool(presence=LO)

    r, p = slopes(0.2)
    assert r > p > 0, (r, p); checked += 1
    r, p = slopes(-0.3)
    assert p > r > 0, (r, p); checked += 1
    assert checked == 6


# ---------------------------------------------------------------- the adjudicator's five, the judge hearing a speech (A-144; V2 p2 §C.3)
# One judge `j` sits, so the beat's margin is his own and `moved["j"]` is how far the speech or the press moved his track.
def _liar():
    """a man who KNOWS the matter false and speaks for it (his own word, a ploy)."""
    return dict(believes=-1.0)


def test_the_adjudicators_reason_validates_what_he_hears():
    """REASON (A-144): validation. A judge of Reason 7 against 1 takes in a sound but plain speaker (Reason 7, Grace 2) against a polished one
    (Reason 1, Grace 7) the better, and the polished one the worse: the share carried and his own track's move go with the sign. CONTROL:
    `sense_step` 0, the margins are equal on every key."""
    checked = 0
    sound = lambda r, **o: _beats(_trial(dict(reason=7.0, grace=2.0), dict(reason=1.0, grace=7.0), dict(reason=r), **o))
    polished = lambda r, **o: _beats(_trial(dict(reason=1.0, grace=7.0), dict(reason=7.0, grace=2.0), dict(reason=r), **o))
    lo, hi = _ends(sound)
    _sign(_carried(hi), _carried(lo), +1, "validation: the sound speaker"); checked += 1
    _sign(_moved(hi, "j"), _moved(lo, "j"), +1, "validation: the sound speaker moves his track"); checked += 1
    lo, hi = _ends(polished)
    _sign(_carried(hi), _carried(lo), -1, "validation: the polished speaker"); checked += 1
    for who in (sound, polished):
        lo, hi = _ends(lambda v: who(v, sense_step=0.0))
        _off(_margin(hi), _margin(lo), "validation: sense_step 0"); checked += 1
    assert checked == 5


def test_the_adjudicators_focus_filters_the_wanderer_and_the_theatre():
    """FOCUS (A-140, A-144): the relevance filter and the theatre filter. A judge of Focus 7 against 1 deducts a wandering speaker's drift
    (`wF`) and so he carries less; and a rattle that lands on a man moves a judge of Focus 7 not at all where it moves one of Focus 1 by twice
    its weight (`theatre`): the judge's track stays nearer the rattled man's side. CONTROL: `off_step` 0 the wanderer's margins are equal; a
    rattle that moves nobody (`rattle_gain` 0) with `off_step` 0 moves the judge equally at both ends, and a failed press's rebound is no theatre."""
    checked = 0
    wander = lambda f, **o: _beats(_trial(dict(focus=1.0), {}, dict(focus=f), rite=_rite(turns=5, standard=5.0, reason_lean=0.2, unrest=0.8), **o))
    lo, hi = _ends(wander)
    assert max(_col(lo, lambda b: b.drift)) > 0
    _sign(_carried(hi), _carried(lo), -1, "wF: the wanderer carries less"); checked += 1
    lo, hi = _ends(lambda v: wander(v, off_step=0.0))
    _off(_margin(hi), _margin(lo), "wF: off_step 0"); checked += 1

    def rattle(f, **o):
        inp = _trial(dict(will=2.0, care=(0.9, 0.5, 0.5), stake=(0.5, 0.0, 0.0)), dict(reason=6.0, presence=6.0), dict(focus=f), **o)
        return _beats(inp, mover="b", choice=PRESS)

    lo, hi = _ends(rattle)
    assert 0.1 < sum(_carried(hi)) / KEYS < 0.9 and any(b.rattled for b in hi)
    _sign(_moved(hi, "j"), _moved(lo, "j"), +1, "theatre: the rattle reaches a judge of Focus 7 less"); checked += 1
    lo, hi = _ends(lambda v: rattle(v, rattle_gain=0.0, off_step=0.0))
    _off(_moved(hi, "j"), _moved(lo, "j"), "theatre: a rattle that moves nobody"); checked += 1
    assert checked == 4


def test_the_adjudicators_attunement_reads_the_ploy_and_the_rattled_man():
    """ATTUNEMENT (A-144, R12, B10): a judge of Attunement 7 against 1 marks down a ploy (`ploy_step` x `wA`): a liar carries less and moves
    his track less; he reads the rattle of a man who is lying as guilt (`discern`) and the rattle of an honest man as nerves, and moves
    accordingly (a sign only: `discern` is within noise, V2 p4 §E). An honest strained man's speech is not marked down: the margins are equal
    on every key (B10). CONTROL: `ploy_step` 0 and `comfort_step` 0, the margins and the moves are equal."""
    checked = 0
    judged = lambda v, a=None, **o: _beats(_trial(dict(a or {}), {}, dict(attunement=v), **o))
    lo, hi = _ends(lambda v: judged(v, _liar()))
    _sign(_carried(hi), _carried(lo), -1, "ploy: the liar carries less"); checked += 1
    _sign(_moved(hi, "j"), _moved(lo, "j"), -1, "ploy: the liar moves the judge less"); checked += 1
    lo, hi = _ends(lambda v: judged(v, _liar(), ploy_step=0.0))
    _off(_margin(hi), _margin(lo), "ploy_step 0"); checked += 1

    def pressed(att, a, **o):
        inp = _trial(dict(a, will=2.0, care=(0.9, 0.5, 0.5), stake=(0.5, 0.0, 0.0)), dict(reason=6.0, presence=6.0), dict(attunement=att), **o)
        return _beats(inp, mover="b", choice=PRESS)

    lo, hi = _ends(lambda v: pressed(v, _liar()))
    assert any(b.rattled for b in hi)
    _sign(_moved(hi, "j"), _moved(lo, "j"), -1, "discern: a false man's rattle read as guilt moves the judge further"); checked += 1
    lo, hi = _ends(lambda v: pressed(v, _liar(), comfort_step=0.0))
    _off(_moved(hi, "j"), _moved(lo, "j"), "comfort_step 0"); checked += 1
    lo, hi = _ends(lambda v: pressed(v, dict(believes=1.0)))
    _sign(_moved(hi, "j"), _moved(lo, "j"), +1, "discern: an honest man's rattle read as nerves"); checked += 1
    strained = lambda v: _beats(inp := _trial(dict(believes=1.0), {}, dict(attunement=v)), st=_state(inp, a=Cond(strain=0.8, rattles=1)))
    lo, hi = _ends(strained)
    _off(_margin(hi), _margin(lo), "an honest strained man is not marked down (B10)"); checked += 1
    assert checked == 7


def test_the_adjudicators_presence_and_seat_cow_the_participant():
    """PRESENCE AND SEAT (A-144): `awe`. Before a judge of Presence 7 against 1, or of a seat of 7 against 1, a petitioner of Will 2 tires sooner
    (the `weary` term of his speeches is the more) and carries less, and a press on him meets less (it lands further). CONTROL: `awe_step` 0,
    the margins are equal on every key."""
    checked = 0

    def petitioner(who, v, press=False, **o):
        inp = _trial(dict(will=2.0, care=(0.9, 0.5, 0.5), stake=(0.5, 0.0, 0.0)), dict(reason=6.0, presence=6.0), {who: v}, **o)
        return _beats(inp, mover="b", choice=PRESS, st=_state(inp, a=Cond(spoken=2, spent=3.0))) if press else \
            _beats(inp, st=_state(inp, a=Cond(spoken=2, spent=3.0)))

    for who in ("presence", "power"):
        lo, hi = _ends(lambda v: petitioner(who, v))
        _sign(_term(hi, "weary"), _term(lo, "weary"), +1, f"awe from {who}: he tires sooner"); checked += 1
        _sign(_carried(hi), _carried(lo), -1, f"awe from {who}: he carries less"); checked += 1
        lo, hi = _ends(lambda v: petitioner(who, v, press=True))
        _sign(_margin(hi), _margin(lo), +1, f"awe from {who}: a press on him lands further"); checked += 1
        for press in (False, True):
            lo, hi = _ends(lambda v: petitioner(who, v, press, awe_step=0.0))
            _off(_margin(hi), _margin(lo), f"awe_step 0 ({who}, press {press})"); checked += 1
    assert checked == 10


def test_the_adjudicators_grace_is_the_folds_and_moves_nothing_in_the_sitting():
    """GRACE (A-144): reception is the fold's (B33.51), not the sitting's, so here only its control: a judge of Grace 1 and one of Grace 7
    hear the same speech and the same press to the same margins and move to the same tracks, key by key."""
    checked = 0
    # the argument is heard where validation shapes it (a sound plain speaker against a polished one), the press where the target holds something
    for choice, mover, a, b in ((ARGUE, "a", dict(reason=7.0, grace=2.0), dict(reason=1.0, grace=7.0)),
                                (PRESS, "b", dict(care=(0.9, 0.5, 0.5), stake=(0.5, 0.0, 0.0)), {})):
        lo, hi = _ends(lambda v: _beats(_trial(a, b, dict(grace=v)), mover=mover, choice=choice))
        _off(_margin(hi), _margin(lo), f"a judge's Grace: the margin ({choice.move})"); checked += 1
        _off(_col(hi, lambda b: b.moved), _col(lo, lambda b: b.moved), f"a judge's Grace: the tracks ({choice.move})"); checked += 1
    assert checked == 4


def test_a_listeners_will_resists_the_argument_and_the_press():
    """WILL, the resisting attribute (A-137): not one of the adjudicator's five. A judge of Will 7 against 1 is the harder to carry by an
    argument (the share carried falls), and a man of Will 7 against 1 is the harder to rattle (the press lands less far)."""
    checked = 0
    lo, hi = _ends(lambda v: _beats(_trial({}, {}, dict(will=v))))
    _sign(_carried(hi), _carried(lo), -1, "a judge's Will against an argument"); checked += 1
    lo, hi = _ends(lambda v: _beats(_trial(dict(will=v, care=(0.9, 0.5, 0.5), stake=(0.5, 0.0, 0.0)), dict(reason=6.0, presence=6.0), {}), mover="b", choice=PRESS))
    _sign(_margin(hi), _margin(lo), -1, "a man's Will against a press"); checked += 1
    assert checked == 2
