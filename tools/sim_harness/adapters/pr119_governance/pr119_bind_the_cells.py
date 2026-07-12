"""pr119_bind_the_cells.py — provisional adapter testing PR#119's §1.3b Bind the Cells /
Goningumi collective liability (ED-SE-0020, designs/territory/governance_play_redesign_v1.md).

The reconciliation doc (designs/audit/2026-07-12-settlement-season-stress-sim/
reconciliation_with_existing_territory_work.md §B.2) sharpens PR#125's "actor cap collision"
finding into three CONFLATED actor granularities: (a) §4.5 Local Actors, a per-settlement-type
COUNT; (b) named NPC dossiers (Goldenfurt carries 9, registry.Settlement.npc_ids is uncapped);
(c) the 5-household population cells §1.3b actually requires — a granularity NO layer models.
This adapter runs that arithmetic against Goldenfurt's REAL npc_ids list (not an invented
count) and Monte Carlo's the collective-liability stacking cascade §1.3b describes.

canon_row=None: §1.3b is PROPOSED, no CURRENT.md row.
"""
from __future__ import annotations

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import build_goldenfurt_settlement

_CELL_SIZE = 5  # §1.3b: "five-household cells"
_REVOLT_STACK = 3  # §1.3b: "Stacking three Collective Liability tags on one cell auto-seeds ... 'Cell Revolt'"


@register_adapter("pr119_bind_the_cells")
class BindTheCellsAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        goldenfurt = build_goldenfurt_settlement()
        params = {
            "goldenfurt_actor_count": len(goldenfurt.npc_ids),  # real, from the fixture
            "cell_size": _CELL_SIZE,
            "revolt_stack": _REVOLT_STACK,
            "seasons": 6,
            "p_infraction_per_cell_per_season": 0.35,
        }
        provenance = {
            "goldenfurt_actor_count": "PROVISIONAL: goldenfurt_fixture.build_goldenfurt_"
                "settlement().npc_ids, read at call time — the real 9 named actors "
                "(designs/territory/goldenfurt_slice/npc_cast.md: 6 NPC dossiers + 3 minor "
                "Local Actors), not an invented count",
            "cell_size": "PROVISIONAL: designs/territory/governance_play_redesign_v1.md "
                "§1.3b — 'partitions the settlement's Local Actors (§4.5) into fixed "
                "five-household cells'",
            "revolt_stack": "PROVISIONAL: same §1.3b — 'Stacking three Collective Liability "
                "tags on one cell auto-seeds a new Crisis-family card, Cell Revolt'",
            "seasons": "test-scenario value, not canon-derived: chosen to give the 3-stack "
                "revolt threshold room to trigger within one trial",
            "p_infraction_per_cell_per_season": "test-scenario value, not canon-derived: "
                "§1.3b states the collective-liability consequence of an infraction, not a "
                "base infraction rate",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="actor_granularity_fit", default_tier=Tier.MINOR,
                branches=["cells_fit_evenly", "cells_remainder"],
                justification="a single deterministic arithmetic check (real actor count "
                               "mod cell size) against Goldenfurt's real npc_ids — tier-1, "
                               "'single check' per the rubric",
            ),
            DecisionPoint(
                name="collective_liability_cascade", default_tier=Tier.MEDIUM,
                branches=["no_stack", "partial_stack", "cell_revolt_triggered"],
                justification="a Disposition-across-the-whole-cell write and a possible "
                               "auto-seeded Crisis card — a settlement-scale, cross-actor "
                               "consequence, tier-2 per the rubric",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "actor_granularity_fit":
            n = params["goldenfurt_actor_count"]
            remainder = n % params["cell_size"]
            branch = "cells_fit_evenly" if remainder == 0 else "cells_remainder"
            n_cells_full = n // params["cell_size"]
            return Outcome(
                decision_point.name,
                {"actor_count": n, "cell_size": params["cell_size"],
                 "full_cells": n_cells_full, "remainder": remainder},
                {"branch": branch},
            )

        if decision_point.name == "collective_liability_cascade":
            n_cells = max(1, params["goldenfurt_actor_count"] // params["cell_size"])
            cell_stacks = [0] * n_cells
            revolt = False
            for _season in range(params["seasons"]):
                for i in range(n_cells):
                    if rng.random() < params["p_infraction_per_cell_per_season"]:
                        cell_stacks[i] += 1
                        if cell_stacks[i] >= params["revolt_stack"]:
                            revolt = True
            if revolt:
                branch = "cell_revolt_triggered"
            elif max(cell_stacks) > 0:
                branch = "partial_stack"
            else:
                branch = "no_stack"
            return Outcome(decision_point.name, cell_stacks, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")
