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

### .designs/systems/settlements/reference/settlement_layer_v30.md
- **What it is:** The Settlement Layer Specification (2026-04-16, many later amendments to 2026-07-13): two-tier map, settlement types/stats, facility tiers, Church infrastructure, L/PS to Mandate, 37-settlement registry, dual-authority governance, subnational factions, settlement events, siege, Entry Terms, player stature ladder, faction emergence/collapse, extended timeline.
- **Status:** "CANONICAL — approved 2026-04-17 (editorial batch acceptance)" with many embedded "PROPOSED, not yet ratified" subsections (§1.8a/b/c, §3.3a, §3.3c, §4.3a/b, §5.3) and "RATIFIED" §3.3b. Reading: the largest single body of settlement intent; mostly unbuilt (settlement flow skeleton shows only stats, Order and a probe ran); the live head per old CURRENT.
- **Bears on:** SE, FA, CHAR, WR, MB, SC
- **Content that matters:**
  - Province Accord = floor(mean settlement Order) (:69); settlement stats Prosperity/Defense/Order 0-5; derived Local Economy = Prosperity×50, Garrison = Defense×20 + Fort×30, Public Order = Order×20 (:53-57).
  - Weight W = base(Type) + Prosperity + FacilityTier (Seat/City/Cathedral 3, Town/Fortress/Port 2, Village/Mine/Outpost 1); q = 0.5L + 0.5PS; Mandate = round(7T/(T+6)) (:166-176); NOTE base values differ from lps_wiring_v1 (Seat 4 / City 3 / Cathedral 4) (lps_wiring :59).
  - Settlement L/PS event tables: L: oath +1, charter +1, regular court +1, stance broken −1; PS: dearth relieved +2, festival +1, defended +2, levy −1, forced billeting −1, public execution −2 (:214-231); succession: normal leaves L unchanged, contested/emergency/imposed L −1 plus Regency (:263-267); emigration: >= 2 Dearth/Order<=1 seasons loses 1 Weight (:294-300).
  - Registry: 37 settlements (35 Kingdom + Himmelenger S-036 + Schoenland S-037); S-006 Goldenfurt Town in Kronmark, S-007 Lowenskyst Fortress (:324-445); sub-features (districts) are not siege targets (:316, :449-483); migration map from the old 36-id list (:489-528).
  - Governor/governance: standing gates (3 Town/Outpost, 4 City/Fortress/Mine, 5 Seat/Cathedral), 4 governance actions Develop/Fortify/Pacify/Administer with Ob formulas (:549-563); subnational faction table with management effects (Church, Guilds, Ministry, Löwenritter, RM, Wardens, Niflhel) (:575-583).
  - Charters/Quo Warranto: revoke Ob = Influence÷2 + floor(age/8); charters older than ~16 seasons need a public Quo Warranto social contest, plus Order −1 peninsula-wide in settlements that faction-type manages (:621-631); Za patron-lapse (:659-669); Seggio council (:677-700).
  - Dearth chain: triggers (Prosperity 0, grain route cut, levy at Prosperity<=1), verbs Open Granary / Fix Prices / Requisition / Ignore / Provision, new `granary` 0-3 field (:767-786); grain routes make Hafenmark dependent on T5/T6 or Ports (:819-834).
  - Siege/assault/bypass (:912-920); Surrender-on-terms vs Storm branches (non-Overwhelming result only) owned jointly with faction_action (:941-960); Entry Terms: Confirm Privileges seeds L=3, Impose Administration seeds L=1 and Order −1 (:989-1012).
  - Stature ladder Renown/Standing to governance scope; 5-stage faction emergence; Founded Faction starting stats L2/PS3/Mil1/Stab3; collapse contracts to city-state (:1027-1093); IP baseline halved; Generational Shift clock 0-10, +1 per 5 years, leaders lose attribute at 10/20/30 years unless TS >= 50 (:1103-1117).
- **Conflicts / stale:** §4.5 says "~45-50 Local Actors across 36 settlements" (:866) and §4.1 "S-015 Gransol Parliament" (:712) while the registry renumbered Gransol to S-018 (:382, migration :505) — stale IDs inside the doc. Part 5 heading is followed by §4.7-4.9 and §4.6 sits after Part 8 (out-of-order). Province Accord rules cite peninsular_strain §2.3-2.4 which operate "by modifying settlement Order"; its §2.1 table uses old IDs. `derived_stats_v1` citation correction note says the real doc marks these formulas "PENDING" (:51). Mandate retired as collapse carrier by ED-IN-0046 (settlements_currency :33) vs §1.8 Mandate as canonical aggregate. Engine uses S-006 Goldenfurt (engine/season/venues.yaml:151) consistent with this registry.
- **Open items:** ED-SETT-01/02 (starting stats, governance Ob calibration) deferred to a smoke test never run in the tree; per-province vs per-settlement grain route tracing; Seggio and Sack branches `needs_jordan`.

