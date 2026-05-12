# SIM-MB-06 Atom Architecture — Handoff
**Date:** 2026-05-12
**From session token:** a0442606ddff818c → 244713e47250a6fc → 888bb57917a91197
**Status:** EXPLORATORY. ED-814 (3×3 composition grid) remains the canonical mechanic. Atom architecture is a candidate replacement that has not yet been ratified.

---

## Where this left off

Seven iterations (v1 → v7) committed across three commits on `jordanelias/ttrpg`:

| Commit | Scope |
|---|---|
| `0121e84` | v5 — atom architecture baseline: 15×15 unit grids, 25×25 battlefield, 5-cell buffer, per-cell movement, side-mirroring, contact-driven engagement, Bii pool formula |
| `b8e652f` | v6 — halt-cell bug fix (Side A bias eliminated), per-cell facing infrastructure, engagement angle modifier (FRONT/FLANK/REAR → defender penalty), Phase C pool formula (C-ii validated) |
| `899ba9f` | v7 — tip support constraint (Phase E), tension F documented |

**Key files in repo (`tests/sim/`):**
- `sim_mb_06_v7.py` — current sim (defaults: POOL_VARIANT=C-ii, TIP_SUPPORT_ENABLED=True, TIP_SUPPORT_GAP=2)
- `sim_mb_06_v7_battery.py` — test battery
- `sim_mb_06_v7_manifest.md` — full change history + open tensions
- `sim_mb_06_v5_visual.html` — pictorial reference (architecture concepts, §8 mirroring correction)

**Visualization on disk** (not in repo): `/mnt/user-data/outputs/sim_mb_06_v5_visual.html`

---

## What works now

- **Side bias eliminated.** Mirror-aware halt logic. Line-vs-Line mirror at n=200: 51.5/48 (within noise).
- **Per-cell facing.** Every cell carries a (dr, dc) unit vector representing its front face. Currently uniform per atom (= advance direction). Foundation for the cascading-pivot mechanic Jordan describes below.
- **Engagement angle classifies FRONT/FLANK/REAR** via cosine of approach vector vs defender's facing. ANGLE_DEF_MOD = {FRONT: 0, FLANK: -1, REAR: -2} applied to defender pool.
- **Composite atoms balance restored** (5% → 38.3% via C-ii).
- **Cannae works naturally.** Horseshoe vs Arrowhead 62% — wings wrap around to flank position, trigger defender penalty.
- **Tip support mechanic available** (currently no-op at X=2 default; at X=1 produces tight-wedge behavior).

---

## The unresolved problem: tension F

**Wedges cannot pierce lines.** Arrowhead vs Line T3/T4 = 0% across all tip-support variants.

Root cause: the Bii pool formula's `engage_frac = engaged_cells / atom_max_width` treats narrow contact as *less* of your unit fighting, not more. Arrowhead tip (1 cell) hits Line front (3 cells adjacent):
- Arrowhead engage_frac = 1/9 → pool ~1 die
- Line engage_frac = 3/5 → pool ~4 dice
- Line outrolls 4:1 against the tip

Historically a wedge concentrates force at a narrow point — this is the entire mechanic. The current sim does the opposite.

---

## Jordan's three-part design for tension F

Captured 2026-05-12 mid-handoff. These are the design direction; the next session implements + tests.

### (1) Cell support — adjacent cells behind contribute

A cell is not isolated. Cells directly behind it in the formation back it up. The tip of an Arrowhead isn't a single unit; it has the second row supporting, third row behind that, etc.

**Implementation sketch:**
```
For each cell in contact, compute its "support stack":
  - row 1 behind: full contribution
  - row 2 behind: diminishing (0.7?)
  - row 3 behind: further diminishing (0.5?)
  - row 4 behind: floor (0.3?)

Effective engage_frac for the contact = sum(in_contact + weighted supporters) / atom_max_width

Cap at 1.0.
```

For Arrowhead tip vs Line at T3:
- Tip in contact: 1
- Supporters: row 1 (3 cells × 1.0 = 3), row 2 (5 × 0.7 = 3.5), row 3 (7 × 0.5 = 3.5), row 4 (9 × 0.3 = 2.7) = 12.7 total
- Effective: (1 + 12.7) / 9 = 1.52 → capped at 1.0

