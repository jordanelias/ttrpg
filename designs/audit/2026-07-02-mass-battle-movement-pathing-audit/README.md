# Mass-battle movement/pathing audit — 2026-07-02

**Status:** Findings ratified (ED-1096). Implementation NOT started — this is the audit + fix-plan
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
| 1.2 | ED-1095 (mounted-archer kiting) is **not effective**: implicit `role='Kite'` never sets `unit_type='ranged'`; the unit neither kites, nor volleys, nor gets a speed edge, on any path | **critical** | CONFIRMED |
| 1.3 | v12 column-local targeting is dead on the node path — pure centroid attraction, wings converge inward during approach | **high** | PARTIALLY_CONFIRMED (correction: a single `GappedLine` subunit's own internal gap is NOT affected — rigid translation preserves it; convergence is a cross-subunit/wing phenomenon only) |
| 1.4 | The envelop/sweep acceptance validators (`validators.py`) are measuring the dead legacy-path arm since ED-1089 and are wired into no CI — "Stage C.4 passed" claims from earlier this session are true only of the legacy grid | **high** | CONFIRMED |
| 1.5 | Formation drift (`check_drift`) corrupts node state on shape change — cells can teleport to `(0,0)` or stack at the anchor | **high** | CONFIRMED |
| 1.6 | `PER_CELL` still defaults OFF — charge shock, brace recoil, cavalry speed, fatigue, and the ED-1091/ED-1095 gates are all compiled out of the default/visualized configuration | **medium** | CONFIRMED |
| 1.7 | `build_army` silently discards unknown per-subunit spec keys (e.g. the workbench's own `'speed':'Fast'` cavalry-wing spec) | **medium** | CONFIRMED |
| 1.8 | Node-path movement is direction-dependent (L1-normalized): diagonal moves ~29% slower than axis-aligned | **low** | CONFIRMED |
| 1.9 | 12 of 15 `ROLE_SPEC` instruction tokens are consumed nowhere (not "10 of 14" as first reported) | **low** | PARTIALLY_CONFIRMED (count + "pure labels" framing corrected — `shape` fields ARE consumed) |
| 1.10 | `check_orders`: a `tick:N` order fires exactly once per battle, not once per engagement turn (`_order_idx` never re-arms) | **low** | CONFIRMED |
| — | Node WHEEL facing update (`units.py:632-636`) stalls at exact 180° reversal (lerp-normalize degenerates to a zero vector) — exactly the case a wheel-to-rear maneuver needs | (folded into fix plan step 5) | code-read confirmed, not battle-probed |

Full per-finding evidence, citations, and the complete adversarial-verification transcript are in
`findings_full.json` (the raw Workflow output) alongside this README.

## 4. Decision gates — RESOLVED (Jordan, 2026-07-02)

All four gates answered. **Gates 1 and 3 are not parameter choices — they specify new mechanics
beyond the original 8-step fix plan's scope.** Recorded verbatim, then translated into concrete
implementation notes. Where Jordan specified a *relationship* but not a *magnitude*, that magnitude
is marked **PROPOSED, not ratified** — per this repo's evidentiary-primitive discipline, a formula
gets proposed and confirmed, never silently invented and shipped.

### Gate 1 — Command/Discipline-gated conditional tactics (NEW SYSTEM)

> "Army configuration allows you to set roles and tactics for subunits. Battle turns allow you to
> issue directives to change to a new role or tactic, but (a) the speed at which the changes occur
> is affected by command rating, (b) the effectiveness of following new role/instructions is
> affected by subunit's discipline. The further you deviate from the originally assigned role and
> instructions, the worse the performance overall for that subunit. Note that we need to allow for
> conditional tactics/roles so that a bulwark block can reorganize into an arrowhead under certain
> conditions, mounted archers can transition from holding a block into kiting, etc. The number of
> options for alternate roles/instructions should be gated by command rating as well, ie if you
> have poor command your subunits can only do one role/instruction as trained well but if you have
> high command your subunits could do three different variants."

**Reframes fix-plan step 2 and finding 1.10 entirely** — this is not "does `reset_positions` reset
or not," it's "what does a mid-battle directive actually cost and how well is it executed." A
subunit has an **assigned (trained) role/instruction package** set at Army Configuration, plus up to
N **conditional variants** (Command-gated count) each with its own trigger predicate — this
generalizes the existing `Order(trigger, behavior)` primitive (`hierarchy/units.py:~203`,
`core/contact.check_orders`) rather than inventing a new one: "conditional tactics" = pre-declared
`Order`s; "directive mid-battle" = a player-issued `Order` inserted live. Two NEW effects layer on
top of what `Order`/`check_orders` already do:

- **(a) Transition speed, gated by Command.** A role/instruction change is not instantaneous —
  it takes T ticks to complete, T decreasing with Command. **PROPOSED formula** (derived only from
  the already-ratified Command clamp bounds, `derive_command` → 1..7, ED-899/PP-504 — no new
  constant invented): `transition_ticks = max(1, 8 - Command)` (Command 1 → 7 ticks; Command 7 →
  1 tick). Mirrors the existing `PC_BRACE_SETUP_DELAY` "N ticks of continuous state before it
  counts" pattern (ED-1095/T2), generalized from a fixed 1-tick delay to a Command-scaled one.
- **(b) Effectiveness during transition, gated by Discipline.** While *actively transitioning* (the
  T-tick window above), the subunit executes at reduced effectiveness — not the trained role's full
  performance, not yet the new role's either. **PROPOSED**: a multiplicative combat-pool penalty
  during the transition window, scaled by `(1 - discipline/DISCIPLINE_MAX)` — reuses the existing
  discipline-as-0..N-scale convention (`TROOP_TYPE_STATS` discipline values already range ~1-6) and
  the existing multiplicative-pool-penalty idiom (`_stamina_pool_penalty`, `core/exchange.py`)
  rather than a new mechanism class. Effectiveness returns to full once the transition completes —
  this is a **temporary** cost, not a permanent one; "the further you deviate... the worse the
  performance" is read as "the bigger the transition (return-to-trained-role vs. a never-before-
  used variant), the more this penalty bites," not as a permanent debuff.
- **(c) Variant-slot count, gated by Command.** Max number of conditional variants (including the
  trained default) a subunit may carry. **PROPOSED**, using only the ratified 1..7 Command range
  split into thirds: Command 1-3 → 1 slot (trained role only, no conditionals); Command 4-5 → 2
  slots; Command 6-7 → 3 slots.
- Explicit design examples confirmed in scope: a bulwark-block subunit reorganizing into an
  Arrowhead under a condition (a shape-changing conditional — composes with fix-plan step 1's
  `check_drift` node-state fix, since a shape change mid-battle is exactly what that step protects);
  mounted archers transitioning from a holding block into kiting (a role/instruction-changing
  conditional, not a shape change).

**Status: mechanism design captured; the three PROPOSED formulas above need Jordan confirmation
before implementation** (this is new design surface, not a bug fix — treating it with the same
"propose, don't fabricate" discipline as Stage F's D1 actor-gate earlier this session).

### Gate 2 — `ranged` derives from the troop's assigned weapon; `kite` is weapon-independent

> "Ranged is troop type as per the weapon assigned to troop. Kite is a behaviour of attacking an
> opponent then fleeing upon countering, which means that it is BEST done with ranged weapons like
> a bow but can still be executed by cavalry with spears/lances."

**Fully specified, ready to implement, corrects the originally-proposed fix.** Two separate things,
previously conflated:
- `unit_type` ('ranged'/'melee') must derive from the troop type's **assigned weapon**, not from the
  role. `tests/sim/mass_battle/equipment/weapons.py` already has exactly this primitive —
  `ARSENAL` entries carry a `reach` field valued `'melee'`/`'ranged'` (`weapons.py:23,34-40`) — and
  its own docstring says "NOT YET WIRED into resolution." Fix: add a `TROOP_TYPE_WEAPON` mapping in
  `troop_types/registry.py` (e.g. `archers→bow`, `crossbow→crossbow`, `sling→sling`,
  `artillery→siege`, everyone else → a melee weapon), and derive `unit_type` from
  `weapons.get(TROOP_TYPE_WEAPON[troop_type]).reach` in `build_army`/`build_unit` when not
  explicitly overridden by the caller (same override-precedence pattern already used everywhere
  else in `build_army`).
- The `kite` **instruction's steering/behavior must not hard-require `unit_type=='ranged'`** — a
  lance-armed cavalry subunit can execute the same attack-then-flee-on-counter pattern. The
  `unit_type=='ranged'` gate (`units.py:727`) stays as a gate on **volley fire during the kite**
  (only a ranged weapon shoots while disengaging), not on whether `kite` steering itself functions.

### Gate 3 — Body facing follows the movement path; attention/FOV target-locks (facing/FOV SPLIT)

> "The unit's face their movement path, but their field of vision is turned towards their target.
> So this means that while they are very responsive to adjust subformation/movement
> pattern/whatever if archers launch an attack at them, their sides are still exposed."

**Splits a currently-unified vector into two.** Confirmed by direct read: `_node_facing`/
`cell_facing_vec` (`units.py:522,629-637,696-699`) is today the SAME vector driving both (i) the
octagon zone / damage-vulnerability calc and (ii) the FOV gate on reach (`_effective_reach`,
`units.py:100`, reusing Stage B's `FOV_HALF_DEG`/`REAR_BLIND_DEG`). Jordan's ruling requires two
separate vectors:
- **Body/movement facing** (existing `_node_facing`/`cell_facing_vec`, mostly unchanged) — follows
  the direction of travel (the waypoint-primitive's current goal vector, once fix step 7 lands),
  NOT the target. This is what the octagon zone reads for flank/rear vulnerability — so a subunit
  moving sideways-to-a-threat is exposed on its actual side, matching "their sides are still
  exposed."
- **Attention/target-lock** (NEW — e.g. `_node_attention`) — turns toward the current
  target/threat, "very responsive" (i.e. effectively unslewed / near-instantaneous re-lock, in
  contrast to body facing's existing discipline-gated `_slew_facing` rate). This is what
  `_effective_reach`'s FOV gate and any future reaction-speed mechanic should read — it governs
  whether a subunit CAN perceive/respond to a threat quickly, decoupled from whether its BODY is
  oriented to defend against that threat's direction.
- Net effect (confirmed as the intended emergent outcome, not just a side effect): a subunit moving
  laterally can react fast to archer fire (attention locks on immediately) but its body — still
  facing its movement direction — presents flank, so the octagon zone reads YELLOW/exposed even
  though the subunit "saw it coming." This is the mechanism that makes flank/rear vulnerability
  meaningful even against attentive, disciplined troops — a body cannot face two directions.

**Status: mechanism fully specified; needs a slew-rate choice for the new attention vector** (fully
instantaneous, or a very fast but still discipline-gated `_slew_facing` at a much higher rate than
body facing — Jordan's "very responsive" reads as functionally instantaneous, proposed as the
default; flag if a rate is wanted instead).

**SEQUENCING RULING (Jordan, 2026-07-02): Gates 1 and 3 are explicitly DEFERRED until AFTER
envelopment/pincer/wheeling pathing is confirmed working.** Do not build the conditional-tactics
system or the facing/attention split on top of movement mechanics that aren't yet proven. Concrete
effect on the fix plan below: step 2 (`reset_positions`) proceeds now in its MINIMAL form only —
stop the node-state no-op / turn-boundary corruption so positions correctly continue across turns
(the direct fix for finding 1.1 and Jordan's core "nonsensical to reset mid-battle" complaint) —
without yet layering gate 1's Command-gated transition-speed / Discipline-scaled effectiveness /
variant-slot-count mechanism on top; step 5 (WHEEL 180° stall) proceeds using the EXISTING unified
facing vector (fixes the stall itself, a real bug independent of the facing/FOV split) rather than
building gate 3's new attention vector first. Gates 1 and 3 return as follow-up work once fix-plan
step 7 (the waypoint primitive) is built, validated against step 6's re-pointed acceptance gate, and
Jordan confirms envelopment/pincer/wheeling reads correctly in a re-run visualization.

### Gate 4 — `PER_CELL` flips to default ON

> "Yes, all options/modules must be turned on."

**Fully specified, matches the ED-1089 precedent exactly.** `PER_CELL` (`config.py:86`) flips
`'0'`→`'1'` default, same treatment as `FIELD_MOVEMENT`/`PC_NODE_COHESION` under ED-1089: `OFF`
must keep reproducing the frozen grid digests byte-for-byte (an explicit `PER_CELL=0` pin, not an
ambient default, per the same `bat.py`/CI-pin discipline ED-1089 established); `ON`-path field
digests need a deliberate re-record (already required by fix-plan steps 2/4/5/7 above, so this
folds into the same re-baseline pass rather than adding a second one); `gauge_mb.py` needs a
re-run under the new default. This unblocks charge shock, brace recoil, cavalry speed, fatigue, and
the ED-1091/ED-1095 gates in the default/visualized configuration (finding 1.6).

## 5. Fix plan (dependency-ordered; Sonnet-executable once gates above are answered)

1. **Fix `check_drift` node-state re-keying** — independent, low-risk, do first (prevents a
   discipline-degrading wing from corrupting `cells()` mid-maneuver and poisoning every later test).
2. **Teach `reset_positions` to reset node state** — gated on decision gate 1.
3. **Wire ED-1095's `unit_type='ranged'` via `ROLE_SPEC` data** (no entity special-casing) — gated
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
