# Octagon facing = damage-received multiplier (ED-MB-0018)

**Date:** 2026-07-23 · **Lane:** MB · **Status:** implemented, DEFAULT ON, field goldens re-recorded.

## Jordan directive (verbatim intent)

> "-2D is not a good penalty. The facing octagon that I have shared many times is supposed to be a
> **damage-received multiplier**, so attacks from behind are supposed to do like **twice as much damage**
> as from the front.
>
> **AND** cells are not able to turn around instantaneously upon contact — there must be time spent for a
> cell to turn around, i.e. **react, and it needs to be at least a couple ticks**.
>
> **PLUS** if a subunit is being attacked from **multiple sides**, then the logic of units rotating in/out
> in support like real life is **divided AND compromised due to shock and distraction — so it's extra bad,
> not just a divide-by-two thing**."

Three requirements, each implemented and asserted below.

## What was wrong before

The octagon zone (GREEN <45°, YELLOW 45–90°, RED ≥90°, per `geometry.octagon_angle`) fed
`ANGLE_DEF_MOD = {GREEN:0, YELLOW:-1, RED:-2}` **into the dice pool / sigma head** — a rear attacker made
the *defender* roll `-2` dice. Two problems:

1. **Too weak.** `-2` dice on a pool of ~6 is roughly a third fewer successes, not "twice the damage." A
   rear attack should be *devastating*; the pool penalty barely moved the casualty exchange (measured:
   legacy rear = **1.25×** front casualties, and after `round()` a `-1` flank penalty often vanished
   entirely → **1.00×**).
2. **Instantaneous.** The refuse mechanic let a cell turn to face a seen threat *in the same tick*, so a
   flank/rear strike was negated before it could land.

## The model now (`PC_OCTAGON_DMG`, default ON)

### (1) Arc = damage-received multiplier

A new `_octagon_dmg_mod(defender, def_cells, atk_cells)` in `resolve_engagements` computes the **pure
per-cell facing arc**, separate from the legacy `_per_cell_angle_mod` (which also bundles the
wrapper/pocket/roll-up *pool* penalties of the old paradigm). Anchors:

| arc zone | `angle_mod` | damage multiplier |
|---|---|---|
| front (GREEN) | 0 | **1.0×** |
| flank (YELLOW) | −1 | **1.5×** |
| rear (RED) | −2 | **2.0×** |

`mult = 1 − arc·(RED−1)/2`, capped at RED, then applied to the **defender's** casualties
(`dmg_a += … · _a_dmg_mult`). Under the flag the pool/sigma angle-penalty is zeroed, so the arc is a
*damage* effect, not a *dice* effect — no double-count.

**Local-centroid fix.** The multiplier reads each defender cell's arc against the centroid of only the
attacker cells **within `OCTAGON_LOCAL_REACH = 2.0`** of that cell (global fallback). This was essential:
with the *global* attacker centroid, a wide line's wing cells in a **head-on** clash read the enemy's
distant centre as an oblique (flank) bearing and took a spurious 1.25× — a normal frontal fight was
inflated. With the local centroid, verified **exactly**:

```
front (B faces attacker)   arc = +0.00  →  mult 1.00×
rear  (B back to attacker)  arc = −2.00  →  mult 2.00×     (same contact cells, only facing differs)
```

Per-seed, a pure rear strike deals **exactly 2× the frontal casualties** (regression:
`test_rear_is_exactly_double_front`). It compounds further with the loss of frontal
brace / charge-shock resistance — a braced front that parries a frontal blow to **zero** is annihilated
when the same blow lands behind it (Cannae). This is grounded in du Picq (a line is lethal to its front,
helpless to its rear) and the encirclement-annihilation pattern.

### (2) Reaction is not instantaneous

A cell hit outside its front arc **keeps its exposed facing** until it has had `FACING_REACTION_TICKS = 2`
to wheel, and it only *ever* wheels if it can **see** the threat (angle ≤ `FOV_HALF_DEG` = 105°) **and**
is not frontally **pinned** (an attacker in its front arc within `PC_PIN_REACH` holds it). Consequences:

