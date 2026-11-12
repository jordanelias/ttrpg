# Digest designs1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: archived design documents under `.designs/` (README, `_architecture`, articulation, characters, combat, factions, fieldwork, mass_battle, npcs, overview; 103 files). All are ARCHIVED-NOT-CANON; read for intent, vocabulary and referents only. Line refs are to the file named in the entry.

### .designs/README.md
- **What it is:** quarantine README for the `.designs/` tree (archived 2026-09-16 per its body).
- **Status:** "Nothing in this tree is canon, and nothing in it resolves at runtime." Reading: live as a rule about the tree; the tree itself is historical.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Frozen, do-not-edit, do-not-add, nothing-points-here rules (:15-23); layout drops the `reference/` segment (:27-33).
  - Count stated as 230 documents; `engine/season/**` deliberately not archived (:37).
  - Reason for the move: prose kept being swept up as authority (:6-9).
- **Conflicts / stale:** the "Nothing points here" claim is contradicted by the audit-suite brief, which now directs lanes to read it; not a defect of the file.
- **Open items:** none.

### .designs/systems/_architecture/reference/_architecture_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (IN/flow/OUT/state/seams/gaps) of the Key-substrate + cross-scale echo transport, traced at commit `6545067`.
- **Status:** "REFERENCE — traced structure only". Reading: historical; its subject (the Key substrate, `keys.py`, echo transport) is RETIRED (ED-IN-0232).
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Documents the retired emit->validate->append->observer path `TickScheduler.emit` and `accounting_boundary` deferral of Faction/Settlement writes (:91-99, :136).
  - Traced gaps: `compute_thread_echo`, `render_protagonist_lens`, `generate_chronicle_entry` had zero callers; `apply_handoff` live for 1 of 8 scale pairs; Accord-Echo branch organically dormant (:195-204).
  - `combat_bridge` was unreachable because `evaluate_triggers` only ever queued `scene_type: "contest"` (:197) and `DISPATCH_COMBAT_BRIDGE` defaulted off (:79).
  - `engine/autoload/npc_ai.py` entry points were stub no-ops and the engine core's sole orphan; live dispatch called `faction_take_action` directly (:209).
  - `engine_clock` contract has `sim_module: none`; `mechanical.season_change` emit was dangling (:205, :210).
  - Seams already moved to ROLE resolution via `references/module_contracts.yaml` (parliamentary_vote, territory_transfer_proposal) (:182-183).
- **Conflicts / stale:** entire Key/echo apparatus retired; anchors (`engine/substrate/keys.py`, `engine/cross_scale/echo_transport.py`, `engine/mc_v18.py`) [UNVERIFIED whether any still exist]. Useful only as a record of which pre-retirement hooks were dead.
- **Open items:** the dormant-hook list (articulation lens, chronicle entry, thread echo) is a referent for what the season loop later had to re-supply (chronicle/articulation) [UNVERIFIED].

### .designs/systems/_architecture/reference/campaign_architecture_v30_index.md
- **What it is:** auto-generated heading/size index (2026-04-19) of `campaign_architecture_v30.md` (dated 2026-04-17).
- **Status:** the indexed doc says "CANONICAL — approved by Jordan 2026-04-17" (:25). Reading: historical index; the full body is not in this file.
- **Bears on:** WR, SE, FA, CHAR.
- **Content that matters:**
  - Scope line lists the content: Church settlement infrastructure (four independent axes), CI=100 mass seizure, RM identity, Thread revelation curve, phased IP escalation, Altonia repulsion, MS loss reform, Coherence asymmetry, Mending community, Portrait Retirement, Lineage, Warden paths (:26).
  - Supersedes the x3 mass-battle MS multiplier and flat Coherence cost tables (:27, §3.1 struck).
  - Section map: Part 6 Warden faction paths (five paths), Part 7 Portrait Retirement and Lineage Acts (3 types), §7.3 Conviction Resolution States (:54-57).
  - Contract `campaign_architecture` was `status: stub` with this doc as its home (see skeleton).
- **Conflicts / stale:** an index only; content must be read from the (missing here) body. Part 8 "PROPAGATION REQUIRED" signals unpropagated edits (:59).
- **Open items:** whether Lineage Acts / Portrait Retirement exist in any engine code [UNVERIFIED].

### .designs/systems/_architecture/reference/canonical_registry.md
- **What it is:** "Canonical Registry (Definitive, Revision 2)", 2026-04-15: the cross-scale table of clocks, territory values, faction stats, attributes, derived values, initiative.
- **Status:** "PARTIALLY SUPERSEDED (combat rows) — banner added 2026-07-01 (ED-1084)". Reading: historical; many rows pre-date d+sigma.
- **Bears on:** CORE, CHAR, SE, FA, WR, DICE, PC, SC, MB, FI.
- **Content that matters:**
  - Global clocks: Metaphysical Stability 0-100 start 72, Church Influence start 28 with milestones 40/55/65/80/100, Invasion Pressure start 20, Political Stability 0-10 (:29-34); MS bands :42; Political Stability bands :60.
  - Territory values 0-4 balanced at 2 (Accord, Piety, Prosperity, Fort), Accord effect table :85-91; Church Seizure Ob = 6 - Piety :99; Prosperity -> Muster Size :79.
  - Faction stats 1-7 (Mandate 0-7, Stability 0-7), seasonal cap +/-2 (:121); card hands per faction :127-132; Intel STRUCK (:123).
  - Ten attributes, creation 31 points (:148-150); universal pool `(Attr x 2)+History+3`, min 5D, TN 7 (:158); Ob = floor(Attr/2)+1 (:164); derived-value table :168-181 (combat pool row marked superseded by `max(5, History+6)` at :15-19).
  - Disposition -5..+5, stepped Ob table, Bonds decoupled (ED-912) (:187-195); universal initiative (:201-209).
  - Cross-system parallel table (:270-277) and simulation calibration data (campaign: Church 53%, 13.3 years avg, Hafenmark collapse 27.8%; :283-294).
- **Conflicts / stale:** Combat pool and "Pool" rows superseded per its own banner (:15-19); the whole `(Attr x 2) + History + 3` pool is pre-d+sigma [UNVERIFIED against current dice owner]; Godot status "Phases 1-12 fully implemented" (:312) is stale. Battle-consequences table (:235-242) is a fact the code should own.
- **Open items:** open decisions J-1 (mass-combat pool), J-3..J-9 (:320-329); unvalidated compounding of Accord + Political Stability + battle consequences (:302).

### .designs/systems/_architecture/reference/conflict_architecture_proposal.md
- **What it is:** design proposal 2026-04-19 on how the game ignites conflict: three-scale hierarchy, bishop appointment, graduated Löwenritter autonomy, royal assassination fuse, Niflhel dissolution, rescoped Tensions Deck.
- **Status:** "CANONICAL" / "CANON — approved by Jordan" (:10-13); supersedes `early_game_ignition_analysis.md`. Reading: historical intent; the file labels itself canon but nothing in a `.md` is a mechanism (§0.05), and "engine_v4 Phase" numbering is pre-season-loop.
- **Bears on:** FA, SE, WR, CHAR, FI.
- **Content that matters:**
  - Three scales Peninsula (consequence) / Province (contest) / Settlement (engine); resolution order each season Settlement -> Province -> Peninsula (:28-34).
  - Five starting friction provinces: T1 Crown vs Church (S003 Cathedral), T8 Hafenmark vs Guilds (S017), T14 Crown vs Löwenritter (S014 Barracks), T4 and T13 Varfell vs RM; fragmentation check each Accounting e.g. Influence 5 vs Ob 3 (:38-52).
  - Bishop appointment Domain Action: Ob 1, needs Church building tier >=2 and (no governor or governor Disposition toward Church >= +2); generates no Casus Belli (:56-72).
  - Graduated Löwenritter autonomy replaces the binary Coup Counter: Loyal / Restless / Autonomous / Split with triggers on Crown Stability <=3 / <=2, Ehrenwall Disposition, 4+ seasons; reversible stages 1-3; Split spawns a faction M3/I2/W3/Mil6/Stab5 (:76-89).
  - Assassination fuse fires S8-S12, three targets (Lenneth/Torben/Almud) each opening a different mid-game (:93-107). Niflhel struck as a faction; black markets (Order<=1 or no governor: Wealth +0.5, Accord -0.5), intelligence-broker NPCs, Thread exploitation sites at Proximity <=2 (:111-123).
  - Tensions Deck cut to 6 cards, draw 1 (:127-144).
- **Conflicts / stale:** relies on a Coup Counter, "Niflhel", PV and Parliament RS/CI/IP/PI clocks; whether engine/season carries any of these [UNVERIFIED]. The Niflhel faction is dissolved here, but `early_game_ignition_analysis.md` still reasons with it.
- **Open items:** Tensions Deck "remainder" cards 2-6 "written during smoke testing, low priority" (:184); intelligence-broker NPC placement Phase 4 (:182).

