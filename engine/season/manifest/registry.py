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
    name = roster_map(roster, column).get(str(key))
    if name is None:
        return None
    contracts = files.MODULE_CONTRACTS_YAML
    if not contracts.exists():
        return dict(module=name, resolver="unknown", doc="module_contracts.yaml not found")
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
            return dict(module=name, resolver=m.get("resolver") or "undeclared", doc=where)
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
