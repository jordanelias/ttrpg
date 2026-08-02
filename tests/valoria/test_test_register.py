"""The test register must stay derived, current, and honest (ED-IN-0122).

WHY. Jordan, 2026-08-02: "track all your tests and their results in such a way that they don't just
become detritus." `references/test_register.json` is that inventory — 132 files, 1,186 tests, each
row carrying what it guards, which lane and module it exercises, whether anyone tried to break it,
and whether it can fail at all.

The register is GENERATED from the AST, never hand-maintained, and this file is what keeps that
true. A hand-maintained inventory of tests would become the detritus it exists to prevent — this
session measured seven registries that had rotted into fiction for exactly that reason.

THE COLUMN THAT EARNS ITS KEEP is `assertionless`: a test function with no `assert` and no
`pytest.raises`/`fail` executes code and cannot fail. That is invisible in a green run and is the
same "reports clean over nothing" shape found seven times in `tools/` this session. Four exist; the
count is pinned below and may only shrink.

TWO NUMBERS THIS REGISTER REPORTS THAT ARE MEANT TO BE UNCOMFORTABLE, both measured, neither fixed
here:
  * **8 files claim mutation-verification; 0 state a kill count.** A claim is not an artifact
    (CLAUDE.md §0.1 point 3). Files written in this very session are among the offenders — their
    counts went into commit messages instead of the docstring, where nothing can read them.
  * **13 of 132 files cite a measurement.** The rest assert without recording what they found.

Neither is asserted as a failure: driving them down is real editorial work, and a gate that goes
red on day one gets switched off. They are surfaced so the number is visible and can move.
"""
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REG = os.path.join(ROOT, 'references', 'test_register.json')

# Tests that execute code but cannot fail. Shrink-only: a NEW one is a defect.
KNOWN_ASSERTIONLESS = 4


@pytest.fixture(scope='module')
def reg():
    if not os.path.exists(REG):
        pytest.fail('references/test_register.json missing — run tools/build_test_register.py')
    with open(REG, encoding='utf-8') as f:
        return json.load(f)


def test_register_is_not_vacuous(reg):
    """Guards the guard: an empty register makes every assertion below trivially true."""
    s = reg['summary']
    assert s['files'] >= 100, f"only {s['files']} test files inventoried — the scan is broken"
    assert s['tests'] >= 900, f"only {s['tests']} tests inventoried"


def test_no_new_assertionless_tests(reg):
    n = reg['summary']['assertionless_tests']
    assert n <= KNOWN_ASSERTIONLESS, (
        f'{n} test function(s) have no assert and no pytest.raises/fail (baseline '
        f'{KNOWN_ASSERTIONLESS}). Such a test executes code and CANNOT FAIL — it is green '
        f'decoration, and a green run cannot show you the difference.')


def test_every_file_explains_what_it_guards(reg):
    """A guard nobody can evaluate is a guard nobody will maintain."""
    undocumented = [n for n, f in reg['files'].items()
                    if 'error' not in f and not f.get('documented')]
    assert not undocumented, (
        f'test file(s) with no module docstring: {undocumented}.\n'
        f'One line saying what breaks if this file is deleted is the minimum.')


def test_lane_attribution_is_derived_not_declared(reg):
    """Lane must come from what a test exercises, not from a header someone maintains.

    `declared_lane` exists as an escape hatch for corpus-wide guards whose subject genuinely is not
    a single module. If it ever becomes the majority, the register has drifted back into a
    hand-maintained artifact and the derivation has stopped working.
    """
    ok = [f for f in reg['files'].values() if 'error' not in f]
    declared = [f for f in ok if f.get('declared_lane')]
    assert len(declared) <= len(ok) // 4, (
        f'{len(declared)}/{len(ok)} files declare a lane by hand — derivation is failing, and a '
        f'hand-maintained field is what this register exists to avoid.')


def test_register_matches_a_fresh_build(reg):
    """Generated artifacts must equal a rebuild, or the committed copy is fiction."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'build_test_register.py'),
                        '--check'], capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, f'build_test_register.py --check failed:\n{r.stdout}\n{r.stderr}'
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'btr', os.path.join(ROOT, 'tools', 'build_test_register.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fresh = mod.scan()
    assert set(fresh) == set(reg['files']), (
        'the committed register lists different files than a fresh scan — regenerate with '
        '`python3 tools/build_test_register.py` and commit.')


# Helper names defined in more than one test file — each is reusable logic that lived where nothing
# could import it, so the next author rewrote it. Shrink-only: extraction is the fix, and a NEW
# duplicate means a helper was copied instead of imported.
KNOWN_DUPLICATED_HELPERS = 21


def test_no_new_duplicated_helpers(reg):
    """Reusable code buried in tests is code that gets missed for import.

    MEASURED at introduction: 253 helper defs / 2,235 LOC inside tests/valoria, with 21 names
    defined across multiple files — `_load` written 12 separate times, `_unit` 9, `field_path` 6.
    That is not a style complaint: every duplicate is a helper someone needed, could not import,
    and wrote again, which is how a suite accumulates divergent copies of the same idea (CLAUDE.md
    §8's same-name-divergent-value defect class, in the test tree rather than the source tree).

    Not asserted to zero — extraction is real work and a gate that goes red on day one gets
    switched off. The count is pinned so it can only improve.
    """
    n = reg['summary']['duplicated_helper_names']
    assert n <= KNOWN_DUPLICATED_HELPERS, (
        f'{n} helper name(s) defined in more than one test file (baseline '
        f'{KNOWN_DUPLICATED_HELPERS}). A helper needed twice belongs in a shared module, not '
        f'copied. See summary.duplicated_helpers in references/test_register.json for the list.')
