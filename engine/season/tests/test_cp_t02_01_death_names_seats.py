"""CP-T02-01 -- A DEATH NAMES THE SEATS IT EMPTIES (H-230 limit 1), WITH HR-1 IN THE SAME CHANGE.

THE CARRIER, NAMED BEFORE THE FIRST EDIT: the Receipt's changes. A dead holder's `hold` leaves the
owner-first store with him (`World.tenures` iterates `persons`), so WITNESS cannot expand that Tenure's
id into the seat (`epistemic._hold_tenure_ends`). Each seat `hold` the death closes is named to the gate
as `Subject.seat(t)`: read as an edge (moved iff G3 lists it), RECEIPTED UNDER THE OFFICE'S ID, earning
`tenure.closed` (`state/gate.py::death_subjects`). The claim WITNESS deposits per change is then about
the Office. No Claim field, no Event field, no world stamp; `chronicle` carries the kind to everyone
alive (`epistemic._ch_chronicle`, `tenure.closed` being a `binding_decision` emit).

The three death writes: `loop/effects_combat.py::_eff_kill` (`fight`/`accept` `Felled`), `_eff_march`'s
`total` arm, `loop/matter.py::_die`.

  (a) FALSIFIER: a planted death of a seat-holder, through the real fold and the real WITNESS, leaves in
      EVERY living person's ledger a claim about the seat, and `world_q.seats_named` returns it for a
      person who was not there. The same at MATTER, for a holder of two seats: one `tenure.closed`
      carrying both seats' receipts. MUTATION: `World.seat_holds` returning nothing (the emission off)
      turns (a) red -- run as a test below.
  (b) A death emptying no seat (its victim's live edges are other kinds) earns no `tenure.closed`.
  (c) HR-1: a `total`-arm `Won` still emits `field.won` and `army.arrived` beside the deaths; a
      `total`-arm `Lost` emits `field.lost` and a `person.died` whose receipts name each pid removed
      once (the fold mints ONE Event per kind per act, its id `H(seed, tick, actor, "<kind>:<act id>")`,
      so "one per pid" is one receipt per pid). MUTATION: every non-death subject earning nothing
      named (`own_kinds` -> `()`, the pre-HR-1 shape) silences `field.won` -- run as a test below.
"""
from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..harness.populated import build_realm
from ..loop import effects_combat
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _die
from ..queries import world_q
from ..seam.contest import Resolution
from ..state.carriers import Act, Person, Rung, Tenure
from ..state.world import World

HOLDER, OFFICE = "p_high", "off_duke"          # `tiny_world`: p_high holds off_duke and stands at S
CROWN, CHURCH = "fac_crown", "fac_church_of_solmund"


def _tiny():
    """`tiny_world` plus `p_near`, who stands at `S` with p_high (so a `fight` between them is admitted)."""
    w = P.tiny_world()
    w.persons["p_near"] = Person("p_near", "a neighbour")
    w.rungs["p_near"] = Rung("p_near", "person")
    w.add_tenure(Tenure("t_near_in", "p_near", "S", "contain", 0))
    w.add_tenure(Tenure("t_near_home", "p_near", "S", world_q.RESIDE_KIND, 0))
    return w


def _felled(w, actor, victim, aid="cp01_kill"):
    """`actor` fights `victim` and the scene fells him: a CONSTRUCTED `Felled` resolution through the
    real fold and the real gate at RESOLVE; the Events logged as the barrier logs them."""
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    res = Resolution("Felled", {"wound_state": {victim: {"felled": True, "health_full": 10,
                                                         "health_remaining": 0}}})
    out = d._fold(w, mint_token(w, WriteClass.ACTS),
                  Act(id=aid, actor=actor, verb="fight", payload={"subject": victim}), res)
    for e in out:
        w.log.append(e)
    return d, out


def _witness(w, d, events):
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), events)


def _about(w, pid, subject):
    return [c for c in w.persons[pid].ledger if c.subject == subject]


