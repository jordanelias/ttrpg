<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/worldbuilding/worldbuilding_integration_v3.md (audit of superseded v1). Do not use as a mechanical reference. Retained for audit trail only. -->

# WORLDBUILDING INTEGRATION v1 — SELF-AUDIT
## Canon compliance, cognitive load, mechanical necessity
## Date: 2026-04-03

---

## AUDIT METHOD

For each proposal in the design document, assess:
1. **Canon compliance** — does it violate any P-01 through P-15 constraint?
2. **Cognitive load** — does it add tracking burden? How many new counters, pools, or decision points?
3. **Three-mode necessity** — does it add something mechanically meaningful to BG/Hybrid, or is it TTRPG-only flavour dressed up as mechanics?
4. **Verdict** — KEEP (mechanically necessary), TRIM (reduce to essential), CUT (flavour only / cognitive bloat), or FLAG (needs simulation before deciding)

---

## SECTION 1: SOLMUND RENAME
**Canon:** No violations. Naming is editorial, not mechanical.
**Cognitive load:** Zero — rename only.
**Three-mode:** Applies to all modes (it's a name).
**Verdict:** KEEP. Straightforward cleanup. Haiku-tier.

## SECTION 2: NAME DISCREPANCIES
**Canon:** No violations.
**Cognitive load:** Zero.
**Three-mode:** N/A — naming only.
**Verdict:** KEEP. Editorial decisions, no mechanical impact.

## SECTION 3: CHURCH FOUR-CARDINAL STRUCTURE

### §3.1 Structure table
**Canon:** No violations.
**Cognitive load:** Low — this is reference information, not a new tracking system.
**Three-mode:** Provides the taxonomy that BG modifiers and NPC profiles hang off.
**Verdict:** KEEP.

### §3.2 Cardinal Authority Pool
**Canon:** No violations.
**Cognitive load:** MEDIUM. Creates 4 sub-pools within the Church faction. In practice this means the GM needs to know which Cardinal is rolling which stat. Already partially exists (stage13 gives Olafsson and Jarnstal distinct roles).
**Three-mode:** TTRPG only. BG abstracts to modifiers (§3.3). Hybrid uses this during Zoom In.
**Verdict:** TRIM. The pool sources are just "use the Church stat that matches the Cardinal's portfolio." This isn't new — it's clarifying what already happens when a Cardinal acts. Remove the table and state the rule: "Cardinals roll the Church faction stat relevant to their portfolio."

### §3.2 Cardinal Independence Check
**Canon:** No violations.
**Cognitive load:** LOW. One roll when a Cardinal defies the Holy See. Rare event.
**Three-mode:** TTRPG only. BG doesn't track Cardinal-vs-Confessor disagreements.
**Verdict:** KEEP but mark TTRPG-only. It's a single contested roll on a rare trigger.

### §3.2 Jarnstal Drift Mechanic
**Canon:** No violations.
**Cognitive load:** MEDIUM. New private counter (0–3), GM-tracked. But this parallels the existing Ehrenwall Coup Counter (also 0–3, GM-tracked). Two private counters tracking institutional fracture within the Crown's allied institutions.
**Three-mode:** The CONSEQUENCES matter in all modes (Church Military splitting off is a major campaign event). But the counter itself is TTRPG granularity.
**Verdict:** TRIM. The counter is fine — it mirrors Ehrenwall and the GM already tracks private counters. But the 4-bullet consequence list is too detailed for a design proposal. State: "At Jarnstal Independence 3: Church Military controlled by Jarnstal not Confessor. Church Stability −2, Theocracy Counter (TC) +2. Crown must respond." Cut the rest — it follows from existing systems.

### §3.2 Klapp Awakening Mechanic
**Canon check — P-08:** "Does any mechanic allow non-sensitives to gain Thread-level knowledge through study alone?" Klapp is DEVELOPING Thread Sensitivity through contact with originary locks — this is experiential, not study. His TS 31 is from handling objects, not reading texts. **PASS.**
**Canon check — P-10:** Klapp's transformation must not be framed as corruption. The current text says "internally compromised" and "begins selectively protecting texts." This is a perceptual shift, not moral failure. **PASS.**
**Cognitive load:** MEDIUM. Already exists in stage13. This section just spells out consequences. No new counters.
**Three-mode:** Campaign-level event. Matters in all modes (Church losing Knowledge Arm effectiveness is a faction stat change).
**Verdict:** KEEP. Already in stage13 — this just formalises the downstream effects.

### §3.3 Cardinal Mechanics (Board Game)
**Canon:** No violations.
**Cognitive load:** LOW. Four static modifiers. Player doesn't track anything new — they just know "Church Military actions −1 Ob if Fortitude Cardinal is active."
**Three-mode:** This IS the BG expression. Good.
**Verdict:** KEEP. But **FLAG for simulation** — do these modifiers make Church overpowered? Church already has the highest starting stats. Adding −1 Ob on Military AND +1D on Heresy AND +1 Wealth/season AND −1 Ob on Influence in university territories is four bonuses with no corresponding costs. Cardinal Loss is the intended counterbalance but it requires active player intervention to trigger.
**BALANCE CONCERN:** Church gets 4 passive bonuses. Other factions get 0 from this change. This needs stress testing.

### §3.3 BG Cardinal Loss
**Cognitive load:** LOW. If a Cardinal is removed, modifier disappears. Replacement costs stated.
**Verdict:** KEEP — it's the necessary counterbalance.

### §3.4 Church Levy Rules
**Canon:** No violations.
**Cognitive load:** MEDIUM-HIGH in TTRPG (contested roll + special cases). LOW in BG (+1D modifier).
**Three-mode:** BG version is clean. TTRPG version adds a contested roll between Crown and Church that will occur rarely (only when Crown needs Church levies AND Church refuses).
**Verdict:** TRIM. BG version is good. TTRPG version: cut the "Church refusal" contested roll. If Crown requisitions, Church can comply or refuse. Refusal is a Leadership Deviation (already handled by existing deviation mechanics). Don't add a new contested roll for something the deviation system already covers.
**Church land taxation:** Crown gains +1 Wealth/season per Church-controlled territory at Prosperity 4+. This is a simple rule that makes Church territory control mechanically interesting for Crown. KEEP.

### §3.5 Excommunication Procedure (Enriched)
**Canon:** No violations.
**Cognitive load:** MEDIUM. Adds pre-roll step (Cardinal of Justice recommendation) and post-excommunication resolution paths (Penance, Debate, Banishment).
**Three-mode:** Penance and Banishment are TTRPG flavour. BG already has Excommunication as a single roll. Adding a 3-path resolution to BG would be cognitive bloat.
**Verdict:** TRIM HEAVILY. The Cardinal of Justice recommendation is flavour — it doesn't change the roll. Excommunication already works mechanically. The penance/banishment paths are narrative consequences the GM can adjudicate without a procedure. CUT the table. Keep one line: "Excommunication reversal paths: Penance (1 season public service, voluntary), Grand Debate (5 exchanges, existing), or Banishment (permanent, requires Church Mandate vs Ob 4)."

### §3.6 Almaic Kyriakos
**Canon:** No violations.
**Cognitive load:** MEDIUM. Adds 4 IP threshold events.
**Three-mode:** These are campaign events that fire in all modes. They interact with existing IP thresholds.
**Verdict:** FLAG. The idea is sound — the Altonian religious institution should matter — but 4 new threshold events on the IP ladder adds to an already complex escalation system. **Need to check existing IP thresholds for overcrowding.** If IP already has events at 30, 50, 65, 75, adding Church-specific events at the same thresholds creates simultaneous triggers. Recommend: consolidate to ONE threshold (IP 50: Almaic Kyriakos envoy — Church chooses cooperate or refuse; consequences branch). Cut the rest — they're speculative.

## SECTION 4: LÖWENRITTER INTERNAL STRUCTURE

### §4.1 Structure table
**Verdict:** KEEP. Reference information.

### §4.2 Arm Mechanics (TTRPG)
**Canon:** No violations.
**Cognitive load:** HIGH. Five arms, each with distinct Domain Actions and stat sources. The Lions' Helm naval mechanics add 3 new Domain Actions (Secure Sea Route, Naval Blockade, Coastal Defence). Knights of the Peace add territory-level modifiers (+1 Ob to covert actions, dispute mediation). Royal Investigators add +1D Intel in Valorsplatz.
**Three-mode:** Naval mechanics matter in BG (Schoenland trade, coastal defence). Knights of the Peace modifiers matter in BG. Royal Investigators matter in BG.
**Verdict:** TRIM SIGNIFICANTLY.

Problems:
1. **Lions' Helm naval** adds an entire naval subsystem. Currently no naval mechanics exist anywhere in the game. Introducing them through a Löwenritter sub-arm is scope creep. Naval should be its own design question if it's added at all.
2. **Knights of the Peace "+1 Ob to covert actions"** overlaps with existing Löwenritter Intel stat. If the Löwenritter already has Intel 3, adding a blanket +1 Ob on top is double-dipping.
3. **Dispute mediation** is flavour. It's what Knights of the Peace do narratively, but mechanising it as an Influence vs Ob 2 roll doesn't add meaningful strategic choice.
4. **Royal Guard "+2 Ob to assassination"** is reasonable but niche. How often do assassinations target Court members? This is a modifier on a Niflhel action that already has high Ob.

**Recommended cuts:**
- CUT Lions' Helm entirely. Flag naval as a future design question (ED-NEW-10).
- CUT Knights of the Peace territory modifier. Löwenritter Intel already covers this.
- CUT dispute mediation.
- KEEP Royal Guard as flavour note (no mechanic — just narrative: "assassination in the Imperial Court is nearly impossible while the Royal Guard is active").
- KEEP Riskbreaker identity resolution (ED-006). The loyalty divergence mechanic is clean and adds meaningful tension.

### §4.2 Riskbreaker Identity (ED-006)
**Canon:** No violations. The Riskbreakers' loyalty to "Valoria the concept" creates a structural tension that's philosophically interesting without touching Thread metaphysics.
**Cognitive load:** LOW. One contested roll (Intel vs Ob 2) when Riskbreakers are ordered against their conviction. Rare.
**Three-mode:** TTRPG/Hybrid. BG doesn't track Riskbreaker morale.
**Verdict:** KEEP. Clean, rare trigger, meaningful consequence.

### §4.3 BG Arm Mechanics
**Cognitive load:** LOW — just modifiers.
**Verdict:** TRIM. Remove Lions' Helm (naval cut). Keep: Knights of the Peace as +1 Ob on covert in Crown territories (simple modifier). Keep Royal Investigators +1D Intel in Valorsplatz. Cut the rest.
**Actually — wait.** If we cut Knights of the Peace territory modifier from TTRPG (§4.2), we shouldn't keep it in BG. The BG abstraction should reflect what exists in TTRPG. If Löwenritter Intel already covers anti-covert capability, the BG modifier is redundant too. **CUT.** Löwenritter's existing stats handle this.

### §4.4 Levy Mechanics
**Cognitive load:** MEDIUM. Contested rolls for levy requisition.
**Three-mode:** BG has a simple Muster system. Adding levy requisition contested rolls is TTRPG-only complexity.
**Verdict:** TRIM. State the rule: "Crown may requisition 2/3 of vassal/Church Military (round down) per season. If the vassal objects, use the existing Leadership Deviation mechanics." Don't create a new contested roll.

## SECTION 5: GUILD INTERNAL STRUCTURE AND ECONOMY

### §5.1–5.2 Guild Hierarchy and Guild Council
**Canon:** No violations.
**Cognitive load:** ZERO in play — this is world reference, not a tracking system.
**Three-mode:** TTRPG worldbuilding. BG and Hybrid don't need to know the internal structure.
**Verdict:** KEEP as TTRPG reference. Not a mechanic — it's setting information that the GM uses for scene framing.

### §5.3 Ministry of Guilds
**Canon:** No violations.
**Cognitive load:** HIGH. Three new Crown Domain Actions (Set Guild Taxation, Enforce Non-Competition, Arrange Imperial Contract). Each is a contested roll with multi-stat consequences.
**Three-mode:** These are Crown-vs-Guilds interactions. BG already handles faction conflict through Domain Actions. Adding 3 named sub-types of Domain Action doesn't change the BG framework — it just labels what already happens.
**Verdict:** CUT as standalone mechanics. These are examples of existing Domain Actions, not new ones. Crown Wealth vs Guilds Wealth is already a valid Domain Action. Crown Influence vs Guilds Influence is already valid. Naming them "Set Guild Taxation" doesn't change the roll or the system — it's flavour framing for the GM. State: "Crown Domain Actions targeting Guilds can be framed as: taxation disputes, monopoly enforcement, or contract negotiations. Use existing Domain Action rules."

### §5.4 Guild Entry and Advancement (PC Mechanics)
**Canon:** No violations.
**Cognitive load:** MEDIUM. Three-stage advancement path with Circles tests, History requirements, and Resource costs.
**Three-mode:** TTRPG only. BG and Hybrid don't track PC guild rank.
**Verdict:** TRIM. This is a character background system. The table is fine as TTRPG reference, but it's not a mechanic that needs to be in the faction design doc. It belongs in a character creation or lifepath appendix. Flag as: "Guild advancement path — TTRPG character creation reference. See future character creation doc."

### §5.5 Burgher Status
**Canon:** No violations.
**Cognitive load:** LOW. One binary status (burgher or not).
**Three-mode:** TTRPG only.
**Verdict:** KEEP as one-line reference: "Burgher status = political participation rights for guild members. Guild Masters and Free Masters qualify. Journeymen and Apprentices do not. Burghers may petition Parliament through the Ministry of Guilds." That's it — don't mechanise it further.

### §5.6 Guild Arbitration (ED-009)
**Canon:** No violations.
**Cognitive load:** MEDIUM. A new proceeding type for the debate system.
**Three-mode:** TTRPG/Hybrid (debate happens in Zoom In). BG doesn't resolve debates.
**Verdict:** FLAG. The debate system already has Royal Audience and Church Tribunal. Adding Guild Arbitration is reasonable but needs to be evaluated alongside the debate system design doc. Don't commit it here — route to debate system design doc for integration. Change status from "resolved" to "proposal pending debate system integration."

## SECTION 6: COURT PARLIAMENT AND GOVERNANCE

### §6.1 Structure table
**Verdict:** KEEP as reference. No mechanical load.

### §6.2 Parliamentary Actions table
**Canon:** No violations.
**Cognitive load:** HIGH. Five new named Parliamentary actions (Recommend Policy, Nominate Minister, Nominate Rectorate, Nominate Civil Magistrate, Motion of No Confidence). Each has its own Ob and consequences.
**Three-mode:** BG already has Parliamentary Vote (stage6 §8.11) as a 3-exchange contested roll. Adding 5 sub-types of Parliamentary action in BG would be massive cognitive bloat.
**Verdict:** TRIM HEAVILY. The existing Parliamentary Vote mechanic (§8.11) already handles Parliament. These 5 actions are sub-types that the GM can frame narratively without new rules. The ONLY one that adds a genuinely new mechanic is Motion of No Confidence (deposal), because it has a unique outcome (regime change) that doesn't exist in the current system.

**Keep:** Motion of No Confidence as a named Parliamentary Vote with specific consequences (Crown Mandate drop, succession trigger). This is a campaign-level event that matters in all modes.
**Cut:** The other 4 Parliamentary actions. They're just Domain Actions with Parliament flavour.

### §6.2 Ducal Presence Requirement
**Cognitive load:** LOW. If Duke isn't in Valorsplatz, Influence halved.
**Three-mode:** TTRPG only. BG doesn't track NPC location at this granularity.
**Verdict:** KEEP as TTRPG GM note. One sentence.

### §6.2 Prestige Economics
**Cognitive load:** LOW. Nobles assigned to Court = +1 Influence in Parliament. Nobles at home = +1 to duchy Domain Actions.
**Three-mode:** TTRPG only.
**Verdict:** CUT. This is GM scene-framing material, not a mechanic. The GM already knows that nobles at Court have more national influence and nobles at home have more local influence. Mechanising the +1 adds tracking burden for minimal strategic value.

### §6.3 Ministry Mechanics
**Cognitive load:** HIGH. Four named Ministries, each with a benefit and disruption effect. Disruption requires a Domain Action to trigger.
**Three-mode:** BG doesn't track Ministries. TTRPG only.
**Verdict:** CUT. Ministries are worldbuilding, not mechanics. The GM doesn't need a table telling them that disrupting the Ministry of Taxation reduces Crown Wealth — that's obvious from the fiction. And "Intel or Influence vs Ob 3 to disrupt a Ministry" is just a Domain Action against Crown with extra flavour. Don't create 4 parallel tracking systems.

### §6.4 Deposal Procedure
**Canon:** No violations.
**Cognitive load:** MEDIUM. Multi-step procedure (Parliamentary vote + Holy See concurrence).
**Three-mode:** Campaign-level event. Matters in all modes.
**Verdict:** KEEP. This is a genuine new mechanic — the constitutional right to depose the Monarch is a structural feature of Valoria that creates real strategic options. The Holy See veto gives the Church leverage. Trim to essentials: "Motion of No Confidence passes Parliament (Influence vs Crown Mandate). Holy See must concur. If both: Crown Mandate → 1, Stability −3, succession crisis. If Holy See refuses: TC +3, TT +2."

## SECTION 7: DUCAL ADMINISTRATION

### §7.1 Structure
**Verdict:** KEEP as reference table. No mechanical load.

### §7.2 Levy Mechanics
**Verdict:** TRIM. Same assessment as §4.4. One-line rule: "Crown may requisition 2/3 of vassal Military per season. Vassal refusal = Leadership Deviation."

## SECTION 8: HISTORICAL CONTEXT

### §8.1 Three Nations → Three Duchies
**Canon:** No violations.
**Cognitive load:** ZERO — it's setting information.
**Three-mode:** Worldbuilding reference. Not a mechanic.
**Verdict:** KEEP as reference. The province-to-duchy mapping is useful GM material.

### §8.2 Altonian Cultural Imperialism
**Canon check — P-08:** CORRECTED in previous edit. Now correctly states the epistemological barrier is metaphysical, not institutional/historical. **PASS.**
**Verdict:** KEEP (already fixed).

## SECTION 9: RESTORATION MOVEMENT LEADER (ED-005)

**Canon check — P-08:** Elder Kaldring has TS 22 (Dormant). She cannot perform Thread operations. Her cultural knowledge is politically valuable but cannot bridge the epistemological barrier. This is correct — she's a contact point, not a practitioner. **PASS.**
**Canon check — P-13:** Her TS 22 means she's below the TS 30+ threshold needed to anchor Community Weaving. She needs a PC practitioner. This correctly preserves the barrier. **PASS.**
**Cognitive load:** LOW. One NPC with standard stat block.
**Three-mode:** NPC — appears in TTRPG/Hybrid Zoom In. BG doesn't need her individually.
**Verdict:** KEEP. Clean NPC proposal, canon-compliant.

## SECTION 10: NEW MECHANICS FROM LORE

### §10.1 Tithe Economy
**Cognitive load:** LOW. +1 Wealth from Church-controlled territories at accounting.
**Three-mode:** Works in BG as a simple accounting rule.
**Canon:** No violations.
**Verdict:** FLAG. Church already has the highest starting Wealth (5) and Influence (6). Adding passive Wealth generation from controlled territories makes them even stronger. **BALANCE CONCERN — same as §3.3 Cardinal modifiers.** This needs to be evaluated as part of a Church balance pass, not approved in isolation.

### §10.2 Charity Network
**Cognitive load:** MEDIUM. Church Wealth −1, Mandate +1 in low-Prosperity territories. Contested roll vs Restoration if both present.
**Three-mode:** TTRPG only — BG doesn't track territory-level Mandate for factions.
**Canon:** No violations.
**Verdict:** CUT. This is flavour. The Church can already spend Wealth on Domain Actions to increase Mandate — that IS the existing mechanic. Naming it "charity" and restricting it to low-Prosperity territories adds a constraint without adding a meaningful strategic choice. The contested roll vs Restoration is cute but adds a new roll to every territory where both factions operate.

### §10.3 University Influence
**Cognitive load:** LOW. +1D in university territories.
**Canon:** No violations.
**Verdict:** FLAG. Same Church balance concern. Church gets yet another bonus in specific territories. Needs to be evaluated with §3.3 and §10.1.

### §10.4 Journeymen Years
**Cognitive load:** LOW.
**Three-mode:** TTRPG only.
**Canon:** No violations.
**Verdict:** TRIM. Keep as a one-line campaign hook: "Journeymen Years: PC travels 3+ territories working in different guilds. Qualifies for Free Master. Broadens Circles." Don't mechanise the per-territory bonuses.

### §10.5 Cognatic Senior Succession
**Cognitive load:** ZERO — it's a setting rule.
**Verdict:** KEEP. One sentence.

## SECTION 11: TERRITORY MAPPING
**Verdict:** KEEP. Reference material, no mechanical load. Necessary for reconciliation.

## SECTION 12: EDITORIAL ITEMS
**Verdict:** KEEP. No mechanical impact — it's a tracking table.

---

# SUMMARY: RECOMMENDED ACTIONS

## KEEP (mechanically necessary, canon-compliant, acceptable cognitive load)
- §1 Solmund rename
- §2 Name discrepancies
- §3.1 Church structure table
- §3.2 Cardinal Independence Check (TTRPG only)
- §3.2 Jarnstal Drift (trimmed)
- §3.2 Klapp Awakening (already in stage13)
- §3.3 BG Cardinal modifiers + Cardinal Loss (FLAG for balance)
- §3.4 Church land taxation (+1 Wealth to Crown from Church territories)
- §4.1 Löwenritter structure table
- §4.2 Riskbreaker identity (ED-006 resolution)
- §6.4 Deposal Procedure (trimmed)
- §7.1 Ducal structure table
- §8 Historical context
- §9 Restoration Movement leader (ED-005)
- §10.5 Cognatic succession
- §11 Territory mapping
- §12 Editorial items

## TRIM (reduce to essential rule statement)
- §3.2 Cardinal Authority Pool → one-line rule
- §3.4 Church levy rules → cut contested roll, use deviation mechanics
- §3.5 Excommunication enrichment → one-line additions
- §4.2 Löwenritter arms → CUT Lions' Helm, Knights of Peace modifier, dispute mediation
- §4.4 Levy mechanics → one-line rule
- §5.5 Burgher status → one-line reference
- §6.2 Parliamentary actions → keep only Motion of No Confidence
- §6.2 Ducal Presence → one-line GM note
- §7.2 Levy mechanics → one-line rule
- §10.4 Journeymen Years → one-line campaign hook

## CUT (flavour only, cognitive bloat, or redundant with existing mechanics)
- §5.3 Ministry of Guilds mechanics (these are existing Domain Actions with labels)
- §5.4 Guild advancement table (character creation appendix, not faction design)
- §6.2 Prestige Economics (GM intuition, not a mechanic)
- §6.3 Ministry Mechanics (worldbuilding, not mechanics — 4 parallel tracking systems)
- §10.2 Charity Network (flavour rename of existing Wealth→Mandate Domain Action)

## FLAG FOR SIMULATION (balance concerns)
- §3.3 + §10.1 + §10.3: Church cumulative passive bonuses (4 Cardinal modifiers + tithe Wealth + university Influence). Church is already the strongest faction by starting stats. Adding passive bonuses without costs needs stress testing before approval.
- §3.6 Almaic Kyriakos IP thresholds — needs IP ladder overcrowding check
- §5.6 Guild Arbitration — route to debate system design doc

## CANON VIOLATIONS FOUND
- §8.2 (ALREADY FIXED): Incorrectly attributed the Forgetting to Altonian cultural destruction. P-08 violation. Corrected in prior commit.
- No other canon violations detected.

## NEW EDITORIAL ITEMS FROM AUDIT
- ED-NEW-10: Naval mechanics as future design question (Lions' Helm cut pending naval system design)
- BALANCE-FLAG-01: Church cumulative passive bonuses from Cardinals + Tithes + University need stress testing before any are approved for BG
