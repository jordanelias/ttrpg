"""A FIELD'S PROVISION -- the `settlements` module's `settlements.provision` entry (A-25; v9 IN-52, the
levy-to-field feed).

MODULE ENTRY: reached by the composition row whose target is `provision` below (`entry: query`), called
by the field adapter `seam/wrappers/mass_battle.py::resolve` once per side through
`engine.substrate.composition.require`, registered in `manifest.MODULE_ENTRIES` at driver construction and
held there by `manifest/registrar.py::require_entries` against the host's declared need
(`queries/world_q.py::QUERY_ENTRIES`).

It takes the host's typed input record and returns a `Provision`, imports the record types and nothing
else, never reads or writes `World`, holds no token and keeps no state.

THE RULE [ASSUMPTION LF-1, delegated-ruled]: a levied treasury PROVISIONS a field; it does not create
troops. Troops stay people, and the stores bound how many of them can be fielded, at the larder's own
ration (`subsistence_weight`: a field eats as the people it is made of eat).
  * `on` false -- the control arm: `troops = weight`, `consumed = ()`, today's field.
  * `on` true  -- `troops = min(weight, min over kinds with ration > 0 of stores[k] // ration[k])`, never
    below 0 (a treasury driven negative fields nobody rather than a negative force), and
    `consumed = ration[k] * troops` per kind with ration > 0, in ration order. A kind the treasury does not
    hold counts as 0 units. A zero debit is left out: it would add a `kind: 0` key to `Rung.stores`
    and move the digest for nothing. A ration with no positive kind bounds nothing (`troops = weight`).
An unprovisioned side fields `troops = 0`; massbattle's crash floor (`_MIN_TROOPS`) lifts it to one
[ASSUMPTION A16]: a floor, not a refusal.
"""
from __future__ import annotations

from engine.season.queries.inputs import Provision, ProvisionInput


def provision(inp: ProvisionInput) -> Provision:
    """The troops a side can field on its treasury, and what fielding them consumes."""
    if not inp.on:
        return Provision(inp.weight, ())
    eats = tuple((k, r) for k, r in inp.ration if r > 0)
    if not eats:
        return Provision(inp.weight, ())
    held = dict(inp.stores)
    troops = max(0, min(inp.weight, min(held.get(k, 0) // r for k, r in eats)))
    return Provision(troops, tuple((k, r * troops) for k, r in eats if r * troops > 0))
