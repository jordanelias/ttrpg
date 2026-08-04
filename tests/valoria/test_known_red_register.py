"""The falsifier for `conftest.py`'s KNOWN_RED register (W1, ED-MB-0061).

A register that excuses failing tests is a loaded gun pointed at the shipping gate. Two ways it
goes wrong, and this file closes both:

1. **A stale entry excuses nothing.** If a listed test is renamed or deleted, the entry silently
   stops matching. Nobody notices, and the register grows a fiction. `test_every_known_red_id_was_collected`
   fails on the first stale id.
2. **It becomes the place failures go to die.** The count is pinned, so ADDING a tenth entry is a
   deliberate act that fails this test until someone changes the number and says why in the commit.
   Growth by accretion is the failure mode; a number in a test is the cheapest brake on it.

The strict-xfail direction (a test that starts PASSING turns the suite red) is enforced by pytest
itself, not here — that is what `strict=True` buys and why it was chosen.
"""
import importlib.util
import os

HERE = os.path.dirname(__file__)


def _load_conftest():
    """Load the sibling conftest by PATH.

    `tests/valoria` is a package (`__init__.py`) and its conftest is not importable as a bare
    `conftest` module, nor as `tests.valoria.conftest` without assuming the rootdir. Loading by
    path makes this test independent of how pytest was invoked.
    """
    spec = importlib.util.spec_from_file_location(
        '_valoria_conftest', os.path.join(HERE, 'conftest.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


valoria_conftest = _load_conftest()

# Pinned deliberately. Raising it requires a commit that says which failure joined the set and why
# it is not a regression. Lowering it is what happens when the MB lane fixes one.
EXPECTED_KNOWN_RED = 9


def test_the_register_has_not_grown_by_accretion():
    n = len(valoria_conftest.KNOWN_RED)
    assert n == EXPECTED_KNOWN_RED, (
        f'KNOWN_RED holds {n} entries, expected {EXPECTED_KNOWN_RED}. If the MB lane fixed one, '
        'remove it here and lower the pin. If a NEW failure was added, say in the commit message '
        'which one and why it is not a regression — a register that grows quietly is how a red '
        'gate becomes a permanently ignored one (ED-MB-0061).')


def _stale_ids(nodeids):
    """The detection logic, extracted so a control can actually exercise it.

    F5 from the process review: the control below asserted only that a planted path does not
    exist -- it never fed that path through the check. Cripple the detection loop and the
    "control" still passed. That is verbatim the defect ED-IN-0139 F3 recorded the same day
    (a control covering one branch, described as covering both), committed inside the test file
    written to prevent it. Extracting the predicate is what makes the control able to fail.
    """
    missing = []
    for nodeid in nodeids:
        path, _, testname = nodeid.partition('::')
        full = os.path.join(HERE, path)
        if not os.path.exists(full):
            missing.append(nodeid + ' (no such file)')
            continue
        with open(full, encoding='utf-8', errors='ignore') as fh:
            if ('def ' + testname + '(') not in fh.read():
                missing.append(nodeid + ' (file exists, test does not)')
    return missing


def test_every_known_red_id_names_a_real_test(pytestconfig):
    """No stale entries: every id must correspond to a file and a test that exists.

    Checked textually rather than by re-running collection — collecting the suite from inside the
    suite is slow and re-entrant. A file-plus-`def` check catches the realistic rot (renamed test,
    deleted file) without that cost.
    """
    missing = _stale_ids(valoria_conftest.KNOWN_RED)
    assert not missing, (
        'KNOWN_RED entries that name nothing — a stale entry excuses a test that no longer '
        f'exists and hides one that does: {missing}')


def test_the_staleness_guard_can_fail():
    """POSITIVE CONTROL: the check must OBSERVE a stale id, in both ways an id can go stale.

    The earlier version asserted only that a planted path was absent and never called the
    detection logic — a control that could not fail.
    """
    assert _stale_ids(['test_no_such_module.py::test_no_such_test']), \
        'the staleness check cannot observe an id whose FILE is gone'
    assert _stale_ids(['test_known_red_register.py::test_renamed_away']), \
        'the staleness check cannot observe an id whose TEST is gone'
    assert _stale_ids(['test_known_red_register.py::test_the_staleness_guard_can_fail']) == [], \
        'the staleness check cries wolf on an id that is fine'


def test_the_register_is_scoped_to_the_known_lane():
    """Every excused test must be one the ED-MB-0061 failure set actually covers.

    This register is gate hygiene for the OTHER lanes, not an amnesty. If an entry appears that
    does not cite the MB ledger item, the mechanism has started absorbing unrelated failures —
    which is precisely how a targeted exception becomes a general one.
    """
    unscoped = [k for k, v in valoria_conftest.KNOWN_RED.items() if 'ED-MB-0061' not in v]
    assert not unscoped, (
        f'{len(unscoped)} KNOWN_RED entr(y/ies) cite no ledger item: {unscoped}. '
        'An excused failure with no owner is an ignored failure.')
