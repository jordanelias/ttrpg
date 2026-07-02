# Mass-battle movement/pathing audit — 2026-07-02

**Status:** Findings ratified (ED-1094). Implementation NOT started — this is the audit + fix-plan
deliverable; the fix plan below is what a future Sonnet-tier pass executes, gated on the four
decision gates in §4.

**Trigger.** Jordan watched a tick-by-tick visualization of the H4 preset (Envelopment vs
Arrowhead, the engine's Cannae-pattern scenario) and observed: *"the wings just go straight to
the opponent. there is no wheeling/circling/going wider and coming back in."* He then supplied two
annotated reference screenshots describing general maneuver capabilities the pathing system needs
to support — not literally both "the Cannae case":

1. Both wings arc wide away from center first, then curl back in to strike from the flank/rear.
   Text form: *"the wings must go WIDER/further away from centre/their opponent to attack from
   side, and if they are to go from behind, they must literally go behind their opponent... if
   this grid is 0,0 at bottom left, then the wings to encircle must literally be at a smaller x
   than their opponent"* — a genuine rear attack requires crossing past the enemy's own extent
   along the approach axis, not just getting laterally adjacent.
2. An asymmetric case (explicitly **not** Cannae-specific — a general capability requirement):
   *"the left wing goes wide then cuts back in to attack from side; right wing wheels from behind
   to attack from point between center and left wing"* — two different wings can run two different
   maneuver shapes in the same battle, and a wheel's terminal goal can be an interior point between
   friendly bodies, not just "directly behind the enemy centroid."

**Method.** A Fable-5-led read-only diagnostic pass (xhigh effort), independently adversarially
verified per-finding by Opus, then synthesized by Fable into this fix plan (per Jordan's routing
ruling: *"probably a fable proposal but sonnet 5 write"* / *"if fable unavailable... use opus 4.8
max effort"* — Fable was available throughout this run, no fallback used). 16 subagent calls,
zero errors, ~980K subagent tokens, 244 tool calls. Every finding below survived independent
verification (CONFIRMED or PARTIALLY_CONFIRMED — 2 findings had a correction applied, noted
inline; zero REFUTED).

---

## 1. Root cause (confirmed)

Since ED-1089 (2026-07-02, `FIELD_MOVEMENT`/`PC_NODE_COHESION` default flipped ON), every battle
runs on the newer "coordinate-field / node" movement path, `Subunit._node_advance`
(`hierarchy/units.py:554-679`). That path does exactly one thing: each tick it steers the whole
body in a straight line toward the enemy's centroid (`units.py:596-616`). It never reads a
subunit's `instructions` or `role`.

All four real maneuver behaviors — the `envelop` wrap-to-rear (`units.py:821-839`), the `sweep`
flank-march (`units.py:849-861`), the overhang-cell `wheel` (`units.py:807-813`), and ranged
`kite` standoff regulation (`units.py:727-733`) — exist in the code, but all four live in the
OLDER "legacy grid" movement path, which `_node_advance` bypasses via an unconditional early
return at `units.py:719-720`. **The maneuvers aren't missing — they're unreachable in the
configuration that runs by default.** Compounding this, `_node_advance` is a pure centroid
attractor with no file-holding term (the v12 "column-local targeting" design,
`orchestration.py:99-104`, exists only on the legacy path too), so wings converge inward as well
as going straight.

## 2. Corrections to claims made earlier this session

Two things reported as fact before this audit turned out to be wrong or imprecise — corrected here
rather than left standing:

- **The "144-tick total freeze" empirical finding is REFUTED.** A direct H4 re-run at HEAD and
  three preceding commits (`FIELD_MOVEMENT=0 PC_NODE_COHESION=0 PER_CELL=1`, matching the original
  test's toggles exactly) shows substantial normal movement every turn, ending in a draw — the
  "draw" and "144 position snapshots" parts of the original report were real, but "zero movement"
  was not. Best-fit explanation: a measurement bug in the original probe (reading each cell's
  immutable formation-coordinate `id` field instead of its live `pos` field would produce exactly
  this false symptom). No code fix needed for this specific claim.
- **The `reset_positions` "teleports to spawn every turn" claim was imprecise.** The function
  writes only `starting_position`/`cell_offsets`/`cell_offsets_c` — the LEGACY grid fields. On the
  default node path, those fields are never read (`cells()` reads only `_node_pos`), so
  `reset_positions` is a **no-op** there, not an over-eager reset. The real, confirmed bug (see
  finding 1.1) is the opposite failure mode: positions get permanently **frozen at wherever they
  ended turn 1** for the rest of the battle, not reset to spawn. Jordan's underlying design
  correction stands and is more urgent than originally framed: *"an army only has subunits reset
  to initial positions... at the start of a new battle... nonsensical for them to return to
  starting positions within the same battle."*

## 3. Findings (all independently verified; severity as assessed)

| # | Finding | Severity | Verdict |
|---|---|---|---|
| 1.1 | `reset_positions` is a positional no-op on the node/field path — turns 2-8 of a multi-turn battle are welded to the turn-1 contact line (126 of 144 ticks show zero movement) | **critical** | CONFIRMED |
| 1.2 | ED-1093 (mounted-archer kiting) is **not effective**: implicit `role='Kite'` never sets `unit_type='ranged'`; the unit neither kites, nor volleys, nor gets a speed edge, on any path | **critical** | CONFIRMED |
| 1.3 | v12 column-local targeting is dead on the node path — pure centroid attraction, wings converge inward during approach | **high** | PARTIALLY_CONFIRMED (correction: a single `GappedLine` subunit's own internal gap is NOT affected — rigid translation preserves it; convergence is a cross-subunit/wing phenomenon only) |
| 1.4 | The envelop/sweep acceptance validators (`validators.py`) are measuring the dead legacy-path arm since ED-1089 and are wired into no CI — "Stage C.4 passed" claims from earlier this session are true only of the legacy grid | **high** | CONFIRMED |
| 1.5 | Formation drift (`check_drift`) corrupts node state on shape change — cells can teleport to `(0,0)` or stack at the anchor | **high** | CONFIRMED |
| 1.6 | `PER_CELL` still defaults OFF — charge shock, brace recoil, cavalry speed, fatigue, and the ED-1091/ED-1093 gates are all compiled out of the default/visualized configuration | **medium** | CONFIRMED |
| 1.7 | `build_army` silently discards unknown per-subunit spec keys (e.g. the workbench's own `'speed':'Fast'` cavalry-wing spec) | **medium** | CONFIRMED |
| 1.8 | Node-path movement is direction-dependent (L1-normalized): diagonal moves ~29% slower than axis-aligned | **low** | CONFIRMED |
| 1.9 | 12 of 15 `ROLE_SPEC` instruction tokens are consumed nowhere (not "10 of 14" as first reported) | **low** | PARTIALLY_CONFIRMED (count + "pure labels" framing corrected — `shape` fields ARE consumed) |
| 1.10 | `check_orders`: a `tick:N` order fires exactly once per battle, not once per engagement turn (`_order_idx` never re-arms) | **low** | CONFIRMED |
| — | Node WHEEL facing update (`units.py:632-636`) stalls at exact 180° reversal (lerp-normalize degenerates to a zero vector) — exactly the case a wheel-to-rear maneuver needs | (folded into fix plan step 5) | code-read confirmed, not battle-probed |

Full per-finding evidence, citations, and the complete adversarial-verification transcript are in
`findings_full.json` (the raw Workflow output) alongside this README.

## 4. Decision gates — Jordan rulings needed before the code below can land

1. **Multi-turn re-arm semantics.** Does each engagement turn re-hold stance / re-arm orders /
   reset instructions for a fresh approach each turn, or do turn-1 releases latch for the whole
   battle? Governs both the `reset_positions` fix (step 2) and the once-per-battle order behavior
   (finding 1.10).
2. **Where `unit_type='ranged'` lives** for the Kite role — a `unit_type` field in `ROLE_SPEC`
   entries, or a `ranged` flag on the troop type. Gates fix step 3 (ED-1093 repair).
3. **Waypoint transit facing policy.** During a wide-out leg, does the body face its movement
   goal, the enemy, or slew between them? The current WHEEL conflates steering target and facing
   target; Image 1's arc makes them differ for many ticks.
4. **Should `PER_CELL` flip to `'1'` alongside ED-1089's field flip?** Independent of the maneuver
   chain, but decides what the flagship visualization actually shows.

## 5. Fix plan (dependency-ordered; Sonnet-executable once gates above are answered)

1. **Fix `check_drift` node-state re-keying** — independent, low-risk, do first (prevents a
   discipline-degrading wing from corrupting `cells()` mid-maneuver and poisoning every later test).
2. **Teach `reset_positions` to reset node state** — gated on decision gate 1.
3. **Wire ED-1093's `unit_type='ranged'` via `ROLE_SPEC` data** (no entity special-casing) — gated
   on decision gate 2. Note: fixes only the DATA half; actual kiting/standoff steering still
   requires step 7.
4. **Restore a lateral file-holding term in `_node_advance`** (port v12) — prerequisite for Image 1.
5. **Fix the node WHEEL's 180° facing stall** — needed for correct rear-attack facing; gated on
   decision gate 3 for the transit-facing question.
6. **Re-point the maneuver acceptance validators at the node path and land them as an executable
   CI gate**, initially RED — the measurement instrument; land BEFORE step 7 to avoid repeating
   the "Stage C.4 passed on the dead path" mistake.
7. **Add the waypoint primitive to `_node_advance`** — the actual Image 1 / Image 2 capability. A
   per-subunit ordered list of `(goal-function, completion-predicate)` pairs consumed ahead of the
   `target_centroid` fallback, modeled directly on the legacy `envelop` two-state machine (already
   a proof-of-concept of exactly this pattern in-repo). Depends on steps 2, 4, 5, 6.
8. **Lower-severity hardening** (parallelizable, after the capability lands): `build_army`
   unknown-key validation, L1→L2 node normalization (defer unless proven necessary — widest
   field-digest blast radius for the smallest gain), ROLE_SPEC instruction-consumer documentation.

**Re-verification burden (not free):** fix steps 2, 4, 5, 7 all change the `bat.py` field digests
(`unit_field`/`cell_field`) — each requires a deliberate, Jordan-signed re-record, since those
digests currently embed the broken behavior. `gauge_mb.py` multi-mode historical bands likely need
a full field-path re-run once turns 2+ genuinely re-approach. The CI **grid** digests (toggles OFF)
are safe by construction throughout — every fix here lives inside `_node_advance`/the node path,
which the grid digests never enter. No fix may invent a new magnitude (clearance/margin/rear-offset
values must derive from `standoff_from_reach`, `COL_WIDTH`, enemy extent, the legacy envelop's `+2`
frontage margin, `BATTLEFIELD_SIZE` — `TROOP_TYPE_REACH` stays empty).

## 6. Path-length budget ruling (Jordan, mid-audit)

Binding on step 7's waypoint primitive: *"use a formula based upon like
0.5×speed×maximum-ticks-in-battle that determines the maximum length of the pathing route that is
allowed to be determined with node placements"* — undeliverable paths are rejected at design time,
never silently truncated. Formula shape + the 0.5 factor are Jordan-ruled; operands derive from
existing primitives (`cell_speed`, `PC_CAVALRY_SPEED_MULT=2.0` — which emergently doubles cavalry's
path budget with zero extra tuning — `TICKS_PER_PHASE=6`, `max_turns=18`/turn, `max_battle_turns=8`).
The **T** operand (max-ticks) was initially mis-scoped to 18 (one engagement turn) based on the
now-corrected `reset_positions` premise in §2 — once step 2 lands, T is the full multi-turn battle
window, not one turn. No new constants may be invented for the operands.
