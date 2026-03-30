# MULTI-SYSTEM NARRATIVE STRESS TESTS
## Integrated TTRPG sequences: debates → combat → threadweaving → faction mechanics
## Model: Sonnet 4.6 | Date: 2026-03-29
## Purpose: Test system transitions, multi-system state tracking, and identify hybrid handoff points

---

# SCENARIO 1: THE BROKEN TREATY
## Systems tested: Negotiation → Debate → Composure → Combat → Personal Pull → Healing → Faction stat consequences → Knot strain → RS
## Cast:
- **Hanne** (PC): Crown faction leader, Spirit 5, Presence 4, Att 3, Agi 3, End 4, Focus 3, TS 55 (Attuned), Coherence 8 (Dissonant). Belief: "Baralta's alliance is the peninsula's only hope." Inspiration: Duty to the Crown (3 points). Close Knot: Baralta (strain 2/6). History: Court Connections 4, Swordsmanship 3.
- **Rolf** (PC): Hafenmark trade delegate, Spirit 3, Presence 5, Att 2, Agi 4, End 3, STR 4, Focus 2, TS 0. History: Maritime Trade 5, Rhetoric 3, Longsword 4. Weapon: HeavyCut Long.
- **Cardinal Veldt** (NPC): Church representative, Spirit 6, Presence 5, Att 4, TS 72 (Sensitive), Coherence 6 (Dissonant). History: Theological Argument 5, Church Law 4. Conviction: Faith. Rhetoric: Authority.
- **Two Church guards** (NPC): Combat Pool 12, HP 27, HeavyCut Long, Medium armour.

### STATE TRACKER
```
RS: 52 (Strained)
TC: 48
Hanne: HP 40/40, 0W, Coherence 8, Composure = Pres 4 + Att 3 = 7
Rolf: HP 27/27, 0W, Composure = Pres 5 + Att 2 = 7
Veldt: HP 27/27, 0W, Coherence 6, Composure = Pres 5 + Att 4 = 9
```

---

### BEAT 1: Negotiation (Social Rolls)

Hanne negotiates a mutual defence pact with Veldt. This is a Treaty (batch_bc_designs.md: G-038). Hanne leads.

**Roll:** Hanne Presence 4 + Court Connections 4 = 8D, TN 7. Ob set by Veldt's resistance: Church Stability (5) ÷ 2 = Ob 3 (round up).

Hanne rolls 8D: expected 3.2 successes at TN 7. P(≥3) = ~73%.

**Result: Success (3 successes, 0 surplus).** Treaty terms established. Crown and Church agree to mutual border defence for 2 seasons. Faction effect: Crown Influence +1 (alliance demonstration), Church Mandate +1 (Crown legitimacy boosts Church standing).

**Rolf objects.** Hafenmark was not consulted. Rolf's Belief: "Hafenmark's independence depends on balancing Crown against Church." This treaty destabilizes that balance.

**SYSTEM TRANSITION: Negotiation → Debate.** Rolf formally challenges the treaty terms. A Debate begins.

**Finding S1-B1-F01:** Treaty negotiation uses a simple Presence + History roll against faction-stat-derived Ob. Clean. But the treaty's faction stat effects (Influence +1, Mandate +1) apply at Accounting, not immediately. **Mid-session treaty effects are deferred.** The Debate that follows cannot reference the stat changes because they haven't applied yet. No gap — this is correct (Accounting-gated effects).

---

### BEAT 2: Debate (Social Combat)

**Debate structure:** Rolf (challenger) vs Hanne (defender of treaty). Veldt is an observer (may intervene).

**Composure pools:**
- Rolf: Presence 5 + Att 2 = 7
- Hanne: Presence 4 + Att 3 = 7

**Exchange 1:**
Rolf attacks with Rhetoric: Evidence (Maritime Trade 5 as basis — "Hafenmark's trade revenues fund Crown defence; exclude us and the funding collapses"). Pool: Presence 5 + Rhetoric 3 = 8D, TN 7. Rolls 3 successes.

Hanne defends with Rhetoric: Appeal ("The peninsula cannot survive divided — this treaty is about survival, not politics"). Pool: Presence 4 + Court Connections 4 = 8D, TN 7. Rolls 2 successes.

**Rolf wins exchange by 1.** Hanne loses 1 Composure: 7 → 6.

**Fibonacci check (PP-133):** Rolf has no allies in the Debate. Veldt is observing. Even if Veldt joined Rolf's side: **PP-133 explicitly excludes Fibonacci from Debates.** No group bonus. Correct.

**Exchange 2:**
Hanne attacks: "You'd let the Southernmost consume us all to preserve your shipping lanes?" (Appeal + Belief bonus). Hanne's Belief ("Baralta's alliance is the only hope") is directly relevant — this IS the alliance. **Belief bonus: +1D** (per Inspiration mechanic? Or per Belief relevance?).

**GAP S1-01: Belief bonus to Debate rolls.** Current rules don't specify a Belief bonus to social combat. Inspiration can be spent for +1D per point, but Beliefs are not Inspirations. **Patch PP-144:** When a character argues FROM a Belief they hold, they gain +1D to the exchange (the conviction is genuine; the argument has weight). This is a one-time bonus per Debate per Belief — not stackable across exchanges. A character arguing against their own Belief: -1D (the argument rings hollow).

Hanne: 8D + 1D(Belief) = 9D, TN 7. Rolls 3 successes.
Rolf defends: 8D, TN 7. Rolls 2 successes.

**Hanne wins by 1.** Rolf loses 1 Composure: 7 → 6.

**Exchange 3:**
Rolf escalates. Calls Hanne a Crown puppet. Personal attack.

**Rhetoric: Authority** (available to Rolf? Rolf's style is unspecified — he's a trade delegate, not Authority-type). Rolf uses Evidence again: "Three treaties in the last decade. Crown broke two. This one will be no different."

Rolf: 8D, TN 7. Rolls 4 successes (strong roll).
Hanne: 8D + 1D(Belief) = 9D, TN 7. Rolls 2 successes.

**Rolf wins by 2.** Hanne loses 2 Composure: 6 → 4.

**Composure at 4:** Hanne is losing the Debate. If Composure reaches 0: Rattled (social consequences, cannot initiate social actions for remainder of scene).

**Hanne considers using Inspiration.** Duty to the Crown (3 points). Spend 1 point: +1 automatic success on next social roll. Points: 3 → 2.

**Exchange 4:**
Hanne, desperate, pivots to emotional appeal. "I was at the border when the last incursion came through. Were you?" Leveraging personal experience.

Hanne: 9D + 1 auto success (Inspiration). TN 7. Rolls 4 successes + 1 auto = 5.
Rolf: 8D, TN 7. Rolls 3 successes.

**Hanne wins by 2.** Rolf Composure: 6 → 4.

**Score: Hanne 4 Composure, Rolf 4 Composure.** Debate is tight. Both damaged.

**Finding S1-B2-F01 (P2):** Debate pacing — 4 exchanges, both at half Composure. At Composure 7, Debates last ~6-8 exchanges. This is 6-8 rounds of social combat. In a table session: ~20-30 minutes of Debate. Feels right for a significant political confrontation. **No pacing issue.**

**Finding S1-B2-F02 (P2):** Inspiration spending in Debates is powerful — auto-successes bypass dice variance. A character with Inspiration 5 can add 5 auto-successes across the Debate, nearly guaranteeing 5 exchange wins. **Inspiration is the social combat equivalent of Thread operations in physical combat — a trump card for invested characters.** Correct by design (Inspiration IS the personal investment mechanic).

