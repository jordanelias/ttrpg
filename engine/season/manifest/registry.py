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
    import yaml as _y
    contracts = files.MODULE_CONTRACTS_YAML
    if not contracts.exists():
        return dict(module=name, resolver="unknown", doc="module_contracts.yaml not found")
    for m in (_y.safe_load(contracts.read_text()) or {}).get("modules") or []:
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
