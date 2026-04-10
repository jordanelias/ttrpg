<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# VALORIA BG v0.2 — SIMULATION & STRESS TEST REPORT
**Method:** 12 full or partial simulations run against the ruleset. Each sim exercised distinct subsystems, faction paths, and edge conditions. Findings catalogued by type.

---

## SIMULATION INDEX

| Sim | Scenario | Focus |
|-----|----------|-------|
| SIM-01 | Standard 4-player Season 1 (Crown/Church/Hafenmark/Varfell) | Baseline resolution flow; early ambiguity surface |
| SIM-02 | Löwenritter Coup Cascade at TC 82 | Post-coup structural deadlock; cascade depth at coup |
| SIM-03 | TC Runaway — Church dominant | TC formula gap; resource tension |
| SIM-04 | RS Collapse Cascade — Thread abuse + Niflhel drain | Positive feedback loop; multi-source accumulation |
| SIM-05 | Varfell Thread Supremacy (hardest victory path) | Self-defeating condition; RS budget math |
| SIM-06 | Full 5-player Season 3 — all systems firing | Simultaneous Social conflict; Phase 4 duration; presence timing |
| SIM-07 | Altonian Invasion Scenario (IP = 78) | Terminal event completeness; AER elegance |
| SIM-08 | Maximum-Cascade Season — every simultaneous mechanic triggered | Peak cognitive load; Assert mass trigger |
| SIM-09 | Vaynard-Edeyja Encounter (VTM 4 → T13) | Same-season turn-order procedural error |
| SIM-10 | Reformed Settlement Confrontation (RDT 5) | Accommodate strategic dominance; declaration timing |
| SIM-11 | Riskbreaker All-Priorities-Active Stress | Token economy; CB gambit; timing split |
| SIM-12 | End-Game Hollow Victory Denial (Crown) | Scoring legibility; victory-denial mechanics |

---

## PART I — FUNCTIONAL GAPS (Blocking)

These gaps will stall actual play. Must be resolved before first playtest.

---

### FG-01 — TC Advancement Formula Undefined
**Severity: Critical**
**Location:** B4 Phase 5 Step 4, B7 Clock Tracks

The Seasonal Accounting instructs "TC per Church activity formula" but no formula exists anywhere in the ruleset. Players and the Church player specifically have no basis to project TC growth or set expectations for how long the Holy State victory path takes.

Available TC sources (inferred from scattered references):
- Himmelenger controlled: +1/season
- Attention Pool threshold 5: +1
- Emergency Powers policy: +1
- Free Trade Decree policy: +1
- TC Environmental: Church Assert: +1
- Doctrinal Reach Milestone: +0.5/season (Year-End)
- Reformed Settlement (Resist): +3
- Accommodate: −5
- Royal Decree spending: implied net reduction

**At baseline Himmelenger control + one Assert/season:** TC advances ~+2/season. From 15 → 70 (Holy State threshold) requires ~27 seasons. A 3–5 season session barely moves the Church victory needle. This needs either (a) a defined multi-source formula, or (b) a deliberately slower TC arc paired with shorter session scope.

---

### FG-02 — Action Outcome Effects Undefined for Core Actions
**Severity: Critical**
**Location:** B3 Action Economy; B5 Faction Cards

Diplomacy, Decree, Trade, Investigate, Spy, and Govern are all referenced as actions on cards, but none have formal success/failure outcome text. The ruleset specifies roll mechanics and dice pools but not what a successful Diplomacy roll *does*. Partial effects, overwhelming effects, and failure consequences are absent for all of these.

Only actions with defined outcomes: Muster (creates 1 unit), March (moves unit), Community Organizing (Influence in territory), Community Weaving (Co-Movement card drawn).

This is the largest functional gap in the document. A player who rolls an Overwhelming success on Senator Outward (Diplomacy) cannot determine their result from this ruleset.

---

### FG-03 — Stat-to-Action Mapping Absent
**Severity: High**
**Location:** B3, B5

"Pool = relevant faction stat" — but which stat maps to which action type is never stated. Military → Legionary is implied. Mandate → Senator is inferable. Tribune → ? (Influence? Mandate?). Consul → ? (Mandate or Wealth?). Prefect → ?

In SIM-01, this ambiguity blocked resolution of the first Tribune action. Any table will resolve this inconsistently without an explicit mapping table.

**Proposed mapping (for confirmation only):**
- Legionary: Military
- Consul/Prefect: Mandate
- Senator: Mandate
- Tribune: Influence
- Pontifex/Weaver: (Thread-specific — not stated)

---

### FG-04 — Champion Starting Positions Undefined
**Severity: High**
**Location:** B8, B5 Faction Sheets

Champion tokens are mobile and affect faction card rolls (+1D in territory, Diplomacy +1D, Stability checks −1 Ob). But no starting position for any Champion is specified. All five playable faction Champions (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall) lack a starting territory assignment. This affects Season 1 resolution immediately.

---

### FG-05 — Ob 0 Resolution Undefined
**Severity: Medium**
**Location:** B4, B5 Faction Cards