### .designs/systems/settlements/reference/settlement_layer_v30_index.md
- **What it is:** Auto-generated heading and token index (2026-07-08) of settlement_layer_v30.md; whole doc 25,697 tokens.
- **Status:** none (generated). Reading: stale against the current body (line numbers off by roughly 40 to 190; omits §1.8's later subsections' final form and §3.3b/c, §1.3a).
- **Bears on:** PROCESS
- **Content that matters:**
  - Token sizes show the weight of the doc: Part 1 7,321 tokens, Part 2 3,617, Part 3 3,044, Part 4 3,681, Part 5 2,719 (:101-139).
  - Heading list omits §3.3b and §3.3c (added after 2026-07-08).
- **Conflicts / stale:** canonical path `designs/territory/` (dissolved).
- **Open items:** none.

### .designs/systems/settlements/reference/territory_temperaments_v30.md
- **What it is:** Per-province public temperament authoring (PP-686 v2 Phase B Stage 6, 2026-05-01) for T1-T17, with a faction aggregate and drift rule.
- **Status:** Header says "Status: CANONICAL" and the banner "PROVISIONAL — Class A authoring... pending Stage 10 calibration". Reading: self-contradictory; provisional data; intent only (engine/season mentions temperament in cohorts.yaml and a few harness/epistemic files, not as this table [UNVERIFIED]).
- **Bears on:** SE, FA, CHAR, WR
- **Content that matters:**
  - Five temperaments as alpha (outcomes) / beta (conduct) pairs: pragmatic 0.7/0.3, traditional 0.3/0.7, balanced 0.5/0.5, principled 0.2/0.8, outcomes-only 0.9/0.1 (:20-26).
  - Province assignments (e.g. T2 Kronmark traditional; T6 Stillhelm, T13 Oastad, T15 Askeheim outcomes-only; T9 principled) (:41-57); faction aggregates uniform-weighted: Crown ≈0.50/0.50, Church 0.20/0.80, Hafenmark ≈0.55/0.45, Varfell ≈0.50/0.50 (:67-70).
  - Faction effective temperament = population-weighted mean over territories; RM and Löwenritter derive theirs from territories they operate in (:28, :72).
  - Drift: `temperament_drift += 0.1 × strain_delta` clamp [−1, 1] on strain shock (:86-89) — uses `env.peninsular_strain_shock` Keys, a retired Key-era interface.
- **Conflicts / stale:** Strain-shock Key interface is retired (ED-IN-0232); Strain itself has no carrier in code (see peninsular_strain entry). VSG ruling wants temperament aggregated across scales, not province-only (settlement_generator §7).
- **Open items:** settlement-level temperament (Stage 6b) deferred; population weighting uniform.

### .designs/systems/settlements/reference/valoria_political_hierarchy_v30.md
- **What it is:** PP-726 political hierarchy canon (2026-05-10): Valn > Kingdom > Duchy > Province > "Territory = Settlement"; special-case entities; settlement counts, march-route rule, province fracturing, political value, governor assignment, vetting block.
- **Status:** "PROVISIONAL — Class A". Banner states §1's "Territory = Settlement" equivalence and §2.3 fracturing rule are SUPERSEDED (2026-07-13) by scale_hierarchy_v1. Reading: partly superseded; Duchy tier, settlement/province counts and special entities still the descriptive base.
- **Bears on:** FA, SE, WR
- **Content that matters:**
  - Three duchies: Valorsmark (Almud, also monarch; 6 provinces; Latinate), Hafenmark (Baralta; 4; Hanseatic), Varfell (Vaynard; 4; Old-Einhir/Norse) (:51-54).
  - Special entities: Himmelenger (Church city-state, sovereign), Askeheim (unincorporated Calamity wilderness, zero settlements), Schoenland (foreign Altonian island, one sea edge, exempt from >=2 rule) (:60-68).
  - Each province 2-3 settlements (7 at 3, 7 at 2 = 35); each settlement connected to >= 2 others (:76-82).
  - political_value = sum of territory_value (by type plus Prosperity/Defense/Order) + province_unification_bonus when one faction owns all territories; scalars TBD (:92-103).
  - Vetting block rates M-1..M-11 and a Q-robust paragraph (three approaches per province-control conflict) (:150-178).
