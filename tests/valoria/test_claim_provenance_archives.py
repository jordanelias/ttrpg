"""`ci_claim_provenance_check` must not lose an entry when it is archived (ED-IN-0165).

THE DEFECT THIS GUARDS. The gate's `LEDGERS` dict named only the two LIVE lane
files. Archiving a settled id to its `_archive.jsonl` sibling therefore removed
every measured number in that entry from the gate's scope — permanently, silently,
and while the gate went on reporting OK.

That matters because archiving is not rare. The IN ledger's 50,000-token cap is
hit routinely — four times in three commits across two sessions — so "archive the
oldest settled ids" is the standard remedy, and each application quietly shrank
the population of claims anyone was checking.

It was found by an adversarial pass on the branch that caused it: archiving
ED-IN-0160/0161 to get back under the cap moved that branch's OWN headline
measurements out of scope, and the gate's count fell 23 -> 22 between origin/main
and HEAD while still reporting green. A gate that examines fewer items and still
says OK is this repository's signature defect class (00_code_leanness.md §1.6,
ED-IN-0149) — here inside the gate that exists to stop claims going unverified.

The fix was free: 22 -> 47 entries in scope, and the gate stays green, because all
25 recovered entries already named an instrument. Nobody had claimed the coverage.
"""
import importlib.util
import json
import os
import re
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, 'tools', 'ci_claim_provenance_check.py')


def _load_provenance_gate():
    # Named for what it loads, not `_gate` — `test_ledger_hygiene.py` already
    # defines a `_gate` and the duplicated-helper ratchet in
    # `test_test_register.py` correctly went red on the collision. Renaming is the
    # fix; raising the baseline would have been the defect the ratchet exists for.
    spec = importlib.util.spec_from_file_location('cpc', GATE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['cpc'] = mod
    spec.loader.exec_module(mod)
    return mod


def test_every_live_ledger_has_its_archive_sibling_in_scope():
    """THE GUARD. For each live ledger under the rule, if an archive sibling
    exists on disk it must also be in `LEDGERS`, at the same cutover id.

    Stated as a derivation rather than as a literal list, so a lane added to the
    rule later inherits the requirement instead of quietly reopening the hole.
    """
    gate = _load_provenance_gate()
    missing = []
    for path, cutover in list(gate.LEDGERS.items()):
        if path.endswith('_archive.jsonl'):
            continue
        sibling = path.replace('.jsonl', '_archive.jsonl')
        if not os.path.isfile(os.path.join(ROOT, sibling)):
            continue                      # no archive yet — nothing to lose
        if sibling not in gate.LEDGERS:
            missing.append(sibling)
        elif gate.LEDGERS[sibling] != cutover:
            missing.append(f'{sibling} (cutover {gate.LEDGERS[sibling]} != {cutover})')
    assert not missing, (
        'archiving an entry would drop its measured claims out of this gate: '
        f'{missing}')


def test_the_archives_actually_carry_entries_in_scope():
    """Non-vacuity. The test above passes trivially if the archives are empty or
    predate every cutover — in which case adding them proved nothing. Require that
    the archive contributes real in-scope entries."""
    gate = _load_provenance_gate()
    contributed = 0
    for path, cutover in gate.LEDGERS.items():
        if not path.endswith('_archive.jsonl'):
            continue
        lane, floor = cutover.rsplit('-', 1)
        full = os.path.join(ROOT, path)
        if not os.path.isfile(full):
            continue
        for line in open(full, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            m = re.match(r'(ED-[A-Z]+)-(\d+)$', row.get('id', ''))
            if m and m.group(1) == lane and int(m.group(2)) >= int(floor):
                contributed += 1
    assert contributed >= 20, (
        f'archives contribute only {contributed} in-scope entries — either the '
        'measurement that justified this change was wrong, or the archives moved')


def test_this_branchs_own_archived_entries_are_back_in_scope():
    """The specific regression, named.

    ED-IN-0160 and ED-IN-0161 carry this programme's headline measurements
    (`ci_common` adoption 11/118 -> 60/118, the Status-reader delta) and were
    archived to get under the size cap. If they are not in scope, the numbers this
    branch published are unverified by the gate built to verify exactly that.
    """
    gate = _load_provenance_gate()
    archive = os.path.join(ROOT, 'registers', 'editorial_ledger_in_archive.jsonl')
    ids = set()
    for line in open(archive, encoding='utf-8'):
        line = line.strip()
        if line:
            try:
                ids.add(json.loads(line)['id'])
            except (json.JSONDecodeError, KeyError):
                pass
    for probe in ('ED-IN-0160', 'ED-IN-0161'):
        assert probe in ids, f'{probe} is not in the archive — this test is checking nothing'
    assert 'registers/editorial_ledger_in_archive.jsonl' in gate.LEDGERS


def test_gate_is_green_with_the_archives_in_scope():
    """The change is only safe because the recovered entries already comply. If a
    future archived entry lacks its instrument, THIS fails — which is the gate
    doing its job rather than a reason to narrow it again."""
    import subprocess
    r = subprocess.run([sys.executable, GATE], cwd=ROOT,
                       capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-2000:]
    m = re.search(r'\[claim-provenance\]\s+(\d+)\s+quantitative', r.stdout)
    assert m, r.stdout[:500]
    assert int(m.group(1)) >= 40, (
        f'scope fell to {m.group(1)} entries — it was 47 when the archives were '
        'brought in, and 22 before. A drop means coverage was lost again.')
