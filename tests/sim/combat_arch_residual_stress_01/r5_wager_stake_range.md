# R5 — Wager Stake Range
## Module 5 of combat_arch_residual_stress_01

**Date:** 2026-05-09
**Mode:** A coverage + B (interaction chains)
**Source question:** *"What is the range of wagerable stakes in the canonical Wager mechanic? Coverage: cosmetic (item, gold) → reputational (Renown, Disposition) → existential (Conviction Scar, Companion bond). Cross-system effects at extremes? Ratification needed for stake-type table + ranges."*

**Decision shape:** stake-type table + ranges + cross-system effect at extremes.

---

## 1. Re-framing the question against actual canon

The synthesis R5 question assumed a flexible "Wager" mechanic with variable stake magnitudes (cosmetic, reputational, existential). **Actual canon has a different structure.** Per `designs/scene/social_contest_v30.md` §6.1.1 and ED-778 (resolved):

- **Wager Obligation** is a *future-conditional Obligation* — an extension of the base Obligation mechanic. The winning side names a verifiable future condition; if met, the losing side delivers a negotiated benefit; if not, default Grand Contest violation consequences fire.
- The "stake" of a Wager is **structurally determined by contest type** (Formal Contest / Grand Contest / Royal Audience / Church Tribunal), not by a free-form stake-severity tag.
- ED-778 closed the spec gap on Wager Obligation edge cases (counterparty death, institutional collapse, condition impossibility).

**The synthesis's premise — that Wager has a free-form cosmetic-to-existential stake range — is not present in canon.** R5 must be re-asked: should canon ADD such a stake-range axis, or is the contest-type-derived stake structure sufficient?

---

## 2. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R5-L01 | obligation_duration_by_contest_type | Formal 2 seasons; Grand 4 seasons or until condition; Royal 2 seasons; Tribunal until revoked | designs/scene/social_contest_v30.md | §6.1 | "\| Formal Contest (Parliament) \| 2 seasons \| Violating faction: Mandate −1. Reputation shift. Contest Fatigue on faction leader. \|" |
| R5-L02 | grand_contest_violation_consequences | Mandate −2, Stability −1, +2 Ob next DA targeting violator | designs/scene/social_contest_v30.md | §6.1 | "**Condition not met within timeframe:** Obligation fails. Default Grand Contest violation consequences fire (Mandate −2, Stability −1, +2 Ob next DA targeting" |
| R5-L03 | wager_obligation_definition | Future-conditional Obligation; verifiable-future-condition framing | designs/scene/social_contest_v30.md | §6.1.1 | "**Wager Obligations (extension — verifiable-future-condition framing):** Obligations may take a future-conditional form when the winning side explicitly extends" |
| R5-L04 | wager_resolution_three_outcomes | Condition Met / Not Met / Partial | designs/scene/social_contest_v30.md | §6.1.1 | "Wager resolution operates on the named condition rather than on duration alone:" |
| R5-L05 | wager_edge_case_spec_complete | ED-778 closed spec gap on edge cases | designs/scene/social_contest_v30.md | §6.1.1 | "[EDITORIAL: ED-778 — Wager Obligation edge cases specified in §6.1.1. Closes spec gap surfaced by stress-test 49: base Wager spec (Condition Met / Not Met / Par" |
| R5-L06 | obligation_player_violation_allowed | Player may violate Obligation; consequences fire | designs/scene/social_contest_v30.md | §6.1 | "**Player Obligations:** When the player loses a contest, they receive an Obligation. The player is not forced to comply — they may violate it. Violation consequ" |
| R5-L07 | conviction_scar_existing_channel | Conviction Scar accumulation through major narrative events | designs/scene/derived_stats_v30.md | §Conviction (R1v2-L11 cross-ref) | "Lifetime; shifts only through Scar accumulation or major narrative events" |

---

## 3. The structurally-defined stake hierarchy

Canon's Wager doesn't have a free-form stake range, but contest types DO encode an implicit stake hierarchy:

| Contest Type | Implicit stake severity | Default consequences (R5-L01, R5-L02) |
|---|---|---|
| **Formal Contest** (Parliament) | Reputational | Mandate −1, Reputation shift, Contest Fatigue |
| **Grand Contest** | Reputational + Material | Mandate −2, Stability −1, +2 Ob next DA |
| **Royal Audience** | Crown-mediated | Crown Mandate −1 (high political severity) |
| **Church Tribunal** | Existential (theological) | Heresy Investigation acceleration, Excommunication eligible |

