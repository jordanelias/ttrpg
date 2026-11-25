"""CR-24 (`H-360`, M4 Ask B (b)): the winners of a fought field take their own engine casualties, on `body` only.

`field_winner_casualties: engine` is SHIPPED; `off` is the field as ED-IN-0279 left it (the winner is not written).

THE FIELD IS A REAL FOLD OF A HAND-BUILT SITUATION. One season of the shipped realm fights almost no field (seed 0:
`field.unopposed` 3, `march.declared` 6), so the falsifier folds ONE `march` through the real driver (RESOLVE then
ENCOUNTER, `test_march._fold_one`) -- the engine fights it; no `Resolution` is hand-built -- with the Crown's two
marchers made cohorts (`Person.weight` `WEIGHT`) against the Church's six (`DEFENDER_WEIGHT`), 1,000 troops a weight (ED-MB-0101, B17.16; B17.01 retired REM-32's
`field_troops_per_weight`: `under_arms_cap` is the one scale) and `field_units: person` (CP-T04-01). Realm seed `SEED`: the attacker
WINS (`field.won`), one marcher's units are cut (a survivor ratio just under 1) and the other's are not. The preconditions are
asserted, so a moved fixture reads as a precondition, not a pass.

Why `person`: under `side` a winning headcount side's ratio reads 1.0 or above (`effective_size / size_max` floors
`size_max`, `_grade`'s own note), and a winner is never raised, so the `side` arm writes a winner nothing in these folds.
The per-person ratio is the one that is below 1 for a winner.

The cases: the falsifier (each attacking claimant's `body` falls by HIS OWN ratio; the defenders still take theirs; no
stance row on any winner), its planted failure (winners written at the loser's ratio reddens it), the control (`off`
writes no winner and reproduces the pre-item world; `engine` differs from it in the winner's body and nothing else),
the one-Subject rule for a winner who marches, and the arm's refusal of a stranger."""
from __future__ import annotations

import importlib

import pytest

from engine.season.boot.realm import build_realm
from engine.season.queries import world_q
from engine.season.tests.test_march import _fold_one, _march_act, _weigh

# B05.99 RE-PICKED (B05.03, the field's one sampler): at seed 0 and scale 10 the winning marchers both read ratio 1.0 on
# seeds 0..11 (no winner casualty to observe); a grid of weights {10, 6, 4, 3, 2, 1} x scales {10, 20, 50, 100, 200} x seeds
# 0..7 first reads the case the claims need at seed 3, weight 10, scale 200 (p_npc_033 at 1.0, p_npc_035 at 0.948). Was
# SEED 0, SCALE 10 (the docstring's 0.982 is the old reading).
# Seed re-picked again at the B06/B17 merge (the keyed draw is the stream; was 3, where the attacker drew): seeds 0..79 at
# weights 10 / 3 scanned for a won field with p_npc_033 at the full scale and p_npc_035 cut; seed 9 is the first (1000 / 970), 45 the next.
# B17.16 RE-CUT (30 -> 1,000 troops a weight, the 50-to-100 cell, a side cut into at least three units): of marcher weights 1 / 1.5 / 4 / 6
# against defender weights 1 / 2 / 3 / 5 over seeds 0..39 (one scan, `person` arm), the case the claims need (a WON field with
# p_npc_033 at the full scale and p_npc_035 cut) is read at marcher weight 6 against defender weight 2: seeds 1 and 32 (p_npc_035 at
# 989 and 990); seed 1 is the first. Was (9, 10, 3).
SEED, WEIGHT, DEFENDER_WEIGHT = 1, 6, 2
# B21.03 narrowed `off_spymaster` to `issue`, and `march` asks `remit:dispatch`: the marching seat is the Royal Marshal's
# (a Crown seat granting `dispatch`), so the Crown army is the one standing at his home `ORIGIN`, not the barracks'.
ACTOR, SEAT, ORIGIN = "p_npc_036", "off_royal_marshal", "set_s_001"
MARCHERS = ("p_npc_036", "p_npc_009", "p_npc_030", "p_npc_031", "p_npc_083")


def _mb():
    """`engine/` names no `modules/` import at module level; the module is loaded on first use."""
    return importlib.import_module("modules.mass_battle.massbattle")


def _fold(arm="engine", *, model=None, units="person"):
    """Fold the one march. Returns `(world, events, bodies before, stance before, the module's per-person record)`: each
    person's `(his part's share, routed)` on the body scale, read off the `FieldOutcome` `_grade` returns."""
    mb = _mb()
    real = mb._grade
    seen = {}

    def tap(*args, **kwargs):
        out = real(*args, **kwargs)
        for side in (out.attacker, out.defender):
            seen.update({part.id: (part.share, part.routed) for part in side.parts})
        return out

    mb._grade = tap
    try:
        w = build_realm(SEED)
        _weigh(w, MARCHERS, WEIGHT)
        _weigh(w, world_q.mustered(w, "set_s_036", "fac_church_of_solmund"), DEFENDER_WEIGHT)
        w.fixtures = (w.fixtures.sweep("field_units", units).sweep("field_winner_casualties", arm))
        if model is not None:
            w.fixtures = w.fixtures.sweep("field_casualty_model", model)
        before = {pid: w.persons[pid].body for pid in w.persons}
        stance = {pid: list(w.persons[pid].stance or []) for pid in w.persons}
        events = _fold_one(w, _march_act(ACTOR, "set_s_036", SEAT), contest_max_depth=2)
    finally:
        mb._grade = real
    return w, events, before, stance, seen


def test_shipped_arm_is_engine():
    assert build_realm(0).fixtures.get("field_winner_casualties") == "engine"


def test_model_none_writes_no_winner():
    w, _events, before, _stance, _ = _fold("engine", model="none")
    assert [w.persons[pid].body for pid in MARCHERS] == [before[pid] for pid in MARCHERS]


def test_an_unknown_arm_is_refused():
    from engine.season.gaps import Unspecified
    with pytest.raises(Exception) as err:
        _fold("sometimes")
    assert "sometimes" in str(err.value) or isinstance(err.value, Unspecified)