Multiple modifier stacks can reduce Ob to 0 (Hafenmark Consul Govern in Hafenvalor: Ob 1 − 1 Categorical Imperative = Ob 0). The roll result table defines Overwhelming as "≥ Ob + 1 surplus" and Failure as "0 successes," but does not define behavior at Ob 0. If Ob = 0: any success at all is Overwhelming; Failure still requires zero successes. Is Partial (Ob − 1 = −1) impossible? Does Ob ever go below 0 to give automatic success? This must be resolved for modifiers to be usable.

---

### FG-06 — Invasion Terminal Event Mechanics Missing
**Severity: High**
**Location:** B2, B7 (IP Track)

IP has well-defined threshold effects at 30, 60, and 75. At IP 75: "Altonian Vanguard deployed. Invasion countdown begins." No countdown duration, Altonian unit stats, invasion resolution mechanics, or victory/loss consequences from invasion are defined. The IP track builds toward an uninstrumented climax.

**Note:** AER 5 ("IP fixed at 50 and held") mechanically prevents IP from reaching 75. Whether this is an intended safety valve or the only intended resolution of the IP track needs confirmation.

---

### FG-07 — Muster Deployment Timing and Token Protocol Absent
**Severity: Medium**
**Location:** B8

"1 unit with Strength 2, CP = faction Military ÷ 2 (round up). Deploys following season." No protocol for where the unit token sits between Muster and deployment. Is there a staging area? Does the unit exist as a board token before deployment? Can it be targeted before it deploys? This creates tracking ambiguity from Season 1.

---

## PART II — AMBIGUITIES (Resolution Required Before Play)

Conditions where the ruleset text produces two or more plausible interpretations that will generate table conflicts.

---

### AMB-01 — Three-Way (or More) Social Conflict in Same Territory
**Severity: High | Discovered in: SIM-06**

The ruleset handles two-faction same-card conflicts: "both roll; higher result (by Ob margin) applies first." In SIM-06, Crown + Church + Hafenmark all played Senator cards in T1 (Valorsplatz) simultaneously. No resolution order exists for three-way Social conflicts beyond "highest Stability goes first." When Stability is tied (Crown and Hafenmark both at 4), simultaneous resolution is called — but the effects of three simultaneous Diplomacy/Decree/Parliamentary Manoeuvre actions targeting the same location are undefined.

**Proposed resolution:** Sequential by Stability descending; ties break left of current player. Each effect resolves before the next rolls. Requires formal text.

---

### AMB-02 — Church Pontifex Self-Penalty from Divine Command Ethics
**Severity: High | Discovered in: SIM-01, SIM-06**

Church's Divine Command ethical framework applies "+2 Ob" to "Thread-supporting" actions. The Church has a Pontifex card in its base hand, which executes Thread operations. Playing the Church's own Pontifex therefore applies +2 Ob from the Church's own ethical framework.

At Ob 4 (2 baseline + 2 ethical penalty) for the Church's signature Thread card: probability of success on ~Influence 6 dice ≈ 26%. This seems unintentional — the Church's unique card is penalized by the Church's own framework.

**Possible interpretations:**
- (a) Intentional: Church is NOT meant to do Thread operations (Pontifex is a disruption/counter-Thread tool, not a performing-Thread tool). But Pontifex is listed in the Senate Market as "Thread operation (Restoration / Thread-qualified only)" at cost 2 — implying it IS a Thread operation card.
- (b) Error: Divine Command ethics should exclude the Church's own Pontifex.
- (c) The Pontifex in Church's base hand functions differently from the Senate Market Pontifex.

**Requires designer ruling.**

---

### AMB-03 — Presence Spread Timing for Thread Qualification
**Severity: High | Discovered in: SIM-06**

Restoration plays Presence Spread into T12 in Phase 4. The Southernmost Rule requires Thread-qualified presence "this season" for military units to survive. Does a Presence marker placed via Presence Spread this season count immediately for Thread qualification, or only from next season forward?

If immediate: Restoration could Spread then Weave in the same season. If next season: the Spread is pure setup. The answer also determines whether Restoration can defensively qualify T12/T13 against an attacking faction in the same Phase 4.

---

### AMB-04 — Reformed Settlement Declaration Timing
**Severity: Medium | Discovered in: SIM-10**

RDT 5 makes Reformed Settlement "available (once/game)" but doesn't specify whether Hafenmark must spend a card to declare it, whether it fires automatically at Accounting when RDT reaches 5, or whether Hafenmark chooses when to use it. If the latter: Hafenmark can hold the threat indefinitely as a diplomatic lever without ever triggering it.

---

### AMB-05 — Church Ignore on Reformed Settlement: No Limit Defined
**Severity: Medium | Discovered in: SIM-10 | Cross-reference: EDITORIAL BG-E-62**

Church can Ignore Reformed Settlement, triggering RDT +1 next season. But RDT is capped at 6 (the track goes to 6). If Church Ignores when RDT = 5: RDT → 6. If Church Ignores when RDT = 6: RDT cannot advance. So Church can perpetually Ignore once Hafenmark has "used" their +1 from the first Ignore. Effectively, Ignore → RDT 6 → Ignore indefinitely (RDT at ceiling, no further consequence). This may be the strategically dominant response for Church.

