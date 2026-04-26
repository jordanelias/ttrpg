<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: worldbuilding_canon_audit_v30_infill.md -->

<!-- v30 baseline — renamed from designs/worldbuilding/worldbuilding_v3_canon_audit.md on 2026-04-13 -->
# WORLDBUILDING v3 — CANON COMPLIANCE & SUPERSESSION AUDIT
## Date: 2026-04-03
## Method: Cross-referenced every v3 proposal against foundations, canon constraints (P-01–P-15), canonical timeline, stage6, stage13, stage7, BG v05, params_factions, editorial ledger.

---

## CANON VIOLATIONS FOUND

### NONE in v3.

All P-01 through P-15 constraints checked. No violations detected.

Specific checks performed:

---

## INFORMATION THAT SUPERSEDES v3 CLAIMS

### 1. Vaynard First Name — CANONICAL TIMELINE GOVERNS

v3 flags ED-NEW-02 asking whether Vaynard's first name is Dienton (lore) or Magnus (design).



### 2. Baralta Spelling — CANONICAL TIMELINE GOVERNS

v3 flags ED-NEW-03 asking whether it's Inga (lore) or Inge (design).


**Action:** Close ED-NEW-03. "Inge" is canonical. Lore's "Inga" is superseded.

### 3. Church Leader Title — CANONICAL DOCUMENTS ALREADY USE BOTH

v3 flags ED-NEW-04 asking whether the title is "Holy See" or "Confessor."




### 4. Stage13 Uses Stale Stat Name "Reach" — Pre-existing Issue


**"Reach" is a stale stat name from an earlier version.** Stage13 was not updated when faction stats were renamed to the current six (Mandate/Influence/Wealth/Military/Intel/Stability). All instances of "Reach" in stage13 should be "Influence."


### 5. Baralta CI Suppression Threshold — Pre-existing Inconsistency

Stage6 §8.4: "While Baralta's Mandate remains **4+** (on 1–7 scale), she suppresses Church Influence at −1/season."

Stage13 L154: "While Baralta's Mandate remains **above 5**, she suppresses Church Influence at −1/season."

These are different values. Mandate 4+ means ≥4. "Above 5" means ≥6. This is a significant mechanical discrepancy.

**Action:** Flag as pre-existing inconsistency. Stage6 is canonical for TTRPG faction mechanics per canonical_sources.yaml. Stage6 value (Mandate 4+) governs. Stage13 needs correction to match.

### 6. Cardinal of Temperance Title — Discrepancy Between Lore and Stage13

Lore: "Cardinal of Temperance manages the universities and observatories."
Stage13 L114: "Cardinal Magnus Klapp — **Scholarship**"



### 7. Almaic Kyriakos — Appears NOWHERE in Canon

- Philosophical Foundations
- Canonical Timeline
- Stage6
- Stage13
- BG v05
- Any params file



### 8. "Piety" Referenced in Stage13 — Undefined Mechanic


"Piety" is not a defined faction stat or clock. It may be a stale reference to a cut mechanic, or an informal reference to Church Mandate.

**Action:** Flag as pre-existing ambiguity. Not caused by v3. "Piety" should probably read "Church Mandate" — confirm with user.

### 9. v3 Klapp Awakening Trigger — Matches BG v05

v3 §3.3 (Klapp Awakening card) states: "Thread operation within 1 territory of Himmelenger, CI ≥ 30, no Heresy Investigation opened this season."


The territory reference is T3 in BG v05 but v3 says "Himmelenger." T3 in the BG v05 territory map (stage7) is "Himmelstift" (which maps to T14 Himmelenger in PP-199). But T3 in the PP-199 map is Halvardshelm (Varfell).

**This is a territory numbering conflict between stage7 and PP-199.** BG v05 was written using stage7 territory numbers. PP-199 renumbered all territories. The Klapp trigger should reference the cathedral city (Himmelenger/Himmelstift) regardless of number, but the specific number needs reconciliation.


### 10. Stage13 Names Only 3 Cardinals — Fourth is Genuinely Missing

Stage13 has sections for:
- Cardinal Arnlod Olafsson — Justice
- Cardinal Magnus Klapp — Scholarship
- Cardinal Osten Jarnstal — Military




### 11. Jarnstal Drift — v3 Adds a Counter That Stage13 Implies But Doesn't Formalise




---

## SUMMARY

| Finding | Severity | Action |
|---------|----------|--------|
| Vaynard = "Magnus" (canonical) | Closes ED-NEW-02 | Remove from open editorials |
| Baralta = "Inge" (canonical) | Closes ED-NEW-03 | Remove from open editorials |
| Confessor + Holy See both valid | Closes ED-NEW-04 | Confessor = title, Holy See = office |
| Stage13 "Reach" = stale "Influence" | Pre-existing | Flag as sync gap |
| Baralta CI suppression: 4+ (stage6) vs >5 (stage13) | Pre-existing | Stage6 governs. Fix stage13. |
| Klapp = "Temperance" not just "Scholarship" | Minor | Use lore title in v3 |
| Almaic Kyriakos = new content, not canon | Informational | Mark as new worldbuilding in v3 |
| "Piety" in stage13 = undefined | Pre-existing | Likely means Church Mandate |
| Klapp trigger territory = name not number | Reconciliation needed | ED-NEW-09 covers this |
| ED-007 resolved but no 4th Cardinal exists | Misleading status | ED-NEW-06 is correct vehicle |
| Jarnstal Counter = new formalisation | No conflict | Consistent with stage13 narrative |
| No canon violations in v3 | — | — |

[EDITORIAL: ED-740 — TC→CI + RS→MS abbreviation disambiguation per ED-782/ED-731. Mechanical abbreviation rename only; no semantic changes to worldbuilding/NPC content.]