### .designs/systems/_architecture/reference/decision_policy_v1.md
- **What it is:** draft precedence policy for what authority wins when design sources disagree, 2026-07-31 (ED-IN-0113 §A, lane IN).
- **Status:** "DRAFT FOR RULING — does NOT ratify on merge". Reading: unclear/superseded in practice (CLAUDE.md §0 `needs_jordan` five-step answer order and §0.05 supersede its function); §3 crux never ruled in this file.
- **Bears on:** PROCESS, DICE, PC.
- **Content that matters:**
  - Evidence base: 134 Jordan-attributed rulings; mechanical canon lost to measured physically-grounded engine behaviour in four cases ED-899, ED-900, ED-901, ED-PC-0005 (:42-64).
  - Proposed precedence: metaphysical canon NO DEFAULT; physics/history and measured engine behaviour outrank mechanical canon; lore/flavour untouched (:70-80).
  - Option (c) "split": A1-A15 constraints supreme, mechanical instantiations subordinate (:111-114).
  - Operational tests: emergence = the "U9 capstone ablation gate" (K=0 degrades continuously); canon needs verbatim quote with locator; history needs cited source with locator (:122-127).
  - Names A5 (Ein Sof) as "the Key substrate" instantiation (:99), a retired mechanism.
- **Conflicts / stale:** Key substrate retired (ED-IN-0232); the precedence function now lives in CLAUDE.md §0.05 (code decides). Counts (213 open items, 94 awaiting Jordan) are July snapshots.
- **Open items:** §3 metaphysical-canon tier ruling never given here; 9 override candidates "not read" (:173).

### .designs/systems/_architecture/reference/derived_stats_v30_index.md
- **What it is:** auto-generated heading/token index (2026-04-19) of `derived_stats_v30.md` (dated 2026-04-18).
- **Status:** indexed doc "PROPOSAL — supersedes prior derived_stats_v30.md" (:25). Reading: historical; body not present here.
- **Bears on:** CORE, CHAR, PC, SC, MB, SE, FA, WR.
- **Content that matters:**
  - Section map reveals scope: Vitality/Stamina (§4), Composure/Concentration (§5), Thread Fatigue (§6.1), TroopCount (§7), Faction Income and Drain (§8.1), "Stat Damage Only From Structural Failure" (§8.2), Settlement scale PENDING (§9) (:28-43).
  - §10 Cross-scale bridges: Disposition cap by Bonds (10.1; later reversed by ED-912), Army Morale as derived composite (10.2), Renown bridge (10.3), Settlement combat defense feedback (10.4) (:44-47).
  - §11 Stat Modification Conversion Registry (PP-680): which routine fluctuations become derived values vs direct stat edits (:49-51).
  - Principle: "Stats are what you CAN do; derived values are what you HAVE right now" (:27).
- **Conflicts / stale:** its Bonds-caps-Disposition bridge was superseded by ED-912 (per canonical_registry :195); its §4.1 "no Ob penalty from wounds" was overridden by ED-PC-0005 (per decision_policy :60).
- **Open items:** Settlement scale marked PENDING at §9.

### .designs/systems/_architecture/reference/early_game_ignition_analysis.md
- **What it is:** analysis 2026-04-19 of why the early game has no fire starters; six historical ignition mechanisms; proposed 8-card Tensions Deck (draw 2), Niflhel Provocation, Löwenritter Martial Honor Pressure.
- **Status:** "SUPERSEDED 2026-04-19" by `conflict_architecture_proposal.md` (:9-15); "Historical precedent research (§2) remains valid". Reading: superseded; keep §2 as precedent catalogue.
- **Bears on:** FA, WR, FI, CHAR.
- **Content that matters:**
  - Diagnosis: every mechanic is a pressure accumulator, not a trigger; passive-build equilibrium is rational for all four factions (:28-32).
  - Six mechanisms with sources: structural provocation (Free Companies, Praetorians, Council of Ten), manufactured incident (Ems Dispatch, Tonkin, Prague), succession, economic shock, ideological flashpoint, calendar deadline (:36-98).
  - Original 8-card deck T1-T8 with concrete stat effects (e.g. T4 Border Incident: Coup Counter +1 and Varfell Accord -1 if no action in 3 seasons) (:134-141); C(8,2)=28 combos (:213).
  - Fabricated Intelligence: Dossier with one attribute +/-2, buyer unaware (:158-166). Löwenritter Pressure: inspection deployment after 4 quiet seasons when Coup Counter <3 (:176-183).
  - "Complexity budget" argument against a new faction, with tracked-value list (:207).
  - Fixed calendar events S4/S8/S12 proposed (:295) and later cut by the successor doc.
- **Conflicts / stale:** Niflhel, Coup Counter, Turmoil, Torben Loyalty tracks all superseded or struck in the successor and registry. Draw-2 vs draw-1 and 8 vs 6 cards conflict with the successor.
- **Open items:** Cardinal unilateral action at Church Stability <=3 (:289) not carried into successor.

### .designs/systems/_architecture/reference/generational_transition_v30.md
- **What it is:** Phase 2.11 spec (2026-04-18) of what persists, transforms, resets, breaks, transfers at PC death or Portrait Retirement.
- **Status:** none stated ("Location: Canonical in player_agency_v30 (proposed §11)"). Reading: historical design; unclear if engine/season implements generations [UNVERIFIED].
- **Bears on:** CHAR, WR, CORE.
- **Content that matters:**
  - Trigger: PC death or Portrait Retirement (>=2 Convictions resolved); one Conviction transforms and transfers (T8 Conviction Legacy) (:13-15).
  - PRESERVE list: faction stats, clocks, settlement states, NPC-to-NPC states, territory control, card hands (:18-29). RESET: Disposition toward PC to faction default, Standing 0, Coherence 10, wounds, Exposure, skills, attributes (:35-47).
  - Resources inheritance `floor(predecessor/2) + new starting` (:58); Renown reset but predecessor Renown >=7 gives +1 (:55).
  - BREAK: all Knots rupture; companions depart (:49-51). TRANSFER: active Obligations pass to new character's faction (:53-54).
- **Conflicts / stale:** Knot/Key/Exposure vocabulary partly retired; [UNVERIFIED] vs current character-state code.
- **Open items:** none stated (one "Open Question Resolved").

### .designs/systems/_architecture/reference/governance_consolidation_v1.md
- **What it is:** consolidated head (2026-07-12, lane IN, Opus 4.8) reconciling the governance proposal arc (44 proposals, 12 authored, 58-card deck, stress test) against built `sim/territory/` code; decisions D1-D6.
- **Status:** "D1-D6 RATIFIED (D1-D5 2026-07-13 ED-IN-0046; D6 ED-IN-0047)". Reading: historical decisions; the `sim/territory` code it names has been dissolved (CLAUDE.md §3 "sim/" dissolved).
- **Bears on:** SE, FA, CHAR, WR.
- **Content that matters:**
  - D1 card-deck is canonical for play, predicate-sweep is the batch oracle (:41-42). D2 AP economy canonical: `AP = 2 + facility_tier (+1 Seat/Cathedral)` (:44-45).
  - D3 Compact modelled as recurring fixed-term `Debt` (`ttl`, `recurs=True`), not a 6th ledger family; built `TAG_KINDS = {Precedent, Grudge, Debt, Reputation, Leverage}` (:47-48).
  - D4 retire `Mandate = round(7T/(T+6))` as collapse carrier; carriers are floor-average Order + province fracturing + Standing/resolution_quality Keys; rename the faction Mandate meter to end a two-Mandates collision (:50-51).
  - D5/D6: Performance Audit merges into the suspicion/recall spine (G606 "Bailiff's Report", `Submit to audit` -2); cumulative suspicion accrual allowed only with E11, a symmetric suspicion-reduction counter (:53-54, :113-127).
  - Finding: settlement `legitimacy`/`popular_support` declared but inert in `sim/`, a port-blocking gap (E5) (:51, :103-105); both harnesses show a negative death-spiral bias, "Flourishing 3.7 vs 659/seed" (:110-112).
  - Starting faction count RULED 4 with intentional emergent-faction mechanic (:206-212).
- **Conflicts / stale:** Key-based Standing routing retired; "Phase P (E1 alone) should not be greenlit" (:199-204) defers to `ners_vsg_reconciliation_v1.md`. Two "6." items numbered in §6 (:187, :194).
- **Open items:** B2 (S-006 identity) and B12 (Territory = Settlement vs three-tier hierarchy conflict) unresolved (:214-219).

### .designs/systems/_architecture/reference/governance_ripple_substrate_v1.md
- **What it is:** integration spec (2026-07-11, lane IN) of a "causal spine": event -> settlement lever -> response burden -> Key -> Standing -> ripples to FI/SC/FA -> arcs.
- **Status:** "PROPOSED (2026-07-11) ... not yet Jordan-ratified" (:13); consolidation doc lists it "RATIFY (+ verify one scoring edge)". Reading: historical; built on the retired Key substrate.
- **Bears on:** SE, FA, SC, FI, WR, CORE.
- **Content that matters:**
  - Five primitives only: Key emission, Ledger tag, Disposition, Π (settlement pressure homeostat), Standing/consolidation_progress (:389-397); the test "a specific field one writes that the other reads" (:399-406).
  - Five minimal new settlement levers: StockLevel, Assessment tag, Capital-Posture, Consent-Rule, route/corridor Precedent (:101-107).
  - Three pressure vectors upward/downward/positional (power_base) kept distinct (:122-141).
  - `resolution_quality = w_d*(delivered-demanded Directive) + w_n*(delivered-demanded Need)` computed on an emitted Key (:191-198); worked famine example (:221-271).
  - Self-audit grades: §6.2 event->Parliament edge AT-RISK because contest resolver has no input reading an external Key; §5 standing and §8 arc feedback HOOK-NEEDED (:466-498).
  - Event-deck draw is a "NEW ENGINE"; P-iii finding: discrete Π band cliff 7->8 Intrigue->Crisis (:537). Four Jordan rulings R-1..R-4 (:427-441).