def _check_a_fight(w) -> tuple:
    """(a) on the fold path. Returns `(kinds, seat receipts, persons lacking a claim on the seat,
    seats_named for the far person)`, so the mutation test reads the same observation."""
    far = "p_king" if "p_king" in w.persons else next(p for p in w.persons
                                                       if world_q.home_of(w).get(p) != "S")
    assert world_q.home_of(w).get(far) != "S", "fixture: the far person stands where the death is"
    assert OFFICE not in world_q.seats_named(w, w.persons[far]), (
        "control: the far person was already told of the seat before the death")
    assert [t.object for t in w.seat_holds(HOLDER)] == [OFFICE], "fixture: p_high does not hold off_duke"
    d, out = _felled(w, "p_near", HOLDER)
    assert HOLDER not in w.persons, "fixture: the planted death did not happen"
    kinds = [e.kind for e in out]
    seat_receipts = [c.subject for e in out if e.kind == "tenure.closed" for c in e.changes
                     if c.subject in w.offices]
    _witness(w, d, out)
    living = list(w.persons)
    assert len(living) >= 3, "fixture: too few living persons for 'every' to mean anything"
    lacking = [p for p in living if not _about(w, p, OFFICE)]
    return kinds, seat_receipts, lacking, world_q.seats_named(w, w.persons[far])


def test_a_a_felled_seat_holder_names_his_seat_to_every_living_person():
    kinds, seats, lacking, named = _check_a_fight(_tiny())
    assert kinds == ["person.died", "tenure.closed"], kinds
    assert seats == [OFFICE], f"the tenure.closed Event's receipts name {seats}, not the seat"
    assert lacking == [], f"living persons holding no claim about {OFFICE}: {lacking}"
    assert OFFICE in named, f"seats_named for a person who was not there is {named}"


def test_a_mutation_with_the_seat_holds_unread_the_death_names_no_seat(monkeypatch):
    """THE MUTATION, run: the emission off (`World.seat_holds` -> `[]`, so `death_subjects` names no
    seat and `remove_person` still closes the holds). The falsifier's positive half must go red."""
    monkeypatch.setattr(World, "seat_holds", lambda self, who: [])
    w = _tiny()
    held = [t for t in w.tenures if t.kind == "hold" and t.subject == HOLDER and t.object == OFFICE]
    assert held, "fixture: p_high does not hold off_duke"
    d, out = _felled(w, "p_near", HOLDER)
    assert not held[0].live, "the cascade stopped closing the hold; this mutation is not the one meant"
    assert [e.kind for e in out] == ["person.died"]
    _witness(w, d, out)
    far = w.persons["p_king"]
    assert OFFICE not in world_q.seats_named(w, far), "the seat reached the far person with the emission off"
    assert any(not _about(w, p, OFFICE) for p in w.persons), "every ledger names the seat anyway"


def test_a_a_matter_death_of_a_two_seat_holder_emits_one_tenure_closed_naming_both():
    """MATTER's `_die`, the per-subject form: `person.died` exactly as before (one receipt, the dead
    man), then ONE `tenure.closed` whose receipts are the two Offices; WITNESS deposits claims on both
    in a ledger of someone far away."""
    w = build_realm(0)
    pid = "p_npc_020"
    seats = sorted(t.object for t in w.seat_holds(pid))
    assert seats == ["off_duke_valorsmark", "off_npc_020"], f"fixture moved: {seats}"
    far = "p_npc_008"
    assert world_q.home_of(w)[far] != world_q.home_of(w)[pid], "fixture: the far person stands with him"
    assert not set(seats) & set(world_q.seats_named(w, w.persons[far])), "control: already told"
    w.step = Step.MATTER
    w._emitted_by_write = []
    _die(w, mint_token(w, WriteClass.MATTER), pid)
    evs = list(w._emitted_by_write)
    assert [e.kind for e in evs] == ["person.died", "tenure.closed"], [e.kind for e in evs]
    assert [c.subject for c in evs[0].changes] == [pid]
    assert sorted(c.subject for c in evs[1].changes) == seats
    assert evs[1].causes == evs[0].causes, "the seat's closure is not caused as the death is"
    assert pid not in w.persons and not w.seat_holds(pid)
    _witness(w, SeasonDriver(w), evs)
    named = world_q.seats_named(w, w.persons[far])
    assert set(seats) <= set(named), f"seats_named for the far person is {named}"


