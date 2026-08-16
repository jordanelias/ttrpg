"""Guards for tools/ci_pp_frozen_check.py — PP as frozen historical vocabulary (ED-IN-0190).

⚠ NO ABOVE-CEILING PP ID IS SPELLED LITERALLY ANYWHERE IN THIS FILE. Docstrings and test bodies
are harvested into `references/test_register.json`, which the gate scans — so writing the example
id in prose makes the generated register violate the rule the test is guarding. That happened, and
it is the same self-matching shape as the gate counting its own docstring. Build the id from
`PP_FROZEN_CEILING`; never type it.

Every assertion here is one the pre-ruling tree WOULD HAVE FAILED. Measured 2026-08-14 on the
tree at fba71e0: the gate reported 4 unannotated archive pointers (all four targets verified
absent from `main`) plus 1 self-match on its own docstring. Both are fixed; these pin them.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_pp_frozen_check as pp  # noqa: E402


def test_the_gate_passes_on_the_live_tree():
    assert pp.run_checks() == [], pp.run_checks()


def test_left_boundary_excludes_OPP(tmp_path, monkeypatch):
    """THE DEFECT THAT WOULD HAVE OPENED THIS GATE WITH 34 FABRICATED FINDINGS.

    `ci_common.PP_ID_PAT` is bare `PP-\\d+`. Scanned over the corpus it matches inside
    `EVT-OPP-03`, and one proposals document alone contributed 34 such hits.
    """
    found = [m.group(0) for m in pp.PP_CITATION_RE.finditer(
        'EVT-OPP-03 and OPP-04 and APP-726 are not patches; PP-652 is')]
    assert found == ['PP-652'], found


def test_right_boundary_does_not_truncate(tmp_path):
    """`PP-72` must not match inside `PP-726` — that would read as under the ceiling."""
    found = [m.group(0) for m in pp.PP_CITATION_RE.finditer('PP-726')]
    assert found == ['PP-726'], found


def test_an_id_above_the_ceiling_FAILS(tmp_path, monkeypatch):
    """Positive control: plant the exact thing 'frozen' forbids."""
    root = tmp_path
    (root / 'systems').mkdir()
    over = f'PP-{pp.PP_FROZEN_CEILING + 1}'   # built, never spelled — a literal here lands in
    (root / 'systems' / 'doc.md').write_text(f'this cites {over}, a brand new patch number\n')
    monkeypatch.setattr(pp, 'REPO_ROOT', str(root))
    monkeypatch.setattr(pp, 'SELF', 'tools/ci_pp_frozen_check.py')
    violations = []
    pp.check_pp_is_frozen(violations)
    assert len(violations) == 1, violations
    assert over in violations[0] and 'frozen ceiling' in violations[0]


def test_an_id_at_the_ceiling_PASSES(tmp_path, monkeypatch):
    """The boundary is inclusive — PP-726 is a real, cited, historical id."""
    root = tmp_path
    (root / 'systems').mkdir()
    (root / 'systems' / 'doc.md').write_text(f'PP-{pp.PP_FROZEN_CEILING} is the last one\n')
    monkeypatch.setattr(pp, 'REPO_ROOT', str(root))
    monkeypatch.setattr(pp, 'SELF', 'tools/ci_pp_frozen_check.py')
    violations = []
    pp.check_pp_is_frozen(violations)
    assert violations == [], violations


def test_an_unannotated_evacuated_pointer_FAILS(tmp_path, monkeypatch):
    """Positive control for R1 — the state the register was actually in before the ruling."""
    root = tmp_path
    (root / 'registers').mkdir()
    (root / 'registers' / 'patch_register_active.yaml').write_text(
        '# Archival batch: 4 applied PPs -> deprecated/archives/patches/gone.yaml\n')
    monkeypatch.setattr(pp, 'REPO_ROOT', str(root))
    violations = []
    pp.check_archive_pointers_name_the_fork(violations)
    assert len(violations) == 1, violations
    assert 'names no fork ref' in violations[0]


def test_annotating_the_pointer_CLEARS_it(tmp_path, monkeypatch):
    root = tmp_path
    (root / 'registers').mkdir()
    (root / 'registers' / 'patch_register_active.yaml').write_text(
        '# Archival batch -> deprecated/archives/patches/gone.yaml  [FORK: c451bcb — not on main]\n')
    monkeypatch.setattr(pp, 'REPO_ROOT', str(root))
    violations = []
    pp.check_archive_pointers_name_the_fork(violations)
    assert violations == [], violations


def test_a_pointer_that_still_EXISTS_needs_no_annotation(tmp_path, monkeypatch):
    """The rule is about absence, not about the path shape — otherwise it would demand a fork
    ref for a register still sitting on main, and teach the next reader that it had left."""
    root = tmp_path
    (root / 'registers').mkdir()
    (root / 'deprecated' / 'archives' / 'patches').mkdir(parents=True)
    (root / 'deprecated' / 'archives' / 'patches' / 'here.yaml').write_text('patches: []\n')
    (root / 'registers' / 'patch_register_active.yaml').write_text(
        '# Archival batch -> deprecated/archives/patches/here.yaml\n')
    monkeypatch.setattr(pp, 'REPO_ROOT', str(root))
    violations = []
    pp.check_archive_pointers_name_the_fork(violations)
    assert violations == [], violations


def test_the_gate_does_not_count_itself():
    """ED-IN-0159 §2.4 recurring: the gate's own docstring spells an above-ceiling id as its
    example, and its first run reported a violation against itself. A census whose configuration
    names its own subject is self-matching by construction."""
    assert pp.SELF.endswith('ci_pp_frozen_check.py')
    assert all(pp.SELF not in os.path.relpath(f, pp.REPO_ROOT) for f in pp._iter_live_files())
