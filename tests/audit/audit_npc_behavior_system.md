# AUDIT REPORT: NPC Behavior System v1
## Audited against: canon/00_philosophical_foundations.md, canon/02_canon_constraints.md, stage6_factions.md, params_factions.md, params_board_game.md, params_core.md, params_contest.md, social_contest_system_v2.md, edeyja_npc.md, character_histories_lifepath.md, geography_design.md, victory_architecture_v1.md, calamity_radiation.md, threadwork_redesign_v25.md
## Date: 2026-04-13
## Auditor: Claude (Opus 4.6)

---

## Summary

15 findings. 3 canon violations (1 hard, 2 soft). 3 source contradictions. 4 mechanical issues. 3 gaps. 2 notes.

---

## CANON CONSTRAINT FINDINGS

### AUD-NPC-01 — P-08 VIOLATION (SOFT): Evidence Resonant Style vs Epistemological Barrier
**Constraint:** P-08 — non-sensitives can recite but not act with Thread-level precision. The barrier is metaphysical, not institutional. Publishing all documents would not end the barrier.

**Issue:** §1.3 defines Evidence Resonant Style as "Specific, verifiable, named facts contradicting their operative belief." §2.2 (Himlensendt) says "Show him facts he cannot dismiss within his theology." No distinction is drawn between ontical evidence (political, historical, documentary) and ontological evidence (Thread-level data). For TS 0 NPCs, Thread-level evidence is epistemically inert per P-08 — they literally cannot render it as knowledge. Using Thread-level evidence as Resonant Style targeting against Himlensendt would violate P-08 because the evidence cannot function as "facts he cannot dismiss" — he cannot even epistemically access the facts.

**Fix required:** §6.2 or §1.3 must specify that Evidence targeting against TS 0 NPCs is restricted to ontical evidence (documents, testimony, political facts, historical records). Thread-level evidence does not function as Evidence Resonant Style against non-sensitives. It is epistemically inert — per Foundations §10.1, "The knowledge is propositionally available — they can recite what they have been told — but they cannot epistemologically reconcile it." A fact that cannot be epistemologically reconciled cannot function as a Resonant Style attack.

**Exception:** If the NPC's TS crosses Stirring (30+) during play, Thread-level evidence becomes valid Evidence targeting. This is the Himlensendt Arc C scenario.

**Severity:** SOFT. The proposal never explicitly permits Thread-level Evidence against TS 0 NPCs, but it fails to explicitly prohibit it. The fix is a clarifying constraint, not a redesign.

---

### AUD-NPC-02 — P-12 VIOLATION (SOFT): NPC Arc Transformation Missing Knot Strain Propagation
**Constraint:** P-12 — a transforming practitioner's thread-shift exerts force on everyone knotted to them. Knot strain mechanics must propagate transformation effects.

**Issue:** §5.2 defines NPC arc profiles including transformation arcs (Vaynard Arc C: epistemic seduction; Himlensendt Arc C: confrontation). Neither arc profile mentions Knot strain propagation to characters knotted to the transforming NPC. Per Foundations §16.3: "Their threads are knotted to other people — family, fellow practitioners, community members. As their threads shift toward the unintelligible pole, the knots exert a subtle pull on those connected to them."

**Scope:** This primarily affects Vaynard Arc C (TS crosses threshold, potential transformation) and Himlensendt Arc C (TS awakening). Almud's TS 28 is near Stirring but does not cross it in any arc — no transformation, no Knot strain. Edeyja's TS 75-80 is already stable — no transformation in progress.

**Fix required:** Arc profiles involving TS threshold crossing must include Knot strain propagation rules:
- NPC at TS 30+: Close Knots to the NPC experience +1 strain/season (per existing Knot strain mechanics in threadwork_v25).
- NPC at TS 50+: Close Knots +2 strain/season; Distant Knots +1 strain/season.
- NPC in epistemic seduction (Vaynard Arc C): Knot strain doubles (the transformation is accelerating).

