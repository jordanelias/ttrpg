# ─────────────────────────────────────────────────────────────────────────────
# COPIED OUT OF THE AUDIT ARCHIVE (2026-09-16, ED-IN-0231 — RULED by Jordan:
# "anything that is being read by engine.py needs to be copied over into a proper location")
#
# Original: .audit/2026-06-03-contest-groundup/engine.py
# Read by:  tools/gen_sigma_parity_goldens.py, to regenerate engine/tests/goldens/sigma_leverage_parity.json,
# which the BLOCKING `Sim Reference Regression` job asserts on
#
# THIS DESTINATION WAS ALREADY RULED, not chosen here: tools/evacuation_plan.py's R-REL-ORACLE
# names `engine/reference/contest-groundup/` and carries the execution steps (update the
# generator's load path in the same commit, regenerate, confirm byte-identical). It is the
# pre-designed home because build_fork.py already maps the OTHER parity oracle,
# tests/sim/v32-combat-balance, to engine/reference/v32-combat-balance — both frozen
# reference implementations in one place, beside the code they validate.
#
# WHY IT MOVED. `.audit/` is a HIDDEN archive — a historical record nothing should depend
# on. A live dependency reaching into it made the archive load-bearing, which is the
# opposite of what archiving it was for: the corpus could not be touched without risking a
# blocking job, and the dependency was invisible to anyone searching the tree normally.
# The archive keeps its copy as the historical record; THIS file is the live one. They are
# byte-identical below this header as of the copy, and are NOT kept in sync — if they ever
# diverge, this one is right and the archived one is history.
# ─────────────────────────────────────────────────────────────────────────────
"""
engine.py — the shared stochastic core. This is the universal Valoria resolution engine
(base d10 success-count + σ-leverage layer), verified 2026-06-02 against params/core.md and
the σ-leverage armature. It is mode-agnostic: it knows nothing about contests, only how a
pool resolves under leverage. Fixed; not tuned here.
"""
from math import sqrt, tanh
import random

# Base engine (params/core.md): net ~ Normal(0.40·pool, 0.80·√pool) at TN 7;
# die map 1→−1, 2-6→0, 7-9→+1, 10→+2; degrees Failure/Partial/Success/Overwhelming; Ob 1–20.
MU_PER_DIE, SD_PER_DIE = 0.40, 0.80  # [canonical: engine/autoload/dice_engine.py §_MU_PER_DIE/_SIGMA_PER_DIE — 0.40 / 0.800 at TN 7; also in this directory's sim_verification_ledger.json]
OB_MIN, OB_MAX = 1, 20
OVERWHELM_SIGMA = 0.85  # de-saturation (diagnostic Lesson 2): live degree-3 bar = pool mean + this·σ,
                        # holding the Overwhelming rate ≈ uniform (~21%) across pools instead of 20%→91%.

# σ-leverage layer (armature §1): modifiers live in σ-space, soft-capped, converted to an Ob shift.
M_MAX = 1.5
LEVEL = {"minor": 0.25, "moderate": 0.50, "strong": 0.75, "major": 1.00}

def level(name):                    return LEVEL[name]
def sigma_N(pool):                  return SD_PER_DIE * sqrt(max(1, pool))
def eff_sigma(net_dsigma):          return M_MAX * tanh(net_dsigma / M_MAX)
def effective_ob(base_ob, net_dsigma, pool):
    """DISPLAY-ONLY (not the resolution path, post ED-884 / ED-934): a floored 'effective
    difficulty' a UI may surface. Resolution applies advantage as net_boost (the mu-shift),
    which leaves base_ob untouched so the Ob floor (OB_MIN, P-232) is never breached."""
    return max(OB_MIN, base_ob - eff_sigma(net_dsigma) * sigma_N(pool))

def net_boost(net_dsigma, pool, capped=True):
    """Advantage as a mu-shift on the expected net (ED-884 resolution; ED-934 combat precedent):
    eff_sigma(dσ)·sigma_N(pool). The σ cancels in the z-score, so the modifier shifts the
    outcome z by exactly eff_sigma at every pool size (uniform impact, TN-exact); base_ob and
    TN are unchanged, so the Ob floor (OB_MIN, P-232) is never breached. This is the
    resolution-path modifier; effective_ob above is retained DISPLAY-ONLY. Replaces the
    pre-ED-884 Ob-reduction path that clamped at OB_MIN and reintroduced 1/√N non-uniformity."""
    eff = eff_sigma(net_dsigma) if capped else net_dsigma
    return eff * sigma_N(pool)

def roll_net(pool):
    s = 0
    for _ in range(pool):
        d = random.randint(1, 10)
        s += -1 if d == 1 else (2 if d == 10 else (1 if d >= 7 else 0))
    return s

def degree(net, ob, pool=None):
    """Canonical bands. Returns 0 Failure / 1 Partial / 2 Success / 3 Overwhelming.
       With `pool` given (live reception): Overwhelming requires clearing a σ-scaled bar
       (pool mean + OVERWHELM_SIGMA·σ), de-saturating the degree-3 rate to ~uniform across pool
       sizes (diagnostic Lesson 2). Pool-less calls keep the legacy 2·ob bar (unit tests only)."""
    if net <= 0:                       return 0
    if net < ob:                       return 1
    if pool is not None:
        thresh = MU_PER_DIE * pool + OVERWHELM_SIGMA * SD_PER_DIE * sqrt(max(1, pool))
        if net >= thresh and net >= max(3, ob): return 3
        return 2
    if net >= 2 * ob and net >= 3:     return 3   # legacy, pool-less unit tests only
    return 2