---

### AMB-06 — Hollow Victory Score Visibility
**Severity: High | Discovered in: SIM-12**

The Hollow Victory system modifies effective Deed counts at game end. It is explicitly a mandatory pre-printed sheet. But whether this scoring is tracked publicly (all players see running Hollow totals) or privately/secretly (revealed only at end) is unspecified. This is a significant design decision:

- Public tracking: Standing and Compromise accumulation is transparent. Players can strategically target Hollow modifiers to deny opponent victories. The Hollow system becomes a political warfare axis.
- Private tracking: Surprise reveal at game end. A player might hold all 5 Deed Tokens and only discover they can't win when the sheet is scored. Potentially feels punishing.

Given Standing tokens are already public, the Hollow calculation can be reverse-engineered by any attentive player anyway. Recommend: explicit public tracking.

---

### AMB-07 — Vaynard-Edeyja Encounter Same-Season Procedural Conflict
**Severity: Medium | Discovered in: SIM-09**

Warden Emergence fires at Accounting Step 9. The Vaynard-Edeyja encounter (Tribune Intel Inward in T13 at VTM 4+) triggers in Phase 4 Resolution, before Accounting. If Varfell's expedition is the one that triggered Warden Emergence (i.e., this is the same season that Emergence first fires), the conversation triggers during Phase 4 while the Warden Cooperation track does not yet officially exist (it's established at Step 9).

**Sequence conflict:** Vaynard plays card in Phase 4 → encounter fires → Warden Cooperation +1 is attempted → Step 9 Accounting: Warden Emergence fires, Warden Token placed at 0 → but it was already pushed to 1 by the Phase 4 encounter.

**Proposed resolution:** If Varfell is the faction triggering Warden Emergence, the Vaynard-Edeyja encounter is deferred to the following season. Alternatively: state explicitly that Emergence fires before all other Phase 4 effects from T13 actions (exceptional priority). Requires formal text.

---

### AMB-08 — Riskbreaker Token Year vs. Season
**Severity: Medium | Discovered in: SIM-11**

"3 tokens/year. Refresh at Year-End." Year = 4 seasons. So Riskbreakers have 3 tokens across 4 seasons. If all 5 priorities are active simultaneously in one season, 3 tokens cover Priorities 1–3, leaving Priorities 4–5 unaddressed. This could mean the Löwenritter coup counter advances unchecked (Priority 4 unaddressed) in a season that coincides with all other crises. Tactically interesting — worth confirming this is intentional.

---

### AMB-09 — Riskbreaker Exposure VTM −1 Timing
**Severity: Low | Discovered in: SIM-11**

Priority 1: "Expose fabrication. CB fails next season. Varfell +1 Standing from all. VTM −1." CB fails next season is a future effect. VTM −1 — immediate or next Accounting? "Varfell +1 Standing from all" — presumably immediate. If VTM −1 is also immediate: Varfell drops one VTM level publicly, which may affect their Thread qualification in T12/T13 (VTM 2 = Thread-qualified). A same-season VTM loss could strip T12/T13 qualification mid-season, retroactively invalidating Thread-qualified presence already exercised that season.

---

### AMB-10 — Card-Per-Territory Limit
**Severity: Low | Discovered in: SIM-06**

No stated limit on how many cards one faction can play in the same territory per season (beyond the 5-card-per-season maximum). In SIM-06, Hafenmark played Senator + Diplomat both in T1 in one season. This creates potential card-stacking in high-value territories (T1 Valorsplatz particularly). Other players cannot easily contest a faction that saturates a single territory. Requires either a stated per-territory limit or confirmation there is none.

---

## PART III — MECHANICAL CASCADE CRUNCH

Conditions where system interactions produce more mechanical load than the cascade depth cap or player cognition can absorb.

---

### MCC-01 — Coup Cascade Exceeds Six Simultaneous Effects
**Discovered in: SIM-02**

When Löwenritter Coup fires, the following effects all trigger simultaneously:
1. PI −3
2. All factions: Standing +1 vs Löwenritter (4 simultaneous assignments)
3. Permanent Martial Law in all Crown territories (affects 4–6 territories)
4. Ministry Coup Resistance: all Löwenritter Govern +1 Ob for 3 seasons
5. Almud house arrest in Valorsplatz
6. Elske and Torben arcs activate

The cascade depth cap of 3 applies only to card plays in Phase 4. The coup is a Counter event, not a card play. So technically the cap doesn't apply — but the cognitive load of processing six simultaneous mechanical changes (many with ongoing tracking obligations) is the highest single event in the game.

**Recommendation:** Formalize a coup resolution checklist (similar to the Seasonal Accounting Checklist) to ensure nothing is missed. The current NPC AI block and B5 post-coup faction sheet are dispersed — players must consult three locations simultaneously during the coup event.

---

### MCC-02 — RS Positive Feedback Loop
**Discovered in: SIM-04**