- A **rear** strike is in the blind arc (>105°) → never perceived → the cell **never turns** → the 2×
  persists for the whole engagement (regression: `test_rear_penalty_persists_across_reaction_window` —
  rear stays exactly 2× at every tick across `FACING_REACTION_TICKS + 3`).
- A **seen flank** threat lands at 1.5× during the 2-tick reaction window, then the cell wheels to face it
  and the penalty drops — a unit *can* react to a flank it sees, but it costs it two ticks of exposure.
- A cell **pinned** frontally (the fixing-force half of an envelopment) can never turn to the flank/rear
  threat — the penalty stands. This is why envelopment needs a pinning force in front.

The per-cell reaction clock (`subunit._react_since`) persists across ticks and resets when the cell is
facing the threat again.

### (3) Multi-side shock compounds

A subunit engaged from **≥2 sides** (`eng_counts[id] ≥ 2`) takes an **extra `×(1 + MULTI_SIDE_SHOCK)`**,
`MULTI_SIDE_SHOCK = 0.5`, **compounding** on top of the arc multiplier — not a mere halving. Orderly
rank-relief (rotating fresh files forward) collapses under encirclement shock and distraction, so a rear
hit *and* a front pin is worse than either alone. (du Picq on the moral collapse of the surrounded; Cannae.)

## Supersession (deliberate)

Under `PC_OCTAGON_DMG=1` the older pool-penalty envelopment machinery — wrapper depth-resist, pocket,
oblique roll-up (all built to make envelopment bite *within* the −2-dice paradigm Jordan is replacing) —
goes **dormant** (its output is zeroed out of the pool). It is subsumed by the new model:

- a wrapped-around attacker sits in the defender cell's **rear arc** → RED → 2×;
- enemies on both lateral sides → **≥2 engagement sides** → multi-side shock.

Roll-up (pure depth-concentration, not a facing effect) is dropped; depth still tells through Lanchester
strength. The **legacy path is preserved verbatim** for `PC_OCTAGON_DMG=0` (byte-exact; the `bat.py`
digest + persubunit stress assert it), so the supersession is opt-out.

## Invariants / balance disclosure

- **I4 (grid oracle).** The multiplier runs on **both** grid and field paths (it must, or field ≠ grid).
  The head-on single-subunit battery rows are all-GREEN → mult 1.0 → **byte-identical**. The three
  flanking rows (envelop / cannae / oblique) legitimately move. **All 4 `bat.py` goldens re-recorded**
  (ED-909 re-baseline precedent, as in ED-MB-0013/0014/0017).
- **I1/I2/I5.** Conservation and determinism hold (no RNG consumed by the arc; casualties still bounded by
  `max(0, DAMAGE_BY_DEGREE − dr)`). No balance constant was tuned to the gauge — the anchors (1.0/1.5/2.0,
  2-tick reaction, +0.5 shock) are the design values Jordan stated.
- **Direction of the balance shift.** Rear/flank engagements are now **materially more lethal** than under
  the −2-dice model. This is the intended correction (envelopment was under-rewarded — the DG-6/ED-MB-0016
  thread). It does **not** by itself fix DG-6 over-decisiveness of *frontal* force-ratio rows (that remains
  the ED-MB-0016 friction + conjunctive-gate follow-on); it makes the *geometric* reward for getting behind
  the enemy real, which is the precondition for envelopment paying off.

## Adversarial review (2026-07-23) — findings + fixes

A five-critic adversarial pass (independent, read-only, structurally isolated) plus an architectural
cell-up audit and a full-campaign gauge A/B were run against the first cut. What they found, and what
changed:

**Confirmed bugs — FIXED:**
- **Reaction-clock cross-engagement leak (R1).** `_react_since` was per-engagement transient state stamped
  with `run_battle`'s per-turn tick (1–18) but stored on the persistent `Subunit` and never reset — so an
  asymmetric re-engagement (notably `run_multi_unit_battle` re-pairing) mis-scored the opening ticks
  (1.2× instead of 1.9×, or a stuck 1.9× that never wheels). Fixed: the clock is now a **frame-independent
  consecutive-tick counter** `(last_tick, count)` and is **reset at engagement boundaries**
  (`reset_positions` grid re-approach, `reset_morale_between_battles` battle boundary; field continuous
  engagements correctly keep it via the node-skip).
