# Track-2 decision prep: `wt`/`spd` cost-path de-leak — measured before/after

**Status:** decision-prep only. No code changed; this is the "measured before/after presented for sign-off"
`HANDOFF.md` asks for before either substitution is flipped live. **No recommendation is made here** — both
substitutions are candidates, not proposals; the harness generating these numbers is
`wt_spd_deleak_measurement.py` in this folder (`python designs/audit/2026-07-01-scene-combat-track2-decision-prep/wt_spd_deleak_measurement.py`
from repo root reproduces everything below).

## Context

`weapons.py`'s own docstring labels `reach`/`wt`/`spd`/`hand` "LEGACY (derived in weapon_physics; live until the
Phase-3 wiring)" — i.e. the original intent was for these hand-authored fields to be fully replaced by derived
weapon_physics quantities. `wt`/`spd` are the two that never got wired. This is genuinely two independent
questions, since they replace with different already-existing derived quantities:

- **A. Damage path** (`core.py:heft_resp`, read by `core.damage` for non-blunt heads only): currently anchors
  on `w.get('wt')` (`'heavy'`/`'light'` binary class), with an optional continuous within-class mass refinement
  (`HEFT_MASS_K=0.15`, active per `config.HEFT_MODE='continuous'`). Its own docstring argues the binary anchor
  is deliberate — it "encodes wieldiness/blade-presence, NOT raw kg" (e.g. the 2kg spear is `'light'`, the
  1.2kg mace is `'heavy'`) — so this is not obviously dead code, but it is a **second, parallel heft
  derivation** alongside `systems.wield_heft` (the g-aware MoI heft already live on the tempo/cost path since
  Stage 2b, commit `d3661936`). The candidate here reuses `wield_heft`'s exact formula
  (`(at_grip(w,0)['I_g'] / REC_I_REF) ** WIELD_HEFT_EXP`) on the damage path too — no new coefficient invented.
- **B. Tempo path** (`systems.py:weapon_tempo`): currently reads `w['spd']` — a bare hand-authored constant
  (range **-0.5 to 3.0** across the roster) — times `config.SPEED_K`. **Revision note:** an earlier draft of
  this packet substituted `weapon_physics.agility(w)` (pure swing-inertia power law) here. That candidate was
  rejected as under-grounded — agility captures only ONE primitive (moment of inertia about the grip axis) and
  ignores balance, hands, and — critically — thrust-vs-swing action type, all of which the engine already
  models elsewhere. The candidate below instead reuses **`systems.recoverability_factor`** (evaluated at
  baseline: `grip_position=0`, `lunge_depth=0`) — the engine's own existing commitment=recovery model, which
  already blends:
  - **weight + balance** — `WP.at_grip(w,0)`'s `I_g` (swing inertia) and `S_g` (static moment / PoB), the same
    primitives `wield_heft` uses;
  - **hands** — a MoI-aware 1H/2H force-couple control credit;
  - **thrust vs swing** — `point_concentration` (continuous "thrust-ness": rapier 0.95, mace 0.02) blending a
    swing-arrest cost (MoI-based) against a thrust-retract cost (static-moment-based) — the primitive the
    agility-only draft entirely lacked;
  - **commitment/recovery** — this function *is* the commitment=recovery axis (its own docstring), so reusing
    it for baseline tempo draws on the engine's already-established grounding rather than inventing a new one.

  As with the damage-path candidate, this is anchored so the `'arming'` sword's tempo contribution is
  unchanged (same convention as `AGI_TEMPO_K`/`REC_I_REF` elsewhere in `config.py`) — one reasonable
  convention, not a decision; a different anchor weapon shifts every candidate number by a constant factor.

  **Caveat, flagged not resolved:** `weapon_tempo`'s `pen` term *already* separately penalises weight and
  hands via `wield_heft` (`WEIGHT_PEN`, `HANDS_COMMIT`). Swapping `spd` for the full
  `1/recoverability_factor` value risks **double-counting weight/hands** — once through `pen`, once through
  `recoverability_factor`'s own `I_g`/`S_g`/hands terms. The numbers below are the *naive full substitution*,
  reported for visibility with this caveat prominent; de-duplicating the overlap (e.g. isolating just the
  thrust-vs-swing blend, independent of magnitude) is exactly the kind of design judgment this packet preps
  for, not something to resolve unilaterally.

## A. Damage path — full results (strength=4, degree=success, per armour tier)

