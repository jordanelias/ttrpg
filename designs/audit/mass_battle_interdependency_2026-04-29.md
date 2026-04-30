# Mass Battle Interdependency Stress Test — Batch 3
<!-- generated: 2026-04-29 | scope: cross-system — mass_battle×core, ×Thread, ×peninsular_strain, ×derived_stats, ×personal_combat, ×strategic_layer, ×victory -->

---

## CRITICAL — IMMEDIATE ACTION

### [INTER-CRIT-01] RS vs MS — confirmed terminology inconsistency, peninsular_strain_v30 needs global replace
peninsular_strain_v30 uses "RS" (Rendering Stability) throughout.
All other docs (mass_battle, victory_v30, core_params, military_layer) use "MS" (Mending Stability).
Evidence RS = MS (same stat): peninsular_strain L451 uses both RS and MS in the same row ("RS = 0 at Accounting... Recovery: MS to 20"). The recovery target cross-references the wider system's term. The depletion events in peninsular_strain (RS −1 per battle, RS −1/season at Strain 9-10) match mass_battle §E.1 (MS −1 per battle) — same values, different names. Neither RS nor MS is formally defined in any fetched doc with a formula distinguishing them.
Verdict: RS = MS. peninsular_strain_v30 requires global RS → MS replacement.
Until fixed: Godot implementation cannot safely reference peninsular_strain for battle consequences.

### [INTER-CRIT-02] IP direct-trigger: ED-743 not propagated to victory_v30 §0.4 or peninsular_strain Step 4e
mass_battle §E.2 (ED-743): "Battle-occurrence is no longer a direct IP or Strain trigger."
victory_v30 §0.4: "Each season with inter-faction battle: IP +2, Strain +1." [STALE]
peninsular_strain Step 4e: "If Battle occurred this season: IP +2." [STALE]
ED-743 is the authoritative ruling. victory_v30 §0.4 and peninsular_strain Step 4e are stale.
Action: propagate ED-743 to both docs. Strike the direct IP/Strain battle-occurrence lines.
Until fixed: any accounting simulation using peninsular_strain or victory_v30 will double-count IP.

### [INTER-CRIT-03] Campaign Supply cost: per-unit vs flat — canonical conflict
derived_stats §8.1: "Campaign Supply: −100 gold/season per unit in hostile territory."
mass_battle §A.14b: "flat cost regardless of how many units are deployed."
3 units in hostile territory: derived_stats = −300g/season; mass_battle = −100g/season.
These are irreconcilable. One must be struck. The design doc (§A.14b) gives the rationale ("flat cost = logistical overhead"). Recommend: derived_stats §8.1 is updated to match the design doc.

---

## SIGNIFICANT — CROSS-SYSTEM GAPS

### [INTER-09d] Overwhelming vs Critical Hit — two thresholds in mass battle
core_params: Overwhelming = net >= 2×Ob AND net >= 3.
mass_battle §A.7 Phase 5 step 6: Critical hit = net >= 3 (Ob-independent).
Tactic execution uses Overwhelming (2×Ob AND >=3). Damage uses Critical (>=3 only).
Two different thresholds in the same system, for the same net-success quantity, doing different things.
GAP: Is Critical hit the mass-battle equivalent of Overwhelming for damage? Not stated.

### [INTER-10c] Thread Ob in mass battle does not map to threadwork three-axis system
mass_battle §A.10: "Thread Ob = 4" for Battle/Campaign scale.
params/threadwork: Total Ob = Depth + Breadth + Distance. Threadwork depth tiers: Object(1), Personal(2), Relational(3), Field(5), Structural(8). No "Territorial" tier.
A battlefield = Field scale (Ob 5 Depth). §A.10 flat Ob 4 ≠ any threadwork depth tier.
The §A.10 flat Ob may be intended as the total three-axis Ob (not Depth Ob only) — but this is not stated.
GAP: §A.10 Thread Ob is a flat abstraction not reconciled with three-axis threadwork system.

### [INTER-10d] Focus stat has no function in mass battle
params/threadwork: Focus = contact window duration only (contact rounds = Focus stat).
params/mass_combat PP-235: "Focus determines Leap success probability but does not extend contact window at mass scale." Contact window = 1 at mass scale always.
If contact window is always 1 and Focus only governs contact window duration: Focus is a dead stat in mass battle.
GAP: Focus has no defined function in mass battle. Either an unstated secondary function exists, or Focus should be explicitly stated as non-applicable at mass scale.

### [INTER-11a] RS vs MS — see INTER-CRIT-01 above.

### [INTER-12b] "Discipline" name collision: unit stat vs faction derived value
derived_stats §10.2 Army Morale: "Discipline modifier: +1 if faction Discipline ≥ 75% of max."
"Faction Discipline" = Stability × 10 (range 10–70, derived from §8).
mass_battle: "Discipline" = per-unit organisational stat (1–7, tracked on unit tokens).
Army Morale formula uses "Discipline" to mean two different things in adjacent bullet points.
GAP: "Discipline" naming collision between unit-stat (1–7) and faction-derived-value (10–70).
Recommend: rename faction-level derived value to "Cohesion" or "Unit Readiness" to avoid collision.

### [INTER-12d] Campaign Supply: per-unit vs flat — see INTER-CRIT-03 above.

### [INTER-12e] Muster costs: Ob roll AND Treasury cost — relationship not stated
derived_stats §8.1: Levy −50g, Professional −150g, Heavy Infantry/Cavalry −300g, Artillery −500g.
military_layer §1.5: Muster requires Ob rolls. No gold cost mentioned.
Neither doc references the other. Do both apply (Ob roll + Treasury cost), or only one?
GAP: Muster cost mechanism — whether Ob roll (§1.5) and Treasury cost (§8.1) both apply is unspecified.

