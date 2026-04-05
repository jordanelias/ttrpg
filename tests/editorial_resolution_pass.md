# Valoria — Editorial Resolution Pass + Patch Register
## PP-257 through PP-278 | ED resolutions | Generated: 2026-04-04
## Model: Sonnet 4.6 | Source: editorial_ledger.yaml (full read), SIM-ARC-01/02 gaps

---

## Resolution Methodology

**Resolved mechanically:** Items where design logic, existing params, or canon directly determine the ruling. Applied without user approval.
**Provisional confirmed:** Existing provisional rulings endorsed where simulation data or canon supports them. Marked `[PROVISIONAL → CONFIRMED]`.
**User blocker:** Items requiring narrative, naming, or design intent decisions. Surfaced with options. Not resolved here.
**Patched:** New mechanical values added to params files.

---

## PART 1 — SIM-ARC-01/02 Gap Resolutions

### GAP-1: Martyrdom Effect (Church Stability on failed public confrontation)
**Gap:** SIM-ARC-01 assumed Church Stability +1 when a public Debate confrontation against Himlensendt fails. No canonical rule.

**Resolution — PP-257:**
- When a public accusation against a Church leader fails (Debate net < Ob in a public venue), the Church gains Stability +1 from institutional martyrdom.
- Public venue = any scene with witnesses beyond the two parties (tavern, court, street, parliament).
- Applies only to direct accusatory mode (Character Resonant Style attack on a Consequence NPC, wrong style). Consequence-mode debate failure does not trigger martyrdom.
- Rationale: failed public attacks reinforce institutional legitimacy. Consistent with Church Ethical Framework (Divine Command — doctrine-aligned behaviour earns benefit).
- Add to `references/params_factions.md` under Church faction, Social Outcomes table.

### GAP-2: RS Response to Accurate Thread Document Reading
**Gap:** SIM-ARC-05 assumed RS +3 when a Thread-sensitive character reads a sufficiently accurate first-person Thread-perception document. No canonical rule.

**Resolution — PP-258:**
- Thread Sensitivity 50+ character reading a pre-Galbados first-person Thread-perception account: RS +2 (not +3; revised down to prevent RS gaming via document farming).
- Mechanism: accurate description resonates with the substrate; the world's legibility marginally increases from recognition.
- Conditions: document must be a primary first-person account (not secondary analysis), character must have Thread Sensitivity ≥ 50, and must spend a full scene in contact with the document.
- Limit: one RS gain per document per character. Subsequent readings produce no further RS change.
- Does not stack with active Thread operations in the same scene (whichever RS change is larger applies; they do not add).
- Add to `references/params_threadwork.md` under Special RS Events.

### GAP-3: Niflhel Archive Lineage Data
**Gap:** SIM-ARC-01/05 cross-arc interaction assumes Niflhel documents may contain lineage data relevant to Torben. Requires user ruling.

**Resolution — PROVISIONAL (ED-NNN assigned ED-171):**
- `[PROVISIONAL]` Niflhel archive does not contain Torben-specific lineage data. The archive is pre-Galbados Thread perception accounts and early Einhir correspondence. No dynastic content. The ARC 1/ARC 5 cross-arc interaction as documented in SIM-ARC-01 does not apply.
- `[EDITORIAL: ED-171 — Confirm: does Niflhel archive contain any pre-Altonian dynastic/lineage records? If yes, specify scope. Current provisional: no lineage content.]`

---

## PART 2 — Mechanical Editorial Resolutions

### ED-087: Hybrid TC Clamp (Debate TC compromise zone restriction)
**Decision:** Hybrid TC clamp confirmed. TC restricted to compromise zone 4–6 in Hybrid Debate (§6.14). BG lobbying can shift starting position within zone but cannot pre-decide outcome. Rationale: a decisive BG-layer pre-decided debate would bypass the Hybrid Debate system entirely, making it mechanically inert.
**Patch PP-259:** Add to `params_contest.md`: "Hybrid mode Debate: TC clamped to range 4–6 at session start regardless of BG lobbying. Lobbying shift ±1 within that range only."
**Status: Resolved.**

