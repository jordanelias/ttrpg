"""Faction.L does NOT reconstruct from the Key log — the open half of save_replay_premise.

WHY THIS EXISTS, and it is a self-correction. On 2026-08-03 I measured `Faction.L` reconstruction
at 4 of 4 factions and recorded the evidence as merely "thin". It was not thin, it was ABSENT:
three of the four sat exactly on the 0.5/7.0 clamps, and a clamped rebuild agrees with a clamped
actual whether or not the deltas are right. The number was a measurement of the clamp, not of the
log. `references/wiring_manifest.yaml` carries the corrected note.

Re-measured on horizons short enough that values have not saturated, so 3-4 factions per run are
genuine comparisons:

    seed 20260803, 5 seasons -> 0/3 rebuilt
    seed 20260803, 6 seasons -> 0/3
    seed 7,        8 seasons -> 0/4
    seed 42,       3 seasons -> 3/4   (best observed)

MECHANISM, which is why this is a design gap and not a bug to patch here. `Faction.adjust()` is the
single owner of faction-stat mutation — 31 non-test call sites across 9 files. Exactly ONE of them,
`engine/cross_scale/echo_transport.py`, emits a Key carrying `Target.stat_deltas`. The other 30
mutate L/Sta/W/Mil with no Key at all, so the log simply does not contain most of the deltas a
replay would need. Closing it means every stat mutation announcing itself, which is the propagation
question ED-1006 holds — not something to design by implication from a test.

WHY xfail(strict=True) RATHER THAN AN ASSERTION OF THE DEFECT. A test that asserts "reconstruction
fails" would go red the moment someone fixes it, punishing the fix. A strict xfail inverts that: it
passes while the gap is open, and fails LOUDLY as XPASS the moment L starts reconstructing, which
is exactly when the manifest note and this file need updating. The gap is recorded as executable
state rather than as a sentence someone has to notice.
"""
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

pytest.importorskip('yaml')

from . import _campaign  # noqa: E402  the single owner of the seeded-campaign runner (CLAUDE.md §8)

# Chosen because L has NOT saturated by here: 3 of 4 factions are off-clamp and therefore
# informative. Longer horizons drive everything to 0.5/7.0 and the comparison becomes vacuous.
SEED = 20260803
SEASONS = 6
FLOOR, CEIL = 0.5, 7.0


def _rebuild_L(initial, log):
    """Replay every Target.stat_deltas L-delta the log carries onto the t0 snapshot."""
    rebuilt = dict(initial)
    for key in log:
        for target in (getattr(key, 'targets', None) or []):
            for stat, delta in (getattr(target, 'stat_deltas', None) or {}).items():
                if stat == 'L' and target.actor_id in rebuilt:
                    rebuilt[target.actor_id] = max(FLOOR, min(CEIL, rebuilt[target.actor_id] + delta))
    return rebuilt


@pytest.fixture(scope='module')
def run():
    from engine.autoload import game_state
    w0 = game_state.create_world(seed=SEED)
    initial = {n: f.L for n, f in w0.factions.items()}
    _res, world, _seen = _campaign.run(SEED, seasons=SEASONS)
    final = {n: f.L for n, f in world.factions.items()}
    log = list(getattr(world, 'key_log', []) or [])
    return initial, final, log


def test_the_sample_is_informative(run):
    """ANTI-VACUITY, and the whole reason the first measurement was wrong.

    An agreement at a clamp is not evidence. This asserts that the comparison below has genuine
    off-clamp factions AND that at least one faction's L actually moved — without both, a
    "reconstructs perfectly" result would mean nothing.
    """
    initial, final, _log = run
    off_clamp = [n for n, v in final.items() if v not in (FLOOR, CEIL)]
    moved = [n for n in final if abs(final[n] - initial[n]) > 1e-9]
    assert len(off_clamp) >= 3, (
        f"only {len(off_clamp)} of {len(final)} factions are off-clamp at seed={SEED} "
        f"seasons={SEASONS}: {final}. Pick a shorter horizon — a clamped comparison proves nothing.")
    assert moved, f"no faction's L moved; there is nothing to reconstruct: {final}"


@pytest.mark.xfail(strict=True, reason=(
    "OPEN GAP, not a flake: 30 of Faction.adjust()'s 31 non-test call sites emit no Key, so the "
    "log lacks most L deltas. Strict, so this fails as XPASS the moment L starts reconstructing — "
    "at which point update references/wiring_manifest.yaml's save_replay_premise note too."))
def test_faction_L_reconstructs_from_the_key_log(run):
    initial, final, log = run
    rebuilt = _rebuild_L(initial, log)
    informative = [n for n, v in final.items() if v not in (FLOOR, CEIL)]
    mismatched = {n: (initial[n], final[n], rebuilt[n])
                  for n in informative if abs(rebuilt[n] - final[n]) > 1e-9}
    assert not mismatched, (
        f"{len(mismatched)} of {len(informative)} off-clamp factions do not reconstruct "
        f"(name: initial -> actual, rebuilt): {mismatched}")


def test_only_one_call_site_emits_stat_deltas():
    """Pins the MECHANISM, so a future reader does not have to re-derive it.

    Counted over source rather than asserted from memory. If a second emitter lands, this fails and
    whoever added it should re-run the reconstruction — that is the intended trigger.
    """
    import re
    roots = [os.path.join(ROOT, 'engine'), os.path.join(ROOT, 'systems')]
    adjusting, emitting_stat_deltas = set(), set()
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in ('__pycache__', 'tests')]
            for fn in filenames:
                if not fn.endswith('.py'):
                    continue
                path = os.path.join(dirpath, fn)
                src = open(path, encoding='utf-8').read()
                rel = os.path.relpath(path, ROOT)
                if re.search(r'\.adjust\(', src) and 'def adjust' not in src:
                    adjusting.add(rel)
                # `stat_deltas=` as a KEYWORD ARGUMENT, not the bare substring. The substring
                # form over-reported immediately: parliamentary_transfer.py mentions
                # `Target.stat_deltas` in a docstring while emitting a Key that carries none.
                # A proxy that cannot tell prose from code is the recurring defect in this repo.
                if re.search(r'stat_deltas\s*=', src):
                    emitting_stat_deltas.add(rel)
    assert adjusting, "found no faction-stat mutation sites — the scan is broken, not the code"
    traced = adjusting & emitting_stat_deltas
    assert traced == {os.path.join('engine', 'cross_scale', 'echo_transport.py')}, (
        f"the set of stat-mutating files that also carry stat_deltas changed: {sorted(traced)}. "
        f"If a new emitter landed, re-run the Faction.L reconstruction — the xfail above may now "
        f"XPASS.")
    assert len(adjusting) >= 8, f"only {len(adjusting)} mutation sites found; expected ~9"
