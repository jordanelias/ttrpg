# Mechanical Review & Audit Record (consolidated)

## Consolidation front matter

- **topic_id:** `06_mechanical_review_audit`
- **atom_count:** 83
- **scope:** valoria_master_document.md atoms not already pulled by other topics. Master mechanical-review record covering die/TN/wager/conviction/scale-transition/etc. Likely candidate for sub-decomposition during execution if 100+ atoms remain.
- **source distribution:**
  - `valoria_master_document.md`: 83 atoms
- **drift surface:** single-source
- **post-audit canon target:** `designs/ (multiple subpaths) — likely sub-decompose during consolidation`
- **status:** assembled (pending audit Stage 3)
- **assembled_from_commit:** atoms committed at `83c37da7001defdf3bb3425b17dda3f934d262d3`

## Audit checklist (Stage 3 input)

- [ ] Sections are non-overlapping or overlap is justified.
- [ ] Mechanical specs match existing designs/ where applicable; new specs are flagged.
- [ ] No internal contradictions across sections.
- [ ] Open Decisions Requiring Jordan (II.2) listed as decision points, not as resolved.

## Known drift dimensions

- High volume — may contain internal redundancy that becomes apparent only after consolidation.
- Section numbering (1.x, 19.x) may need re-anchoring against existing designs/.

## Content

Atoms in section_index order from source.

<!-- atom: valoria_master_document__00__preamble | section_index: 0 | source_section: "(preamble)" -->


# VALORIA — Master Mechanical Review and Audit Record

<!-- atom: valoria_master_document__01__conversation-date-2026-04-24-to-2026-04-25-compile | section_index: 1 | source_section: "Conversation Date: 2026-04-24 to 2026-04-25 | Compiled from session work" -->


## Conversation Date: 2026-04-24 to 2026-04-25 | Compiled from session work

<!-- atom: valoria_master_document__03__1-1-die-face-rule-d10 | section_index: 3 | source_section: "1.1 Die Face Rule (d10)" -->


## 1.1 Die Face Rule (d10)

| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes |

Net = total successes − total 1s. May be negative (PP-246). Same rule in every system. No exceptions.

**N** ✓ Foundation of all resolution. **R** ✓ The 1-face as anti-success means pool size is a risk calculation — larger pools can still produce net 0 if 1s cluster. **E** ✓ Four effect values (−1, 0, +1, +2); three non-zero outcomes. Learnable in one roll. **S** ✓ Universal. Zero system-specific overrides.

⚠ **FLAG-01: Chain rule comment.** params/core.md contains a note about an exploding-10 variant (E ≈ +1.43). This is NOT canonical. Strike or mark NON-CANONICAL to prevent implementation contamination.

<!-- atom: valoria_master_document__05__1-3-obstacle-scale | section_index: 5 | source_section: "1.3 Obstacle Scale" -->


## 1.3 Obstacle Scale

Ob 1 (Routine) → 2 (Moderate) → 3 (Difficult) → 5 (Entrenched) → 8 (Structural) → 20 (Foundational, cap). Floor: 1. Cap: 20. Intermediate values (4, 6, 7) appear in calculated Obs and are valid — the named scale is reference, not enumeration.

**N** ✓ **R** ✓ Non-linear spacing creates natural tier breaks. **E** ✓ **S** ⚠ BG mode has Ob 10 exception (Overwhelming unavailable, Partial ≥ 5). TTRPG has Ob 20 exception (Overwhelming unavailable, Partial ≥ 10). Two different exception thresholds for the same concept. Minor — unify to single "extreme Ob" rule parameterized by mode.

<!-- atom: valoria_master_document__06__1-4-degrees-of-success | section_index: 6 | source_section: "1.4 Degrees of Success" -->


## 1.4 Degrees of Success

| Degree | Condition |
|--------|-----------|
| Overwhelming | Net ≥ 2×Ob AND net ≥ 3 |
| Success | Net ≥ Ob |
| Partial | Net > 0 but < Ob |
| Failure | Net ≤ 0 |

**N** ✓ Four degrees → four narrative outcomes. Partial is the "yes but" that drives story. **R** ✓ 2×Ob naturally scales. Floor of 3 prevents trivial Overwhelmings at Ob 1. **E** ✓ Four categories. Two conditions for Overwhelming. One each for others. **S** ✓ Universal across all systems.

<!-- atom: valoria_master_document__11__3-1-pool-split-off-def | section_index: 11 | source_section: "3.1 Pool Split (Off/Def)" -->


## 3.1 Pool Split (Off/Def)

Each round: allocate Combat Pool dice between Offence and Defence. Min 1 each (except Full Guard/Feint).

**N** ✓ THE core combat decision. **R** ✓ 10D pool → 5/5 balanced, 8/2 aggressive, 2/8 defensive. Each split tells a story. **E** ✓ Zero overhead. **S** ✓ Same paradigm in mass combat Phase 5.

<!-- atom: valoria_master_document__12__3-2-initiative | section_index: 12 | source_section: "3.2 Initiative" -->


## 3.2 Initiative

Exchange 1: higher Attunement declares last (information advantage). Subsequent: transfers to exchange winner. Tie: stays with holder. Tiebreak: Att → Agi → GM/coin (PP-239).

**N** ✓ **R** ✓ Attunement (not Agility) for E1 = perceptive > fast. Cross-build value. **E** ✓ Three rules. **S** ✓

<!-- atom: valoria_master_document__13__3-3-weapon-system-3-binary-axes | section_index: 13 | source_section: "3.3 Weapon System (3 Binary Axes)" -->


## 3.3 Weapon System (3 Binary Axes)

Reach (Short −1 TN / Long +0) × Weight (Light −1 / Heavy +0) × Type (Blade +0 / Blunt +1). Base TN 7. Produces TN 5 (Short Light Blade) to TN 8 (Long Heavy Blunt).

**N** ✓ 8 archetypes from 3 bits. **R** ✓ Each axis = real trade-off. Short hits more, Long reaches more. Heavy hits harder, Light hits more often. Blunt ignores armour scaling, Blade is effective against unarmoured. **E** ✓ **Best subsystem in the game.** Three yes/no questions → TN. **S** ⚠ **DECISION-04 (ED-129 OPEN):** Ranged weapons NOT mapped to this matrix. Bow/crossbow/sling use legacy LP/HP/LBl/HBl classification. Dual taxonomy until resolved. Unarmed is also outside the matrix (separate TN 8 assignment) — the system covers weapons only.

### 3.3a STR Minimums

Min STR = count of (Heavy, Long) axes. 1 below: −1D. 2+ below: cannot wield. Count the bits = STR min.

**N** ✓ **E** ✓ No table needed.

### 3.3b Weapon Modifier vs Armour Tier

Blades: +3/+6 scaling to +0 against heavy. Blunts: +3/+5 flat regardless.

**N** ✓ Blade/blunt distinction mechanized. **R** ⚠ "I need a mace against that knight" — intuitive strategic reasoning. However, **ED-131 (OPEN): values are unplaytested design-intent numbers.** Cannot confirm Robustness until simulation verifies lethality curves. Heavy Blade +6 vs None = potentially instant wound against End 4. **E** ✓ Blades linear decrease; blunts flat. Two rules.

### 3.3c Damage Formula

Damage = net hits + STR + weapon modifier. Critical (net ≥ 3): weapon modifier doubled.

**N** ✓ Three components: skill, power, weapon. **E** ✓ Addition chain. Crit doubles one value — same threshold as Overwhelming (net ≥ 3). Mechanical rhyme.

<!-- atom: valoria_master_document__14__3-4-armour | section_index: 14 | source_section: "3.4 Armour" -->


## 3.4 Armour

None/Light/Medium/Heavy. STR mins 0/2/3/4. Drain per action +0/+0/+1/+2. Wield constraint: Stamina cannot drop to ≤ 1.

**N** ✓ **R** ✓ Durability/mobility trade-off. **S** ⚠ Stamina interaction depends on ED-694 formula being canonical (End × 5 with armour as per-action drain modifier, not base Stamina reduction). Confirm.

<!-- atom: valoria_master_document__15__3-5-wound-system | section_index: 15 | source_section: "3.5 Wound System" -->


## 3.5 Wound System

Vitality = End × 10 + equip. Wound Interval = End + 6. Wounds = floor(cumulative_damage / interval). −1D/wound. Incapacitated at Vitality 0. No cap/hit. No reset. Multiple wounds from one hit possible.

**N** ✓ **R** ✓ Gradual degradation. **E** ✓ One formula. One penalty type. No severity categories. **S** ✓ ED-200/201 resolved all ambiguities.

<!-- atom: valoria_master_document__16__3-6-actions-14 | section_index: 16 | source_section: "3.6 Actions (14)" -->


## 3.6 Actions (14)

| Action | Key Rule | N |
|--------|----------|---|
| Strike | Standard Off vs Def → damage | ✓ |
| Feint (PP-294) | Commit N dice (min 3). Remainder to Def. Margin = dice opponent loses next round. Non-stacking. Floor 1D. | ✓ |
| Full Guard | All Def. Mass Mismatch exempt. | ✓ |
| Escape (PP-634) | Agi TN 7 Ob 1. Contested if pursued. Partial = exit + free strike. | ✓ |
| Take a Breath | Restore Stamina. Cannot in melee. | ✓ |
| Rescue (PP-285/406/407) | N Off dice contest attacker. Win: redirect, +2 Momentum if struck. Fail: +1 Momentum if wounded. Chain block. | ✓ |
| Disarm | Off vs (STR+Agi) as Ob. | ✓ |
| Dodge | Full pool Def vs one ranged attack. Forfeit Off. | ✓ |
| Tie Up | Both −2D. Blocks Escape. | ✓ (marginal but enables Escape-blocking) |
| Retrieve | Post-Disarm pickup. | ✓ (conditional) |
| Establish Distance | Range management. | ✓ |
| Stunt | +1D to +5D environmental. | ✓ |
| Desperate Strike | Spend 2 Stamina, +bonus Off. | ✓ |
| Parry | Spend 1 Stamina, +1D Def. | ✓ |

