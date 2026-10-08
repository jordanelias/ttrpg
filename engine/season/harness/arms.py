"""arms.py — the n-seed two-arm CONTROLLED comparison, ported from `tools/balance_oracle.py`
onto `engine/season`'s own `build_realm` + season-loop execution (plan position `28-i`, M5).

WHY THIS IS NOT A FILE COPY. `tools/balance_oracle.py` ran the old faction/strategic-scale
campaign driver's `run_campaign` (deleted at plan position `28-iii`) under one mechanic patched to its old and new
behaviour, tallied a WINNER per campaign, and reported a per-faction win-share delta with a
two-proportion z. `engine/season/` has no campaign, no winner and no faction-elimination
condition, so none of that host loop survives the port unchanged. What DOES survive is the
shape of the question: run `n` seeds under two settings of the SAME mechanic, in the same
process, on the same seed sequence, and report a delta with the control CLAUDE.md §0.1 pt 4
requires — "a number without a control is not a measurement, in either direction."

⚠ THE OLD LIVE COMPARISON (`private_ladder`/`owner_ladder`) DOES NOT COME ALONG, AND THIS IS A
FINDING FROM THIS PORT, NOT A CHOICE MADE FOR CONVENIENCE. It patched
`systems.social_contest.sim.contest.resolver.degree_from_net` and `degree_extension.degree` —
the SUBSYSTEM's own copy of the ladder. Verified against the live tree (2026-09-29):
`engine/season/seam/ladder.py`'s `degree_of()` (the ONLY place a subsystem result becomes a band
the season loop writes on) has three branches — `combat_degree` for a `wound_state` result,
`field_degree` for a mass-battle result, and for a `net`/`ob` margin it calls
`degree_ladder()` (`:88-108`), which imports `engine.dice_engine.dice_engine.degree_from_net`
BY DOTTED PATH, directly — never `systems.social_contest.sim.contest.resolver`. The season
loop's own "a standing" contest (the `tell` verb, `seam/wrappers/sigma.py`) is graded through
that engine-owned ladder, not the subsystem's. So patching the subsystem's copy from inside
`engine/season/` would leave BOTH arms of a `build_realm`-based comparison identical by
construction — exactly the "campaign-unreachable change" CLAUDE.md §7 names as a FAKE CONTROL,
not a measurement. This is the same shape of mistake `rosters.yaml`'s own
`field_casualty_models` note (see below) already warns about for a DIFFERENT campaign-driver-only tool
reaching for a season-only question; here it is the reverse defect, a season-side tool reaching
for a question outside its own subsystem's wiring.

⚠ A SECOND, STRUCTURAL REASON IT DOES NOT COME ALONG. `_contest_ladder_arm`'s patch imports
`systems.social_contest.sim.contest.degree_extension`/`resolver` — a `systems.*` import. Carrying
that function into a file under `engine/` (even as inert, retired, "importable but not wired in"
code, as the other retired pair is kept below) would add a NEW nested `engine -> systems`
import that `tests/valoria/test_engine_does_not_import_systems.py`'s `NESTED_BASELINE = 0` ratchet
does not permit without a deliberate, separately-justified bump to that ceiling — outside this
position's declared file scope. Both findings point the same way, so the mechanic is retired in
full rather than carried forward inert. Its code is not lost: `tools/balance_oracle.py` gets a
`FORK:` row at this commit's own SHA in `references/restructure_ledger.md`, same as every other
retirement, and the function is there verbatim for anyone who needs the historical record of what
the pre-ED-SC-0032 private ladder did.

WHAT REPLACES IT AS THE LIVE COMPARISON: `field_casualty_model` (H-148), and the choice is not
invented here — `rosters.yaml`'s own `field_casualty_models` note (2026-09-04/M4) says so by name:

    "`tools/balance_oracle.py` DOES NOT APPLY TO THIS QUESTION AND MUST NOT BE RUN FOR IT. That
    tool patched `dice_engine` and compared campaign-driver arms (the driver was deleted at
    plan position `28-iii`); `march` and
    `field_casualty_model` live entirely in `engine/season/`, which that driver could not reach ...
    Patching it would leave both of `balance_oracle.py`'s arms identical by construction --
    exactly the 'campaign-unreachable change' CLAUDE.md §7 names as a fake control, not a
    measurement. If this arm is ever re-examined, the instrument is a `field_casualty_model` sweep
    through `engine/season`'s own corpus."

This port IS that re-examination. `field_casualty_model` is read by exactly one call site,
`loop/effects.py::_eff_march`'s `perform()`, on every LOST field battle: `scaled_by_degree` (the
ruled default — Jordan, 2026-09-04, "the combat engine determines the result there," applied to
this magnitude the same way it was to `wound_harm_model`'s) scales the losing side's body by the
engine's own survivor ratio and floors at 1 — a wound, never a kill; `total` re-runs the pre-M4
defect deliberately, "losing costs everything," and floors at 0 (`w.remove_person` follows). Both
values are real, live, season-reachable settings of a fixture `build_realm`'s own world already
carries (`data/fixtures.py:521`, default `scaled_by_degree`) — no monkeypatch of module-global
state is needed, unlike the retired arms below: each `World` owns its own `Fixtures`, so an arm is
applied by handing the freshly-built world a swept copy (`w.fixtures = w.fixtures.sweep(...)`,
the exact idiom `harness/populated.py::creed_sweep` and `engine/season/tests/test_march.py`
already use for this same fixture) before the season loop runs on it.

THE OUTCOME METRIC. There is no win-share on the season side (CLAUDE.md's plan for this position
says so explicitly). What `populated.run()` already computes, and what `creed_sweep` (the one
existing season-side two-arm comparison, `harness/populated.py`, ED-IN-0229) already treats as ITS
effect signal, is `act_subjects` — the count of resolved acts naming another person, a self, or
"not a person," summed straight from the census `populated.census()` builds every run. Reusing it
here (rather than inventing a new field) is the same discipline CLAUDE.md §8 asks for: compose on
the existing single owner. `two_proportion_z` is generalised to take each arm's own `n` (the two
arms' total resolved-act counts will differ slightly once a battle actually kills someone, since a
dead person acts in no later season) rather than assuming one shared `n`, which is the special
case `na == nb` reduces to.

⚠ THE SAME PAIRED-SAMPLE CAVEAT `two_proportion_z`'s original docstring carried still applies, and
for the same reason: both arms run the IDENTICAL seed sequence (`base_seed + i`), which is the
point — it removes between-arm variance so the fixture is the only difference — but a
two-proportion z assumes independent samples, so on paired, correlated arms it OVERSTATES the
standard error and UNDER-DETECTS a real shift. The bias runs toward the null, the safe direction
for a control.

WHAT THIS PORT DID NOT VALIDATE. `populated.build_realm(0)` measured at 0.77s and one seed of
`populated.run(seasons=2, seed=0)` at 46.7s (2026-09-29, this session, on the working tree at this
commit) — a single seed, not the full default `n`/`--seasons` invocation below. Field battles are
DECLARED at RESOLVE and fought later at ENCOUNTER (M4), so a `march` needs to survive past
DECLARED into a resolved WON/LOST before `field_casualty_model` has anything to bite on; that one
seed's 2 seasons produced 9 DECLARED marches and 0 resolved ones. Whether the DEFAULT `--n`/
`--seasons` below produce enough resolved field battles to move `act_subjects` by a measurable
amount was NOT run in this session — the honest position, per CLAUDE.md §0.1 pt 3, is to say so
rather than to imply a validated default. The tool prints how many acts and how many resolved
field battles it saw, so a reader can judge the sample size for themselves.

HOW TO ADD AN ARM. `ARMS` maps a name to the `field_casualty_model` value that arm runs under.
Keep exactly two, in one process, on the same seed sequence — running them as two invocations
reintroduces every between-process difference the control exists to remove.

Usage:
    python3 -m engine.season.harness.arms                  # default: n=10, 2 seasons/seed
    python3 -m engine.season.harness.arms --n 30 --seasons 4
    python3 -m engine.season.harness.arms --seed 20260819
"""
from __future__ import annotations