**Severity:** SOFT. The proposal references epistemic seduction correctly (Foundations §16.1) but omits the relational propagation consequence (§16.3). The fix is additive, not a redesign.

---

### AUD-NPC-03 — P-04/P-10 COMPLIANCE: Confirmed PASS
**Constraint:** P-04 (monstrosity = ontological, not moral), P-10 (epistemic seduction = perceptual shift, not corruption).

**Status:** The proposal correctly frames all NPC arcs as transformation rather than corruption. §12 states "No NPC is 'evil' — they are structurally positioned. Arc emergence produces transformation, not corruption." Vaynard Arc C uses "epistemic seduction" correctly per Foundations §16.1. No moral valence assigned to monstrous entities or transformation states. **PASS.**

---

## SOURCE CONTRADICTIONS

### AUD-NPC-04 — CONTRADICTION: Baralta Conviction Changed Without Editorial Flag
**Source:** stage6_factions.md §8.4 — "Conviction: Order · Resonant Style: Evidence"

**Proposal:** §2.3 assigns Baralta primary Conviction as "Precedent" (new category), not "Order."

**Analysis:** Stage6 is a stale compilation stage (canonical_sources.yaml: "Stage6 OUTDATED"). However, for TTRPG factions, stage6 is the only source — no design-layer replacement exists. The existing "Conviction: Order" entry is the canonical value until explicitly superseded.

The proposal's "Precedent" is arguably a better fit for Baralta's Categorical Imperative framework and her described behavior ("constitutional procedure IS justice"). The existing "Order" duplicates Almud's Conviction, losing a meaningful distinction between Crown and Hafenmark leaders. However, the change was made without editorial flag.

**Additionally:** BG params_board_game.md lists Baralta's motto as "Faith is not mediated — it is lived" — this expresses Faith, not Order or Precedent. The proposal puts Faith as secondary Conviction, which is consistent with the motto. But the motto-Conviction alignment is with Faith (secondary), not Precedent (proposed primary).

**Fix required:** Flag the change as `[EDITORIAL: ED-4xx — Baralta Conviction changed from Order (stage6 canonical) to Precedent. Rationale: distinguishes Baralta from Almud; aligns with Categorical Imperative framework. User approval required.]`

**Severity:** MEDIUM. The change is defensible but unauthorized.

---

### AUD-NPC-05 — CONTRADICTION: Vaynard Arc A vs edeyja_npc.md
**Source:** edeyja_npc.md — "If he reaches TK 5 and comes to her, she will talk to him — possibly for the first time in her life that she's talked to someone who understands what she's managing."

**Proposal:** §5.2 Vaynard Arc A — "May seek Edeyja — she would assess him and probably reject him (he has knowledge without competence)."

**Analysis:** Direct contradiction. The canonical Edeyja document explicitly states she WOULD engage with TK 5 Vaynard. The proposal says she would "probably reject him." The Edeyja document's statement is specific and canonical.

The proposal's logic (knowledge without competence) has merit — Vaynard at TK 5 but TS < 30 lacks experiential Thread engagement. But the canonical document already accounts for this: Edeyja talks to him because he "understands what she's managing," not because he can perform Thread operations. His structural understanding (TK 5 = "understands what Solmund was structurally") is sufficient for conversation, not collaboration.

**Fix required:** Revise Vaynard Arc A: "At TK 5, Vaynard may seek Edeyja. Per edeyja_npc.md: she will engage substantively — he understands the Calamity's mechanism structurally. However, she will not grant full collaboration (Warden Cooperation) without demonstrated Thread competence (TS 30+). The conversation is real; the operational partnership requires more."

**Severity:** HIGH. Direct contradiction with a canonical NPC document.

---

### AUD-NPC-06 — CANON TENSION: Edeyja Arc C vs "She never leaves the Southernmost"
**Source:** edeyja_npc.md — "She never leaves the Southernmost. Scenes with her always occur in Southernmost territory."

**Proposal:** §5.2 Edeyja Arc C — "Edeyja may leave the Southernmost for the first time. This is a campaign-defining event."

