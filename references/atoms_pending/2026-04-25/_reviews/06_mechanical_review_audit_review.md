# Exhaustive Review — `06_mechanical_review_audit`

**Topic:** Mechanical Review & Audit Record (consolidated)
**Atoms:** 83
**Method:** strict ID-presence check in primary registers (definition-pattern aware: YAML `id: X-N` for ED/PP, `| T-N |` table-row or `## T-N` heading for T/M) + repo path-existence + substantive-claim extraction with best-match canon excerpt.

## Summary

### ID classification

- **DEFINED-IN-CANON:** present as a defined entry in primary register (YAML `id:` for ED/PP; table row or heading for T/M).
- **MENTIONED-IN-CANON:** appears in canon corpus but not as a primary-register definition (likely cross-reference or editorial marker).
- **PARTIAL:** defined in canon, but atom's discussion is materially richer.
- **NEW:** not present in any fetched canon file.

| status | count |
|---|---|
| DEFINED-IN-CANON | 2 |
| MENTIONED-IN-CANON | 27 |
| PARTIAL | 0 |
| NEW | 0 |

### Path verification

| status | count |
|---|---|
| EXISTS | 3 |
| MISSING-FROM-REPO | 1 |

### Substantive claims surfaced: 139

## ID-by-ID comparison

### ED-129 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/combat.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items`):
  > Spirit as practitioner tax — intentional? Spirit has 4 non-practitioner uses | Low | | DECISION-03 | — | Certainty trigger asymmetry (6 toward 0 vs 3 toward 5) — intentional? | Low | | DECISION-04 | ED-129 | Ranged weapon mapping to 3-axis or separate category | Medium | | DECISION-05 | ED-131 | Weapon modifier values pending playtesting | Medium | | DECISION-06 | ED-295 | **CLASH stalls at median
- **canon context** (`params/combat.md`):
  > -         damage formula revised (armour-dependent modifier); Mass Mismatch exemptions corrected; --> <!--         Close/Far zone terminology flagged ED-129 (open). Stage 1/2 struck ED-130. Reach zone flagged ED-129 (open). -->  # params_combat.md — Personal Combat  ## Pool Formula Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5) Stamina = Endurance × 5 (ED-694 canonical; PP-611 supe

### ED-131 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/combat.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items`):
  > ECISION-03 | — | Certainty trigger asymmetry (6 toward 0 vs 3 toward 5) — intentional? | Low | | DECISION-04 | ED-129 | Ranged weapon mapping to 3-axis or separate category | Medium | | DECISION-05 | ED-131 | Weapon modifier values pending playtesting | Medium | | DECISION-06 | ED-295 | **CLASH stalls at median — P1-BLOCKER** | **P1** | | DECISION-07 | ED-297 | AMPLIFY dominance over CLASH — inten
- **canon context** (`params/combat.md`):
  > Blade | +3 | +2 | +1 | +0 | | Heavy Blade | +6 | +4 | +2 | +0 | | Light Blunt | +3 | +3 | +3 | +3 | | Heavy Blunt | +5 | +5 | +5 | +5 |  [EDITORIAL: ED-131 — Exact modifier values require playtesting to confirm. Values above are the design intent from comments; simulation needed before treating as final.]  ## Initiative and Pool Allocation (PP-232)  Initiative determines declaration order, not act

### ED-200 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__15__3-5-wound-system`):
  > Incapacitated at Vitality 0. No cap/hit. No reset. Multiple wounds from one hit possible.  **N** ✓ **R** ✓ Gradual degradation. **E** ✓ One formula. One penalty type. No severity categories. **S** ✓ ED-200/201 resolved all ambiguities.
- **canon context** (`references/propagation_log.md`):
  > eferences/params_contest.md | ED-295/296 open — CLASH/REINFORCE formula fixes pending; do not compile until resolved | | references/params_combat.md (ED-200/201/202/203 rulings) | combat-rulings-2026-04-04 | designs/combat/combat_v30.md | Wound cap, carry-over, recovery, pool floor — resolved by design doc silence. Propagate to compilation on next pass. | | references/params_contest.md (PP-401 REI

### ED-295 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items`):
  > tional? | Low | | DECISION-04 | ED-129 | Ranged weapon mapping to 3-axis or separate category | Medium | | DECISION-05 | ED-131 | Weapon modifier values pending playtesting | Medium | | DECISION-06 | ED-295 | **CLASH stalls at median — P1-BLOCKER** | **P1** | | DECISION-07 | ED-297 | AMPLIFY dominance over CLASH — intentional? | Medium | | DECISION-08 | — | Shield Wall flanking — should flanking n
- **canon context** (`references/propagation_log.md`):
  > bonus; must propagate to BG design doc on next compile | | designs/contest/social_contest_v30.md | contest-movement | references/params_contest.md | ED-295/296 open — CLASH/REINFORCE formula fixes pending; do not compile until resolved | | references/params_combat.md (ED-200/201/202/203 rulings) | combat-rulings-2026-04-04 | designs/combat/combat_v30.md | Wound cap, carry-over, recovery, pool floo

### ED-297 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/contest.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items`):
  > separate category | Medium | | DECISION-05 | ED-131 | Weapon modifier values pending playtesting | Medium | | DECISION-06 | ED-295 | **CLASH stalls at median — P1-BLOCKER** | **P1** | | DECISION-07 | ED-297 | AMPLIFY dominance over CLASH — intentional? | Medium | | DECISION-08 | — | Shield Wall flanking — should flanking negate +2D Def? | Low | | DECISION-09 | PP-508 | Splitting dominance — suffic
- **canon context** (`params/contest.md`):
  > rator's margin is small. Fix: apply max(0, ...) floor to REINFORCE movement. **Mechanical fix — can apply without user decision if authorized.**  ### ED-297: AMPLIFY dominant over CLASH AMPLIFY produces ~5 movement/exchange vs CLASH ~0 at median. Coalitions are mechanically superior to solo advocacy. May be intended design (rewarding alliances). **User decision required: confirm or rebalance.**  #

### ED-618 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/npcs/npc_character_analyses_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__83__16-2-named-npc-profiles-12-core`):
  > es FAILED. **E** ✓ Three attributes per NPC. Lookup table. **S** ✓ Profiles feed into Decision Procedure (§16.3), Priority Trees (§16.5), and Arc Profiles (§16.4).  ### 16.2a Torben Emergence Window (ED-618)  First faction to reach Disposition ≥ +2 before Season 8 sets his primary Conviction. If none: defaults to Order. After S8: locked. Conviction determines Crown Priority Tree behavior if Torben
- **canon context** (`designs/npcs/npc_character_analyses_v30.md`):
  > (sub-roll 3–4, params/bg/royal_assassination.md):** If Torben is the sub-rolled target, the fuse fires S8–S12 and he dies. His Conviction window arc (ED-618) terminates; consequences activate Almud's Arc E (The Bereaved Father) — Crown must deploy military to T4 to retrieve Elske from Altonia. Compound Varfell provocation + Altonian diplomatic crisis. See designs/npcs/npc_behavior_v30.md §2.8 and 

### ED-633 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/editorial_ledger_archive.yaml`.
- **atom context** (`valoria_master_document__81__15-5-siege-ed-633`):
  > ## 15.5 Siege (ED-633)  Legionary Inward + unit adjacent. Ob = 2 + Fort Level. OW: Fort −2. Cap 5 seasons. RS −1/season.  ---  # 16. NPC BEHAVIOR SYSTEM
- **canon context** (`canon/editorial_ledger_archive.yaml`):
  > 026-04-18)"    - id: ED-632     date: 2026-04-19     description: "Shadow Renown — CANON spec in faction_politics_v30 §2.2b.i."     status: resolved     severity: P1     source: "2026-04-19"    - id: ED-633     date: 2026-04-19     description: "Deniability Debt — CANON spec in faction_politics_v30 §2.2b.ii."     status: resolved     severity: P1     source: "2026-04-19"    - id: ED-721     date: 

