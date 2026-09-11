"""`manifest/registry.py` -- the role -> provider rows and the two checks over them.

`04 §C.5` spells the call the seam makes, and this module answers it:

    provider = manifest.resolve("contest", prizes[prize])

`04 §A.2:136` types the module -- *"role -> provider rows, resolved at boot"* -- and `04:1031`'s
build step 10 states its done-condition: *"a misspelled manifest row fails at boot naming the row."*
"""

from __future__ import annotations

from typing import Any, Optional

from ..data import files
from ..data.rosters import roster_map
from ..gaps import NoProducer, Unspecified

# ⚠ THE ROLE NAMES ARE DATA, NOT A LITERAL HERE. A role maps to the roster that declares its
# providers; adding a role is a data edit plus one row in this map, and the map exists so
# `resolve` does not branch on a role's name. Two entries today because there is one seam.
_ROLE_ROSTERS = {"contest": ("contest_subsystems", "prizes")}
# ⚠ ONE ENTRY TODAY, because there is one seam. (A first writing of the line above said
# "two entries today" beside a dict of one -- a count written from memory next to the thing
# it counts.)


# ---------------------------------------------------------------------------
# ⚠ THE CONTRACTS FILE IS READ AND PARSED **ONCE PER PROCESS**, AND THE CACHE IS A BUG FIX RATHER
# THAN AN OPTIMISATION. `check_rows()` runs on every `SeasonDriver` construction (that is where
# `04:1031`'s "at boot" actually reaches a run), and it resolves every row; each `resolve` was
# re-reading and re-parsing `references/module_contracts.yaml` from disk. The corpus builds many
# drivers, and the season suite went from ~170s to over 600s -- measured, on the commit that wired
# it. A per-process cache is safe because the file is repository content that cannot change under a
# running season; a test that needs it re-read clears `_CONTRACTS_CACHE`.
# ---------------------------------------------------------------------------
_CONTRACTS_CACHE: list = []


def _contracts() -> list:
    """`references/module_contracts.yaml`'s `modules:` list, parsed once."""
    if not _CONTRACTS_CACHE:
        import yaml as _y
        text = files.MODULE_CONTRACTS_YAML.read_text()
        _CONTRACTS_CACHE.append((_y.safe_load(text) or {}).get("modules") or [])
    return _CONTRACTS_CACHE[0]


# ---------------------------------------------------------------------------
# `U1`: THE ROLE -> PROVIDER **CALLABLE** TABLE, AND IT IS THE OTHER HALF OF THE ROW.
#
# `resolve(role, key)` above answers *WHICH MODULE owns this key* by reading data. This answers
# *WHAT DO I CALL* -- the provider itself, registered by the module that defines it. `04 §C.5:682`
# spells the seam's call as `provider = manifest.resolve("contest", prizes[prize])`, and a name is
# only half a provider: something has to turn it into a function without the seam branching on it.
#
# ⚠ **THE DECORATOR IS `@effect_for`'s PATTERN AND THE REASON IS THE SAME ONE.** A table filled by
# decoration lives in the module that defines the decorated things, or it is empty at the moment the
# seam reads it. `loop/effects.py` states that rule at length for `EFFECTS`; this is it once more,
# one seam along.
#
# ⚠ **AND IT IS WHAT REPLACES `if _sub["module"] == "personal_combat":` IN `seam/contest.py`.**
# ED-SC-0033 clause (1) rules exactly that: *"the seam dispatches by manifest ROW rather than the
# hardcoded personal_combat literal"*. A literal in the seam is a second registry that disagrees
# with the first the day a row moves.
# ---------------------------------------------------------------------------
# ⚠⚠ **THE TABLE AND THE DECORATOR MOVED TO `manifest/providers.py`, A LEAF, TO BREAK A REAL
# IMPORT CYCLE.** They were defined here beside `_load_providers()`, which imports
# `seam/wrappers/*`, while the wrappers import the decorator back:
# `manifest.registry -> seam.wrappers.sigma -> manifest -> manifest.registry`.
# `_load_providers`'s docstring called that cycle *"genuine"* and made its import lazy, which hid
# it from the interpreter and not from the instrument: the cycle count went 3 -> 4 on the `U1`
# tree, and `tests/valoria/test_import_cycle_game_state_npe.py` says why in its own words --
# *"A deferred or bare-named import hides a cycle from an instrument; it does not remove it."*
# The table is a PRIMITIVE and this module is a POLICY over it; splitting them makes the package
# acyclic by construction. Re-exported here so every existing caller of
# `manifest.registry.provider` is untouched.
from .providers import PROVIDERS, provider      # noqa: F401


