# VALORIA — FIELDWORK SYSTEM v1.1 — §12 Open Items and Editorial Flags
## Parent: designs/scene/fieldwork_v30.md
## Status: DESIGN — canonical subsystem file. PP-628/PP-630/PP-632 applied 2026-04-13.
## Mode applicability: ALL

## §12 OPEN ITEMS AND EDITORIAL FLAGS

### Open editorials (authorial — Jordan)

| ID | Description | Priority |
|----|-------------|----------|
| ED-507 | POI catalog per territory. Each territory needs 2–6 authored POIs across depth levels (Landmark, Resource, Secret, Remnant, Anomaly, Breach) with conditional availability gates. Cross-reference with geography_design.md and calamity_radiation.md required. | P2 |
| ED-508 | Named NPC starting Dispositions. Lifepath derivation formula (±0.5 increments, floor) is now canonical — ED-508 (pending Jordan) now covers only the specific starting values for the named NPC roster (Vaynard, Baralta, Cardinals, Torben, Elske, Klapp, Almud, Maret Uln, Edeyja) once Jordan provides lifepath profiles. ARC-T23 Remembrancer partially addresses RM context. | P2 |
| ED-509 | Godot POI node architecture (§10.1). Validation against Valoria-game Godot project structure. Deferred until Godot implementation phase. | P3 |

### Resolved editorials (PP-630/PP-631/PP-632)

| ID (was) | Resolution |
|----------|------------|
| ED-496 (ED-NEW-03) | Survey pool = Influence. Canonical. |
| ED-497 (ED-NEW-04) | Exposure→AP confirmed safe (PP-581, ~11% TC acceleration). |
| ED-498 (ED-NEW-05) | Negotiate boundary defined §5.7. GM determines, no player choice. |
| ED-499 (ED-NEW-07) | Evidence Track persistence: §4.1 explicit. No extra overhead. |
| ED-500 (ED-NEW-08) | Disposition decay rate: SIM-DEBT-FW-03 confirmed pacing. Decay now above +2 (PP-632). |
| ED-501 (ED-NEW-09) | Thread-Read co-movement: uses threadwork §3.2 directly. |
| ED-502 (ED-NEW-10) | Breach+Coherence stacking: intentionally proportional (PP-581). |
| ED-503 (ED-NEW-12) | Spirit not overloaded: unified metaphysical attribute. |
| ED-504 (ED-NEW-13) | Desperate Trail: 4D at TN 8 ≈ 60% viable. Confirmed. |
| ED-505 (ED-NEW-14) | Finding+Contest: +2D Recall, Evidence not consumed. |
| ED-506 (ED-NEW-15) | POP cap: subject to −1 cap (unlike Binding Ops). Note in params_threadwork. |
| ED-NEW-02 | Named NPC Dispositions: now derivable from lifepath formula. Outstanding: specific NPC profiles (→ ED-508). |
| ED-NEW-11 | Pool formula ×2: RESOLVED PP-615. |

### Simulation debt — all RESOLVED

| ID | Resolution |
|----|------------|
| SIM-DEBT-FW-01 | RESOLVED (PP-583). Ob calibration sound across Depth 1–5. |
| SIM-DEBT-FW-02 | RESOLVED (PP-576/PP-583). Evidence pacing confirmed. |
| SIM-DEBT-FW-03 | RESOLVED (PP-583). Disposition economy confirmed. |
| SIM-DEBT-FW-04 | RESOLVED (PP-581). AP feedback bounded. |
| SIM-DEBT-FW-05 | RESOLVED (PP-583). Survey vs Govern niches confirmed. |
| SIM-DEBT-FW-06 | RESOLVED (PP-583). Cover calibration confirmed. |
| SIM-DEBT-FW-07 | RESOLVED (PP-577). All 6 transition directions functional. |
| SIM-DEBT-FW-08 | RESOLVED (PP-578/PP-579). Threadwork×fieldwork confirmed. |
| SIM-DEBT-FW-09 | RESOLVED (PP-579). NPC arc Domain Echo cascades confirmed. |
| SIM-DEBT-FW-10 | RESOLVED (PP-580). Extended threadwork confirmed. |

### Disposition/Knot redesign — PP-632 (2026-04-13)

Major redesign applied to fieldwork_socializing.md:
- Disposition range: −3 to +5 → **−4 to floor(Bonds/2)+1**
- Ob rule: stepped table → **max(1, base Ob − Disposition)** direct subtraction
- Starting Disposition: faction table → **lifepath ±0.5 increments, floor**
- Knots: TS-gated Thread construct → **being-with (Mitsein), any character, Bonds-governed**
- Knot pool: (Bonds×2)+3. Tiers: Close 5 / Medium 2 / Loose 1. Max: floor(Bonds/2)+1
- Formation: max Disposition + Connect roll (Ob = tier). Breaking: rupture (Disposition →−4) vs loss (Coherence −1)
- Information gates updated for new Disposition range
- Decay threshold: above +3 → **above +2**

SIM-DEBT: Disposition/Knot system requires simulation pass (add to SIM-DEBT register).

| ID | Description |
|----|-------------|
| SIM-DEBT-SOC-01 | Calibrate new Ob = max(1, base − Disposition) across all social actions at representative pool sizes and Disposition values. Verify no action becomes trivially easy or impossible at range extremes. |
| SIM-DEBT-SOC-02 | Knot formation pacing: verify Close Knot formation timing across Bonds 1–7 and representative social pools. Confirm 3–5 season arc for Close Knot. |
| SIM-DEBT-SOC-03 | Knot breaking Composure damage: Close Knot rupture = 5 Composure damage. Verify this is severe but survivable (Composure = Charisma + 6; minimum 7). |

### Propagation status

| File | Change | Status |
|------|--------|--------|
| designs/scene/fieldwork_socializing.md | Disposition+Knot redesign | **DONE** (PP-632) |
| designs/ttrpg/threadwork_redesign_v25.md | Knot mechanics section added | **DONE** (PP-632) |
| references/params_threadwork.md | Knot pool/tier mechanics | **DONE** (PP-632) |
| references/params_core.md | Bonds attribute Knot governance note | **DONE** (PP-632) |
| references/canonical_sources.yaml | Fieldwork SHA updated | **DONE** (PP-632) |
