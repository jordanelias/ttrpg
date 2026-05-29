# Faction Resolution — Remediation Development (Tested Candidates)

**Date:** 2026-05-28
**Develops:** ED-876 (P1, Trigger-5 cliff), ED-874 (P2, faction σ-leverage non-uniform), ED-865/F1 (P2, bare-pool degeneracy) — the connected faction-side cluster, all rooted in "faction rolls a bare stat as a small pool with no aggregation."
**Method:** resolution-diagnostic skill **Stage 4** — run the diagnostic on each *proposed* fix to verify it flattens the target defect **without introducing new defects**. Sim: `sim_faction_remediation.py` (this folder), 60k–120k-trial MC, authoritative die rule.
**Owner contract:** this produces **tested candidates with measured trade-offs.** It does **not** choose the faction redesign — the design decision (and the exact aggregation formula / resolver parameters) is Jordan's. PROPOSED parameters are flagged as such.
**Bias:** `[SELF-AUTHORED — bias risk]`. §4 surfaces what each candidate costs, not just what it fixes.

---

## §0 — Headline

**Two of the three findings have a clean shared fix; the third splits in two and only half of it is fixable by aggregation — which is itself the result.**

1. **ED-876 (Trigger-5 cliff) — clean fix found, Stage-4 passes.** Removing the `pool ≥ 6` clause from Condition C's *gate* (keeping it in the *cost* table) flattens the firing curve from non-monotonic to monotonic and removes the 25× Cmd-3 collapse spike, while still punishing 100% of genuine routs. **Recommend.**
2. **ED-865/F1 (floor degeneracy) — fixable by either aggregation or deterministic+stochastic.** The bare-2D 0.070 problem rises to ~0.47 (aggregation) or 0.30 (deterministic). Either works at the floor.
3. **ED-874 (σ-leverage non-uniformity) — NOT fixable by pool aggregation, only by deterministic+stochastic.** σ-leverage ∝ 1/√baseline is irreducibly non-uniform for *any* dice pool; aggregation narrows it but pushes leverage below band, and a ×2 multiplier makes it worse. A deterministic+stochastic resolver gives constant leverage by construction. **This is a new structural argument** for the deterministic+stochastic direction on the σ-leverage dimension specifically.

---

## §1 — ED-876: Trigger-5 Condition C smoothing (Stage-4 PASS)

**Defect (CC-5):** Condition C fires the gate on `net ≤ −2 OR pool ≥ 6 OR officer-lost`. The `pool ≥ 6` clause auto-fires on *any* failure once the pool reaches 6D, so battle→Stability exposure leaps 8.7× at Cmd 2→3 and compound collapse jumps ~25× (0.9% → 22.6%).

**Fix-A:** remove `pool ≥ 6` from Condition C (the *gate*). Keep it in the *cost* table (an already-triggered loss is still −2 at pool ≥ 6). The gate then fires on a genuine rout (`net ≤ −2`) or officer loss only.

**Stage-4 result — firing rate by defender pool, current vs Fix-A:**

| Faction Cmd | Pool | Current firing | **Fix-A firing** |
|---|---|---|---|
| 1 | 2D | 0.0% | 0.0% |
| 2 | 4D | 1.9% | 1.9% |
| **3** | **6D** | **16.4%** | **1.7%** |
| 4 | 8D | 11.3% | 1.4% |
| 5 | 10D | 7.9% | 1.1% |

The curve goes **monotonic and flat** (~1–2%, the genuine-rout rate) — the Cmd-3 cliff is gone.

**Stage-4 new-defect check — are genuine large-force routs still punished?** Of actual rout outcomes (`net ≤ −2`) at large pools, Fix-A still applies a Stability cost **100%** (840/840 at 8D; 661/661 at 10D). Only "disciplined withdrawal" failures (net 0 / −1) at large pools are now spared — which **matches the canonical intent verbatim** ("Partial excluded — disciplined withdrawal, no Stability cost"). No new defect. The fix narrows the gate to exactly what the design says it should catch.

**Recommendation:** apply Fix-A. It is minimal (one clause moved from gate to cost-only), removes a P1 robustness defect (single attribute point → 25× collapse swing), and is fully consistent with the rule's stated intent. `[CONFIDENCE: high]`

---

## §2 — ED-865/F1 + ED-874: the resolver shape (two halves, different answers)

The bare-stat faction pool has two distinct problems. The Stage-4 sweep shows they do **not** share a fix.

### §2a — Floor degeneracy (ED-865/F1): fixable by either route

P(success) at a weak faction, by resolver:

| Resolver | stat 2 vs Ob 2 | stat 2 vs Ob 3 | stat 7 vs Ob 4 |
|---|---|---|---|
| Bare pool (current) | 0.262 | **0.070** | 0.361 |
| Flat-aggregated (+4) [PROPOSED] | 0.669 | 0.471 | 0.626 |
| Deterministic+stochastic [PROPOSED] | 0.300 | 0.300 | 0.800 |

The degenerate 0.070 bare-2D pivotal action rises to a playable ~0.47 (aggregation) or 0.30 (deterministic). **Either route fixes the floor.** Ceiling new-defect check: flat-agg at stat 7 vs an easy Ob 2 reaches 0.865 (not auto-success); deterministic is capped at 0.90. Neither trivializes the ceiling.

### §2b — σ-leverage uniformity (ED-874): NOT fixable by aggregation

σ-leverage per stat point across the range (armature band [0.24, 0.36]):

