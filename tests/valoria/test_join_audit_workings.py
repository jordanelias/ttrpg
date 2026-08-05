"""Guards for `tools/join_audit_workings.py` — the join that lets working papers be purged.

WHY THIS NEEDS A TEST BEFORE IT RUNS, NOT AFTER. The tool deletes files. Its whole safety argument
is one property — the joined document can be split back into the exact bytes it swallowed — and
once `--purge` has run, that property is unfalsifiable against the sources, because the sources are
gone. So the round-trip has to be pinned while the fragments still exist, and it has to be pinned
with controls that can actually fail. A "verified" flag on an irreversible operation is worth
exactly as much as the check behind it.

The controls below plant the three ways a concatenate-and-split scheme silently loses content:
a fragment whose body contains something that looks like a delimiter, a body whose trailing
newlines get eaten by the join, and a body that is empty.
"""
import os
import sys

import pytest

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import join_audit_workings as J  # noqa: E402


# --------------------------------------------------------------------------------------
# The property the deletion rests on
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize('bodies', [
    {'a/x.md': 'plain body\n'},
    {'a/x.md': 'one\n', 'a/b/y.md': 'two\n', 'c/z.md': 'three\n'},
    # trailing-newline handling: the join adds framing newlines around the body, and a naive
    # implementation strips or doubles the body's own. Both directions are content loss.
    {'a/x.md': 'no trailing newline'},
    {'a/x.md': 'many trailing newlines\n\n\n'},
    {'a/x.md': ''},                                   # empty file
    {'a/x.md': 'unicode — en-dash, ×, “curly”\n'},
    # a body that CONTAINS delimiter-shaped text: the realistic way an exact-match splitter
    # mis-parses, and the reason the delimiter carries the path rather than being a bare marker.
    {'a/x.md': 'discussing <!-- VALORIA-JOINED-FRAGMENT BEGIN: fake/path.md --> inline\n'},
])
def test_join_split_round_trips(bodies):
    """split(join(x)) == x, for the content shapes that break naive concatenation."""
    parts = [J.HEADER.format(unit='audit/test-unit', count=len(bodies))]
    for rel, body in bodies.items():
        parts.append(J.BEGIN.format(path=rel) + '\n')
        parts.append(body)
        parts.append('\n' + J.END.format(path=rel) + '\n\n')
    recovered = J.split(''.join(parts))
    assert recovered == bodies, (
        'the join is not reversible for this content shape — which means a purge based on it '
        f'would lose bytes. expected {bodies!r}, recovered {recovered!r}')


def test_the_round_trip_can_fail():
    """POSITIVE CONTROL (§0.1 point 2): a corrupted join must NOT round-trip.

    Without this, `test_join_split_round_trips` could be passing because `split` returns whatever
    it was given, or because the comparison is vacuous.
    """
    body = 'original body\n'
    rel = 'a/x.md'
    text = (J.BEGIN.format(path=rel) + '\n') + body + ('\n' + J.END.format(path=rel) + '\n')
    tampered = text.replace('original', 'tampered')
    assert J.split(tampered)[rel] != body, \
        'the round-trip comparison cannot observe a changed body — the safety argument is empty'


def test_split_of_something_with_no_fragments_is_empty_not_wrong():
    """An inert join must be detectable as inert rather than reported as a successful zero-file one.

    `verify()` treats an empty recovery as a problem for exactly this reason: a join that swallowed
    nothing, followed by a purge, is the silent-total-loss case.
    """
    assert J.split('# just a document\n\nno fragments here\n') == {}


# --------------------------------------------------------------------------------------
# Live tree: whatever has been joined must still be reversible
# --------------------------------------------------------------------------------------

def test_every_joined_unit_in_the_tree_round_trips():
    """The CI property. After a purge this checks the join is still internally splittable;
    before one, it checks it byte-for-byte against the surviving sources."""
    units = J.joined_units()
    if not units:
        pytest.skip('no joined units in the tree yet')
    problems = []
    for u in units:
        problems += J.verify(u, against_sources=bool(J.fragments(u)))
    assert not problems, f'{len(problems)} joined unit(s) no longer round-trip: {problems[:5]}'


def test_joined_units_are_not_secretly_empty():
    """A joined file that recovers zero fragments would pass a naive 'no problems' check."""
    for u in J.joined_units():
        with open(os.path.join(J.unit_root(u), J.JOINED_NAME), encoding='utf-8') as fh:
            recovered = J.split(fh.read())
        assert recovered, f'{u}: the joined document contains no recoverable fragment'