- **Conflicts / stale:** States 56-edge settlement graph (:12, :178) vs 49 edges in settlement_adjacency (:44) and the sourcebook's "49 vs 55 vs 56" debt. Deprecates "T1..T17" naming yet every other document and the engine still uses T-ids. "Almund (Almud)" spelled two ways (:49).
- **Open items:** fracturing triggers and reunification thresholds, political-value scalars, ED-055 naval scope, Askeheim healing path (:141-144).

### .designs/systems/social_contest/reference/social_contest_currency_v1.md
- **What it is:** Currency-lineage note (2026-08-14, ED-IN-0189) carrying the retired `CURRENT.md` Social contest head-row narrative.
- **Status:** "REFERENCE — currency lineage only". Reading: historical, but a dense timeline of SC rulings.
- **Bears on:** SC, FA, CORE
- **Content that matters:**
  - Contest_rebuild staged (Gate 0 2026-06-30; ED-1055..1062 Stages 1a-3); kernel at `systems/social_contest/sim/contest/` (:33).
  - ED-SC-0002 RULED 2026-07-08: COMPOSED keying (Persuasion-Track band gates magnitude; genre selects stat/channel: Memory to L/Mandate, Projection to I) (:33).
  - P1 consequence spine EXECUTED with ECHO_TRANSPORT default ON: faction-scale auto-resolve via parliamentary_bridge and personal-scale Emergency Council via scene_dispatch; both can fire in one season (double-fire), calibration case under ED-SC-0013's Auto/Manual Resolution Duality (FORK-C tolerance needs_jordan) (:33).
  - Open: ED-SC-0015 (Total-Victory Mandate −1 stacking with Censure −1 = −2); P0 docket ED-SC-0003/0004/0005 (ED-SC-0004 blocks calibration) (:25, :33).
  - Three-lens audit (2026-08-06, ED-SC-0017..0022): three resolution models under one name; Stage 3 (CR4/armature/CR5) unreachable because `build_contest` has no armature param; BG "one-season" Mandate −1 is permanent; no record spine (Record primitive exists at settlements ledger.py) (:33).
- **Conflicts / stale:** Cites `engine/params/contest.md`, `params_tables.yaml` (retired), echo_transport (retired Key-era), `engine/cross_scale/*` (gone). Text is cut mid-sentence at line 33 (ends at "...KU-1 flags)").
- **Open items:** ED-SC-0015, ED-SC-0003..0005 were open at writing; later EDs ED-SC-0033..0039 (proceedings ownership) are referenced in the AUDIT_BRIEF as ruled [UNVERIFIED here].

### .designs/systems/social_contest/reference/social_contest_flow_skeleton_v1.md
- **What it is:** Traced flow skeleton of the old social-contest code (kernel `contest/`, parliamentary_vote, stay, scene_dispatch, parliamentary_bridge) at commit 6545067 with `path:line symbol` anchors; some rows corrected 2026-09-26.
- **Status:** "REFERENCE — traced structure only". Reading: historical for call sites (engine/cross_scale and mc_v18 are gone), but the kernel files it names still exist under systems/social_contest/sim/contest/ (verified by ls).
- **Bears on:** SC, FA, CORE
- **Content that matters:**
  - Kernel API: `build_contest` (adapter) -> `resolve_contest` (router, game "agon" only live) -> `Bout.resolve` exchange loop over `venue.budget`, moves pass/hard/support/shift/evidence/rebut/advance with reserve spending, faults, win-condition (:64-97).
  - Evidence is a hidden-value item presented by `evidence` move (no roll); `rebut` gated by `venue.allow_rebuttal` default False (:87-88) — directly relevant to the brief's evidence-as-typed-input question.
  - Gaps: armature (CR4/CR5) unreachable from `build_contest`; no durable record (only queued faction-stat deltas); `resistance` metadata-only and never supplied; `game` consensus/negotiation/inquiry STUBS unreachable; Emergency Council always closes by Panel vote, never Persuasion Track (:177-186).
  - Dead or orphaned: `parliamentary_stay.invoke_stay/resolve_stay_lift` zero callers; `contest/faction.py` zero production callers; `agon_harness.py` zero callers; `Standing.strip` never called (:181-183, :192).
  - Four coexisting resolvers: Bout, run_parliamentary_vote, legacy run_contest (retired 2026-09-26, ED-SC-0033), faction.coalition_vote (:191).
  - Church Tribunal/Excommunication exist twice (contest-kernel proceedings and independent FA modules) (:185); 9-node import cycle in the contest package, runtime-broken only by function-scoped imports (:190).
- **Conflicts / stale:** `contest_legacy_stub` deleted (the file notes it). `scene_dispatch`, `parliamentary_bridge`, `mc_v18` named here are not in the tree [UNVERIFIED but `engine/mc_v18.py` absent]. A `modules/social_contest` module now exists (ls modules) — the skeleton predates it.
- **Open items:** none stated; gaps are the open items.