import argparse
import collections
import math

from ..data.rosters import FIELD_CASUALTY_MODELS
from . import populated

# Absolute imports reachable without a `sys.path` hack: this module is a real package member
# (`engine.season.harness.arms`), unlike the standalone script it replaces, which had to insert
# the repo root by hand to be runnable as `python3 tools/balance_oracle.py`.
from engine.dice_engine import dice_engine, sigma_leverage as SL  # noqa: F401 (kept for _pool_arm)

# [JUSTIFIED: the conventional two-sided 5% critical z-value, unchanged from `tools/balance_oracle.py`'s identical constant — a standard statistical threshold, not a fitted game magnitude]
Z_THRESHOLD = 1.96          # two-sided 5%


# ---------------------------------------------------------------------------------------------
# THE LIVE COMPARISON — season-reachable, fixture-driven. No undo needed: each arm hands a fresh
# `World` its own swept `Fixtures` copy before the season loop runs on it, so nothing global is
# ever mutated and there is nothing to restore.
# ---------------------------------------------------------------------------------------------

#: `total` is the pre-M4 control ("losing costs everything", the code as it stood before
#: `field_casualty_model` existed); `scaled_by_degree` is the ruled default. Swap in `none` (the
#: second control, isolating the write from the band) to re-run the three-way comparison
#: `engine/season/tests/test_march.py` already exercises structurally; kept to two arms here on
#: the same "keep exactly two" discipline `tools/balance_oracle.py` stated.
ARMS = {
    'total':            'total',
    'scaled_by_degree': 'scaled_by_degree',
}

