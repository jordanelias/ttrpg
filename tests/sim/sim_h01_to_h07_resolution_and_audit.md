# SIM-H-01 Gap Resolution + Unique Test Suite + Mechanical Audit
## Date: 2026-04-04 | Author: valoria-simulator + valoria-mechanic-audit

---

# PART 1: GAP RESOLUTIONS

## F-H01 — Forgetting Check failure rate (44%)
**Status: CONFIRMED DESIGN — no patch required.**
The 44% combined fail/partial rate for a TS 58 practitioner at Interior depth is intentional. The Southernmost extracts cost from even expert practitioners. The Forgetting Check is the system's primary tool for ensuring the Southernmost cannot be solved through repeated visits.
**Action:** None. Document as design note in params_threadwork.

---

## F-H02 — Debate CLASH stalemate at parity pools
**Status: CONFIRMED DESIGN — no patch required.**
Movement requires margin ≥ 3 at resistance 4. Near-parity pools (19D vs 20D) produce stalemates by design. The Debate system rewards asymmetric preparation (genre choice, audience alignment) over raw pool advantage. This is correct behaviour.
**Action:** None.

---

## F-H03 — Crown Intel stat undefined
**Status: CONFIRMED GAP — resolved by canonical text.**
stage6_factions.md explicitly marks Crown Intel as `—` (no stat). The stage6 text states: "The Crown is structurally weakest at covert operations. Its strength is open, honourable action." Crown does NOT have Intel. The simulation's proxy via Influence was mechanically wrong.

**Resolution (PP-236):** Crown Investigate actions use **Influence** at **+1 Ob** (covert actions are structurally harder for the Crown — this is a design constraint, not a proxy). This is already implicit in stage6; PP-236 makes it explicit in params_factions.

**PROVISIONAL:** The +1 Ob covert penalty for Crown is derived from the "structurally weakest at covert operations" statement. If the designer intends a different penalty modifier, flag for revision.
`[EDITORIAL: ED-147 — Crown covert action penalty: +1 Ob on Influence-based covert rolls is PROVISIONAL. Confirm or set exact modifier. P2.]`

**Patch PP-236:**
- File: references/params_factions.md
- Add: "Crown covert actions (investigation, sabotage, intelligence): use Influence pool at +1 Ob. Crown has no Intel stat. This constraint is a faction design feature."

---

## F-H04 — Revolution Agitation near-certain failure
**Status: CONFIRMED DESIGN — no patch required.**
Revolution Influence 3 vs Mandate Ob 4 produces P(success) ≈ 3% per season. This is intentional: Revolution is a pressure generator operating under structural disadvantage. Its function is to accumulate Institutional Pressure over time, not to win individual Domain Actions. The system correctly represents an insurgent faction constrained by resource scarcity.
**Action:** None.

---

## F-H05 — Public Instability track undefined for TTRPG/Hybrid
**Status: PARTIALLY DEFINED — gap in Hybrid/TTRPG layer.**
`params_factions.md` defines Public Instability as a BG clock (starting value 5). The BG doc (bg_v05) references it in scenarios. But no TTRPG or Hybrid definition exists in any canonical file.

**Resolution (PP-237):**
Public Instability is a **Hybrid-mode secondary clock** (TTRPG mode does not track it as a clock — it is folded into Institutional Pressure in TTRPG). In Hybrid mode:
- Range: 0–10
- Starting value: 5 (matches BG starting value)
- Increases: +1 per season a Revolution Agitation Domain Action resolves (any degree), +1 per season Institutional Pressure increases while TC > 40
- Decreases: −1 per season Crown or Guilds completes a successful social Domain Action targeting the Harbour District or equivalent territory
- Threshold at 8: Faction Fracture risk — Revolution gains a free Agitation action at no Domain Action cost
- Threshold at 10: Shared loss condition check (not Rupture — Institutional collapse, distinct from RS=0 Rupture)

**[PROVISIONAL] — this definition is mechanically derived from BG analogue + IP interaction logic. Requires user confirmation before canonical use.**
`[EDITORIAL: ED-148 — Public Instability in Hybrid/TTRPG mode: definition above is PROVISIONAL. Confirm range, thresholds, and interaction with IP. P2.]`

**Patch PP-237:** Add Public Instability Hybrid definition to params_factions.md.

---

## F-H06 — Lowenritter response trigger at Varfell Military 6
**Status: GAP — no canonical trigger exists.**
No document defines a Lowenritter response triggered by Varfell Military reaching 6. The Lowenritter coup trigger (stage6 §8.9) fires on TC-40 Crown inaction or Crown losing 2+ territories — not on Varfell Military thresholds.

**Resolution (PP-238):**
Varfell Military 6 does NOT trigger a Lowenritter response. The simulation's assumption was incorrect. Lowenritter response to Varfell Military growth is handled through normal NPC AI: Lowenritter Institutional Tendency is "maintain border deterrence." When Varfell Military exceeds Lowenritter Military (currently equal at 5/6), the NPC AI should prioritise a Military Consolidation order the following season. This is a GM guidance note, not a threshold mechanic.