### .designs/systems/social_contest/reference/social_contest_system_v2.md
- **What it is:** The v2 social contest spec (Opus 4.6 session 2026-04-04, PP-234 and later patches): format-follows-context, GM setup, Argue pool, Appraise/Choose/Argue exchange, CLASH/REINFORCE/CROSS/TIE, strain and Concentration, asymmetric proceedings, BG vote and hybrid modes.
- **Status:** "SUPERSEDED — canonical doc is designs/scene/social_contest_v30.md ... DO NOT CITE AS LIVE RULES" (banner :9-19). Reading: superseded; vocabulary and design intent only; §-anchors map 1:1 to v30 except §5 and §9.6.
- **Bears on:** SC, CHAR, FI, FA
- **Content that matters:**
  - Two genres (Memory = retention/actual, Projection = protention/potential) and two orientations (Revealing / Obscuring); style bonus +1D primary genre, +1D matching audience boost, max +2D (:34-38, :78-93).
  - Argue pool = (primary attribute × 2) + History bonus; primary attribute by adjudicator: Expert judge Cognition, Crowd Charisma, No adjudicator Attunement, Panel Cognition (provisional) (:56-61, :126-133).
  - Evidence: Recall bonus +2D "when citing a specific, named, verifiable claim (document, date, prior statement, named precedent)", binary, either genre (:168); Evidence Track Findings from fieldwork add +1D on Exchange 1, max +2D, not consumed, must be declared at setup (:313) — the only evidence-as-input rule in v2, a bonus die rather than a refutation.
  - Interaction types CLASH/REINFORCE/CROSS/TIE and Doubt Marker for Obscuring wins (:171-206); Persuasion Track 0-10, Side A wins >= 7, B <= 3, compromise 4-6, Total Victory >= 9 / <= 1 (:98, :248, :265).
  - Composure = Charisma + 6, Rattled marks at strain >= Composure, 2 marks = socially incapacitated; Concentration = Focus + Recall, Spent at 0 (:215-228); first-to-speak deliberately deterministic (higher Attunement acts last) (:234-241).
  - Asymmetric proceedings: Church Tribunal track starts biased at 6, disadvantaged party halved resistance (:271-281); BG Parliamentary Vote: pool = sum of Mandate per side, Total Victory = loser Mandate −1 one season (:342-358).
- **Conflicts / stale:** Composure retired as the contest tracker name (CR3/ED-1056: re-homed onto Face, per the v30 infill :39). "Presence/Memory" renamed. Panel adjudicator "not yet designed" here (ED-137) but implemented in the kernel (flow skeleton S1.4). Pre-Contest Preparation and Findings bonus not seen in the kernel's move list [UNVERIFIED].
- **Open items:** Escalation between social modes, negotiation ZOPA-style compromise, Appraise expansion, SIM-DEBT-03/04 (:404-416).

### .designs/systems/social_contest/reference/social_contest_system_v2_index.md
- **What it is:** Auto-generated index (2026-04-18) of the v2 spec; 7,112 tokens.
- **Status:** none (generated). Reading: stale/historical.
- **Bears on:** PROCESS, SC
- **Content that matters:** Heading map only; §4 Exchange Structure 1,632 tokens, §2 GM Setup 1,082 (:74-76). canonical_sha "unknown" (:11).
- **Conflicts / stale:** canonical path `designs/scene/` (dissolved).
- **Open items:** none.

### .designs/systems/social_contest/reference/social_contest_v30_index.md
- **What it is:** Auto-generated index (2026-07-02) of the live-at-the-time social_contest_v30.md body (22,256 tokens).
- **Status:** none (generated); the indexed doc is "CANONICAL — approved 2026-04-17". Reading: gives the only view in my set of v30's added sections.
- **Bears on:** SC, FA, CHAR, WR
- **Content that matters:**
  - v30 adds §6.1 Obligations (post-contest binding commitments, 2,564 tokens), §6.2 Conviction Scar Visibility, §6.3 Chain Contests (unresolved tension generates follow-up), §7.1 Excommunication Tribunal (ED-625), §7.2 Succession Contest (ED-665), §7.3 Heresy Investigation Lifecycle (ED-772), §9.4b Adjudicator Thread Response (ED-667), §10.1 Parliamentary Stay (ED-631) (:38-58).
  - §5 renamed "First to Speak"; §9.6 renamed "Chamber Violence (Forced Forfeit)" (ED-897) (:37, :52).
  - Largest sections: §4 Exchange Structure 5,362 tokens, §6 Post-Contest 3,911, §7 Asymmetric 3,303 (:84-90).
