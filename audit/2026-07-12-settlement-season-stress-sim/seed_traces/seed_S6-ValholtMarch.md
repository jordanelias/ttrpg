# S6 "Valholt March" (3-settlement territory, single player-governor, cross-scale Mandate + AP-triage + adversarial-Directive stress)

## SETUP
Valholt March is a 3-settlement Varfell territory under one governor, Lendmann Sigrid (Std 4). Valholt (Seat: P4/O3/D3/L4/PS4/FacTier2 → W9, q4, AP4, Π3) anchors the March; Nedre (Town: P2/O2/D1/L3/PS3/FacTier1 → W5, q3, AP3, Π5) is struggling; Kolstad (Village: P1/O2/D1/L2/PS2/FacTier0 → W2, q2, AP2, Π6) is poor and near the crisis band. Starting Mandate = clamp(round(7·T/(T+6))) with T=Σ W·(q/7)=7.86 → Mandate 4. Territory Treasury income = Σ Prosperity×10 = 70. Two hereditary Seggi are recognized at the Valholt Seat (sl §3.3c): one sole-adjudicates commercial disputes, one gates the Fortify-Walls method. Faction pressure arrives as a recurring cross-settlement Directive from Sigrid's Varfell patron-Jarl (Extract/Suppress) that forces trading one settlement's welfare for another; an ambitious reeve in Nedre is an NPC ambition-in-motion feeding Π. Note: the seed labels Sigrid "Lendmann Std4," but the Varfell ladder places Lendmann at Std3 (Land-Grant) and Hersir at Std4 — treated as Std4/Hersir-tier titled Lendmann, one rank below the Jarl (Std5) Recognized-Deed fork.

## SEASON TRACES
## SEASON 1 — "The Locked Bargain"

**Π start:** Valholt 3, Nedre 5, Kolstad 6 (seed values). Bands: all three MID (3–7) → dramatic band (Petition/Friction/Intrigue). **Draw counts** = 1+⌊Π/3⌋: Valholt 2, Nedre 2, Kolstad 3 (7 cards — already a territory-scale volume problem for one player, see GAP-7).

**Cards drawn (real deck IDs, matched to state):**
- Valholt: GOVFRIC-02 *Guildhall Rises* (Governance-Friction); + a minor Petition (folded into "AP not spent on growth").
- Nedre: COURT-02 (Court/Standing, first-playable Demotion-resolver slice) — the reeve petitions for office; + GOVFRIC card.
- Kolstad: a CLIM subsistence-friction card (StockLevel-low, Kolstad P1); + the cross-settlement **Extract Directive**; + ECON-02 (Debt→Outlawed, first-playable).

**Spine — the adversarial Directive.** The patron-Jarl issues an **Extract** Directive over the March (levy grain+troops for the faction war footing). Complying strips the two poor settlements. Sigrid responds **Bargain** (§1.4) — a social contest vs the PA to soften the open-ended extraction into a fixed-term **Compact / Encabezamiento** (gp §1.3a Negotiate-Quota method + HAB-5), locking extraction at a sustainable level for a 4-season term.

