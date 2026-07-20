# S5 "Eisgrund" — Mine Outpost, Varfell, patron-lapse cascade stress

## SETUP
Eisgrund is a Mine Outpost (base(Type)=1) starting Prosperity 3, Order 2, Defense 2, Legitimacy 2, Popular Support 3, FacilityTier 0 (→ AP=2, no augment), Pi 4; W_s = 1+3+0 = 4, q_s = 0.5·2+0.5·3 = 2.5. A Za-style guild charter (sl §3.3b) runs the miners' guild; the charter's patron field points at a Standing-5 Varfell Jarl whose seat is precarious (a rival Jarl is circling). Roster: PLAYER Thane Bjorn (Varfell Standing 3, pragmatism-ethic, power_base ≈ merit/measurable so w_n-leaning — poorly shielded on the Downward jaw); NPC guild head (existentially dependent on the charter); NPC rival Jarl (moving against the patron). The design intent under load: sl §3.3b Za patron-lapse (auto-lapse at next Accounting if patron drops below threshold, with a "Patron's Rivals Move" Intrigue firing one season prior opening a Treat-verb Bargain window), the 2-AP triage economy, and the charter-lapse cascade. All PR#119 provisional items ACTIVE.

## SEASON TRACES
## SEASON 1 — Pi_start 4 (mid band 3–7), draw 1+⌊4/3⌋ = 2 cards

**Cards drawn (mid → Petition/Friction/Intrigue):**
1. **Patron's Rivals Move** (Intrigue family, sl §3.3b) — the designed one-season-prior warning. Predicate matches: charter patron field = precarious Std-5 Jarl. Opens a Treat-verb Bargain window.
2. **GOVFRIC-01 / Boschi Publici Requisition** (Friction/Directive family, VEN-SE-2 grounding) — an Extract Directive from the province tied to Eisgrund's named ore-production dependency.

**Character engagements (AP=2):**
- Bjorn → **Treat (1 AP)** on card 1: negotiate a bridging side-deal to hedge the charter against the failing patron (Treat verb → Chits stored as Debt tag).
- Bjorn → **Directive-Bargain (reactive)** on card 2: social contest vs the PA to soften the requisition quota.
- Bjorn → **Investigate (1 AP)** the rival Jarl's covert backing (expose/expel/co-opt/shelter fork).

**MAJOR rolls:**
- Treat-Bargain — dice_pool, ~6D TN7, Ob 2 (rival pressure Ob 3 − Varfell pragmatism/measurable −1). **P(≥2 net) ≈ 63%** → SUCCESS. Writes a **Debt (bridging hedge)** tag.
- Directive-Bargain — d_sigma (ED-874, +10%/pt, FLOOR.05/CAP.90), Bjorn Std3 with patron still nominally backing ≈ +1 net pt → **P ≈ 60%** → SUCCESS. Writes a **Compact** tag (HAB-5 Encabezamiento: fixed-term extraction below live capacity); PS 3→2.
- Investigate — FI dice_pool, ~5D TN7, Ob 2. **P(≥2 net) ≈ 54%** → **FAIL taken.** (fail trace in structured rows). Rival not surfaced; **Grudge (rival Jarl)** written.

**End S1:** Prosperity 3, Order 2, Defense 2, L 2, PS 2. Tags: Debt(hedge), Compact(active), Grudge(rival). Mandate feedback SKIPPED — single-settlement Mandate is degenerate (see gaps). 
**Pi update:** 4 + Needs(guild-security unserved +1) + Grudges(rival +1) + NPC ambitions(rival Jarl +1, guild head stirring +1 = +2) + shock(0) − releases(Compact/Debt defused Directive −1) = **7** → Pi_start S2 = 7 (mid-band top; one nudge from the R-4 Crisis cliff).

---
## SEASON 2 — Pi_start 7 (mid top), draw 1+⌊7/3⌋ = 3 cards — THE ACCOUNTING