- **Conflicts / stale:** Duplicates the title "SOCIAL CONTEST SYSTEM v2" for a v30 file (:23).
- **Open items:** none.

### .designs/systems/social_contest/reference/social_contest_v30_infill.md
- **What it is:** Prose/rationale extracted from social_contest_v30.md (infill half of a skeleton/infill pair).
- **Status:** "CANONICAL — approved 2026-04-17" copied from skeleton header. Reading: fragment; one-document-in-parts with v30 body.
- **Bears on:** SC, CHAR
- **Content that matters:**
  - CR3/ED-1056: the Charisma×3 buffer is retained but re-homed onto the Face tracker; "Composure" as the contest-tracker name retired; Rattled at strain >= Face; Knot-as-Face-buffer (:39-41).
  - Jordan CONFIRMED scoped-rename-only (Composure to Face) at Gate A; knots_v30 §4.2 still says "Knot-as-Composure-buffer" (:41).
  - ED-897: canonical genre/orientation names Memory/Projection and Revealing/Obscuring; "Past/Future", "Direct/Indirect" are pre-PP-234 labels (:36).
  - §9.6 Chamber Violence = immediate forfeit, exception monster incursion/catastrophe (:55-57).
- **Conflicts / stale:** Uses "Past/Future" in rationale (:24-25) against the Memory/Projection canon (:36).
- **Open items:** none.

### .designs/systems/threadwork/reference/thread_horizontal_integration_spec.md
- **What it is:** ED-673..ED-681 (2026-04-17) cross-system Thread fire paths and editorial resolutions: Thread Domain Echo, Scene Slate Thread-State scenes, settlement Thread environment, CV drift, perception table, lifepath-to-TS derivation, Thread warfare NPC AI doctrine, Case Board dual-depth overlay, Rendering Crisis beats.
- **Status:** "ED-673 through ED-681 | Status: CANONICAL". Reading: intent/historical; its target sections were to be inserted into other docs by "propagation" (the propagation map lists target docs under dissolved `designs/`).
- **Bears on:** WR, FI, CHAR, FA, SE, GO
- **Content that matters:**
  - Thread Domain Echo: fires when RS change >= 1, or witnessed Conviction Scar, or Gap/Lock/Knot created/destroyed at Territorial+; effect ±1 to the most relevant faction stat (Dissolution −1 Stability, territorial Mending +1 Mandate, unauthorised Lock −1 Mandate); queued to next Accounting; cap 1 per scene per faction (:38-62).
  - Scene Slate Step 2b: RS <= 20 mandatory Thread Crisis scene; active Gap/Lock/threshold-crossing/WC advance add scenes; max 1 Thread-State scene per Slate (:74-86).
  - Settlement Thread effects are per-territory, not per-settlement (editorial resolution 6) (:27, :108); CV drift from public Thread operations capped ±2 per territory per season (:122-136).
  - Starting Truth/TS from lifepath table, base Truth 4, TS 0; Formation 2F gives Truth 2, TS +10 (:172-189).
  - Case Board Thread Layer: TS >= 30 toggle; linking rendered evidence to substrate evidence of the same event advances the Evidence Track +1 (max one insight bonus per investigation) (:225-239) — evidence-linking as typed object, relevant to FI/SC.
  - Thread warfare NPC doctrine as priority tree amendments: RS <= 25 forces defensive only; Niflhel Harvest gate 1 Dissolution/season at RS <= 30, suspended <= 20; Church has no amendment (:199-217). These are scripted per-faction NPC rules.
  - Rendering Crisis as four designed beats with Spirit checks (Withdrawal, Knot, Place, Choice), career rhythm framing (:249-261).
- **Conflicts / stale:** Resolution 3 "no battle-driven TS development" is design intent only. Depends on ms_budget.md and wc_survival_spine.md. "Composure 0 (Contest)" column (:150) uses the retired Composure name (now Face).
- **Open items:** none (document closes its own questions); propagation never traceable in the tree.

### .designs/systems/threadwork/reference/thread_horizontal_integration_spec_index.md
- **What it is:** Auto-generated index (2026-04-19) of the integration spec; 4,914 tokens.
- **Status:** none (generated). Reading: stale pointer (`designs/threadwork/`).
- **Bears on:** PROCESS
- **Content that matters:** heading map; largest section ED-681 (649 tokens) (:78).
- **Conflicts / stale:** line numbers shifted vs body.
- **Open items:** none.

