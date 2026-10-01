"""engine/substrate/canon_buckets.py — continuous → canonical-index bucketing helpers.

Relocated `canonical_accord` out of `engine/autoload/game_state.py` (OI-52a, ED-IN-0097,
`audit/2026-07-29-code-shape-open-items/01_orchestration_plan_v1.md` §3 Wave 4 item 2, 2026-07-29 --
path unresolved after the `audit/` -> `.audit/` rename, ED-IN-0231; the surviving `.audit/` corpus
carries no directory by this name).

WHY. `structure_audit.py` flagged a 2-node import cycle: `engine.autoload.game_state` lazily
imports `systems.world.sim.npe.NPC` inside `restore_world` (game_state.py:370), and
`systems.world.sim.npe` lazily imported `game_state.canonical_accord` inside
`_ecology_weights` (npe.py:184, the ONLY thing npe.py imported from game_state at all). Both
edges were already function-local — no runtime import-time deadlock — so this was a
graph-hygiene defect, not a live bug, but `structure_audit`'s cycle census still counts it.

`canonical_accord` is a small pure function: it takes a `float` and returns an `int` via fixed
threshold comparisons, with no dependency on `game_state`'s `World`/`Territory`/`PT_MAP`/
`ACCORD_MAP` state at runtime (its docstring documents the `ACCORD_MAP` thresholds it mirrors,
it does not read the dict). That makes it a substrate-tier leaf both `game_state` and `npe` can
import at module top level without recreating the cycle: `engine/substrate/` already has no
internal dependents (see `engine/substrate/stubwire.py`; `keys.py`, the other worked example this
line used to cite, retired under ED-IN-0232), so adding
this here breaks the npe→game_state edge outright rather than merely deferring it.

`game_state.py` re-exported `canonical_accord` from here so every existing importer of
`engine.autoload.game_state.canonical_accord` kept working unchanged — a pure relocation.

[29b, 2026-10-01] `game_state.py` is DELETED (plan position `29b`), and with it the re-export and its
sibling `canonical_pt`, which was never moved here: its only two importers, `systems/overview/sim/ci_track.py`
and `systems/factions/sim/mass_seizure.py`, were deleted in the same commit, so there was nothing to move it
for. The one retained reader of `canonical_accord` is `systems/world/sim/npe.py`, which leaves at `29d`;
that deletion leaves this module with no reader. (This block is padded to the line count of the text it
replaced so archived flow-skeleton anchors into this file's code lines stay in range.)




"""
from __future__ import annotations


def canonical_accord(continuous_accord: float) -> int:
    """Map continuous Accord (range 0.5-7.0 per `game_state.ACCORD_MAP`) → canonical integer 0-4.
    ACCORD_MAP: 1.0, 2.5, 4.0, 5.5, 7.0. Midpoints: 1.75, 3.25, 4.75, 6.25.

    Uses nearest-neighbor with midpoints between successive canonical floats — direct `int()`
    drifts (e.g. `t.accord=5.5` is canon Accord 3, but `int(5.5)=5` falsely reads as bucket 4)."""
    if continuous_accord < 1.75: return 0
    if continuous_accord < 3.25: return 1
    if continuous_accord < 4.75: return 2
    if continuous_accord < 6.25: return 3
    return 4
