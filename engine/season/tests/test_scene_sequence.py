"""B08.02 / B08.03 (`16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md`, "Gate"; ruling A-9: a scene is a short sequence) --
INSIDE ONE SCENE, AN INTERACTION MAY HANG ON THE BAND OF THE ONE BEFORE (R-03.c).

`Act.after` names the bands of the scene's previous interaction at which this one is attempted (`None`: always). The fold
reads it (`loop/resolve.py::_sequence_refusal`): outside the named bands the interaction is refused at the clause `sequence`
(`data/verbs.py::SEQUENCE_CLAUSE`), an Event with no `changes` (A-62), and the first interaction's Event stands (A-81). A
previous interaction whose prize is deferred to ENCOUNTER (`04` §C.4) defers what hangs on it, and the band read is the one
ENCOUNTER produces.

  FALSIFIERS: the second interaction folds although the first missed its band; a step after a deferred prize is refused at
  RESOLVE on the band nobody fought (`Declared`); a keyed `emits_on_refusal:` row with no `sequence:` key loads; at
  `interactions_per_scene = 1` the realm hash moves (`SEQ` "Falsifier"); a scene's interactions fold out of the chooser's order.
  CONTROLS: `after = None` folds as before; the shipped table loads.

The fold orders SCENES (B08.03), so a planted scene's interactions fold in the chooser's order whatever their strata.
"""
from __future__ import annotations

import copy
import types
from unittest import mock

import pytest
import yaml

from ..boot.realm import build_realm
from ..data import verbs as VERBS
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..data.rosters import COMBAT_BANDS, DECLARED
from ..data.verbs import VERB_TABLE
from ..harness import populated as POP
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..seam.wrappers import combat
from ..state.carriers import Act, Scene
from .test_in12_step9 import ARGUER, HEARER, _argue_world

CHAL, ACC, OTHER, HIGH = "p_mid", "p_low", "p_other", "p_high"     # `tiny_world`: all at the hearth `Hh`
FOUGHT = tuple(b for b in COMBAT_BANDS if b != DECLARED)           # the bands a fight reports at ENCOUNTER

# The realm content hash of `build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("interactions_per_scene", 1))` after one
# season, `PYTHONHASHSEED=0` (the plan's HASH READING), reading @769f305cc6a809d4cc0c9f22ee78806cfb5bc973 -- B08's base
# before B08.02 edited any game code. A TEST-LOCAL PIN NO OTHER ITEM MAY MOVE: with one interaction per scene there is
# no within-scene order and no previous interaction, so neither the `after` read nor B08.03's scene key may move it.
ONE_INTERACTION_SEASON_1 = "0325a35125b97745272e900f5a926db0"


@pytest.fixture(autouse=True)
def _a_dispute_behind_every_challenge(monkeypatch):
    """`challenge`'s DISPUTE conjunct is `test_cr87_violence_contexts.py`'s; here every challenger holds one."""
    monkeypatch.setattr(world_q, "holds_dispute", lambda p, referent, *read: True)


def _world():
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _run(w, d, *scenes):
    """RESOLVE then ENCOUNTER over the planted scenes (`{id: Scene}`, the shape DELIBERATE returns), logged as a lap
    does. Returns `(RESOLVE's events, ENCOUNTER's events)`."""
    depth = w.fixtures.get("contest_max_depth")
    w.step, w.frozen = Step.RESOLVE, False
    acts = [a for sc in scenes for a in sc.acts]
    first = d.resolve(mint_token(w, WriteClass.ACTS), acts, depth, scenes={sc.id: sc for sc in scenes})
    second = d.encounter(mint_token(w, WriteClass.ACTS), first, depth)
    w.log.extend(first + second)
    return first, second


def _of(d, events, act_id):
    return [e for e in events if d.act_of[e.id].id == act_id]


class _Spy:
    """Counts the personal-combat scenes the fold fights (wraps `combat.entry_for`, read at call time)."""

    def __init__(self):
        self.calls = []
        self._real = combat.entry_for

    def __call__(self, prize, module, *rest):
        entry, refusal = self._real(prize, module, *rest)
        if entry is None:
            return entry, refusal

        def fn(inp, rng, **kw):
            got = entry.fn(inp, rng, **kw)
            self.calls.append(inp)
            return got
        return types.SimpleNamespace(fn=fn), refusal

    def patch(self):
        return mock.patch.object(combat, "entry_for", self)


