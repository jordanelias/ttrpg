# Event-Card Integration Map

## Status: PROPOSED — compendium integration pass, not yet Jordan-ratified

**Scope of this section.** Valoria's event-card material now exists in three separate corpora that were
authored independently and never cross-referenced against one another:

1. **The 58-card grounded deck** — `designs/audit/2026-07-11-grounded-event-card-deck/grounded_event_card_deck_v1.md`
   (Lane IN, PROPOSED, author-pass not yet Jordan-ratified). Produced by a 15-agent Workflow (7 thematic
   generators → adversarial per-cluster critic → Opus synthesis) mining four research dockets.
2. **The 28-card Goldenfurt starter deck** — `designs/territory/goldenfurt_slice/event_deck.md` (slice
   S-006, bespoke settlement instance, `governance_play_redesign_v1.md §2` engine).
3. **The ~94-card HEV historical catalogue** — `designs/architecture/governance_compendium_v1/event_cards/2*.md`
   (`21_succession_civilwar.md` through `30_ripple_chains.md` plus `210_trade_monopoly_merchant_capital.md`;
   `30_ripple_chains.md` is chain-mechanics, not a card list, and is not counted below). The task brief's
   figure of "~124" catalogue cards is an estimate that does not match the working tree — the actual count,
   confirmed by direct enumeration of every `### HEV-` heading across all ten `2*.md` files, is **94**. That
   discrepancy is flagged rather than silently corrected to a round number.

**A methodological caveat that governs everything below.** The 58-card grounded-deck source document is
itself a *critique/audit* document, not a flat card-text dump: it reproduces full branch text for only nine
"worked example" cards (EVT-OPP-01 [tail only], EVT-OPP-03, EVT-OPP-07, EVT-OPP-08, EVT-COURT-06,
EVT-COURT-08, EVT-OPP-02, EVT-OPP-06, EVT-XSCALE-07), and covers the remaining ~49 cards only via (a) the
§6 provenance table (every card's ID + docket + sub-section citation, which **is** complete and authoritative
for all 58), (b) the §5 AT-RISK/lever-dependency ledgers (partial one-liner context for a subset), and (c)
scattered prose mentions in §3/§4. **Per-card `family` is therefore only independently confirmed for 11 of
58 cards** (the 6 explicit Opportunity cards, the 4 explicit Ambition cards, and the 1 explicit Thread card
— all under their own `### ═══ FAMILY (N) ═══` headers in the source). The source's own §4C aggregate count
(Crisis 22, Petition 6, Opportunity 6, Ambition 4, Intrigue 7, Thread 1 = 46 of 59 pre-merge) leaves a
13-card Friction residual that is an **arithmetic inference by this compendium pass, not a value asserted in
the source** — flagged in Table 1 and the totals below rather than presented as confirmed. Do not treat
Table 1's un-confirmed family cells as ratified; they are the best-available read of a document that does
not fully specify itself.

---

## 1. The 58-card grounded deck

Grounding codes are the exact docket citations from the source's §6 provenance table (Docket A = historical
concerns action catalogue §2.x sub-sections; Docket B = comparative governance VEN/HRE/HAB/IT/CHN codes;
Docket C = court/standing A–H letter-code taxonomy; Docket D = proactive-opportunity S/O/T/F codes).
`family: confirmed` = stated under an explicit family header in the source. `family: inferred` = this
compendium's best read from cluster-default prose (§4C: "every high-Π cluster [climatic, cross-scale]
defaulted to Crisis") or from an explicit in-prose family label (e.g. "three severance-**Crisis** cards").
`family: unresolved` = the source gives no family signal beyond the docket citation; do not treat as
ratified.

### Docket A — Historical Concerns Action Catalogue (33 cards)