The synthesis's "cosmetic → existential" range is *partially* achieved through contest-type selection. Cosmetic stakes (item, gold) are NOT canonically a contest outcome — they're the province of fieldwork-Socializing exchanges, not formal contests. Existential stakes (Conviction Scar, Companion bond) ARE canonical for Tribunal contests and for decisive contests producing Conviction Scars (R5-L07).

---

## 4. Candidates

| ID | Name | Description |
|---|---|---|
| **C5.1** | Preserve canonical Wager Obligation | Wager is the future-conditional Obligation per §6.1.1. Stakes are derived from contest type per R5-L01. No new stake-severity axis introduced. |
| **C5.2** | Add explicit stake-severity tag | Wager Obligations gain a "stake severity" tag (cosmetic / reputational / existential) modifying violation consequences. New decision-point per Wager. |
| **C5.3** | Voluntary stake escalation | Players may voluntarily declare elevated stakes ("I stake my Conviction Scar on this") at contest start, enabling existential consequences for any contest type. |

---

## 5. NERS at full grain — 24 cells per candidate

### C5.1 — Preserve canonical (contest-type-derived stakes)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Canon mature post-ED-778 (R5-L05). Stake hierarchy implicit in contest type. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Wager resolution three-outcome table (R5-L04) covers all cases. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Contest type maps cleanly to scope (province → settlement → person). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Cross-system effects (Mandate, Stability, Reputation, Heresy Investigation) all wire through existing channels. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Conviction Scar (R5-L07) operates as the existential-stake channel for decisive contests; not specific to Wager. |
| Horizontal | ⚠ | ✓ | ✓ | ✓ | ⚠ on the design-pattern question: synthesis asked about cosmetic/wager bet — that genre-pattern is not present in canon, which may be a gap if Jordan wants tavern-game / dueling-stake content. |

**Verdict C5.1:** 23/24 ✓, 1 ⚠ on Horizontal (cosmetic-stake gap if desired). Canonical preservation; canon is mature.

### C5.2 — Add explicit stake-severity tag

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ⚠ | ⚠ | Stake-severity tag duplicates the contest-type structure (which already encodes severity per R5-L01). ⚠ S: redundant with existing canon. |
| Bottom-up | ⚠ | ⚠ | ✓ | ⚠ | Tag would need to interact with Obligation duration, violation consequences, edge case resolutions — substantial spec work. |
| Vertical | ✓ | ⚠ | ✓ | ⚠ | Cross-scale severity already mapped via contest type → faction-stat consequence. Adding tag duplicates. |
| Diagonal | ✓ | ⚠ | ✓ | ⚠ | New tag interacts with Conviction track (R5-L07) — Scar generation triggered by tag rather than contest decisiveness. Reframes existing Scar mechanic. |
| Lateral | ✓ | ⚠ | ⚠ | ⚠ | Wager-with-tag becomes more complex than Wager-without-tag for low gain. |
| Horizontal | ✓ | ⚠ | ✓ | ⚠ | Achieves "explicit cosmetic-existential range" but at significant complexity cost. |

**Verdict C5.2:** N=⚠ on 2, E=⚠ on 5, R=⚠ on 2, S=⚠ on 5. **PASS but high cost; functionally redundant with contest-type hierarchy.**

### C5.3 — Voluntary stake escalation

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ⚠ | ✓ | ⚠ | Player declares "I stake X" at contest start — adds player-agency surface; needs spec for what's stakable. |
| Bottom-up | ⚠ | ⚠ | ✓ | ⚠ | Voluntary Conviction Scar staking interacts with Conviction track mechanics (R5-L07) — Scar accumulation rules need extension. |
| Vertical | ✓ | ⚠ | ✓ | ⚠ | Cross-scale: a voluntarily staked Companion bond at scene scale propagates to relational and faction layers. New cross-layer pathway. |
| Diagonal | ⚠ | ⚠ | ✓ | ⚠ | Threadwork, fieldwork, mass-battle interactions: a stake-escalated Wager might trigger Threadwork operations (Companion bond as Knot ↔ stake). Substantial cross-system surface. |
| Lateral | ✓ | ⚠ | ✓ | ⚠ | Voluntary stake mechanic interacts with Conviction Wager (R-pending) and existing Obligation structure — joint spec needed. |
| Horizontal | ✓ | ✓ | ✓ | ⚠ | Genuine new player-agency surface — gives players narrative leverage by accepting elevated stakes. Strong horizontal value. |

