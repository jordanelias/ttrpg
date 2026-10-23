"""v9 IN-59 (b) (RS-26) -- THE AUDIENCE HALF OF THE ACCESS GATE: entering a guarded rung needs standing.

`move` and `migrate` carry a second conjunct, `relation` of `to`, `audience` -- one new WORLD-ONLY stem
(`data/requires.py: REQUIRES_STEMS`, `WORLD_ONLY_STEMS`), answered by `WorldReader.read` through
`world_q.admits_audience`. Admitted if ANY limb holds: a seat the mover holds reaches the rung; he holds
a live writ (addressed to him) whose issuing seat reaches it; he owes a live sworn `oblige` to a seat
that reaches it; or nobody guards it (`guard_weight == 0`, IN-60).

THE FALSIFIERS, each on a hand-built world (`probes.tiny_world`: `R` > `D` > `S` > `Hh`; `p_high` holds
`off_duke`, rung `D`, and stands at `S`; `p_low`, `p_mid`, `p_other` stand at `Hh`) through the real
fold (`SeasonDriver.resolve`). The guarded court is `S` with a sworn cohort planted beside the Duke
(`guard_weight(S) == 3`), the edge `build_realm(guards=True)` writes:
  1. `move` into the guarded court: REFUSED (`travel.blocked`) for a stranger and for three near-misses
     (an imposed oblige, a hand-planted writ with no issuing Event, and each limb's REACH condition: a
     seat, an oath and a real writ whose seat's purview does not reach `S`); ADMITTED (`travel.moved`) for a seat-holder whose seat reaches `S`, a writ-holder (a real
     `issue` through `off_duke`, handed to him), and a sworn man (a live `oblige` to `off_duke`).
  2. An ordinary `move` into an UNGUARDED rung by a seatless person still executes -- the failure if the
     stem were a `basis` conjunct (every seatless `move` refused); and the SAME stranger into the same
     court executes once the cohort's oath ends (the refusal is the guard's, nothing else).
  3. `migrate` into the guarded court: refused for the stranger, admitted for a sworn man.
MUTATIONS, run at the build 2026-10-23, each RED then restored GREEN (results in the commit message):
  * `admits_audience` returning `True` -> falsifier 1's and 3's refusals RED.
  * the guard limb dropped (every rung read as guarded) -> falsifier 2 RED.
  * each admitting limb dropped in turn (seat / oath / writ) -> its admitted case in falsifier 1 RED
    (the oath also falsifier 3's sworn migrant).
  * the oath limb's `not t.imposed` dropped -> `imposed_oblige` RED; the writ limb's issuing-seat test
    dropped (any held writ admits) -> `planted_writ` RED; the oath limb admitting an oblige to ANY
    office -> `oath_out_of_reach` RED; the writ limb dropping its `purview_reaches(...)` test on the issuing seat
    -> `writ_out_of_reach` RED; the oath limb dropping its `purview_reaches(...)` test -> `oath_out_of_reach`
    RED (B-Y close, Phase 1; re-run after Phase 2 rewrote the limbs).
"""

from __future__ import annotations

from ..data.matrix import WriteClass
from ..data.requires import REQUIRES_STEMS, WORLD_ONLY_STEMS
from ..data.verbs import VERB_TABLE
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import DETERMINED_BY, Act, Claim, Office, Tenure
from .test_in10_record_operands import _hold_document

COURT, SEAT, DUKE = "S", "off_duke", "p_high"
MOVER = "p_mid"                                  # seatless, sworn to nobody, at `Hh`
OPEN = "Hh"                                      # an unguarded rung the mover can reach from `S`


def _world(guarded=True):
    """`tiny_world`, a guard cohort (weight 3) at the Duke's own place sworn to his seat, one MATTER
    barrier run."""
    w = P.tiny_world()
    if guarded:
        P.plant_cohort(w, "c_guard", COURT, weight=3)
        w.add_tenure(Tenure("t_guard_oath", "c_guard", SEAT, "oblige", 0))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _go(w, d, verb, key, who=MOVER, to=COURT):
    return _kinds(_fold(w, d, Act(id=key, actor=who, verb=verb, payload={"to": to})))


def _writ_to_mover(w, d, key="w1", issuer=DUKE, seat=SEAT):
    """A REAL writ: `issuer` `issue`s through `seat` (default the Duke through `off_duke`, so the Record
    has a creating Event and an issuing seat, K-52) addressed to the mover, and it is handed to him --
    planted, as `give`'s own tests own the handing (`test_in12_arrest.py::_warrant_to_watchman`'s
    shape)."""
    w.persons[issuer].ledger.append(Claim("c_knows_mover", issuer, MOVER, "exists:Person", 1, 0,
                                          "firsthand", 100, "own"))
    assert _kinds(_fold(w, d, Act(id=key, actor=issuer, verb="issue", via=seat,
                                  payload={"subject": MOVER, "to": MOVER}))) == ["dispensation.issued"]
    rid = f"rec:{key}"
    for t in w.tenures:
        if t.kind == "hold" and t.object == rid and t.live:
            t.until = w.tick
    w.add_tenure(Tenure(f"t_{key}_mover", MOVER, rid, "hold", since=w.tick))
    assert world_q.writs_held(w, w.persons[MOVER]) == (rid,)
    return rid


# ======================================================================================
# THE GRAMMAR: one stem, world-only, on both rows; no form added
# ======================================================================================

def test_in59b_audience_is_one_world_only_stem_on_move_and_migrate():
    assert "audience" in REQUIRES_STEMS and "audience" in WORLD_ONLY_STEMS
    for verb in ("move", "migrate"):
        assert "audience" in VERB_TABLE[verb].requires_typed.stems(), verb
    assert VERB_TABLE["migrate"].refusal_for("audience") == ("travel.blocked",)