Arrowhead now gets full pool. Line also gets full pool (its support stack also caps). Now it's a fair contest decided by shape mods + size, not by engage_frac penalizing the tip.

This is **F-i variant** (with weighted support). Cleaner version: just sum all cells in support cone with uniform weight.

### (2) Puncture mechanism — speed / momentum at contact

Speed and approach affect whether the unit rushes through or gets caught holding ground. Needs a puncture mechanism.

**Implementation sketch:**
```
At engagement, compute relative speed at contact:
  attacker_momentum = attacker_cell.last_turn_speed
  defender_momentum = defender_cell.last_turn_speed (0 if halted)

If attacker_momentum > defender_momentum:
  Attacker gets +1D per (attacker_momentum - defender_momentum)

Bonus caps at +3D or similar.
```

For Arrowhead tip hitting halted Line:
- Tip last turn speed: 2 (Arrowhead tip cell)
- Line cell last turn speed: 0 (halted on contact)
- Puncture bonus: +2D to Arrowhead

This is **F-ii**. Compounds with (1): the tip arrives with full support stack AND momentum bonus.

### (3) Cascading resolution — multiple sub-phases per combat turn with facing rotation

**This is the structurally significant one.** Multiple resolution phases per combat turn, where each phase triggers facing rotations that expose flanks to subsequent waves.

**Implementation sketch:**
```
Combat turn = sequence of sub-phases (ripples).

Sub-phase 1:
  - Find all current contacts
  - Resolve engagement
  - Mark engaged defender cells: rotate facing to point toward attacker
  - Apply damage from sub-phase 1

Sub-phase 2:
  - Find new contacts (some attacker cells from row N+1 are now adjacent to
    defender cells that have rotated and exposed their flanks)
  - Resolve engagement with updated facings
  - Some defender cells now take FLANK or REAR attacks (defender pool penalty
    from angle modifier)
  - Rotate newly-engaged cells

Continue up to N sub-phases per turn or until no new contacts.
```

For Arrowhead vs Line:
- **Sub-phase 1**: Tip (1 cell) contacts Line center (3 cells, cols 10-12). Line center cells engaged; they rotate facing toward tip (col 11). Line cells at cols 10 and 12 now face partially-inward instead of straight-forward.
- **Sub-phase 2**: Arrowhead row 1 (3 cells at cols 10-12) arrives. Cells at col 10 and col 12 hit Line cells that just rotated — those Line cells now present FLANK or REAR (depending on rotation amount). Big defender penalty. Arrowhead row 1 dominates.
- **Sub-phase 3**: Arrowhead row 2 (5 cells, cols 9-13). Line cols 9 and 13 rotated in sub-phase 2 to face row 1 attackers. Now they expose flanks to row 2.
- **Sub-phase 4**: Row 3 (7 cells), then row 4 (9 cells)...

The cascade produces wedge piercing because each row of the wedge attacks cells that have just been forced to reorient.

**Combined with (1) and (2):** wedge piercing emerges naturally:
- (1) gives tip full pool to survive sub-phase 1
- (2) gives tip momentum bonus on initial contact
- (3) gives subsequent rows FLANK/REAR bonuses as Line rotates inward

### (3a) Cell-level facing rotation rules — open design question

How exactly do cells rotate? Some options:
- **Rule A**: When a cell engages an attacker not on its front face, it rotates to face that attacker (full pivot)
- **Rule B**: Cell facing partially rotates toward engaged target (gradient, e.g., 30° per engagement)
- **Rule C**: Cell facing locks on the closest attacker, full pivot, no further rotation that turn
- **Rule D**: Defender's facing rotates only if defender has "free flank" — i.e., no other enemy already engaging that side

Needs design pass.

### (3b) Number of sub-phases per turn — bounded loop

Sub-phases continue while new contacts form. Bound: max 5-7 sub-phases per turn (otherwise risk of unbounded cascade for circular topologies). Each sub-phase = 1 unit of "battle time".

