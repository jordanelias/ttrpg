# WORLDBUILDING v3 — CANON COMPLIANCE & SUPERSESSION AUDIT
## Date: 2026-04-03
## Method: Cross-referenced every v3 proposal against foundations, canon constraints (P-01–P-15), canonical timeline, stage6, stage13, stage7, BG v05, params_factions, editorial ledger.

---

## CANON VIOLATIONS FOUND

### NONE in v3.

All P-01 through P-15 constraints checked. No violations detected.

Specific checks performed:
- **P-08 (epistemological barrier):** §7.2 correctly states Altonian destruction is political, not source of Forgetting. Elder Kaldring (§8) at TS 22 cannot bridge the barrier. Community Weaving requires TS 30+ practitioner. **PASS.**
- **P-10 (epistemic seduction framing):** Klapp Awakening (§3.2, §3.3) does not use corruption language. Describes perceptual shift. **PASS.**
- **P-04 (monstrosity = ontological not moral):** No monster references in v3. **N/A.**
- **P-07 (Calamity = rendered-side):** No Calamity references in v3. **N/A.**
- **P-01 (inseparability):** No Thread operations proposed. Event cards do not introduce Thread ops without co-movement. **PASS.**

---

## INFORMATION THAT SUPERSEDES v3 CLAIMS

### 1. Vaynard First Name — CANONICAL TIMELINE GOVERNS

v3 flags ED-NEW-02 asking whether Vaynard's first name is Dienton (lore) or Magnus (design).

**The canonical timeline (03_canonical_timeline.md L95) says: "Duke Magnus Vaynard."** The canonical timeline is authoritative. "Magnus" is the canonical name. The lore's "Dienton" is from pre-project drafts and is superseded.

**Action:** Close ED-NEW-02. Magnus Vaynard is canonical. Lore epithet "The White Wolf" may be adopted if desired (editorial, not mechanical). Note: stage13 already has Vaynard but no epithet.

### 2. Baralta Spelling — CANONICAL TIMELINE GOVERNS

v3 flags ED-NEW-03 asking whether it's Inga (lore) or Inge (design).

**The canonical timeline (L94) says: "Duchess Inge Baralta."** Stage6 says "Inge." Stage13 says "Inge." All canonical documents use "Inge."

**Action:** Close ED-NEW-03. "Inge" is canonical. Lore's "Inga" is superseded.

### 3. Church Leader Title — CANONICAL DOCUMENTS ALREADY USE BOTH

v3 flags ED-NEW-04 asking whether the title is "Holy See" or "Confessor."

**Canonical timeline (L93) says: "Confessor Arne Himlensendt — Head of Church."** Stage6 §8.3 uses "Confessor." Stage13 uses "Confessor." The lore uses "Holy See" as the title of the office.

**Recommendation:** "Confessor" is the canonical personal title (how you address the person). "Holy See" is the office title (the seat, not the person). Both can coexist. The lore says "the Holy See who is elected from among the Bishopry" — the Holy See is the position, not the person. The Confessor occupies the Holy See.

**Action:** Can close ED-NEW-04 with: "Confessor = personal title. Holy See = institutional office. Both canonical. The Confessor IS the Holy See."

### 4. Stage13 Uses Stale Stat Name "Reach" — Pre-existing Issue

Stage13 references "Church Reach 7" (L108), "Reach 5" (L156), "Church Reach +1" (L162), "Crown Reach" (L251). Stage6, BG v05, and params_factions all use "Influence" — "Reach" does not appear in any of these.

**"Reach" is a stale stat name from an earlier version.** Stage13 was not updated when faction stats were renamed to the current six (Mandate/Influence/Wealth/Military/Intel/Stability). All instances of "Reach" in stage13 should be "Influence."

**Action:** Flag as pre-existing inconsistency. Not caused by v3. Add to file_index.md KNOWN STALE SYNC GAPS or raise as a cleanup item.

### 5. Baralta TC Suppression Threshold — Pre-existing Inconsistency

Stage6 §8.4: "While Baralta's Mandate remains **4+** (on 1–7 scale), she suppresses Theocracy Counter at −1/season."

Stage13 L154: "While Baralta's Mandate remains **above 5**, she suppresses Theocracy Counter at −1/season."

These are different values. Mandate 4+ means ≥4. "Above 5" means ≥6. This is a significant mechanical discrepancy.

**Action:** Flag as pre-existing inconsistency. Stage6 is canonical for TTRPG faction mechanics per canonical_sources.yaml. Stage6 value (Mandate 4+) governs. Stage13 needs correction to match.

### 6. Cardinal of Temperance Title — Discrepancy Between Lore and Stage13

Lore: "Cardinal of Temperance manages the universities and observatories."
Stage13 L114: "Cardinal Magnus Klapp — **Scholarship**"

v3 §3.1 maps Klapp to "Temperance (Knowledge)" but stage13 titles him "Scholarship." The lore cardinal title is "Temperance"; stage13 uses a functional label "Scholarship."

