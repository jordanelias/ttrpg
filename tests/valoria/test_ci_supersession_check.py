"""
Unit tests for the pure core of ci_supersession_check (find_matches).

find_matches is I/O-free: given the register's `entries` list and a set of changed
repo-relative paths, it returns one match dict per entry whose 'files_to_recheck'
overlaps the changed set. These tests pin that contract.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))
import ci_supersession_check  # noqa: E402


def _entry(superseded_id, recheck, scope='', replacement=''):
    return {
        'superseded_id': superseded_id,
        'scope': scope,
        'replacement': replacement,
        'files_to_recheck': recheck,
    }


def test_overlap_returns_match_with_id_and_touched():
    entries = [
        _entry(
            '250715f',
            ['designs/provincial/victory_v30.md', 'params/bg/ci_seizure.md'],
            scope='Engine v3 seizure threshold',
            replacement='Threshold remains CI >= 60; probabilistic declaration.',
        ),
    ]
    changed = {'designs/provincial/victory_v30.md', 'designs/unrelated.md'}

    matches = ci_supersession_check.find_matches(entries, changed)

    assert len(matches) == 1
    m = matches[0]
    assert m['id'] == '250715f'
    # Only the overlapping path is reported, and it is sorted.
    assert m['touched'] == ['designs/provincial/victory_v30.md']
    assert m['scope'] == 'Engine v3 seizure threshold'
    assert m['replacement'] == 'Threshold remains CI >= 60; probabilistic declaration.'


def test_multiple_overlap_paths_sorted():
    entries = [
        _entry('E1', ['b/file.md', 'a/file.md', 'c/file.md']),
    ]
    changed = {'c/file.md', 'a/file.md', 'z/other.md'}

    matches = ci_supersession_check.find_matches(entries, changed)

    assert len(matches) == 1
    assert matches[0]['touched'] == ['a/file.md', 'c/file.md']


def test_no_overlap_returns_empty():
    entries = [
        _entry('250715f', ['designs/provincial/victory_v30.md']),
    ]
    changed = {'README.md', 'tools/ci_common.py'}

    assert ci_supersession_check.find_matches(entries, changed) == []


def test_empty_entries_returns_empty():
    assert ci_supersession_check.find_matches([], {'anything.md'}) == []


def test_no_entries_arg_none_safe():
    # Defensive: a falsy entries value yields no matches.
    assert ci_supersession_check.find_matches(None, {'anything.md'}) == []


def test_non_dict_and_bad_recheck_entries_skipped():
    entries = [
        'not-a-dict',
        {'superseded_id': 'NoRecheck'},                       # missing files_to_recheck
        {'superseded_id': 'BadRecheck', 'files_to_recheck': 'designs/x.md'},  # str, not list
        _entry('Good', ['designs/x.md']),
    ]
    changed = {'designs/x.md'}

    matches = ci_supersession_check.find_matches(entries, changed)

    assert [m['id'] for m in matches] == ['Good']


def test_missing_id_defaults_to_question_mark():
    entries = [{'files_to_recheck': ['designs/x.md']}]
    matches = ci_supersession_check.find_matches(entries, {'designs/x.md'})
    assert matches[0]['id'] == '?'


def test_scope_and_replacement_truncated():
    entries = [
        _entry('Long', ['designs/x.md'], scope='s' * 200, replacement='r' * 200),
    ]
    m = ci_supersession_check.find_matches(entries, {'designs/x.md'})[0]
    assert len(m['scope']) == 80
    assert len(m['replacement']) == 120