| Weapon | Head | Heft (live → candidate) | none | light | medium | heavy |
|---|---|---|---|---|---|---|
| rapier | point | 0.05 → 0.94 | 9→15 (**+6**) | 8→13 (**+5**) | 5→8 (**+3**) | 5→8 (**+3**) |
| arming | cut_thrust | 0.03 → 0.87 | 9→15 (**+6**) | 8→13 (**+5**) | 5→8 (**+3**) | 5→7 (**+2**) |
| longsword | cut_thrust | 1.00 → 1.00 | 16→16 (+0) | 14→14 (+0) | 11→11 (+0) | 11→11 (+0) |
| greatsword | straight_cut | 1.20 → 1.60 | 18→20 (+2) | 11→13 (+2) | 5→6 (+1) | 3→4 (+1) |
| sabre | curved_cut | 0.00 → 0.80 | 9→15 (**+6**) | 6→9 (+3) | 3→4 (+1) | 2→3 (+1) |
| dagger | cut_thrust | 0.00 → 0.30 | 9→11 (+2) | 8→10 (+2) | 7→8 (+1) | 7→8 (+1) |
| paired_short | cut_thrust | 0.00 → 0.51 | 9→12 (+3) | 8→11 (+3) | 5→7 (+2) | 5→7 (+2) |
| **spear** | **point** | **0.15 → 2.25** | **10→24 (+14)** | **9→21 (+12)** | **6→16 (+10)** | **6→16 (+10)** |
| staff | blunt | N/A — blunt damage-heft comes from percussion authority, not `heft_resp` (inert for this residual) |
| mace | blunt | N/A (same as above) |
| poleaxe | blunt | N/A (same as above) |

