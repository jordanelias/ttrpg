# DICE — one roller, one ladder class, one rule for a fraction of a die

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — A-5 (the bell curve everywhere) changes what the owner's roll is. Edit A (`_MARGIN_EPS`) and Edit C (mass battle composes on the owner) stand, with the owner's roll now `roll_net_continuous`; **Edit B (the stochastic die in `roll_net`) is withdrawn** with the whole-dice roll; the gate's *byte-equal goldens* cannot hold and is replaced by one declared re-pin; the falsifier reads: `grep -rn "randint(1, 10)" modules/ engine/season/` prints nothing (addendum C-4). Below one die there is one rule in the owner (`U5a_DICE_owed_edits.md` §1 rows 4–5).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §2 row A-5 and 7b-7 ("What it changes", Edit B, gates 1–2 and the falsifier rewritten to the one declared re-pin; Edit B's body removed), `U3_CONFLICT_LEDGER.md` C3-L1 (Edit A is withdrawn: the margin is quantised once at the ladder to integer milli-units, so `_MARGIN_EPS` is not needed; `R1_READ.md` 7b-18 is the same decision), C3-N16 (problem 2's count: 6 with `i*0.1`, 18 with `i/10`), `U5b_MB_rulings_in_the_field.md` §1 row 1 (Edit C's table reads the owner's continuous roll and deletes `roll_pool_fractional`: one rule below one die, in the owner); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`; C3-D2: the field's sampler swap lands here in B05, before the keyed draw).

**Depends on:** `U5a_DICE_owed_edits.md` §1 (B05: the one sampler, the quantised margin, one rule below one die).
**Lands in batch:** B05 (`B05-one-roll`, IN with MB), with `U5a_DICE_owed_edits.md` §1 row 4 and `U5b_MB_rulings_in_the_field.md` §1 (C3-D2; U3 §4.1 row 18), before `10_DICE_exported_face_rule_and_band_edges.md`.

## Status: PROPOSED

Carries findings F-DICE-07 and F-DICE-08 of `../audits/10_DICE_audit.md`. Lanes that own the
edited files: IN (the dice engine), MB (`modules/mass_battle/resolution.py`).

## What it changes in `engine/season/` at runtime

*(Reconciled, W3-1, 7b-7, C3-L1.)* Edit C only. A field battle's dice, bands and sigma boost become the dice
engine's functions (`roll_net_continuous`, `degree_from_net` through `degree_label`, `soft_cap`, `net_boost`);
every graded draw outside combat moves to the bell curve in one declared re-pin (`U5a_DICE_owed_edits.md`
§1). Every fought field moves; the re-record is that batch's one re-pin.

## The problem, with evidence

1. **A second roller exists.** `modules/mass_battle/resolution.py:37-55` (`roll_pool`) rolls its own d10s
   and spells the face rule a second time; `:57-77` (`roll_pool_fractional`) is a third fractional-pool
   rule; `:101-120` (`compute_degree`) is a ladder copy with a `1e-9` tolerance the owner lacks;
   `:209-230` (`_sigma_softcap`, `_sigma_net_boost`) re-type `soft_cap`, `net_boost` and the per-die sigma
   `0.800`. `modules/mass_battle/` imports nothing from `engine.*` (grep: zero import lines).
   `march` reaches it from the loop (`seam/wrappers/mass_battle.py`).