- **Multi-pair order-dependence (R2).** A cell struck in ≥2 pairs in one tick advanced the clock twice; the
  counter is now **idempotent within a tick** (same `t` → no double-advance).
- **Multi-side shock fired on the wrong trigger (balance-critic A1 / A1-gap, arch-critic #1).** It keyed on
  `eng_counts ≥ 2` — the arc-blind count of opposing *subunit-pairs* — so **two attackers both in the front
  arc** got the +50% "encirclement" shock (a concentric frontal pinch, `b_dmg_mult` measured 1.75×), while
  **one wide body genuinely wrapping two arcs** (`eng_count==1`) got none. Replaced with a **bearing/face**
  trigger: each contacting enemy body is classified by the **nearest perimeter face** of the defender
  (front/rear/left/right — Jordan's midpoint-of-each-perimeter-line model), and the shock fires on the
  number of **distinct faces** struck, **graded** `×(1 + MULTI_SIDE_SHOCK·(n_sides−1))` (2 sides→1.5×,
  3→2.0×, 4→2.5×).
- **Double-count (arch-critic #2).** `ENCIRCLEMENT_PENALTY` (a legacy pool/sigma penalty on the *same*
  `eng_counts ≥ 2` trigger) was **not** gated by the flag, so encirclement was charged once on offence
  (pool) and again on defence (damage multiplier). Now gated `if not PC_OCTAGON_DMG` — the octagon
  multi-side shock is the single owner.
- **`t=None` footgun (arc-critic A4).** A `t=None` call silently *instant-faced* every flank/side threat
  (zeroing the penalty). Now `t=None` leaves the penalty standing (a wheel can't be timed without a tick).

**Corrections to the claims above (the model is right; two statements here were imprecise):**
- The "**capped at RED=2.0×**" wording is only the *arc* cap. Multi-side shock compounds on top, so a rear
  pair on a 2-sided body legitimately reaches **~3.0×** (rear 2.0 × shock 1.5) — the annihilation regime.
- "**flank 1.5×**" is the YELLOW *band* (45–90°); a **perpendicular** (≥90°) hit is RED (2.0×), and
  "front → 1.00× exactly" holds for **aligned equal-width** formations — a one-file offset or width
  mismatch puts overhang cells at the 45° boundary (YELLOW), a real (small) characterization the first
  cut over-generalized. No head-on clash ever reads *rear*.

**Design characterization (balance-critic Part B, full gauge A/B, n=60):** the mirror row is byte-identical;
the rows the flag moves shift **toward** their historical bands (H2 +8.3, H5 +6.7, H6 −19.1 toward), and
**no** row becomes more over-decisive in the decisiveness metric. The honest caveat: the marquee
envelopment rows (H3/H4) are *already* 100%-decisive under **both** flags, so the octagon buff does not fix
DG-6 there; it deepens the **casualty exchange ratio** (attacker losses fall, defender losses rise) toward
the Cannae ~11%-inflicting-~85% figure. The A1 fix (no shock on a frontal double-team) + grading soften the
"cliff" the first cut introduced. `PC_ENVELOP_SHOCK` (the *offence-side* moral-shock complement) is left
live — it models a distinct facet (the enveloped unit fights back less) and is not a duplicate of the
defence-side damage multiplier; the "single model" phrasing above is corrected to "the single owner of the
multi-side *damage* effect."

**Still gated `needs_jordan`:** the default-ON flip and the exchange-ratio characterization (the
decisiveness gauge cannot see the casualty-ratio change — a candidate gauge addition is noted below).

## Follow-ons

- The wrap still seals a horseshoe, not a full ring (no cavalry rear-transit) — carried from ED-MB-0017.
- `MULTI_SIDE_SHOCK` currently triggers at ≥2 sides with a flat compound; a graded "how surrounded"
  (3-side, 4-side) escalation is a candidate refinement.
- A full-campaign A/B of the default-ON flip (win-share drift) should be run once the ED-MB-0016 friction
  and conjunctive-envelopment gate land, since all three interact on the envelopment rows.
