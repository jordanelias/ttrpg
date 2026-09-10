"""`season.manifest` -- **role -> provider rows, resolved at boot.** One of
`04_CODE_ARCHITECTURE.md` §A.2's nine modules (`04:136`), typed by Stage 2 §D.4 (`04:125`): *"the
seam names a role; a manifest row names the provider; resolved at boot."*

⚠ **THIS MODULE CONSOLIDATES THREE PRIMITIVES THAT ALREADY EXISTED; IT DOES NOT MINT A FOURTH.**
Unit L4 (ED-IN-0206) found the role->provider rule written in three places and this package is where
it lives once (`CLAUDE.md` §8):

| was | now |
|---|---|
| `state/world.py::World.boot` -- the `missing` scan and the `NoProducer` raise, inline on a STORE | `manifest.check_roles()` owns the rule; `World.boot` delegates and keeps its signature, because callers hold a `World` |
| `seam/contest.py::contest_subsystem` -- the `rosters.yaml` x `module_contracts.yaml` crossing, at FIRST CALL | `manifest.resolve("contest", prize)` owns the crossing; the seam asks it, which is `04 §C.5`'s own spelling |
| `engine/substrate/composition.py::ROLES` | **untouched and NOT retired.** It is the ENGINE-wide role->module registry `CLAUDE.md` §3 names, one layer out from the season package. Recorded so a later reader does not read this module as its replacement |

⚠ **"RESOLVED AT BOOT" IS SATISFIED AT `boot()`, NOT AT IMPORT, AND THE DISTINCTION IS DELIBERATE.**
`04 §D.4` and `04:1031` want *"a misspelled manifest row fails at boot naming the row"*. Validating at
module import would make every reader of one name pay for `module_contracts.yaml`, which is exactly
what `season/data/__init__.py` and `season/state/__init__.py` both record at length as the reason
this package loads lazily. `boot()` is the boot. `check_rows()` is called from there.

**NO PROVIDER ROW IS LANDED HERE.** The row for a social contest is U1's, and `ED-SC-0037` rules its
value: `engine/autoload/sigma_leverage.py`, interim, repointed when the proceedings subsystem lands.
This unit lands the signature, the crossing and the boot-time failure only.
"""

from .registry import check_rows, check_roles, resolve

__all__ = sorted(
    _n for _n, _v in list(globals().items())
    if not _n.startswith("_") and getattr(_v, "__module__", "").startswith(__name__)
)
