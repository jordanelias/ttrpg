# Digest designs2
## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane `designs2`: archived design documents under `.designs/systems/{overview,settlements,social_contest,threadwork,ui,victory,world}/reference/` (assignment `scratchpad/assign/L_designs2.txt`, 71 files). All carry the `ARCHIVED-NOT-CANON` banner; read for intent, vocabulary and referents only. Entries are in assignment order and appended as read.

### .designs/systems/overview/reference/peninsular_strain_v30.md
- **What it is:** The "Turmoil System v1" design (file named peninsular_strain), dated 2026-04-14, approved 2026-04-17; defines Accord, Strain, universal victory, faction toolkits for territory acquisition.
- **Status:** "CANONICAL — approved 2026-04-17 (editorial batch acceptance). Integrated into victory_v30.md." Reading: historical/intent; the code does not carry Strain or Accord as stored scalars.
- **Bears on:** FA, SE, WR, CORE, SC (Govern/contest hooks)
- **Content that matters:**
  - Accord (0-3) per territory, derived as floor(mean Order of settlements in province) (:76, :226-248); Accord >= 2 required for TCV to count (:72); Accord 1 = Govern Ob +1 and zero Prosperity, Accord 0 = Revolt, garrison fights Popular Uprising (Military vs Ob 2) (:63-68).
  - Accord vs Order scale distinction: Accord is province, Order (0-5) is settlement; Order 0 resolves before Accord 0 in the same Accounting (:150-158).
  - Strain track 0-10, advances +1 per Accord<=1 territory (cap +3/season), +2 faction elimination, +1 Revolt (:300-308); decays -1 when no territory-instability, -1 per Treaty pair (cap -2), -1 public diplomatic resolution (:314-318); thresholds Peace/Tension/Fracture/Crisis/Collapse at 0-2/3-4/5-6/7-8/9-10 (:324-330).
  - Held-instability trigger (ED-743) supersedes battle-occurrence (ED-623) for both IP and Strain: IP +0/+1/+2/+3 by count of Accord<=1 territories (0-1/2-3/4-5/6+) (:276-290).
  - Universal victory "Peninsular Sovereignty": all 15 playable territories (T1-T14, T17), Accord >= 2 on directly held, Turmoil <= 6, held 2 consecutive Accountings; hegemony counts Treaty-bound/Submitted/Mandate-dominated rivals; Truce and Commercial do not qualify (:425-440). Partition co-victory kept un-struck by ruling ED-IN-0025 despite GD-1 (:467).
  - Personal-scale pathways (Domain Echo): +/-1 Order per settlement per season from PC actions (social fieldwork Disposition +3 with 2+ NPCs, investigation resolution, public violence, killing a named NPC, public defiance) (:193-204); Accord-by-acquisition-method table (conquest 1; Show of Force/Parley/Treaty/Pastoral 2; RM organizing 3; Church Seizure by PT) (:519-532).
- **Conflicts / stale:** `engine/season/rosters.yaml:3456` states GD-1's Accord and Stability clauses are not carried (no stored scalar, no carrier); a grep for "turmoil|peninsular_strain" in engine/ and modules/ .py returns nothing. The IP/Strain/Accord machinery is therefore design-only. Cites "Cultural Reformation" (struck CR-STRIKE-2026-04-19), `params_board_game.md` (board game excluded, videogame-only scope, :569). Duplicate section number "§2.5" (Restoration exception :168 and Settlement Targeting :224). The PP-NEW-05/06 rows (:602-603) still describe the superseded battle-occurrence triggers; the index file's heading for §4.4 is "No Cross-Feeding" versus the body's "Shared Signal".
- **Open items:** Table of Category B settlement targeting (:228-250) is where "which settlement takes the Order change" is decided; nothing in code reads it [UNVERIFIED beyond grep]. §8 items all marked resolved.

### .designs/systems/overview/reference/peninsular_strain_v30_index.md
- **What it is:** Auto-generated heading and token index (doc_index_gen.py, 2026-04-19) of peninsular_strain_v30.md.
- **Status:** none of its own (generated). Reading: historical/stale (line numbers refer to an older version of the canonical; says canonical was at `designs/provincial/`, a dissolved tree).
- **Bears on:** PROCESS
- **Content that matters:**
  - Heading index of 44 sections with token sizes; whole document 10,765 tokens, §2 alone 4,427 (:72-80).
  - Records the heading "§4.4 Strain and IP — No Cross-Feeding" (:51) which the body later renamed "Shared Signal, Independent Aggregation" (ED-743).
  - Index line numbers (e.g. §2.7 at 172) do not match the current body (§2.7 at :193), so it is out of date.
- **Conflicts / stale:** Index and body disagree on line positions and §4.4 title; canonical path `designs/provincial/` is a dissolved directory (CLAUDE.md §3 "Dissolved").
- **Open items:** none.