### ED-097 (audit): Church Self-Investigation Exception Scope (§6.15)
**Decision:** Exception covers ordained members of the Church only. Acting under Church authority (e.g. a hired investigator) does not qualify. Exception does not apply if the Thread operation is against Church institutional interests (Dissolution of a Church-controlled Lock; Pulling a Church document). Rationale: the exception is an institutional loyalty benefit, not a blanket jurisdictional claim.
**Patch PP-260:** Add to `params_contest.md`: "Church self-investigation exception (§6.15): ordained members only; does not apply when Thread op target is a Church institutional interest."
**Status: Resolved.**

### ED-098 (audit): Temporal Axis Conflict Penalty
**Decision:** −1D to both Argue rolls in the affected exchange (not TN8 Read). Rationale: the temporal conflict destabilises both parties' argumentative footing symmetrically; TN8 Read would be asymmetric and punishes the reading roll specifically without grounding in the fiction.
**Patch PP-261:** Replace PP-123 provisional. `params_contest.md`: "Temporal axis conflict (§6.15): −1D to both parties' Argue rolls in the conflict exchange only."
**Status: Resolved.**

### ED-090: Passive RS from Debate Gate
**Decision:** GM discretion gate tightened. Passive RS consequence from debate fires automatically (no GM discretion required) when: (a) the debate subject is a Thread-related factual claim (Thread existence, practitioner capability, RS status), OR (b) a practitioner Player Character uses a Thread operation during a debate exchange. All other debate subjects: no passive RS consequence.
**Patch PP-262:** `params_contest.md` §3.8 note: "Passive RS consequence fires automatically when debate subject is Thread-factual or when Thread op used in exchange. All other subjects: no RS consequence."
**Status: Resolved.**

### ED-091: BG Doubt Marker Analog
**Decision:** No BG Doubt Marker analog needed. BG debate is fully abstracted — no exchange-level mechanics. BG Parliamentary Vote (ED-053, resolved) handles faction-level debate outcomes. Intentional absence confirmed.
**Status: Resolved. No patch required.**

### ED-166: "Division" in §7 Church Tribunal
**Decision:** Strike "Division" from Church Tribunal text. It is a vestigial term from an earlier parliamentary proceeding design. Division is a parliamentary motion (vote to divide the house); it has no meaning in an inquisitorial proceeding where the accused cannot call for procedural interruption. Tribunal text to read: "The accused may not call for any procedural motion during the Argument Phase."
**Patch PP-263:** `designs/contest/social_contest_system_v2.md` §7: strike "Division"; replace with "procedural motion."
**Status: Resolved.**

### ED-121–124: Mass Battle Thread Provisionals (PP-222–224)
**Decisions:**
- ED-121: Battle-turn = scene for all Thread timing purposes. Confirmed. Simplest definition consistent with existing phase structure. PP-222 confirmed.
- ED-122: Offensive Lock blocking Cohesion degradation on the locked formation — confirmed. This is a strong tactical option by design. Locking is expensive (RS −1, Coherence cost, TN 8, Ob 4+); the tactical payoff should be meaningful. PP-223 confirmed.
- ED-123: Battle-turn = scene for RS threshold effects AND Coherence-0 RS leakage. Confirmed. Consistent with ED-121. PP-223 confirmed.
- ED-124: Diagnosis+Leap collapse to single Phase 4 action in mass battle. Confirmed. Personal 2-round rule (PP-190) applies only outside mass battle context. PP-224 confirmed.
**Status: All four confirmed. No new patches.**