---

## Suggested next-chat workflow

1. **Bootstrap** as usual (PI at `/mnt/project/VALORIA_PAT`, scripts via `gh api`)
2. **Read this handoff** in full
3. **Read** `tests/sim/sim_mb_06_v7.py` and `sim_mb_06_v7_manifest.md` to understand v7 state
4. **Implement F as v8**, following Jordan's three-part design:
   - Start with (1) cell support — simplest, biggest single-fix candidate
   - Add (2) puncture — small additive enhancement
   - Then (3) cascading resolution — the big architectural lift
5. **Test against the Arrowhead-vs-Line target** at each step. Target: Arrowhead T3 vs Line T3 climbs from 0% to ~50-60% (acknowledging Line should still win sometimes; the wedge isn't unstoppable).
6. **Don't break Cannae** (Horseshoe vs Arrowhead must remain in 40-60% range)
7. **Lethality concern persists**: current Line-vs-Line mean = 9.7 turns vs target 3-6. Probably resolves once engage_frac math is fixed (currently most engagements roll too few dice).

---

## Lessons from v1–v7 (read before starting v8)

1. **Hooks fire late.** Constants check, co-file requirements, sim_gate — design the verification ledger and module manifest ALONGSIDE the sim code, not at commit time.
2. **The transcript compaction summary is reliable.** Trust it over recomputing state.
3. **Side bias from broken mirror-aware halt logic was subtle.** Diagnostic that swaps geometry vs swaps args is the right tool — confirmed geometric not arg-order bias in one test.
4. **Mirror correctly throughout.** Three places use cell positions: `cells()`, `advance_cells()`, and `run_battle`'s halt loop. All must use `oriented_pattern`. The halt loop was missing this in v5, caused 80/20 bias.
5. **Verbose tracing of one battle reveals more than 1000 batched trials.** When `a_engaged ≠ b_engaged` in a symmetric mirror match, the asymmetry source is visible immediately.
6. **The pool formula has more impact than any shape modifier.** All shape tuning (Phase C variants, ANGLE_DEF_MOD, tip support) sits on top of the engage_frac multiplier. If that multiplier is structurally wrong, no amount of shape modifier rescues it.

---

## Open tensions still in queue after F

- **Horseshoe vs Line: 0%** — separate investigation. Possibly resolved by tension F changes (thin center gets support stack), but may need its own mechanic.
- **Lethality 9.7 turn mean vs 3-6 target** — atoms under-damage. Probably resolves with tension F's engage_frac fix.
- **B-ii curving wings** — deferred. Cannae appears to work via angle modifier alone. Reopen only if Horseshoe winrate doesn't normalize.
- **Promotion of atom architecture to canonical** — requires F resolution, lethality fix, all matchups in 30-70% range. Then write ED-826 (or whatever ID) superseding ED-814.

---

## Quick-reference: critical values

| Value | Current | Target |
|---|---|---|
| Side bias (mirror match) | 51.5/48.5 | ~50/50 ✓ |
| Composite vs Uniform | 38.3% | 35-50% ✓ |
| Cannae (Horseshoe vs Arrowhead) | 62% | 40-60% ✓ |
| Arrowhead vs Line T3 | **0%** | **~40-60%** ← tension F |
| Horseshoe vs Line T3 | **0%** | **~40-60%** ← possibly tension F |
| Lethality (Line mirror mean turns) | **9.7** | **3-6** ← possibly tension F |

---

## Files to read on next bootstrap (priority order)

1. **This document** (`sim_mb_06_handoff_2026-05-12.md`)
2. `tests/sim/sim_mb_06_v7_manifest.md` (v7 module manifest)
3. `tests/sim/sim_mb_06_v7.py` (current sim source)
4. `tests/sim/sim_mb_06_v7_battery.py` (test battery patterns)
5. `tests/coverage_matrix.md` (cumulative state across all SIM-MB-XX iterations)
6. `tests/sim/sim_mb_06_v5_visual.html` (architecture reference — read in browser if needed)

Skip: anything earlier (v1–v6) unless investigating a specific historical issue. The current state is captured in v7 + this handoff.
