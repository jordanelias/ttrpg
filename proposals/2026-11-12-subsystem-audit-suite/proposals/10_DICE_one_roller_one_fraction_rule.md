# DICE — one roller, one ladder class, one rule for a fraction of a die

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-13) — A-5 (the bell curve everywhere) changes what the owner's roll is. Edit A (`_MARGIN_EPS`) and Edit C (mass battle composes on the owner) stand, with the owner's roll now `roll_net_continuous`; **Edit B (the stochastic die in `roll_net`) is withdrawn** with the whole-dice roll; the gate's *byte-equal goldens* cannot hold and is replaced by one declared re-pin; the falsifier reads: `grep -rn "randint(1, 10)" modules/ engine/season/` prints nothing (addendum C-4). Below one die there is one rule in the owner (`U5a_DICE_owed_edits.md` §1 rows 4–5).

## Status: PROPOSED

Carries findings F-DICE-07 and F-DICE-08 of `../audits/10_DICE_audit.md`. Lanes that own the
edited files: IN (the dice engine), MB (`modules/mass_battle/resolution.py`).

## What it changes in `engine/season/` at runtime

Nothing at the shipped arms, by construction, and that is the gate. The season's social roll deals whole
dice from whole pools (`seam/wrappers/pool.py::faculty` returns `int`), so the fractional-pool rule is
unreached there; a fought field draws the same `randint(1, 10)` per die in the same order as today, so its
stream and the season's `World.content_hash()` are unmoved. What changes is that a field battle's dice,
bands and sigma boost are the dice engine's own functions instead of copies, and that a fractional pool
has one meaning wherever whole dice are dealt.

## The problem, with evidence

1. **A second roller exists.** `modules/mass_battle/resolution.py:37-55` (`roll_pool`) rolls its own d10s
   and spells the face rule a second time; `:57-77` (`roll_pool_fractional`) is a third fractional-pool
   rule; `:101-120` (`compute_degree`) is a ladder copy with a `1e-9` tolerance the owner lacks;
   `:209-230` (`_sigma_softcap`, `_sigma_net_boost`) re-type `soft_cap`, `net_boost` and the per-die sigma
   `0.800`. `modules/mass_battle/` imports nothing from `engine.*` (grep: zero import lines).
   `march` reaches it from the loop (`seam/wrappers/mass_battle.py`).
2. **The two ladders are not one behavioural class.** Probe (audit §12, E-04): over `net, ob ∈ {i·0.1}`,
   6 of 10,000 cells differ (for example `net 4.3, ob 3.3`: owner Partial, mass battle Success); over
   `{i/40}`, 72 of 160,000. `tests/valoria/test_degree_ladder_single_owner.py:302-309` sweeps integers,
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

**A. `engine/dice_engine/dice_engine.py` (owner of the ladder).** Give the ladder the tolerance its copy
needed, once:

```python
_MARGIN_EPS = 1e-9   # ulp recovery at a band edge; no designed quantity resolves at 1e-9

def degree_from_net(net, ob, extension=None, **context) -> Degree:
    margin = net - ob
    if margin < -_MARGIN_EPS:      return Degree.FAILURE
    if margin < 1 - _MARGIN_EPS:   return Degree.PARTIAL
    if margin >= 3 - _MARGIN_EPS:  ...extension branch, unchanged...
    return Degree.SUCCESS
```

The season path grades an integer `settled_margin` against 0 and is untouched. Combat's nets are Normal
draws; a draw within `1e-9` of an edge has probability of order `1e-9` per roll.

**B. `engine/dice_engine/sigma_leverage.py` (owner of the whole-dice roll).** Replace the rounding with
the stochastic die, in the two functions that already share one rule:

```python
def _dice_split(pool) -> tuple[int, float]:
    """(whole dice, chance of one more): floor and fraction of the pool, floored at one die."""
    p = max(1.0, float(pool)); whole = math.floor(p); return whole, p - whole

def roll_net(pool, tn=TN_STANDARD, rng=None) -> int:
    whole, frac = _dice_split(pool)
    rng = rng if rng is not None else random.Random()
    net = dice_engine.roll_pool(whole, tn=tn, rng=rng).net
    if frac > 0.0 and rng.random() < frac:        # drawn only when there is a fraction
        net += dice_engine.roll_pool(1, tn=tn, rng=rng).net
    return net
```