### ED-670 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/npcs/npc_behavior_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__89__16-8-heresy-jurisdiction-ed-670`):
  > ## 16.8 Heresy Jurisdiction (ED-670)  Jurisdiction varies by territory controller: Full in Church, permitted in Crown (with cooperation), blocked in Hafenmark (Sovereign Authority Doctrine), tolerated at +1 Ob in Varfell, none in Uncontrolled.  **N** ✓ Church authority is not universal — it depends on whose territory the heretic is i
- **canon context** (`designs/npcs/npc_behavior_v30.md`):
  > ance; most likely Cardinal to experience Conviction crisis if exposed to Thread evidence |   ---   #### §2.13a Extra-Territorial Heresy Jurisdiction (ED-670)  Church heresy designation operates differently inside vs outside Church-controlled territories:  | Territory controller | Church heresy authority | Mechanical effect | |---|---|---| | Church (T9 + Church-controlled) | Full — Inquisitors may 

### ED-694 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/mass_battle_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__14__3-4-armour`):
  > ight/Medium/Heavy. STR mins 0/2/3/4. Drain per action +0/+0/+1/+2. Wield constraint: Stamina cannot drop to ≤ 1.  **N** ✓ **R** ✓ Durability/mobility trade-off. **S** ⚠ Stamina interaction depends on ED-694 formula being canonical (End × 5 with armour as per-action drain modifier, not base Stamina reduction). Confirm.
- **canon context** (`designs/provincial/mass_battle_v30.md`):
  > rritorial | | Campaign | ~1,000 soldiers | Territorial | | War | ~5,000 soldiers | Structural |  Scale sets **block_size** for TroopCount derivation (ED-694):  | Scale | block_size | |-------|-----------| | Skirmish | 10 | | Company | 100 | | Battle | 500 | | Campaign | 1,000 | | War | 5,000 |  **TroopCount = Size × block_size** (set at muster). Size becomes a computed integer: `Size = floor(Troop

### PP-233 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__43__7-1-core-formula-pp-233`):
  > ## 7.1 Core Formula (PP-233)  Pool = min(Size, Command) + Command. H = min(Discipline, Command) + DR. Total Health = Size × H. Damage/success = 1 + Power. Simultaneous damage.  **N** ✓ **R** ✓ **Command caps both pool and Health contributions — generalship dominates.** Size 6 + Command 3 → 6D, not 9D. Correct asymmetry. **E**
- **canon context** (`references/propagation_log.md`):
  > battle resolution, not Size/Power/Discipline) - references/params_factions.md → NOT REQUIRED (no mass combat stat references in factions params)  ### PP-233 — Mass Combat Unit Formula (2026-04-03) Source: design conversation 2026-04-03. Commit: 6db033d. Propagation targets: - references/params_mass_combat.md → DONE (6db033d) - references/glossary.md → DONE (this commit — new terms: Size, Power, Di

### PP-238 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/factions/stats_1_7_scale.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__16__3-6-actions-14`):
  > Establish Distance | Range management. | ✓ | | Stunt | +1D to +5D environmental. | ✓ | | Desperate Strike | Spend 2 Stamina, +bonus Off. | ✓ | | Parry | Spend 1 Stamina, +1D Def. | ✓ |  ⚠ **STALE-03: PP-238 vs PP-294 (Feint).** PP-238 says full pool to Off, Def = 0. PP-294 says partial commitment (min 3) with remainder to Def. PP-294 is more recent and more detailed. **Strike PP-238.**  ⚠ Rescue i
- **canon context** (`params/factions/stats_1_7_scale.md`):
  > ent.  --- <!-- PP-236 applied 2026-04-04: Crown covert actions rule --> <!-- PP-237 applied 2026-04-04: Public Instability Hybrid definition --> <!-- PP-238 applied 2026-04-04: Lowenritter reactive Military NPC guidance --> <!-- PP-241 applied 2026-04-04: Crown-Lowenritter covert delegation rule (PROVISIONAL) --> <!-- PP-244 applied 2026-04-04: Scene→Mass transition modifier table (PROVISIONAL) --