**Analysis:** The canonical document's statement is present-tense descriptive ("she never leaves"), not a metaphysical impossibility. Arc C is premised on extraordinary crisis conditions (Warden count 0 OR RS ≤ 20). Under these conditions, the behavior described in the canonical document would be expected to change — the conditions under which "she never leaves" are precisely the conditions Arc C specifies have failed.

This is a TENSION, not a violation. The arc explicitly frames this as a departure from her established behavior, which is the definition of arc emergence. However, the canonical document does not contemplate this possibility, and the proposal should acknowledge the departure explicitly.

**Fix required:** Add to Arc C: "This arc explicitly overrides edeyja_npc.md §'She never leaves the Southernmost.' The canonical statement describes her current behavior under current conditions. Arc C specifies the conditions under which that behavior changes. The canonical document's later statement — 'She needs help she cannot ask for from people who don't know she exists' — implies she would act differently if the Southernmost's survival required it."

**Severity:** LOW. The tension is acknowledged and justified by the arc's crisis conditions.

---

## MECHANICAL ISSUES

### AUD-NPC-07 — Framework Drift Exceeds Stat Ceiling (1–7 Scale)
**Issue:** §7.1 Church Framework Drift: "If no external challenge for 2 consecutive seasons: Influence +1 (institutional confidence)." Church starts at Influence 6. After 4 unchallenged seasons (2 increments), Influence reaches 8 — exceeding the 1–7 stat scale.

**Also applies to:** Hafenmark Influence drift (+1/season when all actions framework-aligned). Hafenmark starts at Influence 4. After 3 eligible seasons, Influence reaches 7 (ceiling). Fine — but the rule does not state a ceiling.

**Fix required:** All Framework Drift rules must include: "Cannot exceed stat ceiling (7). Cannot go below stat floor (1)." This mirrors the existing seasonal cap language.

**Severity:** MEDIUM. Mechanical error, easy fix.

---

### AUD-NPC-08 — Framework Drift Bypasses Seasonal Cap
**Issue:** The existing seasonal cap is ±2 per stat per season from Domain Actions (PP-242). Framework Drift is passive (not a Domain Action). The proposal does not specify whether Framework Drift counts toward the seasonal cap.

**Precedent:** CI passive advance (+1/season, PP-402) is explicitly separate from the DA cap. RS baseline decay (−1/year, PP-255) is separate from DA effects. These suggest passive effects are NOT subject to the DA seasonal cap.

**Fix required:** Explicitly state: "Framework Drift is a passive effect, not a Domain Action. It does not count toward the ±2 DA seasonal cap. It IS subject to the stat ceiling (7) and floor (1)."

**Severity:** LOW. Consistent with existing passive effect precedent, but needs explicit statement.

---

### AUD-NPC-09 — Resonant Style +1D Stacking Creates Large Pools
**Issue:** §6.5 permits up to +5D positional bonus on Argue rolls (genre +1, audience +1, Resonant Style +1, Recall +2). Combined with a high-attribute pool (e.g., Charisma 7 → 14 base + History bonus ≈ 8 + 5D positional = 27D at TN 7), this produces very high success probability. Against audience resistance of 1–2, a single exchange could move the Conviction Track by 5+ points, producing Total Victory in one exchange.

**Existing caps:** No existing rule caps total bonus dice on Argue rolls.

**Status:** Already flagged as SIM-DEBT in the proposal (SIM-NPC-02). The proposal correctly identifies this as requiring simulation. However, the audit notes that 27D pools were never contemplated in the contest system design (social_contest_system_v2.md §3 implies pools of ~8–14D as typical).

**Fix required:** None immediate — simulation will determine if rebalancing is needed. But the proposal should note that 27D pools are possible and represent an extreme case.

**Severity:** LOW (flagged for simulation, not a rule error).

---

