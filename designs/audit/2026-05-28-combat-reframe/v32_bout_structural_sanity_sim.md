# v32 Bout Engine — Structural Sanity Sim

**Verdict: the v32 bout engine is structurally sound — it terminates, responds monotonically to build advantage, and the σ-space soft-cap holds the no-foreclosure property (F2) at the bout level. Balance is NOT validated and was not the target: v32's constants (base Ob, M_max, set bonuses, handling coupling) are all draft/sim-tunable, so a balance sim would only reflect the numbers I picked. This sim validates the *engine*, not the *numbers*.**

`[CONFIDENCE: high on structure — the three structural properties are robust to the constants; LOW/none on balance — explicitly out of scope]`

---

## What was tested, and why only structure

A balance sim of a system whose magnitudes are all "draft, sim-tunable" is circular — it measures the inputs, not the design. The non-circular questions are structural: *does the reframed state-graph engine behave sanely regardless of the eventual constants?* Four checks, 20k Monte Carlo bouts each, on the canonical d10 engine (1→−1, 2–6→0, 7–9→+1, 10→+2) with §12.3 σ-space modifiers (level→δσ, soft cap `eff = 1.5·tanh(net_σ/1.5)`, Ob shift `eff·0.8√pool`).

### 1. Termination ✓
Bouts mean **2.6 steps**, max **8**, **0%** hit the 12-step cap. The engine terminates cleanly; the cap is never the binding stop. No runaway / infinite-bind loop — the §12.6 termination structure works.

### 2. Monotonicity ✓
Win-rate rises smoothly with pool advantage (symmetric Ob, vs pool 10):

| A pool | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|
| A wins | 27% | 48% | 63% | 74% | 81% |

A better build wins more, with no inversion or discontinuity. This is the sane baseline — advantage converts to win-probability continuously (the A1/A2 σ-space + soft-cap shape working as intended).

### 3. No foreclosure (F2 at bout level) ✓
A under an escalating adverse σ stack (equal pools):

| A net_σ | 0 | −1.0 | −2.0 | −3.0 | −5.0 |
|---|---|---|---|---|---|
| A wins | 63% | 9% | 2% | 2% | 2% |

Even a crushing disadvantage leaves A winning **~2%, never 0%** — the `tanh` saturates, so −3.0 and −5.0 clamp to the same floor. F2 (no modifier stack forecloses an outcome) holds through a full multi-step bout. The bout-level floor (~2%) is lower than the single-roll floor (~9%, F2 §12.3) because the disadvantage reapplies every step — expected and still strictly positive.

### 4. Fast vs Strong — illustrative only, NOT a verdict
`Fast(pool 12, Ob 2.0) vs Strong(pool 10, Ob 1.5) → Fast 73% / Strong 27%.`
**This is constant-dependent and not a balance claim.** The numbers are draft, and the model artifact below inflates the higher-pool side. Real Fast-vs-Strong balance is I-17 (Phase 11–14 sims with tuned constants + the full sub-action/CLP model).

---

## Honest artifact: equal pools give A 63%, not 50%

The simultaneous-resolution model resolves a same-step double-fell to **A** (A's wound-to-B is checked before B's felled-state), so "ties" on a same-step double-KO go to A. This is a **model artifact of the declaration order, not a v32 property** — v32 has a clash tiebreaker (§4.7) that would govern this, not an unconditional first-mover win. The artifact does not affect checks 1–3 (termination, the *shape* of monotonicity, and the no-foreclosure floor are all robust to it); it only means the absolute win-rates sit above 50% baseline. Do not read the 63% (or the §4 Fast 73%) as a balance figure.

---

## Scope boundary

Validates: engine terminates, monotonic in advantage, σ-space soft-cap prevents foreclosure across a full bout. Does **not** validate: build balance, weapon-class balance, handling necessity (N5), transition-discontinuity feel (N1) — all of which need tuned constants and the complete sub-action/CLP model (I-17). This sim is a green light on *implementability and well-behavedness*, not on *balance*.

`[SELF-AUTHORED — bias risk: this validates an engine I designed. Guarded by (a) scoping to structure not balance — refusing the flattering balance claim the draft constants can't support, (b) disclosing the 63% declaration-order artifact rather than reporting it as a 50/50 baseline, (c) flagging check 4 as constant-dependent. An independent reviewer would add: the bout model is simplified (no explicit state-by-state sub-action policy, no resource/Stamina depletion, no facing) — so "terminates and is monotonic" is necessary but not sufficient for the full engine; the Phase 11–14 sims remain the real test.]`

---

## Reproducible sim code

```python
import numpy as np
rng = np.random.default_rng(42)

def roll_net(pool):                      # canonical d10 engine
    pool = max(1, int(round(pool)))
    d = rng.integers(1, 11, size=pool)
    return np.where(d==1,-1, np.where(d<=6,0, np.where(d<=9,1,2))).sum()

M = 1.5                                   # §12.3 soft-cap M_max
def eff_ob(base_ob, pool, net_sigma):     # σ-space modifier -> Ob shift
    sN = 0.8*np.sqrt(max(1,pool))
    return base_ob - M*np.tanh(net_sigma/M)*sN

def bout(pA,pB,oA,oB,sA,sB,maxsteps=12):  # simultaneous-resolution bout
    wA=wB=0
    for step in range(maxsteps):
        nA=roll_net(pA); nB=roll_net(pB)
        if nA >= eff_ob(oA,pA,sA)+wB: wB+=1   # artifact: A checked first
        if nB >= eff_ob(oB,pB,sB)+wA: wA+=1
        if wB>=3: return 'A',step              # felled at MW+1
        if wA>=3: return 'B',step
    return ('A' if wB>wA else 'B' if wA>wB else 'D'), maxsteps
# winrate = fraction of N bouts returning 'A'
```

`[READ: combat_v32_proposal.md §4.7 (clash tiebreaker / termination), §12.3 (σ-space soft cap), §12.6 (bout chain termination)]`