| ID | Family | One-line (from source where available) | Historical grounding (docket cite) |
|---|---|---|---|
| CLIM-01 | Crisis *(inferred, cluster-default)* | R-1 StockLevel lever dependency; climatic/geographical cluster | §2.5 |
| CLIM-02 | Crisis *(inferred)* | climatic/geographical cluster | §2.5 |
| CLIM-03 | *unresolved* | route/corridor Precedent lever dependency (R-1) | (climatic cluster; §2.x per §6 pattern — not separately itemized in §6, see XSCALE-06 sibling) |
| CLIM-04 | Crisis *(inferred)* | climatic/geographical cluster | §2.4 |
| CLIM-05 | Crisis *(inferred)* | climatic/geographical cluster | §2.4 |
| CLIM-06 | Crisis *(inferred)* | carries a Contagion-Vector thread-like fuse, filed under triggering family | §2.7 |
| CLIM-07 | Crisis *(inferred)* | climatic/geographical cluster | §2.8 |
| CLIM-08 | Crisis *(inferred)* | climatic/geographical cluster | §2.5 |
| CLIM-09 | Crisis *(inferred)* | shares the Assessment-tag "when to re-Survey" lever with ECON-05/GEO-08 | §2.7 |
| GEO-01 | *unresolved* | geopolitical cluster | §2.1 |
| GEO-02 | *unresolved* | invokes the Compact family lever; "fully wired on current canon, playable today" | §2.1 |
| GEO-03 | *unresolved* | geopolitical cluster | §2.2 |
| GEO-04 | Crisis *(inferred — explicit "severance-Crisis" label)* | **The Severed Enclave** — Berlin Blockade: an enclave with no contiguous land supply, survival gated on a pre-banked Fortify airbase/corridor tier; near-duplicate of XSCALE-08 (cross-cluster collision, §4A.1), differentiated by owning route/corridor Precedent as load-bearing | §2.2 |
| GEO-05 | *unresolved* | geopolitical cluster | §2.2 |
| GEO-06 | *unresolved* | "Settle Arrears" — existing Debt family; "fully wired on current canon, playable today" | §2.3 |
| GEO-07 | *unresolved* | geopolitical cluster | §2.3 |
| GEO-08 | *unresolved (post-revision Assessment-tag lever added)* | shares the Assessment-tag lever with CLIM-09/ECON-05 | §2.1 |
| GEO-09 | *unresolved* | Denounce branch resolves through Church Tribunal (`dice_pool`/`social_contest`); downstream censure use is SC AT-RISK | §2.1 |
| ECON-01 | Crisis *(inferred — explicit "ECON-01 Crisis" wording, §4B)* | Capital-Posture:Debased; chains from ECON-05 (Debase-spiral Ω-d loop, §4B) | §2.9 |
| ECON-02 | *unresolved* | Debt→Outlawed, L-legible SC predicate; "fully wired on current canon, playable today" | §2.9 |
| ECON-03 | *unresolved* | Privileged Estates Veto — the reform IS decided in Parliament/Consulta; the Consent-Rule flip is the contested motion itself (SC wired today, not AT-RISK) | §2.9 |
| ECON-04 | *unresolved* | Capital-Posture ledger family dependency (R-1), backstops ECON-08's Bargain branch | §2.9 |
| ECON-05 | *unresolved (Friction-flavored per §4B "stale rolls → raises Levy Ob")* | Assessment-tag lever; chains into ECON-01 (Debase-spiral) | §2.9 |
| ECON-06 | *unresolved* | Parliament composition change (new Banking voting bloc), routes through faction Standing eligibility/Mandate — WIRED FA path, not the §13 hook | §2.10 |
| ECON-07 | *unresolved* | economic cluster | §2.10 |
| ECON-08 | *unresolved* | route/corridor Precedent lever dependency (R-1); Bargain branch backstopped by Capital-Posture | §2.10 |
| XSCALE-01 | Crisis *(inferred — "Cooling cascade")* | cascade-stacking risk at high Π alongside GOVFRIC-06; StockLevel lever dependency | §2.8 |
| XSCALE-02 | *unresolved* | PROPOSED Outlawed ledger-tag family dependency (contagion clause) | §2.3 |
| XSCALE-03 | *unresolved* | cross-scale/peninsula cluster | §2.10 |
| XSCALE-04 | *unresolved* | cross-scale/peninsula cluster | §2.10 |
| XSCALE-05 | *unresolved* | cross-scale/peninsula cluster | §2.1 |
| XSCALE-06 | Crisis *(inferred — explicit "severance-Crisis" label)* | ABCD Line — economic single-source severance, no-Bargain; owns route/corridor Precedent lever; one of the "three severance-Crisis cards" with GEO-04/XSCALE-08 | §2.2 |
| **XSCALE-07** | **Thread (confirmed)** | **The Paper Storm** — John Law's Mississippi Bubble/Banque Royale collapse (1716–1720) + French assignat hyperinflation + Hamilton's Funding & Assumption; Capital-Posture:Speculative ratchet; the deck's *only* first-class Thread card | §2.9 |
| XSCALE-08 | Crisis *(inferred — explicit "severance-Crisis" label)* | Berlin Blockade sibling to GEO-04 (near-duplicate, cross-cluster collision §4A.1), rests on the Fortify FacilityTier gate, adds an arbitration branch citing Suez 1956 | §2.2 |

