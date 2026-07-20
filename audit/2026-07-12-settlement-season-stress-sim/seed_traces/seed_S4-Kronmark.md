# S4-Kronmark

## SETUP
Kronmark (S-004), a granary-adjacent agricultural TOWN (base Weight 2, so W_s = 2 + Prosperity 3 + FacilityTier 1 = 6), enters the sim at Prosperity 3 / Order 3 / Defense 1, Legitimacy 4 / Popular Support 4 (q_s = 0.5·4 + 0.5·4 = 4), FacilityTier 1 (AP = 2 + 1 = 3), Pi 6 and rising, under an active env.disaster famine (3-season crop failure covering S1-S3, modeled as external_shock via a regional Cooling flag, per substrate §5.5). PLAYER governor Aldric is Crown-ladder Standing 3 (Banneret), power_base = patronage (seated by Minister Voss) → resolution_quality weight w_d HIGH, w_n low. The roster: hungry Local Actors carrying an unserved relief Need; a grain Guild Master (Gu-Std3+) who will autonomously write a hoarding ordenanza; and superior faction patron Minister Voss, who issues an Extract Directive and pushes a Survey to lock the extraction base. Kronmark is treated as an effectively single-settlement holding, which itself strains the Mandate math (Mandate = Σ over settlements) — flagged as a gap. All 12 PR#119 provisional items active.

## SEASON TRACES
## SEASON 1 — Pi_start 8 (Crisis band)

**Pi recompute:** carried Π 6 + external_shock famine (+1) + unserved relief Need (+1) = 8. Matches substrate §5.5 (Cooling flag pushes 6→8). Band = HIGH (8-10) → Crisis. Draw = 1 + floor(8/3) = **3 cards**.

**Cards drawn (Crisis-weighted):**
- **CLIM-01 — Famine / StockLevel==None Crisis** (Climatic family). Trigger `StockLevel==None AND external_shock AND Π≥8` matches exactly. ⚠️ Source-fidelity: CLIM-01 exists in the deck **only as an ID** (§5 lever-ledger, StockLevel lever) — the grounded deck file carries full branch/delta text for only 9 cards, all of them low-Π Opportunity/Ambition/Thread. The entire Crisis band this seed lives in is **unspecified branch-data** (recorded as GAP-1). Resolved via the generic §C.2 resolver bucket (d_sigma Directive choice, FAIL_FLOOR .97) plus the §5.5 template.
- **GOVFRIC-05 — grain-unrest friction escalated to Crisis** (Governance-friction, re-familied to Crisis at high Π per §4 "every high-Π cluster defaulted to Crisis"). ID-only.
- Third draw filtered/de-duped against the same StockLevel cooldown → resolves to the patron pressure vector, surfaced as the **Extract Directive (Voss)** + **Survey push (1.3a)** rather than a fourth Crisis card. This is the §5.5 vise arriving live.

**Non-card layer — Directive (§1.4):** Minister Voss issues **Extract**. The §3 vise is live: Need = relief (feed the town) vs Directive = extract the quota; AP (3) and Treasury (Prosperity×10 = 30) insufficient for both. Aldric additionally activates **Retain Clerks (1.1a Clerk Capacity)**: 1 AP + W−1 (=5) spent → +1 effective AP (Clerk Capacity 1), giving 3 effective AP for governance verbs; Clerk Corruption counter set to 1 (silently raises Intrigue draw-weight for later seasons).

**Character engagements:**
- **SC (dice_pool):** Aldric **Bargains** the Extract Directive vs Voss to soften the quota — see MAJOR ROLL R1.
- **d_sigma (Directive response):** Aldric attempts **relief** on the Need jaw with his remaining AP — see MAJOR ROLL R2.
- **SC/FA:** Aldric tries to **resist/delay Voss's Survey** (1.3a Locked Extraction) — see MAJOR ROLL R3.

