"""
Unit tests for the pure core of engine_params_check (ED-1052).

validate_file and quote_in_doc are I/O-free (a doc_reader is injected), so these tests
pin the round-trip + schema guarantees without touching the filesystem.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import engine_params_check as E  # noqa: E402


def _reader(docs):
    return lambda path: docs.get(path)


def test_quote_in_doc_whitespace_normalized():
    assert E.quote_in_doc("Range: **1–7**", "... Range:   **1–7**  (all attributes) ...") is True
    assert E.quote_in_doc("not present", "some other text") is False


def test_clean_file_has_no_errors():
    data = {
        "schema_version": 1, "subsystem": "t",
        "scalars": {"tn": {"value": 7, "type": "int",
                           "source": {"doc": "d.md", "quote": "| Standard | 7 |"}}},
        "formulas": {"pool": {"expr": "(agility * 2) + 3", "inputs": ["agility"],
                              "clamp": {"min": 5},
                              "source": {"doc": "d.md", "quote": "Agility × 2"}}},
        "tables": {"faces": {"rows": {"10": 2},
                             "source": {"doc": "d.md", "quote": "face 10"}}},
    }
    docs = {"d.md": "| Standard | 7 | Agility × 2 ... face 10 +2"}
    assert E.validate_file(data, _reader(docs)) == []


def test_quote_drift_flagged():
    data = {"schema_version": 1, "subsystem": "t",
            "scalars": {"x": {"value": 9, "type": "int",
                              "source": {"doc": "d.md", "quote": "value is 9"}}}}
    errs = E.validate_file(data, _reader({"d.md": "value is 7"}))
    assert any("quote not found" in e for e in errs)


def test_missing_doc_flagged():
    data = {"schema_version": 1, "subsystem": "t",
            "scalars": {"x": {"value": 1, "type": "int",
                              "source": {"doc": "gone.md", "quote": "x"}}}}
    errs = E.validate_file(data, _reader({}))
    assert any("not found in working tree" in e for e in errs)


def test_clamp_min_gt_max_flagged():
    data = {"schema_version": 1, "subsystem": "t",
            "scalars": {"x": {"value": 1, "type": "int", "clamp": {"min": 9, "max": 2},
                              "source": {"doc": "d.md", "quote": "x"}}}}
    errs = E.validate_file(data, _reader({"d.md": "x"}))
    assert any("clamp.min" in e for e in errs)


def test_formula_undeclared_identifier_flagged():
    data = {"schema_version": 1, "subsystem": "t",
            "formulas": {"f": {"expr": "agility * mystery", "inputs": ["agility"],
                               "source": {"doc": "d.md", "quote": "x"}}}}
    errs = E.validate_file(data, _reader({"d.md": "x"}))
    assert any("mystery" in e for e in errs)


def test_formula_may_reference_other_param_keys_and_math():
    data = {"schema_version": 1, "subsystem": "t",
            "scalars": {"base": {"value": 3, "type": "int",
                                 "source": {"doc": "d.md", "quote": "x"}}},
            "formulas": {"f": {"expr": "min(base, agility)", "inputs": ["agility"],
                               "source": {"doc": "d.md", "quote": "x"}}}}
    assert E.validate_file(data, _reader({"d.md": "x"})) == []


def test_non_numeric_scalar_flagged():
    data = {"schema_version": 1, "subsystem": "t",
            "scalars": {"x": {"value": "seven", "type": "int",
                              "source": {"doc": "d.md", "quote": "x"}}}}
    errs = E.validate_file(data, _reader({"d.md": "x"}))
    assert any("must be a number" in e for e in errs)


def test_bool_is_not_a_number():
    data = {"schema_version": 1, "subsystem": "t",
            "scalars": {"x": {"value": True, "type": "int",
                              "source": {"doc": "d.md", "quote": "x"}}}}
    errs = E.validate_file(data, _reader({"d.md": "x"}))
    assert any("must be a number" in e for e in errs)


def test_empty_file_flagged():
    errs = E.validate_file({"schema_version": 1, "subsystem": "t"}, _reader({}))
    assert any("no scalars, formulas, or tables" in e for e in errs)


if __name__ == '__main__':
    fns = [v for k, v in sorted(globals().items()) if k.startswith('test_') and callable(v)]
    p = f = 0
    for fn in fns:
        try:
            fn(); p += 1
        except AssertionError as e:
            f += 1; print(f"FAIL {fn.__name__}: {e}")
    print(f"{p} passed, {f} failed")
    sys.exit(1 if f else 0)