# Assert the two values are what we think they are BEFORE running anything — the same discipline
# `_contest_ladder_arm` stated and the same reason it broke once (ED-SC-0032 moved its target out
# from under it). A value the roster no longer carries would make `_eff_march` raise `Ungraded`
# mid-run instead of failing here, cheaply, at import time.
assert len(ARMS) == 2, f'expected exactly two arms, got {sorted(ARMS)}'
assert len(set(ARMS.values())) == 2, 'the two arms must differ, or the comparison is a fake control'
for _name, _model in ARMS.items():
    assert _model in FIELD_CASUALTY_MODELS, (
        f'arm {_name!r} names {_model!r}, not in `field_casualty_models` '
        f'({sorted(FIELD_CASUALTY_MODELS)}) — the roster moved and this arm no longer reaches it')
del _name, _model


def run_arm(model: str, n: int, base_seed: int, seasons: int) -> dict:
    """`n` seeded realms, `field_casualty_model` swept to `model`, `seasons` seasons each.

    Returns `{'tally': Counter(act_subjects), 'acts': total resolved acts, 'seeds': n}`. Building
    and running are ONE step per seed (`populated.run`'s own `w=` parameter lets a caller build
    first and inspect after; not needed here, since `act_subjects` is already the census field this
    reads).
    """
    tally: collections.Counter = collections.Counter()
    total_acts = 0
    for i in range(n):
        w = populated.build_realm(base_seed + i)
        w.fixtures = w.fixtures.sweep('field_casualty_model', model)
        out = populated.run(seasons, base_seed + i, None, w=w)
        total_acts += out['acts']
        for k, v in out['act_subjects'].items():
            tally[k] += v
    return {'tally': tally, 'acts': total_acts, 'seeds': n}


def two_proportion_z(a_count: int, a_n: int, b_count: int, b_n: int) -> float:
    """Pooled two-proportion z, generalised to two independent denominators.

    `tools/balance_oracle.py`'s original assumed one shared `n` (the campaign count, identical for
    both arms by construction). Here the two arms' total resolved-act counts can differ once a
    battle actually kills someone under `total` and does not under `scaled_by_degree` — a dead
    person acts in no later season — so each arm supplies its own denominator. `a_n == b_n`
    reduces to the original formula exactly.

    ⚠ SAME PAIRED-SAMPLE CAVEAT AS THE ORIGINAL: both arms run the IDENTICAL seed sequence, so
    treating them as independent OVERSTATES the standard error and UNDER-DETECTS a real shift.
    Read a non-significant result as "no shift large enough for an independence-assuming test to
    see", not as "no shift". The bias runs toward the null, the safe direction for a control.

    Returns 0.0 when the pooled rate is degenerate (0 or 1) or either arm saw zero trials."""
    if a_n <= 0 or b_n <= 0:
        return 0.0
    pooled = (a_count + b_count) / (a_n + b_n)
    if pooled <= 0 or pooled >= 1:
        return 0.0
    se = math.sqrt(pooled * (1 - pooled) * (1.0 / a_n + 1.0 / b_n))
    if se == 0:
        return 0.0
    return ((b_count / b_n) - (a_count / a_n)) / se