### MAJOR ROLL R1 — Bargain the Extract Directive (dice_pool, SC)
Pool = (Cognition 3 × 2) + History 1 = **7D**, TN 7, vs Ob = Voss Cha 4 ÷ 2 = 2, +1 for Voss's Directive backing → **Ob 3**. P(net ≥ 3 on 7D) ≈ **48%**.
**FAILURE trace (depth 3):**
- **L1 (immediate):** Bargain fails; full quota stands. Comply forced. Levy method fires L/PS −1 and Order −1: **PS 4→3, Order 3→3** (Order −1 offset by nothing yet), **L held 4** (Bargain protected legitimacy narrative even on loss). Debt-of-Standing tag NOT written (he Complied, didn't Defy). Π unchanged this step.
- **L2 (ripple):** Extraction-in-full during famine converts the unserved relief Need into a durable **Grudge tag (hungry Local Actors)** and puts the grain-hoarder's **Ambition card into motion**. New content: FI lead opened — grain-hoarder's black-market Debt tag becomes Investigate-discoverable (substrate §5.5 S5 FI hook); SC seeded — a Hafenmark-style Petition-right holder can cite the resolution Key via stakes.source_key.
- **L3 (further):** resolution_quality Key = w_d·(delivered_Directive − demanded_Directive ≈ 0, met) + w_n·(delivered_Need − demanded_Need, strongly negative) → net negative on the Need jaw only. Because w_d HIGH, this does NOT yet trip §1.0a Demotion (he served his patron). Emergent-arc seed planted: "the governor who fed the war and starved the town" (arc-generator reads the Key chain).

### MAJOR ROLL R2 — Famine relief attempt (d_sigma, Directive-response Need jaw)
d_sigma: base 50% + 10%/pt advantage, FLOOR .05 / CAP .90. Relief demanded ≈ 3 units; Aldric affords ≈ 1 (AP + thin Treasury after extraction) → advantage −2 → **P ≈ 30%**. FAIL_FLOOR .97 caps catastrophic branch at 3%.
**FAILURE trace (depth 3):**
- **L1:** Relief under-delivers. **Prosperity 3→2** (extraction net of famine). Need remains unserved → carries +1 into next Π. No stat gain; no Momentum.
- **L2:** Under-served town changes operation: Order now brittle (militia/consent options degrade); generates a **Petition card** for next season (Local Actors demand relief) and a live **stakes.source_key** hook — but note this SC edge is graded AT-RISK in the substrate (§14.3): canon's contest resolver has "Define stakes" but no ratified hook reading an external Key. Recorded under GAP as an at-risk dependency actually load-bearing here.
- **L3:** Mandate contribution drops (q_s falling toward 3). Region: correlated Cooling shock hits sibling settlements simultaneously (peninsula layer, R-3 territory scale UNBUILT). Arc: grief/grievance biases the hoarder Ambition upward for S2.

### MAJOR ROLL R3 — Resist Voss's Survey lock (dice_pool / FA, 1.3a)
Pool 7D, TN 7, vs Voss-backed Ob 4 (institutional authority) → P(net ≥ 4 on 7D) ≈ **40%**.
**FAILURE trace (depth 3):**
- **L1:** Survey succeeds; **Assessment tag `assessed_base` written and LOCKED at Prosperity-3-era figure** (~8-season cooldown before re-survey). Fiscal Stance / Levy now reads the locked figure, not live Prosperity. Π +0 immediate but a structural debt: the lock is stale-high the instant Prosperity fell to 2 in R2.
- **L2:** Operation change: every future extraction reads 3 while the town holds 2 and falling — the stale-high Assessment can "strip a declined settlement below subsistence via neglect" (1.3a explicit failure mode). New content: FA window — Voss can now extract on paper regardless of collapse; no player verb caps this (see GAP-7 subsistence floor).
- **L3:** This is the mechanical fuse for S2-S4 collapse. Arc seed: a Compact/Assessment "lock-in during worsening crisis" — the defining stress of this seed — is now armed and cannot be unwound for ~8 seasons.

**Pi_end S1 → S2 start:** clamp(8 + unserved Need 1 + new Grudge 1 + hoarder Ambition-in-motion 1 + shock 1 − player release 1[partial relief]) = clamp(11) = **10**.
**State end S1:** P2 O3 D1 L4 PS3; Clerk Corruption 1; tags: Grudge(Local Actors), Assessment(locked@3); Standing Crown 3 (protected).

---

## SEASON 2 — Pi_start 10 (Crisis band, saturated)

Draw = 1 + floor(10/3) = **4 cards**. Band HIGH → Crisis.

**Cards drawn:**
- **CLIM-01 famine** re-armed (shock still active, S2 of 3). ID-only.
- **GOVFRIC-02 — Guildhall Rises / Ordenanza** (Governance-friction): the grain Guild Master (Gu-Std3+) autonomously writes a **hoarding-protection ordenanza** → triggers **1.3c Ordenanza Ratification** (Hold Court gains Ratify/Reject/Amend). ID-only branch, resolved via the 1.3c rule text in the kernel.
- **CLIM-09 / ECON-05 Assessment-lever card** — the locked-high Assessment now biting (shares Assessment-tag lever per §5). ID-only.
- **Grain-unrest Crisis** (GOVFRIC re-familied). ID-only.

**Character engagements:**
- **Hold Court (1 AP) → 1.3c Ordenanza (SC):** Aldric must Ratify / Reject / Amend the hoarding ordenanza — MAJOR ROLL R4 (Amend contest).
- **Keep Order via 1.3b Bind the Cells (1 AP):** to hold Order against grain unrest. Deterministic: partitions Local Actors into 5-household cells with Group Leaders, **Order +1 → O 3→4**. Writes latent Collective Liability exposure.
- **d_sigma:** grain-unrest Crisis response — MAJOR ROLL R5.
- **Mandate feedback:** T = W6·(q/7). q now 0.5·4 + 0.5·3 = 3.5 → T = 3.0 → Mandate = round(7·3/9) = 2. q_s 3.5 ≥1 above Mandate 2 → **PS −1 feedback → PS 3→2** (max ±1/settlement/season). Perverse: the collapsing town is still "above mandate," so the homeostat drains PS instead of granting L.

### MAJOR ROLL R4 — Amend the hoarding ordenanza (dice_pool, 1.3c)
Amend = contest for half-bonus-or-reject. Pool 7D TN 7 vs Guild Master Ob 3 → **P ≈ 48%** (call it ~50%).
**FAILURE trace (depth 3):**
- **L1:** Amend fails → resolves as **Reject at −1**: **Disposition −2 (Guild), Grudge (Guild) written**, no Guild Influence gain. Ordenanza rejected means hoarding stays legally unregulated AND the guild is now hostile.
- **L2:** Operation: the grain guild shifts to obstruction; hoarding continues with no price cap (kernel has no anti-gouging verb — GAP-1/G1 BYZ-4). New content: Intrigue draw-weight rises (Guild Grudge + Clerk Corruption 1 stack); FA — guild can call in the patron-rival network.
- **L3:** Two Grudges now stacked (Local Actors + Guild) → both feed S3 Π and Intrigue. Arc: the hoarder Ambition card is now near-certain to fire as a Crisis. Standing: a second negative-Need resolution Key logged.

### MAJOR ROLL R5 — Grain-unrest Crisis response (d_sigma)
With Bind the Cells Order +1 in hand, advantage +1 → **P ≈ 60%**.
**FAILURE trace (depth 3):**
- **L1:** Unrest not contained. **Order 4→3** (net of the +1 Bind cushion), **PS 2→2** floor pressure. One cell member's infraction fires **Collective Liability tag (Disp −1 whole cell)** — first of the three that stack toward a Cell Revolt.
- **L2:** Operation: Bind the Cells has now inverted from an Order tool into a revolt accelerant (its documented downside). New content: FI opened on the infraction; SC — a censure Petition can cite the cascade Key.
- **L3:** With 1 of 3 Collective Liability stacked, the **Cell Revolt Crisis card** is now armed for S3. Region: Mandate bleed compounds. Arc: revolt-spiral seed.

**Pi_end S2 → S3 start:** clamp(10 + unserved Need 1 + Grudge×2 (2) + Ambition 1 + shock 1 − release 0) = clamp(15) = **10**.
**State end S2:** P1 (famine + locked-high extraction stripping toward subsistence) O4 D1 L4 PS2; Clerk Corruption 1; tags: Grudge×2, Assessment(locked@3, now stale-high vs live 1), Collective Liability ×1; Standing 3.

---

## SEASON 3 — Pi_start 10 (Crisis peak)

Draw = **4 cards**.
**Cards drawn:**
- **Cell Revolt Crisis** (from stacked Collective Liability). ID-only.
- **CLIM-01 famine** (S3 of 3, final shock season). ID-only.
- **3.3b Za Patron-Lapse precursor — "Patron's Rivals Move" Intrigue card** fires (Clerk Corruption + stacked Grudges lifted Intrigue weight enough to draw it): signals Voss's standing is about to drop, giving Aldric a 1-season Treat-verb Bargain window. Intrigue family.
- **Hoarder Ambition Crisis** (EVT-OPP-02-class factional ambition, but at Π10 it lands as Crisis, not the Π≤3 Opportunity form — the low-Π branch data is unreachable here; GAP-1 again).

**Character engagements:**
- **d_sigma:** Cell Revolt Crisis response — MAJOR ROLL R6.
- **§1.0a:** three consecutive negative-Need resolution Keys (S1-S3) now meet the "3 consecutive failures" default Demotion trigger — but w_d HIGH still shields it *as long as Voss stands*. The Patron's-Rivals-Move card means that shield is expiring. Aldric attempts an **Appeal** pre-emptively — MAJOR ROLL R7.
- **Treat (1 AP):** Aldric spends his 3.3b Bargain window trying to shore Voss (stores a Debt chit) — deterministic, partial.

### MAJOR ROLL R6 — Cell Revolt Crisis (d_sigma)
3 Collective Liability now stacked (S2's one + two more from famine-season infractions) → advantage −2 → **P ≈ 30%**.
**FAILURE trace (depth 3):**
- **L1:** Revolt breaks. **Order 4→2** (−2), **PS 2→1** (−1), Prosperity at subsistence floor **1**. "Cell Revolt" Crisis fully realized. Garrison Strength = Def 1×20 + Fort×30 too thin to suppress cleanly.
- **L2:** Operation: Kronmark is now ungovernable at full AP; Keep Order options collapse to Force (PS−) only. New content: FA — the faction's domain-action window shifts defensive (Mandate = Σ L/PS drops hard, substrate §6.3); FI — revolt exposes the hoarder's Debt for a later Investigate.
- **L3:** Region: correlated Cooling famine means sibling towns are near-revolt too; a peninsula-scale unrest arc emerges as the sum of many locally-rational Comply choices (substrate §6). Standing: the revolt is the public-scandal-class input that upgrades the pending Demotion from default −1 toward severe −2. Arc: "the province that starved together."

### MAJOR ROLL R7 — Appeal against pending Demotion (dice_pool, faction-internal Piety/Standing track)
2-season appeal window; contest vs Std-7 adjudicator. Aldric pool ≈ 6D (no relevant bonus dice, Reputation trending 'Weak'), TN 7, vs Ob 4 (Std-7 adjudicator strength) → P(net ≥ 4 on 6D) ≈ **28%**.
**FAILURE trace (depth 3):**
- **L1:** Appeal denied. Demotion stands, timed to the patron-lapse. No stat delta yet; the standing_change is queued to fire at S4 Accounting.
- **L2:** Operation: Aldric governs S4 as a lame-duck; his verbs still cost full AP but his Directives carry a suspicion penalty. New content: SC — the denied appeal writes a Precedent re-weighting his *successor's* legitimacy-Crisis draw (substrate §5.5 S7).
- **L3:** With Voss's standing dropping (3.3b), w_d collapses → the three logged negative-Need Keys (previously shielded) now count as §1.0a sustained Duty-failure → Demotion confirmed. Arc: succession-crisis seed for whoever inherits Kronmark.

**Pi_end S3 → S4 start:** famine shock now ENDS (3-season crop failure complete). clamp(10 + unserved Need 1 + Grudge×2 (2) + Ambition 1 + shock 0 − release 0) = clamp(14) = **10**. (Shock ending doesn't help yet — grudges/ambition saturate it.)
**State end S3:** P1 O2 D1 L4 PS1; Clerk Corruption 1; tags: Grudge×2, Assessment(locked@3, catastrophically stale vs live 1), Collective Liability ×3 (revolt fired), Debt(Voss-Treat chit); Standing 3 → Demotion queued.

---

## SEASON 4 — Pi_start 10 (Crisis, but shock gone)

Draw = **4 cards**.
**Cards drawn:**
- **3.3b Za Patron-Lapse fires at Accounting:** Voss's standing dropped below threshold → Aldric's patronage-charter privileges **lapse automatically, no Quo Warranto** (Intrigue→resolved). This is the trigger event, not a roll.
- **Post-revolt Recovery Petition** (Local Actors, now that shock is gone). Petition family.
- **ECON Assessment-strip card** — the locked@3 Assessment still extracting against a live-1 town (fires every accounting; 1.3a). ID-only.
- **Hoarder consolidation** (Intrigue).

**Character engagements — Standing resolution (deterministic §1.0a, resolution_quality → standing_change bridge):**
- w_d collapses with Voss. The queued Demotion resolves. Magnitude: default is 1 rank (3 consecutive Duty-failures); the S3 public revolt is a public-scandal-class aggravator (−2). Net ruling per §1.0a: **Crown Standing 3 → 2 (Banneret → Crown Agent), one rank**, with the scandal noted but not compounded to −2 because the Appeal, though denied, established a mitigating record (2-season window still open on re-advance). No intermediate pass-through; mentor/Hall/Livery resync within 1 season. **Recognition Fork (1.0b) note:** had Aldric *succeeded*, he sat exactly at the Std-3 Formal Recognition rung where the Confirm(Honryoando)/New-Grant(Shinonkyūyo) fork triggers — famine denied him that fork entirely and instead spent it. His prior Confirm-eased Demotion thresholds (1.0b) are why the drop held at −1 rather than −2. **1.0d Court Attendance did NOT trigger** (requires Std-4+ absentee; Aldric is Std-3) — correctly inert, recorded rather than forced.
- **AP now reduced:** FacilityTier still 1 but patronage-charter lapse strips the Retain-Clerks arrangement (patron-scoped) → back to base AP 3, no Clerk bonus. Clerk Corruption counter frozen at 1.
- **Recovery begins:** Aldric spends AP on Keep Order (Consent, PS+1) and partial relief now that extraction pressure *should* ease — except the Assessment lock still reads 3. He cannot legally lower it for ~5 more seasons.

**No new MAJOR probability roll with real stakes this season** — the season's pivot (patron-lapse + Demotion) is deterministic accounting, and recovery verbs at low Π advantage resolve near-cap. State-writes only.

**Pi_end S4 → S5 start:** clamp(10 + unserved Need 1 + Grudge×2 (2) + Ambition 1 + shock 0 − releases 4 [Consent Keep Order, relief, revolt spent, Petition served]) = clamp(10) = **8**.
**State end S4:** P1→2 (Develop consent) O2→3 D1 L4→5 (q now well below Mandate → L+1 feedback) PS1→2; Standing Crown 2; tags: Grudge×2 (decaying), Assessment(locked@3, still live), Collective Liability cleared post-revolt, Dishonored NOT flagged (drop to 2, membership retained).

---

## SEASON 5 — Pi_start 8 → recompute (mid/high boundary)

**Pi recompute:** carried 8 + unserved Need 1 − releases 4 (sustained relief + consent order + Petition + hoarder Investigate expose) = clamp(5) = **5**. Band MID (3-7) → Petition/Friction/Intrigue. Draw = 1 + floor(5/3) = **2 cards**.

**Cards drawn:**
- **Recovery Petition** (Local Actors seek durable relief / lower assessment). Petition family.
- **Assessment-friction / Fiscal card** — the still-locked@3 base vs recovering-but-capped Prosperity 2. Friction family (1.3a residue).

**Character engagements:**
- **Investigate (1-2 AP):** Aldric finally surfaces the grain-hoarder's black-market Debt (the FI lead opened back in S1) → choose expose. Deterministic-ish; releases Π further, PS+1.
- **Keep Order (Consent, 2 AP, PS+1):** rebuild — MAJOR ROLL R8.
- **Mandate feedback:** q now 0.5·5 + 0.5·2 = 3.5, Mandate ~2-3 → roughly balanced; L holds.

### MAJOR ROLL R8 — Recovery Keep Order (Consent) (d_sigma)
Low-Π, Grudges decaying, advantage +1-2 → **P ≈ 65%**.
**FAILURE trace (depth 3):**
- **L1:** Consent order-build fails: **Order 3→3** (no gain), 2 AP wasted, **PS held 2**. Recovery stalls one season.
- **L2:** Operation: with the Assessment still locked@3, a stalled recovery means the town re-approaches subsistence; the Fiscal Friction card can re-escalate to Crisis if Prosperity dips. New content: Petition-right holder can re-open a stakes.source_key motion citing the stalled-recovery Key.
- **L3:** Region: Kronmark stays a net Mandate drag on the faction; Aldric (now Std-2) has a thinner buffer for a second Demotion. Arc: the "starved town" arc persists into a slow-recovery epilogue rather than closing; successor-legitimacy Precedent from S3 remains live.

**Pi_end S5:** clamp(5 + Need 1 − releases 2) = **4**. Stabilizing.
**State end S5:** P2 O3 D1 L5 PS2; Standing Crown 2 (Crown Agent, re-advance path open); tags: Grudge×2 (decayed), Assessment(locked@3 — the un-expirable trap, ~4 seasons remaining), hoarder exposed (Debt called). Town survived at subsistence; governor demoted one rank; the fiscal lock outlives the crisis that justified opposing it.

## VERDICT
WHAT HELD: The core famine vise (substrate §5.5) resolved faithfully — Need vs Directive with w_d-high shielding, negative resolution_quality Keys accumulating under patron protection, then converting to Demotion when 3.3b Za Patron-Lapse pulled the shield. The Standing bridge, Bind-the-Cells revolt inversion, Clerk-Corruption-to-Intrigue feedback, and the 1.3a locked-assessment fuse all produced a coherent, unauthored 5-season collapse-and-partial-recovery arc ('the governor who fed the war and starved the town'), with the town surviving at subsistence and Aldric demoted exactly one rank. Every ripple routed through one of the 5 substrate primitives (Key/tag/Disposition/Pi/Standing). WHAT BROKE: (1) The deck cannot actually run a Crisis seed — 0 of the matched crisis cards carry branch data; the engine improvised every crisis resolution from the generic C.2 bucket (GAP-1, the most serious finding). (2) 1.3a has no subsistence floor and an ~8-season cooldown, so a lock justified by one season's Prosperity legally strips the town for years after the crisis ends — no player verb reverses it (GAP-7). (3) The protective Compact (OPP-03) is Pi-gated OUT of the exact crisis where it's needed, leaving only the patron-favorable locked-HIGH assessment (GAP-3). (4) No anti-gouging price verb exists during famine (GAP-1/BYZ-4). (5) Mandate is degenerate for a single-settlement holding and the K=6 homeostat perversely drains PS from a collapsing town that is nominally 'above' its own Mandate (GAP-5). Re-litigating the cuts: BYZ-4 (price control) and VEN-SE-4 (Dedizione) are the two rejected proposals that most directly answer live play pressure this seed generated — both were cut for redundancy that famine conditions expose as incomplete; VEN-FA-2 would relieve the AP vise but was correctly cut to preserve it as the intended stress. Net: the standing/ripple substrate is robust; the fiscal-lock (1.3a) and the crisis half of the deck are the two subsystems that fail under load.