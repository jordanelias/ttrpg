# VALORIA COMBAT MECHANIC AUDIT
## Source: designs/combat/combat_design_v1.md (v1.3) | params_combat.md (v0.14-AUD4)
## Date: 2026-04-02
## Modes run: A (Formula), B (Number Systems), C (Interaction Chains), D (Gap Detection), E (Core Principles), F (Playtest Burden), G (Cross-Mode)

---

## MODE A — FORMULA VALIDATION

| ID | Formula | Min | Avg | Max | Issues | Status |
|----|---------|-----|-----|-----|--------|--------|
| A-01 | Combat Pool = (Agi×2) + History + 3 | Min pool: 2+0+3=5 (floor enforced) | Agi 3, Hist 3pts+3=6: (6)+6+3=15 | Agi 7, Hist maxed ≈7+3=10: (14)+10+3=27 | No upper cap stated. 27D pool is playable but triggers Fibonacci-suppression of output variance at high pools. No cap = design intent? Flag P3. | MINOR P3 |
| A-02 | Damage = max(0, net hits + weapon modifier − DR) | 0 (floor) | e.g. net 2, HC +4, Med DR 3 = 3 | Crit (net≥3 → mod×2): net 5, HC +8, no DR = 13 | Critical hit doubles modifier only, not net hits — formula is unambiguous. But "Critical Hit (net hits ≥ 3): weapon modifier doubled" is stated ONLY in params_combat, not in combat_design_v1 §5 (Damage Resolution). Design doc omits this rule entirely. Discrepancy: params has it, design doc lacks it. | **P1-DISCREP** |
| A-03 | Stamina = End + History + 1 − armour modifier | Min: 1 (floor enforced PP-165) | End 3, Hist 0, Light (0): 4 | End 7, Hist 10: 18; capped by recovery mechanics | Floor at 1 confirmed. No division-by-zero risk. Boundary at heavy armour (−2) + End 1 + no History = 0 → floors to 1. Confirmed correct. | PASS |
| A-04 | Health = End + 6 | Min: 7 (End 1) | End 3 → 9 | End 7 → 13 | Wound trigger: "damage ≥ Health threshold (typically 3+)" — "typically 3+" is imprecise. Actual trigger is not "Health threshold" — damage reduces Health to 0, then Wound fires. Params says "Health = Endurance score. One Wound per contact that deals damage ≥ Health threshold." Design doc §7 says "Health = Endurance score. One Wound per contact that deals damage ≥ Health threshold." But params_core.md says "Health = Endurance + 6." These are contradictory formulas. **Critical discrepancy.** | **P1-FORMULA CONFLICT** |
| A-05 | Wound Max = f(Endurance) | End 1–3: 2 wounds | End 4–5: 3 | End 6–7: 4 | Table is internally consistent. At End 3, max 2 wounds before incap; each wound −1D. With start pool ~11D (Agi 3×2 + Hist 6 + 3), 2 wounds = −2D = 9D remaining. Functional. | PASS |
| A-06 | PP-086 Mass damage = max(0, net_successes_over_Ob + disposition_modifier) | Defensive: min 0 | Standard: net 2 over Ob + 2 (Off) = 4 | Overwhelming net + 4 Offensive = high | "Net successes over Ob" is ambiguous: does this mean (net successes − Ob) or successes that exceed Ob threshold? If former: possible negative → floor applies. If latter: partial success (successes > 0 but < Ob) = 0 damage. Intent unclear. | **P1-AMBIGUITY** |
| A-07 | CR = ⌈(Presence + Cognition) ÷ 2⌉ | Min: 1 (both at 1) | Pres 3 + Cog 3 = 3 | Pres 7 + Cog 7 = 7 | No division by zero. Ceiling function well-defined. Wound penalty: +1 Ob per wound applies to CR checks. At 3 wounds + CR 3 pool → Ob 3 penalty on all CR checks. Functional but brutal — design intent. | PASS |
| A-08 | Fibonacci Group Bonus (Offence only) | 1 attacker: +0 | 3 attackers: +2D | 8+: +5D | Cap at 5D confirmed. Params states "8+ → +5D" but design doc §8 states "5th+: +5D." Off-by-one between docs — is cap at 5 attackers or 8 attackers? | **P2-DISCREP** |
| A-09 | Effective CP = min(CP, Strength) in mass combat | Both at 1: 1 | CP 5, Str 4: 4 | Both at ceiling: cap | No negative risk. Correctly prevents phantom dice. PASS | PASS |
| A-10 | Damage (ranged) = net successes + weapon modifier (no STR) | Min: 0 | LP, net 2, +0 mod: 2 | HP vs heavy armour, net 4, +2 mod, no DR: 6 | STR provisional (ED-092): design doc does not include STR in damage formula. Params confirms provisional. This is a live ambiguity for melee (not ranged) damage. Ranged confirmed STR-free. Melee STR question open. | P2-PROVISIONAL |