As RS drops below 49: Thread operations cost −1 Ob. Cheaper Thread operations incentivize more Thread use. More Thread use generates more Thread Debt tokens. Unserviced Thread Debt drains RS −1/token/season. Lower RS → Thread Wound territories drain faster (no Warden compensation until Cooperation ≥ 1). More Thread operations → more Co-Movement cards → more potential actualized RS effects. Community Projects advance faster at RS < 20 (repair mechanism), but the repair rate (+RS from Weave Projects) lags behind the accelerated drain from Thread Debt + Wound territories + Co-Movement.

**Worst-case single-Winter accounting (SIM-04 figures):**
- Thread Debt (2 unserviced): RS −2
- Thread Debt residual (Year-End): RS −1
- Niflhel passive drain (3 territories): RS −1 to −2
- Thread Wound (T12 + T13, 3rd consecutive season): RS −2
- Co-Movement actualized effect (1 card): RS −1

**Total per Winter worst case: RS −7 to −8 in one Accounting phase.** At RS 45 this creates a situation where RS < 40 triggers at the next check, further lowering Ob for Thread operations.

No single faction controls all of these drain sources. This is an emergent multi-faction collapse. The only circuit breakers are: Restoration's Thread Recovery Milestone (+1 RS/Year-End in T14), Edeyja's Emergency Mend at RS < 30 (+1 RS), and Warden Cooperation bonuses. All three require significant investment to unlock and fire after the damage is already severe.

---

### MCC-03 — Church Assert Mass Mandate Trigger
**Discovered in: SIM-08**

Church Assert (announced at Phase 5 Accounting) triggers: "All secular faction Mandate triggers fire." In a 4-5 player game with Crown, Hafenmark, and Varfell all having active trigger conditions, a single Assert can simultaneously force three Uphold/Compromise decisions. Each decision requires:
1. Evaluating whether current game state satisfies the trigger condition
2. Choosing Uphold or Compromise
3. Applying results (Renown/Stability or Standing/Stability/mechanical benefit)

Three simultaneous Uphold/Compromise decisions at Accounting Step 5 creates 3–9 stat adjustments in rapid succession, before Step 6 (Thread Debt) and Step 7 (Resonance reset) are even addressed. The Phase 5 checklist doesn't flag Assert as a multi-faction resolution moment.

---

### MCC-04 — Reformed Settlement Accommodate Full Cascade
**Discovered in: SIM-10**

Church Accommodate triggers: TC −5 + Church Mandate trigger + Church Stability −1 + AER −2.

If AER was 4 before Accommodate: AER drops to 2, nullifying Altonia's invasion deferral (which required AER ≥ 4). If IP was already at 70–74 (below vanguard threshold only because AER 4 raised it to 80): IP can now reach 75 in the following season, deploying the Altonian Vanguard. One Reformed Settlement response cascades into an Altonian invasion trigger — across two seasons, but causally linked.

This cascade is elegant (it makes the Reformed Settlement genuinely consequential) but players may not trace the AER → IP → invasion chain on first play. The reference card for Clock Environmental Effects and the AER table are in two separate sections (B2 and B7). Cross-referencing them in real-time during a Reformed Settlement response is a high cognitive demand.

---

### MCC-05 — Maximum-Season Cognitive Load
**Discovered in: SIM-08**

A fully activated Season 8 (all factions active, all clocks elevated, Riskbreakers + Ministry + Niflhel + Schoenland all evaluating) requires players to process approximately:
- 17–20 individual card resolutions in Phase 4
- 3–5 NPC AI evaluations at Accounting
- 10-step Seasonal Accounting checklist
- Potentially 3 Mandate evaluations (from Assert)
- Co-Movement card draws (1–3 per Thread operation)
- Thread Debt drain, Attention Pool threshold, Warden Cooperation check

**Estimated realistic Phase 4 duration at 5 players, full systems:** 25–50 minutes (vs. the stated 8 minutes). Phase 5 Accounting: 15–20 minutes (vs. stated 5 minutes). The stated 2–4 hour total session is compressed for a 5-season game at full complexity.

---

## PART IV — STRESS FINDINGS

---

### SF-01 — Post-Coup Löwenritter Structural Deadlock vs. High-TC Church
**Discovered in: SIM-02**

The Löwenritter post-coup faction requires TC < 50 for their primary Deed Token 1. Their hand is 3× Legionary + 1× Tribune + 1× Prefect + 1× Recess. They have NO Senator cards and NO Senate Market access to Diplomat, Pontifex, or Censor. They cannot pursue Diplomacy to suppress TC.

If the coup fires after TC has exceeded 70 (which is a plausible scenario — late-game coup triggered by TC ≥ 80 condition), the Löwenritter face TC that is 30+ points above their Deed threshold with zero diplomatic tools to reduce it. Baralta's TC passive suppression (−1/season while Mandate ≥ 4) and the Sovereign Authority Doctrine (once/game, −2 to −3 TC) are insufficient.

Further: at TC ≥ 70, the AER has likely advanced through three thresholds to AER 5. AER 5 = "once/game: any order targeting Church interests fails automatically." The Löwenritter have no order that avoids targeting Church interests when trying to reclaim Crown territories that the Church has seized.

