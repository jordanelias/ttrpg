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

⚠ AND THE OBVIOUS FIX WAS DESTRUCTIVE, which is the second half and the more useful one
(ED-IN-0181). I wired that generator's `--update` into the cron and ran it. It reported success.
It also round-tripped the whole register through a YAML loader/dumper and stripped **39 comment
lines to 0, losing 5,081 characters** of section headers and repointing rationale — while its own
`--help` calls the flag "Write drift_report back into mechanics_index.yaml". Reverted; the cron
step was added in 04e0289 and removed in the next commit, before it ever ran; the family now
declares NO refresher, with the
reason recorded at the declaration.

The lesson generalises past this tool: **a `--update` flag's description is not its effect.**
Before scheduling any generator, run it once and diff for what it removed, not only for what it
wrote. A weekly unattended write is the worst possible place to discover the difference.

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


# NAMED FOR THE FILE IT READS, not `workflow_text` (ED-IN-0181). That name already exists in
# tests/valoria/test_compile_is_not_invocation.py where it holds valoria-ci.yml — a DIFFERENT
# file. Two fixtures, one name, two meanings is the same defect this session spent the day on,
# at fixture scope; the duplicate-helper gate caught it, and the fix is to say which workflow,
# not to share a helper that was never shared logic.
@pytest.fixture(scope='module')
def audit_refresh_yaml():
    assert os.path.exists(WORKFLOW), f'{WORKFLOW} is gone — nothing refreshes anything'
    return open(WORKFLOW, encoding='utf-8').read()


def test_every_family_declares_a_refresher():
    """A family with no `refresher` key is the state that hid mechanics-index. `None` is a valid
    answer, but it must be paired with `no_refresher_because` — see the test below; None alone
    once meant two different dispositions."""
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


def test_every_refreshable_family_is_actually_run_by_the_cron(audit_refresh_yaml):
    """THE REGRESSION. Declaring a refresher the cron never invokes is the same blind spot with
    extra paperwork."""
    missing = []
    for fam in ast_mod.FAMILIES:
        gen = fam.get('refresher')
        if gen is None:
            continue
        if gen not in audit_refresh_yaml:
            missing.append((fam['name'], gen))
    assert not missing, (
        'family/families declare a refresher that .github/workflows/audit-refresh.yml never runs:\n  '
        + '\n  '.join(f'{n} -> {g}' for n, g in missing)
        + '\n\nAdd the step to the cron, or set refresher=None WITH a no_refresher_because reason.')


def test_every_refreshed_artifact_is_actually_committed(audit_refresh_yaml):
    """RUNNING A GENERATOR IS NOT REFRESHING AN ARTIFACT (ED-IN-0182).

    The test above checks the cron INVOKES the generator. That is one level short of the failure
    it was built after, and the gap was live: `build_glossary.py` was added to the cron while
    `references/glossary/` appeared in neither the diff-check nor the `git add` list, so the job
    regenerated the glossary inside the runner and discarded it. The job would have reported
    success and the coverage guard would have reported the family covered, over a family that was
    still only fresh by luck — a green light over the exact condition it was written to detect.

    So the join has two legs now: the generator is invoked, AND its output is committed.
    """
    add_lines = [ln for ln in audit_refresh_yaml.splitlines() if ln.strip().startswith('git add ')]
    assert add_lines, 'no `git add` line in audit-refresh.yml — nothing it generates is committed'
    staged = ' '.join(add_lines)

    orphaned = []
    for fam in ast_mod.FAMILIES:
        if fam.get('refresher') is None:
            continue
        for artifact in fam.get('artifact_paths', ()):
            # a directory entry in `git add` covers everything beneath it
            covered = artifact in staged or any(
                artifact.startswith(tok) for tok in staged.split() if tok.endswith('/'))
            if not covered:
                orphaned.append((fam['name'], artifact))
    assert not orphaned, (
        'the cron regenerates these artifacts and never commits them:\n  '
        + '\n  '.join(f'{n} -> {a}' for n, a in orphaned)
        + '\n\nAdd the path to BOTH the diff-check and the `git add` list in audit-refresh.yml. '
          'A generator that runs and whose output is discarded is worse than one that never ran: '
          'the job goes green and the coverage guard reports the family covered.')


def test_the_join_is_not_vacuous(audit_refresh_yaml):
    """Assert that it asserted — a workflow that ran nothing would pass the test above trivially
    only if every family were frozen, so pin that the cron really does invoke generators."""
    invoked = set(re.findall(r'python3 ([\w/.\-]+\.py)', audit_refresh_yaml))
    assert len(invoked) >= 5, (
        f'audit-refresh.yml invokes only {len(invoked)} generator(s): {sorted(invoked)}. '
        f'The cron was gutted, or the parse broke.')
    declared = {f.get('refresher') for f in ast_mod.FAMILIES if f.get('refresher')}
    assert declared & invoked, 'no declared refresher matches anything the cron runs'


