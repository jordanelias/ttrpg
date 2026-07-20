<!-- [CLOSED: 2026-04-28 session] -->
<!-- STATUS: SESSION CLOSE OBSERVATIONS — all 68 ERS stress test issues with comprehensive context -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/16_session_close_observations.md -->

# Session Close: Political Dynamics Stress Test — Comprehensive Observations

**Session:** 2026-04-28-stress-test  
**System tested:** `12_development_specification.md` (political dynamics / ERS system, current spec)  
**Batches:** 13 (technical), 14 (NERS all directions), 15 (NERS batch 3)  
**Total issues:** 68  

---

## OVERARCHING OBSERVATIONS

### 1. The Architecture Is Sound

After 68 issues across three batches, the spec's fundamental architecture holds. The five-layer model (per-NPC state → armature → Event Impact Matrix → Settlement/Faction Meta-Armatures → Player-Facing Surfaces) is logically coherent. The cascade attenuation model (0.7/boundary), the three-path Belief revision system, the five Accounting procedures — these are well-conceived. None of the 68 issues require architectural redesign.

This is important context: the issues are concentrated in implementation gaps (undefined functions, missing values, unused fields) and design specification gaps (undefined thresholds, unspecified triggers), not in structural failures. The skeleton works. The flesh is missing in places.

### 2. Four Classes of Issues Dominate

Across all 68 issues, four classes account for ~85% of findings:

**Class A — Undefined functions or values (15 issues):** The spec specifies that something happens but not how. `select_proposal()`, `conviction_alignment_multiplier`, `max_scars`, `generate_new_project()`, `visible_actions` for generated projects, `backstory_tags` consuming procedure, settlement signal window derivation, `knowledge_type` decay rates, DA failure Concern salience, Priority 4 Scene Slate trigger. These are authoring and spec completeness items, not design decisions. They have correct answers derivable from the system's own logic — they just weren't written down.

**Class B — Unused fields or systems (8 issues):** concern_history (write-only), backstory_tags (never read), knowledge_type decay (authored, unimplemented), EventImpact.visibility (authored, unenforced), symbolic_effects/210-entry table (consumed by nothing), certainty/ts (cross-system orphans). Pattern: the spec authored data structures that the procedures don't reference. This is a spec-procedure alignment failure — either the procedures need to be written, or the fields need to be removed. The 210-entry symbolic resonance table is the most costly of these: significant authoring effort with zero procedural consumption.

**Class C — Tie-breaking and edge-case undefined behavior (6 issues):** Memory replacement ties, Concern cap ties, Opinion initialization on first contact, Passive NPC Memory replacement, conviction_secondary=None at Scar 3+, unknown event types in resonance table. These are all implementation-facing: they don't matter until someone writes the code, at which point implementations will make arbitrary choices that diverge. They should be specified.

**Class D — Cross-procedure ordering and double-write (5 issues):** Procedures B, C, D all writing to Opinions (double-count on the same data structure). Knowledge → Concern lag (1 season). Settlement Signal lag (1-2 seasons). Procedure E drift delayed. Concern resolution vs Procedure D double-counting. Pattern: the sequential Accounting model creates inherent lags and write-order dependencies that aren't fully resolved in the spec.

### 3. Two Issues Are Blocking for Implementation

**E-36-A** (`select_proposal()` undefined) and **E-48-A** (`max_scars` undefined) are the only issues where implementation is literally impossible without a design decision from Jordan. Every other issue either has a specified-enough behavior to implement with a reasonable assumption, or is a missing field that defaults to zero/null gracefully.

These two must be resolved before implementation begins. All other Critical-tier issues (the salience-4/5 cliff, the crash on empty Passive NPC sets) are implementation-blocking in a crash sense but have obvious correct patches that don't require Jordan input.

### 4. The Single-Writer Opinion Problem Is the Most Consequential Architectural Gap

Three procedures write to the same Opinion data structure in one Accounting pass:
- Procedure B-Resolution (directly, via Concern resolution outcome)
- Procedure C (directly, via Project completion legacy)
- Procedure D (from Memories)

This produces double-counting (B-Resolution creates a Memory AND writes an Opinion; D then processes the same Memory). The fix (single-writer model: B and C produce Memories only; D consolidates all Opinion changes) is clean and doesn't affect any other system. But it requires rewriting the apply_resolution() and apply_project_legacy() functions. This should be the first spec edit.

### 5. The 210-Entry Symbolic Resonance Table Decision