# ---------------------------------------------------------------------------------------------------------------------
# 1 -- A STEP OUTSIDE ITS BAND IS REFUSED AT `sequence`, AND THE STEP BEFORE IT STANDS
# ---------------------------------------------------------------------------------------------------------------------

def _challenge_then_fight(after):
    """`[challenge, fight]` (`SEQ`'s own pair): the challenger issues the challenge, then fights the man he challenged."""
    ch = Act(id="ch0", actor=CHAL, verb="challenge", payload={"subject": ACC}, scene="sc0")
    f = Act(id="f1", actor=CHAL, verb="fight", payload={"subject": ACC}, scene="sc0", after=after)
    return Scene("sc0", CHAL, acts=[ch, f])


def test_unconditional_second_step_is_fought_as_before():
    # CONTROL: no `after` -- the fight is declared at RESOLVE and fought at ENCOUNTER, as before B08.02.
    w, d = _world()
    first, second = _run(w, d, _challenge_then_fight(None))
    assert [e.kind for e in _of(d, first, "f1")] == ["fight.declared"], [e.kind for e in first]
    assert _of(d, second, "f1"), "CONTROL: the unconditional fight was not fought at ENCOUNTER"


ARGUE_BANDS = tuple(b for b, written in VERB_TABLE["argue"].writes_by_degree.items() if written)   # `argue` writes at Overwhelming and Success


def _argue_scene(i, after, first_to=HEARER, then_to=HEARER):
    """`[argue, argue]` on one uttered Proposition, in one scene, the arguer's `i`-th: the first argument rolls at RESOLVE (a contested,
    non-deferred prize; the act id keys its draw, so `i` picks the band it lands in), the second hangs on `after`.
    Returns `(driver, RESOLVE's events, the second act)`."""
    w, d, pid, _ = _argue_world()
    f = Act(id=f"ar_{i}", actor=ARGUER, verb="argue", payload={"subject": pid, "to": first_to}, scene="sc0")
    s = Act(id=f"ar_{i}b", actor=ARGUER, verb="argue", payload={"subject": pid, "to": then_to}, scene="sc0", after=after)
    first, _second = _run(w, d, Scene("sc0", ARGUER, acts=[f, s]))
    return d, first, s


def _first_band(i):
    d, first, _s = _argue_scene(i, None)
    return {e.degree for e in _of(d, first, f"ar_{i}")}


def _skipped(d, first, s):
    return _of(d, first, s.id)


def test_second_step_skipped_when_first_misses_band_logs_sequence_refusal():
    """A CONTESTED prior reaches a real band at RESOLVE (`argue`, a roll on the actor's pool, an act id keying the draw): the first act id,
    scanned upward from 0, whose argument lands outside the bands `argue` writes in (Failure or Partial) is the miss; the same act id lands there
    on every run (the draw is keyed to it and the seed). The second argument hung on the bands `argue` writes in is then refused at `sequence`,
    with no changes and no band (A-62), while the first's Event stands (A-81)."""
    miss = next(i for i in range(40) if not (_first_band(i) & set(ARGUE_BANDS)))
    (band,) = _first_band(miss)
    assert band in ("Failure", "Partial"), band
    d, first, s = _argue_scene(miss, ARGUE_BANDS)
    prior = _of(d, first, f"ar_{miss}")
    assert prior and {e.degree for e in prior} == {band}, "the first argument did not reach the band the scan read"
    skipped = _skipped(d, first, s)
    assert [e.kind for e in skipped] == list(VERB_TABLE["argue"].refusal_for(VERBS.SEQUENCE_CLAUSE)), [(e.kind, e.degree) for e in first]
    assert all(e.changes == [] and e.degree is None for e in skipped), "a refusal writes nothing and carries no band (A-62)"
    assert all(e in prior or e in skipped for e in first), "an Event neither the first's nor the refusal"

    # CONTROLS: hung on the band it reached, the second is NOT refused; unhung, it folds as before; and a first that reaches a written band
    # lets the second through.
    d, first, s = _argue_scene(miss, (band,))
    assert _skipped(d, first, s) and all(e.kind != "argument.refused" for e in _skipped(d, first, s)), "hung on the band reached, the second was refused"
    won = next(i for i in range(40) if _first_band(i) & set(ARGUE_BANDS))
    d, first, s = _argue_scene(won, ARGUE_BANDS)
    assert all(e.kind != "argument.refused" for e in _skipped(d, first, s)), "a first that reached a written band still refused the second"


