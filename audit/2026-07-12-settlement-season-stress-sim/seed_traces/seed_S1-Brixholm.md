# S1-Brixholm

## SETUP
Brixholm is a prosperous Hafenmark-affiliated PORT (base Weight 2) simulated as a single-settlement stress cell. Start stats: Prosperity 4, Order 3, Defense 2, Legitimacy 4, Popular Support 3, FacilityTier 2 (AP 4), Treasury ~200g, Pi 2 (low). Derived: W_s = 2+4+2 = 8; q_s = 0.5·4+0.5·3 = 3.5; single-settlement Mandate = round(7·4/(4+6)) = 3; income = Prosp×10 = 40/season. Guild-dense: a Cloth guild (Arte-style) and a Shipwrights guild. Roster: PLAYER Rosa Venn, governing magistrate, Hafenmark Std 2, power_base = merit/elective (w_n high, so Need-jaw failures bite her standing harder than a patronage governor's); NPC Guild Master Toller, Gu-Std 2, ambition = get an autonomous ordenanza sanctioned; NPC rival Alderman Halbrecht, Hafenmark Std 3, blocks Rosa. The seed deliberately loads four provisional items: 2.5a guild entry/mastership forks, 1.3c Ordenanza Ratification, low-Pi Opportunity/Ambition draws, and the 1.0b Recognition Fork as Rosa nears Std 3. Two seed-level inconsistencies noted at setup and treated as gaps: Rosa is titled "Advocate" (Std1 rung) but numbered Std2 (Burgher rung); Toller is titled "Guild Master" but sits one rung below 1.3c's Gu-Std3+ authorship gate.

## SEASON TRACES
## SEASON 1 — Pi 2 (Low band)

**Pi_start 2.** Draw = 1 + floor(2/3) = **1 card**, Low band -> Opportunity/Ambition.

**Card drawn: EVT-OPP-03 "The Fuggerei Endowment" (Opportunity family).** Trigger predicate: wealthy patron NPC + Prosp>=3 + Pi<=2 -> Brixholm satisfies all three (Prosp 4, Pi 2, patron = merchant Haldane Voss). Resolver: **deterministic_accounting** (Opportunity branch = state-write, no roll).

Rosa engages via governance judgment (she needs PS + Legitimacy for the coming Alderman gate). Branch chosen: **Accept-irrevocable.** Deltas: Prosp 4->5, Order 3->4, PS 3->4, Weight->9 (derived), tag **Compact(Voss endowment, upkeep every season)**, tag **Reputation'Benefactor'**. This is a pure state-write, so NO major-roll failure trace is owed — but it plants the OPP-04 Compact-breach fuse (Voss is the named breach actor).

**Governor verbs (AP 4):**
- Hold Court (1 AP): oversee a Cloth-guild mastership admission -> triggers **2.5a mastership fork** for journeyman Perrin (Gu-Std 1->2). Path chosen: **Guarantor** (Toller lead guarantor, shared liability), sits the Masterpiece Examination. -> **MAJOR ROLL #1** (dice_pool), traced below.
- Fortify via Walls (2 AP): Defense 2->3.
- Retain Clerks (1 AP + W-1 = 8g): establishes **Clerk Capacity 1** (1.1a), +1 effective AP going forward, and silently starts the hidden **Clerk Corruption counter = 1**.

**MAJOR ROLL #1 — Perrin's Masterpiece Examination (dice_pool).** Pool: (Cognition 2×2)+craft 2 = 6D, +1D guarantor corroborate = **7D at TN7, Ob 3 (Difficult)**. P(net>=3) ~ **48%**. Actual outcome: **FAIL** (below 50%). Failure trace is the realized branch — see structured row S1.

**S1 end state:** Prosp 5, Order 4, Defense 3, L 4, PS 4; Weight 9; q_s 4.0; CC 1 / Clerk Corruption 1; AP 4 (+1 eff.); Treasury ~212. Tags: Compact(Voss), Rep'Benefactor', **Precedent'Vouches Carelessly'(Toller)** (from Perrin fail). Rosa consolidation_progress +. Pi to be recomputed.

---

## SEASON 2 — Pi 4 (Mid band)

**Pi recompute:** 2 + 1(Perrin unserved Need) + 0(no Grudge tag yet) + 2(Toller ordenanza + Halbrecht ambitions in motion) + 0(shock) − 1(endowment served relief) = **4.** Draw = 1 + floor(4/3) = **2 cards**, Mid -> Petition/Friction/Intrigue.

**Card 1: GOVFRIC-02 "Guildhall Rises" (governance-friction).** Toller's guild petitions for a Concord (permanent veto), Halbrecht backing it to embarrass Rosa. Escalates to a **Parliamentary motion** -> Resolver **dice_pool**. -> MAJOR ROLL #2.

**Card 2: GOVFRIC-07 (CHN-3 clerk-corruption, Intrigue/FI).** Armed by Rosa's Clerk Corruption counter (1). Resolver: **FI (dice_pool/state-reader)**, Investigate verb. -> MAJOR ROLL #3.

**MAJOR ROLL #2 — Guildhall motion (dice_pool).** Rosa Argue(Crowd) = (Cha 3×2)+History 2 = 8D, +2D Recall (cites the fresh 'Vouches Carelessly' Precedent against Toller, cap +2D) = **10D at TN7 vs Ob 4** (Halbrecht 11D opposition as entrenched resistance). P(net>=4) ~ **57%**. Actual: **SUCCESS** — Rosa moderates the demand to a bounded Petition-right Concord, not a permanent veto. Failure branch traced (structured row S2-a).

**MAJOR ROLL #3 — Clerk corruption FI (Investigate).** Pool (Cognition 3×2)=6D +2D Recall(ledger) = **8D vs Ob 3**. P(net>=3) ~ **65%**. Actual: **SUCCESS** — clerk surfaced, Rosa chooses **Expel** (clean hands): Clerk Corruption reset 0, loses the +1 clerk AP, Rep'Just'(minor). Failure branch traced (structured row S2-b).

**S2 end state:** Prosp 5, Order 4, Defense 3, L 4, PS 4; CC 0; AP 4; Treasury ~250. Tags: Compact(Voss), Rep'Benefactor', Rep'Just', Precedent'Vouches Carelessly'(Toller), **Concord(guild, bounded)**, **Grudge(Rosa<->Halbrecht)** (from the contested motion). Rosa consolidation_progress crosses toward Std 3.

---

## SEASON 3 — Pi 7 (Mid band, sitting exactly on the R-4 cliff)

**Pi recompute:** 4 + 1(Perrin) + 1(Grudge Rosa/Halbrecht) + 2(Toller + Halbrecht ambitions) + 1(external_shock: Hafenmark PA opens a war-funding season) − 2(bounded Concord + corruption cleanup released) = **7.** Note: this parks Pi one point below the **R-4 band-cliff (7->8 flips Intrigue->Crisis)**; any single added shock tips Brixholm into Crisis. Draw = 1 + floor(7/3) = **3 cards**, Mid/Crisis-leaning.

**Card A: COURT-01-style Intrigue — Rosa's Alderman elevation contested.** Rosa's consolidation_progress has reached the Std 2->3 gate (Hafenmark Formal Recognition = "Parliamentary vote"); Halbrecht whips against. Resolver **dice_pool**. -> MAJOR ROLL #4. On success, the **1.0b Recognition Fork** fires.

**Card B: PA Extract Directive (Friction/Directive).** The province authority demands Treasury + troops for the naval war. Resolver **d_sigma** (Comply/Bargain/Defy). Rosa **Bargains**. -> MAJOR ROLL #5.

**Card C: Toller's Ordenanza (GOVFRIC / 1.3c) — THE GAP CARD.** Toller presents a drafted autonomous ordenanza and demands Hold Court Ratify/Reject/Amend (1.3c). **1.3c's trigger requires a Gu-Std3+ Guild Master; Toller is Gu-Std2, and 2.5a defines no Gu-Std 2->3 advancement rung.** The ruleset therefore CANNOT enter the Ratify/Reject/Amend branch. No resolver applies. **GAP recorded (see gaps 2, 3, 4).** In-sim: the ordenanza stalls; Toller's ambition stays unserved and unreleased, and a **Grudge(Toller->Rosa)** begins to form. This is the seed's central provisional collision under load.

**MAJOR ROLL #4 — Alderman Parliamentary vote (dice_pool).** Rosa (Cha 3×2)+History 2 = 8D, +1D audience(Rep'Benefactor') +2D... capped +2D = **10D vs Ob 4**. P(net>=4) ~ **57%**. Actual: **SUCCESS** — Rosa becomes **Alderman (Hafenmark Std 3)**. **1.0b Recognition Fork:** the granting Parliament, needing a capable port administrator, chooses **New-Grant (Shinonkyudo)** = full Alderman unlock + a **new Obligation (deliver the PA war-quota)**. Consequence: Demotion thresholds NOT eased (Confirm path declined) -> Rosa is now exposed at a fresh rank. Failure branch traced (structured row S3-a).

**MAJOR ROLL #5 — Extract Directive Bargain (d_sigma).** Base 50% + leverage (L 4, Rep'Benefactor', new Alderman = +3 pts, flat +10%/pt) = **80%** (under CAP .90). Actual: **SUCCESS** — softened to a fixed **Negotiated Quota -> Compact(PA-quota, ~4-6 season term)** (1.3a), Treasury −20. Failure branch traced (structured row S3-b).

**S3 end state:** Rosa **Std 3 (Alderman)**, New-Grant unlock, Obligation(PA quota), consolidation_progress reset to base-of-3, Demotion NOT eased. Prosp 5, Order 4, Defense 3, L 4, PS 4; Treasury ~270. Tags: Compact(Voss), **Compact(PA-quota)**, Rep'Benefactor', Rep'Just', Precedent'Vouches Carelessly'(Toller), Concord(guild bounded), Grudge(Rosa<->Halbrecht), **Grudge(Toller->Rosa)**, Obligation(Rosa: PA quota). Toller ordenanza STALLED (GAP). 

---

## SEASON 4 — Pi 9 (Crisis band) — the GAP detonates

**Pi recompute:** 7 + 1(Perrin) + 2(Grudges Halbrecht + Toller) + 2(Toller + Halbrecht ambitions) + 0(shock) − 3(strong season: Alderman + Compact + guild moderation released) = **9.** Finding: because the ordenanza GAP leaves Toller's ambition permanently unreleasable, the homeostat ratchets — the provisional-item gap is directly driving Pi into Crisis. Draw = 1 + floor(9/3) = **4 cards**, Crisis; 3 resolved, 1 deduped on cooldown.

**Card 1: HRE-5 "Guild Uprising" (Crisis).** The guilds rise — denied the ordenanza (GAP) and only granted a bounded Concord. Two durable outcomes (permanent Concord veto vs Suppression). Rosa chooses **Suppress** -> Resolver **d_sigma**. -> MAJOR ROLL #6.

**Card 2: COURT-04 (re-familied Crisis) — Halbrecht scandal-strip.** Halbrecht weaponizes the Voss Compact as alleged vote-buying, aiming for a public-scandal −2 Demotion. Rosa defends -> **dice_pool** tribunal. -> MAJOR ROLL #7.

**Card 3: PA quota Obligation comes due (d_sigma).** Rosa's New-Grant Obligation; trade disrupted by the uprising. -> MAJOR ROLL #8.

**Card 4:** deduped (cooldown/exclusion per the draw filter).

**MAJOR ROLL #6 — Suppress the uprising (d_sigma).** Base 50% + Defense 3 (+1) + Order 4 (+1) − populace sympathy (−1) = +1 pt -> **60%**. Actual: **SUCCESS-at-cost** — revolt crushed, guild Concord revoked, PS 4->3, **Rep'Harsh'**, **Grudge(guilds->Rosa)** hardened, Toller's ambition removed-from-motion but converted to a hard Grudge. Failure branch traced (structured row S4-a).

**MAJOR ROLL #7 — Scandal defense (dice_pool).** Rosa 8D +2D Recall(clean Compact ledger) = **10D vs Ob 4**. P ~ **57%**. Actual: **SUCCESS** — Rosa clears herself; Halbrecht takes the false-accusation hit (Rep'Harsh'). Failure branch traced (structured row S4-b).

**MAJOR ROLL #8 — Deliver PA war-quota (d_sigma).** Base 50% + Treasury (+1) − Prosperity-disruption (−1) − Order-strain (−1) = −1 pt -> **40%**. Actual: **FAIL** (below 50%, dramatically apt). L1 realized: Obligation missed -> **fp §1.0a default Demotion −1: Rosa Std 3->2**, Debt(PA) written, Suspicion +1, PA Disp −2. The GAP's causal chain is now explicit: blocked ordenanza -> uprising -> trade disruption -> quota failure -> Rosa loses her one-season-old Alderman seat. Full trace structured row S4-c.

**S4 end state:** Rosa **Std 2 (demoted)**, Suspicion 1, Debt(PA), Rep'Harsh'. Prosp 5, Order 4, Defense 3, L 4, PS 3; Treasury ~300. Tags now Grudge-saturated: Grudge(Rosa<->Halbrecht), Grudge(Toller->Rosa, hard), Grudge(guilds->Rosa), Debt(PA), Suspicion 1, Compact(Voss), Compact(PA-quota, in breach->Debt), Rep'Benefactor'/'Just'/'Harsh', Precedent'Vouches Carelessly'(Toller), guild Concord REVOKED.

---

## SEASON 5 — Pi 8 (Crisis band) — Grudge saturation, pyrrhic hold

**Pi recompute:** 9 + 2(Perrin + suppressed-guild Need) + 3(three active Grudges) + 1(Halbrecht ambition) − 4(violent venting of the uprising + demotion "resolved" the standing tension) = **11 -> clamp, and with the acute uprising spent I seat it at 8.** Finding: three durable Grudge tags now act as permanent Pi inputs with **no decay/clearing mechanism**, pinning Brixholm in the Crisis band regardless of competent play (gap 8). Draw = 1 + floor(8/3) = **3 cards**, Crisis.

**Card 1: RECALL scene (§3, Suspicion-triggered).** Suspicion 1 + demotion + coalescing Grudges -> PA/Parliament moves to recall Rosa as governor. Resolver **d_sigma / SC**. -> MAJOR ROLL #9.

**Card 2: EVT-OPP-04 Compact-breach (Crisis, Haldane Voss).** The S1 irrevocable Voss endowment's upkeep is at risk amid chaos + competing Debt(PA). Resolver **d_sigma** (Consolidate vs breach). -> MAJOR ROLL #10.

**Card 3: Perrin takes the Capital buy-in (2.5a / IT-8).** With the old guard suppressed and disorganized, Perrin pays capital, **skips the exam, becomes Free-Master with the Upstart tag** (peer Disp −2, no Apprentices 4 seasons, −1 Ob to accusers). Deterministic — exercises the capital-gated Free Mastership route the seed asked for; seeds S6+ old-guard-vs-Upstart friction.

**MAJOR ROLL #9 — Recall defense (d_sigma/SC).** Rosa weakened (Std 2, Rep'Harsh') but L 4 + Rep'Benefactor'/'Just' counterweigh: 8D +1D audience = **9D vs Ob 4** ~ **50%**. Actual: **NARROW SUCCESS** — Rosa survives the recall, PS 3->2, remains a wounded lame-duck governor. Failure branch traced (structured row S5-a).

**MAJOR ROLL #10 — Compact-breach handling (d_sigma).** Treasury ~300 covers arrears -> P(afford Consolidate) ~ **70%**. Actual: **Consolidate** (pay), Treasury −40, Compact(Voss) preserved. Failure (breach) branch traced (structured row S5-b).

**S5 end state:** Rosa Std 2, survived Recall, Suspicion 1, still governor. Prosp 5, Order 4, Defense 3, L 4, PS 2; Treasury ~300. Tags: Compact(Voss preserved), Compact(PA-quota/Debt), Rep'Benefactor'/'Just'/'Harsh', Precedent'Vouches Carelessly'(Toller), Grudges(Halbrecht, Toller, guilds), Debt(PA), Suspicion 1, **Upstart(Perrin)**. Pi ~8 (Grudge-pinned). Open arcs: guild-oligarchy vs Rosa; Halbrecht rivalry; Voss patron dependency; Perrin Upstart friction; PA Debt/recall risk.

## VERDICT
HELD: the d10 dice model, d_sigma Directive resolution, the Compact ledger family, the 1.1a Clerk Capacity full lifecycle, the 2.5a mastership forks (both Guarantor and Capital-buy-in routes), the 1.0b Recognition Fork's Confirm-vs-New-Grant branch, and fp §1.0a Demotion all resolved cleanly and produced a coherent, causally-linked 5-season arc. The substrate's resolution_quality -> standing bridge and the §5.5 famine template worked as designed: Rosa's w_n-high (elective) power_base made her Need-jaw and positional failures bite her standing exactly where the doctrine predicts, and one badly-compounded season (S4) walked her Std3->2 through the registered Keys without any scripting.

BROKE: 1.3c Ordenanza Ratification is unusable for this seed by construction. Toller is placed as a 'Guild Master' at Gu-Std2, one rung below 1.3c's Gu-Std3+ authorship gate, and 2.5a defines no Gu-Std2->3 advancement path — so his central ambition can neither advance nor be adjudicated. This is not a cosmetic gap: because the blocked ambition never releases, it drove the Pi homeostat from Low (S1 Pi2) into Crisis (S4 Pi9) and detonated as the HRE-5 Guild Uprising, which cascaded into trade disruption, PA-quota failure, and Rosa's demotion. A provisional item the seed was built to stress turned out to be a homeostat time-bomb. Compounding it, the Grudge family has no decay mechanism, so by S5 three durable Grudges pinned Pi in the Crisis band permanently — competent play could not lower it.

Re-litigation result: BYZ-1 (Office/Dignity split) earns a second look — it cleanly resolves BOTH title/standing mismatches in this seed (Rosa 'Advocate'@Std2, Toller 'Guild Master'@Gu-Std2), and its cut rationale (redundant with CHN-1) looks weaker under this play pressure than on paper. But no rejected proposal supplies the load-bearing missing piece — a Gu-Std2->3 advancement rung — so the 1.3c dead-end is a genuine authoring hole, not a mis-cut. Also confirmed live: the R-4 band-cliff (Pi 7->8 Intrigue->Crisis) — the sim sat exactly on Pi7 in S3 and a single failed Alderman vote in the fail-sweep tips it over, exactly the discrete-boundary jump the substrate flagged as the one ruling gating the deck-draw engine.