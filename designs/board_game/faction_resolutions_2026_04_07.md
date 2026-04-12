<!-- DEPRECATED -->
> **DEPRECATED — 2026-04-11**
> Working design notes (PP-428+, ED-318+). Content absorbed into references/params_factions.md and designs/board_game/valoria_bg_v05_simulation_and_patches.md (canonical).
> Do not use as a canonical source.

---

# Valoria — Faction Playability Resolutions
<!-- DATE: 2026-04-07 | PP-428 onwards | ED-318 onwards -->
<!-- Sources: params_factions.md, valoria_bg_v05, victory_architecture_v1.md, params_board_game.md (all canonical, fully read) -->

---

## PREAMBLE

Card hands (canonical from params_board_game.md):
| Faction | Hand |
|---------|------|
| Crown | 2× Legionary, 1× Consul, 1× Senator, 1× Prefect, 1× Recess |
| Church | 2× Senator, 1× Pontifex, 1× Consul, 1× Legionary, 1× Recess |
| Hafenmark | 2× Consul, 1× Senator, 1× Legionary, 1× Diplomat, 1× Recess |
| Varfell | 2× Tribune, 1× Legionary, 1× Consul, 1× Colonist, 1× Recess |

Domain Expertise (+1D): Crown = Legionary | Church = Senator | Hafenmark = Consul/Prefect | Varfell = Tribune

All proposals respect existing card hand composition. No new card types introduced without an editorial flag.

---

## PROPOSALS REQUIRING USER DECISION FIRST

The following items need design input before patch text can be written.

### [EDITORIAL: ED-318] — Total Domination TCV threshold and Formal Submission mechanic

The user established that all four factions have a Total Domination path (hold all territories except T15 Askeheim and T16 Schoenland, by elimination OR submission). Total controllable TCV = 28. Two design questions before formalising:

**Q1:** Is the threshold TCV = 28 (every controllable territory), or is some lesser number acceptable for Total Domination (e.g. TCV ≥ 24, allowing a small holdout)?