2. **The two ladders are not one behavioural class.** Probe (audit §12, E-04): over `net, ob ∈ {i·0.1}`,
   6 of 10,000 cells differ (for example `net 4.3, ob 3.3`: owner Partial, mass battle Success); over
   `{i/40}`, 72 of 160,000. (6 with the tenth formed as `i*0.1`, 18 with `i/10`, `audits/25_GROUNDING_ENGINE.md`
   V-16; moot after A-5's one ladder, C3-N16.) `tests/valoria/test_degree_ladder_single_owner.py:302-309` sweeps integers,
   quarter-step nets and half-step obstacles only. Every one of those is exactly representable in binary,
   so the margin is exact and the tolerance cannot act: the assertion cannot observe the difference it
   excludes (CLAUDE.md §0.1 pt 2).
3. **Three rules for one quantity, a fraction of a die.** `sigma_leverage._dice_dealt` rounds
   (`max(1, int(round(pool)))`, and Python rounds half to even: 2.5 deals 2 dice, 3.5 deals 4);
   `roll_net_continuous` samples a Normal at the fractional pool; `roll_pool_fractional` deals the whole
   part and one more die with probability equal to the fraction. Probe (E-05), Partial-or-better at Ob 2:
   pool 2.49 → 26.00 % by rounding against 32.86 % by the stochastic die; pool 2.51 → 40.00 % against
   33.14 %. Rounding is a 14-point step at the half; the stochastic die is linear and is the same shape
   as `settle_margin`'s rule for a fraction of a margin (CP-T01-04).

## The resolution, decided

Ladder step 3 and 4. The ruling of 2026-08-15 (`registers/handoffs/HANDOFF_archive.md`, "Resolver
architecture — RULED") reads *"ONE resolver for all d10 probability"* and *"No system keeps its own
bands"*. The two other registered modules already import the dice engine
(`modules/social_contest/roll.py:60`, `modules/combat/core.py:20-21`); mass battle's isolation is recorded
in its own text as *"a porting-architecture call nobody has made"* (`resolution.py:104-106`), so no ruling
holds it. The call is made here: mass battle composes on the owner.

## The edits

**A.** *(Withdrawn, W3-1, C3-L1: the first text added `_MARGIN_EPS = 1e-9` to `degree_from_net`. The
margin is converted once at the ladder to integer milli-units, `round(MARGIN_SCALE × margin)`, and compared
with `BAND_FLOORS` in the same units (`U5a_DICE_owed_edits.md` §1 row 1;
`10_DICE_exported_face_rule_and_band_edges.md` Edit A), so no tolerance is needed and `04:903`, D-29 hold.)*

**B.** *(Withdrawn by the U5a head with the whole-dice roll, A-5; its body is removed, W3-1.)*

**C. `modules/mass_battle/resolution.py` (MB lane).** Each of the four becomes a call:

| today | becomes |
|---|---|
| `roll_pool(n, tn=7)` — own loop over `rngsource.get().randint(1, 10)` | `sigma_leverage.roll_net_continuous(pool, rng)` (A-5, W3-1: the bell curve; the draw is keyed when `11_GO_one_draw_owner.md` lands in B06, C3-D2) |
| `roll_pool_fractional(pool, tn=7)` | deleted (W3-1: one rule below one die, in the owner, `U5a_DICE_owed_edits.md` §1 rows 4–5) |
| `compute_degree(net, ob)` | `dice_engine.degree_label(net, ob)` over `degree_from_net`; `_DEGREE_EPS` deleted |
| `_sigma_softcap`, `_sigma_net_boost`, local `_SIG_PER_DIE = 0.800` | `sigma_leverage.soft_cap`, `sigma_leverage.net_boost`; `_SIGMA_ZERO_SNAP` stays in mass battle (its own producers' dust) |

`modules/mass_battle/config.py:302` `PER_DIE_NET_EV = 0.4` becomes `dice_engine.MU_PER_DIE`.

**D. Tests that move with it** (edited in the same commit, not added): `test_degree_ladder_single_owner.py`
drops the mass-battle row from `LADDERS` (it is a call now) and its `_PRODUCES_BAND` allowance;
`test_degree_boundary_epsilon.py` re-points its imports at the owner; `test_band_odds.py:115-119`
(`band_odds(2.6, 2) == band_odds(3, 2)`) is deleted with the fraction rule (W3-1, A-5); `test_tn7_always.py:95`'s
face-copy pin goes with the copy.

## The gate (execution artifacts)

*(Reconciled, W3-1, 7b-7: the byte-equal gates cannot hold under A-5.)*

1. `grep -rn "randint(1, 10)" modules/ engine/season/` prints nothing.
2. `U5a_DICE_owed_edits.md` §1 gate (2): the odds shown are the odds dealt, at that gate's stated n.
3. `python tools/export_sim_params.py --check` after `--build` (two literals leave mass battle).
4. Mass battle's golden batteries and every seeded field result re-recorded **once**, with the B05 batch's
   one re-pin, and said plainly in the commit.

## The falsifier

After the edit, `grep -rn "randint(1, 10)" modules/ engine/season/` prints nothing, and the probe in audit §12
(E-04) prints `0 of 10000` (one ladder). A degree graded by any function other than the owner's under
`modules/mass_battle` is the failure.

## NERS reading (CLAUDE.md §0.06; E last)

- **N.** Cut the second roller and nothing in play is lost but a second sampler: the field battle draws from
  the one bell curve (A-5). Tested
  bottom-up (one face rule), lateral (three modules, one import) and diagonal (the port transcribes one
  roller, one ladder).
- **R.** Completeness: the 1-ulp disagreement and the rounding step at a half pool are extremes where the
  present code breaks; both close.
- **S.** *Calculations consistent in methodology*: one die rule, one ladder class, and the fraction of a
  die and the fraction of a margin are settled the same way (paid in probability).
- **E, as a ratio.** Four functions and four literals leave the tree; one tolerance and one helper enter.

## Cost class

A small build in the MB lane (C), inside B05's one declared re-pin. Not design-first.

**Tests and lands (W3-1).** The four test files of Edit D; `tests/valoria/test_degree_ladder_single_owner.py`
with the mass-battle row gone; gate 1's grep as a test in `engine/season/tests/test_mass_battle_module.py::test_no_d10_face_in_mass_battle`.
Lands: an IN-lane implementation session under `/methodology-execute` with MB review; `sonnet`.