### .designs/systems/threadwork/reference/threadwork_applications.md
- **What it is:** Part 1 of 2 of "Threadwork — Practical Applications by Subsystem" (2026-09-10, lane WR, ED-WR-0010): worked cases and doctrine for threadwork in combat, social contest, mass battle and fieldwork, carried across from a "Valoria Unreality Suite" of 2026-09-06.
- **Status:** "PROPOSED — REFERENCE ONLY. HELD BACK FROM RATIFICATION-ON-MERGE IN FULL." (:10). Reading: live as intent vocabulary only; explicit that deleting it changes nothing in the game; `needs_jordan` row for adoption and whether threadwork_v30 Part 3 is edited or superseded.
- **Bears on:** WR, PC, SC, MB, FI, CHAR
- **Content that matters:**
  - Four pricing rules: direction decides cost (restorative negative/free, manipulative 1-2 steps plus a step per season held, destructive 1-2 steps and damage not confined); reading is free and working is dear; detection ladder by reach 30/50/70/90 and "no reach returns content: operations are provable, contents are not"; practitioner degrades and cannot see it (present displacement vs resting point) (:50-127).
  - The one code note: `systems/threadwork/sim/coherence.py` still implements the superseded 10→0 clamped integer; needs two quantities, an environment condition on recovery, a direction gate and a resilience term (:123-127).
  - Combat: threadwork is a prepared action never a combat action (Leap window); difficulty ladder for fighting a drifting practitioner Dissonant/Fragmented/Fractured; directness beats the drift; a mob beats a threadcut being where a champion cannot; never Past-Pull a threadcut being (leaves a Gap) (:131-215).
  - Social contest: threadwork cannot persuade; pre-negotiation survey is the capability (shape of knots/pulls, never content); a court "cannot use one of you is lying as its default frame" and "needs a distinct category of proceeding for the operated-upon case"; sworn testimony from retained experience outweighs documentary records; practitioner testimony is structurally hedged, attacked through observers; usability-by-band table, "a drifting practitioner wins the room and loses the record" (:249-380).
  - Mass battle: the commander's instrument is prognosis not operation; terrain preparation decisive and invisible below reach 70; no command lattices, no held formations; theatre tension is a line item (sustained manipulative work raises substrate tension, incursions drop Accord, forcing mandatory governing actions); doctrine list of 8 (:385-532).
  - Fieldwork: thread forensics gives the shape of a crime, ordinary investigation its content; orphan signatures legible to non-sensitives; "honest irreconcilable witnesses are a lead"; test capacity not recall; interview log must record repetition counts (satiation manufactures a signature); an archive that works its own holdings destroys admissibility; incursion findings carry no motive (:541-667).
- **Conflicts / stale:** Disagrees with the Coherence code (explicit). Priced in "bands" because absolute Coherence figures were deliberately removed. wc/ms_budget-era Coherence "10→0" model vs rulings: flagged by the doc itself.
- **Open items:** adoption decision (needs_jordan); coherence.py rewrite listed as a code change, not design question; the doc's strongest SC/FI hooks (a distinct proceeding for the operated-upon; repetition-count logging) have no counterpart in code [UNVERIFIED].

### .designs/systems/threadwork/reference/threadwork_applications_part2.md
- **What it is:** Part 2 of 2 of Threadwork practical applications (2026-09-10, WR, ED-WR-0010): factions/politics, twelve economic sectors, institutions, the strategic loop, presentation/UI, safety requirements, a "what must never be built" list, and a carried/dropped ledger.
- **Status:** "PROPOSED — REFERENCE ONLY. HELD BACK FROM RATIFICATION-ON-MERGE IN FULL." Reading: intent vocabulary; self-declares bias risk and "medium" confidence on per-subsystem attributions (:545-550).
- **Bears on:** WR, FA, SE, CORE, GO, CHAR
- **Content that matters:**
  - Principal-agent: a noble formed in a Church polity cannot perform, verify or retain threadwork; "the retained practitioner is an agent the principal structurally cannot supervise" (:24-40).
  - Catalogue of faction/parliament/diplomacy applications with cost/detection/counter; structural traps: records problem, action-economy loop (tension to incursions to Accord drop to mandatory response), retinue problem; verdict "very good at taking a territory; structurally hostile to holding fifteen" (:44-131).
  - Sector viability test (restorative fraction, holding, externality, knotting); healthcare highest value, construction/water/education fail; triage inversion; calendar and tenure externalities; materials pre-assembly rule (:139-285). Safety trap: a society that succeeds at civil defence reduces its practitioner supply (:276-284).
  - Eight institutions (Tendency Survey, Tension Register, Knot Registry with sparsity cap, Working-Site Model, Assay, Attestation Cadence, Apprenticeship Orders, Exposure Rota); oversight has a structural ceiling (:288-307).
  - Strategic layer: "the single highest-value piece of unbuilt threadwork" is `rendering.py`'s `apply_rs_strain`/`check_calamity_threshold`, said to be "a wired stub" while Turmoil and MS clocks are "live" (:345-349); strain should accrue from a HELD manipulative shape, and MS settlement consequences should be keyed to direction not verb (:351-358).
  - Incursion response by mode (ordinary: cordon and wait; transient: record it, no stat block; threadcut: separate institution); Locked Zones cordon and survey, a competent commander uses one as an anchored flank (:362-380).
  - Presentation rules: one perception path (external term + internal term + noise + criterion = force); insight never helps (no dispel/truesight); drift as observer-computed channel inconsistency; no Coherence number ever shown; two histories never reconciled; four endgames by reach at crossing (:386-473); safety requirements (photosensitivity, depersonalization, dehumanization) (:477-487); "must never be built" list (:493-512).
