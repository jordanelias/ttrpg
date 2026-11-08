"""CP-T04-02 (B10-12; AM-C-09 REPAIR): `marshal`, the standing order of battle. A seat granting `dispatch` mints an
`order_of_battle` Record `[at, role, retreat_at]` through `_mint_document`; `field_input` reads, per side, the one whose
holder edge is newest (`world_q.standing_order`); `resolve_field` maps its `role` onto each subunit of a headcount line.
This file is the item's own; nothing here is a shared pin.

THE USER'S RULING, AND ITS COST. The entry's Stop-if ("friction drowns a role's effect") was met on the roles a headcount
line's stand-in troop type (`infantry`) may take (`hole_register.yaml` H-361); the user ruled it built as written, with the
order's `role` ranging over the module's whole `ROLE_SPEC` and NOT gated by `registry.role_allowed`
[ASSUMPTION; medium; Jordan to correct; revert: gate it]. `test_the_role_is_not_gated_by_role_allowed` pins the bypass.

THE FIELD IS HAND-SIZED, NOT NATURAL. One shipped season fights no `field.won` or `field.lost` (the aperture reading), and
at the shipped `field_troops_per_weight` of 1 every subunit routs at tick 1, so no role could matter. The falsifier runs on
a real fold of `set_s_014` (the Crown's two marchers, weight 10 each) and `set_s_036` (the Church's six, weights 4,4,3,3,3,3)
at `SCALE` 30, the garrison worn to condition 0 (an open field) or kept (WALLS); the record is `field_input`'s own, as
`test_cp_t04_05_graded_walls.py` builds it, with the place (`territory='T3'`, an OPEN_FLAT polygon) and no origin (no river).
The ORDERS in it are not hand-set: each is a real `marshal` act folded through the driver by a seat that grants `dispatch`
and whose purview reaches the place (the King at `set_s_014`, the Cardinal of Justice at `set_s_036`).

FALSIFIER (the entry's, three parts): paired seeds (`random.Random(0..199)` in both arms), the same two sides, (1) a `Shock`
role against a `ShieldWall` role on the attacker: the band distributions differ by more than the +-7 points; (2) a defender's
order changes a defended (WALLS) field; (3) two orders in two seasons, the newer governs (and the older is not deleted).
PLANTED FAILURES: an order ignored by `field_input`, and a module that ignores the role, each leave the arms equal, so
the same predicate reddens. CONTROLS: no order held is the field as it was (`orders is None`); an order held by another
faction's seat, about another place, or already closed is not read; the exported role set is `ROLE_SPEC`'s names and
the exporter's `--check` passes, and a planted drift is seen."""
from __future__ import annotations

import importlib
import random
import subprocess
import sys
from collections import Counter
from dataclasses import replace
from functools import lru_cache
from pathlib import Path

import pytest

from engine.season.data.verbs import CHOICE_SOURCED, VERB_TABLE, act_key
from engine.season.decision.options import operand_bags
from engine.season.gaps import Forbidden
from engine.season.harness.populated import build_realm
from engine.season.queries import world_q
from engine.season.queries.inputs import FieldOrder
from engine.season.seam.wrappers import mass_battle as wrapper
from engine.season.state.carriers import Act, Question
from engine.season.tests.test_march import _fold_one
from engine.substrate import battle_orders

HOME, TARGET = "set_s_014", "set_s_036"
ATT_FACTION, DEF_FACTION = "fac_valorsmark", "fac_church_of_solmund"
KING, KING_SEAT = "p_npc_020", "off_king"                          # Valorsmark; dispatch; reaches HOME and TARGET
CARDINAL, CARDINAL_SEAT = "p_npc_038", "off_cardinal_justice"      # Church; dispatch; reaches TARGET only
MARCHERS = ("p_npc_033", "p_npc_035")
ATT_WEIGHT, DEF_WEIGHTS, SCALE, SEEDS = 10, (4, 4, 3, 3, 3, 3), 30, range(200)
NOISE = 0.07            # the entry's band: +-7 points
DEGREES = ("Overwhelming", "Success", "Partial", "Failure")


def _mod(name):
    """`engine/` names no `modules/` import, not even a function-local one (`test_engine_does_not_import_systems.py`);
    a module is loaded by string on first use."""
    return importlib.import_module(f"modules.mass_battle.{name}")


def _mb():
    return _mod("massbattle")


