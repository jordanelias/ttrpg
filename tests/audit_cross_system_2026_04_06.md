# Cross-System Audit: Calamity Radiation × Threadwork × Canon × Hybrid × Board Game

## Scope
Five systems reviewed collectively and independently for internal consistency, cross-system alignment, and canon compliance. Documents examined:

| System | Canonical Source |
|--------|----------------|
| Calamity Radiation | `designs/setting/calamity_radiation.md` |
| Threadwork | `designs/ttrpg/threadwork_redesign_v25.md` |
| Canon | `canon/00_philosophical_foundations.md` + `canon/02_canon_constraints.md` |
| Board Game | `designs/board_game/valoria_bg_v05_simulation_and_patches.md` + `designs/board_game/victory_architecture_v1.md` |
| Hybrid / State Transfer | `skills/valoria-orchestrator/references/state_transfer_spec.md` + threadwork_v25 §7.2 |

Also cross-referenced: `references/params_board_game.md`, `designs/setting/geography_design.md`.

---

## A. FINDINGS — CROSS-SYSTEM CONFLICTS

### A-01. RS Threshold Bands: Calamity Radiation vs Threadwork vs params_board_game (CONFLICT — P1)

Three documents define RS threshold bands. They disagree.

| RS Range | Calamity Radiation | Threadwork §5.3 | params_board_game |
|----------|-------------------|-----------------|-------------------|
| 100–80 | Stable | Stable | — |
| 79–60 | Strained | Strained | 72–50: "No modifier" |
| 59–40 | Fragile | Fragile | 49–30: Thread −1 Ob, non-Thread +1 Ob in T12/T13 |
| 39–20 | Fractured | Fractured | 29–20: Entity encounters T12/T13, Muster +1 Ob |
| 19–1 | Critical | Critical | Below 20: +1 Ob all, entity encounters uncontrolled |

**Conflicts:**
1. params_board_game uses entirely different RS band boundaries (72–50, 49–30, 29–20, below 20) than both threadwork and calamity_radiation (100–80, 79–60, 59–40, 39–20, 19–1). These are not compatible abstractions — they define different mechanical break points.
2. params_board_game has no "Stable" or "Strained" band distinction; everything above 50 is "no modifier." Calamity Radiation has effects active at Askeheim even in the 100–60 band.
3. params_board_game says Thread operations get "−1 Ob" below RS 49 (making Thread ops easier when the world is unstable). Threadwork §5.3 says Thread operations get "+1 Ob" at Critical band. These point in opposite directions. The params_board_game value appears to be a legacy from the old Thread Tension system (where high tension = more Thread power), which should have been inverted when Thread Tension was replaced by Rendering Stability.
4. params_board_game references "T12/T13" as the affected territories at intermediate RS bands. Calamity Radiation uses node-distance graduation from T15 (Askeheim). These are different systems — params_board_game applies effects to specific named territories, while calamity_radiation computes effects dynamically from proximity ratings. The params_board_game references appear stale (pre-calamity_radiation.md).

**Required action:** params_board_game RS Effects section (L169–193) must be rewritten to align with calamity_radiation.md's Simplified BG Lookup Table. The current params_board_game RS Effects section is mechanically incompatible with the canonical Calamity Radiation framework.

---

### A-02. Southernmost Zones vs Proximity Ratings (CONFLICT — P1)

Two geographic overlay systems exist for the same territory set:

1. **params_board_game "Southernmost Zones"** (L808–820): Defines zones 1–3 + Epicentre with RS effects per zone (e.g., Zone 2: "RS thresholds +10 early", Zone 1: "RS −1/season any occupation").
2. **calamity_radiation.md "Node Distance Map"**: Defines proximity 0–5 from Askeheim with a full RS-band × proximity matrix.

These are redundant and conflicting systems describing the same thing — geographic RS effects. The Southernmost Zones system in params_board_game was the predecessor; calamity_radiation.md superseded it. But params_board_game still contains the old system without marking it as superseded.

**Required action:** params_board_game Southernmost Zones section must be replaced with a pointer to calamity_radiation.md, or updated to reflect the Proximity Rating system.

---

