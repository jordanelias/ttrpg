"""`check_requirements` resolves each conjunct's `argv` to something that exists (`IS-A-01`, the
nine-gate's edit 1), and reads `scales[].conjunct` (`IS-A-04`).

A planted scratch file per test, through the helpers of `test_register_reading.py`. The register
executes nothing: it asks whether the command named is one it can find. Arms: B a module that does
not exist; C a `-k` whose only name is `import`; D `argv: ["true"]`; the control is the shipped file.
"""
from __future__ import annotations


from engine.season.harness import register
from engine.season.tests.test_register_reading import conjunct, refused, row

TEST_FILE = "engine/season/tests/test_register_reading.py"


def one(argv, holds="yes", rid="R-01", status="met"):
    return [row(rid, status, [conjunct(rid + ".a", holds=holds, argv=argv)])]


def test_all_met_with_missing_module_exits_nonzero(tmp_path, monkeypatch, capsys):
    rows = [row(f"R-0{n}", "met", [conjunct(f"R-0{n}.a",
              argv=["python", "-m", "engine.season.harness.no_such_module"])]) for n in range(1, 10)]
    rc, out = refused(tmp_path, monkeypatch, capsys, rows)
    assert rc != 0 and "no_such_module" in out and "does not exist" in out, out


def test_a_module_that_exists_resolves(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys,
                      one(["python", "-m", "engine.season.harness.storybar"]))
    assert rc == 0, out


def test_a_module_under_a_missing_parent_is_a_violation_not_a_crash(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys,
                      one(["python", "-m", "no_such_pkg.no_such_module"]))
    assert rc != 0 and "no_such_pkg.no_such_module" in out, out


def test_a_path_resolves_by_existence(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys, one(["python", "tools/m1_acceptance.py"]))
    assert rc == 0, out
    rc, out = refused(tmp_path, monkeypatch, capsys, one(["python", "tools/no_such_tool.py"]))
    assert rc != 0 and "tools/no_such_tool.py" in out and "does not exist" in out, out


def test_k_expression_naming_only_import_is_refused(tmp_path, monkeypatch, capsys):
    argv = ["python", "-m", "pytest", TEST_FILE, "-k", "zz_no_such_test or import"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(argv))
    assert rc != 0 and "zz_no_such_test" in out, out


def test_k_expression_needs_every_name_not_one(tmp_path, monkeypatch, capsys):
    """Each name must be found; the boolean is not evaluated (an `and` of names in two tests passes here)."""
    both = ["python", "-m", "pytest", TEST_FILE, "-k",
            "a_met_row_without_a_reading and a_clean_scratch_file"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(both))
    assert rc == 0, out
    one_dead = ["python", "-m", "pytest", TEST_FILE, "-k",
                "a_met_row_without_a_reading or zz_no_such_test"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(one_dead))
    assert rc != 0 and "zz_no_such_test" in out, out


def test_k_expression_does_not_resolve_a_name_under_not(tmp_path, monkeypatch, capsys):
    argv = ["python", "-m", "pytest", TEST_FILE, "-k",
            "a_met_row_without_a_reading and not zz_no_such_test"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(argv))
    assert rc == 0, out


def test_k_expression_reads_only_the_test_files_named(tmp_path, monkeypatch, capsys):
    """A name that exists in another test file does not satisfy a `-k` over this one."""
    argv = ["python", "-m", "pytest", TEST_FILE, "-k", "test_measure_true_is_refused"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(argv))
    assert rc != 0, out
    argv = ["python", "-m", "pytest", "engine/season/tests", "-k",
            "test_measure_true_is_refused"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(argv))
    assert rc == 0, out


def test_a_pytest_file_that_is_missing_is_refused(tmp_path, monkeypatch, capsys):
    argv = ["python", "-m", "pytest", "engine/season/tests/test_no_such_file.py", "-k", "x"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(argv))
    assert rc != 0 and "test_no_such_file.py" in out, out


def test_measure_true_is_refused(tmp_path, monkeypatch, capsys):
    rc, out = refused(tmp_path, monkeypatch, capsys, one(["true"]))
    assert rc != 0 and "not a command this check can find" in out, out


def test_an_unread_conjunct_is_not_resolved(tmp_path, monkeypatch, capsys):
    """`IS-A-02` writes conjuncts whose instrument a later batch builds: an `unread` one carries an
    argv but is not resolved (a met row still refuses it, for being unread)."""
    argv = ["python", "-m", "engine.season.harness.no_such_module"]
    rc, out = refused(tmp_path, monkeypatch, capsys, one(argv, holds="unread", rid="R-05",
                                                       status="not_met"))
    assert rc == 0, out


def test_a_scales_row_naming_no_r04_conjunct_is_refused(tmp_path, monkeypatch, capsys):
    rows = [row("R-04", "partial", [conjunct("R-04.a"), conjunct("R-04.b", holds="unread")])]
    rc, out = refused(tmp_path, monkeypatch, capsys, rows,
                      scales=[{"scale": "x", "conjunct": "R-04.a"}])
    assert rc == 0, out
    rc, out = refused(tmp_path, monkeypatch, capsys, rows,
                      scales=[{"scale": "x", "conjunct": "R-04.c9"}])
    assert rc != 0 and "R-04.c9" in out, out


def test_a_scales_row_with_no_conjunct_key_is_refused(tmp_path, monkeypatch, capsys):
    """B02.31 gave each scale its conjunct, so a row without the key is a violation."""
    rc, out = refused(tmp_path, monkeypatch, capsys, [row()], scales=[{"scale": "x"}])
    assert rc != 0 and "names no conjunct" in out, out


def test_shipped_file_exits_zero(capsys):
    """The control: the shipped file satisfies the register (B02.38 wrote the nine's conjuncts and
    B02.31 the scales' keys)."""
    assert register.check_requirements() == 0, capsys.readouterr().out


def test_a_measure_is_resolved_the_way_an_argv_is(tmp_path, monkeypatch, capsys):
    """A row's `measure:` goes through the one resolver a conjunct's `argv` does: a `-k` naming no test, a module that
    does not exist and a command the check cannot find are each refused; the text after `#` is the row's note."""
    ok = "python -m engine.season.harness.register --requirements  # a note with `-k nothing_here`"
    rc, out = refused(tmp_path, monkeypatch, capsys, [row(measure=ok)])
    assert rc == 0, out
    for bad in ("python -m pytest engine/season/tests -k 'zzz_no_such_test_anywhere'",
                "python -m engine.season.harness.no_such_module",
                "true"):
        rc, out = refused(tmp_path, monkeypatch, capsys, [row(measure=bad)])
        assert rc != 0 and "R-01" in out, (bad, out)