### Docket B — Comparative Governance Research (9 cards, VEN/HRE/HAB/IT/CHN codes)

| ID | Family | One-line | Historical grounding (docket cite) |
|---|---|---|---|
| GOVFRIC-01 | *unresolved* | fuses VEN-SE-2 with the route/corridor lever and Arsenal dependency | VEN-SE-2 |
| GOVFRIC-02 | *unresolved* | **Guildhall Rises** — the seat-allocation Charter/Suppress Key is a genuine `stakes.source_key` candidate (WIRED-adjacent); shares the Consent-Rule lever with COURT-06/ECON-03 | HRE-5 |
| GOVFRIC-03 | *unresolved* | governance-friction cluster | HAB-5 |
| GOVFRIC-04 | *unresolved* | governance-friction cluster | IT-7 |
| GOVFRIC-05 | *unresolved* | governance-friction cluster | HAB-7 |
| GOVFRIC-06 | *unresolved* | **The Vermilion Substitution** — Verify branch resolves through `dice_pool`/`social_contest` (up-tier verification, wired today); cascade-stacking risk partner to XSCALE-01 | CHN-7 |
| GOVFRIC-07 | *unresolved* | **In the Governor's Name** — CHN-3 is the *named* WIRED FI precedent; "fully wired on current canon, playable today" | CHN-3 |
| GOVFRIC-08 | *unresolved* | PROPOSED Outlawed ledger-tag family dependency | HRE-6 |
| GOVFRIC-09 | *unresolved* | governance-friction cluster | HAB-4 |

### Docket C — Court & Standing Research (8 cards, A–H letter-code taxonomy)

| ID | Family | One-line | Historical grounding (docket cite) |
|---|---|---|---|
| COURT-01 | *unresolved* | chokepoint-gatekeeper pattern (access-monopoly-by-favor); "fully wired on current canon, playable today" via the Demotion resolver + Hold Court | D2/HAB-2 |
| COURT-02 | *unresolved* | Demotion resolver + Hold Court; "fully wired on current canon, playable today" | C4/E1/G3 |
| COURT-03 | *unresolved* | Demotion resolver + Hold Court; "fully wired on current canon, playable today" | H4/G9 |
| COURT-04 | Crisis *(confirmed by §4C: "the COURT-04 re-family added one more [Crisis]")* | re-familied to Crisis during the critic/synthesis pass | G6/CHN-8/A9 |
| COURT-05 | *unresolved* | court/standing cluster | B2/B3/B7 |
| **COURT-06** | **Ambition (confirmed)** | **The Banked Claim** — Habsburg marriage diplomacy banking a contingent claim on an occupied seat, dormant until the target line lapses; Romanos Lekapenos's staged marital climb; Ottoman damat's permanent consort-advisor ceiling; introduces the Consent-Rule lever | C1/C8/C3 |
| COURT-07 | *unresolved (differentiated, not cut — see §3 Dedup below)* | **The chokepoint gatekeeper, differentiated cut** — re-cut around `concurrent_roles` role-stacking + the Crown-Agent parallel-channel overlay (Richelieu); FI lead re-keyed from embezzlement to role-accumulation to avoid colliding with COURT-01 | A6/H7/E3 |
| **COURT-08** | **Ambition (confirmed)** | **The Protégé's Move** — cardinal-nephew's Anointed Successor: a term-limited patron installing a protégé early by waiving the gate; successor-designate/parallel_asset_pool transfer; extractive kin-gatekeeper's short horizon | A2/A5/E7 |