### PP-239 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/combat.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__12__3-2-initiative`):
  > ## 3.2 Initiative  Exchange 1: higher Attunement declares last (information advantage). Subsequent: transfers to exchange winner. Tie: stays with holder. Tiebreak: Att → Agi → GM/coin (PP-239).  **N** ✓ **R** ✓ Attunement (not Agility) for E1 = perceptive > fast. Cross-build value. **E** ✓ Three rules. **S** ✓
- **canon context** (`params/combat.md`):
  > efence = 0 this round. Feinting character exposed — incoming attacks resolve against Defence 0. On success: opponent −2D Defence next round only.  ## PP-239 — Initiative tiebreaker Equal Attunement in Exchange 1: higher Agility acts last. If Agility also equal: GM or coin flip.  ## PP-247 — Action priority order | Priority | Action | |----------|--------| | 1 | Strike | | 2 | Feint | | 3 | Disarm,

### PP-246 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/factions/stats_1_7_scale.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__03__1-1-die-face-rule-d10`):
  > ## 1.1 Die Face Rule (d10)  | Face | Effect | |------|--------| | 1 | −1 success | | 2–6 | 0 | | 7–9 | +1 success | | 10 | +2 successes |  Net = total successes − total 1s. May be negative (PP-246). Same rule in every system. No exceptions.  **N** ✓ Foundation of all resolution. **R** ✓ The 1-face as anti-success means pool size is a risk calculation — larger pools can still produce net 0 if 1s cl
- **canon context** (`params/factions/stats_1_7_scale.md`):
  > rown-Lowenritter covert delegation rule (PROVISIONAL) --> <!-- PP-244 applied 2026-04-04: Scene→Mass transition modifier table (PROVISIONAL) --> <!-- PP-246 applied 2026-04-04: Lowenritter ethical framework modifiers extracted (Niflhel struck) -->  ## Crown Covert Actions (PP-236) [PROVISIONAL — ED-147]  Crown has NO Intel stat. Crown covert actions (investigation, sabotage, intelligence gathering

### PP-251 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/mass_battle_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__45__7-3-key-mechanics`):
  > ## 7.3 Key Mechanics  **Discipline Degradation (PP-251):** Fires when BOTH: Size loss > Discipline AND this unit's loss > opponent's by ≥ 1. Symmetric = no trigger. Asymmetry mechanic, not attrition.  **Morale:** Range 1–7. Floor 1 (general present). At 0: rout. Cap −3/Cascade (general death uncapped). Contagion −1 adjacent (no cascade).  **Formations:
- **canon context** (`designs/provincial/mass_battle_v30.md`):
  > — organisational integrity. Starting value = min(general's Command, Military ceiling above).  **Discipline check — DETERMINISTIC (PP-502, propagating PP-251):** *[P1-04]* Discipline degrades by 1 when BOTH conditions are met (checked at Phase 6 Step 2): (1) Total Size lost this turn > current Discipline rating (2) This unit's Size loss exceeds the opposing unit's Size loss by ≥ 1 Symmetric losses 

### PP-285 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/factions_personal.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__16__3-6-actions-14`):
  > | All Def. Mass Mismatch exempt. | ✓ | | Escape (PP-634) | Agi TN 7 Ob 1. Contested if pursued. Partial = exit + free strike. | ✓ | | Take a Breath | Restore Stamina. Cannot in melee. | ✓ | | Rescue (PP-285/406/407) | N Off dice contest attacker. Win: redirect, +2 Momentum if struck. Fail: +1 Momentum if wounded. Chain block. | ✓ | | Disarm | Off vs (STR+Agi) as Ob. | ✓ | | Dodge | Full pool Def v
- **canon context** (`params/factions_personal.md`):
  > ion's relevant stat. Ob = target faction's relevant stat (1–7 scale, no division). Seasonal cap: ±2 per stat per season at accounting. Minimum Ob: 1 (PP-285).  ### Ethical Framework Modifiers | Alignment | Ob Modifier | |-----------|------------| | Aligned with faction framework | −1 Ob | | Neutral / unrelated | ±0 | | Opposed to framework | +1 Ob | | Church revealing Thread truth | +2 Ob | Min Ob

### PP-294 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/board_game.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__16__3-6-actions-14`):
  > ## 3.6 Actions (14)  | Action | Key Rule | N | |--------|----------|---| | Strike | Standard Off vs Def → damage | ✓ | | Feint (PP-294) | Commit N dice (min 3). Remainder to Def. Margin = dice opponent loses next round. Non-stacking. Floor 1D. | ✓ | | Full Guard | All Def. Mass Mismatch exempt. | ✓ | | Escape (PP-634) | Agi TN 7 Ob 1. Contested if pursued. Partial = exit + free strike. | ✓ | | Tak
- **canon context** (`params/board_game.md`):
  > REVIEW]   - BG Overwhelming Threshold — Final (PP-281 / PP-299)   - ED-056 Resolution (PP-293) — Zoom In TC Win-Delay Exploit   - ED-072 Resolution (PP-294) — Concurrent Zoom In Ordering   ... +9 more headings  ## [params_bg_faction_actions.md](references/params_bg_faction_actions.md)  ~4,793 tokens    - Faction Unique Actions — Board Game (PP-428–442, 2026-04-07)     - Church — Piety Spread (PP-4

### PP-402 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__79__15-3-tc-competitive-formula`):
  > ## 15.3 TC Competitive Formula  PP-402 (unconditional passive +1/season) repealed. Seven-step formula: Conditional Passive → Piety Yield → Charity Advantage → Templar Presence → Assert → Suppress → Baralta. Cap ±5/season.  **R** ✓ Church must EARN CI through active institutional maintenance. **E** ⚠ Seven steps dense for human play. God
- **canon context** (`references/propagation_log.md`):
  > ref/arcs_46_55_consolidated.md` | `gm_ref/arcs_46_55_consolidated.md` | `gm_ref/arcs_46_55_consolidated.md` | `references/params_factions.md` | Cites PP-402, PP-403, Domain Action Ob formula, ethical framework modifiers | REFERENCE | | `gm_ref/arcs_46_55_consolidated.md` | `references/params_threadwork.md` | Cites PP-255, Leap table, Contact Duration, Coherence | REFERENCE | | `gm_ref/arcs_46_55_c