def test_second_step_skipped_when_first_was_refused_at_admission():
    """THE NONE-BAND POLICY (`_sequence_refusal`'s tag): a first argument refused at admission (here: the arguer names himself as the hearer,
    the `counterparty` clause) reaches no band, so the second -- whose own hearer is valid -- hung on any band is skipped; unhung it folds."""
    d, first, s = _argue_scene(0, ARGUE_BANDS, first_to=ARGUER)
    prior = _of(d, first, "ar_0")
    assert [e.kind for e in prior] == ["argument.refused"] and all(e.degree is None for e in prior), [(e.kind, e.degree) for e in prior]
    skipped = _skipped(d, first, s)
    assert [e.kind for e in skipped] == ["argument.refused"] and all(e.changes == [] and e.degree is None for e in skipped)
    d, first, s = _argue_scene(0, None, first_to=ARGUER)          # CONTROL: unhung, the second argument's own fold runs and is not refused
    assert all(e.kind != "argument.refused" for e in _skipped(d, first, s)), [(e.kind, e.degree) for e in first]


# ---------------------------------------------------------------------------------------------------------------------
# 2 -- A DEFERRED PRIZE DEFERS WHAT HANGS ON IT
# ---------------------------------------------------------------------------------------------------------------------

def _fight_then_fight(after):
    """`[fight, fight]`: he fights one man and, at the bands `after` names, then a second. `the body` is fought at
    ENCOUNTER (`rosters.yaml`, `step: ENCOUNTER`), so at RESOLVE the first reaches only its declared band."""
    w, d = _world()
    f0 = Act(id="f0", actor=ACC, verb="fight", payload={"subject": CHAL}, scene="sc0")
    f1 = Act(id="f1", actor=ACC, verb="fight", payload={"subject": OTHER}, scene="sc0", after=after)
    spy = _Spy()
    with spy.patch():
        first, second = _run(w, d, Scene("sc0", ACC, acts=[f0, f1]))
    return w, d, first, second, spy


def test_deferred_first_step_defers_second():
    # Hung on every band a fight reports: the step after the deferred one is deferred with it, then fought.
    w, d, first, second, spy = _fight_then_fight(FOUGHT)
    for aid in ("f0", "f1"):
        declared = _of(d, first, aid)
        assert [e.kind for e in declared] == ["fight.declared"], (aid, [e.kind for e in first])
        assert all(e.degree == DECLARED and e.changes == [] for e in declared)
    band = {e.degree for e in _of(d, second, "f0")}
    assert len(band) == 1 and band <= set(FOUGHT), band
    (band,) = band
    assert len(spy.calls) == 2, "the step hung on the band ENCOUNTER produced was not fought"
    assert "fight.declared" not in [e.kind for e in _of(d, second, "f1")]

    # Hung on every band BUT the one the first fight produces: deferred at RESOLVE (never read against `Declared`),
    # then refused at `sequence` on the band ENCOUNTER produced.
    w, d, first, second, spy = _fight_then_fight(tuple(b for b in FOUGHT if b != band))
    assert [e.kind for e in _of(d, first, "f1")] == ["fight.declared"], "refused at RESOLVE on a band nobody fought"
    assert {e.degree for e in _of(d, second, "f0")} == {band}, "the first fight did not reproduce its band"
    skipped = _of(d, second, "f1")
    assert [e.kind for e in skipped] == list(VERB_TABLE["fight"].refusal_for(VERBS.SEQUENCE_CLAUSE))
    assert all(e.changes == [] and e.degree is None for e in skipped)
    assert len(spy.calls) == 1, "the step outside its band was fought"


# ---------------------------------------------------------------------------------------------------------------------
# 3 -- THE CLAUSE IS DECLARED: A KEYED ROW MUST KEY `sequence:`
# ---------------------------------------------------------------------------------------------------------------------

_SRC = yaml.safe_load(VERBS.VERB_TABLE_YAML.read_text())


