"""Pytest configuration for `tests/valoria` — the KNOWN-RED register (W1, ED-MB-0061).

WHY THIS EXISTS, and why it is a register rather than nine decorators.

`pytest tests/valoria` is the repo's SHIPPING gate (CLAUDE.md §0.1). Since the mass-battle
flags-ON commit it has been red on nine tests, and ED-MB-0061 records the specific defect: the
merge that turned `main` red left the failure set **unrecorded**, so *"no other lane could
distinguish a new regression from the known set"*. That is the whole cost of a red gate — not the
nine failures, which are understood and owned by the MB lane, but the tenth failure nobody
notices because it arrives into a list everyone has learned to scroll past.

This branch hit exactly that: three commits landed while CI reported nine failures, and each time
the only way to know none of them was mine was to re-run the suite against `origin/main` in a
detached worktree and diff the lists by hand. A gate that requires a manual differential to read
is not a gate.

**Marked `strict=True` deliberately.** A non-strict xfail would silently absorb a FIX as well as a
failure, so the MB lane would get no signal when its work lands. Strict means: these must fail;
if one starts passing, the suite goes red and this register must be updated in the same commit
that fixed it. The register is therefore self-retiring — it cannot rot in the passing direction.

**It cannot rot in the other direction either**: `test_known_red_register.py` asserts every id
below was actually collected, so a renamed or deleted test fails loudly rather than leaving a
stale entry that quietly excuses nothing. Without that, this file would be a way to make the
suite green by naming tests that no longer exist.

**This is not MB work.** No mass-battle code, config, golden or threshold is touched by anything
here; the failures stay failures and stay ED-MB-0061's to fix. It is gate hygiene for every OTHER
lane, which is why it lives in `tests/valoria/` rather than in the MB tree.
"""
import pytest

# nodeid (relative to tests/valoria/) -> why it is red.
# SOURCE OF TRUTH for the known-red set. Cited: ED-MB-0061.
KNOWN_RED = {
    'test_conditional_orders.py::test_conditional_withdraw_fires_when_enemy_closes':
        'conditional withdraw does not fire — flags-ON residual (ED-MB-0061 Track F)',
    'test_conditional_orders.py::test_own_strength_fires_when_attrited':
        'own_strength order never advances _order_idx — flags-ON residual (ED-MB-0061 Track F)',
    'test_dg2_yield_residuals.py::test_rally_keeps_pressured_yielding_subunit':
        'rally clears yielding below the rally fraction — DG2 residual (ED-MB-0061)',
    'test_intent_resolution.py::test_holder_survives_better_with_intent':
        'intent-on holder no longer survives better — flags-ON residual (ED-MB-0061)',
    'test_obb_contact_toi.py::test_head_on_no_interpenetration_no_stall':
        'OBB commit permits body interpenetration — geometry spec residual (ED-MB-0061)',
    'test_obb_contact_toi.py::test_cavalry_charge_reaches_contact':
        'charge drives bodies into interpenetration — geometry spec residual (ED-MB-0061)',
    'test_mass_battle_byte_exact.py::test_byte_exact_unit_mode':
        'unit-mode golden digest drifted and has not been re-recorded (ED-MB-0061)',
    'test_mass_battle_byte_exact.py::test_byte_exact_cell_mode':
        'cell-mode golden digest drifted (ED-MB-0061). Note this test ALSO self-skips off the '
        'reference platform, so it reports SKIPPED locally and xfail on CI — a runtime skip wins '
        'over an xfail marker, so strict=True is safe here rather than a latent xpass.',
    'test_stochastic_rout.py::test_per_cell_break_subsumes_the_body_level_one':
        'per-cell and body-level break points have separated again (ED-MB-0061)',
}


def pytest_collection_modifyitems(config, items):
    """Apply the register at collection time. One owner, no scattered decorators."""
    for item in items:
        rel = item.nodeid.split('tests/valoria/')[-1]
        reason = KNOWN_RED.get(rel)
        if reason is not None:
            item.add_marker(pytest.mark.xfail(strict=True, reason=f'KNOWN-RED: {reason}'))


# ─────────────────────────────────────────────────────────────────────────────────────────────
# THE GENERATED LAYER — built on demand, never committed (culling wave 5, ED-IN-0194, 2026-08-22)
# ─────────────────────────────────────────────────────────────────────────────────────────────
# Eleven artifacts under `references/` and `systems/*/_identifier_census.yaml` were UNTRACKED. They
# are built from tracked sources and were never authored, and committing them made every prose edit
# a diff in files no human wrote — adding ONE document to `proposals/` churned three of them and
# turned a blocking gate red.
#
# THIS FIXTURE IS THE SINGLE OWNER OF THE BUILD ORDER, and the order is not cosmetic: two builders
# READ another's output (`build_engine_atlas` and `build_contract_index` both consume
# `references/key_graph.json`), so a test that built only what it names would get a stale or absent
# input depending on execution order. Session-scoped, so the cost is paid once per run.
#
# WHAT REPLACED THE `--check` GATES. Each of these builders had a `--check` mode whose entire job
# was detecting a STALE COMMITTED COPY. With nothing committed there is no staleness to detect, so
# that failure class does not exist any more — it was deleted, not weakened. What the tests assert
# now is the invariant that survives: *the builder runs against the real sources and produces a
# well-formed artifact*. A builder that crashes, or emits something malformed, still fails.
import json as _json
import os as _os
import subprocess as _subprocess
import sys as _sys
import time as _time

import pytest as _pytest

_REPO = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), '..', '..'))