### PP-508 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/mass_battle_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items`):
  > BLOCKER** | **P1** | | DECISION-07 | ED-297 | AMPLIFY dominance over CLASH — intentional? | Medium | | DECISION-08 | — | Shield Wall flanking — should flanking negate +2D Def? | Low | | DECISION-09 | PP-508 | Splitting dominance — sufficient terrain counter-play? | Medium | | DECISION-10 | — | IP rate halving — mode-specific or global? | Low | | DECISION-11 | ED-NEW-TC-01 | Conditional passive thr
- **canon context** (`designs/provincial/mass_battle_v30.md`):
  > mune to that flank | 1 | Sacrifices offence | | Hammer & Anvil | Shield Wall holds; Fast unit envelops | 3 | Break Anvil first |  Splitting doctrine (PP-508 — replaces P2-14 note, ED-358): Splitting is structurally across simultaneous engagements. Simulation results: - Split dominates concentration by +9% to +45% win-rate depending on Command matchup. - Only cases where split advantage is negligib

### PP-512 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/provincial/peninsular_strain_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__68__13-2-faction-toolkits-not-alternate-endpoints`):
  > ## 13.2 Faction Toolkits (NOT Alternate Endpoints)  **Crown:** Treaty + rival suppression. Crown Treaty (PP-512–523) = most detailed single action. **Church:** Mass Seizure (one-shot). P(declare) = ((CI−60)/40)^3.3. Pool = Influence + floor(CI/15). Ob = 10 − PT − infrastructure. **Hafenmark:** Dynastic Assertion. PV ≥ 13 + PI ≥ 5 + Crown Mandate ≤ 3. **Varfell:** Path A (Intelligence Hegemony) or 
- **canon context** (`designs/provincial/peninsular_strain_v30.md`):
  > Battle is required for garrisoned territories).  ### §5.1 Crown — Formal Crown Treaty (Existing)  See victory_v30.md §3.1 for full Treaty mechanics (PP-512/513/514/523).  **Card type:** Senator Outward (Crown only). **Ob:** floor(target Mandate / 2) + 1, min 1. **Pool:** Influence.  Crown Treaty subordinates rival factions diplomatically. Treaty-bound factions count toward Crown's effective hegemo

### PP-606 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/threadwork.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__31__5-6-substrate-saturation-counter-pp-606`):
  > ## 5.6 Substrate Saturation Counter (PP-606)  ≥3 ops/battle turn → +1 Ob/+1 Coherence (cap +2). Counter ≥ 3 → +2 Ob rest of battle. ≥3 at end → RS −1 at Accounting. Hard cap −1/battle. Replaces old ×3 multiplier.  **N** ✓ **E** ✓ Counter. Threshold. Two penalty tiers.
- **canon context** (`params/threadwork.md`):
  > n end. No permanent penalties. TS 30+ on Success: readable Thread information (Discovery Event or Belief revision).  ## Substrate Saturation Counter (PP-606 — canonical; was Dissonant Counter PP-502) When ≥ 3 Thread operations fire in a single mass battle turn, substrate saturates: | Condition | Effect | |---|---| | 3+ ops in one battle turn | All subsequent ops that turn: +1 Ob, +1 Coherence cost

### PP-607 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/threadwork.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__34__5-9-dissonance-pp-607-610`):
  > ## 5.9 Dissonance (PP-607/610)  Spirit TN 7 vs Factor (1–4). Failure: −1D Spirit (scene/season). TS 30+ on Success: Discovery Event.  **N** ✓ **R** ✓ Dual outcome (harm/discovery from same stimulus).
- **canon context** (`params/threadwork.md`):
  > CK (PP-603). Reality takes full consequence. Starting: TTRPG default 60; BG default 72. RS = 0: Rupture (shared loss).  ## Dissonance — Spirit Check (PP-607, PP-610 — canonical) When Thread operations fire nearby, character enters Thread-disrupted space, or POP affects their temporal experience: Spirit check TN7 vs Dissonance Factor.  Dissonance Factor by source: - Thread operation nearby (brief):

### PP-632 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/scene/derived_stats_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__32__5-7-knots-pp-632`):
  > ## 5.7 Knots (PP-632)  Pool = (Bonds × 2) + 3. Close 5 / Medium 2 / Loose 1. Max = floor(Bonds/2)+1. Rupture: Disp → −4, Composure damage. Loss: Coherence −1. Simultaneous Rupture cap (PP-633): ≤ 75% Composure.  **N** ✓ Mechanizes relationships as ontological structures. Any character — TS not required. **R** ✓ Three t
- **canon context** (`designs/scene/derived_stats_v30.md`):
  > res Bonds ≥ 5. Knot candidacy (Disposition +5) requires Bonds ≥ 5 (achievable at creation).  Cross-reference: fieldwork_v30 §5.1, params_core §Bonds (PP-632/PP-684), companion_specification §2.1.  ### 10.2 Army Morale (Mass Combat Derived Composite)  **Army Morale = floor(average unit Morale) + Command modifier + Discipline modifier**  | Component | Source | Range | |-----------|--------|-------| 

### PP-633 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/core.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__32__5-7-knots-pp-632`):
  > ## 5.7 Knots (PP-632)  Pool = (Bonds × 2) + 3. Close 5 / Medium 2 / Loose 1. Max = floor(Bonds/2)+1. Rupture: Disp → −4, Composure damage. Loss: Coherence −1. Simultaneous Rupture cap (PP-633): ≤ 75% Composure.  **N** ✓ Mechanizes relationships as ontological structures. Any character — TS not required. **R** ✓ Three tiers with distinct mechanical benefits. **E** ✓ One pool, three tiers, one cap.