def _loads(mutate):
    """`_load_verb_table` over the shipped table with `mutate` applied; the SystemExit text, or None."""
    doc = copy.deepcopy(_SRC)
    mutate(doc)
    with mock.patch.object(VERBS, "VERB_TABLE_YAML") as fake:
        fake.exists.return_value = True
        fake.read_text.return_value = yaml.safe_dump(doc, allow_unicode=True)
        try:
            VERBS._load_verb_table()
        except SystemExit as e:
            return str(e)
    return None


def test_keyed_row_without_sequence_key_is_refused_at_load():
    assert _loads(lambda doc: None) is None, "CONTROL: the shipped table loads"
    keyed = [r["verb"] for r in _SRC["verbs"] if isinstance(r.get("emits_on_refusal"), dict)]
    assert keyed, "no keyed row: the rule observed nothing"
    for verb in keyed:      # PER ROW, NOT PER VERB NAMED: every keyed row can be a second interaction
        def drop(doc, verb=verb):
            next(r for r in doc["verbs"] if r["verb"] == verb)["emits_on_refusal"].pop("sequence", None)
        msg = _loads(drop)
        assert msg is not None and f"verb_table.yaml: {verb!r} keys no refusal for the failable clause(s) ['sequence']" in msg, (verb, msg)


# ---------------------------------------------------------------------------------------------------------------------
# 4 -- THE CONTROL: ONE INTERACTION PER SCENE IS TODAY'S WORLD
# ---------------------------------------------------------------------------------------------------------------------

def test_one_interaction_per_scene_hash_equals_today():
    w = build_realm(0, fixtures=DEFAULT_FIXTURES.sweep("interactions_per_scene", 1))
    assert w.fixtures.get("interactions_per_scene") == 1
    POP.run(seasons=1, seed=0, w=w)
    assert w.content_hash() == ONE_INTERACTION_SEASON_1


# ---------------------------------------------------------------------------------------------------------------------
# 5 -- A SCENE FOLDS CONTIGUOUSLY, IN THE CHOOSER'S ORDER (B08.03's scene key)
# ---------------------------------------------------------------------------------------------------------------------

def test_scene_folds_contiguously_in_chooser_order():
    """Two scenes whose interactions sit in different strata, in opposite orders: a fold ordering ACTS by stratum
    interleaves them and turns the first one round; a fold ordering SCENES keeps each whole and in the chooser's order.
    No stratum is declared here: the order is the fold's own."""
    w, d = _world()
    sa = Scene("sa", CHAL, acts=[Act(id="a0", actor=CHAL, verb="challenge", payload={"subject": ACC}, scene="sa"),
                                 Act(id="a1", actor=CHAL, verb="fight", payload={"subject": ACC}, scene="sa")])
    sb = Scene("sb", HIGH, acts=[Act(id="b0", actor=HIGH, verb="fight", payload={"subject": OTHER}, scene="sb"),
                                 Act(id="b1", actor=HIGH, verb="challenge", payload={"subject": OTHER}, scene="sb")])
    _run(w, d, sa, sb)
    folded = [a.id for a in w.acts if a.id in {"a0", "a1", "b0", "b1"}]
    assert sorted(folded) == ["a0", "a1", "b0", "b1"], folded
    for sc in (sa, sb):
        at = [folded.index(a.id) for a in sc.acts]
        assert at == list(range(at[0], at[0] + len(at))), (sc.id, folded)


def test_realm_scenes_fold_contiguously_in_chooser_order_over_two_seasons():
    """R-03.c on the realm (B08.04's gate): over `build_realm(0)`, two seasons, EVERY scene whose interactions were folded two or more at
    a time (the act store's order is the fold's) was folded in the chooser's own order (`Scene.acts`) and with nothing of another scene
    between them. `checked >= 1` so a realm that formed no multi-interaction scene fails rather than passing on nothing."""
    w = build_realm(0)
    POP.run(seasons=2, seed=0, w=w)
    folded_at = {a.id: i for i, a in enumerate(w.acts)}
    checked = 0
    for sc in w.acts.scenes():
        at = [folded_at[a.id] for a in sc.acts if a.id in folded_at]
        if len(at) < 2:
            continue
        checked += 1
        assert at == sorted(at), (sc.id, "folded out of the chooser's order", at)
        assert at[-1] - at[0] == len(at) - 1, (sc.id, "another scene's act sits between this scene's interactions", at)
    assert checked >= 1, "the realm formed no scene of two interactions in two seasons: the order was not observed"