# (builder, [artifacts it produces]) in DEPENDENCY ORDER. FOUR edges make the order load-bearing —
# this comment said "two" until an adversarial pass recounted them (2026-08-22):
#   * `references/key_graph.json` is read by THREE builders — build_contract_index.py:68,
#     build_engine_atlas.py:57, build_execution_map.py:212
#   * `references/execution_trace.json` is read by build_engine_atlas.py:59 and build_execution_map
#   * `references/execution_map.json` is read by build_engine_atlas.py:58
# The order below satisfies all of them; the undercount was in the description, not the tuple. It is
# corrected rather than left, because the next person to add a builder will size the risk from this
# comment.
#
# `trace_execution_phases.py` is the expensive one (~9.5s — it profiles a full seeded campaign) and
# it is FIRST rather than omitted on cost grounds. Omitting it does not fail: both consumers report
# an absent input rather than absorbing it (`test_engine_atlas.py::
# test_missing_input_is_reported_not_silently_absorbed` pins that), so the layer would build green
# with every subsystem reading as "not observed at this seed". That is the false-absence error the
# tracer's own docstring warns about, arrived at by a fixture rather than by a reader — worse than
# the 9.5s, and paid once per session.
_GENERATED_LAYER = (
    ('trace_execution_phases.py',  ['references/execution_trace.json']),
    ('build_key_graph.py',         ['references/key_graph.json']),
    ('build_execution_map.py',     ['references/execution_map.json', 'references/EXECUTION_MAP.md']),
    ('build_engine_atlas.py',      ['references/engine_atlas.json', 'references/ENGINE_ATLAS.md']),
    ('build_contract_index.py',    ['references/CONTRACT_INDEX.md', 'references/KEY_INDEX.md']),
    ('build_identifier_census.py', ['references/identifier_census.json']),
    ('definitions_store.py',       ['references/definitions/definitions.yaml']),
)


def _build_the_layer():
    """Run every builder, in dependency order. Returns {builder: artifacts}."""
    built = {}
    for builder, artifacts in _GENERATED_LAYER:
        path = _os.path.join(_REPO, 'tools', builder)
        if not _os.path.exists(path):
            continue                      # retired builder; its artifacts went with it
        args = [_sys.executable, path]
        if builder == 'definitions_store.py':
            args.append('--build')        # this one needs an explicit build flag
        r = _subprocess.run(args, cwd=_REPO, capture_output=True, text=True)
        assert r.returncode == 0, (
            f'{builder} failed to build the generated layer:\n{r.stdout}\n{r.stderr}\n'
            f'These artifacts are UNTRACKED (culling wave 5), so a builder that cannot run leaves '
            f'nothing on disk at all — this is the failure that replaced "the committed copy is '
            f'stale", and it is a harder failure, not a softer one.')
        built[builder] = artifacts
    return built


@_pytest.fixture(scope='session')
def generated_layer(request, tmp_path_factory):
    """Build every untracked generated artifact, in dependency order. Returns {builder: artifacts}.

    Request this from any test that reads one of them. It is idempotent and session-scoped, so
    ordering between tests cannot matter — which is the property that made the committed copies
    look necessary in the first place.

    EXACTLY ONE PROCESS BUILDS, EVEN UNDER `-n auto`, and that is not an optimisation.
    `scope='session'` is per-WORKER, not per-run: with N xdist workers, N processes would run these
    seven builders concurrently against one shared `references/` directory. A reader on worker 3
    then sees `key_graph.json` mid-write — the same shared-tree race that took `test_engine_atlas`
    down on 2026-08-22, arriving from the fixture instead of from a test.

    The gate is an `O_CREAT | O_EXCL` create in xdist's shared base temp dir, which is atomic on
    every filesystem this runs on. The winner builds and writes a `.done` marker; the others block
    on that marker. No `filelock` dependency — CI installs `pyyaml pytest numpy pytest-xdist` and
    nothing else, so a fixture that imported one would fail on the runner and pass locally, which
    is the same class of defect as the race it is fixing.
    """
    if not hasattr(request.config, 'workerinput'):
        return _build_the_layer()         # not under xdist: this process is the only one

    shared = tmp_path_factory.getbasetemp().parent
    done = shared / 'generated_layer.done'
    lock = shared / 'generated_layer.lock'
    try:
        fd = _os.open(str(lock), _os.O_CREAT | _os.O_EXCL | _os.O_WRONLY)
    except FileExistsError:
        fd = None

    if fd is not None:                    # we won the race; we build
        try:
            built = _build_the_layer()
            done.write_text(_json.dumps(built), encoding='utf-8')
        finally:
            _os.close(fd)
        return built

    # Someone else is building. Wait for the marker rather than racing them.
    deadline = _time.monotonic() + 900
    while _time.monotonic() < deadline:
        if done.exists():
            return _json.loads(done.read_text(encoding='utf-8'))
        _time.sleep(0.25)
    raise RuntimeError(
        f'timed out after 900s waiting for another xdist worker to build the generated layer '
        f'({done} never appeared). The builder process most likely died; its own assertion text '
        f'would be in that worker\'s output.\n'
        f'KNOWN COST, stated rather than hidden: when a builder DOES die, every other worker waits '
        f'the full 900s before reaching this line, so the common failure presents as a ~15-minute '
        f'silent CI hang and then an error that points at a different process. The alternative — a '
        f'short timeout — turns a slow machine into a spurious failure, which is worse. If this '
        f'fires in CI, read the FIRST worker\'s output, not this one\'s.')


@_pytest.fixture(scope='session')
def generated_layer_paths(generated_layer):
    """Absolute paths of every artifact the layer produced, for existence assertions."""
    return [_os.path.join(_REPO, a) for arts in generated_layer.values() for a in arts]