### AUD-NPC-10 — RM Presence Spread Rate May Be Too Fast
**Issue:** §7.1 RM Framework Drift: "+1 adjacent territory per season when RM Stability ≥ 3." RM post-founding Stability is 3 (Success) or 4 (Overwhelming). At Stability 3, RM spreads to 1 new territory every season. Over 4 seasons (1 year), 4 new territories gain Presence markers. The peninsula has 17 territories.

**Analysis:** Presence markers are not territorial control — they are influence markers. But they affect Community Organising pools (+1D per adjacent territory with Presence) and RM victory conditions. Automated spread at 1/season means RM covers 10+ territories within 3 years of founding, which may undermine the difficulty of the RM victory path.

**Fix required:** Consider gating spread on an action cost (RM must spend a Domain Action to spread, not passive drift). Alternatively, cap at 1 Presence spread per 2 seasons, or require Community Organising success before spread fires.

**Severity:** LOW (balance concern, not a rule violation). Already implicitly flagged under SIM-NPC-04.

---

## GAPS

### AUD-NPC-11 — GAP: Varfell Ethical Framework Label Mismatch Between Sources
**BG params_board_game.md:** "Varfell (Epistemic Reason) — Evidence-based Intel −1 Ob | Emotional/reactive +1 Ob"
**Stage6_factions.md:** "Consequentialist Pragmatism — Actions with measurable outcomes within one season −1 Ob | Actions with uncertain or long-term payoff +1 Ob"

The proposal uses "Consequentialist Pragmatism" (stage6 label) and derives Vaynard's behavior accordingly. But BG params use "Epistemic Reason" with different modifiers. These are substantively different frameworks: one evaluates by outcomes, the other by evidence quality.

**Impact on proposal:** The Stance Triangle for Vaynard assumes Consequentialist Pragmatism. If BG uses Epistemic Reason, Vaynard's BG Priority Tree may need different Priority 3 triggers (evidence-based rather than outcome-based).

**Fix required:** This is a pre-existing inconsistency between BG and TTRPG faction descriptions. The proposal should note it and flag for reconciliation. Recommend aligning on one label. "Epistemic Consequentialism" (evidence-driven outcomes evaluation) may bridge both.

**Severity:** PRE-EXISTING. Not introduced by the proposal.

---

### AUD-NPC-12 — GAP: NPC Belief Formation Mechanics Not Specified for Non-Leader NPCs
**Issue:** §3.1 says "Named NPCs hold 2–3 Beliefs." §4.2 says non-named NPCs have no Beliefs. But several important NPCs fall between these categories — Cardinals, Riskbreakers, Maret Uln (pre-succession), Aldric Hann, Torben. The proposal provides Beliefs for some (Hann, Cardinals) but the criteria for who qualifies as "named" is not formalized.

**Fix required:** Define: "A named NPC holds Beliefs if they have (a) a Stance Triangle defined in this document, OR (b) a canonical NPC document (e.g., edeyja_npc.md), OR (c) faction leader status. All other NPCs are non-named for Belief purposes, regardless of whether they have a proper name."

**Severity:** LOW (clarification needed, not a rule error).

---

### AUD-NPC-13 — GAP: Solidarity Resonant Style Requires Knot, But NPC Knot Formation Unspecified
**Issue:** §1.3 says Solidarity Resonant Style "requires active Knot with the NPC." §6.3 confirms: "Requires active Knot (Close or Distant) with NPC." But NPC Knot formation is not specified in the proposal OR in existing documents. PC-to-PC Knots are formed through play (threadwork_v25 §Knots). PC-to-NPC Knots are referenced in the character_histories_lifepath.md (Stages 1–3 produce suggested Close Knots) but the mechanical process for forming NEW Knots with NPCs during play is not formalized.

**Impact:** Without a Knot formation mechanic, Solidarity Resonant Style is inaccessible against NPCs who are not pre-assigned Knot partners at character creation. This makes Solidarity the hardest Resonant Style to activate — possibly too hard.