⚠ **STALE-03: PP-238 vs PP-294 (Feint).** PP-238 says full pool to Off, Def = 0. PP-294 says partial commitment (min 3) with remainder to Def. PP-294 is more recent and more detailed. **Strike PP-238.**

⚠ Rescue is the most complex single action (6 sub-rules). Approaching per-action ceiling. Manageable.

<!-- atom: valoria_master_document__17__3-7-fibonacci-group-bonus | section_index: 17 | source_section: "3.7 Fibonacci Group Bonus" -->


## 3.7 Fibonacci Group Bonus

2v1: +1D, 3v1: +2D, 4–5v1: +3D, 6–7v1: +4D, 8+: +5D. Offence only.

**N** ✓ **R** ✓ Diminishing returns prevent mob-stacking. **E** ✓ 6-entry lookup.

<!-- atom: valoria_master_document__18__3-8-mass-mismatch | section_index: 18 | source_section: "3.8 Mass Mismatch" -->


## 3.8 Mass Mismatch

Light vs Heavy attacker: defensive successes −1 (min 0). Exempt: Full Guard only.

**N** ✓ **E** ✓ One rule. One exemption.

<!-- atom: valoria_master_document__19__3-9-ranged-combat | section_index: 19 | source_section: "3.9 Ranged Combat" -->


## 3.9 Ranged Combat

Cannot fire at melee range. Cover: Soft (+DR) / Hard (blocks). Terrain closing: 1–3 rounds. Reload (HP crossbow): full round.

**S** ⚠ Ranged DR uses a separate table from melee weapon-mod-vs-armour. Two mental models for "how armour works." Godot should unify into single armour resolution function with weapon-type dispatch.

---

# 4. SOCIAL CONTEST

<!-- atom: valoria_master_document__20__4-1-adjudicator-pool-rotation | section_index: 20 | source_section: "4.1 Adjudicator → Pool Rotation" -->


## 4.1 Adjudicator → Pool Rotation

Expert Judge → Cognition. Crowd → Charisma. No Adjudicator → Attunement.

**N** ✓ Prevents single-stat social dominance. **R** ✓ Venue selection = strategic. **E** ✓ Three categories, direct mapping.

<!-- atom: valoria_master_document__21__4-2-styles-2-2 | section_index: 21 | source_section: "4.2 Styles (2×2)" -->


## 4.2 Styles (2×2)

Precedent (Memory+Revealing) / Suppression (Memory+Obscuring) / Vision (Projection+Revealing) / Insinuation (Projection+Obscuring).

**N** ✓ **R** ✓ Maps to NPC Resonant Style vulnerabilities. **E** ✓ 2×2 matrix. Self-explanatory labels.

<!-- atom: valoria_master_document__22__4-3-interaction-types | section_index: 22 | source_section: "4.3 Interaction Types" -->


## 4.3 Interaction Types

Clash (same genre, opposite orientation) / Reinforce (same genre, same) / Cross (different genres) / Tie (equal successes).

**N** ✓ **R** ⚠ **ED-295 (OPEN, P1-BLOCKER):** CLASH stalls at median. `floor(margin × modifiers − resistance)` = 0 movement when margin barely exceeds resistance. Two evenly-matched debaters with 10D pools regularly produce margin 1–2; after resistance subtraction and flooring, movement = 0. The contest system's primary interaction type produces null outcomes in its most common use case. **This is a functional failure, not a flag.** Resolution defaults to Composure/Concentration attrition, making the CT track vestigial for matched opponents.

⚠ **ED-297 (OPEN):** AMPLIFY (coalition) dominates CLASH (solo) at ~5 movement/exchange vs ~0. **DECISION-07:** Intentional (rewarding alliances) or rebalance?

<!-- atom: valoria_master_document__23__4-4-conviction-track-0-10 | section_index: 23 | source_section: "4.4 Conviction Track (0–10)" -->


## 4.4 Conviction Track (0–10)

Win ≥ 7 / ≤ 3. Compromise 4–6. Start GM-set. Resistance = avg Stability − 1, min 0.

**N** ✓ Three outcomes. **E** ✓ 11 values, two thresholds, one zone.

<!-- atom: valoria_master_document__24__4-5-composure-concentration | section_index: 24 | source_section: "4.5 Composure / Concentration" -->


## 4.5 Composure / Concentration

Composure = Cha × 3. Strain ≥ Composure → Rattled (+1 Ob). 2 marks = social incapacitation.
Concentration = Foc + Rec. −1/exchange, −1 on loss. At 0: Spent (−2D, opponent +1D). Resets.

**N** ✓ Dual resource mirrors Vitality/Stamina. **R** ✓ Rattled = permanent degradation; Spent = cyclical spike. **E** ✓ **S** ✓ Knot buffer redirects strain — mechanizes emotional support.

<!-- atom: valoria_master_document__27__5-2-three-axis-ob | section_index: 27 | source_section: "5.2 Three-Axis Ob" -->


## 5.2 Three-Axis Ob

Total Ob = Depth + Breadth + Distance. All additive.

**Depth (Fibonacci):** Object 1, Personal 2, Relational 3, Field 5, Structural 8, Foundational 13. TS gates (30/50/70/90). Mending Ob = Depth − 1.

**Breadth (Linear):** Single 0, Small group 1, Formation 2, Battlefield 3, Regional 4. Each step ≈ 10× scope.

**Distance (Linear + TS gates):** Contact 0, Near 1, Distant 2, Far 3. Same TS tier gates as Depth.

**N** ✓ **R** ✓ TS gates create hard access tiers. **E** ✓ Fibonacci depth is mathematically motivated. Breadth/Distance are linear. **S** ✓ A Relational-Formation-Distant operation = Ob 3+2+2 = 7. Even Edeyja struggles.

<!-- atom: valoria_master_document__28__5-3-operations | section_index: 28 | source_section: "5.3 Operations" -->


## 5.3 Operations

Standard (TN 7): Weaving, Pulling, Mending, Community Weaving. Binding (TN 8): Locking, Dissolution. POP (TN 8/9). Mending immune to opposition — prevents repair-counter paradox.

**N** ✓ Six ops: repair/preserve/open/freeze/destroy/temporal. **E** ✓ Three TN tiers, three risk categories.

<!-- atom: valoria_master_document__29__5-4-opposing-operations-pp-653 | section_index: 29 | source_section: "5.4 Opposing Operations (PP-653)" -->


## 5.4 Opposing Operations (PP-653)

Pairs: Weave/Pull, Lock/Dissolution, Lock/Pull, Weave/Dissolution. Engagement modifier: +floor(opponent TPS/2), min +1. N-way (3+): all fail, Gap forms, RS −(2×n). Prevents dogpiling.

**E** ⚠ Resolution table has 6 outcomes with 3–4 consequences each. Most complex table in the game. Manageable for TTRPG; requires careful Godot implementation.

<!-- atom: valoria_master_document__30__5-5-gap-self-closure | section_index: 30 | source_section: "5.5 Gap Self-Closure" -->


## 5.5 Gap Self-Closure

Object 1 season (0 RS drain). Relational 2 (1/season). Field 4 (2). Structural 8 (3). Foundational 32 (5). Scale hierarchy: must Mend deepest first.

**N** ✓ Reality self-heals. **R** ✓ Structural Gap = 24 total RS damage if unrepaired (40% of starting RS). Real stakes. **E** ✓ Doubling pattern.

<!-- atom: valoria_master_document__31__5-6-substrate-saturation-counter-pp-606 | section_index: 31 | source_section: "5.6 Substrate Saturation Counter (PP-606)" -->


## 5.6 Substrate Saturation Counter (PP-606)

≥3 ops/battle turn → +1 Ob/+1 Coherence (cap +2). Counter ≥ 3 → +2 Ob rest of battle. ≥3 at end → RS −1 at Accounting. Hard cap −1/battle. Replaces old ×3 multiplier.

**N** ✓ **E** ✓ Counter. Threshold. Two penalty tiers.

<!-- atom: valoria_master_document__32__5-7-knots-pp-632 | section_index: 32 | source_section: "5.7 Knots (PP-632)" -->


## 5.7 Knots (PP-632)

Pool = (Bonds × 2) + 3. Close 5 / Medium 2 / Loose 1. Max = floor(Bonds/2)+1. Rupture: Disp → −4, Composure damage. Loss: Coherence −1. Simultaneous Rupture cap (PP-633): ≤ 75% Composure.

**N** ✓ Mechanizes relationships as ontological structures. Any character — TS not required. **R** ✓ Three tiers with distinct mechanical benefits. **E** ✓ One pool, three tiers, one cap.

<!-- atom: valoria_master_document__34__5-9-dissonance-pp-607-610 | section_index: 34 | source_section: "5.9 Dissonance (PP-607/610)" -->


## 5.9 Dissonance (PP-607/610)

Spirit TN 7 vs Factor (1–4). Failure: −1D Spirit (scene/season). TS 30+ on Success: Discovery Event.

**N** ✓ **R** ✓ Dual outcome (harm/discovery from same stimulus).

<!-- atom: valoria_master_document__37__6-2-fieldwork-pool-and-attribute-rotation | section_index: 37 | source_section: "6.2 Fieldwork Pool and Attribute Rotation" -->


