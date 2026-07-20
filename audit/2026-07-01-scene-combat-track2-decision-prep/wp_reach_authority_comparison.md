# Track-2 decision prep: `WP.reach()`/`WP.authority()` vs their live counterparts

**Status:** decision-prep only. Neither `WP.reach()` nor `WP.authority()` is wired into live resolution —
both are labeled `[BUILD-ONLY / DIAGNOSTIC — not wired into live resolution; do not add a call site]` in
`weapon_physics.py`, and a prior attempt to delete them as "dead code" was adversarially caught (deleting
one horn of a Jordan-reserved single-source-target decision is not the same as it being safe to delete —
see PR #47's body). **This doc does not recommend picking a side** — it tabulates what each currently
computes and where they diverge, per the harness `wp_reach_authority_measurement.py` in this folder.

## reach: `WP.reach()` vs `systems.reach_base()` (the live path)

| Weapon | `WP.reach()` | `reach_base()` (live) | ratio |
|---|---|---|---|
| rapier | 3.35 | 6.18 | 0.54 |
| arming | 2.30 | 5.42 | 0.42 |
| longsword | 3.14 | 5.99 | 0.52 |
| greatsword | 4.67 | 6.95 | 0.67 |
| sabre | 2.50 | 5.55 | 0.45 |
| dagger | 0.70 | 4.44 | 0.16 |
| paired_short | 0.90 | 4.39 | 0.21 |
| spear | 5.98 | 7.80 | 0.77 |
| staff | 3.92 | 6.49 | 0.60 |
| mace | 1.80 | 5.14 | 0.35 |
| poleaxe | 4.15 | 6.62 | 0.63 |
| longsword_halfsword | 2.44 | 5.55 | 0.44 |

**They are not a constant scale factor apart** — the ratio ranges from 0.16 (dagger) to 0.77 (spear), so no
single affine remap (`a*x+b`) makes them coincide across the roster; `weapon_physics.py`'s own docstring
already flags this precisely: *"weapon_physics.reach() spans ~0.7–6.0 (head_len-based); the LIVE
systems.reach_base it replaces spans ~4.5–7.8 (L0=4.0-based)... wiring reach() in UNSCALED zeroes the
long-weapon close penalty (spear 5.98 < 6.5 [CLOSE_REACH_REF])."* Both derive from the same underlying
geometry (`head_len`, `grip_len`, 2H rear-hand setback), differing in: (a) `reach_base` adds a body/arm
offset `L0=4.0` that `WP.reach()` lacks entirely (a standing-reach term, not weapon-only); (b) the 2H term's
gain differs (`REACH_GEOM_SCALE` vs `K_GRIP_REACH`, tuned independently); (c) both carry the SAME
`reach_adj` per-weapon residual, flagged `[SIM-CALIBRATE]`/not grounded in both.

**What picking `WP.reach()` as canonical would require:** either a full re-derivation of `L0`/`CLOSE_REACH_REF`/
`reach_adj`/the gap-normalisation together in one pass (re-tuning everything downstream that assumes the
4.5–7.8 band), or keeping `reach_base`'s *shape* (weapon geometry + a body-offset constant) and just
re-deriving its gain from `WP.reach()`'s cleaner geometric form. Neither is a drop-in swap.

## "authority": `WP.authority()` vs the live path's actual impact-force inputs

| Weapon | `WP.authority()` | `percussion_authority()` (live, blunt only) | live edged-heft (`core.heft_resp`, non-blunt only) |
|---|---|---|---|
| rapier | 0.46 | 0.00 | 0.05 |
| arming | 0.47 | 0.00 | 0.03 |
| longsword | 0.52 | 0.00 | 1.00 |
| greatsword | 0.77 | 0.00 | 1.20 |
| sabre | 0.39 | 0.00 | 0.00 |
| dagger | 0.23 | 0.00 | 0.00 |
| paired_short | 0.28 | 0.00 | 0.00 |
| spear | 0.92 | 0.00 | 0.15 |
| staff | 0.38 | 2.51 | N/A (blunt) |
| mace | 0.77 | 7.45 | N/A (blunt) |
| poleaxe | 0.62 | 5.83 | N/A (blunt) |
| longsword_halfsword | 0.42 | 0.00 | 1.00 |

**`WP.authority()` and `percussion_authority()` are not measuring the same thing, and comparing them directly
is misleading** — `percussion_authority()` is defined to be exactly 0 for every non-blunt head by construction
(edged/pointed weapons don't deliver concussive force), so the "0.00" column for every bladed weapon above is
not a gap `WP.authority()` fills, it's the correct live value for a different physical concept.

The live engine's actual analogue to "impact force" is **split by head type**:
- **Blunt weapons:** `percussion_authority()` IS live (feeds `core.damage`'s blunt-transmit path directly) —
  no residual here, this one is already single-sourced.
- **Edged/pointed weapons:** the live "impact" term is `strength + HEFT_HEAVY * heft_resp(w)` (`core.damage`'s
  `impact` line) — i.e. `core.heft_resp`, not `percussion_authority` and not `WP.authority()` either.
  `WP.authority()` (`sqrt(mass) * (0.30 + pob)`) is a *third*, currently-unwired formula for the same general
  concept ("forward momentum"), computed uniformly across ALL weapons including blunt ones (where it's simply
  never read). Its own docstring is explicit about this: *"Live resolution gets impact force from
  percussion_authority (blunt) + core.coupling's DELIVERY/strength terms (edged) instead."*

**What this means for the single-source-target decision:** there are, right now, three overlapping-but-distinct
"impact" formulas in the codebase — `WP.authority()` (unwired, uniform), `percussion_authority()` (live,
blunt-only), and `core.heft_resp` (live, non-blunt-only, and itself the subject of the *other* Track-2
residual in `wt_spd_deleak_report.md`). Resolving the `WP.reach()`/`WP.authority()` fork cleanly likely means
deciding what `WP.authority()` is even FOR before deciding whether to wire it — as written, it doesn't have a
single live counterpart to replace, it overlaps two.

## Where each is called from (confirms zero live callers)

Both `reach()` and `authority()` are called only from `weapon_physics.py`'s own `if __name__ == '__main__':`
self-test block (confirmed via grep across `designs/scene/combat_engine_v1/` — no other file references
either function). Deleting either is exactly the fork the Gate-1 audit reserved for Jordan (see HANDOFF.md
"Still open" and PR #47's body) — this doc changes nothing about that; it only makes the divergence concrete.