---

### BEAT 3: Veldt Intervenes (Thread Operation Mid-Debate)

Veldt has been observing. Veldt's Conviction: Faith. The treaty serves Church interests. Rolf's opposition threatens Church Mandate.

**Veldt Diagnoses Rolf's configuration.** TS 72 — full perception of Rolf's thread. Veldt perceives: Rolf's configuration is tight around his mercantile identity. His arguments are genuine — he IS his trade connections. His thread is firmly actualized around Hafenmark independence.

**Veldt decides to Weave on the Debate's relational configuration — stabilizing the treaty agreement itself.** Relational Weaving, Ob 3.

**SYSTEM COLLISION: Thread operation during active Debate.** What is the interaction?

**Action economy:** Veldt is an observer, not a Debate participant. Observers don't take Debate actions. Veldt's Thread operation is a separate action track running parallel to the Debate.

**Veldt's sequence:** Diagnosis round (simultaneous with Exchange 4 above). Next round: Leap. Pool: Att 4 + History (Theological Argument) 5 + TPS 7 = 16D, TN 7, Ob 1. Auto. Contact established. Next round: Relational Weaving on the treaty configuration. Pool: Spirit 6 + History 5 + TPS 7 = 18D, TN 7, Ob 3. P(≥3) = ~98%.

**Effect of Relational Weaving on a Debate's subject:** The treaty is stabilized at the Thread level. The configuration of the agreement is drawn toward coherence. Mechanically: what does this do to the Debate?

**GAP S1-02: Thread operation effect on active social combat.** No rule specifies how Weaving on a relational configuration affects an ongoing Debate about that configuration.

