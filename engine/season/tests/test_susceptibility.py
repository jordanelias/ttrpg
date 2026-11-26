"""B24.35 -- WHICH GROUND MOVES WHOM: the four conditions of an act and the grounds they back (WGM edits 2-3; `17_CENSUS_C1A_02` W4's `which_ground` half).

A hearer's `Person.traits` (`moved_by_evidence`, `_consequence`, `_authority`, `_solidarity`; B04.07) say which grounds move HIM. For one who holds none every ground moves him
as it always did; for one who holds some, the host (`seam/wrappers/sigma.py::_backed`) says which of THOSE grounds back this act -- the ground's own `backed_by` cell
(`rosters.yaml: grounds`), one of the four `capability_when_keys` conditions (`sigma.WHEN_BACKING`) -- and the proceeding (`proceeding.speech`) counts a ground's positive fit with him
only when it is in `Present.backed`. A hand-built world (`probes.tiny_world`) and the module reached by its composition row; the realm control reads one season.
"""
from __future__ import annotations

from dataclasses import replace

from ..data.rosters import FACTION_BY_PROP
from ..queries.inputs import Choice
from ..seam.wrappers import sigma as S
from ..state.carriers import Claim, Proposition, Tenure
from .test_sc_proceeding_host import ROWS, _build, _world
from .test_sc_proceeding_module import P, _key

ARGUER, HEARER, THIRD = "p_low", "p_mid", "p_other"
TRAITS = ("moved_by_evidence", "moved_by_consequence", "moved_by_authority", "moved_by_solidarity")
SEEDS = 400


def _sitting(*, traits=TRAITS, stance=(), topic="m1", cited=(), arguer_ledger=(), hearer_ledger=(), pursuits=None, verb="argue"):
    """`tiny_world`, the copyist `p_low` arguing to the clerk `p_mid` in the full conversation (`verb`, `argue` unless given): the clerk holds `traits`, his own `stance` rows, his `pursuits`
    and `hearer_ledger`; the copyist's own ledger is `arguer_ledger`. Returns `(world, Input)`."""
    w = _world()
    w.persons[HEARER].traits = frozenset(traits)
    w.persons[HEARER].stance = list(stance)
    w.persons[HEARER].pursuits = dict(pursuits or {})
    w.persons[HEARER].ledger = hearer_ledger if isinstance(hearer_ledger, list) else list(hearer_ledger)
    w.persons[ARGUER].ledger = list(arguer_ledger)
    inp, _card = _build(w, (ARGUER,), row=ROWS["conversation"], subject=HEARER, verb=verb, topic=topic, effort=1, cited=cited)
    return w, inp


def _backed(inp):
    return next(p for p in inp.room if p.id == HEARER).backed


def _deed(holder, about):
    """A firsthand deed claim of `about`'s that a hearer with `liberty` for his pursuit scores against him (`fight.declared`: -0.33 on liberty, `test_cr87`'s reading)."""
    return Claim(f"c_deed_{holder}", holder, about, "fight.declared", True, 0, "firsthand", 100, "own")


def test_no_seated_trait_is_hash_equal(monkeypatch):
    """CONTROL (WGM gate (a)). Seed 0, one season, the realm's seated traits stripped: the hash is the same with the backing gate taken out (`_backed` answering `None`, every ground,
    as it did before this item) as with it in, so nothing this item added -- `Present.backed`, the cited kinds, the speech's gate -- moves a world that seats no trait. (`Person.traits`
    is hashed, so the control strips it from BOTH arms; the realm as built seats some, which is asserted.) FALSIFIER: a gate that moves a hearer who holds no trait."""
    from ..boot.realm import build_realm
    from ..harness.populated import run

    def season(gate):
        w = build_realm(0)
        seated = sum(1 for p in w.persons.values() if p.traits)
        for p in w.persons.values():
            p.traits = frozenset()
        if not gate:
            monkeypatch.setattr(S, "_backed", lambda *a: None)
        run(1, 0, w=w)
        return w.content_hash(), seated
    (with_gate, seated), (without, _) = season(True), season(False)
    assert seated > 0 and with_gate == without


def test_a_solidarity_hearer_is_moved_more_often_only_when_the_condition_holds():
    """The `fit` source, read at the sitting. A hearer who holds `moved_by_solidarity` and is argued to on `solidarity` (his bond-care raised so the ground's fit is positive,
    the same for his pair-mate who holds no trait), 400 paired seeds, the track he is left on: with the arguer's regard at or above the floor (`regard_at_least: 3`) he is moved
    exactly as his pair-mate is, at every seed -- the ground backs the act and nothing is added; below it the positive fit counts for nothing with him, so he is moved LESS than his
    pair-mate at every seed and, over the seeds, past where he started less often; his pair-mate's own rate moves smoothly with regard, the trait's step is the floor. FALSIFIER: the
    two equal with the condition unmet (the gate is not read), or unequal with it met (the trait is acting as a flat modifier)."""
    def room(trait, regard):
        _w, inp = _sitting(traits=("moved_by_solidarity",) if trait else (), stance=[(ARGUER, regard, 1)])
        return replace(inp, room=tuple(replace(p, care=(0.5, 0.5, 0.9)) if p.id == HEARER else p for p in inp.room))     # the clerk values whom he stands with

    def decide(view, me):
        o = next((o for o in view.options if o.move == "argue" and o.ground == "solidarity") if me.id == ARGUER else (o for o in view.options if o.move == "rest"))
        return Choice(o.move, o.ground, o.item, o.relation)

    def tracks(inp):
        return [dict(P.proceed(inp, _key("susc", i), decide=decide).state.tracks)[HEARER] for i in range(SEEDS)]

    def moved(inp, track):
        return sum(t > next(p for p in inp.room if p.id == HEARER).start for t in track)
    checked, rates = 0, {}
    for regard in (2, 3, 4):
        plain, trait = room(False, regard), room(True, regard)
        assert _backed(plain) is None and _backed(trait) == (("solidarity",) if regard >= 3 else ()), regard
        for p in (plain, trait):
            assert P.fit(p, next(x for x in p.room if x.id == HEARER), p.room[0], "for", "solidarity", None) > 0      # a positive fit is the thing the gate can take away
        tp, tt = tracks(plain), tracks(trait)
        rates[regard] = (moved(plain, tp), moved(trait, tt))
        for a, b in zip(tp, tt):
            checked += 1
            assert (a == b) if regard >= 3 else (b < a), (regard, a, b)
    assert checked >= 3 * SEEDS
    assert rates[3][1] == rates[3][0] and rates[4][1] == rates[4][0] and rates[2][1] < rates[2][0], rates
    assert rates[3][1] - rates[2][1] > 5 * (rates[3][0] - rates[2][0]), rates                 # the step at the floor is the trait's, not regard's own slope