- **canon context** (`params/core.md`):
  > -246–248, PP-255, PP-261, PP-289–290, PP-381, PP-383–386, PP-389, PP-551, PP-553, PP-610–611, PP-615, PP-617, PP-623, PP-627, PP-628, PP-629, PP-632, PP-633 --> <!-- PP-247 (Combat Pool formula corrected to match stage1 §2.3/§3.4: Agi + hist_pts + 3) --> <!-- PP-248 (Stamina formula corrected to End+1 per stage1 §3.9; Health row clarified) --> <!-- PP-232 (Ob cap raised to 20; Overwhelming floor 3

### PP-634 — **MENTIONED-IN-CANON**

- **detail:** Appears in `params/combat.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__16__3-6-actions-14`):
  > | ✓ | | Feint (PP-294) | Commit N dice (min 3). Remainder to Def. Margin = dice opponent loses next round. Non-stacking. Floor 1D. | ✓ | | Full Guard | All Def. Mass Mismatch exempt. | ✓ | | Escape (PP-634) | Agi TN 7 Ob 1. Contested if pursued. Partial = exit + free strike. | ✓ | | Take a Breath | Restore Stamina. Cannot in melee. | ✓ | | Rescue (PP-285/406/407) | N Off dice contest attacker. Win
- **canon context** (`params/combat.md`):
  > f (which yields +2 per PP-406) - Failed intercept with no rescuer wound: no Momentum return (correct tension maintained)  ## Surrender and Disengage (PP-634)  **Yield:** Declared at Phase 1. Opponent chooses: Accept (combat ends; prisoner/withdrawal) or Refuse (unresisting — no contest roll). Cannot Yield while faction's objective is actively contested in zone.  **Disengage:** Phase 1 declaration,

### PP-642 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__88__16-7-npc-recruitment-pp-642`):
  > ## 16.7 NPC Recruitment (PP-642)  Four-step: Identify (Disp +4/+5 = not recruitable) → Approach (Cha pool, Ob = floor(highest Disp / 2)+1) → Offer (one incentive, modifies Ob) → Resolution (Failure = faction warned; Partial = +1 Disp, retry −1 Ob; Success = joins; OW = joins + intel).  Hooks: Weak (−2 Ob, reusable on failure). St
- **canon context** (`references/propagation_log.md`):
  > ) |  ## PP-641–642 Propagation (2026-04-13)  ### PP-641 — Opposing Operations → threadwork design doc | Source | Target | Status | |---|---|---|  ### PP-642 — NPC Recruitment | Source | Target | Notes | |---|---|---| | `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_contest.md` | Findings citation extracted ✓ | | `designs/systems/npc_behavior_v30.md` §9.5 | `references/params_comba

### PP-653 — **DEFINED-IN-CANON**

- **detail:** Defined in primary register `canon/patch_register_active.yaml`.
- **atom context** (`valoria_master_document__29__5-4-opposing-operations-pp-653`):
  > ## 5.4 Opposing Operations (PP-653)  Pairs: Weave/Pull, Lock/Dissolution, Lock/Pull, Weave/Dissolution. Engagement modifier: +floor(opponent TPS/2), min +1. N-way (3+): all fail, Gap forms, RS −(2×n). Prevents dogpiling.  **E** ⚠ Resolution table has 6 outcomes with 3–4 consequences each. Most complex table in the game. Manageable f
- **canon context** (`canon/patch_register_active.yaml`):
  > , T4/T11/T12 at 2 (Varfell-area old Einhir traditions), remainder     at 3.   affects:   - designs/provincial/peninsular_strain_v30.md   - references/params_board_game.md   status: provisional  - id: PP-653   date: 2026-04-18   severity: P1   description: "Opposing Operations params propagation from design doc 2.6. Adds opposing engagement modifier, resolution table, knot strain, FR vs FR, N-way, 

### PP-661 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__90__16-9-roster-tracking-pp-661`):
  > ## 16.9 Roster Tracking (PP-661)  Three tiers: Active (~35 cap, full state tracking), Passive (~30, compact), Background (unlimited, identity only). Demotion triggers: 4+ seasons off-screen, low Disposition inertia, faction removal. Inner circle structurally Active. Companion app display at each tier.  **N** ✓ Without roster mana
- **canon context** (`references/propagation_log.md`):
  > | DONE — aggregated | | tests/thread_stress/threadwork_audit_register.md §F | references/ms_budget.md §5 | DONE — peak scenarios incorporated |   ## PP-661 — Faction Politics Throughline Resolutions (2026-04-17)  | Changed File | Propagates To | Reason | |-------------|--------------|--------| | `designs/systems/throughline_resolutions_v1.md` (NEW) | `designs/systems/faction_politics_expanded_v1.m

### PP-684 — **MENTIONED-IN-CANON**

- **detail:** Appears in `references/propagation_log.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__39__6-4-socializing-disposition`):
  > ## 6.4 Socializing / Disposition  Range −3 to +5. Ceiling = Bonds (PP-684). 7 action types (Read, Converse, Connect, Impress, Rumour, Negotiate, Gift/Bribe).  **R** ✓ Bonds cap forces relational investment. Sincerity Gate (Spirit TN 7 Ob 1, 37% failure at Spirit 3) prevents transactional relationship farming.  ### 6.4a Information Gates (Parallel Access)  | Method | D0 |
