# Mode E — Core Principles Compliance: Faction / Political

Cross-referenced against the 13 core principles table in the skill definition
(`skills/valoria-mechanic-audit/SKILL.md`), which in turn derive from `canon/02_canon_constraints.md`
§A (P-01–P-15, personal-scale TTRPG Foundations) and §B (GD-1–GD-3, game-design constraints — these
apply *directly* to this subsystem and are checked explicitly below alongside the 13).

The faction/political layer is a **strategic/institutional-scale** system (BG Domain Actions,
Accounting, Parliament, rank ladders). Most of the 13 principles are personal-character-scale
mechanics (dice pools, wounds, Histories) that this subsystem legitimately does not implement
directly — same as `mass_battle` or `settlement_layer` would not. Per Mode E's own test column,
"ABSENT" is recorded factually where the mechanic doesn't apply at this scale, distinguished from a
canon *violation* (which would require an ABSENT where the mechanic SHOULD apply, or an ALTERED
without documented justification).

| # | Principle | Test | Verdict | Notes |
|---|---|---|---|---|
| 1 | Roll only when meaningful | Is there a "when to roll" gate? | ALTERED | No single named "when to roll" gate text at the faction layer, but the pattern holds structurally: Phase 2 Concession declaration is explicitly "No roll" (`faction_layer_v30.md` §3.3), Parliament Phase 2 is player negotiation at the table, and the d+σ resolver only fires for genuinely contested/uncertain Domain Actions — not every faction decision rolls. Adapted appropriately to strategic scale; not a violation. |
| 2 | Let It Ride | Is re-roll prohibition stated? | ABSENT | No explicit "no re-roll" statement anywhere in the 5 target docs. The single-draw structure of the d+σ resolver (`stats_1_7_scale.md` §Domain Action Resolution) structurally discourages re-rolling (one `r ~ U[0,1)` draw per action, consumed action-slot economy), but this is implicit, not stated. Low-severity documentation gap, not a mechanical violation — **no action**, not filed as new ED. |
| 3 | Fail Forward | Does failure advance narrative? | PRESENT | Consistently implemented: Church Seizure Failure → Mandate −1 (not "nothing happens"); Excommunication Failure → sympathy-martyr swing to the target; every DA Failure carries a stated consequence (Stability, Mandate, or Accord effect) rather than a null result. |
| 4 | Histories, not Skills | Are Histories lived experience, not categories? | ABSENT-BY-SCALE | Personal-character mechanic; not applicable to the faction/institutional layer. Not a violation — this subsystem does not model individual character Histories. |
| 5 | Pool = Attribute + History bonus | Is the base formula preserved? | ABSENT-BY-SCALE | Same as above — faction Domain Actions use the ratified d+σ margin resolver (`M = acting_stat − difficulty`), not a dice-pool-plus-History formula. This is a deliberate, already-ratified architectural choice (ED-874) distinct from personal-scale dice pools, not a lapsed application of P-05. |
| 6 | Wound system with escalating Ob | Is +1 Ob per wound implemented? | ALTERED | No literal "wound" track at faction scale, but a structurally analogous escalating-consequence system exists: the five Stability Triggers (`faction_layer_v30.md` §1.2) accumulate toward Collapse (§1.5), and Royal Decree's own "+1 Ob/season for consecutive use" fatigue mechanic is a direct escalating-difficulty pattern. Justified as scale-appropriate adaptation, not a canon violation. |
| 7 | Inspiration/Spirit economy | Is the emotional resource system present? | PRESENT (cross-referenced) | Not native to the faction layer, but properly delegates: Community Weaving's pool is `(Spirit×2)+History+TPS` (`params/threadwork.md` PP-616, cross-subsystem), and the caste-transgressive-Conviction mechanic (`faction_politics_v30.md` §3.6.1–§3.6.2) explicitly uses Spirit-pool checks (TN 7, Ob 1–3). |
| 8 | Virtues & Vices | Is moral character mechanical? | ALTERED (documented, ratified) | The legacy Ethical Framework Modifier system (Virtue/Faith/Categorical Imperative/etc. as binary Ob modifiers) was formally superseded by the PP-686 v2 triadic Mission/Cascade/Public-Expectation model (`faction_behavior_v30.md` §1, §6.4; `SUPERSESSION-PP686-001/002/003`). Moral character remains mechanical — it now flows through Convictions (PP-684 taxonomy) cascading up through faction leadership rather than a flat per-faction alignment tag. This is an explicitly ratified, well-documented alteration, not a silent drift. |
| 9 | Social combat via Rhetoric (Appeals, Debates, Negotiation distinct) | Are Appeals, Debates, Negotiation distinct? | PRESENT | Grand Debate (`faction_layer_v30.md` §4.2) explicitly delegates to `social_contest_v30.md`'s canonical Rhetoric structure rather than reimplementing it; Negotiation (§3.3, 3-phase Positioning/Concession/Ratification) and Parliament (§5, vote-based) are kept structurally distinct from each other and from Grand Debate. No collapsing of the three into one mechanic. |
| 10 | Reach/Speed priority | Does weapon geometry determine combat flow? | ABSENT-BY-SCALE | Personal-combat-only mechanic (governed by `combat_engine_v1`, a different subsystem). Not applicable here. |
| 11 | Phase-based combat | Is collaborative action within phases supported? | ABSENT-BY-SCALE (distinct sense) | The faction layer *does* have its own phase structure (`faction_layer_v30.md` §7 Turn Sequence, Phase 4 Priority 1–7 / Phase 5 Accounting Steps 1–10), but this is the BG/Accounting turn structure, not the personal-combat-engine "phase-based combat" the principle names. No violation — different mechanic, correctly scoped to `mass_battle`/`combat_engine_v1` where the personal-combat sense applies. |
| 12 | Beginner's Luck | Is accessibility for untrained attempts present? | ABSENT-BY-SCALE | Personal-character mechanic; not applicable to institutional-scale Domain Actions. |
| 13 | Circles and Resources | Are social/economic resolution systems present? | PRESENT | Strongly implemented: Wealth stat, Treasury/Fiscal-Stance yield formula (§5.9, PROPOSED), and — notably — a direct mechanical tie-in to the personal-scale Circles mechanic: Excommunication "strips target's Circles bonus with Church contacts" (`faction_canon_v30.md` §9; `stats_1_7_scale.md` Unique Actions). This is a clean cross-scale integration, not a duplicate reinvention. |