`band_odds` enumerates the same mixture: `(1 - frac) · counts(whole) + frac · counts(whole + 1)`, exact in
`Fraction`. A whole pool draws nothing extra, so every shipped stream is as it was. Note the floor moves:
a sub-1D pool deals one die as today. Mass battle's own sub-1D rule (below one die, a die with
probability equal to the pool, `resolution.py:72-76`) is a different floor; it stays in
`roll_pool_fractional`, which keeps its body and calls the engine's `roll_pool` for the dice (see C).

**C. `modules/mass_battle/resolution.py` (MB lane).** Each of the four becomes a call:

| today | becomes |
|---|---|
| `roll_pool(n, tn=7)` — own loop over `rngsource.get().randint(1, 10)` | `dice_engine.roll_pool(n, tn=tn, rng=rngsource.get()).net` (same draws, same order; `rngsource.get()` is a `Random` or the stdlib module, both carry `randint`) |
| `roll_pool_fractional(pool, tn=7)` | kept, body unchanged; its two `roll_pool` calls are now the engine's dice (its sub-1D floor is mass battle's own) |
| `compute_degree(net, ob)` | `dice_engine.degree_label(net, ob)`; `_DEGREE_EPS` deleted |
| `_sigma_softcap`, `_sigma_net_boost`, local `_SIG_PER_DIE = 0.800` | `sigma_leverage.soft_cap`, `sigma_leverage.net_boost`; `_SIGMA_ZERO_SNAP` stays in mass battle (its own producers' dust) |

`modules/mass_battle/config.py:302` `PER_DIE_NET_EV = 0.4` becomes `dice_engine.MU_PER_DIE`.

**D. Tests that move with it** (edited in the same commit, not added): `test_degree_ladder_single_owner.py`
drops the mass-battle row from `LADDERS` (it is a call now) and its `_PRODUCES_BAND` allowance;
`test_degree_boundary_epsilon.py` re-points its imports at the owner; `test_band_odds.py:115-119`
(`band_odds(2.6, 2) == band_odds(3, 2)`) is re-stated as the mixture; `test_tn7_always.py:95`'s face-copy
pin goes with the copy.

## The gate (execution artifacts)

1. `python -m pytest engine/tests modules/mass_battle -q` and mass battle's golden batteries byte-equal
   before and after (the dice stream is unchanged).
2. `PYTHONHASHSEED=0 python -m engine.season.harness.headless --seasons 2 --seed 0`: the same
   `CONTENT HASH` before and after; a run that fights a field (`engine/season/tests/test_march.py`) equal.
3. `python tools/export_sim_params.py --check` after `--build` (two literals leave mass battle).

## The falsifier

After the edit, `grep -rn "randint(1, 10)" modules/ engine/` prints one line, in `dice_engine.roll_pool`.
The probe in audit §12 (E-04) prints `0 of 10000`. If either mass-battle golden or the season hash moves,
the claim "same draws, same order" is false and the edit is reverted.

## NERS reading (CLAUDE.md §0.06; E last)

- **N.** Cut the second roller and nothing in play is lost: the field battle rolls the same dice. Tested
  bottom-up (one face rule), lateral (three modules, one import) and diagonal (the port transcribes one
  roller, one ladder).
- **R.** Completeness: the 1-ulp disagreement and the rounding step at a half pool are extremes where the
  present code breaks; both close.
- **S.** *Calculations consistent in methodology*: one die rule, one ladder class, and the fraction of a
  die and the fraction of a margin are settled the same way (paid in probability).
- **E, as a ratio.** Four functions and four literals leave the tree; one tolerance and one helper enter.

## Cost class

Edit (A, B) plus a small build in the MB lane (C), with a golden-equality gate. Not design-first.