**Headline finding: the spear is the extreme outlier.** Its damage roughly **doubles to 2.5×** across every
armour tier under the candidate (+10 to +14 flat damage, not just percentage). This is because the spear is
categorically `wt='light'` (correctly, by the wieldiness-class logic — it doesn't handle like a mace) but its
actual swing inertia (`wield_heft`'s MoI-based measure) is large — a 2m two-handed weapon has real rotational
mass regardless of its wieldiness class. `longsword` is (by construction) the one weapon where live and
candidate coincide almost exactly — **both formulas were independently anchored to the longsword as the "2H
cut-thrust reference" reading ~1.0**, so they agree there and diverge everywhere else; it is not evidence the
formulas are otherwise similar.

**Why this matters for the open spear-dominance question:** `forward_roadmap.md`'s spear-fix finding (2026-06-30)
already identifies the spear as flat-dominant (94-96% win rate across tiers), attributed ~88% to the *approach*
phase, not closed-exchange damage. **This candidate would add a large damage boost on top of that**, which
would likely compound rather than help the already-known dominance problem — a material consideration for
whichever way Jordan rules on this residual.

## B0. Grounding check — does the current `spd` already track a real primitive?

Before proposing any substitution, the harness checks whether the existing hand-tuned `spd` constants
already correlate with a grounded quantity (Lesson 2, "ground, don't pick" — measure before inventing):

| Weapon | spd (live) | point_concentration (thrust-ness) | hands | I_g | S_g | recoverability_factor | 1/recov |
|---|---|---|---|---|---|---|---|
| rapier | 1.5 | 0.95 | 1 | 0.1125 | 0.159 | 0.798 | 1.253 |
| arming | 1.5 | 0.60 | 1 | 0.0885 | 0.150 | 0.714 | 1.401 |
| longsword | 0.5 | 0.80 | 2 | 0.1390 | 0.212 | 1.000 | 1.000 |
| greatsword | 0.0 | 0.62 | 2 | 0.6663 | 0.749 | 4.185 | 0.239 |
| sabre | 2.0 | 0.45 | 1 | 0.0657 | 0.103 | 0.508 | 1.967 |
| dagger | 3.0 | 0.95 | 1 | 0.0024 | 0.012 | 0.300 | 3.333 |
| paired_short | 2.5 | 0.65 | 1 | 0.0152 | 0.016 | 0.300 | 3.333 |
| spear | 0.0 | 0.78 | 2 | 2.0665 | 1.417 | 8.553 | 0.117 |
| staff | 0.0 | 0.05 | 2 | 0.3623 | 0.018 | 0.565 | 1.770 |
| mace | 0.0 | 0.02 | 1 | 0.1709 | 0.366 | 1.669 | 0.599 |
| poleaxe | -0.5 | 0.78 | 2 | 1.1366 | 0.410 | 2.404 | 0.416 |

**corr(spd, point_concentration) = +0.359** (weak-moderate) — **corr(spd, 1/recoverability_factor) = +0.878**
(strong). **This is the headline finding of this section:** the existing hand-tuned `spd` values already
track `recoverability_factor` — a function built much later (Stage 2, commit `baaa6d77`) — far more closely
than they track thrust-vs-swing alone. This suggests `spd` was, whether deliberately or not, an informal
approximation of roughly the same physics `recoverability_factor` now formalizes — which **lowers the risk**
of this de-leak relative to a residual that was tracking nothing grounded at all.

## B. Tempo path — full results

`K' = 0.6425` (solved so `(1/recoverability_factor)('arming') * K' == spd('arming') * SPEED_K`).

| Weapon | spd (live) | 1/recov | live term | candidate term | live tempo | candidate tempo | Δ tempo |
|---|---|---|---|---|---|---|---|
| rapier | 1.5 | 1.253 | 0.900 | 0.805 | 2.149 | 2.054 | -0.095 |
| arming (anchor) | 1.5 | 1.401 | 0.900 | 0.900 | 2.201 | 2.201 | +0.000 |
| longsword | 0.5 | 1.000 | 0.300 | 0.643 | 1.500 | 1.843 | +0.343 |
| greatsword | 0.0 | 0.239 | 0.000 | 0.154 | 1.200 | 1.354 | +0.154 |
| sabre | 2.0 | 1.967 | 1.200 | 1.264 | 2.561 | 2.625 | +0.064 |
| dagger | 3.0 | 3.333 | 1.800 | 2.142 | 3.564 | 3.905 | +0.342 |
| paired_short | 2.5 | 3.333 | 1.500 | 2.142 | 3.088 | 3.730 | **+0.642** |
| spear | 0.0 | 0.117 | 0.000 | 0.075 | 1.200 | 1.275 | +0.075 |
| **staff** | 0.0 | 1.770 | 0.000 | 1.137 | 1.200 | 2.337 | **+1.137** |
| mace | 0.0 | 0.599 | 0.000 | 0.385 | 1.200 | 1.585 | +0.385 |
| poleaxe | -0.5 | 0.416 | -0.300 | 0.267 | 0.900 | 1.467 | +0.567 |

**Headline finding: the properly-grounded candidate tells a materially different (and more physically
coherent) story than the rejected agility-only draft did.** The staff — not the spear — is now the largest
mover (+1.137, nearly doubling its tempo), because `recoverability_factor` correctly identifies it as
**centre-balanced** (`S_g=0.018`, near-zero static moment — the "gathered pole" the recovery/grip model
already established: *"a GATHERED pole (lower I_g) is lighter to wield... mace flat (a club, not a pole)"*):
despite real swing inertia, a centre-gripped staff recovers to guard easily, matching real quarterstaff
technique's reputation for flowing, rapid recovery. **The spear's tempo move shrinks to +0.075** (vs. +0.409
under the rejected agility-only draft) — `recoverability_factor` recognizes that a spear thrust, while
directionally simple, still commits a great deal of mass held far from the body (`S_g=1.417`, by far the
largest in the roster), so it is NOT rewarded with a large tempo gain the way the pure-MoI measure suggested.
**This directly narrows the earlier concern** that the tempo de-leak would compound the spear's already-known
damage-path dominance (section A) — under this better-grounded candidate, the spear's tempo barely moves;
the damage-path finding (+10 to +14 flat) stands largely on its own, undiluted by an unwarranted tempo boost.
Both blunt weapons unaffected by section A (staff, poleaxe) pick up substantial tempo gains here instead
(+1.137, +0.567) — a real, separate lever this residual would pull, previously undocumented in `HANDOFF.md`
or `forward_roadmap.md`.

## What this does and doesn't tell you

- This is a **like-for-like substitution measurement**, not a recommendation. Both current fields (`wt`, `spd`)
  and both candidates (`wield_heft` reuse, `recoverability_factor` reuse) are legitimate design choices already
  present elsewhere in this exact engine — the question is genuinely which one should be the single source,
  not which one is "correct."
- **The tempo candidate double-counts weight/hands against `pen` and is not a clean drop-in** (flagged in
  Context above, repeated here because it matters): `weapon_tempo`'s existing `pen` term already penalises
  weight (`WEIGHT_PEN * wield_heft`) and 2H-ness (`HANDS_COMMIT * wield_heft`) separately from whatever
  replaces `spd`. Since `recoverability_factor` ALSO derives from weight/balance/hands, using it whole for
  the `spd` slot penalises those primitives twice. A clean de-leak likely needs to either reduce `pen`'s
  existing terms proportionally, or isolate just `recoverability_factor`'s thrust-vs-swing (`point_concentration`)
  contribution independent of its magnitude/weight terms. That decomposition is a design call, not something
  resolved here.
- The tempo candidate's anchor (`'arming'`) is a convention, not a neutral fact — re-anchoring on a different
  reference weapon would shift every number in column "candidate term"/"Δ tempo" by a constant multiplicative
  factor without changing the *relative* ordering.
- Neither candidate has been re-balanced against the rest of the engine (mirror-fairness, matchup win-rates) —
  these are isolated per-weapon deltas on fixed inputs, not a re-tuned roster. If either substitution is
  approved, the joint-calibration methodology (`combat_balancing_methodology.md` §4) applies before merging, per
  the repo's own "no change without a regression guard" lesson (`forward_roadmap.md` Lesson 1).