def test_b_a_death_emptying_no_seat_earns_no_tenure_closed():
    """(b): p_near holds no seat; his live edges are `contain` and `reside`. Felled by p_high, his
    death emits `person.died` alone and no receipt names an Office."""
    w = _tiny()
    edges = [t.kind for t in w.tenures if t.subject == "p_near" and t.live]
    assert edges and "hold" not in edges, f"fixture: p_near's live edges are {edges}"
    assert w.seat_holds("p_near") == []
    _d, out = _felled(w, HOLDER, "p_near", aid="cp01_kill_b")
    assert "p_near" not in w.persons, "fixture: the planted death did not happen"
    assert [e.kind for e in out] == ["person.died"], [e.kind for e in out]
    assert not any(c.subject in w.offices for e in out for c in e.changes)


def test_b_a_realm_death_closing_only_commit_edges_earns_no_tenure_closed():
    """(b) on the realm: a person whose only live non-presence edges are `commit` edges (to a faction)
    dies by `fight`; no `tenure.closed`. The loop asserts it found him (`checked`)."""
    w = build_realm(0)
    home = world_q.home_of(w)
    checked = 0
    for pid, p in sorted(w.persons.items()):
        kinds = {t.kind for t in w.tenures if t.subject == pid and t.live}
        if "commit" not in kinds or "hold" in kinds or w.seat_holds(pid):
            continue
        killer = next((q for q, h in sorted(home.items()) if h == home.get(pid) and q != pid), None)
        if killer is None:
            continue
        _d, out = _felled(w, killer, pid, aid=f"cp01_b_{pid}")
        if pid in w.persons:
            continue
        assert [e.kind for e in out] == ["person.died"], (pid, [e.kind for e in out])
        assert not any(c.subject in w.offices for e in out for c in e.changes)
        checked += 1
        break
    assert checked == 1, "no committed, seatless, co-located person was found to kill"


def _defenders_total(w):
    w.fixtures = w.fixtures.sweep("field_casualty_model", "total")
    return world_q.mustered(w, "set_s_036", CHURCH)


def _march(w, res):
    d = SeasonDriver(w)
    w.step = Step.ENCOUNTER
    w.frozen = False
    return d._fold(w, mint_token(w, WriteClass.ACTS),
                   Act(id="m1", actor="p_npc_033", verb="march", payload={"subject": "set_s_036"},
                       via="off_npc_033"), res)


def _won_total(w):
    """A CONSTRUCTED total-arm `Won` (Won is unreachable at fixture scale, `test_march.py`): the Crown's
    army (re-housed off the target first, `test_march.py::_no_resident_crown`'s edit) kills every
    defender of `set_s_036` and arrives."""
    for t in w.persons["p_npc_037"].tenures:
        if t.kind == "contain" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_cp01_037_moved", "p_npc_037", "b_s_002_cottage", "contain", w.tick))
    defenders = _defenders_total(w)
    attackers = world_q.mustered(w, "set_s_014", CROWN)
    seats = sorted(t.object for pid in defenders for t in w.seat_holds(pid))
    res = Resolution("Won", {"parties": {"claimants": attackers, "subject_members": defenders},
                             "result": {"attacker_size_pct": 1.0, "defender_size_pct": 0.0}})
    return defenders, attackers, seats, _march(w, res)


