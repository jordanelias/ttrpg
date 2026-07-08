# ed_options.md — Subtractive docket (Jordan-rulable)

## Status: PROPOSED (2026-07-08) · one row per subtractive verdict · grouped by lane
Columns: `action | lane | verdict | criterion | intent_gate | severity | retires_downstream | one_line`. KEEP verdicts (62) omitted here — they carry no docket action. Judge each row as-if-built.

---

## PC — personal combat (11 subtractive)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Feint | PC | DISTILL | N — Abstractable/Duplicate (WS-5 ratified dissolution) | UNDETERMINED | P2 | module_contracts combat.feint PENDING row; PP-212/238/277/291/293/294 bespoke text | wrapper.py:140 already calls commit~2 "a feint" — the commit mechanic narrates it |
| Establish Distance | PC | MERGE | N — Duplicate vs Escape | UNDETERMINED | P2 | Escape standalone rule-block + resolution-order row | zero differentiated resolution text; a partial/full split would be invented |
| Escape | PC | MERGE | N — Duplicate vs Establish Distance | UNDETERMINED | P2 | Escape standalone rule-block + resolution-order row | identical mechanic, co-scheduled Priority 4, no textual differentiation |
| Disarm | PC | MERGE | N — Duplicate (Contact-axis precedent) | UNDETERMINED | P2 | Disarm/Tie Up/Retrieve collapse to 1; aligns combat.grapple PENDING | state_graph I7b/D8-D9 already branches intents by outcome, not separate rolls |
| Tie Up | PC | MERGE | N — Duplicate vs Disarm | UNDETERMINED | P2 | collapse to 1; drops PP-213 bespoke text | same Contact-axis template as Disarm |
| Retrieve | PC | MERGE | N — Abstractable/Edge-case | UNDETERMINED | P3 | Retrieve standalone rule-block + resolution-order row | Disarm is the only weapon-drop trigger; no independent decision to lose |
| Full Guard | PC | DISTILL | N — Abstractable vs base pool-split | UNDETERMINED | P3 | 2 ACTIONS rows (w/ Dodge); dup sim ACTION_RESOLUTION_ORDER | 0-Offence floor is redundant packaging; Templar talent re-keys to the state check |
| Dodge | PC | MERGE | N — Abstractable vs Full Guard/base pool-split | UNDETERMINED | P3 | 2 ACTIONS rows (w/ Full Guard); dup sim entries | ACTIONS table already classes both as "Reactive"; ranged-only carried by TN/DR |
| Rescue | PC | REFINE | Q-elegant — special-cased carve-outs | DELIBERATE | P2 | — (concept KEEP; simplify text) | eligibility gate + core contest load-bearing; chain-block/incap carve-outs read as accreted patches |
| Take a Breath | PC | REFINE | Ω-c/Μ-α — rest-state stalemate | UNDETERMINED | P3 | — (fix likely one layer up at scene pacing) | no forcing function vs mutual-rest stalemate |
| Stunt | PC | REFINE | Q-smooth — undefined dependency; no-GM premise conflict | NOT-INTENDED | P2 | — (bound to fixed-geometry vocabulary) | ED-1061 + combat_v30:372 fixed-geometry Stunt vocab proves the bounded fix achievable |

## SC — social contest (3 subtractive)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Recall citation + Pre-Contest Prep | SC | REFINE | Ω-d cost-hidden / Q-elegant unflagged exception | NOT-INTENDED | P2 | KU-1 (global stacking-cap docket item, P0) | +5D +3D +1D = +9D on a 12–18D pool, no combined ceiling; corroborated by 2026-07-04 L-A |
| Appraise | SC | REFINE | N-Abstractable (channel a) / Q-robust (channel b) | NOT-INTENDED | P2 | — (narrow to proceeding-type scope) | trivial for the 2 venue-fixed proceedings; unresolved fixed-at-setup vs senses-current contradiction |
| Wager Obligation | SC | DISTILL | N-Abstractable (self-duplicated scope) | NOT-INTENDED | P3 | generational_transition Obligation-interruption (shared rule) | institutional-collapse rows fold into a shared Obligation-interruption rule; PC-death rows already reuse TRANSFER/RESET — leave those |