- **Conflicts / stale:** every "Key emission" step is retired apparatus (ED-IN-0232); the Π-weighted deck, Standing ladder, `da_outcome.*` Keys must be re-read against current engine/season [UNVERIFIED].
- **Open items:** R-1 (levers in scope?), R-2 (NPC contest player seat), R-3 (author Territory connective-tissue scale), R-4 (Π cliff intended or softened).

### .designs/systems/_architecture/reference/governance_type_registry_v1.md
- **What it is:** registry/index (2026-07-13, lane IN) classifying every governance/politics/faction/clock type across the scale hierarchy as FLAG, VECTOR, or VECTOR-with-derived-FLAG; sketches a `Field` primitive.
- **Status:** "PROPOSED / REFERENCE ... Jordan-vetoable ... §4's architecture proposal is genuinely new and unratified". Reading: historical; §4 depends on the retired Key/Echo substrate.
- **Bears on:** SE, FA, CORE, WR.
- **Content that matters:**
  - Dominant real pattern is VECTOR-with-derived-FLAGS (MS, CI, IP, Turmoil, Π, Accord); a Key is one-shot and "structurally the wrong shape" for a continuous meter (:51-58, :242-250).
  - Decay status table: MS and Turmoil/Strain have specified decay; Π a homeostat `clamp(Π + pressures - releases, 0, 10)`; CI, IP, Church Attention Pool, Order have no natural decay (:151-160, :112).
  - Same-name collisions: Prosperity (settlement 0-5 vs legacy territory 1-7), Disposition (personal vs settlement local actor), Guild Favour, Standing, Mandate (:168-174).
  - Legitimacy/Popular Support "Confirmed inert in `sim/` — 100/100 `lps_inert_check`" (:106); Mandate `round(7T/(T+K))` retired as collapse carrier (:107).
  - Three costumes of one consent gate (populace acceptance, Mandate aggregation, `compliance(L)` tax yield) flagged as one MERGE/DISTILL candidate (:196-203); `power_base` as organising field of the Ascendancy layer (:94, :209-214).
  - Proposed `Field` schema (range, aggregate_fn, propagate_fn, decay_fn, derived_flags) (:261-279).
- **Conflicts / stale:** Key/Echo armature retired (ED-IN-0232); the Prosperity, Disposition, Mandate name collisions may still exist in code [UNVERIFIED]. The L/PS-inert claim is a July snapshot [UNVERIFIED].
- **Open items:** OF-3 `decay()` fork; collisions §2.8 "found, not yet resolved"; `Field` vs `Gauge` naming (:306).

### .designs/systems/_architecture/reference/holonic_container_doctrine_v1.md
- **What it is:** architectural doctrine (ratified 2026-07-02, ED-1083/ED-1094) cross-mapping the workflow spec's holonic container/wrapper concepts to existing Valoria artifacts; names two failure modes.
- **Status:** "CANONICAL — ratified 2026-07-02"; body also says "this doc itself is PROPOSED" (:102), an internal contradiction. Reading: its two guardrails live on in CLAUDE.md §10; the cross-map targets (Key substrate, `sim/` ladder) are retired/dissolved.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Doctrine: one uniform shape at every scale, structure top-imposed and behaviour bottom-up; contract constrains shape never behaviour (:26-34).
  - Failure modes scripting drift and shape divergence, binding on all infill (:56-77), now restated in CLAUDE.md §10.
  - Cross-map row: module_contracts "27 modules, 10/27 `doc: null`, 11/27 `[ASSUMPTION]` resolvers" (:46); holonic ladder `personal -> thread -> provincial -> territory -> peninsular -> world` (:47).
  - Propagation spec (up/down transforms, termination) called "the highest-value unauthored canon in the repo" and deferred (:49, :93-100).
  - Container hygiene: no `sys.path` reach-ins, tunables in declared config, shared services in `autoload/` (:79-91).
