"""Guards for `tools/export_params_constants.py` — the dump that lets engine/params/*.md leave.

WHY A DELETION-ENABLING DUMP NEEDS A TEST MORE THAN MOST TOOLS. Its output is the ONLY thing
standing between "the prose is redundant" and "the prose is gone". If the capture is incomplete,
nothing notices until someone needs a value that no longer exists anywhere.

The structured-table view is the useful one, but it is NOT what makes deletion safe — a parser I
cannot prove total is not a safety argument. The raw capture is, and `test_capture_is_lossless`
is the assertion that carries the whole weight.
"""
import os
import subprocess
import sys

import pytest
import yaml

HERE = os.path.dirname(__file__)
ROOT = os.path.join(HERE, '..', '..')
DUMP = os.path.join(ROOT, 'engine', 'engine_params', 'params_tables.yaml')


@pytest.fixture(scope='module')
def doc():
    with open(DUMP, encoding='utf-8') as fh:
        return yaml.safe_load(fh)


def _source_files():
    import glob
    return sorted(
        os.path.relpath(p, ROOT).replace(os.sep, '/')
        for p in glob.glob(os.path.join(ROOT, 'engine', 'params', '**', '*.md'), recursive=True))


def test_capture_is_lossless(doc):
    """EVERY source file present, and byte-identical. This is the deletion's safety argument.

    Not "most files" and not "the tables" — every byte. A structural parser can silently drop a
    cell caveat or a whole file it does not recognise (six files yield no table at all), and the
    loss would only surface when someone needed the value.
    """
    src = _source_files()
    assert src, 'no engine/params/*.md found — this guard has gone blind'
    missing = [f for f in src if f not in doc['raw']]
    assert not missing, f'{len(missing)} params file(s) absent from the dump: {missing[:5]}'
    mismatched = []
    for f in src:
        with open(os.path.join(ROOT, f), encoding='utf-8', errors='ignore') as fh:
            if fh.read() != doc['raw'][f]:
                mismatched.append(f)
    assert not mismatched, f'{len(mismatched)} file(s) not byte-identical: {mismatched[:5]}'


def test_round_trip_check_passes():
    r = subprocess.run([sys.executable, 'tools/export_params_constants.py', '--check'],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, f'params dump drifted:\n{r.stdout}\n{r.stderr}'


def test_the_losslessness_guard_can_fail(doc, tmp_path):
    """POSITIVE CONTROL: drop one file from the capture and the assertion must notice.

    Without this, `test_capture_is_lossless` could be passing because `doc['raw']` is a superset
    of everything, or because the comparison is vacuous. Mutating a copy keeps the tree untouched.
    """
    src = _source_files()
    victim = src[0]
    holed = dict(doc['raw'])
    holed.pop(victim)
    missing = [f for f in src if f not in holed]
    assert missing == [victim], 'the completeness check cannot observe a dropped file'


def test_tables_were_actually_parsed(doc):
    """The structured view is a convenience, but an empty one would mean the parser broke."""
    assert doc['table_count'] > 100, f"only {doc['table_count']} tables parsed — parser regression?"
    assert doc['row_count'] > 1000, f"only {doc['row_count']} rows parsed — parser regression?"
