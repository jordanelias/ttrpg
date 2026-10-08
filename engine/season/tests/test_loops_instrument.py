"""IN-24 (`BOUND-LOOPS`): `harness/loops.py` -- the derived cycle check (`H-106`) and the bound read.

Falsifiers, each with its control in the same test:
  (1) a planted amplifier with no LOOP row makes derived != declared, naming it;
  (2) a planted over-bound value for a LOOP row fails the bound check.
Plus that the derivation can observe a declared loop going missing (a check that can only ever say
"equal" observes nothing), and that a drifted read map is reported rather than raised.
"""

import pytest

from engine.season.harness import loops as L
from engine.season.harness import register as R


@pytest.fixture(scope="module")
def shipped():
    """`(processes, LOOP-row signs, derived cycles)` of the shipped tree. `Process` is frozen and
    `compare` only reads, so the tests that only read these share one build."""
    procs, _ = L.build_processes()
    signs = {r: row.get("sign") for r, row in L.loop_rows(R.load()).items()}
    return procs, signs, L.derive_cycles(procs)


def test_planted_amplifier_with_no_loop_row_makes_derived_differ_and_is_named(shipped):
    procs, signs, derived = shipped
    control = L.compare(derived, signs, L.DECLARED_CYCLES)
    plant = L.Process("PLANTED: stores breed stores", (("Rung.stores", "+"),),
                      (("Rung.stores", "+"),))
    res = L.compare(L.derive_cycles(procs + (plant,)), signs, L.DECLARED_CYCLES)
    assert not res["equal"]
    # RELATIVE control: the plant is what adds the cycle, and it moves nothing else
    assert ("Rung.stores",) not in control["by_sign"]["+"]["undeclared"]
    assert ("Rung.stores",) in res["by_sign"]["+"]["undeclared"]
    assert res["by_sign"]["+"]["underived"] == control["by_sign"]["+"]["underived"]


def test_removing_the_witness_fan_out_makes_its_declared_loops_underived(shipped):
    procs, signs, _ = shipped
    cut = tuple(p for p in procs if p.name != "WITNESS: fan-out over the log")
    assert len(cut) == len(procs) - 1
    res = L.compare(L.derive_cycles(cut), signs, L.DECLARED_CYCLES)
    assert not res["equal"]
    gone = {r for _, r in res["by_sign"]["+"]["underived"]}
    assert gone == {"H-102", "H-112"}


def test_a_loop_row_with_no_cycle_key_is_a_mismatch_not_a_silent_pass(shipped):
    _, signs, derived = shipped
    res = L.compare(derived, {**signs, "H-999": "+"}, L.DECLARED_CYCLES)
    assert not res["equal"] and res["unmapped"] == ["H-999"]


def test_sign_algebra_damping_and_unknown():
    damp = L.Process("decay", (("q", "+"),), (("q", "-"),))
    amp = L.Process("mint", (("q", "+"),), (("r", "+"),))
    back = L.Process("back", (("r", "+"),), (("q", "?"),))
    got = {(c["key"], c["sign"]) for c in L.derive_cycles((damp, amp, back))}
    assert got == {(("q",), "-"), (("q", "r"), "?")}


def test_over_bound_value_fails_the_bound_check():
    rows = {"H-104": ("Person.claim_ledger",)}
    bound = {("H-104", "Person.claim_ledger"): 200}
    over = L.check_bounds(rows, {"Person.claim_ledger": 201}, bound)
    assert over["failed"] and over["checked"] == 1
    assert over["lines"][0]["verdict"] == "FAIL"
    # controls: at the bound passes; no bound is UNCHECKED (never a pass); no reading is NOT OBSERVED
    at = L.check_bounds(rows, {"Person.claim_ledger": 200}, bound)
    assert not at["failed"] and at["lines"][0]["verdict"] == "PASS"
    free = L.check_bounds(rows, {"Person.claim_ledger": 201}, {})
    assert not free["failed"] and free["checked"] == 0
    assert free["lines"][0]["verdict"] == "UNCHECKED"
    none = L.check_bounds(rows, {}, bound)
    assert none["lines"][0]["verdict"] == "NOT OBSERVED" and none["checked"] == 0


def test_a_bound_on_a_quantity_off_the_row_refuses():
    with pytest.raises(ValueError, match="names no looped quantity"):
        L.check_bounds({"H-104": ("Person.claim_ledger",)}, {}, {("H-104", "Event"): 1})


def test_a_requires_stem_with_no_read_map_is_reported_as_drift(monkeypatch):
    _, control = L.build_processes()
    trimmed = {k: v for k, v in L.STEM_READS.items() if k != "stores"}
    monkeypatch.setattr(L, "STEM_READS", trimmed)
    _, blind = L.build_processes()
    assert len(blind["drift"]) > len(control["drift"])
    assert any("REQUIRES_STEMS" in m and "'stores'" in m for m in blind["drift"]), blind["drift"]


def test_a_bad_bound_is_refused_before_the_slow_observation(monkeypatch):
    def boom(*a, **k):
        raise AssertionError("observe ran before the bound was validated")
    monkeypatch.setattr(L, "observe", boom)
    with pytest.raises(SystemExit) as excinfo:
        L.main(["--base-seed", "1", "--n", "1", "--seasons", "1", "--bound", "H-104:Event=1"])
    assert excinfo.value.code == 2          # argparse's refusal, not the exit of a finished run
