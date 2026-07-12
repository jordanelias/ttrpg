# S2 "Dunmark" — frontier Fortress, contested border, hard Extract Directive under war pressure

## SETUP
Dunmark is a frontier Fortress (base Weight 2) on a contested border, starting Prosperity 2 / Order 2 (restive) / Defense 4 / Legitimacy 3 / Popular Support 2, FacilityTier 1 (AP=3), Treasury ~60g, Pi 5. Derived: Weight W = base(2)+Prosp(2)+FacTier(1) = 5; q_s = 0.5·L + 0.5·PS = 2.5; single-settlement Mandate contribution ≈ 2 (T=5·2.5/7=1.786; round(7·1.786/7.786)=2); faction income = Prosp×10 = 20g/season. Roster: PLAYER Banneret Aldric Vos (Crown Standing 3, power_base = Crown-appointed → w_d high in the resolution_quality vise); an NPC Crown envoy/Minister issuing an Extract Directive (troops + coin for a border war); an NPC militia captain of doubtful loyalty. Latent: restive Local Actors, a rumored smuggling ring. The seed is built to load the Directive fork (Comply/Bargain/Defy-Divert), the Levy verb + Negotiate-Quota→Compact substrate (§1.3a), Bind the Cells (§1.3b) with Collective-Liability/Cell-Revolt stacking, mid-Pi Petition/Friction/Intrigue draws, and Suspicion accumulation on Defy → Recall.

## SEASON TRACES

# S2 "Dunmark" — 5-Season Trace

State carried forward every season. Standing ladder: Crown (Petitioner0→Retainer1→Crown Agent2→**Banneret3**→Crown Lieutenant4→Seneschal5→…). d_sigma = clamp(0.50 + 0.10·net_adv, .05, .90). dice_pool odds read from the TN7 table.

---

## SEASON 1 — "The Envoy's Ask"
**Pi_start = 5** (given, mid band). Draw = 1 + ⌊5/3⌋ = **2 cards**, mid band → Petition/Friction/Intrigue.
**Central event (not a card, a §1.4 Directive):** Crown envoy issues **Extract Directive** (troops + coin for the war).

**Cards drawn:**
- **GOVFRIC-01** *(Governance Friction / Friction)* — smuggling-corridor friction (route/corridor lever, AT-RISK per §5). Matches trigger: rumored ring + frontier corridor.
- **A Petition** *(Petition family)* — restive Local Actors' grievance over the coming levy (Order 2, restive).