- **MAJOR ROLL S1-1 — Bargain (dice_pool, social contest).** Pool: (Cognition×2)+History ≈ 6D, +2D Recall citation (cites the March's assessed capacity) → **8D, TN7**, Ob = Jarl Cha÷2 ≈ 3. **P(≥3 net) ≈ 57%** (reference table 8D). **Resolved: SUCCESS (marginal)** → Compact tag written on the March (fires every season, term 4), extraction locked moderate; Kolstad partly shielded. *Failure branch traced below (row S1-1).*

**Other resolutions (deterministic verbs):**
- Kolstad: **Develop (Treasury method, 2AP)** → Prosperity 1→2 (W 2→3), serving the subsistence card; consumes ALL Kolstad AP (triage bite: no AP left for Order).
- Nedre: **Hold Court (1AP)** on the reeve → Precedent(reeve-managed); reeve ambition persists (feeds Π).
- Valholt: **Retain Clerks (1AP + W−1=8 Treasury)** → Clerk Capacity CC1 (+1 effective AP next season) and starts a hidden **Clerk Corruption** counter (gp §1.1a); **Sponsor (1AP)** a Seggio ally → Def 3→4 + Disposition + Debt tag. 2 AP unspent (maintenance).

**Π end:** Valholt 3→2 (served), Nedre 5 (reeve ambition offsets Hold-Court release), Kolstad 6→5 (famine need served).
**Mandate end:** q V4/N3/K2; W V9/N5/K3 → T=8.14 → **Mandate 4** (unchanged). L-feedback (q ≥1 below Mandate 4): Nedre L3→4, Kolstad L2→3. **Standing:** Sigrid Std4, Rep'—', Compact & Clerk-Corruption(1) live.

---

## SEASON 2 — "The Endowment and the Diverted Directive"

**Π recompute:** Valholt 2 (Clerk Corruption raises Intrigue *draw-weight*, not Π); Nedre 5+1(reeve)=6; Kolstad 5+1(Compact fires/strips)=6.
**Draw counts:** Valholt Π2 → **LOW band** → 1 card, Opportunity/Ambition; Nedre 3; Kolstad 3.

**Cards drawn:**
- Valholt: **EVT-OPP-03** *Fuggerei/Pliny endowment* (Opportunity) — trigger met (wealthy patron NPC + Prosp≥3 + Π≤2). Resolver: **deterministic_accounting** (no roll).
- Nedre: an **Ordenanza** written autonomously by a Nedre guild master (gp §1.3c); + reeve friction.
- Kolstad: Compact-strip friction + a Keep-Order-pressure card.

**Resolutions:**
- Valholt OPP-03 **Accept-irrevocable**: Prosp 4→5, Order 3→4, PS 4→5, FacilityTier 2→3 (the card's "Weight+1"), **W 9→11**, beneficial Compact-forever + Rep'Benefactor'. (Note: had S1 Developed Valholt, Prosperity would have hit the illegal 6 — the 0–5 cap forced S1 to spend Valholt AP on Sponsor/Clerks instead, a real cap-driven sequencing constraint.) AP next season → 2+3 = 5.
- **Directive #2 = Suppress** (Jarl orders the reeve's Nedre faction crushed). Sigrid **Defy-Divert** (§1.4, 0 AP): protects Nedre/reeve → Nedre PS 3→4, reeve Disposition+, but **Standing-debt +1 and Suspicion +1** (→1). (Defy is deterministic — no contest.) All three Directive responses now exercised: Bargain(S1)/Defy(S2)/Comply(S3).
- **MAJOR ROLL S2-1 — Amend the ordenanza (dice_pool, Hold Court §1.3c Amend branch, 1AP).** Pool ≈ **7D, TN7**, Ob = guild-master Cha÷2 ≈ 3. **P(≥3 net) ≈ 48%** (interpolated 6D/8D). **Resolved: SUCCESS (marginal)** → Amend passes, half the ordenanza's bonus applied, no Grudge, Guild Influence flat. *Failure branch traced (row S2-1).*
- Kolstad: **Bind the Cells (Keep Order method, 1AP)** → Order 2→3, forms 5-household cells with a Collective-Liability regime (gp §1.3b) — a cheap-order seed that becomes a Cell-Revolt time-bomb. **AP TRIAGE BITE:** she wanted to also **Survey** (2AP, to lock assessed_base) but Kolstad's 2 AP can't cover Bind(1)+Survey(2)=3 → Survey deferred; the Compact stays the only extraction anchor, and it is not re-based to Kolstad's declining Prosperity (the gp §1.3a stale-figure hazard now armed).

**Π end:** Valholt 2, Nedre 6, Kolstad 6.
**Mandate end:** q V4.5/N4/K2.5; W V11/N5/K3 → T=11.0 → **Mandate 5** (rises — Valholt's endowment boom lifts the whole territory; the Weight-11 Seat dominates). L-feedback (≥1 below 5): Nedre L4→5, Kolstad L3→4. **FINDING:** the periphery's fate is invisible here — Mandate rose purely on the Seat.

---

## SEASON 3 — "Comply and Starve" (the substrate §5.5 pattern, live)

**Π recompute:** Valholt 2; Nedre 6+1(reeve)=7; Kolstad 6+1(Compact strip)+1(Collective-Liability friction)=**8 → CRISIS band**.
**Draw counts:** Valholt 1 (LOW/Opp, but Clerk-Corruption re-weights toward Intrigue); Nedre 3; Kolstad Π8 → 1+2=3 (CRISIS).

**Cards drawn:**
- Kolstad: **CLIM Famine Crisis** (StockLevel-low + external shock, Kolstad P2) — the exact §5.5 shape.
- Valholt: Clerk-Corruption flips the low-band draw into an **Intrigue** ("clerk skims/extorts").
- Nedre: reeve-simmer + Keep-Order card.

**Spine — the famine vise.** Simultaneously the Jarl issues **Extract** again (Directive #3). The §3 vise is live: Need=relief vs Directive=extract, insufficient AP/Treasury for both. Sigrid's positional vector: appointed/patronage-seated → **w_d high**; defying spends the Jarl's capital. She is Weight-rational (Kolstad W3 vs a Mandate-5 she just earned) and **Complies** — extracts, leaves relief unserved. This is the substrate's "affordable given power_base, not given the event."

- **MAJOR ROLL S3-1 — Kolstad famine containment via Keep Order/Force (d_sigma).** Leverage = Garrison Strength (Def1×20 + Fort0×30 = 20) vs entrenched hunger-unrest; legible ≈ **P 50%** (d_sigma flat, FLOOR .05/CAP .90). **Resolved: FAILURE** — the designed collapse. *Depth-3 trace, row S3-1.* Result: Kolstad Order 3→1, Prosperity 2→1, PS 2→1, L 4→3, Grudge(populace), Collective-Liability cells all trip (Cell-Revolt flag), **Π 8→9, W 3→2.** The stale Compact now strips a P1 settlement (gp §1.3a below-subsistence hazard REALIZED).
- **MAJOR ROLL S3-2 — Investigate the Valholt clerks (dice_pool FI).** Pool Attunement+Recall ≈ **6D, TN7**, Ob = concealment 2. **P(≥2) ≈ 63%.** **Resolved: SUCCESS** → skim exposed, Clerk Corruption reset to 0 (loses the CC AP-source). *Failure branch traced, row S3-2.*
- Nedre: Keep Order (Consent, 2AP) → Order 2→3, PS 4→5; Hold Court (1AP) on reeve — holds the line.

**Π end:** Valholt 2, Nedre 7, Kolstad 9 (revolt zone).
**Mandate end:** q V4.5/N5/K2; W V11/N5/K2 → T=11.21 → **Mandate 5 (HOLDS).** **HEADLINE FINDING:** Kolstad in open revolt (Order 1, PS 1, below subsistence) moved territory-T by only −0.5, absorbed by rounding and offset by Nedre's L-feedback. The Mandate cannot see the revolt. Worse: L-feedback (Mandate 5, K q2 ≥1 below) pushes **Kolstad L 3→4** even as it burns — Legitimacy auto-inflates while PS craters, so q(Kolstad)=2.5 *masks* the collapse from the aggregation. The real cross-scale signal that propagated was the **resolution_quality Key (strongly negative Need-jaw)** → logged Duty-failure, NOT the Mandate.

---

## SEASON 4 — "Recall, Revolt, and the Two-Rank Fall"

**Π recompute:** Valholt 2→3 (governor under scrutiny); Nedre 7; Kolstad 9+1(revolt)=**10**.
**Draw counts:** Valholt 1; Nedre 3; Kolstad Π10 → 1+3=4 (CRISIS).

**Cards drawn:**
- Kolstad: **Cell Revolt Crisis** (gp §1.3b — 3 stacked Collective Liability).
- The accountability event: Suspicion(1) + the famine mishandling trip a **Recall scene** (§1.4) fused with the **Court Attendance obligation** (fp §1.0c/1.0d — Std-4+ absentee governor of 3 settlements). Skip → Suspicion ×2; she must attend.
- Nedre: reeve watching for weakness.

**Spine — Sigrid answers for the March.**
- **MAJOR ROLL S4-1 — Court/Recall defense (dice_pool).** She fights to frame Kolstad as "served the Jarl's Extract" (w_d protection, per §5.5 S4) rather than "public scandal." Pool (Charisma×2)+History ≈ 6D, +2D citation (Extract compliance), −? for Suspicion → ≈ **8D, TN7**, Ob = Senior-Jarl (Std7) adjudicator Cha÷2 ≈ 4. **P(≥4 net) ≈ 44%.** **Resolved: FAILURE** — the "public scandal" framing (a Cell Revolt is loud) sticks → **Severe Demotion −2 (fp §1.0a): Sigrid Std4 → Std2 (Thane).** No intermediate pass-through; Hall/Livery/Mentor resync within 1 season; Appeal window opens (2 seasons). *Depth-3, row S4-1.*
- **MAJOR ROLL S4-2 — Suppress the Cell Revolt (d_sigma).** Almost no AP (Kolstad 2), revolt entrenched, Garrison 20 vs high Ob → **P ≈ 35%.** **Resolved: FAILURE** → Kolstad Order 1→0, PS 1→0, **secedes / goes Outlawed (HRE-6-class); removed from the March.** Precedent(secession)+permanent Grudge. *Depth-3, row S4-2.*

**Π end:** Valholt 3, Nedre 7, Kolstad LOST.
**Mandate end (2 settlements):** q V4.5/N5; W V11/N5 → T=10.64 → **Mandate 5 → 4.** Even TOTAL LOSS of a settlement drops Mandate only one step — and that step is the *removal* of a small positive contribution, not any negative "drag." A dead settlement contributes 0; it cannot pull Mandate down. L-feedback (Mandate 4, N q5 ≥1 above) → **Nedre PS 5→4** (over-served penalty). **Standing:** Sigrid Std2, Dishonored-adjacent flag, Appeal pending.

---

## SEASON 5 — "The Dissolution of the March"

**Π recompute:** Valholt 3→4 (Std2 governor holding a Seat = legitimacy crisis); Nedre 7+1(reeve, emboldened by a demoted governor)=**8 → CRISIS**.
**Draw counts:** Valholt 1–2; Nedre 3.

**Cards drawn:**
- Nedre: reeve's bid (Crisis-band Intrigue/defection) + a **Za Patron-Lapse** "Patron's Rivals Move" Intrigue (sl §3.3b): a Nedre guild whose patron was a Seggio noble weakened by Sigrid's own demotion sees privileges lapse at next Accounting — the reeve's bloc absorbs the freed clients.
- Valholt: legitimacy-friction (Std2 anomaly).

**Spine — two doomed high-stakes rolls.**
- **MAJOR ROLL S5-1 — Appeal the Demotion (dice_pool, Varfell Pragmatism-track vs Std-7 adjudicator).** Weakened pool ≈ **6D, TN7**, Ob ≈ 4. **P(≥4 net) ≈ 30%.** **Resolved: FAILURE** → Appeal denied, Std2 stands, window closes, no further internal remedy. *Depth-3, row S5-1.* (Note: the ruleset specifies the Appeal as a "faction-internal **Piety** Track" contest — undefined for Varfell; substituted Pragmatism. See GAP-5.)
- **MAJOR ROLL S5-2 — Reeve's bid for Nedre (dice_pool).** Sigrid (Std2, weak) vs rising reeve. Pool ≈ **5D, TN7**, Ob ≈ 4. **P(≥4 net) ≈ 20%.** **Resolved: FAILURE** → reeve seizes effective control of Nedre; Nedre Order 3→2, reeve faction PS+, Grudge(Sigrid). *Depth-3, row S5-2.*

**Π end:** Valholt 4, Nedre reeve-held.
**Mandate end (effectively Valholt only):** q V4.5; W V11 → T=7.07 → **Mandate 4.** The March, reduced from 3 settlements to a single contested Seat, holds Mandate 4 — the SAME as the 3-settlement start. Over five seasons the Mandate walked 4→4→5→5→4→4 while the territory lost two settlements to revolt/defection and its governor fell two ranks and failed her appeal. **The Mandate aggregation transmitted almost none of it.**

**Provisional items under load this run:** Compact/Encabezamiento (S1 create, S2–S4 fire, S3 stale-strip); Clerk Capacity + hidden Corruption (S1 retain, S3 Intrigue detonation & FI); Bind the Cells → Collective Liability → Cell Revolt (S2→S4); Ordenanza Ratification Amend (S2); Locked-Extraction/Survey AP-triage block (S2); Directive Bargain/Defy/Comply (S1/S2/S3); Recognition/Demotion −2 + Appeal (S4/S5); Court Attendance/Performance Audit (S4); Za Patron-Lapse (S5); Seggio Council obstruction (throughout, GAP-4). The Recognition **Fork** (fp §1.0b, Confirm-vs-New-Grant) never triggered — the arc ran toward demotion, not a Recognized Deed, so the fork was armed but never exercised.

## VERDICT
WHAT HELD: The core resolvers all ran cleanly — d_sigma Directives, dice_pool contests, and FI checks each resolved with legible, reference-table-grounded odds, and every card routed through exactly one ratified resolver (no new engine invented in-play). The §1.4 Comply/Bargain/Defy Directive machinery, the Compact/Locked-Extraction substrate, Clerk Capacity, Bind-the-Cells→Cell-Revolt, Ordenanza Amend, and the fp §1.0a Demotion+Appeal ladder all took load and produced coherent, traceable state. The substrate's resolution_quality→standing bridge worked exactly as the §5.5 famine trace predicts: w_d-high (patronage-seated) Sigrid Complied with Extract and starved Kolstad WITHOUT immediate demotion, and the negative Need-jaw Key propagated correctly into FI (grain-hoarder), SC (censure via stakes.source_key), and FA (domain-action window) consumers.

WHAT BROKE — THE HEADLINE: The seed's designed stress, 'cross-scale ripple where one settlement collapse drags Mandate down,' is substantially REFUTED for a low-Weight settlement. Because Mandate = clamp(round(7T/(T+6))) is a saturating, Weight-weighted function dominated by the Seat (W11 vs W2-3), Kolstad's full arc — revolt, secession, below-subsistence — moved territory-T by ~0.5 and the rounded Mandate not at all (it held at 5 through the collapse). Over five seasons the territory lost TWO of three settlements and its governor fell two ranks and failed her appeal, while Mandate walked 4→4→5→5→4→4. Worse, the L-feedback loop (§1.8) ACTIVELY inflated the dying settlement's Legitimacy (Kolstad L 3→4 while in open revolt), so q masked the collapse from the very aggregation meant to detect it. The real cross-scale carrier was NOT the Mandate but the Standing/resolution_quality Key and the ledger tags (Grudge, Precedent, secession) — the substrate's Key bridge transmitted the collapse; the Mandate aggregation was too coarse and too Seat-dominated to. Design implication: peripheral collapse must be surfaced through Standing/Accord/tag channels, not Mandate, OR Mandate needs a floor/penalty term for settlements below subsistence so a burning village is visible in the number.

SECONDARY BREAKS: AP triage genuinely bit (Kolstad's 2AP could not cover Bind+Survey, forcing the stale-Compact hazard) — but ONLY because the single-governor/multi-settlement AP economy (GAP-1) is undefined; the whole triage premise rests on an unspecified rule. The mid-band deck (GAP-2) is where all three settlements lived and is exactly where the deck has no branch data — the most-played band is the least-specified. Seggio obstruction (GAP-4) and the non-Church Appeal track (GAP-5) both dead-ended the ruleset. Net: the mechanics that resolve individual events are solid; the cross-scale AGGREGATION and the territory-scale governor economy are the fragile, under-specified surfaces this seed exposed.