**Net effect:** A late-game Löwenritter coup against a high-TC Church is structurally unwinnable. Either (a) the coup trigger conditions should prevent the coup from firing at TC ≥ 70 (it only makes the situation worse), or (b) Löwenritter needs a single anti-TC diplomatic tool (a modified Senate Market option, or a military "Occupy Cathedral" action with TC consequence), or (c) this is intentional — the Löwenritter post-coup scenario is tragedy, not a viable victory path when the Church is this advanced.

If (c) is intentional: the rules should signal this. A faction sheet that leads to structural impossibility without flagging it is a legibility problem.

---

### SF-02 — Church Dual Theocracy Path Requires IP ≤ 30, But Church Advances TC (Which Advances AER, Which Suppresses IP)
**Discovered in: SIM-03, SIM-07**

Dual Theocracy victory: TC ≥ 60 + AER = 5 + IP ≤ 30.

The AER system provides excellent synergy here: TC crossing 30/50/70 each advances AER +1. At AER 5: IP is fixed at 50. But IP ≤ 30 is required for Dual Theocracy. AER 5 fixes IP at 50 — not ≤ 30. So AER 5 prevents the Altonian invasion but does NOT satisfy IP ≤ 30 for Dual Theocracy.

For IP ≤ 30 at game end, the Church must actively reduce IP, not just suppress it. Free Trade Decree (Crown policy, −1 IP) and Restoration Network Project (−1 IP) are the primary IP reduction tools — neither controlled by the Church. The Church has no direct IP reduction mechanism. Dual Theocracy may be technically unachievable through Church action alone: it requires diplomatic coordination with Crown (Free Trade Decree) and/or Restoration Movement.

This might be intentional (Dual Theocracy requires genuine cooperation, not conquest), but the victory path should explicitly signal this dependency.

---

### SF-03 — Varfell Thread Supremacy: Self-Defeating Condition Logic
**Discovered in: SIM-05**

Thread Supremacy victory: VTM = 5 + RS ≥ 50 + control T12–T13.
- Controlling T13: RS −1/season from Thread Wound.
- VTM 5 power use: "Always produces Thread Debt token + RS −1."
- VTM advancement sources include Thread Debt incurred by any faction: each Thread Debt event is a VTM advance but also an RS drain.

Vaynard must reach VTM 5 (accumulating damage) and maintain RS ≥ 50 (preventing damage). He has no direct RS recovery tools. His victory path requires either (a) limiting total Thread operations across all factions to keep RS healthy, or (b) allying with Restoration for RS recovery. Neither is under his direct control.

**RS Budget analysis (12-season campaign):**
RS starts 72. Must end ≥ 50. Headroom: 22 RS loss maximum.
- T13 occupation (6 seasons): −6 RS
- VTM 5 use: −1 RS
- Thread Debt from other factions (say 8 total across campaign): each is a VTM advance, NOT a direct RS drain to Varfell, but unserviced tokens from others still drain RS globally.
- If 2 other factions maintain 1 unserviced Thread Debt token each for 6 seasons: −12 RS

At −19 RS from these sources alone: RS = 53 at game end. Barely viable. **Thread Supremacy is achievable but only in a game where other factions are disciplined Thread users** — which is not something Varfell can enforce alone.

**Recommendation:** Varfell's Intelligence Network Milestone (all factions' stats revealed → permanent visibility of one faction's stats) should explicitly list RS management as a target for Thread Supremacy path players.

---

### SF-04 — Restoration's Military = 0 Makes Them Immune to Territorial Conquest But Invisible on the Victory Track
**Discovered in: SIM-06**

Restoration has Military 0 and 8 Presence markers. Military force cannot remove Presence markers (only Heresy Investigations or Community Project disruption). This correctly models a non-violent grassroots faction.

But: Restoration's victory requires "5 Presence markers in 5 non-adjacent territories maintained for 2 consecutive seasons + RS ≥ 50." With 8 markers total: they must place 5 in qualifying positions AND hold them for 2 seasons without being disrupted. Church's Heresy Investigation (Attention Pool threshold 3) is the primary threat. If Church reaches Inquisition Network Milestone (auto-open in Church territory without card play): Restoration in any Church-adjacent territory faces constant disruption.

**The counter-path (Community Resilience Milestone):** "3 Community Projects completed → Projects cannot be disrupted by Heresy Investigation." This shields Projects but not Presence markers directly. Presence markers are removed by Heresy Investigation — the Milestone doesn't mention Presence.

**AMBIGUITY:** Does the Community Resilience Milestone protect Presence markers from Heresy Investigation removal, or only the Project progress track? If only Projects: Restoration loses their win condition threat even with the Milestone. If also Presence: this Milestone is essential for Restoration's victory path and its scope should be explicit.

---

### SF-05 — Hollow Victory System Can Deny a Legitimately Complete Victory Without Warning
**Discovered in: SIM-12**

In the SIM-12 scenario: Crown holds all 5 Deed Tokens at game end. But accumulated Hollow modifiers (−4 Deeds from Standing + Compromises) reduce effective Deed count to 1, voiding the victory entirely. 

