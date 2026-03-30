session_close: 2026-03-29
checkpoint: 14
completed_stages:
  - terminology-refactor: threadweaving → threadwork (all active files)
next_action:
  skill: valoria-orchestrator
  input_file: session_log_current.md
  parameters: {}
open_gaps_added: []
editorial_decisions_pending: []
blockers: []
notes: >
  Renamed threadweaving → threadwork throughout. Weaving is a subtype of threadwork;
  naming the system after a subtype was incorrect. File renames: canon_reaudit/review
  _threadweaving_v24/v25 and designs/threadweaving_redesign_v25 all updated.
  threadweaved → threadworked in patch_proposals.


---

```yaml
session_close: 2026-03-29T_DEBATE_DESIGN
phase: design
subsystem: debate/social
completed:
  - "Debate system redesign v1: quaestio-based architecture, 6-move structure (3 genres × 2 orientations)"
  - "Philosophical grounding: genres = temporal axes (Past/Present/Future), orientations = intelligibility axis (Revealing/Obscuring)"
  - "Faction ethical modes mapped to genre susceptibility (Crown=virtue, Church=divine command, Hafenmark=Kantian, Varfell=consequentialist, Guilds=relativist, Restoration=Rawlsian)"
  - "Narrative example: Baralta vs Vaynard treaty dispute in Parliament"
  - "Stress test v1: 17 pre-test findings, 10 patches (D-01 through D-10), 7 retest findings (R-01 through R-07)"
  - "Stress test v2: 4 new patches (v2-P01 through v2-P04), Church Tribunal asymmetric scenario tested"
  - "System-breaking bug found and fixed: Divergence used raw successes not margin (v2-P04)"
  - "Obscuring redesigned as denial tool: Doubt Marker blocks opponent tracker movement (v2-P02)"
  - "Attunement read calibrated: failure = misleading signal, no History bonus (D-02)"
  - "Genre weights mechanical derivation from Question + Ethical Mode, fixed at setup (D-01)"
  - "Conviction Track: 0-10, thresholds 7/3, resistance = avg Stability - 1 (D-03 + v2-P01)"
  - "Terminology: threadweaving → threadwork (logged prior session, not yet applied)"
key_decisions:
  - "Genre names: Past / Present / Future (not Forensic/Epideictic/Deliberative)"
  - "Orientation names: Revealing / Obscuring"
  - "Quaestio structure rejected as too rigid — replaced with action-choice per exchange"
  - "Topic sets genre, not orator — genre shifting is a tactical move, not free choice"
  - "GM keeps Conviction Track hidden, reveals ledger after debate"
  - "Attunement read happens each exchange, not once pre-debate"
  - "Revolution faction does not exist — only Restoration"
  - "Hafenmark is a duchy (port, pass, mines) not a merchant faction"
patches_applied:
  - "D-01: Genre weight derivation"
  - "D-02: Attunement read calibration"
  - "D-03: Conviction Track specification (revised by R-07, v2-P01)"
  - "D-04A: Strain = margin + 1 + Presence mod (revised by R-06)"
  - "D-04B: Rattled = -2D + lose Focus defence"
  - "D-04C: Concentration -1 extra on loss"
  - "D-05: Clash/Competition/Divergence (revised by R-04, v2-P02, v2-P04)"
  - "D-06: Ties produce mutual strain + tracker lean"
  - "D-07: Focus passive floor(Focus/2)"
  - "D-08: Presence modifier floor((Presence-3)/2)"
  - "D-09: Memory +2D binary citation bonus"
  - "D-10: Composure = Poise + Bonds + 3"
  - "v2-P01: Resistance = avg Stability - 1"
  - "v2-P02: Obscuring = Doubt Marker"
  - "v2-P03: Asymmetric proceedings halved resistance"
  - "v2-P04: Divergence uses half successes"
editorial_pending:
  - "Corroboration in Church Tribunal (permitted or blocked?)"
  - "Niflhel social mode (no formal debate — what CAN they do?)"
  - "Genre pivot procedure (orator argues off-topic genre)"
  - "Grand Debate role alternation (who gets 3 propositions vs 2?)"
  - "Multiple Doubt Markers (second Obscuring win while one active)"
  - "Guilds moral relativism GM flex in weight-setting"
untested:
  - "Multi-party debates (3+ orators)"
  - "Thread operations during debate"
  - "Parliamentary proceeding type"
  - "Royal Audience proceeding type"
  - "Corroboration in practice"
  - "Regroup exploit with revised depletion"
  - "Rattled → Unmask decision point"
output_files:
  - "designs/debate_system_redesign_v1.md"
  - "designs/debate_example_v1.md"
  - "designs/debate_stress_test_v1.md"
  - "designs/debate_stress_test_v2.md"
next_action:
  - "Compile patched debate system into stage9_social.md replacement"
  - "Test multi-party debates and Parliamentary proceeding"
  - "Test Thread operation × debate interaction"
  - "Resolve 6 editorial decisions"
```