**Add to params_factions.md:** "Lowenritter NPC priority: if any bordering faction's Military exceeds Lowenritter Military, Lowenritter NPC AI prioritises Military Consolidation (internal) the following season."

**Patch PP-238:** params_factions.md — add Lowenritter reactive military guidance.

---

## F-H07 — RS natural decay rate assumed −1/season
**Status: SIMULATION ERROR — corrected.**
RS has NO natural baseline decay. RS changes only from:
- Thread operation degree outcomes (Partial: −1 to −6; Failure: −2 to −8 depending on operation type)
- Lock drift: −1/season per locked territory at Accounting
- Gap persistence: −4/season per active Gap at Accounting
- Mending: +1 to +2 per successful operation

The simulation's RS 54→53 transition was incorrect. RS should have been **RS 54→54** (unchanged) absent any Lock drift or Gap persistence in Season 6. The SIM-H-01 season contained no Locks or Gaps.

**Corrected Season 6 exit RS: 54 (unchanged).**

**Patch PP-239:** Correct SIM-H-01 accounting in tests/sim_h01_hybrid_season6.md. Add explicit RS change rule to params_threadwork: "RS does not decay naturally. All RS changes are event-driven. See Locking chronic consequences (§Locking) and Gap persistence (§Mending) for seasonal RS costs."

---

## F-H08 — Inspiration spend on named NPC focus
**Status: DESIGN NOTE — no patch required.**
Named NPC Inspirations (+4D for Spirit 4) vs abstract Inspirations: same mechanical rule, significant practical advantage for high-Attunement characters with named relationships. This is correct — Inspirations are designed to reward investment in specific narrative relationships. No action needed.

---

## F-H09 — Hybrid season pacing within 2–2.5hr target
**Status: CONFIRMED — no action required.**

---

## SUMMARY — PATCHES THIS SESSION

| Patch | File | Change | Provisional? |
|-------|------|--------|-------------|
| PP-236 | params_factions.md | Crown covert actions: Influence pool +1 Ob | YES (ED-147) |
| PP-237 | params_factions.md | Public Instability Hybrid definition | YES (ED-148) |
| PP-238 | params_factions.md | Lowenritter reactive Military guidance | NO |
| PP-239 | params_threadwork.md + sim_h01 | RS no natural decay; Season 6 RS corrected to 54 | NO |

## EDITORIAL ITEMS ADDED THIS SESSION

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| ED-143 | PC Mira Sondhal — simulation construct | P2 | Open |
| ED-144 | PC Arend Voss — simulation construct | P2 | Open |
| ED-145 | PC Sister Dagmara Kuhl — simulation construct | P2 | Open |
| ED-146 | PC Theron Ault — simulation construct | P2 | Open |
| ED-147 | Crown covert penalty: +1 Ob provisional | P2 | Provisional |
| ED-148 | Public Instability Hybrid definition | P2 | Provisional |

---

# PART 2: UNIQUE TEST SUITE

## TEST DESIGN RATIONALE
Six tests targeting mechanics not covered in the existing SIM-X-01–16 matrix.
Each test probes a specific interaction, edge case, or mode-transition not previously run.

---

## SIM-H-02: Forgetting Check Cascade — Multi-Session Southernmost Exposure
**Mode:** TTRPG | **Mechanics:** Forgetting Check stacking, TS growth, Coherence
**Novel element:** Multiple Forgetting Checks across 3 scenes in a single session (repeated exposure within same seasonal visit).

**Setup:** A practitioner (TS 45, Cog 4, Rec 3, Foc 4) makes three Forgetting Checks in the same session:
- Scene 1: Boundary zone (Ob 1)
- Scene 2: Interior (Ob 2) — same day, continuous presence
- Scene 3: Deep Interior (Ob 3) — reached the Einhir core approach

**Question:** Do Forgetting Checks stack? Does failing the first affect subsequent checks?

**Canonical search:** threadwork_redesign_v25 and stage4_southernmost describe Forgetting Checks per exposure depth but do not address same-session stacking.

**Ruling (PROVISIONAL, PP-240):** Forgetting Checks within the same scene do not stack — only the deepest applicable Ob applies. Across multiple scenes in the same session, each check is independent (separate exposure events). A Failure on Scene 1 Forgetting Check does not increase Ob for Scene 2 — the Forgetting strips what was learned, but the mechanism itself does not degrade.

**Simulation — Practitioner profile:**
TS 45 → TPS 4. Pool: Cog(4) + Rec(3) + TS-bonus(45÷20=2) = 9D | TN 8

| Scene | Ob | E[net] | P(pass) | P(partial) | P(fail) |
|-------|----|---------|---------|-----------| --------|
| 1: Boundary | 1 | 9×0.20=1.8 | ~93% | ~5% | ~2% |
| 2: Interior | 2 | 1.8 | ~70% | ~18% | ~12% |
| 3: Deep Interior | 3 | 1.8 | ~40% | ~30% | ~30% |

**Cumulative full retention (all three Overwhelming):** (P≥3 at 9D TN8)³ = (~15%)³ ≈ 0.3%
**Cumulative at least partial success all three:** (~70%)³ ≈ 34%
**Expected outcome:** Scene 1 success, Scene 2 success, Scene 3 partial or failure.