def test_each_ground_is_backed_by_its_own_condition_alone():
    """A hearer who holds all four traits is backed on no ground with nothing to back it; each fact of the act backs ITS ground and no other: regard at the floor (clamped at
    `STANCE_MAX`) `solidarity`, a cited `record` `evidence`, a deed of the matter's subject in the ARGUER'S ledger that his pursuits score against him `consequence`, and the
    matter being a faction's creed he holds a live `commit` to `authority`. One who holds none is backed on every ground (`None`), and so is the arguer himself
    and a hearer of any act whose verb is not `backed_verbs`' (`tell`, `lie`).
    FALSIFIER: a fact that backs two grounds, or a ground backed by nothing it names."""
    assert _backed(_sitting()[1]) == ()
    assert _backed(_sitting(stance=[(ARGUER, 5, 5)])[1]) == ("solidarity",) and _backed(_sitting(stance=[(ARGUER, 2, 1)])[1]) == ()
    assert _backed(_sitting(cited=("record",))[1]) == ("evidence",) and _backed(_sitting(cited=("testimony",))[1]) == ()
    assert _backed(_sitting(pursuits={"liberty": 1.0}, topic=THIRD, arguer_ledger=[_deed(ARGUER, THIRD)])[1]) == ("consequence",)
    assert _backed(_sitting(pursuits={"honour": 1.0}, topic=THIRD, arguer_ledger=[_deed(ARGUER, THIRD)])[1]) == ()      # a deed his pursuits score for the doer
    creed = next(iter(FACTION_BY_PROP))
    w = _world()
    w.persons[HEARER].traits = frozenset(TRAITS)
    w.propositions[creed] = Proposition(creed, "OUGHT", THIRD, "creed", True, 0)
    asked = lambda: next(p for p in _build(w, (ARGUER,), row=ROWS["conversation"], subject=HEARER, verb="argue", topic=creed, effort=1)[0].room if p.id == HEARER).backed
    assert asked() == ()                                                                                              # a creed Proposition he is not committed to
    w.add_tenure(Tenure("t_creed", HEARER, creed, "commit", since=0))
    assert asked() == ("authority",)
    assert _backed(_sitting(traits=())[1]) is None and next(p for p in _sitting()[1].room if p.id == ARGUER).backed is None
    assert all(_backed(_sitting(verb=v, stance=[(ARGUER, 5, 5)])[1]) is None for v in ("tell", "lie"))     # a `tell` or a `lie` hears him as it always did: `backed_verbs` is `argue` alone


def test_no_when_key_reads_the_hearers_ledger(monkeypatch):
    """`consequence_held` reads the ARGUER'S own ledger judged by the HEARER'S pursuits, and never the hearer's ledger (`04` §B.2 F8). A hearer whose own ledger holds a deed claim
    his pursuits score against its doer moves nothing while the arguer's ledger holds none, and his ledger raises if `_backed` opens it (the builder's own reads of it, for his
    `believes`, are his); the same claim in the arguer's ledger backs `consequence`. FALSIFIER: a read of the hearer's ledger (raises), or a ground backed by a claim only he holds."""
    gate = {"on": False}

    class Shut(list):
        __iter__ = lambda self: self._guard("__iter__")
        __len__ = lambda self: self._guard("__len__")
        __getitem__ = lambda self, i: self._guard("__getitem__", i)
        __contains__ = lambda self, x: self._guard("__contains__", x)

        def _guard(self, name, *a):
            if gate["on"]:
                raise AssertionError("the hearer's ledger was opened by a condition")
            return getattr(super(), name)(*a)
    real = S._backed

    def guarded(w, hearer, ctx):
        gate["on"] = True
        try:
            return real(w, hearer, ctx)
        finally:
            gate["on"] = False
    monkeypatch.setattr(S, "_backed", guarded)
    _w, held_by_hearer = _sitting(traits=("moved_by_consequence",), pursuits={"liberty": 1.0}, topic=THIRD, hearer_ledger=Shut([_deed(HEARER, THIRD)]))
    assert _backed(held_by_hearer) == ()
    _w, held_by_arguer = _sitting(traits=("moved_by_consequence",), pursuits={"liberty": 1.0}, topic=THIRD, arguer_ledger=[_deed(ARGUER, THIRD)], hearer_ledger=Shut())
    assert _backed(held_by_arguer) == ("consequence",)