# ---------------------------------------------------------------------------------------------
# RETIRED ARM — historical record only, same status as `tools/balance_oracle.py` gave it:
# "kept as historical records, importable/constructible but not wired into ARMS." Ported
# VERBATIM (unchanged logic) because it imports no `systems.*` and still constructs and
# undoes cleanly against the live tree (verified 2026-09-29). THE OTHER TWO PAIRS THAT WERE PORTED WITH
# IT, `_ARMS_BOUNDS` (`_pre_ruling_bounds_arm`) AND `_ARMS_FLOOR` (`_floor_arm`), WERE DELETED AT PLAN
# POSITION `29b` (2026-10-01): they patched `descriptors.faction_bounds` and `game_state.Faction.adjust`,
# both deleted with the faction layer, and their own note said they ran against the old campaign driver's
# Faction model, deleted at `28-iii`. Their source is at the `FORK:` ref in `references/restructure_ledger.md`.
# `_contest_ladder_arm` does NOT
# appear here — see the module docstring for why it is retired to the `FORK:` ref instead of
# carried forward inert.
# ---------------------------------------------------------------------------------------------

def _pool_arm(round_pool: bool):
    """Patch `roll_net_continuous` to round (the pre-2026-08-21 behaviour) or not. Returns undo."""
    original = SL.roll_net_continuous

    def patched(pool, tn=SL.TN_STANDARD, rng=None):
        p = max(1, int(round(pool))) if round_pool else max(1.0, float(pool))
        return dice_engine.continuous_engine_sample(pool=float(p), tn=tn, rng=rng)

    SL.roll_net_continuous = patched
    return lambda: setattr(SL, 'roll_net_continuous', original)


#: Retired comparison, kept because `_pool_arm` is the record of what `roll_net_continuous` did
#: before M1 juncture 1 half A.
_ARMS_POOL = {
    'rounded':    lambda: _pool_arm(True),
    'fractional': lambda: _pool_arm(False),
}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--n', type=int, default=10, help='realms PER ARM (default 10)')
    ap.add_argument('--seasons', type=int, default=2, help='seasons per realm (default 2)')
    # [JUSTIFIED: the base seed `tools/balance_oracle.py` defaulted to, carried unchanged so a default-invocation result stays comparable to that tool's own past runs — arbitrary but fixed]
    ap.add_argument('--seed', type=int, default=20260819, help='base seed (default 20260819)')
    args = ap.parse_args(argv)

    names = list(ARMS)
    results = {name: run_arm(ARMS[name], args.n, args.seed, args.seasons) for name in names}
    a, b = results[names[0]], results[names[1]]
    categories = sorted(set(a['tally']) | set(b['tally']))

    print(f"\n{args.n} realm(s) per arm, {args.seasons} season(s) each, "
          f"seeds {args.seed}..{args.seed + args.n - 1}")
    print(f"total resolved acts — {names[0]}: {a['acts']}, {names[1]}: {b['acts']}\n")
    print(f'{"act subject":<16}{names[0]:>11}{names[1]:>13}{"delta pp":>11}{"z":>9}')
    significant = []
    for cat in categories:
        ac, bc = a['tally'].get(cat, 0), b['tally'].get(cat, 0)
        pa = 100 * ac / a['acts'] if a['acts'] else 0.0
        pb = 100 * bc / b['acts'] if b['acts'] else 0.0
        z = two_proportion_z(ac, a['acts'], bc, b['acts'])
        flag = '  SIGNIFICANT' if abs(z) > Z_THRESHOLD else ''
        if flag:
            significant.append(cat)
        print(f'{str(cat):<16}{pa:>10.1f}%{pb:>12.1f}%{pb - pa:>+10.1f}{z:>+9.2f}{flag}')

    print()
    if significant:
        print(f'[arms] {len(significant)} act-subject categor(y/ies) shifted significantly: '
              f'{", ".join(map(str, significant))}. The mechanic MOVED the acted-on population.')
    else:
        print(f'[arms] no category shifted significantly (|z| <= {Z_THRESHOLD}). This is a '
              f'CONTROL, not proof of no effect — it bounds the effect at this n, it does not '
              f'exclude one. See the module docstring for what this run did not validate.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