- **canon context** (`references/propagation_log.md`):
  > 30.md` (ED-629 dependency) | `designs/systems/faction_politics_expanded_v1.md` §2.7 | ED-629 Thread stress resolution may require Warden audit |  ### PP-684 — Disposition ceiling = Bonds (was floor(Bonds/2)+1) | Source | Target | Status | |--------|--------|--------| | references/params_core.md (Bonds definition) | designs/fieldwork/fieldwork_v30.md §5.1 | DONE | | references/params_core.md (Bonds

### TC-01 — **MENTIONED-IN-CANON**

- **detail:** Appears in `designs/scene/fieldwork_v30.md` but not as a defined entry in primary register.
- **atom context** (`valoria_master_document__103__ii-2-open-decisions-requiring-jordan-16-items`):
  > D Def? | Low | | DECISION-09 | PP-508 | Splitting dominance — sufficient terrain counter-play? | Medium | | DECISION-10 | — | IP rate halving — mode-specific or global? | Low | | DECISION-11 | ED-NEW-TC-01 | Conditional passive thresholds pending smoke-test | Deferred | | DECISION-12 | — | Conviction taxonomy reducibility (9 → 7 universal + 2 specific?) | Low | | DECISION-13 | — | Aggregate cognit
- **canon context** (`designs/scene/fieldwork_v30.md`):
  > use. Detection → Disposition −3. | | DIS-01/02 | Non-sensitive partner Dissonance: §2.7. Spirit check vs Dissonance Factor. Field team rotation. | | TC-01/02/03/04 | Threadcut being social fieldwork: §2.8. Testimonial tag. P-08 bridged by being's translation. Evidence Track = player-level knowledge. Counter-investigation possible. | | MA-02/03 | Mending arcs as investigation: §2.4. Severity reduct

## Path verification

| path | status | atom occurrences |
|---|---|---|
| `params/core.md` | EXISTS | 1 |
| `params/combat.md` | EXISTS | 1 |
| `designs/architecture/derived_stats_v30.md` | MISSING-FROM-REPO | 1 |
| `params/bg/core.md` | EXISTS | 1 |

## Substantive claim findings

_139 substantive claims (max 3 per atom) with best-match canon excerpts._

### Matched claims (126)

- **atom** `valoria_master_document__03__1-1-die-face-rule-d10`
  - claim: > May be negative (PP-246).
  - best match: `params/core.md` (overlap 2/2)
  - canon excerpt: > ccess | | 2–6 | 0 | | 7–9 | +1 success | | 10 | +2 successes |  Net successes = total successes minus total 1s (including bonus dice results). May be negative. Note: expected value of face-10 under chain rule ≈ +1.43 net at TN7 (geometric series). Hi

- **atom** `valoria_master_document__03__1-1-die-face-rule-d10`
  - claim: > **R** ✓ The 1-face as anti-success means pool size is a risk calculation — larger pools can still produce net 0 if 1s cluster.
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 7/8)
  - canon excerpt: > tions, the Foundations govern.*  ---  # PART ONE: CORE ENGINE  ## 1.1 Dice  Roll a pool of d10s.  | Result | Effect | |--------|--------| | 7–9 | One success | | 10 | One success + roll one bonus die (chains indefinitely) | | 1 | Subtract one success

- **atom** `valoria_master_document__03__1-1-die-face-rule-d10`
  - claim: > **E** ✓ Four effect values (−1, 0, +1, +2); three non-zero outcomes.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 4/4)
  - canon excerpt: >  damage. Two stats unified in personal combat split here:  - **Size** — headcount. Health pool. Casualties reduce it directly. - **Power** — fighting effectiveness per soldier. Equipment and   training. Determines dice rolled.  **Effective Combat Poo

- **atom** `valoria_master_document__05__1-3-obstacle-scale`
  - claim: > Intermediate values (4, 6, 7) appear in calculated Obs and are valid — the named scale is reference, not enumeration.
  - best match: `designs/arcs/arc_expansion_v30.md` (overlap 7/8)
  - canon excerpt: > ng internal Church evidence of RS degradation is an Authority appeal Almud cannot dismiss (the source is Church-internal, his Virtue Ethics framework values institutional honesty).  ---  #### Arc B: The Fortress (Expanded Behavioral Consequences)  **

- **atom** `valoria_master_document__05__1-3-obstacle-scale`
  - claim: > **E** ✓ **S** ⚠ BG mode has Ob 10 exception (Overwhelming unavailable, Partial ≥ 5).
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 4/4)
  - canon excerpt: > directly. bonus (+1 per 2 dice). **Volley Size loss is recorded but NOT applied until Phase 6 Step 1.** *[P2-06, ED-037 provisional: TN 6 intentional exception]*  **Phase 3 — Manoeuvre** Fast → Standard → Slow. Environmental modifiers applied. Reserv

- **atom** `valoria_master_document__05__1-3-obstacle-scale`
  - claim: > TTRPG has Ob 20 exception (Overwhelming unavailable, Partial ≥ 10).
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 4/4)
  - canon excerpt: > directly. bonus (+1 per 2 dice). **Volley Size loss is recorded but NOT applied until Phase 6 Step 1.** *[P2-06, ED-037 provisional: TN 6 intentional exception]*  **Phase 3 — Manoeuvre** Fast → Standard → Slow. Environmental modifiers applied. Reserv

- **atom** `valoria_master_document__06__1-4-degrees-of-succes`
  - claim: > **R** ✓ 2×Ob naturally scales.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 2/2)
  - canon excerpt: > omotion event | +1 | Automatic; each Rb-Std advancement per §2.2 ladder |  **Cap:** +2 Shadow Renown per season maximum. Shadow Renown does not decay naturally.  **Effects:**  | Shadow Renown | Effect | |---------------|--------| | 3+ | Covert NPCs (

- **atom** `valoria_master_document__06__1-4-degrees-of-succes`
  - claim: > Floor of 3 prevents trivial Overwhelmings at Ob 1.
  - best match: `designs/audit/gameplay_assessment_2026_04_21.md` (overlap 2/4)
  - canon excerpt: > mechanic. **Emergent situations.** None. **Tradeoff.** None. **Verdict.** G-texture — or more precisely, G-frame. This is a framework commitment that prevents an incoherent-mechanic from being built. Its gameplay contribution is negative-space: it co

- **atom** `valoria_master_document__103__ii-2-open-decisions-`
  - claim: > Spirit has 4 non-practitioner uses | Low |
| DECISION-03 | — | Certainty trigger asymmetry (6 toward 0 vs 3 toward 5) — intentional?
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 7/8)
  - canon excerpt: > social pools (Appeal, Circles); faction actions |  ### Metaphysical  | Attribute | Abbreviation | Governs | |-----------|-------------|---------| | **Spirit** | Spi | Will, existential resilience, inner coherence; Certainty derivation; Confrontation 

- **atom** `valoria_master_document__107__ii-6-mechanics-flagg`
  - claim: > Some are narrow (Disarm+Retrieve at ~20% relevance, Tie Up at ~5%) but each fills a tactical niche.
  - best match: `designs/npcs/npc_behavior_v30.md` (overlap 4/7)
  - canon excerpt: > ueried. Success: one NPC with TS ≥ 30 in that settlement during the spike season is identified as a probable practitioner. This does not confirm — it narrows the search.  A character with TS 10–29 who accesses the deep archive gets an uneasy sense th

- **atom** `valoria_master_document__112__iii-1-findings-regis`
  - claim: > MS band transition at 60 is the designed valley-breaker.
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 3/4)
  - canon excerpt: > is is not a roll — it is a narrative commitment confirmed at seasonal accounting.  ## 5.2 The Leap — Entering Contact  The Leap is the practitioner's transition from ordinary perception to Thread contact. It is always risky, always costly, and never 

- **atom** `valoria_master_document__115__iii-4-claims-that-ar`
  - claim: > ---

# PART IV: ITEMS REQUIRING RE-VERIFICATION BEFORE ACTION

These findings should be checked against source before being used to drive design changes.
  - best match: `designs/ui/valoria_ui_ux_v4_1.md` (overlap 8/8)
  - canon excerpt: > tal restatement completes. Spec-autonomy target: v4.2+ (see valoria_ui_ux_v4_2_workplan.md, F-69 Option B) **Audit trail:** incorporates all critical findings from valoria_ui_ux_v4_audit.md + valoria_ui_ux_v4_audit_addendum.md (both 2026-04-16) **Str

- **atom** `valoria_master_document__118__iv-3-recursive-drift`
  - claim: > The reduction to 4 in Part II §II.10 was directional but not exhaustively re-justified.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 3/4)
  - canon excerpt: > e card triggers** (per worldbuilding_v30 §4.3 Card: Riskbreaker Exposure). Crown Domain Actions against non-Crown factions +1 Ob. | | 4 | Cooling-off reduction disabled (Debt sticks above 4). | | 5 | **Parliamentary inquiry opens** — Grand Debate (Cr

- **atom** `valoria_master_document__11__3-1-pool-split-off-de`
  - claim: > Min 1 each (except Full Guard/Feint).
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 2/3)
  - canon excerpt: > directly. bonus (+1 per 2 dice). **Volley Size loss is recorded but NOT applied until Phase 6 Step 1.** *[P2-06, ED-037 provisional: TN 6 intentional exception]*  **Phase 3 — Manoeuvre** Fast → Standard → Slow. Environmental modifiers applied. Reserv

- **atom** `valoria_master_document__11__3-1-pool-split-off-de`
  - claim: > **N** ✓ THE core combat decision.
  - best match: `references/propagation_log.md` (overlap 2/2)
  - canon excerpt: >  source it | |-------------|--------------------|-----------------------------| | `params_core.md` | ALL skills | `stage1_core_engine.md` | | `params_combat.md` | simulator G1, combat-simulator | `designs/combat/combat_v30.md`, `stage8_combat.md` | |

- **atom** `valoria_master_document__11__3-1-pool-split-off-de`
  - claim: > **R** ✓ 10D pool → 5/5 balanced, 8/2 aggressive, 2/8 defensive.
  - best match: `designs/provincial/faction_politics_v30.md` (overlap 2/3)
  - canon excerpt: > resolved via SUC-03.  ---  # PART 9 — CROSS-FACTION RANK PARITY  Per Finding A-11 and BALANCE-POL-01, the expanded rank ladders must be cross-faction balanced. The **same Standing number** should grant roughly equivalent mechanical weight across fact

- **atom** `valoria_master_document__124__v-6-other-likely-unr`
  - claim: > The reliability disclosure at the start should be re-read before any single finding is acted on.
  - best match: `designs/arcs/arc_expansion_v30.md` (overlap 6/7)
  - canon excerpt: >  is the political win). | | Crown Obligation honored toward Löwenritter: "Maintain garrison in T10" | Ehrenwall: Coup Counter −1 (Crown demonstrating reliability on a specific commitment is exactly what her assessment tracks). | | Crown Obligation vi

- **atom** `valoria_master_document__13__3-3-weapon-system-3-b`
  - claim: > Produces TN 5 (Short Light Blade) to TN 8 (Long Heavy Blunt).
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 5/6)
  - canon excerpt: > er | Object (Past-Oriented) | 3 | 80 | Burned letter readable; broken object briefly whole; glimpse of the object's prior state. Duration: one round. Produces TD +1. |  ---  ## 15.3 Forced Resolution Operations  *Collapses a thread configuration to o

- **atom** `valoria_master_document__13__3-3-weapon-system-3-b`
  - claim: > **S** ⚠ **DECISION-04 (ED-129 OPEN):** Ranged weapons NOT mapped to this matrix.
  - best match: `params/combat.md` (overlap 5/6)
  - canon excerpt: > -         damage formula revised (armour-dependent modifier); Mass Mismatch exemptions corrected; --> <!--         Close/Far zone terminology flagged ED-129 (open). Stage 1/2 struck ED-130. Reach zone flagged ED-129 (open). -->  # params_combat.md — 

- **atom** `valoria_master_document__14__3-4-armour`
  - claim: > Drain per action +0/+0/+1/+2.
  - best match: `designs/scene/derived_stats_v30.md` (overlap 2/2)
  - canon excerpt: > sources  ### 4.1 Vitality (survival resource)  | Property | Value | |----------|-------| | Formula | Endurance × 10 | | Range | 10–70 | | Direction | Drains down from max | | Depleted at | 0 (incapacitated) | | Equipment | Armor adds flat Vitality (+

- **atom** `valoria_master_document__14__3-4-armour`
  - claim: > Wield constraint: Stamina cannot drop to ≤ 1.
  - best match: `designs/world/character_histories_v30.md` (overlap 3/4)
  - canon excerpt: >  | | **3-LO4: Patrol Officer (Threadcut Encounter Veteran)** | ★ Anomaly Recognition (unique: +1D Cognition to assess threadcut being threat/movement/constraints) · ★ Classified Knowledge (unique: once/arc invoke classified info for +2D; risks Order 

- **atom** `valoria_master_document__14__3-4-armour`
  - claim: > **S** ⚠ Stamina interaction depends on ED-694 formula being canonical (End × 5 with armour as per-action drain modifier, not base Stamina reduction).
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 7/8)
  - canon excerpt: > |-----------|-------------|---------| | **Agility** | Agi | Speed, precision, reflexes; combat pool base; dodge; initiative | | **Endurance** | End | Stamina, vitality, resilience; Health derivation; Breather recovery | | **Strength** | Str | Raw phy

- **atom** `valoria_master_document__15__3-5-wound-system`
  - claim: > Wound Interval = End + 6.
  - best match: `designs/scene/derived_stats_v30.md` (overlap 2/2)
  - canon excerpt: > | Armor adds flat Vitality (+4 leather, +6 chain, +8 plate). Consumables restore on rest (+4 rations, +8 healer's kit). Poisons drain per round. |  **Wound Interval = Endurance + 6** (unchanged). Wounds accrue at each interval of cumulative damage: `

