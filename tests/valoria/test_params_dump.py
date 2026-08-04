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
    """Every file under engine/params/, walked — NOT globbed for `*.md`.

    The gate review's F2: the evacuation rule matches the whole tree while the capture matched
    `**/*.md`, and this helper used the same `.md` filter — so guard and capture shared a blind
    spot and a non-markdown (or hidden) file would evacuate uncaptured with nothing going red.
    Walking makes the test's notion of "the source" the same as the DELETION's notion of it.
    """
    root = os.path.join(ROOT, 'engine', 'params')
    out = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            out.append(os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/'))
    return sorted(out)


def _source_bytes(rel):
    with open(os.path.join(ROOT, rel), 'rb') as fh:
        return fh.read()


def test_capture_is_lossless(doc):
    """EVERY source file present, and byte-identical. This is the deletion's safety argument.

    Not "most files" and not "the tables" — every byte. A structural parser can silently drop a
    cell caveat or a whole file it does not recognise (six files yield no table at all), and the
    loss would only surface when someone needed the value.

    COMPARED AS BYTES, and that is the point (gate review F1). This assertion used to read the
    source in text mode with `errors='ignore'` — the same lossy read the exporter used — so a CRLF
    line or an undecodable byte would be normalised or dropped identically on both sides and the
    pair would agree with each other while diverging from the file. Two lossy reads that match are
    not evidence of losslessness. Encoding the captured text back to UTF-8 and comparing raw bytes
    is: it can observe the failure it excludes.
    """
    src = _source_files()
    assert src, 'nothing under engine/params/ — this guard has gone blind'
    missing = [f for f in src if f not in doc['raw']]
    assert not missing, f'{len(missing)} params file(s) absent from the dump: {missing[:5]}'
    mismatched = [f for f in src if _source_bytes(f) != doc['raw'][f].encode('utf-8')]
    assert not mismatched, f'{len(mismatched)} file(s) not byte-identical: {mismatched[:5]}'


def test_round_trip_check_passes():
    r = subprocess.run([sys.executable, 'tools/export_params_constants.py', '--check'],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, f'params dump drifted:\n{r.stdout}\n{r.stderr}'


def test_the_completeness_guard_can_fail(doc):
    """POSITIVE CONTROL for the COMPLETENESS branch: drop one file, the assertion must notice.

    Without this, `test_capture_is_lossless` could be passing because `doc['raw']` is a superset
    of everything, or because the comparison is vacuous. Mutating a copy keeps the tree untouched.
    """
    src = _source_files()
    victim = src[0]
    holed = dict(doc['raw'])
    holed.pop(victim)
    missing = [f for f in src if f not in holed]
    assert missing == [victim], 'the completeness check cannot observe a dropped file'


@pytest.mark.parametrize('mutate,label', [
    (lambda s: s.replace('|', '¦', 1), 'one cell delimiter'),
    (lambda s: s + '\n', 'one trailing newline'),
    (lambda s: s.replace('\n', '\r\n', 1), 'one LF -> CRLF'),
    (lambda s: s.replace('5', '6', 1), 'one digit'),
])
def test_the_byte_comparison_can_fail(doc, mutate, label):
    """POSITIVE CONTROL for the BYTE branch — the one the completeness control never touched.

    The gate review's F3: the only control planted an OMISSION, so the byte comparison — the
    branch carrying the word "byte-identical" — had no falsifier at all, and the ledger described
    the control as planting "a mismatch", which it did not. These four mutations are the failure
    modes that actually threaten the claim: a mangled table delimiter, a stripped/added trailing
    newline, a newline translation (the exact F1 hazard), and a changed digit — a wrong NUMBER
    surviving into the fork being the outcome this whole capture exists to prevent.
    """
    src = _source_files()
    victim = src[0]
    mutated = mutate(doc['raw'][victim])
    assert mutated != doc['raw'][victim], f'the {label} mutation was a no-op — control is vacuous'
    assert _source_bytes(victim) != mutated.encode('utf-8'), \
        f'the byte comparison cannot observe a changed {label}'


def test_a_non_markdown_file_would_not_evacuate_uncaptured():
    """The capture's glob must cover the whole tree the evacuation rule deletes (F2).

    `R-PARAMS-DUMPED` matches `engine/params/**`; the exporter globs `**/*.md`. If those ever
    disagree, a file is deleted that nothing captured. The exporter now refuses to write in that
    case — this asserts the two scopes are equal in the tree as it stands, so the refusal is a
    guard rather than a permanent tripwire.
    """
    import glob
    globbed = {os.path.relpath(p, ROOT).replace(os.sep, '/')
               for p in glob.glob(os.path.join(ROOT, 'engine', 'params', '**', '*.md'),
                                  recursive=True)}
    walked = set(_source_files())
    assert walked - globbed == set(), (
        f'{len(walked - globbed)} file(s) under engine/params/ are outside the capture glob and '
        f'would evacuate uncaptured: {sorted(walked - globbed)[:5]}')


def test_tables_were_actually_parsed(doc):
    """The structured view is a convenience, but an empty one would mean the parser broke."""
    assert doc['table_count'] > 100, f"only {doc['table_count']} tables parsed — parser regression?"
    assert doc['row_count'] > 1000, f"only {doc['row_count']} rows parsed — parser regression?"