**Patch PP-145:** Relational Weaving on the subject of an active Debate grants the side defending the Woven configuration +2D to their next exchange (the agreement's Thread-level coherence strengthens their argument — reality is literally on their side). The opposing side perceives nothing (TS 0) but feels their arguments becoming less convincing — the words ring hollow against a configuration that has been stabilized.

This is NOT mind control. The Weaving doesn't change anyone's beliefs. It stabilizes the agreement's configuration, making arguments against it feel less coherent (because the configuration IS more coherent). The opponent's Beliefs remain intact. Their arguments remain logically valid. They just... don't land as hard.

**Detection:** Rolf (TS 0) cannot perceive the operation. If a TS 30+ ally were present, they'd sense an operation in the scene.

**Coherence cost:** -1 (Relational scale). Veldt: 6 → 5. Now at Dissonant threshold border.

**RS cost:** 0 (success).

**Finding S1-B3-F01 (P1): Thread operations during Debates are extremely powerful and nearly undetectable.** A practitioner observer can tip a Debate by Weaving on the subject. +2D is significant — it would have given Hanne 11D on Exchange 4 instead of 9D. The opponent has no counter unless they have a TS 30+ ally to detect the operation and a practitioner ally to counter-Weave.

**Finding S1-B3-F02 (P1): This is the social equivalent of the Pull-Bot.** A practitioner who Weaves on Debate subjects can dominate political outcomes. The cost (Coherence -1 per Debate) is the only limiter. Over 10 Debates: Coherence drops by 10 (from 10 to 0). **A dedicated social-manipulator practitioner can influence ~8 Debates before Rendering Crisis.** This is a campaign-defining number of political interventions.

**[EDITORIAL: Is +2D correct for Thread-boosted Debate? Could be +1D (subtler) or a flat bonus success (more reliable). The magnitude determines how dominant Thread manipulation is in politics.]**

---

### BEAT 4: Debate Erupts into Combat

**Exchange 5:** Hanne, boosted by Veldt's Weaving (+2D per PP-145):
Hanne: 9D + 2D(Weaving) = 11D, TN 7. Rolls 4 successes.
Rolf: 8D, TN 7. Rolls 2 successes.

**Hanne wins by 2.** Rolf Composure: 4 → 2.

Rolf, at Composure 2, realizes he's losing. His Belief ("Hafenmark's independence depends on balancing Crown against Church") is being crushed. He perceives the argument is somehow wrong — his points aren't landing — but can't identify why.

**Rolf snaps.** Draws his longsword. Debate is over. Combat begins.

**SYSTEM TRANSITION: Debate → Combat.** All Debate effects persist. Both characters carry their Composure damage (social strain). Rolf is at Composure 2 (near Rattled).

**Does Composure damage affect combat?** Composure is a social damage buffer. It does not map to physical combat stats. No combat penalty from low Composure. But:

**GAP S1-03: Transitioning from Debate to Combat — carryover effects.** When a Debate erupts into violence, do any social states carry?

**Patch PP-146:** Composure damage does not affect combat pools. But a character at Composure 0 (Rattled) who enters combat is still Rattled: -2D to social rolls (relevant if they try to negotiate mid-fight, call for surrender, or command allies). Composure recovers naturally after the scene. **The emotional state is carried; the mechanical penalty is limited to social actions.**

Additionally: the character whose Composure broke (if any) gains **Momentum -1** (they enter combat emotionally destabilized — not a Momentum bonus, a deficit that must be overcome before Momentum can accumulate). Characters who won the Debate: no combat bonus (winning an argument doesn't make you fight better).

**Combat state:**
```
Rolf: HP 27/27, 0W, Composure 2, HeavyCut Long (TN 6/7, +5). Pool: (4×2)+4+3=15D. Stamina: 3+4+1=8.
Hanne: HP 40/40, 0W, Composure 4, LightCut Short (TN 5/6, +2). Pool: (3×2)+3+3=12D. Stamina: 4+3+1=8.
Veldt: In contact (Leap succeeded earlier). 2 operation rounds remaining.
Church Guard A: Pool 12, HP 27, HeavyCut Long, Medium armour.
Church Guard B: same.
```

**Round 1 (Rolf strikes first — higher Agi):**
Rolf declares Strike on Hanne. Hanne declares Dodge (no weapon drawn — she was in a political meeting).

**Hanne is Unarmed.** Hit TN 8/Def TN 9. Hanne's 12D defence at TN 9: expected ~2.4 successes. Rolf 10D offence at TN 6: expected ~5.0 successes. Excess: ~2.6. Damage: 2.6 + 4(STR) + 5(HCut) = 11.6. DR from no armour: 0.

**Hanne takes ~12 damage.** 40 → 28. Crosses 30 threshold: 1W, -1D.

**Hanne's Knot (Baralta) strain:** Hanne is in a political scene that has turned violent. Does this affect Baralta Knot strain? No — Baralta isn't present. Knot strain comes from Intelligibility decay, Composure buffering, Calling, and external events. Combat damage to Hanne doesn't directly strain the Baralta Knot unless Hanne uses the Knot.

**Hanne considers Calling her Knot.** Call a Knot: +2 strain, +3D to any roll related to the Knot's relationship. Is combat with a political opponent "related to" the Baralta alliance? Arguably yes — Hanne is fighting to defend the treaty that embodies the alliance. **GM judgment: yes.** Hanne may Call Baralta for +3D to her next roll. Strain: 2 → 4 (approaching wrongness threshold of 6 for Close Knot? Threshold is 3 strain for Close Knot wrongness — Hanne's Baralta Knot is ALREADY past wrongness at strain 4.)

**Finding S1-B4-F01 (P2):** Calling a Knot mid-combat is powerful (+3D) but strain 4 immediately puts a Close Knot past wrongness threshold (3). Baralta will sense something is wrong about Hanne. If Hanne Calls again: strain 6 = Crisis. The Knot as a combat resource is a one-shot boost with severe relational consequences.

---

### BEAT 5: Veldt Threads Mid-Combat

Veldt is still in contact from the Debate-phase Weaving. 2 operation rounds remaining. Veldt redirects: Personal Pull on Rolf (Ob 2). Pool: 18D, TN 7, Ob 2. Auto.

**Rolf at -2D.** Pool drops from 15D to 13D.

**Detection:** Rolf (TS 0) perceives nothing. He just feels... slower. Less certain. His arms don't move the way they should. This is the rendering destabilization — his physical coordination is loosened.

**Next operation round:** Veldt Weaves on Hanne (Personal, Ob 2 + 1 Overweave = Ob 3). Healing. Pool: 18D, TN 7, Ob 3. ~98%. Restores (4+6) = 10 HP. Hanne: 28 → 38. Above 30 threshold. Wound removed. Pool penalty removed.

**Veldt's contact drops end of this round (Focus exhausted).** Veldt returns to rendering. Coherence cost: -1 (Relational Weaving earlier) already paid. Personal ops: 0 additional cost. Veldt Coherence: 5.

**State after Veldt's intervention:**
```
Rolf: HP 27/27, 0W, -2D (Pulled), Pool 13D effective. Composure 2.
Hanne: HP 38/40, 0W (healed), Pool 12D. Composure 4.
Veldt: Contact dropped, Coherence 5, Combat Pool 7D (low — scholar, not fighter).
```

**The fight is now 3v1 (Hanne + Veldt + 2 guards vs Rolf).** Rolf at -2D and outnumbered.

**Rolf's only option:** Withdraw or surrender.

**Finding S1-B5-F01 (P1): Thread operations during the Debate-to-combat transition are seamless.** Veldt's contact window from the Debate carries into combat. The practitioner who was Weaving on the treaty now Pulls an attacker and heals an ally — all within the same contact window. **No system boundary between Debate-phase and combat-phase Thread operations.** This is correct (contact is contact regardless of what non-Thread scene is happening around it) but makes practitioners who begin threading during social scenes effectively pre-buffed for combat: they skip the 2-round setup cost because they Leaped during the Debate.

**[HYBRID NOTE: In hybrid mode, Debate occurs during Personal Phase. If combat erupts mid-Debate, it remains in Personal Phase (TTRPG rules). Thread operations carry across the transition. No hybrid handoff issue — this is entirely within one phase.]**

---

### BEAT 6: Aftermath — Faction Consequences

**Treaty status:** The Weaving stabilized the treaty's configuration, but Rolf's violence constitutes a treaty violation by Hafenmark.

**PP from batch_bc_designs (G-036 — Treaty betrayal):**
- Rolf attacked a treaty party. Hafenmark receives: Stability -1 (2 seasons), casus belli granted to Crown, Grievance Marker from Church.
- Rolf individually: Reputation damage with Crown and Church. -1D to Circles rolls with both factions for 2 seasons.

**RS consequence from Veldt's Weaving:** Success at Relational scale = RS unchanged. But the Over-Actualisation hazard applies: subsequent Thread operations targeting this treaty configuration +1 Ob. The treaty is now brittle.

**If Rolf or Hafenmark attempts to break the treaty by force later:** The Woven treaty may shatter into a Relational Shifting Object (per brittleness sidebar). A political agreement shattering at the Thread level produces: RS -1, social wrongness in the zone (all TS 10+ observers perceive the "breaking" of something beyond the political), and the treaty's terms unravel not just politically but ontologically.

**Finding S1-B6-F01 (P2):** Treaty Weaving creates a metaphysical trap. Breaking a Woven treaty damages the substrate. This is a powerful deterrent — and a powerful weapon. A faction that Weaves all its treaties can punish treaty-breakers with RS damage. The Church, with TS 72 Veldt, could systematically Weave every agreement they participate in, making treaty-breaking structurally dangerous. **This is a viable Church strategy for political dominance through Thread manipulation of the political fabric.** Philosophically consistent with P-01 (inseparability): political agreements ARE configurations in the rendered world. Weaving them has Thread consequences.

---

### SCENARIO 1 SUMMARY

**Systems exercised:** Negotiation (social roll), Debate (4+ exchanges, Composure tracking, Rhetoric, Inspiration spending), Thread operations during Debate (Relational Weaving), Debate→Combat transition (Composure carryover), Combat (pool split, wound tracking, Unarmed rules), Thread operations during combat (Pull, heal), Knot strain (Call a Knot), Faction consequences (treaty betrayal), RS and Coherence tracking, Over-Actualisation, Belief bonus.

**State changes across scene:**
```
RS: 52 → 52 (unchanged — Weaving success, no degradation)
TC: 48 (unchanged this scene — Church operations were Thread, not institutional)
Hanne: HP 40→28→38, Composure 7→4, Knot Baralta strain 2→4 (past wrongness), 0W.
Rolf: HP 27 (undamaged but Pulled -2D), Composure 7→2, Reputation damaged.
Veldt: Coherence 6→5. Contact used.
Hafenmark: Stability will drop -1 at Accounting. Grievance Marker from Church.
Crown: Influence will gain +1 at Accounting.
```

**New patches:** PP-144 (Belief bonus to Debate), PP-145 (Weaving effect on Debate), PP-146 (Debate→combat carryover).

**Gaps found:** 3 (all patched inline).

**P1 findings:** 2 (Thread manipulation of Debates is dominant; contact window carries across system transitions).

---

# SCENARIO 2: THE SIEGE OF EHRENFELD
## Systems tested: Mass combat → Zoom In → Personal combat → Siege → Thread bombardment → Lock → Mending → TS growth → Faction Domain Actions → Territory effects → Scale transitions
## Cast:
- **Sigrid** (PC): Löwenritter officer, Spirit 4, Presence 3, Agi 4, End 5, STR 5, Focus 1, TS 0. History: Military Campaign 5, Fortification 3. HeavyCut Long, Heavy armour. Belief: "Ehrenfeld will not fall while I breathe." Combat Pool: (4×2)+5+3=16D. HP: 44.
- **Torben** (NPC): TS 82 (Sensitive), Spirit 5, Att 5, Focus 5, End 3. Varfell-aligned. Coherence 7. Present to perform Thread operations during the siege.
- **Crown assault force:** 3 units (2 HeavyCut infantry, 1 HeavyBlunt specialist). Officer: Presence 4, Military 4.
- **Löwenritter garrison:** 2 units (1 HeavyCut elite, 1 LightCut skirmisher). Fortification level 3.

### STATE TRACKER
```
RS: 48 (Fragile band — Shifting Objects spawn spontaneously)
TC: 55
Ehrenfeld: Fortification 3, Garrison Cohesion 4, Prosperity 3.
Crown attacking: 3 units, Military 5.
Löwenritter defending: 2 units, Military 4.
Torben: HP 27/27, Coherence 7, Contact Rounds: 0 (not in contact).
```

---

### BEAT 1: Siege Declaration (Domain Action)

Crown declares Siege order on Ehrenfeld. Per G-047 (siege mechanic):
- Attacker options: Assault, Starve, Bombard, Negotiate, Thread Bombardment.
- Crown chooses **Assault** (Military vs Fortification + Garrison bonus).

**Siege roll:** Crown Military 5 vs Ehrenfeld Fortification 3 + Garrison bonus (Cohesion 4 ÷ 2 = +2) = Ob 5.
Crown rolls: 5D (Military score as pool? Or Military + officer History?).

**GAP S2-01: Siege roll pool composition.** G-047 lists "Military Ob = [target]" but doesn't specify the attacking pool.

**Patch PP-147:** Siege assault pool = faction Military score + commanding officer's Military History bonus. Crown: 5 + 4 = 9D, TN 7, Ob 5. P(≥5 on 9D) = ~54%. Coin flip — as sieges should be.

**Result: Partial (3 successes, needed 5).** Assault partially succeeds. Per G-047: "Success: garrison Cohesion -2." Partial isn't defined in G-047.

**GAP S2-02: Siege Partial result.** G-047 has Success/Overwhelming/Failure but no Partial.

**Patch PP-148:** Siege Partial = attacker gains foothold but doesn't breach. Garrison Cohesion -1 (half of Success). Fortification undamaged. Attacker loses 1 unit strength (casualties from failed assault).

**State after Assault:**
```
Crown: 3 units → 2.5 effective (1 unit damaged).
Ehrenfeld: Garrison Cohesion 4 → 3. Fortification 3 (intact).
```

**Siege continues next season.** Per G-047: each season of siege TT +1 (now RS -1). RS: 48 → 47.

---

### BEAT 2: Thread Bombardment (Season 2)

Crown brings Torben forward. Torben attempts Thread Bombardment per G-047: "Practitioner Thread Bombardment: Weaving or Pulling at Structural scale against fortification."

**Torben's operation:** Structural Pulling on Ehrenfeld's fortification configuration. This is a Structural-scale operation — the fortification IS a Structural configuration (a built environment with deep temporal weight).

Pool: Spirit 5 + History (assume Einhir Scholar 4) + TPS 8 = 17D. TN 7. Structural Pulling: Ob? Structural = Ob 5 (from Weaving table). Pulling Ob depends on actualization: fortification is firmly actualized (old, maintained) = Ob 3. But Structural scale minimum Ob... there's no Pulling-specific Ob-by-scale table. Pulling uses actualization level, not scale.

**GAP S2-03: Pulling Ob does not scale with target scale.** Pulling Ob = actualization level (1-5). A Structural target that is "normally actualized" is Ob 2 regardless of scale. This means Pulling a fortress wall costs the same as Pulling a door handle. The scale shows up in TS requirements (Structural = TS 70+) and Coherence cost (-2 at Structural), not in Ob.

**Is this correct?** Philosophically: Pulling engages the actualization level of the target — how firmly it's rendered. A firmly actualized fortress wall (Ob 3) is harder to Pull than a loosely actualized fence (Ob 1) regardless of scale. The scale determines the DEPTH of engagement (and thus TS requirement and Coherence cost), not the difficulty of the Pull itself.

**This seems right but has an implication:** a TS 70 practitioner can Pull on Structural targets at Ob 2-3 with 17D pools — near-certain success. The cost is Coherence -2 (Structural scale). **Structural Pulling is easy to execute but expensive in Coherence.** A practitioner can perform ~5 Structural Pulls before Coherence Crisis (from 10 to 0). Each Pull loosens a Structural configuration.

**Torben's Pull:** 17D, TN 7, Ob 3. P(≥3) = ~97%. Success.

**Effect on fortification:** The fortification's configuration is loosened. Per GP-03, Pulling on equipment = -1 stat. But fortification isn't a weapon or armour — it's a territory feature with a Fortification score. **Pulling on a fortification: Fortification -1 for Pull duration (end of scene at 0 surplus, end of session at 1 surplus, seasonal at 2+).** Torben got 3 successes, needed 3: 0 surplus. Duration: end of scene. Fortification 3 → 2 for this scene.

**But Torben is at Structural scale:** Coherence -2. Torben: 7 → 5. Entering Dissonant.

**RS unchanged** (Pull success).

**Implication for next assault:** Crown assaults again. Ob drops from 5 (Fort 3 + Garrison bonus) to 4 (Fort 2 + Garrison bonus adjusted). Crown: 9D, Ob 4. P(≥4) = ~73%. Much better.

**Finding S2-B2-F01 (P1): Structural Pulling on fortifications is devastatingly effective.** Near-certain success, immediate Fortification reduction, enables subsequent assault. **A single practitioner can reduce any fortification by 1 per scene for Coherence -2.** Two operations across two seasons: Fortification 3 → 1. The fortress becomes trivially assaultable. **Thread Bombardment is the siege-breaker — no conventional fortification can withstand sustained practitioner assault.** This is intentional (practitioners are terrifying) but may need balancing: either Fortification should provide DR against Thread operations, or Structural Pulling should require higher Ob against built structures.

---

### BEAT 3: Zoom In — Personal Scale During Siege

**Sigrid declares a sortie.** Per G-047 defender options: Sortie = Military Ob = attacker garrison ÷ 2.

But Sigrid wants to personally lead the sortie. **Scale transition: Zoom In from mass combat to personal combat.**

**Per G-002 (scope transition mechanic):** Zoom In = switch from domain/mass to personal scale. The mass combat continues around the personal scene. Sigrid's unit provides context (they're fighting around her) but Sigrid resolves personally.