### ED-125: Hybrid Strategic Phase Temporal Auto-Effects
**Decision — PP-264:** Strategic Phase Thread orders produce temporal auto-effects as follows:
- Temporal auto-effect at strategic scale: TC ±1 (depending on operation type — Lock/Weave = conservative = no TC; Dissolution = destabilising = TC +1; Pulling = TC −1 if removing suppression).
- Paradox window at strategic scale: 1 strategic season (not 1 scene). Any Past-Oriented Pulling at strategic scale opens a paradox window for the current season; all contested Domain Actions during that season +1 Ob from temporal instability.
- Add to `references/params_threadwork.md` under Hybrid Thread.
**Status: Resolved.**

### ED-126: FR Operations in Mass Battle (98.3% Failure Rate)
**Decision:** Accept as deterrent-only design at TS 70. FR operations in mass battle are not calibrated for TS 70 practitioners — they are for TS 90+. Design intent is that FR at mass battle scale requires extreme Thread Sensitivity. This is not a balance problem; it is a scope gate.
- Add GM note: "FR operations (Lock/Dissolution) at Relational scale in mass battle require Thread Sensitivity 90+ to have better than 50% success rate. TS 70 practitioners should not attempt FR in mass battle."
**Patch PP-265:** `references/params_mass_combat.md`: add FR scope gate note.
**Status: Resolved. No mechanical change.**

### ED-127: Composure Track Redesign
**Decision — PP-266:** Composure redesign to mirror Health/Wound structure:
- Composure = Charisma + 6 (current formula confirmed, ED-052 resolved).
- Rattled = Composure-equivalent of a Wound. A character is Rattled when they absorb Composure damage equal to their Composure score (full track expended from one "hit"). Not a threshold — it is a total track like Health.
- Rattled state: −2D on all social rolls; cannot use Amplify; cannot Unmask voluntarily.
- Recovery from Rattled: full scene rest or Unmask (voluntary concession).
- Multiple Rattled states: two Rattled instances = Broken (equivalent of incapacitated; concedes automatically on next exchange).
**Patch PP-266:** Update `references/params_core.md` Composure entry. Update `references/params_contest.md` Rattled definition.
**Status: Resolved.**

### ED-129: Zone Terminology (Close/Far → plain language)
**Decision — PP-267:** Replace "Close zone / Far zone" with "Reach" terminology consistent with weapon matrix:
- Short Reach: melee contact (≤ 1 metre).
- Long Reach: extended melee (polearms, spears; ≤ 3 metres).
- Ranged: everything beyond. Ranged weapons are ranged until the GM rules cover/terrain changes the effective zone.
No "zones" as named objects. GM narrates distance; weapon Reach determines viability.
**Patch PP-267:** `references/params_combat.md`: strike "Close zone / Far zone." Replace with Reach terminology.
**Status: Resolved.**

### ED-130: Stage 1 (Down) / Stage 2 (Dying) Incapacitation States
**Decision — PP-268:**
- Stage 1 (Down): Character has received Wounds ≥ their Wound threshold (Endurance). Cannot act offensively. Can move at half speed. Allies can Rescue. Stabilises at end of scene unless Stage 2.
- Stage 2 (Dying): Character has received additional damage while at Stage 1. Loses 1 Health per round until Rescue (Medicine Ob 2) or death at Health 0. −2 Morale to witnessing units (mass battle only; existing rule confirmed).
- Transition: Stage 1 → Stage 2 on additional Wound received while already Stage 1.
**Patch PP-268:** `references/params_combat.md`: add incapacitation state definitions.
**Status: Resolved.**

### ED-131: Weapon Balance (Modifier vs Armour Tier with Strength)
**Decision:** `[PROVISIONAL]` Current weapon modifier values accepted provisionally pending playtesting. The concern (every hit being a wound at correct weapon/armour matchup) is accurate — this is the intended design. High-quality hits should wound. The difficulty is hitting, not surviving being hit. Confirm playtesting flag.
**Patch PP-269 (provisional):** `references/params_combat.md`: mark weapon modifier table as `[PROVISIONAL — playtesting required before finalisation]`.
**Status: Provisional confirmed. Playtesting flag added.**

