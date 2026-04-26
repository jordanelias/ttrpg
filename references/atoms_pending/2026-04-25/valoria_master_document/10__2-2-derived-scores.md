---
atom_id: valoria_master_document__10__2-2-derived-scores
source_file: valoria_master_document.md
source_section: "2.2 Derived Scores"
section_index: 10
total_sections: 125
line_count: 38
char_count: 2731
source_sha256: 8f501f471217ba59
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 2.2 Derived Scores

| Score | Formula | Range | Notes |
|-------|---------|-------|-------|
| Vitality | End × 10 | 10–70 | +flat from equipment. ED-694 canonical. |
| Stamina | End × 5 | 5–35 | Variable action costs (standard 5, heavy 8, defensive 3). Armour adds drain. |
| Wound Interval | End + 6 | 7–13 | Wounds = floor(cumulative_damage / interval). On-the-fly computation. |
| Composure | Cha × 3 | 3–21 | Social damage buffer. Equipment adds flat. |
| Combat Pool | (Agi × 2) + H + 3 | derived min 5 | Same pattern as all pools. Agi 1 = 5D (derived, not a separate floor). |
| Thread Fatigue | Spi × 5 | 5–35 | Counts up from 0. Variable op costs (Pulling 5, Locking 7, Dissolution 10). |
| Certainty | 0–5 (assigned) | bidirectional | Cosmological worldview track. |
| Coherence | 10→0 (countdown) | practitioner | Ontological rendering frame. At 0: NPC transition. |
| Resolve | = Spirit | 1–7 | Max Inspiration value. |

All linear. No compounding formulas. Implementation trivial.

⚠ **STALE-01: CSR §3 Composure.** complete_systems_reference.md says `Cha + 6`. Canonical is `Cha × 3` (ED-694). At Cha 7: old = 13, new = 21. Significant divergence at high Charisma.

⚠ **STALE-02: PP-275 Stamina.** States `End + H + 1 − armour mod`. ED-694 canonical: `End × 5`. These produce very different values (End 4: PP-275 ≈ 8; ED-694 = 20). PP-275 must be struck. This also affects Take a Breath restore formula (PP-275 says "Endurance score"; ED-694 says "(End + History) × 2" — which History is unspecified).

### 2.2a Certainty Track Details

6 values. Movement: 6 triggers toward 0 (Thread acceptance), 3 toward 5 (reinforcement). Effects: Cert 5 (+1D orthodox, nullify first Coherence loss/session); Cert 2–1 (−1D orthodox, +1 Coherence recovery); Cert 0 (−2D orthodox, +1D Thread communities, +2 Coherence recovery, +1 TS growth/major encounter, arch-heretic).

**N** ✓ Central thematic axis. **R** ✓ Both poles reward commitment. **E** ✓ Extremes have effects; middle is transitional. **S** ⚠ **DECISION-03:** Asymmetric triggers bias toward 0. Confirm this is intentional narrative arc (progressive discovery of Thread reality).

Cert 0 has 5 simultaneous effects — highest effect-density on any single track value. Manageable but note for UI: display as a consolidated status panel.

### 2.2b Coherence Details

Countdown 10→0. War-scale: 7-turn battle = −7. Recovery: +1/season non-practice + +1 Knot Anchoring. Max +2/season = 3.5 seasons full recovery from Coherence 3. Independent of TS and Certainty — three orthogonal practitioner axes.

**N** ✓ **R** ✓ **E** ✓ **S** ✓ Certainty 0 giving +2/long rest rewards Thread acceptance with faster Coherence recovery. Thematically correct.

---

# 3. PERSONAL COMBAT