### A-03. Victory Architecture vs params_board_game Victory Conditions (STALE — P1)

victory_architecture_v1.md (canonical per canonical_sources.yaml) defines an entirely different victory system from params_board_game §Victory Conditions (L193–266):

| Dimension | victory_architecture_v1 | params_board_game |
|-----------|------------------------|-------------------|
| Structure | TCV thresholds + political conditions, 2 Accounting hold | Deed-count system (3–5 Deeds per faction) |
| Crown primary | TCV ≥ 18 + suppress all rivals + IP < 60 + PI ≥ 3 | 5 Deeds + PI ≥ 3 gate |
| Church primary | TCV ≥ 10 + CV ≥ 3 all held (post-TC 75) | 4 Deeds + AER ≥ 3 + TC ≥ 65 |
| Hafenmark primary | TCV ≥ 12 + Mandate ≥ 4 + PI ≥ 5 + Crown Mandate ≤ 3 | 3 paths (Reformed Valoria / Theological Supremacy / Parliamentary) |
| Löwenritter | Conditions-based (TCV ≥ 10 + political gates) | 5 Deeds |
| Hollow Victory | Dissolved | Active (modifier table present) |
| Deed Tokens | Dissolved (PP-427) | Active throughout |

params_board_game still contains the full Deed-based system, Hollow Victory modifiers, territory references using old numbering (T12 = Valorsplatz vs T1 in current geography), and Crown victory conditions that were explicitly superseded. This is the propagation work identified as Priority 1 in the session log.

**Required action:** params_board_game §Victory Conditions, §Hollow Victory, and §Co-Victory Pairings must be rewritten to match victory_architecture_v1.md. All Deed Token references removed. Territory numbering corrected throughout.

---

### A-04. TC Generation: victory_architecture vs params_board_game (CONFLICT — P2)

victory_architecture_v1.md §7 defines a 5-step TC generation sequence (Institutional Momentum → Conviction Yield → Assert → Suppress → Hafenmark Structural Suppression) with TC starting at 28 and phase transition at 75.

params_board_game references TC starting at 28 (corrected by PP-189) and primary victory at TC ≥ 65 (P-32). The phase transition at TC 75 and the new TC generation formula (including Conviction Yield based on per-territory CV values) are not reflected in params_board_game.

**Required action:** params_board_game TC generation section must be updated to match victory_architecture §7.

---

### A-05. state_transfer_spec.md: CV — ALREADY PRESENT (FALSE FINDING)

On closer inspection, state_transfer_spec.md already contains CV in both the Variables that TRANSFER table ("Territory CV (0–5) → Scene context, read-only, changes queue as Domain Echo ±1 max per Zoom In") and the Zoom Out table ("Faith-affecting personal scene → CV ±1 in that territory, queued to Accounting"). No action needed.

---

### A-06. state_transfer_spec.md: Victory Check at Accounting — ALREADY PRESENT (FALSE FINDING)

On closer inspection, state_transfer_spec.md already contains the rewrite (PP-420): "Victory condition checks for ALL factions fire at Accounting Step 12 regardless of active Zoom In." No action needed.

---

### A-07. Threadwork §5.3 Geographic Graduation Cross-Reference (PROPAGATION PENDING — P2)

threadwork_v25 §5.3 includes the note: "The threshold effects below are not global. They radiate outward from Askeheim (T15) by node distance." This note references calamity_radiation.md correctly. However, calamity_radiation.md's Integration Notes flag two additional PROPAGATION PENDING items:
1. threadwork_v25 §5.3 RS threshold table should note "geographic graduation per calamity_radiation.md"
2. threadwork_v25 Part 6 should cross-reference the Gap-severity classification.

Checking threadwork_v25: §5.3 already contains the geographic graduation note (ED-302 callout box). Part 6 §6.1 already contains the Gap-severity classification cross-reference. **These propagation items appear to have been completed but calamity_radiation.md's Integration Notes were not updated to mark them done.**

**Required action:** calamity_radiation.md Integration Notes should be updated to mark threadwork cross-references as DONE.

---

### A-08. Calamity Radiation BG Lookup Table vs Threadwork §5.4 (INCONSISTENCY — P2)