- **atom** `valoria_master_document__15__3-5-wound-system`
  - claim: > Incapacitated at Vitality 0.
  - best match: `params/combat.md` (overlap 2/2)
  - canon excerpt: > rance + 6) × (max Wounds + 1) — total pool, never resets. Wound threshold every (Endurance + 6) points of damage; Wound counter +1 at each threshold. Incapacitated at 0 HP. (PP-232, ED-438)  **Armour wield constraint (PP-232):** A character cannot we

- **atom** `valoria_master_document__15__3-5-wound-system`
  - claim: > **S** ✓ ED-200/201 resolved all ambiguities.
  - best match: `references/propagation_log.md` (overlap 2/3)
  - canon excerpt: > eferences/params_contest.md | ED-295/296 open — CLASH/REINFORCE formula fixes pending; do not compile until resolved | | references/params_combat.md (ED-200/201/202/203 rulings) | combat-rulings-2026-04-04 | designs/combat/combat_v30.md | Wound cap, 

- **atom** `valoria_master_document__16__3-6-actions-14`
  - claim: > Win: redirect, +2 Momentum if struck.
  - best match: `designs/npcs/npc_behavior_v30.md` (overlap 3/3)
  - canon excerpt: > sion. Cannot target RM or seize RM-held territory. | | Secondary Conviction | Reason | Retains Varfell's institutional knowledge-seeking tendency but redirects it toward collaborative rather than acquisitive ends. | | Ethical Framework | Shifts from 