def has(role: str, module: str) -> bool:
    """Is a provider REGISTERED for this row? Read by `resolvable_verbs()`'s third gate.

    ⚠ IT IS A QUESTION ABOUT THE CODE, NOT ABOUT THE DATA, WHICH IS WHY IT IS SEPARATE FROM
    `resolve`. A roster row may name a module the contracts file declares and nothing may have
    registered a callable for it — `mass_battle` is exactly that today. `resolve` answers *whose
    prize is this*; this answers *can anybody actually run it*, and a verb is resolvable only on the
    second.

    ⚠ **IT NO LONGER IMPORTS ANYTHING TO MAKE THE ANSWER TRUE.** `_load_providers()` stood
    here and imported `seam/wrappers/*`, which was an import cycle -- see
    `seam/wrappers/__init__.py` for the loop and the cut. The seam registers its own providers
    now, so this READS a table somebody else filled, which is what a registry should do. Every
    real caller arrives through `loop/driver.py` or `loop/resolve.py`, both of which import
    `..seam`."""
    return (str(role), str(module)) in PROVIDERS


def call(role: str, module: str):
    """The registered provider, or `None`. The seam's one lookup.

    ⚠ Reads the table; never fills it. See `has()` and `seam/wrappers/__init__.py`."""
    return PROVIDERS.get((str(role), str(module)))


def resolve(role: str, key: Any) -> Optional[dict]:
    """The provider a role's registry names for this key, or `None` if no row claims it.

    `None` IS A REAL ANSWER, not a failure: an unclaimed prize leaves the seam's generic refusal
    intact, which is the behaviour `seam/contest.py` had before this rule moved here and which its
    callers still depend on. What is NOT a real answer is a row naming a module no contract
    declares -- that raises, because the dispatch target would otherwise be invented.

    ⚠ NEITHER HALF IS INVENTED HERE. The KEY is what Part E's `contests:` column carries; the
    PROVIDER is a module `references/module_contracts.yaml` already declares with a resolver."""
    roster, column = _ROLE_ROSTERS.get(role, (None, None))
    if roster is None:
        raise Unspecified(
            f"no registry is declared for role {role!r}", "S43",
            needs=f"a `{role}` entry in manifest/registry.py's role map, and the roster it names",
            law="04 §D.4 -- the seam names a ROLE and a manifest row names the PROVIDER. A role "
                "with no registry has no provider to name, and guessing one is the path literal "
                "in a body that S43 refuses")
    # ⚠ `U1`: A PRIZE IS A ROW NOW, NOT A MODULE STRING, AND BOTH SHAPES ARE READ HERE SO THE
    # SCHEMA CHANGE IS ONE EDIT RATHER THAN A SWEEP. `module:` is whose prize it is — what the
    # contracts file is checked against and what the seam names when it refuses. `provider:` is
    # what actually runs it, which `manifest.call` asks for separately, and the two are different
    # questions the moment an interim resolver stands in for an unbuilt subsystem.
    row = roster_map(roster, column).get(str(key))
    if row is None:
        return None
    # ⚠⚠ **A NON-DICT ROW IS A MODULE WITH NO PROVIDER, AND SAYING SO IS THE FIX — NOT DELETING
    # THE BRANCH.** A `/simplify` pass read this as a dead compatibility shim, on the grounds that
    # all four shipped rows are dicts. They are; the branch is still live, because
    # `test_a_misspelled_manifest_row_fails_at_boot_naming_the_row` PLANTS a bare string
    # (`{"a fabricated prize": "no_such_subsystem"}`) as its misspelled-row arm, and deleting the
    # branch turned that boot refusal from a typed `Unspecified` naming the row into a raw
    # `AttributeError`. The suite caught it; the reasoning that it was unreachable did not.
    # ⚠ WHAT *WAS* WRONG IS THE SECOND READ, AND IT IS FIXED BELOW: it spelled
    # `row.get("provider") if isinstance(row, dict) else row`, so a string row returned the MODULE
    # as the PROVIDER — the one confusion `U1` added the `provider:` field to end. A string names
    # WHOSE prize it is and nothing about what runs it, so the provider is `None` and the row
    # refuses downstream like any other row with no provider.
    name = row.get("module") if isinstance(row, dict) else row
    if name is None:
        raise Unspecified(
            f"`{roster}` has a row for {key!r} with no `module:`", "S39",
            needs="a `module:` naming the subsystem that owns the prize",
            law="a prize row names WHOSE contest it is before it names what runs it; a row with a "
                "provider and no module says a thing can be rolled without saying what it is")
    provider_name = row.get("provider") if isinstance(row, dict) else None
    contracts = files.MODULE_CONTRACTS_YAML
    if not contracts.exists():
        return dict(module=name, provider=provider_name, resolver="unknown",
                    doc="module_contracts.yaml not found")
    for m in _contracts():
        if m.get("module") == name:
            # ⚠ THE PYTHON, NOT THE MARKDOWN. Jordan, 2026-09-02: *"we aren't using the .md or
            # anything for those systems. those are super outdated."* The contracts file carries
            # both a `doc:` (markdown) and a `sim_module:` (the live Python) for these three, and
            # the first version of this refusal printed the `doc:` -- so it pointed a reader at a
            # file its owner calls superseded.
            where = m.get("sim_module") or ""
            if not where:
                guess = files.subsystem_sim_dir(name)
                where = (f"systems/{name}/sim/" if guess.is_dir()
                         else f"(no `sim_module:` in module_contracts.yaml; "
                              f"`doc:` is {m.get('doc')!r} and is out of date)")
            return dict(module=name, provider=provider_name,
                        resolver=m.get("resolver") or "undeclared", doc=where)
    raise Unspecified(
        f"`{roster}` maps {key!r} to {name!r}, which is in no module contract", "S39",
        needs="a module named in references/module_contracts.yaml",
        law="the roster may only name a subsystem the contracts file declares -- otherwise the "
            "dispatch target is invented")