## FA — faction/domain (6 subtractive)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Parliamentary Motion — punitive cluster | FA | DISTILL | N — Abstractable (parameterizable fields) | DELIBERATE | P2 | 5 rows of faction_layer_v30 §5.4 + §5.5 ladder share → 1 | preserve Outlawry CB-to-all + Blockade Military-gate as explicit parameters |
| da.* Key contract taxonomy | FA | REFINE | Q-elegant — undeclared verb→bucket crosswalk | UNDETERMINED | P2 | domain_actions doc:null closure → crosswalk-table task | NOT a duplicate catalog — it's the substrate's normal Key-routing layer; author the crosswalk |
| Investigate/Intel + Spy | FA | REFINE | Q-robust — Spy lacks a stated Failure branch | UNDETERMINED | P2 | add explicit Failure clause to Spy's row | named contrast: sibling Survey has a Failure branch, Spy doesn't |
| Diplomacy between players | FA | DISTILL | N — Duplicate coverage (Treaty §3.3 Ph2) | UNDETERMINED | P3 | −1 row from params/bg/core.md Standard Action Ob table | §3.3/§3.8 states the mechanic verbatim; §3.2 frames Treaty-init as the Senator Social action |
| Claim Masterless units | FA | DISTILL | N — Abstractable/Edge-case | DELIBERATE | P3 | faction_layer_v30 §1.5 dedicated rule → conditional clause in Conquest | uncontested race + disband-on-failure expressible as one clause on Conquest target-selection |
| "Thread Operation" as FA-scale action | FA | REFINE (downgraded from PRUNE) | Q-smooth — authoring hygiene, not scale-break | DELIBERATE | P3 | single-source TW attempt_* logic; keep FA slot-cost/PP-182 interface note | legitimate FA/TW interface (like March/Conquest's Fort table), not a pure duplicate |

## SE — settlements (7 subtractive)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Grant / Revoke Subnational Mgmt | SE | PRUNE | N/Ω pass; lane-homing dedup | DELIBERATE | P2 | consolidates into FA C-FA-12 (domain_actions) | it is a Provincial-Authority Domain Action, not SE-native — single-ownership |
| Trade | SE | PRUNE | Ω-a personal-only + N duplicate/abstractable | NOT-INTENDED | P3 | closes module_contracts settlement_economy retirement | bare income roll, zero settlement/faction/NPC effect unlike every sibling |
| Sponsor / Sponsor event | SE | MERGE | Ω-d dominant-strategy from duplicate specs | NOT-INTENDED | P2 | OPT-16 staging | §9 no-downside flat version strictly dominates the Debt-bearing redesign version |
| Investigate | SE | DISTILL | N — duplicate roll-engine (not outcome menu) | UNDETERMINED | P2 | redesign §5.2 build item 3 (event-deck engine) −1 resolver | share the check math only, not the FI scene-graph apparatus |
| Administer | SE | DISTILL | N — abstractable (both halves subsumed) | NOT-INTENDED | P3 | OPT-16 staging | risk-free info half dominates Investigate; maintenance half subsumed by Keep Order Consent |
| Fund Development | SE | MERGE | N — duplicate/special-cased vs Develop funding | NOT-INTENDED | P3 | OPT-16 staging | content-free die-bonus with no Ledger tag of its own; folds into Develop |
| Treat | SE | REFINE | Q-smooth — chit call-in trigger unspecified | UNDETERMINED | P3 | — (spec the trigger) | no-GM engine makes the unspecified call-in an implementability gap |

## WR — world / Scene Slate (4 subtractive incl. 1 clause CUT)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Step 6 — Territorial Scenes | WR | MERGE (+ clause CUT) | N — duplicate coverage | UNDETERMINED | P3 | NPC-arrival→Step 5 merge; Thread-phenomenon clause CUT (retires that clause) | CUT (not merge) the Thread clause to protect Step 2b's scarcity discipline |
| Step 7 — Ambient Scenes | WR | DISTILL | Flavor-only (Ω, Μ-γ) | DELIBERATE | P3 | one numbered Scene-Slate Step | pursued payoff is minor filler Step 6 could deliver without a dedicated Step |
| Witness Mode — Narrative Input Sentence | WR | DISTILL (downgraded P2→P3) | Flavor-only + no-GM invariant mismatch | NOT-INTENDED | P3 | the Narrative Input surface | inert beat resolved by NPC AI treating player as absent; no downstream hook |
| Step 4 — Conviction-Aligned Scenes | WR | REFINE | Q-elegant — capitalization-as-signal fails | DELIBERATE | P3 | — (explicit keyword-tagging → one-breath rule) | system keywords double as English words → routine nagging or silent Step-4 drop |

## FI — field investigation (2 subtractive)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Interview (single-roll object) | FI | MERGE | N — duplicate coverage (two incompatible live specs) | NOT-INTENDED | P2 | ED-921 + fieldwork half of ED-IN-0016/EP-8 → one Jordan call per cluster_C-FI.md | investigation_systems_v30:425 asserts "instead of" total replacement, not tiering; audit names the collapse, not the winner |
| Dialogue Lattice utterance-selection | FI | REFINE | Q-elegant — composed 5-filter chain | DELIBERATE | P3 | — (simplify/expose, don't discard) | C-FI-2 shows the composed complexity already produced an unnoticed internal contradiction |

## TW — threadwork (2 subtractive)

| action | lane | verdict | criterion | intent_gate | sev | retires_downstream | one_line |
|---|---|---|---|---|---|---|---|
| Past-Oriented Pulling | TW | DISTILL | N — abstractable into Pulling | DELIBERATE | P2 | folds POP into generalized Pulling; realizes orphaned "POP Binding" TN row | POP's Ob replaces Depth+Breadth+Distance entirely (scale-blind); canon already wants it generalized |
| Mending | TW | REFINE | Q-robust — false "3 viable approaches" | DELIBERATE | P2 | — (collapse the pseudo-menu) | collective/Einhir "approaches" are the same operation + Ob table at scale; Amendment 3 zero-cost asymmetry untouched |

---

### Overturned by the inverted critic (recorded, no docket action)
| action | lane | prior | outcome | why |
|---|---|---|---|---|
| Tactic: Concentration | MB | (dominance flag) | **OVERTURNED-TO-KEEP** | win-rate deficit is the named counter working as intended; Ω-d-in-reverse not charter-licensed |
| Selecting a deliberative game | SC | REFINE/P1 | **OVERTURNED-TO-KEEP** | four source mechanisms are distinct, not skins; REFINE functionally judged pre-Stage-4 spec completeness — cardinal-rule violation |
