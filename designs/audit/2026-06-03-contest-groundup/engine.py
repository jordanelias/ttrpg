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
MU_PER_DIE, SD_PER_DIE = 0.40, 0.80
OB_MIN, OB_MAX = 1, 20

# σ-leverage layer (armature §1): modifiers live in σ-space, soft-capped, converted to an Ob shift.
M_MAX = 1.5
LEVEL = {"minor": 0.25, "moderate": 0.50, "strong": 0.75, "major": 1.00}

def level(name):                    return LEVEL[name]
def sigma_N(pool):                  return SD_PER_DIE * sqrt(max(1, pool))
def eff_sigma(net_dsigma):          return M_MAX * tanh(net_dsigma / M_MAX)
def effective_ob(base_ob, net_dsigma, pool):
    return max(OB_MIN, base_ob - eff_sigma(net_dsigma) * sigma_N(pool))

def roll_net(pool):
    s = 0
    for _ in range(pool):
        d = random.randint(1, 10)
        s += -1 if d == 1 else (2 if d == 10 else (1 if d >= 7 else 0))
    return s

def degree(net, ob):
    """Canonical bands. Returns 0 Failure / 1 Partial / 2 Success / 3 Overwhelming."""
    if net <= 0:                       return 0
    if net < ob:                       return 1
    if net >= 2 * ob and net >= 3:     return 3
    return 2
