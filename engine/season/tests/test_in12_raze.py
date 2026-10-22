"""v9 IN-12 step 11 -- `raze` (#453 §9.2, §10.4 step 11): the closer of `H-166` limit 3, licensed by
OCCUPATION (the exercised seat's faction `mustered` at a settlement another faction holds -- the read
`loop/effects_information.py::_seize_rung` inlines, copied into `loop/effects_founding.py::_eff_raze`).

The entry's falsifier, verbatim: *"`w.rungs` shrinks; a `raze` where the seat has no army is refused"*.
Every test drives the act through the REAL fold (`SeasonDriver.resolve`, the gate, the cascade) on
`build_realm(0)`; the occupation is made by a real `march` (`army.arrived`), never planted. Each claim
has a control one change away (no march, so no army), so the cause is the occupation and nothing else.

What is pinned AS IT READS, not as a design (`hole_register.yaml` H-228): the cascade is Layer 1's and
nothing else (`architecture/meta/04_CODE_ARCHITECTURE.md` §B.8), so what stood in the razed town is left
placeless and a Site's `rung` field keeps the gone id. Those assertions redden when H-228 closes.
"""

from engine.season.data.matrix import Step, WriteClass
from engine.season.harness import populated as POP
from engine.season.harness.populated import build_realm
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.state import gate as G
from engine.season.state.carriers import Act

CROWN = "fac_crown"
TOWN = "set_s_016"            # Hafenmark-held; no Crown member stands there at build
ACTOR, SEAT = "p_npc_033", "off_npc_033"   # a Crown seat granted `dispatch`; his army stands at `set_s_014`