**Verdict C5.3:** N=⚠ on 3, E=⚠ on 5, R=✓ on 6, S=⚠ on 5. **PASS with substantial spec work; novel player-agency value but cross-system coupling extensive.**

### Cross-candidate summary

| Candidate | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| C5.1 Preserve canonical | 6/6 (1⚠) | 6/6 | 6/6 | 6/6 | **PASS — minimal work, canon mature** |
| C5.2 Stake-severity tag | 4/6 (2⚠) | 1/6 (5⚠) | 4/6 (2⚠) | 1/6 (5⚠) | **PASS but redundant with contest-type hierarchy** |
| C5.3 Voluntary stake escalation | 3/6 (3⚠) | 1/6 (5⚠) | 6/6 | 1/6 (5⚠) | **PASS with substantial spec; novel agency value** |

---

## 6. Mode B — Interaction chain analysis

### Chain 1: Contest type → implicit stake severity → violation consequences (canon)

Per R5-L01 + R5-L02: each contest type encodes a stake severity tier. Player choosing to escalate from Formal to Grand contest IS choosing higher stakes. Canonically the stake-magnitude axis is *contest-type selection*, not an additional tag.

Under C5.1: player makes stake decision via contest-type selection. Mature mechanic.

Under C5.2: player makes stake decision twice — once via contest-type (which already implies stakes), once via explicit tag. Redundant decision-point.

Under C5.3: player makes stake decision via contest-type AND can voluntarily escalate. Two-axis stake structure; richer but adds complexity.

### Chain 2: Conviction Scar generation in decisive contests (R5-L07)

Per R5-L07 and prior R1v2-L11: Conviction Scar accumulation happens through "Scar accumulation or major narrative events." Decisive contest outcomes already generate Scars per npc_behavior §3.3.

Under C5.1: existential stakes (Conviction Scar) emerge from decisive outcomes, automatic.

Under C5.2: a "existential" tag would force Scar generation regardless of contest decisiveness — *changes* the Scar mechanic by detaching it from decisive-outcome trigger.

Under C5.3: voluntary "I stake my Scar" at contest start would also force Scar on loss regardless of decisiveness — same Scar-mechanic-detachment issue but player-initiated rather than tag-driven.

**The Scar mechanic's coupling to decisive outcomes is structurally important.** Both C5.2 and C5.3 weaken this coupling. C5.1 preserves it.

### Chain 3: Player agency surface (Horizontal direction)

C5.1: player agency = choice of contest type. Existing.

C5.2: player agency = contest type + tag. Tag is GM-derivable from contest type, so player choice is largely cosmetic.

C5.3: player agency = contest type + voluntary stake escalation. Genuine new surface. Player can accept higher consequences for higher reward — narrative leverage.

C5.3 has the strongest Horizontal value for player agency. But the cross-system coupling cost is substantial.

### Chain 4: Wager Obligation edge cases (R5-L05)

ED-778 just resolved Wager Obligation edge cases (counterparty death, institutional collapse, condition impossibility). Adding stake-severity tags or voluntary escalation would require ED-778-equivalent edge case work for the new axes — re-opening recently-closed spec ground.

### Chain 5: Cosmetic-stake mechanic (item, gold)

If Jordan wants tavern-game / dueling-purse content (cosmetic stakes), this is mechanically a fieldwork-Socializing exchange, not a formal contest. The synthesis's "cosmetic" tier may be misclassified — it belongs to fieldwork mechanics (informal exchange, no Obligation track), not to Wager (formal Obligation). C5.1 implicit answer: cosmetic stakes are NOT a Wager mechanic; they are fieldwork.

---

## 7. Mode D — Edge cases (compressed)

### Boundary
**EC-D5.B-01 [P3] (C5.3):** What is the maximum voluntary stake? Companion bond? Conviction Track Resonance? Coherence track? Each is structurally permanent; all-or-nothing stakes break the "scaled severity" intent.

### Cascade
**EC-D5.C-01 [P2] (C5.2/C5.3):** Stake-tag interaction with chain contests (§6.3): does a "existential" tag persist across Compromise → chain follow-up? Spec gap.

### Regression
**EC-D5.R-01 [P3] (C5.3):** Players optimize: voluntary-stake-existential at every contest where they expect to win. Conviction Scar farming on opponents.

### Crunch cascade
**EC-D5.CR-01 [P2] (C5.2):** Per-contest tag selection adds bookkeeping that duplicates contest-type encoding.