- **Conflicts / stale:** `sim/`, `autoload/`, `articulation.py` stubs, Key substrate are gone; module counts stale. Status line says CANONICAL yet text says PROPOSED.
- **Open items:** downward Key delivery (register #1, ED-1006), `engine_clock` authorship (ED-1051) at time of writing.

### .designs/systems/_architecture/reference/hybrid_gaps_v30.md
- **What it is:** skeleton (atomized 2026-04-13) of 17 resolved hybrid TTRPG+board-game session-structure gaps (session 2026-03-26), prose in the `_infill` sibling.
- **Status:** "All 17 open hybrid design gaps resolved." Reading: historical; assumes a human Game Master, contradicting the no-GM rule.
- **Bears on:** CORE, GO, PROCESS.
- **Content that matters:**
  - Session phases Personal -> Strategic -> Cascade; one session minimum per season (:22-28).
  - Fog of war: faction stats shown to non-owners as four bands In ruins=1, Poor 2-3, Good 4-5, Excellent 6-7; Intelligence always hidden (:35-42; infill :20-22).
  - 12 cross-system handoff types resolve by batching to Cascade; mandatory-scene triggers (:47-75).
  - Resource/Wealth stress: faction Wealth stressed if Wealth < 2 x Resources rolled; testing variant 2x-1 (:90-99).
  - Player-Character death puts faction in Crisis (-1 all stats one season) (:119).
- **Conflicts / stale:** "Game Master" throughout vs CLAUDE.md "There is no GM — the engine resolves everything"; "Intelligence" stat struck per canonical_registry :123. The skeleton drops sub-steps (G-094 step 1, G-085 triggers, G-092, G-088-090 bodies) which only the infill carries.
- **Open items:** the 2x vs 2x-1 threshold flagged for "Phase 3 stress testing" (:97).

### .designs/systems/_architecture/reference/hybrid_gaps_v30_infill.md
- **What it is:** prose infill for `hybrid_gaps_v30.md` (companion; one document in parts).
- **Status:** none stated. Reading: historical; same GM assumption.
- **Bears on:** CORE, GO, FA.
- **Content that matters:**
  - Boundary ambiguity: a stat of exactly 4 displays Poor or Good on a 1d6 roll (1-3/4-6), fixed per scene (:20).
  - NPC-only orders resolve first in Strategic phase and are narrated; no scene unless a PC is present (:26-27).
  - Siege Zoom-In triggers only on player-seeks-contact or NPC unit attacking a PC's unit (:32-34).
  - Cascade is "not skippable" and GM-controlled; step list incl. Domain Echoes first, board update last (:40-44).
  - Expedition PC: another PC proxies, else faction runs on NPC AI with one Belief-level directive/season (:46-48); PC death succession options 1-3, default 3 (:50-54).
  - Knot/Inspiration consequences from board events gated by in-scene discovery (:61-64).
- **Conflicts / stale:** as above (GM). Faction "Intelligence" stat struck.
- **Open items:** none.

### .designs/systems/_architecture/reference/integration_proposal_v30_index.md
- **What it is:** generated heading/size index (2026-04-18) of "Holistic Critique & Integration Architecture" (2026-04-15, ~15k tokens; body absent).
- **Status:** none stated. Reading: historical; body not readable here.
- **Bears on:** CORE, GO, SC, FI, FA, WR.
- **Content that matters:**
  - Names three integration mechanisms: Domain Echo, Scene Slate, Dialogue Lattice (:33-35).
  - Parts: Progressive Revelation / three visibility modes, 7 integration gaps (Counselor negotiation, Occupation + scene generation, Parliament civic bridge, Resource symmetry, Lattice filter-chain transparency, NPE -> Named NPC, Scene Slate recovery) (:36-46).
  - Part 8 Domain Echo Reference Table; Part 11 "What must not change"; Part 12 priorities (blocking / high value / creative) (:52-62).
- **Conflicts / stale:** an index only; the Domain Echo / Scene Slate vocabulary maps to retired echo transport.
- **Open items:** the gaps listed are unresolved from this file alone.

### .designs/systems/_architecture/reference/key_echo_armature_v1.md
- **What it is:** seam-contract layer and "Echo Matrix" (2026-07-07, lane IN, Fable tier) over Key substrate, with fork docket 5.1-5.16 and Jordan's ruling log.
- **Status:** "RATIFIED (Jordan, 2026-07-07 ... ED-IN-0026)". Reading: superseded/retired as a whole by ED-IN-0232 (Key substrate retired); valuable as a record of the audit findings and rulings.
- **Bears on:** CORE, SC, SE, FA, FI, DICE.
- **Content that matters:**
  - Audit headline: "no executable Key substrate" at that time; "transport is islands, not organs" (contest kernel, threadwork, knots, settlement layer built-but-unreachable); `zoom_out({})` dropped outcomes; 100% of contest scenes deferred (:34-50).
  - Seam-contract row fields incl. required FEEDBACK line (what the player sees when a seam fires) (:56-68).
  - Directions: bottom-up, top-down, lateral, diagonal (`causes[]`), outward (rendering), temporal (:78-177).
  - Ruling 5.12: adopt symmetric ER-2 continuity correction and pool-aware Overwhelming bar across contest and combat kernels, execution pending ED-PC-0003 (:266, :288).
  - 5.3/5.4: OF-7 deferred-apply and OF-B1 no-sync-re-entry RATIFIED, defaults flipped True (:279-280). 5.2 `decay()` deferred (:278). 5.11 CI milestone 75-vs-80 discrepancy kept as data (:265, :287).
  - Candidate new Key types for settlement revolt/captured/surrendered/collapse, CI milestone, era transition, second calamity (:186-199).
- **Conflicts / stale:** the substrate it standardised was retired; the CI milestones 40/55/65/80/100 vs presentation 75 discrepancy needs a code check [UNVERIFIED]; ruling 5.12 (shared degree continuity correction) may or may not have executed [UNVERIFIED].
- **Open items:** 5.5 RNG model collision (single `World.rng` vs per-emission seed vs named draw service), deferred to PR-2; 5.8/5.9 (ED-SC-0002 echo keying, ED-SE-0002 Accord stacking) left to SC/SE lanes.

### .designs/systems/_architecture/reference/key_substrate_v30.md
- **What it is:** PP-687 "Universal Key Substrate" spec (promoted 2026-05-01): every event is a typed append-only Key; one update rule; Memory as Key references; causal graph; determinism.
- **Status:** header says both "Status: CANONICAL" (:15) and "Status: PROVISIONAL" (:18, :635). Reading: RETIRED (ED-IN-0232 retired keys.py, echo transport, emit/consume); historical vocabulary source only.
- **Bears on:** CORE, CHAR, SC, FA, WR.
- **Content that matters:**
  - Key schema: id, type, source_actor, emitted_at (season_index, sub_step_index), causes[], targets[] with role and impact_vector, stat_deltas, scale_signature, symbolic_dimensions, visibility, time_horizon, permanence, payload (:40-84); eight validation invariants (:120-133).
  - Four Conviction axes (hierarchical, sacred, instrumental, traditional) and a 13x4 Conviction->axis matrix; `interpretation = Sum armature_position * symbolic_dimensions * impact_vector` (:135-164).
  - Update rule in 7 steps, amended by OF-7 deferred-apply and OF-B1 no-sync-re-entry (:194-239).
  - NPC Memory as Key refs with salience 0..3, `compute_salience = clamp(abs(interp) * {1.5,1.0,0.5}, 0, 3)` (:276-327); only ~15% of Keys carry `causes[]` (:376); sim: 2,703 Keys/30 seasons, ~1,000 memory entries per NPC at 30 seasons (:575-583).
  - Determinism: RNG seeded per Key emission, stable sort, x86_64 FP (:406-422); V1-V8 battery, V7/V8 never measured in production (:556-569).
- **Conflicts / stale:** Key substrate retired; the Memory/salience/armature-interpretation mechanism is the design origin of NPC memory and may or may not have a live successor in `engine/season/` [UNVERIFIED]. Double status line.
- **Open items:** salience form "provisional pending Stage 10 calibration" (:327, :629); 5th axis permitted as Class B extension (:146).

### .designs/systems/_architecture/reference/key_type_registry_v30.md
- **What it is:** registry (55 types by its own count) of Key types in 7 families with payload fields, emitting/consuming systems, defaults.
- **Status:** "Status: CANONICAL" (:17). Reading: retired with the Key substrate; useful as a roster of event kinds the old design considered significant.
- **Bears on:** CORE, CHAR, FA, SE, WR, PC, SC, MB, FI.
- **Content that matters:**
  - Families and examples: scene_event (dialogue, witness, gift, insult, threat, thread_operation, draft_da, displacement, interaction, gossip), da_outcome (public_governance, covert_betrayal, diplomatic_alliance, antinomian_action, economic_intervention), mechanical_event (season_change, accounting, cascade_resolution, mission_shift, scene_entered/exited/skipped, project_advanced, settlement_captured, era_transition, second_calamity, theocracy_unification_declared) (:45-610).
  - state_transition: scar_acquired, standing_change (magnitude 1-3 per faction_politics 1.0a), coup_attempted, succession, project_completed/failed, settlement_revolt, opinion_revised, concern_resolved (:613-765, :1164-1249).
  - Five ED-IN-0014 types are DECLARE-ONLY (zero emit sites) because the gates they describe (settlement Order 0, undefended auto-capture, era transitions, CI=100) have no evaluator in the loop (:472-609) — a record of mechanisms that were never built.
  - `mechanical.second_calamity` (MS<=5 sustained 10 seasons in Post-Calamity Era) is "the only true campaign terminal" (:546); `era_transition` covers MS=0, recovery, IP=100 3-phase occupation, anarchy (:508).
  - `scene.accord_echo` live but organically dormant (:977-1013). Combat subtypes strike/hit/felled/resolved (:907-975).
  - Extension process requires a `references/rendering_dispositions.yaml` row for every new type (:1288-1299); total count reconciled to 55 (:1264).
- **Conflicts / stale:** registry retired with substrate (ED-IN-0232); `references/rendering_dispositions.yaml` "does not exist yet" (:1100) [UNVERIFIED now]. Several `[STUB]` payloads "inferred, not canon-specified" (:156, :173, :191, :924).
- **Open items:** dual-emitter ownership of the CI=100 event undecided between ci_political and territorial_piety (:595-602).

### .designs/systems/_architecture/reference/ners_vsg_reconciliation_v1.md
- **What it is:** reconciliation (2026-07-13, lane IN) of the PR#127 empirical harness branch with the PR#128 "VSG" settlement-generator design branch; merged D/E/B blocker register and 7-phase workplan.
- **Status:** "ALL SIX ITEMS RULED (D1-D5 ED-IN-0046; D6+B1 ED-IN-0047; B2+B12 direct Jordan ruling 2026-07-13)". Reading: historical decisions; the code harness it cites (`tools/sim_harness/`, `sim/territory/`) [UNVERIFIED whether any survives].
- **Bears on:** SE, FA, WR, CORE.
- **Content that matters:**
  - Execution findings: writing `Compact` through built `ledger_add()` silently accepts unknown kinds 100/100; G606 cumulative suspicion drives 100% of terminal recalls even at the most lenient tuning; L/PS reads zero outside declarations 100/100; unaugmented Π term pins settlements at ceiling 298/300 (`PI_RUNAWAY_SUSTAINED`) (:47-51).
  - E1 (Π restoring term) must ship bundled with E3 (subsistence floor) and E7 (positive-feedback path) (:51, :81, :108-115).
  - New items E8 (reconcile IT-2 Condotta x0.5 Mil against four `faction.Mil` read sites: `_mil_advantage_signal`, `CONQUEST_MIN_MIL`, muster-pool formula, `_faction_to_unit`), E9 (Ministry action economy), E10 (HRE-2 Chapter Capture acquisition cost) (:86-88).
  - B12 RULED: Settlement -> Territory (new tier) -> Province (only while a common faction holder) -> Duchy -> Country; governance-type cascade; L/PS as consent modulator; monarch and Parliament chain-bypass; overrules PP-726 §1/§2.3 (`scale_hierarchy_v1.md`) (:225-236).
  - B1 starting factions 4; B2 S-006 stays Goldenfurt; geography YAML migrated to 37 settlements (:202-223). B11: `engine_clock` unauthored blocks Relay Tier/Beacon Network (:101).
  - Event-deck engine: 13-of-28-card harness real; at skill 0.0 82% ruin, skill 1.0 100% prosper (:98).
- **Conflicts / stale:** "Territory" now a real tier vs older "Territory = Settlement" docs; Key-bearing routing retired. `engine_clock` status may have changed [UNVERIFIED].
- **Open items:** Part 41 Relay Tier/Beacon Network held until `engine_clock` (B11); VSG §7 open calls (temperament promotion, off-owner allegiance axis, weight/tau calibration) (:127).

### .designs/systems/_architecture/reference/player_agency_v30_index.md
- **What it is:** generated heading/size index (2026-04-19) of `player_agency_v30.md` (dated 2026-04-15, ~11k tokens; body absent).
- **Status:** indexed doc "CANONICAL — approved 2026-04-17 (editorial batch acceptance)" (:25). Reading: historical; body not here.
- **Bears on:** CHAR, CORE, WR, FA.
- **Content that matters:**
  - Structure: Convictions (§2), Duties (§3, types and completion, Duty vs Conviction tension §3.5), Scene Slate (§4, generation algorithm §4.2 = 1,115 tokens, slate size §4.3, opportunities not pursued §4.5) (:38-55).
  - §5 Stature progression with Renown Track (cross-faction personal authority) and leadership acquisition vs staying independent (:56-60).
  - §6 Scene Action Budget (base, modifiers, scene action economy) (:61-64); §9 Resources (Throughline T2), §10 Conviction Legacy (T8), §11 Lineage Acts (mentorship, succession, thread legacy, no lineage act) (:73-80).
  - Precedent analysis: Romance of Three Kingdoms, CK3, Disco Elysium, Mount & Blade/Manor Lords, Pathologic 2, Pentiment (:31-37).
  - Canon compliance claims P-03 (perceptual horizon defines available scenes) and P-15 (Beliefs personal, Duties cultural, Convictions metaphysical) (:29).
- **Conflicts / stale:** index only; the Scene Slate and SA budget are the design origin of the "scene slate" referenced by the retired Key types.
- **Open items:** none visible.

### .designs/systems/_architecture/reference/propagation_spec_v1.md
- **What it is:** cross-scale propagation contract (ratified 2026-07-02, J-38/ED-1093): season-as-tick ordering, aggregate-up (Domain Echo), distribute-down, termination proofs.
- **Status:** "CANONICAL — ratified 2026-07-02"; amended 2026-07-07 (OF-7/OF-B1 ratified); §1 O.1 corrected 2026-08-27 (ED-IN-0199). Reading: written for the retired Key substrate; its per-tick/season-as-tick ordering logic is the design ancestor of `engine/season/` ordering.
- **Bears on:** CORE, SE, FA, SC.
- **Content that matters:**
  - Season is the tick: SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY; accounting is six steps, the sixth a report-only province-Accord drift probe; ORD-1 dict insertion order load-bearing, ORD-2 no `set()` gating emission order (:65-108). A 2026-08-27 correction records that the "engine_clock" module the text named did not exist until then and ordering sat inside the ACTION callback (:67).
  - Arc vs year cadence: `new_arc` fires on season%4==1, year-end decay on season%4==0, a deliberate one-tick offset "not a bug" (:75).
  - AU-1: faction stat has no setter, `faction_stat = AGGREGATE(settlement stats) (+) Sum national_event_modifier`; echoes write a settlement locus cell or a decaying modifier; faction target `stat_deltas` must stay empty (:163-189).
  - Theorem A (no scene resolved in tick N can cause another in tick N; slate frozen once) and Theorem B (drain halts under `CASCADE_DEPTH_MAX`/`EMISSIONS_PER_TICK_MAX`); cross-tick convergence explicitly NOT proven; C1 macro-loop magnitude bounded by echo cap +/-2 per stat (:318, :351-359).
  - Open D.6 double-count risk: down-targeted settlement deltas may overlap what the aggregate reads, breaking convergence (:271).
  - Stability Crisis hysteresis (ED-749: edge-triggered, re-arm after Stab >=3 for two Accountings, player faction only) was a rule the sim did not comply with (:361).
  - Three unreconciled RNG models (single `World.rng`, per-emission seed, named-draw service) (:127).
- **Conflicts / stale:** all Key/KeyLog/`cascade_depth` machinery retired; `decay()`, cap constants and RNG model never ruled (per armature). Whether `engine/season/` honours the one-tick arc/year offset and hysteresis is [UNVERIFIED].
- **Open items:** OF-CAP, OF-3 decay(), OF-D6 disjointness, RNG-MODEL-COLLISION, ORD-3/ORD-4, O-2 (`new_season` label computed nowhere), OF-HYSTERESIS-AUDIT for other level-triggered §4.3.2 triggers (:389-404).

### .designs/systems/_architecture/reference/repo_state_armature_v1.md
- **What it is:** charter (ED-IN-0077, 2026-07-20) for a "repository state armature": one definitions store, one review aggregator `review_core.py`, one ratchet baseline.
- **Status:** "RATIFIED — charter + Phases 0-2 ... Phase 3 COMPLETE ... Phase 5 HELD BACK pending OPT-AV-1". Reading: historical/superseded; the file itself records `review_core.py` RETIRED 2026-08-21 (ED-IN-0194) (:94) and the banner it builds is forbidden by CLAUDE.md §0.3.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Three artifacts: `references/definitions/` single source, `tools/review_core.py` -> `review_state.json`, `registers/review_baseline.yaml` count-ceiling ratchet (:36-82).
  - View inversion: `names_index.yaml` and `descriptor_registry.yaml` regenerated at their existing paths as `# GENERATED` views so blocking readers are never rewired (:46-52).
  - P5 attribute centralization hard-gated on Jordan ruling OPT-AV-1 (7/9/10-with-Recall roster) (:135-137); collapse 3 Combat-Pool definitions into one `kind: formula`.
  - CI job regrouping explicitly rejected (:103-106).
  - Top risk: lossy regeneration of the naming spine, mitigated by parity test (:157-165).
- **Conflicts / stale:** it asserts a SessionStart banner as BUILT, contradicting CLAUDE.md §0.3 (banner retired); `review_core.py` retired. Phase 2 `definitions/` store status unknown [UNVERIFIED].
- **Open items:** OPT-AV-1 attribute roster (see CHAR lane); Phase 4 freshness absorption.

### .designs/systems/_architecture/reference/repository_keep_set_v1.md
- **What it is:** keep-set / evacuation plan (2026-08-04, ED-IN-0125/0127/0128/0129/0139): `main` keeps code-first, outdated prose evacuates to a tag.
- **Status:** "RULES RATIFIED ... PER-DIRECTORY DISPOSITIONS PROPOSED ... No deletion is authorised by this document." Reading: historical; the evacuation executed (the tree now has `.designs/`, no `audit/`), but this table is the rationale, partition of record was `tools/evacuation_plan.py`.
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - Rule cuts on outdated, not format: prose with no code pair (`canon/`, 14 `godot: no-oracle` specs) stays authoritative; prose with a code pair is "information only" (:55-60).
  - `engine/params/` evacuated after capture into `engine/engine_params/params_tables.yaml` (43 files, 258 tables, 1,367 rows); provenance `[canonical: params/...]` cites the fork (:67-90).
  - `registers/` kept, restarted via read-only `registers/archive/` snapshot because 103 files cite `ED-` IDs and `validate_ed_citations.py` is blocking (:199-206).
  - Eight things that go red under mass deletion (ED citations, restructure ledger alias rows, co-file checker, scope ratchet, freshness pins, SessionStart banner, `tests/valoria`, dashboard) (:294-318).
  - Standing review gate: adversarial read-only critic after every milestone; three defects found only by review (:257-290).
  - Streamlined means working tree; do not rewrite history because SHAs are cited (:353-383).
- **Conflicts / stale:** counts (3148 files -> 1691 KEEP) are snapshots; CLAUDE.md now says there is "no `deprecated/` tree". `canon/` MB code home `tests/sim/mass_battle` re-home status [UNVERIFIED].
- **Open items:** §10 open calls (godot stale docs per-file, skills/proposals per-file) are overtaken by events.

### .designs/systems/_architecture/reference/scale_transitions_v30_index.md
- **What it is:** generated heading/size index (2026-04-18) of `scale_transitions_v30.md` v1.0 (2026-04-13, ~5.2k tokens; body absent).
- **Status:** indexed doc "DESIGN — canonical for scale transitions and mode bridging" (:25). Reading: historical; cited by the retired echo transport and `cross_scale` code.
- **Bears on:** CORE, SC, MB, FI, FA.
- **Content that matters:**
  - Section map: §3 eight handoff rules plus §3.9 Fieldwork <-> all systems (largest: 652 tokens), §4 Zoom In/Out with §4.3.2 mandatory zoom-in triggers and §4.3.3 world-state triggers, §4.4 "Where Were You?" retrospective scene generation (:31-46).
  - §5 Domain Echo: trigger, amount, timing by mode, Debate (PP-108), Accord Echo (§5.5), Thread Echo (§5.6, ED-673) (:48-54).
  - §7 Sufficient Scope register-shift trigger; §8 scope shift rules; §9 PC Faction Embedding (ED-075); §11 Contested Figure System (ED-167/168) (:61-65).
- **Conflicts / stale:** index only; the "Zoom In/Zoom Out" and "Domain Echo" vocabulary maps onto the season loop's scene dispatch [UNVERIFIED current equivalents].
- **Open items:** none visible.

### .designs/systems/_architecture/reference/scale_transitions_v30_infill.md
- **What it is:** prose infill for `scale_transitions_v30.md` (companion, one doc in parts).
- **Status:** "DESIGN — canonical for scale transitions and mode bridging" (:14). Reading: historical.
- **Bears on:** CORE, SC, MB, FI.
- **Content that matters:**
  - TTRPG is baseline; Board Game abstracts; Hybrid is the bridge, not a third mode (:18-19).
  - Multiple simultaneous Zoom Ins resolve in Attunement order, then Agility, then GM (ED-072, ED-160) (:40).
  - Domain Echo in Hybrid queues and fires at next BG Accounting Step 3 (:48); BG clock advances only at Accounting (:55).
  - Sufficient Scope: faction-scope if an action would normally require a Domain Action roll (treaty, accusation, territorial claim); GM makes final call (ED-074) (:59-61).
  - Scope shift once per round, second costs +1 Inspiration (:63). Contested Figure killed between Zoom Ins is redirected or Zoom Out (:67-68).
- **Conflicts / stale:** relies on GM adjudication; no-GM engine must resolve scope by rule.
- **Open items:** skeleton body of most subsections is not in this part.

### .designs/systems/_architecture/reference/session_a_spec_patches.md
- **What it is:** spec patch list (2026-04-19, Session A): 6 patches + backstory strike, all propagated.
- **Status:** "ALL PATCHES PROPAGATED". Reading: historical; documents what was changed in params/NPC trees at the time.
- **Bears on:** FA, SE, WR, CHAR.
- **Content that matters:**
  - Three-scale resolution model (settlement -> province -> peninsula) inserted into phases (:17-45).
  - Bishop appointment as Church Consul-Outward action: Influence vs Ob 1; Overwhelming gives Accord +1 and PT +1; Partial gives Church Stability -1; Failure no Casus Belli (:49-80).
  - Secession candidates limited to settlements held by a national faction; subnational/Uncontrolled settlements cannot secede (:89-103).
  - RM emergence requires Order = 0 (not <=1), PT <=1, local Disposition toward Yrsa Vossen >= +3 (:107-124).
  - Splinter Influence split 60/40 like Mandate (:128-142). Crown P4 default: garrison T2 Kronmark if ungarrisoned and a Varfell unit is active in T4 (:146-163).
  - Patch 7 strikes the prior king's assassination as pre-game backstory in favour of the Royal Crisis fuse (:167-175).
- **Conflicts / stale:** targets (`params/bg/*`, `designs/provincial/*`) are gone; whether the Order=0 RM threshold and 60/40 split live in current faction code is [UNVERIFIED].
- **Open items:** none.

### .designs/systems/_architecture/reference/tensions_pair_validation.md
- **What it is:** validation (post 2026-04-19) that all 15 pairs of the six rescoped Tensions Deck cards C1-C6 yield a belligerent, a target, and opportunity/obligation for the rest.
- **Status:** none stated. Reading: historical; the deck itself (draw 1) was set by the conflict proposal, this file validates draw-2 pairs, so partly overtaken.
- **Bears on:** FA, WR.
- **Content that matters:**
  - Six cards: C1 Crown-Church (S003), C2 Crown-Varfell border, C3 Crown-Löwenritter, C4 Hafenmark-Church bishop claim, C5 Hafenmark-Guilds (S017), C6 Varfell-RM (:20-27).
  - Method: criteria 1-3 (belligerent, target, opportunity or obligation) applied by hand to all 15 pairs; 15/15 pass (:11-14, :277).
  - Weakest pair C5+C6 (two internal crises, quiet "cold start"); strongest C1+C2, C3+C4, C1+C4 (:281-283).
- **Conflicts / stale:** pass/fail judged by reading, not by simulation, and the "draw 2" premise conflicts with the "draw 1" of `conflict_architecture_proposal.md` [UNVERIFIED which is current].
- **Open items:** none.

### .designs/systems/_architecture/reference/videogame_mode_spec_index.md
- **What it is:** generated heading/size index (2026-04-19) of `videogame_mode_spec.md` (2026-04-17, ~4.1k tokens; body absent).
- **Status:** indexed doc "CANONICAL — single-mode extraction reference for Godot implementation" (:25). Reading: historical; brief names the full spec as a cross-cutting read.
- **Bears on:** GO, CORE, all.
- **Content that matters:**
  - Collapses TTRPG/BG/Hybrid branching to one videogame spec; per-system mode collapse for combat, social contest, fieldwork, threadwork, mass battle, scale transitions, faction layer, NPC behavior, player agency, companion, settlement layer (:30-41).
  - §2 unified threadwork mode table, §3 "GM Decides" resolution register, §4 What is discarded, §5 implementation priority (:42-45).
- **Conflicts / stale:** index only; the "GM Decides" register is the mapping from human-GM rules to engine rules and would be a primary referent for any no-GM conformance audit.
- **Open items:** the full body is in `.designs/systems/_architecture/` or elsewhere [UNVERIFIED location].

### .designs/systems/articulation/reference/articulation_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `6545067`) of the articulation layer: `engine/cross_scale/articulation.py` as subscriber to the Key scheduler.
- **Status:** "REFERENCE — traced structure only". Reading: historical; subject (Key-scheduler subscriptions) retired.
- **Bears on:** CORE, WR, GO.
- **Content that matters:**
  - Tier 1 `render_protagonist_lens`, Tier 3 `generate_chronicle_entry` have zero callers; Tier 2 `evaluate_articulation_triggers` only called by a stub-wiring regression probe (:130-132).
  - `subscribe_all` wired 13 callbacks (`_TRIGGER_TYPE_IDS`) at every boot, but 10 of 13 trigger types had zero production emitter, so none could fire under default flags: "structurally present and dormant" (:133-137).
  - Fired callback `_on_key` ignored the Key and returned a `stubwire.stub_resolve` no-op; only a telemetry counter (`CampaignResult.stub_hits`) moved (:81-87).
  - `scene.combat_felled` subscribed but has no emission path; `scene.combat_resolved` behind default-off `DISPATCH_COMBAT_BRIDGE` (:134-135).
  - Declared `consumes` wildcard `{type: "*"}` vs actual 13 explicit ids (:138). `subscribe_all` non-idempotent (:139).
- **Conflicts / stale:** the articulation tier model (protagonist lens / cut scenes / chronicle) was a stub then; whether `engine/season/` has a chronicle or narrative-render function is for the WR/GO lanes [UNVERIFIED].
- **Open items:** none; every gap was a traced finding.

### .designs/systems/characters/reference/character_histories_v30_index.md
- **What it is:** generated heading/size index (2026-04-20) of `character_histories_v30.md` (lifepath system, ~9.8k tokens; body absent).
- **Status:** indexed doc "CANONICAL — approved 2026-04-17 (editorial batch acceptance)" (:24). Reading: historical; paired with `_infill`.
- **Bears on:** CHAR, FA.
- **Content that matters:**
  - Four stages: Origin (8: Crown Heartland, Highland, Fjord, Southern Einhir, Himmelenger, Valorsplatz Underclass, Border, Displaced), Formation (7), Vocation (9 faction/cross-faction groups), Catalyst (7) (:29-65).
  - Scope: SaGa-style sparking, Recall-gated equip slots, skill levels 1-3 (:25).
  - Sections on Skill Level Design Principle, Character Creation Summary, canonical test character Mira Sondhal (ED-143), Open Editorial Items (:66-69).
  - Godot implementation noted in `valoria-game/docs/history_skill_integration.md` (:28).
- **Conflicts / stale:** index only; the vocation lists with skills are in the skeleton body, not here. [UNVERIFIED] whether engine has a lifepath generator.
- **Open items:** see infill (ED-377, ED-380, ED-390, ED-391).

### .designs/systems/characters/reference/character_histories_v30_infill.md
- **What it is:** prose infill for the lifepath system: origin/formation/catalyst narrative, no vocation or skill-list content.
- **Status:** "CANONICAL — approved 2026-04-17" (:13). Reading: historical; skeleton portion missing here so mechanical content (skills per stage) is incomplete.
- **Bears on:** CHAR, WR, FA.
- **Content that matters:**
  - Four lifepath stages each grant a History; 5 starting skills at Level 1; Origin grants 1, Vocation 2 (at least 1 unique), Catalyst 1 (:19-20, :91, :103).
  - Equip slots `max_equipped = Recall` (1-7); skill Level 2 needs History dice_bonus >= 3, Level 3 >= 5 (:22-23).
  - Starting Truth values by origin: Highland 4, Himmelenger 5, Valorsplatz Underclass 3, Border 4, Displaced 2; Self-Taught Formation applies Truth -1 (:34, :48, :52, :59, :65, :80).
  - Displaced origin grants unique skill "Scarred by the Unreal" (immune to Composure loss and surprise-round penalties from Thread phenomena; Thread Sensitivity +3) (:65).
  - 4C "Lost Someone" uses a GM "ghost sheet" (anti-fridge clause); 4G Religious Crisis direction "GM determines" (:108, :117). 4F events: Spartfell Incident, Templar Suppression, Ducal Border Clash (:113-115).
  - Cultural fact: 245 years of Church suppression of Einhir inheritance (:43).
- **Conflicts / stale:** GM-dependent clauses (4C, 4G) have no engine equivalent unless the engine derives them [UNVERIFIED]. Cross-ref list names retired docs.
- **Open items:** ED-377 (Intuitive Threadwork + co-movement), ED-380 (Deep South +8 TS Leap eligibility), ED-390 (new setting events need approval), ED-391 (ghost sheet) (:126-129).

### .designs/systems/characters/reference/characters_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `654506799c63`) of `systems/characters/sim/{conviction,beliefs,companion}.py`: Conviction Scars, Beliefs, companion stub, world snapshot round-trip.
- **Status:** "REFERENCE — traced structure only". Reading: historical trace, but its gap table records which Conviction mechanics were uncalled.
- **Bears on:** CHAR, FI, SC, CORE.
- **Content that matters:**
  - `apply_conviction_scar` flow: Thread-witnessing season cap (one Scar per Conviction per season), Certainty-scaled magnitude, thresholds destabilised=1, shifted=2, in-crisis >=3 (:68-79).
  - Gap 1: no production entry exercised the core mechanics; the only caller `knots.apply_knot_loss` has zero production callers; `social_success` caller `contest_legacy_stub.run_contest` is dead; `run_companion_scene` is a stub only a probe calls (:151).
  - Gap 2: `add_belief` has zero callers, so no live campaign can contain a `Belief` (:152). Gap 4: `restore_world` test-only (:154). Gap 5: `check_conviction_threshold` and `revise_belief` have zero callers even in tests (:155).
  - Gap 3: `piety_track` contract declared Key consumption the code never implemented (:153).
  - Gap 7 CLOSED 2026-08-24: knots called `apply_conviction_scar` with `conviction='Loyalty'`, absent from the 9-name roster, so every scar silently no-op'd; roster now single-owned in `references/descriptor_registry.yaml:conviction_roster` and an unknown name raises; caller now passes `'Honor'` (:157).
- **Conflicts / stale:** `systems/characters/sim/*` and `engine/mc_v18.py` anchors may be moved or deleted [UNVERIFIED]; the Convictions-as-9 vs 13 roster question is settled in code (gap 7) but design docs (conviction_track_v30, PP-718) speak of 13.
- **Open items:** whether `engine/season/` consumes Convictions/Beliefs at all (CHAR audit); a no-op scar-on-unknown-name was a silent failure of the "stub that returns success" class.

### .designs/systems/characters/reference/conviction_track_v1_pp718_vetting.md
- **What it is:** a full "N/Mu/M-1..M-11/T/Q" vetting walkthrough (2026-05-10) of PP-718 per-Conviction Scar accumulation.
- **Status:** none stated; ends "Overall: Class B vetting passes". Reading: historical justification for the rule; the mechanic is what matters.
- **Bears on:** CHAR, FA, WR.
- **Content that matters:**
  - Rule: crisis fires when any single Conviction reaches 3+ Scars (not aggregate); multi-primary NPCs Scar each Conviction independently; cultural-background-only (weight 0.2-0.4) crises produce muted drift (:11-17).
  - Crisis-table roll 5: legacy "Autonomy survival" replaced by Self-Other-orientation override (Autonomy renamed Liberty per PP-684) (:16, :127).
  - Pre-PP-684 mapping Reason->Scholastic, Autonomy->Liberty, Continuity roster-determined (:17).
  - Thread-witnessing Scar cap 1 per season per NPC; witness requirement: direct presence or credible testimony (Evidence Track + Disposition >= +1); Player Conviction Check = Spirit pool TN 7 Ob 1 (ED-664) (:69, :147, :183, :250).
  - Faction effective_convictions aggregated from member NPCs (PP-686 §3.2); Cascade math consumes it (:50, :259).
  - Final tally 5 plus, 5 satisfies, 1 n/a, 0 violations after recalibrating M-1/M-9 to avoid double-counting (:209, :288).
- **Conflicts / stale:** the 13-Conviction taxonomy vs the 9-name code roster in `conviction.py` (see characters flow skeleton gap 7) [UNVERIFIED current code]. The vetting framework (N/Mu/M/T/Q) is itself a prose process, not a mechanism.
- **Open items:** none.

### .designs/systems/characters/reference/conviction_track_v30.md
- **What it is:** NB: despite the filename, this is the **Piety Track (PT, per-territory) and Church Influence (CI) redesign**, PP-406..PP-418 (2026-04-05), not the per-character Conviction system. Skeleton; prose in `_infill`.
- **Status:** "CANONICAL — approved 2026-04-17"; §4.2, §4.3, §6, §7 "SUPERSEDED-BY GD-1 (peninsula-only victory)"; §4.1 and §3 pacing superseded by PP-421 (CI runs to 100, no freeze). Reading: part live (PT/CI mechanics), part historical (Church/Varfell victory paths).
- **Bears on:** SE, FA, WR, CHAR (naming).
- **Content that matters:**
  - PT 0-5 per territory (0 = Einhir Restoration, 5 = Solmund Orthodoxy); starting values by territory T1..T17; T15 fixed 0 "cannot increase by any means"; seasonal move cap +/-1 (:30-72). Name collision: the stat "Conviction (PT)" vs per-character Convictions (ED-644 notes PT term equivalence) (:39).
  - Calamity Drift: MS <=50, <=35, <=20 erode PT by 1 at Accounting for adjacent, within 2 steps, all territories; ignores +/-1 cap (:92-98); Thread-op drift capped at +/-2 combined (:114).
  - Church Seizure Ob = 2 + Fort + max(0, 3 - PT), floor 1; modifiers Consecrated -1, failed-seizure +1 each, Löwenritter +1; results by degree (:144-176).
  - CI per season: passive +1, Conviction Yield floor(sum 1 at PT5, 0.5 at PT4), Assert Influence vs Ob 2 (+1; failure Stability -1), Suppress negates passive, Hafenmark Baralta Mandate >=4 gives CI -1 (:191-214).
  - RM emergence: Warden's Accord (WA) -3..+3; emergence needs WA <=-2, >=3 territories PT <=1, MS <=50; one-shot; starting stats Mandate = count PT<=1 (min2,max5), Influence 4, Wealth 1, Military 0, Stability 3 (:317-375).
  - Environmental presentation per PT transition and Church Attention Pool indicators 0..4+ (:502-527).
- **Conflicts / stale:** CI milestone set 40/55/65/80/100 vs stale "CI 75" row (:538), armature 5.11 left unresolved; presentation of CI 75 still in file. GAP list: RM emergence frequency, Community Weaving feedback loop, Consecrated seizure edge case, Fort Level data absent (:468-476). Victory sections (TCV >=18, AEA clock, Hollow Victory) dead per GD-1.
- **Open items:** [GAP] CI pacing against CI-100 model never simulated; [GAP] AEA pacing; Hafenmark Secular Governance PT floor of 2.

### .designs/systems/characters/reference/conviction_track_v30_index.md
- **What it is:** generated heading/size index (2026-04-18) of the Piety Track doc (~7.3k tokens); section line numbers refer to the earlier un-superseded text.
- **Status:** "CANONICAL — approved 2026-04-17". Reading: historical; older than body (still uses TC/CV/RS terminology).
- **Bears on:** SE, FA, CHAR (naming).
- **Content that matters:**
  - Heading map shows pre-rename vocabulary: "TC Generation", "CV Change Environmental Events", "RS-Linked CV Erosion" (:31-37, :58-60), i.e. TC = Theocracy Counter (now CI), CV = Conviction value (now PT), RS (now MS).
  - Largest sections: §11 presentation layer (1,134 tokens), §5 RM emergence (879), §4 victory (850).
- **Conflicts / stale:** index terminology (TC, CV, RS) is superseded by CI/PT/MS in the body.
- **Open items:** none.

### .designs/systems/characters/reference/conviction_track_v30_infill.md
- **What it is:** prose infill for the Piety Track doc; header says "Status: Design Proposal — Awaiting User Review".
- **Status:** "Design Proposal — Awaiting User Review" (:14). Reading: historical; skeleton carries the later CANONICAL status; "CV" terminology is stale.
- **Bears on:** SE, FA, WR.
- **Content that matters:**
  - Rationale: PT captures popular belief, not institutional Church power (Mandate) nor theological correctness; Restoration pole is recovered cultural memory, not a competing faith (:20).
  - "Drift: None. CV is sticky" (:23) — contradicted by Calamity Drift and Thread drift in the skeleton.
  - Each faction may attempt one PT movement action per season total, not per territory (:25).
  - Consecrated: PT cannot drop below 4 while Church controls (:29), matching skeleton §1.4 only partly (skeleton says lost if Church loses control AND PT <4).
  - RM emergence is one-shot; suppression does not restore pre-emergence state (:53-56). Path B blocked if RM has emerged (:60). Hollow Victory scoring unresolved (ED-304) (:48).
  - Co-victory impossible if RM hostile (WA >= +2 cannot coexist) (:65).
- **Conflicts / stale:** "drift none" vs skeleton Calamity Drift; per-faction one action per season vs skeleton per-territory actions. The skeleton wins in time.
- **Open items:** ED-304 Hollow Victory scoring.

### .designs/systems/combat/combat_engine_v1/reference/README.md
- **What it is:** short README of the personal-combat engine v1 (modular, multimodal, matrix-validated); file list and status.
- **Status:** "CANONICAL — ratified by ED-900/904 and docket ED-1029". Reading: live as history of the engine now at `modules/combat/` (CURRENT.md names the head).
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Files: core.py (sigma-resolution + armour-aware damage), combatant.py, config.py, systems.py, tradition.py, wrapper.py (engagement state machine: measure/approach/close, displacement, re-opening, bind, feinting, 95% cap) (:16-20).
  - Validated against the four-state weapon matchup matrix A0 unarmoured -> A3 full plate (:14-15).
  - Canonical resolution is d_sigma (sigma-leverage), additive-coupled damage and ED-1041 bilateral-Ob wounds, "NOT the v30 model (Agi x2 pool / TN-7 / multiplicative STR)" (:24-25).
- **Conflicts / stale:** file locations moved (code now `modules/combat/`); the pool model note agrees with canonical_registry's superseded rows.
- **Open items:** none.

### .designs/systems/combat/combat_engine_v1/reference/REARCHITECTURE_v1.md
- **What it is:** 2026-06-29 re-architecture blueprint (Class-C, Jordan-vetoable) for the combat engine: six layers L0-L5.
- **Status:** none stated; "Class-C, Jordan-vetoable". Reading: partly executed historical blueprint; which phases landed is [UNVERIFIED].
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Six layers one-way: L0 weapon primitives (`weapon_physics.py`: mass, head_len, grip_len, pommel_kg, wclass, hilt...) -> L1 core (`resolve` mu-shift, degree, pool) -> L2 weapon-gated subsystems (`systems.py` + `capabilities.py`) -> L3 wrapper (orchestrate only, owns all mutation) -> L4 traditions -> L5 abilities (:24-53).
  - Symmetry: weapon = sum of physical primitives; tradition = sum of ability primitives; ability = learned ACCESS to a graph transition, never a +X dial (:51-55).
  - Violation worklist: wrapper assembles `net_sigma` inline; `HEFT`, `GATE`, `spd`, `reach_base` hand tables to be derived from physics; `closes_poorly`, `wt`, `seize` vestigial (:59-71).
  - Five phased steps; Phase 1 build-only, Phase 2 behaviour-preserving byte-identical, Phase 3 re-baseline (mirror=50, no one-shot, tier spread) (:73-87).
  - Blocked on Jordan: D-A damage scale, pommel_kg singletons, affinity-budget build layer, K_* gains, pick vs mace vs plate, seize lever retire/reroute, reach dominance r~0.83 (:89-97).
- **Conflicts / stale:** `seize` lever later found dead (see ability_armature); the "access not modifier" principle contradicts ability_armature §1 ("Modulate, never unlock").
- **Open items:** the seven "blocked on Jordan" items are a decision list that may have been answered in `modules/combat/` [UNVERIFIED].

### .designs/systems/combat/combat_engine_v1/reference/ability_armature.md
- **What it is:** provisional armature (framework) for martial-tradition abilities: levers, phase x competence cross-product, source material by tradition, workflow.
- **Status:** "Provisional". Reading: partly superseded by the L5 "ability = access" model in REARCHITECTURE; ED-PC-0042 label fix recorded.
- **Bears on:** PC.
- **Content that matters:**
  - Principles: modulate never unlock; invariant-safe (unequipped = no change); every ability needs a documented technique (bottom-up) AND a historical precedent (top-down) with a source tier S1..S5; priority-gap traditions get no ability until S1/S2 anchored (:20-25, :158-159).
  - Phases Approach / Initiative-seizure / Exchange / Separation; competences Measure, Balance, Reading, Seizing, Countering, Parrying, Striking, Tempo, Leverage (:33-52).
  - `seize` lever is DEAD: its consumer (`seizure_score` + `initiative_seize`) cut 2026-06-05, so `vorschlag` and `sen_no_sen` do nothing when equipped (ED-PC-0042) (:55, :178-182). Live levers: `counter_success` (Indes), `counter_select` (mezzo tempo), `anti_overcommit` (true times) (:177).
  - Balance is NOT a stat: `effective_balance = f(Agility) x poise(context) x ability_factor` (Jordan) (:75-87).
  - Chinese Ming manuals are mnemonic shorthand, treat as thin; selection-effect universal warning (:24, :152-153).
- **Conflicts / stale:** the document contradicts itself on `seize` (§2c correction vs table rows, fixed in labels only); contradicts REARCHITECTURE's access-model.
- **Open items:** reopen/disengage lever not built; Balance re-sourcing from Agility queued.

### .designs/systems/combat/combat_engine_v1/reference/combat_balancing_methodology.md
- **What it is:** scene-combat WS-8 methodology doc for balancing combat variables via `workbench/balance.py`.
- **Status:** "Methodology + instrument doc (mechanical-tier; not canon-gated)". Reading: live method; baseline numbers are a 2026-06-28 point-in-time (N=300/cell).
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Analytic vs Monte-Carlo must agree within +/-2pp; `net ~ Normal(mu*pool + soft_cap(net_sigma)*sigma_n, sigma_n)` banded by `core.degree` (:25-32).
  - One-factor-at-a-time, position-swapped, mirror at 50, Wilson 95% CI, parity noise +/-2-3pp at N~3000, acceptance band 0.40-0.60 (`r8.BAND_LO/HI`) (:34-41).
  - Two-pass: weapon-only then attribute-parity; joint not single-knob; contextual balance C1 "no option globally best" (:43-69).
  - Ablation gate: a lever that does not move outcomes beyond noise is cut (proven-inert `seize` precedent) (:71-76).
  - Baseline: weapons reach-dominated (spear 91, rapier 88, staff 84 ... arming 49, dagger 31, mace 28); marginal attribute +1: cog +26, strength +20, agi +20; tradition spread 6.8pp exceeds band; after WS-4 `none` fixed to ~49 but only 2 distinct context leaders, spanish broadly strong, chinese broadly weak (:81-105).
- **Conflicts / stale:** baseline is pre-redesign; `workbench/balance.py` named as live (CLAUDE.md §9 task routing also cites it).
- **Open items:** tradition channel-leverage equalisation (design-laden, "paradigm-strength = Jordan's call") (:105).

### .designs/systems/combat/combat_engine_v1/reference/combat_throughlines_v1.md
- **What it is:** design-spine doc (mechanical-tier) naming the co-primordial throughlines of a combat exchange and the commitment = recovery axis.
- **Status:** "Design-spine doc (mechanical-tier)". Reading: live as intent; formulas need code check.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Exchange converges on two poles hit vs be hit; every throughline adds a term to `net_sigma` -> `degree` -> hit or riposte (:16-20).
  - Throughline table: distance/measure, reach, reading, timing/tempo, balance/structure, technique, weapon morphology, commitment/recovery with engine loci (:22-36).
  - Commitment = recovery: a feint is the minimal-commit pole (`commit 2` already is the feint, so feint dissolved into attack in WS-5) (:44-52).
  - `overcommit_exposure = max(0, COMMIT_EXPOSE_K*(commit-3)*recoverability_factor) - discipline`; recoverability from footwork, PoB x weight (`mass x pob_frac`; forward-heavy mace 1.74x vs hand-balanced rapier 0.95x), stance, grip/extension; measured poleaxe/mace lose ~5pp in duel (:53-63).
- **Conflicts / stale:** formulas (`recoverability_factor`, `COMMIT_EXPOSE_K`) belong to `modules/combat/`; check live names [UNVERIFIED].
- **Open items:** "the same treatment is owed to the others" (other throughlines) (:70).

### .designs/systems/combat/combat_engine_v1/reference/engagement_psychology_recovered.md
- **What it is:** salvage (scene-combat WS-0) of three uncommitted engagement-psychology docs, reconstructed from audit Reconciliation 3.
- **Status:** "Reconstructed-from-audit (mechanical-tier)". Reading: historical/provenance; findings feed WS-5.
- **Bears on:** PC, SC (reading as deliberative game).
- **Content that matters:**
  - Already faithful in engine: legibility (point 0.80 hard to read; cut/blunt 1.25; +commit, +lunge), feint as read contest `read_d` vs `read_a` logistic, overcommit exploit (`read_win and commit>=4 -> Indes/sen steal + overcommit_exposure -> riposte`) (:28-40).
  - Genuine additions: regime-contest lens "The Approach" (biased weights over measure/contact/tempo, NOT a planner), the contact axis clinch/disengage/choke (consumes dead `clinch` weapon field), and Wariness ENG-1 `WARINESS_K*(1-familiarity)` with a mandatory spread-floor so commit distribution {2,3,4,5} cannot collapse (:46-65).
  - Pre-contact `seize` cut 2026-06-05 after ablation ~0; do not revive (:68-69).
- **Conflicts / stale:** the original three source docs never committed (only this salvage exists).
- **Open items:** whether the contact axis was ever built (see phase4_5 plan: not started as of 2026-07-01).

### .designs/systems/combat/combat_engine_v1/reference/phase4_5_plan_v1.md
- **What it is:** verbatim recovery of an uncommitted plan (`perform-an-intensive-plan-jolly-llama.md`, 2026-06-29) for scene-combat Phases 3/4/5, annotated with execution status as of 2026-07-01.
- **Status:** per-phase bracketed status; Phase 3 DONE (PR #40, #47), Phase 4 (4a/4b/4c) and Phase 5 NOT STARTED. Reading: historical plan; many principles are stated here and nowhere else.
- **Bears on:** PC, DICE, SC.
- **Content that matters:**
  - The Primitive Principle (a weapon is a label for an aggregate of primitives; never tune per weapon name), the Attack-Defence Convergence Principle (threat without receiving threat; seizing initiative = convergence), and the Tradition-Is-Not-A-Weight Principle (a tradition = curriculum + selection bias; efficacy = weapon primitives x learned ability x state) (:89-93).
  - Four primitive layers C (9 stats: strength, agi, end, cog, att, spirit, focus, history, disp, each 1-7), W, T, S (:65-71); wrapper contract: pure subsystems, wrapper owns all mutation (:81).
  - Workstream-0 grounding: `sim_verification_ledger.json` and `grounding_ledger.md` never created (:153-155); honest `[ASSERTED]` / `[FIAT]` flags over forced citations (:157-168).
  - Phase 3 fixes: `puncture_pressure` key mismatch; blunt transmission scaled by `p_auth/8` (wooden staff transmitted like a steel mace); `REACH_DECAY_K=0.35` FIAT; `wt` and `spd` still read live in `core.py:55` and `systems.py:46` (:181-206).
  - Phase 4a game-theory layer (Bayesian read, mixed-strategy commit, Stackelberg initiative, struck-line wariness, concentration-lapse error) and 4b/4c unbuilt (:247-283); Phase 5 contact axis unbuilt (:224-236).
  - WS-7 multi-combatant deferred, ED-911, "DESIGN-ONLY" (:73).
- **Conflicts / stale:** Phase 4/5 statuses are 2026-07-01; PC lane must verify against `modules/combat/` (the engine may have moved since) [UNVERIFIED].
- **Open items:** missing grounding ledger files; `wt`/`spd` deletion; `HALFSWORD_HEFT_RELIEF` possibly subsumed by continuous grip-position model.

### .designs/systems/combat/combat_engine_v1/reference/tradition_decomposition_v1.md
- **What it is:** WS-3 bottom-up decomposition of martial traditions (German, Italian, Japanese, Spanish, English, thin Chinese/Filipino) into technique -> primitive -> node -> gate -> access/bias/tendency records.
- **Status:** "Decomposition artifact (mechanical-tier)"; update note 2026-06-29 says WS-4 dissolution landed. Reading: provenance for the tradition model.
- **Bears on:** PC.
- **Content that matters:**
  - Old tradition model was a 7-dim scalar channel-weight vector (e.g. `german tactile=1.35`); measured 18.8pp imposition spread and 6.8pp unconditional spread (none lowest at 45.1) (:21-27).
  - Substrate primitives: measure, tempo, feel/tactile, leverage, perception/visual, precommit, structure/balance; state-graph nodes Approach, AwaitTempo, Exchange{read,commit,mode,roll}, Bind, Riposte, HitLanded (:51-58).
  - Emergent profiles: German fights to the bind, Italian refuses the bind (cavazione), Japanese wins before the blade moves, Spanish owns the approach geometry, English counters at the true time (:79-129).
  - Three identities the scalar vector cannot express: Italian bind-refusal, the contact axis, Spanish footwork-as-geometry (:157-160). Spanish `balance` channel 80% suppressed in-engine; Japanese `precommit` fired only in feint (~30%) (:150-151).
  - Sparse-tradition rule: Chinese one mechanic (burst from reach), Filipino flow, no abilities asserted (:131-138).
- **Conflicts / stale:** scalar numbers superseded by equal-affinity-budget model (2026-06-29).
- **Open items:** contact-axis accesses (clinch/disengage/choke) and `seize` retirement remain open.