- **Conflicts / stale:** Says "Turmoil ... live and already ticking" (:347) — Turmoil/Strain has no carrier in engine/modules .py (grep), and `systems/overview/sim/ms_track.py` [UNVERIFIED present]. `rendering.py` greps found no `NotImplementedError` or those two function names at the path searched, so the "wired stub" claim is [UNVERIFIED] / possibly stale. Contradicts the older WC spine's "Wardens/WC 3 is the singular endgame path" by dropping WC entirely from the analysis.
- **Open items:** the same needs_jordan adoption call as Part 1; art/accessibility constraints are requirements the GO lane has no row for [UNVERIFIED].

### .designs/systems/threadwork/reference/threadwork_flow_skeleton_v1.md
- **What it is:** Traced flow skeleton of the old threadwork sim (operations, coherence, collective, opposing, co_movement, rendering, threadcut) at commit 6545067 with `path:line symbol` anchors.
- **Status:** "REFERENCE — traced structure only". Reading: historical (call sites in `engine/cross_scale/*`, `engine/mc_v18.py`, `engine/autoload/*` are gone: `ls engine/cross_scale` fails); the module list under `systems/threadwork/sim/` still exists (operations.py, coherence.py, collective.py, opposing.py, co_movement.py, rendering.py, threadcut.py).
- **Bears on:** WR, FI, CORE, MB
- **Content that matters:**
  - Operations: attempt_leap/weaving/pulling/past_pulling/locking/dissolution/mending share `_resolve_operation` (pool from spirit/ts/history; Ob from DEPTH_OB only); Mending costs 0 Coherence (ED-871 exemption) (:64-78).
  - Collective op: Anchor = highest TS; helpers add floor(Cognition/2); lattice fracture +1 Ob (:80-84). Opposing: 3x3 Meets/Partial/Failure table, Ob modifier from opponent TPS (:86-90). Co-Movement 15-card deck drawn once per op (:92-94). Threadcut interaction (:96-99).
  - Gaps: no Key emitted; no production caller reaches any `attempt_*` (only tests); campaign loop and scene_dispatch never reach Thread scale; Rendering Part 5 fully stub-wired; mass-battle `threadwork_check` is a `pass` no-op; defect C-TW-3 (blanket Partial/Failure −1 Coherence mis-hits Leap); Thread Fatigue declared in contract but unimplemented; Three-Axis Ob (Breadth, Distance tables) dead; `attempt_leap` docstring claims a `ts_minimum` read the body never performs (:158-168).
  - The one cross-subsystem live call: fieldwork knots.py calls `apply_coherence_delta` on Knot rupture (:34, :147).
- **Conflicts / stale:** `systems/threadwork/sim/rendering.py` docstring now says it "held two stubwire.stub_resolve armature stubs" (past tense, so they were since changed) — the skeleton's S8 and threadwork_applications_part2's "wired stub" claim are stale against the file header [verified lines 4]. Many world fields cited (`practitioners`, `threadcut_beings`, `comovement_deck`) lived in the retired game_state.py.
- **Open items:** none stated; gaps listed above.

### .designs/systems/threadwork/reference/threadwork_philosophical_reference_v30.md
- **What it is:** Empty skeleton of the philosophical framing (headings only) extracted from threadwork_redesign_v25 Part 1; used by the canon-guard for P-01..P-15.
- **Status:** "REFERENCE — not a design doc". Reading: reference; this half is headings only (prose is in the infill).
- **Bears on:** WR, PROCESS
- **Content that matters:**
  - Seven headings: What Threads Are; Ein Sof and Spooling; What Thread Sensitivity Does; The Scale Principle; The Two States: Perception and Contact; Why Thread Operations Produce Unpredicted Consequences; Why This Matters for Play (:24-57).
