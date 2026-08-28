## Manifest

| path | lines | records | note |
|---|---|---|---|
| `audit/2026-07-12-governance-compendium/_workings_joined.md` | 2734 | 63 | Single joined file, 16 fragments, read in full (all 2734 lines). Fragments in scope: event-card integration map (19–306), §2.10 trade (309–444), §2.1–2.9 HEV catalogue sections (447–1248, 94 cards verified by direct `### HEV-` count), §30 ripple chains (1251–1544, 12 chains, unvetted per its own header), four re-evaluation sets (1547–2734, 44 items). No sub-section had zero in-scope content. |

## Records

```yaml
- id: H8B-001
  name: Event-Card Corpus Overview
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:20
  system: settlement-governance
  touches: [faction-strategy, economy-accounting]
  slice: content
  statement: >-
    Valoria's event-card material exists in three independently-authored corpora never
    cross-referenced before this compendium pass: the 58-card grounded deck (PROPOSED,
    `designs/audit/2026-07-11-grounded-event-card-deck/`), the 28-card Goldenfurt starter deck
    (bespoke settlement instance, slice S-006), and the ~94-card HEV historical catalogue —
    the 94 count independently verified by direct enumeration of every `### HEV-` heading across
    the ten source sections. Combined family totals across all three: Petition 13, Friction 33,
    Opportunity 18, Crisis 82, Intrigue 19, Ambition 12, Thread 4 (180 combined; 181 counting
    the grounded deck's pre-merge internal count of 59).
  status: audit-finding

- id: H8B-002
  name: Event-Card Dedup — Unresolved MERGE and Unverifiable Cluster Overlap
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:229
  system: settlement-governance
  touches: [territory-world]
  slice: gap
  statement: >-
    The grounded deck's own §4A.1 flags GEO-04 and XSCALE-08 as near-duplicate "Severed Enclave"
    cards (both citing HEV-BLOC-09, the Berlin Blockade) with an open MERGE recommendation this
    compendium found still unresolved. Separately, the climatic/geographical cluster CLIM-01…09
    cites only §2.x sub-section numbers rather than named historical cases, so its overlap
    against 46 HEV cards spanning QUAKE/WATER/FAM/PLAGUE/CLIM could not be checked and is an
    open verification task, not a resolved dedup.
  status: audit-finding

- id: H8B-003
  name: Confirmed Same-Case Overlaps — Grounded Deck vs HEV Catalogue
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:210
  system: settlement-governance
  slice: content
  statement: >-
    Eight grounded-deck cards are confirmed to cite the identical historical case as a specific
    HEV catalogue card (e.g. GEO-04/XSCALE-08 → HEV-BLOC-09 Berlin Blockade; XSCALE-06 →
    HEV-BLOC-08 ABCD Line). The densest is XSCALE-07 "The Paper Storm," a single Thread card
    fusing three separate HEV-COIN cases (HEV-COIN-06/07/08: John Law's Mississippi Bubble, the
    French assignat collapse, and Continental-currency/Hamilton's Funding & Assumption). The
    compendium recommends cross-referencing these pairs rather than re-authoring a second
    historical-grounding paragraph for each.
  status: audit-finding

- id: H8B-004
  name: HEV Event-Card Resolution Model
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:315
  system: settlement-governance
  touches: [faction-strategy, territory-world]
  slice: process
  statement: >-
    Every HEV card follows one fixed shape, confirmed across all 94 cards: a boolean Trigger
    predicate over settlement/faction state → three Response branches (Comply/Bargain/Defy, each
    with stat deltas and Ledger-tag writes) → a Follow-on that seeds a later card by writing a
    durable tag, raising Π, or setting a hidden stat → an "Introduces (Action)" field naming the
    new verb/Directive-type/method the card adds to the governance menu → a closing Loop
    paragraph stating the incentive the mechanism creates. This is PROPOSED source-audit prose
    describing an authoring convention, not built code.
  status: designed-canonical

- id: H8B-005
  name: HEV Cards Propose 8 Directive Types Beyond the Baseline's 6
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:531
  system: settlement-governance
  touches: [faction-strategy]
  slice: gap
  statement: >-
    The action catalogue baseline (`research/cross_scale_action_catalogue_v1.md:250`) lists six
    Directive types (Extract/Tax/Suppress/Install/Host/Cede). The HEV card corpus proposes at
    least eight more, never reconciled against that census: Embargo (targets a third faction,
    line 531), Multilateral Embargo (line 587), Quarter (sibling to Host, line 658), Recall
    (disbands an appanage prince's forces, line 508), Relief (line 1118) and Remit (tax/tribute
    forgiveness, lines 1126/1158), Directive: Fiscal Reform (reverse-scale — the PA issues it to
    itself, line 1205), and Divert Logistics to Muster (a first-class option, line 935). None are
    built or ratified; all are PROPOSED prose from a 2026-07-12 pre-restructure audit.
  status: audit-finding

- id: H8B-006
  name: Standing Institutions as Pre-Crisis Mitigation — a Recurring HEV Shape
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:826
  system: settlement-governance
  slice: content
  statement: >-
    At least eight HEV cards independently propose a "standing institution" — a persistent
    Facility whose prior investment determines a later Crisis card's severity roll instead of
    reacting after the fact: Water Board (line 826), Water Magistracy (line 866), two separate
    Ever-Normal Granary proposals (lines 846, 1063), Grain Ministry (line 987), River Conservancy
    Directorship (line 796), Coalition Fortify Pool (line 642), Sanità Lazzaretto (line 1047), and
    Civic Granary (line 1118). None exist in the baseline's settlement-governance verb list; all
    are PROPOSED prose only.
  status: audit-finding

- id: H8B-007
  name: Ledger TAG_KINDS is a Closed 5-Kind Enum — "Compact"/"Charter"/"Assessment" Are Not In It
  source: systems/settlements/sim/ledger.py:30
  system: settlement-governance
  touches: [faction-strategy, personnel-roster]
  slice: gap
  formula: 'TAG_KINDS = {"Precedent", "Grudge", "Debt", "Reputation", "Leverage"}'
  statement: >-
    Verified directly against code: `systems/settlements/sim/ledger.py:30` ships a closed
    five-member tag enum whose fifth kind is Leverage, not Compact. Design prose across this
    corpus — the settlement-governance baseline's own "five tag families" list, PR#119's §1.3a,
    and at least nine distinct proposals re-evaluated in this file (HAB-5, CHN-4, CHN-5, CHN-6,
    HRE-3, HRE-4, HRE-5, VEN-SE-2, VEN-SE-3, SE-JP2, SE-JP3) — assumes or proposes a "Compact,"
    "Charter," or "Assessment" tag family with no representation in shipped code. Any of those
    names crossing into an implementation must resolve onto one of the five real kinds (most
    often Leverage or Debt) rather than being authored as a new slot.
  status: built
  status_evidence: systems/settlements/sim/ledger.py:30

- id: H8B-008
  name: "THR-01 — The Debasement→Famine→Coup Spiral"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1267
  system: economy-accounting
  touches: [faction-strategy, settlement-governance]
  slice: process
  statement: >-
    A five-step cross-domain chain: Roman-style `Levy:Debase` stacks a Capital-Posture:Debased
    tag → a Gresham's-Hoarding Crisis stalls Prosperity → the thinner tax base satisfies an
    Ancien-Régime-style Fiscal Reform trigger, whose Defy branch writes a hidden Concealed-Deficit
    Precedent → a General-Crisis Cooling flag plus that concealed deficit lets a Great-Famine-1315
    card fire uncushioned → the famine's unresolved-Needs follow-on writes Reputation:Hated and
    Grudge, satisfying a Muscovite-Time-of-Troubles pretender Intrigue that unseats the dynasty.
    Extracted verbatim from the source audit and flagged there as not yet vetted against the live
    card corpus.
  status: audit-finding

- id: H8B-009
  name: "THR-02 — Chokepoint Toll Funds a Private Army"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1293
  system: economy-accounting
  touches: [faction-strategy]
  slice: process
  statement: >-
    A toll chokepoint accrues foreign-faction Debt whose follow-on seeds a "rival contests the
    strait" Friction; the contesting rival, denied a Compact, routes trade underground, satisfying
    a Kongo-style "untaxed trade node" trigger whose un-Ratified lineage wealth compounds into
    private Military — exactly the Toluid-style mandatory-contest condition (≥2 contenders each
    holding independent Military) at the next succession. Terminal payoff: the toll the governor
    built to enrich the settlement finances the appanage strength that fractures the faction; the
    un-pulled lever is the Recall Directive. Not yet vetted against the live card corpus.
  status: audit-finding

- id: H8B-010
  name: "THR-03 — Single-Commodity Develop → Blockade → Runner Corruption → Plague"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1314
  system: economy-accounting
  touches: [settlement-governance]
  slice: process
  statement: >-
    A single-commodity Develop concentration makes a faction blockade-vulnerable; the blockade's
    follow-on seeds garrison-funding-collapse Crises, satisfying a Spanish-Fury-style
    unpaid-garrison mutiny trigger whose follow-on writes contagion Grudge at loyalist
    settlements; funding blockade-runners to compensate seeds a corruption Intrigue, and the
    runner corridor is an unvetted long-distance route satisfying a Black-Death-style Contagion
    Vector condition whose relief shipment near-guarantees a Plague Crisis next season. Terminal
    payoff: a commodity-concentration choice becomes an epidemic. Not yet vetted against the live
    card corpus.
  status: audit-finding

- id: H8B-011
  name: "THR-04 — Neglected Dike Diverted to War → Flood → Relocation → Charter Fight"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1338
  system: territory-world
  touches: [settlement-governance, faction-strategy]
  slice: process
  statement: >-
    A war Directive diverts dike Maintenance; a severe-storm roll fires a St.-Elizabeth's-Flood-
    style Crisis whose follow-on seeds Petition pressure toward a standing institution if the
    settlement survives, or drops its Weight below the survivability floor if not — satisfying a
    Val-di-Noto-style relocation trigger gated by Charter-holder consent via Quo Warranto. A
    hostile Charter-holder converts the disaster into a Revoke-Franchise/Nationalize-Charter fight
    whose arbitration writes a "charters contestable by force" Precedent lowering every future
    bypass bar. Terminal payoff: a diverted dike ends in a constitutional precedent about land
    ownership. Not yet vetted against the live card corpus.
  status: audit-finding

- id: H8B-012
  name: "THR-05 — Un-Staged Muster Spreads Plague That Strips the War Machine"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1360
  system: mass-battle-seam
  touches: [settlement-governance]
  slice: process
  statement: >-
    A frontier Conquest followed by an un-staged Muster redeploy (Antonine-Plague pattern) fires
    an epidemic in every interior settlement receiving troops; its follow-on seeds a
    faction-level "muster route is a plague road" Friction lowering the faction's own
    mil-advantage signal, and the interior Order/Prosperity hits satisfy a Chongzhen-style trigger
    where `Granary_FacilityTier==0` (Treasury went to the war, not granaries), whose follow-on
    seeds a rebel-warlord Ambition that becomes an open Conquest-target for a rival. Terminal
    payoff: the faction's own aggressive Muster manufactures the rebellion a rival then exploits;
    the un-pulled lever is Staged Demobilization. Not yet vetted against the live card corpus.
  status: audit-finding

- id: H8B-013
  name: "THR-06 — Overcrowding Refuge → Plague Kills the Patron → Contested Succession"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1382
  system: faction-strategy
  touches: [settlement-governance]
  slice: process
  statement: >-
    Refuge Walls without same-season relief stacks an Overcrowding tag; a Plague-of-Athens-style
    Crisis's follow-on, on a failed patron-NPC mortality check, seeds a succession vacancy that
    satisfies a Year-of-the-Four-Emperors-style Anarchy trigger (weak heir, comparable-Standing
    rivals); a Donative-bought military win reseeds the Crisis unless Ratify closes it, and if the
    Extract-Succession-Oath option was never taken, the resulting G≤1 SPLIT seeds recurring
    "Baronial Free Agency." Terminal payoff: a defensive-overcrowding choice at one settlement
    cascades into a nineteen-winter faction fracture. Not yet vetted against the live card corpus.
  status: audit-finding

- id: H8B-014
  name: "THR-07 — Siltation → Merchant Exodus → Merchant-Capital Captures the Ladder"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1405
  system: economy-accounting
  touches: [faction-strategy]
  slice: process
  statement: >-
    Un-dredged harbor SiltLevel plus a Guild tariff Comply fires a Merchant-Exodus Crisis whose
    follow-on permanently transfers trade-Reputation to a named rival settlement; the rival's
    merchant surge satisfies a Fugger-style Underwrite trigger, and repeated Underwrite-Comply
    seeds an Ambition where the financier claims a Ministry/Consulta seat; with the Crown
    fiscally dependent, a Plassey/Jagat-Seth-style Intrigue trigger is met and a funded coup
    installs a diwani-equivalent Levy assignment for the financier. Terminal payoff: a silted
    harbor ends with a merchant house running the province. Not yet vetted against the live card
    corpus.
  status: audit-finding

- id: H8B-015
  name: "THR-08 — Cooling Epoch → Correlated Famine → Cascade → Mass Demotion → Recovery Incapacity"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1427
  system: faction-strategy
  touches: [settlement-governance]
  slice: process
  statement: >-
    A world-level Cooling flag raises Π everywhere; a faction that never builds a relief Ministry
    accumulates roster-wide Grudge whose follow-on seeds a multi-settlement famine-Crisis cascade;
    the correlated Grudge triggers concurrent Demotion Magnitude events on the faction's own
    ladder, stripping the Standing-4+ governors needed to authorize Remit/relief, so the next
    Cooling-arc Π spike lands on a leaderless roster and a Norse-Greenland-style implicit
    abandonment plays out at multiple frontier settlements at once. Terminal payoff: Remit plus a
    relief Ministry were the un-built levers at step 1. Not yet vetted against the live card
    corpus.
  status: audit-finding

- id: H8B-016
  name: "THR-09 — Fixed Quota Through Drought → Resurvey Neglect → Outlawry"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1451
  system: economy-accounting
  touches: [settlement-governance]
  slice: process
  statement: >-
    A Bengal-1770-style fixed-quota Precedent sits latent as a silent check; a Cocoliztli-style
    megadrought fires with `seasons_since_Survey>=8`, so Extract charges a stale-high
    `assessed_base` below subsistence, whose follow-on seeds a repeat harder-Ob Crisis each season
    and writes Grudge(Crown) raising the next Survey's Ob; the compounding Grudge plus a
    mass-mortality flag satisfies a Drogheda-style trigger whose Outlawed-tag follow-on raises
    Grudge/Intrigue in the territory for generations. Terminal payoff: never refreshing the
    Survey ends in a confiscation regime; the un-pulled lever was Emergency Resurvey. Not yet
    vetted against the live card corpus.
  status: audit-finding

- id: H8B-017
  name: "THR-10 — Cheap Hulls → Storm Loss → Locked Out of the Fix → Embargo Vulnerability"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1472
  system: economy-accounting
  touches: [faction-strategy, mass-battle-seam]
  slice: process
  statement: >-
    A cheap-Levy fleet (Spanish-Armada-style) meets a Rendezvous-Failure Friction forcing a
    high-exposure route; the ensuing storm Crisis writes Debt on the Crown, which gates the
    Treasury needed for the Purpose-Built-Galleon upgrade, locking the faction out of its own
    mitigation; the residual Debt, if concentrated in one Sponsor, satisfies an Edward-III-style
    default trigger whose Outlawed-tag follow-on removes that Sponsor as a financier, and with
    the navy gutted the faction's single-source resupply becomes an ABCD-Line/Multilateral-Embargo
    target. Terminal payoff: the coalition embargo collapses the response fork to Comply/Defy;
    Storm-Season Withdrawal and Purpose-Built Galleon were the un-pulled levers. Not yet vetted
    against the live card corpus.
  status: audit-finding

- id: H8B-018
  name: "THR-11 — Quarantine Complacency → Trade-Fair Bribe → Plague → Assassination"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1495
  system: settlement-governance
  touches: [faction-strategy]
  slice: process
  statement: >-
    A high-Standing Guild's patronage leverage meets a Marseille-style Quarantine Waiver Petition
    trigger; a Ratify voids the Sanità's Quarantine_Tier for one shipment, whose follow-on spikes
    a Venice-Lazzaretto-style Plague Crisis to near-certain; resolving it via Segregation Camps
    writes Grudge(magnitude≥2) whose follow-on seeds an assassination-class Intrigue, and a
    successful assassination forces a Recall/succession scene and a Π spike. Terminal payoff: a
    merchant guild's trade-fair bribe three steps back kills the governor; the structural root is
    the unbuilt sanitation Develop that made Force "necessary." Not yet vetted against the live
    card corpus.
  status: audit-finding

- id: H8B-019
  name: "THR-12 — Untaxed Mine Wealth → Depletion Revolt → Standing Transfer"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1517
  system: economy-accounting
  touches: [faction-strategy, territory-world]
  slice: process
  statement: >-
    Potosí-style Mita conscription buys time against OreGrade depletion, accruing Grudge toward
    an Uprising Crisis plus a permanent PS-decline tag; as the mine plays out, an Erzgebirge-style
    fixed-charter Friction fires (no Tribunal renegotiation), whose follow-on seeds a "New Rush"
    Opportunity at a rival settlement as miners and capital migrate; the source settlement's
    collapsing Prosperity/PS plus the rival's surge satisfies a Mesopotamia-salinization/
    Sumer-to-Akkad endgame pattern transferring Standing/Recognition on the faction ladder to the
    rival. Terminal payoff: resource-geography playing out rewrites the rank ladder; Amalgamation
    and Tribunal renegotiation were the un-pulled levers. Not yet vetted against the live card
    corpus.
  status: audit-finding

# ===== Re-evaluation set 1: China & Byzantium (14 items) =====

- id: H8B-020
  name: "BYZ-1 — Office/Dignity Split, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1574
  system: personnel-roster
  touches: [faction-strategy]
  slice: mechanic
  statement: >-
    Proposal forks the faction-rank Standing stat into revocable Office + sticky Dignity. Prior
    NERS verdict DISTILL (confirmed) on M-6/Mu-alpha/T-fail defects in its ED-776 re-scoping.
    Re-evaluation against built code: RECONCILE, not REDUNDANT — the built `Settlement.legitimacy`/
    `popular_support` fields are a similarly-shaped revocable/sticky pair but are INERT (never
    read/written in `sim/`) and operate at a different scale (settlement, not individual FA rank),
    so they don't duplicate BYZ-1, but the two "decoupled sticky-vs-revocable" shapes now coexist
    in the corpus. Does not change the NERS verdict; adds a terminology-collision warning for
    whoever eventually wires the inert fields.
  status: audit-finding

- id: H8B-021
  name: "BYZ-3 — Guarantor Guild Entry, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1605
  system: personnel-roster
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is joint-liability guild-entry sponsorship writing a "Vouched-For" tag. Prior NERS
    verdict REFINE (confirmed) on unquantified magnitudes. Re-evaluation against built code:
    COLLIDES (partial) — `ledger.py`'s shipped `TAG_KINDS` has exactly five kinds
    (Precedent/Grudge/Debt/Reputation/Leverage) with no sixth slot, so "Vouched-For" cannot be a
    standalone tag family and must be authored as a typed Debt or Leverage instance instead. This
    changes the NERS verdict by adding a concrete required fix beyond quantification: re-type the
    tag before promotion.
  status: audit-finding

- id: H8B-022
  name: "BYZ-6 — Consolidated Command (Doux), Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1632
  system: faction-strategy
  touches: [settlement-governance]
  slice: mechanic
  formula: "AP = 2 + Σ facility_tier (pooled, across member settlements)"
  statement: >-
    Proposal is a pooled-AP multi-settlement governor with concentrated revolt risk (Π = max of
    members). Prior NERS verdict REFINE (overturned from DISTILL), asking for a pooled-AP cap
    formula NERS itself could not supply. Re-evaluation against built code: STILL-VALID and now
    promote-ready — the built per-settlement formula `AP = 2 + facility_tier` sums exactly to
    BYZ-6's proposed pooled formula, resolving NERS's single biggest blocker with real numeric
    grounding. This changes the verdict from "REFINE, blocked" toward promote-ready.
  status: audit-finding

- id: H8B-023
  name: "BYZ-7 — Pronoia Grant, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1661
  system: personnel-roster
  touches: [faction-strategy]
  slice: mechanic
  statement: >-
    Proposal grants revenue-without-governance to an individual FA rank-holder. Prior NERS
    verdict MERGE (confirmed) — its own source instructs reusing §3.3a's formula, and it is
    mechanism-identical to that section's `floor(charter_age_seasons/8)` Quo Warranto logic.
    Re-evaluation against built code: REDUNDANT, unaffected — `sim/territory/` doesn't model a
    rank-holder/governor split at all, so the built substrate neither strengthens nor weakens the
    design-doc-internal MERGE call. Does not change the verdict.
  status: audit-finding

- id: H8B-024
  name: "BYZ-8 — Oath-Bound Administrator, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1684
  system: faction-strategy
  slice: mechanic
  statement: >-
    Proposal lets an heir renounce dynastic claim for delegated high office at reduced Coup
    Counter sensitivity. Prior NERS verdict MERGE (confirmed, corrected target) — presupposes a
    "barred office" axis Part 7 doesn't have, and its Coup Counter numeric hook is independently
    unresolved (ED-931). Re-evaluation against built code: REDUNDANT, unaffected — the built
    substrate models settlement-scale governance only, not faction-scale succession rules or Coup
    Counter, so nothing in it bears on the MERGE. Does not change the verdict.
  status: audit-finding

- id: H8B-025
  name: "BYZ-9 — Cardinal Ratification Override, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1705
  system: faction-strategy
  touches: [npc-social]
  slice: mechanic
  statement: >-
    Proposal lets Crown/Parliament override a Church College Cardinal election at a legitimacy
    cost. Prior NERS verdict REFINE (confirmed) — the eligibility clause imports diocesan
    structure that doesn't exist at Cardinal rank. Re-evaluation against built code: STILL-VALID
    — despite the shared word "legitimacy," the proposal's cost currency (Disposition + Precedent
    + CI) is not the inert settlement `legitimacy`/`popular_support` field, and BYZ-9 operates one
    layer above anything `sim/territory/` models, so no collision exists. Does not change the
    verdict; adds a note to preempt future confusion once that field is wired.
  status: audit-finding

- id: H8B-026
  name: "CHN-2 — Imperial Examination Ladder, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1728
  system: personnel-roster
  touches: [faction-strategy]
  slice: mechanic
  statement: >-
    Proposal is a non-sponsorship credentialing pipeline (capped pass rates, a "Waiting Laureate
    Pool") filling a flat §1.1b administrative-branch gap; carries `needs_jordan`. Prior NERS
    verdict REFINE (confirmed) — no autonomous consequence for an unmanaged pool, and the
    capped-passer count binds to no resolution primitive. Re-evaluation against built code:
    STILL-VALID, defect unresolved — nothing in `sim/territory/`, `ledger.py`, or the Goldenfurt
    slice models an examination/credentialing pipeline or a population-capped tournament
    primitive. Does not change the verdict.
  status: audit-finding

- id: H8B-027
  name: "CHN-3 — Clerk Capacity, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1752
  system: personnel-roster
  touches: [settlement-governance]
  slice: mechanic
  formula: "AP = 2 + facility_tier (+1 Seat/Cathedral); proposed cap: Clerk Capacity <= facility_tier"
  statement: >-
    Proposal ("Retain Clerks") is a second AP source converting Wealth into AP with a hidden
    Clerk-Corruption counter. Prior NERS verdict REFINE (confirmed) — no acquisition/growth
    mechanism or ceiling specified, so dominance (Omega-d) cannot be disproven. Re-evaluation
    against built code: RECONCILE — the shipped `AP = 2 + facility_tier` formula supplies the
    missing numeric anchor to cap Clerk Capacity against, and a 500-seed stress sweep found a
    runaway-negative regime in a world with no AP economy at all, making an uncapped second AP
    source a plausible aggravator. This changes the verdict: NERS's abstract "no ceiling" finding
    becomes a concrete, specifiable fix, and the stress-test finding raises the stakes of skipping it.
  status: audit-finding

- id: H8B-028
  name: "CHN-4 — Salt Certificate, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1782
  system: economy-accounting
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is a tradeable, geography-siloed monopoly token with a one-way "Convert to Hereditary
    Franchise" door. Prior NERS verdict REFINE (overturned from a stub MERGE) — not duplicate of
    Guild-charter or Toll, but specifies no autonomous churn hook. Re-evaluation against built
    code: COLLISION-adjacent — the built `TAG_KINDS` enum has no "Compact" kind (the shipped 5th
    is Leverage), and CHN-4's franchise-conversion tag is exactly the kind of durable claim-tag
    mint a careless pass would misname "Compact." Changes the verdict by adding a concrete typing
    constraint: the tag must resolve to built Leverage.
  status: audit-finding

- id: H8B-029
  name: "CHN-5 — Kaizhongfa Colonize Directive, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1804
  system: economy-accounting
  touches: [settlement-governance]
  slice: mechanic
  statement: >-
    Proposal is the batch's only calendar-driven decay clock — Debt/Precedent tags fire on a
    schedule, paying the governor. Prior NERS verdict REFINE (overturned from MERGE — the
    dossier's claimed §1.3a corroboration was fabricated on source-check). Re-evaluation against
    built code: RECONCILE — the built `pressure (Pi)` field is the natural home for an autonomous
    per-settlement clock, and Goldenfurt's CG-1 fix already solved Pi's mis-sign/death-spiral
    failure mode, so authoring CHN-5 as a Pi-modifying trigger inherits that fix for free rather
    than risking re-deriving it. Changes the verdict: implement via built Pi, and type its tag
    family as Debt/Leverage, not "Compact."
  status: audit-finding

- id: H8B-030
  name: "CHN-6 — Gongsuo Registration, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1833
  system: settlement-governance
  slice: gap
  statement: >-
    Proposal is a symmetric registered/unregistered visibility toggle for guilds, opening a
    "Squeeze" Friction card. Prior NERS verdict MERGE (confirmed) — "Squeeze" duplicates the
    already-landed Clerk-Corruption Intrigue trigger, among four other redundancy findings.
    Re-evaluation against built code: RECONCILE plus a new dependency — the built `suspicion`
    field is the concrete analog of the exposure axis CHN-6 wants, reinforcing the duplication
    finding, but a separate stress-sweep root finding (F1: settlement-type taxonomy undefined)
    means CHN-6 cannot be merged until that taxonomy is resolved, since registration consequences
    plausibly differ by settlement type. Changes the verdict by adding a hard precondition NERS
    lacked visibility into.
  status: audit-finding

- id: H8B-031
  name: "CHN-7 — Chancellery Gatekeeper, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1864
  system: settlement-governance
  touches: [faction-strategy]
  slice: mechanic
  statement: >-
    Proposal is a named NPC between the Provincial Authority and governor who can silently
    substitute a harsher Directive — an information-asymmetry failure mode; carries
    `needs_jordan`. Prior NERS verdict: NOT ADJUDICATED (hit transient structured-output failures
    across three workflow passes, filed carried-forward). Re-evaluation against built code:
    RECONCILE — the Goldenfurt slice's worked, 32-finding-verified Directive Comply/Bargain/Defy
    pipeline with 9 named actors is the first concrete substrate CHN-7 has ever had to attach to,
    raising two open questions (10th actor vs. reused role; the roster-cap convention). No prior
    verdict to change, but evaluability materially improved.
  status: audit-finding

- id: H8B-032
  name: "CHN-8 — Institutional Purge (Bloc), Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1892
  system: faction-strategy
  touches: [personnel-roster]
  slice: gap
  statement: >-
    Proposal is a bloc-scale mass-demotion trigger for a whole credentialed cohort at once,
    wielded by CHN-7's gatekeeper. Prior NERS verdict PRUNE (hardened from DISTILL) — a costless,
    contest-free, unaccountable mass-purge switch with no defense roll or backlash, and four later
    proposals depend on it as a reused primitive, propagating the gap. Re-evaluation against built
    code: REDUNDANT-of-a-fix — the Goldenfurt slice's recall-death-spiral solution (capped
    increment, Submit-to-audit escape hatch, Reputation:Just counter-weight) is exactly the
    three-part safety valve CHN-8 lacks, corroborating rather than overturning PRUNE. Does not
    change the verdict; supplies a concrete repair template if ever revived.
  status: audit-finding

- id: H8B-033
  name: "CHN-9 — Kaochengfa Performance Audit, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1923
  system: personnel-roster
  slice: mechanic
  statement: >-
    Proposal is a patron-imposed triplicate-ledger toggle speeding both demotion and promotion,
    auto-lapsing when the patron falls. Prior NERS verdict MERGE (confirmed) — reproduces §1.0a's
    existing one-rank demotion endpoint with no independent consequence, and no promotion-cadence
    rule exists anywhere in the corpus for its "speeds promotion" claim to hook. Re-evaluation
    against built code: STILL-VALID, unaffected — nothing in `sim/territory/` or Goldenfurt models
    FA-rank promotion cadence. Does not change the verdict; this is one of two MERGE verdicts
    requiring deletion of an already-landed subsection (§1.0d), a live PR-blocking issue under this
    repo's default-ratification rule.
  status: audit-finding

# ===== Re-evaluation set 2: Habsburg Spain & Italy (12 items) =====

- id: H8B-034
  name: "HAB-1 — Corregidor, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:1992
  system: settlement-governance
  touches: [personnel-roster]
  slice: mechanic
  statement: >-
    Proposal seats a specialist appointee over a sitting governor, overriding only Hold
    Court/Investigate on term-scoped self-expiring tags. Prior NERS verdict KEEP (overturned from
    a stub MERGE) — mechanizes an existing unmechanized §1.4 audit stub, distinct from SE-7's
    Visita/Residencia and IT-1's Podestà. Re-evaluation against built code: STILL-VALID — the
    built `Settlement.suspicion` field is a real, read/written field HAB-1 can gate on (unlike
    inert `legitimacy`/`popular_support`), strengthening the KEEP. Does not change the verdict.
  status: audit-finding

- id: H8B-035
  name: "HAB-2 — Valido, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2016
  system: faction-strategy
  slice: gap
  statement: >-
    Proposal is an informal Favorite power-track granting routing control over all Ministry
    consultas, broader than the formal Standing-6/7 gates it sits beside. Prior NERS verdict CUT
    (confirmed) — a strictly cheaper dominant path to power than the formal gates (Omega-d
    failure). Re-evaluation against built code: SUPERSEDED, i.e. the cut is reinforced — the
    entire premise leans on outperforming Legitimacy-adjacent levers, but built
    `legitimacy`/`popular_support` are INERT (never read/written in `sim/`), so the power-track has
    no live state to attach to even setting aside the dominance failure. Does not change the
    verdict; adds an independent code-level reason.
  status: audit-finding

- id: H8B-036
  name: "HAB-4 — Overlapping Consulta Arbitration, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2040
  system: faction-strategy
  slice: mechanic
  statement: >-
    Proposal is inter-ministry conflict arbitration (Agenda-Set vs. Ratify procedures) with a
    Latency-to-paralysis cost denominated in Competence. Prior NERS verdict REFINE (confirmed) —
    "Ministry priority action" is used as an undefined term with unclear AP draw. Re-evaluation
    against built code: STILL-VALID with a resolution path — the built `AP = 2 + facility_tier`
    formula is the only live seasonal-budget primitive, so the open question should resolve to
    "Ministry actions draw the same AP pool" rather than inventing a parallel currency; no
    Ministries or Competence tracks exist in the built schema to duplicate. Does not change the
    REFINE verdict but closes a previously-unverifiable gap.
  status: audit-finding

- id: H8B-037
  name: "HAB-5 — Encabezamiento (Negotiated Quota), Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2065
  system: economy-accounting
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is a negotiated fixed-term tax lock below live capacity, pitched explicitly as "the
    5th Ledger tag," with a reciprocal one-Petition-per-term obligation. Prior NERS verdict KEEP
    (no steelman needed) — one of only two clean items in the entire 12-item authored-into-canon
    set. Re-evaluation against built code: COLLIDES, the single most consequential finding in this
    set — `ledger.py`'s actual fifth `TAG_KINDS` member is Leverage, not Compact, so HAB-5 was
    adjudicated against a tag family that does not exist in code. This changes the verdict from
    "ratify as-is" to "reconcile the tag-family naming/schema before ratifying" — flagged as
    exactly the kind of held-back item that must not be silently ratified by a routine PR merge.
  status: audit-finding

- id: H8B-038
  name: "HAB-6 — Crush the Estates, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2094
  system: faction-strategy
  touches: [settlement-governance]
  slice: mechanic
  statement: >-
    Proposal is an irreversible action permanently rewriting a ratified faction's rank-ladder gate
    (e.g. a supermajority vote to direct crown appointment, forever). Prior NERS verdict KEEP
    (overturned from PRUNE) — the dossier's re-home target operates strictly post-threshold and
    cannot absorb HAB-6's vote-elimination consequence. Re-evaluation against built code:
    STILL-VALID — the built `subnational` dict field is a plausible home for faction-ladder state
    at settlement scale, but nothing built implements or contradicts an irreversible rank-ladder
    rewrite yet. Does not change the verdict.
  status: audit-finding

- id: H8B-039
  name: "HAB-7 — Ordenanza Ratification, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2116
  system: settlement-governance
  slice: mechanic
  statement: >-
    Proposal is a Petition-card three-branch fork (Ratify/Reject/Amend) for guild-authored
    ordenanzas using existing Hold Court/Ledger/Influence machinery. Prior NERS verdict KEEP (no
    steelman needed) — the other of the two clean authored items. Re-evaluation against built
    code: STILL-VALID — because it reuses existing machinery rather than proposing a new tag kind,
    it does not hit the Compact-vs-Leverage collision that HAB-5 does; `open_needs` is a plausible
    but non-load-bearing implementation anchor. Does not change the verdict; remains the cleanest
    item in the entire set.
  status: audit-finding

- id: H8B-040
  name: "IT-1 — Podestà, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2135
  system: personnel-roster
  touches: [settlement-governance]
  slice: mechanic
  statement: >-
    Proposal is an outsider-contracted governor immune to internal faction rolls, with
    appointer-liability billing the appointing faction's Legitimacy. Prior NERS verdict REFINE
    (overturned from MERGE) — only its "Fair Magistrate" clause duplicates the existing Reputation
    tag. Re-evaluation against built code: RECONCILE on that clause — Goldenfurt's live G606 escape
    hatch already uses Reputation:Just to lower recall Ob, the exact built analog of "Fair
    Magistrate," turning an abstract merge instruction into a concrete implementation move. Does
    not change the REFINE verdict; flags that the appointer-liability channel targets the
    currently-INERT Legitimacy field as a build-order dependency.
  status: audit-finding

- id: H8B-041
  name: "IT-2 — Condotta, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2161
  system: mass-battle-seam
  touches: [personnel-roster]
  slice: mechanic
  statement: >-
    Proposal is a three-phase mercenary contract state machine (Ferma→Aspetto→Lapsed) with
    poaching during Aspetto and a post-lapse cooldown. Prior NERS verdict REFINE (confirmed) — a
    recalled-Mil-pool multiplier is unreconciled against `massbattle.py::_faction_to_unit`, and it
    builds no shared Debt hook for garrison-pay wages. Re-evaluation against built code:
    STILL-VALID with a direct RECONCILE target confirmed — `march_layer` is confirmed army
    logistics not governor economy (consistent with reconciling against mass-battle code), and the
    built `Debt` tag kind is exactly the shared wage-liability clock the audit called for, not new
    infrastructure to invent. Does not change the REFINE verdict; removes ambiguity about whether
    new ledger machinery is needed (it isn't).
  status: audit-finding

- id: H8B-042
  name: "IT-5 — Legation Split, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2185
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is a Weight-threshold brake on delegated multi-settlement authority, paired with
    BYZ-6's pooled-AP accelerator as one governance section. Prior NERS verdict REFINE (overturned
    from MERGE) — the dossier's three claimed collisions evaporated on source-check. Re-evaluation
    against built code: RECONCILE-first — governance in `sim/` is strictly per-settlement with no
    multi-settlement AP economy at all, so BYZ-6's pooled-AP resource IT-5 is meant to brake has no
    built substrate to attach to. This changes the verdict on sequencing (not on REFINE itself):
    it is now a firm build-order gate — BYZ-6's pooled-AP field must exist before IT-5's trigger
    can be authored against it.
  status: audit-finding

- id: H8B-043
  name: "IT-6 — Fiscal Tribunal, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2212
  system: settlement-governance
  slice: mechanic
  statement: >-
    Proposal is a self-binding institution — Levy-via-Tribunal writes a Precedent raising the
    governor's own future Levy Ob, and gives Local Actors an AI-triggered reversal petition. Prior
    NERS verdict: NOT ADJUDICATED (queued, hit transient structured-output failures, carried
    forward, STEP-3 status `needs_jordan`). Re-evaluation against built code: STILL-VALID as a
    design proposal but cannot receive a formal re-eval category since no prior verdict exists —
    the built `Precedent` tag and `open_needs` field are both plausible, non-colliding
    implementation anchors. No prior verdict to change; needs a real NERS pass before promotion.
  status: audit-finding

- id: H8B-044
  name: "IT-7 — Seggio Council, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2236
  system: faction-strategy
  touches: [settlement-governance]
  slice: mechanic
  statement: >-
    Proposal is a hereditary noble corporate-faction archetype sitting outside the
    Charter/Quo-Warranto system, sharing a collective Eletti bloc-Treat. Prior NERS verdict
    REFINE (confirmed) — three Q gaps: a stripped Hold-Court case class with no replacement
    resolver, ambiguous Guild-row interaction, and an omitted recognition cost. Re-evaluation
    against built code: RECONCILE with a genuine hook — the built `subnational` dict field is
    precisely the structure a hereditary, non-transferable body needs, confirming the category is
    already anticipated rather than novel. Does not change the REFINE verdict; de-risks the
    authoring follow-up without resolving the three Q gaps.
  status: audit-finding

- id: H8B-045
  name: "IT-8 — Capital-Gated Mastership, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2262
  system: personnel-roster
  slice: mechanic
  statement: >-
    Proposal is an alternate guild Free-Master gate: buy the rank in exchange for a durable
    Upstart tag (Disposition penalty, Apprentice lock, easier expulsion). Prior NERS verdict
    REFINE (confirmed) — one of three cost clauses cites a nonexistent accuser/defendant role
    outside the Church Excommunication Tribunal. Re-evaluation against built code: STILL-VALID, no
    collision — caste/guild-rank mechanics sit entirely outside the built Settlement schema, which
    neither confirms nor contradicts them. Does not change the verdict; this is a pure design-text
    defect independent of anything built.
  status: audit-finding

# ===== Re-evaluation set 3: Japan & remaining SE/FA (8 items) =====

- id: H8B-046
  name: "SE-JP1 — Goningumi Collective-Liability Cells, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2318
  system: settlement-governance
  touches: [npc-social]
  slice: gap
  statement: >-
    Proposal binds a settlement's Local Actors into fixed five-household collective-liability
    cells with a compounding "Cell Revolt" failure mode. Prior NERS verdict MERGE (confirmed) —
    the design-prose §4.5 cap of 1–2 Local Actors per settlement makes the mechanic
    non-executable, plus an Omega-d self-selection dominance concern. Re-evaluation against built
    code: RECONCILE — three mutually incompatible built/queued Local-Actor representations exist
    (`npc_ids` unbounded list; Goldenfurt's 9 named actors; the stress harness's count-per-type
    abstraction), none matching the prose 1–2 cap the MERGE relied on, so the stated fatal flaw
    does not survive contact with any built representation. Changes the verdict: MERGE's *reason*
    fails, but it should not simply flip to KEEP either, since which Local-Actor representation
    SE-JP1 targets must be declared first.
  status: audit-finding

- id: H8B-047
  name: "SE-JP2 — Kokudaka Cadastral Survey, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2326
  system: settlement-governance
  touches: [economy-accounting]
  slice: gap
  statement: >-
    Proposal periodically locks an `assessed_base` figure that Extract reads until the next
    Survey, creating an exploitable surplus or a neglect-detonates-revolt hazard. Prior NERS
    verdict REFINE (confirmed) — no event-deck card, no Assessment-vs-Compact precedence rule.
    Re-evaluation against built code: COLLIDES on two independent axes worse than the audit knew —
    the built `Settlement` schema has no `assessed_base` field at all (not a missing enumeration,
    an absent storage substrate), and the "Compact" family it shares with HAB-5 does not exist in
    `ledger.py`'s actual TAG_KINDS (Leverage is the real 5th kind). Changes the verdict: fixing
    this now requires adding a genuine schema field and resolving the tag-family mismatch, not
    editing prose cross-references.
  status: audit-finding

- id: H8B-048
  name: "SE-JP3 — Za Guild Patronage Lapse, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2334
  system: settlement-governance
  touches: [faction-strategy]
  slice: gap
  statement: >-
    Proposal auto-lapses guild privileges when a patron's Standing falls, extending the settlement
    Charter tag. Prior NERS verdict REFINE (overturned from MERGE — different scale/tag/resolver
    than the claimed duplicate) — a real Omega-d gap: patron-collapse bypasses Quo Warranto's
    age-scaling with no contagion echo. Re-evaluation against built code: COLLIDES — the "Charter"
    tag §3.3a assumes is real does not exist among the built five `TAG_KINDS`, mirroring the exact
    absence already flagged for a sibling proposal (HRE-5); `charter_age_seasons` also has no
    schema home. Changes the verdict: the fix is now a schema decision (map Charter onto Leverage
    or Precedent) before the age-scaling prose fix can even apply.
  status: audit-finding

- id: H8B-049
  name: "SE-JP4 — Shi-no-ko-sho Status Freeze, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2342
  system: personnel-roster
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is a caste-mobility-lock toggle trading Order for permanently blocked
    caste-crossing Rank Advancement. Prior NERS verdict CUT (confirmed) — a zero-upkeep dominant
    strategy, and its blanket block silently nullifies deliberately-authored caste-critique
    escape valves. Re-evaluation against built code: SUPERSEDED — Order is a real built field, but
    the stress-sweep's own root finding F1 (settlement-type taxonomy undefined) means a
    type-scoped freeze condition sits on ground the built work already flagged as ambiguous,
    compounding rather than rescuing the item. Does not change the verdict; still CUT, more
    firmly, and not worth revisiting even if F1 is later fixed.
  status: audit-finding

- id: H8B-050
  name: "FA-JP2 — Goon-hoko Recognition Fork, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2350
  system: faction-strategy
  slice: mechanic
  statement: >-
    Proposal splits every Recognition Event into a Confirm-vs-New-Grant fork, giving faction
    leaders a legible stonewalling lever across all four rank ladders. Prior NERS verdict REFINE
    (confirmed) — "ease by one step" is an undefined operand and a citation to §1.4 is broken
    (wrong actor-direction). Re-evaluation against built code: STILL-VALID, unaffected — this is
    pure FA-lane faction-rank content that no built-work fact (settlement registry, tag kinds,
    Goldenfurt, `march_layer`) touches. Does not change the verdict.
  status: audit-finding

- id: H8B-051
  name: "FA-JP3 — Shinpan/Fudai/Tozama Vassal Tiering, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2358
  system: faction-strategy
  slice: mechanic
  statement: >-
    Proposal is a three-axis vassal classification (kinship, grant-size, council-eligibility)
    intended to differentiate the Varfell faction. Prior NERS verdict DISTILL (confirmed) — its
    fixed-at-investiture hard-exclusion shape reintroduces a gate-type §1.3/§3.2 deliberately
    withholds from Varfell, without supersession. Re-evaluation against built code: STILL-VALID,
    unaffected — no built schema, tag, or AP-economy fact intersects an FA-lane vassal-tiering
    axis. Does not change the verdict.
  status: audit-finding

- id: H8B-052
  name: "FA-JP4 — Sankin-Kotai Court Attendance + Hostage-Kin, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2366
  system: faction-strategy
  touches: [npc-social]
  slice: mechanic
  statement: >-
    Proposal is a recurring court-presence cost plus a hostage-kin lever that eases Demotion
    Magnitude thresholds while making the hostage a legible target. Prior NERS verdict REFINE
    (confirmed, steelman survived) — the "eases by one step" magnitude is undefined; "Treasury
    cost" should be a bare Wealth figure. Re-evaluation against built code: STILL-VALID — the
    "travel/retinue" framing gestures at `march_layer`, but that layer is confirmed army-logistics
    only with no cross-settlement AP economy, foreclosing a tempting but unsupported fix and
    confirming the audit's own bare-Wealth-figure recommendation is correct and sufficient. Does
    not change the verdict.
  status: audit-finding

- id: H8B-053
  name: "FA-JP5 — Metsuke/Ometsuke Segregated Surveillance, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2374
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal splits faction surveillance into two independent, non-poolable tracks (own-officers
    vs. vassal-lord watch). Prior NERS verdict DISTILL (confirmed) — no funding cost/decay/clamp
    specified, and it re-opens a deliberate prior narrowing of Investigate unacknowledged.
    Re-evaluation against built code: RECONCILE, a new collision the prior pass had no way to see
    — the built `Settlement.suspicion` field is a single scalar that Goldenfurt's verified G606
    fix builds directly on; forking surveillance into two tracks risks fragmenting or bypassing
    that working mechanism if FA-JP5's "own-officers" track is meant to be the same field. Changes
    the verdict: sharpens DISTILL with a concrete risk of breaking a verified built mechanism, not
    just under-specification.
  status: audit-finding

# ===== Re-evaluation set 4: Venice & HRE (10 items) =====

- id: H8B-054
  name: "HRE-2 — Chapter Capture, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2413
  system: faction-strategy
  touches: [npc-social]
  slice: mechanic
  statement: >-
    Proposal is pre-vacancy patronage banking — a governor spends Duty-slots to bank College seats
    against a specific Arm, converting to vote-weight only if a vacancy fires there. Prior NERS
    verdict KEEP (overturned from a stub DISTILL) — proactive vs. reactive is genuinely distinct,
    and Duty-slot cost holds against dominance. Re-evaluation against built code: STILL-VALID —
    the proposed "seats owed" counter touches none of the five built `TAG_KINDS` and doesn't read
    or write the inert legitimacy fields, so no collision surface exists. Does not change the
    verdict.
  status: audit-finding

- id: H8B-055
  name: "HRE-3 — Convene the Circle, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2438
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is a new AP verb pooling Directive obligations across peer settlements, writing a
    "Circle Quota" tag callable by any member — the corpus's first lateral (governor-to-governor)
    obligation axis. Prior NERS verdict REFINE (confirmed) — the trigger condition has no
    mechanical referent, and "Circle Quota" claims a sixth Ledger tag family. Re-evaluation
    against built code: RECONCILE, harder than the audit could see — `march_layer` is confirmed
    army logistics with no cross-settlement AP economy at all (not merely an unspecified ceiling,
    an absent layer), and `TAG_KINDS` is a closed five-member enum with no open sixth slot to
    extend into. Changes the verdict: raises the bar from "fix two Q gaps" to "no multi-settlement
    layer exists for this to plug into yet."
  status: audit-finding

- id: H8B-056
  name: "HRE-4 — Borrow, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2471
  system: economy-accounting
  touches: [faction-strategy]
  slice: mechanic
  statement: >-
    Proposal is a financier loan secured against a named extractive right, spawning an
    Investigate-discoverable financier-actor, reusing (not duplicating) Quo Warranto for clawback.
    Prior NERS verdict KEEP (overturned from a stub MERGE) — a new "Concession" tag differs from
    both Debt and Compact. Re-evaluation against built code: RECONCILE, narrower than HRE-3/VEN-
    SE-2 — the closed five-member `TAG_KINDS` has no slot for a sixth "Concession" family, but its
    differentiation logic survives as a rename/subsumption into the existing Leverage kind rather
    than a structural rebuild. Does not change the underlying KEEP; retypes "Concession" onto
    built Leverage before authoring.
  status: audit-finding

- id: H8B-057
  name: "HRE-5 — Guild Uprising (Compact/Suppress), Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2498
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is one crisis trigger with two opposite durable outcomes: Concord installs a
    permanent guild veto claimed to write under a "Compact" tag distinct from a claimed "Charter"
    tag; Suppression zeroes Guild Influence with a never-decaying Grudge floor. Prior NERS verdict
    REFINE (confirmed) — flagged a name collision, presuming a real landed Compact tag to
    distinguish Concord from. Re-evaluation against built code: COLLIDES, worse than the prior
    pass could know — there is no "Compact" in `ledger.py`'s `TAG_KINDS` at all, so the audit's
    proposed fix (rename away from the existing Compact) is itself unresolvable; the real
    collision is Concord-vs-Leverage. Changes the verdict: HRE-5 cannot be safely authored until
    the corpus-wide Compact/Leverage question is settled.
  status: audit-finding

- id: H8B-058
  name: "HRE-6 — Reichsacht, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2530
  system: faction-strategy
  touches: [settlement-governance]
  slice: mechanic
  statement: >-
    Proposal is an "Outlawed" status flag with a contagion clause (harboring exposes the
    harborer) but enforcement-dependent teeth — a Crown decree that can visibly, legibly fail.
    Prior NERS verdict KEEP (no steelman needed) — no existing mechanic does this job, and the
    cost asymmetry (declaring side free, responding side fully costed) holds against dominance.
    Re-evaluation against built code: STILL-VALID and now more implementable — Goldenfurt's
    32-finding-verified Directive Comply/Bargain/Defy pipeline is exactly the "shelter branch =
    costed Defy" mechanism the proposal needs, and its verified suspicion-cap/Reputation:Just
    recall fix is directly adjacent machinery to reuse. Does not change KEEP; makes it cheaper to
    execute.
  status: audit-finding

- id: H8B-059
  name: "HRE-7 — Mediatize, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2557
  system: territory-world
  touches: [faction-strategy]
  slice: gap
  statement: >-
    Proposal is a new Immediate/Mediatized settlement-status axis issuable only as
    negotiated-treaty compensation — administrative demotion without a battle. Prior NERS verdict
    REFINE (overturned from MERGE) — its sole delivery mechanism (a negotiated peace-treaty
    payload) doesn't exist in canon, and composition with an existing Charter is unspecified.
    Re-evaluation against built code: RECONCILE — the composition target itself, §1.8
    Legitimacy/Mandate, is not merely under-specified but dead code: `legitimacy`/`popular_support`
    are never read or written in `sim/`, and the Mandate formula that would consume them is not
    implemented. Changes the verdict: this is a strictly harder blocker (no live system to compose
    against at all) and should sequence behind the Legitimacy-wiring work it depends on.
  status: audit-finding

- id: H8B-060
  name: "VEN-SE-1 — State Arsenal, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2590
  system: economy-accounting
  touches: [settlement-governance]
  slice: mechanic
  statement: >-
    Proposal is a fourth Develop-funding method with a persistent per-settlement Wage/Pension
    Debt liability firing every season regardless of use. Prior NERS verdict CUT (confirmed, N
    plank corrected) — for +1 AP over base Develop it removes roll variance and doubles output at
    an avoidable cost, violating the section's own design law. Re-evaluation against built code:
    REDUNDANT, reinforcing the CUT — the built `Debt` tag already covers the wage-liability half
    with no missing schema, and the live `AP = 2 + facility_tier` economy confirms exactly the
    tuned surface the near-free AP buy would distort. Does not change the verdict.
  status: audit-finding

- id: H8B-061
  name: "VEN-SE-2 — Boschi Pubblici Requisition, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2619
  system: economy-accounting
  touches: [settlement-governance]
  slice: gap
  statement: >-
    Proposal is a new Directive type tying a province to a named production dependency (e.g.
    timber → Arsenal), with a Defy consequence starving the dependent building. Prior NERS verdict
    REFINE (confirmed) — the flagship Defy consequence presupposes an Arsenal auto-success bonus
    that does not exist in its own cited source, and the Directive may silently bypass Compact
    auto-resolution. Re-evaluation against built code: RECONCILE on both grounds — VEN-SE-1's CUT
    removes the Defy branch's cited counterparty entirely, and the Compact-bypass question is
    unanswerable pending the same corpus-wide Compact/Leverage resolution blocking HRE-5. Changes
    the verdict on both grounds; gated jointly on picking a new dependent-building target and the
    shared tag-family reconciliation.
  status: audit-finding

- id: H8B-062
  name: "VEN-SE-3 — Bonifiche Capital Posture, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2649
  system: economy-accounting
  touches: [mass-battle-seam]
  slice: gap
  statement: >-
    Proposal is a fifth Ledger tag family where a military loss triggers an economic choice and
    changes what type of extraction a Directive may ask for. Prior NERS verdict: not adjudicated
    (carried forward after transient structured-output failures). Re-evaluation against built
    code: COLLIDES — the proposal's premise ("a fifth family") is false against the built engine,
    since the actual fifth `TAG_KINDS` member is Leverage, not Compact, making VEN-SE-3 a
    contender for a sixth slot in a closed five-member enum rather than a filler of an open fifth.
    No prior verdict to change, but this materially narrows what a future adjudication pass can
    conclude; gated on the same Compact-vs-Leverage resolution as HRE-5/VEN-SE-2.
  status: audit-finding

- id: H8B-063
  name: "VEN-SE-5 — Scuole Grandi, Re-Evaluated"
  source: audit/2026-07-12-governance-compendium/_workings_joined.md:2677
  system: settlement-governance
  touches: [npc-social]
  slice: gap
  statement: >-
    Proposal is a caste-excluded Civic Prestige resource that subtracts from the Π pressure
    homeostat only while excluded-caste Grudges drive it. Prior NERS verdict DISTILL (confirmed,
    one plank corrected) — minting a new resource plus a conditional term on a central formula is
    a mandatory Class-A trigger the proposal fails by its own self-declared scale-isolated text.
    Re-evaluation against built code: STILL-VALID direction, RECONCILE on landing details — the
    built `pressure (Pi)` field has documented, real death-spiral history (Goldenfurt's CG-1 fix),
    concretely corroborating "keep this off the central formula," and the recommended re-homing
    onto Debt/Reputation tags is directly supported since both are real, uncontested built kinds.
    Does not change DISTILL; strengthens its follow-up recommendation with a code-verified reason.
  status: audit-finding
```

## Coverage notes

Read all 2734 lines in full, no sampling. Verified counts independently rather than trusting the source's own arithmetic: the "~94-card HEV catalogue" claim checks out exactly (10+8+10+10+9+10+9+9+9+10=94 `### HEV-` headings across the ten domain sections), and `systems/settlements/sim/ledger.py:30` was opened directly to confirm the single highest-value cross-cutting finding in this lane — the corpus-wide "Compact"/"Charter"/"Assessment" tag-family proposals collide with a built, closed five-member `TAG_KINDS` enum whose real fifth member is `Leverage`. That one code fact is the load-bearing driver behind roughly a third of the 44 re-evaluation records (H8B-021, 028, 030, 037, 047, 048, 055–057, 059, 061, 062), so I recorded it once as its own code-cited `gap` (H8B-007) rather than repeating the citation in every dependent record's `formula`/`status_evidence` field.

Two source-internal discrepancies I did not resolve, since resolving them is a later stage's job, not extraction: (1) the Habsburg/Italy re-eval header claims "11 items" but lists and re-adjudicates 12 (HAB×6 + IT×6) — I harvested all 12 as found. (2) the event-card integration map's own family-count table is explicitly self-described as partly "inferred"/"unresolved" rather than ratified (only 11 of the 58 grounded-deck cards have a confirmed family), which I preserved as a caveat inside H8B-001 rather than silently presenting the totals as solid.

Per the contract's explicit steer, I did not transcribe the 94 HEV cards, the 58-card grounded deck, or the 28-card Goldenfurt deck individually — only the shared resolution-model mechanism (H8B-004), the family taxonomy and totals (H8B-001, H8B-003), the dedup findings (H8B-002), and two cross-card structural patterns that recur across many cards and are not in either baseline (new Directive-type candidates, H8B-005; the standing-institution shape, H8B-006). Every card's own bespoke "Introduces (Action)" mini-verb (Toll, Sunset Review, Broker Diversion, Dredge Harbor, etc.) was read but deliberately not minted as an individual record — they are settlement-scale flavor variants on verbs the baseline catalogue already censuses (Develop/Fortify/Treat/Levy funding forks), and recording each would have been exactly the "long but worthless" transcription failure the contract warns about. All §30 ripple chains (12/12) were harvested individually since each is a genuine multi-step cross-scale `process`, and every chain's record notes the section's own "extracted verbatim, not yet vetted against the live card corpus" caveat. All four re-evaluation sets were harvested in full (44/44 items, matching the ~50 verdict-token count the task description anticipated once multi-word verdicts like "COLLISION-adjacent" and "REDUNDANT-of-a-fix" are counted), since the task named these the closest existing worked example of the exact reconciliation analysis a later synthesis stage must perform.