#!/usr/bin/env python3
"""Every generated artifact that can go stale must have something that un-stales it (ED-IN-0180).

THE DEFECT THIS EXISTS FOR. `tools/audit_staleness.py` reported six families stale and could not
say which of them anything would ever fix — it had no field for that. Five were refreshed by the
weekly `audit-refresh` cron. **`mechanics-index` was refreshed by nothing.** Its generator was
wired into CI as `--strict`, which only VALIDATES and is warn-only, so the drift was reported on
every run and acted on by no one; it reached 32 files behind before the two facts were joined by
hand.

That is the ED-IN-0159 §1.6 shape one level up: not dead scope, but a live signal with no consumer.
A staleness report nobody is obliged to answer is decoration.

THE JOIN. Each family now declares a `refresher`; this test checks that script is actually run by
`.github/workflows/audit-refresh.yml`. It is the same both-directions join
`broken_dependency_checker` already performs between `ci_checks_registry.yaml` and the CI workflow,
applied to the refresh cron instead — a declaration on one side and an invocation on the other,
neither trusted alone.
"""
from __future__ import annotations

import os
import re
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import audit_staleness as ast_mod  # noqa: E402

WORKFLOW = os.path.join(ROOT, '.github', 'workflows', 'audit-refresh.yml')


@pytest.fixture(scope='module')
def workflow_text():
    assert os.path.exists(WORKFLOW), f'{WORKFLOW} is gone — nothing refreshes anything'
    return open(WORKFLOW, encoding='utf-8').read()


def test_every_family_declares_a_refresher():
    """A family with no `refresher` key is the state that hid mechanics-index. `None` is a valid
    answer — a deliberately frozen artifact — but it has to be said out loud."""
    for fam in ast_mod.FAMILIES:
        assert 'refresher' in fam, (
            f"family {fam['name']!r} declares no `refresher`. Name the script that regenerates it, "
            f"or None if it is deliberately frozen. Silence is how mechanics-index drifted.")


def test_every_declared_refresher_exists_on_disk():
    for fam in ast_mod.FAMILIES:
        gen = fam.get('refresher')
        if gen is None:
            continue
        assert os.path.exists(os.path.join(ROOT, gen)), (
            f"family {fam['name']!r} names refresher {gen}, which is not in the tree")


def test_every_refreshable_family_is_actually_run_by_the_cron(workflow_text):
    """THE REGRESSION. Declaring a refresher the cron never invokes is the same blind spot with
    extra paperwork."""
    missing = []
    for fam in ast_mod.FAMILIES:
        gen = fam.get('refresher')
        if gen is None:
            continue
        if gen not in workflow_text:
            missing.append((fam['name'], gen))
    assert not missing, (
        'family/families declare a refresher that .github/workflows/audit-refresh.yml never runs:\n  '
        + '\n  '.join(f'{n} -> {g}' for n, g in missing)
        + '\n\nAdd the step to the cron, or set refresher=None and say why it is frozen.')


def test_the_join_is_not_vacuous(workflow_text):
    """Assert that it asserted — a workflow that ran nothing would pass the test above trivially
    only if every family were frozen, so pin that the cron really does invoke generators."""
    invoked = set(re.findall(r'python3 ([\w/.\-]+\.py)', workflow_text))
    assert len(invoked) >= 5, (
        f'audit-refresh.yml invokes only {len(invoked)} generator(s): {sorted(invoked)}. '
        f'The cron was gutted, or the parse broke.')
    declared = {f.get('refresher') for f in ast_mod.FAMILIES if f.get('refresher')}
    assert declared & invoked, 'no declared refresher matches anything the cron runs'


def test_mechanics_index_specifically_is_covered(workflow_text):
    """The one that was missing. Named explicitly so a future edit that drops it fails loudly
    rather than reverting to the reported-but-never-fixed state."""
    fam = next(f for f in ast_mod.FAMILIES if f['name'] == 'mechanics-index')
    assert fam.get('refresher') == 'tools/mechanics_index_gen.py'
    assert 'tools/mechanics_index_gen.py --update' in workflow_text, (
        'the mechanics index is back to being validated but never regenerated. `--strict` in '
        'valoria-ci.yml only REPORTS drift; `--update` in audit-refresh.yml is what fixes it.')


def test_a_frozen_family_is_allowed_but_must_be_explicit():
    """npc-audit points at a frozen historical artifact. The rule is that it says so."""
    frozen = [f['name'] for f in ast_mod.FAMILIES if f.get('refresher') is None]
    assert frozen, 'expected at least one deliberately-frozen family (npc-audit)'
    for name in frozen:
        assert name == 'npc-audit', (
            f'{name} declares no refresher. If it is genuinely frozen say so here; if it just '
            f'lacks one, that is the mechanics-index defect recurring.')