**Q2:** What does Formal Submission look like mechanically for non-Crown factions? For Crown, Formal Crown Treaty is already designed (Diplomacy, Ob = target Mandate, mutual consent, target Mandate −1/Stability +1). For other factions, a "Vassalage" action is needed. Proposed options:
- **Option A:** Formal Submission uses the same mechanic as Formal Crown Treaty (Senator Outward, Ob = target Mandate, mutual consent), available to all factions, not just Crown. The submitting faction accepts Mandate −1, Stability +1. Triggers the "suppress" condition for the dominant faction.
- **Option B:** Formal Submission is a separate mechanic (Senator Outward, Ob 2, dominant faction rolls against submitting faction's Stability), not requiring mutual consent — the dominant faction can force submission if they've reduced the target's Stability below 3.
- **Option C:** No Formal Submission mechanic for non-Crown factions. Total Domination requires full elimination of all rivals. Submission (as a gentler path) remains Crown-exclusive.

### [EDITORIAL: ED-319] — Parish/Cathedral construction cost and duration

Proposed: Church Consul action initiates Parish construction (2 sequential seasons of Consul action in same territory with AP ≥ 2 = Parish complete). Cathedral requires Parish + 3 more seasons of Consul action. Wealth costs TBD. Questions:

**Q1:** Is the 2-season Parish / 5-season Cathedral cadence appropriate? Church has 1 Consul card — committing to construction means no Trade or Govern in that territory for multiple seasons. Does that opportunity cost feel right?

**Q2:** Should construction survive territory control changes? (Proposed: no — control transfer destroys the structure.) Or should Parishes be transferable (the building still stands even if another faction takes the territory)?

**Q3:** Wealth cost: Proposed Parish = Wealth 1, Cathedral = Wealth 2 (additional, on top of Parish). Church Wealth starts at 5. Does this feel appropriately weighty without being prohibitive?

### [EDITORIAL: ED-320] — Hafenmark Diplomat card definition

Hafenmark's hand includes a Diplomat card (unique to Hafenmark). No canonical mechanical definition found in any read document — PP-181 mechanics exist only in SUPERSEDED v04 B5. The Diplomat card's action and Ob are undefined in any current canonical source. Before proposals touching Hafenmark's card-based mechanics can be written, the Diplomat card needs to be defined.

**Q:** What does the Hafenmark Diplomat card do? Is it a specialised Diplomacy action (Senator Outward function with different Ob or scope), a Parliamentary tool, a Trade-adjacent action, or something else?

### [EDITORIAL: ED-321] — RDT/TD full mechanic extraction

RDT (Reformed Doctrine Track, 0–6) and TD (Theological Dissatisfaction, 0–5) are Hafenmark private tracks. Full mechanics documented only in SUPERSEDED v04 B5. Current canonical sources reference them (PP-181) but do not reproduce their tables. From what can be inferred: RDT advances from Reformed Settlement events, RDT 6 = Diplomatic actions targeting Hafenmark +1 Ob.

Cannot propose "surface RDT as a visible progression arc" (Priority 16) without reading the full mechanic. Either the v04 B5 content needs extracting into params_factions.md, or the designer can confirm/restate the RDT table here.

**Q:** Confirm or restate the full RDT track mechanics (0–6 threshold effects and advancement triggers) and TD track (0–5 effects and triggers), so they can be extracted to params_factions.md.

---

## RESOLUTIONS — DIRECT PATCHES

The following items can be resolved without user decision. Text below is ready to commit.

---

### PP-428 — Church: Piety Spread action (CV-raising pre-seizure)

**Resolves:** Review concern B1 (CV static pre-seizure). Addresses the circular dependency between CV and TC generation.

**Card type:** Consul Inward (Church only). Uses Church's single Consul card. Opportunity cost: no Govern or Trade in the same season if Piety Spread is played.

**Scope:** Any territory (Church-controlled or not). Church must have at least 1 Attention Pool point in the target territory (AP ≥ 1). If AP = 0 in that territory, Piety Spread is unavailable there — the Church has no established presence to build from.

**Roll:** Influence vs Ob = controlling faction's Mandate ÷ 2 (round up, min 1) + Fort Level.
Doctrine-aligned: −1 Ob. Ob floor: 1.

| Degree | Effect |
|--------|--------|
| Overwhelming | CV +1 in territory; AP +1 in territory (missionary activity draws attention) |
| Success | CV +1 in territory |
| Partial | No CV change; AP +1 in territory (presence felt but not yet persuasive) |
| Failure | Church Stability −1 (congregation pushed back); AP unchanged |

**CV cap:** Piety Spread is a deliberate Church action. Subject to the 1 CV-change action per territory per season cap. Calamity Drift and seizure Overwhelming CV bonuses are consequences, not actions — not capped.

**Post-TC 75:** Piety Spread continues to function. Restriction: may only target territories adjacent to a Church-held territory (range-limited during active seizure campaign). Cannot target T15 or T16.

---

### PP-429 — Church: Active Inquisition action (Attention Pool-raising)

**Resolves:** Review concern B3 (Attention Pool has no Church-driven input). Gives Church player agency over Inquisitor deployment.

**Card type:** Senator Inward (Church only). Uses one of Church's two Senator cards. Church can still Decree or Excommunicate with the second Senator.

**Roll:** Mandate vs Ob = territory Stability ÷ 2 (round up, min 1). Ob floor: 1.

| Degree | Effect |
|--------|--------|
| Overwhelming | AP +3 in territory; if AP now ≥ threshold, Inquisitor deploys immediately (does not wait for Accounting) |
| Success | AP +2 in territory |
| Partial | AP +1 in territory |
| Failure | AP −1 in territory (backlash); Church Stability −1 |

**Sustained pressure rule:** If AP ≥ 8 in any territory at Accounting: that territory Stability −1 (resentment from prolonged Inquisition). This fires at Accounting Step 4 alongside clock advances. Applies once per territory per Year-End regardless of how AP reached 8.

**Interaction with existing AP:** Active Inquisition stacks with passive AP accumulation from Thread activity. Both sources contribute to the same per-territory AP track.

**Heresy Investigation eligibility:** Active Inquisition does not itself open an HI. The resulting AP level may reach the HI-triggering threshold at Accounting (per existing Church AP rules), which then requires a valid target per P-25.

---

### PP-430 — Church: Cardinal Focus (seasonal decision)

**Resolves:** Review concern B4 (Cardinal system generates no decisions). Converts passive Cardinal mechanics into a weekly player choice.

Each season during Phase 1 (Strategy Declaration), the Church player designates one Cardinal as **Focused**. One designation per season. The Focused Cardinal's function is enhanced for that season. No cost; declarative only.

| Cardinal | Base function | Focused enhancement |
|----------|--------------|-------------------|
| Fortitude | Templar deployment (Stability ≥ 2 required) | Templar unit deploys this season without consuming Church's Legionary card (the order comes from the Cardinal directly) |
| Justice | HI oversight | The AP threshold for first Inquisitor deployment in any one territory is reduced by 1 this season |
| Prudence | +0.5 Wealth/season from tithed territories | +1 Wealth this season (full integer; rounds normally at Year-End in addition) |
| Temperance | AER maintenance via university city | AER +1 this season (active diplomatic engagement, not merely maintenance) |

**Cardinal schism interaction:** If Cardinal schism fires (Church Stability = 2 + hostile Senator action this season), the schisming Cardinal acts independently regardless of Focus designation. Focus is suppressed on the schisming Cardinal for that season.

**Note on Fortitude Focus:** Templar deployment without spending Legionary card means Church can deploy Templars AND use their Legionary card for military action in the same season. This is the most powerful Focus option and is intentionally available — Templar deployment is already gated by Stability ≥ 2 and requires Cardinal of Fortitude to be active.

---

### PP-431 — Hafenmark: Parliamentary Challenge (seasonal TC tool)

**Resolves:** Review concern C2 (Hafenmark lacks recurring TC-influence agency between Sovereign Authority Doctrine uses).

**Card type:** Senator Inward (Hafenmark only). Uses Hafenmark's single Senator card. Opportunity cost: no Decree or other Senator action this season.

**Frequency:** Once per season. Not limited by campaign arc. Cannot be used in the same season as Sovereign Authority Doctrine (Doctrine is the arc-use; Challenge is the seasonal tool — they are distinct).

**Roll:** Mandate vs Ob 2.

| Degree | Effect |
|--------|--------|
| Overwhelming | TC −2; Church must Uphold or Appease their Institutional Mandate response |
| Success | TC −1 |
| Partial | No TC effect; Hafenmark Stability −1 (the challenge was seen as overreach) |
| Failure | Hafenmark Stability −1; Church Mandate +1 (Parliament rebuked) |

**Doctrine relationship:** Parliamentary Challenge does not spend the Sovereign Authority Doctrine arc-use. The Doctrine remains available for its dramatic arc-level effect (TC −2/−3 + Church Mandate −1) regardless of how many Challenges Hafenmark has played.

**Ethical framework:** Parliamentary Challenge is grounded in constitutional precedent (Hafenmark's framework). It is a procedurally grounded action: −1 Ob applies... wait, the roll is already at Ob 2 with no modifier listed. Add: if Parliament Integrity (PI) ≥ 5, Ob −1 (PI 5 = full Parliament, procedural challenge has institutional backing). Ob floor 1.

---

### PP-432 — Hafenmark: Parliamentary Session (proactive PI-building, once per arc)

**Resolves:** Review concern C1 (Hafenmark has no proactive PI-building tool; TC suppression is automatic).

**Card type:** Senator Outward (Hafenmark only). Uses Hafenmark's single Senator card. Usable once per campaign arc (every 4 seasons). Tracked with a counter on Hafenmark's faction mat.

**Procedure:** Hafenmark declares a Parliamentary Session. All other playable factions declare Vote or Abstain before Phase 4 resolves. NPC factions vote per their institutional tendency AI (Church: Oppose if TC ≥ 40; Crown: Support if Mandate ≥ 4; Varfell: Abstain unless co-victory conditions align). Voting is public. Abstaining generates no mechanical effect.

**Resolution at Accounting:**
- **Majority Support** (≥ half of participating factions voted): PI +1. Hafenmark Mandate +1 (Parliament ratified a motion; legitimacy accrues). Supporting factions gain Resentment token vs any faction that voted against.
- **Majority Opposition** (more votes against than for): Hafenmark Stability −1. PI unchanged. Opposing factions gain +1 Standing (blocked a Hafenmark initiative).
- **Tie:** Motion fails by abstention. No PI change. TC +1 (institutional paralysis — per existing tie rule in batch_f_designs.md G-023).

**Blocking faction consequence (per PP-405):** Any faction that votes against gains a Resentment token vs Hafenmark. Hafenmark gets −1 Ob on Domain Actions targeting that faction; that faction gets +1 Ob targeting Hafenmark.

**Ministry interaction:** If Ministry has AP-token in T12 (Valorsplatz) this season, Parliamentary Session Ob is reduced by 1 (Ministry facilitates the session procedurally). Since there is no roll for the session itself (it's a vote), this instead means: Ministry's Vote counts as Support automatically when AP-token present in T12.

---

### PP-433 — Crown: Royal Charter (institution-building action)

**Resolves:** Review concern A2 (Crown has no distinctive growth mechanic; play identity is passive holding).

**Card type:** Consul Inward (Crown only). Uses Crown's single Consul card.

**Scope:** Any Crown-controlled territory. Cannot Charter a territory Crown does not control. Cannot Charter T15 or T16.

**Roll:** Mandate vs Ob = territory Prosperity ÷ 2 (round up, min 1). Ob floor 1. Virtue Ethics: visible, public institution-building = −1 Ob.

| Degree | Effect |
|--------|--------|
| Overwhelming | Territory becomes a **Crown Charter Territory** this season AND Prosperity +1 |
| Success | Territory becomes a **Crown Charter Territory** |
| Failure | Mandate −1 (attempted Charter rejected by local resistance) |

**Crown Charter Territory effects (permanent while Crown controls it):**
- All factions' Govern and Trade actions in that territory: Ob −1 (legitimate governance reduces friction)
- Church Seizure Ob in that territory: +1 (administrative apparatus resists institutional capture)
- Crown's own Govern/Trade in that territory: Ob −2 (stacks with the general −1 reduction)
- If control transfers to another faction: Charter dissolves. Territory reverts to standard state.

**Charter limit:** Crown may have at most (Mandate ÷ 2, round up) Charter Territories active simultaneously. At Mandate 5: max 3 Charters. This represents administrative bandwidth. If Crown loses Mandate and drops below the cap, no existing Charters dissolve — but new Charters cannot be created until Mandate recovers.

**Victory interaction:** Formal Crown Treaty (the "suppress" tool) and Royal Charter (the "hold" tool) are complementary. A Chartered territory that a rival faction has submitted treaty control over is more stable — both effects apply.

---

### PP-434 — Crown: Formal Crown Treaty surfaced as primary faction mechanic

**Resolves:** Review concern A3 (Formal Crown Treaty is buried in victory conditions; should be a primary strategic tool).

No mechanical change. Documentation change only.

The Formal Crown Treaty is already defined in victory_architecture_v1.md §3.1. This patch adds it explicitly to Crown's faction action list in params_board_game.md and params_factions.md under Crown's Domain Actions, alongside Royal Decree and Royal Charter.

**Formal Crown Treaty (Senator Outward, Crown only):** Ob = target faction's Mandate. Both factions must agree (target may refuse; refusal generates no consequence for either party). On agreement: target faction Mandate −1, Stability +1. Treaty satisfies the "suppress" condition for that faction in Crown's victory check for as long as the Treaty holds. Crown breaking the Treaty: Crown Stability −2, Mandate −1, permanent Grievance Marker vs the betrayed faction. Treaty dissolves if target faction Mandate reaches 0.

**New addition (not previously defined):** A faction that has submitted to Formal Crown Treaty may not be the target of Crown military actions while the Treaty holds. If Crown attacks a Treaty partner, the Treaty dissolves immediately + Crown Stability −2 + Mandate −1 (same as breaking it).

---

### PP-435 — Crown: Royal Decree Overwhelming enhancement

**Resolves:** Review concern A1 (Royal Decree is mechanically thin; Overwhelming has same effect as Success).

Current: Mandate vs Ob 2. Success/Overwhelming: one faction stat ±1, immediate. No distinction between degrees.

**Change:** On Overwhelming (net ≥ 2× Ob = net ≥ 4 at Ob 2), Crown may choose one of:
- (a) stat ±2 to one faction (instead of ±1)
- (b) stat ±1 to two different factions simultaneously (same season, same decree)
- (c) stat ±1 to one faction AND suspend one threshold effect for one season (e.g. prevent TC passive +1 from firing, or prevent IP +1 from firing, or prevent PI degradation from one source this season)

Standard Success remains: stat ±1 to one faction. No change.

Consecutive use fatigue unchanged: +1 Ob per consecutive season of use.

---

### PP-436 — Crown: Thread Liaison (RS engagement path)

**Resolves:** Review concern A4 (Crown has no RS engagement tool despite RS being relevant to co-victory conditions).

**Mechanic (declarative, no roll):** Once per season during Phase 1, Crown may designate one allied faction as their **Thread Liaison**. "Allied" = a faction with whom Crown has an active Formal Crown Treaty, OR a faction that voted Support in a Parliamentary Session called by Hafenmark, OR a faction with Resentment tokens vs a common enemy.

**Effect:** Thread operations performed by the Liaison in Crown-held territories this season generate RS changes that count toward Crown's co-victory RS threshold tracking. No mechanical RS change occurs — it is purely a tracking rule for co-victory eligibility. Crown cannot designate themselves. Designation is public.

**Removal:** If Crown and the Liaison faction enter military conflict this season, the Liaison designation dissolves immediately.

**Rationale:** This gives Crown a reason to protect Thread-active allies (Varfell, Restoration as ambient force) rather than suppress them, which is consistent with Almud's personal character (private sympathies with the Restoration) and creates interesting diplomatic dynamics.

---

### PP-437 — Crown: Diplomatic Outreach to Schoenland (IP management)

**Resolves:** Cross-faction systemic concern (Crown has no dedicated IP-management Domain Action despite IP < 60 being a victory condition).

**Card type:** Senator Outward (Crown only). Target: Schoenland (T16). Ob = current AER level (AER 0 = Ob 0, but floor 1 applies; AER 5 = Ob 5).

**Roll:** Influence vs Ob.

| Degree | Effect |
|--------|--------|
| Overwhelming | IP −2 this season; AER +1 |
| Success | IP −1 this season; AER +0.5 (track fractional; apply at Year-End) |
| Partial | No IP change; AER +0.5 |
| Failure | AER −0.5 (diplomatic misstep damages relationship) |

**Ethical framework:** Public diplomatic action = Virtue Ethics aligned = −1 Ob.

**Frequency:** Once per season. Cannot be used in the same season as Formal Crown Treaty (both use the Senator card).

**Schoenland orientation interaction:** If Valoria is fragmented (3+ factions with Stability ≤ 2 simultaneously), Ob +2 for this action (Schoenland hedges toward Altonia when Valoria is weak).

---

### PP-438 — Varfell: VTM Discretion (TC suppression spend)

**Resolves:** Review concern D2 (VTM advancement raises TC; no mitigation exists).

At VTM 3+, Varfell may spend 1 Patience Counter during Accounting (before TC is calculated) to suppress their VTM's TC contribution for that season only.

**Effect:** The TC +1/+2/+3 that would be generated by Vaynard's VTM level (from TK track) does not fire this Accounting. TC advances normally from all other sources (Institutional Momentum, Conviction Yield, Assert, etc.) — only the VTM-specific contribution is suppressed.

**Limit:** Cannot suppress more than once per 2 consecutive seasons. Track with a "Discretion Cooldown" marker on Varfell's mat: placed when suppression fires, removed at start of next Year-End Accounting (every 4th season). While marker is present, VTM Discretion unavailable.

**Rationale:** Vaynard can maintain deliberate opacity about his Thread knowledge for a season, but sustained concealment is exhausting and the institution eventually notices patterns.

---

### PP-439 — Varfell: Revelation Tokens for Path A "fully revealed" condition

**Resolves:** Review concern D4 ("fully revealed" condition for Path A is underspecified).

A rival faction's stats are "fully revealed" to Varfell when either:
- (a) Varfell achieves an **Overwhelming** result on an Investigate/Intel Tribune action targeting that faction (reveals complete stat block at point of roll), OR
- (b) Varfell spends **4 Patience Counters** on a Spy action targeting that faction (4 PC Spy already defined; its outcome now formally includes "fully reveal all stats").

**On full revelation:** Varfell places a **Revelation Token** on the target faction's mat. Token is visible to all players. It is permanent for this game — it cannot be removed by any mechanic. Revelation Tokens placed while a stat was accurate remain even if the stat subsequently changes; the token indicates "Varfell fully revealed this faction's stats at one point in time," not ongoing certainty.

**Path A tracking:** Two Revelation Tokens on two different rival faction mats = Path A "2 rival factions fully revealed" condition met. Token count is checked at Accounting Step 12 alongside other victory conditions.

**Fog of war note:** The target faction knows they've been revealed (Revelation Token is public). This is intentional — the political consequence of Varfell's intelligence supremacy becoming visible is part of the game's tension.

---

### PP-440 — Varfell: Ethical Framework clarification for Intel actions

**Resolves:** Review concern D3 (ethical framework ambiguity — does VTM-building Tribune action attract −1 Ob or +1 Ob?).

Add to Varfell's faction sheet: "Tribune Intel actions (Investigate, Spy, VTM-building in Thread-active territories) are **concrete measurable outcome** actions. Consequentialism applies: −1 Ob on these actions. The outcome of a Tribune action is determined this season (the roll either succeeds or does not); the long-term value of accumulated VTM is a separate consideration that does not modify the roll's Ob."

"Actions that attract the +1 Ob penalty: public ideological campaigns, open diplomatic commitments with no measurable near-term payoff, relationship investments with no intelligence yield."

---

### PP-441 — Varfell: Counter-Narrative (TC interaction tool)

**Resolves:** Cross-faction systemic concern (Varfell has no TC tool; TC is a 2-faction contest between Church and Hafenmark while Crown and Varfell watch).

**Card type:** Tribune Outward (Varfell only). Varfell has 2 Tribune cards — this uses one. Can be played alongside a second Tribune action in the same season.

**Target:** Any Church-held or Church-prominent territory (territory where Church Mandate > controlling faction Mandate).

**Roll:** Intel (Influence for Varfell) vs Ob = Church Mandate ÷ 2 (round up). Consequentialism: evidence-based Intel = −1 Ob. Ob floor 1.

| Degree | Effect |
|--------|--------|
| Overwhelming | TC −1 this season; AP +2 in target territory (Varfell operatives document Church overreach — feeds AP system, potentially triggering HI against the Church if they're now prominent enough) |
| Success | TC −0.5 this season (apply as fractional; aggregate at Year-End, floor to 0) |
| Partial | AP +1 in target territory; no TC effect |
| Failure | Varfell's Intel network in that territory exposed; Church Attention Pool notes Varfell presence (AP +1 tagged as Varfell — Church player is informed Varfell has been operating there) |

**Note on TC −0.5:** Fractional TC is already in use (Conviction Yield generates 0.5 increments). The existing fractional tracking applies. TC cannot go below 0 via this mechanic.

---

### PP-442 — Counter-intelligence postures (all factions)

**Resolves:** Cross-faction systemic concern (Intel asymmetry has no counter-mechanics for Hafenmark or Church).

**Crown — Royal Guard (already exists, needs surfacing):**
Per PP-241 (Löwenritter Royal Investigators), Crown may cancel one successful Intel action targeting Crown per season. This mechanic already exists. No new mechanical text — add to Crown faction sheet explicitly: "Royal Guard: once per season, Crown may cancel one successful Tribune Investigate or Spy action targeting Crown. Announced at Phase 4 Priority 1 resolution. Does not cost a card."

**Hafenmark — Procedural Objection:**
New Hafenmark reactive mechanic. When Varfell successfully reveals a Hafenmark stat (any degree of Tribune Investigate against Hafenmark, not just Overwhelming), Hafenmark may immediately declare a **Procedural Objection**. This costs Hafenmark their Parliamentary Challenge use for the season (the Objection is filed through the same constitutional mechanism). If Hafenmark's Mandate ≥ 4 at the moment of objection: the revealed stat is replaced with a false value for all non-Varfell observers. Varfell retains the true value (they did the work); everyone else sees an inaccurate number (Hafenmark's procedural machinery obscures the leak). The false value is set by Hafenmark's player privately (any value within the stat's valid range). Corrected at next Accounting when all stats are publicly verified.

No roll required. Declarative. Once per season.

**Church — Sanctuary extension:**
Existing Church tactic card: Sanctuary (protect 1 NPC from targeting 1 season). Extension: Sanctuary may also be declared against a Varfell Spy action (4 PC spend) before that action resolves. If declared: Varfell's Spy action targets the wrong person or territory — they spend 4 PC but learn a false stat block instead of the true one (Hafenmark's parallel to Procedural Objection, but Church-style: the person is hidden behind institutional walls). Church may use this once per season regardless of whether Sanctuary has been used for NPC protection. These are two separate applications of the same tactic card.

---

## ITEMS DEFERRED TO EDITORIAL DECISIONS

The following proposals from the review cannot be implemented until the editorial items above are resolved:

| Proposal | Blocked by |
|----------|-----------|
| Total Domination formal condition | ED-318 (TCV threshold + Submission mechanic) |
| Parish/Cathedral building system | ED-319 (cost, duration, destruction rules) |
| Parliamentary Session voting procedures | ED-320 (Diplomat card definition affects who "participates") |
| Expose RDT as visible progression | ED-321 (RDT/TD full mechanics unknown) |
| Hafenmark Diplomat card proposals | ED-320 |

---

## SUMMARY TABLE

| PP | Faction | Item | Type |
|----|---------|------|------|
| PP-428 | Church | Piety Spread — Consul Inward, CV-raising | New action |
| PP-429 | Church | Active Inquisition — Senator Inward, AP-raising | New action |
| PP-430 | Church | Cardinal Focus — seasonal designation | New mechanic |
| PP-431 | Hafenmark | Parliamentary Challenge — Senator Inward, TC −1 seasonal | New action |
| PP-432 | Hafenmark | Parliamentary Session — Senator Outward, PI-building, once/arc | New action |
| PP-433 | Crown | Royal Charter — Consul Inward, institution-building | New action |
| PP-434 | Crown | Formal Crown Treaty — surfaced as primary mechanic | Documentation |
| PP-435 | Crown | Royal Decree Overwhelming enhancement | Mechanic enhancement |
| PP-436 | Crown | Thread Liaison — declarative RS engagement | New mechanic |
| PP-437 | Crown | Diplomatic Outreach to Schoenland — Senator Outward, IP management | New action |
| PP-438 | Varfell | VTM Discretion — PC spend to suppress TC contribution | New spend option |
| PP-439 | Varfell | Revelation Tokens — Path A "fully revealed" formalization | Formalization |
| PP-440 | Varfell | Ethical framework clarification for Intel actions | Clarification |
| PP-441 | Varfell | Counter-Narrative — Tribune Outward, TC interaction | New action |
| PP-442 | All | Counter-intelligence postures (Royal Guard surface, Procedural Objection, Sanctuary extension) | New mechanics |
| ED-318 | All | Total Domination TCV threshold + Formal Submission | User decision |
| ED-319 | Church | Parish/Cathedral cost, duration, destruction | User decision |
| ED-320 | Hafenmark | Diplomat card definition | User decision |
| ED-321 | Hafenmark | RDT/TD full mechanic extraction | User decision |
