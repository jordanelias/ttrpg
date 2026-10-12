"""`seam/wrappers/_entry.py` -- the module-entry lookup the three providers share.

A provider calls the module entry its prize row names (`module_entry:`), found in
`manifest.MODULE_ENTRIES`, which the registrar fills at `SeasonDriver` construction. A call reaching
a provider before any driver was constructed finds the role unregistered; that is the typed
`ENGINE-UNAVAILABLE` refusal, never a direct import of the module.

⚠ A LEAF, AS THE WRAPPERS' OWN IMPORTS ARE: `manifest.registrar` and `manifest.registry` are imported
by module, not through the `manifest` package. `registrar.py` imports only `gaps`; `registry.py`
imports `data/` and `gaps`; neither imports `seam/`, so no import here closes a loop back into it."""
from __future__ import annotations

from typing import Any

from ...manifest.registrar import MODULE_ENTRIES
from ...manifest.registry import resolve as prize_row


def entry_for(prize: Any, module: str) -> tuple:
    """`(entry, None)` when the prize row's `module_entry:` role is registered, else
    `(None, refusal)` with `refusal` the `ENGINE-UNAVAILABLE` dict naming `module`."""
    role = (prize_row("contest", prize) or {}).get("module_entry")
    entry = MODULE_ENTRIES.get(role)
    if entry is not None:
        return entry, None
    return None, dict(status="ENGINE-UNAVAILABLE", module=module,
                      why=f"prize {prize!r} names module entry {role!r}, which MODULE_ENTRIES does not "
                          f"hold -- the registrar fills it at SeasonDriver construction")