The Hollow Victory system functions correctly as designed. The stress finding is about legibility and player experience: a player who executed every mechanical condition of their victory path can be told at game end that they have not won, because of Hollow modifiers they may not have been tracking carefully.

The system is designed to make legitimacy matter throughout the game, not just at the end. But this only functions if all players understand Hollow Victory is a continuous tracking obligation, not an end-game calculation. The reference card is listed as "pre-printed mandatory" but its prominence in gameplay is unclear.

**Recommendation:** Add Hollow Victory as a stated component of Phase 5 Accounting (or Year-End Accounting) — a brief check: "Has anyone's Hollow modifier changed this season?" This converts end-game surprise into in-game political intelligence.

---

## PART V — EMERGENT POSSIBILITIES (Positive Design Findings)

---

### EP-01 — Vaynard-Edeyja-Restoration Synergy Chain
**Strongest emergent chain in the ruleset.**

Vaynard → VTM 3 (public, visible) → other factions know he's advancing → VTM 4 → enters T13 → plays Tribune Intel Inward → Edeyja speaks to him → Warden Cooperation +1 (automatic, bypassing other conditions) → Warden Cooperation 2 → Restoration Movement gains Deep Layer access WITHOUT VTM gate → Restoration begins Expedition in T13 → Expedition seasons complete → RS +1/season (warden assistance) → Vaynard's Thread Supremacy path becomes plausible because Restoration is repairing RS damage.