---

## MODE B — NUMBER SYSTEM COHERENCE

| System | Range | Scale Basis | Analogous Systems | Inconsistency |
|--------|-------|-------------|------------------|---------------|
| Attributes | 1–7 | Human-scale 1–7 | All attributes | Consistent. |
| Health | 7–13 | End + 6 | Composure (Pres + 6, same formula) | Consistent internal logic. BUT: design doc §7 says "Health = Endurance score" (not +6). Params_core says "Health = Endurance + 6." **Same P1-FORMULA CONFLICT as A-04.** One of these documents is wrong. |
| Wounds | 2–4 max | Endurance bracket | — | Wound max table is a 3-tier bracket. Reasonable. |
| Combat Pool | 5–27+ | (Agi×2) + Hist + 3 | Debate pool (Pres×2 + Hist — see SIM-DEBT-01) | No cap on Combat Pool. Debate pool has analogous structure. Range acceptable. P3 cap flag above. |
| Weapon TN (Hit) | 5–8 | d10 | Core TN 6/7/8 | TNs 5 (Light Cut hit) and 8 (Unarmed/LP) extend slightly outside core TN range of 6–8. Hit TN 5 means even low-pool attackers get high expected return. P3: verify Light Cut hit TN 5 is intentional (easier to hit with daggers/light blades — plausible). |
| Weapon TN (Def) | 6–9 | d10 | Hit TN range | Def TN 9 (Unarmed) — is this correct? Params table shows "Unarmed | 8 | 9 | +0." Design doc shows "Unarmed | 8 | 9 | +0 | Short." At Def TN 9, expected success rate ~10% per die. A 6D defender against unarmed attacker: ~0.6 defence successes expected. Effectively provides almost no defence. Is this intended (unarmed attack is hard to defend against = clinch/grapple context)? Flag P2 for design review. |
| DR (Melee) | 0–6 | Armour tier × weapon type | Ranged DR | Melee Heavy vs LC = 6 DR. A Light Cut hit average ~2 net hits + 1 mod = 3 total. After 6 DR = 0 damage. Light Cut is effectively useless vs Heavy armour, which is likely intended. Confirm. |
| DR (Ranged) | 0–5 | Armour tier × projectile type | Melee DR | LP (arrow) vs Heavy = 5 DR. Heavy armour vs arrows = near-immunity. HP bolt vs Heavy = only 3 DR — bolt penetrates better, as designed. HBl (lead) vs Heavy = 2 DR only — lead shot penetrates, as designed. Consistent with note in design doc. |
| BG Martial | 1–5 | Unit quality | TTRPG CP (1–7) | BG Martial tops at 5. TTRPG CP effectively uncapped (pool 5–27+). Conversion via B.2 table (not included in params_combat — must be in params_mass_combat or state_transfer_spec). Inconsistency in range does not matter if B.2 table is correct and present. |
| Cohesion | 1–7 (TTRPG), 0–6 (BG) | Integrity scale | — | BG Cohesion 0–6, TTRPG 1–7. Floor difference documented in state_transfer_spec (BG 0 → TTRPG 1). However the ceiling difference (BG max 6, TTRPG max 7) is documented but the reason is not stated. P3: document why BG ceiling is lower. |

---

## MODE C — INTERACTION CHAIN ANALYSIS

