"""The claim-provenance gate must read every field a claim or its instrument can live in (ED-IN-0122).

WHY. `ci_claim_provenance_check` enforces ED-PC-0040: a ledger entry stating measured numbers must
name the instrument that produced them. It built its scan blob from `("description", "provenance")`
only — so **the field literally named `measured_by` was invisible to the gate that demands an
instrument.**

That is a two-sided defect, and only one side was visible:

  * The loud side: ED-IN-0122's own entry put its `MEASURED-BY:` marker in `measured_by` and the
    gate failed it as "names no instrument." The commit that fixed CI moved the marker into
    `description` — which unblocked the build while leaving the cause in place.
  * The silent side, which is the dangerous one: an entry whose *numbers* live in `measured_by` was
    never scanned for claims at all, so it could never be asked for an instrument. A gate that
    cannot see a field cannot fail on it, and a rule nothing can fail on is not enforced.

MEASURED before widening (CLAUDE.md §0.1 point 4 — a number without a control is not a measurement,
and §8's warning that a blocking-gate reader change needs its own expected-delta test, not a
drop-in): scope **23 → 25** entries, violations **0 → 0**, NEW violations **0**. The widen imports
no backlog, which is why it lands green rather than opening one.

This file is the falsifier (§0.1 point 3). Narrowing the blob back to two fields fails
`test_measured_by_is_in_scope`; the planted-fixture cases assert the gate can still observe the
failure it excludes, in both directions.
"""
import sys
import os

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

cpc = pytest.importorskip('ci_claim_provenance_check')

# Every field that can carry either a quantitative claim or its MEASURED-BY marker. Adding a field
# to the entry schema means adding it here — that is the intended maintenance cost, and it is the
# whole point: the roster is explicit so an unread field is a visible omission rather than a
# silent one.
REQUIRED_FIELDS = ('description', 'provenance', 'measured_by')


def _blob_fields():
    """The field tuple the gate actually scans, read from source rather than re-declared.

    Re-declaring it here would make this test pass while the gate reads something else — the exact
    class of "assertion that cannot observe the failure it excludes" this module exists to close.
    """
    src = open(os.path.join(ROOT, 'tools', 'ci_claim_provenance_check.py'), encoding='utf-8').read()
    marker = 'for k in ('
    idx = src.index(marker, src.index('blob = '))
    return {tok.strip().strip('"\'') for tok in src[idx + len(marker):src.index(')', idx)].split(',')
            if tok.strip()}


@pytest.mark.parametrize('field', REQUIRED_FIELDS)
def test_measured_by_is_in_scope(field):
    fields = _blob_fields()
    assert field in fields, (
        f"the claim-provenance gate does not scan {field!r} (it scans {sorted(fields)}).\n"
        f"A field the gate cannot read is a field the gate cannot enforce: an entry whose numbers "
        f"live there is never scanned for claims, and an entry whose MEASURED-BY marker lives "
        f"there is failed for having no instrument. Both happened (ED-IN-0122).")


def test_a_claim_in_measured_by_is_now_observable():
    """Planted fixture, silent side: numbers in `measured_by`, no marker anywhere → must violate."""
    entry = {'id': 'ED-IN-9999', 'description': 'a change.',
             'measured_by': 'coverage went from 12 -> 40 files'}
    blob = ' '.join(str(entry.get(k, '')) for k in _blob_fields())
    claims = [why for pat, why in cpc.CLAIM_PATTERNS if pat.search(blob)]
    assert claims, 'a measured transition in measured_by must register as a quantitative claim'
    assert not cpc.MARKER.findall(blob), 'fixture must carry no instrument'


def test_an_instrument_in_measured_by_now_satisfies_the_gate():
    """Planted fixture, loud side: claim in `description`, marker in `measured_by` → must pass.

    This is the shape the gate rejected on ED-IN-0122 and the reason the marker was relocated. With
    the blob widened, the semantically correct placement is accepted and the relocation becomes
    unnecessary rather than mandatory.
    """
    entry = {'id': 'ED-IN-9999', 'description': 'files went from 1 -> 11.',
             'measured_by': 'MEASURED-BY: tests/valoria/test_tool_input_paths_resolve.py'}
    blob = ' '.join(str(entry.get(k, '')) for k in _blob_fields())
    assert [why for pat, why in cpc.CLAIM_PATTERNS if pat.search(blob)], 'fixture must make a claim'
    found = cpc.MARKER.findall(blob)
    assert found, 'an instrument named in measured_by must satisfy the gate'
    assert os.path.exists(os.path.join(ROOT, found[0])), 'and the instrument must exist in the tree'


def test_the_live_ledgers_still_pass():
    """Guards against importing a backlog: the measured delta was 0 new violations, and it stays 0.

    If this goes red, the widen has surfaced real pre-existing debt — which is a finding to triage,
    not a reason to narrow the blob back.
    """
    # check() returns an int exit code: 0 == clean, 1 == violations. Asserting against a tuple of
    # plausible truthy values (as the first draft of this line did) would have passed on `True` or
    # `None` — values the function never returns — making the assertion unable to observe the
    # failure it excludes. §0.1 point 2, caught in review of this very file.
    assert cpc.check() == 0, 'live ledgers now violate the widened gate — triage the debt, do not narrow the blob'