The symbolic_effects field appears in the Event Impact Matrix and is populated via the 210-entry conviction × event-type resonance table. No procedure in the spec consumes it. This table represents the largest single authoring commitment in the spec (~200+ entries). Before authoring begins, Jordan must decide:

- **Option A (keep, define consumption):** Define symbolic_effects as Concern salience modifiers in Procedure B. `contradicted` resonance → +1 salience on Concern generation. `aligned` → -1 salience. This integrates the table into procedure output with minimal added complexity and makes the authoring investment worthwhile.
- **Option B (cut):** Remove symbolic_effects from the Event Impact Matrix. Save ~200 authoring entries. The Conviction × event-type signal is captured indirectly through armature interpretation anyway — NPCs whose armature is Faith-weighted will already interpret Faith-contradicting events as higher-urgency Concerns. The table may be redundant with the armature system.

This is the highest-stakes design decision to emerge from the tests. The table either needs a procedural home or needs to be cut before authoring begins.

### 6. Scene Slate Pressure Is a Player Experience Risk

R-39-A identified that in a politically active mid-campaign season, all five player scene actions may be consumed by NPC-driven mandatory Priority 1-3 content. This is the only issue that directly threatens the game's core UX goal ("positive feedback loop between player decisions and mechanics"). If players cannot make discretionary scene choices, the feedback loop breaks — they are reacting to the world, not shaping it.

The fix (Concern-driven Outreach as available rather than mandatory) is non-invasive. But the underlying tension between NPC initiative and player agency requires ongoing monitoring through playtest. The current design favors NPC initiative heavily — which produces emergent narrative richness but may frustrate strategic players who want to direct their own agenda.

### 7. The Salience-4 vs Salience-5 Binary Cliff Is a Tuning Risk

Multiple tests converged on the same issue from different angles (E-VERT-A, S-DIAG-A): the 0.7² attenuation from personal to faction scale creates a binary threshold at salience 5 (reaches faction influence at 2.45) vs salience 4 (reaches 1.96 — below the influence threshold of 2.0). A personal event at salience 4 has zero faction-level effect; at salience 5 it has meaningful influence.

This binary behavior is an authoring trap: event designers must know that salience 4 personal events don't propagate to faction level. This is unintuitive — a "significant" event (salience 4) appears to have no political consequence, while a "major" event (salience 5) suddenly does. The propagation_weight patch addresses this, as does slightly lowering the influence threshold to 1.5 for high-weight events.

### 8. NPC Standing Is Static — Missing a Major Robustness Vector

R-40-A identified that NPC Standing never changes during a campaign. Standing weights the Faction Meta-Armature — the same Marshal who starts at S6 ends the campaign at S6 regardless of whether all his projects failed. The proposed fix (annual recalculation based on Project completion and DA success) adds modest complexity but significantly enriches the emergent political dynamics: a failing Marshal loses institutional weight, a rising Bishop gains it. This is a direct implementation of "makes players feel like they are impacting the game world" — if the player engineers the Marshal's failures, the Marshal's influence should visibly diminish.

### 9. The Knot Auto-Surfacing Opacity Contradiction Is Minor But Matters

S-LAT-A: Knot partner Concerns are "automatically surfaced" — but the opacity principle throughout the spec states that NPCs share by choice through scenes, not by direct data access. The Knot auto-surfacing is the only place in the spec where an NPC's inner state bypasses the choice-to-share model.

The fix is narrative framing only: replace "auto-surfaced" with "generates mandatory Priority 2 Outreach scene driven by the Concern." The player still learns about the Concern through dialogue, not mechanical readout. Mechanically identical. Philosophically consistent with the opacity model.

### 10. The Revision-Arc for Imposed Beliefs (RS-50) Is Correct and Should Be Documented