def _marshal(actor, via, place, role, retreat="none", aid="mz"):
    return Act(id=aid, actor=actor, verb="marshal", payload={"subject": place, "role": role, "retreat_at": retreat},
               via=via)


def _world(orders=(), worn=True):
    """The shipped realm resized so the sides are even, plus each `(actor, via, place, role, act id, tick)` order folded
    through the real driver. `worn` wears the target's garrison to 0 (an open field); else it stays (WALLS)."""
    w = build_realm(0)
    for pid in MARCHERS:
        w.persons[pid].weight = ATT_WEIGHT
    for pid, wt in zip(world_q.mustered(w, TARGET, DEF_FACTION), DEF_WEIGHTS):
        w.persons[pid].weight = wt
    w.fixtures = w.fixtures.sweep("field_troops_per_weight", SCALE)
    if worn:
        for s in w.sites.values():
            if s.kind == "garrison" and s.rung == TARGET:
                s.condition = 0
    for actor, via, place, role, aid, tick in orders:
        w.tick = tick
        kinds = [e.kind for e in _fold_one(w, _marshal(actor, via, place, role, aid=aid))]
        assert "order.marshaled" in kinds, kinds
    return w


def _record(w):
    att = world_q.mustered(w, HOME, ATT_FACTION)
    dfn = world_q.mustered(w, TARGET, DEF_FACTION)
    return replace(wrapper.field_input(w, att, dfn, TARGET, factions=(ATT_FACTION, DEF_FACTION), origin_place=HOME),
                   origin=None, territory="T3")


def _bands(inp):
    """(attacker win share, {degree: share}) over the paired seeds."""
    c, wins = Counter(), 0
    for s in SEEDS:
        g = _mb().resolve_field(inp, random.Random(s))
        c[g["degree"]] += 1
        wins += g["attacker_wins"]
    return wins / len(SEEDS), {k: c[k] / len(SEEDS) for k in DEGREES}


def _differs(a, b):
    """THE FALSIFIER'S PREDICATE (one function, so a planted failure is judged by the very check the real arm is): the
    band distributions differ by more than the noise band in at least one band."""
    return max(abs(a[1][k] - b[1][k]) for k in DEGREES) > NOISE


@lru_cache(maxsize=None)
def _arm(att_role=None, def_role=None, worn=True):
    orders = []
    if att_role:
        orders.append((KING, KING_SEAT, HOME, att_role, "mz_att", 3))
    if def_role:
        orders.append((CARDINAL, CARDINAL_SEAT, TARGET, def_role, "mz_def", 3))
    inp = _record(_world(orders, worn))
    return inp.orders, _bands(inp), inp.fort_level


# --------------------------------------------------------------------------------------------------------------- falsifier

def test_falsifier_a_shock_order_against_a_shieldwall_order_on_the_attacker_differs_beyond_noise():
    (oa, shock, _), (ob, wall, _) = _arm("Shock"), _arm("ShieldWall")
    assert oa == (FieldOrder("Shock", "none"), None) and ob == (FieldOrder("ShieldWall", "none"), None)
    assert _differs(shock, wall), (shock, wall)
    assert abs(shock[0] - wall[0]) > NOISE, (shock[0], wall[0])             # the win share moves too, not only a band


def test_falsifier_a_defenders_order_changes_a_defended_field():
    (_, none, fort), (od, shock, fort2) = _arm(worn=False), _arm(None, "Shock", worn=False)
    assert fort == fort2 == 1.0                                              # WALLS: a defended field, not an open one
    assert od == (None, FieldOrder("Shock", "none"))
    assert _differs(none, shock), (none, shock)
    assert abs(none[0] - shock[0]) > NOISE, (none[0], shock[0])


def test_falsifier_two_orders_in_two_seasons_the_newer_governs_and_the_older_is_kept():
    for older, newer in (("Shock", "ShieldWall"), ("ShieldWall", "Shock")):
        w = _world([(KING, KING_SEAT, HOME, older, "mz_old", 3), (KING, KING_SEAT, HOME, newer, "mz_new", 4)])
        assert _record(w).orders == (FieldOrder(newer, "none"), None), (older, newer)
        assert world_q.standing_order(w, ATT_FACTION, HOME).id == "rec:mz_new"
        assert "rec:mz_old" in w.records                                      # older orders are ignored, not deleted
        assert _bands(_record(w)) == _arm(newer)[1]                          # ... and it is the newer's field, seed for seed
    assert _differs(_arm("Shock")[1], _arm("ShieldWall")[1])                  # (so the two cases are not one field)


