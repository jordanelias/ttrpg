I have all the citations I need. Now compiling the complete harvest output.

## Manifest

| path | lines | records | note |
|---|---|---|---|
| audit/2026-07-12-governance-compendium/00_index.md | 64 | 0 | Pure index/TOC. Confirms `event_cards/` (94 cards) and `reeval/` (44 files) are named but do not exist on disk — flagged per contract, no records cited under those paths. |
| audit/2026-07-12-governance-compendium/40_roster_officer_system.md | 621 | 21 | Full-read. The eight M1–M8 mechanisms (not ten — see Coverage notes) plus the `power_base` architecture, the autonomous loop, and 7 named architectural gaps. |
| audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md | 494 | 13 | Full-read. ~72 catalogued historical proposals (S/O/T/F/X series) read in full; only the load-bearing new entities/levers extracted as records — not the individual proposals (see Coverage notes). |
| audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md | 254 | 8 | Full-read. Counted ~99–101 verb rows, not the index's claimed 109 (see Coverage notes). Only governance/personnel-relevant, non-baseline verbs harvested individually. |
| audit/2026-07-12-governance-compendium/43_directive_types.md | 121 | 9 | Full-read. Cross-checked against `systems/settlements/sim/registry.py` and `systems/settlements/settlement_generator_v1.md`. |
| audit/2026-07-12-governance-compendium/44_standing_institutions.md | 274 | 9 | Full-read. |
| audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md | 152 | 5 | Full-read. Cross-checked against `systems/settlements/sim/registry.py` (confirms no granular meters exist, consistent with the cited Jordan ruling). |
| audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md | 449 | 10 | Full-read. Verified the 58 = 12+9+23+14 partition (exact match to index's claim). |
| audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md | 117 | 7 | Full-read. The "24 un-run NERS probes" is one register row about an unexecuted grid, not 24 distinct harvestable probes (see Coverage notes). |

## Records

```yaml
# ==================== 40_roster_officer_system.md ====================

- id: H8A-001
  name: Officer/Ascendancy naming resolution
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:272
  system: personnel-roster
  touches: [mass-battle-seam, faction-strategy]
  slice: gap
  statement: Part 40 proposes resolving the "officer" term collision with mass-battle's auto-generated unit commander by naming the rise-to-power system "Ascendancy" and its roles Retainer/Patron/Advisor. This exact resolution already stands in the baseline as a settled vocabulary table.
  baseline_ref: personnel_muster_integration_master_v1.md §2.3 (line 149)
  status: audit-finding

- id: H8A-002
  name: Patronage chains (M1)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:30
  system: personnel-roster
  touches: [faction-strategy]
  slice: mechanic
  statement: An NPC's rank climb is gated on an `upward_patron` edge plus a derived `clientele_breadth` score; the mechanism collapses top-down when the patron falls, decaying clientele_breadth and freezing advancement.
  formula: "advance: +f(clientele_breadth, upward_patron.Disposition), frozen if upward_patron stalls; downfall: patron falls -> clientele_breadth decays / cohort auto-purges"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M1 row, line 825) — top-line summary already there; this record adds the driver/vulnerability formula, which the baseline does not carry

- id: H8A-003
  name: Credentialed merit (M2)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:33
  system: personnel-roster
  touches: [faction-strategy]
  slice: mechanic
  statement: Advancement requires clearing a two-stage gate (objective competence plus a discretionary sponsor bond); the bond persists after the exam, and the whole track is undone by a later rewrite of the credential criteria rather than by a rival's direct action.
  formula: "advance: +1 if two-stage credential gate + tutoring-investment cleared (else capped); downfall: credential_criteria rewrite re-tests the holder out"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M2 row, line 826)

- id: H8A-004
  name: Kinship / marriage alliance (M3)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:34
  system: personnel-roster
  touches: [faction-strategy, npc-social]
  slice: mechanic
  statement: Power rides a blood-tie rather than an office, advancing on marriage/betrothal/heir-birth Keys; it fails via a generational flip or demographic lapse — one Disposition-flip or a missed marriage voids a multi-season investment at the last step.
  formula: "advance: on marriage/betrothal/heir-birth Keys (A8/H1); pays a recurring rank-independent bonus once the tie holds; downfall: generational flip / demographic lapse"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M3 row, line 827)

- id: H8A-005
  name: Court proximity / favoritism (M4)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:35
  system: npc-social
  touches: [faction-strategy]
  slice: gap
  statement: Informal Royal-Intimacy outperforms formal Standing (the favorite/valido shape) and collapses binary rather than graduated — loss of intimacy or the patron's death is total, often violent. Unlike the other seven mechanisms, M4 has no corresponding `power_base` enum value (the enum lists patronage/merit/kinship/bureaucratic/military/purchased/ideological, seven values for eight mechanisms) — court favoritism is instead carried by the auxiliary meters (`shadow_standing`, Royal-Intimacy), an internal inconsistency the document does not itself flag.
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M4 row, line 828)

- id: H8A-006
  name: Bureaucratic chokepoint control (M5)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:36
  system: personnel-roster
  touches: [faction-strategy]
  slice: mechanic
  statement: Power accrues from sitting on a routing/access path (correspondence, seals, adjudication) without a vested office; it is undone by a single bypass channel or by succession, since authority-by-proxy has zero transferability.
  formula: "advance: +f(Keys successfully filtered/routed); resets to 0 if the patron falls; downfall: single bypass channel or succession"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M5 row, line 829)

- id: H8A-007
  name: Purchased office / venality (M6)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:37
  system: personnel-roster
  touches: [economy-accounting, faction-strategy]
  slice: mechanic
  statement: Rank, or a toll-post athwart it, is bought directly with Treasury; the resulting legitimacy has no loyalty reserve and evaporates the instant a rival offers something money cannot buy.
  formula: "advance: instant on Treasury spend; writes purchased_legitimacy/Exposure; downfall: no loyalty reserve suppresses the Coup Counter buffer"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M6 row, line 830)

- id: H8A-008
  name: Armed retinue / military power-base (M7)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:38
  system: mass-battle-seam
  touches: [faction-strategy, personnel-roster]
  slice: mechanic
  statement: A personal, self-loyal force is built outside the formal ladder; it falls to a coalition purge or a subordinate-flip because the ruler routes around the strength rather than matching it. This is the category the corpus flags with the highest officer/political-rank naming-collision density (~20 of 96 entries).
  formula: "advance: +f(retinue.leverage/autonomy, self-financing Keys); downfall: coalition purge or subordinate-flip"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M7 row, line 831)

- id: H8A-009
  name: Ideological / moral authority (M8)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:39
  system: npc-social
  touches: [faction-strategy]
  slice: mechanic
  statement: Standing-independent legitimacy (prophetic, jurisprudential, credentialing-body) accrues without a ladder entry; it cannot be bought or demoted, only outcompeted in its own currency or purged by covert violence.
  formula: "advance: +f(aggregate scene.witness/scene.gossip) feeding moral_authority/renown; downfall: counter-authority in the same currency, or covert violence"
  status: audit-finding
  baseline_ref: cross_scale_action_catalogue_v1.md §9.3 (M8 row, line 832)

- id: H8A-010
  name: power_base field (the Ascendancy organizing enum)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:149
  system: personnel-roster
  touches: [faction-strategy, mass-battle-seam]
  slice: primitive
  statement: A proposed enum field on the NPC sheet — {patronage, merit, kinship, bureaucratic, military, purchased, ideological} — that simultaneously types an NPC's climb driver, its downfall shape, and whether a Dismissal against it is enforceable. The document calls it "the single most load-bearing addition" in the whole roster proposal.
  status: audit-finding

- id: H8A-011
  name: ConsolidationEngine — one engine, three scale-bindings
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:88
  system: personnel-roster
  touches: [settlement-governance, faction-strategy]
  slice: process
  statement: A single ambition-engine-derived `ConsolidationEngine` with a `scale_binding` field in {settlement, court, lineage} reuses the goal/method/timeline/progress/trajectory grammar across three entity scopes. The settlement binding stays blocked on the unbuilt settlement registry; the court binding (Standing ladder + Knots graph, both already existing) is proposed as shippable without it; the lineage binding is Jordan-gated.
  status: audit-finding

- id: H8A-012
  name: Shared rank space + bounded auxiliary meters
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:94
  system: personnel-roster
  touches: [faction-strategy]
  slice: gap
  statement: Proposes NPCs climb the same Standing ladder as the player (not a parallel NPC-only ladder), with parallel-track pressures (moral_authority, renown, shadow_standing, service_rank, Dignity, custody_bonus) modeled as a bounded, named set of off-ladder auxiliary meters that substitute-in or force ratification, rather than as competing seat-spaces. This is explicitly the resolution to the corpus's recurring "how many parallel status/power tracks" tension (needs_jordan item 3), but is itself unratified.
  status: audit-finding

- id: H8A-013
  name: player_seats_are_contestable toggle
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:535
  system: personnel-roster
  touches: [faction-strategy]
  slice: gap
  statement: Whether an NPC can actually depose or supersede the player at a rank the player holds is left as a single design-taste toggle; the architecture supports either setting. The document's own inclination is yes, gated behind a coalition threshold, so the player is only deposable once over-consolidated past ordinary challenges.
  status: audit-finding

- id: H8A-014
  name: Autonomous Ascendancy loop (advance + threshold card)
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:192
  system: personnel-roster
  touches: [faction-strategy]
  slice: process
  statement: Each Accounting, consolidation_progress advances via a power_base-typed driver (seven distinct formulas, one per power_base value); at threshold an "Ascendancy card" fires with a power_base-appropriate menu (claim office, betray patron, expose secret, install successor, capture the gate, cohort capture, convert to asset, press a banked claim, force ratification, purge predecessor, seize Mandate custody), emitted through the Key substrate.
  status: audit-finding

- id: H8A-015
  name: "gap" — Lineage/clan-scope object above NPC lifespan
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:549
  system: personnel-roster
  touches: [faction-strategy]
  slice: gap
  statement: The Accounting-cascade tick needs an entity above a single NPC's lifespan to model multi-generation cases (Wang Mang's dynastic_leverage across five reigns; malikane family Entrenchment). Called "the single biggest structural ask" of the roster proposal; whether Valoria wants clan-scale actors at all is left as a scope call.
  status: audit-finding

- id: H8A-016
  name: "gap" — Coalition / joint ambition object
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:554
  system: personnel-roster
  touches: [faction-strategy]
  slice: gap
  statement: Ambitions today are strictly per-NPC; a multi-NPC joint ambition object is needed for the Night-of-the-Long-Knives-style Coalition Purge (G6) and the Thermidor-style procedural purge (G9). Called "the clearest new-mechanic requirement" in the entire downfall set.
  status: audit-finding

- id: H8A-017
  name: "gap" — Peninsula-scale renown aggregation
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:558
  system: personnel-roster
  touches: [npc-social]
  slice: gap
  statement: A jurisprudential/doctrinal `renown` track must sum witness/gossip Keys across many settlements an NPC never administers, requiring an aggregation scope above any single settlement — a gap the document calls out explicitly by name in its own framing.
  status: audit-finding

- id: H8A-018
  name: "gap" — Mandate custody separable from possession
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:561
  system: personnel-roster
  touches: [faction-strategy]
  slice: gap
  statement: Physically controlling a Mandate-bearing figure without deposing them (Cao Cao's "support the Son of Heaven") needs `custodian_id` distinct from `holder_id`, so custody grants a legitimacy bonus while base Standing is untouched. Called "the sharpest genuine architectural gap" of the whole roster set.
  status: audit-finding

- id: H8A-019
  name: "gap" — In-transit Key interception
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:563
  system: personnel-roster
  touches: [faction-strategy]
  slice: gap
  statement: The engine has no mechanism for one NPC intercepting another NPC's Keys before they resolve (correspondence-filtering chokepoint roles); every chokepoint-control entry in the corpus needs this primitive and none currently has it.
  status: audit-finding

- id: H8A-020
  name: "gap" — Dormant/conditional and hidden-visibility Ledger tags
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:566
  system: personnel-roster
  touches: []
  slice: gap
  statement: Two proposed new Ledger-tag capabilities are unbuilt: a tag that sits inert until a specific Key fires (`trigger_condition: succession`, for succession-cascade purges) and a tag with a hidden/concealed visibility flag that only becomes legible after an exposure Key (e.g. embezzlement Debt invisible until `audit_exposed`).
  status: audit-finding

- id: H8A-021
  name: "gap" — co_leadership state and mutable office succession_rule
  source: audit/2026-07-12-governance-compendium/40_roster_officer_system.md:568
  system: faction-strategy
  touches: [personnel-roster]
  slice: gap
  statement: Part 2's succession model treats Leadership as a single binary state and offices as static slots; the corpus needs an intermediate co_leadership/shared-rule state (Romanos I Lekapenos) and a mutable per-office succession_rule (Carolingian hereditary lock-in), neither of which exists today.
  status: audit-finding

# ==================== 41_proactive_scale_menus.md ====================

- id: H8A-022
  name: Organization entity (own Standing ladder + AP pool)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:238
  system: settlement-governance
  touches: [faction-strategy, personnel-roster]
  slice: primitive
  statement: A proposed new entity type — a member roster on its own Standing ladder (parallel to, not nested inside, faction Standing), an Org AP pool, and an optional Org Treasury — representing a membership that is dispersed across settlements it does not own (guilds, orders, chartered companies). No existing state can express a body holding land or members the faction doesn't administer.
  status: audit-finding

- id: H8A-023
  name: Territory entity (roster + governance-mode + command-split flags)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:268
  system: territory-world
  touches: [settlement-governance, faction-strategy]
  slice: primitive
  statement: A proposed new entity — a roster of settlements plus an appointed-administrator identity, a Governance-Mode flag (Local/Appointed), and a civil/military-split flag — representing a cluster held as an aggregate. This is the object the document identifies as answering both the previously-open BYZ-6 (Consolidated Command) and IT-5 (Legation Split) design questions.
  status: audit-finding

- id: H8A-024
  name: "gap" — inter-settlement propagation lever contingent on unauthored temporal model
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:345
  system: territory-world
  touches: [cross-scale-plumbing]
  slice: gap
  statement: Relay Tier (0–3, propagation speed) and Beacon Network (0–3, alarm hop-radius) are named "the single strongest new-state case in the corpus," but both presume Valoria has inter-settlement latency for a turn structure to gate — a temporal model that does not exist (`engine_clock` carries `doc: null` per CLAUDE.md §6). The lever cannot be evaluated until that gap closes.
  status: audit-finding

- id: H8A-025
  name: Shared cross-settlement Reserve Pool
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:346
  system: territory-world
  touches: [economy-accounting]
  slice: primitive
  statement: A treasury-like store, distinct from any single settlement's walled Treasury, that moves surplus between settlements (Inca Qollqa, Song Ever-Normal rollout). The internal interest/replenish logic is explicitly left underspecified — "a design intent, not a spec."
  status: audit-finding

- id: H8A-026
  name: The Grant Ledger (revenue rights held by a third party)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:347
  system: territory-world
  touches: [personnel-roster, economy-accounting]
  slice: primitive
  statement: A ledger recording revenue rights over a settlement bundle held by an entity that is neither the settlement nor the whole faction (an Ottoman-timar-style grant-holder). Named the literal seam between settlement and faction scale.
  status: audit-finding

- id: H8A-027
  name: Muster tag (land-tenure-for-defense)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:348
  system: territory-world
  touches: [mass-battle-seam]
  slice: primitive
  statement: A proposed Ledger-tag family giving a permanent Defense floor with no ongoing Treasury upkeep, paid for by a permanent Prosperity-growth tax; it auto-answers Levy directives with troops instead of Treasury, but is Disposition-contingent — a garrison whose loyalty collapses can flip the tag to Grudge and defect.
  formula: "permanent Defense floor; no AP/Treasury upkeep; permanent Prosperity-growth reduction; flips to Grudge/refusal if garrison Disposition collapses"
  status: audit-finding

- id: H8A-028
  name: Cordon-Complete chain-topology flag
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:349
  system: territory-world
  touches: []
  slice: primitive
  statement: A binary/tiered aggregation flag over a defined settlement chain (Hadrian's Wall, the Belgorod Line) that pays a bonus only while the chain is geographically unbroken; one member settlement dropping below threshold removes the bonus for the whole territory.
  status: audit-finding

- id: H8A-029
  name: BYZ-6 / IT-5 concrete resolution shape (command-split flag + per-verb permissions table)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:372
  system: territory-world
  touches: [faction-strategy]
  slice: gap
  statement: The two previously open-ended "needs_jordan (undefined)" multi-settlement proposals now have a concrete proposed shape — a command-split flag on the Territory entity (Consolidated Command = "consolidated" setting, historically the dangerous one) and a per-verb authority-tier permissions table (Split Verb Authority, the Venetian rettori pattern) rather than an all-or-nothing legation. Still an open Jordan ruling, now a choice among specified options rather than an open design problem.
  status: audit-finding

- id: H8A-030
  name: power_base as scale-action eligibility filter; consolidation_progress as the spent/reset resource
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:400
  system: personnel-roster
  touches: [faction-strategy, territory-world]
  slice: mechanic
  statement: Proposed integration rule between the Ascendancy roster system and the four-scale action menus — power_base type gates which scale-actions a character can initiate (e.g. no Raise a Standing Corps without a military basis), while consolidation_progress is the currency faction-scale structural reorgs raise, spend, or reset on a rival. Explicitly self-flagged as reading cleanly off `initiator_level` fields but not yet checked against the Ascendancy doc's own power_base semantics — needing canon-guard review before adoption.
  status: audit-finding

- id: H8A-031
  name: "gap" — Organization economy unspecified
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:449
  system: settlement-governance
  touches: [economy-accounting]
  slice: gap
  statement: The Organization entity's resource loop is undefined — what "Org AP"/"Guild Capacity" numerically is, and how Org Treasury relates to member dues, responsions tithes, and assay fees. Called "the single biggest authoring gap" behind the whole Organization scale, including the org-scale Fugger Audit-Branch circuit-breaker (see H8A-060).
  status: audit-finding

- id: H8A-032
  name: Territory Reach-Cap trigger (the one required number)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:353
  system: territory-world
  touches: []
  slice: gap
  statement: A settlement-count or AP-load threshold past which a Territory's own Order/Π aggregates start representing "the governor can't reach everyone," forcing a Partition/Redistrict rather than an indefinite decline; explicitly flagged as the one place in the whole four-scale proposal where a bare number is unavoidable, and it is left unspecified per CLAUDE.md §5.
  status: audit-finding

- id: H8A-033
  name: Four-scale characteristic-tension framing (Organization / Settlement / Territory / Faction)
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:24
  system: territory-world
  touches: [settlement-governance, faction-strategy]
  slice: process
  statement: Proposes that Organization, Settlement, Territory and Faction are not four sizes of one thing but four different kinds of managed object, each with its own intrinsic tension (Organization: unity vs dispersion; Settlement: bounded budget vs compounding pressure; Territory: reach vs uniformity vs local autonomy; Faction: control vs the cost of centralization) — the framing used to derive which of the ~72 catalogued historical proposals needs new state versus a verb option on an existing scale.
  status: audit-finding

- id: H8A-034
  name: Proactive-menu and reactive Crisis-card system must ship as one loop
  source: audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:488
  system: settlement-governance
  touches: [faction-strategy]
  slice: gap
  statement: Several proactive-governance levers (intendants, forced annexation-compensation, standardization) are historically load-bearing for collapse (the Fronde, the Satsuma rebellion). If stacked Grudges from using them do not auto-seed Crisis-family cards, the game gets the centralizing upside with none of the historical downside — an explicitly named risk if the two systems ship sequentially rather than together.
  status: audit-finding

# ==================== 42_action_verb_catalogue.md ====================

- id: H8A-035
  name: Parent-verb re-indexing scheme over the event-card corpus
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:19
  system: settlement-governance
  touches: []
  slice: process
  statement: Re-indexes the ~94-card historical event catalogue (organized by event) into the inverse view organized by parent verb — the eight base settlement verbs (Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate) plus Directive and a NEW bucket — so a designer can ask "what can a governor do, and which verb does it hang off of."
  status: audit-finding

- id: H8A-036
  name: "gap" — four unresolved reskin/duplicate mechanic clusters
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:211
  system: settlement-governance
  touches: []
  slice: gap
  statement: The source catalogue did not collapse four same-mechanic/different-name clusters: the standing famine-buffer facility (Ever-Normal Granary vs Civic Granary), the currency-clearing Directive (Recoinage vs Currency Reset), the convoy/fleet timing-exposure mechanic (Storm-Season Staging/Withdrawal vs Flota Scheduling), and the general "Crisis-gated post-loss unlock" pattern (Lighthouse, Purpose-Built Galleon, Coalition Fortify Pool) — each flagged as needing consolidation before a Godot implementer re-derives the same gate three times independently.
  status: audit-finding

- id: H8A-037
  name: Court Officer Disposition (Keep Order lever against bribed defection)
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:84
  system: personnel-roster
  touches: [faction-strategy, mass-battle-seam]
  slice: mechanic
  statement: A proposed Keep Order/Treat lever that shores up a high-rank officer's loyalty specifically to deny a rival faction the Rival Cohort opening for a bribed defection or coup, motivated by the Battle of Plassey / Jagat Seth bankers case.
  status: audit-finding

- id: H8A-038
  name: Succession-configuration Directive family (Oath, Fratricide, Partible, Elective)
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:185
  system: faction-strategy
  touches: [personnel-roster]
  slice: mechanic
  statement: Four proposed succession-shaping mechanics under the Directive bucket: Extract Succession Oath (a fifth, oath-based heir claim basis that taxes defectors with Grudge/Reputation:Oathbreaker), Fratricide Law (strips all losing claimants rather than let them persist as splinters), Partible Succession (a durable founding-time config that maximizes dynastic footprint but permanently disables peaceful succession rows), and Elective Succession (routes contested succession to an electoral tally instead of pure strength/Standing math).
  status: audit-finding

- id: H8A-039
  name: Convene Consulta / Convene Rival Assembly
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:190
  system: faction-strategy
  touches: [personnel-roster]
  slice: mechanic
  statement: Two paired succession-contest mechanics — Convene Consulta tallies Standing+Disposition+Influence for a majority-wins Regency succession, bypassing the dice resolver; Convene Rival Assembly lets a losing claimant convene their own legitimating assembly and Defy the verdict, overriding a unified resolution into a permanent split.
  status: audit-finding

- id: H8A-040
  name: Settle & Confiscate (post-Conquest personnel/land replacement)
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:191
  system: faction-strategy
  touches: [personnel-roster, territory-world]
  slice: mechanic
  statement: A proposed post-Conquest domain action forcing subnational faction-roster replacement and land reallocation after a "quarter denied" atrocity (Siege & Sack of Drogheda), writing a fresh Outlawed tag that raises future Grudge/Intrigue generationally.
  status: audit-finding

- id: H8A-041
  name: Trade Writ (Levy cap on untaxed lineage wealth)
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:189
  system: faction-strategy
  touches: [economy-accounting, personnel-roster]
  slice: mechanic
  statement: A proposed Levy method capping an untaxed lineage's independent Wealth at a Disposition cost, or driving it underground (Outlawed + Grudge) if the target Rejects — motivated by the Kongo Civil Wars.
  status: audit-finding

- id: H8A-042
  name: "Hard-won lesson" unlock class (Crisis-gated post-loss unlock)
  source: audit/2026-07-12-governance-compendium/42_action_verb_catalogue.md:233
  system: settlement-governance
  touches: []
  slice: process
  statement: A named general design pattern behind three separate proposed mechanics (Lighthouse, Purpose-Built Galleon, Coalition Fortify Pool): a mitigation is unlocked only after its associated crisis has fired once and been survived — "you must suffer the loss once before the mitigation becomes purchasable."
  status: audit-finding

# ==================== 43_directive_types.md ====================

- id: H8A-043
  name: Embargo (Directive targeting a third faction)
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:21
  system: faction-strategy
  touches: [economy-accounting]
  slice: mechanic
  statement: A proposed Directive type whose Comply/Bargain/Defy fork is resolved not by the settlement it targets but by the enforcing settlement, over how much of its own trade to sacrifice to damage a third faction's economy; Bargain grants a License Exception (a callable Debt chit).
  formula: "trigger: target holds bloc-network trade-dependent Prosperity AND hegemon Grudge-tagged toward it AND hegemon cross-faction Standing >= target's, mid-high Pi"
  status: audit-finding

- id: H8A-044
  name: Multilateral / Coalition Embargo
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:31
  system: faction-strategy
  touches: [economy-accounting]
  slice: mechanic
  statement: A coalition-issued variant of Embargo (H8A-043) gated through Ministry/Consulta, whose defining feature is that it structurally removes the Bargain branch entirely — the response collapses to a binary Comply (capitulate) or Defy (Muster into war).
  status: audit-finding

- id: H8A-045
  name: Recall (disband an appanage grantee's independent military)
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:41
  system: faction-strategy
  touches: [personnel-roster, mass-battle-seam]
  slice: mechanic
  statement: A proposed Directive targeting a grantee holder (not a settlement) that disbands their independently-held military; its Defy branch is diagnostic — refusal to disband confirms the grantee intends to convene a rival legitimating assembly and is itself the signal a succession is about to permanently fracture.
  status: audit-finding

- id: H8A-046
  name: Quarter (forces Force-method Keep Order, overriding the governor)
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:51
  system: settlement-governance
  touches: []
  slice: mechanic
  statement: A sibling Directive to the canon Host type, coercively forcing Force-method order-keeping on a settlement for its duration and overriding the governor's own Consent/Clergy preference; ignoring the resulting Petition strain escalates to a Boston-Massacre-style Crisis that ratchets the governor's own future menu toward more coercion.
  status: audit-finding

- id: H8A-047
  name: Nationalize Charter (crisis-gated Quo Warranto bypass via arbitration)
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:61
  system: faction-strategy
  touches: [economy-accounting]
  slice: mechanic
  statement: A proposed, not-confirmed-as-enum-member Directive-shaped action seizing a Charter outside the normal 16-season Quo Warranto window once the holder's leverage has independently eroded; resolution routes through Ministry/Consulta arbitration that can override the battlefield outcome rather than the campaign deciding it.
  status: audit-finding

- id: H8A-048
  name: Sovereign Bargain (rank-gated Bargain amendment, Standing-6+ only)
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:71
  system: faction-strategy
  touches: [settlement-governance]
  slice: mechanic
  statement: Not a new Directive type but a rank-gated amendment converting an open-ended reprisal spiral under an active Suppress-family occupation into a bounded, fires-once Compact indemnity; available only to a Standing-6+ actor, so an ordinary governor cannot invoke it.
  status: audit-finding

- id: H8A-049
  name: Reconciled Directive enum (6 canon + 6 proposed)
  source: audit/2026-07-12-governance-compendium/43_directive_types.md:94
  system: faction-strategy
  touches: [settlement-governance]
  slice: derivative
  statement: Consolidates the live canon Directive enum (Extract, Tax, Suppress, Install, Host, Cede — verified current against `research/cross_scale_action_catalogue_v1.md` §2.3) against six PROPOSED additions (Embargo, Multilateral Embargo, Recall, Quarter, Nationalize Charter, Sovereign Bargain), with an open question of whether the last two should be full enum members or amendments on existing Directives.
  status: audit-finding

- id: H8A-050
  name: "gap" — active_directive is an unconstrained string in code, not the enum any design doc describes
  source: systems/settlements/sim/registry.py:81
  system: settlement-governance
  touches: [cross-scale-plumbing]
  slice: gap
  statement: The live `Settlement.active_directive` field is typed `str | None` with no enum enforcement anywhere in `systems/settlements/sim/registry.py`, while three design surfaces (the canon 6-type enum, Part 43's proposed 6-type expansion, and `settlement_generator_v1.md`'s "expanded taxonomy") all assume a closed, validated Directive type set. Per CLAUDE.md §0.05, code is the mechanism — and the code currently enforces nothing.
  status: audit-finding
  status_evidence: "systems/settlements/sim/registry.py:81"

- id: H8A-051
  name: "gap" — a later design doc already cites Part 43's proposed Directive types as if adopted
  source: systems/settlements/settlement_generator_v1.md:126
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: The 2026-07-13 `settlement_generator_v1.md` (PROPOSAL, one day after this compendium) draws "Directive priors from the expanded taxonomy (Extract/Tax/Suppress/Install/Host/Cede + Embargo/Recall/Quarter)" as though Part 43's proposed additions were already settled, despite both documents carrying only PROPOSED status and neither having flipped a `## Status:` line.
  status: audit-finding

# ==================== 44_standing_institutions.md ====================

- id: H8A-052
  name: Standing crisis-defusing institution — the class definition
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:27
  system: settlement-governance
  touches: [territory-world]
  slice: primitive
  statement: Defines a proposed object class — a build-once facility/office/charter that must exist before its trigger fires, is family-scoped (lowers draw-weight for a whole crisis family, not one card), is self-consuming or ring-fenced from the ordinary Treasury/AP cycle, and works by decoupling a defensive function from the pressure that would otherwise starve it.
  status: audit-finding

- id: H8A-053
  name: Water Board (ring-fenced flood-defense levy)
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:48
  system: settlement-governance
  touches: [economy-accounting]
  slice: mechanic
  statement: A chartered institution — explicitly "a win condition, not an automatic grant," earned via cross-settlement Petition pressure after a catastrophic flood — funded by its own levy that is ring-fenced from Directive diversion, so a war-funding choice cannot starve flood defense.
  status: audit-finding

- id: H8A-054
  name: Ever-Normal Granary (StockLevel auto-consume against famine)
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:59
  system: settlement-governance
  touches: [economy-accounting]
  slice: mechanic
  statement: A Develop facility upgrade that accumulates a StockLevel meter via Sponsor spend in good seasons and auto-draws it when a drought/famine Crisis fires, capping severity and blocking the rebel-Ambition follow-on; decays if Treasury is diverted to Muster/Conquest instead.
  status: audit-finding

- id: H8A-055
  name: Coalition Fortify Pool (multi-faction pre-funded siege defense)
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:86
  system: faction-strategy
  touches: [mass-battle-seam, settlement-governance]
  slice: mechanic
  statement: Multiple factions jointly pre-fund a threatened settlement's Fortify ahead of a known existential-siege Crisis; surviving unlocks further cross-faction pooling, so investment and survival compound across crisis cycles.
  status: audit-finding

- id: H8A-056
  name: Loop-property recoverability classifier
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:166
  system: settlement-governance
  touches: [gap]
  slice: process
  statement: Reads the event catalogue's per-card "Loop" prose clause as a latent classifier sorting every crisis card into RECOVERABLE (blunted, denied escalation, survivable) versus TERMINAL (a one-way ratchet, a permanent cap, a self-reinforcing/inheritable spiral) — and finds the discriminating variable is almost always a single bit: was a standing institution built before the trigger fired.
  status: audit-finding

- id: H8A-057
  name: "gap" — the institution library covers world-state axes but not the Standing/rank axis
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:249
  system: settlement-governance
  touches: [personnel-roster]
  slice: gap
  statement: Cross-walking the standing-institution catalogue against the 2026-07-12 stress test's 8 doom-loop patterns finds every material-axis doom-loop (Prosperity, Order, Treasury, Defense, Pi) has a named circuit-breaker institution, but none of the three Standing/rank-axis doom-loops (the universal 7/7 demotion spiral, patron-lapse un-shielding, undefined Suspicion->Recall threshold) can be broken by any facility — their fix is resolution-substrate tuning, not an institution to build. Called the "load-bearing result" of the whole synthesis.
  status: audit-finding

- id: H8A-058
  name: "gap" — Ledger tag-family proliferation across five new proposed families
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:268
  system: settlement-governance
  touches: [faction-strategy]
  slice: gap
  statement: The corpus now proposes five additional Ledger-tag families (Compact, Concession, Outlawed, Capital-Posture, and a new Muster family) atop the existing set, with Muster/Compact flagged as possibly collapsible and Concession/Capital-Posture overlapping at frontier entries; a consolidation pass is called for before any of the five ship. This directly compounds the code-vs-design Ledger divergence recorded separately (H8A-081).
  status: audit-finding

- id: H8A-059
  name: Fugger Audit-Branch (org-scale circuit-breaker for hidden corruption)
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:130
  system: settlement-governance
  touches: [economy-accounting]
  slice: mechanic
  statement: An organization-scale institution reusing the Investigate resolver inward on the org's own branch officers, converting a hidden, silently-compounding embezzlement risk into a visible, scheduled one. Named as the pre-built circuit-breaker for the stress test's Clerk-Corruption "loaded gun" doom-loop, but not yet wired to the settlement Clerk-Capacity loop it would defuse.
  status: audit-finding

- id: H8A-060
  name: Decoupling-vs-coupling design test for a proposed institution
  source: audit/2026-07-12-governance-compendium/44_standing_institutions.md:257
  system: settlement-governance
  touches: []
  slice: process
  statement: Proposes a falsifiable design test — a candidate standing institution is only a genuine circuit-breaker if it names the specific coupling it severs (e.g. flood funding decoupled from the war Directive); if it breaks no coupling, it is a stat bump, not a defuser.
  status: audit-finding

# ==================== 45_hidden_longfuse_stats.md ====================

- id: H8A-061
  name: Jordan's standing abstraction ruling (food-supply meters fold into Prosperity)
  source: audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md:11
  system: settlement-governance
  touches: [economy-accounting]
  slice: ruling
  statement: Jordan's standing ruling is that food-supply and similar granular resource meters can abstract into Prosperity rather than requiring dedicated tracked stats; this Part is explicit that it does not override that ruling and treats it as the default for every proposed stat below. Verified consistent with the live tree — `Settlement` in registry.py carries no SiltLevel/StockLevel/OreGrade/etc. fields.
  status: designed-canonical
  status_evidence: "systems/settlements/sim/registry.py:55-84 (no granular resource-meter fields present, consistent with the ruling)"

- id: H8A-062
  name: Depth-layer track-vs-abstract decision framework
  source: audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md:21
  system: settlement-governance
  touches: []
  slice: process
  statement: A three-question test for whether a proposed environmental stat should be tracked explicitly or folded into Prosperity: is the fuse cross-settlement (a Prosperity number can't carry info between settlements), is it multi-decade (outlives the governor who caused it), and does a proposed institution need a legible gate to check against.
  status: audit-finding

- id: H8A-063
  name: RisingWaterLevel — the one stat the abstraction ruling cannot absorb
  source: audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md:137
  system: territory-world
  touches: [settlement-governance]
  slice: gap
  statement: A hidden cross-settlement tag where an upstream settlement's Scour choice silently raises a downstream settlement's flood risk, invisible to that settlement's own governor until a delayed Crisis fires. Applying the framework in H8A-062, this is the one proposed stat where abstraction to Prosperity genuinely breaks the mechanic, since Prosperity is local by construction and the entire dramatic point is that the downstream sheet shows nothing wrong.
  status: audit-finding

- id: H8A-064
  name: "gap" — StockLevel is blocked on an unresolved binary adopt/reject decision, not a granularity spectrum
  source: audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md:140
  system: settlement-governance
  touches: [economy-accounting]
  slice: gap
  statement: Unlike the other seven proposed stats, StockLevel cannot be "a little bit tracked": either food supply stays fully abstracted to Prosperity and Ever-Normal Granary becomes a flat method with no separate meter, or the granary mechanic is adopted whole-cloth with its own tracked StockLevel — a half-tracked meter that exists but doesn't really gate anything is explicitly called worse than either pure option.
  status: audit-finding

- id: H8A-065
  name: SiltLevel — conditional tracking recommendation (province-tier only)
  source: audit/2026-07-12-governance-compendium/45_hidden_longfuse_stats.md:133
  system: territory-world
  touches: [settlement-governance]
  slice: derivative
  statement: Recommends tracking SiltLevel only where a province-tier institution (Water Magistracy) consumes it as a shared veto gate; single-settlement harbor siltation with no cross-settlement lagoon can abstract to a Prosperity-trajectory modifier instead.
  status: audit-finding

# ==================== tier3_proposal_status_closure.md ====================

- id: H8A-066
  name: Verified — 58-proposal partition matches the index's claimed counts
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:44
  system: faction-strategy
  touches: [settlement-governance]
  slice: content
  statement: Counted directly against the register's own tables (§3.2a–d): 12 authored into PR#119, 9 promote-ready unlanded, 23 needs-Jordan, 14 cut, summing to 58 — an exact match to `00_index.md`'s claimed 12/9/23/14 partition. Unlike Part 42's verb count, this claim verifies clean.
  status: audit-finding

- id: H8A-067
  name: IT-3 "Sforza Gambit" reinstatement — bounded force-seizure/emergence resolver
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:170
  system: faction-strategy
  touches: [personnel-roster]
  slice: gap
  statement: A cut proposal (mercenary-captain converts a condotta into sovereignty when his employer destabilizes) that a 2026-07-12 stress test reproduced end-to-end with no resolver to cover it — the single strongest reinstatement candidate of the four, and the register's #1 prioritized finding for Jordan. Reinstatement shape: a bounded, single-purpose governance-scale force-seizure/emergence resolver, down-scoped from the "unbuilt emergence pipeline" it was originally cut against.
  status: audit-finding

- id: H8A-068
  name: VEN-SE-4 "Dedizione" reinstatement — mid-tenure negotiated extraction cap
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:181
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: A cut proposal (negotiated submission treaty preserving local privilege for legitimacy at an extraction cap) that recurred as a partial fix across four of seven stress-test seeds; its stated duplicate (SE-5) only fires at annexation, not mid-tenure, so the shape it fills is genuinely unfilled elsewhere.
  status: audit-finding

- id: H8A-069
  name: VEN-SE-7 "Sindici Inquisitori" reinstatement — roving Π-suppression audit floor
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:190
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: A cut proposal reinstated narrowly for the absentee/suppressed-Π case, not as a general add — its roving-frequency floor is exactly what the Bind-the-Cells (SE-JP1) mechanic's deliberate Π suppression evades, and its independent archive is what the CHN-9 audit-vs-Recall double-path reconciliation needs.
  status: audit-finding

- id: H8A-070
  name: BYZ-4 reinstatement — price-control half only
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:199
  system: settlement-governance
  touches: [economy-accounting]
  slice: gap
  statement: Only the price/wage-ceiling half of a cut grab-bag proposal is reinstated, to fill a confirmed gap — famine-seed stress runs have no lever to curb hoarder profiteering during a famine Crisis. The foreign-merchant channeling half remains cut.
  status: audit-finding

- id: H8A-071
  name: Crown Administrative branch flat-rank problem — the docket's #1 needs-Jordan item
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:223
  system: faction-strategy
  touches: [personnel-roster]
  slice: gap
  statement: Of the three Crown Standing-3 specialty branches in `faction_politics_v30.md` §1.1b, Martial and Intelligence each open a rich sub-office ladder while Administrative states it opens none — seven competing proposals (CHN-2, HRE-1, VEN-FA-1, VEN-FA-2, IT-4, HAB-3, FA-JP1) target this one empty slot. The question of whether the flatness is deliberate contrast or an oversight is an unresolved Jordan taste call; CHN-2 (Imperial Examination Ladder) is the surviving candidate shape if the answer is yes.
  status: audit-finding

- id: H8A-072
  name: CHN-8 "Institutional Purge (Bloc)" — PRUNE verdict, costless mass-purge switch
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:125
  system: faction-strategy
  touches: [personnel-roster]
  slice: gap
  statement: A bloc-scale demotion trigger that, as specified, is a costless, contest-free, wielder-unaccountable, undetectable mass-purge switch — it fires unilaterally off a third party's Disposition with no defense roll, no backlash, and inherits total invisibility from its dependency CHN-7. Pulled from promote-ready, along with four dependent proposals (A4, A9, D3, Cohort Capture), until a non-dominance cost, a telegraph, and a leader-tier appeal threshold are specified.
  status: audit-finding

- id: H8A-073
  name: "gap" — the promised reeval/ directory of 44 files was never authored
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:28
  system: faction-strategy
  touches: []
  slice: gap
  statement: This register's own §3.0 confirms `reeval/` is empty — no standalone per-proposal re-evaluation files exist. The task brief named those files as the source of the "re-eval-vs-built-work verdict," but that work was in fact delivered as the single stress-test synthesis document instead. Confirms the caller's warning that `00_index.md`'s claimed `reeval/` directory does not exist on disk.
  status: audit-finding

- id: H8A-074
  name: Three NERS-un-adjudicated proposals (IT-6, CHN-7, VEN-SE-3)
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:416
  system: faction-strategy
  touches: [settlement-governance]
  slice: gap
  statement: Of the 44 kept proposals, 3 (Fiscal Tribunal, Chancellery Gatekeeper, Bonifiche Capital Posture) hit transient structured-output failures across three NERS audit passes and carry no subtractive verdict at all — the only un-triaged residual in the 58-proposal set, each additionally needing its own Jordan ruling (NPC-reversal-without-consent; silent harsher-Directive substitution; a sixth Ledger-tag family).
  status: audit-finding

- id: H8A-075
  name: HAB-2 "Valido" — CUT as pitched, narrower version viable
  source: audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:116
  system: faction-strategy
  touches: [personnel-roster]
  slice: gap
  statement: The Favorite/Valido power-track proposal is cut as pitched — it is a cheaper path to Std-7-rivaling power with only a tail-risk binary collapse as its cost (a dominance violation) — but the register notes a far narrower version (one new Total-magnitude collapse trigger plus a Disposition-threshold flavor note, no chair-gate bypass, no new resource) is a materially different proposal that could still land. Decision is bound together with BYZ-1's "how many parallel status tracks" ruling.
  status: audit-finding

# ==================== tier4_discovered_open_work.md ====================

- id: H8A-076
  name: F1 — settlement type-taxonomy drift (8 canon types vs 11 real registry types)
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:88
  system: settlement-governance
  touches: [territory-world]
  slice: gap
  statement: The canonical settlement-types table defines 8 types (Seat/City/Town/Fortress/Port/Cathedral/Mine/Outpost); the live registry's real type set is 11, adding Village, Fortress-City, and Cathedral-City with no defined facility slots, stats column, or local-actor counts. Cross-confirmed independently by a hand-audit and a 500-seed batch stress test, and named the structural root of 7 downstream findings.
  status: audit-finding

- id: H8A-077
  name: "gap" — 24-probe NERS stress grid specified but never executed
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:90
  system: settlement-governance
  touches: []
  slice: gap
  statement: The 500-seed stress harness defines a 24-probe NERS grid in its design, but the reported run (500 seeds x 120 seasons, 403 tests) never executed those 24 probes. This is one register row naming an unexecuted grid, not 24 individually specified probes — any NERS-sourced verdict resting on this grid (e.g. the §1.0d MERGE confirmation) should be read as "designed but unvalidated," not empirically settled.
  status: audit-finding

- id: H8A-078
  name: "gap" — Ledger tag-family divergence (code Leverage vs proposed Compact "5th family")
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:98
  system: settlement-governance
  touches: [faction-strategy]
  slice: gap
  statement: The built `ledger.py` TAG_KINDS set is {Precedent, Grudge, Debt, Reputation, Leverage}, but a separate governance proposal (PR#119's §1.3a) introduces Compact as a purported "5th family" in the slot Leverage already occupies. The baseline action catalogue independently lists the canon family set as Precedent/Grudge/Debt/Reputation/Compact with no mention of Leverage at all — a three-way disagreement between code, this compendium's cited proposal, and the baseline's own citation. Flagged as needing reconciliation before §1.3a-derived work ratifies.
  status: audit-finding
  status_evidence: "systems/settlements/sim/ledger.py:30"
  baseline_ref: cross_scale_action_catalogue_v1.md §2.4 (line 267, lists Compact with no Leverage)

- id: H8A-079
  name: "gap" — §1.0d Performance Audit likely duplicates Goldenfurt's existing G606 recall
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:101
  system: personnel-roster
  touches: [settlement-governance]
  slice: gap
  statement: The proposed Kaochengfa Performance Audit accountability cascade (§1.0d, CHN-9) is flagged as a second accountability mechanism competing with the already-designed Goldenfurt suspicion->recall cascade (G606) rather than merging onto it — one of two new cross-cutting reconciliation items the stress-test's own reconciliation pass surfaced as unresolved anywhere in the corpus.
  status: audit-finding

- id: H8A-080
  name: "gap" — church infrastructure keyed per-territory, not per-settlement as designed
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:68
  system: settlement-governance
  touches: [territory-world]
  slice: gap
  statement: `infrastructure.py` stores church-infrastructure state by `territory_id`, but the governing design specifies it per settlement (including a -4 seizure cap also specified per-settlement) — silently coarsened to province granularity in code. Any proposal reasoning about per-settlement church-infrastructure state is working against code that only tracks the province aggregate.
  status: audit-finding
  status_evidence: "systems/settlements/sim/infrastructure.py (per tier4's own citation; not independently re-opened in this pass)"

- id: H8A-081
  name: "gap" — unused per-season generation constants in infrastructure.py
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:69
  system: settlement-governance
  touches: []
  slice: gap
  statement: `infrastructure.py` defines `PT_GAIN_*`, `CI_GAIN_TEMPLAR`, and `ORDER_GAIN_*` constants per canon design, but no entry point applies them — only `build`/`count`/`seizure_ob_modifier` are wired. Per-season passive generation of PT/CI/Order from church infrastructure is described in design and absent from code.
  status: audit-finding

- id: H8A-082
  name: Cross-cutting discipline note — this compendium exists to prevent re-deriving already-solved problems
  source: audit/2026-07-12-governance-compendium/tier4_discovered_open_work.md:111
  system: settlement-governance
  touches: [faction-strategy]
  slice: process
  statement: This register was written specifically because a prior stress-test pass re-derived roughly a third of its findings from scratch without first reading the Goldenfurt slice or the baseline territory/settlement audit; it names four items (type-taxonomy drift, the Compact-vs-Leverage Ledger collision, the §1.0d-vs-G606 duplicate, and church-infra granularity) as unresolved anywhere in the corpus and liable to silently re-open if a future pass assumes them settled.
  status: audit-finding
```

## Coverage notes

Both non-existent directories (`event_cards/`, `reeval/`) were confirmed absent and no path under either was cited; `00_index.md`'s claims about them are pointers into `_workings_joined.md` (H8B's file), not this lane's. Two of the index's own headline counts turned out inflated on direct count: Part 42 claims "109 entries" but I counted ~99–101 verb rows across its ten tables (some rows bundle two named actions, e.g. "Convene Consulta / Convene Rival Assembly"); Part 40's index blurb claims "10 rise-to-influence mechanisms" but the file's own §40.1 defines exactly eight (M1–M8) — the "10" appears to conflate the 8 mechanisms with the 10 lettered research categories (A–J), which cross-cut them (categories G and H are downfall/rival-faction cross-cuts of M1/M4/M5/M7, not new mechanisms). Tier 3's counts, by contrast, verified exactly (12+9+23+14=58) and Tier 4's "24 un-run NERS probes" turned out to be one register row naming an unexecuted grid, not 24 separately specified probes — I recorded that distinction rather than fabricating 24 records. Part 41's ~72 catalogued historical proposals (S/O/T/F/X series) were read in full but deliberately not harvested as individual records per the dedup instruction — only the load-bearing new entities/levers (Organization, Territory, propagation, reserve pool, grant ledger, muster tag, cordon flag) were extracted, since transcribing all 72 would have been the "long worthless document" the contract warns against; the same restraint was applied to Part 40's ~96 individual historical case entries (A1–J10), harvested only at the M1–M8 mechanism level plus the explicitly-named architectural gaps, not case-by-case. The clearest genuine cross-file finding, surfaced only by reading tier4 and the code together, is the three-way Ledger tag-family disagreement (code's `Leverage`, the baseline's `Compact`, and this compendium's own `Compact`-as-"5th-family" proposal) — recorded as H8A-078.