def check_roles(manifest: dict, required_roles: tuple) -> None:
    """S43. Every required role has a provider, or a STARTUP FAILURE WITH A NAME IN IT.

    Moved here from `World.boot`, where the rule sat inline on a STORE. The `World` keeps the
    method -- its callers hold a world, not a manifest -- and delegates, so the rule lives once."""
    missing = [r for r in required_roles if r not in (manifest or {})]
    if missing:
        raise NoProducer(
            f"role(s) {missing} have no provider in the manifest", "S43",
            needs="a registry row naming a role and its provider",
            law="S43 -- the engine names the ROLE; the registry names the MODULE; RESOLUTION "
                "HAPPENS BY STRING AT BOOT. A missing provider is a startup failure with a name "
                "in it. THE MANIFEST IS THE SEAM; A PATH LITERAL IN A BODY IS NOT")


def check_rows() -> list:
    """`04:1031`'s done-condition: **a misspelled manifest row fails at boot naming the row.**

    Every row of every declared role's roster is resolved once. A row naming a module no contract
    declares raises from `resolve` with the row in the message, so the failure names what to fix
    rather than surfacing three seasons later as a null.

    ⚠ CALLED FROM `World.boot`, NOT AT IMPORT, and the reason is in this package's docstring: an
    import-time read of `module_contracts.yaml` would make every reader of one name pay for it.
    Returns the rows it checked, so a caller can assert the sweep was not empty -- a validator that
    resolved nothing has reported clean over an unexamined registry (`CLAUDE.md` §0.1 pt 2)."""
    checked = []
    for role, (roster, column) in _ROLE_ROSTERS.items():
        for key in roster_map(roster, column):
            resolve(role, key)
            checked.append((role, key))
    return checked


def unclaimed_contest_prizes() -> list:
    """§B.13 invariant 9 (`04:467`): **every verb's `contests:` prize is in the subsystem roster.**

    ⚠ **THIS IS THE OTHER HALF OF A MANIFEST ROW AND `check_rows()` DOES NOT COVER IT.** `check_rows`
    validates every roster row's PROVIDER -- that the module it names is one the contracts file
    declares. It says nothing about the KEY side: a verb declaring `contests: the bodyy` loads
    clean, boots clean, and at first call `resolve` returns `None` (a real answer, for a prize no row
    claims), so the seam falls through to its generic refusal, **naming no row.** That is the
    first-call failure mode `04:1031` replaces, surviving in the half nobody checked. Found by the
    Fable gate on Arc 1.

    Returned rather than raised, and deliberately: `04:467`'s invariant belongs to the LOADER
    (§B.13's twelve), and `data/`'s one loader is itself unbuilt -- `04:131`. Wiring a raise here
    would put a data invariant in the manifest and make the seam the loader. The list is what a
    caller asserts on, and `test_every_contested_verbs_prize_is_in_the_subsystem_roster` is that
    caller until the loader exists."""
    from ..data.verbs import VERB_TABLE
    claimed = set(roster_map(*_ROLE_ROSTERS["contest"]))
    out = []
    for verb, row in VERB_TABLE.items():
        prizes = getattr(row, "contests", None)
        if not prizes:
            continue
        for p in ([prizes] if isinstance(prizes, str) else list(prizes)):
            if str(p) not in claimed:
                out.append((verb, str(p)))
    return out
