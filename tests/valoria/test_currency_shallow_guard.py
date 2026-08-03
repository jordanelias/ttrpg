"""The CURRENT.md stamp check must not invert under a depth-1 checkout (ED-IN-0123).

WHY. `currency_consistency_check.check_current_stamp` compares CURRENT.md's reconcile stamp against
`git log -1 --format=%cs -- <each canonical head>`. That is sound with history and **meaningless
without it**: at `actions/checkout`'s default depth of 1 there is exactly ONE commit, so every path
returns HEAD's date and EVERY canonical head falsely reads as touched today.

MEASURED: the `currency.stamps` signal went RED in the `compliance-check` job — the only job running
`review_core --check` and the only one of the three that did not set `fetch-depth: 0` — while the
identical command passed locally on full history. It surfaced the moment a commit landed more than
one day after the stamp, i.e. once the grace window closed. Before that the false drift was masked
by the grace day, which is why a latent CI-config bug looked like a sudden content regression.

WHAT THIS FILE DELIBERATELY DOES *NOT* TEST. A fourth test pinned `fetch-depth: 0` in the workflow
YAML. It was DELETED, for two reasons worth recording. First, it could not fail: the assertion
`'fetch-depth: 0' in block` matched the explanatory COMMENT above the directive, so mutating the
directive to `fetch-depth: 1` left it green — the same assert-cannot-observe-its-own-failure defect
this suite exists to catch, committed inside the guard written to catch it. Second, and the reason
it was not simply repaired: a test guarding a YAML line, guarding a tool, guarding a date stamp, in
an index of prose the fork plan puts on its do-not-read list, is four levels of indirection from
anything that executes. The ratio stopped making sense before the bug did. The workflow comment at
the `fetch-depth` line carries the reason it must stay; that is the right weight for this.

TWO FIXES, because either alone is insufficient:
  * `.github/workflows/valoria-ci.yml` now sets `fetch-depth: 0` on `compliance-check` — the real
    repair, restoring the check's inputs.
  * `_history_is_unusable()` degrades honestly if it ever runs shallow again — it reports "cannot
    measure" instead of emitting a page of fabricated drift (§0.1 point 4: a number without a
    control is not a measurement, and neither is a date).

THE DISCRIMINATOR IS COMMIT COUNT, NOT SHALLOWNESS, and the first version got that wrong. It asked
`git rev-parse --is-shallow-repository`, which returns `true` for ANY depth-limited clone. Measured
on the authoring container: shallow=true, **76 commits**, per-path dates working correctly. That
guard would have silently disabled a working check on every machine cloning with `--depth 50` —
trading a false-positive gate for an absent one, which is the worse trade. Only at depth 1 do the
dates carry no information, and that is what is detected.
"""
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

ccc = pytest.importorskip('currency_consistency_check')


def test_guard_does_not_fire_on_a_real_checkout():
    """The live tree has history, so the check must RUN — not skip.

    This is the assertion that would have caught the first version: it fires on any depth-limited
    clone, and this repository's own checkout is one.
    """
    assert not ccc._history_is_unusable(), (
        'the stamp check believes this checkout has no usable history and is skipping itself. '
        f'`git rev-list --count HEAD` reports '
        f'{subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()} '
        f'commits — the discriminator must be commit COUNT, not `--is-shallow-repository`.')


def test_per_path_dates_actually_differ_here():
    """Guards the guard: proves history is usable by observing two paths with different dates.

    If every path returned the same date this test would pass vacuously on a broken checkout while
    `test_guard_does_not_fire_on_a_real_checkout` also passed — so it asserts the *observable*
    property the stamp check depends on, not merely the flag that predicts it.
    """
    head = ccc._git_last_commit_date('.')
    older = [p for p in ('systems/', 'canon/', 'references/', 'engine/')
             if ccc._git_last_commit_date(p) and ccc._git_last_commit_date(p) != head]
    assert older, (
        f'every sampled path reports the same commit date as HEAD ({head!r}), which is the '
        f'signature of a depth-1 checkout. The stamp check cannot distinguish a touched head from '
        f'an untouched one here.')


def test_depth_one_clone_reports_cannot_measure_not_drift():
    """The falsifier. In a genuine depth-1 clone the check must say it cannot measure.

    Builds a real depth-1 clone and copies in the WORKING-TREE tool — cloning alone would test the
    committed version, which is how an earlier run of this same check produced a misleading result.
    """
    import shutil
    import tempfile
    if ccc._history_is_unusable():
        pytest.skip('authoring checkout is already depth-1; the positive case cannot be built here')
    with tempfile.TemporaryDirectory() as tmp:
        dst = os.path.join(tmp, 's')
        r = subprocess.run(['git', 'clone', '--depth', '1', '--quiet', f'file://{ROOT}', dst],
                           capture_output=True, text=True)
        if r.returncode != 0:
            pytest.skip(f'could not build a depth-1 clone here: {r.stderr.strip()[:120]}')
        shutil.copy(os.path.join(ROOT, 'tools', 'currency_consistency_check.py'),
                    os.path.join(dst, 'tools', 'currency_consistency_check.py'))
        assert subprocess.run(['git', 'rev-list', '--count', 'HEAD'], cwd=dst,
                              capture_output=True, text=True).stdout.strip() == '1'
        out = subprocess.run([sys.executable, 'tools/currency_consistency_check.py'],
                             cwd=dst, capture_output=True, text=True)
        combined = out.stdout + out.stderr
        assert 'SKIPPED' in combined and 'depth-1' in combined, (
            f'a depth-1 checkout must report that it cannot measure. Got:\n{combined[-400:]}')
        assert 'predates head' not in combined, (
            'a depth-1 checkout emitted per-head drift — the fabricated-drift failure this guard '
            f'exists to prevent:\n{combined[-400:]}')