**Finding SIM-H-02-F1:** A TS 45 practitioner (above eligibility floor) loses operationally useful intelligence from Deep Interior exposure ~60% of the time. This is the system correctly producing diminishing returns on solo Southernmost expeditions. Collective operations (multiple practitioners sharing Forgetting burden) are mechanically incentivised but undefined — gap flagged.

**[GAP: Collective Forgetting — does one practitioner's Forgetting Check success allow them to carry others' intelligence? No rule found. Flag: GAP-H-01.]**

**Edge case — TS 59 (Mira):** With TS 59, TS-bonus = 2 (same as TS 45 — no improvement until TS 60). This is a cliff: TS 59 and TS 45 have identical Forgetting pools. TS 60 grants +3 bonus dice. This creates a meaningful advancement goal.

**Finding SIM-H-02-F2:** TS bonus dice cliff at every multiple of 20 creates discrete advancement incentive. Confirmed design. TS 59→60 is the most actionable near-term goal for Mira.

---

## SIM-H-03: Crown Investigate with PP-236 — Corrected Pool
**Mode:** Hybrid (Strategic Phase) | **Mechanics:** Domain Action, Crown covert, PP-236
**Novel element:** First test using the corrected Crown covert rule (Influence pool +1 Ob).

**Setup:** Season 7. Crown investigates Revolution Southernmost access. Corrected pool: Influence(4) at +1 Ob → Ob 3+1=4 (base Ob 3 for "difficult" covert target, +1 Crown covert penalty).

Pool: 4D | TN 7 | Ob 4

| Degree | Net needed | P |
|--------|-----------|---|
| Overwhelming | ≥8 AND ≥3 | <1% (4D cannot reach 8 net) |
| Success | ≥4 | ~5% |
| Partial | 1–3 | ~53% |
| Failure | ≤0 | ~42% |

**Finding SIM-H-03-F1:** Crown investigation (corrected) is P(success) ≈ 5%. Even with +1 Ob penalty vs prior simulation's proxy, the result is similar — Crown cannot reliably run intelligence operations. Partial is the expected outcome: fragmentary intelligence, actor unidentified.

