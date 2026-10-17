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

import functools
import subprocess
import sys
from types import SimpleNamespace

from .test_module_registrar import _run

ROOT = __file__.rsplit("/tests/", 1)[0]

_PROBE = """
import sys
sys.path.insert(0, {root!r})
import engine.season.seam            # the ONLY import under test
from engine.season.manifest import PROVIDERS
from engine.season.data.rosters import roster_map   # reads data; registers nothing
# v9 FI-02: EVERY ROLE'S ROWS, read off the role map (`_ROLE_ROSTERS`, data, registers nothing), so the
# `inquiry` role's provider is covered as each prize row's is -- and a third role would be too.
from engine.season.manifest.registry import _ROLE_ROSTERS
named = sorted({{"%s/%s" % (role, r.get("provider") if isinstance(r, dict) else None)
                for role, (roster, column) in _ROLE_ROSTERS.items()
                for r in roster_map(roster, column).values()}})
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
    assert "contest/personal_combat" in got and "contest/social_contest" in got, (
        f"importing `engine.season.seam` registered {got or '[]'}. Both wrappers must register on "
        "that import alone — `seam/__init__.py` imports `. wrappers`, and `wrappers/__init__.py` "
        "imports each module. If this is empty, every `SeasonDriver` construction refuses.")
    assert named and "contest/mass_battle" in named, (
        f"the prize rows name {named}; this arm exists to cover every one of them, `mass_battle` "
        "included, and an empty list makes it vacuous (§0.1 pt 2)")
    assert any(n.startswith("inquiry/") for n in named), (
        f"no `inquiry` row names a provider ({named}); v9 FI-02's role is covered by this arm, and its "
        "absence would make the arm vacuous for it (§0.1 pt 2)")
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


# ---------------------------------------------------------------------------
# v9 FI-02 (`SM-3`), built with FI-03 (`ED-FI-0002`): THE SECOND ROLE, `inquiry`. Its EXIT and its two
# falsifiers, each in a FRESH SUBPROCESS -- the within-process form passes by order of construction
# (`MODULE_ENTRIES` and `composition.ROLES` are process globals another test's drivers fill), the hazard
# `test_module_registrar.py` documents. The role's name is the subject under test, so it is spelt; its
# rows, keys and entries are read off the data, never named.
# ---------------------------------------------------------------------------

_ROLE = "inquiry"

# The shared fresh-process harness is `test_module_registrar.py`'s (`_run` formats only `root` into
# `_HEAD`: the driver, `World`, `MODULE_ENTRIES`, `composition` and `construct()`); this adds the role's
# own rows. Built with `repr`, so the preamble carries no `{}` placeholder.
_ROLE_PREAMBLE = f"""
import engine.season.manifest.registry as R
ROLE = {_ROLE!r}
ROSTER, COLUMN = R._ROLE_ROSTERS[ROLE]
ROWS = R.roster_map(ROSTER, COLUMN)
"""


def _fresh(body: str):
    return _run(_ROLE_PREAMBLE + body)


def test_fi02_exit_check_rows_returns_a_pair_for_the_inquiry_role():
    """FI-02's EXIT: `check_rows()` -- `04 PART E step 10`'s boot sweep, which iterates the role map --
    returns at least one `(inquiry, key)` pair, and exactly one per row the role's roster carries. The
    count is asserted before the membership, so a sweep that resolved nothing cannot pass (`CLAUDE.md`
    §0.1 pt 2); and the driver constructs on the shipped rows (the control for the two refusals below)."""
    keys, pairs, control = _fresh("""
