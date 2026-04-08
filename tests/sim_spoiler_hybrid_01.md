# SIM-SPOILER-HY-01 — Hybrid Mode Spoiler Faction Simulation
## Date: 2026-04-07 | Mode: C (Full Scenario) + K2 (State Transfer) + G-HY + L (Cognitive Load)
## Scenario: Varfell acting as spoiler against Church, while Crown pursues Peninsula Sovereignty

---

## FETCH LOG
canonical_sources.yaml: ✓ fetched (156 lines)
references/params_board_game.md: ✓ fetched (1068 lines)
references/params_factions.md: ✓ fetched (480 lines)
designs/board_game/victory_architecture_v1.md: ✓ fetched (368 lines)
skills/valoria-orchestrator/references/state_transfer_spec.md: ✓ fetched (230 lines)

---

## Setup

**3-player board game layer:** Crown (pursuing Solmundan Orthodoxy victory — wait, Crown pursues Peninsula Sovereignty), Church of Solmund (pursuing Solmundan Orthodoxy), Varfell (spoiler — targeting Church, trying to prevent Church from reaching TC 75 and entering seizure phase).

**Correction:** For a clean spoiler test, Crown is pursuing their win path, Church is pursuing theirs, Varfell is the spoiler targeting Church's victory.

**Why Varfell spoiling Church:**
Church primary victory requires TC ≥ 75 → seizure phase → TCV ≥ 10 + CV ≥ 3 everywhere. Varfell's tools that affect Church's victory path:
- Counter-Narrative (PP-441-COR): AP +2, occasional TC −0.5 on Overwhelming
- VTM development: VTM 3+ = Expedition access → Warden Cooperation → RS maintenance (Church path is fragile if RS collapses)
- Tribune Intel: expose Church territory stats; reveal Inquisitor positions
- Thread Supremacy path (Path C): RS ≥ 50 condition means Varfell cares about RS stability — which directly undermines Church's trajectory if RS falls

**Spoiler goal:** Keep TC below 60 long enough for Crown or Hafenmark to win first. TC starts 28. With passive +1/season and no Assert, TC reaches 75 in 47 seasons (never in one game arc). Church NEEDS Assert to push TC up meaningfully. Varfell's spoiler job: prevent TC advancing rapidly enough by disrupting Church's ability to accumulate without cost.

---

## State (starting, Hybrid mode arc — Season 4 of first arc)

