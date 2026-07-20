# Ground-Up Social Contest — Audit (all directions) + Stress Test

`[SELF-AUTHORED — bias risk]` Auditing my own just-committed system; treated as external, attacked rather than confirmed. The stress test found a severe defect the structure alone hid.

## VERDICT: NON-COMPLIANT — a turn-order bias makes symmetric contests 87/13.
Fails **R**. The structure is sound and the deterministic clinch path works; the defect is in the resolution loop and is a structural fix, not a number tweak. Consistent with the ratification (structure ratified, resolution detail provisional), but it must be fixed.

## P1 — Turn-order bias (severe, R)
Identical contestants (faculty 4 v 4, standing 5 v 5, honest v honest) split **A 0.87 / B 0.13** — not the ~50/50 fairness demands. Root cause: the merits threshold is checked **mid-exchange**, so the first mover (always A) reaches it first, and the clock is shallow enough that a half-turn head start decides. Stress evidence:
- Resolution depth: 1 exchange → all draws; **2 exchanges → already resolved** (0.02 draw). The clock averages over ~2 receptions — a near-disguised-binary (Lesson 4).
- Threshold sweep (budget 6): T≤8 resolves ~always; T=10 → 0.44 draw; T=14 → all draw. Depth trades directly into draws (the Pareto tension), so deepening alone is not the fix.
- Stage-4 re-test: **alternate first mover → 0.15/0.85** (bias merely flips — confirms turn order, not skill, decides); **merits checked at exchange boundary → 0.42/0.42, 0.16 draw** (symmetry restored); boundary + deeper clock T=8 → 0.40/0.39, 0.20 draw. The fix is **boundary resolution**, validated, introducing no new asymmetry.

## N R S E (all directions)
- **N — pass.** Each primitive maps to a corpus invariant; none redundant. Minor watch: standing builds on merit-success (a coupling); the stress shows it is *not* load-bearing for snowball (below), so it could be decoupled without loss — candidate for Lesson-1 simplification, not a failure.
- **R — fail.** The turn-order bias (P1). Secondary: the floor pool (faculty 1 → 5D, the bottom of healthy) is noisier — but the bias *shrinks* there (0.57/0.38) because slower resolution gives both sides more attempts, which is the same depth lever. Holds elsewhere once P1 is fixed.
- **S — pass (core) / unvalidated (cross-mode).** Components are categorized correctly (dice reception + deterministic conditions + clock + continuous resources); the deterministic-wrapper/stochastic-core composite is smooth. But only the contested core is built — the dyadic, appeal, negotiation, ceremonial sub-systems are scaffolds, so cross-mode transitions are untested. Incomplete, not wrong.
- **E — pass, with a watch.** Outcomes are intuitable: named defeat-conditions, a visible merits clock, hidden σ-roll surfaced as advantage levels. Watch over-apparatus (two resources + stasis + appeals + self-gating + two resolution paths) if the modes don't end up justifying the depth.

## Secondary findings (confirmed by stress)
- **Defeat-condition path is sound.** Overreacher loses 100% by barred-device clinch; off-ground 0.99; staller loses (15% silence-clinch, 85% on merits); honest-vs-honest never clinches. The deterministic clinch does the load-bearing work the diagnostic wanted, no roll.
- **Standing loop is bounded, not a snowball.** A standing lead of 9 v 5 barely moves the result (0.86 vs the 0.87 baseline) — the Phase-4 positive loop is damped+capped as intended; not a defect.
- **Skill is currently dominated by turn order.** faculty 6 v 2 → 0.96 but 4 v 4 → 0.86: a 4-point faculty gap adds only ~10pp over the turn-order baseline. Once P1 is fixed this should read cleanly.

## Remediation (worst-first; lesson-mapped)
1. **P1 turn-order → resolve the merits threshold at the exchange boundary** (both sides move, then test), not mid-exchange. Structural, validated (→ symmetric). Lesson 4 + a fairness fix the skill's lessons don't name explicitly (flag: a *turn-order/simultaneity* lesson, surfaced rather than forced into an existing one).
2. **Clock depth → balance pass.** With boundary resolution, set T and the reception-variance band for "deep enough to average, shallow enough to decide" — the residual draw rate (~0.16 at T=4) is the knob. A genuine balance question on a now-fair resolver; the variance band is Jordan's feel call.
3. **Defeat-condition counts (evasion/silence = 2)** are sharp `[SEED]`s — set in the same balance pass; mechanism is sound.
4. **(Optional, Lesson 1)** decouple standing-build from merit-success if it proves non-load-bearing — simplifies without loss.

## Stage-4 re-test summary
The P1 fix (boundary resolution) was re-run through the resolution loop: restores ~50/50 on symmetric contests, leaves the defeat-condition clinches intact (fault-based, checked immediately), and introduces a tunable draw rate rather than a new bias. Clean. The remaining tension (draws vs decisiveness) is balance, not structure.