# ======================================================================================
# FALSIFIER 1 -- the guarded court: a stranger refused, each limb admitted
# ======================================================================================

def test_in59b_falsifier_1_a_guarded_court_refuses_a_stranger_and_admits_seat_writ_and_oath():
    def stranger(w, d):
        return MOVER, "travel.blocked"

    def imposed_oblige(w, d):                    # a sentence to serve the seat is no oath
        w.add_tenure(Tenure("t_sentence", MOVER, SEAT, "oblige", 0, payload={DETERMINED_BY: SEAT}))
        return MOVER, "travel.blocked"

    def planted_writ(w, d):                      # a writ no Event made has no issuing seat
        _hold_document(w, w.persons[MOVER], "dispensation",
                       {"terms": MOVER, "to": [MOVER], "at": None}, rec_id="rec_planted")
        assert world_q.writs_held(w, w.persons[MOVER]) == ("rec_planted",)
        return MOVER, "travel.blocked"

    def _warden_seat(w, rung="Hx"):              # a seat on a hearth reaches nothing at `S`
        if rung not in w.rungs:
            w.rungs[rung] = type(w.rungs["Hh"])(rung, "hearth")
            w.add_tenure(Tenure("t_hx", rung, "S", "contain", 0))
        w.offices["off_warden"] = Office("off_warden", "Warden", rung, ["issue"], faction="Crown")

    def seat_out_of_reach(w, d):
        _warden_seat(w)
        w.add_tenure(Tenure("t_warden", MOVER, "off_warden", "hold", 0))
        return MOVER, "travel.blocked"

    def oath_out_of_reach(w, d):                 # sworn, but to a seat that reaches nothing at `S`
        _warden_seat(w)
        w.add_tenure(Tenure("t_mover_oath_hx", MOVER, "off_warden", "oblige", 0))
        return MOVER, "travel.blocked"

    def writ_out_of_reach(w, d):                 # a REAL writ, issued through a seat that reaches nothing at
        _warden_seat(w, rung="Hh")               # `S`; at `Hh` it reaches the mover, so `issue` is authorized
        w.add_tenure(Tenure("t_warden", "p_other", "off_warden", "hold", 0))
        _writ_to_mover(w, d, key="w2", issuer="p_other", seat="off_warden")
        return MOVER, "travel.blocked"

    def seat_holder(w, d):                       # his own seat's purview reaches the court
        w.offices["off_reeve"] = Office("off_reeve", "Reeve", COURT, ["issue"], faction="Crown")
        w.add_tenure(Tenure("t_reeve", MOVER, "off_reeve", "hold", 0))
        return MOVER, "travel.moved"

    def writ_holder(w, d):
        _writ_to_mover(w, d)
        return MOVER, "travel.moved"

    def sworn_man(w, d):
        w.add_tenure(Tenure("t_mover_oath", MOVER, SEAT, "oblige", 0))
        return MOVER, "travel.moved"

    checked = 0
    for case in (stranger, imposed_oblige, planted_writ, seat_out_of_reach, oath_out_of_reach,
                 writ_out_of_reach, seat_holder, writ_holder, sworn_man):
        w, d = _world()
        assert world_q.guard_weight(w, COURT) == 3, "the court is guarded"
        who, want = case(w, d)
        assert _go(w, d, "move", case.__name__, who=who) == [want], case.__name__
        where = world_q.home_of(w)[who]
        assert (where == COURT) == (want == "travel.moved"), (case.__name__, where)
        checked += 1
    assert checked == 9


# ======================================================================================
# FALSIFIER 2 -- the gate does not kill the verb
# ======================================================================================

def test_in59b_falsifier_2_a_seatless_move_into_an_unguarded_rung_still_executes():
    """Three arms, each a seatless, unsworn, writless mover: an unguarded world; a move into an
    unguarded rung of the guarded world (a cohort planted at `S` walks out to `Hh`); and the stranger
    into the court once the cohort's oath ends (the refusal was the guard's and nothing else's)."""
    w, d = _world(guarded=False)
    assert world_q.guard_weight(w, COURT) == 0
    assert _go(w, d, "move", "open_world") == ["travel.moved"]

    w, d = _world()
    P.plant_cohort(w, "c_visitor", COURT, weight=2)
    assert world_q.guard_weight(w, OPEN) == 0
    assert _go(w, d, "move", "out", who="c_visitor", to=OPEN) == ["travel.moved"]

    w, d = _world()
    assert _go(w, d, "move", "before") == ["travel.blocked"]
    oath = next(t for t in w.tenures if t.id == "t_guard_oath")
    oath.until = w.tick                          # the ONE write: the guard's oath ends
    assert world_q.guard_weight(w, COURT) == 0
    assert _go(w, d, "move", "after") == ["travel.moved"]


# ======================================================================================
# FALSIFIER 3 -- `migrate` cannot walk past the guard
# ======================================================================================

def test_in59b_falsifier_3_migrate_into_the_guarded_court_is_refused_for_a_stranger_and_admits_a_sworn_man():
    w, d = _world()
    assert _go(w, d, "migrate", "mg_stranger") == ["travel.blocked"]
    assert world_q.residence_of(w)[MOVER] == OPEN, "a refused migrant changed residence"
    w.add_tenure(Tenure("t_mover_oath", MOVER, SEAT, "oblige", 0))
    assert _go(w, d, "migrate", "mg_sworn") == ["residence.changed"]
    assert world_q.residence_of(w)[MOVER] == COURT