**Fix required:** Cross-reference threadwork_v25 for existing Knot mechanics. If NPC Knot formation is absent, flag as `[GAP: NPC Knot formation mechanic needed — blocks Solidarity Resonant Style accessibility]`. The lifepath system's "suggested Knot" at Stages 1–3 provides a starting framework but does not cover mid-campaign Knot formation with new NPCs.

**Severity:** MEDIUM. Blocks a core mechanic for one of four Resonant Styles.

---

## NOTES (Non-Actionable Observations)

### AUD-NPC-14 — NOTE: Torben Blank Conviction Is Intentional But Novel
**Observation:** §2.8 proposes that Torben starts with no primary Conviction — "first faction to invest in him sets his initial Conviction." This is a novel design choice with no precedent in existing NPC design. All other named NPCs have defined starting Convictions.

The design intent is clear (Torben as contested narrative asset), and the Loyalty track (existing mechanic, range 0–7) already models factional competition for Torben's allegiance. Adding Conviction as a second dimension of contest is defensible.

**No fix required.** Already flagged as ED-525 in the proposal. User confirmation needed.

---

### AUD-NPC-15 — NOTE: Arc Emergence Default Outcomes Favor Status Quo
**Observation:** If PCs do not intervene, the default arcs are:
- Almud → Arc B (Fortress): Certainty drifts up, Order doubles down.
- Himlensendt → Arc A (Zealot): CI advances unchallenged.
- Baralta → either Arc A (triumph) or Arc C (excommunication), depending on Church CI progress.
- Vaynard → stalls at TK 3, never reaches awakening.
- Edeyja → Arc A (Holdout): wardens slowly lose ground.

This means the default game state — without PC social intervention — trends toward Church Theocracy (Himlensendt unchallenged), Crown rigidity (Almud's Fortress), Varfell stagnation (TK cap), and Southernmost decline (Edeyja holding but losing). This is a GOOD design outcome: it creates urgency for PC engagement. The world gets worse if players do not act. Noting for user awareness, not as a finding.

---

## FINDINGS SUMMARY

| ID | Category | Severity | Fix Type |
|---|---|---|---|
| AUD-NPC-01 | Canon (P-08) | SOFT | Clarifying constraint |
| AUD-NPC-02 | Canon (P-12) | SOFT | Additive rule |
| AUD-NPC-04 | Source contradiction | MEDIUM | Editorial flag |
| AUD-NPC-05 | Source contradiction | HIGH | Text revision |
| AUD-NPC-06 | Canon tension | LOW | Acknowledgment text |
| AUD-NPC-07 | Mechanical | MEDIUM | Ceiling/floor rule |
| AUD-NPC-08 | Mechanical | LOW | Explicit statement |
| AUD-NPC-09 | Mechanical | LOW | Simulation (already flagged) |
| AUD-NPC-10 | Mechanical | LOW | Balance consideration |
| AUD-NPC-11 | Pre-existing gap | PRE-EXISTING | Note and flag |
| AUD-NPC-12 | Gap | LOW | Definition clause |
| AUD-NPC-13 | Gap | MEDIUM | Cross-reference or new mechanic |

AUD-NPC-03, AUD-NPC-14, AUD-NPC-15 are PASS/NOTE (no fix required).

---

## RECOMMENDED FIX PRIORITY

1. **AUD-NPC-05** (HIGH): Revise Vaynard Arc A to match edeyja_npc.md on Edeyja's TK 5 engagement.
2. **AUD-NPC-01** (SOFT canon): Add TS-gate to Evidence Resonant Style — Thread-level evidence only valid against TS 30+ NPCs.
3. **AUD-NPC-02** (SOFT canon): Add Knot strain propagation to transformation arc profiles.
4. **AUD-NPC-04** (MEDIUM): Add editorial flag for Baralta Conviction change.
5. **AUD-NPC-07** (MEDIUM): Add stat ceiling/floor to Framework Drift.
6. **AUD-NPC-13** (MEDIUM): Flag NPC Knot formation gap.
7. All other findings: LOW priority, addressable during params extraction.

*End of audit.*