## 6.2 Fieldwork Pool and Attribute Rotation

Pool = (Primary Attr × 2) + H + 3. TN 6/7/8. 12 sub-types using 7 different attributes (Cog, Att, End, Rec, Spi, Bon, Cha). No dump stats — every attribute has fieldwork utility.

<!-- atom: valoria_master_document__38__6-3-evidence-track | section_index: 38 | source_section: "6.3 Evidence Track" -->


## 6.3 Evidence Track

Progress clock: 0 → threshold (Simple 3 / Complex 5 / Structural 8). Persistent across scenes/sessions. One track per investigation regardless of territory. Progress by degree: Failure +0/+2 Exp, Partial +1/+1, Success +2/+0, OW +3/−1.

**R** ✓ **Exposure is the investigation cost.** Even success accumulates Exposure. Only OW reduces it.

### 6.3a Reconstruct

At threshold: Ob = 1. Failure = plausible but WRONG conclusion (GM doesn't reveal error). Partial = correct "what," incomplete "why." Success = full picture. OW = full picture + implication.

**R** ✓ **Wrong-conclusion-on-failure is outstanding.** Creates genuine epistemic uncertainty — the player must decide whether to trust their investigation or keep digging.

### 6.3b Desperate Trail

After 3 consecutive failures: TN → 8. Clears on Success or season change.

**N** ✓ Prevents stalling. **E** ✓ One rule. One clear condition.

<!-- atom: valoria_master_document__39__6-4-socializing-disposition | section_index: 39 | source_section: "6.4 Socializing / Disposition" -->


## 6.4 Socializing / Disposition

Range −3 to +5. Ceiling = Bonds (PP-684). 7 action types (Read, Converse, Connect, Impress, Rumour, Negotiate, Gift/Bribe).

**R** ✓ Bonds cap forces relational investment. Sincerity Gate (Spirit TN 7 Ob 1, 37% failure at Spirit 3) prevents transactional relationship farming.

### 6.4a Information Gates (Parallel Access)

| Method | D0 | D1 | D2 | D3 | D4 |
|--------|----|----|----|----|-----|
| Exploration | Auto | Cog ≥ 2 | Cog ≥ 3 | TS ≥ 10 | TS ≥ 30 |
| Investigation | Auto | Ob 1 | Ob 2 | Ob 3 + TS ≥ 10 | Ob 5 + TS ≥ 30 |
| Socializing | Any Disp | Disp +1 | Disp +2 | Disp +3 | Disp +4 |

Three routes to the same information. Each with different costs.

<!-- atom: valoria_master_document__40__6-5-exposure-system | section_index: 40 | source_section: "6.5 Exposure System" -->


## 6.5 Exposure System

Cover = Cog + most relevant History. Determines Noticed/Watched/Compromised thresholds (Cover 3: thresholds 3/5/7; Cover 12+: 8/10/12). Per-territory. Resets on season change or territory exit. Watched → +1 Church Attention Pool.

**R** ✓ Cover 3 = detected in 3 scenes. Cover 9 = full season. Cover 12+ = near-immune.

<!-- atom: valoria_master_document__41__6-6-rendering-strain-depth-3 | section_index: 41 | source_section: "6.6 Rendering Strain (Depth 3+)" -->


## 6.6 Rendering Strain (Depth 3+)

Depth 3 (Remnant): minor. TS < 10: vague unease. Certainty pressure.
Depth 4 (Anomaly): Coherence check Ob 1. Failure: Coherence −1. Certainty −1 if ≥ 3.
Depth 5 (Breach): Coherence −1 automatic. Certainty forced ≤ 2. TS +1 permanent.

**R** ✓ **Breach as simultaneous cost and benefit:** Coherence −1 but TS +1 permanent. The rendering breaks but expands. Beautiful risk/reward.

<!-- atom: valoria_master_document__43__7-1-core-formula-pp-233 | section_index: 43 | source_section: "7.1 Core Formula (PP-233)" -->


## 7.1 Core Formula (PP-233)

Pool = min(Size, Command) + Command. H = min(Discipline, Command) + DR. Total Health = Size × H. Damage/success = 1 + Power. Simultaneous damage.

**N** ✓ **R** ✓ **Command caps both pool and Health contributions — generalship dominates.** Size 6 + Command 3 → 6D, not 9D. Correct asymmetry. **E** ⚠ Double `min()` creates non-obvious behavior. Large units with bad generals: durable but ineffective. Correct but needs clear documentation. **S** ✓ Simultaneous damage prevents first-mover advantage.

<!-- atom: valoria_master_document__45__7-3-key-mechanics | section_index: 45 | source_section: "7.3 Key Mechanics" -->


## 7.3 Key Mechanics

**Discipline Degradation (PP-251):** Fires when BOTH: Size loss > Discipline AND this unit's loss > opponent's by ≥ 1. Symmetric = no trigger. Asymmetry mechanic, not attrition.

**Morale:** Range 1–7. Floor 1 (general present). At 0: rout. Cap −3/Cascade (general death uncapped). Contagion −1 adjacent (no cascade).

**Formations:** Line, Shield Wall (−1D Off/+2D Def), Wedge (+2D Off/−1D Def), Skirmish, Column, Reserve. ⚠ **DECISION-08:** SW +2D Def on ALL sides including flanks. Historically wrong. Consider flanking negation?

**Splitting (PP-508):** Dominates concentration +9% to +45%. Counters: Narrow Pass, Feigned Retreat. ⚠ **DECISION-09:** Verify map provides sufficient terrain counter-play (≥ 40% of locations).

<!-- atom: valoria_master_document__46__7-4-provisional-count | section_index: 46 | source_section: "7.4 PROVISIONAL Count" -->


## 7.4 PROVISIONAL Count

**14 PROVISIONAL items** — most of any system. These span Volley TN (ranged damage output), Discipline triggers (attrition dynamics), Shield Wall scope (defensive meta), and Commander bonus formulas. Changing any one changes system behavior. **S** ✗ The system is designedly incomplete — it cannot be rated smooth. Implementation must treat all 14 as configurable parameters. Focused canonicalization pass required before Godot implementation.

---

# 8. SCENE CONTAINERS

<!-- atom: valoria_master_document__48__8-2-scene-lifecycle | section_index: 48 | source_section: "8.2 Scene Lifecycle" -->


## 8.2 Scene Lifecycle

1. **Entry** — triggered by player action, NPC, world event, or Scene Slate
2. **Resolution** — one of the mechanics above
3. **Consequences** — stat changes, track advances, Exposure, Disposition
4. **Domain Echo check** — Sufficient Scope? If yes → faction stat change
5. **Transition** — to next scene, Accounting, or scale shift

⚠ **GAP-01: Scene Lifecycle not formally codified.** These five steps are implicit across documents but never stated as a unified model. For Godot: create a SceneLifecycle class.

<!-- atom: valoria_master_document__49__8-3-scene-budget-and-scene-slate | section_index: 49 | source_section: "8.3 Scene Budget and Scene Slate" -->


## 8.3 Scene Budget and Scene Slate

Hybrid mode: 2–3 personal scenes/season (Personal Phase). Priority 0 (mandatory): Settlement Revolt, Heresy Investigation, Faction Leader Removal, Mass Battle at Settlement, Companion Arc, Knot Crisis, Stability Crisis, Rank Advancement. Priority 1 (optional): Clock Band Transition, NPC Conviction Crisis, Treaty events, Territory Control Change, Warden Emergency. Overflow: NPC AI handles excess mandatory scenes with reduced player influence.

**"Where Were You?" retrospective scenes** (§4.4): Free narrative moment for major events the player missed. No action cost. Player experiences emotional weight and decides response.

⚠ **GAP-02:** "Where Were You?" implementation is thin — what does the player DO in this scene? Is there a roll? Needs more definition for Godot.

---

# 9. DOMAIN ACTIONS AND FACTION LAYER

<!-- atom: valoria_master_document__50__9-1-card-hand-economy | section_index: 50 | source_section: "9.1 Card-Hand Economy" -->


## 9.1 Card-Hand Economy

6 cards (5 action + 1 Recess). Play 1/season. Domain Expertise +1D on faction specialty card. Each faction's hand defines their strategic identity: Crown 2× Legionary, Church 2× Senator, Hafenmark 2× Consul, Varfell 2× Tribune, RM 2× Praetor.

**N** ✓ **R** ✓ Hand composition IS faction nature. **E** ✓ Play 1. Resolve 1.

<!-- atom: valoria_master_document__51__9-2-action-ob-formulas | section_index: 51 | source_section: "9.2 Action Ob Formulas" -->


## 9.2 Action Ob Formulas

Most common pattern: floor(stat/2)+1. All use TN 7. Same degree table as personal scale.

Key actions: Muster Ob 2. March no roll. Govern floor(Prosperity/2)+1. Trade floor(Prosperity/2)+1. Diplomacy floor(NPC Stability/2)+1. Survey (5−Proximity)+1. Investigate Ob 2. Spy floor(Intel/2)+1. Community Weaving (100−MS)÷20. All floors 1.

**E** ✓ Consistent formula structure. **S** ✓ Ob formulas derive from game state — dynamic difficulty as world changes.

<!-- atom: valoria_master_document__53__9-4-faction-starting-stats | section_index: 53 | source_section: "9.4 Faction Starting Stats" -->


## 9.4 Faction Starting Stats

Crown 22 total / Church 25 / Hafenmark 20 / Varfell 20 / RM none (statless). Ceilings: M 0–7, I 1–7, W 0–7, Mil 0–7, S 0–7.

⚠ **STALE-04: params/bg/core.md Faction Assignment table duplicated.** Formatting error.

<!-- atom: valoria_master_document__54__9-5-global-tracks | section_index: 54 | source_section: "9.5 Global Tracks" -->


## 9.5 Global Tracks

MS 72 (Rupture at 0). CI 28 (Seizure at 60, Mass Seizure at 100). IP 20 (Vanguard at 75, three-phase invasion). PI 7 (Crown elim at 20). Löwenritter Graduated Autonomy (Loyal→Restless→Autonomous→Split).

<!-- atom: valoria_master_document__55__9-6-accord-0-3-per-territory | section_index: 55 | source_section: "9.6 Accord (0–3, per territory)" -->


## 9.6 Accord (0–3, per territory)

Aligned 3 / Compliant 2 / Resistant 1 / Revolt 0. Province Accord = floor(average settlement Order). Accord ≥ 2 required for TCV.

<!-- atom: valoria_master_document__56__9-7-peninsular-strain-0-10 | section_index: 56 | source_section: "9.7 Turmoil (0–10)" -->


## 9.7 Turmoil (0–10)

Peace 0–2 / Tension 3–4 (Mandate check) / Fracture 5–6 (Accord −1 one territory) / Crisis 7–8 (Accord −1 ALL non-capital, Mandate Ob 2) / Collapse 9–10 (Accord cap 2, Mandate Ob 3, MS −1/season). Decay −1/peaceful season.

**R** ✓ **THE anti-war mechanic.** At Crisis, ALL factions lose Accord in ALL non-capital territories.

---

# 10. SCALE TRANSITIONS AND DOMAIN ECHO

<!-- atom: valoria_master_document__59__10-3-zoom-in-zoom-out | section_index: 59 | source_section: "10.3 Zoom In / Zoom Out" -->


## 10.3 Zoom In / Zoom Out

**Zoom In:** BG → Personal. Legal entry: after Phase 1/3/6.1. BG degree → Ob modifier (Failure +1, Success −1, OW −2). **Zoom Out:** Personal → BG. State transfer via Echo. Phase 6 continues with updated state.

**Mandatory triggers (8):** Cannot be declined. **Optional triggers (5):** Presented but declinable. Scene budget overflow: NPC AI handles excess.

---

# 11. SEASONAL CONTAINER AND ACCOUNTING

<!-- atom: valoria_master_document__61__11-2-hybrid-phase-structure | section_index: 61 | source_section: "11.2 Hybrid Phase Structure" -->


## 11.2 Hybrid Phase Structure

Strategic Phase (BG Domain Actions) → Personal Phase (2–3 scenes). BG degree feeds Personal Phase as Fieldwork Offset. Domain Echoes from Personal Phase queue to Accounting.

---

# 12. WORLD-STATE MECHANICS

<!-- atom: valoria_master_document__63__12-2-ci-church-influence | section_index: 63 | source_section: "12.2 CI (Church Influence)" -->


## 12.2 CI (Church Influence)

Range 0–100. Start 28. Seizure at 60 (one-shot). Seven-step Accounting formula: Conditional Passive (0/+1/+2 by prominence count) → Piety Yield → Charity Advantage → Templar Presence → Assert → Suppress → Baralta. Cap ±5/season.

**R** ✓ Seven sources each attackable at different points. No single counter shuts CI down; multiple collectively can.

<!-- atom: valoria_master_document__64__12-3-ip-invasion-pressure | section_index: 64 | source_section: "12.3 IP (Invasion Pressure)" -->


## 12.3 IP (Invasion Pressure)

Range 0–100. Start 20. Three-phase invasion (100/85/80 sustained). Three repulsion paths (military OW ×2, diplomatic Elske Loyalty ≥ 6, resistance Underground Network). Permanent resolution possible.

**R** ✓ Three repulsion paths = three factional approaches to the same external threat.

<!-- atom: valoria_master_document__65__12-4-pi-parliament-integrity | section_index: 65 | source_section: "12.4 PI (Parliament Integrity)" -->


## 12.4 PI (Parliament Integrity)

Range 0–20. Start 7. Crown elimination at 20. Anti-Crown pressure meter.

<!-- atom: valoria_master_document__67__13-1-universal-victory-peninsular-sovereignty | section_index: 67 | source_section: "13.1 Universal Victory — Peninsular Sovereignty" -->


## 13.1 Universal Victory — Peninsular Sovereignty

All 15 territories + Accord ≥ 2 + Strain ≤ 6, held 2 consecutive Accountings. Effective hegemony (Treaty-bound, Submitted, institutionally dominated) counts.

**R** ✓ Three simultaneous requirements prevent pure military steamrolling. 2-consecutive hold prevents flash wins.

<!-- atom: valoria_master_document__68__13-2-faction-toolkits-not-alternate-endpoints | section_index: 68 | source_section: "13.2 Faction Toolkits (NOT Alternate Endpoints)" -->


## 13.2 Faction Toolkits (NOT Alternate Endpoints)

**Crown:** Treaty + rival suppression. Crown Treaty (PP-512–523) = most detailed single action.
**Church:** Mass Seizure (one-shot). P(declare) = ((CI−60)/40)^3.3. Pool = Influence + floor(CI/15). Ob = 10 − PT − infrastructure.
**Hafenmark:** Dynastic Assertion. PV ≥ 13 + PI ≥ 5 + Crown Mandate ≤ 3.
**Varfell:** Path A (Intelligence Hegemony) or Path B (Southernmost Dominion, WR ≥ 3, Season ≥ 12).
**RM:** Two-phase Cultural Revolution. PT ≤ 1 in ≥ 4 territories → Cultural Uprising of T9 (one roll, Ob = CI/10).
**Löwenritter:** Regency Establishment (successor confirmed) or Military Consolidation (8 seasons without confirmation).

**R** ✓ Church Mass Seizure is the game's best single mechanic: years of preparation for one decisive moment. Exponential declaration probability models institutional restraint perfectly.

<!-- atom: valoria_master_document__69__13-3-co-victory-6-pairings | section_index: 69 | source_section: "13.3 Co-Victory (6 Pairings)" -->


## 13.3 Co-Victory (6 Pairings)

Crown+Hafenmark, Crown+Varfell, Varfell+RM, Hafenmark+RM, Löwenritter+Hafenmark, Church+Hafenmark (Partition). Incompatible: Crown+Church, Crown+Löwenritter, Church+Varfell, Church+RM.

Partition includes accept/reject prompt. Rejection = betrayal path — game's most emotionally complex ending.

<!-- atom: valoria_master_document__70__13-4-world-state-transitions | section_index: 70 | source_section: "13.4 World-State Transitions" -->


## 13.4 World-State Transitions

**MS=0 → Post-Calamity:** Acquisition suspended 3 seasons. Mending Echo doubled. Game continues — "No shared loss. No fade to black." True terminal: Second Calamity after 10 seasons at MS ≤ 5.

**IP=100 → Phased Invasion:** Three corridors. Three repulsion paths. Full repulsion permanently resolves threat. RM Presence → Underground Network 1:1 conversion.

**All Factions Dissolved → Anarchy:** Governance becomes direct. Founded Organizations claim territories. New faction formation possible.

---

# 14. SETTLEMENT LAYER

<!-- atom: valoria_master_document__71__14-1-architecture | section_index: 71 | source_section: "14.1 Architecture" -->


## 14.1 Architecture

17 provinces containing 36 authored settlements. Province = strategic layer. Settlement = personal layer. 8 types (Seat, City, Town, Fortress, Port, Cathedral, Mine, Outpost). 3 stats each (Prosperity/Defense/Order, 0–5). Province Accord = floor(average settlement Order).

**R** ✓ Accord EMERGES from governance rather than being set directly. Personal governance → strategic outcome.

<!-- atom: valoria_master_document__72__14-2-dual-authority-governance | section_index: 72 | source_section: "14.2 Dual-Authority Governance" -->


## 14.2 Dual-Authority Governance

Provincial Authority (faction) + Settlement Governor (NPC/player/subnational). Governor assignment gated by Standing (3+ for Town, 4+ for City/Fortress, 5+ for Seat). Four governance actions: Develop, Fortify, Pacify, Administer. Free governance action/season for player-governors.

<!-- atom: valoria_master_document__73__14-3-church-4-axis-infrastructure | section_index: 73 | source_section: "14.3 Church 4-Axis Infrastructure" -->


## 14.3 Church 4-Axis Infrastructure

Religious Building (None/Chapel/Church/Cathedral) × Templar Station × Inquisitor Base × Church Governor. Independent axes, not linear progression. Seizure Ob modifiers stack. Maximum −4 per settlement. Parish Social Services create the Geneva Trap: Church infrastructure helps secular governors while generating PT/CI.

**R** ✓ Pastoral Assumption (Church fills governance vacuums at Ob 1) creates incentive for secular factions to maintain governance — vacuums get filled by the Church. Historically accurate.

<!-- atom: valoria_master_document__74__14-4-faction-emergence-5-stages | section_index: 74 | source_section: "14.4 Faction Emergence (5 Stages)" -->


## 14.4 Faction Emergence (5 Stages)

Cell → Organization (2+ settlements) → Movement (4+ settlements, 2+ provinces) → Faction (full stat sheet) → Hegemon (2+ province Seats). Clear requirements per stage. Re-emergence pathway available for collapsed factions.

**R** ✓ **The bottom-up progression path.** No other game in this genre offers settlement-to-national-power progression.

<!-- atom: valoria_master_document__75__14-5-faction-collapse | section_index: 75 | source_section: "14.5 Faction Collapse" -->


## 14.5 Faction Collapse

Last province lost → city-state (partial stat sheet, one settlement). Full collapse only on leader death with no Standing 4+ successor. Factions contract, they don't vanish. Baralta losing all provinces but keeping Gransol = Duchess of Gransol, reduced but alive. Can rebuild.

<!-- atom: valoria_master_document__76__14-6-extended-timeline | section_index: 76 | source_section: "14.6 Extended Timeline" -->


## 14.6 Extended Timeline

Generational Shift clock (0–10, +1/5 years). TS ≥ 50 exempt (rendering sustains high-TS beings). IP rate halved for extended games. ⚠ **DECISION-10:** IP halving — mode-specific or global?

---

# 15. MILITARY LAYER

<!-- atom: valoria_master_document__77__15-1-unit-representation | section_index: 77 | source_section: "15.1 Unit Representation" -->


## 15.1 Unit Representation

4 stats: Type (fixed), Size (1–7, casualties), Discipline (1–7, degrades), Experience (0–2, upgrades Power). Military stat caps max Power and starting Discipline.

<!-- atom: valoria_master_document__78__15-2-muster | section_index: 78 | source_section: "15.2 Muster" -->


## 15.2 Muster

Size = 2 (base) + Prosperity modifier (0/+1/+2). Power = floor(Military/2)+1. Prerequisites gate by Prosperity, Wealth, officer proficiency. On Muster success + Wealth failure: downgrade to Light Infantry.

<!-- atom: valoria_master_document__79__15-3-tc-competitive-formula | section_index: 79 | source_section: "15.3 TC Competitive Formula" -->


## 15.3 TC Competitive Formula

PP-402 (unconditional passive +1/season) repealed. Seven-step formula: Conditional Passive → Piety Yield → Charity Advantage → Templar Presence → Assert → Suppress → Baralta. Cap ±5/season.

**R** ✓ Church must EARN CI through active institutional maintenance. **E** ⚠ Seven steps dense for human play. Godot: automated breakdown screen.

<!-- atom: valoria_master_document__80__15-4-accord-military | section_index: 80 | source_section: "15.4 Accord → Military" -->


## 15.4 Accord → Military

Accord 3: +1D defender. Accord 1: Martial −1, Levy-only Muster. Accord 0: no offensive use, no Muster.

<!-- atom: valoria_master_document__81__15-5-siege-ed-633 | section_index: 81 | source_section: "15.5 Siege (ED-633)" -->


## 15.5 Siege (ED-633)

Legionary Inward + unit adjacent. Ob = 2 + Fort Level. OW: Fort −2. Cap 5 seasons. RS −1/season.

---

# 16. NPC BEHAVIOR SYSTEM

<!-- atom: valoria_master_document__83__16-2-named-npc-profiles-12-core | section_index: 83 | source_section: "16.2 Named NPC Profiles (12 core)" -->


## 16.2 Named NPC Profiles (12 core)

| NPC | Faction | Primary Conv | Secondary Conv | Primary RS | TS | Certainty |
|-----|---------|-------------|----------------|-----------|-----|-----------|
| Almud | Crown | Order | Reason | Consequence | 28 | 3 |
| Himlensendt | Church | Faith | Order | Evidence | 0 | 5 |
| Baralta | Hafenmark | Precedent | Faith | Evidence | 0 | 4 |
| Vaynard | Varfell | Reason | Autonomy | Consequence | 14 | 3 |
| Ehrenwall | Löwenritter | Order | Autonomy | Consequence | 0 | 4 |
| Vossen | RM | Equity | Continuity | Solidarity | 0 | 2 |
| Hann | RM | Equity | Autonomy | Consequence | 0 | 3 |
| Torben | Crown (heir) | Emergence window S1–8 | Autonomy | Solidarity | 0 | 4 |
| Edeyja | Wardens | Continuity | Reason | Evidence | 75–80 | 0 |
| Maret Uln | Varfell (succ.) | Equity | Reason | Evidence | 35 | 2 |
| Haelgrund | Ministry | Continuity | Precedent | Consequence | 12 | 4 |
| Guild Council | Guilds | Autonomy | — | Consequence | 0 | 4 |

**N** ✓ Every faction leader has a mechanically defined Stance Triangle. No NPC is "evil" — each is structurally positioned. **R** ✓ Each profile creates distinct decision patterns. Almud (Order+Reason, Consequence RS) will crack when shown the COST of maintaining order. Himlensendt (Faith+Order, Evidence RS) will crack when shown FACTS theology cannot dismiss. Baralta (Precedent+Faith, Evidence RS) will crack when shown her procedures FAILED. **E** ✓ Three attributes per NPC. Lookup table. **S** ✓ Profiles feed into Decision Procedure (§16.3), Priority Trees (§16.5), and Arc Profiles (§16.4).

### 16.2a Torben Emergence Window (ED-618)

First faction to reach Disposition ≥ +2 before Season 8 sets his primary Conviction. If none: defaults to Order. After S8: locked. Conviction determines Crown Priority Tree behavior if Torben becomes leader.

**R** ✓ **Torben is a contested narrative asset.** His Conviction is player-determined through relational investment, not authored. The S8 deadline creates urgency. The faction-specific outcomes create strategic consequences for the investment.

### 16.2b Inner Circle NPCs

Crown (5): Voss (Order/Authority), Reichard (Precedent/Evidence), Thale (Autonomy/Consequence), Linder (Faith/Authority), Kreutz (Order/Authority).
Hafenmark (2): Heljason (Precedent/Evidence), Geirson (Order/Consequence).
Varfell (2): Holdar (Continuity/Consequence), Stenskald (Community/Solidarity).
Church Cardinals (4): Fortitude (Faith+Order), Justice (Faith hardline), Prudence (Order+Autonomy), Temperance (Reason+Faith).

**N** ✓ Inner circle NPCs add depth to faction decision-making. Cardinals only activate independently during Church Stability ≤ 2 schism events — otherwise they follow Himlensendt. **S** ✓ Structurally Active — cannot be demoted below Passive tier while faction is in play.

<!-- atom: valoria_master_document__84__16-3-decision-procedure | section_index: 84 | source_section: "16.3 Decision Procedure" -->


## 16.3 Decision Procedure

### Step 1: Institutional Filter
Apply Ethical Framework Ob modifiers. For unnamed NPCs, this IS the decision.

### Step 2: Conviction Check
Named NPCs check if the decision contradicts their Conviction. If no contradiction → follow Framework.

### Step 3: Decision Fork
| Scar count | NPC chooses... |
|---|---|
| 0 | Conviction over Framework. Leadership Deviation Stability check. |
| 1 | Whichever Conviction the most recent Scar did NOT address. |
| ≥ 2 | GM uses Conviction Crisis table (d6). |
| Stability ≤ 1 | Autonomy regardless. |

**N** ✓ Three-step procedure handles all NPC decisions. **R** ✓ Scar count creates progressive unpredictability — fresh NPCs are institutional; scarred NPCs are personal. **E** ✓ Three steps. **S** ✓ Leadership Deviation links to faction Stability (Accounting).

<!-- atom: valoria_master_document__86__16-5-bg-priority-trees-all-factions | section_index: 86 | source_section: "16.5 BG Priority Trees (All Factions)" -->


## 16.5 BG Priority Trees (All Factions)

Standardized 7-level structure: Survival → Conviction-critical → Framework-aligned → Institutional Tendency → Secondary → Reactive → Pass.

Each faction's tree reflects their identity:
- **Crown:** Royal Decree, Treaty, garrison T2 when Varfell threatens, Torben Loyalty.
- **Church:** Heresy Investigation, Assert (TC), Piety Spread, Seizure at TC ≥ 75.
- **Hafenmark:** Sovereign Authority Doctrine, Suppress TC, Dynastic Proclamation, Constitutional responses only.
- **Varfell:** Private Collection, Tribune Investigate, March to T15 for Path B, no military first-strike.
- **Löwenritter:** Coup readiness, Sovereignty defense, full military response.
- **RM:** Community Organizing, Presence spread, no military response ever.
- **Guilds:** Economic Leverage, trade protection, no Conviction-critical tier.
- **Wardens:** Gap/Mending priority, assessment of new practitioners, absolute deterrence.

**N** ✓ Every NPC faction has a defined decision algorithm. No ambiguity in AI behavior. **R** ✓ Each tree produces faction-appropriate behavior across all game states. **E** ✓ 7-level template. Same structure all factions. **S** ✓ Priority Trees feed into Scene Slate (Outreach/Demand generation, §16.6).

<!-- atom: valoria_master_document__87__16-6-npc-outreach-demand-generation | section_index: 87 | source_section: "16.6 NPC Outreach / Demand Generation" -->


## 16.6 NPC Outreach / Demand Generation

Each season, NPCs evaluate whether to generate Scene Slate entries for the player. Outreach (Disp ≥ +2 + relevant Conviction + priority tree action). Demand (Disp ≤ −2 + institutional authority + hostile action). Volume cap: 3 Outreach + 2 Demand per season.

**N** ✓ **The World→Player bridge.** NPCs don't wait to be approached — they reach out. **R** ✓ Volume cap prevents inbox overload. Prioritization by Disposition/authority ensures the most relevant NPCs surface. **S** ✓ Subnational faction outreach (Guild, Ministry, RM, Warden) competes with national-level outreach for the same cap — natural tension between scales.

<!-- atom: valoria_master_document__88__16-7-npc-recruitment-pp-642 | section_index: 88 | source_section: "16.7 NPC Recruitment (PP-642)" -->


## 16.7 NPC Recruitment (PP-642)

Four-step: Identify (Disp +4/+5 = not recruitable) → Approach (Cha pool, Ob = floor(highest Disp / 2)+1) → Offer (one incentive, modifies Ob) → Resolution (Failure = faction warned; Partial = +1 Disp, retry −1 Ob; Success = joins; OW = joins + intel).

Hooks: Weak (−2 Ob, reusable on failure). Strong (Ob → 1, burned on failure + Mandate −2). Max one Hook per NPC.

Defection: Spirit TN 7, Ob = Disp toward recruiting faction. Fires from Priority Tree when belief-contradiction triggers. Not a player roll.

**N** ✓ NPC recruitment is a structured process with real stakes. **R** ✓ The +4/+5 loyalty gate prevents recruiting genuinely loyal NPCs. Strong Hook's failure consequence (burned + Mandate −2) creates real risk. **E** ✓ Four steps. Clear Ob formula. **S** ✓ Recruitment integrates with Disposition (fieldwork), Hooks (investigation/espionage), and Priority Trees (defection).

<!-- atom: valoria_master_document__89__16-8-heresy-jurisdiction-ed-670 | section_index: 89 | source_section: "16.8 Heresy Jurisdiction (ED-670)" -->


## 16.8 Heresy Jurisdiction (ED-670)

Jurisdiction varies by territory controller: Full in Church, permitted in Crown (with cooperation), blocked in Hafenmark (Sovereign Authority Doctrine), tolerated at +1 Ob in Varfell, none in Uncontrolled.

**N** ✓ Church authority is not universal — it depends on whose territory the heretic is in. **R** ✓ Creates strategic asylum mechanics — a heretic can flee to Hafenmark. **S** ✓ Integrates with Baralta's Categorical Imperative framework (no extra-constitutional Church authority).

<!-- atom: valoria_master_document__90__16-9-roster-tracking-pp-661 | section_index: 90 | source_section: "16.9 Roster Tracking (PP-661)" -->


## 16.9 Roster Tracking (PP-661)

Three tiers: Active (~35 cap, full state tracking), Passive (~30, compact), Background (unlimited, identity only). Demotion triggers: 4+ seasons off-screen, low Disposition inertia, faction removal. Inner circle structurally Active. Companion app display at each tier.

**N** ✓ Without roster management, NPC count grows unbounded. **E** ✓ Three tiers. Clear demotion rules. **S** ✓ Promotion/demotion is reversible. No permanent NPC loss from demotion.

---

# 17. CAMPAIGN ARC

<!-- atom: valoria_master_document__93__16-3-mending-community | section_index: 93 | source_section: "16.3 Mending Community" -->


## 16.3 Mending Community

MS recovery is cumulative across all active Menders. Spirit tiers (1–2 Journeyman, 3–4 Skilled, 5 Expert, 6 Master). MS budget creates the strategic calculus: enough Mending to survive, distributed across multiple practitioners and factions.

---

# 18. CROSS-SYSTEM ASSESSMENT

<!-- atom: valoria_master_document__94__20-1-formula-consistency | section_index: 94 | source_section: "20.1 Formula Consistency" -->


## 20.1 Formula Consistency

All pools: (Attr × 2) + H + 3. TN 6/7/8 everywhere. Ob 1–20 everywhere. Degree table universal. Pool floor 1D universal. Domain Echo same trigger/amount/cap everywhere. Clock paradigm consistent (increase/decrease/threshold) for MS, CI, IP, PI, Turmoil, Accord, Evidence Track, Exposure.

**The game has one resolution engine expressed at multiple scales.** This is the system's greatest architectural strength.

<!-- atom: valoria_master_document__95__20-2-the-complete-pipeline | section_index: 95 | source_section: "20.2 The Complete Pipeline" -->


## 20.2 The Complete Pipeline

```
Die Roll → Pool Split/Action → Scene Resolution → Consequences →
Domain Echo → Faction Stat Change → Accounting → Clock Advance →
Threshold Event → Scene Slate → Next Scene
```

Every step mechanically defined. No step requires undefined resolution. **Pipeline is complete.**

<!-- atom: valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items | section_index: 103 | source_section: "II.2 Open Decisions Requiring Jordan (16 items)" -->


## II.2 Open Decisions Requiring Jordan (16 items)

| # | ID | Issue | Priority |
|---|-----|-------|----------|
| DECISION-01 | — | TN 9 POP Binding near-impossibility — intentional? | Low |
| DECISION-02 | — | Spirit as practitioner tax — intentional? Spirit has 4 non-practitioner uses | Low |
| DECISION-03 | — | Certainty trigger asymmetry (6 toward 0 vs 3 toward 5) — intentional? | Low |
| DECISION-04 | ED-129 | Ranged weapon mapping to 3-axis or separate category | Medium |
| DECISION-05 | ED-131 | Weapon modifier values pending playtesting | Medium |
| DECISION-06 | ED-295 | **CLASH stalls at median — P1-BLOCKER** | **P1** |
| DECISION-07 | ED-297 | AMPLIFY dominance over CLASH — intentional? | Medium |
| DECISION-08 | — | Shield Wall flanking — should flanking negate +2D Def? | Low |
| DECISION-09 | PP-508 | Splitting dominance — sufficient terrain counter-play? | Medium |
| DECISION-10 | — | IP rate halving — mode-specific or global? | Low |
| DECISION-11 | ED-NEW-TC-01 | Conditional passive thresholds pending smoke-test | Deferred |
| DECISION-12 | — | Conviction taxonomy reducibility (9 → 7 universal + 2 specific?) | Low |
| DECISION-13 | — | Aggregate cognitive load target — what reference game? | Low |
| DECISION-14 | — | Evidence/positional bonus stacking (within or outside +5D cap?) | Medium |
| DECISION-15 | — | Crown Treaty lapse→re-sign cycling — intentionally unblocked? | Low |
| DECISION-16 | — | Certainty 3–4 dead zone — add minimal effects? | Low |

<!-- atom: valoria_master_document__106__ii-5-rating-corrections-applied | section_index: 106 | source_section: "II.5 Rating Corrections Applied" -->


## II.5 Rating Corrections Applied

| Item | Original | Corrected | Rationale |
|------|----------|-----------|-----------|
| §3.3b Weapon modifiers | R ✓ | R ⚠ | Unplaytested values (ED-131) |
| §4.3 Contest interactions | R ✓ | R ⚠ | CLASH stalls at median |
| §7 Mass Combat overall | S ⚠ | S ✗ | 14 PROVISIONAL = incomplete |
| §6.2 Fieldwork sub-types | E ✓ | E ⚠ | 12 sub-types = lookup demand |
| §11.1 Accounting | E ⚠ | E ✗ player / E ✓ engine | Split rating |
| §16.1a Conviction taxonomy | E ✓ | E ⚠ | Reducibility unexamined |

<!-- atom: valoria_master_document__107__ii-6-mechanics-flagged-for-removal | section_index: 107 | source_section: "II.6 Mechanics Flagged for Removal" -->


## II.6 Mechanics Flagged for Removal

**NONE.** All 14 combat actions, all NPC sub-systems, all faction toolkits remain necessary after stress-testing. Some are narrow (Disarm+Retrieve at ~20% relevance, Tie Up at ~5%) but each fills a tactical niche.

<!-- atom: valoria_master_document__112__iii-1-findings-register-14-items | section_index: 112 | source_section: "III.1 Findings Register (14 items)" -->


## III.1 Findings Register (14 items)

| # | Finding | Priority | Reliability |
|---|---------|----------|-------------|
| GX-09 | Domain Echo at ±1 may be below perceptual threshold | P1 | Math verified (floor function absorption); player-perception claim is extrapolation |
| GX-10 | ±1 modifier granularity below conscious perception | Medium | [TTRPG-FRAMING] In videogame, UI can display probabilities. Concern reduced. |
| GX-11 | Faction failure emotional weight investment-dependent | Medium | Hypothesis — depends on how faction identity is presented in implementation |
| GX-12 | Power moments exist in math, not presentation | P1 | Mechanically verified; presentation absence is a content design requirement |
| GX-13 | RM may be hardest to enjoy as single-player faction | Medium | [TTRPG-FRAMING partial] RM was designed for 5-player TTRPG. Single-player viability unverified. |
| GX-14 | Victory is confirmed, not experienced | P1 | True at design level — no victory ceremony specified. Implementation-fixable. |
| GX-15 | Strategic/personal split narrows audience | Low | Positioning observation, not flaw |
| GX-16 | Mid-campaign engagement valley (Season 5-12) | Medium-P1 | [TTRPG-FRAMING partial] Valley is real but spans ~3-6 hours of videogame play, not ~15. MS band transition at 60 is the designed valley-breaker. |
| WB-11 | Turmoil anti-war signal diffused across 4 causal links | Medium | Causal chain length verified; emotional consequence claim is extrapolation |
| WB-12 | NPC personality is presentation-dependent | P1 | Stance Triangle AI sophistication verified; player perception of personality requires authored content |
| WB-13 | Thread engagement geographically concentrated | Medium | Verified — TS gates + Thread location distribution support this |
| WB-14 | Philosophical depth needs mid-register vocabulary | Medium | Recommendation, not finding — depends on UI vocabulary choices |
| WB-15 | 6 emotional registers, none mechanically guaranteed | P1 | Generally true of any game — mechanics scaffold, presentation realizes |
| WB-16 | Hafenmark Parliament mechanically thin vs Church CI pipeline | Medium | Comparison verified; correctness of asymmetry is a design judgment |

<!-- atom: valoria_master_document__115__iii-4-claims-that-are-speculative-hypothesis-level | section_index: 115 | source_section: "III.4 Claims That Are Speculative/Hypothesis-Level" -->


## III.4 Claims That Are Speculative/Hypothesis-Level

These findings make claims about player behavior or audience response that cannot be verified from source documents:

- ±1 modifier perception thresholds (genre-comparative, not Valoria-specific)
- "Audience narrowness" estimates
- Engagement valley emotional impact
- RM playability as solo faction
- Faction failure emotional weight by player type

These are testable through playtesting. They are not verified findings.


---

# PART IV: ITEMS REQUIRING RE-VERIFICATION BEFORE ACTION

These findings should be checked against source before being used to drive design changes. They are flagged because they were generated under conditions of compressed context or recursive drift from source.

<!-- atom: valoria_master_document__117__iv-2-claims-i-cannot-currently-verify | section_index: 117 | source_section: "IV.2 Claims I Cannot Currently Verify" -->


## IV.2 Claims I Cannot Currently Verify

In late conversation turns I made specific quantitative claims without re-fetching source. These are flagged as unverified:

- "~9 tracked values per combat turn" — count derived from memory of params/combat.md
- "Mass combat fires 5 times across a 20-season campaign" — projection, not data
- "Mass combat documentation = ~20% of design corpus" — guess
- "Investigation completes in 3-5 seasons" — projection
- "Most Domain Action Ob formulas use floor(stat/2)+1" — pattern observation, not enumeration
- Specific battle-step counts (35-56 per battle) — calculated from memory of phase structure

If any of these drive a design decision, re-fetch the source first.

<!-- atom: valoria_master_document__118__iv-3-recursive-drift-risk | section_index: 118 | source_section: "IV.3 Recursive Drift Risk" -->


## IV.3 Recursive Drift Risk

Each audit pass referenced the prior audit's text rather than re-reading source. Inherited errors are possible. Specifically:

- The "intensified gameplay audit" extended themes from the "gameplay audit" which extended the "intensified mechanical audit" which audited the "mechanical audit." Four layers of self-reference.
- Findings in the gameplay audit cite section numbers from the mechanical review without re-checking that the cited content matches the citation.
- The throughline analysis (Part I §19) generated 8 meta-throughlines because the task asked for them. The reduction to 4 in Part II §II.10 was directional but not exhaustively re-justified.

**Recommendation:** Treat Parts II and III as a register for verification work. Parts I content closer to fetch-time is more reliable than late-conversation extrapolations.


---

# PART V: HANDOFF FOR UNREVIEWED SYSTEMS

The following systems were referenced but not atomically reviewed. They require separate NRES review against source documents before Godot implementation can be considered specified.

<!-- atom: valoria_master_document__121__v-3-derived-stats-gap-07 | section_index: 121 | source_section: "V.3 Derived Stats (GAP-07)" -->


## V.3 Derived Stats (GAP-07)

**Why it matters:** Treasury, Legitimacy, Reputation, Cohesion are videogame-layer values that translate faction stats into player-visible economic and political pressure. The economic throughline (T2, T10) is unverified without these.

**Sources to fetch:** `designs/architecture/derived_stats_v30.md` or equivalent.

**Review questions:**
- How is Treasury computed from Prosperity?
- How does Legitimacy interact with Mandate?
- What are Reputation effects? (NPC Disposition modifiers?)
- How does Cohesion derive from Discipline + Morale?
- Are these stats player-facing or engine-internal?

<!-- atom: valoria_master_document__122__v-4-caste-social-structure | section_index: 122 | source_section: "V.4 Caste / Social Structure" -->


## V.4 Caste / Social Structure

**Why it matters:** Listed in throughline connectivity but never reviewed. Caste system likely governs NPC Standing ceilings, social mobility, factional recruitment pools.

**Sources to fetch:** Search for `caste` or `social_structure` in design docs.

<!-- atom: valoria_master_document__123__v-5-royal-assassination-fuse | section_index: 123 | source_section: "V.5 Royal Assassination Fuse" -->


## V.5 Royal Assassination Fuse

**Why it matters:** Tension Card mechanic referenced in Almud Arcs D/E/F. Activation conditions, sub-roll probabilities, timing window (S8–S12). Campaign-altering mechanic gated behind a random draw.

**Sources to fetch:** Search for `tension_card`, `assassination_fuse`, or Almud arc D/E/F documents.

<!-- atom: valoria_master_document__124__v-6-other-likely-unreviewed-items | section_index: 124 | source_section: "V.6 Other Likely Unreviewed Items" -->


## V.6 Other Likely Unreviewed Items

These were inferred during the review but not directly examined:

- **Tension Cards in general** (the Royal Assassination Fuse is one example; the system as a whole may have multiple cards)
- **Subnational faction mechanics** (Guild, Ministry, Underground Network, RM cells) — referenced but not atomically reviewed
- **Tension Deck** (referenced in the conflict architecture proposal — fetched but only structurally reviewed)
- **POI templates** (referenced in settlement layer — types, generation rules)
- **Discovery Procedure** (exploration fieldwork sub-mechanic)
- **Conflict Architecture v30** (fetched but only structurally reviewed, not atomically)

---

# CONCLUDING NOTES

This master document is a record of session work. It is structured for navigation, but its findings are not all of equal reliability. The reliability disclosure at the start should be re-read before any single finding is acted on.

The work covered:
- 17 systems atomically reviewed (Part I)
- 10 stale references identified (Part II)
- 16 open decisions surfaced (Part II)
- 11 gaps identified (Part II)
- 17 PROVISIONAL items catalogued (Part II)
- 6 rating corrections applied (Part II)
- 14 gameplay/worldbuilding findings produced (Part III, with reliability flags)
- 4 genuinely emergent meta-throughlines identified (Part II)
- 5 systems flagged for separate review (Part V)
- Multiple TTRPG-vs-videogame framing errors identified and corrected (Part III)

The work did NOT cover:
- Verification of late-conversation quantitative claims against source
- Re-reading of source documents after the early fetches
- Playtesting of any finding
- Companion, Player Agency, Derived Stats, Caste, or Royal Assassination Fuse systems
- Implementation-layer specifications (UI, narrative generation, victory ceremony, NPC voice)

**End of master document.**

## Provenance

Atom-by-atom inventory in source/section order:

| atom_id | source | section_index | source_section | lines |
|---|---|---|---|---|
| `valoria_master_document__00__preamble` | `valoria_master_document.md` | 0 | (preamble) | 1 |
| `valoria_master_document__01__conversation-date-2026-04-24-to-2026-04-25-compile` | `valoria_master_document.md` | 1 | Conversation Date: 2026-04-24 to 2026-04-25 | Comp | 1 |
| `valoria_master_document__03__1-1-die-face-rule-d10` | `valoria_master_document.md` | 3 | 1.1 Die Face Rule (d10) | 15 |
| `valoria_master_document__05__1-3-obstacle-scale` | `valoria_master_document.md` | 5 | 1.3 Obstacle Scale | 6 |
| `valoria_master_document__06__1-4-degrees-of-success` | `valoria_master_document.md` | 6 | 1.4 Degrees of Success | 11 |
| `valoria_master_document__11__3-1-pool-split-off-def` | `valoria_master_document.md` | 11 | 3.1 Pool Split (Off/Def) | 6 |
| `valoria_master_document__12__3-2-initiative` | `valoria_master_document.md` | 12 | 3.2 Initiative | 6 |
| `valoria_master_document__13__3-3-weapon-system-3-binary-axes` | `valoria_master_document.md` | 13 | 3.3 Weapon System (3 Binary Axes) | 24 |
| `valoria_master_document__14__3-4-armour` | `valoria_master_document.md` | 14 | 3.4 Armour | 6 |
| `valoria_master_document__15__3-5-wound-system` | `valoria_master_document.md` | 15 | 3.5 Wound System | 6 |
| `valoria_master_document__16__3-6-actions-14` | `valoria_master_document.md` | 16 | 3.6 Actions (14) | 23 |
| `valoria_master_document__17__3-7-fibonacci-group-bonus` | `valoria_master_document.md` | 17 | 3.7 Fibonacci Group Bonus | 6 |
| `valoria_master_document__18__3-8-mass-mismatch` | `valoria_master_document.md` | 18 | 3.8 Mass Mismatch | 6 |
| `valoria_master_document__19__3-9-ranged-combat` | `valoria_master_document.md` | 19 | 3.9 Ranged Combat | 10 |
| `valoria_master_document__20__4-1-adjudicator-pool-rotation` | `valoria_master_document.md` | 20 | 4.1 Adjudicator → Pool Rotation | 6 |
| `valoria_master_document__21__4-2-styles-2-2` | `valoria_master_document.md` | 21 | 4.2 Styles (2×2) | 6 |
| `valoria_master_document__22__4-3-interaction-types` | `valoria_master_document.md` | 22 | 4.3 Interaction Types | 8 |
| `valoria_master_document__23__4-4-conviction-track-0-10` | `valoria_master_document.md` | 23 | 4.4 Conviction Track (0–10) | 6 |
| `valoria_master_document__24__4-5-composure-concentration` | `valoria_master_document.md` | 24 | 4.5 Composure / Concentration | 7 |
| `valoria_master_document__27__5-2-three-axis-ob` | `valoria_master_document.md` | 27 | 5.2 Three-Axis Ob | 12 |
| `valoria_master_document__28__5-3-operations` | `valoria_master_document.md` | 28 | 5.3 Operations | 6 |
| `valoria_master_document__29__5-4-opposing-operations-pp-653` | `valoria_master_document.md` | 29 | 5.4 Opposing Operations (PP-653) | 6 |
| `valoria_master_document__30__5-5-gap-self-closure` | `valoria_master_document.md` | 30 | 5.5 Gap Self-Closure | 6 |
| `valoria_master_document__31__5-6-substrate-saturation-counter-pp-606` | `valoria_master_document.md` | 31 | 5.6 Substrate Saturation Counter (PP-606) | 6 |
| `valoria_master_document__32__5-7-knots-pp-632` | `valoria_master_document.md` | 32 | 5.7 Knots (PP-632) | 6 |
| `valoria_master_document__34__5-9-dissonance-pp-607-610` | `valoria_master_document.md` | 34 | 5.9 Dissonance (PP-607/610) | 6 |
| `valoria_master_document__37__6-2-fieldwork-pool-and-attribute-rotation` | `valoria_master_document.md` | 37 | 6.2 Fieldwork Pool and Attribute Rotation | 4 |
| `valoria_master_document__38__6-3-evidence-track` | `valoria_master_document.md` | 38 | 6.3 Evidence Track | 18 |
| `valoria_master_document__39__6-4-socializing-disposition` | `valoria_master_document.md` | 39 | 6.4 Socializing / Disposition | 16 |
| `valoria_master_document__40__6-5-exposure-system` | `valoria_master_document.md` | 40 | 6.5 Exposure System | 6 |
| `valoria_master_document__41__6-6-rendering-strain-depth-3` | `valoria_master_document.md` | 41 | 6.6 Rendering Strain (Depth 3+) | 8 |
| `valoria_master_document__43__7-1-core-formula-pp-233` | `valoria_master_document.md` | 43 | 7.1 Core Formula (PP-233) | 6 |
| `valoria_master_document__45__7-3-key-mechanics` | `valoria_master_document.md` | 45 | 7.3 Key Mechanics | 10 |
| `valoria_master_document__46__7-4-provisional-count` | `valoria_master_document.md` | 46 | 7.4 PROVISIONAL Count | 8 |
| `valoria_master_document__48__8-2-scene-lifecycle` | `valoria_master_document.md` | 48 | 8.2 Scene Lifecycle | 10 |
| `valoria_master_document__49__8-3-scene-budget-and-scene-slate` | `valoria_master_document.md` | 49 | 8.3 Scene Budget and Scene Slate | 12 |
| `valoria_master_document__50__9-1-card-hand-economy` | `valoria_master_document.md` | 50 | 9.1 Card-Hand Economy | 6 |
| `valoria_master_document__51__9-2-action-ob-formulas` | `valoria_master_document.md` | 51 | 9.2 Action Ob Formulas | 8 |
| `valoria_master_document__53__9-4-faction-starting-stats` | `valoria_master_document.md` | 53 | 9.4 Faction Starting Stats | 6 |
| `valoria_master_document__54__9-5-global-tracks` | `valoria_master_document.md` | 54 | 9.5 Global Tracks | 4 |
| `valoria_master_document__55__9-6-accord-0-3-per-territory` | `valoria_master_document.md` | 55 | 9.6 Accord (0–3, per territory) | 4 |
| `valoria_master_document__56__9-7-peninsular-strain-0-10` | `valoria_master_document.md` | 56 | 9.7 Turmoil (0–10) | 10 |
| `valoria_master_document__59__10-3-zoom-in-zoom-out` | `valoria_master_document.md` | 59 | 10.3 Zoom In / Zoom Out | 10 |
| `valoria_master_document__61__11-2-hybrid-phase-structure` | `valoria_master_document.md` | 61 | 11.2 Hybrid Phase Structure | 8 |
| `valoria_master_document__63__12-2-ci-church-influence` | `valoria_master_document.md` | 63 | 12.2 CI (Church Influence) | 6 |
| `valoria_master_document__64__12-3-ip-invasion-pressure` | `valoria_master_document.md` | 64 | 12.3 IP (Invasion Pressure) | 6 |
| `valoria_master_document__65__12-4-pi-parliament-integrity` | `valoria_master_document.md` | 65 | 12.4 PI (Parliament Integrity) | 4 |
| `valoria_master_document__67__13-1-universal-victory-peninsular-sovereignty` | `valoria_master_document.md` | 67 | 13.1 Universal Victory — Peninsular Sovereignty | 6 |
| `valoria_master_document__68__13-2-faction-toolkits-not-alternate-endpoints` | `valoria_master_document.md` | 68 | 13.2 Faction Toolkits (NOT Alternate Endpoints) | 11 |
| `valoria_master_document__69__13-3-co-victory-6-pairings` | `valoria_master_document.md` | 69 | 13.3 Co-Victory (6 Pairings) | 6 |
| `valoria_master_document__70__13-4-world-state-transitions` | `valoria_master_document.md` | 70 | 13.4 World-State Transitions | 12 |
| `valoria_master_document__71__14-1-architecture` | `valoria_master_document.md` | 71 | 14.1 Architecture | 6 |
| `valoria_master_document__72__14-2-dual-authority-governance` | `valoria_master_document.md` | 72 | 14.2 Dual-Authority Governance | 4 |
| `valoria_master_document__73__14-3-church-4-axis-infrastructure` | `valoria_master_document.md` | 73 | 14.3 Church 4-Axis Infrastructure | 6 |
| `valoria_master_document__74__14-4-faction-emergence-5-stages` | `valoria_master_document.md` | 74 | 14.4 Faction Emergence (5 Stages) | 6 |
| `valoria_master_document__75__14-5-faction-collapse` | `valoria_master_document.md` | 75 | 14.5 Faction Collapse | 4 |
| `valoria_master_document__76__14-6-extended-timeline` | `valoria_master_document.md` | 76 | 14.6 Extended Timeline | 8 |
| `valoria_master_document__77__15-1-unit-representation` | `valoria_master_document.md` | 77 | 15.1 Unit Representation | 4 |
| `valoria_master_document__78__15-2-muster` | `valoria_master_document.md` | 78 | 15.2 Muster | 4 |
| `valoria_master_document__79__15-3-tc-competitive-formula` | `valoria_master_document.md` | 79 | 15.3 TC Competitive Formula | 6 |
| `valoria_master_document__80__15-4-accord-military` | `valoria_master_document.md` | 80 | 15.4 Accord → Military | 4 |
| `valoria_master_document__81__15-5-siege-ed-633` | `valoria_master_document.md` | 81 | 15.5 Siege (ED-633) | 8 |
| `valoria_master_document__83__16-2-named-npc-profiles-12-core` | `valoria_master_document.md` | 83 | 16.2 Named NPC Profiles (12 core) | 34 |
| `valoria_master_document__84__16-3-decision-procedure` | `valoria_master_document.md` | 84 | 16.3 Decision Procedure | 18 |
| `valoria_master_document__86__16-5-bg-priority-trees-all-factions` | `valoria_master_document.md` | 86 | 16.5 BG Priority Trees (All Factions) | 16 |
| `valoria_master_document__87__16-6-npc-outreach-demand-generation` | `valoria_master_document.md` | 87 | 16.6 NPC Outreach / Demand Generation | 6 |
| `valoria_master_document__88__16-7-npc-recruitment-pp-642` | `valoria_master_document.md` | 88 | 16.7 NPC Recruitment (PP-642) | 10 |
| `valoria_master_document__89__16-8-heresy-jurisdiction-ed-670` | `valoria_master_document.md` | 89 | 16.8 Heresy Jurisdiction (ED-670) | 6 |
| `valoria_master_document__90__16-9-roster-tracking-pp-661` | `valoria_master_document.md` | 90 | 16.9 Roster Tracking (PP-661) | 10 |
| `valoria_master_document__93__16-3-mending-community` | `valoria_master_document.md` | 93 | 16.3 Mending Community | 8 |
| `valoria_master_document__94__20-1-formula-consistency` | `valoria_master_document.md` | 94 | 20.1 Formula Consistency | 6 |
| `valoria_master_document__95__20-2-the-complete-pipeline` | `valoria_master_document.md` | 95 | 20.2 The Complete Pipeline | 10 |
| `valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items` | `valoria_master_document.md` | 103 | II.2 Open Decisions Requiring Jordan (16 items) | 21 |
| `valoria_master_document__106__ii-5-rating-corrections-applied` | `valoria_master_document.md` | 106 | II.5 Rating Corrections Applied | 11 |
| `valoria_master_document__107__ii-6-mechanics-flagged-for-removal` | `valoria_master_document.md` | 107 | II.6 Mechanics Flagged for Removal | 4 |
| `valoria_master_document__112__iii-1-findings-register-14-items` | `valoria_master_document.md` | 112 | III.1 Findings Register (14 items) | 19 |
| `valoria_master_document__115__iii-4-claims-that-are-speculative-hypothesis-level` | `valoria_master_document.md` | 115 | III.4 Claims That Are Speculative/Hypothesis-Level | 19 |
| `valoria_master_document__117__iv-2-claims-i-cannot-currently-verify` | `valoria_master_document.md` | 117 | IV.2 Claims I Cannot Currently Verify | 13 |
| `valoria_master_document__118__iv-3-recursive-drift-risk` | `valoria_master_document.md` | 118 | IV.3 Recursive Drift Risk | 17 |
| `valoria_master_document__121__v-3-derived-stats-gap-07` | `valoria_master_document.md` | 121 | V.3 Derived Stats (GAP-07) | 13 |
| `valoria_master_document__122__v-4-caste-social-structure` | `valoria_master_document.md` | 122 | V.4 Caste / Social Structure | 6 |
| `valoria_master_document__123__v-5-royal-assassination-fuse` | `valoria_master_document.md` | 123 | V.5 Royal Assassination Fuse | 6 |
| `valoria_master_document__124__v-6-other-likely-unreviewed-items` | `valoria_master_document.md` | 124 | V.6 Other Likely Unreviewed Items | 38 |
