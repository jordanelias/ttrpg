"""`engine/` must not name `systems/`. Six sites still do; this pins them so they can only go away.

THE PREMISE (Jordan, 2026-08-20): **`systems/` stems from `engine/` and `references/`.** `engine/`
is the root — the executable model and the single owner of each rule — and `systems/<sub>/sim/`
composes on top of it. A top-level `from systems...` inside `engine/` inverts that: the root names
its own dependents, and the package graph acquires a cycle.

WHAT WAS MEASURED, 2026-08-20. `CLAUDE.md` §3 claimed the dependency graph is "acyclic, autoload is
a leaf". It is neither. Six non-test modules under `engine/` import `systems.*` at module level, and
`engine/autoload/game_state.py` imports seven subsystems' state classes inside functions — deferred
imports hide a cycle from the interpreter, they do not remove it. `systems/factions/sim/
faction_action.py:42` imports `engine.autoload.game_state` while `game_state.py:384` imports
`systems.factions.sim.treaty`; that is a package-level cycle, live today.

WHY THIS IS A RATCHET AND NOT A CLIFF. A hard "zero imports" assertion would be red on arrival and
would be deleted within a session. `ALLOWED` is a ceiling that can only go DOWN: each seam that
moves to registration-driven composition deletes its line here, in the same commit, and a NEW
inversion fails immediately. That is the same shape as `.godot-compile-baseline` in the port.

SUBJECT, under `CLAUDE.md` §0.1 pt 5's load-bearing predicate: the architecture of the executable
model that the Godot port is generated against — the game, not this repository's process. It earns
its existence. It is also the falsifier §0.1 pt 3 requires for the claim "the direction is being
inverted": without it, the last seam removed would be silently re-added by the next session.

`engine/tests/` is exempt. A test may reach across any boundary to set up a case; that is what tests
are for, and forbidding it would only push the reach into a fixture.
"""
from __future__ import annotations

import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parents[2]
ENGINE = REPO / 'engine'

# Top-level `from systems...` / `import systems...` — column 0 only. An import nested inside a
# function is a DIFFERENT (and also real) problem, tracked separately; conflating them would make
# this list churn on refactors that change nothing about the package graph.
TOP_LEVEL_SYSTEMS_IMPORT = re.compile(r'^(?:from|import)\s+systems[.\s]', re.M)

# THE CEILING. Every entry is a seam to be moved to registration-driven composition
# (proposals/2026-08-20-return-to-game-plan-v1.md Act C3). Remove the line when the seam lands.
# NEVER add one.
ALLOWED = {
    # Removal order, cheapest first. Seam 1 (cross_scale/echo_transport.py) LANDED 2026-08-20: it
    # imported systems.settlements.sim.registry for STAT_MIN/STAT_MAX alone, a 0-5 bound that
    # references/descriptor_registry.yaml already declares as `set.order`, so it now reads the root
    # via engine.substrate.descriptors. Value-identical by construction; the seeded goldens were the
    # control and did not move.
    'mc_v18.py': 2,                          # 2. campaign-driver callbacks: faction_action, season
    'cross_scale/parliamentary_bridge.py': 3,  # 3. and delete the lateral duplicate of this same
                                             #    seam at systems/factions/sim/parliamentary_transfer.py:54
}
BASELINE_TOTAL = 5


def _offenders():
    found = {}
    for path in sorted(ENGINE.rglob('*.py')):
        rel = path.relative_to(ENGINE).as_posix()
        if rel.startswith('tests/') or '__pycache__' in rel:
            continue
        hits = TOP_LEVEL_SYSTEMS_IMPORT.findall(path.read_text(encoding='utf-8'))
        if hits:
            found[rel] = len(hits)
    return found


def test_no_new_engine_to_systems_inversion():
    found = _offenders()
    new = sorted(set(found) - set(ALLOWED))
    assert not new, (
        'NEW engine/ -> systems/ import(s): ' + ', '.join(new) + '\n'
        'engine/ is the root; systems/ stems from it. Compose through an engine.substrate '
        'registration point instead of naming the subsystem, or if this seam genuinely cannot move '
        'yet, say so in the plan and add it here deliberately — never as a drive-by.'
    )


def test_the_allow_list_can_only_shrink():
    found = _offenders()
    stale = sorted(set(ALLOWED) - set(found))
    assert not stale, (
        'These seams no longer import systems/: ' + ', '.join(stale) + '\n'
        'Good — delete them from ALLOWED and lower BASELINE_TOTAL in this same commit. A stale '
        'ceiling is how a ratchet stops ratcheting.'
    )


def test_the_total_did_not_rise():
    total = sum(_offenders().values())
    assert total <= BASELINE_TOTAL, (
        f'engine/ -> systems/ imports ROSE {BASELINE_TOTAL} -> {total}.'
    )
    assert total == BASELINE_TOTAL, (
        f'engine/ -> systems/ imports FELL {BASELINE_TOTAL} -> {total}. Lower BASELINE_TOTAL to '
        f'{total} in this commit so the progress is banked.'
    )


def test_this_check_can_observe_its_own_failure(tmp_path):
    """An assertion that cannot observe the failure it excludes is an absent assertion (§0.1 pt 2)."""
    probe = tmp_path / 'probe.py'
    probe.write_text('from systems.factions.sim import treaty\n')
    assert TOP_LEVEL_SYSTEMS_IMPORT.search(probe.read_text())
    nested = tmp_path / 'nested.py'
    nested.write_text('def f():\n    from systems.factions.sim import treaty\n')
    assert not TOP_LEVEL_SYSTEMS_IMPORT.search(nested.read_text()), \
        'the pattern must not fire on a function-local import — that is a different problem'


def test_the_documented_cycle_is_still_real():
    """`CLAUDE.md` §3 says the graph is acyclic and autoload is a leaf. It is not, and this records
    the concrete cycle so the claim cannot be quietly restored while the code still contradicts it.
    Delete this test in the commit that breaks the cycle — and fix §3 in the same commit."""
    fa = (REPO / 'systems' / 'factions' / 'sim' / 'faction_action.py').read_text(encoding='utf-8')
    gs = (REPO / 'engine' / 'autoload' / 'game_state.py').read_text(encoding='utf-8')
    assert 'engine.autoload.game_state' in fa, 'the systems -> engine half of the cycle moved'
    assert 'systems.factions.sim.treaty' in gs, 'the engine -> systems half of the cycle moved'