def test_a_tie_on_the_holder_edge_goes_to_the_later_in_w_tenures():
    w = _world([(KING, KING_SEAT, HOME, "Shock", "mz_a", 5), (KING, KING_SEAT, HOME, "ShieldWall", "mz_b", 5)])
    held = [t for t in w.tenures if t.kind == "hold" and t.live and t.object in ("rec:mz_a", "rec:mz_b")]
    assert len(held) == 2 and held[0].since == held[1].since == 5
    assert world_q.standing_order(w, ATT_FACTION, HOME).id == held[-1].object


# ----------------------------------------------------------------------------------------------------- planted failures

def test_planted_failure_an_order_ignored_by_field_input_reddens_the_falsifier(monkeypatch):
    monkeypatch.setattr(wrapper, "_standing_order", lambda *a: None)
    mutant = []
    for role in ("Shock", "ShieldWall"):
        inp = _record(_world([(KING, KING_SEAT, HOME, role, "mz_att", 3)]))
        assert inp.orders is None
        mutant.append(_bands(inp))
    assert not _differs(*mutant)
    with pytest.raises(AssertionError):
        assert _differs(*mutant)


def test_planted_failure_a_module_that_ignores_the_role_reddens_the_falsifier(monkeypatch):
    monkeypatch.setattr(_mb(), "_role_fields", lambda role: {})
    mutant = [_bands(_record(_world([(KING, KING_SEAT, HOME, role, "mz_att", 3)]))) for role in ("Shock", "ShieldWall")]
    assert not _differs(*mutant)


# ---------------------------------------------------------------------------------------------------------------- controls

def test_control_no_order_held_is_the_field_as_it_was():
    inp = _record(_world())
    assert inp.orders is None
    for s in list(SEEDS)[:20]:
        assert (_mb().resolve_field(inp, random.Random(s))
                == _mb().resolve_field(replace(inp, orders=(None, None)), random.Random(s)))


def test_control_an_order_of_another_faction_or_place_or_a_closed_one_is_not_read():
    # held by a Church seat, about the Crown's place: the attacker's faction is the Crown's
    w = _world([(CARDINAL, CARDINAL_SEAT, TARGET, "Shock", "mz_c", 3)])
    assert world_q.standing_order(w, ATT_FACTION, TARGET) is None            # a Church order is not the Crown's
    assert world_q.standing_order(w, DEF_FACTION, HOME) is None              # ... nor about another place
    assert _record(w).orders == (None, FieldOrder("Shock", "none"))
    # a closed hold: the order is no longer held, so it is no order
    for t in w.tenures:
        if t.kind == "hold" and t.object == "rec:mz_c":
            t.until = w.tick
    assert world_q.standing_order(w, DEF_FACTION, TARGET) is None
    assert _record(w).orders is None
    # a holder who holds no seat of the faction: a Record minted by a seatless person is not the faction's order
    w2 = _world([(KING, KING_SEAT, HOME, "Shock", "mz_k", 3)])
    for t in list(w2.persons[KING].tenures):
        if t.kind == "hold" and t.live and t.object in w2.offices:
            t.until = w2.tick
    assert world_q.standing_order(w2, ATT_FACTION, HOME) is None


# ----------------------------------------------------------------------------------------------------- the act and the fan

def test_marshal_mints_an_order_record_with_three_keys_and_a_hold_and_refuses_an_unreaching_seat():
    w = _world([(KING, KING_SEAT, HOME, "Skirmish", "mz1", 7)])
    rec = w.records["rec:mz1"]
    assert rec.kind == "order_of_battle"
    assert rec.subject_matter == {"at": HOME, "role": "Skirmish", "retreat_at": "none"}          # no `reserve`, no `general`
    hold = [t for t in w.tenures if t.kind == "hold" and t.object == "rec:mz1" and t.live]
    assert [(t.subject, t.since) for t in hold] == [(KING, 7)]
    # the Spymaster grants `dispatch` but his purview (terr_T1) does not reach HOME: refused at `authority`
    w2 = _world()
    kinds = [e.kind for e in _fold_one(w2, _marshal("p_npc_033", "off_spymaster", HOME, "Shock", aid="mz2"))]
    assert kinds == ["marshal.unauthorized"] and not [r for r in w2.records.values() if r.kind == "order_of_battle"]