**Engagements:**
- **FA/Directive response (SC contest — Bargain):** Aldric declines straight Comply (stripping a border fortress's Defense is suicidal) and **Bargains** vs the envoy to soften terms.
  - *MAJOR ROLL 1 — Bargain, dice_pool.* Pool = (Cha3×2)+History2 = **8D TN7**, Ob = envoy Cha5÷2 = **3**. **P(net≥3) = 57%.**
  - **Actual outcome: SUCCESS.** Terms softened → coin only, troops waived. Treasury 60→**40**, Defense held **4**, Order 2→**1** (partial levy strain), PS held **2**. resolution_quality mildly positive (served Directive + protected the Need/Defense jaw) → consolidation_progress toward Crown Lieutenant, no rank change.
  - **FAILURE TRACE (swept regardless) — see major_roll_failures S1 Bargain.**
- **Levy verb + §1.3a Negotiate Quota → Compact:** Aldric tries to lock the war-extraction figure into an **Encabezamiento Compact** so future levies read a fixed base, not live Prosperity.
  - *MAJOR ROLL 2 — Negotiate Quota, d_sigma.* Leverage: low Treasury + restive settlement = net_adv −1 → **P = 40%.**
  - **Actual outcome: FAILURE.** No Compact tag written; the war-levy stays ad-hoc/recurring. PS 2→**1**. (Failure trace = major_roll_failures S1 Negotiate.)
- **FI — smuggling ring (GOVFRIC-01):** Aldric spends AP to **Investigate**.
  - *MAJOR ROLL 3 — Investigate, FI dice_pool.* Pool = Attunement+Recall ≈ **6D TN7**, Ob **2**. **P(≥2) = 63%.**
  - **Actual outcome: SUCCESS.** Ring surfaced; Aldric chooses **co-opt** → **Debt tag** (smugglers owe intel/revenue), latent Order risk.
- **Petition:** resolved at **Hold Court** (1 AP, deterministic) → **Precedent** ("levy-relief promised").

**AP spend:** Bargain(SC, free-ish)/Investigate 1 + Hold Court 1 + Keep-Order-adjacent 1 = 3/3.
**Pi recompute → S2:** 5 + Needs(+1 relief) + Grudges(+1 partial-levy) + Ambitions(+1 captain; smuggling co-opted, neutral) + shock(+1 war) − releases(−3: Bargain served Directive-Need, ring co-opted, court eased Petition) = **6**.
**End S1:** Prosp2 Order1 Def4 L3 PS1 · Treasury40 · Suspicion0 · Tags: Grudge(partial-levy), Debt(co-opted smugglers), Precedent(levy-relief). **Pi_end = 6.**

---

## SEASON 2 — "Binding the Cells"
**Pi_start = 6** (mid). Draw = 1 + ⌊6/3⌋ = **3 cards**, mid band.

**Cards drawn:**
- **GOVFRIC-07** *(Friction/Intrigue; CHN-3 corrupt-clerk precedent)* — surfaces because Aldric retains a clerk this season (Clerk Corruption).
- **A Petition** — restive-actor grievance recurs (Order still 1).
- **"Patron's Rivals Move" (sl §3.3b Za-lapse Intrigue)** — drawn but **no Za/guild patron is established at Dunmark → predicate unmet → card whiffs/re-shuffled.** (Recorded: deck can deal a card whose precondition the settlement cannot satisfy — see GAP A.)

**Engagements:**
- **Keep Order — §1.3b Bind the Cells (1 AP):** Order 1→**2**; partitions Local Actors into 5-household collective-liability cells with Group Leaders. **COLLISION (GAP C):** a frontier Fortress holds only 1–2 Local Actors (§4.5 cap) → cannot populate 5-household cells. Provisional item is ACTIVE so the engine forces it, treating garrison rank-and-file + townsfolk as the cell substrate — **but this is non-executable as written.** Begins **Collective Liability** tracking.
- **Retain Clerks — §1.1a Clerk Capacity (1 AP + W−1 = 1AP + 4g):** buys CC1 → +1 effective AP, but this season nets **0 AP** (spend 1, gain 1) and raises the hidden **Clerk Corruption** counter → +Intrigue draw-weight. (Opacity = GAP E.)
- **FI — cell infraction:** the co-opted smugglers slip a shipment; an Investigate confirms it → **1st Collective Liability stack** written (whole cell Disp −1). Deterministic write, no major roll.
- **Petition** eased at Hold Court under the levy-relief Precedent (deterministic).

**Pi recompute → S3:** 6 + Needs(+1 relief) + Grudges(+2: cells resented + prior) + Ambitions(+1 captain) + shock(+1) − releases(−4: Bind strongly suppresses, Order+1) = **7**.
**End S2:** Prosp2 Order2 Def4 L3 PS1 · Treasury ~56 · Suspicion0 · CC1 (Clerk Corruption+1) · Collective-Liability ×1 · **Pi_end = 7** (sitting on the R-4 band cliff).

---

## SEASON 3 — "Defiance on the Wall"
**Pi_start = 7** (mid band, top edge — the R-4 7→8 Intrigue/Crisis cliff is one tick away). Draw = 1 + ⌊7/3⌋ = **3 cards**.

**Central event:** the war intensifies → envoy issues a **second Extract Directive** (more troops).

**Cards drawn:**
- **GOVFRIC-06** *(Friction/Intrigue, "Vermilion Substitution"; Verify branch = dice_pool, WIRED)* — the doubtful militia captain substitutes a harsher order than Aldric issued (CHN-7 Chancellery-Gatekeeper shape).
- **An Intrigue** — clerk skims (from S2 Clerk Corruption counter firing).
- **A Petition** — cell resentment.

**Engagements:**
- **Directive → Defy-Divert (0 AP):** Aldric refuses to strip the wall again. **Standing-debt** incurred + **Suspicion 0→1**; PS 1→**2** (protects populace), Local-Actor Disposition +; Defense held **4**. (Defy is a choice, not a roll — but note §5 scores it as maximally negative on the Directive jaw = GAP F.)
- **SC/FI — Verify the captain (GOVFRIC-06 Verify):**
  - *MAJOR ROLL 4 — Verify, dice_pool.* ≈ **7D TN7**, Ob **2**. **P(≥2) ≈ 69%.**
  - **Actual outcome: FAILURE.** Captain's harsher substitution stands; Order 2→**1**; troops' Grudge; a contested second exchange pushes **Suspicion 1→2**. (Full failure trace = major_roll_failures S3.)
- **Cell infraction #2:** a Group Leader defies the levy-Defiance fallout → **2nd Collective Liability stack.**

**Pi recompute → S4:** 7 + Needs(+2: Defy left Crown-Need unserved + relief) + Grudges(+1 cells) + Ambitions(+1 captain emboldened) + shock(+1) − releases(−4: Defy protected settlement, some pressure vented via PS+) = **8**.
**End S3:** Prosp2 Order1 Def4 L3 PS2 · **Suspicion2** · Standing-debt logged · Collective-Liability ×2 · **Pi_end = 8** — **crosses the R-4 cliff into the Crisis band.**

---

## SEASON 4 — "The Wall Eats the Town" (Crisis)
**Pi_start = 8** (HIGH band → Crisis). Draw = 1 + ⌊8/3⌋ = **3 cards**, Crisis-weighted.

**Cards drawn (Crisis family):**
- **CELL REVOLT** *(Crisis)* — the **3rd Collective Liability stack** lands (a cell member's extraction-resentment infraction) → the §1.3b "3 stacked → Cell Revolt Crisis" trigger fires.
- **A Suspicion→Recall trigger** — a third Directive this season is Defied again (**Suspicion 2→3**), crossing the Recall threshold → **Recall scene** convenes.
- **An Intrigue** — the militia captain positions to fill any command vacuum.

**Engagements — two crises stack:**
- **Cell Revolt — Suppress (d_sigma):**
  - *MAJOR ROLL 5 — Suppress, d_sigma.* Garrison leverage net_adv +1 → **P = 60%.**
  - **Actual outcome: FAILURE.** Revolt spreads: Order 1→**0**, PS 2→**0** (−2), Defense 4→**3** (garrison turned inward), L 3→**2**; **Reputation → Hated**, Grudge stacks. (Failure trace = major_roll_failures S4 Suppress.)
- **Recall scene — Defend the seat (SC dice_pool):**
  - *MAJOR ROLL 6 — Recall defense, dice_pool.* Rattled-penalized from the crisis → ≈ **6D TN7**, Ob **3**. **P(net≥3) = 40%.**
  - **Actual outcome: FAILURE.** Aldric is **recalled.** resolution_quality catastrophically negative on **both** jaws (defied the Directive AND lost the settlement) → §1.0a **Severe demotion, public scandal −2**: **Banneret(3) → Retainer(1)** (no intermediate pass-through; mentor/Hall/Livery resync within 1 season). Debt(ally) called.

**Pi recompute → S5:** 8 + Needs(+1) + Grudges(+2 revolt aftermath) + Ambitions(+1 captain) + shock(+1) − releases(−6: forceful suppression + Recall removes the flashpoint governor) = **7**.
**End S4:** Prosp2 Order0 Def3 L2 PS0 · Reputation(Hated) · Aldric Standing **1 (Retainer)** · seat vacated · **Pi_end = 7.**

---

## SEASON 5 — "The Banner Unmade"
**Pi_start = 7** (mid). Draw = 1 + ⌊7/3⌋ = **3 cards**.

**Cards drawn:**
- **An Intrigue** — the militia captain / a rival consolidates de facto command of the under-Ordered fortress.
- **An Opportunity** *(Ambition-adjacent)* — a successor's legitimacy play (predicate: vacated seat, low q_s).
- **A Petition** — the co-opted-then-abandoned smugglers petition/defect.

**Engagements:**
- **Appeal (§1.0a, 2-season window) — faction-internal Piety Track contest vs Std-7 adjudicator (dice_pool):**
  - *MAJOR ROLL 7 — Appeal, dice_pool.* Small pool vs a Std-7 adjudicator → ≈ **5D TN7**, Ob **4**. **P ≈ 22%.**
  - **Actual outcome: FAILURE.** Demotion to Retainer(1) **stands**; Dishonored-adjacent flag; no further appeal. (Failure trace = major_roll_failures S5.)
- **Arc payoff (emergent, unauthored sum):** Dunmark — disarmed-by-extraction (S1), suppressed-then-revolted (S2→S4), leaderless (S4) — passes to whoever holds it: the disloyal captain and the defecting smugglers now anchor an enemy-leaning border pocket. **Region power shift ratified.** Arc **"The Banner That Broke the Border"** closes and seeds the successor's legitimacy-Crisis draw (§5.5 Precedent-on-successor pattern).

**End S5:** Dunmark effectively lost as a reliable Crown hold; Aldric Retainer(1), re-advance only via Initiation Gates. **Pi_end = 7.**

---

### Pi arc summary: 5 → 6 → 7 → **8 (R-4 cliff crossed → Crisis)** → 7. Standing arc: Banneret(3) held through S3, −2 Severe at S4 → Retainer(1), Appeal fails S5.


## VERDICT
HELD: the core d10/pool odds, the Directive fork, the Pi homeostat + Pi-weighted draw, the Ledger tag families, and the resolution_quality -> Standing -> Demotion bridge all resolved cleanly and produced a coherent, unauthored downfall arc ('The Banner That Broke the Border') — a governor who was locally rational at every step (Bargain to save the wall, Defy to protect the town, Suppress the revolt) yet demoted from Banneret to Retainer, with the fortress lost to the region. The §5.5 Kronmark template ported exactly: w_d-high protected Aldric from the S1 Need-jaw failure, then failed him at the S4 dual-jaw collapse. The R-4 band cliff (Pi 7->8) fired as a real, load-bearing threshold, converting accumulated mid-Pi Friction into a forced Crisis — evidence the cliff IS a dramatic feature, not just a modeling wart, though still a ruling-gated finding.\n\nBROKE / STRAINED: (1) The deck is hollow — 49 of 58 cards have no branch data, so every mid-Pi Friction/Intrigue draw had to be resolved by generic resolver-bucket, not card content; and the deck dealt a precondition-unsatisfiable card (Za-lapse with no patron) with no whiff rule. (2) Bind the Cells is non-executable on this settlement: §1.3b's 5-household cells collide with §4.5's 1-2 Local-Actor cap, yet the whole Cell-Revolt escalation (the seed's marquee stress) depends on it — I had to force it. (3) Suspicion->Recall runs on an undefined threshold; the entire Recall outcome rested on fiat values. (4) Compact-vs-Directive precedence and (5) Clerk Capacity AP accounting are both underspecified enough to make state indeterminate. (6) resolution_quality structurally mis-scores a sanctioned Defy as Duty-failure, double-punishing a blessed verb.\n\nRE-LITIGATION SIGNAL: four cut proposals earned a 'partial' under real load — VEN-SE-7 (Sindici Inquisitori) is the sharpest, since its roving Pi-suppression floor is exactly what Bind-the-Cells' deliberate Pi suppression was built to evade; VEN-FA-2 (Ducal Chancellery) cleanly specifies the AP-buffer that its winning rival CHN-3 leaves ambiguous; VEN-SE-4 (Dedizione) and HAB-2 (Valido) each patch a live precedence/scoring gap. None was a clean 'yes' — but four cuts look under-tested against this seed, and two live-canon collisions (deck emptiness, Cell/actor-cap) are not fillable by any rejected proposal and need in-PR fixes.