External resolver fires first: **patron-survival roll** (d_sigma at faction scale; Bjorn's S1 counter failed, rivals Std-5-backed with momentum). **P(patron survives) ≈ 35%** → FAIL → **charter AUTO-LAPSES at Accounting** (sl §3.3b, "no Quo Warranto needed"). This is the designed cascade detonation.

**Cards drawn (mid):**
1. **Za Patron-Lapse Accounting** (Intrigue→cascade, sl §3.3b).
2. **GOVFRIC-02 / Guildhall Rises** (Friction, Consent-Rule lever).
3. **COURT-02** (Petition, Hold Court dispute over now-uncharter ed guild privileges).

**Character engagements (AP=2):**
- Bjorn → **Sponsor guild (2 AP)** responding to card 1: durable +1 Prosperity + Disposition, writes a **Debt(Bjorn owes)** tag. The S1 Debt(hedge) FIRES here, softening the lapse. AP now EXHAUSTED.
- Cards 2 and 3 get **NO AP** → forced-triage failures (structural).

**MAJOR roll:** patron-survival (above), FAIL taken → cascade.
Sponsor is deterministic (no roll): lapse Prosperity 3→2, Sponsor +1 → net 3; Weight momentarily 4→3→4.
Card 2 unfunded → adverse: Order 2→1, standing Guild-Influence/Grudge claim.
Card 3 unfunded → dispute unadjudicated: no Precedent, disputant Grudge, unserved Need.

**End S2:** Prosperity 3, Order 1, Defense 2, L 2, PS 2. **CHARTER LAPSED.** Tags: Compact(active), Grudge(rival), Grudge(guild), Debt(Bjorn/Sponsor). Bjorn spent his entire season treading water.
**Pi update:** 7 + Needs(miners livelihood +1, court +1 = +2) + Grudges(rival +1, guild +1 = +2) + ambitions(rival ascendant +1, guild head unmoored/defection-risk +1 = +2) + shock(lapse aftermath +1) − releases(Sponsor stabilized −1) = 13 → clamp **10** → Pi_start S3 = 10. **CRISIS.** R-4 band cliff realized: 7 → pinned 10.

---
## SEASON 3 — Pi_start 10 (HIGH/Crisis), draw 1+⌊10/3⌋ = 4 cards

**Cards drawn (Crisis-weighted):**
1. **Guild-Head Defection** (Crisis/defection — the unmoored NPC defects to the rival Jarl).
2. **GEO-04 / Severed Enclave** (Crisis — rival pressure severs the ore route).
3. **XSCALE-01** (Crisis — flagged Demotion-Magnitude cascade-STACKING at high Pi).
4. **Miners' Revolt** (Crisis — sustained-high-Pi breaking event; Order 1).

**Character engagements (AP=2) — triage 4 crises with 2 AP:**
- Bjorn → **Treat/co-opt guild head (1 AP)** to prevent defection.
- Bjorn → **Keep Order — Force (1 AP)**: Order +1, PS −1 (brittle).
- Cards 2 and 3 UNFUNDED → adverse.

**MAJOR rolls:**
- Retain guild head — dice_pool ~6D, Ob 3 (Std-5 counter-bid − Varfell −1 → still 3 vs entrenched offer). **P(≥3 net) ≈ 40%** → **FAIL taken** → guild head DEFECTS (fail trace in rows).
- Keep Order-Force — d_sigma, Order 1 but Force reliable ≈ **P 65%** → SUCCESS (Order 1→2, PS 2→1); fail-trace logged in rows.
- Card 2 (Severed Enclave) unfunded: Prosperity −1 → 1; the **Compact's locked assessed_base now exceeds live Prosperity 1** — gp §1.3a stale-high Assessment hazard → **Compact breach pending** (bonds to OPP-04).
- Card 3 (XSCALE-01) unfunded: simultaneous negative Keys (charter lapse + defection + Compact breach) STACK → Demotion-Magnitude escalation input.

**End S3:** Prosperity 1, Order 2, Defense 2, L 2, PS 1. Bjorn **DEMOTED Std 3→2** (fp §1.0a default 1-rank: Disposition decline + ~3rd consecutive negative resolution_quality season; title "Thane" now matches Std 2). Tags: + Grudge(guild-head), rival foothold-in-settlement, Compact-breach-pending, Reputation drift(Harsh).
**Pi update:** 10 + Needs(+3) + Grudges(+3) + ambitions(rival+foothold +1) + shock(Compact breach +1) − releases(revolt suppressed −1, defection resolved one ambition −1) = 16 → clamp **10** → Pi_start S4 = 10. Pinned Crisis — no circuit-breaker (see gaps).

---
## SEASON 4 — Pi_start 10 (Crisis pinned), draw 4 cards

**Cards drawn (Crisis):**
1. **OPP-04 / Compact-breach Crisis** (Prosperity 1 < locked assessed_base; gp §1.3a).
2. **Miners' Revolt round 2** (PS 1).
3. **Rival Jarl Domain Action** (FA — rival converts his foothold into a formal claim; faction_politics consumes-edge da_outcome window).
4. **GEO-04 Severed Enclave persists.**

Note: fp §1.0d Patron-Sponsored Performance Audit **auto-lapsed** — its sponsoring patron vacated in S2, so that Downward-jaw Recall pressure evaporated (coherent silver lining).

**Character engagements (AP=2):**
- Bjorn → **Contest rival domain action (1 AP, SC)**.
- Bjorn → **Keep Order — Bind the Cells (1 AP, gp §1.3b)**: Order +1 (2→3), partitions actors into 5-household cells with Collective Liability tags.
- Cards 1 and 4 UNFUNDED → Compact breaches; enclave persists.

**MAJOR roll:**
- Contest rival domain action — dice_pool ~5D, Ob 3 (rival Std5 entrenched − Varfell −1... still 3). **P(≥3 net) ≈ 31%** → **FAIL taken** → rival gains a formal ore-revenue claim over Eisgrund (fail trace in rows).
- Bind the Cells — deterministic Order +1; risk: 3 stacked Collective Liability → future Cell Revolt.

**End S4:** Prosperity 1, Order 3, Defense 2, L 2, PS 1. Bjorn Std 2 (Demotion-to-1 now pending). Tags: + rival Precedent+claim, Collective-Liability ×cells, Compact BREACHED (tag cleared, Grudge written). Dual-authority squeeze maxes the Positional vector.
**Pi update:** 10 + Needs(+3) + Grudges(+3) + ambitions(rival +1) − releases(Bind Cells −1, Compact ended −1) = 15 → clamp **10** → Pi_start S5 = 10. Still pinned.

---
## SEASON 5 — Pi_start 10 (Crisis pinned), draw 4 cards — DENOUEMENT

**Cards drawn (Crisis):**
1. **Demotion/Appeal Scene** (fp §1.0a — accumulated negative resolution_quality triggers formal Demotion proceeding; 2-season Appeal window, faction-internal contest vs Std-7 adjudicator).
2. **Cell Revolt** (gp §1.3b — 3 stacked Collective Liability from S4 fires).
3. **Rival Sovereignty Bid** (rival attempts to convert foothold/claim into control) — NO ratified card/verb covers this (GAP → IT-3).
4. **Subsistence Collapse** (Prosperity 1 + stale Assessment) — NO rule for below-subsistence (GAP).

**Character engagements (AP=2):**
- Bjorn → **Appeal the Demotion (1 AP-equivalent, dice_pool vs Std-7 adjudicator)**.
- Bjorn → **Keep Order (1 AP)** on Cell Revolt.
- Cards 3 and 4 UNFUNDED.

**MAJOR rolls:**
- Appeal — dice_pool ~5D, Ob 4 (Std-7 adjudicator − Varfell −1). **P(≥4 net) ≈ 20%** → **FAIL taken** → **Bjorn Std 2→1 (Thane→Huscarl)**; membership retained, re-advance via Initiation Gates (fail trace in rows).
- Cell-Revolt Keep Order — d_sigma, Order 3 but Collective-Liability drag ≈ **P 55%** → SUCCESS (barely holds); fail-trace logged in rows.
- Card 3 unfunded → rival consolidates unopposed; Card 4 unfunded → subsistence floor breached with no defined engine consequence.

**End S5 (terminal):** Prosperity 1, Order 3, Defense 2, L 2, PS 1→0. Bjorn **Std 1 (Huscarl)**, Eisgrund's ore economy captured by the rival Jarl bloc, charter permanently lapsed. The tragic arc "the pragmatic thane who inherited a patron's doom" — Std 3 → Std 1, mine captured — completed, authored by no single event but the cascade the seed was built to produce.

## VERDICT
HELD: The seed's designed cascade fired exactly as engineered. sl 3.3b Za patron-lapse worked mechanically end-to-end - the 'Patron's Rivals Move' Intrigue gave a real S1 Treat-verb Bargain window, the S2 Accounting auto-lapsed the charter on the patron's fall, and every downstream ripple routed through registered substrate Keys (faction_politics consumes-edge for Mandate bleed and the rival domain-action window; stakes.source_key for the seeded Petition/legitimacy contests; resolution_quality -> fp 1.0a for Bjorn's Std 3->2->1 slide). The Compact/Assessment substrate (gp 1.3a + HAB-5), Bind the Cells (gp 1.3b), and the Demotion ladder all behaved. The R-4 band cliff is REAL and dangerous: Pi crossed 7->10 at S2 and PINNED at 10 for three seasons, a self-sustaining death spiral.

BROKE (structurally, not by bad luck): (1) The 2-AP FacilityTier-0 economy cannot service a 4-card Crisis draw, and the only AP-relief lever (Clerk Capacity) is a dead-end at CC0 - triage was forced failure, re-litigating VEN-FA-2's cut. (2) No Pi circuit-breaker exists once past the cliff. (3) gp 1.3a explicitly threatens 'below subsistence' but no engine defines that terminal state. (4) IT-3 (The Sforza Gambit) was cut as 'not yet earned,' yet play produced its exact end-state - a rival converting an economic foothold into settlement control with no resolver to cover it: the strongest re-litigation of the 14 cuts. (5) Re-patroning a lapsed charter and revoking a hardened 3.3c privilege both lack any non-force path this kernel can resolve. (6) Single-settlement Mandate feedback is degenerate. Net: the provisional items are individually sound but their INTERACTION under a real cascade exposes a missing emergence layer (IT-3-shaped) and a missing high-Pi/low-AP relief valve - both previously judged 'not this pass,' both now under demonstrated load.