"""IMPORTING THE SEAM MUST REGISTER ITS PROVIDERS, AND THE FAILURE MODE WAS SILENT.

`CLAUDE.md` §0.1 pt 5 lets a guard exist only where the defective artifact is load-bearing on THE
GAME or on a Jordan decision. This one is: until plan position `30`, `manifest.has(role, module)` was
`loop/driver.py::resolvable_verbs()`'s third gate, so an unregistered provider REMOVED A VERB FROM
THE GAME — quietly, with no exception, no refusal and no Event. `30` deleted that clause and made the
same state a REFUSAL AT DRIVER CONSTRUCTION (`manifest.check_contest_prizes()`, naming the prize);
the second test below watches the refusal, so the guard still observes the consequence rather than
the table alone.

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
from engine.season.data.rosters import roster_map   # reads data; registers nothing
named = sorted({{"contest/%s" % (r.get("provider") if isinstance(r, dict) else None)
                for r in roster_map("contest_subsystems", "prizes").values()}})
print(repr((sorted("%s/%s" % k for k in PROVIDERS), named)))
"""


def test_importing_the_seam_registers_every_wrapper_provider():
    """A subprocess, so no other test's imports can make this pass.

    Plan position `30`: it also asserts EVERY provider a prize row names — `mass_battle` joined the
    two it spelled — so a third prize row whose wrapper the seam does not import fails here, before
    driver construction refuses it."""
    out = subprocess.run([sys.executable, "-c", _PROBE.format(root=ROOT)],
                         capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, out.stderr[-2000:]
    got, named = eval(out.stdout.strip())             # two lists, from our own probe
    assert "contest/personal_combat" in got and "contest/sigma_leverage" in got, (
        f"importing `engine.season.seam` registered {got or '[]'}. Both wrappers must register on "
        "that import alone — `seam/__init__.py` imports `. wrappers`, and `wrappers/__init__.py` "
        "imports each module. If this is empty, every `SeasonDriver` construction refuses.")
    assert named and "contest/mass_battle" in named, (
        f"the prize rows name {named}; this arm exists to cover every one of them, `mass_battle` "
        "included, and an empty list makes it vacuous (§0.1 pt 2)")
    missing = sorted(set(named) - set(got))
    assert not missing, (
        f"prize row provider(s) {missing} are not registered by importing `engine.season.seam` "
        f"(registered: {got}). Every `SeasonDriver` construction refuses them by name.")


_MUTATION = """
import sys
sys.path.insert(0, {root!r})
import engine.season.seam                      # registers every provider
from engine.season.manifest import MODULE_ENTRIES, PROVIDERS
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.world import World
SeasonDriver(World(0))                         # constructs while the table is filled
before = sorted(resolvable_verbs())
PROVIDERS.clear()                              # the failure, induced
MODULE_ENTRIES.clear()
after = sorted(resolvable_verbs())
try:
    SeasonDriver(World(0))
    refusal = None
except Exception as exc:                       # the type is asserted by the test
    refusal = (type(exc).__name__, str(exc))
print(repr((before, after, refusal)))
"""


def test_emptying_the_provider_table_refuses_driver_construction():
    """THE CONSEQUENCE, OBSERVED RATHER THAN MODELLED (§0.1 pt 2).

    The first test says the table is filled. This says filling it MATTERS. Until plan position `30`
    the consequence was SILENT — an empty table shrank `resolvable_verbs()` (MEASURED 2026-09-11:
    18 verbs filled, 17 cleared; `tell` left) — and this test asserted the shrink. `30` deleted
    `resolvable_verbs()`'s `manifest.has` clause and made the empty table a REFUSAL at driver
    construction, naming the prize; so this asserts the refusal, and that the verb set no longer
    moves (the old silent path is gone, not merely shadowed). Clearing `MODULE_ENTRIES` too is the
    plan's arm: the registrar refills it from the rows, so its emptiness alone refuses nothing."""
    out = subprocess.run([sys.executable, "-c", _MUTATION.format(root=ROOT)],
                         capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, out.stderr[-2000:]
    before, after, refusal = eval(out.stdout.strip())  # a tuple, from our own probe
    assert before, "`resolvable_verbs()` returned nothing even with the providers registered"
    assert refusal is not None, (
        "clearing `manifest.PROVIDERS` did NOT refuse `SeasonDriver` construction. Then nothing "
        "consults the table at construction, and the registration the test above checks is "
        "decorative — the silent path `30` closed would be open again with nothing watching it.")
    kind, text = refusal
    assert kind == "Unspecified" and "nobody registered" in text and "prize" in text, (
        f"the refusal is not the typed one naming the prize: {refusal}")
    assert after == before, (
        f"clearing the provider table moved `resolvable_verbs()` ({before} -> {after}): the deleted "
        "`manifest.has` clause, or a second copy of it, is consulting the table again")