By S4, typical game state:
TC: 34 (passive baseline, Church hasn't Asserted yet). RS: 70. IP: 22. PI: 6.

| Faction | Mandate | TCV | Notes |
|---------|---------|-----|-------|
| Crown | 5 | 14 | Expanding. 2 seasons from TCV 16. |
| Church | 5 | 3 | Holding T9 Himmelenger. Planning TC push. |
| Varfell | 4 | 6 | VTM 2. Has Tribune presence in T9 adjacent territories. |
| Hafenmark | 4 | 9 | Stable. |

---

## Board Game Phase — S5

**Church plan (non-spoiler):** Assert (Phase 4 Priority 6, Special/Unique Power). TC +2 (replaces passive +1). TC 34 → 36.

**Varfell spoiler plan:**
Primary tool: Counter-Narrative (Tribune Outward) in T9 (Himmelenger, Church capital, CV 5). 
Ob = Church Mandate ÷ 2 round up = 3. Consequentialism −1 → Ob 2.
Roll: Intel 4D vs Ob 2. (Using probability table: P(OW) 27%, P(Succ) 29%, P(Partial) 31%, P(Fail) 13%.)
- **Result: Success.** AP +2 in T9. (No TC effect — TC effect only on Overwhelming.)

Church Attention Pool = 2. First Inquisitor threshold AP ≥ 3 (ED-322). Not yet reached — Church tracks.

Secondary tool: Varfell also plays **Spy** (Tribune Outward) on Church. Wait — Counter-Narrative AND Spy both need Tribune Outward card. Varfell's card hand: 4 shared + 2 faction cards. Tribune Outward is a shared card. One use per season (1 card = 1 action). Must choose Counter-Narrative OR Spy, not both.

Varfell chooses Counter-Narrative (AP generation + TC chance). No Spy this season.

**Church's response to Counter-Narrative success:**
Church knows Varfell played Counter-Narrative in T9 (it's a declared outward action — Target territory is public). Church can:
1. Play Cardinal Focus: Justice next season (AP threshold −1 → first Inquisitor at AP ≥ 2). With AP already at 2, Inquisitor deploys at Focus declaration next season.
2. Play Active Inquisition in T9 next season to raise AP and justify Inquisitor deployment.
3. Play nothing — accept AP accumulation.

**Accounting Step 5:** Church AP = 2. Below threshold (first at 3). TC passive +1 → TC 35. Assert's TC +2 fires at Priority 6 before Accounting → TC 34 → 36 before passive → 37.

Actually: Assert is Phase 4 Priority 6. Passive TC advance fires at Accounting Step 4 (clock advances). Assert's effect at Priority 6 during Phase 4 = TC +2 (replaces passive). But passive fires at Accounting — two different timings.

**Ruling clarification (TC timing):** Assert effect fires during Phase 4 Priority 6 resolution. The effect is: "TC +2 total (replaces passive; not additive)" — per params_factions.md. This means Assert replaces the passive +1 that would fire at Accounting. So Assert → TC +2 at Phase 4 (immediate effect). Accounting Step 4: no additional passive (already replaced by Assert). Net: TC +2 this season total.

TC 34 + 2 (Assert) = **TC 36**.

**S5 end state:** TC 36. Church AP 2 (below threshold). Varfell Counter-Narrative created AP but didn't trigger Inquisitor yet.

---

## HYBRID ZOOM IN — S6 Trigger

**Crown's S6 action:** Crown attempts to take T14 (Ehrenfeld, currently Crown-held per setup — wait, Ehrenfeld IS Crown-held at start). Crown wants to expand. They march into T9 (Himmelenger, Church). Battle triggers.

**Zoom In trigger:** Crown player has a named Player Character — Marshal Edren — commanding the assault on Himmelenger. Marshal Edren is present → Zoom In eligible.

**Zoom In declaration:** Crown triggers Zoom In. BG phase suspends. Zoom In resolves as TTRPG personal scene.

### State Transfer (BG → TTRPG)

Per state_transfer_spec.md §1:

| BG Variable | TTRPG Equivalent | Transformed value |
|---|---|---|
| T9 CV (5) | Scene context: strong Piety atmosphere, NPC faith high, crowds hostile to Crown intrusion | Read-only |
| Crown Battle unit Strength | Unit Str in TTRPG mass combat | Crown Military 3 → TTRPG Str = ⌈3 ÷ 1.5⌉ = 2 |
| Church Fort 2 (T9) | Defender +2D | Fort level preserved as bonus pool |
| Church Military 4D + Fort 2D = 6D pool | BG Cohesion 6 → TTRPG Cohesion 6 direct | Cohesion 6 |
| BG turn phase suspended | Suspended at Phase 4 Battle resolution | All other faction turns hold |

**TTRPG Scene: Siege of Himmelenger Cathedral**

Marshal Edren leads 2 TTRPG combat units (Str 2 each). Church defenders hold Himmelenger (Str 2, Cohesion 6, Fort 2 providing +2D defensive bonus).

**TTRPG Mass Combat Phase 1:**
Edren's Command: Coordination 4 → 4D. Ob 2. P(Succ): ~85%.
Result: Success. +1 to allied unit attack pool this phase.

**Church Defender morale check (TTRPG Ob = attacker's net successes from Command):**
Church Morale (Cohesion + 1 = 7, max cap). TN 7, Ob 1. Defenders steady — no morale break.

**TTRPG Combat Round 1:**
Crown attacks: Unit 1, Martial equivalent (from B.2 conversion) — Crown Military stat 3 → CP 3. 3D vs Ob = Church Cohesion ÷ 2 = 3. +1D from Command = 4D vs Ob 3.
P(Succ): ~40%. 
Result: Partial. Church takes half damage. Church unit Health −1.

Church counter: 6D (Military 4 + Fort 2) vs Ob = Crown Cohesion (starting 4, TTRPG: set to BG Cohesion equivalent of Crown battle unit — using BG Military 3, Cohesion = 4 per B.2). Ob 4 for Church attack.
Church 6D vs Ob 4: P(Succ): ~55%.
Result: Success. Crown unit Health −1. 

**State after Round 1:** Crown unit Health −1. Church unit Health −1. Marshal Edren uninjured (commanding, not in direct melee yet).

**Varfell spoiler in Hybrid mode:**
Varfell has a Tribune (agent character) in Himmelenger — established via prior Counter-Narrative action. During Zoom In personal phase, Varfell's agent acts. 

**Varfell agent action (TTRPG personal scale):**
Goal: not help Crown take Himmelenger (that doesn't spoil Church — it removes Church from board entirely, leaving no one to accumulate TC, meaning game continues without Church as meaningful actor). Varfell's spoiler goal is to keep Church alive but suppress TC. 

Varfell's agent attempts to **leak information to Church about Crown's battle plan** (Varfell wants Church to WIN the battle — keeping Church alive as TC-suppressed faction is better than eliminating Church who then can't be spoiled). Tribune Intel action: reveal Crown's Marshal position to Church Commander.

TTRPG Tribune Intel (Investigate, Ob 1 in own operative's area): 4D vs Ob 1. Overwhelming near-certain.
Result: Overwhelming. Church Commander gains +1D for one round (advance knowledge of Crown's flanking route). 

**Round 2 (modified by Varfell Intel):**
Church defends with +1D this round (Varfell sabotage of Crown's surprise): Church 7D vs Ob 4.
P(Succ): ~65%.
Result: Success. Crown unit Health −2 (cumulative). Crown unit breaks (Health ≤ 0 threshold at TTRPG scale).

**Combat resolution:** Crown routs. Marshal Edren retreats. Zoom Out triggered.

### State Transfer (TTRPG → BG)

Per state_transfer_spec.md Zoom Out:

| TTRPG Outcome | BG Update |
|---|---|
| Crown unit broken (Health = 0) | BG unit Strength 0 (unit destroyed). Crown Military −1. |
| Church unit Health −1 | BG Church unit Strength −1 (converted back) |
| Varfell Tribune in T9 (personal action) | Domain Echo queued: Intel network in T9 (declared as Varfell presence in T9). Fires at Accounting as Varfell AP-token in T9? No — Domain Echo is faction stat change, not token. **Ruling: Tribune's action in T9 is a personal TTRPG action, not a Domain Action. No Domain Echo fires. The Intel reveal is a personal-scale outcome — it doesn't translate to BG stats.** |
| T9 CV unchanged | No Faith-affecting scene — no CV Domain Echo |
| Marshal Edren retreats (wounded? Crown player declares yes — dramatic stakes) | Edren takes 1 Wound. BG: Commander bonus unaffected (wounds are personal). |

**Domain Echo clarification:** Varfell's Tribune leaking intel to Church — is this a Thread operation consequence? No — it's a non-Thread personal skill action. The state_transfer_spec only queues Thread operation RS consequences and explicit Domain Actions. Personal combat support (Tribune passing information to defend against Crown) is personal narrative. No BG stat change. Correct.

**BG resumes:** Crown failed to take T9. Crown Military now 2 (down from 3 — further attrition). Church holds T9.

**TC accounting (S6):** Church chose NOT to Assert (they were defending). Passive +1 only. TC 36 → 37.
Church AP: still 2. Below threshold.

---

## S7 — Varfell spoiler escalates

**Board Game phase — Church plans Assert:**
Church has stabilised after Crown's failed assault. Now plays Assert (Phase 4 Priority 6). TC 37 → 39.

**Varfell spoiler response:**
Counter-Narrative in T9 again (same territory, AP was reset at Accounting S5 and S6). 
Ob = Church Mandate ÷ 2 = 3, Consequentialism −1 = Ob 2. Intel 4D vs Ob 2.
Result: **Overwhelming** (rolled 27% chance). TC −0.5. AP +2 in T9.

TC effect: Church Assert (+2 this season) − 0.5 (Counter-Narrative OW) = net +1.5 TC.
Running fractional TC: 37 + 1.5 = **TC 38.5** (track decimal).
AP in T9 = 2. Threshold at 3 — still below.

**S8:** Church Assert again. TC 38.5 + 2 = 40.5. Varfell Counter-Narrative → Success (AP +2, no TC). AP accumulates across seasons? No — AP resets at Accounting Step 5. Each season's AP is independent. Varfell's Counter-Narrative creates AP within the season, but it can only trigger threshold once if it reaches ≥ 3 within that season.

**AP sequencing:** Counter-Narrative fires Phase 4 Priority 1 (Intel, first in sequence). AP +2 at Priority 1. Active Inquisition (Church) fires at Phase 4 Priority 4 (Domain). If Church also plays Active Inquisition this season: AP +2 (Counter-Narrative) + AP+2 or +3 (Active Inquisition) = AP 4–5 before Accounting. First Inquisitor threshold AP ≥ 3: fires. Second threshold AP ≥ 6: may fire if Church Inquisition hits Overwhelming.

**S8 with both:** AP = 2 (Counter-Narrative) + 3 (Active Inquisition Overwhelming) = 5. First Inquisitor deploys in T9. Second Inquisitor: AP ≥ 6, not reached. AP resets to 0.

**Inquisitor in T9 (Himmelenger):** Counter-Narrative in T9 is now +2 Ob. Ob 2 → Ob 4.

**Varfell S9 Counter-Narrative in T9 (Ob 4, Intel 4D):** P(OW): ~1%, P(Succ): ~15%, P(Fail): ~44%.
**Finding: Inquisitor in Church's own capital renders Counter-Narrative nearly unworkable.** Varfell must either:
a) Accept the Ob 4 risk and continue Counter-Narrative (low value, high fail)
b) Shift Counter-Narrative to other Church-prominent territories without Inquisitors
c) Use Tribune to REMOVE the Inquisitor — Investigate action in T9. But Investigate in Church territory with Inquisitor: +2 Ob (Ob 2 + 2 = Ob 4 also). Same penalty. Breaking an Inquisitor network requires sustained success at +2 Ob.

**Finding P1 — Spoiler lockout by Inquisitor:** Church can neuter Varfell's primary spoiler tool by deploying an Inquisitor in their own capital. This is a natural counter-play that costs Church the AP system (Inquisitors are a resource generated by AP accumulation — deploying in own territory is defensive but reduces offensive AP generation elsewhere).

**Finding P2 — Spoiler shift to adjacent territories:** Varfell pivots Counter-Narrative to T2 (Kronmark, Crown-controlled, Church-prominent if Church Mandate > Crown Mandate). Church Mandate 5 > Crown Mandate (now reduced by Decree chain to 4 — wait, Crown's target is Church here, not Varfell. Crown's Decree chain targeting Church would lower Church Mandate. If Church Mandate 4, Crown Mandate 5 → Church is NOT prominent in Crown territories. Counter-Narrative requires "Church-held or Church-prominent territory." At Church M 4, Crown M 5: Church not prominent in Crown territories. Varfell loses valid targets outside T9.

**Finding P3 — Church-prominent territory requirement is a significant constraint on Varfell spoiling:**
Varfell can only Counter-Narrative in:
- Church-held territories (T9 Himmelenger)
- Church-prominent territories (Church Mandate > controller's Mandate)

If Crown maintains Mandate ≥ Church Mandate: no Crown territories are valid. If Hafenmark maintains Mandate ≥ Church Mandate: no Hafenmark territories valid. Varfell's own territories: Church Mandate must exceed Varfell Mandate (both start at 4/5 — Church 5 > Varfell 4 initially, but equalises quickly).

**Valid Counter-Narrative targets (Church M 5, starting):**
- T9 Himmelenger (Church controlled): always valid
- Any territory where controller Mandate < 5: Hafenmark M 4 → all Hafenmark territories valid. Varfell M 4 → own territories valid.

**S9 pivot:** Varfell plays Counter-Narrative in T7 (Rendstad, Hafenmark-controlled, Hafenmark M 4 < Church M 5). Ob = Church M ÷ 2 = 3, Consequentialism −1 → Ob 2. No Inquisitor in T7. Intel 4D vs Ob 2.
Result: **Success.** AP +2 in T7. This AP is in Hafenmark territory — it raises AP pressure in T7, not T9. Hafenmark player is annoyed: an Inquisitor may deploy in their territory.

**[EDITORIAL: ED-325 — Confirm that AP from Counter-Narrative in faction-X territory causes Inquisitor deployment in that territory if threshold reached. Is AP tracked per-territory or globally? Current understanding: AP is a Church global pool — accumulation from any territory contributes to threshold, but Inquisitor deploys in the territory where the AP threshold was triggered (the territory where the AP was generated). Requires designer confirmation before BG compilation.]**

---

## Spoiler Sustainability Assessment — Hybrid vs BG

### Hybrid-specific dynamics

**1. Zoom In disrupts Board Game timing.**
Varfell's agent in T9 can trigger personal-scale actions that benefit Church without being a Domain Action (no Domain Echo). Varfell's Tribune passing intelligence to Church defenders during Crown's assault is purely personal-scale — no BG trace, no Domain Echo. This means Varfell can engage in covert spoiling behaviour that is **invisible to the BG layer.** The BG sees: Crown failed assault. It doesn't see: Varfell's Tribune helped Church win.

**Finding P4 — Hybrid spoiling is harder to counter-detect.** In BG-only, all actions are public (card plays are declared). In Hybrid, personal-scale Tribune actions during Zoom In are not Domain Actions and leave no BG trace. Varfell can help Church survive without Crown knowing Varfell was responsible. This is interesting but requires no mechanical correction — it's a designed asymmetry of Hybrid mode.

**2. Domain Echo limit constrains Zoom In spoiling.**
Varfell's agent actions during Zoom In may not queue Domain Echoes unless they are explicitly Domain-class actions (Govern, Trade, etc.). Personal Intel, combat support, and information sharing are personal-scale outcomes. This prevents Hybrid Zoom In from becoming a way to bypass BG stat change caps via personal-scene stacking.

**3. State transfer creates Varfell spoiler opportunity:**
On Zoom Out, Unit Strength losses translate back to BG stats. Crown Military 2 after S6 assault means Crown's TCV expansion is blocked — they can't march into adjacent territories without military capacity. Varfell's Tribune action (helping Church win the battle during Zoom In) translates to Crown Military reduction on Zoom Out. Varfell spoils Crown's expansion by protecting Church in Hybrid mode.

**Finding P5 — Cross-faction spoiling in Hybrid:** Varfell (targeting Church for BG-layer TC suppression) simultaneously assists Church in Hybrid Zoom In scenes to weaken Crown. The two spoiling objectives are not contradictory: Varfell wants Church to survive (can't spoil a dead faction) AND wants Church TC suppressed. Both goals are served by helping Church beat Crown militarily while running Counter-Narrative to suppress TC advance.

---

## Mode L: Cognitive Load Assessment

**Hybrid spoiler cognitive requirements:**
1. Track BG: Counter-Narrative target eligibility (Church Mandate vs controller Mandate)
2. Track BG: Church AP per territory per season
3. Track Hybrid: which personal actions during Zoom In count as Domain Actions (Domain Echo?) vs personal narrative
4. Track Hybrid: state transfer on Zoom Out (Crown Military losses)
5. Maintain separate spoiler objective from own win condition (Varfell pursuing Thread Supremacy while spoiling Church)

**Load rating: HIGH.** The Hybrid spoiler requires managing two strategic layers simultaneously. The Zoom In/Zoom Out state transfer adds calculation burden. Varfell's dual goal (spoil Church TC + pursue Path C) creates competing resource demands on Tribune card and Intel stat. 

**Recommendation:** Hybrid spoiler is achievable by experienced players but should not be attempted as a first-game strategy. The cognitive load of simultaneous BG suppression + Hybrid personal-scale actions + win path tracking is substantial.

**Friction point:** Determining Counter-Narrative target eligibility (Church Mandate vs territory controller Mandate) requires comparing stats publicly known but frequently changing. At fast-moving game states, this check must happen every season. Recommend: print territory Church Prominence on faction sheets (updated at Accounting: "Church prominent in: [list territories]").

**[EDITORIAL: ED-326 — Recommend a "Church Prominence tracker" on the Church mat listing territories where Church Mandate exceeds controller Mandate. Updated at Accounting. Reduces per-season calculation for Counter-Narrative eligibility and Seizure Ob. Flag for designer confirmation.]**

---

## Simulation Verdict

**Hybrid Mode Spoiler (Varfell spoiling Church): FUNCTIONAL with notable caveats.**

Varfell's spoiler capability in Hybrid is stronger than in BG-only because personal-scale Zoom In actions are invisible at the BG layer. However, the spoiler is heavily constrained by:
- Counter-Narrative target eligibility (Church Prominence requirement)
- Inquisitor deployment (Church can lock out Counter-Narrative in own capital)
- AP reset cycle (AP resets every Accounting — AP pressure doesn't accumulate across seasons, only within one season)
- Card hand limits (Tribune Outward: one use per season)

The spoiler is viable as a side strategy for Varfell pursuing Thread Supremacy (Path C), where RS maintenance and TC suppression share objectives. Pursuing spoiler as primary strategy at the cost of win path investment is suboptimal for Varfell — the spoiler tools are side effects of Varfell's normal play, not dedicated spoiler mechanics.

**Cross-mode interest:** The Hybrid finding (Varfell secretly assisting Church during Crown's Zoom In assault) is a compelling emergent scenario — a faction that is simultaneously suppressing Church's TC rise and helping Church survive military threats. No new rules needed; this arises naturally from the BG/Hybrid layer distinction.

**Open items:**
- [EDITORIAL: ED-325 — AP per-territory vs global pool; Inquisitor deployment target when Counter-Narrative generates AP in faction-X territory]
- [EDITORIAL: ED-326 — Church Prominence tracker recommendation]

