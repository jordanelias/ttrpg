# Social Contest Engine — Ratification (final state, 2026-06-03)

**Status:** ratified for commit by Jordan. A MECHANICAL proposal (clean-room redesign), Jordan-vetoable —
not a canon change. It diverges from the canonical `social_contest_v30` (Composure + Conviction model);
see `TERMINOLOGY.md`. 62/62 tests pass.

## What it is
A ground-up redesign of the Social Contest as a general engine for two-party adjudicated discourse,
grounded bottom-up in the rhetoric/oratory research corpus and validated top-down against real
institutions and canon. Only canonical dependencies: the shared resolution engine (d10 success-count +
σ-leverage armature) and the NERS criteria.

## Architecture (wrapper-over-modules, acyclic DAG)
`contract` (types) · `engine` (shared stochastic core) · `primitives` (the substrate) · `resolver`
(Bout wrapper + top-down Venue spec) · `modes` (institution presets) · `policy` (decoupled policies) ·
`faction` (adapter: faction-layer discourse). **Venue-determined:** no privileged "merits" — primitives
accumulate per-side advancement; the venue supplies the win-condition and the defeat-catalogue.

## Capabilities
- **Substrate:** Stasis (the question at issue), three pisteis (ethos/pathos/logos), Standing, Reserve,
  Room, Readiness, Resonance (role↔character blend), SelfGating, σ-leverage (= canon's σ-leverage).
- **Evidence:** hidden-value dossier, relevance-gated, corroboration with diminishing returns, hard proof
  (readiness-independent).
- **Pressure on the adjudicator:** institutional tilt + public-raised susceptibility.
- **Persuasion jitter:** removes exact-tie artifacts.
- **Win-conditions:** ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, **PersuasionTrack** (canon's
  two-pole banded track: committee/decisive/total).
- **Adjudicators:** single or Panel (jury/bench/council).
- **Faction adapter:** per-voter motions with the committee outcome (§5.4/§10), Succession contests that
  fracture realms on the track (§7.2 unified/decisive/split with §7.2.1 ratios), §10 coalition pooling
  (multi-faction coalitions pooled onto the two-party engine).

## Verification
- 62 tests (`tests.py`), all green; suite covers engine, primitives, win-conditions, evidence, pressure,
  jitter, PersuasionTrack bands, and the faction adapter.
- Development record: `AUDIT`, `CODE_REVIEW`, `STRESS`, `STRESS_MODULATION`, `STRESS_MATRIX`,
  `MODULATION_DESIGN`, `AUDIT_MODULATION`, `HISTORICAL_VALIDATION`, `VENUE_VALIDATION`,
  `EVIDENCE_PRESSURE_VALIDATION`, `FACTION_NOTES`, `TERMINOLOGY`.
- Architecture review findings: #1 (dead state), #3 (evidence API), #5 (silent appeal), #7 (dead code),
  #8 (free-regroup) FIXED; #2 (spec/runtime split) DONE; #4 (two-party) RESOLVED — canon's contests are
  two-pole throughout, so the A/B spine is faithful; multi-faction coalitions pool onto it (demonstrated by
  `coalition_vote`), no N-party spine needed.

## Known boundaries / open items (honest)
- Non-adversarial motions (Subsidy, Treaty Ratification) not modelled — one-party persuasion vs the body.
- Succession downstream split (stat division by ratio, Stability floor 3, territory/treaty split,
  schismatic identity) not modelled — that is faction-layer state, not engine logic.
- `coalition_vote` uses a single BG-scale pooled roll (intended coarseness; per-voter `vote()` is the finer
  resolution).
- Specific canonical faction stats/dispositions not yet wired from canon.
- Test suite is unseeded and exits 0 even on failure (review finding #6, not addressed).
- `Leverage` is the bare-named σ-leverage (rename to `SigmaLeverage` deferred, logged in `TERMINOLOGY.md`).
- §7.2.1 split-ratio table implemented literally despite a mild counter-intuition; flagged, not altered.
