"""`season.manifest` -- **role -> provider rows, resolved at boot.** One of
`04_CODE_ARCHITECTURE.md` §A.2's nine modules (`04:136`), typed by Stage 2 §D.4 (`04:125`): *"the
seam names a role; a manifest row names the provider; resolved at boot."*

⚠ **THIS MODULE OWNS THE ROLE->PROVIDER RULE ONCE (ED-IN-0206, `CLAUDE.md` §8); IT MINTS NO FOURTH PRIMITIVE.**

| owner | rule |
|---|---|
| `manifest.check_roles()` | the `missing` scan and the `NoProducer` raise; `state/world.py::World.boot` delegates and keeps its signature, because callers hold a `World` |
| `manifest.resolve("contest", prize)` | the `rosters.yaml` x `module_contracts.yaml` crossing, which `seam/contest.py::contest_subsystem` asks, as `04 §C.5` spells it |
| `engine/substrate/composition.py::ROLES` | **a separate registry, not replaced by this module.** It is the ENGINE-wide role->module registry `CLAUDE.md` §3 names, one layer out from the season package |

⚠ **"RESOLVED AT BOOT" IS SATISFIED AT `boot()`, NOT AT IMPORT, AND THE DISTINCTION IS DELIBERATE.**
`04 §D.4` and `04 PART E step 10` want *"a misspelled manifest row fails at boot naming the row"*. Validating at
module import would make every reader of one name pay for `module_contracts.yaml`, which is exactly
what `season/data/__init__.py` and `season/state/__init__.py` both record at length as the reason
this package loads lazily. `boot()` is the boot. `check_rows()` is called from there, and from
`SeasonDriver.__init__`, the one place every run passes (the registrar and the
driver-construction refusals run there too).

**NO PROVIDER ROW IS LANDED HERE.** The row for a social contest is U1's; its provider is the social
contest scene's provider (`social_contest`, `ED-SC-0037`).
This module holds the signature, the crossing and the boot-time failure only.
"""

from .registry import (
    PROVIDERS, call, check_contest_prizes, check_effects, check_graded_tasks,
    check_inquiry_modules, check_preconditions, check_rows, check_roles, has, provider, resolve,
)
# A-25: the REGISTRAR and its one table. `registrar.py`'s docstring defines
# a module entry; `SeasonDriver.__init__` runs it, then the refusals above, on every construction.
from .registrar import MODULE_ENTRIES, ModuleEntry, register_module_entries, require_entries

__all__ = sorted(
    _n for _n, _v in list(globals().items())
    if not _n.startswith("_") and getattr(_v, "__module__", "").startswith(__name__)
)
