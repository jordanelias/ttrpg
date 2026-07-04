# Adversarial refutation notes — finding `collision-engine-has-no-engine`

## Claim under test
Convergence Markers (self-named "emergent narrative engine") exist only as 8 hand-authored
trigger+payload annotations in `references/arcs/arc_register_events.md §VI`; no Key type,
module_contract, sim module, or resolver detects trigger-coincidence or applies the combined
payload. => flagship emergence mechanism is aspirational prose.

## Text verification (direct reads)
- `arc_register_events.md §VI` (L23-63): 8 markers (A,B,C,D,E,F,G,J), each "Trigger: … Combined: …".
  Bespoke COMBINED payloads that are NOT mere summation, e.g. COLLISION A adds "TC generation
  pauses"; §VI header L25 explicitly: "the combined pressure is not predictable from the constituent
  vectors without the marker." => an applier IS required; the extra pressure does not emerge from
  running vectors independently.
- `throughlines_complete.md` T-24 (L197-200): "These convergences are the game's emergent narrative
  engine." Body has **no Implementation status line** (every neighbor T-23,T-25,T-26… has one).
  Summary table L290: System Doc Coverage cell = bare "arc_register"; "Fully specified" refers to
  arc-register coverage of the DEFINITIONS, not a runtime detector.

## Refutation attempts (all fail)
1. `references/collision_registry.yaml` — NOT the convergence engine; it is
   `attribute_mechanic_collisions` (name-collision hygiene). Finder correctly called it unrelated.
2. "Emergent-by-construction, no applier needed" — refuted by §VI's own text: bespoke non-summative
   payloads. Refutation fails; text reinforces the finding.
3. "Rides a generic scripted-event/trigger engine (sibling of §V BG Conviction Events)" — checked
   all 27 modules in `module_contracts.yaml` (module: grep): NO arc_register / events / trigger /
   convergence module. `game_director`, `scenario_authoring`, `miraculous_event` exist but none is
   contracted to detect trigger-coincidence, and no contract references convergence (grep: only
   L231 name-collision, L442 numerical convergence). Refutation fails.
4. sim/ hits (`massbattle.py` L1206 physics collision; `restoration_movement.py` numerical
   convergence; sigma_leverage) — numerical/physical, not narrative. Finder's "numerical only" holds.

## Tracking check (not a duplicate)
- Ledger convergence hits: ED-479/ED-412 (arc-40 timeline COMPRESSION formula), ED-1085/ED-1093
  (numerical kernel/cross-tick convergence). None track a convergence-marker runtime detector.
- HANDOFF hits: all ID-collisions / RNG-MODEL-COLLISION / continuous-collision physics.
- Decision queue: only cross-tick numerical convergence. Not on charter calibration list.
=> genuinely NEW, untracked.

## Intent
No safeguard artifact: no ED, no "illustrative-only" tag, no design note scoping the markers as
deliberately-unimplemented. Doc framing is internally contradictory — calls them the "emergent
narrative engine" and says moments are "not designed — structural," yet they are 8 named
hand-authored bespoke entries. Plausible DELIBERATE reading (authored campaign highlights meant to
ride a future event engine) exists but is unsupported by any artifact and would still be
deliberate-WITHOUT-safeguard. => UNDETERMINED, but not safeguarded-deliberate => does not refute.

## Severity re-judge
P1 overstates. Base emergence has other channels — T-23 NPC Arc Emergence is "Fully implemented";
vectors/clocks/thresholds carry emergence independently. Convergence Markers are a CURATED dramatic
surface (8 marquee crises), not the whole emergence substrate; the doc's "the emergent narrative
engine" is rhetorical overclaim. Real defect: 8 authored qualitatively-different combined pressures
never render for lack of a detector+applier — materially narrows the designed emergent-crisis
surface and dramatic legibility, but does not zero out emergence. => revise P1 -> P2.

## Verdict
CONFIRMED (claim verified against text; no safeguard => deliberate-without-safeguard OR accidental).
Direction top-down; novelty NEW. Severity revised P2. Intent UNDETERMINED.