| Mechanic | Upstream Inputs | Downstream Outputs | Chain Length | Flags |
|----------|----------------|-------------------|--------------|-------|
| Combat Pool split | Agility, History, Wounds | Offence dice, Defence dice → damage, DR subtraction → Health → Wounds | 4 | Clean linear chain. No circularity. |
| Wound system | Damage, Health threshold | −1D Combat Pool, +1 Ob all rolls, Incapacitation | 2 | Dual penalty (pool AND Ob) — cumulative effect compounds exponentially at high wound counts. At 3 wounds: −3D pool, +3 Ob — effective collapse. This is design-intent per PP-165. No loop. |
| Stamina | Endurance, History, armour, rounds elapsed | Out of Breath (−2D) → Take a Breath action (no offensive capability) | 3 | Stamina depletion + wounds can stack: depleted Stamina (−2D) + 3 wounds (−3D) = −5D from a starting pool. At base pool 15D: 10D remaining with +3 Ob. Severe but recoverable (Take a Breath). **Amplification interaction:** −2D (Stamina) AND −1D per wound stack on same pool. Flag P2: are these intended to stack simultaneously? |
| Fibonacci Group Bonus | Attacker count, unsupported condition | +Offence dice only | 2 | "Unsupported" condition: "target has no allies in the zone." No definition of "in the zone" vs "adjacent zone." If 1 ally is adjacent, is target supported? Gap — see Mode D. |
| Initiative (range-based) | Weapon reach, zone, Agility contest | Priority ordering → damage applies per priority | 3 | Initiative transfers on hit, feint success, or distance change. Three distinct transfer triggers — all documented. Chain clean. |
| Feint | Offence-only roll, Ob 2 | −2D to opponent Defence next exchange | 2 | "Next exchange" = next round? Or next action within same round? Undefined. Gap — see Mode D. |
| Cover | Declared in Phase 1 | DR addition against ranged (stacks with armour) | 2 | Cover + armour DR stacks additively — explicitly stated. LP vs Heavy armour + Hard cover = blocked. Correct. Cover declared in Phase 1 only — timing locked (ED-098 provisional). |
| Disarm | Offence roll vs Str+Agi Ob | Weapon dropped | 2 | Disarm Ob = opponent Str + Agi combined as difficulty. If Str 5 + Agi 5 = Ob 10: practically impossible. At Ob cap 10 this is the hardest possible action. Edge case: Is Ob 10 the hardest achievable via Disarm? Confirm no stacking (wounds → +Ob) would push past 10. Ob cap 10 confirmed in params_core. No stacking past 10. |
| Mass combat damage (PP-086) | Net successes, Ob, disposition modifier | Strength reduction → Cohesion check → Morale check → rout | 4 | PP-086 ambiguity (A-06 above) is upstream of this entire chain. If "net successes over Ob" is interpreted incorrectly, all downstream cascade is wrong. P1 above is critical. |
| Ranged weapon at Close zone | Zone pressure, pool | Full pool to Defence, no Offence | 2 | Rule is clearly stated. But "Melee weapons cannot retaliate against a ranged attack from Far zone" (§5 Reach Rules) — can a melee character at Close zone attack a ranged character also at Close zone? Yes — they are both at Close zone, so melee can attack normally. This is correct. |
| Tie Up | Close range Offence roll | Both at disadvantage, escape requires Strength contest | 3 | "Both parties at disadvantage" is undefined — what is the mechanical effect of "at disadvantage"? Gap — see Mode D. |
| Stunt | GM sets N (max 5) | +N Offence dice | 2 | GM sets N up to 5. No resolution mechanism for contested Stunt claims (player argues 5, GM says 2). Discretionary — by design, but no guidance. P3. |
| Thread in combat (Leap) | Practitioner commits all pool to Defence | ~60% hit probability during Leap | 2 | "~60% hit probability" is cited as a design outcome (§10) — source of calculation not shown. Verified in params? Flag: confirm this probability is based on a known pool size. P3. |

---

## MODE D — GAP DETECTION