def test_c_a_total_won_still_emits_field_won_and_army_arrived_beside_the_deaths():
    w = build_realm(0)
    defenders, attackers, seats, out = _won_total(w)
    assert defenders and attackers and seats, "fixture: no defender, attacker or defending seat"
    kinds = [e.kind for e in out]
    assert kinds == ["field.won", "army.arrived", "person.died", "tenure.closed"], kinds
    assert not any(pid in w.persons for pid in defenders), "the total arm left a defender standing"
    (died,) = [e for e in out if e.kind == "person.died"]
    assert sorted({c.subject for c in died.changes} & set(defenders)) == sorted(defenders)
    (closed,) = [e for e in out if e.kind == "tenure.closed"]
    assert sorted(c.subject for c in closed.changes if c.subject in w.offices) == seats


def test_c_mutation_with_no_subject_naming_the_bands_kinds_the_deaths_silence_field_won(monkeypatch):
    """THE MUTATION, run: the HR-1 form off -- `own_kinds` returning `()`, so the movers, the losers'
    own outcome and the treasuries name nothing (the pre-HR-1 `None`) while the dead name `person.died`.
    The non-empty `earned` set then drops the band's kind and the arrival: the falsifier goes red."""
    monkeypatch.setattr(effects_combat, "own_kinds", lambda declared: ())
    _d, _a, _s, out = _won_total(build_realm(0))
    kinds = [e.kind for e in out]
    assert "field.won" not in kinds and "army.arrived" not in kinds, kinds
    assert "person.died" in kinds


def test_c_a_total_lost_emits_field_lost_and_a_person_died_naming_each_pid_removed():
    w = build_realm(0)
    _defenders_total(w)
    attackers = world_q.mustered(w, "set_s_014", CROWN)
    assert len(attackers) >= 2, "fixture: one attacker cannot show 'each pid'"
    seats = sorted(t.object for pid in attackers for t in w.seat_holds(pid))
    res = Resolution("Lost", {"parties": {"claimants": attackers,
                                          "subject_members": world_q.mustered(w, "set_s_036", CHURCH)},
                              "result": {"attacker_size_pct": 0.0, "defender_size_pct": 1.0}})
    out = _march(w, res)
    kinds = [e.kind for e in out]
    assert kinds[:2] == ["field.lost", "person.died"], kinds
    removed = [pid for pid in attackers if pid not in w.persons]
    assert removed == attackers, f"the total arm left {set(attackers) - set(removed)} standing"
    (died,) = [e for e in out if e.kind == "person.died"]
    named = [c.subject for c in died.changes if c.subject in attackers]
    assert sorted(named) == sorted(removed) and len(set(named)) == len(named), named
    if seats:
        (closed,) = [e for e in out if e.kind == "tenure.closed"]
        assert sorted(c.subject for c in closed.changes if c.subject in w.offices) == seats
    else:
        assert "tenure.closed" not in kinds


def test_c_control_a_scaled_won_with_no_death_publishes_what_it_did_before():
    """CONTROL on the non-death path: the shipped `scaled_by_degree` arm floors at 1, kills nobody, and
    a `Won` with a moving army publishes `field.won` and `army.arrived` and nothing else -- the two kinds
    `None` earned before HR-1."""
    w = build_realm(0)
    for t in w.persons["p_npc_037"].tenures:
        if t.kind == "contain" and t.live:
            t.until = w.tick
    w.add_tenure(Tenure("t_cp01_037_moved", "p_npc_037", "b_s_002_cottage", "contain", w.tick))
    assert w.fixtures.get("field_casualty_model") == "scaled_by_degree", "the shipped arm moved"
    defenders = world_q.mustered(w, "set_s_036", CHURCH)
    res = Resolution("Won", {"parties": {"claimants": world_q.mustered(w, "set_s_014", CROWN),
                                         "subject_members": defenders},
                             "result": {"attacker_size_pct": 1.0, "defender_size_pct": 0.5}})
    assert [e.kind for e in _march(w, res)] == ["field.won", "army.arrived"]
    assert all(pid in w.persons for pid in defenders)