threadwork_v25 §5.4 states: "Rendering Stability replaces Thread Tension on the board game track. Invert all Thread Tension references." It then says "Rendering Stability is hidden from players by default."

calamity_radiation.md provides a "Simplified BG Lookup Table" that the facilitator performs "one lookup per territory per season." This is compatible with threadwork §5.4's hidden RS principle — the facilitator sees the number, players see the effects.

However, the calamity_radiation BG Lookup Table uses different RS band boundaries (100–60, 59–40, 39–20, 19–1) than the params_board_game RS Effects table (72–50, 49–30, 29–20, below 20). This is the same conflict as A-01 manifesting in the BG-specific lookup.

No separate action needed — resolved by A-01.

---

### A-09. Warden Cooperation Track: Two Definitions (CONFLICT — P2)

victory_architecture §6 defines Warden Cooperation (WC) as a 0–3 track with effects:
- WC ≥ 1: +1D all Thread ops peninsula-wide
- WC ≥ 2: RS decay rate halved
- WC ≥ 3: RS +2/season at Accounting

params_board_game Accounting Step 10 says "Warden Cooperation check" but does not define the track's values, effects, or range. The WC track's effects have direct implications for the Calamity Radiation framework (RS decay rate halved at WC ≥ 2 interacts with the radiation matrix's RS-band effects).

**Required action:** params_board_game must include the WC track definition from victory_architecture §6, or point to it.

---

## B. FINDINGS — INTERNAL SYSTEM ISSUES

### B-01. Calamity Radiation: RS Band 100–60 Conflates Two Threadwork Bands (MINOR — P3)

Calamity Radiation uses RS 100–60 as a single band ("Stable / Strained"). Threadwork §5.3 separates these into RS 100–80 (Stable — no phenomena) and RS 79–60 (Strained — occasional wrongness). The Calamity Radiation matrix assigns effects to Proximity 0 even in the 100–60 band (Mending Gaps, micro-Gap emergent beings, +1 Ob non-Thread, Forgetting active). These effects align with threadwork's "Strained" effects, not "Stable."

This is not necessarily wrong — Askeheim is the wound itself, so effects there at even high RS are defensible. But the RS 100–60 label is misleading because the "Stable" half (100–80) should have no effects even at Proximity 0 per threadwork §5.3's "Stable" definition.

**Question for editorial:** Should Askeheim have effects even at RS 100–80 (Stable), or should the Calamity Radiation matrix split this band into two rows matching threadwork?

---

### B-02. Calamity Radiation: Threadcut Being TS Ranges vs Threadwork §6 (CONSISTENT — No Action)

Calamity Radiation defines: Micro-Gap (TS 20–40), Standard Gap (TS 50–70), Catastrophic Gap (TS 80+). Threadwork §6 cross-references this classification and uses the same TS ranges. No conflict.

---

### B-03. Calamity Radiation: "Forgetting active" at Proximity 0 (UNGROUNDED — P3)

The Calamity Radiation matrix states "Forgetting active" at Askeheim in the RS 100–60 band. The Forgetting is defined in Foundations §10.2 (P-13) as a rendering failure: Southernmost knowledge is mechanically untransmittable to non-sensitives. This is a permanent metaphysical condition of the Southernmost, not an RS-dependent effect.

If Forgetting is permanent at Askeheim regardless of RS, it shouldn't appear in the RS-dependent radiation matrix — it should be listed as a permanent Askeheim property. If it IS RS-dependent (weakening at high RS, strengthening at low RS), that would contradict P-13's framing of the epistemological barrier as metaphysical rather than circumstantial.

**Question for editorial:** Is the Forgetting at Askeheim RS-dependent or permanent? If permanent, remove from the radiation matrix and document as a permanent T15 property.

---

### B-04. Board Game: Thread Ob Inversion Error in params_board_game (CONFIRMED BUG — P1)

params_board_game L172: "RS 49–30: Thread operations: −1 Ob."

This says Thread operations become easier as the world destabilises. Threadwork §5.3 says the opposite: at Critical (19–1), "All Thread operations +1 Ob worldwide (the substrate resists manipulation)." The params_board_game value is a holdover from the Thread Tension system where rising tension made Thread work easier. When Thread Tension was replaced by Rendering Stability (inverted), this modifier should have been inverted too.

**Required action:** params_board_game RS Effects table must invert the Thread Ob modifier: at lower RS bands, Thread operations should have +1 Ob, not −1 Ob. This is captured in A-01 but flagged separately because it's a directional error, not just a band-boundary disagreement.

---

### B-05. Victory Architecture: Varfell Path B References "Warden's Accord (WA)" — Undefined in BG (GAP — P2)

Victory architecture §3.4 Path B requires WA ≥ +1 and "Blocked if RM has emerged (WA ≤ −2)." §8 defines WA as a −3 to +3 track starting at 0, used for RM emergence conditions.

WA is not defined in params_board_game. The track, its movement rules, and its interaction with RM emergence are only in victory_architecture. Since victory_architecture is canonical, this is technically correct — but params_board_game should at minimum contain a pointer.

**Required action:** params_board_game should include WA track reference.

---

### B-06. Victory Architecture: Conviction Track (CV) Starting Values — Not in params_board_game (GAP — P1)

CV starting values per territory (T15 = 0 hard-fixed, T9 = 5, Hafenmark territories = 3, Varfell = 2, Crown = varies) are defined only in victory_architecture §2. params_board_game contains no CV track definition. CV is a core game state variable that affects Church seizure Ob, Calamity Drift, and victory conditions.

**Required action:** params_board_game must include CV starting values, movement rules, and Calamity Drift thresholds.

---

### B-07. Canon Compliance: Calamity Radiation Framework (PASS with 1 FLAG)

Tested against all 15 canon constraints (P-01 through P-15):

| Constraint | Result | Notes |
|-----------|--------|-------|
| P-01 (Inseparability) | PASS | Radiation effects reference Thread operations and Co-Movement; the framework doesn't define new operations that would need co-movement checks. |
| P-02 (Ein Sof = positive being) | PASS | "The wound tears wider" — framed as structural failure, not malevolent agency. |
| P-03 (Rendering = consciousness) | **FLAG** | "Forgetting active" at Proximity 0 — see B-03. If this implies the Forgetting is RS-dependent, it could conflict with P-03/P-13's framing of rendering as a consciousness process not a world-state effect. |
| P-04 (Monstrosity = ontological) | PASS | Threadcut beings described as unique entities without moral framing. |
| P-05 (Three emergence modes) | PASS | Gap-severity classification aligns with Mode 3 (threadcut = continuous self-maintenance). |
| P-06 (Threadcut = is without becoming) | PASS | Classification table notes threadcut beings maintain themselves through continuous Thread work. |
| P-07 (Calamity = rendered-side) | PASS | "Structural failure in the substrate" — no ground agency. |
| P-08 (Epistemological barrier) | PASS | No mechanism bypasses the barrier through study. |
| P-13 (Forgetting) | **FLAG** | Same as P-03 flag — Forgetting in the RS-dependent matrix could imply it varies with world state. |
| P-14 (BG inseparability) | PASS | BG Lookup Table triggers Co-Movement effects for Thread operations. |

---

### B-08. Canon Compliance: Victory Architecture (PASS)

| Constraint | Result | Notes |
|-----------|--------|-------|
| P-01 | PASS | Community Weaving explicitly fires Co-Movement card draw. |
| P-07 | PASS | RS framed as substrate stability, not ground agency. |
| P-14 | PASS | BG Thread operations produce co-movement via card deck. |
| P-15 | n/a | Coherence not directly addressed (correct — BG doesn't track it). |

No canon violations. CV = 0 at Askeheim justified via P-03 + Foundations §8. Church seizure Ob includes CV modifier, maintaining inseparability of ideological and military dimensions.

---

### B-09. Hybrid Mode: Coherence Declaration vs Calamity Radiation (NO CONFLICT — P3 NOTE)

threadwork_v25 §7.2 defines Hybrid Coherence rules (PP-198, PP-200, PP-207). Calamity Radiation defines geographic RS effects. These systems interact at the Cascade Phase:
- A PC leading Thread operations in a Proximity 0–1 territory faces both Coherence cost and +Ob from calamity radiation effects.
- This double cost is philosophically correct (operating near the wound is harder AND degrades the practitioner) but the interaction is not explicitly documented anywhere.

**Recommendation:** Add a note to state_transfer_spec.md or calamity_radiation.md: "Hybrid mode: Calamity Radiation Ob modifiers apply to both Personal Phase Thread operations (TTRPG rules) and Strategic Phase Thread orders (BG rules). Coherence cost from PC-declared leadership (PP-198) stacks independently with Radiation Ob modifiers."

---

## C. FINDINGS — TERRITORY NUMBERING INCONSISTENCIES

### C-01. params_board_game Uses Stale Territory Numbers (CONFIRMED — P1)

| params_board_game Reference | What It Says | Current Geography (geography_design.md) |
|---------------------------|-------------|----------------------------------------|
| L196: Crown Deed 2 | "Control T12 (Valorsplatz) + T9 (Arcansheld)" | T1 = Valorsplatz, no territory named Arcansheld |
| L214: Church Deed 3 | "T14 (Himmelenger)" | T9 = Himmelenger |
| L808–820: Southernmost Zones | T13 = Stillhelm, T12 = Oastad | T6 = Stillhelm, T13 = Oastad |
| L553: Varfell | "T9 (Vargstad)" | No territory named Vargstad; T4 = Grauwald (Varfell start) |

These are pre-geography_design.md numbering. victory_architecture_v1.md uses the correct current numbering throughout. params_board_game has not been updated.

**Required action:** Full territory number sweep in params_board_game. This is part of the A-03 rewrite.

---

## D. SUMMARY

### P1 Items (Blocking — Must Resolve)

| ID | Description | Files Affected |
|----|------------|----------------|
| A-01 | RS threshold bands disagree across 3 docs; params_board_game uses wrong bands + inverted Thread Ob | params_board_game |
| A-02 | Southernmost Zones vs Proximity Ratings — redundant, conflicting | params_board_game |
| A-03 | Victory conditions fully superseded but not propagated | params_board_game |
| ~~A-05~~ | ~~CV not in state_transfer_spec~~ | Already present (false finding) |
| B-04 | Thread Ob inversion error (−1 should be +1) | params_board_game |
| B-06 | CV track not in params_board_game | params_board_game |
| C-01 | Stale territory numbering throughout params_board_game | params_board_game |

### P2 Items (Should Resolve)

| ID | Description | Files Affected |
|----|------------|----------------|
| A-04 | TC generation formula not propagated | params_board_game |
| ~~A-06~~ | ~~Victory check at Accounting rewrite not propagated~~ | Already present (false finding) |
| A-07 | calamity_radiation.md Integration Notes not updated to mark completed cross-refs | calamity_radiation.md |
| A-09 | Warden Cooperation track not in params_board_game | params_board_game |
| B-05 | WA track not in params_board_game | params_board_game |
| B-09 | Hybrid + Calamity Radiation Ob stacking not documented | state_transfer_spec.md or calamity_radiation.md |

### P3 Items (Editorial Flags)

| ID | Description | Decision Needed |
|----|------------|----------------|
| B-01 | RS 100–60 band conflates Stable/Strained at Proximity 0 | Should Askeheim have effects at RS 100–80? |
| B-03 | Forgetting in RS-dependent matrix — should it be permanent T15 property instead? | Is Forgetting RS-dependent or permanent? |

### Canon Compliance

All five systems PASS canon constraints (P-01 through P-15) with two minor flags on Forgetting placement in Calamity Radiation (B-03, B-07).

### Systemic Observation

The core conflict pattern is clear: **params_board_game is the primary stale document.** It predates the Calamity Radiation framework, the Victory Architecture redesign, the Conviction Track system, the territory renumbering, and the RS inversion from Thread Tension. Nearly all P1 findings trace to params_board_game containing superseded mechanical values. The session log's Priority 1 work list (params_board_game propagation) is the correct fix.

calamity_radiation.md, threadwork_v25, and victory_architecture_v1.md are internally consistent with each other and with canon. The only cross-system conflicts between these three documents are minor (RS band label granularity at B-01).
