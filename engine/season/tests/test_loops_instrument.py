"""IN-24 (`BOUND-LOOPS`): `harness/loops.py` -- the derived cycle check (`H-106`) and the bound read.

Falsifiers, each with its control in the same test:
  (1) a planted amplifier with no LOOP row makes derived != declared, naming it;
  (2) a planted over-bound value for a LOOP row fails the bound check.
Plus the shipped-tree reading itself, and that the derivation can observe a declared loop going
missing (a check that can only ever say "equal" observes nothing).
"""

from engine.season.harness import loops as L
from engine.season.harness import register as R


def _shipped():
    procs, _ = L.build_processes()
    signs = {r: row.get("sign") for r, row in L.loop_rows(R.load()).items()}
    return procs, signs


def test_shipped_tree_reads_amplifiers_derived_equal_declared():
    procs, signs = _shipped()
    res = L.compare(L.derive_cycles(procs), signs, L.DECLARED_CYCLES)
    amp = res["by_sign"]["+"]
    assert res["equal"], (amp["undeclared"], amp["underived"], res["unmapped"], res["stale"])
    # assert it asserted: the equality is over a non-empty set on both sides, not two empties
    assert amp["derived"] and amp["declared"]
    assert {r for _, r in amp["declared"]} == {r for r, s in signs.items() if s == "+"}
    assert sorted(k for k, _ in amp["declared"]) == amp["derived"]


def test_planted_amplifier_with_no_loop_row_makes_derived_differ_and_is_named():
    procs, signs = _shipped()
    control = L.compare(L.derive_cycles(procs), signs, L.DECLARED_CYCLES)
    assert control["equal"]
    plant = L.Process("PLANTED: stores breed stores", (("Rung.stores", "+"),),
                      (("Rung.stores", "+"),))
    res = L.compare(L.derive_cycles(procs + (plant,)), signs, L.DECLARED_CYCLES)
    assert not res["equal"]
    assert res["by_sign"]["+"]["undeclared"] == [("Rung.stores",)]
    assert res["by_sign"]["+"]["underived"] == []


def test_removing_the_witness_fan_out_makes_its_declared_loops_underived():
    procs, signs = _shipped()
    cut = tuple(p for p in procs if p.name != "WITNESS: fan-out over the log")
    assert len(cut) == len(procs) - 1
    res = L.compare(L.derive_cycles(cut), signs, L.DECLARED_CYCLES)
    assert not res["equal"]
    gone = {r for _, r in res["by_sign"]["+"]["underived"]}
    assert gone == {"H-102", "H-112"}


def test_a_loop_row_with_no_cycle_key_is_a_mismatch_not_a_silent_pass():
    procs, signs = _shipped()
    res = L.compare(L.derive_cycles(procs), {**signs, "H-999": "+"}, L.DECLARED_CYCLES)
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
    try:
        L.check_bounds({"H-104": ("Person.claim_ledger",)}, {}, {("H-104", "Event"): 1})
    except ValueError as e:
        assert "names no looped quantity" in str(e)
    else:
        raise AssertionError("a bound on a quantity the row does not loop was accepted")


def test_a_requires_stem_with_no_read_map_refuses(monkeypatch):
    trimmed = {k: v for k, v in L.STEM_READS.items() if k != "stores"}
    monkeypatch.setattr(L, "STEM_READS", trimmed)
    try:
        L.build_processes()
    except SystemExit as e:
        assert "REQUIRES_STEMS" in str(e)
    else:
        raise AssertionError("a stem with no read map was silently dropped")