### Docket D — Proactive Opportunity Research (8 cards, S/O/T/F codes)

| ID | Family | One-line | Historical grounding (docket cite) |
|---|---|---|---|
| EVT-OPP-01 | Opportunity *(confirmed, under the Opportunity family header)* | **The Aqueduct/Great Works** — a Develop sub-option riding existing Prosperity/Defense/Order/Treasury stats; branches on crediting the regime vs. personal glory (the Appius move) vs. deferring the overrun | S1 |
| **EVT-OPP-02** | **Ambition (confirmed)** | **The Rival's Games** — Agrippa's aedileship (33 BCE): self-financed public works (baths, games) converting private munificence into political ascent, credit accruing to the person not the settlement | S2 |
| **EVT-OPP-03** | **Opportunity (confirmed)** | **The Perpetual Endowment** — Jakob Fugger's Fuggerei (Augsburg, 1521), an irrevocable perpetual almshousing endowment, paired with Pliny the Younger's Comum benefactions; flagship case for the Compact Ledger family (ED-SE-0019); Ω-d-bonded to OPP-04 | S12/S3 |
| EVT-OPP-04 | Opportunity *(inferred — chained "bonded pair" with OPP-03 per §4B)* | Compact upkeep — the delayed-fuse Crisis when a successor tries to breach the OPP-03 endowment Compact | O8/S12 |
| EVT-OPP-05 | Opportunity *(inferred, Docket D cluster default)* | proactive-opportunity cluster | O4 |
| **EVT-OPP-06** | **Ambition (confirmed)** | **The Confraternity Rises** — Scuola Grande di San Rocco (Venice, 1478), a lay confraternity giving prestige/office/charitable standing to cittadini/merchants locked out of the patrician Maggior Consiglio; alternate rank ladder | O10 |
| **EVT-OPP-07** | **Opportunity (confirmed)** | **The Turnpike Charter** — the Standon–Wadesmill turnpike trust (1663), England's first toll road, a self-funding inter-settlement link; introduces the route/corridor Precedent lever | T19 |
| **EVT-OPP-08** | **Opportunity (confirmed)** | **The Relic Redeemed** — Louis IX's acquisition of the Crown of Thorns (1239), redeemed from Venetian creditors (not bought), enshrined in the purpose-built Sainte-Chapelle to anchor Capetian sacral legitimacy | F10 |

**Confirmed family total (11 of 58):** Opportunity 6 (OPP-01/03/04/05/07/08), Ambition 4 (COURT-06/08,
OPP-02/06), Thread 1 (XSCALE-07). **Source-asserted aggregate (§4C), not all individually attributable:**
Crisis 22/59, Petition 6/59, Intrigue 7/59 (pre-merge counts; the deck landed at 58 after COURT-07 was
differentiated rather than cut, so these totals need a −1/reallocation the source does not spell out
card-by-card). **Friction: not stated by the source at all** — this compendium infers a 13-card residual
(59 − 46) but assigns it to no specific IDs; treat the "Crisis *(inferred)*" cells above (drawn from the
explicit §4C "every high-Π cluster defaulted to Crisis" line, applied to the climatic and cross-scale
clusters) as the *strongest* available signal, not a ratified per-card family.

---

## 2. The 28-card Goldenfurt deck

Slice S-006, `designs/territory/goldenfurt_slice/event_deck.md`. Unlike the grounded deck, Goldenfurt cards
are bespoke settlement-instance content built around named local NPCs (Magistrate Hedda, Grainmaster Orsk,
Bailiff/agent Konrad, Curate Wessel, ranger/RM contact Greta, dock-fixer Tomas, smuggler Niflhel, widow
Mertha) rather than citations to a specific historical case — so this table has no "historical grounding"
column; §3 below explains why that changes the dedup approach for this deck.