### [INTER-12f] Campaign-scale defeat consequences missing from derived_stats §8
mass_battle §A.14: "Campaign-scale defeat: Discipline −30, Mandate −1."
derived_stats §8.1 lists "Battle loss: Discipline −15" but not campaign-scale defeat as a separate drain.
The Campaign-scale defeat entry is missing from derived_stats §8.1. Needs to be added.

### [INTER-12g] Unit upkeep — RESOLVED
"Professional" for upkeep purposes = §A.14c definition (Light Infantry and above).
Levy = no upkeep. All others = −25g/season. Consistent.

### [INTER-14a] military_advance Ob vs BG Battle Ob — same event, two resolution systems
faction_layer §2.2: military_advance Ob = 2 + Fort level. Determines Occupation outcome.
mass_battle §B.3: BG Battle pool vs TN7, Ob from tactic table. Determines unit damage and territory control.
QUESTION: Do both fire for the same march, or does BG Battle supersede military_advance?
If both: military_advance outcome (Partial/Success/Overwhelming) and BG Battle outcome (Win/Partial/Lose) could conflict.
If BG Battle only: faction_layer §2.2 Ob table is vestigial.
GAP: Relationship between military_advance Ob roll and BG Battle resolution undefined.

### [INTER-14b] Garrison cost "−1 pool" — undefined pool
faction_layer §2.3: "Garrison cost: −1 pool per occupied territory."
"Pool" not specified. Likely = military_advance roll pool. Not stated.
GAP: Garrison cost pool is undefined.

### [INTER-14c] Accord during Occupation: frozen (§2.3) vs erodes from Battle (peninsular_strain §2)
faction_layer §2.3: "Accord frozen at pre-Occupation value during military contest."
peninsular_strain §2: "Battle in a territory you control (you are defender): Accord −1."
Displaced faction retains control during Occupation (§2.3). A Battle in that Occupied territory → Accord −1 from peninsular_strain. But §2.3 says Accord is frozen.
GAP: Accord during Occupation — frozen or erodes from Battle?

### [INTER-14d] Siege × Occupation simultaneous state — undefined
Siege Action targets Fort ≥ 2 territories. Occupation = military presence marker.
Can a territory be simultaneously Occupied AND Sieged by the displaced faction?
No rule addresses this state.
GAP: Siege × Occupation simultaneous state.

### [INTER-14e] War Authorisation — does it cover Siege Action?
Siege Action uses "Legionary Inward" card. War Authorisation grants free first military_advance.
Siege may not be classified as military_advance. If so, War Authorisation does not apply.
GAP: Whether War Authorisation covers Siege Action undefined.

### [INTER-17b] Knights Templar unit count — inside or outside Military×2 ceiling?
derived_stats §8: Military × 2 = max active units.
military_layer §1.8: KT governed by separate cap (max 2), not Military ceiling.
Does KT count toward Military×2, or is KT count tracked separately?
GAP: KT unit count vs Military×2 ceiling.

### [INTER-17c] Scene→Mass social win bonus: general Command pool or unit combat pool?
scale_transitions: "Social win: +1D to relevant unit Command this turn."
Command is a general stat, not a unit stat. "Relevant unit" implies a specific unit.
GAP: Social win +1D target — general's Command tactic pool or a unit's combat pool?

---

## CONFIRMED CONSISTENT

- Coherence auto-cost: fully consistent across mass_battle §A.10, threadwork, scale_transitions. ✓
- Thread pool formula (Spirit×2 + History + TPS): consistent, applies in mass battle. ✓  
- TroopCount / Size / Health reverse formula: derived_stats §7 confirms and extends mass_battle §A.3/§A.4. ✓
- E-FAIL-01 CLOSED: output scaling (§A.3) and PP-233 are complementary, not conflicting. ✓
- E-FAIL-02 CLOSED: Army Morale modifiers are in derived_stats §10.2 (+1 if Command≥4; −1 if Command≤2). ✓
- TN for Volley (6) consistent with core_params "Controlled" definition. ✓
- Die rule (face-10 = +2) applies in mass battle; no override needed. ✓
- Rout contagion and Morale floor consistent. ✓
- Levy garrison fights Popular Uprising (defensive = permitted). ✓
- Domain Echo timing in Hybrid: queued to Accounting, no mid-battle stat change. ✓ Clean for Godot.
- Muster cost + delay: Treasury cost immediate, unit available next season. Consistent. ✓
- Unit upkeep "professional" = §A.14c definition (Light Infantry and above). RESOLVED. ✓
- General personal combat: uses full personal combat system per scale_transitions. ✓
- Wounds on general: accrue per combat_v30 Wound Interval; +1 Ob per wound to tactic rolls. ✓
- Fibonacci: §A.8 Concentration references personal combat system. Exact value needs personal combat §8. [MINOR]

---

## CLOSED PRIOR GAPS (from Batch 1/2)

- E-FAIL-01: NOT a conflict. Output scaling and PP-233 are two layers of the same system.
- E-FAIL-02: Army Morale modifiers defined in derived_stats §10.2. Add cross-reference to mass_battle.

---

## MINOR / ELEGANT

- [9e] Momentum applicability in mass battle: implicit (non-Thread rolls = eligible). Confirm explicitly.
- [13c] TN for general personal combat during mass battle: default 7 or battle-context 8?
- [13d] Mass Mismatch Penalty has no counterpart in personal combat params — mass-battle-only rule.
- [13e] Fibonacci bonus value for Concentration tactic (exact dice) not specified in mass battle.
- [17e] Muster payment timing (immediate cost, deferred unit) — confirm explicitly in military_layer §1.4.