| stat | Bare pool (mult 1) | Flat-agg +4 (mult 1) | ×2 pool (mult 2) |
|---|---|---|---|
| 2 | 0.354 (in) | 0.204 (low) | 0.500 (HIGH) |
| 3 | 0.289 (in) | 0.189 (low) | 0.408 (HIGH) |
| 4 | 0.250 (in) | 0.177 (low) | 0.354 (in) |
| 5 | 0.224 (low) | 0.167 (low) | 0.316 (in) |
| 6 | 0.204 (low) | 0.158 (low) | 0.289 (in) |
| 7 | 0.189 (low) | 0.151 (low) | 0.267 (in) |
| **spread** | **0.165** | **0.053** | **0.233** |

**The structural finding:** σ-leverage = (0.4·mult)/(0.8·√baseline) ∝ 1/√baseline, which is **irreducibly non-uniform for any dice pool**:
- **Flat aggregation** narrows the spread (0.165 → 0.053) but pushes the *entire curve below the band* — it trades non-uniformity for **uniformly low leverage** (a stat point barely moves outcomes). Not a fix; a different defect.
- **×2 multiplier** makes low-stat leverage *too high* (0.500) — worse uniformity (spread 0.233).
- **No pure pool transformation** lands σ-leverage uniformly in-band across the stat range, because the √baseline term cannot be made constant while the pool scales with the stat.

**Deterministic+stochastic** (P = clamp(base + slope·stat)) gives **leverage = slope = constant by construction** — perfectly uniform across the range (0.10/pt at the [PROPOSED] base 0.10 / slope 0.10 / cap 0.90), with the cap preventing auto-success. **This is the only tested resolver that fixes ED-874.**

---

## §3 — The decision this forces (Jordan's call)

The cluster does not have one fix; it has a **fork**, and the Stage-4 evidence sharpens it:

| Finding | Aggregate the pool (ER-9) | Deterministic+stochastic (GD-2-orthogonal; CK3/EU/KoDP) |
|---|---|---|
| ED-865 floor degeneracy | **fixes** (0.070 → 0.47) | **fixes** (→ 0.30) |
| ED-874 σ-leverage uniformity | **does NOT fix** (pushes leverage low) | **fixes** (constant leverage) |
| ED-876 Trigger-5 cliff | independent — Fix-A applies either way | independent — Fix-A applies either way |
| Disruption to canon | smaller (keeps the dice-pool paradigm) | larger (new resolver shape for faction scale) |
| In-project precedent | mass-battle summed pool | none at faction scale |

**The honest read:** if σ-leverage uniformity (ED-874) is a requirement, **only deterministic+stochastic satisfies it** — pool aggregation cannot, and the Stage-4 sweep proves it rather than asserting it. If ED-874 is acceptable-as-low-priority and the floor degeneracy (ED-865) is the real concern, **aggregation is the smaller-disruption fix.** This is a genuine design trade-off (paradigm disruption vs σ-leverage uniformity), so per the owner contract it is **surfaced for Jordan, not resolved here.**

**ED-876 Fix-A is independent of that fork and recommended regardless.**

---

## §4 — Stage-4 self-critique & limits

- **The deterministic+stochastic parameters (base 0.10 / slope 0.10 / cap 0.90) are PROPOSED illustrations, not tuned.** They demonstrate constant leverage and a safe ceiling; the actual values would need tuning against the desired faction win-rate curve and the Ob distribution (which itself depends on the F2-ruled `floor(stat/2)+1`). I am not proposing these as final.
- **σ-leverage is a *standard*, not a law of fun.** The armature A6 band (0.24–0.36) is itself a Claude-authored heuristic (flagged in the armature compliance doc as needing the across-range refinement this very analysis uses). "ED-874 is only fixable by deterministic+stochastic" is conditional on treating A6 uniformity as a requirement; Jordan may reasonably rate low-but-uniform or in-band-but-non-uniform as acceptable. The finding is "here is the trade-off," not "you must switch resolvers."
- **Fix-A is the robust result.** It rests on the verbatim Trigger-5 gate + the recovery-independent firing curve; it does not depend on any PROPOSED parameter or on the σ-leverage standard. `[CONFIDENCE: high]`.
- **Not modeled:** the officer-loss Trigger-5 path under Fix-A (unchanged — still fires); interaction of a deterministic faction resolver with Domain Echo (which feeds *stat* deltas — compatible, but unsimulated); multi-faction dynamics.

---

## §5 — Ledger impact (consolidated master)

- **ED-876:** add the Fix-A tested candidate (remove pool ≥ 6 from Condition C gate; keep in cost table) with the Stage-4 result (firing flattened, routs still 100% punished). Recommendation: apply. Remains P1 until applied.
- **ED-865/F1 + ED-874:** annotate with the Stage-4 fork — floor degeneracy fixable either way; σ-leverage uniformity fixable *only* by deterministic+stochastic (pure-pool-aggregation proven insufficient). This strengthens the deterministic+stochastic option in the engine-reconciliation §7 register on the σ-leverage dimension specifically.
- No new ED IDs required (these develop existing candidates). Not appended to the live ledger (JSONL migration owns it); recorded in `ledger_candidates_consolidated.json`.

`[CONFIDENCE: high]` — §1 (Fix-A) and §2b (σ-leverage irreducibility) are the load-bearing results, both grounded in computation + verbatim canon. `[CONFIDENCE: medium]` — the specific deterministic parameters and whether ED-874 uniformity is a hard requirement (Jordan's call).