- **Conflicts / stale:** none.
- **Open items:** none.

### .designs/systems/threadwork/reference/threadwork_philosophical_reference_v30_infill.md
- **What it is:** The prose of the philosophical reference: threads as co-movement of three axes (actuality, intelligibility, temporality), Ein Sof and spooling, scale principle, perception vs contact (the Leap).
- **Status:** "REFERENCE — not a design doc". Reading: reference/vocabulary.
- **Bears on:** WR, FI, CHAR
- **Content that matters:**
  - Thread = co-movement of three axes; touching one touches all three, hence co-movement consequences (d6 random) are "things that simply happened" (:20, :42-43).
  - Scale Principle: intelligible-to-unintelligible ratio varies by scale; Structural operations produce severe co-movement and escalating Ob; "the game rewards restraint and punishes ambition" is the stated foundational design principle (:30-35).
  - Perception (TS-based, rendering) vs Contact (Leap suspends rendering); no bridge between them (:37-40).
  - GM narrates operations in two phases; after the Leap, outcome described from outside (:45) — assumes a GM, which the engine replaces (CLAUDE.md "no GM").
- **Conflicts / stale:** the GM-narration instruction (:45) predates "there is no GM". Moves from the older "Past/Future" vocabulary elsewhere.
- **Open items:** none.

### .designs/systems/threadwork/reference/threadwork_v25_historical.md
- **What it is:** Pre-atomization snapshot (2026-04-13; text dated v2.6/v3.1, 2026-03-27 revised 04-02) of the whole Threadwork mechanics document: operations, Coherence 10→0, co-movement, Rendering Stability world track, threadcut beings, Knot mechanics, cross-mode.
- **Status:** "HISTORICAL — pre-atomization snapshot"; self-header "design proposal, requires editorial approval" with a CANONICAL POOL NOTICE. Reading: historical; overlapped by threadwork_v30; used for rationale and numbers only.
- **Bears on:** WR, FI, PC, MB, CHAR, FA
- **Content that matters:**
  - Operation pool: (Spirit × 2) + relevant History bonus + Thread Pool Score (TPS = TS ÷ 10), TN 7 (TN 8 for Past-Oriented Pulling, Locking, Dissolution); Leap Ob 2 at TS 30-49, 1 at TS 50+, +1 per Wound; Leap is a Priority 5 full-round action; contact lasts Focus rounds (Focus 1 = no operations) (:113-182).
  - Operation-by-operation degree tables: Weaving (over-actualisation at Relational+), Pulling (duration by surplus), Past-Oriented Pulling (TS 70+, RS ≤ 60, Ob by recency 3-7), Locking (chronic RS drift; Permanent Lock forms Locked Zones), Dissolution (RS −3 to −8, Failure = Gap + Monstrous Incursion), Mending (Ob by Gap severity, ceiling 8; 0.. −1 Coherence in v25) (:220-486).
  - Collective ops: Anchor highest TS, helpers add floor(Cognition ÷ 2), lattice fracture +1 Ob (:488-508); Opposing ops 3x3 table with opponent-TPS Ob modifier (:514-568).
  - Coherence 10→0 track: scale-based loss (Object/Personal 0, Relational/Territorial −1, Structural −2, FR +1), per-operation cap −1, thresholds Stable 10-8 / Dissonant 7-5 / Fragmented 4-3 / Fractured 2 / Severed 1 / Rendering Crisis 0; recovery only by non-practice (+1/season) or Knot anchoring (:571-651). THIS is the quantity the 2026-09 applications document says was superseded.
  - Rendering Stability world track 100→0, default start 60, bands Stable/Strained/Fragile/Fractured/Critical/Rupture, seasonal change cap ±10; "RS Critical is the point of no return... designed. The Einhir reached the same point" (:733-776).
  - Knot mechanics: pool (Bonds × 2) + 3 points, tiers Close 5 / Medium 2 / Loose 1, max Knots floor(Bonds/2)+1; Rupture Disposition → −4; Loss = Coherence −1 (:850-904).
  - Mode branching table TTRPG/BG/Hybrid; Hybrid Coherence declaration rule: the PC who declares leadership at Phase 1 of Cascade pays (:964-973, :955).
- **Conflicts / stale:** Coherence 10→0 versus applications doc's two-quantity model (explicit disagreement); RS/MS no carrier in the season architecture (rendering.py header: no rendering or mending clock among the three licensed clocks). Hybrid/Board-game modes excluded (videogame-only). Many [PROVISIONAL] PP patches inline.
- **Open items:** ST-TW-01 (Coherent Strike free at Object scale), several simulation tasks listed in the implementation sequence (:1005-1018) with no results here.