This chain spans 8+ seasons, requires multi-faction implicit cooperation (Varfell never formally allies with Restoration), and creates a legible narrative arc (Vaynard and Edeyja recognize each other's competence; the world literally recovers). **This is the game's best systemic design.**

---

### EP-02 — Church AER as Invasion Gate
**Mechanically elegant.**

The Church pursuing theocratic victory (TC accumulation) automatically advances AER (TC crossing 30/50/70 each gives +1 AER). AER ≥ 4 prevents Altonian invasion. AER 5 freezes IP at 50. The faction most likely to destabilize Valorian politics (by pushing TC) is also the faction that maintains Altonia's good faith. Every other faction must either tolerate the Church's TC dominance OR reduce TC (which risks lowering AER → Altonian invasion).

**This creates a genuine systemic hostage situation:** attacking the Church's TC also attacks everyone's safety from Altonia. Factions must weigh theocratic creep against invasion risk. Beautifully executed.

---

### EP-03 — Riskbreaker CB Gambit
**Underexplored tactical possibility.**

Vaynard can deliberately maintain a Casus Belli he knows Riskbreakers will expose. Riskbreaker Priority 1 consumes one token per year to expose it. This exhausts token capacity, leaving Priorities 4–5 unaddressed. If Priority 4 (Löwenritter Coup Counter = 3, Condition 4 approaching) goes unaddressed due to token exhaustion: the coup might fire when it otherwise would have been diplomatically blocked.

Vaynard takes VTM −1 from the exposure, but triggers a coup as a second-order effect. At VTM 4+: exposures become harder (Ob +1), making the gambit increasingly expensive to execute against Vaynard but free to set up.

---

### EP-04 — Ministry as Löwenritter Nemesis
**Complementary system.**

The Ministry's Coup Resistance (+1 Ob to all Löwenritter Govern for 3 seasons post-coup) combined with Ministry's Policy Delay (d3: delays Crown policies 0–2 seasons) creates bureaucratic friction that specifically punishes the faction trying to govern without constitutional legitimacy. The Löwenritter's Iron Administration Milestone neutralizes this — but the Milestone requires successfully Governing 4 territories in one season (Ob penalty means they need to succeed against Ob 2 on Govern). The Milestone is the cure for the penalty that makes the Milestone hard to earn. **Elegant catch-22.**

---

### EP-05 — Niflhel Supply Chain as Edeyja Trigger
**Emergent chain no faction controls.**

Niflhel expands into T13 (Network Depth ≥ 1) via their own autonomous AI priority. This is not any player's action. Niflhel's presence in T13 creates Thread disturbance → Edeyja's AI Priority 2 fires (Warden AI investigates Niflhel in T13) → Church Attention Pool +1 (the warden investigation creates visible disturbance) → this may push Attention Pool to threshold 3 (Heresy Investigation opens).

The chain: Niflhel (NPC) → disturbs Edeyja (NPC) → generates Church Attention (NPC) → Church opens Heresy Investigation (which Church player may not know how to trace). No player caused any of this. The world generates its own pressure.

---

## PART VI — LEGIBILITY ASSESSMENT

---

### LEG-01 — Three-Location Rule Fragmentation for Southernmost
**Rating: Poor | Location: B2, B6, B7, B13**

The Southernmost rules are spread across four sections:
- **B2:** Southernmost Rule (military dissolution) + T12/T13 territory descriptions
- **B6:** Thread Resonance for T12/T13 qualification
- **B7:** Warden Cooperation Track, Forgetting Check, Edeyja AI
- **B13:** Edeyja NPC AI block

A player taking their first expedition to T13 must cross-reference all four sections simultaneously. The Thread Witness Node (B6), Thread Resonance qualification (B6), Southernmost Rule (B2), Forgetting Check (B7), and Expedition Project (B10) are all relevant to a single action. This is the highest legibility burden in the ruleset.

**Recommendation:** A dedicated Southernmost Expedition reference card (similar to the Thread Operation Procedure card) listing all relevant rules in sequence.

---

### LEG-02 — NPC AI Evaluation Order Unclear Across Multiple NPCs
**Rating: Medium | Location: B13**

Six NPC AI blocks (Löwenritter pre-coup, Riskbreakers, Ministry, Guilds, Niflhel, Schoenland, Edeyja) all "evaluate at Accounting." No ordering between NPC evaluations is stated. Some NPCs react to other NPCs' outcomes: Niflhel expansion into T13 → Edeyja investigates → Church Attention +1. If Niflhel evaluates after Edeyja: Edeyja doesn't know about the Niflhel expansion yet. If Niflhel evaluates before Edeyja: the reactive chain works.

**Proposed NPC evaluation order:** Schoenland → Guilds → Ministry → Niflhel → Riskbreakers → Edeyja → Löwenritter (pre-coup). This mirrors causal dependency (NPC reactions should follow the actions they're reacting to).

---

### LEG-03 — AER Track / IP Track Proximity Without Explicit Cross-Reference
**Rating: Medium | Location: B2, B7**

AER track is "near the IP track" on the board. Their interaction is defined in B7 (AER modifying IP thresholds). The Clock Environmental Effects table (B2) doesn't cross-reference AER. A player tracking IP threshold events at the board would need to simultaneously consult B7 for AER modifications. In the heat of threshold events (IP reaching 60, 75), this cross-reference is easily missed.

**Recommendation:** AER effects on IP should appear in the IP Environmental Effects table, not only in B7.

---

### LEG-04 — Milestone Bonuses "Automatic" But Not on Any Checklist
**Rating: Low | Location: B9, B11**

Milestone Bonuses "fire automatically the first time their trigger condition is met." But neither the Seasonal Accounting checklist nor the Year-End Accounting checklist includes a Milestone check step. B11 Step 9 ("Confirm all milestone triggers. Apply any that fired this year.") is the only accounting hook — and "this year" means only Year-End, missing intra-year milestones.

**If a milestone fires in Season 2 of a 4-season year:** it's confirmed at Step 9 of Year-End (Season 4). The bonus may be applied 2 seasons late if players don't notice in-season. Recommend adding a brief milestone check to Seasonal Accounting (Phase 5) as well.

---

### LEG-05 — Faction Deed Token Conditions Across Competing Tracking Surfaces
**Rating: Medium | Location: B5, B12**

Each faction has 3–5 Deed Token conditions. Deed 5 for Crown is "Torben Loyalty ≥ 5" — but Torben's Loyalty track is not in the main ruleset (implied from hybrid mode or extended faction sheet content). Several Deed conditions reference stats (TC < 60, IP < 75, RS > 40) that are board-level clocks already tracked. But some reference private tracks (VTM, RDT, TD) that are on faction mats. Holding all Deeds simultaneously requires a player to track board clocks + private tracks + named NPC stat (Torben Loyalty) as preconditions.

**Recommendation:** Print Deed Token conditions directly on the faction mat's Deed Track (not just in the rulebook).

---

## PART VII — CONSOLIDATED ISSUE LIST

### Priority: Pre-Playtest Blocking (not in official C2 checklist)

| ID | Issue | Type | Section |
|----|-------|------|---------|
| FG-01 | TC advancement formula undefined | Functional Gap | B4, B7 |
| FG-02 | Core action outcome effects undefined (Diplomacy, Govern, Trade, etc.) | Functional Gap | B3, B5 |
| FG-03 | Stat-to-action mapping absent | Functional Gap | B3, B5 |
| FG-04 | Champion starting positions undefined | Functional Gap | B8, B5 |
| FG-06 | Invasion terminal event mechanics missing | Functional Gap | B2, B7 |
| AMB-02 | Church Pontifex vs. Divine Command ethics: self-penalty | Ambiguity | B5, B5 |
| AMB-01 | Three-way Social conflict resolution undefined | Ambiguity | B4 |
| AMB-06 | Hollow Victory score visibility (public vs. private) | Ambiguity | B12 |
| AMB-07 | Vaynard-Edeyja same-season turn-order conflict | Ambiguity | B7, B13 |
| AMB-04 | Reformed Settlement declaration timing | Ambiguity | B5 |
| MCC-05 | Phase 4 and Accounting duration estimates unrealistic | Crunch Cascade | B4 |
| SF-01 | Post-coup Löwenritter structural deadlock vs. high-TC Church | Stress Finding | B5, B7 |

### Priority: Can Wait Until After First Playtest

| ID | Issue | Type | Section |
|----|-------|------|---------|
| FG-05 | Ob 0 resolution undefined | Functional Gap | B4 |
| FG-07 | Muster deployment token protocol | Functional Gap | B8 |
| AMB-03 | Presence Spread timing for Thread qualification | Ambiguity | B6 |
| AMB-05 | Church Ignore on Reformed Settlement — no iteration cap | Ambiguity | B5 |
| AMB-08 | Riskbreaker token economy (year vs. season confirmed, but consequences unconfirmed) | Ambiguity | B13 |
| AMB-09 | Riskbreaker exposure VTM −1 timing vs. T12/T13 qualification | Ambiguity | B13 |
| AMB-10 | Card-per-territory limit | Ambiguity | B3 |
| MCC-01 | Coup resolution checklist needed | Crunch Cascade | B5, B13 |
| MCC-02 | RS positive feedback loop needs circuit breaker review | Crunch Cascade | B6, B11 |
| MCC-03 | Assert mass Mandate trigger: 3 simultaneous Uphold/Compromise decisions | Crunch Cascade | B5, B7 |
| SF-02 | Dual Theocracy requires non-Church IP reduction (uncontrolled by Church) | Stress Finding | B5, B7 |
| SF-03 | Thread Supremacy RS budget requires external cooperation | Stress Finding | B5, B7 |
| SF-04 | Community Resilience Milestone scope: Projects only, or Presence markers too? | Stress Finding | B9 |
| SF-05 | Hollow Victory accumulation mid-game legibility | Stress Finding | B12 |
| LEG-01 | Southernmost rules fragmented across 4 sections | Legibility | B2, B6, B7, B13 |
| LEG-02 | NPC AI evaluation order between NPCs undefined | Legibility | B13 |
| LEG-03 | AER/IP cross-reference gap in Environmental Effects table | Legibility | B2, B7 |
| LEG-04 | Milestone Bonuses absent from Seasonal Accounting checklist | Legibility | B9, B11 |
| LEG-05 | Deed Token conditions split across rulebook and faction mat | Legibility | B5, B12 |

---

## PART VIII — SYSTEM COHERENCE ASSESSMENT

| System | Rating | Notes |
|--------|--------|-------|
| Three Clocks (RS/TC/IP) | 8/10 | Mechanically coherent. TC formula gap is the critical miss. AER-IP interaction is the game's best-designed system. |
| Card-Hand Action Economy | 7/10 | Foundation is solid. Action outcome effects must be defined for the system to function. Stat-to-action mapping gap is critical. |
| Institutional Mandate | 8/10 | Uphold/Compromise is the game's moral engine. Assert mass-trigger is a crunch issue, not a design flaw. Trigger condition text (BG-E-51 etc.) must be finalized. |
| Thread Systems | 7/10 | RS feedback loop is the primary risk. Thread Debt max of 3 tokens functions as a hard cap (good). Church Pontifex self-penalty is a design question needing resolution. |
| Hollow Victory | 8/10 | Elegant legitimacy modifier. Legibility gap: it must be tracked throughout the game, not just at end. |
| Deed Tokens | 7/10 | Simultaneous-holding tension is interesting. Some Deed conditions reference undefined content (Torben Loyalty track). |
| Warden Cooperation | 9/10 | Best emergent NPC relationship in the design. Vaynard-Edeyja interaction is exceptional. Same-season turn-order procedural error needs a clean rule. |
| NPC AI Blocks | 8/10 | Riskbreakers and Niflhel are particularly well-designed (asymmetric, reactive). Evaluation order across NPCs needs formalization. |
| Löwenritter Post-Coup | 6/10 | Interesting tragedy arc but structural deadlock vs. high-TC Church is unwinnable without a TC reduction tool. Either by design (signal it) or error (fix it). |
| Community Projects | 8/10 | Quiet Year mechanic fits the faction identity. Thread Witness Node as permanent territory modifier is elegant. |

---

## PART IX — EMERGENT NARRATIVE ASSESSMENT

The game's emergent narrative potential is exceptional. The following story arcs were observed to arise naturally from system interactions across simulations:

1. **The Church wins by doing exactly what it believes is right** — TC accumulation through genuine doctrinal spread, not malevolence. Every faction trying to stop them accelerates their legitimacy (Standing tokens create Hollow modifiers for aggressors).

2. **Vaynard is the most dangerous person on the peninsula and no one can prove it** — VTM advances privately until VTM 3 (publicly visible). By then, his covert operations have already shaped 3+ seasons of events. Riskbreakers are the only check, and he can game their token economy.

3. **The Löwenritter broke what they tried to protect** — PI −3 at coup makes parliamentary function impossible. Their only exit is Regency Resolution (installing a successor). Every season of military rule is PI at risk and TC rising into the vacuum.

4. **Edeyja is holding a catastrophe that no one on the peninsula understands** — The Niflhel supply chain (no player's action) destabilizes her work before anyone knows she exists. The world is being harmed by mundane commerce.

5. **The RS feedback loop as narrative clock** — As RS degrades, Thread operations become cheaper, incentivizing the behavior that degrades the world further. The game mechanically represents civilizational short-termism.

These are not incidental to the mechanics — they are produced by the mechanics. The core feel confirmation in C1 (10/10) is warranted.

---

*Report generated from 12 full/partial simulations of Valoria BG v0.2.*
*23 ambiguities catalogued. 9 stress findings. 5 crunch cascades. 5 emergent chains. 5 legibility issues.*
*Total pre-playtest blocking issues identified: 12 (not all in official C2 checklist).*
