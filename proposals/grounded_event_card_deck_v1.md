# Grounded Event-Card Deck — Breadth Pass Across All Four Research Dockets

## Status: PROPOSED (2026-07-11) · Lane: IN (cross-cutting; SE, FA) · Author-pass, not yet Jordan-ratified

**What this is.** The actual event-deck content the four research passes were for: 58 grounded cards
spanning all four dockets (`2026-07-09-comparative-governance-research`, `2026-07-10-historical-concerns-
action-catalogue`, `2026-07-11-rise-to-power-roster-system-research`, `2026-07-11-proactive-governance-
scale-research`) and all seven card families, each **complete with impacts** and bound to the governance
ripple substrate (`designs/architecture/governance_ripple_substrate_v1.md`). Every card names its
historical grounding, trigger predicate, scale_signature, response branches with concrete stat/tag deltas
and a §5 resolution_quality signal, three-vector burden, honestly-graded FI/SC/FA ripples, and a named
follow-on arc actor.

**Method.** A 15-agent Workflow — 7 thematic generators spanning all four dockets (climatic/geographical,
geopolitical, economic, court/standing, proactive-opportunity, governance-friction, cross-scale/peninsula)
→ an **independent objective adversarial critic** per cluster (default-CUT, six verifiable gates: grounding
authenticity, the substrate §9 read/write-dependency test, Ω-d non-dominance, duplicate/reskin,
completeness, lever discipline; never saw the generator's reasoning) → an Opus 4.8 max-effort deck synthesis
with honest cut/keep + cross-cluster-pattern + AT-RISK + provenance-breadth accounting.

**Critic result (stated honestly).** 59 cards generated; **40 KEEP / 19 REVISE / 0 CUT** (the one merge —
COURT-07 — was differentiated rather than cut, → 58). Zero cuts is flagged, not celebrated: every card
cleared the four §10 gates and the 19 REVISE defects were narrowly fixable (18 dependency/overclaim — mostly
FA claims that moved a stat which does *not* feed Mandate, corrected to route through a real L/PS/Standing
driver — and 1 Ω-d), corrected inline. A 0-CUT rate on an adversarial default-CUT pass is a soft signal the
critic under-applied its stance at the margin; the cross-cluster synthesis (§4 below) supplies the harder
cuts the per-cluster critic structurally could not see (the GEO-04/XSCALE-08 near-duplicate, the three-card
severance suite, family imbalance).

---

## Architecture compliance — §14.4 of the substrate, applied to the deck

The substrate's §14.4 is a binding gate: no card is *implementable* until it carries (a) an owning module +
resolver from the fixed enum, (b) registry-valid Key types for everything it emits/consumes with any gap
surfaced as a finding, and (c) a resolution-diagnostic P-i…P-v verdict for any draw. This section applies
that gate to the whole deck. It **classifies by resolver/module bucket** (the compliance facts are shared,
not 58 bespoke analyses) and **surfaces every contract delta as a finding** — it does **not** silently edit
`references/module_contracts.yaml` (a `valoria-module-adjudicator` ratification step, gated on the rulings +
Jordan sign-off, and the registry's own discipline forbids silent edge-normalization).

### C.1 · The draw — one engine for the whole deck
Every card is drawn by the same Π-weighted event-table engine. Its resolution-diagnostic verdict is done
once, in substrate **§14.2**: PASS on P-i (band) / P-ii / P-iv / P-v, with **one P-iii FINDING** (the
discrete band cliffs, Π 7→8 flips Intrigue→Crisis) = ruling **R-4**. Classified by inspection, no card's
response branches introduce a *bespoke* roll — all route to an existing resolver (C.2) — so the deck needs
**no per-card draw diagnostic beyond §14.2**.

### C.2 · Card resolution — three ratified resolvers, zero new engines
Each card's response branches resolve through one of three already-ratified resolver-enum members
(classified by the branch's impact shape; the definitive per-card assignment is the C.5 adjudicator step):

| Resolution shape | Resolver (enum) | Where in the deck | Status |
|---|---|---|---|
| Governor-verb / Directive choice (Comply/Bargain/Defy, Sponsor, Levy, Fortify, Hold Court) | **`d_sigma`** (`domain_actions`; ED-874 — legible odds, flat +10%/pt uniform leverage, FAIL_FLOOR .97 graded) | the bulk of Crisis/Friction/Petition branches | RATIFIED |
| Pure state-write (an Opportunity/Ambition that writes Prosperity/Order/Treasury directly) | **`deterministic_accounting`** (`settlement_layer`) | most Opportunity/Ambition branches | RATIFIED |
| A branch that *is itself a contest* (Denounce→Tribunal, Verify→up-tier, a Parliament motion) | **`dice_pool`** (`social_contest`, 5–18D "keep dice") | GEO-09 Denounce, GOVFRIC-06 Verify, ECON-03/06 Parliament, several COURT branches | RATIFIED |

→ **Every card resolution is a legal IN→resolver→OUT on an existing resolver; no card invents a new engine.**
This confirms, across the whole deck, the substrate §14.1 finding that the response branches need no new resolver.

### C.3 · Key types — registered vs. findings-to-surface
- **REGISTERED (legal today):** the standing-bridge OUT `state.standing_change` (already emitted by
  `faction_politics`, in-contract); resolution Keys `da_outcome.*` / `scene.*_resolved`; env shocks
  `env.disaster` / `env.peninsular_strain_shock`; the Mandate rollup (the `settlement_layer` §1.8 derivation).
  The **resolution_quality signal rides the existing Key `impact_vector`** — **no new Key type** (substrate §14).
- **FINDINGS TO SURFACE (new edges, not silently added):** (1) the `faction_politics ← settlement-resolution`
  consumes-edge (the §5 bridge); (2) the five lever state-rows on `settlement_layer` (R-1); (3) the
  `social_contest` `stakes.source_key` consumes-edge (the AT-RISK SC hook — ~50 cards depend on it); (4) the
  PROPOSED Ledger families (Outlawed, Capital-Posture, Compact) invoked by GOVFRIC-08/XSCALE-02/ECON-01/04 and
  the Compact cards — surface for family ratification. **No card introduced a wholly new Key *type*** — all use
  registered families or already-PROPOSED ones.

### C.4 · The one new engine to ratify
The Π-weighted deck-draw engine (§14.2), tagged `[NEW ENGINE — surface for canon ratification]`, carrying the
single P-iii band-cliff finding (R-4). C.1/C.2 confirm no card resolution introduces a *second* new engine.

### C.5 · What remains — the module-adjudicator execution step
Full per-card **A1–A12 contract transcription** (`valoria-module-adjudicator`, `contract_adjudicator.py`) is
the EXECUTION step: it edits `module_contracts.yaml` to land the C.3 edges, and is gated on R-1/R-2/R-4 +
Jordan sign-off. It is deliberately **not** done here — silent contract edits violate the registry's
visible-findings rule. This appendix has done the *classification* and surfaced every delta; the adjudicator
run lands the edges once the rulings are made.

### C.6 · Compliance verdict
- **Architecture shape — COMPLIANT.** Every card is a legal IN→resolver→OUT; zero new resolution engines; the
  one new engine (the draw) is diagnosed with a single ruling attached.
- **Resolution diagnostic — APPLIED.** The draw passes 4/5 P-properties; one P-iii finding (R-4).
- **Module contracts — CLASSIFIED + FINDINGS SURFACED, no silent edits.** The adjudicator execution and the
  R-1/R-2/R-3/R-4 rulings are the gating follow-ups; nothing here is authored into `module_contracts.yaml`.

**Net:** the deck is delivered as *implementable mechanics in correct code-architecture shape* — not design
sketches — with the resolution diagnostic run on its one new engine and every module-contract delta surfaced
as an adjudicator finding rather than an asserted or silently-committed change.

---

branch armed if the multi-turn build minted a provisional Treasury shortfall during construction.
- **Scale:** personal|settlement.
- **Branches:**
  - **Dedicate it to the city** — inaugurate the works in the settlement's name, on-budget: Prosperity +1, Defense +1 (drought/siege resilience), Order +1, Π -1, Treasury -0; Precedent 'officeholder delivered major infra' on the regime (not the person). *Signal:* a durable public good delivered above demanded → instrumental (+) and traditional (+).
  - **Inscribe your own name on the arches** — claim the credit personally (the Appius move): Prosperity +1, Defense +1, L +1 (to the officeholder), rival officeholders Disp -1, Treasury -0; Reputation 'Builder' on the character + Grudge(rivals). *Signal:* Need positive but credit captured personally rather than for the regime → strong hierarchical (+) for the individual, ambiguous downward.
  - **Defer the overrun** — open the works now, phase the contractor's final payment: Prosperity +1, Defense +1 now; Treasury retained but Debt(settlement) fires each future call; Π +1 deferred; latent Precedent 'officeholders may stretch budget for infra'. *Signal:* Need positive, fiscal prudence below demanded → instrumental (-).
- **Three-vector burden:** Positional — the decision is credit-allocation and fiscal timing, not whether to build. A patronage-seated governor who inscribes personally risks the patron expecting the glory; a merit/bureaucratic governor benefits most from the completion Key routing toward advancement (w_d high), so 'dedicate to the city' is the affordable answer that still feeds their standing.
- **Ripples:** FI **WIRED** (the defer/overrun branch raises concealment inventory — the contractor who skimmed the overrun becomes discoverable carrying the settlement's Debt; CHN-3 shape). SC **AT-RISK** (the completion Key becomes a citable predicate — the officeholder's own advancement motion, or on the Debt branch a rival's overspend-Censure; needs stakes.source_key). FA **real via Mandate** (the personal-credit branch moves **L +1** — an L/PS input to Mandate — opening a faction expansion/Sponsor window).
- **Follow-on:** An audit-or-honor arc around master-engineer Corvin Vask: on the defer branch his skimmed overrun ripens into an FI lead; on the dedicate branch his craft-Reputation seeds a follow-up Great-Work petition (O11).
- **New lever:** **none** — Prosperity/Defense/Order/Treasury + Debt/Precedent/Reputation; per S1 the Aqueduct is a Develop sub-option riding existing stats.

---

#### EVT-OPP-03 — The Perpetual Endowment (Opportunity) **[REVISED]**
- **Grounding:** Jakob Fugger's Fuggerei (Augsburg, 1521) — irrevocable almshousing at a fixed nominal rent, un-renegotiable in perpetuity; paired with Pliny the Younger endowing Comum's library/baths/teacher's salary — docket S12 + S3. (The Compact family's flagship case, ED-SE-0019.)
- **Trigger:** exists wealthy patron NPC (high Weight/Treasury) AND settlement.Prosperity ≥3 (a poor population to house) AND Π≤2; the patron proactively offers to found a perpetual charitable institution.
- **Scale:** personal|settlement.
- **Branches:**
  - **Accept the irrevocable terms** — the endowment stands forever: Prosperity +1, Order +1 (permanent, non-decaying), **PS +1 [REVISED — added]**, founder Weight +1; settlement Treasury -0 (patron-funded); Compact binding ALL future administrators to the fixed terms (never renegotiable) + founder Reputation 'Benefactor'. *Signal:* a durable welfare institution delivered above demanded → strong traditional (+) and instrumental (+).
  - **Accept but reserve renegotiation** — take it as a revocable grant: Prosperity +1, Order +1, **PS +1 [REVISED — added]** now but decays unless re-Sponsored; patron Disp -2 (insulted). *Signal:* delivered positive but weaker and you wronged the giver → instrumental (+), upward jaw (-) (patron slighted).
  - **Decline** — refuse a perpetual obligation binding your successors: no stat gain; patron Disp -2; PS -1 (the poor resent a refused charity); Grudge(patron) + Reputation 'Snubbed benefactor' on the patron (fuels their countermove). *Signal:* Need unserved → upward jaw (-) and instrumental (-).
- **Three-vector burden:** Positional — accepting the irrevocable terms binds every future holder of your seat via a Compact you can never undo; the seat's autonomy is the price. A kinship/dynastic seat prizes the permanent founder-Weight; a short-tenure purchased office externalizes the Compact onto successors at no cost to itself (a cheap yes that is really a debt on the office — the cross-tenure externality that keeps the accept branch from being a free win: the Compact obligation bites via the chained EVT-OPP-04).
- **Ripples:** FI **WIRED** (a snubbed/insulted patron may covertly fund opposition — who is bankrolling your critics). SC **AT-RISK** (the Compact becomes a live contest predicate the season a successor tries to breach it — 'may we break the founder's charter?'; needs stakes.source_key).
- **FA [REVISED — critic fix applied]:** With **PS +1** now on the two accept branches, the claim is true via a real driver: **Prosperity/Order/PS rise → settlement L/PS up → Mandate = Σ L/PS rises.** *(Original moved only Prosperity/Order/Weight — none of which feed Mandate; Prosperity feeds faction Treasury, Σ Prosperity×10, not Mandate. The added PS supplies the genuine L/PS mover the claim requires.)*
- **Follow-on:** Merchant-patron Haldane Voss's Compact becomes a delayed-fuse Crisis: the 'day they broke Voss's charter' arc seeds if any future administrator moves to dissolve it (see EVT-OPP-04).
- **New lever:** **none of the five settlement levers** — the permanence is carried by the Compact Ledger family (existing, ED-SE-0019).

---

#### EVT-OPP-07 — The Turnpike Charter (Opportunity) **[REVISED]**
*(Critic: the batch's best lever discipline — the skew branch invokes route/corridor Precedent exactly as §2 defines it.)*
- **Grounding:** The Standon–Wadesmill turnpike trust (1663), England's first toll road — a self-funding inter-settlement link maintained from tolls not the parish rate — docket T19 'Charter Inter-Settlement Link'.
- **Trigger:** settlement lies on a trade corridor adjacent to 2+ settlements AND joint-magistrate proposal on the table AND faction charter available AND Π≤2; neighboring magistrates offer to co-charter a self-funding toll road.
- **Scale:** settlement|territory.
- **Branches:**
  - **Charter the trust** — build the toll road on shared terms: Prosperity +1, Weight +1 (trade flow), Π -1 (corridor trade-friction dampened), Treasury ~0 (tolls self-fund); Precedent 'inter-settlement links chartered by trust' + Grudge(merchants) if tolls set high. *Signal:* regional trade served above demanded → instrumental (+).
  - **Charter it but subsidize low tolls from the Treasury**: Prosperity +1, Weight +1, Treasury -1 (subsidy); merchants Disp +1; Precedent 'links chartered with subsidized tolls', no merchant Grudge. *Signal:* positive and goodwill bought, but public Treasury spent where tolls could have paid → downward/fiscal jaw (-).
  - **Route it to favor your settlement** — skew the corridor through your gate: Prosperity +2 (to you); neighbor settlements Grudge (bypassed); your future Prosperity now hinges on one chokepoint; route/corridor Precedent set to SINGLE-CORRIDOR (a targetable vulnerability) + Grudge(neighbor magistrates). *Signal:* delivered above demanded for you but the neighbors' Need is actively wronged → hierarchical (+), instrumental/traditional (-) (you fractured the corridor). The +2 is not a free win — it buys a geographic weakness.
- **Three-vector burden:** Positional + upward — a cross-jurisdiction deal needing the faction charter forces the governor to act between scales, negotiating with peers and a superior at once; merchants bearing the tolls are the upward pressure. A military/regional seat can push the skewed self-favoring route through by weight; a bureaucratic seat prefers the clean chartered trust.
- **Ripples:** FI **WIRED** (skewed or skimmed toll revenue seeds a corruption lead — who is really collecting at the gate). SC **AT-RISK** (the route/corridor Precedent as the predicate of a trade-dispute contest with bypassed neighbors; needs stakes.source_key).
- **FA [REVISED — critic fix applied]:** Restated onto its real canon channel: **Prosperity rise → faction Treasury (Σ Prosperity ×10), and the corridor is a territory-scale trade asset → a real trade-posture window; this routes through Treasury, NOT Mandate (no L/PS moved on any branch).** *(Original "Weight/Prosperity rise → settlement L/PS up → Mandate rises" removed — Weight and Prosperity are not Mandate inputs.)*
- **Follow-on:** Reeve Halquist of the bypassed town nurses the Grudge from the skew branch into a corridor-rivalry arc (a competing toll road, or a Parliament motion to break your Precedent).
- **New lever:** **route/corridor Precedent (single-corridor/diversified)** — invoked ONLY on the skew branch: Prosperity records the AMOUNT of trade, not that a settlement's prosperity now hangs on ONE named chokepoint a rival can read and attack. The other two branches invoke no lever.

---

#### EVT-OPP-08 — The Relic Redeemed (Opportunity) [KEEP]
*(Critic: best-grounded card in its batch — the redeemed-from-a-creditor correction is baked in.)*
- **Grounding:** Louis IX's acquisition of the Crown of Thorns (1239) — REDEEMED from the Venetian creditors who held it in pawn (not bought on an open market), then enshrined in the purpose-built Sainte-Chapelle to anchor Capetian sacral legitimacy — docket F10 'Acquire Legitimacy Object → Enshrine'.
- **Trigger:** a legitimacy object is available for redemption from a creditor AND settlement is a capital/high-Weight seat AND (Treasury≥2 OR credit available) AND Π≤2.
- **Scale:** settlement|faction.
- **Branches:**
  - **Redeem the relic in cash** — enshrine it in the capital: Treasury -2, then Weight +1, Prosperity +1 (pilgrimage), L +1; Relic tag (inert) → enshrined + Precedent 'restores legitimacy through the sacred'. *Signal:* sacral-legitimacy Need delivered above demanded, paid honestly → strong sacred (+) and traditional (+).
  - **Acquire on credit** — enshrine now, pay the creditor later: Weight +1, Prosperity +1, L +1 now; Debt(creditor); fiscally-conservative Standing-holders Disp -1; Relic tag enshrined + Debt to the redeeming creditor (a hidden broker really holds the note). *Signal:* sacred now (+), but the Treasury is mortgaged → downward/fiscal jaw (-) for later seasons.
  - **Decline** — the coin is better spent on walls and grain: no gain; a RIVAL seat may redeem it instead → their Weight +1, your relative L -1; if a rival takes it, Reputation 'Defender of the Faith' accrues to THEM. *Signal:* no actor wronged, but a legitimacy opportunity ceded → neutral-to-negative on sacred (relative to a rival who seized it).
- **Three-vector burden:** Positional + downward — legitimacy is the seat's own currency, so acquiring concentrates it on you; a credit redemption answers to the creditor. An ideological/sacred-legitimacy seat overreaches for enshrinement (even on credit); a merit/bureaucratic seat reads the coin as better spent on Defense and declines.
- **Ripples:** FI **WIRED** (the credit branch seeds a concealed broker/creditor — who really holds the Debt behind the redemption). SC **AT-RISK** (the enshrined Relic's legitimacy, or the Debt behind it, as a contest predicate — a rival argues it was overpriced or mortgages the realm; needs stakes.source_key). FA **real via Mandate** (Weight/L rise, with **L +1** the genuine L/PS mover → settlement L/PS up → Mandate rises → opens a faction Legitimacy-Broadcast window, the Augustan Res Gestae move).
- **Follow-on:** Lombard banker Ezio Marchetti holds the redemption note: on the credit branch his Debt-call seeds a future fiscal Crisis if unpaid; on the decline branch the rival who enshrined it seeds a legitimacy-rivalry arc.
- **New lever:** **none** — per F10 the relic is a Ledger tag (Relic → enshrined); Weight/Prosperity/L/Treasury + Debt/Precedent/Reputation.

---

### ═══════════ AMBITION (4) ═══════════

---

#### EVT-COURT-06 — The Banked Claim (Ambition) **[REVISED]**
- **Grounding:** Habsburg marriage diplomacy banking a contingent claim on a currently-occupied seat that sits dormant until the target line lapses (docket C1), read with Romanos Lekapenos's staged marital climb to co-leadership (C8) and the Ottoman damat's permanent consort-advisor ceiling (C3).
- **Trigger:** a marriage_contract_banked opportunity is available AND a claimant NPC carries ambition goal 'dynastic' AND the settlement council has a Consent-Rule set AND Π 0-2.
- **Scale:** personal|settlement|faction.
- **Branches:**
  - **Take the marriage and bank the claim**: marriage_contract_banked Key recorded, claimant fast-tracks to Standing 3 (gates skipped, C9) with succession_eligible=false set permanently (the C3 damat ceiling), Mandate +1 (alliance L/PS), rival house Grudge; if Consent-Rule=Unanimity and one councillor holds out, the claim is blocked and this forces branch C; Precedent 'this-marriage-was-a-political-payment' (latent) + Debt(allied house). *Signal:* dynastic security delivered on the traditional axis (Directive jaw +); the ceiling flag caps the upside honestly (the claimant can never convert the tie into a throne).
  - **Decline** — keep your options open: allied house Disp -1, no claim banked, Π stays low; a rival may take the marriage instead; Reputation 'independent' + mild Grudge(spurned house). *Signal:* neutral-to-negative — the opportunity lapses; the Need jaw registers a foregone security the faction head may later hold against the governor.
  - **Flip the Consent-Rule to Majority to force the alliance past the holdout**: spend AP/Mandate to change the council Consent-Rule Unanimity→Majority, the holdout loses their veto, Order -1 (procedural fight), the alliance passes, the councillor may defect; Precedent 'council-rule-changed-under-pressure' + strong Grudge(holdout). *Signal:* you delivered the alliance but spent the council's consent norm → sacred/traditional (-) (a procedural covenant broken), instrumental (+); a consent-legitimated governor damages their own base.
- **Three-vector burden:** Positional — a kinship-seated governor (base = marriage networks) affords branch A cheaply; a bureaucratic/consent-legitimated governor pays dearly for branch C because flipping the Consent-Rule undermines the norm that seats them. Downward (the faction head wants the alliance secured); upward (the council and the governed whose consent norm is at stake).
- **Ripples:** FI (the holdout councillor's secret dealings — why he really vetoes — become a lead). **SC [REVISED]:** the Consent-Rule change is a constitutional predicate a motion **may cite** (whether one member's veto binds) — flagged **AT-RISK** pending the stakes.source_key hook. *(The Consent-Rule lever invocation is left as-is — correctly justified.)* FA (the alliance shifts Mandate; the banked claim seeds a future succession domain-action window).
- **Follow-on:** The banked claim sits dormant until the target line's heir dies without issue (C1), then auto-fires 'press the claim' — a long-fuse succession arc; Councillor Brant (the holdout) and Lady Ellin (the allied heir).
- **New lever:** **Consent-Rule (§2, HAB-6)** — branch C's decision is precisely 'does one council member's veto bind, or can a majority override it,' which changes the shape of the decision (whether the governor can act at all); Prosperity/Order/L/PS cannot express whether a single actor holds a structural veto.

---

#### EVT-COURT-08 — The Protégé's Move (Ambition) **[REVISED]**
- **Grounding:** The cardinal-nephew's Anointed Successor — a term-limited patron installing a protégé early by waiving the gate, racing his own remaining tenure and accruing a faction-wide nepotism debt (docket A2), read with the successor-designate/parallel_asset_pool transfer (A5) and the extractive kin-gatekeeper's short horizon (E7).
- **Trigger:** a Standing 6+ NPC has low expected_tenure (term-limited/aging) AND ambition goal 'install successor' AND a protégé candidate exists AND a patronage_installation Key is pending AND **Π 0-2 [REVISED — tightened from 0-4 to sit cleanly in the Ambition band]**.
- **Scale:** personal|settlement.
- **Branches:**
  - **Bless the installation** — waive the gate and seat the protégé: protégé Standing 0→3 (gate waived), patron Disp +2 (now owes the governor), passed-over candidates Grudge, a faction-wide Nepotism-debt counter +1, Order 0; Debt(patron) + Precedent 'nepotism-tolerated' + the Nepotism-debt counter (which at threshold fires a systemic Reform-Backlash demotion wave on all protégé-tagged seats, the 1692 abolition). *Signal:* merit gate bypassed (Need -) but the patron served (traditional/hierarchical +); the accumulating Nepotism-debt is the guilt-by-association timebomb across every blessed seat.
  - **Block the installation** — enforce the gate: protégé denied, patron Grudge (strong) and ambition thwarted (trajectory may shift covert/extractive per E7), L +1 (merit upheld), Order 0; Precedent 'gate-enforced'. *Signal:* merit Need (+); but a thwarted short-horizon patron is dangerous — they may liquidate their prerogatives into portable wealth on the way out (E7 extractive shift).
  - **Bargain** — install the protégé but re-parent them to yourself, not the patron (A5 successor_designate): protégé installed at Standing 2 with a successor_designate pointer to the governor, the patron's parallel_asset_pool re-parents to the governor on the patron's exit, Treasury -1, patron mild Grudge (feels co-opted); Debt(protégé) + Compact/Precedent 'succession-brokered'. *Signal:* mid instrumental/traditional — the governor captures the succession asset; repeated use raises up-tier Suspicion toward the governor's own lineage (the Yuan Shikai lineage-suspicion accrual).
- **Three-vector burden:** Positional — a patronage-seated governor blessing a fellow patron's protégé cheaply thickens the patronage web their base runs on; a merit/ideological-seated governor spends legitimacy to bless nepotism against their base. Downward (the aging patron, a senior peer, presses); upward (the passed-over merit candidates watch whether advancement is earned or granted).
- **Ripples:** FI (the protégé's unearned status conceals a competence secret an Investigate can surface). **SC [REVISED]:** the installation is a nepotism-audit predicate a motion **may cite**, with the Nepotism-debt counter as its factual basis — flagged **AT-RISK** pending the stakes.source_key hook. *(Was asserted as a wired predicate.)* FA (the protégé's new seat adds/removes settlement L → Mandate; the Nepotism-debt threshold opens a faction-wide backlash window).
- **Follow-on:** Lord Emeric — if installed, the patron's death re-runs the succession (A5 transfer, or the Yuan Shikai 'claim office' endgame); if blocked, thwarted patron Prioress Idonea shifts extractive, converting her prerogatives to portable assets.
- **New lever:** **none** — expected_tenure is a seat property; patronage_installation reuses Debt/Standing/Mandate + the Nepotism-debt Ledger counter.

---

#### EVT-OPP-02 — The Rival's Games (Ambition) [KEEP]
- **Grounding:** Agrippa's aedileship (33 BCE) — he cleaned the Cloaca Maxima, ran free baths and games out of his OWN purse, converting private munificence into political ascent — docket S2 'Sponsor (self-financed)', where credit accrues to the person, not the settlement.
- **Trigger:** exists Local-Actor with ambition.method=factional AND Standing rising AND settlement.PS contestable AND Π≤3; fires when that NPC's ambition.progress crosses its act-threshold (§3.2).
- **Scale:** personal|settlement.
- **Branches:**
  - **Let them spend** — pocket the public benefit, cede the applause: Prosperity +1, Order +1 (their coin, real works); your relative L -1 as PS goodwill shifts to the rival; Reputation 'Benefactor' on the rival NPC. *Signal:* the Need served but by a competitor → your delivered-credit below demanded on your own standing → hierarchical (-) (someone else out-provided you).
  - **Match the gift from the Treasury** — outspend them for the crowd: Treasury -2, PS +1 (to you), L +1, rival Disp -1; Grudge(rival). *Signal:* Need positive and credited to you, but public Treasury spent on a positional contest a superior may question → downward jaw (-).
  - **Regulate it** — cap private munificence (an anti-ambitus/sumptuary ruling): Order +1, rival's Reputation gain blocked, rival Disp -2; Precedent 'private games capped' + Grudge(rival). *Signal:* you protected the seat but left the Need underserved and wronged an actor → instrumental (-), hierarchical (+) (rule upheld).
- **Three-vector burden:** Positional — a rival is contesting the seat's own popularity, and the prize is the governed's goodwill (upward). A purchased-office holder is most exposed to being out-benefacted (should regulate or match); a patronage seat can call its patron to counter-sponsor rather than drain Treasury.
- **Ripples:** FI **WIRED** (the regulate/block branch drives the rival covert — their backers' funding becomes a lead). SC **AT-RISK** (the rival's 'Benefactor' Reputation as the predicate for a seat-challenge motion; needs stakes.source_key). FA (if the rival's PS grows unchecked, their settlement L/PS contribution shifts the faction Mandate toward whichever bloc they back).
- **Follow-on:** Aedile-aspirant Marca Vint advances toward a parliamentary bid; her 'Benefactor' tag biases her future Ambition card's draw-weight upward (§8 deck re-weight).
- **New lever:** **none** — PS/L/Order/Treasury + Reputation/Grudge/Precedent and the Standing ladder.

---

#### EVT-OPP-06 — The Confraternity Rises (Ambition) [KEEP]
- **Grounding:** The Scuola Grande di San Rocco (Venice, founded 1478) — a lay confraternity giving prestige, office and charitable standing to cittadini/merchants locked out of the patrician Maggior Consiglio; an alternate rank ladder beside the closed faction one — docket O10 'Found Confraternity (Org Charter)'.
- **Trigger:** exists wealthy NPC whose power_base is INELIGIBLE for the faction Standing ladder (e.g. non-patrician) AND Directive pressure on the excluded class is high AND Π≤3; fires when that NPC's ambition.progress crosses threshold and they found the confraternity.
- **Scale:** personal|settlement.
- **Branches:**
  - **Bless it** — let the confraternity flourish as a lawful prestige ladder: Order +1, Prosperity +1 (its charity), PS +1 (a valve for the excluded); founder gains org-scoped Standing; founder Reputation 'Founder' + latent Grudge/rivalry between the confraternity and the establishment as it grows. *Signal:* the excluded class's Need served above demanded → instrumental (+) and traditional (+), but it seeds a rival power center.
  - **Co-opt it** — attach the confraternity to your patronage: founder Disp +1, you gain a client network; founder's independent Standing captured under yours; Compact (mutual obligation) — you owe protection, it owes votes. *Signal:* positional jaw (+) (you turned a rival ladder into a clientele) but you now owe a Compact → mixed.
  - **Suppress it** — deny the charter; a shadow prestige ladder is a shadow government: Order +1 (short-term), PS -1, founder Disp -2; Grudge(founder) + Outlawed tag if it persists underground. *Signal:* the valve shut → instrumental/hierarchical (-); drives the org covert.
- **Three-vector burden:** Positional + upward — a parallel prestige ladder could grow into a shadow government that contests the seat itself; the excluded class's pressure is the upward source. An establishment/kinship-seated governor is most threatened and should co-opt or suppress; a merit-seated governor can safely bless it and ally.
- **Ripples:** FI **WIRED** (the suppress/Outlawed branch drives the confraternity covert — Investigate surfaces its underground cells and secret membership). SC **AT-RISK** (the confraternity's grown org-Standing as a voting bloc whose backing is a motion predicate; needs stakes.source_key). FA (if it grows, its members' PS shifts the faction Mandate toward whichever side it backs).
- **Follow-on:** Cloth-merchant Tomas Aldemar's confraternity becomes a faction-in-miniature: blessed, it seeks a Great-Work charter (O11); co-opted, it calls in the Compact at an inconvenient vote; suppressed, it seeds an Intrigue/Crisis chain.
- **New lever:** **none of the five settlement levers** — an Organization entity on its own scoped Standing ladder + Reputation/Compact/Outlawed/Grudge + PS/Order.

---

### ═══════════ THREAD (1) ═══════════

---

#### EVT-XSCALE-07 — The Paper Storm (Speculative Cascade / Bank-Run Contagion) (Thread) [KEEP]
- **Grounding:** John Law's Mississippi Bubble / Banque Royale collapse 1716-1720 — the Bank Run 'imposes an emergency Keep Order tax on every settlement holding the paper' — docket §2.9; reinforced by the French assignat hyperinflation (Capital-Posture:Speculative pegged to contested land) with Hamilton's Funding & Assumption as the consolidation off-ramp. Capital-Posture Ledger family = shortlist #1.
- **Trigger:** a Capital-Posture:Speculative tag (Charter-Fiat paper) held across ≥3 settlements AND its issued size exceeds the real backing ratio AND Π rising. The Thread ticks each season the backing gap widens, resolving to a Bank Run Crisis at threshold.
- **Scale:** settlement|territory|peninsula.
- **Branches:**
  - **Consolidate the paper** (Funding & Assumption — pool every settlement's Speculative/Debt into one faction-level Compact backed by the whole Mandate): faction Treasury -2 now; a Concession (a capital-relocation/centralized-extraction Precedent strengthening the PA's reach); backing ratio restored, the Run defused; Compact (consolidated) + Concession; clears Capital-Posture:Speculative across the holders. *Signal:* fiscal stability delivered (Need +) → instrumental (+); local autonomy ceded to the centre (Directive -).
  - **Keep issuing** (roll the paper forward): immediate Treasury/Prosperity +1 this season; backing ratio worsens; the Thread advances toward the deterministic Bank Run, which permanently burns the Charter-Fiat method and levies an emergency Keep Order tax on every holder (Order -2 peninsula-wide); Capital-Posture:Speculative +1 + a hidden 'backing-breach' counter. *Signal:* surface-positive this season, deferred strongly negative → instrumental (-); the demanded-minus-delivered gap is hidden until detonation.
  - **Cap issuance + partial backing settlement** (bleed the fuse slowly): cap the Speculative tag; compensate the dispossessed backing-holders; slower, does not fully clear but keeps the Thread below detonation; Concession + Capital-Posture held (not cleared). *Signal:* partial both jaws → traditional/instrumental.
- **Three-vector burden:** Downward (the Directive:Extract that drove Charter-Fiat issuance) + positional (the fiscal seat). A purchased-office holder who bought in with paper has no metallic reserve to consolidate (branch 1 unaffordable) and is structurally pushed to roll the paper forward until it detonates; an ideological/merit PA can spend legitimacy on the painful consolidation. The Thread makes the burden a TIMING choice — deferral raises the eventual consolidation price (the one-way Capital-Posture ratchet).
- **Ripples:** FI **WIRED** (a note-forger/insider who dumped paper before the breach). SC **AT-RISK** (the hidden backing-breach counter, once surfaced, as a Consulta fiscal-inquiry predicate; needs stakes.source_key). FA **via Mandate** (a defused Run raises faction Mandate/reach; a Bank Run bleeds Mandate across every holder simultaneously — correlated, peninsula-scale, forcing a defensive posture).
- **Follow-on:** The assignat coupling — if the Speculative tag was backed by Grudge-tagged confiscated land, the Run deepens the dispossessed faction's Recognition-Denial (§1.0b) and seeds a restitution Intrigue; Almoner-Treasurer Elke, the paper's architect, whose Standing is staked to the backing ratio — a Demotion Magnitude drop on detonation seeds her own downfall arc.
- **New lever:** **Capital-Posture** — the whole card is the Capital-Posture:Speculative ratchet detonating across scale; it re-types the extraction decision (paper vs real Prosperity) in a way a Treasury number cannot express.

---

## 3. The cut cards, with cause

**None.** The independent critic returned zero CUT verdicts across all 59 cards. Every card cleared the four §10 gates on grounding, meaningful choice, progression, and arc fuel; the 19 REVISE verdicts were all narrowly-fixable defects (18 dependency/overclaim, 1 Ω-d non-dominance), corrected inline above.

The nearest thing to a cut was **EVT-COURT-07**, which failed a **duplicate/reskin** gate against COURT-01 (near-identical trigger state, two of three overlapping branches, a shared Heshen-H7 FI lead). The critic's fix offered a fork: differentiate or MERGE into 01. **Differentiation was applied** — COURT-07 is re-cut around `concurrent_roles` role-stacking + the Crown-Agent parallel-channel overlay (E3 Richelieu), branches that COURT-01 does not carry, and its FI lead is re-keyed from embezzlement to role-accumulation. The two now do distinct mechanical jobs (access-monopoly-by-favor undone by a side channel vs illegitimate role-stacking neutralized by strip/bypass/consolidate). Had that differentiation been impossible, COURT-07 would have merged into COURT-01 and the deck would be 58.

---

## 4. Cross-cluster patterns the per-cluster passes couldn't see

**A. Cross-cluster reskin clusters (same mechanical card generated independently).**

1. **The Severed Enclave — GEO-04 vs XSCALE-08.** Both are Berlin Blockade cards: an enclave with no contiguous land supply, survival gated on a *pre-banked* Fortify airbase/corridor tier, resolving to Sponsor-corridor / cede / endure. This is the single most serious cross-cluster collision in the batch — same grounding, same hard-precondition mechanic, same three-branch shape, even the same "retroactive audit of a Fortify decision" framing. They are held apart only by lever ownership (GEO-04 invokes route/corridor Precedent as load-bearing; XSCALE-08 deliberately *declines* it and rests on the Fortify FacilityTier) and by XSCALE-08's added arbitration branch. **MERGE candidate.** Recommendation: keep **one** enclave card. GEO-04 is the tighter, higher-praised version (critic: "strongest card in the cluster"); fold XSCALE-08's arbitration branch (Suez, override-the-battlefield) into GEO-04 as a fourth response and retire XSCALE-08, OR re-scope XSCALE-08 explicitly to the *peninsula/coalition* scale so it is the multi-settlement sibling of the settlement-scale GEO-04. As written they are 90% the same card in two clusters.

2. **Coalition-embargo vs enclave-blockade — XSCALE-06 vs the enclave pair.** XSCALE-06 (ABCD Line, economic single-source severance, no-Bargain) is adjacent to the enclave cards (geographic severance) and the critic already flagged the GEO-04/XSCALE-06 adjacency. All three are "supply cut off, pre-investment decides survival" cards. They are differentiated correctly (economic monopoly vs land enclave; war vs arbitration; lever split across them), but **the deck is carrying three severance-Crisis cards** and should confirm that is a deliberate resource-geography suite, not redundancy. Keep all three only if the lever-ownership split (XSCALE-06 owns route/corridor Precedent; XSCALE-08 owns the Fortify-tier gate; GEO-04 owns single-corridor) is preserved as authored — otherwise two of the three collapse together.

3. **The chokepoint gatekeeper — COURT-01 vs COURT-07** (within-cluster, but the same pattern recurs cross-cluster in **GOVFRIC-06** The Vermilion Substitution and **GOVFRIC-07** In the Governor's Name). Four cards across two clusters run "a court/chancery/clerk intermediary corrupts the flow between ruler and governed, surfaced by Investigate." After the COURT-07 revision they are distinguished (access-monopoly / role-stacking / Directive-forgery / clerk-extortion), and all four cite genuinely different historical mechanisms — but this is the deck's densest mechanical neighborhood and the shared Heshen-H7 FI lead had to be re-keyed once already. **Audit the FI leads across all four to guarantee no two collide on the same concealed-actor archetype.**

4. **Marriage-banks-a-claim — COURT-06** stands alone but shares the Consent-Rule veto-flip mechanic with **ECON-03** (Privileged Estates Veto) and **GOVFRIC-02** (Guildhall Rises, Concord branch). Three cards now flip or install a Consent-Rule. That is the correct level of reuse for a sanctioned lever (not a collision — different content, different families), but it means **Consent-Rule is the deck's most-exercised new lever (3 cards)** and R-1 must land before any of those three branches is playable.

5. **Stale-Assessment gap — CLIM-09, ECON-05, and (post-revision) GEO-08** all now exercise the Assessment tag's "when to re-Survey" decision. Three cards, three clusters, one lever. Correctly differentiated (epidemic mortality / land-economy collapse / pretender-credibility fuel) but confirm the lever's rules read identically across all three.

**B. Ω-d risks that only appear when cards combine.**

- **The Debase spiral is a two-card loop:** ECON-05 (stale rolls → raises Levy Ob) chains *by design* into ECON-01 (Capital-Posture:Debased). In a campaign where both are live, a governor who Defies ECON-05 is railroaded toward the ECON-01 Crisis with the Debased tag already written — the *combination* removes the clean-Recoinage option ECON-01's own Ω-d relies on. Not a defect, but flag that ECON-01's non-dominance was graded *in isolation*; verify it still holds when arriving pre-loaded from ECON-05.
- **The Compact-endowment chain (OPP-03 → OPP-04):** OPP-03's accept branch is only non-dominant *because* the Compact obligation bites later via OPP-04. If OPP-04 is not in the same campaign deck, OPP-03's accept branch reverts to a near-free win (the critic's original concern). **These two must ship together or OPP-03 loses its Ω-d.** Treat them as a bonded pair, not two independent draws.
- **Cascade-stacking at high Π:** XSCALE-01 (Cooling cascade), GOVFRIC-06 (forged harsher Directive), and any settlement-scale Crisis drawn the same season can compound Demotion Magnitude inputs. The per-card passes graded each Key survivable alone; the aggregate roster-wide read (XSCALE-01's explicit mechanic) is the place to stress-test whether stacked negative Keys produce an unintended death-spiral.

**C. Family over/under-representation (the pattern the per-cluster passes structurally could not see).**

- **Crisis is 22/59 (37%)** — over-represented. Every high-Π cluster (climatic, cross-scale) defaulted to Crisis, and the COURT-04 re-family added one more. The Π-gating explains it, but a deck this Crisis-heavy will feel relentless in play.
- **Thread is 1/59** — critically under-mined. Only XSCALE-07 (Paper Storm) is a true Thread (a per-season ticking fuse resolving to a Crisis at threshold). Several cards *contain* thread-like fuses (CLIM-06's Contagion-Vector, ECON-03's Concealed-Deficit, ECON-04's backing-ratio, OPP-03's Compact) but are filed as their triggering family. **The deck needs 3–5 more first-class Thread cards** to make the slow-fuse layer legible as its own draw category.
- **Ambition is 4/59** — thin. All four are strong (COURT-06/08, OPP-02/06), but four Ambition cards cannot carry the low-Π draw band that the substrate's Π-gate promises (low Π → Opportunity/Ambition). **Author more Ambition** to balance the low-Π shelf, or the low-Π draws will be dominated by the 6 Opportunity cards.
- **Petition (6), Opportunity (6), Intrigue (7)** are healthy and well-distributed across dockets.

---

## 5. Honest coverage & AT-RISK ledger

This is the objective-critique payoff: what is playable today vs what is gated.

**§13 AT-RISK Parliament edge (needs an authored `social_contest` `stakes.source_key` hook before the SC ripple mechanically fires).** Until R-2/ED-SC-0015 lands, these cards deliver their FI and FA ripples but their **SC ripple degrades to "a motion may cite the Key as narrative predicate"** — real narratively, not mechanically wired:

- **Cards whose SC edge is AT-RISK (SC ripple gated):** CLIM-01, CLIM-02, CLIM-04, CLIM-05, CLIM-06, CLIM-08, GEO-01, GEO-02, GEO-03, GEO-04, GEO-05, GEO-06, GEO-07, GEO-08, GEO-09 (downstream censure use), ECON-01, ECON-04 [after revision], ECON-05 [after revision], ECON-07 [after revision], COURT-01, COURT-02 [after revision], COURT-03 [after revision], COURT-04 [after revision], COURT-05 [after revision], COURT-06 [after revision], COURT-07 [after revision], COURT-08 [after revision], OPP-01, OPP-02, OPP-03, OPP-04, OPP-05, OPP-06, OPP-07, OPP-08, GOVFRIC-01, GOVFRIC-04, GOVFRIC-05, GOVFRIC-06, GOVFRIC-07, GOVFRIC-08, GOVFRIC-09, XSCALE-01, XSCALE-02, XSCALE-03, XSCALE-04, XSCALE-05, XSCALE-06, XSCALE-07, XSCALE-08. **(≈50 cards — nearly the whole deck depends on the §13 hook for its full SC ripple.)** This is the deck's single largest dependency and the highest-leverage thing to author next.
- **Cards whose SC content is WIRED TODAY (do not need the §13 hook):**
  - **ECON-03** — the reform is *literally decided in Parliament/Consulta*; the Consent-Rule flip IS the contested motion (the SC content is the mechanism, not a Key-predicate hook).
  - **ECON-06** — the Parliament *composition* change (a new Banking voting bloc) routes through faction Standing eligibility / Mandate, the WIRED FA path, not the Key-opening-Ob hook.
  - **GEO-09** (Denounce branch) and **GOVFRIC-06** (Verify branch) — the action ITSELF is a contest (the Church Tribunal / the up-tier verification); that contest is real today. Their *downstream* censure predicates remain AT-RISK.
  - **GOVFRIC-02** — the seat-allocation Charter/Suppress Key is a genuine stakes.source_key *candidate* the critic rates as a real predicate, but full wiring still awaits the hook; treat as WIRED-adjacent.

**R-1 (new settlement lever) dependency — cards that will not fully express until the lever is ratified:**

- **StockLevel:** CLIM-01, XSCALE-01. (2 cards)
- **Assessment tag:** CLIM-09, ECON-05, GEO-08 [after revision]. (3 cards)
- **route/corridor Precedent:** CLIM-03, GEO-04, ECON-08, OPP-07, GOVFRIC-01, XSCALE-06. (6 cards)
- **Capital-Posture ledger family:** ECON-01, ECON-04, XSCALE-07. (3 cards — and it back-stops ECON-08's Bargain branch and XSCALE-07's whole spine.)
- **Consent-Rule:** ECON-03, GOVFRIC-02, COURT-06. (3 cards)
- **Total lever-gated: 17 distinct cards** (route/corridor Precedent is the most load-bearing at 6). All these need R-1 ratification before their lever-branch is mechanically playable; several (CLIM-03, GOVFRIC-01) can *partially* play on existing stats with the lever branch degraded.

**PROPOSED Outlawed ledger-tag family dependency:** GOVFRIC-08, XSCALE-02 (contagion clause). Awaits the Outlawed family's ratification (substrate §2.2/§9).

**Fully wired on current canon and playable TODAY (all three ripple channels resolve on existing machinery, no new lever, SC either wired or gracefully degrading to cite):** the cleanest are **ECON-02** (Debt→Outlawed, L-legible SC predicate), **ECON-06** (composition-via-Standing), **GEO-06** (Settle Arrears, existing Debt family), **GOVFRIC-07** (CHN-3 is the *named* WIRED FI precedent), **COURT-02/03** (Demotion resolver + Hold Court), **GEO-02** (Compact family), **OPP-04** (Compact upkeep). These are the recommended **first-playable slice** for a vertical prototype — they exercise FI (WIRED), FA (via Mandate on real L/PS movers), and the arc engine without waiting on R-1 or R-2.

**Net readiness posture:** the deck is **arc-ready and FI-ready today** (every card has a WIRED-or-honest FI lead and a named follow-on actor), **FA-ready today** for the ~40 cards moving a real L/PS/Standing driver (after the six FA-overclaim revisions, every surviving FA claim routes through an actual Mandate/Treasury/Standing driver), but **SC-gated** for ~50 cards on the single §13 hook and **lever-gated** for 17 cards on R-1. **Author the §13 stakes.source_key hook and ratify route/corridor Precedent first — those two unlock the most cards.**

---

## 6. Provenance breadth statement

The design lead required BREADTH across all four research dockets. Confirmed — all four are mined, none collapsed. Per-docket surviving-card counts (attributed by each card's `grounding` field, not by cluster label):

**Docket A — Historical Concerns Action Catalogue (`historical_concerns_action_catalogue_v1`, the §2.1–§2.10 catalogue + shortlist/Chain synthesis).** The most-mined docket, underwriting four clusters.
- climatic_geographical: CLIM-01 (§2.5), CLIM-02 (§2.5), CLIM-04 (§2.4), CLIM-05 (§2.4), CLIM-06 (§2.7), CLIM-07 (§2.8), CLIM-08 (§2.5), CLIM-09 (§2.7) — 8
- geopolitical: GEO-01 (§2.1), GEO-02 (§2.1), GEO-03 (§2.2), GEO-04 (§2.2), GEO-05 (§2.2), GEO-06 (§2.3), GEO-07 (§2.3), GEO-08 (§2.1), GEO-09 (§2.1) — 9
- economic: ECON-01 (§2.9), ECON-02 (§2.9), ECON-03 (§2.9), ECON-04 (§2.9), ECON-05 (§2.9), ECON-06 (§2.10), ECON-07 (§2.10), ECON-08 (§2.10) — 8
- cross_scale_peninsula: XSCALE-01 (§2.8), XSCALE-02 (§2.3), XSCALE-03 (§2.10), XSCALE-04 (§2.10), XSCALE-05 (§2.1), XSCALE-06 (§2.2), XSCALE-07 (§2.9), XSCALE-08 (§2.2) — 8
- **Docket A total: 33 surviving cards.**

**Docket B — Comparative Governance Research (`comparative_governance_research_v1`, the VEN/HRE/HAB/IT/CHN codes).**
- governance_friction: GOVFRIC-01 (VEN-SE-2), GOVFRIC-02 (HRE-5), GOVFRIC-03 (HAB-5), GOVFRIC-04 (IT-7), GOVFRIC-05 (HAB-7), GOVFRIC-06 (CHN-7), GOVFRIC-07 (CHN-3), GOVFRIC-08 (HRE-6), GOVFRIC-09 (HAB-4) — 9
- **Docket B total: 9 surviving cards.**

**Docket C — Court & Standing Research (the A–H letter-code taxonomy: access/gatekeeping, initiation gates, marriage-claims, conduits, coalition purges, denunciation, nepotism).**
- court_standing: COURT-01 (D2/HAB-2), COURT-02 (C4/E1/G3), COURT-03 (H4/G9), COURT-04 (G6/CHN-8/A9), COURT-05 (B2/B3/B7), COURT-06 (C1/C8/C3), COURT-07 (A6/H7/E3), COURT-08 (A2/A5/E7) — 8
- **Docket C total: 8 surviving cards.**

**Docket D — Proactive Opportunity Research (the S/O/T/F codes: infrastructure Sponsor, Organization charters, Territory links, Legitimacy objects).**
- proactive_opportunity: OPP-01 (S1), OPP-02 (S2), OPP-03 (S12/S3), OPP-04 (O8/S12), OPP-05 (O4), OPP-06 (O10), OPP-07 (T19), OPP-08 (F10) — 8
- **Docket D total: 8 surviving cards.**

**Cross-docket fusions (breadth beyond single-docket mining):** several surviving cards deliberately fuse a Docket-A historical case with a Docket-B/C/D mechanism — e.g. GOVFRIC-01 fuses VEN-SE-2 (B) with the route/corridor lever and Arsenal dependency (A §2.5/§2.8), XSCALE-07 fuses §2.9 John Law (A) with the Capital-Posture family (shortlist #1), and OPP-08 fuses F10 (D) with the Sainte-Chapelle redemption correction. The court_standing cards routinely braid three A–H sub-cases each.

**Breadth verdict:** All four dockets are represented in the surviving deck (33 / 9 / 8 / 8). **No docket is under-mined to the point of collapse.** The distribution is deliberately weighted toward Docket A (the historical concerns catalogue is the deepest well and feeds four of seven clusters), with Dockets B, C, and D each contributing a full dedicated cluster of 8–9 cards. The BREADTH requirement is met: the deck spans all four research dockets and all seven card families, with every surviving card complete with impacts (stat/tag deltas, resolution_quality signal, three-vector burden, honestly-graded FI/SC/FA ripples, and a named follow-on actor).