| ID | Type | Description | Location | Severity | Status |
|----|------|-------------|----------|----------|--------|
| GAP-CMB-01 | Undefined term | "Disadvantage" in Tie Up action — no mechanical definition. "Both parties at disadvantage next round." | §4 Actions | P1 | OPEN |
| GAP-CMB-02 | Missing resolution | Feint "next exchange" timing — does −2D Defence apply to next round, or rest of current round? | §4 Actions | P1 | OPEN |
| GAP-CMB-03 | Formula conflict | Health formula: design doc §7 says "Health = Endurance score"; params_core says "Health = Endurance + 6." One is wrong. | §7 / params_core | P1 | OPEN |
| GAP-CMB-04 | Missing rule | Critical Hit (net ≥ 3: weapon modifier doubled) appears in params_combat but not in design doc §5. Players reading design doc cannot find this rule. | §5 / params_combat | P1 | OPEN |
| GAP-CMB-05 | Ambiguous formula | PP-086 mass damage: "net successes over Ob" — does this mean net − Ob (can be negative, floored) or successes that exceed Ob (partial = 0)? | §9 / PP-086 | P1 | OPEN |
| GAP-CMB-06 | Undefined condition | Fibonacci "unsupported" — does an ally in an adjacent (not same) zone count as supporting the target? | §8 | P2 | OPEN |
| GAP-CMB-07 | Conflicting value | Fibonacci cap: design doc §8 says "5th+: +5D cap" (meaning 5 attackers triggers cap). Params says "8+: +5D." Is cap at 5 or 8 attackers? | §8 / params_combat | P2 | OPEN |
| GAP-CMB-08 | Missing rule | Dodge action (params_combat Actions Summary) references "ED-067 resolved — provisional" but §4 Actions table in design doc does not list Dodge as a named action. Actions list in design doc ends at Stunt. | §4 / params_combat | P2 | OPEN |
| GAP-CMB-09 | Missing procedure | Ranged vs ranged (mirror match) — stated as "[PROVISIONAL — GAP-PROJ-01]" in params. No resolution procedure exists. | params_combat | P2 | OPEN |
| GAP-CMB-10 | Missing rule | Versatile weapons (Light/Medium/Heavy) appear in the weapon TN table in design doc §5, but params_combat weapon table does NOT include Versatile types. | §5 / params_combat | P2 | OPEN |
| GAP-CMB-11 | Imprecise rule | "typically 3+" for wound trigger — Health is a specific number; the trigger should be stated precisely, not "typically." | §7 | P2 | OPEN |
| GAP-CMB-12 | Missing edge case | Out of Breath (Stamina 0): −2D to all rolls. If simultaneously at max wounds (−3D) and OoB (−2D), total = −5D. Is this additive? Confirmed as likely yes (no exception stated), but not explicitly stated. | §7 / params_combat | P2 | OPEN |
| GAP-CMB-13 | ED-033 open | Commander bonus formula conflict — three formulas extant. Blocks any simulation requiring commander bonus calculation. | §12 open items | P1 | OPEN (editorial) |
| GAP-CMB-14 | ED-040 open | Artillery Balanced disposition lock — intentional? | §12 open items | P2 | OPEN (editorial) |
| GAP-CMB-15 | Missing rule | P2-B11-19: Thread Tension (TT) 80+ effect in mass battle — design doc flags this as open, no rule defined. | §12 | P2 | OPEN |
| GAP-CMB-16 | Provisional unresolved | ED-092: STR in damage formula — unresolved. Melee damage formula does not include STR, but STR minimum table implies STR has mechanical relevance beyond minimum wield. If STR is not in the damage formula, the only role of STR above minimum is: nothing. Is STR above minimum intentionally irrelevant to damage? | §5 / params_combat | P2 | OPEN (editorial) |
| GAP-CMB-17 | Missing rule | Rescue action: "Declare before opponent's attack resolves. Interpose. Requires adjacent zone." — What are the mechanical consequences of interposing? Rescuer takes the hit? Takes half damage? Absorbs one die? No resolution stated. | §4 Actions | P1 | OPEN |

---

## MODE E — CORE PRINCIPLES COMPLIANCE