def _fold(w, act, encounter=False):
    """Fold ONE act through the real driver's RESOLVE (and ENCOUNTER, for a `march`), into `w.log`."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    depth = w.fixtures.get("contest_max_depth")
    out = d.resolve(mint_token(w, WriteClass.ACTS), [act], depth)
    if encounter:
        out = out + d.encounter(mint_token(w, WriteClass.ACTS), out, depth)
    w.log.extend(out)
    return [e.kind for e in out]


def _raze(w, target=TOWN, act_id="rz1", actor=ACTOR, via=SEAT):
    return _fold(w, Act(id=act_id, actor=actor, verb="raze", payload={"subject": target}, via=via))


def _occupy(w, town=TOWN):
    """The Crown's army marches on `town` through the real fold and ARRIVES (`Unopposed`: no Hafenmark
    member defends it) -- occupation made by the verb that makes it, not planted."""
    kinds = _fold(w, Act(id="m1", actor=ACTOR, verb="march", payload={"subject": town}, via=SEAT),
                  encounter=True)
    assert "army.arrived" in kinds, kinds
    assert world_q.mustered(w, town, CROWN), "the Crown does not stand there"
    assert world_q.holder_faction_of(w, town) == "fac_hafenmark", "an arrival wrote a title (R-6)"
    return w


def test_in12_11_a_raze_where_the_seat_has_no_army_is_refused():
    """THE ENTRY'S SECOND FALSIFIER: no march, so the Crown is not `mustered` at the Hafenmark town --
    the same act, actor and seat is `raze.refused`, `w.rungs` is unmoved and the town stands. Its
    CONTROL is the next test (one change: the march)."""
    w = build_realm(0)
    assert world_q.mustered(w, TOWN, CROWN) == [], "fixture: the Crown already stands there"
    n = len(w.rungs)
    assert _raze(w) == ["raze.refused"]
    assert len(w.rungs) == n and TOWN in w.rungs
    assert "rung.razed" not in [e.kind for e in w.log]


def test_in12_11_an_occupied_settlement_is_razed_and_w_rungs_shrinks():
    """THE ENTRY'S FIRST FALSIFIER, `H-166` limit 3's: after the Crown's army arrives, the SAME act is
    `rung.razed` -- the town leaves `w.rungs` (one fewer), the Event is in `w.log` naming it, and no live
    Tenure names it any more."""
    w = _occupy(build_realm(0))
    n = len(w.rungs)
    assert _raze(w) == ["rung.razed"]
    assert len(w.rungs) == n - 1 and TOWN not in w.rungs
    razed = [e for e in w.log if e.kind == "rung.razed"]
    assert len(razed) == 1 and any(c.subject == TOWN for c in razed[0].changes), razed
    assert not [t for t in w.tenures if t.live and TOWN in (t.subject, t.object)]


def test_in12_11_every_closed_edge_is_admitted_under_the_cascade_and_nothing_opens(monkeypatch):
    """THE WRITE IS LAYER 1's CASCADE AND NOTHING ELSE (`04_CODE_ARCHITECTURE.md` §B.8): every Tenure
    the razing changes is a CLOSURE of an edge naming the town, none opened, each admitted by the gate:
    the RAZER'S OWN `contain` there under `T-m` (asked first: an owner closing his own edge), every
    other under `cascade` (the Rung is in the write's `gone`)."""
    w = _occupy(build_realm(0))
    naming = {t.id: t.subject for t in w.tenures if t.live and TOWN in (t.subject, t.object)}
    assert len(naming) >= 3, "fixture: the town carries its own contain and what stands in it"
    assert ACTOR in naming.values(), "fixture: the razer's army stands in the town"
    seen = []
    real = G.tenure_write_basis

    def spy(*args, **kw):
        out = real(*args, **kw)
        seen.append((args[1].id, args[2] is None, out))
        return out
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    assert _raze(w) == ["rung.razed"]
    assert {tid for tid, _, _ in seen} == set(naming), seen
    assert not any(opened for _, opened, _ in seen), seen
    assert all(basis == (G.T_M if naming[tid] == ACTOR else G.CASCADE) for tid, _, basis in seen), seen


def test_in12_11_each_decline_of_the_occupation_read_is_refused():
    """`_eff_raze`'s declines, each one change from the admitted razing above (the Crown's army stands
    under each place, the same seat and actor): the TERRITORY above the occupied town (the Crown is
    mustered under it and Hafenmark holds it -- only the kind test refuses; so the territory set
    `rosters.yaml: endings.peninsular_sovereignty` selects is never shrunk by a razing), and the
    Crown's OWN town its army marched from (`set_s_014`: mustered, but nothing foreign to raze). Each
    is `raze.refused` and the place stands."""
    w = build_realm(0)
    assert world_q.holder_faction_of(w, "set_s_014") == CROWN and world_q.mustered(w, "set_s_014", CROWN)
    assert _raze(w, "set_s_014", act_id="rz_own") == ["raze.refused"]
    assert "set_s_014" in w.rungs
    _occupy(w)
    assert w.rungs["terr_T7"].kind == "territory" and world_q.mustered(w, "terr_T7", CROWN)
    assert world_q.holder_faction_of(w, "terr_T7") == "fac_hafenmark"
    territories = sum(1 for r in w.rungs.values() if r.kind == "territory")
    assert _raze(w, "terr_T7", act_id="rz_terr") == ["raze.refused"]
    assert sum(1 for r in w.rungs.values() if r.kind == "territory") == territories


def test_in12_11_h228_what_stood_in_the_town_is_left_placeless_pinned_as_it_reads():
    """H-228, PINNED AS IT READS (#453's own recorded GAP): the cascade closes the `contain` of what stood
    in the town and re-homes nothing -- the town's cohort is placeless, its quarters are roots, the
    occupying army stands nowhere, and its Sites still name the gone id in their `rung` field. Each
    assertion reddens when H-228 closes. And THE SEASON RUNS ON: one season through `populated.run`
    after the razing completes without a raise (the world survives the dangling references)."""
    w = _occupy(build_realm(0))
    cohort, quarter = f"cohort_{TOWN}", "q_s_016_market_quarter"
    army = world_q.mustered(w, TOWN, CROWN)
    sites = sorted(s.id for s in w.sites.values() if s.rung == TOWN)
    assert sites and army
    assert _raze(w) == ["rung.razed"]
    homes = world_q.home_of(w)
    assert world_q.place_of(w, cohort) is None and homes.get(cohort) is None
    assert all(homes.get(p) is None for p in army), [(p, homes.get(p)) for p in army]
    assert not any(t.live and t.kind == "contain" and t.subject == quarter for t in w.tenures)
    assert quarter in w.rungs
    assert sorted(s.id for s in w.sites.values() if s.rung == TOWN) == sites
    POP.run(seasons=1, seed=0, w=w)
    assert TOWN not in w.rungs
