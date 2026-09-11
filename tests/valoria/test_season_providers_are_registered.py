"""IMPORTING THE SEAM MUST REGISTER ITS PROVIDERS, AND THE FAILURE MODE IS SILENT.

`CLAUDE.md` §0.1 pt 5 lets a guard exist only where the defective artifact is load-bearing on THE
GAME or on a Jordan decision. This one is: `manifest.has(role, module)` is
`loop/driver.py::resolvable_verbs()`'s third gate, so an unregistered provider REMOVES A VERB FROM
THE GAME — quietly, with no exception, no refusal and no Event.

THE DEFECT THIS EXISTS FOR WAS REAL AND WAS MADE HERE, 2026-09-11, while cutting an import cycle.
`U1` had `manifest/registry.py` import `seam/wrappers/*` to run their `@provider` decorators; that
closed a cycle (`registry -> wrappers.combat -> decision -> ... -> state.world -> manifest ->
registry`) which `tests/valoria/test_import_cycle_game_state_npe.py` counted. The cut moved the
imports into `seam/wrappers/__init__.py` — and nothing imported THAT package. MEASURED at that
moment: `resolvable_verbs()` returned 17 instead of 18, `manifest.PROVIDERS` was empty, and `tell`
executed **0 times in `tiny_world` where it had executed 32** across ten seasons. No error was
raised anywhere. The repair is one line in `seam/__init__.py`; this is what fails if it is ever
removed again.

⚠ THE ASSERTION IS ON `import engine.season.seam` ALONE, deliberately. That is the contract the
cut created — *the seam owns its providers* — and asserting it via `loop.driver` instead would
pass for the wrong reason the day some other module happens to pull the wrappers in.
"""
from __future__ import annotations

import subprocess
import sys

ROOT = __file__.rsplit("/tests/", 1)[0]

_PROBE = """
import sys
sys.path.insert(0, {root!r})
import engine.season.seam            # the ONLY import under test
from engine.season.manifest import PROVIDERS
print(sorted("%s/%s" % k for k in PROVIDERS))
"""


def test_importing_the_seam_registers_every_wrapper_provider():
    """A subprocess, so no other test's imports can make this pass."""
    out = subprocess.run([sys.executable, "-c", _PROBE.format(root=ROOT)],
                         capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, out.stderr[-2000:]
    got = out.stdout.strip()
    assert "contest/personal_combat" in got and "contest/sigma_leverage" in got, (
        f"importing `engine.season.seam` registered {got or '[]'}. Both wrappers must register on "
        "that import alone — `seam/__init__.py` imports `. wrappers`, and `wrappers/__init__.py` "
        "imports each module. If this is empty, every contesting verb has silently left "
        "`resolvable_verbs()` and the season is running a smaller game with no error raised.")


_MUTATION = """
import sys
sys.path.insert(0, {root!r})
import engine.season.seam                      # registers both providers
from engine.season.manifest import PROVIDERS
from engine.season.loop.driver import resolvable_verbs
before = sorted(resolvable_verbs())
PROVIDERS.clear()                              # the silent failure, induced
after = sorted(resolvable_verbs())
print(repr((before, after)))
"""


def test_emptying_the_provider_table_removes_verbs_from_the_game():
    """THE CONSEQUENCE, OBSERVED RATHER THAN MODELLED (§0.1 pt 2).

    The first test says the table is filled. This says filling it MATTERS — that an empty table
    silently shrinks the verb set instead of raising. Without this arm, the first test could pass
    against a `has()` nothing consults, and the guard would be watching a wire that carries
    nothing.

    ⚠ IT DOES NOT ASSERT WHICH VERBS OR HOW MANY. `resolvable_verbs()`'s other two gates (a
    `requires:` predicate or typed cell, and an effect where the verb writes) exclude verbs for
    reasons that have nothing to do with the manifest — `kill / wound` is excluded by one of them
    today despite having a registered provider — so pinning a set here would fail for reasons this
    test is not about. What is asserted is the DIRECTION and that it is non-empty.

    MEASURED 2026-09-11: 18 verbs with the table filled, 17 with it cleared; the one that leaves
    is `tell`, which is the verb `U1` made contesting."""
    out = subprocess.run([sys.executable, "-c", _MUTATION.format(root=ROOT)],
                         capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, out.stderr[-2000:]
    before, after = eval(out.stdout.strip())          # a tuple of two lists, from our own probe
    assert before, "`resolvable_verbs()` returned nothing even with the providers registered"
    lost = sorted(set(before) - set(after))
    assert lost, (
        f"clearing `manifest.PROVIDERS` removed NO verb from `resolvable_verbs()` "
        f"({len(before)} before, {len(after)} after). Then the third gate is not consulting the "
        "manifest at all, and the registration the test above checks is decorative — which makes "
        "that test's pass meaningless rather than reassuring.")
    assert set(after) < set(before), (
        f"clearing the provider table did not strictly shrink the verb set: {before} -> {after}")