def test_mechanics_index_is_NOT_wired_because_its_generator_is_destructive(audit_refresh_yaml):
    """The inverse of what this test asserted an hour ago, and the inversion is the finding.

    I wired `mechanics_index_gen.py --update` into the cron, ran it, and it looked fine: the tool
    printed `[OK] Wrote drift_report back` and the diff was large but plausible for a register 32
    files behind. It was not fine. `--update` documents itself as writing the drift report back;
    it actually round-trips the entire YAML through a loader/dumper and **silently strips every
    comment** — measured on the real file, **39 comment lines to 0 and 5,081 characters gone**,
    including the section headers and the inline notes recording why individual paths were
    repointed.

    Scheduling that weekly would have deleted hand-written prose unattended, in a PR nobody reads
    closely because "it is just a regeneration". Reverted in the commit after the one that added it, before the cron ever fired.

    So the honest state is: mechanics-index has NO refresher, keeps reporting stale, and the fix is
    a code change making the generator comment-preserving — not a cron line. This test pins that,
    so nobody re-wires it from the tempting half of the story.
    """
    fam = next(f for f in ast_mod.FAMILIES if f['name'] == 'mechanics-index')
    assert fam.get('refresher') is None, (
        'mechanics-index declares a refresher again. If mechanics_index_gen.py was made '
        'comment-preserving, prove it first — regenerate and assert the comment count is '
        'unchanged — then wire it and update this test.')
    # Match a `run:` LINE, not the substring. The first version of this assertion checked
    # `'--update' not in audit_refresh_yaml` and failed on the workflow's own comment EXPLAINING why
    # --update is absent — prose about a thing counted as the thing, at small scale, in a test
    # written minutes after recording that exact class twice (ED-IN-0180's grep-vs-AST and the
    # HANDOFF_IN "ED-WR-0010 NOT allocated" false positive). It is a persistent reflex, not a
    # one-off, which is why it is written down here rather than quietly fixed.
    runs = [ln for ln in audit_refresh_yaml.splitlines() if ln.strip().startswith('run:')]
    offenders = [ln.strip() for ln in runs if 'mechanics_index_gen' in ln]
    assert not offenders, (
        f'a mechanics_index_gen invocation is back in audit-refresh.yml: {offenders}. '
        f'Its --update flag strips every comment from the register it writes (ED-IN-0181).')


def test_a_family_without_a_refresher_must_say_why():
    """`refresher: None` means "nothing regenerates this" and NOTHING MORE (ED-IN-0182).

    An earlier version of this file treated None as "frozen historical artifact" and put both
    None-families in one set called `frozen` — while one of them was not frozen at all, it was
    blocked by a defect. One word carrying two dispositions, inside the session that ruled
    vocabulary must be idempotent (ED-IN-0179). The reason is now an explicit field.
    """
    for fam in ast_mod.FAMILIES:
        if fam.get('refresher') is not None:
            continue
        reason = fam.get('no_refresher_because')
        assert reason, (
            f"family {fam['name']!r} has no refresher and no `no_refresher_because`. Say which it "
            f"is — 'frozen' (nothing should regenerate it) or 'blocked-by-defect' (something "
            f"should, and cannot yet). A bare None hides the difference.")


def test_every_family_points_at_a_live_artifact():
    """THE CHECK THAT WOULD HAVE CAUGHT npc-audit, and it had rotted twice before anyone did.

    That family's artifact was `audit/lane-a/…`, which left main in the 2026-08-05 evacuation
    (`restructure_ledger.md:1319` carries `audit/lane-a/` as `FORK:c451bcb`). The family reported
    "(no data)" silently — and its own comment recorded an EARLIER repointing after exactly the
    same failure, from the retired `designs/audit/` tree. It was repointed onto a path that was
    itself evacuated two weeks later.

    A staleness row whose subject has left the tree degrades to silence rather than to an error,
    so it cannot announce its own death. This is the announcement.
    """
    dead = []
    for fam in ast_mod.FAMILIES:
        for artifact in fam.get('artifact_paths', ()):
            base = artifact.split('*')[0]
            if not os.path.exists(os.path.join(ROOT, base)):
                dead.append((fam['name'], artifact))
    assert not dead, (
        'family/families name an artifact that is not in the tree:\n  '
        + '\n  '.join(f'{n} -> {a}' for n, a in dead)
        + '\n\nIf its subject was retired, RETIRE THE FAMILY — do not repoint it at a third path. '
          'If the artifact merely moved, repoint it and say so.')
