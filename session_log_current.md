# Valoria Session Log — Current

```yaml
session_id: 2026-04-03T_SYSTEM_REVIEW_AND_PATCHES
phase: PROPAGATION COMPLETE
status: AWAITING EDITORIAL DECISIONS

## SESSION SUMMARY
System overview produced from full params read. Docx review applied (PP-232).
Mass combat unit formula designed and committed (PP-233). All propagated.

## COMMITS THIS SESSION
- 22ee783: PP-232 docx review batch (params_core/combat/debate/threadwork/mass_combat + ED-127–135)
- 6db033d: PP-233 mass combat unit formula (pool/health/damage/size recalc)
- [this commit]: PP-232/233 propagation (glossary, scale_transitions, propagation_map, coverage_matrix, session_log)

## PATCHES APPLIED
- PP-232: ~30 mechanical corrections from docx review across all subsystems
- PP-233: Mass combat unit formula (Pool = min(Size,Command)+Command; H = min(Discipline,Command)+DR; etc.)

## EDITORIAL FLAGS RAISED (9 open, require user decision)
- ED-127: Composure track redesign (mirror Health/Wound structure)
- ED-128: Certainty stat decoupled from Spirit — design pending
- ED-129: Close/Far zone terminology → plain-language distance descriptors
- ED-130: Stage 1/Stage 2 incapacitation states — undefined
- ED-131: Damage modifier vs armour tier table — requires playtesting
- ED-132: Debate Step 1 action name (not "Read" — Appraise? Judge?)
- ED-133: Diverge state trigger — design rationale required
- ED-134: Diagnosis mandatory pre-op action — rationale disputed
- ED-135: "Forced Resolution" term — replacement needed
- ED-136: CP acronym collision (Character Points vs Combat Power/now Power)

## SIM-DEBT
- SIM-DEBT-01: Debate Mode C re-sim needed (pool formula changed PP-232)
- SIM-DEBT-02: Debate CLASH corroboration calibration pending
- SIM-DEBT-03: Mass combat DR-in-Health × Power-vs-armour interaction not yet simulated

## BLOCKERS (pre-existing, unchanged)
- ED-001: Card-Hand BG system
- ED-036: Altonian unit stats provisional
- ED-048: Ceiral name

next_session_start:
  priority_1: "Resolve editorial flags ED-127 through ED-136 (user decisions required)"
  priority_2: "Run SIM-DEBT-01 Debate Mode C re-sim with corrected pool (Cognition×2+History)"
  priority_3: "Run SIM-DEBT-03 mass combat calibration (DR/Health/Power interaction)"
  priority_4: "Update designs/mass_combat/mass_battle_v3.md to reflect PP-232/233 unit formula"
```
