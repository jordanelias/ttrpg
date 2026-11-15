"""B03.68 -- THE THREAD OPERATION ROSTER (`rosters.yaml: thread_operations`) AND THE VERB LOADER'S CHECK ON IT.

A thread operation is one named working a practitioner attempts on the thread. The roster is the closed set of
their names; a verb row that names one through its `operation:` column names a member or the load refuses
(as it refuses an off-roster `beneficiary:`). No shipped row names one yet -- the rows are B35's -- so the
planted row is the only observation of the check.
"""
from __future__ import annotations

import pytest

from .test_governance_build import _LEVY_ROW, _load_with, _verb_table_text


def test_a_verb_row_naming_an_unrostered_operation_is_refused():
    from ..data.rosters import THREAD_OPERATIONS
    assert "fly" not in THREAD_OPERATIONS, "the planted operation must really be outside the roster"
    src = _verb_table_text()
    planted = src.replace(_LEVY_ROW, _LEVY_ROW + '    operation: "fly"\n', 1)
    assert planted != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="thread_operations"):
        _load_with(planted)
    # control: the same row naming a rostered operation loads, so the refusal above is the roster's and not
    # the loader refusing the column itself as an unknown key
    member = sorted(THREAD_OPERATIONS)[0]
    ok = src.replace(_LEVY_ROW, _LEVY_ROW + f'    operation: "{member}"\n', 1)
    assert ok != src
    _load_with(ok)


def test_the_roster_names_the_seven_operations():
    from ..data.rosters import THREAD_OPERATIONS
    assert THREAD_OPERATIONS == frozenset(
        {"leap", "weave", "pull", "past_pull", "lock", "dissolve", "mend"})