The post-Contest Belief arc (NPC's armature autonomously erodes an imposed Belief over 4-8 seasons unless player reinforces it) is the system working as designed. This is one of the strongest emergent behaviors the spec produces. It means:
- Player can impose beliefs through sufficient political investment (Total Victory Contests)
- Imposed beliefs are unstable unless maintained through ongoing relationship investment
- Abandoned NPCs eventually recover toward their Conviction-authentic positions

This creates a compelling maintenance dynamic for player-shaped NPCs. It deserves explicit documentation in §3.5 as a featured design behavior, not a gap.

---

## ISSUE REGISTER (All 68)

### Batch 1 — Technical (13_stress_tests_extended.md)

| ID | Area | Severity | Summary |
|---|---|---|---|
| ST-13-A | Memory replacement | Medium | Tie-break undefined for equal-salience Memory cap |
| ST-13-B | Memory merge | Medium | Merge trigger conditions unspecified |
| ST-14-A | Concern dropping | Medium | Tie-break undefined for Concern cap |
| ST-14-B | Concern cap | Low | Transient overflow under simultaneous events |
| ST-15-A | Opinion initialization | High | First-contact Opinion initialization unspecified |
| ST-15-B | Procedure E+D | High | Drift written to non-existent Opinion object on first contact |
| ST-16-A | Memory salience floor | Clarify | Permanent max-salience lock — intentional, needs documentation |
| ST-17-A | Path A reset | High | Reset mechanism requires per-Belief `contested_this_season` flag — not implementable as written |
| ST-18-A | Procedure B ordering | Low | Mood set during B-Resolution active for DA phase — implicit, needs clarification |
| ST-19-A | DA phase + Grieving | High | Grieving major-action auto-fail not wired into DA Proposal Phase pseudocode |
| ST-19-B | Project stall | Clarify | Grieving-induced Project stall behavior correct but undocumented |
| ST-20-A | Settlement Signal | **Critical** | ZeroDivisionError / max() crash on empty Passive NPC set |
| ST-20-B | Settlement Signal | Medium | No governor fallback when Passive NPC set is empty |
| ST-21-A | Cascade attenuation | Medium | Downward propagation from peninsula-scale undefined |
| ST-21-B | Event Impact Matrix | Low | scale_signature split-by-scale not defined |
| ST-22-A | Anomaly detection | Medium | "Major external crisis" threshold undefined |
| ST-23-A | Armature | High | conviction_secondary=None at Scar 3+ crashes weight derivation |
| ST-24-A | Event Impact Matrix | High | Unknown event_type crashes Matrix construction — no fallback |
| ST-25-C | Anomaly detection | Low | "Disposition-with-leader" referent ambiguous |
| ST-26-B | Faction Meta-Armature | Clarify | institutional_stability regeneration path unspecified |
| ST-27-A | Project legacy | Low | "Obstructor" for failed Project legacy undefined |
| ST-28-A | Concern resolution | Medium | Knowledge entries not searchable in Concern resolution |
| ST-29-A | Loyalty Cover | Low | Decay rate unspecified |
| ST-29-B | Loyalty Cover | Low | Base player.cover relationship to bonus undefined |
| ST-30-A | Witness Mode | Medium | No uniqueness constraint on NPC per Accounting |
| ST-31-A | Procedure E sharing | High | Knowledge sharing has no sensitivity gate — faction secrets propagate in ambient contact |
| ST-31-B | NPC self-monitoring | Design choice | No Concern generated on sensitive information disclosure |
| ST-32-A | Opinion drift | High | Double-counting: B-Resolution writes Opinion AND resulting Memory processed by Procedure D |

### Batch 2 — NERS All Directions (14_ners_stress_tests.md)

| ID | Area | Criterion | Severity | Summary |
|---|---|---|---|---|
| N-TOP-A | Settlement layer | N | Gap | Layer validity contingent on Passive NPC count; dependency not flagged |
| N-BOT-A | backstory_tags | N | Friction | Field authored but consumed by no procedure |
| N-BOT-B | certainty / ts | N | Gap | Cross-system orphans; scope unclear |
| N-BOT-C | concern_history | N | Design-Fail | Write-only field — populated but never read |
| N-BOT-D | knowledge_type | N | Design-Fail | Decay behavior authored in §2.7, not implemented in any procedure |
| N-BOT-E | EventImpact.visibility | N | Design-Fail | Authored but not enforced in Concern generation |
| N-HORIZ-A | Knowledge sharing | N | Gap | seek-tag vocabulary unspecified — match frequency unknown |
| N-HORIZ-B | Gossip | N | Friction | No mechanical input to gossip system — player-informing only |
| N-LAT-A | DA failure Concern | N | Design-Fail | Salience for DA-failure-generated Concern unanchored |
| N-LAT-B | Priority 4 Scene Slate | N | Design-Fail | NPC-NPC interaction → Scene Slate trigger threshold undefined |
| N-DIAG-A | Standing 5 milestone | N | Friction | Player enters Meta-Armature invisibly — no in-game signal |
| N-DIAG-B | Exposure + Anomaly | N | Gap | Both detection paths can fire same season without coordination |
| E-TOP-A | Player intuition | E | Gap | Design stance needed: opaque-by-design vs legible-by-design |
| E-BOT-A | Opinion drift formula | E | **Critical** | conviction_alignment_multiplier is undefined — formula unresolvable |
| E-BOT-B | Armature modifiers | E | Design-Fail | Additive vs multiplicative unspecified; normalization rule missing |
| E-VERT-A | Cascade attenuation | E | Friction | Uniform 0.7 creates salience-4 vs 5 binary cliff at faction influence |
| E-HORIZ-A / S-HORIZ-A | Procedures B/C/D | E+S | Design-Fail | Three procedures write to Opinions; single-responsibility violation |
| E-LAT-A | Scene Slate integration | E | Friction | Four scattered hooks vs one clean PoliticalSlate interface |
| E-DIAG-A | Diagonal chain | E | Acceptable | Legible only to heavily-invested players — known tradeoff |
| R-BOT-A | Personality modifiers | R | Gap | Personality → armature modifier table unauthored; values unverifiable |
| R-VERT-A | Personal → faction | R | Friction | Personal victories feel insignificant at faction scale by design |
| R-LAT-A | Cross-system chain | R | Gap | Strategy valid but gated by uncontrollable conditions |
| R-DIAG-A | 6-season investment | R | Gap | Expected faction-shift threshold for max investment undefined |
| S-TOP-A | Player-visible output | S | Acceptable | Rich internal state, limited player-visible output — opacity by design |
| S-VERT-A | Scale transition lag | S | Friction | Settlement Signal 2-season lag in cross-scale propagation |
| S-HORIZ-B | Procedure E lag | S | Acceptable | E effects delayed 1 Accounting vs B/C — realistic, acceptable |
| S-LAT-A | Knot opacity | S | Design-Fail | Knot auto-surfacing contradicts opacity principle |
| S-DIAG-A | Salience cliff | S | Friction | Same salience-4/5 binary cliff — diagonal context |

### Batch 3 — NERS Continued (15_stress_tests_batch3.md)

| ID | Area | Criterion | Severity | Summary |
|---|---|---|---|---|
| N-33-A | Scar count | N | Design-Fail | Conviction vs peripheral Scars indistinguishable; peripheral revisions shift core armature |
| N-34-A | Project stall | N | Friction | Stall threshold uniform; not horizon-proportional |
| N-35-A | Population Disposition | N | Design-Fail | No update trigger — static value in dynamic formula |
| E-36-A | DA competition | E | **Critical** | select_proposal() undefined — inner-circle competition unimplementable |
| E-37-A | Mood triggers | E | Design-Fail | Vindicated and Resolved Moods have no specified trigger conditions |
| E-38-A | symbolic_effects | E | Design-Fail | Consumed by no procedure — 210-entry table mechanically inert |
| E-38-B | symbolic_effects | N | Design-Fail | 210 authored entries with zero mechanical output — waste if uncorrected |
| R-39-A | Scene Slate | R | Design-Fail | Player may have zero discretionary scene actions mid-campaign |
| R-39-B | Scene Slate | S | Friction | NPCs hold initiative; player reacts rather than directs |
| R-40-A | NPC Standing | R | Design-Fail | Standing static — faction power distribution never shifts |
| R-41-A | Crisis masking | R | Design choice | Player can suppress anomaly detection via manufactured crises; persistence counter optional |
| R-42-A | Passive NPC Memory | N | Gap | Replacement rules unspecified for Passive tier |
| S-43-A | Knowledge lag | S | Friction | 1-season lag between Knowledge acquisition and Concern generation — structural |
| S-44-A | Settlement Signal | S | Design-Fail | Disposition-with-player amplifies ALL Memories, not just player-involving |
| S-45-A | Read action | S | Friction | +3 Disposition yields no additional Read benefit vs +2 — misleading progression |
| S-45-B | Information systems | N | Gap | Read/Outreach are two separate information systems with separate gates — undocumented |
| S-46-A | Project generation | S | Design-Fail | Replacement Project derivation after completion unspecified |
| E-47-A | Settlement Signal window | E | Friction | 2-season window is a magic constant |
| E-47-B | Settlement Signal window | E | Friction | Uniform window regardless of settlement density |
| E-48-A | Faction Meta-Armature | E | **Critical** | max_scars undefined — institutional_stability formula unresolvable |
| NS-49-A | visible_actions | N+S | Design-Fail | Procedurally-generated Projects produce null Observable Behavior surface |
| NS-49-B | Observable Behavior | S | Design-Fail | Silent null-output failure when visible_actions missing |
| RS-50-A | Imposed Belief arc | R+S | Clarify | Post-Contest Belief recovery arc correct but undocumented; should be featured |

---

## PRIORITY ORDER FOR SPEC REVISION

**Must resolve before any implementation work:**

1. **E-36-A** — Define `select_proposal()` algorithm and domain_armature_alignment table
2. **E-48-A** — Define `max_scars` = inner_circle_active_npc_count × 2
3. **E-BOT-A** — Define `conviction_alignment_multiplier` values in §6.2 Procedure D
4. **E-HORIZ-A / S-HORIZ-A / ST-32-A** — Single-writer Opinion model (B and C produce Memories only; D consolidates)
5. **ST-20-A** — Null guard in `compute_settlement_signal()` for empty Passive NPC sets
6. **ST-23-A** — Fallback for conviction_secondary=None at Scar 3+
7. **ST-24-A** — Fallback for unknown event_type in resonance table
8. **E-BOT-B** — Specify armature modifier math as additive + normalize per dimension

**Must resolve before authoring begins:**

9. **E-38-A/B** — Decision: define symbolic_effects consumption (Concern salience modifier) OR cut the 210-entry table
10. **N-BOT-C** — Define concern_history consumption or remove field
11. **N-BOT-D** — Implement knowledge_type decay in Procedure B
12. **N-BOT-E** — Enforce EventImpact.visibility in Procedure B Concern generation
13. **ST-15-A/B** — Define Opinion initialization on first contact
14. **ST-19-A** — Add Grieving handling to DA Proposal Phase pseudocode
15. **S-LAT-A** — Rephrase Knot auto-surfacing as Priority 2 Outreach scene
16. **N-33-A** — Split scar_count into scars_total and scars_conviction
17. **E-37-A** — Define Vindicated and Resolved trigger conditions
18. **N-35-A** — Define Population Disposition update trigger or remove from Meta-Armature
19. **R-39-A** — Redefine Priority 3 Outreach as available content, not mandatory
20. **R-40-A** — Define NPC Standing recalculation at Campaign Year boundary
21. **S-44-A** — Scope Settlement Signal Disposition-with-player amplification to player-involving Memories only
22. **S-46-A** — Define replacement Project derivation (pre-authored queue + Conviction-based fallback)
23. **NS-49-A/B** — Define visible_actions templates for procedurally-generated Projects

**Can be addressed during implementation:**

24. ST-13-A/B — Memory tie-breaking and merge trigger
25. ST-14-A/B — Concern cap tie-breaking and loop ordering
26. ST-17-A — Path A reset via contested_this_season flag
27. ST-22-A — Major external crisis threshold definition
28. ST-27-A — Project failure obstructor tracking
29. ST-28-A — Knowledge entries in Concern resolution search
30. ST-29-A/B — Loyalty Cover decay rate and base value relationship
31. ST-30-A — Witness Mode uniqueness constraint
32. ST-31-A — Knowledge sharing sensitivity gate
33. N-LAT-A/B — DA failure Concern salience and Priority 4 Scene Slate threshold
34. R-42-A — Passive NPC Memory replacement rules
35. E-VERT-A / S-DIAG-A — Salience cliff (propagation_weight or threshold adjustment)
36. E-47-A/B — Settlement Signal window derivation
37. S-43-A — Priority Knowledge fast path (salience 5)
38. N-34-A — Horizon-proportional stall threshold
39. N-45-B — Read/Outreach two-system documentation

**Document as featured behavior (no spec change required):**

40. RS-50-A — Post-Contest Belief recovery arc
41. ST-16-A — Permanent salience-5 founding Memory behavior
42. R-41-A — Crisis masking (with optional persistence counter enhancement)
43. E-DIAG-A — Diagonal chain legibility tradeoff
44. N-DIAG-A — Standing 5 milestone visibility (add Outreach scene)

---

## HEALTH ASSESSMENT

The political dynamics system as specified in `12_development_specification.md` is **implementable with targeted spec work**. The 68 issues are concentrated in four addressable classes. No issue requires architectural revision. The system produces correct emergent behavior in clean paths (demonstrated in R-TOP, R-HORIZ, RS-50-A analysis).

**Estimated spec revision scope:** ~40-60 targeted edits to doc 12 covering all priority-1 and priority-2 items. The highest-value single edit is the single-writer Opinion model (resolves ST-32, E-HORIZ, S-HORIZ simultaneously). The second highest-value is the symbolic_effects decision (resolves E-38-A/B and determines whether 210 entries need authoring).

**Authoring scope impact:** If symbolic_effects table is cut: saves ~200 entries. If backstory_tags removed: saves ~210 entries (35 NPCs × 6 tags). Total potential authoring reduction from scope cuts: ~400 entries. These are mechanical dead weight; cutting them does not reduce the system's functional output.
