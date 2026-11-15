"""H-141 -- a subject that earns every kind cannot be silenced by a named one.

`Subject.earns=None` is the plain-list contract (the subject earns EVERY kind the row declares), and
`loop/resolve.py::_fold` reads an EMPTY `earned` set as "all declared kinds". The moment one moved
subject of the same `Change` names a kind, `earned` is non-empty and the `None` subject's contract is
dropped without a word. HR-1 chose naming over a sentinel (`Subject`'s docstring), so the mix is refused
where it is built: at `Change` construction, as an `InstrumentDefect` naming the subjects.

The control beside the refusal: an all-`None` `Change`, an all-named one and a single subject each
still construct, so the refusal can only be the mix.
"""
import pytest

from engine.season.gaps import InstrumentDefect
from engine.season.state.gate import Change, Subject


def _noop():
    return None


def test_a_change_mixing_none_and_named_earns_is_refused():
    plain = Subject.entity("rungs", "R-plain")
    named = Subject.entity("rungs", "R-named", earns="x")
    with pytest.raises(InstrumentDefect) as raised:
        Change((plain, named), _noop)
    said = str(raised.value)
    assert "R-plain" in said and "R-named" in said, said
    # the order of the subjects does not matter
    with pytest.raises(InstrumentDefect):
        Change((named, plain), _noop)
    # a tuple of kinds is a named earns too
    with pytest.raises(InstrumentDefect):
        Change((plain, Subject.entity("rungs", "R-many", earns=("x", "y"))), _noop)


def test_the_refusal_is_the_mix_alone():
    a, b = Subject.entity("rungs", "A"), Subject.entity("rungs", "B")
    na, nb = Subject.entity("rungs", "A", earns="x"), Subject.entity("rungs", "B", earns="y")
    checked = 0
    for subjects in ((), (a,), (a, b), (na,), (na, nb)):
        assert Change(subjects, _noop).subjects == subjects
        checked += 1
    assert checked == 5
