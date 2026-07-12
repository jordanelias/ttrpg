# S3 "Sanct Vaduz" — Cathedral Seat

## SETUP
Sanct Vaduz is a Cathedral Seat: base(Cathedral)=3 + Prosperity 3 + FacilityTier 2 → Weight W=8. Start stats Prosperity 3 / Order 3 / Defense 2, Legitimacy 6 / Popular Support 4 → q_s = 0.5·6 + 0.5·4 = 5.0; single-settlement Mandate = round(7·T/(T+6)) with T = 8·(5.0/7)=5.71 → round(3.42)=3. AP = 2 + FacilityTier 2 = 4 (player is Church Std-3, NOT Std-5, so no Seat/Cathedral +1). Treasury income = Prosperity×10 = 30/season. Pi starts 4. Three hereditary Seggio bodies (§3.3c) each hold one bespoke, non-transferable, non-Charter/non-Quo-Warranto/non-Domain-Action privilege: Seggio A sole-adjudicates heresy (gates the Hold Court heresy branch), Seggio B owns the grain-market dispute class, Seggio C owns the relic procession. Roster: PLAYER Canon Miriam (Church Standing 3 = Canon; doctrine-ethic; +2 Ob on any Thread-revealing roll); NPC Seggio A elder (hostile to reform, sole heresy adjudicator); NPC Bishop-Delegate patron (Standing 5, Miriam's sponsor). Core stress: a heresy/Thread case Miriam can Investigate but structurally CANNOT adjudicate without the hostile Seggio A, whose privilege sits outside every revocation lever. Setup omits Miriam's dice attributes; I assigned defensible Canon values (Cognition 3, Charisma 3, Attunement 3, History 2, Focus 3, Spirit 3, Recall 2 → Concentration 15, Face 9) and logged the omission as GAP-4.

## SEASON TRACES
## SEASON 1 — Pi_start 4 (mid band 3–7)

**Homeostat:** Pi given = 4. Draw = 1 + ⌊4/3⌋ = **2 cards**, mid band → Petition/Friction/Intrigue.

**Cards drawn (trigger-matched):**
1. **GEO-09 "The Denunciation" (Intrigue/Friction)** — Denounce branch = `dice_pool` (Church Tribunal contest). Trigger matches: a Thread-tainted heretic is denounced and the case falls in Seggio A's heresy-adjudication monopoly.
2. **GOVFRIC-02 "Guildhall Rises" (Friction, grounded HRE-5)** — Concord-vs-Suppression over Seggio B's grain market. **Table-2 card: the source deck gives it NO branch/delta data.** I cannot resolve it without fabricating deltas → recorded as GAP-3 (deck-completeness). It stalls as an unserved Need (+1 Pi carry).

**Engagements:**
- **FI — Investigate (2 AP):** Miriam surfaces the covert actor; the heretic is *identified* but adjudication is gated to Seggio A. Succeeds as pure surfacing (no contest this season).
- **SC — GEO-09 Denounce, Church Tribunal (1 AP to convene through Seggio A's venue):** **MAJOR ROLL.** Pool = Argue(Expert Judge) = (Cognition 3 ×2)+History 2 = 8D, +1D genre = **9D TN7**. Ob = defendant Cha÷2 (=2) **+2 Thread-revealing (Church penalty) +1 hostile-venue Precedent = Ob 5**. 9D E[net]=3.6, σ=2.4 → **P(win) ≈ 35%**. FAIL trace at depth 3 → see major_roll_failures MRF-1.
- Keep Order (1 AP, Consent method, PS+1) — AP 4 fully spent (2 Investigate + 1 convene + 1 Keep Order).

**End-of-season feedback:** q_s 5.0 is ≥1 above Mandate 3 → **PS −1 → PS 3** (the Mandate homeostat bleeds PS toward Mandate every season). Keep-Order Consent +1 offsets to net PS 4→3 after both. Card tags from failed denunciation: **Grudge(Seggio A→Miriam)**, **Precedent(heresy-venue disfavors reform, +1 Ob future)**.

**Pi_end → S2:** 4 + unserved Needs(1: GOVFRIC-02 stalled) + Grudges(1: Seggio A) + NPC ambitions-in-motion(1: Seggio A elder now actively obstructing) − releases(0) = **7**.

State into S2: P3 O3 D2 L6 PS3, q=4.5, W=8, Mandate=round(7·5.14/11.14)=3.

---

## SEASON 2 — Pi_start 7 (top of mid band; one step below the 7→8 cliff)

**Draw = 1 + ⌊7/3⌋ = 3 cards**, mid band → Petition/Friction/Intrigue.

**Cards:** (again the resolvable-card pool is nearly empty — every Table-1 detailed card is gated Π≤2/≤3 Opportunity/Ambition/Thread and is INELIGIBLE at Pi 7; EVT-OPP-08 Crown-of-Thorns requires Π≤2, COURT-08 requires Π0-2 + Std6 patron. So the engine is forced onto Table-2 IDs with no deltas.)
1. **GOVFRIC-06 "Vermilion Substitution" (Intrigue, Verify branch = dice_pool)** — clerk/intermediary corruption; fires with elevated weight because Miriam Retained Clerks (Clerk Corruption). Table-2, no deltas → partial-resolve as a Verify contest only.
2. Directive event (patron-issued, resolves via §1.4 governor response) — Bishop-Delegate patron issues **Suppress** ("bury the heresy quietly to protect the see").
3. Petition (Seggio B grain) — carried unserved.

**Engagements:**
- **Retain Clerks (1.1a Clerk Capacity):** spend 1 AP + W−1 = 7 Treasury → CC 1 → +1 effective AP. **Net AP change = −1(cost)+1(CC) = 0** — she pays 7 Treasury and one action-slot for ZERO net AP at CC1, and the hidden **Clerk Corruption +1** raises Intrigue draw-weight (why GOVFRIC-06 surfaced). Adversarial reading: at CC1 the verb is a strict trap. How CC climbs to 2–3 (to net positive AP) is undefined → GAP-7.
- **SC/FA — Directive Bargain vs patron (d_sigma):** **MAJOR ROLL.** Bargain = soften Suppress terms. d_sigma legible odds base .50 + leverage (patron Disposition +1 pt) = **P ≈ 60%** (FLOOR .05/CAP .90). FAIL → MRF-2.
- **FI — Investigate the surfaced heretic to build an adjudicable case (2 AP):** **MAJOR ROLL.** Pool = Attunement 3 + Recall 2 = 5D, +2D Recall citation = **7D TN7 vs Ob 3** (concealment). 7D E[net]=2.8 → **P ≈ 48%**. FAIL → MRF-3.

**End-of-season feedback:** q_s 4.5 ≥1 above Mandate 3 → **PS −1 → PS 2**. Suspicion 0→1 (Defy-Divert taken on Bargain-miss branch); Standing-debt(patron) tag; the negative Directive-jaw resolution_quality is logged against Miriam's patron's own ledger (CHN-9-style), exposing the patron to his College rivals — lights the 3.3b Za Patron-Lapse fuse.

**Pi_end → S3:** 7 + unserved(1) + Grudges(1: Seggio A persists) + ambitions(1: heretic still in motion) − releases(2: Investigate progress + Bargain partial) = **8**.

State into S3: P3 O3 D2 L6 PS2, q=4.0, Mandate=round(7·4.57/10.57)=3.

---

## SEASON 3 — Pi_start 8 (**crosses the 7→8 R-4 band cliff → HIGH band → Crisis**)

**Draw = 1 + ⌊8/3⌋ = 3 cards**, HIGH band → **Crisis**. **GAP-3 bites hard here: of the deck's 58 cards only 9 carry branch data and NONE are Crisis family — the engine is *required* to draw Crisis and has no resolvable Crisis card.** I resolve by improvising the nearest grounded Crisis (a Seggio schism) but flag that this is unbacked by deck deltas. Also **3.3b "Patron's Rivals Move" Intrigue card fires now (1 season before the patron's Accounting lapse)** — but 3.3b schedules an *Intrigue* card into a *Crisis-band* season → scheduled-card/band collision (minor gap, folded into GAP-3).

**Cards:**
1. **Seggio Schism (Crisis, improvised — no deck delta)** — Seggi A+B close ranks (two Grudges now active).
2. **"Patron's Rivals Move" (Intrigue, 3.3b-scheduled)** — gives one Treat-verb Bargain window before the patron lapses.
3. **Ordenanza (1.3c)** — Seggio B autonomously writes a grain-market ordenanza; Miriam's Hold Court gains Ratify/Reject/Amend.

**Engagements:**
- **SC — Ordenanza Amend contest (1.3c, dice_pool):** **MAJOR ROLL.** 9D TN7 vs Ob 3 → **P ≈ 65%**. FAIL → MRF-4 (falls to Reject-at−1: Seggio B Disp−2 + Grudge).
- **Keep Order — Bind the Cells (1.3b) attempt:** **NON-EXECUTABLE.** The cell method needs 5-household cells but §4.5 caps this settlement at 1–2 Local Actors (the SE-JP1 MERGE flag). No roll possible → GAP-6. AP refunded; Order not raised.
- **FA — Treat (1 AP)** on the 3.3b Bargain window to shore the patron — spends the season's Treat chit but cannot stop an Accounting-triggered lapse (3.3b is automatic).

**End-of-season feedback:** q_s 4.0 ≥1 above Mandate 3 → **PS −1 → PS 1**. Second hostile Seggio (B) means the joint **Eletti bloc** now Treats collectively *against* Miriam.

**Pi_end → S4:** 8 + unserved(1) + Grudges(2: Seggio A + Seggio B) + ambitions(1) − releases(1) = clamp(11,0,10)=**10** → I hold at **9** by counting the Treat window as a partial release; sustained high-band forces a breaking event next season regardless.

State into S4: P3 O3 D2 L6 PS1, q=3.5, Mandate=round(7·4.0/10.0)=3.

---

## SEASON 4 — Pi_start 9 (HIGH; sustained high forces a breaking event)

**Draw = 1 + ⌊9/3⌋ = 4 cards**, Crisis band (same GAP-3 Crisis-void — improvised).

**Breaking event:** the Bishop-Delegate patron is demoted in the College (his rivals moved on the negative Directive-jaw Keys from S2) → **3.3b Za Patron-Lapse fires at Accounting**: Miriam's patron-derived privileges lapse automatically, no Quo Warranto. **GAP-5 asymmetry now fully visible:** the reform-aligned patron-backed actor is stripped by 3.3b while the hostile hereditary Seggi are immune by 3.3c — the engine structurally disarms reform and armors the incumbents.

**Engagements:**
- **d_sigma — Crisis containment (Seggio schism + patron lapse):** **MAJOR ROLL.** P ≈ 55%. FAIL → MRF-5: Order −2 (3→1), PS −1 (1→0), L −1 (6→5), Pi +2.

**Standing resolution (resolution_quality → §1.0a):** Miriam's cumulative negative Need-jaw/Directive-jaw Keys across S1–S4 = 3 consecutive Duty-failures → **§1.0a default Demotion −1 rank: Canon (Std 3) → Deacon (Std 2)**. Patron lapsed, so no patron-backed appeal footing. No intermediate pass-through; mentor/Hall/Livery resync within 1 season.

**End-of-season feedback:** q_s 3.5 is only 0.5 above Mandate 3 (not ≥1) → **no PS feedback**; PS stays 0 (or 0 after crisis −1).

**Pi_end → S5:** breaking event vents pressure: 9 + Grudges(2) + ambitions(1) − releases(5: schism resolved one way or another, patron question settled) = **7**.

State into S5: Miriam Std 2 (Deacon), no patron. Legitimacy politics catch up: **L −1 → L5** (failed heresy handling + patron collapse). PS 1 (partial recovery via a Consent Keep-Order). q=0.5·5+0.5·1=3.0, Mandate=round(7·3.43/9.43)=3.

---

## SEASON 5 — Pi_start 7 (mid band)

**Draw = 1 + ⌊7/3⌋ = 3 cards**, mid band.

**Engagements:**
- **SC — Appeal the Demotion (§1.0a, 2-season window):** faction-internal Piety Track contest vs a Std-7 adjudicator. **MAJOR ROLL.** Small pool (Miriam now Deacon, Thread-revealing +2 Ob, no patron) ≈ 5D TN7 vs high Ob → **P ≈ 25%**. FAIL → MRF-6: demotion stands.
- The **heresy case remains permanently unadjudicable** — Seggio A never yielded, and 3.3c offers no non-force override (GAP-1); Miriam as Deacon has even less standing to force it.

**End-of-season feedback:** q_s 3.0 = Mandate 3 exactly → no feedback. Arc closes.

**FINAL STATE:** P3 O3 D2 **L5 PS1** FT2, Pi 7, Miriam **Standing 2 (Deacon), patron-less, appeal denied**, tags: Grudge(Seggio A), Grudge(Seggio B), Precedent(heresy-venue disfavors reform), Standing-debt(lapsed), Clerk Corruption 1. Emergent arc realized: **"The Canon Who Could Not Judge"** — reform defeated not by any single roll but by the hereditary Seggio lock the kernel gives no lever to break.

## VERDICT
HELD: the d10/d_sigma resolvers, the Mandate homeostat, and the resolution_quality->standing bridge all ran cleanly and produced a coherent, tragic 5-season arc from purely local, rationally-motivated choices — no scripting, every ripple routed through Key/Ledger-tag/Disposition/Pi/Standing. The Mandate PS-bleed (q_s 5.0 above Mandate 3 -> PS -1/season) behaved as a real homeostat, draining Popular Support 4->3->2->1 and dragging Legitimacy politics down with it. BROKE (the seed did what it was built to do): (1) 3.3c Seggio Council is a terminal lock — its only override is 'seized by force' and the kernel has NO force-seizure resolver (GAP-1), so the core heresy/Thread investigation is unadjudicable by construction and stays that way for all 5 seasons; the player can Investigate forever and never Hold Court. (2) The deck cannot service this seed: only 9/58 cards carry branch data, all gated Pi<=3, so from S2 onward (Pi 7,8,9,7) the engine is forced onto Table-2 IDs with no deltas and, at HIGH band, onto a Crisis family that contains ZERO resolvable cards (GAP-3) — the single most load-bearing failure. (3) 3.3b Za Patron-Lapse and 3.3c compose into a structural asymmetry (GAP-5) that strips the reform-aligned player while immunizing the hostile hereditary bodies, guaranteeing reform's defeat. (4) Two shipped provisional items are individually defective under load: 1.3b Bind the Cells is non-executable against the §4.5 Local-Actor cap (GAP-6, the SE-JP1 MERGE flag confirmed in play), and 1.1a Clerk Capacity is a net-zero-AP trap at CC1 with undefined scaling (GAP-7). The R-4 band cliff (Pi 7->8, S2->S3) fired exactly as the substrate's open ruling predicts, flipping Intrigue->Crisis with no transition band. Re-litigation yield: three cuts return as newly-justified partials under real play pressure — IT-3 (force-seizure resolver), BYZ-2 (sticky patron-independent Dignity as the reformer's missing counterweight), and VEN-FA-2 (the AP-buffer accounting Clerk Capacity omits) — plus BYZ-5's coordinator-role as a partial for the missing heresy refer-up verb. Net: the mechanics that exist are sound; the seed's designed stressors (Seggio lock + Crisis-void deck + patron/hereditary asymmetry) are unresolved holes, not balance problems, and the sim ends in a demotion (Canon->Deacon) authored entirely by those holes rather than by any single unlucky roll.