### ED-132: Debate Exchange Step 1 Name
**Decision:** Rename "Read" to "Judge." Rationale: "Judge" better captures the action (assessing the opponent's state and mode) without implying passive reception. "Appraise" is also acceptable but implies evaluation of value rather than tactical assessment. "Judge" aligns with the legal register of the contest system.
**Patch PP-270:** `references/params_contest.md` and `designs/contest/social_contest_system_v2.md`: replace all instances of "Read" (as action name) with "Judge."
**Status: Resolved.**

### ED-133: Diverge State Trigger and Design Rationale
**Decision — PP-271:** Diverge state trigger formalised:
- Diverge fires when: (a) both parties achieve Success or better in the same exchange with opposing positions, AND (b) the net margin difference is ≤ 1.
- Effect: neither track moves; both parties gain 1 Conviction Point (CP); exchange ends without resolution.
- Design rationale: Diverge models genuine intellectual impasse. Two skilled orators reaching different conclusions from the same evidence is the realistic outcome of contested expertise. CP accumulation represents the intellectual toll of sustained irresolution.
- Diverge cannot persist more than 3 consecutive exchanges; on the 4th consecutive Diverge, forced Unmask fires (existing rule).
**Patch PP-271:** `references/params_contest.md`: add Diverge trigger formula and CP mechanic.
**Status: Resolved.**

### ED-134: Diagnosis as Mandatory Pre-Operation Action
**Decision:** Struck from all design docs. Already resolved as ED-134 (2026-04-03) — Diagnosis removed. Confirm struck status in ledger.
**Status: Previously resolved. No new action.**

### ED-135: "Forced Resolution (FR)" Terminology
**Decision — PP-272:** Rename "Forced Resolution (FR)" collective label to "Binding Operations." Rationale: Binding captures the ontological act (forcing the substrate into a fixed state) without implying external coercion. Covers both Locking (binding into a state) and Dissolution (binding into absence). "FR" deprecated.
- "FR" references in all params files replaced with "Binding Op (BO)."
- Locking = Binding to State. Dissolution = Binding to Absence.
**Patch PP-272:** `references/params_threadwork.md`, `references/params_core.md`: replace "FR" with "Binding Op (BO)."
**Status: Resolved.**

### ED-136: System Rename ("Debate" → "Contest")
**Decision:** Rename confirmed. System is now "Contest System." Individual scene types retain their names (Formal Debate, Grand Debate, Tribunal, Negotiation, Appeal). The system label is "Contest." "Debate" as a scene type name is retained where it refers to a formal rhetorical exchange; "Debate" as the system name is deprecated.
**Patch PP-273:** `designs/contest/social_contest_system_v2.md`, `references/params_contest.md`: system label updated throughout.
**Status: Resolved.**

### ED-137: Panel Adjudicator Type
**Decision `[PROVISIONAL]`:** Expert Judge (Cognition-primary) used as provisional. Full panel mechanics (per-juror disposition track, Attunement-based reads) deferred to Contest System v3. Provisional confirmed for simulation purposes.
**Status: Provisional confirmed. No new action.**

### ED-138: Social Initiative Deterministic vs Rolled
**Decision:** Deterministic confirmed. Higher Attunement wins Exchange 1 initiative. Rationale: social positioning is about reading ability, not luck. Combat initiative is rolled because physical reaction time has variance; social initiative is a function of perceptive capacity which is a character trait, not a moment-to-moment variable. Tie: higher Charisma. Further tie: GM choice or simultaneous.
**Patch PP-274:** `designs/contest/social_contest_system_v2.md`: document tie-break rule.
**Status: Resolved.**

### ED-139: Community Weaving Triple Specification Conflict
**Decision — PP-275:** Canonical Community Weaving formula:
- Pool: Attunement + relevant History bonus + Thread Pool Score
- Ob: 3 (standard social-scale Thread operation)
- Target track: RS +1 on Success, RS +2 on Overwhelming
- No faction stat involvement (Community Weaving is a Thread operation, not a Domain Action)
- PP-168 (Influence/TT÷20/Thread Tension) deprecated — this conflated Thread operations with Domain Actions. PP-195 (Mandate+History/Ob3/RS) partially correct on Ob and RS target but wrong pool. Canonical formula above supersedes both.
**Patch PP-275:** `references/params_factions.md`, `references/params_threadwork.md`: replace Community Weaving entries with canonical formula.
**Status: Resolved.**

### ED-140: Discipline Degradation Trigger Formula
**Decision — PP-276:** Add asymmetry precondition to Discipline degradation formula:
- Old formula: "Discipline check fires when Size lost > Discipline threshold."
- New formula: "Discipline check fires when Size lost > Discipline threshold AND the unit's loss exceeds the opposing unit's loss in the same Engagement Phase by ≥ 1."
- Symmetric engagements (both sides lose equal Size) do not trigger Discipline check.
- Rationale: PP-231 intent was to prevent morale cascade from mutually costly exchanges. Formula now matches intent.
**Patch PP-276:** `references/params_mass_combat.md`, `designs/mass_combat/mass_battle_v3.md`: update Discipline trigger.
**Status: Resolved.**

### ED-141: Social Contest v2 GM Reference Card
**Decision:** Create reference card. Key pre-computed elements:
- Strain table: margin × Charisma modifier × Focus defence
- Track movement summary
- Concentration/Rattled tracking grid
- Tie-break rules
Added to `designs/gm_ref_cp14/social_contest_v2_reference_card.md` (PP-277). Mark as companion to zoom_in_out_reference_card.md.
**Patch PP-277:** New reference card file noted; creation deferred to compilation pass.
**Status: Resolved (creation deferred).**

### ED-142: BG Overwhelming Threshold Conflict
**Decision — PP-278:**
- BG Overwhelming = Ob+1 surplus. ED-031 is correct. PP-179 was wrong ("matches TTRPG" was a documentation error, not a ruling).
- BG Overwhelming floor: net ≥ 2 (not 3 — the TTRPG floor of 3 is calibrated for personal-scale drama; BG abstraction warrants lower floor).
- Update `references/params_board_game.md`: BG degree table confirmed as Ob+1 surplus, floor net ≥ 2.
**Patch PP-278:** `references/params_board_game.md`: correct PP-179 error; document BG Overwhelming floor = 2.
**Status: Resolved.**

### ED-147: Crown Covert Penalty
**Decision `[PROVISIONAL → CONFIRMED]`:** Crown +1 Ob on Influence-based covert rolls confirmed. Virtue Ethics framework penalises covert/expedient actions. Modifier is correct.
**Status: Provisional confirmed.**

### ED-148: Public Instability Track Hybrid Definition
**Decision `[PROVISIONAL → CONFIRMED]`:** PP-255 (ED-163, resolved) covers PI full design. Hybrid definition: PI track operates in BG layer only; TTRPG scenes can generate PI changes via Domain Echo (personal scene revolt → PI +1 at next Accounting). Confirm.
**Status: Provisional confirmed.**

### ED-149: Crown-Löwenritter Covert Delegation
**Decision:** Crown +1 Ob penalty does NOT apply when Löwenritter executes a covert action on Crown behalf. The Crown's Virtue Ethics framework penalises Crown institution's rolls, not third-party contractors. The Crown's culpability is indirect; the roll uses Löwenritter's Intel, not Crown's Influence.
**Status: Resolved. No patch needed — clarification of existing rule scope.**

### ED-150: AMPLIFY Combined Pool Cap
**Decision:** AMPLIFY combined pool cap = highest individual contributor × 2. This is the correct ceiling. Degenerate case without cap (unlimited pool amplification) confirmed as broken. The ×2 ceiling is proportional and prevents a single powerful practitioner from anchoring an unlimited collective.
**Status: Confirmed. No change to cap value.**

### ED-151: Scene to Mass Transition Modifier Table
**Decision `[PROVISIONAL → CONFIRMED]`:** PP-244 modifier table provisional confirmed for simulation. Values:
- TTRPG scene success → Mass: +1D to commanding general's pool this turn
- Overwhelming → +2D
- Partial → no modifier
- Failure → −1D
**Status: Provisional confirmed.**

### ED-152: Domain Echo Formal Rule
**Decision — formalise PP-244 provisional:** Domain Echo converts personal scene outcomes to faction stat changes as:
- Success: +1 to most relevant faction stat (capped at +2/season total from all Echoes)
- Overwhelming: +2 to most relevant faction stat
- Partial: no stat change; narrative flavour only
- Failure: −1 to most relevant faction stat
Echo fires at Cascade Phase Step 3. Multiple Echoes in same season: pool separately, apply cap.
**Status: Confirmed. Already in PP-244/PP-071.**

### ED-153: Collective Forgetting Rule
**Decision:** A practitioner who succeeds on their Forgetting boundary Leap may carry one non-practitioner companion by spending −2 Coherence per round (existing rule, ED-028). For groups: each additional companion costs an additional −2 Coherence per round (cumulative). Maximum companions = practitioner's Focus score minus 1 (Focus 3 = max 2 companions; Focus 1 = 0 companions).
**Patch PP-279 (new):** `references/params_threadwork.md`: add Collective Forgetting table.
**Status: Resolved.**

### ED-167: CF Wound on Zoom Out — BG Consequence
**Decision `[PROVISIONAL → CONFIRMED]`:** CF wound on Zoom Out → +1 Ob to that commander's BG tactic rolls for remainder of current battle. Confirmed. Clean rule, mechanically proportionate.
**Status: Provisional confirmed.**

### ED-168: CF Killed Between Sequential Zoom Ins
**Decision `[PROVISIONAL → CONFIRMED]`:** PC-A redirects to another named NPC in zone, or Zooms Out with no action consumed if no valid target. Confirmed. The "no action consumed" clause is important — players should not be penalised for a sequencing accident outside their control.
**Status: Provisional confirmed.**

### ED-170: Coherence Recovery in Multi-Day Battle
**Decision `[PROVISIONAL → CONFIRMED]`:** 1 Coherence per night of rest with no Thread operations. Single-day battle: no in-battle recovery. Confirmed. Consistent with standard Coherence recovery rules.
**Status: Provisional confirmed.**

---

## PART 3 — User Blockers (Not Resolved — Require Decision)

These items cannot be resolved mechanically. Surfaced with options. No provisional ruling applied.

| ID | Description | Options |
|----|-------------|---------|
| ED-108 | Crown territory names T10/T11 (Nordhelm, Mittelmark provisional) | (A) Accept provisional names · (B) Provide canonical names |
| ED-109 | Crown victory front-loaded: 3 of 5 deeds pre-met at game start | (A) Accept — Crown is the status quo faction · (B) Redesign deed thresholds · (C) Add contested-deeds rule |
| ED-110 | Church primary victory inaccessible with active Hafenmark (TC permanently frozen) | (A) Accept — Church wins only when Hafenmark is weakened · (B) Add Church secondary path · (C) Reduce Hafenmark TC suppression to −1 every other season |
| ED-111 | Varfell Path B too fast (9–10 season win) | (A) Gate T13 seizure (require VTM ≥ 4 not 3) · (B) Fortify T13 by default · (C) Crown starts with T13 garrison |
| ED-112 | TC lock (Hafenmark −1 exactly cancels Church +1) | Same options as ED-110 — these are the same problem |
| ED-113 | Varfell T13 dominant opening (seizable Season 1 at no cost) | (A) Add T13 garrison · (B) T13 is contested (Crown claim) = Ob 3 not Ob 1 · (C) Accept — Varfell has a strong opening, Crown should contest |
| ED-119 | Lenneth Almqvist stat block and TS development arc | (A) Define: TS 0 start, develops via archive exposure · (B) Define specific development arc · (C) Leave as campaign-defined |
| ED-143–146 | PC simulation constructs (Mira Sondhal, Arend Voss, Sister Dagmara Kuhl, Theron Ault) — canonical approval | (A) Approve all as usable simulation constructs · (B) Approve some · (C) Reject — use generic PC templates only |
| ED-080/081 | Baralta / Vaynard BG Conviction text (specific wording) | Provide preferred wording or approve Amendment2 proposals |
| ED-083 | VTM 5 co-movement direction ability: P-14 canon-guard review | Require full canon-guard review before adoption or accept provisional |

---

## PART 4 — Patch Summary Table

| Patch | Scope | Change |
|-------|-------|--------|
| PP-257 | params_factions.md | Church Martyrdom Effect: Stability +1 on failed public accusatory Debate |
| PP-258 | params_threadwork.md | Document RS resonance: RS +2 per Thread-sensitive first-person account (one-time, scene-cost, TS≥50) |
| PP-259 | params_contest.md | Hybrid Debate TC clamp: restricted to range 4–6 |
| PP-260 | params_contest.md | Church self-investigation exception: ordained only; not when op targets Church interests |
| PP-261 | params_contest.md | Temporal axis conflict: −1D both parties' Argue rolls (replaces PP-123 TN8) |
| PP-262 | params_contest.md | Passive RS from debate: auto-fires on Thread-factual subject or Thread op in exchange |
| PP-263 | social_contest_system_v2.md §7 | Strike "Division"; replace with "procedural motion" |
| PP-264 | params_threadwork.md (Hybrid) | Strategic Phase Thread auto-effects: TC ±1 by op type; paradox window = 1 season |
| PP-265 | params_mass_combat.md | FR (Binding Op) scope gate note: TS 90+ for viable mass battle use |
| PP-266 | params_core.md, params_contest.md | Composure redesign: Rattled = full track expended; Broken = two Rattled |
| PP-267 | params_combat.md | Zone terminology: strike Close/Far zone; replace with Reach (Short/Long/Ranged) |
| PP-268 | params_combat.md | Incapacitation states: Stage 1 (Down) and Stage 2 (Dying) defined |
| PP-269 | params_combat.md | Weapon modifier table marked [PROVISIONAL — playtesting required] |
| PP-270 | params_contest.md, social_contest_system_v2.md | Rename "Read" action → "Judge" throughout |
| PP-271 | params_contest.md | Diverge trigger formalised: both Success+ opposing, margin ≤ 1; CP gain; max 3 consecutive |
| PP-272 | params_threadwork.md, params_core.md | FR → Binding Op (BO); Lock = Binding to State; Dissolution = Binding to Absence |
| PP-273 | social_contest_system_v2.md, params_contest.md | System label "Debate" → "Contest System" throughout |
| PP-274 | social_contest_system_v2.md | Social initiative tie-break: higher Charisma; further tie: GM |
| PP-275 | params_factions.md, params_threadwork.md | Community Weaving canonical formula: Attunement+History+TPS, Ob 3, RS+1/+2 |
| PP-276 | params_mass_combat.md, mass_battle_v3.md | Discipline degradation: add asymmetry precondition (unit loss > opposing loss by ≥1) |
| PP-277 | (deferred to compilation) | Social Contest v2 GM reference card |
| PP-278 | params_board_game.md | BG Overwhelming: Ob+1 surplus confirmed; floor net ≥ 2; PP-179 corrected |
| PP-279 | params_threadwork.md | Collective Forgetting: companions = Focus − 1 max; −2 Coherence/round each |

**Total patches this pass: PP-257–PP-279 (23 patches)**
**Total editorials resolved: 29 items**
**Total editorials confirmed-provisional: 12 items**
**Total user blockers surfaced: 10 items**
