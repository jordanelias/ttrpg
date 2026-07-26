# Workbench — mass_battle

**node:** engine-live · resolver `dice_pool` · doc `systems/mass_battle/mass_battle_v30.md`

**responsiveness:** 0/4 engine edges co-mentioned in prose (heuristic)

| ENGINE (warp — what the contracts wire) | PROSE (weft) |
|---|---|
| emits `scene_outcome.battle_concluded` (dangling — unconsumed) | _✗ silent_ |
| emits `scene.battle_concluded` → faction_state | _~ mentioned (endpoint only)_ |
| emits `scene.battle_concluded` → npc_behavior | _✗ silent_ |
| emits `scene.battle_concluded` → piety_track | _~ mentioned (endpoint only)_ |

## Divergence cards — 4 open · 0 resolved
_Each card is an iteration point. Resolve by moving EITHER side (articulate the prose, or change the engine); record the answer in `references/observatory_dispositions.yaml`._

- **[unspecced_wiring]** `wb-00aeffeb7f` — Engine wires mass_battle emits [scene_outcome.battle_concluded] scene_outcome.battle_concluded; prose is 'silent'. Articulate it in the design — or should the engine not do this?
  - prose: _silent_ (medium (endpoint absent from doc))
- **[unspecced_wiring]** `wb-a5297ca67a` — Engine wires mass_battle emits [scene.battle_concluded] to faction_state; prose is 'mentioned'. Articulate it in the design — or should the engine not do this?
  - prose: _mentioned_ (medium (endpoint present, relationship term absent))
- **[unspecced_wiring]** `wb-aed4c97e25` — Engine wires mass_battle emits [scene.battle_concluded] to npc_behavior; prose is 'silent'. Articulate it in the design — or should the engine not do this?
  - prose: _silent_ (medium (endpoint absent from doc))
- **[unspecced_wiring]** `wb-bc5fee87ac` — Engine wires mass_battle emits [scene.battle_concluded] to piety_track; prose is 'mentioned'. Articulate it in the design — or should the engine not do this?
  - prose: _mentioned_ (medium (endpoint present, relationship term absent))

_Prototype (R1). Prose matching is heuristic co-occurrence (word-boundary literal + namespace-stripped phrase, proximity-gated), confidence-tagged — a LEAD, not a verdict. Precise articulation detection needs the program §3 canonical-identifier registry. MEASURES, never gates._