- **atom** `valoria_master_document__16__3-6-actions-14`
  - claim: > Fail: +1 Momentum if wounded.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 2/2)
  - canon excerpt: > alties, territory infrastructure damage, and one hidden consequence (NPC death, Accord shift, or evidence planted during the chaos). Overwhelming: +1 Momentum (tactical understanding). | | Address the population | Charisma check, Ob 2 | Success: Sett

- **atom** `valoria_master_document__16__3-6-actions-14`
  - claim: > PP-294 says partial commitment (min 3) with remainder to Def.
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 3/4)
  - canon excerpt: > tegrity woven so knowledge persists even if material form is destroyed. **W-06 Dissolving a Monstrous Configuration** (Ob 3–5): Entity destroyed; Gap partially closed. **W-07 Rekindling** (Personal, Ob 2): Restores Composure strain and may replenish 

- **atom** `valoria_master_document__17__3-7-fibonacci-group-b`
  - claim: > **E** ✓ 6-entry lookup.
  - best match: `designs/provincial/mass_battle_v30.md` (overlap 2/2)
  - canon excerpt: >   ---  ### A.11 SOUTHERNMOST  Non-Thread-sensitive units (Thread Sensitivity < 30) cannot operate in Southernmost. They dissolve without awareness on entry — no casualties, no Morale trigger, no Discipline check. Remove from battle map. This is why S

- **atom** `valoria_master_document__19__3-9-ranged-combat`
  - claim: > Terrain closing: 1–3 rounds.
  - best match: `deprecated/valoria_ttrpg_complete.md` (overlap 3/3)
  - canon excerpt: > l rolls instead) - Armour: no pool penalty (armour provides damage reduction only) - Fibonacci group bonus: adds to Offence allocation specifically - Terrain/zone: GM may impose +1 Ob for adverse terrain; does not reduce pool  ## 3.5 Attack Resolutio

_(96 more matched.)_

### Unmatched claims — possibly NEW or rephrased (13)

- atom `valoria_master_document__12__3-2-initiative`: > Tiebreak: Att → Agi → GM/coin (PP-239).
- atom `valoria_master_document__13__3-3-weapon-system-3-b`: > **N** ✓ 8 archetypes from 3 bits.
- atom `valoria_master_document__24__4-5-composure-concent`: > −1/exchange, −1 on loss.
- atom `valoria_master_document__27__5-2-three-axis-ob`: > TS gates (30/50/70/90).
- atom `valoria_master_document__29__5-4-opposing-operatio`: > N-way (3+): all fail, Gap forms, RS −(2×n).
- atom `valoria_master_document__30__5-5-gap-self-closure`: > Foundational 32 (5).
- atom `valoria_master_document__31__5-6-substrate-saturat`: > ≥3 at end → RS −1 at Accounting.
- atom `valoria_master_document__53__9-4-faction-starting-`: > Ceilings: M 0–7, I 1–7, W 0–7, Mil 0–7, S 0–7.
- atom `valoria_master_document__54__9-5-global-tracks`: > PI 7 (Crown elim at 20).
- atom `valoria_master_document__63__12-2-ci-church-influe`: > Seizure at 60 (one-shot).
- atom `valoria_master_document__68__13-2-faction-toolkits`: > P(declare) = ((CI−60)/40)^3.3.
- atom `valoria_master_document__81__15-5-siege-ed-633`: > Ob = 2 + Fort Level.
- atom `valoria_master_document__94__20-1-formula-consiste`: > TN 6/7/8 everywhere.

## Recommendation

**Recommendation: CANONICAL-PROMOTION-NEEDED — 27 IDs mentioned in canon but not in primary register; promote to formal entries before ingestion.**

- ID classification: {'DEFINED-IN-CANON': 2, 'MENTIONED-IN-CANON': 27, 'PARTIAL': 0, 'NEW': 0}
- Path verification: {'EXISTS': 3, 'MISSING-FROM-REPO': 1}
- Substantive: 126 matched / 13 unmatched