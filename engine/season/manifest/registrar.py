"""`manifest/registrar.py` -- THE REGISTRAR: every composition row that carries a module ENTRY,
resolved by string and recorded in ONE table, `MODULE_ENTRIES`, at driver construction.

Plan position `30` (A-25; `ED-IN-0284`, revised by `ED-IN-0285`). Terms, defined where code invokes
them (`CLAUDE.md` §4):

  * A MODULE is running code reached by a composition row (`references/module_contracts.yaml`
    `composition_roles:`); its one identity is its directory name (`rosters.yaml` `modules:`).
  * A MODULE ENTRY is a composition row that carries `entry:` -- HOW the loop calls its target:
    `verb_call` (a verb's loop-side adapter calls it, and the row names that verb in `verb:`),
    `step_call` (a loop step calls it) or `query` (a projection consumer calls it). The closed set
    is owned by `tools/export_composition.py::_ENTRIES`, which validates it at export beside
    `kind:`; this module reads the cooked rows through `engine/substrate/composition.py` and never
    re-validates what the exporter owns. A row with no `entry:` is not an entry and is skipped.
  * The REGISTRAR is `register_module_entries()`, and it is the ONLY writer of `MODULE_ENTRIES`.

WHAT IT DOES NOT DO, and each absence is ruled (A-25): it writes nothing to `EFFECTS` or
`PROVIDERS` -- `@effect_for` and `@provider` stay host, so `data/verbs.py::_derive_openers_from_effects`
is untouched; and it imports no module. A target is resolved by STRING, through
`composition.require`, when the driver is constructed and never at import, so importing this module
pulls in no `systems.*`/`modules.*` code
(`tests/valoria/test_engine_does_not_import_systems.py::test_importing_every_engine_module_pulls_in_no_subsystem`).

IDEMPOTENT. `SeasonDriver.__init__` runs it on every construction, and a corpus constructs many
drivers in one process: the same rows give the same table and no refusal. What it REFUSES, naming
the row (the shape of `registry.check_rows()`, `04:1031` -- *"a misspelled manifest row fails at
boot naming the row"*):

  (b) an `entry: verb_call` row whose `verb:` names no verb row;
  (d) one entry registered twice -- one target under two roles, one verb bound by two `verb_call`
      rows, or a role the table already holds bound to a different target;
  and a role the table holds that NO ROW declares. That entry was written by something other than
  this registrar from a row -- a second writer, or a row deleted under a live process -- and a
  table with two writers is the import-time self-registration `ED-IN-0284` records as the measured
  silent drop (`seam/__init__.py`'s own account).

`ID-13`, READ EXACTLY: no production composition row carries `entry:` at `30`, so the pass over
production rows registers nothing until `31a` lands the first; `tests/valoria/test_module_registrar.py`
plants one, each case in a fresh subprocess, because `MODULE_ENTRIES` is a process global another
test's imports could fill.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from ..gaps import Unspecified


@dataclass(frozen=True)
class ModuleEntry:
    """One registered module entry: the composition row's own fields, and the resolved callable."""
    role: str
    entry: str
    verb: Optional[str]
    target: str
    fn: Any


#: `{role: ModuleEntry}` -- THE ONE TABLE. Written by `register_module_entries()` and nothing else.
MODULE_ENTRIES: dict = {}


def _refuse(what: str, needs: str) -> None:
    raise Unspecified(
        what, "04:1031", needs=needs,
        law="04:1031 -- a misspelled manifest row fails at boot naming the row. A-25: a module is "
            "reached by ONE composition row, registered once, by the registrar alone")


def register_module_entries(verb_table: dict) -> list:
    """Register every composition row carrying `entry:` into `MODULE_ENTRIES`; return the roles.

    `verb_table` is the loaded verb table, passed by the caller so this module adds no import edge
    into `data/` (the driver already holds it). Refusals (b) and (d) and the unbacked-entry refusal
    are in the module docstring; each names the row. The returned list is what a caller asserts on
    to see the sweep was not empty (`CLAUDE.md` §0.1 pt 2)."""
    from engine.substrate import composition

    fresh: dict = {}
    by_target: dict = {}
    by_verb: dict = {}
    for role in sorted(composition.ROLES):
        row = composition.ROLES[role]
        entry = row.get("entry")
        if not entry:
            continue
        verb, target = row.get("verb"), row["target"]
        # (b) -- a `verb:` names a verb row, or the adapter that would call this entry does not exist.
        if verb is not None and verb not in verb_table:
            _refuse(f"composition row {role!r} (`entry: {entry}`) names `verb: {verb!r}`, which is "
                    f"no row of verb_table.yaml",
                    needs="the verb row this entry's adapter belongs to, or the row's `verb:` fixed")
        # (d) -- one entry, one row.
        if target in by_target:
            _refuse(f"module entry {target!r} is registered twice, by composition rows "
                    f"{by_target[target]!r} and {role!r}",
                    needs="one composition row per module entry; delete the other")
        if verb is not None and verb in by_verb:
            _refuse(f"verb {verb!r} has two `{entry}` entries, composition rows {by_verb[verb]!r} "
                    f"and {role!r}",
                    needs="one module entry per verb -- which module a verb calls has one answer")
        by_target[target] = role
        if verb is not None:
            by_verb[verb] = role
        fresh[role] = ModuleEntry(role, entry, verb, target, composition.require(role))

    for role, held in MODULE_ENTRIES.items():
        new = fresh.get(role)
        if new is None:
            _refuse(f"MODULE_ENTRIES holds {role!r} ({getattr(held, 'target', held)!r}), which no "
                    f"composition row declares",
                    needs="the composition row back, or the second writer of MODULE_ENTRIES removed "
                          "-- the registrar is its only writer")
        if new != held:
            _refuse(f"module entry {role!r} is registered twice: the table holds "
                    f"{getattr(held, 'target', held)!r} and "
                    f"its composition row now names {new.target!r}",
                    needs="one registration per entry, by the registrar from its row")
    MODULE_ENTRIES.update(fresh)
    return sorted(fresh)
