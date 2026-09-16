# Orphaned-mechanics audit — mass-battle engine (2026-07-24)

Triggered by finding `perimeter.py` (the target-point/normal primitive, task #18) built but never wired.
Jordan directive (immutable): **built work is ratified and wired by default; no deferring as "Jordan-gated
follow-up."** This is the full inventory of built-but-dead code, with wiring status.

## Modules built, never imported by the live engine
| module | what it is | status |
|---|---|---|
| **`perimeter.py`** | target-points (face midpoints + corners) + outward normals; `nearest_target`, `approach_alignment` | **WIRED (ED-MB-0035)** into `_envelop_goal` (infantry flank face targeting) |
| `provenance.py` | primitive-provenance registry seed; "does NOT touch the engine … CI cross-check is a later stage" | dead data seed — CI cross-check unbuilt |
| `lanchester_signature.py` | P-L linear/square-law regression script | standalone test script (run via `__main__`) |
| `validators.py` | historical-goal top-down validator harness (`v_cannae`/`v_shock`/…) | test/validation-only harness |
| `workbench/{server,trace}.py` | viz HTTP server + trace runner | standalone tooling |
| `bat.py` | byte-exact golden-digest CLI | oracle runner (correct) |

## Dead / disabled MECHANICS (ranked by significance)
1. **`PC_ENVELOP_SIGMA = 0.0`** (hardcoded "DISABLED") — `_envelopment_sigma` computes the enveloper's
   overhang bonus **every tick then multiplies by zero**. *Status:* left 0.0 — its Incr6 implementation
   IDs the "wider" side by unit-level col-grid width, which **mis-targets a split envelop army** (thin
   wings read as narrower than the single enemy line → naive enable rewards the DEFENDER, measured C7
   100→20). Needs per-CONTACT overhang targeting — folded into the envelopment rebuild, NOT deferred.
2. **`PC_FACING_MODEL`** (+ `PC_FACING_ATTENTION/SLEW_BASE/FOV_GATE/ROUT`) — the entire graded turn-to-face
   / rear-blind-arc / rout-away-facing reaction layer, and the helper **`_slew_facing`**, are **dead by
   default** (master gate off; `PC_FACING_SLEW_BASE` tagged "CALIBRATED-DEBT, NOT ratified, do not
   enable"). *Status:* FLAGGED for Jordan — this one carries an explicit prior "do not enable", so it is
   the one place I'm checking before flipping (calibration debt, not a clean wire-up).
3. **`PC_WHEEL`** overhang-wheel-to-flank — default ON but its only consumer sits in `advance_cells`
   **after** the node-path early-return, so it **never fires** on the default (field) path; no node-path
   equivalent. *Status:* superseded in practice by the ED-MB-0035 perimeter flank targeting + orbital
   wheel; the standalone overhang-wheel is redundant — mark for removal or node-port in the rebuild.
4. **`B6`** multi-side shock computed per cascade sub-phase (a front+rear body saw 1 face/call) — **WIRED
   (ED-MB-0035):** `_compute_atom_sides` now runs once on the full tick and threads into every sub-phase.

## Dead config constants (structural, low risk)
`PC_FLANK_DEPTH_RESIST`, `PC_REFILL_FLOOR`, `PC_ROTATE_FLOOR`, `MORALE_EROSION_DAMP`,
`ROUT_EXHAUSTION_MORALE_HIT`, `ROUT_FLOOR_LOSS_PCT`, `SUBUNIT_ROUT_FLOOR` (unenforced), `MAX_TROOPS_PER_UNIT`,
`BUFFER_CELLS`, `UNIT_GRID_SIZE`, `REACH_LONG` (troop_types/registry) — defined/exported, never read by
the engine. *Status:* triage in the rebuild — wire the ones with intended mechanics (the rout floors, the
rotate/refill floors → the rotation model T1–T3), drop the truly structural-legacy ones.

## Wired this session (ED-MB-0035)
- `perimeter.py` → `_envelop_goal` (infantry turns onto the enemy's nearest FLANK face).
- **Orbital wheel** (`_envelop_wheel_goal`) — cavalry maintains `ENVELOP_STANDOFF` radius and wheels to the
  enemy REAR, then closes (Jordan's "maintain distance … radius … defines wheeling"). C4 cav-envelop
  **6 → 83** (into band 75-95); C7 holds 100.
- B6 multi-side-on-full-tick.
