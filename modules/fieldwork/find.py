"""WHAT A FINDING UNCOVERS -- the `fieldwork` module's entry (A-25; v9 FI-02 + FI-03, `SM-3`,
`ED-FI-0002`), the automated mode of the fieldwork container.

A MODULE ENTRY: reached by the composition row whose target is `find` below (`entry: step_call` -- RESOLVE's
per-act bookkeeping calls it for an Event an inquiry produced, not a verb's adapter), registered in
`manifest.MODULE_ENTRIES` by the registrar at driver construction, and called by the host adapter
`seam/wrappers/fieldwork.py::find` -- the `@provider("inquiry", "fieldwork")` that
`rosters.yaml: inquiry_modules` names for the kind a finding emits.

It takes the host's typed input record and returns a typed output record, and imports the record types,
nothing else. It never reads or writes `World`, holds no token and keeps no state between calls. IT TAKES
NO RNG BECAUSE IT DRAWS NOTHING (A-25 rule 3, *rng is a parameter*, met trivially): the roll that decided
the band is the inquiry's, `social_contest.roll`'s through FI-01's route, one roll owner (S27.2). A
playable mode that draws takes its generator as a parameter, as `roll(inp, rng)` does.

THE RULE, AUTOMATED MODE: the band's terms are `inp.terms[inp.band]`; a band with none uncovers nothing.
Otherwise every trail item the host projected is uncovered, showing those terms, in `(emitted_at,
event_id)` order. WHICH items exist is the host's projection (`epistemic.trail_of`); what the band decides
is HOW MUCH of each the finder learns. ⚠ THIN BY DESIGN, AND SAID SO: the module applies a band-to-terms
table to a list. What it buys is the seam a PLAYABLE fieldwork mode attaches at (A-25: the host gets the
same typed output either way).
"""
from __future__ import annotations

from engine.season.queries.inputs import FieldworkInput, Findings


def find(inp: FieldworkInput) -> Findings:
    """One finding -> `Findings`: `(event id, terms shown)` per uncovered trail item, or nothing."""
    shown = tuple(inp.terms.get(inp.band) or ())
    if not shown:
        return Findings(())
    items = sorted(inp.items, key=lambda t: (t.emitted_at, t.event_id))
    return Findings(tuple((t.event_id, shown) for t in items))
