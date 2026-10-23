"""HOUSING -- the `settlements` module's `settlements.housing` entry (A-25; v9 IN-07 E4).

MODULE ENTRY: reached by the composition row whose target is `housing` below (`entry: query` -- the
projection wrappers `queries/world_q.py::population` and `capacity` call it), registered in
`manifest.MODULE_ENTRIES` at driver construction and held there by `manifest/registrar.py::require_entries`
against the host's declared need (`queries/world_q.py::QUERY_ENTRIES`). The host reaches it by role string
through `engine.substrate.composition.require`, because `capacity` has a driverless caller
(`harness/populated.py`, seating cohorts at world-gen).

It takes the host's typed input record and returns a typed output record, imports the record types and
nothing else, never reads or writes `World`, holds no token and keeps no state. `residence_of` (with its
two-edge `Forbidden`), the public wrappers with their `TRACE.query` lines and `_eff_migrate`'s refusal
(`population + weight > capacity`, an effect body) stay host.

THE RULE (moved here from `world_q.population` and `world_q.capacity`; unchanged clause for clause):
  * POPULATION: the summed `Person.weight` of the residents whose residence lies in the subtree --
    RESIDENTS, not persons present (RR-2); `weight`, not a head count (a cohort fills `weight` places).
  * CAPACITY: `max(floor, the dwelling Sites whose own rung lies in the subtree)` (`ED-SE-0051`): a rung
    with no dwelling still houses the floor, and one more dwelling raises the rung and every ancestor.
  * A half whose inputs are `None` was not projected and is answered `None`.
"""
from __future__ import annotations

from engine.season.queries.inputs import Housing, HousingInput


def housing(inp: HousingInput) -> Housing:
    """The subtree's population and capacity, each from its own half of the record."""
    population = None
    if inp.residents is not None:
        population = sum(weight for _pid, home, weight in inp.residents if home in inp.subtree)
    capacity = None
    if inp.dwelling_rungs is not None:
        built = sum(1 for rung in inp.dwelling_rungs if rung in inp.subtree)
        capacity = max(inp.floor, built)
    return Housing(population, capacity)