| # | Principle | Status | Evidence | Flag |
|---|-----------|--------|----------|------|
| 1 | Roll only when meaningful | PRESENT | Combat explicitly rolls only when Strike/Feint/Disarm are declared. No passive rolls. | — |
| 2 | Let It Ride | NOT TESTED | No re-roll prohibition stated in combat doc. Combat is multi-exchange by design — each round is a new declaration, not a re-roll. Principle may not apply to multi-round combat (each round = new stakes). P3: clarify if Let It Ride applies to repeated combat rounds. | P3 |
| 3 | Fail Forward | PARTIALLY PRESENT | Failure in combat (0 damage dealt) = still costs a round of Stamina, which advances state. But Partial success outcome (some successes but below Ob) — combat has no Ob structure (it's Offence vs Defence direct contest), so "Partial" as defined in core doesn't apply. Failure means opponent took no damage. No "failure advances narrative" mechanism stated for combat specifically. P3: consider whether combat failures have a Fail Forward hook. | P3 |
| 4 | Histories, not Skills | PRESENT | Combat Pool = Agi + weapon proficiency History. Lived experience (History) is primary. | — |
| 5 | Pool = Attribute + History bonus | ALTERED (justified) | Combat formula = (Agi×2) + History + 3. Doubling Agility and adding +3 base is a departure from standard pool formula. Alteration documented as design intent (combat is higher-variance than social). | ALTERED — documented |
| 6 | Wound system with +1 Ob per wound | PRESENT | §7 and PP-165 confirm +1 Ob per wound cumulative. | — |
| 7 | Inspiration/Spirit economy | NOT TESTED IN COMBAT | Combat doc does not reference Inspiration. Is Momentum (params_core) the combat analogue? Momentum is gained on Overwhelming success, spent for +1 success. If Momentum ≠ Inspiration, the Spirit economy may be disconnected from combat. Flag P2. | P2 |
| 8 | Beliefs as moral character | NOT APPLICABLE | Combat is mechanical resolution. Belief expression is TTRPG narrative layer. No flag. | — |
| 9 | Social combat via Rhetoric | PRESENT (separate system) | Debate system exists (params_debate). No incursion into personal combat. | — |
| 10 | Reach/Speed priority | PRESENT | §3 Initiative and §5 Reach Rules fully implement reach-based priority. | — |
| 11 | Phase-based combat | PRESENT | §2 Round Structure implements 6-phase structure. | — |
| 12 | Beginner's Luck | NOT MENTIONED | No Beginner's Luck rule in combat doc or params_combat. If untrained characters can attempt combat, their pool = (Agi×2) + 0 History + 3 = minimum 5D. Floor at 5D effectively provides accessibility. Formal Beginner's Luck rule not stated but floor achieves the intent. P3. | P3 |
| 13 | Circles and Resources | NOT APPLICABLE TO COMBAT | — | — |

---

## MODE F — PLAYTEST BURDEN ANALYSIS

| Mechanic | Time(s) | Lookups | Tracking | Decisions | Load | Flag |
|----------|---------|---------|----------|-----------|------|------|
| Pool split (Offence/Defence) | 15s | 0 | 1 (pool total) | 1 (split ratio) | Low | — |
| Strike resolution | 30s | 1 (weapon mod) | 3 (net hits, DR, damage) | 0 | Medium | — |
| Wound application | 10s | 1 (wound table) | 2 (wound count, Ob cumulative) | 0 | Low | — |
| Stamina tracking | 10s | 0 | 1 (Stamina counter) | 0 | Low | — |
| Ranged combat setup | 45s | 3 (zone, DR table, ammo type) | 4 (zone, cover declared?, ammo type, reload status) | 2 (cover declare, ammo) | **High** | P2: 3 lookups at zone establishment; occurs every combat involving ranged |
| Cover declaration | 15s | 1 (cover DR table) | 1 (cover status) | 1 (declare in Phase 1) | Low | P2: timing is a hard constraint — missing Phase 1 declaration = no cover. Likely to be missed by new players. |
| Fibonacci bonus | 20s | 1 (table) | 1 (attacker count in zone) | 0 | Low | — |
| Disarm action | 40s | 2 (target Str, target Agi → Ob calculation) | 2 (Ob, success degree) | 1 | Medium | P2: player must know opponent's Str and Agi to calculate Ob. Information access may be blocked by design. |
| Wound max lookup | 10s | 1 (Endurance bracket table) | 1 | 0 | Low | — |
| Feint chain | 25s | 0 | 2 (success result, −2D carry-forward) | 1 | Medium | P2: carry-forward (−2D next exchange) requires a token or note to track. |
| Mass combat full round | 90s+ | 4+ (formation, disposition, DR, Str) | 6+ (Str, Cohesion, Morale, Ob, breaks, attachments) | 3+ | **High** | **P1: exceeds 90s threshold. Mandatory lookup count >2 per round. Occurs every mass combat round.** |
| Thread-in-combat (Leap) | 60s | 2 (Coherence, Contact Rounds) | 3 (pool committed, Coherence, Contact Rounds) | 1 | **High** | P2: practitioner player must hold multiple Thread-specific values while resolving normal combat for all other participants. |

---

## MODE G — CROSS-MODE CONSISTENCY

State transfer spec confirmed present and non-stale (PP-107 applied, 2026-04-02).

| Mechanic | Modes | Transition Defined? | State Preserved? | Flag |
|----------|-------|-------------------|-----------------|------|
| Combat Pool split | TTRPG | N/A (BG has no split) | BG uses Martial stat (abstraction documented) | — |
| Wound penalties | TTRPG → Hybrid | PARTIALLY | Wounds → +1 Ob CR checks (Hybrid). State_transfer_spec confirms. Wound −1D does NOT apply to BG commander bonus — documented. | — |
| Wound penalties | TTRPG → BG | DOCUMENTED | "Wounds taken by PC general: BG commander bonus unaffected." Confirmed. | — |
| Unit Strength conversion | BG → TTRPG Zoom In | DEFINED | B.2 conversion table: TTRPG Str = ⌈BG Health ÷ 1.5⌉ (PP-107). Confirmed in state_transfer_spec. | — |
| Stamina | TTRPG → Mass Combat | SUSPENDED | "PC Stamina: not tracked during mass combat." Confirmed. | — |
| Fibonacci Group Bonus | TTRPG only | N/A — no BG/Hybrid equivalent defined | BG uses Martial stat. Group bonus has no BG analogue. **Undocumented absence.** | P2: no BG equivalent of flanking/group attack bonus. Tactical depth asymmetry. |
| Feint | TTRPG | Not applicable in BG/Hybrid abstraction | Absent in BG (single roll per engagement). | P3: document explicitly as "Feint is TTRPG-only — no BG equivalent." |
| Cover (ranged) | TTRPG → BG | UNDOCUMENTED | Cover DR rule appears in TTRPG. BG has no cover mechanic referenced. Does BG treat terrain as cover? | **P2: Cover has no BG analogue documented. Territory type does not map to DR.** |
| Ranged weapons (zone requirement) | TTRPG → BG | UNDOCUMENTED | BG unit type (ranged) is mentioned but zone requirement (Far zone) has no BG equivalent. BG uses territory adjacency, not zones. How does "Far zone required to fire" translate to BG? | **P2: Ranged zone requirement has no BG translation documented.** |
| Mass combat damage formula (PP-086) | TTRPG mass / Hybrid | DEFINED (within TTRPG mass layer) | PP-086 mass damage formula is TTRPG mass combat. BG uses different abstraction (unit Martial stat). Transition from TTRPG mass → BG not fully documented for damage. | P2: TTRPG mass → BG Zoom Out damage equivalence not defined. |
| Thread in combat (Coherence) | TTRPG → Hybrid | DEFINED | "Coherence −1 per Thread operation in mass battle (ST-TW-03)." Confirmed in design doc §10. | — |
| Thread in combat → BG | BG | DEFINED (abstractly) | "Thread operations abstracted to Co-Movement cards and faction Thread orders." Confirmed. | — |
| Debate → Conviction Track → BG | TTRPG → BG Zoom Out | PARTIALLY defined | PP-108: "Debate outcome (CT ≥7 or ≤3) → Domain Echo: faction Mandate ±1." Defined. But BG→TTRPG debate Zoom In is P1 gap (K2-F-02) — this is pre-existing, not a combat audit finding. | — |
| Armour DR | TTRPG → BG | UNDOCUMENTED | BG weapon types map to "Anti-Armour keyword and unit type" per §5 design doc. No Anti-Armour keyword definition found in combat doc or params_combat. | **P1: Anti-Armour keyword referenced but undefined.** |

---

## SUMMARY

### P1 Findings (blocks play)

| ID | Description |
|----|-------------|
| GAP-CMB-01 | "Disadvantage" in Tie Up: no mechanical definition |
| GAP-CMB-02 | Feint "next exchange" timing undefined |
| GAP-CMB-03 | Health formula conflict: design doc §7 vs params_core |
| GAP-CMB-04 | Critical Hit rule absent from design doc (params only) |
| GAP-CMB-05 | PP-086 mass damage formula ambiguity |
| GAP-CMB-13 | ED-033: Commander bonus formula conflict (3 formulas) |
| GAP-CMB-17 | Rescue action: no mechanical resolution for interposition |
| G-P1-01 | Anti-Armour keyword: referenced in §5, undefined everywhere |

### P2 Findings (ambiguity / asymmetry)

| ID | Description |
|----|-------------|
| A-07 | Unarmed Def TN 9: ~10% success per die — confirm intent |
| A-10 | ED-092: STR in melee damage — unresolved provisional |
| GAP-CMB-06 | Fibonacci "unsupported" — adjacent zone counts? |
| GAP-CMB-07 | Fibonacci cap: 5 attackers (design doc) vs 8 attackers (params) |
| GAP-CMB-08 | Dodge action: in params but not in design doc §4 |
| GAP-CMB-09 | Ranged vs ranged mirror: no resolution procedure |
| GAP-CMB-10 | Versatile weapons: in design doc §5, absent from params_combat |
| GAP-CMB-11 | Wound trigger "typically 3+" — imprecise |
| GAP-CMB-12 | OoB + max wounds stacking: not explicitly stated additive |
| GAP-CMB-14 | ED-040: Artillery Balanced disposition lock |
| GAP-CMB-15 | TT 80+ effect in mass battle undefined |
| GAP-CMB-16 | STR above wield minimum: no mechanical effect if not in damage formula |
| E-07 | Inspiration/Spirit economy disconnected from combat |
| F-Ranged | Ranged combat setup: High cognitive load, 3 lookups per engagement |
| F-Mass | Mass combat round: >90s, >4 lookups — P1 burden threshold |
| G-Fib | Fibonacci Group Bonus has no BG analogue |
| G-Cover | Cover DR has no BG translation |
| G-Ranged-Zone | Ranged zone requirement has no BG translation |
| G-MassDmg | TTRPG mass → BG Zoom Out damage equivalence not defined |

### P3 Findings (polish)

| ID | Description |
|----|-------------|
| A-01 | No upper cap on Combat Pool |
| A-08 | Fibonacci cap value (5D) stated, but attacker count trigger differs between docs |
| B-Cohesion | BG Cohesion ceiling (6) vs TTRPG (7): reason not documented |
| E-02 | Let It Ride: applicability to repeated combat rounds unclear |
| E-03 | Fail Forward: no combat failure hook |
| E-12 | Beginner's Luck: not explicitly stated (floor at 5D achieves intent) |
| F-Cover | Cover Phase 1 timing: likely to be missed by new players |
| F-Stunt | Stunt N value: no guidance for contested GM adjudication |
| G-Feint | Feint: not documented as TTRPG-only explicitly |

---

## RECOMMENDED IMMEDIATE ACTIONS (P1 resolution order)

1. **GAP-CMB-03 / GAP-CMB-04** — Resolve Health formula conflict. Confirm which is correct (Endurance or Endurance+6). Add Critical Hit rule to design doc §5.
2. **GAP-CMB-17** — Define Rescue mechanical resolution (rescuer absorbs the attack? takes damage instead? halves it?).
3. **GAP-CMB-01** — Define "disadvantage" for Tie Up — suggest: −2D to Combat Pool for both parties.
4. **GAP-CMB-02** — Define "next exchange" for Feint — suggest: next round only.
5. **GAP-CMB-05** — Clarify PP-086 mass damage formula wording.
6. **G-P1-01** — Define Anti-Armour keyword for BG layer.
7. **GAP-CMB-13** — Escalate ED-033 commander bonus conflict for immediate editorial resolution (blocks mass combat simulation).
