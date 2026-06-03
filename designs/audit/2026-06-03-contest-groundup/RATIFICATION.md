# Ground-Up Social Contest — Ratification (revised, corrected state)

**Date:** 2026-06-03 (revised) · **Authority:** Jordan directive. Supersedes the initial ratification, which predated the audit.

## What is ratified
1. **The ground-up structure** (unchanged): the primitives (stasis terrain + fallback ladder, the three modes of proof ethos/pathos/logos, standing, reserve, self-gating triage, leverage, the merits clock, the defeat-condition catalogue), the modes-of-discourse typology (deliberative/forensic/ceremonial/dyadic/appeal/negotiation), and the composite resolver (deterministic clinch OR merits accumulation around a small stochastic reception core). Validated top-down by the rhetoric corpus.
2. **The corrected wrapper-over-modules implementation**, after the all-directions audit:
   - the audit found a severe turn-order bias (symmetric contests 87/13); it is **fixed** — merits are judged at the exchange boundary, and **symmetry is now a unit invariant** (identical contestants ~50/50).
   - appeals are **functional** (logos→merits, ethos→standing, pathos→room), not inert.
   - the resolver is a thin wrapper composing the primitives; a shared `contract` module removes the former import cycle; opponent passed explicitly; dispatch/scoring split; boundary input validation.
   - 34/34 unit + invariant + integration tests pass.

## What is provisional (not ratified)
- **All numbers remain `[SEED]`** — the balance pass (threshold, reserve sizes, lever magnitudes, defeat-condition counts, reception-variance band) is still pending; the variance band is a Jordan feel call.
- Deeper deliberative/forensic differentiation (distinct win conditions/decision rules beyond opening ground).
- The four non-core modes (dyadic, appeal, negotiation, ceremonial) remain scaffolds.

## Provenance
No v30 inheritance. The only canonical reference is the shared resolution engine (verified `core.md` + σ-leverage armature), which is engine-level, not contest-specific.

## Validation status
Structure ratified; architecture corrected and unit-tested; audit complete with its P1 fixed and re-validated. **Stress test in progress** (this session). Balance pass and scaffold sub-systems remain.