**Action:** v3 should use the lore title "Temperance" with stage13's functional description. "Cardinal of Temperance (Scholarship)" or just "Cardinal of Temperance" with scholarship noted as portfolio. Minor — not a mechanical issue.

### 7. Almaic Kyriakos — Appears NOWHERE in Canon

The Almaic Kyriakos (Altonian religious institution) appears only in the pre-project lore documents. It is not referenced in:
- Philosophical Foundations
- Canonical Timeline
- Stage6
- Stage13
- BG v05
- Any params file

v3 §3.6 proposes an IP 50 interaction with the Almaic Kyriakos. This is entirely new worldbuilding that has no canonical basis. It's lore material that was never adopted into the design.

**Action:** ED-NEW-07 correctly flags this as needing review. The proposal is valid worldbuilding but should be clearly marked as NEW CONTENT, not integration of existing canon. It introduces a new named institution into the game.

### 8. "Piety" Referenced in Stage13 — Undefined Mechanic

Stage13 L315: "Church military arm, commanded by Cardinal Jarnstal. Deployable without royal authorisation **when Piety is high.**"

"Piety" is not a defined faction stat or clock. It may be a stale reference to a cut mechanic, or an informal reference to Church Mandate.

**Action:** Flag as pre-existing ambiguity. Not caused by v3. "Piety" should probably read "Church Mandate" — confirm with user.

### 9. v3 Klapp Awakening Trigger — Matches BG v05

v3 §3.3 (Klapp Awakening card) states: "Thread operation within 1 territory of Himmelenger, TC ≥ 30, no Heresy Investigation opened this season."

BG v05 Scenario A (L495): "Thread operation within 1 territory of T3, Theocracy Counter ≥ 30, no Heresy Investigation opened this season."

The territory reference is T3 in BG v05 but v3 says "Himmelenger." T3 in the BG v05 territory map (stage7) is "Himmelstift" (which maps to T14 Himmelenger in PP-199). But T3 in the PP-199 map is Halvardshelm (Varfell).

**This is a territory numbering conflict between stage7 and PP-199.** BG v05 was written using stage7 territory numbers. PP-199 renumbered all territories. The Klapp trigger should reference the cathedral city (Himmelenger/Himmelstift) regardless of number, but the specific number needs reconciliation.

**Action:** This is part of ED-NEW-09 (territory name reconciliation). v3 should reference the territory by name ("Himmelenger / cathedral city territory") not by number, since numbers are in flux.

### 10. Stage13 Names Only 3 Cardinals — Fourth is Genuinely Missing

Stage13 has sections for:
- Cardinal Arnlod Olafsson — Justice
- Cardinal Magnus Klapp — Scholarship
- Cardinal Osten Jarnstal — Military

There is no Cardinal of Prudence in stage13. The lore establishes four cardinals. ED-007 (already in the ledger, status: resolved) addressed this: "Fourth cardinal identity is a narrative decision deferred to campaign development."

v3 correctly flags ED-NEW-06 for the Cardinal of Prudence name/profile. This is consistent with the ledger. However, ED-007's resolution says "resolved" but the actual fourth cardinal was never designed. The resolution was to defer it.

**Action:** ED-NEW-06 is the right vehicle. ED-007 should be re-examined — its "resolved" status is misleading since no fourth cardinal was actually created.

### 11. Jarnstal Drift — v3 Adds a Counter That Stage13 Implies But Doesn't Formalise

Stage13 L125-128 says Jarnstal's Belief is "The Knights Templar should be independent of all political authority" and "Jarnstal is drifting toward unilateral action."

v3 §3.2 formalises this as a 0–3 counter (Jarnstal Independence Counter). Stage13 implies the drift but doesn't track it. This is a genuine new mechanic. It's a reasonable formalisation of existing narrative direction.

**No supersession issue.** v3 is adding structure to what stage13 describes qualitatively. This is design work, not contradiction.

---

## SUMMARY

| Finding | Severity | Action |
|---------|----------|--------|
| Vaynard = "Magnus" (canonical) | Closes ED-NEW-02 | Remove from open editorials |
| Baralta = "Inge" (canonical) | Closes ED-NEW-03 | Remove from open editorials |
| Confessor + Holy See both valid | Closes ED-NEW-04 | Confessor = title, Holy See = office |
| Stage13 "Reach" = stale "Influence" | Pre-existing | Flag as sync gap |
| Baralta TC suppression: 4+ (stage6) vs >5 (stage13) | Pre-existing | Stage6 governs. Fix stage13. |
| Klapp = "Temperance" not just "Scholarship" | Minor | Use lore title in v3 |
| Almaic Kyriakos = new content, not canon | Informational | Mark as new worldbuilding in v3 |
| "Piety" in stage13 = undefined | Pre-existing | Likely means Church Mandate |
| Klapp trigger territory = name not number | Reconciliation needed | ED-NEW-09 covers this |
| ED-007 resolved but no 4th Cardinal exists | Misleading status | ED-NEW-06 is correct vehicle |
| Jarnstal Counter = new formalisation | No conflict | Consistent with stage13 narrative |
| No canon violations in v3 | — | — |