### .designs/systems/overview/reference/wc_survival_spine.md
- **What it is:** ED-669 design note on Warden Cooperation (WC, 0-3) as the "second contest" (survival vs sovereignty), 2026-04-17, revised 2026-04-24 (ED-741, ED-759).
- **Status:** "ED-669 | Status: CANONICAL". Reading: historical/intent; WC has no carrier in engine (grep of engine/modules for WC track/warden_coop returns nothing).
- **Bears on:** WR, FA, FI (threadwork), UI/GO
- **Content that matters:**
  - Two contests: sovereignty (many solutions) vs world survival (RS maintenance, RS 0 = Rupture = all factions lose) (:20-26); note this conflicts with peninsular_strain's "No shared loss" (peninsular_strain :473).
  - WC track effects: 1 = +1D all Thread operations, 2 = Gap/Lock RS drain halved, 3 = RS +2/season at Accounting (Edeyja Mending) (:32-37).
  - Three viable late-game paths (disciplined non-Warden, WC3 + discipline, WC3 + successful Wager) plus a trap path 4 (:49-54).
  - WC decay: >= 2 disruptive Continuity ops in a season gives WC -1 (cap -1/season); Arc D Confrontation fires only if WC was >= 1 in any of the prior 4 seasons (:56-58); calibration rationale ED-759 (:60).
  - IP/expedition tension: IP rise forces military to border defence while Southernmost expeditions need escort (:66-79) — but states IP +3/season "during inter-faction battles" (:77), which ED-743 superseded.
  - Faction orientation table (Varfell primary driver, Church resistor, Niflhel structural adversary with an RS-monitoring subroutine gating Harvest) (:95-104).
- **Conflicts / stale:** Its closing line (:130) "WC 3 is the singular endgame survival path" contradicts its own three-path reframing (:49-54, ED-741). IP trigger at :77 is stale vs ED-743. Cites arc_register ARC-S15/S32/S33/S34, thread_constitutive_integration_analysis_v2 [UNVERIFIED existence].
- **Open items:** "Niflhel NPC AI must have an RS-monitoring subroutine" (:124) is a hard-coded NPC rule request (scripting-drift risk if built as such).