**Finding SIM-H-03-F2:** If Crown wants reliable intelligence, it must use Lowenritter Intel 4 as the rolling pool (Lowenritter as Crown's deniable covert arm, per stage6 §8.9). Lowenritter Intel 4 vs Ob 3 (standard covert, no Crown penalty): P(≥3) ≈ 26%. Still weak, but meaningfully better than Crown direct action. This is the correct mechanical incentive: Crown delegates covert work to Lowenritter.

**Domain Action clarification (PP-241):** "When Crown delegates a covert Domain Action to Lowenritter, the roll uses Lowenritter Intel pool (no Crown covert penalty applies — the constraint is institutional, not operational). The Lowenritter acts as agent; the Crown bears political consequences of discovery."

`[EDITORIAL: ED-149 — Crown-Lowenritter covert delegation mechanic: PP-241 is PROVISIONAL. Confirm whether Crown covert penalty applies when Lowenritter executes on Crown's behalf. P2.]`

---

## SIM-H-04: Debate AMPLIFY — Same Genre, Same Orientation
**Mode:** TTRPG (social scene) | **Mechanics:** Debate AMPLIFY interaction
**Novel element:** AMPLIFY has never been simulated. All prior debate tests used CLASH.

**Setup:** Dagmara (Ordained Deacon History 4pts, Cha 5, Cog 4, Att 5) and Theron (Merchant-factor 4pts, Cha 5, Cog 4, Att 4) both choose **Future/Revealing** in Parliament against a Church-backed counter-speaker.

**AMPLIFY rule:** Combined pools vs Conviction Track resistance. Audience: mixed Parliament (Hafenmark, Guilds, Crown delegates). Resistance = avg Stability = avg(4, 4, 3) = 3.7 → **4** (round up).

**Combined pool:** Dagmara argue pool: (Cog 4 × 2) + History bonus(7) = **15D**. Theron argue pool: (Cog 4 × 2) + History bonus(7) = **15D**. Combined: **30D**.

**AMPLIFY resolution:** Roll combined pool vs Ob = resistance (4). Net successes above resistance = track movement.

E[net] at 30D TN7: 30 × 0.30 = **9.0**
P(≥4): >99%
Expected movement: net 9 − resistance 4 = **5 track points toward Dagmara/Theron** (capped by track boundaries).

Conviction Track starts at 5 (neutral). Movement of 5 → **Track position 10** (Side A wins). Dagmara and Theron's combined Future/Revealing AMPLIFY wins the Parliament motion in a single exchange.

**Finding SIM-H-04-F1:** AMPLIFY with two high-pool orators is **decisively powerful**. 30D combined vs resistance 4 produces near-certain maximum track movement. This is not a bug — two expert orators with aligned strategy should dominate. But it creates a strategic incentive to always coordinate orientation before a Debate.

**Finding SIM-H-04-F2:** AMPLIFY has no natural cap on combined pool. At extreme coordination (3+ expert orators, all aligned), track movement could be 20+ in one exchange. Resistance of 4 is insufficient as a cap.

**[GAP: AMPLIFY combined pool cap — no maximum specified. With 4 expert orators, combined pool could exceed 60D, producing 14+ expected track movement in one exchange. GAP-H-02.]**

**Provisional ruling (PP-242):** AMPLIFY combined pool maximum = (highest individual pool) × 2. This prevents degenerate stacking while preserving meaningful collaboration. At 15D max individual × 2 = 30D cap — which still produces the above result, but prevents 4-orator blowouts.

`[EDITORIAL: ED-150 — AMPLIFY pool cap. PP-242 is PROVISIONAL. Confirm whether combined pool should be capped, and at what ceiling. P1 — degenerate case possible without cap.]`

---

## SIM-H-05: Locking at Structural Scale — RS Drift Calculation
**Mode:** TTRPG | **Mechanics:** Locking, RS chronic drift, seasonal accounting
**Novel element:** Tests the Locking chronic consequence table (−1 or −2 RS/season depending on Lock age) across 5 seasons. Not previously simulated.

**Setup:** Season 1 of Lock. Practitioner (TS 70, Foc 5) successfully Locks a Structural configuration (TN 7, Ob 8). 
Pool: Spirit(4) + Attunement(4) + TPS(7) + History(7) = 22D | Ob 8
E[net]: 22 × 0.30 = 6.6. P(≥8): ~25%. **Most likely: Partial.** But assume Success for this test.

**Success outcome:** Configuration locked. RS −1 (from degree table). Lock persists.

**5-season RS drift (chronic consequences table from threadwork v25):**

| Season | Lock age | RS drift/season | Cumulative RS loss |
|--------|----------|-----------------|--------------------|
| 2 | 1 season | −1 | −1 |
| 3 | 2 seasons | −1 | −2 |
| 4 | 3 seasons | −1 | −3 |
| 5 | 4 seasons | −2 | −5 |
| 6 | 5 seasons | −2 | −7 |

Plus initial Success cost: −1 RS from degree table.
**Total RS loss from one Structural Lock over 5 seasons: −8.**

Starting RS 54 → RS 46 by Season 6 from this Lock alone. That drops RS into the Fragile band (40–59) where it already was — but approaches the Fractured threshold (39).

**Finding SIM-H-05-F1:** A single Structural Lock, if unresolved, costs −7 RS over 5 seasons of drift plus −1 on success = −8 total. This is significant but not catastrophic in isolation. Two concurrent Structural Locks would cost −14–16 over 5 seasons — likely terminal at current RS levels.

**Finding SIM-H-05-F2:** Reversal pool: Pull at Ob = (TS÷10 round up) − 2 = (70÷10=7) − 2 = **Ob 5**. Structural Pull: Pool = Spirit(4) + History(7) + TPS(7) = 18D. E[net]: 5.4. P(≥5): ~45%. Reversal is risky. The mechanic correctly prices long-term Locks as high-stakes decisions.

**Finding SIM-H-05-F3:** Permanent Lock (4+ seasons, substrate adapted): **Dissolution fails automatically.** Only the Einhir framework can address it. This is the Locked Zone formation mechanic — the Southernmost's Locked Zones are the result of Einhir-era Locking at this scale, now permanently substrate-adapted. The system is mechanically consistent with the setting.

---

## SIM-H-06: Momentum as Automatic Successes — Edge Case at Ob 1
**Mode:** TTRPG | **Mechanics:** Momentum spend, Ob 1 rolls, minimum pool rule
**Novel element:** Momentum spent on Ob 1 rolls — does excess auto-success produce Overwhelming?

**Rule (params_core):** 1 Momentum = 1 automatic success (non-Thread rolls only). Overwhelming: net ≥ 2×Ob AND ≥3.

**Case:** Character with 2 Momentum spends 1 on an Ob 1 roll. Automatic success: net 1. That alone meets Ob 1. Do they roll remaining pool, adding to net 1?

**Canonical text:** "1 Momentum = 1 automatic success." Does not say "replace roll" — implies addition to roll.

**Resolution (PP-243):** Momentum automatic successes add to the roll result. A character spending 1 Momentum on an Ob 1 roll: the auto-success meets Ob 1, and rolling the pool can push to Overwhelming if total net ≥ 2 AND ≥ 3. Spending 2 Momentum on Ob 1: auto 2 successes = Overwhelming if ≥ 3 net total — but auto 2 alone doesn't meet Overwhelming floor of 3; must still roll or have pool that produces ≥1 net.

**Edge case — Momentum on Ob 1, pool 1D:** Spend 1 Momentum. Auto 1 success = Success. Roll 1D TN 7. E[net additional]: 0.30. If die shows 10: net 1+2=3, 2×Ob=2, Overwhelming. If die shows 7-9: net 1+1=2, ≥2×Ob but net<3 → **not Overwhelming** (floor of 3 not met). If die shows 1: net 1-1=0 → **Failure** (auto success cancelled by 1-result).

**Finding SIM-H-06-F1:** Rolling 1 on a die cancels an auto-success. This is correct per the dice rule ("1 = −1 success") and creates interesting risk for Momentum spends on 1D pools. A desperate character spending their last Momentum on a 1D roll has ~10% chance of it backfiring.

**Finding SIM-H-06-F2:** Momentum spend on minimum pool (1D) is a genuine tactical decision, not a free upgrade. The risk is real. This is correct design.

---

## SIM-H-07: Cross-Mode Transition — Scene→Mass Combat
**Mode:** Hybrid (Personal Phase → Strategic Phase) | **Mechanics:** Scene→Mass zoom, AUD-P1-15
**Novel element:** Tests the underspecified Scene→Mass transition flagged in AUD-P1-15.

**Setup:** Arend (Combat Pool 15D, weapon TN 6, Stamina 7) is in personal combat against a Lowenritter Riskbreaker (Combat Pool 10D, weapon TN 7, Stamina 6) when the Strategic Phase begins — a border skirmish escalates to a faction-level military engagement.

**Transition trigger:** Hybrid mode §12.3 states "if an order generates a scene (assassination attempt, diplomatic confrontation), pause resolution and run the TTRPG scene." The reverse is not specified: no rule covers personal combat scenes escalating INTO Strategic Phase mass resolution.

**Gap (AUD-P1-15):** The Scene→Mass transition is underspecified. Two sub-gaps:
1. Does the personal combat result affect the faction-level military roll?
2. What happens to the personal combatants when the zoom shifts?

**Provisional ruling (PP-244):**
1. **Personal combat outcome as Domain Modifier:** If the personal scene resolves before Strategic Phase mass resolution:
   - PC overwhelming success → mass action at −1 Ob (opponent general/officer neutralised)
   - PC success → no modifier
   - PC partial → mass action at +1 Ob (friendly position degraded)
   - PC failure → mass action at +2 Ob (PC captured/wounded, morale cost)
2. **Unresolved personal combat at zoom:** If the zoom occurs mid-combat (session time, not in-fiction time), pause the personal combat. Resolve Strategic Phase mass action. Apply the mass outcome as context for the personal combat resolution in the next session.

`[EDITORIAL: ED-151 — Scene→Mass transition rules (PP-244). This defines AUD-P1-15. PROVISIONAL. Confirm modifier values and whether unresolved combat carries across phases. P1-BLOCKER for Hybrid integration.]`

**Simulation:**
Arend vs Riskbreaker, 1 round. Arend: 15D split 9 Offence / 6 Defence (Stamina 7, initiative via higher Agi).
Riskbreaker: 10D split 6 Offence / 4 Defence.

Arend Offence (9D) vs Riskbreaker Defence (4D), TN 6 (weapon):
E[net Arend offence]: 9 × 0.40 = 3.6
E[Riskbreaker defence net]: 4 × 0.30 = 1.2
Net hits by Arend: 3.6 − 1.2 = 2.4 → Hit lands.
Damage: Weapon (Short Heavy Blade) = base 3, STR mod (+1 for Str 4), DR reduction (Riskbreaker medium armour DR 2): damage = 3+1−2 = 2. Riskbreaker Stamina 6−2 = 4.

Riskbreaker Offence (6D, TN 7) vs Arend Defence (6D):
E[Riskbreaker offence net]: 6 × 0.30 = 1.8
E[Arend defence net]: 6 × 0.30 = 1.8
Net: 0 — no hit (expected).

**Round 1 outcome:** Arend hits for 2 Stamina. Riskbreaker Stamina 6→4. Arend unhurt.

**Personal scene outcome: partial success** (Riskbreaker wounded but not incapacitated; combat ongoing). Per PP-244 provisional: Strategic Phase mass action at **+1 Ob** (friendly position not fully secured).

**Finding SIM-H-07-F1:** PP-244 provisional modifiers are calibrated reasonably. A single combat round producing "partial" generates a meaningful but not crippling +1 Ob on the mass action — correct design intent.

**Finding SIM-H-07-F2:** The "mid-combat zoom" pause rule is the main design challenge. Players in active combat do not want their combat interrupted by a Strategic Phase. The recommended implementation: complete the personal combat round, then apply result before Strategic Phase. If combat cannot complete in session time, use the mid-point state to set a provisional modifier.

---

# PART 3: MECHANICAL AUDIT

## AUDIT SCOPE
Systems touched by SIM-H-01 and SIM-H-02 through SIM-H-07.
Modes: A (isolation), B (interaction), D (edge cases).

---

## AUDIT-01: Hybrid Phase Structure — Completeness Check

**Phases:** Personal → Strategic → Cascade → Accounting.

| Phase | Rule coverage | Gap |
|-------|--------------|-----|
| Personal Phase | Stage12 §12.3 — defined. Max 3 scenes. Player-triggered scenes: defined. | ✓ |
| Strategic Phase | Domain Action rules in stage6 — defined. Board game card layer not used in TTRPG-adjacent Hybrid. | ✓ |
| Cascade Phase | "Domain Echoes, threshold events, and cross-mode consequences applied." Specific Domain Echo rules: undefined. | ⚠ GAP-H-03 |
| Accounting | Clock advances, victory condition check. | ✓ |

**GAP-H-03:** Domain Echo rules — what converts a personal scene result into a faction stat change — are referenced but not defined in any canonical file. The simulation used the stage6 §8.1 domain action text ("the personal roll resolves both the personal outcome and the faction effect simultaneously") as a proxy, but this applies only to Domain Actions initiated by PCs, not to personal scenes that have downstream faction consequences.

`[EDITORIAL: ED-152 — Domain Echo formal rule: how personal scene outcomes convert to faction stat changes in Cascade Phase. P1-BLOCKER for Hybrid compilation. Provisional working rule: personal scene result sets Domain Echo magnitude (Overwhelming: +2 to triggering stat; Success: +1; Partial: 0; Failure: −1 to related faction stat).]`

---

## AUDIT-02: Debate System — Interaction Type Coverage

| Interaction | Simulated? | Finding |
|-------------|-----------|---------|
| CLASH | SIM-X-05, SIM-H-01 | Well-defined. Movement formula verified. |
| AMPLIFY | SIM-H-04 (this session) | Pool cap gap found (GAP-H-02). Provisional PP-242 applied. |
| CROSS | Never simulated | [GAP-H-04: CROSS interaction rules exist in params_debate but have not been stress-tested. Particularly: when two different genres both move the track independently, do they use separate resistance rolls? Can they cancel each other?] |
| DIVERGE | Never simulated | [GAP-H-05: DIVERGE state (ED-133 open) — trigger condition unresolved. Cannot simulate until ED-133 closed.] |

**Audit finding AUD-D-01:** CROSS interaction has a latent ambiguity: if both orators score differently-directed CROSS track movements in the same exchange, the resolution order is unspecified. If both move first, the net could be zero. If sequential, the declarer's movement is applied before the responder's, giving the responder a structural advantage (they see the track position before their result is applied). Recommend: CROSS exchanges apply both movements simultaneously after rolling.

`[PROVISIONAL PP-245: CROSS exchange — both genre evaluations resolve simultaneously. Neither orator's movement is visible to the other before application. Net track position after CROSS = position + movement A − movement B (or + movement B if B pushes same direction). Pending ED-133 DIVERGE resolution before CROSS→DIVERGE transition can be defined.]`

---

## AUDIT-03: Faction Domain Action — Ethical Framework Modifier Completeness

**All faction frameworks documented in stage6/params_factions:**

| Faction | Framework | Aligned −1 Ob | Contradict +1 Ob | Special |
|---------|-----------|--------------|------------------|---------|
| Crown | Virtue Ethics | Present-genre actions | Covert/deceptive | — |
| Church | Divine Command | Past-genre + institutional | Revealing Thread truth | +2 Ob Thread reveal |
| Hafenmark | Categorical Imperative | Parliamentary/rules-based | Unilateral | — |
| Varfell | Consequentialism | Information-driven | Ideological commitment | — |
| Guilds | Moral Relativism | GM picks genre | Fixed ideology | — |
| Revolution | Rawlsian Social Contract | Future-genre + equity | Elite alliance | — |
| Niflhel | None | Covert always −1 Ob | Open action | — |
| Lowenritter | Martial Honour | Military/Crown-loyal | Political manipulation | — |

**Finding AUD-03-F1:** Niflhel "covert always −1 Ob" is not in params_factions.md. It appears in stage6 as an ethical framework modifier but is not extracted to params. Minor params maintenance issue.

**Finding AUD-03-F2:** Lowenritter framework "Martial Honour" — the −1/+1 Ob conditions are described narratively in stage6 but not reduced to formula. "Military/Crown-loyal: −1 Ob; Political manipulation: +1 Ob" is an audit derivation, not canonical text. Needs extraction.

**Patch PP-246:** Extract Niflhel and Lowenritter ethical framework modifiers to params_factions.md in the Ethical Framework table.

---

## AUDIT-04: Thread Operation RS Costs — Consistency Check

| Operation | Success RS | Partial RS | Failure RS | Source |
|-----------|-----------|-----------|-----------|--------|
| Weaving | 0 | −1 | −2 | threadwork v25 |
| Pulling | 0 | −1 | −2 | threadwork v25 |
| Past-Oriented Pulling | 0 | −1 | −2 (×scale) | threadwork v25 |
| Locking | −1 | −2 | −3 | threadwork v25 |
| Dissolution | −3 | −6 | −8 | threadwork v25 |
| Mending (success) | +1 | 0 | −2 | threadwork v25 |
| Collective Weaving | Per scale | Per scale | Per scale | threadwork v25 |

**Finding AUD-04-F1:** RS costs are internally consistent across operations — Dissolution is approximately 3× Weaving cost, reflecting its destructive nature. Locking costs less at Success (−1) than Dissolution (−3) but accumulates chronically. The table is correctly calibrated.

**Finding AUD-04-F2:** "Past-Oriented Pulling ×scale" — the scale multiplier is defined for mass battle (×3, ST-TW-03) but not for Personal/Relational/Structural/Territorial/Foundational scales in sequential order. The Foundational scale (Einhir Catastrophe reversal) has an explicit ×3 mentioned in one passage but this is not in the degree table. Gap confirmed from prior audit (no new finding here, but confirms AUD-P1-16 scope).

---

## AUDIT-05: Clock Interaction — TC × IP × RS Cascade Risk

**Three-clock interdependency at current state (TC 45, IP 34, RS 53):**

| Clock pair | Interaction | Current risk |
|-----------|-------------|-------------|
| TC ↑ + RS ↓ | Church action rate increases as world degrades; more Thread suppression orders raise Ob for practitioners → slower RS recovery | ACTIVE — TC 45, RS Fragile |
| IP ↑ + Mandate | Institutional Pressure rise erodes faction Mandate floors; Revolution agitation at IP 34 has near-zero impact but IP 40 threshold changes domain action queuing | LOW — IP 34 below 40 threshold |
| RS ↓ + Faction Stability | RS ≤ 19: all factions make Stability checks Ob 1 per season. Currently RS 53: not triggered | LOW |
| TC 50 threshold | Church may demand formal RS inquiry. Requires Crown cooperation at TC 50. If Crown refuses: IP +2 | APPROACHING — TC 45, 5 points away |

**Finding AUD-05-F1:** TC 50 threshold arriving in 1–2 seasons is the most immediate cascade risk. If Crown refuses Church RS inquiry, IP rises +2 (to 36). This is still below IP 40 (domain action queuing change) but narrows the margin.

**Finding AUD-05-F2:** The three clocks are designed to produce converging crises. At TC 55, RS 48, IP 40: Church has parliamentary leverage, Thread operations are harder, and Crown loses domain priority. This triple-threshold convergence is the mid-to-late campaign pressure the system is designed to produce. From current state (Season 6/7), this convergence is 3–4 seasons away. Pacing is correct.

---

## AUDIT-06: Belief/CP Economy — Mid-Campaign Rate Check

**PC CP totals after Season 6:**
| PC | Total CP | Seasons | Rate |
|----|---------|---------|------|
| Mira | 16 | 6 | 2.7/season |
| Arend | 13 | 6 | 2.2/season |
| Dagmara | 11 | 6 | 1.8/season |
| Theron | 9 | 6 | 1.5/season |

**Expected rate (params, stage2):** 1–4 CP per session from Belief events. At 1 session/season in Hybrid mode: expected 1–4 CP/season.

**Finding AUD-06-F1:** All PCs are in range. Mira (2.7/season) is near the high end — her active Belief 2 (RS investigation) drives consistent CP accumulation. Theron (1.5/season) is at the low end — his Beliefs are slower to trigger (merchant-layer, not front-line).

**Finding AUD-06-F2:** No History advancement in Season 6 for any PC. All PCs need Ob ≥ their primary attribute score to trigger Challenged. Mira (Cog 5) needs Ob ≥ 5 rolls; her Diagnosis was at Ob 3. This means her scholarship History is not advancing despite active use — the roll difficulty is below her attribute. This is correct: the advancement system correctly tracks whether you're being genuinely tested, not just whether you're using the skill. At mid-campaign, PCs should be approaching their first Ob ≥ attribute rolls as they take on larger challenges.

---

## AUDIT SUMMARY — FINDINGS REGISTER (this session)

| ID | Type | Severity | Description | Patch/Editorial |
|----|------|----------|-------------|----------------|
| F-H01 | Confirmed design | — | Forgetting 44% fail rate intentional | None |
| F-H02 | Confirmed design | — | CLASH stalemate at parity intentional | None |
| F-H03 | Gap resolved | P2 | Crown no Intel stat; Influence +1 Ob | PP-236, ED-147 |
| F-H04 | Confirmed design | — | Revolution agitation near-zero win rate intentional | None |
| F-H05 | Gap resolved (provisional) | P2 | Public Instability Hybrid definition | PP-237, ED-148 |
| F-H06 | Simulation error resolved | P2 | Lowenritter trigger undefined; no canonical trigger at Military 6 | PP-238 |
| F-H07 | Simulation error resolved | P1 | RS no natural decay; Season 6 RS corrected | PP-239 |
| F-H08 | Confirmed design | — | Named NPC Inspiration bonus intentional | None |
| F-H09 | Confirmed design | — | Hybrid pacing correct | None |
| SIM-H-02-F1 | New finding | P2 | TS 45 practitioner loses Deep Interior data 60% of time | None (design) |
| SIM-H-02-F2 | New finding | P2 | TS bonus cliff at multiples of 20 — confirmed design | None |
| GAP-H-01 | New gap | P2 | Collective Forgetting rule undefined | ED-153 |
| SIM-H-03-F1 | New finding | P2 | Corrected Crown investigate P(success) ≈ 5% | PP-236 applied |
| SIM-H-03-F2 | New finding | P2 | Crown-Lowenritter delegation incentivised mechanically | PP-241, ED-149 |
| SIM-H-04-F1 | New finding | P1 | AMPLIFY with coordinated orators is decisive | PP-242, ED-150 |
| GAP-H-02 | New gap | P1 | AMPLIFY combined pool cap undefined | PP-242 provisional |
| SIM-H-05-F1 | New finding | P2 | Structural Lock: −8 RS over 5 seasons | None (design) |
| SIM-H-05-F2 | New finding | P2 | Reversal at Ob 5 is ~45% — high stakes priced correctly | None |
| SIM-H-05-F3 | Confirmed design | — | Permanent Lock → only Einhir framework; consistent with setting | None |
| SIM-H-06-F1 | New finding | P2 | 1-result cancels Momentum auto-success on 1D pool | PP-243 |
| SIM-H-06-F2 | Confirmed design | — | Momentum on minimum pool is a genuine risk | None |
| SIM-H-07-F1 | New finding | P1 | Scene→Mass transition provisional modifiers calibrated | PP-244, ED-151 |
| SIM-H-07-F2 | New finding | P1 | Mid-combat zoom: implementation guidance needed | PP-244 |
| GAP-H-03 | New gap | P1 | Domain Echo formal rule undefined | ED-152 |
| AUD-D-01 | Audit finding | P2 | CROSS exchange simultaneity unspecified | PP-245 provisional |
| GAP-H-04 | New gap | P2 | CROSS interaction not simulated | Defer to next session |
| GAP-H-05 | Gap (known) | P1 | DIVERGE state blocked by ED-133 | Deferred |
| AUD-03-F1 | Audit finding | P2 | Niflhel covert −1 Ob not in params_factions | PP-246 |
| AUD-03-F2 | Audit finding | P2 | Lowenritter framework not extracted to params | PP-246 |
| AUD-04-F1 | Confirmed | — | RS costs internally consistent | None |
| AUD-04-F2 | Known gap | P2 | PO-Pull scale multiplier table incomplete | AUD-P1-16 |
| AUD-05-F1 | New finding | P2 | TC 50 threshold imminent (1–2 seasons away) | None |
| AUD-05-F2 | Confirmed design | — | Three-clock convergence pacing correct | None |
| AUD-06-F1 | Confirmed | — | CP rates in range | None |
| AUD-06-F2 | Confirmed design | — | History advancement requires Ob ≥ attribute; working correctly | None |

---

## NEW PATCHES THIS SESSION (PP-236 to PP-246)

| Patch | Description | File | Provisional? |
|-------|-------------|------|-------------|
| PP-236 | Crown covert: Influence pool +1 Ob | params_factions.md | YES |
| PP-237 | Public Instability Hybrid definition | params_factions.md | YES |
| PP-238 | Lowenritter reactive Military NPC guidance | params_factions.md | NO |
| PP-239 | RS no natural decay; correct SIM-H-01 | params_threadwork.md | NO |
| PP-240 | Forgetting Check stacking: deepest Ob per scene, independent across scenes | params_threadwork.md | YES |
| PP-241 | Crown-Lowenritter covert delegation rule | params_factions.md | YES |
| PP-242 | AMPLIFY combined pool cap = highest individual × 2 | params_debate.md | YES |
| PP-243 | Momentum auto-successes add to roll; 1-result can cancel | params_core.md | NO |
| PP-244 | Scene→Mass transition modifier table | params_factions.md (Hybrid section) | YES |
| PP-245 | CROSS exchange simultaneous resolution | params_debate.md | YES |
| PP-246 | Niflhel + Lowenritter ethical framework modifiers extracted | params_factions.md | NO |

## NEW EDITORIAL ITEMS THIS SESSION (ED-147 to ED-153)

| ID | Description | Priority |
|----|-------------|----------|
| ED-147 | Crown covert penalty +1 Ob — confirm modifier | P2 |
| ED-148 | Public Instability Hybrid thresholds — confirm | P2 |
| ED-149 | Crown-Lowenritter delegation: penalty carries or not | P2 |
| ED-150 | AMPLIFY pool cap — confirm ceiling | **P1** |
| ED-151 | Scene→Mass transition modifiers — confirm | **P1-BLOCKER** (AUD-P1-15 resolution) |
| ED-152 | Domain Echo formal rule — confirm definition | **P1-BLOCKER** (Hybrid compilation) |
| ED-153 | Collective Forgetting rule — define | P2 |

---

## P1-BLOCKERS STATUS (all modes)

| ID | Description | Status |
|----|-------------|--------|
| ED-139 | Community Weaving triple spec | Open (user) |
| ED-140 | Discipline degradation trigger | Open (user) |
| ED-142 | BG Overwhelming threshold | Open (user) |
| ED-150 | AMPLIFY pool cap | Provisional (user confirmation needed) |
| ED-151 | Scene→Mass transition modifiers | Provisional (user confirmation needed) |
| ED-152 | Domain Echo formal rule | Provisional (user confirmation needed) |
| AUD-P1-15 | Scene→Mass transition (partially addressed by ED-151) | Provisional |
| AUD-P1-16 | 17 Hybrid gaps pending integration | Ongoing |

---

*Commit targets:*
- `tests/sim_h01_to_h07_resolution_and_audit.md`
- `references/params_factions.md` (PP-236, 237, 238, 241, 244, 246)
- `references/params_threadwork.md` (PP-239, 240)
- `references/params_core.md` (PP-243)
- `references/params_debate.md` (PP-242, 245)
- `canon/patch_register.yaml` (PP-236–246)
- `canon/editorial_ledger.yaml` (ED-147–153)
- `tests/coverage_matrix.md` (SIM-H-02 through SIM-H-07)
- `session_log_current.md`
