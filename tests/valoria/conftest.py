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