**Sigrid charges toward Torben** (the practitioner performing Thread Bombardment). She must cross the battle zone and reach him before he completes his next operation.

**Distance:** Torben is behind Crown lines. Sigrid must: (1) break through Crown front line, (2) reach Torben in the rear.

**Crown front line:** 2 guards engage Sigrid. 2v1 with Fibonacci +1D each.
Guard A: 12D + 1D = 13D. Guard B: 12D + 1D = 13D. Sigrid: 16D, splits defence: 8D each.

Guard A offence (7D + 1D Fib = 8D at TN 6): ~4 successes. Sigrid defence (8D at TN 7): ~3.2 blocks. Excess: ~0.8. Damage: 0.8 + 3(STR) + 5(HCut) = 8.8. DR Heavy vs HeavyCut: 5. Net: ~3.8 damage.
Guard B: same. ~3.8 damage.
**Total damage per round: ~7.6.** Sigrid at 44 HP: takes first wound threshold at 33 HP. **~2 rounds to first wound.**

Sigrid offence: she doesn't attack guards — she uses **Establish Distance** to push through. Agility + Swordsmanship? No — Establish Distance is a combat action for changing range, not for movement past enemies. **Sigrid needs a Withdraw action** to disengage, then movement to reach Torben.

**GAP S2-04: Disengaging from melee to reach a different target.** The combat system has no explicit "run past enemies to reach a target behind them" action. Withdraw is §8.4 (not in the compiled stage8_combat.md I have). Closest: Rescue (join an ally's engagement) but there's no ally engaged with Torben.

**Patch PP-149:** Breaking through an engagement to reach a rear target = declare "Break Through" as action type. Roll Offence dice at TN 7 vs each engaged opponent's Offence successes. Success: you leave the engagement and enter the next zone. Failure: you're still engaged and each opponent gets a free Strike (+2D, as you turned your back). **High-risk action with severe failure consequences.** Correct — charging through enemy lines should be dangerous.

Sigrid: 10D offence at TN 7 vs Guard A (7D offence at TN 6 = ~3.5) and Guard B (~3.5). Sigrid needs ≥ 3.5 on each. At 10D TN 7: ~4.0 expected. Close but probably succeeds. If she fails against either: that guard hits her with +2D.

**Assuming Sigrid breaks through (Round 2):** She reaches Torben.

---

### BEAT 4: Sigrid vs Torben — Fighter vs Practitioner

Torben: Combat Pool 7D (Agi 1×2 + History 2 + 3). HP 27. No armour. No weapon (scholar-practitioner).
Sigrid: 16D (possibly -1D at 1W = 15D). HP 44 (minus ~15 damage = ~29, 1W). HeavyCut Long, Heavy armour.

**This is X-03 in practice.** Optimized fighter vs mid-tier practitioner without bodyguards.

Sigrid splits 10/5 (heavy offence). Torben at 7D defence.
Sigrid hits: 10D at TN 6 = ~5.0. Torben blocks: 7D at TN 7 = ~2.8. Excess: ~2.2.
Damage: 2.2 + 5(STR) + 5(HCut) = 12.2. DR: 0 (Torben has no armour). **12 damage per round.**
Torben at 27 HP: 27→15 (crosses 18, 1W). **One hit puts Torben at 1W, -1D.**

**Round 2:** Torben at 6D (7-1W). Defence: 6D at TN 7 = ~2.4. Sigrid: ~5.0. Excess: ~2.6. Damage: 12.6. Torben: 15→2 (crosses 9, 2W). **Two hits, two wounds, near-incapacitation.**

**Round 3:** Torben at 5D. Defence: ~2.0. Sigrid: ~5.0. Excess: ~3.0. Crit? Excess ≥ 3: yes. Damage: 3.0 + 5 + 10(doubled mod) = 18. Torben: 2→0. **Incapacitated.**

**Torben killed in 3 rounds.** If Torben tries to thread: Diagnosis (Round 1, Defence-only at 7D — Sigrid hits for 12). Leap (Round 2, Defence-only at 6D — Sigrid hits for 13). Torben is dead before contact establishes.

**Finding S2-B4-F01:** Confirms X-03. A practitioner without bodyguards dies in 3 rounds against an optimized fighter. **Torben needed at least 2 bodyguards to survive long enough to thread.** The sortie — Sigrid breaking through lines to reach the practitioner — is the correct tactical counter to Thread Bombardment. **This is a valid and important tactical option that conventional military forces can execute.**

**Finding S2-B4-F02 (P2):** TS growth check for Sigrid? She is TS 0, End 5, Spirit 4. She just killed a TS 82 practitioner in melee. Did she witness a Thread operation? Torben was Pulling on the fortification — but Sigrid has TS 0, so she perceived nothing Thread-related. **No Discovery Event. No TS growth.** Killing a practitioner in combat does not expose you to Thread reality unless you WITNESS the operation (TS 10+ required for passive perception). Sigrid just killed a man. A strange, scholarly man. She doesn't know what he was doing.

**But if Torben had time to Leap and Sigrid observed the physical effects** (a wall loosening, stones shifting): that's a "qualifying event" for TS growth if Sigrid holds the confrontation. Spirit check + Belief bonus, TN 7, Ob 1. Sigrid Spirit 4: P(≥1) = ~76%. At +5 TS: Sigrid reaches TS 5 (still Inert, but tracking). **Killing a practitioner mid-operation can trigger the non-practitioner's Thread awakening** — the irony of the anti-Thread warrior beginning their own Thread sensitivity arc.

---

### BEAT 5: Mass Combat Resolution + Territory Consequences

Crown assault continues with reduced fortification.

**Assault roll:** 9D, TN 7, Ob 4 (Fort 2 + Garrison 1 [Cohesion 3÷2]). P(≥4) = ~73%.

**Result: Success.** Crown breaches Ehrenfeld. Garrison Cohesion -2 → 1. Fortification breached (0 remaining).

**Territory control shifts.** Crown controls Ehrenfeld. Löwenritter faction: Military -1 (lost a defensive position). Löwenritter Stability check triggered: roll Stability vs Ob 1.

**Löwenritter coup trigger check:** Ehrenfeld is a Löwenritter core territory. Losing it triggers coup monitoring per NPC AI. If additional conditions met: Ehrenwall (Löwenritter commander) may attempt coup against Crown.

**RS during siege season:** -1 (siege stress) + -1 (Torben's Structural Pull consequence — wait, Pull success = RS unchanged. But the siege itself = RS -1/season). RS: 47 → 46.

**TC during siege:** Crown military action has no TC effect unless Church is involved. TC 55 unchanged.

**Finding S2-B5-F01 (P2):** Territory control changes trigger multiple faction systems simultaneously: Military stat adjustment, Stability check, coup monitoring, Prosperity recalculation, supply line checks (G-056). A single siege resolution cascades through 5+ subsystems. **All of these are Accounting-gated** — they apply at season end, not mid-scene. The GM must track which effects are pending and apply them at the correct time. **Bookkeeping is significant but manageable with a Faction Dashboard.**

---

### SCENARIO 2 HYBRID NOTES

| Beat | TTRPG | Board Game | Hybrid Handoff |
|---|---|---|---|
| Siege declaration | Domain Action (implicit) | Siege order (explicit) | Strategic Phase: Siege order placed. If PC leads: Zoom In at Personal Phase. |
| Thread Bombardment | Full threadweaving sequence | Weave order vs Fortification | Strategic Phase: Weave order resolves mechanically. No Coherence cost unless PC leads (PP-145 from threadweaving_v25.md §7.2). |
| Sortie/Zoom In | Personal combat scene | N/A (board game has no personal scale) | Personal Phase: GM creates sortie scene. Board game paused. |
| Mass combat resolution | Zone-based operational | Disposition table (single roll) | Strategic Phase: disposition table. Personal Phase: Zoom In scenes. |
| Territory consequences | Accounting | Accounting (same) | Cascade Phase: all effects applied simultaneously. |

**Hybrid gap identified (S2-HYB-01):** Thread Bombardment during siege exists in both TTRPG (full sequence) and board game (Weave order). In hybrid: does the practitioner Zoom In to perform the Bombardment personally (TTRPG rules, full Coherence cost) or abstract it (board game Weave order, no personal Coherence cost unless PC leads)? **The PC leadership rule from §7.2 applies: if a PC practitioner leads the operation, they pay full Coherence cost and roll full TTRPG rules. If NPC-led: board game abstraction, no PC Coherence cost.** This creates a meaningful player choice: lead the operation (better odds, personal Coherence cost) or delegate (worse odds, no cost).

---

# SCENARIO 3: THE COURT OF WHISPERS
## Systems tested: Impression Track → NPC relationship → Circles → Belief challenge → Debate (Grand Debate / Excommunication) → Thread counter-operation → Heresy Investigation trigger → TC threshold
## Cast:
- **Maren** (PC): Church Inquisitor (undercover as a court advisor). Spirit 5, Presence 4, Att 4, Agi 2, End 3, Focus 4. TS 62 (Attuned). Coherence 9. History: Church Law 5, Investigation 4, Theology 3. Belief: "The Church's authority is divine — Thread operations by non-Church practitioners are heresy." Close Knot: Cardinal Veldt (strain 1/3). Impression Track with Duke Vaynard: 3/5.
- **Vaynard** (NPC): Duke. Spirit 4, Presence 5, Att 3, Focus 2. TS 14 (Inert). History: Political Maneuvering 5, Intelligence 4. Conviction: Reason. Private Collection available.
- **Almud** (NPC): Countess. TS 85 (Sensitive). Spirit 6, Att 5, Focus 5, Presence 3. Coherence 6. History: Einhir Scholar 5, Court Connections 3. Present but not openly a practitioner.
- **Court audience:** 12 NPCs of varying rank. 3 have TS 10-29 (sense wrongness). 1 has TS 35 (senses operations).

### BEAT 1: Impression Track Advancement

Maren has been cultivating Vaynard for 3 sessions. Impression Track at 3/5. This session: Maren provides Vaynard with intelligence about Church troop movements near Varfell borders (genuine intel, given with Church approval as bait for a larger investigation).

**Impression Track roll:** Presence 4 + Investigation 4 = 8D, TN 7, Ob 2 (Vaynard's caution). P(≥2) = ~97%.
**Success.** Impression Track: 3 → 4.

At Impression Track 5: Vaynard can become an Inspiration focus for Maren (per G-040). But Maren's Belief condemns Vaynard's Thread-curiosity. The Impression Track is building toward a relational bond that contradicts Maren's Belief. **This is a Belief challenge — the game's primary character development mechanic.**

**Finding S3-B1-F01 (P3):** Impression Track building toward Inspiration that contradicts a Belief creates automatic character tension. No rule forces the contradiction — it emerges from play. The player will eventually face: abandon the Belief (character growth), or abandon the relationship (Impression Track resets). **This is the system working exactly as intended.**

---

### BEAT 2: Heresy Detection

Maren's Investigation 4 + TS 62 makes her a formidable Inquisitor. She's been Diagnosing court members covertly. TS 62 passive perception: "Thread operations in the same building; residue in the room; practitioner Coherence levels."

**Maren detects Almud.** Almud's Coherence is 6 (Dissonant). Maren passively perceives: someone in the court has Dissonant-level Coherence. Close Knots of that person would be sensing wrongness.

**Active Diagnosis (covert):** Maren rolls Cognition + Investigation to identify the specific practitioner. Concealment from TS 35 observer: Cognition only (no History), TN 7, Ob = observer's TS ÷ 30 = 2 (round up). Maren Cognition (unspecified — assume 3): 3D, TN 7, Ob 2. P(≥2) = ~26%. **Low chance of concealment from the TS 35 observer.**

**GAP S3-01: Diagnosis concealment uses Cognition only but the practitioner's TS isn't factored into their concealment ability.** A TS 62 practitioner should be better at concealing their Diagnosis than a TS 30 practitioner. The current rule gives both the same Cognition-only pool.

**Patch PP-150:** Diagnosis concealment pool = Cognition + TPS (Thread perception translates to Thread concealment — the practitioner understands what they're hiding). Maren: Cognition 3 + TPS 6 = 9D, TN 7, Ob 2. P(≥2) = ~91%. Much more realistic for a high-TS practitioner.

Maren successfully conceals her Diagnosis from the TS 35 observer. She identifies Almud as the Dissonant practitioner. She logs a Heresy Investigation finding.

---

### BEAT 3: Grand Debate — Excommunication Attempt

Maren brings formal charges of heresy against Almud. Per existing rules: Excommunication = Grand Debate (5 exchanges). Church Mandate vs target.

**But Maren is an undercover Inquisitor — she's been posing as a secular advisor.** Revealing Church authority triggers: (a) Vaynard's trust collapses (Impression Track resets to 0 — betrayal), (b) Maren's cover is blown, (c) the investigation may be compromised.

**Maren's player decides to reveal.** Impression Track with Vaynard: 4 → 0 (betrayal of trust). Vaynard's reaction: Stability check? No — Vaynard is an individual, not a faction. Vaynard's trust in Maren is a narrative consequence, not a mechanical one. **Except:** if Maren had reached Impression Track 5, Vaynard would have become an Inspiration. Resetting from 4 means no Inspiration was established, so no Grief Scene. Just narrative anger.

**Grand Debate: Maren (Church authority) vs Almud (self-defence).**

**Composure:**
- Maren: Presence 4 + Att 4 = 8
- Almud: Presence 3 + Att 5 = 8

**Maren's advantage:** Church Law 5, Belief bonus (+1D from "Church authority is divine"), Inspiration (if any — assume Duty to the Faith, 2 points).

**Almud's advantage:** Spirit 6 (high conviction), TS 85 (can perceive Thread-level reality), Court Connections 3.

**Exchange 1:** Maren prosecutes. "The accused has performed Thread operations without Church sanction. This is heresy under the Pact of [date]."
Pool: Presence 4 + Church Law 5 + 1D(Belief) = 10D, TN 7. Rolls 4 successes.
Almud defends: "I am a scholar, not a heretic. My research serves the Crown's understanding of the Southernmost threat."
Pool: Presence 3 + Court Connections 3 = 6D, TN 7. Rolls 2 successes.

**Maren wins by 2.** Almud Composure: 8 → 6.

**Exchange 2:** Almud counter-attacks: "The Church cannot define heresy when it does not understand what it condemns. Your theology is ignorance dressed as doctrine."
Pool: Presence 3 + Einhir Scholar 5 = 8D (using scholarly expertise as rhetorical basis), TN 7. Rolls 3 successes.
Maren defends: 10D (same), TN 7. Rolls 3 successes.

**Tie.** No Composure change. Exchange is a draw.

**Exchange 3:** Maren escalates: "The accused's Coherence is visibly degraded. TS-sensitive witnesses can confirm her rendering is unstable. She is a danger to everyone in this room."

**This is extraordinary.** Maren is publicly describing Thread-level reality in a court. Most of the audience has TS 0 and cannot verify her claims. But 3 audience members have TS 10-29 (they've felt wrongness around Almud). And 1 has TS 35 (they've sensed operations).

**Maren is Calling Witnesses.** Does this mechanic exist?

**GAP S3-02: Witness testimony in Grand Debates.** No rule for calling witnesses or introducing evidence mid-Debate. Debates are exchange-based social combat, not legal proceedings with procedural rules.

**Patch PP-151:** Calling a Witness = spend one exchange action to present testimony instead of arguing. Roll Circles (to find a willing witness) or Presence + relevant History (to present testimony compellingly). Witness testimony adds +1D to the caller's NEXT exchange if the testimony is relevant and the witness is credible. Maximum 2 witnesses per Grand Debate (prevents witness-spam).

Maren calls the TS 35 courtier as witness. Roll: Presence 4 + Investigation 4 = 8D, TN 7, Ob 2 (witness credibility check). Success. +1D to Maren's next exchange.

**Exchange 4:** Maren, with witness testimony (+1D):
Pool: 10D + 1D = 11D, TN 7. Rolls 4 successes.
Almud: 8D, TN 7. Rolls 2 successes.

**Maren wins by 2.** Almud Composure: 6 → 4.

**Exchange 5 (final):** Almud is losing. She considers using Thread operations to influence the Debate (as Veldt did in Scenario 1).

**Almud Diagnoses the Debate's relational configuration.** But she's a PARTICIPANT, not an observer. She must take a Debate exchange AND thread simultaneously.

**GAP S3-03: Can a Debate participant thread during their own Debate?** The action economy is different: Debate exchanges are social actions; Thread operations are Thread actions. Can a character do both?

**Patch PP-152:** A Debate participant may perform Thread operations INSTEAD of a Debate exchange — they forfeit their exchange action (effectively passing that exchange, giving the opponent an unopposed exchange = opponent wins by their full success count). The practitioner Diagnoses/Leaps/operates during the forfeited exchange(s). **Threading during your own Debate costs you exchanges.** This prevents simultaneous social+Thread action while allowing the tactical choice: "I'll lose this exchange to set up a Thread intervention."

Almud forfeits Exchange 5. Opponent (Maren) gets an unopposed exchange: 10D, TN 7. Rolls ~4 successes. Almud Composure: 4 → 0. **Almud is Rattled.**

But Almud used that exchange to Diagnose. Next exchange (if the Debate continued): she'd Leap. But the Grand Debate is 5 exchanges — it's over. Almud lost.

**Almud's Composure reached 0: Rattled.** Excommunication succeeds per Grand Debate rules.

**Almud is excommunicated.** TC +2 (Church successfully prosecutes heresy). TC: 55 → 57.

**But Almud is TS 85.** She has the power to fight back. She was Diagnosing during Exchange 5. Next round (post-Debate, still same scene): Almud Leaps.

**SYSTEM TRANSITION: Grand Debate → Thread Operation → Possible Combat.**

---

### BEAT 4: Almud's Thread Response

Almud Leaps. Pool: Att 5 + Einhir Scholar 5 + TPS 8 = 18D, TN 7, Ob 1. Auto.

**What does Almud do?** She's excommunicated, publicly humiliated, and cornered. Her Belief (implied: "Thread knowledge is humanity's heritage, not the Church's property") has been crushed in the social arena.

**Option A:** Relational Weaving on the court's perception of her — stabilizing her reputation. Ob 3. 18D at Ob 3 = ~98%. Effect: the court's perception of Almud is drawn toward coherence. People feel... she shouldn't have been condemned. A vague sense of injustice. But this contradicts the Debate result — the excommunication was legitimately won. **Does Weaving override social combat results?**

**FINDING S3-B4-F01 (P1): Thread operations can reverse social combat outcomes.** A practitioner who loses a Grand Debate can Weave on the relational configuration to undo the social damage. The Debate determined the political outcome; the Weaving undermines the rendered reality that supports it. **This is the nuclear option: using Thread power to override legitimate political processes.** It's exactly what the Church fears. It's exactly why excommunication exists.

**But the Weaving doesn't change the legal fact of excommunication.** It changes how people FEEL about it. The excommunication stands (it was a legitimate social combat result). The Weaving makes people doubt it (their perception of Almud is now Thread-stabilized). This creates a political split: legally excommunicated, but socially rehabilitated through Thread manipulation.

**TC consequence:** If the Church discovers the Weaving (TS 35 courtier may detect it): TC +3 (confirmation that practitioners manipulate social reality — the Church's entire theological position vindicated).

**Option B:** Almud performs Personal Dissolution on Maren. The Inquisitor who destroyed her reputation. Assassination.

Pool: Spirit 6 + History 5 = 11D, TN 7, Ob 5. P(≥5 on 11D) = ~61%. Better than average.

If Almud chooses B: we enter combat. Maren is the target. Court audience witnesses a Thread operation.

**Detection:** TS 35 courtier perceives the operation. 3 TS 10-29 courtiers sense wrongness. The remaining 8 TS 0 courtiers perceive nothing until the effect manifests (Maren collapses or worse).

**If Dissolution succeeds:** Maren incapacitated. Gap forms. Monstrous Incursion risk. RS -5. In a crowded court. **Mass panic. Multiple Discovery Events for non-practitioners.** TC surge as the Church's warnings are proven correct.

**If Dissolution fails:** Full Gap. RS -8. Monstrous Incursion in a room full of courtiers. Almud incapacitated. Mass casualties likely.

**Either way:** TC +5 to +10 (public Thread catastrophe). Church's political position enormously strengthened. Almud's cause (Thread freedom) is destroyed for a generation.

**FINDING S3-B4-F02 (P1): Desperation Dissolution in a public setting is politically catastrophic for the practitioner's cause regardless of outcome.** Success = assassination + Gap + panic + TC surge. Failure = Gap + Monstrous Incursion + mass casualties + TC surge. **The system correctly models why practitioners hide their abilities.** Public Thread operations are politically suicidal even when mechanically viable.

---

### BEAT 5: TS Growth Cascade

**If Dissolution succeeds or fails in the court:** Multiple qualifying events for TS growth.

12 courtiers witness a Thread catastrophe. Those with TS 10-29 (3 courtiers): Spirit check TN 7 Ob 1 for TS growth.
- Average Spirit 3: 3D at TN 7. P(≥1) = ~70%. **~2 of 3 gain +5 TS.** They move from 10-29 to 15-34. If any cross 30: they can now perceive Thread operations actively.

TS 0 courtiers: qualify if they "hold the confrontation" (don't flee). Spirit check TN 7 Ob 1. Success: +5 TS (0 → 5, still Inert but tracking). ~70% of those who stay gain TS.

**If 8 of 12 courtiers gain +5 TS:** 8 new TS-tracking NPCs in a single scene. Over subsequent sessions: some will reach TS 10 (passive perception), then 30 (active perception). **A single public Thread catastrophe creates a generation of Thread-sensitive individuals.**

**TC consequence:** Mass Thread-awareness event. TC +3 (minimum — public awareness that Thread reality is real). Combined with the Dissolution consequences: TC could surge by +8 to +13 in one scene. TC 57 → 65-70. **Approaching critical TC thresholds where the Church gains institutional powers (excommunication at TC 60, Inquisition expansion at TC 70, potential seizure at TC 80).**

**FINDING S3-B5-F01 (P1): A single public Thread catastrophe can cascade through TC, TS growth, RS, and faction politics simultaneously.** The system correctly models catastrophic exposure events. **The cascading consequences are enormous and non-linear** — each consequence amplifies the others (TC surge enables Church power, Church power enables more Inquisitions, more Inquisitions expose more practitioners, more exposure events further surge TC). **This is the positive feedback loop that the Church's anti-Thread stance is designed to exploit.**

---

### SCENARIO 3 HYBRID NOTES

| Beat | TTRPG | Board Game | Hybrid Handoff |
|---|---|---|---|
| Impression Track | Tracked per PC/NPC pair, scene-by-scene | N/A (board game has no NPC relationships) | Personal Phase only. Board game cannot advance Impression Tracks. |
| Heresy detection | Investigation + TS perception | Spy order (Intelligence roll) | Strategic Phase: Spy order detects practitioners mechanically. Personal Phase: Inquisitor PC investigates narratively. |
| Grand Debate | 5-exchange social combat | Single roll (Church Mandate vs target) | If both parties are PCs: Personal Phase, full Debate. If one is NPC: board game single roll OR Personal Phase GM scene. |
| Thread operation post-Debate | Full TTRPG threadweaving | N/A at this scale | Personal Phase. Thread consequences (RS, TC) applied at Cascade Phase Accounting. |
| TS growth cascade | Individual Spirit checks | N/A (board game has no TS tracking) | Personal Phase only. Mass TS growth creates campaign-level consequences tracked in GM notes. |

**Hybrid gap (S3-HYB-01):** TC changes from Personal Phase Thread catastrophes must be batched to Cascade Phase (Accounting-gated per threadweaving_v25.md §5.3). A mid-Personal-Phase TC surge of +8 doesn't trigger TC threshold effects until Cascade Phase. **This means the Church doesn't gain its TC 70 powers until the season AFTER the catastrophe.** This is a one-season delay that is either a buffer (giving other factions time to respond) or a frustrating desynchronization (the narrative impact is immediate but the mechanical impact is deferred). **[EDITORIAL: Should catastrophic TC surges (+5 or more from a single event) trigger threshold effects immediately, bypassing the Accounting gate? This would make public Thread catastrophes feel appropriately devastating in real-time.]**

---

# SCENARIO 4: THE NIFLHEL OPERATION
## Systems tested: Intelligence (faction) → Circles → Infiltration → Personal combat → Dissolution → Pursuit → RS cascade → Domain Echo → Political fallout
## Compressed format — key beats only.

**Mission:** Niflhel operatives assassinate a Crown general using a practitioner (Dissolution).

### Beat 1: Intelligence Gathering
Niflhel Intelligence 6 vs Crown Intelligence 4. Spy order: 6D + operative History 4 = 10D, TN 7, Ob = Crown Intel ÷ 2 = 2. P(≥2) = ~96%. Success: Crown general's location, schedule, and guard rotation obtained.

### Beat 2: Infiltration
Niflhel operative (Agi 5, History: Espionage 4) infiltrates Crown compound. Agi 5 + Espionage 4 = 9D, TN 7, Ob 3 (compound security level). P(≥3) = ~88%. Success: inside, undetected.

### Beat 3: The Strike
Practitioner (TS 65, Spirit 5, History 4) Diagnoses the general. Next round: Leaps. Pool: Att 4 + Espionage 4 + TPS 6 = 14D, TN 7, Ob 1. Auto. Next round: Personal Dissolution (Ob 5). Pool: Spirit 5 + History 4 = 9D, TN 7, Ob 5. P(≥5 on 9D) = ~37%.

**37% success.** Not great. Niflhel knows this. They've planned for both outcomes.

**On success (37%):** General dissolved. Gap forms. RS -5. Micro-Incursion. Practitioner exits via pre-planned route. Crown loses a military commander: Military -1 (effective) until replacement appointed. Political crisis: who did this? No physical evidence (no blade, no poison — the general simply ceased to exist).

**On Partial (45%):** General becomes a Personal Shifting Object. Does not die immediately but is incapacitated and deteriorating. Crown has ~1 session to Mend (requires a TS 50+ practitioner — does Crown have one?). If they do: general saved but Crown now knows Thread assassination is possible. If they don't: general dies within 1d3 sessions. Political consequences identical but delayed.

**On Failure (18%):** Full Gap. RS -8. Monstrous Incursion in Crown compound. Practitioner incapacitated. Niflhel operative must abort. The operative faces: escape through a compound in chaos (Monstrous Entity + panicking guards), or be captured with an incapacitated practitioner who is evidence of Niflhel's Thread capabilities.

**FINDING S4-F01 (P1): Thread assassination has a ~37% success rate at mid-tier, with ~45% "delayed success" (Partial = target deteriorating) and ~18% catastrophic failure.** The total "target eliminated" rate is ~82% (success + partial if not Mended). **This makes Thread assassination reliable enough to be a strategic tool but unreliable enough to be terrifying** — every operation has nearly 1-in-5 odds of catastrophic blowback.

### Beat 4: Pursuit (if operative must flee)

On failure: operative runs. Guards pursue. Chase mechanics?

**GAP S4-01: No pursuit/chase mechanic.** Combat assumes both parties want to fight. No rule for "one side runs, the other chases."

**Patch PP-153:** Chase = extended contest. Each round: runner rolls Agi + relevant History vs pursuers' Agi + relevant History. Runner needs 3 cumulative excess successes to escape. Pursuer needs 3 to catch. If runner is caught: combat begins. If runner escapes: they're free.

Operative: Agi 5 + Espionage 4 = 9D. Guards: Agi 3 + Guard Duty 2 = 5D. Operative is heavily favoured: ~2 excess/round. Escapes in ~2 rounds.

### Beat 5: Political Fallout (Domain Echo)

Crown loses general. Military effectiveness: -1D to next Military Domain Action (temporary, until replacement). Crown Mandate check: Stability vs Ob 1. Failure: Mandate -1 (the Crown cannot protect its own officers).

Niflhel's Intelligence advantage: +1D to next Intelligence roll (successful operation boosts network confidence).

TC effect: If the attack becomes publicly known as Thread-based: TC +2 (public fear). If kept secret: TC unchanged.

RS: already paid (-5 or -8) during the operation. No additional RS cost from political consequences (rendered-side effects don't drain the substrate).

---

# MASTER INTEGRATION FINDINGS

## System Transitions Tested

| Transition | Scenario | Finding |
|---|---|---|
| Negotiation → Debate | S1 | Clean. Composure tracks are independent of social rolls. |
| Debate → Combat | S1 | PP-146: Composure carries but only affects social actions. Clean. |
| Thread ops during Debate | S1, S3 | PP-145, PP-152: Powerful. Practitioners dominate social politics. |
| Mass combat → Personal (Zoom In) | S2 | Clean via G-002 scope transition. |
| Personal combat → Thread ops | S1, S2, S3 | Clean. Contact window crosses system boundaries. |
| Grand Debate → Thread response | S3 | PP-152: forfeit exchange to thread. Clean but dominant. |
| Thread catastrophe → TS cascade → TC surge | S3 | Cascading — non-linear consequences. Working as designed. |
| Intelligence → Infiltration → Dissolution | S4 | PP-153 (chase). Otherwise clean. |

## New Patches This Batch

| ID | Description | Source |
|---|---|---|
| PP-144 | Belief bonus to Debate: +1D when arguing from held Belief | S1-B2 |
| PP-145 | Relational Weaving on Debate subject: +2D to defending side next exchange | S1-B3 |
| PP-146 | Debate→Combat carryover: Composure carries, Rattled applies to social actions only | S1-B4 |
| PP-147 | Siege assault pool: faction Military + officer History | S2-B1 |
| PP-148 | Siege Partial result: Cohesion -1, attacker loses 1 unit strength | S2-B1 |
| PP-149 | Break Through action: Offence at TN 7 vs each opponent's Offence; failure = free Strike +2D | S2-B3 |
| PP-150 | Diagnosis concealment: Cognition + TPS (not Cognition only) | S3-B2 |
| PP-151 | Witness testimony in Grand Debates: +1D next exchange, max 2 witnesses | S3-B3 |
| PP-152 | Threading during own Debate: forfeit exchange to Diagnose/Leap/operate | S3-B3 |
| PP-153 | Chase mechanic: extended Agi contest, 3 cumulative excess to resolve | S4-B4 |

## Critical Findings for Editorial

| Priority | Finding | Impact |
|---|---|---|
| P1 | Thread operations reverse social combat outcomes (S3-B4-F01) | Practitioners dominate politics unless countered by other practitioners |
| P1 | Public Thread catastrophe cascades through TC/TS/RS/faction simultaneously (S3-B5-F01) | Single event can shift entire campaign trajectory |
| P1 | Structural Pulling trivializes fortifications (S2-B2-F01) | Siege warfare collapses against practitioners |
| P1 | Fighter sortie is the correct anti-practitioner tactic (S2-B4-F01) | Confirms intended rock-paper-scissors: practitioners beat structures, fighters beat unprotected practitioners |
| P1 | Thread assassination is 82% effective (success + partial) (S4-F01) | Niflhel's strategic position is terrifying — they can eliminate any non-practitioner target with high reliability |
| P2 | Contact windows carry across system transitions seamlessly (S1-B5-F01) | No gap — but practitioners who begin threading in social scenes get 2 free setup rounds |
| P2 | Immediate TC surge from catastrophic events (S3-HYB-01) | Hybrid timing question — should catastrophic surges bypass Accounting gate? |

## Remaining EDITORIAL Queue (cumulative)

1. Personal Pull balance (X-15 from prior batch)
2. Personal Dissolution lethality / resistance roll (X-17)
3. Heal loop mitigation — Overweave acceleration (X-04)
4. Pull stacking floor (X-05)
5. Mass Lock RS drain cap (X-08)
6. Thread Weaving effect on Debates — magnitude (+1D vs +2D) (S1-B3)
7. Structural Pulling vs Fortification — should Fortification provide resistance? (S2-B2)
8. Catastrophic TC surge — bypass Accounting gate in hybrid? (S3-HYB)
