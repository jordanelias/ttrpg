# Social Contest — modular build (ground-up, corrected)

Built ground-up from the rhetoric corpus; corrected per the code-architecture review into a clean
**wrapper-over-modules** shape. No v30 reference. Numbers are tunable `[SEED]`s. **34/34 tests pass.**

## Layers
- **contract.py** — shared types (`Move`, `ContestView`, `FaultState`, `Adjudicator`, side identity `A/B`/`other`). Depends on nothing; breaks the former resolver↔policy import cycle.
- **engine.py** — the shared stochastic core (σ-leverage + base d10), verified, fixed.
- **primitives.py** — one module per primitive: Stasis (+ladder), Appeal, Standing/Reserve (stateful), Pool, SelfGating (triage), Leverage (static), Room (pathos's target), Merits (verdict clock), DefeatConditions (`check → (side, reason)`).
- **resolver.py** — the **wrapper** (`Bout`): owns state, composes modules, adds no mechanics beyond sequencing.
- **modes.py** — contested-debate core (deliberative/forensic flavors); the distinct sub-systems are honest scaffolds.
- **policy.py** — decoupled policies via the contract; no resolver internals.
- **tests.py** — per-module unit tests + wrapper invariants + integration.

## Corrections applied (from the review)
- **Appeals are now functional** (were inert): logos→merits, ethos→standing, pathos→room. Unit-tested ("appeals matter": pure-ethos cannot win the verdict).
- **Circular dependency removed** via `contract.py` (no lazy import).
- **Hidden `_opp_standing` side-channel removed** — the opponent is passed explicitly.
- **`_process` god-function split** into dispatch (`_apply`) / reception (`_reception`) / scoring (`_score`).
- **Turn-order bug fixed**: merits judged at the **exchange boundary** (both move, then judge); a clinch still ends immediately. Symmetry is now a **unit invariant** (identical contestants ~50/50), not just an integration hope.
- **Single fault-state** (`FaultState`); `check` returns `(side, reason)` in one pass (`_why` deleted). Side identity defined once in `contract`.
- **Leverage made static**; **Pool moved into primitives**; **adjudicator split out of `Config`**; **boundary validation** (bad move/ground raises `ValueError`); dead imports and a duplicated default removed.

## Resolution (the two paths)
A bout ends by a **deterministic clinch** (a side incurs a named defeat-condition — barred device, self-contradiction, evasion, silence; tested to fire against the right side) or by **merits accumulation** at the boundary. The stochastic surface is only the per-move reception.

## Remaining (honest scope)
- **Balance `[SEED]` pass** on the now-fair resolver (threshold, reserve sizes, lever magnitudes, defeat-condition counts, and the reception-variance band — the last a Jordan feel call).
- **Deeper deliberative/forensic differentiation** (distinct win conditions/decision rules beyond opening ground).
- The four scaffold sub-systems (dyadic, appeal, negotiation, ceremonial).