## GD-1 / GD-2 / GD-3 (§B, game-design constraints — directly applicable at this scale)

| Constraint | Test | Verdict | Notes |
|---|---|---|---|
| GD-1 (sole victory = Peninsular Sovereignty) | Does any doc declare a faction-specific victory condition? | PRESENT (compliant) | `faction_state_authoring_v30.md` §1 FSA-1 reconciliation explicitly reframes every non-Crown `mission.primary_objective` as an "approach-track" toward the universal victory, not a separate win trigger, and cites the GD-1 struck-content list correctly. See FA-D-03 (gap register) for the one loose-end identifier (Löwenritter's `victory.crown_peninsular_sovereignty` label not appearing in the FSA-1 enumeration) — a naming/reference gap, not a GD-1 violation in substance (Löwenritter's mission text and notes are unambiguous that it does not name an independent win condition). |
| GD-2 (deterministic threat response precedes stochastic selection) | Does AI action-selection run mandatories before stochastic candidates? | Not directly testable from these 5 docs | GD-2's `mandatory_actions(faction, world)` pass lives in `sim/provincial/faction_action.py` (implementation, out of scope for these design docs) and is cross-referenced correctly (`faction_layer_v30.md` §0 audit-patch table cites GD-2-adjacent migration work). No design-doc-level contradiction found. |
| GD-3 (Revolt → Insurgency → Faction pipeline) | Does faction-layer content block insurgency invasion of any faction, including the parent? | PRESENT (no contradiction found) | Not directly authored in these 5 docs (lives in `designs/world/insurgency_pipeline_v30.md`), but nothing in the faction/political docs contradicts GD-3's invariants (Collapse procedure §1.5 explicitly allows "Any faction may Claim Masterless units," consistent with open invasion eligibility). |

## Summary

No P1 core-principles violations found. All ABSENT verdicts are scale-appropriate (personal-character
mechanics not modeled at the institutional/faction layer, matching the pattern the corpus uses
consistently for `mass_battle` and `settlement_layer` as well) rather than lapsed applications of a
principle that should apply here. The one ALTERED-without-full-citation item (Let It Ride, #2) is
below the P1/P2 bar — implicit rather than violated.

**Disposition: no action.** No ED filed under Mode E.