### Ambiguity
**EC-D5.A-01 [P1] (C5.2/C5.3):** "Existential" / "reputational" / "cosmetic" boundary criteria undefined. Same problem as R1v2 C1.2 "catastrophic" tag.

### Incoherence
**EC-D5.I-01 [P2] (C5.2/C5.3):** Conviction Scar mechanic decouples from decisive-outcome trigger. Reframes existing canon.

### Optimal play
**EC-D5.O-01 [P3] (C5.3):** Player optimal: stake heavily when winning probability high; refuse Wager when winning probability low. Canonical contest-fatigue mechanic doesn't fully constrain this.

### Degenerate
**EC-D5.DG-01 [P3] (C5.2):** Stake-tag becomes purely cosmetic (always set to match contest type) → C5.2 collapses to C5.1 with overhead.

---

## 8. Decision-shape findings

**Recommendation: C5.1 (preserve canonical Wager Obligation; clarify that the synthesis's "cosmetic-existential stake range" is implicitly addressed by contest-type selection).**

**Defer C5.3 (voluntary stake escalation) for explicit Jordan ratification — it has genuine player-agency value but substantial cross-system coupling cost. Not auto-rejecting.**

**Reject C5.2 (stake-severity tag) — functionally redundant with contest-type hierarchy R5-L01.**

**Rationale:**

1. **Canon is mature post-ED-778 (R5-L05).** Wager Obligation has been edge-case-closed. The synthesis's "stake range" question presumed a free-form mechanic that doesn't exist in canon; the existing structure (contest type → implicit stake severity → typed violation consequences) achieves the same coverage through structural means.

2. **C5.1 passes 23/24 NERS** with 1 ⚠ on Horizontal (cosmetic-stake gap if desired for tavern-game content). The cosmetic gap is correctly addressed in fieldwork-Socializing mechanics, not in Wager.

3. **C5.2 is functionally redundant.** The stake-severity tag duplicates contest-type encoding. Adding it would create a parallel decision-point that GMs would likely default to "tag matches contest type."

4. **C5.3 has genuine player-agency value** but requires:
   - Spec for what's voluntarily stakable (Conviction Scar? Companion bond? Coherence?).
   - Edge case work parallel to ED-778 for the new agency surface.
   - Cross-system coupling spec (voluntary-Scar-stake interaction with npc_behavior §3.3 decisive-outcome Scar generation).
   This is significant additional work. Recommend Jordan consider C5.3 as a separate design initiative, not as part of R5 ratification.

**Implementation under C5.1 (no mechanical change; documentation):**

- Affirm `social_contest_v30.md §6.1.1` as canonical Wager Obligation spec.
- Clarify in §6.1 preamble: stake severity is encoded in contest-type selection (R5-L01); there is no parallel stake-tag axis.
- Address the "cosmetic stake" gap by directing tavern-game / dueling-purse content to fieldwork-Socializing mechanics (informal exchange), distinct from formal Wager Obligation.

**Decision-shape statement for Jordan ratification:**

> Wager Obligation per `social_contest_v30.md §6.1.1` is canonical and mature post-ED-778. Stake severity is structurally derived from contest type (Formal / Grand / Royal / Tribunal), not from a parallel stake-magnitude axis. The synthesis's "cosmetic → existential range" is partially achieved through contest-type selection (Tribunal = existential; Grand = reputational + material) and partially deferred to fieldwork-Socializing (cosmetic / item / gold exchanges, which are not Wager). Voluntary stake escalation (player elects elevated consequences for elevated reward) is a candidate refinement (C5.3) — has genuine player-agency value but requires substantial spec work; recommend treating as a separate design initiative.

**Open items for Jordan:**

- Affirm C5.1 as R5 closure.
- Decide on C5.3 — pursue as separate PP, defer indefinitely, or reject?
- Confirm: cosmetic-stake content (tavern games, dueling purses) routed to fieldwork, not Wager?

---

## 9. Module status

| Item | Status |
|---|---|
| Canonical sources fetched at full depth | ✓ |
| R5 question re-framed against actual canon | ✓ |
| Verification ledger entries (7) | ✓ |
| NERS full-grain analysis | ✓ |
| Mode B chains (5) | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding (C5.1 primary; C5.3 deferred initiative; C5.2 reject) | ✓ |
| Cosmetic-stake routing clarification | ✓ |

**Module 5 status: verified.**