def test_a_role_outside_the_closed_set_is_refused_before_anything_is_written():
    w = _world()
    for i, payload in enumerate(({"subject": HOME, "role": "Berserker", "retreat_at": "none"},
                                 {"subject": HOME, "role": "Shock", "retreat_at": "0.1"}, {"subject": HOME})):
        with pytest.raises(Forbidden):
            _fold_one(w, Act(id=f"bad{i}", actor=KING, verb="marshal", payload=payload, via=KING_SEAT))
    assert not [r for r in w.records.values() if r.kind == "order_of_battle"]


def test_operand_bags_ranges_role_and_retreat_at_over_their_closed_sets():
    w = build_realm(0)
    p, q = w.persons[KING], Question("q:mz", "need", (HOME,))
    bags = operand_bags(p, VERB_TABLE["marshal"], q, HOME, w.fixtures)
    assert CHOICE_SOURCED["marshal"] == ("role", "retreat_at")
    assert len(bags) == len(battle_orders.ROLES) * len(battle_orders.RETREAT_AT) == 45
    assert {(b["role"], b["retreat_at"]) for b in bags} == {(r, a) for r in battle_orders.ROLES
                                                           for a in battle_orders.RETREAT_AT}
    assert all(b["subject"] == HOME for b in bags)
    assert len({act_key("marshal", HOME, b) for b in bags}) == 45            # one act id each, or the store refuses the second
    # a row that carries no choice is untouched: one bag
    assert len(operand_bags(p, VERB_TABLE["march"], q, TARGET, w.fixtures)) == 1


# ---------------------------------------------------------------------------------- the module's vocabulary and the bypass

def test_the_role_set_is_the_modules_the_export_is_current_and_drift_is_seen(monkeypatch, tmp_path):
    import json
    ROLE_SPEC = _mod("config").ROLE_SPEC
    from engine.season.data import rosters
    assert battle_orders.ROLES == tuple(ROLE_SPEC) == _mb().ORDER_ROLES == tuple(rosters.ORDER_ROLES)
    assert battle_orders.RETREAT_AT == _mb().ORDER_RETREAT_AT == tuple(rosters.ORDER_RETREAT_AT)
    root = Path(__file__).resolve().parents[3]
    r = subprocess.run([sys.executable, "tools/export_battle_orders.py", "--check"], cwd=root, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    sys.path.insert(0, str(root / "tools"))
    try:
        import export_battle_orders as E
        # PLANTED DRIFT 1: a committed artifact missing a role the module names is stale, and `--check` fails
        stale = json.loads(E.OUT and Path(E.OUT).read_text(encoding="utf-8"))
        stale["roles"] = stale["roles"][:-1]
        monkeypatch.setattr(E, "OUT", str(tmp_path / "battle_orders.json"))
        Path(E.OUT).write_text(json.dumps(stale, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        assert E.main(["--check"]) == 1
        # PLANTED DRIFT 2: the module's order roles diverge from `ROLE_SPEC`'s names: refused at build
        monkeypatch.setattr(_mb(), "ORDER_ROLES", _mb().ORDER_ROLES + ("Wedge",))
        with pytest.raises(SystemExit):
            E.build()
    finally:
        sys.path.remove(str(root / "tools"))


def test_the_role_is_not_gated_by_role_allowed():
    """THE BYPASS (H-361): `Shock` is not in `infantry`'s menu, the line's stand-in troop type, and the order still sets the
    subunit's role, shape and instructions; no order is the subunit exactly as it was."""
    ROLE_SPEC, role_allowed = _mod("config").ROLE_SPEC, _mod("troop_types.registry").role_allowed
    mb = _mb()
    assert not role_allowed("infantry", "Shock") and "Shock" in ROLE_SPEC
    ordered = mb._weighted_unit("a", 20, 5, SCALE, "Shock").subunits[0]
    plain = mb._weighted_unit("a", 20, 5, SCALE).subunits[0]
    assert (ordered.role, ordered.shape, ordered.instructions) == ("Shock", "Arrowhead", ("charge",))
    assert (plain.role, plain.shape, plain.instructions) == (None, "Line", ())
    persons, _ = mb._person_unit("a", (5, 5), ("x", "y"), 5, SCALE, None, "ShieldWall")
    assert [(s.role, s.shape) for s in persons.subunits] == [("ShieldWall", "Line")] * 2   # on the `person` arm too
    with pytest.raises(ValueError):
        mb._weighted_unit("a", 20, 5, SCALE, "Berserker")