pairs = R.check_rows()
print(repr((sorted(ROWS), sorted(k for r, k in pairs if r == ROLE), construct())))
""")
    assert len(pairs) >= 1, f"`check_rows()` returned no `{_ROLE}` pair -- the sweep did not reach the role"
    assert pairs == keys, f"`check_rows()` checked {pairs} of the role's rows {keys}"
    assert control is None, control


def test_fi02_deleting_the_inquiry_composition_row_refuses_construction_naming_it():
    """FI-02 FALSIFIER 1: delete the role's composition row in a fresh process -> `SeasonDriver`
    construction refuses, naming the row. `before == []` makes it the fresh-process form: the registrar
    holds nothing to miss, so the refusal is `check_inquiry_modules`' -- the declaration that the row must
    exist (the row's `module_entry:`). RED WHEN PLANTED (run 2026-10-17): with the
    `check_inquiry_modules(VERB_TABLE)` call deleted from `loop/driver.py`, construction succeeds
    (`refusal` is `None`) and this test fails."""
    got = _fresh("""
entries = sorted({row["module_entry"] for row in ROWS.values() if isinstance(row, dict)})
out = []
for role in entries:
    MODULE_ENTRIES.clear()                    # each pass fresh: an earlier pass must not fill it
    in_rows = role in composition.ROLES
    saved = composition.ROLES.pop(role, None)
    out.append((role, in_rows, sorted(MODULE_ENTRIES), construct()))
    composition.ROLES[role] = saved
print(repr(out))
""")
    assert got, f"the `{_ROLE}` rows name no module entry -- this falsifier observes nothing"
    for role, in_rows, before, refusal in got:
        assert in_rows, f"the `{_ROLE}` rows name {role!r}, which no composition row declares"
        assert before == [], f"MODULE_ENTRIES was filled before construction: {before}"
        assert refusal is not None, f"deleting composition row {role!r} did NOT refuse construction"
        kind, text = refusal
        assert kind == "Unspecified" and repr(role) in text and "no composition row declares" in text, (
            refusal)


def test_fi02_a_misspelled_inquiry_row_fails_check_rows_naming_it():
    """FI-02 FALSIFIER 2: misspell the module a role row names, in a fresh process -> `check_rows()` raises
    `Unspecified` naming the roster, the row's key and the misspelling (`04 PART E step 10`: *"a misspelled
    manifest row fails at boot naming the row"*). The key is read off the roster, not named. RED WHEN
    PLANTED (run 2026-10-17): with `check_rows()`'s `resolve(role, key)` line deleted, it returns cleanly
    and this test fails."""
    got = _fresh("""
key = sorted(ROWS)[0]
bad = dict(ROWS[key], module=str(ROWS[key]["module"])[:-1])
real = R.roster_map
R.roster_map = lambda roster, column: (dict(real(roster, column), **{key: bad})
                                       if (roster, column) == (ROSTER, COLUMN) else real(roster, column))
try:
    R.check_rows()
    refusal = None
except Exception as exc:
    refusal = (type(exc).__name__, str(exc))
print(repr((ROSTER, key, bad["module"], refusal)))
""")
    roster, key, misspelt, refusal = got
    assert refusal is not None, f"`check_rows()` accepted `{roster}` row {key!r} naming {misspelt!r}"
    kind, text = refusal
    for name in (roster, repr(key), repr(misspelt)):
        assert name in text, f"the refusal does not name {name}: {refusal}"
    assert kind == "Unspecified", refusal


# ---------------------------------------------------------------------------
# `check_inquiry_modules`' REFUSALS, EACH PLANTED (B1, B2 (c)-(e)). ONE fresh process runs all four
# plants, each restoring what it changed before the next, and each test reads its own: the empty-table
# test above cannot reach these, because `check_contest_prizes` refuses first when every provider is
# gone. The row's key, provider and entry are read off the data; the planted kind is a covert kind
# (`rosters.yaml: covert_kinds`), a deed no graded inquiry emits. RED WHEN PLANTED (run 2026-10-17,
# then restored): the four refusals' conditions set to `False` -- each of the four tests below RED.
# ---------------------------------------------------------------------------

_PLANTS = """
from engine.season.manifest import PROVIDERS
from engine.season.data.rosters import COVERT_KINDS
KEY = sorted(ROWS)[0]
NAME = ROWS[KEY]["provider"]

def with_rows(rows):
    real = R.roster_map
    R.roster_map = lambda roster, column: (rows if (roster, column) == (ROSTER, COLUMN)
                                           else real(roster, column))
    try:
        return construct()
    finally:
        R.roster_map = real

def with_provider(fn):
    real = PROVIDERS.pop((ROLE, NAME))
    if fn is not None:
        PROVIDERS[(ROLE, NAME)] = fn
    try:
        return construct()
    finally:
        PROVIDERS[(ROLE, NAME)] = real

out = dict(
    control=construct(),
    no_entry=with_rows(dict(ROWS, **{KEY: {k: v for k, v in ROWS[KEY].items() if k != "module_entry"}})),
    unregistered=with_provider(None),
    no_keyword=with_provider(lambda w, a, e: None),
    ungraded_kind=with_rows(dict(ROWS, **{sorted(COVERT_KINDS)[0]: ROWS[KEY]})),
)
print(repr((ROSTER, KEY, NAME, sorted(COVERT_KINDS)[0], out)))
"""


@functools.lru_cache(maxsize=None)
def _plants():
    roster, key, name, kind, out = _fresh(_PLANTS)
    return SimpleNamespace(roster=roster, key=key, name=name, kind=kind, out=out)


def _refused(case: str, *names: str) -> None:
    out = _plants().out
    assert out["control"] is None, f"the shipped rows do not construct: {out['control']}"
    refusal = out[case]
    assert refusal is not None, f"plant {case!r} did NOT refuse construction"
    got, text = refusal
    assert got == "Unspecified", refusal
    for n in names:
        assert n in text, f"plant {case!r}'s refusal does not name {n}: {refusal}"


def test_fi02_an_inquiry_row_with_no_module_entry_refuses_naming_it():
    """B1: the role's row with its `module_entry:` popped -> construction refuses naming the roster, the
    row and the missing field (it passed `_check_module_entry` unchecked, and failed at the first find)."""
    plants = _plants()
    _refused("no_entry", plants.roster, repr(plants.key), "module_entry")


def test_fi02_an_unregistered_inquiry_provider_refuses_naming_it():
    """B2 (c), step 1: ONLY the inquiry row's provider popped from the table (every contest provider
    stays, so `check_contest_prizes` passes) -> refused naming the roster, the row and the provider."""
    plants = _plants()
    _refused("unregistered", plants.roster, repr(plants.key), repr(plants.name), "nobody registered")


def test_fi02_an_inquiry_provider_without_the_module_entry_keyword_refuses_naming_it():
    """B2 (d), step 3: the provider replaced by one taking no `module_entry` keyword -> refused naming
    the row and the keyword, at construction rather than as a `TypeError` at the first find."""
    plants = _plants()
    _refused("no_keyword", plants.roster, repr(plants.key), repr(plants.name),
             "no `module_entry` keyword")


def test_fi02_an_inquiry_row_keyed_on_a_kind_no_graded_verb_emits_refuses_naming_it():
    """B2 (e), `_graded_verb_emits_it`: a second row, keyed on a covert deed kind, same entry -> refused
    naming that key: no graded inquiry emits it, so it would reach the entry carrying no degree."""
    _refused("ungraded_kind", repr(_plants().kind), "no graded inquiry emits")
