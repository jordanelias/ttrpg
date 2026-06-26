---
schema_version: 1
session_token: 1bd81c9e9bca010e
created_at: '2026-06-26T22:13:47.451836+00:00'
status: active
task_scope: 'combat-traditions: morphology critique -> integration spec -> NERS distillation
  (contact-axis regime pair clinch/disengage/choke)'
context_tokens_at_checkpoint: 83470
files_verified:
- designs/scene/combat_engine_v1/wrapper.py
- designs/scene/combat_engine_v1/systems.py
- designs/scene/combat_engine_v1/tradition.py
- designs/scene/combat_engine_v1/core.py
- designs/scene/combat_engine_v1/config.py
- designs/scene/combat_engine_v1/ability_armature.md
sim_ledger_present: false
commits_this_session: []
completed:
- Morphology critique of combat_analysis_rev2 abilities/traditions (outputs/combat_traditions_morphology_critique.md)
- Schema integration spec with state-graph insertion markers (outputs/combat_traditions_integration_spec.md)
- Adversarial NERS distillation + contact-axis fold (outputs/combat_traditions_ners_distillation.md)
- 'Correction: eff_cw channel-wiring landed 2026-06-13 (40b58b04) -> 8 abilities live,
  not 5; tradition.py docstring stale'
- 'Correction: original ''three missing efficacy axes'' overstated; engine already
  expresses most of D5/D7'
- Distilled ~11 levers -> 3 (clinch, disengage, choke); folded absorb/redirect/evade
  and targeting dials into existing machinery
pending:
- 'OPTIONAL: safe_commit the 3 deliverables under designs/audit/2026-06-25-combat-traditions-morphology/
  with Citations block (Jordan go)'
- Combat-engagement psychology research pass (intent disguise/reveal, overcommit,
  hesitation, MMA regime-imposition)
- Read combatant.py in full to confirm choke_clock field/reset surface before any
  patch
- 'Sims: invariant-safety pass + value calibration for clinch/disengage/choke before
  they land in-engine'
- Apply the four-axis vetting to the 7 TRADITIONS (chinese mode<->profile mismatch;
  filipino/chinese anchoring) — Jordan-led on flavour
decisions_made:
- Cut the granular force-relation family (redirect/evade/absorb) and targeting taxonomy
  (T1/T5/T7/T3 dials) — fail NERS-N/E
- Keep clinch+disengage+choke as the contact-axis regime pair + finish — the one genuinely-missing,
  felt, efficacy-core distinction
- Hold regime-imposition as biased WEIGHTS over existing engagement() machinery, NOT
  a regime-selection planner
- 'cripple (merged T2+T6) deferred like power-source: flag the gap, do not build on
  spec'
open_questions:
- 'Internal-power seam (Jordan canon-structure): inert flavour (a) / engine [M] channels
  (b) / actual Thread metaphysics (c)?'
- Targeting effect-type as scalar levers vs a single categorical 'target' lever (adds
  a 3rd op type) — design trade-off
- 'absorb cut: keep as a distinct active-mitigation mechanic if play shows it''s felt
  vs fold into Endurance — least-certain cut'
next_bootstrap_actions:
- bootstrap design + re-pin as_of; verify the engine SHAs are still HEAD
- 'if landing: safe_commit deliverables to the audit dir + co-file canonical_sources,
  with Citations (wrapper/systems/tradition/core/config + 5 morphology uploads)'
---

# Session Checkpoint — 2026-06-26 22:13 UTC

**Task scope:** combat-traditions: morphology critique -> integration spec -> NERS distillation (contact-axis regime pair clinch/disengage/choke)
**Session token:** `1bd81c9e9bca010e`
**Context at checkpoint:** ~83,470 tokens

## Narrative

Combat-traditions work arc (no canon committed; deliverables staged in outputs). Used the uploaded martial-morphology corpus to critique the combat_engine_v1 abilities/traditions layer, then proposed a schema integration, then ran an adversarial NERS pass that distilled it hard. All engine claims grounded first-hand at HEAD (wrapper/systems/tradition/core/config read with line numbers). Two self-corrections landed along the way: (1) the eff_cw channel-wiring pass shipped 2026-06-13 (40b58b04), so EIGHT abilities are live, not five — tradition.py's 'pending/inert' docstring is stale; (2) the original critique's 'three missing efficacy axes' OVERSTATED the gap — the engine already expresses most of force-relation (leverage, counter/steal, dodge) and targeting (poise-break, conc-drain, damage), so the genuine gap is narrow. Distillation outcome: cut ~11 proposed levers to a 3-lever CONTACT-AXIS PAIR — clinch (force the fight in) + disengage (refuse/slip the bind, the rapierist's missing escape) + choke (the clinch's incapacitation finish). Reframe: the primary contest is which REGIME the bout occupies (measure/contact/tempo bias-space); the engine already produces measure emergently and biases tempo, leaving only the contact axis's defensive pole missing. Hold the line: tendencies via biased weights, NOT a regime-selection planner. Next: a combat-engagement-psychology research pass (in progress), then an optional safe_commit landing the three deliverables under the audit dir.

## Completed this session

- Morphology critique of combat_analysis_rev2 abilities/traditions (outputs/combat_traditions_morphology_critique.md)
- Schema integration spec with state-graph insertion markers (outputs/combat_traditions_integration_spec.md)
- Adversarial NERS distillation + contact-axis fold (outputs/combat_traditions_ners_distillation.md)
- Correction: eff_cw channel-wiring landed 2026-06-13 (40b58b04) -> 8 abilities live, not 5; tradition.py docstring stale
- Correction: original 'three missing efficacy axes' overstated; engine already expresses most of D5/D7
- Distilled ~11 levers -> 3 (clinch, disengage, choke); folded absorb/redirect/evade and targeting dials into existing machinery

## Pending (in order)

1. OPTIONAL: safe_commit the 3 deliverables under designs/audit/2026-06-25-combat-traditions-morphology/ with Citations block (Jordan go)
2. Combat-engagement psychology research pass (intent disguise/reveal, overcommit, hesitation, MMA regime-imposition)
3. Read combatant.py in full to confirm choke_clock field/reset surface before any patch
4. Sims: invariant-safety pass + value calibration for clinch/disengage/choke before they land in-engine
5. Apply the four-axis vetting to the 7 TRADITIONS (chinese mode<->profile mismatch; filipino/chinese anchoring) — Jordan-led on flavour

## Decisions made

- Cut the granular force-relation family (redirect/evade/absorb) and targeting taxonomy (T1/T5/T7/T3 dials) — fail NERS-N/E
- Keep clinch+disengage+choke as the contact-axis regime pair + finish — the one genuinely-missing, felt, efficacy-core distinction
- Hold regime-imposition as biased WEIGHTS over existing engagement() machinery, NOT a regime-selection planner
- cripple (merged T2+T6) deferred like power-source: flag the gap, do not build on spec

## Open questions

- Internal-power seam (Jordan canon-structure): inert flavour (a) / engine [M] channels (b) / actual Thread metaphysics (c)?
- Targeting effect-type as scalar levers vs a single categorical 'target' lever (adds a 3rd op type) — design trade-off
- absorb cut: keep as a distinct active-mitigation mechanic if play shows it's felt vs fold into Endurance — least-certain cut

## Next bootstrap actions

*(When a new session bootstraps, these are the first steps to take.)*

1. bootstrap design + re-pin as_of; verify the engine SHAs are still HEAD
2. if landing: safe_commit deliverables to the audit dir + co-file canonical_sources, with Citations (wrapper/systems/tradition/core/config + 5 morphology uploads)

