"""THE FIELDWORK CONTAINER'S PROVIDER -- the host adapter and the host INPUT BUILDER for the `fieldwork`
module's entry (v9 FI-02 + FI-03, `SM-3`, `ED-FI-0002`), registered as `@provider("inquiry", "fieldwork")`:
the second role in `manifest/registry.py::_ROLE_ROSTERS`, whose rows (`rosters.yaml: inquiry_modules`) are
keyed by the KIND a finding emits. Jordan, 2026-09-05 (SM-3): *"investigation is not a contest seam. it is
its own thing."*

It DECIDES NOTHING. `fieldwork_input` (the host input builder) projects the trail an inquiry can uncover
(`epistemic.trail_of`) and freezes it, with the finding's degree and `rosters.yaml: finding_terms`, into
`queries/inputs.py::FieldworkInput`; `find` (the adapter) calls the module entry the row names
(`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its composition row) and holds its return to
`Findings`. What a finding uncovers is `modules/fieldwork/find.py`'s; what the finder then HOLDS is
WITNESS's (`loop/witness.py`'s found deposit), as what a witness holds is.

⚠ THE PLACEMENT QUESTION, ADJUDICATED AT THE SITE RATHER THAN ASSUMED (`sigma.py`'s precedent, and its
form). `04_CODE_ARCHITECTURE.md` §A.2 types `seam/wrappers/*` as CONTEST provider adapters: they write
*"nothing, ever"*, read *"the projection"*, return *"a `Margin`"*, hold token *"none"*. This module is
not a contest provider and returns no `Margin`. Two readings were available: **(i)** it is a wrapper BY
ROLE -- it writes nothing, reads a projection, holds no token, and returns the typed record its module
returns, which is that row's contract with the record's type generalised from one role to two; **(ii)**
§A.2's row is a contest-only row, and a second role's adapter is a new row the document must gain. **This
unit takes (i)** and states the deviation for amendment: column 3, *"a `Margin`"*, is met by its analogue
(`Findings`, held at the module boundary as `sigma.py` holds `Margin`), and nothing else in the row moves.
A second deviation lives with the caller: `loop/witness`'s may-read column (`04` §A.2) does not list a
driver-held `findings` store, and the found deposit reads one (`SeasonDriver.findings`, `act_of`'s shape:
event-keyed, driver-owned, resolver-side). Both are Layer 1 amendments, recorded and NOT made here.

⚠ THIS MODULE IMPORTS NOTHING FROM `systems/` OR `modules/` AND INSERTS NO `sys.path`. The entry is
reached by STRING, through `MODULE_ENTRIES`, as `sigma.py`'s is. A call reaching here before any driver
was constructed in the process finds the role unregistered: `ENGINE-UNAVAILABLE`, the shared typed refusal.
"""
from __future__ import annotations

from typing import Any

from ...data.rosters import FINDING_TERMS
from ...epistemic import act_refs, trail_of
from ...gaps import Unspecified
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT, for `sigma.py`'s reason (no import here closes a loop).
from ...manifest.providers import provider
from ...queries.inputs import FieldworkInput, Findings, TrailItem
from ._entry import entry_for

# The `inquiry_modules` rows' `provider:` string: the module's one identity (A-25). Reached by it only.
_PROVIDER = "fieldwork"


def fieldwork_input(w: Any, act: Any, event: Any) -> FieldworkInput:
    """THE HOST INPUT BUILDER: `World` -> the frozen record `find` reads.

    The finder is the inquiry's actor; what he inquired into is what the act names (`act_refs`, the one
    owner of *what is this act about*); the band is the finding Event's degree, which the one ladder
    decided (`None` for an ungraded finding, which `finding_terms` keys nothing for). `terms` is the
    table itself, copied: the module picks the band's row, so no band is read here."""
    refs = act_refs(act)
    trail = trail_of(w, refs[0] if refs else None, act.actor)
    return FieldworkInput(band=event.degree,
                          items=tuple(TrailItem(e.id, e.kind, e.emitted_at) for e in trail),
                          terms=dict(FINDING_TERMS))


@provider("inquiry", _PROVIDER)
def find(w: Any, act: Any, event: Any, *, module_entry: Any = None):
    """One finding -> the module's `Findings`, or the `ENGINE-UNAVAILABLE` dict when the entry is not
    registered. ⚠ A RETURN THAT IS NOT `Findings` RAISES, NAMING THE ENTRY: a module that hands back
    anything else is a software defect, never a game outcome (`sigma.py::resolve`'s `Margin` hold)."""
    inp = fieldwork_input(w, act, event)
    entry, refusal = entry_for(None, _PROVIDER, module_entry)
    if entry is None:
        return refusal
    out = entry.fn(inp)
    if not isinstance(out, Findings):
        raise Unspecified(
            f"module entry {entry.role!r} ({entry.target}) returned {type(out).__name__} "
            f"{out!r:.120}, which is not `Findings`", "ED-FI-0002",
            needs="the entry returning `queries.inputs.Findings(found)`",
            law="A-25 -- the host reads the typed record its module returns; an untyped return is a "
                "second contract nobody declared")
    return out