| ID | Family | One-line |
|---|---|---|
| G101 | Petition | "Only Sons" — Mertha's son taken in the war-levy; Hold Court / Comply / Bargain / ignore |
| G102 | Petition | Guild foothold dispute — Brun vs. the Guild toll; court for Brun / for Orsk / Treat |
| G103 | Petition | Aldith begs relief from falling Prosperity/Orsk hoarding; Sponsor / Develop-via-Guild / ignore (seeds G402 Famine) |
| G201 | Friction (Directive: Extract) | "The War-Levy" — Bailiff Ems delivers the Crown's writ (forty men, a tenth of the grain); Comply / Bargain / Defy-Divert |
| G202 | Friction (Directive: Tax) | Harvest tithe; Comply / Defy / Bargain — collides with G103 |
| G203 | Friction (Suppress) | "Shut the circle" — Rune-Meld/RM foothold + Church Attention rising; Force / Shelter / token |
| G204 | Friction (the Geneva trap) | "The Curate's Offer" — Wessel offers parish hands to steady Order at the cost of Church-infra creep; Keep Order: Consent / Clergy / Decline / Bargain |
| G205 | Friction (Directive: Host) | Quarter a Hafenmark envoy in your one Wing — capacity pressure; bump the inner circle or Defy |
| G301 | Opportunity | Harvest fair; Sponsor / attend / skip |
| G302 | Opportunity | A loyal sergeant seeks service — recruit (faction-emergence knot) / decline |
| G303 | Opportunity | Hedda offers alliance — ally (Stage 2→3 progress, Crown break) / decline (the deck's worked-example payoff) |
| G401 | Crisis | "Conscription Riot" — the widow's grief becomes a crowd; Keep Order: Force / Concede / Hedda mediates |
| G402 | Crisis | Famine (Prosperity 0 or G103 ignored ×2); Sponsor relief / beg Crown (Debt) / let Orsk "relieve" (profiteering) |
| G403 | Crisis | Black market entrenches (Order ≤1, 2+ seasons); Investigate→crack down / tolerate |
| G404 | Crisis | Raid at the ford — mandatory scene, often the cost of defying G201; Militia defend / emergency Fortify / abandon |
| G501 | Intrigue | The widow's son returns embittered (seeded by G101-comply) — RM recruit or rioter; Counsel / ignore |
| G502 | Intrigue | "Orsk's Whisper" — the Grainmaster buys the Bailiff's ear; Investigate / Confront / Concede the charter |
| G503 | Intrigue | Wessel's letter to the Inquisitor; Investigate→expose him as informer / appease / ride it out |
| G504 | Intrigue | Niflhel calls a favour through Tomas; Comply covert / refuse / turn him in (may implicate Hedda → G505) |
| G505 | Intrigue (the keystone) | "The Magistrate's Brother" — proof Hedda shielded her smuggler brother; Bury (warn) / Bury (hold, coercive leverage) / Expose |
| G601 | Ambition (fires at G01 progress ≥4) | "Hedda's Bid" for the Kronmark seat — resolution branches on allied/estranged/compromised relationship state |
| G602 | Ambition (fires at Orsk progress ≥3) | Charter gambit / engineered shortage — by-state fork on toll-cap Precedent / Guild-funded / contested |
| G603 | Ambition (fires at Wessel progress ≥4) | Chapel→Church — the Geneva trap closes; durable Order but Church-infra seizure vector, removal needs Mass Battle/Mandate Challenge |
| G604 | Ambition (fires at Tomas progress ≥3) | The river economy goes load-bearing — by-state fork on co-opted/cracked-down/co-governed |
| G605 | Ambition (fires at Greta progress ≥5) | The public Einhir rite — Tolerate (Precedent, PS surge) / Disperse by force (uprising branch, Church Attention spike) |
| G606 | Ambition (fires at G06 progress ≥4) | "The Bailiff's Report" — recall threat; buried (if leverage held) / faction-emergence backfire / Submit to audit (sustainable Just path) / Recall scene |
| G701 | Thread | "The stone circle stirs" — Weaving→Order+1 / Dissolution→Defense−1 & Order−1; ties Greta to the Thread layer |
| G702 | Thread | "The forgotten field" — crops grow wrong, time slips; Investigate→harvest residue / Mend |

**Family totals (per the deck's own §Coverage table):** Petition 3, Friction 5, Opportunity 3, Crisis 4,
Intrigue 5, Ambition 6, Thread 2 = **28**.

---

## 3. Dedup note — grounded/Goldenfurt overlap against the ~94-card HEV catalogue

**Framing.** The 58-card grounded deck cites specific historical cases the same way the HEV catalogue does
(a named event + era + docket citation), so genuine same-case duplication is checkable directly. Goldenfurt,
by contrast, is a bespoke settlement instance built around invented local NPCs — its cards are *worked
applications* of generic mechanics (Directive/Levy Friction, Famine Crisis, Confraternity/Guild Ambition),
not citations to a specific historical case, so there is no case-identity dedup to run against it; its
overlap risk is structural (mechanic/lever reuse), covered at the end of this section.

### 3.1 Confirmed same-case overlaps (grounded deck ↔ HEV catalogue) — cross-reference, do not duplicate

| Grounded-deck card | HEV catalogue card | Same historical case | Recommended compendium handling |
|---|---|---|---|
| GEO-04 (The Severed Enclave) | **HEV-BLOC-09** — Berlin Blockade (1948–49), `22_blockade_embargo_chokepoint.md` | Identical case (Soviet blockade of land/water routes to West Berlin, Allied airlift) | GEO-04 is the settlement-scale mechanical elaboration (Fortify-tier precondition, response branches, ripples); HEV-BLOC-09 is the catalogue's canonical historical-grounding citation. Cross-reference GEO-04 → HEV-BLOC-09 as its source citation; do not re-author a second historical-grounding paragraph for GEO-04. |
| XSCALE-08 (Severed Enclave, peninsula-scale sibling) | **HEV-BLOC-09** — Berlin Blockade | Identical case, shared with GEO-04 (the deck's own §4A.1 flags GEO-04/XSCALE-08 as a near-duplicate pair — "90% the same card in two clusters," a MERGE candidate) | Same handling as above, plus resolve the source's own open MERGE recommendation (fold XSCALE-08's arbitration branch into GEO-04, or re-scope XSCALE-08 explicitly to peninsula/coalition scale) before this compendium treats both as final canon. |
| XSCALE-08's arbitration branch (Suez override-the-battlefield) | **HEV-BLOC-10** — Suez Crisis & Canal Closure (1956), same file | Identical case | Cross-reference only; do not duplicate the Suez grounding paragraph. |
| XSCALE-06 (economic single-source severance, no-Bargain) | **HEV-BLOC-08** — ABCD Line & US Oil Embargo on Japan (1940–41), same file | Identical case (coalition embargo cutting off strategic resources ahead of Pearl Harbor) | Cross-reference XSCALE-06 → HEV-BLOC-08. |
| **XSCALE-07 (The Paper Storm, Thread)** | **HEV-COIN-06** — John Law's Mississippi Bubble/Banque Royale collapse (1716–1720), `29_debasement_fiscal_default.md` | Identical case | The single densest overlap in the corpus (see next two rows) — XSCALE-07 braids three separate HEV cases into one Thread card. |
| XSCALE-07 (same card, assignat coupling) | **HEV-COIN-07** — French assignat hyperinflation (1790s), same file | Identical case | Cross-reference; do not duplicate. |
| XSCALE-07 (same card, the "consolidation off-ramp") | **HEV-COIN-08** — Continental currency collapse / Hamilton's Funding & Assumption (1770s–1790), same file | Identical case | Cross-reference; do not duplicate. XSCALE-07 is effectively a *fusion card* of HEV-COIN-06/07/08 plus the new Capital-Posture ledger mechanic — the compendium should present it as "derived from HEV-COIN-06/07/08" rather than a fourth independent grounding. |

### 3.2 Near-neighbor overlaps (same family/dynasty/theme, distinct specific case — flag, do not merge)

| Grounded-deck card | HEV catalogue neighbor | Relationship |
|---|---|---|
| EVT-OPP-03 (The Perpetual Endowment — Fugger's Fuggerei, Augsburg 1521) | **HEV-TRADE-02** — Fugger mining monopolies / Habsburg election financing (HRE, 1519), `210_trade_monopoly_merchant_capital.md` | Same historical dynasty (the Fuggers) and adjacent year, but a **distinct specific case** (perpetual charitable almshousing endowment vs. mining-monopoly election financing) — not a duplicate, but the compendium should note the shared-actor risk if both cards are drawn in the same campaign (the same NPC lineage appearing in two unrelated card contexts). |
| ECON-01 (Capital-Posture:Debased, the general debasement/Capital-Posture ratchet mechanic) | The entire **HEV-COIN-\*** cluster (10 cards, `29_debasement_fiscal_default.md`: Roman Third-Century Crisis, England's Great Debasement, Bardi & Peruzzi default, Ottoman akçe debasement, Estates-General summons, Weimar/Zimbabwe hyperinflation, plus the three cases already merged into XSCALE-07) | Family-level convergence, not case-identity: ECON-01/ECON-05 supply the *generic mechanic* (the Capital-Posture ledger family, R-1) that any future card drafted from a specific HEV-COIN case should route through, rather than re-deriving a parallel debasement mechanic. Flag for the module-adjudicator pass: **any new card grounded in an as-yet-unused HEV-COIN case (01–05, 09–10) should bind to the existing Capital-Posture lever, not invent a new one.** |
| GOVFRIC-01 (fuses VEN-SE-2 with the route/corridor lever and Arsenal dependency) | **HEV-WATER-09** — Venice's river diversions / Magistrato alle Acque, `25_flood_drought_siltation.md`; **HEV-PLAGUE-05** — Venice Lazzaretto/1630–31 quarantine failure, `27_plague_epidemic.md` | Same city (Venice) across three cards, three distinct institutional mechanisms (Arsenal/trade-corridor governance vs. hydraulic-works standing institution vs. public-health failure) — no case overlap, flagged only so a future "Venice cluster" audit doesn't mistake three legitimately distinct cases for redundancy. |
| The whole climatic/geographical cluster (CLIM-01…09) | **HEV-QUAKE-\*** (9), **HEV-WATER-\*** (10), **HEV-FAM-\*** (9), **HEV-PLAGUE-\*** (9), **HEV-CLIM-\*** (9) — 46 catalogue cards across five files | Structural risk, not a confirmed duplicate: Docket A's climatic/geographical sub-sections (§2.4/§2.5/§2.7/§2.8) plausibly draw from the same case-space the HEV catalogue independently mined (both corpora cover famine, quake, flood, plague, storm). **This compendium could not verify individual CLIM-01…09 groundings against specific HEV IDs** because the grounded-deck source does not give per-card historical-case names for these nine cards (only §2.x sub-section citations — see Table 1's "unresolved" cells). **Flag as an open verification task**, not a resolved dedup: before compiling a combined climatic/geographical card list, someone with access to the underlying `historical_concerns_action_catalogue_v1` docket needs to name each CLIM card's specific historical case and re-run this cross-reference. |

### 3.3 Goldenfurt — structural (mechanic-level) overlap only

Goldenfurt's 28 cards do not carry individual historical-case citations, so no row-by-row dedup against the
HEV catalogue applies. The overlap that *does* exist is mechanic-level:

- **G201 (The War-Levy) / G202 (Harvest tithe)** reuse the Directive:Extract/Tax friction shape that
  underlies the entire grounded-deck governance-friction cluster (GOVFRIC-\*) and several HEV-\* Friction
  cards (e.g. HEV-SIEGE-06 Colonial Billeting/Quartering Acts, HEV-BLOC-05 Barbary Tribute). No specific-case
  duplication — Goldenfurt's levy is a Solmund-peninsula-generic instance of the same lever, not a citation
  of any one historical event.
- **G402 (Famine)** is a generic Famine Crisis instance; the HEV-FAM-\* cluster (9 cards: Great Famine
  1315–17, Bengal 1770, Irish Famine, etc.) supplies the historical grounding *family* this mechanic draws
  from, but G402 does not cite any single one of them.
- **G603 (Chapel→Church, the Geneva trap)** and **G204 (The Curate's Offer)** are the same "sacral
  institution absorbs a secular Order function" mechanic that HEV catalogue cards address structurally
  (e.g. the Church-Attention/Assessment machinery), again without a specific-case citation to dedup against.
- **Recommendation:** treat Goldenfurt as a *worked instance layer* sitting on top of the grounded deck's
  and HEV catalogue's mechanics — the compendium should cross-reference Goldenfurt cards to the *lever or
  family* they instantiate (Directive-Friction, Capital-Posture, Compact, Consent-Rule, etc.), not to a
  specific historical case, since none is claimed.

---

## 4. Combined family-count totals across all three sources

| Family | 58-card grounded deck | 28-card Goldenfurt deck | ~94-card HEV catalogue | Combined |
|---|---|---|---|---|
| Petition | 6 *(§4C aggregate, pre-merge /59)* | 3 | 4 | 13 |
| Friction | **13 *(inferred residual — not asserted by the source; see §1 caveat)*** | 5 | 15 | 33 |
| Opportunity | 6 *(confirmed)* | 3 | 9 | 18 |
| Crisis | 22 *(§4C aggregate, pre-merge /59)* | 4 | 56 | 82 |
| Intrigue | 7 *(§4C aggregate, pre-merge /59)* | 5 | 7 | 19 |
| Ambition | 4 *(confirmed)* | 6 | 2 | 12 |
| Thread | 1 *(confirmed)* | 2 | 1 | 4 |
| **Total** | **59** *(pre-merge; final deck is 58 after COURT-07 was differentiated rather than cut into COURT-01 — see the source's §3)* | **28** | **94** | **181** (180 using the post-merge 58) |

**How the HEV catalogue column was built.** Direct enumeration of the family marker on every
`### HEV-...` heading across the ten `2*.md` files, taking the *first-listed* family where a card carries a
compound label (e.g. `HEV-SUCC-02 · Friction→Crisis` counted as Friction; `HEV-WATER-04 ·
Opportunity→Friction/Crisis` counted as Opportunity). Several HEV cards are explicitly multi-family
chain cards in their own text (e.g. `HEV-WATER-08 · Opportunity→Friction→Ambition`, `HEV-CLIM-09 · Crisis
chain (Friction→multi-settlement)`) — the single-family total above under-represents that chaining; a
finer accounting would need a per-card multi-family tally, which this pass did not attempt (flagged as a
follow-on refinement, not done here to avoid asserting numbers beyond what a straight heading-count
supports).

**Reading the combined table.** Crisis dominates every corpus (22/58 grounded, 4/28 Goldenfurt, 56/94 HEV —
all in the 15–60% range), consistent with the grounded deck's own §4C finding that Crisis is
over-represented ("a deck this Crisis-heavy will feel relentless in play"). Thread is thin everywhere (1
grounded, 2 Goldenfurt, 1 HEV = 4 total across ~180 cards) — the grounded deck's own recommendation to
author "3–5 more first-class Thread cards" (§4C) reads as even more urgent once the HEV catalogue is folded
in, since the catalogue does not supply additional Thread depth either. Ambition is Goldenfurt's strongest
family (6/28, NPC-firing by design) but the corpus's thinnest elsewhere (4 grounded, 2 HEV) — Goldenfurt's
NPC-ambition-ladder pattern (G601–G606) is a candidate template for authoring the grounded deck's own
under-represented Ambition shelf.

---

## 5. Open follow-ups this map surfaces

1. **Resolve the GEO-04/XSCALE-08 MERGE** the grounded deck's own §4A.1 leaves open, before either card is
   compiled into a combined canonical list — right now both would independently cross-reference HEV-BLOC-09,
   which is the duplication risk made concrete.
2. **Name the CLIM-01…09 specific historical cases.** The grounded-deck source only cites §2.x sub-sections
   for this cluster, not named events — §3.2 above flags this as the single largest unresolved dedup gap
   (46 potentially-adjacent HEV cards across QUAKE/WATER/FAM/PLAGUE/CLIM that could not be checked).
3. **Route future Capital-Posture-family cards through ECON-01/ECON-05/XSCALE-07**, not a re-derived
   mechanic, per §3.2's HEV-COIN convergence flag.
4. **Author 3–5 new Thread cards** — the deficit is corpus-wide (4/181 combined), not just a grounded-deck
   problem as originally scoped in that source's own §4C.
5. **This compendium section itself needs a family-confirmation pass** against the grounded-deck's original
   58 card bodies (not yet fully written out in the source document) before the "inferred"/"unresolved"
   cells in Table 1 can be promoted to ratified canon — flagged prominently per this repo's ED-1094 rule
   that a PROPOSED item held back from full ratification must say so loudly, not silently.