### .designs/systems/settlements/goldenfurt_slice/reference/README.md
- **What it is:** README of the Goldenfurt Governance Vertical Slice v1 (S-006 Goldenfurt, Crown breadbasket town in Kronmark), a worked example of governance_play_redesign_v1; 2026-06-23.
- **Status:** "PROPOSAL, 2026-06-23". Reading: historical/proposal; never ratified as written (the slice's own files carry findings).
- **Bears on:** SE, FA, CHAR, CORE
- **Content that matters:**
  - Four interlocking artifacts: npc_cast (6 NPC dossiers + 3 minor), event_deck (28 cards, 7 families), sim_build_spec, generation_methodology (:13-18).
  - Loop: Π (pressure) recomputes each season; deck draws 1 + floor(Π/3) cards; the Crown issues a Directive (Extract/Tax/Suppress/Host); governor has AP (3 for a Town, FacilityTier 1) (:44-66).
  - Accounting maps Prosperity to Crown Treasury and Order to Kronmark Accord (floor-avg) (:62).
  - Adversarial verification: 32 findings (15 high); fixed list including a mis-signed Π homeostat term and 7 undeclared fields (:81-85).
  - Claims S0-S1 built in `sim/territory/registry.py`, `ledger.py` on "this branch" with 6 tests (:88); `sim/` is a dissolved tree (CLAUDE.md §3) so this build no longer exists in the working tree [verified: `ls sim` empty/absent].
  - Duplicated "Build status / what's next" sections that contradict each other (:87-92 says S0-S1 built; :94-96 says "none of it runs") (:87, :94).
- **Conflicts / stale:** `sim/territory/*` retired; "Key"/Ledger-tag substrate parallels retired designs. Repo grep finds "Goldenfurt" only in engine/season/cohorts.yaml and venues.yaml (the live engine has a different treatment).
- **Open items:** numeric tuning (AP curve, Π band, suspicion-to-recall threshold) pending a "§9 sim sweep" that is not in the tree; Thread family thin (:92).

### .designs/systems/settlements/goldenfurt_slice/reference/event_deck.md
- **What it is:** 28-card starter event deck for Goldenfurt (families Petition G1xx, Friction G2xx, Opportunity G3xx, Crisis G4xx, Intrigue G5xx, Ambition G60x, Thread G7xx).
- **Status:** none stated in-file (slice README: PROPOSAL). Reading: historical/proposal.
- **Bears on:** SE, FA, CHAR, WR
- **Content that matters:**
  - Card schema: triggers (predicates on Π, Order, directive, Ledger tags), weight (base + modifiers), cooldown, npc_refs, the_ask, responses with AP cost, check, effects, `seeds` chains (:32-40).
  - Churn invariant: every card has >= 1 response with a Π delta and every player response writes >= 1 Ledger tag (:13); v1.1 fixes (G201 Π deltas, G204 secular relief, G606 "Submit to audit") (:46, :55-59, :104-108).
  - NPC ambition cards G601-G606 resolve "by relationship/state" (allied / estranged / compromised) rather than by script (:95-100, :130-132), which is the nearest design precedent for state-conditioned NPC outcomes.
  - Recall scene: a social contest to keep a post, Ob lowered by `Reputation:Just` (:108) — evidence/reputation as typed input to a contest.
  - Two-season churn trace shows S1 choices become S2 deck (:139-146).
- **Conflicts / stale:** EVT-G204 is duplicated in the file: old and v1.1 weight/ask/responses blocks both present (:52-66), with different conditions (`Wessel.progress` vs `Wessel.advance`) and old `Decline` = Π +1 vs v1.1 Π+0. Card G505 gets `Investigated(Tomas)` predicate that needs a history-trigger grammar the README lists as unresolved (sim-F4).
- **Open items:** predicate-grammar history triggers; empty Wessel/Greta collision card (README :84).

### .designs/systems/settlements/goldenfurt_slice/reference/generation_methodology.md
- **What it is:** Retrospective note (2026-07-12, lane SE) on the "vectorized-slice-stack with noisy throughlines" authoring technique used for the Goldenfurt slice, with a reproduction recipe.
- **Status:** "ANALYSIS / working notes (retrospective, Jordan-vetoable)". Reading: historical/proposal; the generator it recommends was later proposed as settlement_generator_v1.
- **Bears on:** SE, CHAR, WR
- **Content that matters:**
  - Pipeline: SEED (map point in valoria_geography_v30.yaml) -> CONDITION (province frame) -> STACK of weighted slices (type, economy bias, governance, religion, temperament) -> NOISE -> THREAD (collision-wired cast + deck + Π homeostat) -> VERIFY (:29-53).
  - Claims ~15,000 nominal profiles from ~30 authored rows, as P(settlement)=P(geo)·prod P(slice_i|geo) (:92-97).
  - Failure modes evidenced by the verification pass: coupled slices sampled independently (7 missing fields), mis-signed weight hidden by noise, threading manufactures dominated choices, one-way ratchets (:139-155); cites a 500-seed stress test where "mean 3.6 of 4 factions eliminated" is the default (`tests/sim/settlement_mgmt_stress_01/`) (:145-149).
  - Honesty note: the S-006 id is triple-booked — geography yaml puts S-006/S-007 in T3 Lowenskyst, settlement_layer :330 / :912 give contradictory names, README and temperaments place Goldenfurt in Kronmark T2 (:194-199). Engine (cohorts.yaml:70, venues.yaml:151) uses S-006 Goldenfurt in T2.
  - Recipe step 3: the cast must collide on four common verbs: Hold Court, Keep Order, Levy, Investigate (:173-176).
- **Conflicts / stale:** references `designs/audit/...` and `designs/territory/` (dissolved trees). The recommended build was apparently never committed as a tool [UNVERIFIED].
- **Open items:** the id/province inconsistency was "worth an ED"; not checked whether one exists.

### .designs/systems/settlements/goldenfurt_slice/reference/npc_cast.md
- **What it is:** Six collision-wired NPC dossiers (G01-G06) and three minor local actors for Goldenfurt, specified for agency (ambition) and leverage.
- **Status:** none in-file (slice PROPOSAL). Reading: historical/proposal; precedent for NPC schema.
- **Bears on:** CHAR, SE, FA, WR
- **Content that matters:**
  - NPC schema: id, role/faction, ethic (alpha outcomes / beta conduct), convictions, ambition {goal, method+escalation, timeline, fires_card, autonomous advance}, loyalty/Disposition, leverage {wants, fears, secret}, Knots, trajectory by state (:13).
  - Autonomous advance rules are per-NPC predicates (e.g. Hedda +1 per season with an open public grievance she champions, +0 if governor rules consistently justly (:48); Konrad +1 per Defy/Bargain, +1 on falling Order, +1 under quota or RM/Niflhel rise, cap +1/season (:115)). These are exactly scripted per-NPC rules, the scripting-drift pattern the brief warns of, where a generic chooser reading conviction would serve.
  - Trajectory branches "if blocked / if conviction violated / if Disposition low" give a reusable shape for state-conditioned NPC response (:52, :64, :78, :92, :105, :119).
  - Secrets/leverage as discoverable via `Investigate` (Konrad takes Orsk's coin; Hedda shields brother Tomas) (:50, :63, :117): secrets are typed leverage objects, not narration.
  - Tomas reachability fix: ferryman Old Brun names who crosses, so an Investigate surfaces Tomas at any Order (:91).
- **Conflicts / stale:** G05 Greta has a duplicated "Trajectory" bullet (:105-106). Engine npcs.yaml:121 has "Hedda Kronvald" (a different Hedda; no Vorn/Orsk/Konrad found by grep).
- **Open items:** Knots to LA-G01..G03 are decorative (verification npc-F5); ethic tags not read by any branch (npc-F6).

### .designs/systems/settlements/goldenfurt_slice/reference/sim_build_spec.md
- **What it is:** Implementation spec for the governance loop: Settlement registry dataclass, Ledger, eight governance verbs, Directive generator, deck engine with Π homeostat, NPC ambition tick.
- **Status:** none in-file (slice PROPOSAL). Reading: superseded/historical (targets `sim/territory/`, `sim/peninsular/` which are dissolved; engine/season is the live code).
- **Bears on:** SE, FA, CORE, CHAR
- **Content that matters:**
  - `Settlement` fields: prosperity/defense/order 0-5, legitimacy L and popular_support PS 0-7, facility_tier 0-3 giving AP = 2 + tier (+1 Seat/Cathedral), suspicion, pressure Π 0-10, active_directive, religious_building, church_attention, ledger (:30-61, :63-65).
  - Ledger tags (Precedent/Grudge/Debt/Reputation/Leverage) live on the settlement not the governor so they survive succession; Reputation single-valued (:78).
  - Eight verbs: develop, fortify, keep_order, hold_court, sponsor, treat, levy, investigate; every verb must write >= 1 world-delta (:97).
  - Π homeostat: Π_next = clamp(Π + unserved needs + 0.5/Grudge + 0.5/ambition-in-motion + shock - player releases + restore_toward(3), 0, 10); draw count 1 + floor(Π/3) (:132-153).
  - Predicate grammar to be kept tiny, no eval; "if a card needs real logic it's a coded handler" (:136, :208).
  - Open risks: content volume (60-100 base cards), AI Directive quality, Π tuning band guess (:208-212).
- **Conflicts / stale:** Names `social_contest(§7)` dangling reference (verification sim-F8). Live engine reaches settlements through `engine/season/` registries, not these modules. The Ledger-tag "kind:key" scheme parallels but is not the retired Key substrate [UNVERIFIED].
- **Open items:** `political_value` (§2.4) and fracturing triggers (§2.3) "remain unspecified in canon" (:212).

### .designs/systems/settlements/goldenfurt_slice/reference/verification_findings.md
- **What it is:** Record of a 4-lens adversarial verification of the Goldenfurt slice (2026-06-23): 32 findings (15 high, 12 medium, 5 low).
- **Status:** none in-file. Reading: historical (one-round review record); most fixes folded in v1.1.
- **Bears on:** SE, CHAR, PROCESS
- **Content that matters:**
  - High defects: mis-signed Π term (CG-1), 7 undeclared fields (sim-F1/2/3/5/7/9), no "none" Directive (CG-3), G201 vise, Konrad purely reactive (npc-F1), G606 recall death-spiral, G204 vise, no payoff-for-play (deck-F5) (:21-38).
  - Pattern "one-way ratchet without a restoring term" recurs (suspicion, recall) (:33, :32).
  - Open: predicate grammar for event-history triggers (sim-F4), empty Wessel/Greta collision (npc-F4), decorative Knots (npc-F5), ethic unread (npc-F6), succession test coverage (F12) (:38-59).
  - Verdict: architecture sound, content has balance and completeness gaps (:67).
- **Conflicts / stale:** README says "fixed in this commit" while some rows still marked pending.
- **Open items:** all rows marked ⏳ (sim-F4, deck-F6, npc-F4/F5, CG-5b, sim-F7b, sim-F8, sim-F10, F11, F12, deck-F7, npc-F6).

### .designs/systems/settlements/reference/generation_sourcebook_v1.md
- **What it is:** Grounding index (2026-07-13, lane SE, cross-cutting IN/FA/WR) for weighted-paradigm-stack generators at settlement, faction and territory scales; includes the 17-province scalar table and a blocker register.
- **Status:** "REFERENCE / working notes, Jordan-vetoable". Reading: historical/reference; several blockers are marked resolved inside it.
- **Bears on:** SE, FA, WR, CHAR, CORE
- **Content that matters:**
  - Three nested stacks: settlement P1-P15, faction F1-F8 (substrate-posture, role template, stat block, holdings, sub-organization ladder, emergence path, 9 political axes, AI directive tree), territory R1-R9 (:29-65).
  - 17-province table with fort 0-4, spiritual_weight 0-5, proximity_calamity 0-5, starting_pros, temperament pair (pragmatic 0.7/0.3, traditional 0.3/0.7, balanced, principled 0.2/0.8, outcomes-only 0.9/0.1) (:76-94).
  - Binding constraint: each generated faction's substrate-posture must be structurally distinct, "never a palette-swap" (:49-51); acceptance bar: a designer answers in one sentence whose position is at risk, what each named actor wants, what happens if no one acts (:124-127).
  - Rulings recorded: starting faction count = 4 (Valorsmark, Hafenmark, Varfell, Church) via ED-IN-0047/ED-FA-0001 (:162); S-006 = Goldenfurt (Kronmark/T2), S-007 = Lowenskyst Fortress (:163).
  - Blocker list B3-B10: type-taxonomy drift, inert L/PS, no settlement-scale Key vocabulary (Key is now retired), no spatial substrate, no typed engine-params schema, event-deck engine zero-code (:164-171).
  - States the live campaign loop `mc_v18` could not reach settlements, contests, fieldwork, NPC-AI (:173-175) — historical; the current loop is engine/season.
- **Conflicts / stale:** B5 (Key vocabulary) refers to the retired Key substrate; B7 (values_master.yaml) is dissolved. Faction count 4 vs the engine's roster [UNVERIFIED which roster engine/season/rosters.yaml carries]. Editorial-debt list (:179-187) includes "Church stat discrepancy L4/PS4/W3 vs 5/5/5".
- **Open items:** the 500-seed negative-bias regime check against real data "not-yet-done" (:170).

### .designs/systems/settlements/reference/governance_play_redesign_v1.md
- **What it is:** Proposal (2026-06-22, extended through 2026-07-13) to make settlement governance "choosing under constraint": AP economy, 8 verbs, Directive, Ledger of Consequence, event deck with Π homeostat, NPC ambition engine.
- **Status:** "PROPOSAL — drafted 2026-06-22"; §1.3c carries "RATIFIED (ED-SE-0023, 2026-07-13)"; §1.1a/§1.3a/§1.3b "PROPOSED". Reading: partly ratified in prose but no code (grep for Directive in engine/season .py returns nothing; verb_table.yaml carries a different verb set).
- **Bears on:** SE, FA, CHAR, SC, CORE
- **Content that matters:**
  - AP = 2 + FacilityTier (0-3), +1 for Seat/Cathedral governors; no carry-over (:39); Clerk Capacity as a hidden second AP source with hidden Clerk Corruption counter (ED-SE-0022, :41-49).
  - Eight verbs with a "method choice that hands power to a different faction" design note: Develop (Treasury/Guild/Corvee), Fortify (Garrison/Militia/Walls), Keep Order (Consent/Force/Clergy), Hold Court, Sponsor, Treat, Levy, Investigate (:59-72); reconciliation: Investigate reuses the fieldwork resolver and only authors the four-way post-discovery choice expose/expel/co-opt/shelter (:76); Administer dropped (:79).
  - Directive types Extract/Tax/Suppress/Install/Host/Cede; responses Comply / Bargain (social contest as petitioner) / Defy-Divert (suspicion +1, to Recall scene) (:123-133).
  - Ledger of Consequence: Precedent/Grudge/Debt/Reputation/Compact (fifth family, ED-SE-0019), survive succession (:141-149); Assessment tag locks a Prosperity figure for Levy/Tax (:83-91); Collective Liability tags -> "Cell Revolt" (:99).
  - Π homeostat and deck draw 1 + floor(Π/3) (:159-213); card schema with triggers, weight, cooldown, excludes, the_ask, responses, follow_on (:174-195).
  - NPC dossier = convictions + ambition{goal, method, timeline, progress} + ethic alpha/beta + leverage{wants, fears, secret} + Knots + trajectory; ambition engine "every significant NPC advances by 1 per Accounting" (:222-249). `sim_npc_as_player` named as the principle (:249, :316).
- **Conflicts / stale:** Part 5.2 build sequence gated on settlement registry G1 (sim/territory, dissolved). The ambition-advance rule here (+1 flat) differs from the dossier-specific predicates in npc_cast.md (:48, :115). Many NPC conviction/ambition/ethic ideas now live in engine/season/decision and goals.yaml [UNVERIFIED]. Mentions Key/Knots PP-724 relational graph.
- **Open items:** AP curve vs verb costs; Π weights; suspicion-to-recall vs faction-emergence thresholds; deck authorship load 60-100 cards (:328-333).

### .designs/systems/settlements/reference/lps_wiring_v1.md
- **What it is:** Buildable spec (2026-07-14, lane SE, executes E5 / ED-FA-0004 Stratum-B / ED-SE-0007) to wire per-settlement Legitimacy and Popular Support (L/PS, 0-7) into aggregation, a "consent-gate" and a write-side.
- **Status:** "PROPOSED (buildable spec)". Reading: superseded in form (targets `sim/territory/*`); the live engine carries legitimacy/stability by a different route (engine/season/tests/test_in23_legitimacy_stability.py exists); `faction_mandate`/`popular_support` not found in engine or modules .py by grep.
- **Bears on:** SE, FA, CORE
- **Content that matters:**
  - Settlement Weight W(s) = base(type) + prosperity + facility_tier, base Seat/Cathedral 4, City 3, Town/Fortress/Port 2, other 1; q(s) = 0.5·L + 0.5·PS; faction Mandate = clamp(round(7·T/(T+6)), 0, 7) with T = sum W·q/7, K=6 ruled (:57-75).
  - Consent-gate: compliance(s) = clamp((q-1)/(6-1), 0, 1) multiplies realized Treasury and AP; control_state HELD (q>=3) / CONTESTED / SLIPPING (q<1), 2 consecutive SLIPPING Accountings triggers an Independence roll (mirrors insurgency pipeline 2-season formation) (:93-126).
  - Write-side sources: scene-conduct echo (`compute_accord_echo`, zero callers), mission-outcome cascade, §1.8a event table, Mandate-to-L mean-reverting drift when |gap| >= 2, conquest init (Impose Administration sets L=1) (:132-150).
  - Accounting-boundary order: snapshot M_prev, accrue, apply, aggregate, gate, consume — argued D.6-disjoint/contractive (:161-174).
  - Calibration flagged for Jordan: base table, Q thresholds, §1.8a ratification, full vs floored Treasury throttle (:197-200); ED-SE-0045 treasury multiplier x10 vs x50 left open (:101).
- **Conflicts / stale:** Refers to `Faction.L`/`Faction.PS` raw scalars to be retired; `parliamentary_bridge`, `echo_transport` (retired Key-era transport), `tools/sim_harness/lps_inert_check` [UNVERIFIED present]. Mandate here is a derived function of settlement L/PS, versus peninsular_strain/victory docs using "Mandate" as a faction stat with its own ladder.
- **Open items:** Q1-Q4 calibration picks; §1.8a ratification; Church-Governor Axis-4 keying.

### .designs/systems/settlements/reference/march_layer_v30.md
- **What it is:** Strategic movement layer: march budget, A* pathfinding, vision/fog of war, adjacency edge types, movement sequencing; PROVISIONAL skeleton with Phase 3 body, 2026-05-01/05-10 (ED-780).
- **Status:** Header says "Status: CANONICAL" then "PROVISIONAL — Phase 3 mechanical body authored 2026-05-10"; self-contradicting. Reading: historical/intent for army movement; the gate to CANONICAL (:199-207) was never recorded as met.
- **Bears on:** MB, SE, FA, GO, FI
- **Content that matters:**
  - march_budget_pixels = Military × 100 × cavalry (1.5 if Cav >= 50%) × skirmish (1.3 if low-tier-only without siege equipment), combined cap 1.7× (:28-39); the same sentence says 1.5×1.3 = 1.95 capped at 1.7.
  - Skirmish force cannot initiate Siege; siege needs Heavy Infantry or Siege unit (:39).
  - Attrition beyond supply radius (default 8 settlements from friendly Mine/Cathedral/Port): +1 strain per season per 4 over budget, 1:1 to Size loss at Accounting (:42).
  - Budgets do not pool across armies; combined engagement needs both to arrive in the same Manoeuvre tick (:45).
  - Unauthorised inter-faction crossing: Casus Belli +1, IP −2, hostile treatment next tick (:124); Askeheim Gate edges give attacker −1D and +1 IP/season for holding (:149).
  - Vision = 240 px × terrain × weather × season; scouting costs half the season budget; Thread-Read observes settlements not mobile units; armies cannot be transported by Threads (:75-87).
- **Conflicts / stale:** Counts "26 edges / 36 settlements" (:93, :156) vs sourcebook's 37-settlement migration (generation_sourcebook :170) and "edges 49 vs 55 vs 56" editorial-debt (sourcebook :185). No march_budget_pixels / cavalry_modifier symbol in engine or modules .py (grep empty), so the formula is not in code. Calls UI "Godot 4.6" — engine version is ruled elsewhere (ED-GO-0002).
- **Open items:** MARCH-01 edge capacity, MARCH-02 Thread leap, MARCH-03 road quality, MARCH-04 naval CB; ED-055 naval left empty (§6 headings only); ED-781 stress tests (:174-182).

### .designs/systems/settlements/reference/scale_hierarchy_v1.md
- **What it is:** Jordan's direct ruling (2026-07-13, lane IN cross-cutting SE/FA/WR) on the scale hierarchy: settlement < territory < province < duchy < country; provinces conditional; governance-type cascade; L/PS as consent gate; cross-scale faction authority.
- **Status:** "RATIFIED — direct Jordan ruling, 2026-07-13, overrules valoria_political_hierarchy_v30 (PP-726) §1's 'Territory = Settlement' equivalence and §2.3's fracturing rule." Reading: ratified intent in prose; the live engine has `rung_kind: territory` and `realm` rungs (rosters.yaml:3450) but whether it carries the conditional-province rule is [UNVERIFIED]; engine/season rosters.yaml:505 still asks whether "territories inside provinces inside duchies inside realm" is required.
- **Bears on:** FA, SE, CORE, WR
- **Content that matters:**
  - New tier: Territory between settlement and province ("multiple settlements per territory, multiple territories per province") (:29-32).
  - Provinces exist only while the same faction holds their constituent territories (emergent aggregation, no fracture state machine) (:34-47).
  - Duke -> provincial governance type -> territorial -> settlement, a noisy bidirectional throughline (:49-68).
  - L/PS is the consent/resistance gate on the cascade; E5 (wiring L/PS) is the precondition for the hierarchy to matter (:70-85).
  - Factions hold PEOPLE and positional weight, not territory; local/provincial/national tiers are independent, not containment (:91-108).
  - Independence of any settlement/territory/province, and cross-scale claiming (e.g. RM claims one settlement directly) (:110-126); national ruler and Parliament bypass the chain (:128-144).
- **Conflicts / stale:** §6 propagation (rewrite of PP-726, sourcebook R/F series, tier field per faction) is "tracked, not yet executed" with no ED allocated (:11). Cites sim/provincial/parliamentary_action.py (dissolved). Conflicts with peninsular_strain's province-level Accord/TCV (territory is the TCV unit there).
- **Open items:** Part 41 Territory-scale content (Relay Tier/Beacon Network) blocked on `engine_clock` B11 (:193-195); governors at territory scale unspecified.

### .designs/systems/settlements/reference/settlement_adjacency_v30.md
- **What it is:** Settlement-level adjacency graph (edge types, canonical set generation rule) and mass battle at settlement scale (terrain from edge, settlement-type modifiers, siege), PP-666, partially superseded post PP-723 (2026-05-10).
- **Status:** Carries both "Status: CANONICAL" and "PROVISIONAL — approved mechanical design 2026-04-19 (PP-666)" with a banner "PARTIALLY SUPERSEDED". Reading: partly superseded by march_layer_v30 for movement; battle-at-settlement section kept.
- **Bears on:** MB, SE, FA, GO
- **Content that matters:**
  - Edge types Road(cost 1), River (attacker −1D), Mountain Pass (cost 2, attacker −1D), Coastal (naval only), Thread-Witnessed (cost 0, character-scale only, no army transport) (:34-40).
  - 49 settlement edges across 36 settlements (19 intra-province, 26 inter-province, 4 thread-witnessed); hub rule: every settlement adjacent to the province hub (Seat > Cathedral > Fortress > City > Port > Town > Mine > Outpost) (:44-50).
  - Army moves up to Military ÷ 2 edges per season (min 1) (:75), versus march_layer's pixel budget (Military × 100).
  - Settlement-type defender modifiers: Fortress +Fort Level to Defender Ob, Seat +1 Defender Discipline, Port +1D with naval reinforcements, Cathedral Church Casus Belli, Mine captured Prosperity (:103-110).
  - Battle consequences at settlement scale: MS, Strain, IP peninsula-wide; Accord drop becomes settlement Order −1; Prosperity −1 on Partial or worse Assault (:114-121). Siege: attacker static, defender Order −1/season to 0 = surrender (:123).
  - Invasion is path-constrained: must engage or bypass the entry settlement (:129-133).
- **Conflicts / stale:** Section numbering out of order (§6 before §5). Edge budget conflicts with march_layer (edges/season vs pixel budget). Counts 36 settlements; sourcebook notes migration to 37. "Strain +1 / IP +2 per battle" (:116-117) is the battle-occurrence trigger that peninsular_strain ED-743 struck (:500).
- **Open items:** edge capacity; Thread-Witnessed leap as transport (:153-154).

### .designs/systems/settlements/reference/settlement_adjacency_v30_index.md
- **What it is:** Auto-generated heading/token index (2026-04-19) of settlement_adjacency_v30.md.
- **Status:** none (generated). Reading: stale (line numbers and the 1,695-token size predate the PP-723 body).
- **Bears on:** PROCESS
- **Content that matters:**
  - Lists 13 headings, canonical was at `designs/territory/` (dissolved) (:10, :23-35).
  - No mechanism content.
- **Conflicts / stale:** Index omits the later §6 cross-reference to march_layer.
- **Open items:** none.

### .designs/systems/settlements/reference/settlement_generator_v1.md
- **What it is:** "Vectorized Settlement Generation (VSG v1)" proposal (2026-07-13, lane SE): a 12-paradigm (+3 downstream) seeded weighted stack that generates a settlement, its characters and event deck; must reproduce Goldenfurt.
- **Status:** "PROPOSAL / working notes, Jordan-vetoable"; closing note "PROPOSED, no ED allocated yet". Reading: proposal; not built (systems/settlements now holds only the geography YAML and SVG; no sim/ directory).
- **Bears on:** SE, CHAR, WR, CORE
- **Content that matters:**
  - Seed rule: seed = sha256(map_point ‖ paradigm_index ‖ campaign_salt) truncated to 64 bits, never a salted builtin hash; temperature τ tunes sharpness (:35-39).
  - Paradigm chain P1 Location, P2 Starting faction, P3 Size, P4 Type (11 types), P5 Piety/Restoration, P6 Altonian influence, P7 Infrastructure, P8 Economy, P9 Caste, P10 Governance type, P11 Political allegiance, P12 Sociopolitical sympathies, P13 Actor roster, P14 Event deck, P15 Verify (:51-67).
  - Three throughline kinds: conditioning (DAG edges), collision (every settlement carries >= 1 Hold-Court collision; opposed subnational pairs share a Friction card; ethic spread), coupling (jointly sample coupled paradigms; P5-P9-P1, P6-P1-P8, P8-P14) (:95-115).
  - P13 NPC sampling includes `power_base` (patronage/merit/kinship/bureaucratic/military/purchased/ideological) "which types the NPC's built-in downfall" (:126).
  - Jordan rulings 2026-07-13: temperament aggregates partially from children across scales; political allegiance off-owner allowed only if the generator can back-trace an in-world cause; weights are a taste surface with "every negative must be able to be offset by some kind of positive... unpredictable and dynamic" (:197-222).
  - Kernel/data/wrapper split: weight tables ARE the authorial surface (versioned data) (:180-186).
- **Conflicts / stale:** Targets `sim/territory/registry.py` (dissolved) and "Compact as recurring Debt subtype" (governance_consolidation D3). Cites 138 register arcs and churn-engine v2 (designs/audit, dissolved).
- **Open items:** which of the twelve paradigms survive a smaller-core cut ("worthy of investigation", :212); aggregation function for temperament.

### .designs/systems/settlements/reference/settlements_currency_v1.md
- **What it is:** Currency-lineage note (2026-08-14, ED-IN-0189) holding the narrative that used to sit in `CURRENT.md`'s settlements head row.
- **Status:** "REFERENCE — currency lineage only; rules nothing, supersedes nothing". Reading: historical.
- **Bears on:** SE, PROCESS
- **Content that matters:**
  - Names the then-live head (`settlement_layer_v30.md`, adjacency, temperaments, geography), plus scale_hierarchy_v1, governance_play_redesign_v1 and `systems/_architecture/reference/ners_vsg_reconciliation_v1.md` ("read before resuming this thread") (:22-27).
  - Lineage of rulings: ED-IN-0046 (D1-D5: Compact = recurring Debt subtype; §1.8 Mandate retired as the collapse carrier; §1.0d merged into suspicion/recall spine), ED-IN-0047 (D6 cumulative per-Defy-season suspicion accrual conditional on E11 symmetric suspicion-reduction; B1 starting 4 factions; B2 S-006 Goldenfurt; B12 hierarchy) (:33).
  - States "No SE-lane sim code yet beyond one dormant proxy" read by `faction_action.py`'s ED-FA-0013 conquest fork (:33).
  - `tools/sim_harness/` tested 29 proposals (audit/2026-07-12-pr119-harness-verification) (:33).
- **Conflicts / stale:** "§1.8 Mandate retired as the collapse carrier" (ED-IN-0046) conflicts with lps_wiring_v1, which builds on Mandate as the aggregate. References `systems/settlements/sim/registry.py` which no longer exists.
- **Open items:** none of its own.

### .designs/systems/settlements/reference/settlements_flow_skeleton_v1.md
- **What it is:** A traced flow skeleton (entry points, IN, flow, OUT, state, seams, gaps) of the OLD `systems/settlements/sim/` code at commit 654506799c…, with `path:line symbol` anchors.
- **Status:** "REFERENCE — traced structure only". Reading: historical; the traced code (`systems/settlements/sim/*`, `engine/mc_v18.py`, `engine/cross_scale/echo_transport.py`, `engine/autoload/game_state.py`) no longer exists (verified: `engine/mc_v18.py` and `systems/settlements/sim` absent).
- **Bears on:** SE, CORE
- **Content that matters:**
  - Seven traced gaps in the old sim: `compute_settlement_state`/`aggregate_to_province` orphaned; `temperaments.py` all four entry points orphaned; Accord drift probe is report-only; two uncoordinated stores (World.territories vs World.settlements, 37 settlements); Accord Echo settlement-write dormant; Ledger has no production writer; `legitimacy`/`popular_support` inert (:147-155).
  - Two production sites write `Territory.accord` bypassing `Settlement.order` (parliamentary_transfer.py:344, mass_seizure.py:293) (:93-96).
  - `religious_building` exists twice with different keys (Settlement vs InfrastructureState), the Settlement copy logically dead (:157).
  - Contract defect: `settlement_layer` contract names the orphan `settlement.py` while live `registry.py` goes uncontracted (:158).
  - Province Accord = floor(mean Order) over real member settlements (:88).
- **Conflicts / stale:** Everything cited has moved or been retired (many "RETIRED 2026-08-21 → FORK:1e4c6f4"). Useful only as evidence of the failure pattern "designed in prose, never wired".
- **Open items:** OI-37 (reconcile Territory.accord vs Settlement.order) is deferred in the old code (:149).
