"""THE NINE'S CONJUNCT RECORD (`IS-A-01`): a row's `met` text is a list of conjuncts the register reads.

`register.check_requirements` reads each row's `conjuncts:` -- `{id, text, argv, expects, holds,
reading}` -- and refuses a status the conjuncts do not support. Each test plants a scratch copy of
the file through `monkeypatch.setattr(register, "REQUIREMENTS", scratch)` and reads the exit code
and the printed line. The register executes nothing: a bare relabel to `met` with honest readings
still exits 0, and no test here claims otherwise.
"""
from __future__ import annotations

import yaml

from engine.season.harness import register

A_MODULE = ["python", "-m", "engine.season.harness.register"]


def reading(**over) -> dict:
    r = {"tree": "d6cf088", "date": "2026-11-14", "seed": 0, "seasons": 1,
         "line": "a printed line", "control": "none", "does_not_show": "one seed"}
    r.update(over)
    return r


def conjunct(cid: str, holds: str = "yes", argv=None, **over) -> dict:
    c = {"id": cid, "text": "a conjunct", "argv": list(argv or A_MODULE),
         "expects": "a printed line", "holds": holds}
    if holds in ("yes", "no"):
        c["reading"] = reading()
    c.update(over)
    return c


def row(rid: str = "R-01", status: str = "met", conjuncts=None, **over) -> dict:
    r = {"id": rid, "statement": "a statement", "status": status,
         "measure": "python -m engine.season.harness.register --requirements",
         "conjuncts": conjuncts if conjuncts is not None else [conjunct(rid + ".a")]}
    r.update(over)
    return r


def plant(tmp_path, monkeypatch, rows, scales=None) -> None:
    """Write a scratch requirements file and point the register at it."""
    doc = {"ruled_by": "scratch", "ed": "scratch", "rows": rows}
    if scales is not None:
        doc["scales"] = scales
    scratch = tmp_path / "requirements.yaml"
    scratch.write_text(yaml.safe_dump(doc), encoding="utf-8")
    monkeypatch.setattr(register, "REQUIREMENTS", scratch)


def refused(tmp_path, monkeypatch, capsys, rows, scales=None):
    plant(tmp_path, monkeypatch, rows, scales)
    rc = register.check_requirements()
    return rc, capsys.readouterr().out


def test_a_clean_scratch_file_exits_zero_and_prints_the_form(tmp_path, monkeypatch, capsys):
    """The control for every refusal below: the same planted file, unbroken."""
    rc, out = refused(tmp_path, monkeypatch, capsys, [row()])
    assert rc == 0, out
    assert "R-01  met  " in out and "1 of 1 conjuncts  tree d6cf088" in out, out


def test_a_met_row_without_a_reading_is_refused(tmp_path, monkeypatch, capsys):
    c = conjunct("R-01.a")
    del c["reading"]
    rc, out = refused(tmp_path, monkeypatch, capsys, [row(conjuncts=[c])])
    assert rc != 0 and "R-01" in out, out


def test_a_met_row_with_one_conjunct_unread_is_refused(tmp_path, monkeypatch, capsys):
    rows = [row(conjuncts=[conjunct("R-01.a"), conjunct("R-01.b", holds="unread")])]
    rc, out = refused(tmp_path, monkeypatch, capsys, rows)
    assert rc != 0 and "R-01.b" in out, out


def test_a_met_row_whose_conjunct_has_no_reading_line_is_refused(tmp_path, monkeypatch, capsys):
    c = conjunct("R-01.a")
    del c["reading"]["line"]
    rc, out = refused(tmp_path, monkeypatch, capsys, [row(conjuncts=[c])])
    assert rc != 0 and "line" in out, out


def test_a_seed_of_zero_is_a_reading_not_an_absence(tmp_path, monkeypatch, capsys):
    """`seed: 0` is falsy; the refusal must read presence, not truth."""
    rc, out = refused(tmp_path, monkeypatch, capsys,
                      [row(conjuncts=[conjunct("R-01.a", reading=reading(seed=0))])])
    assert rc == 0, out


def test_a_met_row_with_no_conjunct_is_refused(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys, [row(conjuncts=[])])
    assert rc != 0 and "R-01" in out, out


def test_a_partial_row_with_no_conjunct_at_yes_is_refused(tmp_path, monkeypatch, capsys):
    rows = [row("R-04", "partial", [conjunct("R-04.a", holds="unread")])]
    rc, out = refused(tmp_path, monkeypatch, capsys, rows)
    assert rc != 0 and "R-04" in out, out
    rows = [row("R-04", "partial", [conjunct("R-04.a", holds="yes"),
                                    conjunct("R-04.b", holds="unread")])]
    rc, out = refused(tmp_path, monkeypatch, capsys, rows)
    assert rc == 0 and "R-04  partial  1 of 2 conjuncts" in out, out


def test_a_not_met_row_may_carry_no_conjunct_at_yes(tmp_path, monkeypatch, capsys):
    rows = [row("R-05", "not_met", [conjunct("R-05.a", holds="unread")])]
    rc, out = refused(tmp_path, monkeypatch, capsys, rows)
    assert rc == 0, out


def test_a_conjunct_with_no_argv_is_refused(tmp_path, monkeypatch, capsys):
    for bad in (None, [], "python -m engine.season.harness.register"):
        c = conjunct("R-05.a", holds="unread")
        c["argv"] = bad
        rc, out = refused(tmp_path, monkeypatch, capsys, [row("R-05", "not_met", [c])])
        assert rc != 0 and "R-05.a" in out and "argv" in out, (bad, out)


def test_a_conjunct_holds_outside_the_three_words_is_refused(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys,
                      [row("R-05", "not_met", [conjunct("R-05.a", holds="maybe")])])
    assert rc != 0 and "holds" in out, out


def test_a_conjunct_id_outside_its_row_is_refused(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys, [row(conjuncts=[conjunct("R-02.a")])])
    assert rc != 0 and "R-02.a" in out, out


def test_the_oldest_reading_names_the_tree_printed(tmp_path, monkeypatch, capsys):
    cs = [conjunct("R-01.a", reading=reading(tree="newer", date="2026-11-14")),
          conjunct("R-01.b", reading=reading(tree="older", date="2026-11-02"))]
    rc, out = refused(tmp_path, monkeypatch, capsys, [row(conjuncts=cs)])
    assert rc == 0 and "2 of 2 conjuncts  tree older" in out, out
