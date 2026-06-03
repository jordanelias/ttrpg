# Social Contest — modular build (ground-up, from the corpus)

Built from the rhetoric corpus and the shared resolution engine. No v30 reference — no Memory/Projection, no genre axis, no Evidence-clock, no inherited formulas or trackers. Structure is corpus-grounded; every number is a tunable `[SEED]` (history validates structure, not numbers). 36/36 tests pass.

## Layers (each file a layer; modules are separable and unit-tested)
- **engine.py** — the shared stochastic core (σ-leverage + base d10 engine), verified constants. Mode-agnostic; fixed, not tuned.
- **primitives.py** — one module per corpus primitive: Stasis (terrain + fallback ladder), Appeal (ethos/pathos/logos), Standing (spendable resource), Reserve (action economy), SelfGating (licit-tactics triage), Leverage (δσ into the engine), Merits (accumulation clock), DefeatConditions (the named-fault loss catalogue).
- **resolver.py** — the composite resolution: a deterministic wrapper (turn order, live stasis ground, merits clock, defeat-condition checklist, ledgers) around a small stochastic core (per-move reception). A contest ends by a **deterministic clinch** (a side incurs a defeat-condition) or by **merits** crossing threshold.
- **modes.py** — modes of discourse as distinct contests. The contested-debate core (deliberative + forensic flavors) is implemented; dyadic counsel, royal appeal, negotiation, and ceremonial are honest scaffolds (declared with their separate win conditions, not faked), because the corpus says they are different games.
- **policy.py** — decoupled policies (read-only view → Move); never touch internals.
- **tests.py** — unit tests per primitive + integration per mode.

## The two resolution paths (the diagnostic's composite, realized)
- **Clinch (deterministic):** the defeat-condition catalogue — barred device (an unlicensed hard tactic, gated by SelfGating), self-contradiction (an illegitimate ground-switch), evasion (repeated off-ground argument), silence (forced passes). Adjudicated against a checklist, no roll. Tests show each fires against the right side, deterministically.
- **Merits (accumulation):** where nothing clinches, on-ground successful reception accrues toward the threshold. The stochastic surface is only the per-move reception magnitude.

## What the tests demonstrate
- Each primitive behaves in isolation (engine math, stasis ladder, standing build/strip, reserve exhaustion/regroup, self-gating licence rule, leverage, merits, every defeat-condition).
- Honest play beats each faulty style: the overreacher always loses by a barred-device clinch; the staller always loses (usually on merits before the silence clinch); off-ground play loses. Clean-vs-clean never clinches (clean play incurs no fault) and resolves by merits.
- A legitimate fallback shift up the stasis ladder does not trip self-contradiction.

## Not done here (honest scope)
The four distinct sub-systems are scaffolds. Numbers are untuned `[SEED]`s — balance (threshold, reserve sizes, lever magnitudes, the reception variance band) is a separate sim-validation pass on this foundation, and how much reception variance to retain is a feel decision for Jordan.
