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

### .designs/systems/combat/reference/combat_c4_draft_v0.md
- **What it is:** draft spec (2026-05-17, ED-864) of three scene-combat mechanics added atop a d10 pool baseline: M1 reach/distance gate, M2 stance x stance counter-table, M3 initiative preemption.
- **Status:** "DRAFT — Jordan review pending. Not yet canonical." Reading: superseded; combat moved to the continuous sigma engine (ED-900/904), so the pool grammar, TN-7 and stance counter-table are obsolete. Historical.
- **Bears on:** PC, DICE.
- **Content that matters:**
  - Distance Bands 0-3 (Grappled, Engaged, Spaced, Reach), start Band 2; attack out of reach collapses to `1D + History` (:33-59); Close/Open actions (:62-68).
  - Four stances Pressure/Patience/Decisive/Cautious with simultaneous reveal and a counter-table (Patience vs Decisive imposes -3D; Pressure vs Cautious caps at Partial; Pressure vs Patience denies Take Breath) (:84-107).
  - M3: higher-Initiative fighter, at <=60% HP and gap >=2, once per duel, cancels opponent's action for 2 stam cost / 3 stam penalty (:119-131).
  - Phase 11 sim: Fast (Agi 6) vs Tough-heavy 22.3% under reach gate; reframing 2: each archetype wins in its domain (:139-161).
  - Seven open canonical questions (gate severity, magnitudes, stance count 4 vs 2, grapple, ranged) (:163-181).
- **Conflicts / stale:** the "reach gate" and "stances" concept re-emerges in the live engine as continuous `reach_base`, `measure_gap` and tradition imposition; reading this as current would conflict with CURRENT.md's combat head.
- **Open items:** all seven questions were never answered in this file.

### .designs/systems/combat/reference/combat_currency_v1.md
- **What it is:** currency lineage note (2026-08-14, ED-IN-0189): the narrative formerly in CURRENT.md's personal-combat head row, moved here.
- **Status:** "REFERENCE — currency lineage only; rules nothing, supersedes nothing". Reading: historical lineage, last reading 2026-07-23.
- **Bears on:** PC, DICE, PROCESS.
- **Content that matters:**
  - Live head `systems/combat/combat_engine_v1/` (engine wins on disagreement); typed export `engine/engine_params/combat_engine_v1.json` GENERATED from `config.py` with a blocking round-trip (:21-25, :31).
  - R2 closing-distance/facing/grip/contact redesign (I0-I8) merged PR #72 (2026-07-04); R3 weapon-model consolidation U0..U9 (:31).
  - U9 capstone (ED-PC-0021): no edge/choke/facing lever robustly cleared the ~+/-4pp noise floor, so all six stayed at K=0; then U10 (ED-PC-0022/0023, PR #226, 2026-07-23) activated the six morphology levers at small grounded baselines behind `ability_factor` (:31).
  - Retraction: the earlier "+2.8pp" ability edge was a tradition-membership confound; correct instrument for a situational lever is per-fight texture with outcome preservation (16-28% of fights play differently, ~3-8% flip the winner) (:31).
  - `IMPOSITION_GATE=False` (imposition mechanism retired as fiat, Jordan); governing principle: every build available (not every build good); efficacy from investment, no fiat (:31).
  - Deferred: MAX_TEMPO_PEN 38-weapon flat-top (needs golden regen), PERC_EXP low-mass compression, PERC_TRANSMIT_FLOOR, adef_cap sel_head; JD-2/3/5/6/7/8 open (:31).
- **Conflicts / stale:** a single 3,955-character line, i.e. the paragraph that CURRENT.md was told to stop carrying; check against `modules/combat/` since the head may have moved [UNVERIFIED].
- **Open items:** JD-2/3/5/6/7/8 and ED-PC-0012 (one-handed sabre "point" gap) at time of writing.

### .designs/systems/combat/reference/combat_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `6545067`) of `combat_engine_v1`: `wrapper.fight`/`engagement` beat loop, core resolve/strike, bridge seam.
- **Status:** "REFERENCE — traced structure only". Reading: historical trace; engine path since moved to `modules/combat/`.
- **Bears on:** PC, CORE, DICE.
- **Content that matters:**
  - `fight` multi-bout harness (max_bouts=12, coin-flip aggressor, `UPSET_FLOOR` symmetric upset flip) vs `engagement` per-exchange bout; the intended per-turn game call `engagement` has no outside caller (:51-61, :156).
  - Per-beat flow: reach_base, `measure_gap` closed-band latch, re-presentation gate, cadence `ready` vs `ACT_THRESHOLD`, half-sword auto-switch, `commit_depth`, `read_contest`, `assemble_net_sigma`, INDES steal, `core.resolve(pool, net_sigma, rng, ob)` with `ob_from_defender` (ED-PC-0058 correction), overcommit exposure, outcome mapping by degree x defender mode, displace-and-step-inside, bind sub-loop (beats can advance by 4 per iteration), riposte role flip, contact axis grapple (:63-96).
  - Entire `combat` scene branch of `scene_dispatch` unreachable because `evaluate_triggers` only fires `contest`; `DISPATCH_COMBAT_BRIDGE` default off; deprecated `systems/combat/sim/combat.py` call deleted 2026-09-25 (:106-110, :153-154).
  - `combat_engine_v1` itself never emits/consumes a Key although the contract says so (:152); `capabilities.py` and `state_graph.py` not imported by the live spine (:155).
  - `engage` contact axis (`contact.grab_available`, `grab_outcome`: disarm/throw/pin/foot_pin/control) exists in the traced code (:93), unlike the plan documents.
- **Conflicts / stale:** the contact axis here exists, contradicting phase4_5_plan_v1's "Phase 5 NOT STARTED" (later than 2026-07-01); `resolve(pool, net_sigma, rng, ob)` signature [UNVERIFIED current].
- **Open items:** whether the season loop now dispatches personal combat at all (PC/CORE audit).

### .designs/systems/combat/reference/combat_reference_v1.md
- **What it is:** consolidation (2026-08-08, ED-PC-0056) of `combat_v30`, `combat_design_v1`, `combat_v30_infill` into one design-layer reference for personal combat (13 sections).
- **Status:** "REFERENCE — subordinate to the `combat_engine_v1/` head (PROPOSED, ED-PC-0056)"; "Where this prose and the engine disagree, the engine wins." Reading: mixed; much of it is a pre-d+sigma d10 TTRPG rule set that the engine superseded, but several world-bridge tables (§13) and surrender/disengage (§11.4) exist nowhere else.
- **Bears on:** PC, FA, SE, FI, WR, MB.
- **Content that matters:**
  - Pool `max(5, Relevant History + 6)`, Agility-independent (RATIFIED R1) (:62); wounds are a fractional Ob (+0.15 attacking / +0.25 defending per wound, ED-1041/ED-PC-0005) not a pool cut (:66, :366); wound penalty to Thread ops +0.15 Ob each (:518, :527).
  - Damage = Impact x Coupling x Quality (Partial 0.6 / Success 1.0 / Overwhelming 1.5), Impact = Strength + Heft additive (:221-228); weapon-vs-armour table kept as relationship reference (:233-238).
  - Health `(End+6) x (MaxWounds+1)`, Wound Interval `End+6`, Max Wounds `floor(End/2)+1` (range 14-65) (:353-364); Stamina `End x 5` (:371).
  - "All weapons are TN7 now" Jordan 2026-08-15; the engine never had per-weapon TN (:410). TN 6/7/8 = Controlled/Standard/Desperate is a situational mode, not a weapon property (:410).
  - §11.4 Surrender and Disengage (Yield accept/refuse; Disengage Agility contest) is the only definition of "surrender" which §13.1's echo table consumes (:28-36, :587-603).
  - §13 world bridge: Combat Domain Echo (officer defeated: acting faction stat +1, target Stability -1; killed adds Mandate -1), Combat Reputation 0..6+ effects and decay -1/yr, settlement consequences (public combat Order -1, vs governor Order -2), Death Cascade (Knot rupture, Disposition -3, Scene Slate P1 entries, Exposure +2 per territory, player Conviction revision) (:652-710).
  - Ranged, cover, terrain, group combat (Fibonacci group bonus +0..+5), Rescue (PP-290/292), stress-FF PP-720, B-mode presentation flag PP-721 (:204-315, :384-466).
- **Conflicts / stale:** the d10 pool, TN matrix, Feint versus roll, resolution-order action table and Strike/Feint/Disarm/Tie Up set are pre-engine; §7 says Health formula "see derived_stats_v30 §4.1" while §366 overrides it (ED-PC-0005); "GM" language throughout; mode-split text kept as historical rationale per its own note (:15).
- **Open items:** pending editorial ED-033 (Commander bonus formula conflict), ED-040 (Artillery Balanced disposition lock), P2-B11-19 (Thread Tension 80+ in mass battle) (:642-644); ED-131 weapon modifier values need playtest (:240).

### .designs/systems/factions/reference/baralta_crown_claim_v30.md
- **What it is:** BG mechanic design (2026-04-11, ED-408..411, PP-661): Crown Succession Contest, Baralta claim, Consecration Crisis, Hafenmark after Baralta takes Crown, three-clock interaction. Skeleton; prose in `_infill`.
- **Status:** "DESIGN (editorial decision, flagged for review)". Reading: historical; depends on Coup Counter, Torben Loyalty, Löwenritter Autonomy clocks, many of which the conflict proposal replaced.
- **Bears on:** FA, CHAR, WR.
- **Content that matters:**
  - Trigger: Crown eliminated (Mandate 0 + Loyalty 0) or Royal Deposition succeeds; claimants need Mandate >= 3 (Löwenritter Autonomy >= 3; Hafenmark Baralta alive + Mandate >= 4; Church CI >= 40), each rolls pool vs Ob 3 TN 7, ties: Löwenritter military, Hafenmark political (:29-52).
  - Baralta Claim Precondition: Crown Mandate <= 2 AND PI >= 5 AND Baralta alive; pool Hafenmark Mandate + Influence; Ob Crown Mandate + 1; +2D on contest if positioned; failure Stability -1, 2-season lockout (:54-64).
  - Consecration Crisis: Church Stability >= 4 refuses (CI +3, Crown Mandate inherited at -2, 3-season validation window else contest reopens); Stability <= 3 consecrates under duress (CI -5, Church Stability -3) (:70-91).
  - Option B: Hafenmark persists under institutional successor if PI >= 4, else fractures (:131-135); Hafenmark-to-Crown recognition ceremony Standing 7 -> Crown Std 5 (:137).
  - Three-clock table (Generational Shift x Löwenritter Autonomy x IP): Crown Stability <= 1 increments Counter automatically; IP >= 60 lowers Torben alignment threshold 3 -> 4; sequencing: Succession first, Autonomy second, IP last (:160-212).
- **Conflicts / stale:** Coup Counter replaced by graduated autonomy (conflict proposal); Option A/B tension with the FA lane's emergent-faction ruling (starting factions = 4); Arc 11 "GM discretion" (:91).
- **Open items:** ED-647 Recognition Ceremony formalization pending (:141).

### .designs/systems/factions/reference/baralta_crown_claim_v30_infill.md
- **What it is:** prose/rationale infill for the Baralta Crown Claim doc.
- **Status:** "DESIGN (editorial decision, flagged for review)". Reading: historical.
- **Bears on:** FA, WR.
- **Content that matters:**
  - Trigger text (infill only): "Ehrenwall Coup fires AND Ehrenwall does not claim the Crown for Löwenritter directly" (:21-23), a different trigger from the skeleton's elimination/deposition — a conflict inside the part-set.
  - Stake Claim = Senator Outward targeting Crown; places a Claim Token (+2D on contest, makes Baralta a succession option in Ehrenwall's Coup assessment, alerts Church) (:25-29).
  - Strategic sweet spot: weaken Church to Stability 3 before claiming; creates tension with Baralta's TC (now CI) suppression interest (:44).
  - Four conditions for a viable claim: Crown Mandate <= 2, PI >= 5, Church Stability <= 3, Hafenmark PI >= 4 (:47).
  - Early-game unconsecrated claim is "a trap"; late-game is "a gamble" (:37, :42).
- **Conflicts / stale:** skeleton vs infill trigger disagreement; "TC" is the retired name for CI.
- **Open items:** none beyond skeleton.

### .designs/systems/factions/reference/ci_political_v30.md
- **What it is:** CI (Church Influence) political legitimacy redesign, stat economy and card system, v1.0 (2026-04-14); skeleton, companion infill named `tc_political_redesign_v30_infill.md`.
- **Status:** "CANONICAL — approved 2026-04-17 (editorial batch acceptance)"; §2.2 victory clause "SUPERSEDED-BY: GD-1 2026-05-30". Reading: partly live intent (CI mechanics, stat change tables, card cooldowns); several pieces superseded by the d+sigma resolver and strain doc.
- **Bears on:** FA, SE, WR, SC, DICE.
- **Content that matters:**
  - CI runs 0-100, no freeze; milestones 28 start, 40 Assertive (+1D Assert/Seizure), 55 Institutional Reach, 65 Dominant, 80 Ascendant (Seizure Ob -1, PT drift), 100 Theocracy Unification; seasonal cap +/-5, +/-3 from player Domain Actions (:84-113).
  - Mass Seizure one-shot, Ob = 10 - PT - infrastructure (floor 1), available from CI >= 60, probability per season `P = ((CI-60)/40)^3.3` (1% at 70, 10% at 80, 39% at 90, 100% at 100) (:95, :423). Contradicts conviction_track Ob `2 + Fort + max(0, 3-PT)`.
  - Spiritual Weight (SW) fixed per territory, total 32 (T9 = 5, T8/T14 = 3, T15 = 0) (:46-65); Piety Yield = sum(PT tier x SW/5) (:69).
  - CI institutional weight `floor(CI/20)` as +votes in Parliament tally or +margin M in resolver (not dice); opponent vote contribution `max(0, Mandate - floor(CI/30))`, floored at 0 (:129-179) — ED-865/874 consistency.
  - Stat change paths per stat; Govern/Trade resolve through d+sigma resolver with `M = Stat - difficulty`, `difficulty = max(1, (Ob-1)*2)`, `Ob = floor(Prosperity/2)+1` (:229, :242); degree tables (:230-249).
  - Strain/Turmoil bands 0-2/3-4/5-6/7-8/9-10 effects on Mandate checks, Accord; Battle -> MS -1; "Battle -> IP +2" struck by ED-743, IP now from Accord-threshold territory counts (:252-265).
  - Card hands, domain expertise, Card->action mapping, Cooldown Track (Pontifex/Prefect/Colonist 2 seasons, Recess 0) (:271-323); AI posture priority stack EXISTENTIAL/DEFEND/CONSOLIDATE/COUNTER-THREAT/EXPAND/OPPORTUNISTIC (:331-349).
  - T9 contributes to CI cap like any territory (ED-721 Option A) (:386).
- **Conflicts / stale:** Starting Accord "capitals = 3" (:429) vs canonical_registry "capitals = 4"; §7.1 and §7.8 still say bonus dice; Church victory sub-requirement CI >= 65 moot after GD-1; Piety Yield formula differs from conviction_track Conviction Yield (both claim CANONICAL) — a two-ladders defect.
- **Open items:** none flagged here beyond resolved ED-NEW-CI-10/11.

### .designs/systems/factions/reference/ci_political_v30_index.md
- **What it is:** generated heading/size index (2026-04-20) of the CI political doc (~5.8k tokens); older heading labels.
- **Status:** none stated. Reading: historical; body is `ci_political_v30.md`.
- **Bears on:** FA.
- **Content that matters:**
  - Pre-ED-865 heading "§3.2 CI Bonus Dice (Church in Political Forums)" (:34) vs body "CI Institutional Weight": shows the rename away from dice.
  - §7.5 titled "Battle -> RS and IP" (RS = old name of MS) (:54).
  - Section sizes show §3 (880) and §7 audit-of-changes (1,044) as the heaviest rule sections.
- **Conflicts / stale:** heading terms (RS, bonus dice) lag the body.
- **Open items:** none.

### .designs/systems/factions/reference/faction_politics_v30_index.md
- **What it is:** generated heading/size index (2026-04-20) of `faction_politics_v30.md` "Faction Politics Patch Register (EXPANDED)" PP-660 (~37k tokens; body absent from `.designs/systems/factions`).
- **Status:** indexed doc "CANONICAL (approved Jordan 2026-04-17, commit PP-660)" (:25). Reading: historical map of a large rank-ladder spec; the body is the largest FA design doc and is not in this lane's files.
- **Bears on:** FA, CHAR, SE.
- **Content that matters:**
  - Standing 0-7 rank ladders for Crown, Hafenmark, Varfell, Church (PART 1, 14.8k tokens), each with specialty branches at Standing 3 and a named inner circle (:32-52).
  - Sub-office ladders: Löwenritter, Riskbreaker (Shadow Renown 0-10, Deniability Debt 0-7 cap 7), Inquisitor, Templar, Guild (Hafenmark-integrated + independent), Niflhel per arm, Warden of the Thread (:53-70).
  - Caste integration (Standing advancement gating, Renown, Initiation Duty, inner-circle Disposition floor, Conviction Scar risk) (:71-77).
  - Part 4 naming reconciliation: a "Solmund naming violation — IMMEDIATE FIX" (:79), CV/PT/SW dissolution, T15 Southernmost vs Askeheim, Varfell vs peninsula naming.
  - Parts 5-9: TC x rank, Baralta Crown Claim x ladder (Outcomes A/B/C, Recognition Ceremony ED-647), Ministry expansion (Crown ministries, Hafenmark committees, Church dicasteries, Varfell councils), Generational Shift fix with Torben Readiness track, cross-faction parity table (:88-111).
- **Conflicts / stale:** this index uses TC terminology; "Skyrim integration" progression pattern is a design referent. The ladder body is cited by the governance_consolidation doc (§1.0b-d).
- **Open items:** ED-634..ED-658 editorial items; the body must be read in `designs/provincial/faction_politics_v30.md` [UNVERIFIED present].

### .designs/systems/factions/reference/faction_succession_split_v30.md
- **What it is:** generalized faction succession contest and split mechanics (PP-666, 2026-04-19; FSS-1 2026-05-30 amendment), plus RM settlement emergence.
- **Status:** "## Status: CANONICAL" and "PROVISIONAL — approved mechanical design 2026-04-19 (PP-666)" in one file (:11-13, ED-712 smoke-test pending). Reading: live design intent for FA; contradictory status line; resolution rewritten for the d+sigma resolver.
- **Bears on:** FA, SE, WR, CHAR.
- **Content that matters:**
  - Trigger matrix: leader eliminated (killed, captured without ransom in 2 seasons, deposed, incapacitated) opens a contest unless a sole heir has Disposition >= +3 AND Standing >= 4; multiple comparable claimants always contest (:32-42).
  - Claim bases: Inner Circle rank (Standing >= 3), blood claim, institutional claim, external backing (costs Diplomatic Token); contender strength deterministic per type (Blood: Mandate + Influence; Institutional: Influence + faction stat Crown=Mandate, Hafenmark/Church=Influence, Varfell=Intelligence; External: backer Influence + own Standing) (:46-58).
  - Two-stage resolution: Stage 1 who leads via resolver `M = strength(top1) - strength(top2)`; Stage 2 whether it splits via deterministic gap G: G>=3 unified, G=2 unified fractious (runner-up Disposition >=0 accepts else splits), G<=1 split; dice tails flip only Failure/Overwhelming (:60-85). Rationale: fragmentation tracks power balance (Carolingian divisio, Diadochi) not dice variance (:67).
  - Split asset division: Mandate/Influence 60/40, Wealth 70/30, units by Loyalty check `Commander Disposition + unit Discipline`, winner Stability -1, splinter Stability 2 (:91-101).
  - RM Settlement Emergence: Order = 0 (hard threshold) AND PT <=1 AND local Disposition toward Yrsa Vossen >= +3; at most once per province per 4 seasons (:160-162).
  - Worked example: Varfell after Vaynard (:119-146) still shows pre-FSS d10 rolls then restates under FSS-1.
- **Conflicts / stale:** "Intelligence" stat (struck per canonical_registry) used as Varfell's rank stat (:57); example's d10 rolls (:131-134) contradict FSS-1; Order=0 thresholds duplicated in session_a_spec_patches Patch 4. Subsumes `baralta_crown_claim` (:179).
- **Open items:** player-led contender mechanics deferred; simultaneous succession order (descending pre-loss Mandate); RM 4-season cooldown balance flagged for smoke-test (:176-178).

### .designs/systems/factions/reference/faction_succession_split_v30_index.md
- **What it is:** generated heading/size index (2026-04-19) of the succession-split doc (~2.7k tokens).
- **Status:** none stated. Reading: historical index.
- **Bears on:** FA.
- **Content that matters:**
  - Section map matches the body: §2 contest framework is the heaviest (1,210 tokens), worked example §3 (454), RM emergence §4 (353) (:40-51).
- **Conflicts / stale:** line numbers predate FSS-1 amendment so section lengths are stale.
- **Open items:** none.

### .designs/systems/factions/reference/faction_systems_overview_v30.md
- **What it is:** single-pane catalog (2026-05-17, Pass 2 follow-up) of every faction-related system, mechanic, action and GD constraint; points at canon rather than duplicating.
- **Status:** "REFERENCE — Pass 2 follow-up 2026-05-17"; self-declares same-chat authorship bias (:310). Reading: historical map of FA surface area and a roster of what was BLOCKED/placeholder.
- **Bears on:** FA, CORE, WR, SC, CHAR.
- **Content that matters:**
  - Six layers L1 primitives, L2 identity, L3 faction action, L4 inter-faction resolution, L5 faction-emergent, L6 peninsular accounting (:25-45).
  - Parliamentary status flag: Parliamentary / Extra-parliamentary / Non-parliamentary (insurgency) (:57-65).
  - GD-1 sole victory = Peninsular Sovereignty (11+ territories sustained 2 seasons, treaties counting); GD-2 mandatory threat response when Accord below threshold; GD-3 insurgency/promoted-faction status gates (:247-249). Promoted factions eligible to win (:210).
  - Action rosters: universal 4 (govern, muster, military_conquest, parliamentary_transfer), Crown 4, Church 6, Hafenmark 3, Varfell 2 (both placeholder-named, e.g. `varfell_mandate_action` "mechanism broken ... double-cost asymmetry") (:89-134).
  - Parliamentary Transfer: 4 modes (Adversarial/Consensual/Punishment/Appeasement) x 8 CB sources (Adjacent Instability, Treaty Violation, Excommunication-current, Building Desecration, Crown Diktat, Combined-Standing, Scar Accumulation, RM pressure) (:158, :185-193).
  - Treaty expiration 90-95%/arc lapse; "13-step cascade" at accounting with 9 faction-relevant steps listed (:173, :229-239).
  - Mass Seizure has 3-source drift (conviction_track PP-411 / ci_political 7.6 / victory 3.2) (:116, :177). ~25 of 31 Pass 2 forward flags on faction surface (:287).
- **Conflicts / stale:** `sim/autoload/npc_ai.py`, `sim/world/restoration_movement.py` paths dissolved; the audit-pending items ("Conviction values contamination") unresolved. ~35 READY / ~8 placeholder / ~7 blocked count is a doc-derived snapshot.
- **Open items:** Pass 2d/e/f canon authoring for Church infrastructure reclamation, home sanctuary T9, Hafenmark equipment, Varfell mandate action; NPC AI priority stack audit.

### .designs/systems/factions/reference/factions_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `6545067`) of `systems/factions/sim/` (16 modules): `faction_take_action` dispatch, parliamentary scene bridge, territory transfer.
- **Status:** "REFERENCE — traced structure only". Reading: historical; useful as a census of FA dead/stub code and doc-vs-code divergences as of Sep 2026 (module paths may have moved to `modules/`/`engine/season/`) [UNVERIFIED].
- **Bears on:** FA, CORE, SC, MB.
- **Content that matters:**
  - `faction_take_action`: RNG-free signals (conquest targets/mil-advantage, undergoverned share, threat) re-weight four base weights BASE_W_UNIQUE/CONQUEST/MUSTER/GOVERN, then ONE `rng.random()` draw against cumulative thresholds; the three `if roll < cum_X` blocks are independent, so a sentinel `_NOOP` falls through to an unconditional `_try_govern` (:72-91, :192).
  - The claimed "GD-2 mandatory threat response before stochastic selection" is false in code: no unconditional mandatory pass (:184). `CONQUEST_MIN_MIL` gate deleted 2026-08-14 by Jordan ruling (:59, :84).
  - Faction-unique actions: only Crown (`crown_initiative.select_initiative_mode`, 3 modes) and Church (priority chain Excommunication -> Council -> Absolution); Varfell and Hafenmark have none and fall to Parliamentary Censure (:79-80, :185).
  - 6 of 16 modules are `stubwire` stubs (`charter_liberties`, `hafenmark_equipment`, `home_sanctuary`, `infrastructure_reclamation`, `varfell_mandate_action`, `varfell_territorial_acquisition`); `mass_seizure.py` (full implementation) and `treaty.process_treaty_expirations`/`register_treaty` have zero production callers; `propose_treaty` is a silent no-op contrary to its docstring (:31-42, :186-187).
  - `world.casus_belli` has zero production writers so every non-Crown CB source in `parliamentary_transfer` is unreachable in a fresh campaign (:191); `Territory.entry_terms_l_seed` is a write-only dynamic attribute (:190); `faction_state` resolver half (`cascade_resolution`/`mission_shift`) unimplemented (:183).
  - Parliament scene: proposer = lowest-Stability eligible faction, establishment = highest-Mandate; vote -> Domain Echo degree; independent CB-gated Territory Transfer motion with sequential gates (mode, GD-3 non-parliamentary, unheld target, self-transfer, last-territory floor, per-arc frequency) and Failure effects by mode (:99-117).
  - Conquest resolves through `resolve_mass_battle` with a permanent placeholder terrain (:85, :197); `faction_action` is the subsystem's sole cut-vertex (:194); `faction_take_action` return string discarded by caller (:189).
- **Conflicts / stale:** the retired Key emission (`scene.battle_concluded`, `da.public_governance`) is log-only and has no subscriber (:188). Whether `engine/season/` supersedes `faction_action` entirely is the FA lane's question.
- **Open items:** `coronation_renewal_prereq` docstring promises a check the body does not implement (:196).

### .designs/systems/factions/reference/factions_personal_v30_index.md
- **What it is:** generated heading/size index (2026-04-20) of "PART EIGHT: FACTIONS" of `factions_personal_v30.md` (~7.1k tokens, body absent here).
- **Status:** none stated. Reading: historical index.
- **Bears on:** FA, CHAR.
- **Content that matters:**
  - Faction roster: 8 factions listed (Crown, Church, Hafenmark, Varfell, Guilds, Niflhel DISSOLVED, People's Revolution/Restoration Movement, Löwenritter) plus Ministry of the Peninsula (Throughline T4) and Schoenland spoiler (:31-41).
  - Faction stats 6-stat 1-7 scale with Starting Values, Domain Actions, Ethical Framework Modifiers, Nine Political Axes (:25-30).
  - 8.11 Parliamentary Vote and 8.12 Seasonal Accounting - Faction Phase (:42-43).
- **Conflicts / stale:** "6-stat" (includes Intel) vs the struck Intel stat in canonical_registry; Niflhel entry already DISSOLVED here.
- **Open items:** none.

### .designs/systems/factions/reference/fail_forward_pp177.md
- **What it is:** working design (2026-04-02, PP-177) of Fail Forward for board-game Domain Actions: Partial = goal + complication, Failure = no goal + complication.
- **Status:** "WORKING DESIGN — not yet committed". Reading: historical/unclear; pre-resolver degree vocabulary; whether the engine applies complications is [UNVERIFIED].
- **Bears on:** FA, CORE, DICE.
- **Content that matters:**
  - Complication must be immediate, legible without GM, state-changing, proportionate (:29); tiers Minor (Standing -1 or Public Instability +1, acting faction's choice, for Partial), Moderate (mandatory per action type, for Failure), Severe (Moderate + Stability -1, Failure on Ob >= 4 only) (:39-43).
  - Per-action complication table for Govern, Trade, Muster, Diplomacy (Failure: target gains Casus Belli), Decree, Parliamentary Manoeuvre, Investigate, Spy, Thread Operation (Thread Debt token + MS -2), Community Organising, Fortify, Parliamentary Vote (:51-65).
  - Parliamentary Manoeuvre degrees: OW delays one pending DA 1 season + opponent Stability -1; Failure Mandate -1 + opponent Standing +1 (:80-85).
  - Canon compliance claims P-07, P-08 (no null-outcome loops), P-11, P-01, P-12 (:101-107); cognitive load +0.5/10 (:120).
- **Conflicts / stale:** "Standing -1" and "Public Instability" terminology (Public Instability struck per canonical_registry); only the Partial choice exists for player-acting factions; NPC factions' choice rule unspecified.
- **Open items:** none stated; "GM notes one datum as unreliable" (:59) has no engine analogue.

### .designs/systems/factions/reference/fractional_province_ownership_v30.md
- **What it is:** split-province mechanic (PP-666, 2026-04-19): province becomes fractional when a non-Seat settlement is held by another faction; PV share, Greater/Lesser naming, consolidation, fragmentation check, secession.
- **Status:** both "## Status: CANONICAL" and "PROVISIONAL — approved mechanical design 2026-04-19" (:11-13, ED-711 smoke-test pending). Reading: superseded on its core premise by the ruled settlement->territory->province hierarchy (province forms only while territories share a faction holder; `scale_hierarchy_v1.md` overrules PP-726 fracturing).
- **Bears on:** SE, FA, MB.
- **Content that matters:**
  - Trigger: >=1 settlement held by a non-nominal faction AND the Seat not held by that faction (:31-37). Settlement PV share = `(settlement Prosperity / sum province Prosperities) x province base PV`; zero-denominator guard FRAC-01 equal split, Accord forced 0 (:44-50).
  - Consolidation: faction holding >=75% of PV share can declare; cost Influence pool vs `Ob = remaining non-faction PV x 2` (round up); targets Submit (Order -2) or Resist (siege next season; default Resist) (:70-83).
  - Fragmentation Check each Accounting: pool Seat-holder Influence vs `Ob = 2 + non-Seat settlements`; Overwhelming holds 4 seasons, Partial drops a non-Seat settlement's Order -1, Failure allows Secession (candidates limited to national-faction-held settlements; subnational/Uncontrolled excluded) (:101-114).
  - Effects: Domain Actions by Seat holder at province level only; armies move along settlement adjacency graph; Casus Belli at settlement scope (:89-97, :159).
- **Conflicts / stale:** province-fracturing rule PP-726 overruled; PV-share rounding 2-decimal vs integer open (:157); "5d10 vs Ob 3" example is pre-resolver.
- **Open items:** PV rounding; Casus Belli scope; "Multiple non-Seat controllers" RESOLVED additive (FRAC-03) (:158).

### .designs/systems/factions/reference/fractional_province_ownership_v30_index.md
- **What it is:** generated heading/size index (2026-04-19) of the fractional province doc (~2.2k tokens).
- **Status:** none stated. Reading: historical index.
- **Bears on:** SE, FA.
- **Content that matters:**
  - Section map identical to body: §2 (1,380 tokens) holds six subsections trigger, PV, naming, consolidation, effects, fragmentation (:42-48).
- **Conflicts / stale:** none beyond body.
- **Open items:** none.

### .designs/systems/factions/reference/franchise_v30.md
- **What it is:** design (2026-05-04) of Franchise, a per-territory parliamentary weight 0-5, with Territory Influence and a Franchise-weighted National Influence replacing the scalar Influence stat.
- **Status:** "DRAFT — awaiting Jordan review". Reading: unclear/proposed; code relevance unknown [UNVERIFIED whether `franchise` exists in engine/season state].
- **Bears on:** FA, SE, CHAR, WR.
- **Content that matters:**
  - Franchise starting values per territory (Valorsplatz/Kronmark/Himmelenger 5, Gransol/Ehrenfeld/Lowenskyst 4, ... Halvardshelm/Oastad 1, Askeheim/Schoenland 0); sum 47: Crown 23 (49%), Hafenmark 13, Varfell 6, Church 5 (:40-60).
  - `territory_influence = controller(+2) + infrastructure_count (0-3) + npc_presence (+1) + governor_bonus (+1)`, clamp 7; Church parish exception counts as infrastructure everywhere (:70-80).
  - `national_influence = clamp(round(Sum(TI x franchise)/Sum(franchise)), 1, 7)`, recomputed at Accounting; used wherever Influence is a roll pool (:102-115).
  - Design consequence: Church reach without proportional political power (~3-4 vs old I=6); Varfell structurally muted (caste expression at strategic layer) (:117-125, :150-162).
  - Shift triggers +/-1 (4+ stable seasons, Accord 0, Seizure, Löwenritter coup, PI <= 2 freezes all, caste reform hook); floor 1 for represented territories (:133-146).
  - Godot sketch: `TerritoryData.franchise`, `compute_national_influence` (:166-201).
- **Conflicts / stale:** Church stat discrepancy BLOCKING (stats_1_7_scale L=5/PS=5/W=5 vs VDL L=4/PS=4/W=3) (:213); "caste reform event (TBD — hooks system)" unspecified (:211).
- **Open items:** NPC location data for the starting TI table, per-territory Church parish data, non-playable factions TI, caste reform hook (:207-213).

### .designs/systems/factions/reference/parliamentary_transfer_v30.md
- **What it is:** canonical spec (Pass 2h, 2026-05-17) of Parliamentary Territory Transfer: pool, Ob, four modes, eight CB sources, vote-contest wrapping, balance validation.
- **Status:** "CANONICAL — Pass 2h authoring 2026-05-17" with PROVISIONAL derivation choices; code module `systems/factions/sim/parliamentary_transfer.py` exists (see factions flow skeleton). Reading: live design intent behind code; the closest doc-to-code pair in the set.
- **Bears on:** FA, SC, SE.
- **Content that matters:**
  - Frequency 1 per arc per faction; Pool = proposer Influence; `Ob = holder Legitimacy + PARL_MAJORITY_OB_BONUS` (default 2); needs a Casus Belli; CB consumed on use (:34-40).
  - Outcome: OW holder L -1 + territory transfers with Accord 1; Success transfer; Partial no transfer, proposer gains CB; Failure proposer Stability -1, holder L +1 (:44-49).
  - Protections: last-territory block, GD-3 extra-parliamentary block, self-transfer block (:52-54).
  - Four modes Adversarial/Consensual/Punishment (no holder L+1 but holder Standing -1)/Appeasement (+2 Accord); CB sources: Crown restoration (Crown territories < 6), adjacent instability (Accord <= 1), Einhir Revival Partial, prior-Transfer Partial, Military Conquest, treaty-violation, excommunication-related, Scar accumulation (>=3) (:62-86).
  - Resolution wrapped in a Parliamentary Vote contest: majority bloc favouring proposer +1D, favouring holder -1D (:100-103); Parliamentary Stay (ED-631) may suspend (:106).
  - v12c N=1000 validation: Crown 24.7 / Church 28.6 / Hafenmark 24.2 / Varfell 22.5; fires ~2-4 times per campaign; Crown initiates ~60%; modes 75/15/5/5; PARL_MAJORITY_OB_BONUS sensitivity (:116-131).
- **Conflicts / stale:** "sim/provincial/parliamentary_transfer.py is a Pass 2l armature stub" (:139) vs the flow skeleton showing a real implementation; `world.casus_belli` has no production writer so most CB sources are unreachable in code (flow skeleton :191); pool-dice terminology vs d+sigma resolver.
- **Open items:** PARL-MODE-DRIFT-001, PARL-VOTE-MODIFIER-001, PARL-PROTECTION-001 awaiting Jordan (:171-173).

### .designs/systems/factions/reference/political_dynamics_keys_migration_v30.md
- **What it is:** PP-687 Phase B Stage 1 spec (2026-05-01): per-procedure deltas to migrate the NPC "doc 12" political-dynamics procedures (B Concern generation/resolution, DA Proposal Phase, C Project advancement, D Opinion Drift, E Off-Screen Interactions) onto the Key substrate. Anchored to line numbers of an audit doc `12_development_specification.md` (not in this tree).
- **Status:** header "PROVISIONAL" and body "## Status: CANONICAL". Reading: retired with the Key substrate; its value is the NPC-dynamics procedure list (the origin of NPC memory/opinion/concern logic).
- **Bears on:** CHAR (NPC decision layer), FA, WR, CORE.
- **Content that matters:**
  - Per-NPC data model: Concerns, Projects, Opinions, Memories, Knowledge, armature position; Real-Time Mood; 10-memory cap becomes 10 MemoryReferences (:41-81).
  - Procedure B generation reads Memory Query with axis-relevance cosine >= 0.3 over `armature_position_personal`; concern regeneration cooldown (PATCH 3.1) (:89-121); resolution emits `state.concern_resolved`; strong contradiction emits `state.belief_revised` and generates a scar (:148-165).
  - Procedure C: stall >= 8 seasons fails a project; progress >= 10 completes; supporters/obstructors get +/-0.5 affect relationship-tagged memory at salience 4 (:211-267). Procedure D: opinion revision emitted when |affect_axis change| >= 0.5 or confidence changes, causes[] wired (:291-312); scene_outcome drift (victor respect/fear) unspecified magnitude, STUB (:325-336).
  - Procedure E: ambient inner-circle interaction, base_prob, Distant Contact 10% cross-faction, gossip when cumulative_drift > 0.5 (:346-433).
  - Accounting sequence B -> DA Proposal Phase -> C -> D -> E; NPC.id ascending tiebreak (:536-576). Estimated 1.5-2 sessions for Godot (:625).
- **Conflicts / stale:** all emission/Key apparatus retired; "Knowledge" kept outside Keys; unspecified drift magnitudes; the engine-facing equivalent of Procedures B-E in `engine/season/` (NPC decision layer) should be compared in the CHAR audit [UNVERIFIED].
- **Open items:** drift magnitude/curve for scene outcomes (ED-936); Articulation Tier 2 calibration of the new Class B types.

### .designs/systems/factions/reference/treaty_expiration_v30.md
- **What it is:** Treaty Expiration mechanic (Pass 2h canonization, 2026-05-17): per-Treaty independent arc-boundary lapse roll at 90-95%, Senator Outward re-binding, treaty violation.
- **Status:** "CANONICAL — Pass 2h authoring 2026-05-17" with PROVISIONAL violation and active-maintenance alternative. Reading: live design intent behind `treaty.py` (whose expiration functions have zero production callers).
- **Bears on:** FA, WR.
- **Content that matters:**
  - Arc boundary (every 4 seasons) each active Crown Treaty rolls uniform [0,1) against `TREATY_LAPSE_RATE` in [0.90, 0.95] (default 0.90); lapse generates no CB, no Standing delta; independent per Treaty and memoryless (:31-60).
  - Re-binding via Senator Outward (Crown, 1/season, Wealth -2, Pool Influence + Standing modifier, Ob = target Stability): OW treaty + target Standing +1; Success treaty; Partial CB-blocking 1 arc; Failure Standing -1 (:66-80). 3 Treaties = 3 season-actions per arc of maintenance (:82).
  - Violation (attack, support external CB, Parliamentary Transfer) voids treaty, wronged party gains CB, violator Standing -2, wronged +1 (:90-103).
  - "Primary Crown-nerf lever": without it Crown wins 55-90%; with it 24.7%; lapse values 0.90/0.92/0.95 statistically equivalent (:13, :117-152).
  - Narrative extreme noted; active-maintenance alternative (v12c §8.3) deferred (:130-134).
- **Conflicts / stale:** "sim/provincial/treaty.py is a Pass 2l armature stub" (:160) vs a later implemented `process_treaty_expirations` that no production code calls (factions flow skeleton :186); the lapse is a pure balance lever — a mechanism with a purpose (nerf Crown) rather than a simulated cause.
- **Open items:** TREATY-VIOLATION-001, TREATY-NARRATIVE-001, TREATY-MEMORYLESS-001 (:191-193).

### .designs/systems/factions/reference/varfell_path_b_v30.md
- **What it is:** ED-311 proposal (2026-04-06) to reduce Varfell's "Path B Southernmost Dominion" victory from 7 conditions to 3-5, with a Warden Recognition (WR) track.
- **Status:** "[SUPERSEDED-BY: GD-1]" banner: peninsula-only victory strikes the path absolutely; VTM struck 2026-04-19. Reading: dead (victory path removed); historical only.
- **Bears on:** FA, WR.
- **Content that matters:**
  - Original 7 conditions: TCV >= 8, control T4, garrison/Tribune in T15, VTM >= 3 (struck PP-663), WC >= 1, WA >= +1, T4 CV <= 1 (:34-45).
  - Option A: TCV >= 8, control T4 AND T13, WR >= 3 (WR track 0-4; WR 4 = Edeyja substantive contact) (:51-66); Option B keeps WA/WC; Option C minimal 3 conditions WR >= 2 (:75-96).
  - Records the decision that Vaynard is "a military conqueror (Reinhardt von Lohengramm parallel)"; Thread/RM is political constituency not a force multiplier; VTM and Cultural Reformation struck (:20-26).
- **Conflicts / stale:** victory path struck; VTM referenced elsewhere (canonical_registry, conviction_track) is struck.
- **Open items:** none live.

### .designs/systems/factions/reference/varfell_path_b_v30_infill.md
- **What it is:** prose infill for the Path B redesign proposal.
- **Status:** "ED-311 | Status: AWAITING USER REVIEW". Reading: dead (path struck by GD-1).
- **Bears on:** FA.
- **Content that matters:**
  - WR advances with successful Expedition seasons; decreases on RM emergence (WR -2) and on neglecting T15 for 3+ seasons (WR -1); blocked permanently if WR falls to 0 after passing 1 (:19-21).
  - T4 CV <= 1 dropped as perverse micro-management ("narrative truth should not require mechanical maintenance") (:22).
  - Win probability unchanged by simplification (:29).
- **Conflicts / stale:** as above.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_bg_v30.md
- **What it is:** fieldwork spec §8 Board Game Mode (v1.1, PP-630): Survey action and mapping of fieldwork activities onto existing BG actions. Skeleton; prose in `_infill`.
- **Status:** "DESIGN — canonical subsystem file". Reading: historical (BG mode formally discarded per videogame mode spec).
- **Bears on:** FI, FA, SE.
- **Content that matters:**
  - Survey = Consul Inward variant, Pool Influence, `Ob = (5 - Proximity Rating) + 1`, min 1 (Askeheim Ob 6, Lowenskyst Ob 1); Success reveals one undiscovered POI giving a territory bonus per category (Resource Prosperity +1; Secret +1D next military/intel action; Remnant Thread Ob -1 for 2 seasons + Thread Debt token; Anomaly MS -1 + Warden Cooperation eligible when Warden Recognition >= 2) (:21-34).
  - Failure +1 Church Attention Pool when targeting Depth >= 3 (:36).
  - Existing-action mapping: Tribune Investigate Ob 2, Tribune Spy Ob `floor(target Intel/2)+1`, Senator Diplomacy Ob `floor(target Stability/2)+1` (:42-47).
- **Conflicts / stale:** "Intel" stat struck; BG mode abstraction.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_bg_v30_infill.md
- **What it is:** infill prose for §8 BG mode.
- **Status:** same as skeleton ("DESIGN — canonical subsystem file"). Reading: historical.
- **Bears on:** FI.
- **Content that matters:**
  - Survey Overwhelming reveals POI plus +1 Influence (:20); no new card types so BG action economy preserved (:22).
- **Conflicts / stale:** none beyond skeleton.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_editorial.md
- **What it is:** fieldwork spec §12 open items and editorial flags (PP-628/630/632 applied 2026-04-13).
- **Status:** "DESIGN — canonical subsystem file". Reading: historical record; the Disposition/Knot redesign described has itself been superseded by ED-912.
- **Bears on:** FI, CHAR, WR.
- **Content that matters:**
  - Open editorials ED-507 (POI catalog per territory, 2-6 POIs across depth levels), ED-508 (named NPC starting Dispositions), ED-509 (Godot POI node architecture) (:20-22).
  - PP-632 redesign: Disposition range -3..+5 -> `-4 .. floor(Bonds/2)+1`, Ob `max(1, base Ob - Disposition)` direct subtraction, starting Disposition from lifepath +/-0.5 increments, Knots as being-with (Mitsein) for any character, Knot pool `(Spirit x 2)+History(Relevant)+3` with tiers Close 5/Medium 2/Loose 1, max `floor(Bonds/2)+1`, rupture sets Disposition to -4, decay threshold above +2 (:57-69).
  - SIM-DEBT-SOC-01..03: Ob calibration, Close Knot formation pacing 3-5 seasons, Close Knot rupture = 5 Composure damage (Composure = Cha + 6, min 7) (:71-75).
  - SIM-DEBT-FW-01..10 all RESOLVED; resolved editorials ED-496..506 (:24-55).
- **Conflicts / stale:** direct-subtraction Ob and Bonds-capped Disposition were reversed by ED-912 (flat -5..+5, stepped table; Bonds drives Knot capacity) per canonical_registry :189-195; propagation list targets (`designs/scene/*`) no longer exist.
- **Open items:** ED-507 POI catalog, ED-508 named NPC starting dispositions.

### .designs/systems/fieldwork/reference/fieldwork_exploration.md
- **What it is:** fieldwork spec §3 Exploration: Points of Interest, discovery procedure, movement/time, rendering strain.
- **Status:** "DESIGN — canonical subsystem file". Reading: live design intent for exploration; GM-based procedure.
- **Bears on:** FI, WR, SE.
- **Content that matters:**
  - POI categories by Depth: Landmark 0, Resource 1, Secret 2, Remnant 3, Anomaly 4, Breach 5; 2-6 POIs per territory, southern territories more Remnants/Anomalies, Askeheim entirely Anomaly/Breach; conditional availability gates (RS/MS band, season, faction control, prior discovery) (:20-33).
  - Discovery procedure: declare intent; perception gate (ontologically unavailable -> no roll wasted); pool `(Attribute x 2)+History`, TN 7, Ob per Depth; degree table with Overwhelming revealing a hidden feature and +1 Momentum; Failure +1 Exposure (:37-47). Multi-character: up to 2 assistants at Ob +1, each failing adds +1 party Exposure (:49).
  - Rendering strain: Depth 3 minor (TS >=10 no effect), Depth 4 Coherence check Ob 1 and Truth -1 if >=3, Depth 5 Coherence -1 automatic, Truth forced <=2, TS +1 (:65-73). Thread-Read is the only fieldwork action that produces co-movement (P-01) (:75).
  - Non-sensitive characters at Depth 3+ generate +0 Exposure; sensitive +1 (:77).
- **Conflicts / stale:** TS thresholds, `TN 7`, GM-prepared POIs vs no-GM engine; "RS" is the old name of MS.
- **Open items:** ED-507 POI catalog per territory unauthored.

### .designs/systems/fieldwork/reference/fieldwork_exposure.md
- **What it is:** fieldwork spec §6 Exposure (Cover, Exposure track, sources, reduction, Church Attention Pool) and §7 derived values.
- **Status:** "DESIGN — canonical subsystem file". Reading: live design intent for the covertness mechanic.
- **Bears on:** FI, WR, FA.
- **Content that matters:**
  - Cover = Cognition + most relevant concealment History; Noticed/Watched/Compromised thresholds table e.g. Cover 1-3: 3/5/7 up to Cover 12+: 8/10/12 (:20-31).
  - Exposure states and consequences: Noticed +1 Ob to fieldwork rolls for the season; Watched lets the dominant faction respond (Church Heresy Investigation eligible); Compromised ends the scene, Dispositions -1, investigations +2 Ob (:37-42).
  - Sources (failed roll +1/+2, Thread-Read +1, Surveil +2, hostile territory +1 per scene, Niflhel social +2); reductions (concealment -2, leave territory resets, season change resets, cover identity -1/scene, faction support -2/season) (:46-66).
  - Church Attention Pool feed: Watched +1 AP at Accounting, Compromised +1 AP; capped +1 per character per territory per season, +2 per territory from fieldwork combined (PP-581) (:70-74).
  - Derived values table: Fieldwork Pool, Investigation Threshold 3/5/8 by scope, Disposition -5..+5, Cover 2-14 (:80-87).
- **Conflicts / stale:** "Niflhel social action" (Niflhel dissolved).
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `654506799c63`) of `systems/fieldwork/sim/{fieldwork,investigation,knots}.py`: scene dispatch, Knot formation/strain/rupture/loss.
- **Status:** "REFERENCE — traced structure only". Reading: historical trace; essential census of how little of fieldwork was live.
- **Bears on:** FI, CHAR, CORE.
- **Content that matters:**
  - `fieldwork.py` and `investigation.py` entry points (`run_fieldwork_scene`, `advance_disposition`, `advance_evidence`, `resolve_npe_response`, `evaluate_dialogue_lattice`, `apply_response_matrix`) are all `stubwire.stub_resolve` typed no-ops; only `fieldwork_knots` has a contract (:152, :157).
  - No production code ever queues a `fieldwork` or `investigation` scene (only `contest` via Stability Crisis); reached only by a test constructing a `SceneSlot` manually (:153).
  - `form_knot` is never called in the season loop; mc_v18 records a `stub_resolve` marker literally named `'form_knot(world-gen|season-tick)'` as an "honest deferral"; `world.knots` stays empty (:154).
  - `form_knot` gates: Bonds >= `KNOT_BONDS_MIN`, Disposition >= `KNOT_DISPOSITION_MIN`, one actor `.ts >= KNOT_TS_MIN_PARTY`, count < `floor(bonds/2)+1`, no existing Knot between the pair, formation roll `roll_pool(pool, tn=KNOT_FORMATION_TN)` branching to Close/Distant/None (:76-87).
  - Only non-test caller of `sustain_knot` is `threadwork/opposing.py:resolve_opposing_operations`, itself orphaned (:155). `apply_knot_loss` applies only `coherence_delta` and `conviction_scar`; `composure_damage` and `disposition_set_to` are write-only into a dict; the FR-Dissolution wound is structurally unreachable (:159, :161).
  - `RUPTURE_COHERENCE_LOSS` flagged `[UNVERIFIED post-ED-912]`; `COHERENCE_BAND_STRAIN_PACING` never read (:158, :160).
- **Conflicts / stale:** the Conviction call used `'Loyalty'` before 2026-08-24 (see characters flow skeleton gap 7).
- **Open items:** none; this is a gap list.

### .designs/systems/fieldwork/reference/fieldwork_godot.md
- **What it is:** fieldwork spec §10 Godot video-game implementation (2026-04-13): exploration map architecture, Intelligibility Gradient visualisation, Investigation Journal, Disposition dialogue, dice visualisation, season/clock integration, plus validation findings G10-F01..F07 against `valoria-game@main`.
- **Status:** "DESIGN — canonical subsystem file"; "No fieldwork implementation exists" at validation. Reading: historical UI/Godot intent.
- **Bears on:** FI, GO, WR.
- **Content that matters:**
  - Intelligibility Gradient: visual presentation by TS band 0-9 default, 10-29 subtle displacement/chromatic aberration near POIs, 30-49 Thread mesh layer, 50-69 persistent overlay, 70+ dissolve at boundaries; Truth-dependent constitution (Truth 5 hellfire palette, Truth 3 ambiguous shimmer, Truth 0 calm structural) (:47-62). POI visibility gates TS >=10 Remnants, >=30 Anomalies, >=50 Breaches (:32-34).
  - Journal: Active Investigations with Evidence Track, ClueItems with reliability tags, InertKnowledge flagged (grayed, blurred; "your character knows this was said, but cannot fully grasp its implications"), Rumour Board (:63-82).
  - Disposition drives dialogue gating; social action approaches Read/Converse/Connect/Impress/Negotiate/Rumour; NPC memory requires NarrativeState persistence (:84-96).
  - Time budget 4-6 time units per season (:115); dice faces 1 skull, 7-9 success, 10 chain/double (:100-109).
  - Findings: POI system, shaders, Journal, Clock HUD absent; blockers A-02 (`NPCTrajectoryEvaluator` disconnected), DA-03 (`NarrativeState.deserialize()` stub), B-03, A-05 (:130-138).
- **Conflicts / stale:** `d10 TN 7` dice visualisation vs sigma resolver; GDScript file names reference an early skeleton; whether these blockers persist is a GO-lane check [UNVERIFIED].
- **Open items:** G10-F07 decision where `ThreadworkSystem.gd` lives.

### .designs/systems/fieldwork/reference/fieldwork_hybrid_v30.md
- **What it is:** fieldwork spec §9 Hybrid Mode: BG Strategic action sets a Fieldwork Offset that adjusts a TTRPG scene.
- **Status:** "DESIGN — canonical subsystem file". Reading: historical (hybrid mode discarded).
- **Bears on:** FI, CORE.
- **Content that matters:**
  - Offset by BG degree: Failure -1, Partial +0, Success +1, Overwhelming +2, cap +/-2, applied as Ob reduction to the TTRPG scene, min Ob 1 (:24-26).
  - Resolution in Cascade Phase: POI discovered -> territory bonus at Accounting; Evidence Track threshold reached -> faction intelligence updated (:27-30). Hybrid season order Strategic then Personal (PP-089) (:34).
- **Conflicts / stale:** requires a human GM; engine equivalent is the strategic-to-scene seam.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_hybrid_v30_infill.md
- **What it is:** infill prose for §9 Hybrid Mode.
- **Status:** "DESIGN — canonical subsystem file". Reading: historical.
- **Bears on:** FI.
- **Content that matters:**
  - Social outcome: NPC Disposition high enough yields faction-level intelligence/support (Domain Echo) (:18).
  - Bonus Personal Phase scene from a Strategic order replaces one of the standard 2-3 scenes; does not extend the seasonal cap (:20).
- **Conflicts / stale:** GM grant.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_investigation.md
- **What it is:** fieldwork spec §4 Investigation: Evidence Track, six actions, evidence quality tags, Desperate Trail, Thread-Read, contested investigation.
- **Status:** "DESIGN — canonical subsystem file". Reading: the principal design statement for investigation; relevant to the detective-game intent but stated in d10 TTRPG terms.
- **Bears on:** FI, SC, WR.
- **Content that matters:**
  - Evidence Track thresholds 3/5/8 (simple/complex/structural) set by GM and hidden; persistent across scenes; one track per investigation but Exposure per territory; depth-limited resolution (answer limited to deepest depth accessed); resolved investigation yields a Finding with reliability = strongest constituent tag (:16-36).
  - Six actions: Examine (Cognition), Interview (Attunement), Research (Recall), Surveil (+2 Exposure), Thread-Read (TS >= 30), Reconstruct (Ob = threshold - progress); progress by degree Fail +0/Exp +2 with possible false lead, Partial +1, Success +2, OW +3 and Exposure -1 (:42-58).
  - Reliability tags Verified / Testimonial / Documentary / Observational / Thread-verified / Unverified / Derived; Thread-verified is Inert Knowledge for non-sensitives (half value) and not admissible in Church Tribunal (:62-77).
  - Desperate Trail after 3 consecutive failed actions: TN 8, Exposure doubles, GM complication, Partial +2; persists through Compromised; clears on Success/Overwhelming or new season (:81-90). "Investigation failures should never produce 'nothing happens'": every failure is a clue about the opposing forces (:92).
  - Contested investigation: concealing party rolls Cognition x 2 + History to set a Concealment Ob per action (:112-114).
- **Conflicts / stale:** Disposition/Ob rules from PP-632 reversed by ED-912; "Memory genre" Contest vocabulary; the flow skeleton shows investigation engine is a stub.
- **Open items:** none stated.

### .designs/systems/fieldwork/reference/fieldwork_rationale.md
- **What it is:** fieldwork spec §13 design rationale index (2026-04-13 split from skeleton).
- **Status:** "CONTENT — rationale only. No mechanical values here." Reading: reference rationale.
- **Bears on:** FI, WR.
- **Content that matters:**
  - Intelligibility Gradient (not Rendering Gradient): rendering is constant (P-01) and what it can process varies (:19-22).
  - Rendering strain on passive Depth 3+ vs co-movement only for Thread-Read, because P-01 governs manipulations, not perception (:25-29).
  - Cover = Cognition + History chosen over Attunement; Sincerity Gate uses Spirit not Attunement; Desperate Trail at 3 failures (3D pool TN 7 Ob 2: P(fail) ~25%, three in a row ~1.6%; 4D at TN 8 ~60% viable) (:31-54).
  - Survey Ob inverse-Proximity; Exposure -> AP cap calibration: fieldwork ~11% of max CI acceleration over 4 seasons (:56-65).
- **Conflicts / stale:** none.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_socializing.md
- **What it is:** fieldwork spec §5 Socializing: Disposition track, social actions, Sincerity Gate, information gates, Beliefs, Knot integration, Niflhel toolkit (PP-632, ED-912).
- **Status:** "DESIGN — canonical subsystem file. PP-632 applied 2026-04-13" but the body already carries ED-912 amendments. Reading: live design intent for social fieldwork; mixes two Ob rules internally.
- **Bears on:** FI, SC, CHAR, FA.
- **Content that matters:**
  - Disposition -5..+5 flat (NOT Bonds-capped, ED-912) with stepped Ob table: Hateful +5 ... Neutral 0 ... Warm -1, Friendly -1, Trusting -2, Devoted -2, Bonded -3; floor Ob 1; labels give information gate per level (:20-36). Starting Disposition from lifepath +/-0.5 increments, floor, clamp (:38-47). Asymmetric per NPC per PC; decay -1/season for Disposition > +2 without contact; <= -3 needs a significant narrative event (:48-52).
  - Social actions: Read (Attunement, Ob 1/2/3 by depth), Converse (Charisma, Ob 2), Connect (Bonds, Ob 3, needs Disposition >= 0), Impress (Charisma, `floor(NPC Cognition/2)+1`, Disposition not subtracted), Rumour, Negotiate, Gift/Bribe (+1 Disposition, one per NPC per season) (:64-72). Degree effect: Failure -1 Disposition and Exposure +1, Partial 0, Success +1, OW +2 and NPC volunteers (:76-81).
  - Line 62 still says "Effective Ob = max(1, base Ob - Disposition)", contradicting the stepped table at :22 (internal conflict, superseded rule not removed).
  - Sincerity Gate: Spirit TN 7 Ob 1 when a character's stated Belief contradicts genuine engagement (:85-98). Information gates by Disposition +1..+4 for Settled/Hidden/Buried/Liminal depth (:102-108).
  - Knots (ED-912): prerequisites Disposition +5, TS >= 30 for one party, PC Bonds >= 5, count < `floor(Bonds/2)+1`, no existing Knot; tiers Distant/Close; formation Spirit pool vs Ob 2 (OW forms Close, Success Distant); strain gauge -5..+5, rupture at +5, Tempered at -5; effects: no seasonal decay, +1D on social actions, shared Composure buffer (:120-145). Breaking: rupture sets Disposition -3 and 4 Composure damage; loss costs Coherence -1 and 4 Composure; simultaneous rupture cap `floor(Composure x 0.75)` min 4 (PP-633) (:147-155). Note editorial doc says rupture sets -4 and 5 Composure (stale).
- **Conflicts / stale:** knots code `form_knot` constants (flow skeleton) vs these values; editorial doc still lists PP-632 values; Niflhel dissolved.
- **Open items:** "NPC-Initiated Social Engagement (§5.9)" appears in the index but not in this part.

### .designs/systems/fieldwork/reference/fieldwork_summary.md
- **What it is:** fieldwork spec §11 three-mode summary table (TTRPG, Board Game, Hybrid, Godot).
- **Status:** "DESIGN — canonical subsystem file". Reading: historical map of mode mapping.
- **Bears on:** FI, GO.
- **Content that matters:**
  - Godot column: navigable map + POI nodes, Journal + Evidence Track progress bar, dialogue + Disposition meter, TS gates POI visibility, per-territory Exposure meter (:16-25).
- **Conflicts / stale:** three-mode structure discarded.
- **Open items:** none.

### .designs/systems/fieldwork/reference/fieldwork_v30_index.md
- **What it is:** generated heading/size index (2026-04-18) of the parent `fieldwork_v30.md` v1.1 (~16.8k tokens), whose parts are the sibling `fieldwork_*.md` files.
- **Status:** indexed doc "DESIGN — approved for commit. Review corrections 2026-04-13 (v1.1), PP-628, PP-630" (:25). Reading: historical map of the fieldwork spec.
- **Bears on:** FI, CHAR, WR.
- **Content that matters:**
  - Section map: Core Principle Intelligibility Gradient; §1 Depth axis; §2 Fieldwork Pool (3.6k tokens; §2.3 system transition rules, §2.4 threadwork during fieldwork, §2.5 Domain Echo from Investigation, §2.6 Knot-mediated remote investigation, §2.8 Threadcut being social fieldwork); §3 Exploration; §4 Investigation; §5 Socializing incl. §5.9 NPC-initiated social engagement (NEW); §6 Exposure; §7-§12 (:30-93).
  - Sections §1, §2 and §5.9 are not in the sibling files read here, so the Depth axis, fieldwork pool, system transition rules and NPC-initiated engagement bodies are only listed in the index.
  - Canon compliance claims P-01, P-03, P-05, P-07, P-08, P-14, P-15 (:27).
- **Conflicts / stale:** the parent body is not present in this lane's file set; the `fieldwork_*` siblings are its atomized parts.
- **Open items:** §12 editorial items (954 tokens of "new editorial items", simulation debt).

### .designs/systems/fieldwork/reference/investigation_systems_v30_index.md
- **What it is:** generated heading/size index (2026-04-18) of "Investigation Systems Proposal" (2026-04-15, ~9k tokens): NPC Population Engine, Investigation Interface, Dialogue Lattice, Response Resolution Matrix.
- **Status:** indexed doc "CANONICAL — approved 2026-04-17 (editorial batch acceptance)" (:26). Reading: historical map of the design set behind the `investigation.py` stubs (`evaluate_dialogue_lattice`, `apply_response_matrix`, `resolve_npe_response`).
- **Bears on:** FI, CHAR, SC, WR.
- **Content that matters:**
  - System 1 NPE: Territory Social Ecology, NPC Genome Record, two-tier generation, persistence, named NPC stance triangles (:30-37).
  - System 2 Investigation Interface: Scene-as-Graph, Traversal Economy, Case Board (+ Thread layer ED-680), Temporal Dimension, Zoom In Triggers (:38-46).
  - System 3 Dialogue Lattice: gate types (756 tokens), visibility rules, outcome types, Sincerity Gate integration (:47-52).
  - System 4 Response Resolution Matrix: Five-Filter Chain (1,244 tokens), full chain example, bidirectionality/interdependency matrix (:53-57). Pending decisions and editorial decisions listed (:59-60).
- **Conflicts / stale:** index only; bodies absent here. The Case Board / Scene-as-Graph / Dialogue Lattice are the proposed engine for detective-style play; code has only stubs.
- **Open items:** "PENDING DECISIONS (mechanical gaps)" and "EDITORIAL DECISIONS REQUIRED" lists not visible.

### .designs/systems/mass_battle/reference/mass_battle_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at `dcf38ef`, anchors re-traced 2026-09-26) of mass battle after the 2026-08-24 engine swap: a 146-line strategic ADAPTER (`massbattle.py`) over the canon cell-scale engine in `systems/mass_battle/sim/`.
- **Status:** "REFERENCE — traced structure only". Reading: partly live; states the post-swap structure and several still-open design questions (many MB code paths have since moved, e.g. `modules/mass_battle/armies.py`).
- **Bears on:** MB, FA, CORE.
- **Content that matters:**
  - History: two disjoint trees (TREE A 1,905-line `massbattle.py`; TREE B 11,342-line cell engine under `tests/sim/mass_battle/` ruled canon J2 2026-08-03) merged by the swap (:21-37).
  - Adapter flow: `resolve_mass_battle(faction_a, faction_b, terrain, world)` builds `Unit`s via `_faction_to_unit` (one Line/infantry subunit, tier 2, command 4, discipline 5, morale 5, `power=round(faction.Mil)`; defender None -> `_GarrisonStub` Mil 1.5), runs `run_battle(unit_a, unit_b, max_turns=18)` under `rngsource.using(rng)`, then grades degree by survivor-size ratio thresholds (`OVERWHELMING_ATTACKER_MIN`) (:79-89, :189-190). Terrain now derived from `terrain_row_for_territory(target, fort_level)` (A7/ED-MB-0074) (:60).
  - Engine tick loop: volley_phase, contact halt, `check_orders`/`assign_targets`, `advance_cells`, `FIELD_MOVEMENT` time-of-impact, cross-side contention, `resolve_engagements_cascading`, simultaneous damage (`PER_CELL` column grid), rout checks, `phase_boundary` order stamina -> discipline -> morale -> rout -> rally -> reform -> threadwork every `TICKS_PER_PHASE` (:99-121).
  - Multi-turn and multi-unit orchestration (reserve commit, pursuit, rout contagion, freed-attacker bonus) exist but the campaign never calls them (:122-136, :191).
  - Gaps: what a faction's army IS at strategic scale is an unanswered design question (adapter uses pre-port defaults) (:189); adapter degree ladder is not the canonical margin-based `degree_from_net` (:190); `tactic_cards` pool modifiers empty; `invoke_altonian_reinforcements` raises `NotImplementedError`; `rally_check` and `threadwork_check` are empty hooks; `CASCADING_ENABLED` hard-coded True (:192-194); `module_contracts.yaml` mass_battle omits `sim_module` (:195).
  - Engine imports nothing outside its folder; engine toggles read from `os.environ` at import time (dozens) (:67, :178).
- **Conflicts / stale:** Key emission for `scene.battle_concluded` retired; the cell-based approach in the audit brief is realised by this engine (MB lane must verify vs `modules/mass_battle/`).
- **Open items:** the strategic Unit mapping, the degree ladder reconciliation, Thread->Mass handoff.

### .designs/systems/mass_battle/reference/mass_battle_v30_index.md
- **What it is:** generated heading/size index (2026-07-29) of `mass_battle_v30.md` v4.10 (~19.5k tokens; body is a sibling file not in this lane).
- **Status:** indexed doc "CANONICAL — approved 2026-04-17"; v4.10 addendum 2026-06-17 "provisional canon, Jordan-vetoable; byte-exact for single-sub-unit units" (:29-30). Reading: a map of the full mass-battle design; the body must be read from `mass_battle_v30.md`.
- **Bears on:** MB.
- **Content that matters:**
  - v4.10 addendum canonises validated engine behaviour: per-sub-unit rout/Morale/Discipline (ED-1019), troop-type presets (ED-1018), per-sub-unit broken scope (ED-1020), Discipline from own loss (ED-1022), continuous Morale (ED-1024), campaign-boundary Morale reset (ED-1025), per-sub-unit formation Discipline (ED-1026), destruction/cascade/recovery closeout (ED-1027) (:30).
  - Part A sections: A.3b Battlefield Geometry (913 tokens), A.4 Unit Stat Block (2,491), A.5 Command, A.6 Formation Types, A.7 Battle Turn Structure (6,324 tokens including Thread phase ED-050), A.12 Rout and Pursuit, A.14b Campaign Supply, A.14c Levy Restriction (:32-50).
  - Part B board-game mass battle (BG unit stats, tactic cards 813 tokens, Hybrid Handoff); Part D Mass Combat World Bridge (post-battle consequence scenes, named unit officers, player morale effect); Part E Battle Consequences (ED-542, ED-743) with cumulative caps per season (:51-67).
- **Conflicts / stale:** line numbers refer to a partly re-ordered body; Part B (board game) is formally discarded in the videogame mode.
- **Open items:** none visible.

### .designs/systems/mass_battle/reference/mass_battle_v30_infill.md
- **What it is:** prose infill of `mass_battle_v30.md` v4.8 (two clarifications only; most sections are stubbed in this part).
- **Status:** "CANONICAL — approved 2026-04-17" (:18). Reading: historical.
- **Bears on:** MB.
- **Content that matters:**
  - Weight-of-numbers (PP-570, PROVISIONAL ED-316): when a unit's Size > 2 x opposing general's Command, the opposing unit must pass a Morale check Ob 1 at Phase 6 Step 2 or lose 1 Morale (:25).
  - PP-MB-01: Effective Power computed at start of Phase 4 using Size at end of Phase 3; all Phase 4 damage applied simultaneously at Phase 5 Step 1 (:36).
  - A Woven unit configuration that shatters (Size loss in one turn > current Discipline) fights at Line formation Discipline 1 for the rest of the battle; Shifting Object status registered post-battle (:45).
  - Personal-combat ranged DR reference LP 0/2/3/5, HP 0/1/2/3, LBl 0/1/2/3, HBl 0/0/1/2 (:29).
- **Conflicts / stale:** weight-of-numbers trigger and scale "PROVISIONAL"; pool terminology (Power, Size) vs the cell engine's Unit/Subunit model.
- **Open items:** ED-316 trigger threshold and BG vs TTRPG scale.

### .designs/systems/mass_battle/reference/military_layer_v30.md
- **What it is:** Military Layer (v1.0, 2026-04-14): board-game unit bridge to mass battle, muster rules, BG battle resolution, and the CI competitive revision. Skeleton.
- **Status:** "CANONICAL — approved 2026-04-17"; ED-MB-0047 repaired its status line. Reading: mixed; unit roster / muster rules are BG-mode history; the CI sections (§3) overlap ci_political_v30; BG battle pool is superseded by the cell-scale engine.
- **Bears on:** MB, FA, SE.
- **Content that matters:**
  - Unit types table (Levy 1/1/7 ... Knights Templar 5/6/11) with BG Martial/Discipline/Health and TTRPG Power/Size TARGET (:62-72); Military stat sets max unit Power and starting Discipline ceiling (Mil 1 -> Power 1/Disc 2 ... Mil 7 -> 7/7) (:78-88).
  - Doctrine notes: Crown standing army = Löwenritter (Crown Military 5 via Power 5/Disc 6 elite units); Hafenmark equipment-quality doctrine from T17 mines and T8 smithing, mechanism "pending simulation" (:92-94).
  - Muster output Size 2, Power `floor(Mil/2)+1`, Prosperity size bonus; prerequisites per type (Heavy Infantry Prosperity >=5 + Wealth Ob 2; Cavalry Prosperity >=6; Artillery Wealth Ob 4 + 1 season); merge max Size 7 (:102-139); Experience Fresh/Seasoned/Veteran capped by Military ceiling (:143-155); Wealth Zero degrades Heavy Infantry and Cavalry Discipline -1/season (:159-166).
  - BG battle pool `Sum(Martial of engaged tokens) + floor(Mil/2)`; margin outcomes; Fort adds dice to defender (:200-225); Siege Action pool `Mil + 3` vs `Ob 2 + Fort`, cap 5 seasons (:180-196).
  - CI revision (§3): PP-402 unconditional passive REPEALED; conditional passive 0/+1/+2 by count of Prominent territories (0-1, 2-4, 5+); Piety Yield (PT 5 +1, PT 4 +0.5, PT 3 +0.5 per PP-667); Charity Advantage (Church Wealth >= controller + 2: +0.5 per territory, max +1); Templar Presence +1 per Templar in PT >=3 Prominent territory (max +2); Assert/Suppress; Baralta -1; cap +/-5; 8-step accounting sequence (:243-361, :418).
  - Accord table: Accord 1 -> Martial -1 and only Levy musterable; Accord 0 -> no Muster (:366-379).
- **Conflicts / stale:** CI Conviction Yield (PT 3 gives +0.5 here) vs `conviction_track_v30` (PT 3/2/1/0: +0); BG token model discarded; PP-667 unit resolutions in §5 table mismatch §1.4 (Prosperity tiers 1-3/4-5/6-7 vs "1-2 +0, 3-4 +1, 5 +2").
- **Open items:** ED-NEW-CI-01 conditional passive thresholds and BALANCE-NEW-CI-01 CI reform pace deferred to "engine_v4 smoke-test" (:416, :419).

### .designs/systems/mass_battle/reference/military_layer_v30_index.md
- **What it is:** generated heading/size index (2026-07-29) of `military_layer_v30.md` (~6.8k tokens).
- **Status:** "CANONICAL — approved 2026-04-17" (:25). Reading: historical map.
- **Bears on:** MB, FA.
- **Content that matters:**
  - Sections: §1 unit representation (2.7k tokens), §2 BG battle resolution, §3 CI revision competitive formula (1.9k tokens, 11 subsections), §4 Accord and Prosperity military interaction, §5.1 Thread integration cross-references (F-02) (:26-57).
- **Conflicts / stale:** none beyond body.
- **Open items:** §5 open editorial items.

### .designs/systems/npcs/reference/baralta_v30.md
- **What it is:** NPC profile extract (2026-04-25) of Duchess Inge Baralta's theological position, moved from the miraculous-event doc.
- **Status:** "PROVISIONAL — pending Jordan editorial review". Reading: character/world intent; no mechanism.
- **Bears on:** ARCS, CHAR, FA.
- **Content that matters:**
  - Baralta accepts the Church's theological content but rejects its monopoly on mediation; direct communion; deeds are evidence of divine favour; historical anchors Isabella I / Henry VIII, Luther's priesthood of all believers, prosperity gospel, deed-monarchy theology (:23-31).
  - Her theology weakens the "perceptual prophylaxis" over generational timescales, exceeding the game's ~5 year span, so "narrative/thematic positioning, not a mechanical variable during play" (:37-39).
  - She is "the Restoration Movement's pure adversary": her authority has two sources (sovereign, Solmund); Einhir pre-Solmund tradition would undermine both (:43).
  - Flagged editorial: NPC analysis §6 should be refined to "questions the Church's exclusive claim to mediate" (:33).
- **Conflicts / stale:** the Baralta Crown Claim doc treats her as the claimant in a mechanic (FA); no mechanical hook for the theology in code.
- **Open items:** the editorial update to the NPC analysis.

### .designs/systems/npcs/reference/edeyja_npc.md
- **What it is:** NPC sheet (2026-03-30) of Edeyja, the Southernmost Warden-Chief.
- **Status:** "Canonical Non-Player Character (working name — pending final name pass)". Reading: character intent and arc-access ladder for ARCS.
- **Bears on:** ARCS, WR, CHAR.
- **Content that matters:**
  - Stats: Thread Sensitivity 75-80 (highest living), Coherence 9, Cognition 5, Focus 5, Endurance 4, social 3-4 (:29-33). Conviction Warden, Resonant Style Evidence (show Thread state data; abstract appeals do not register) (:38-39).
  - Warden lineage dying (single digits to low teens); wardens do not recruit; the Forgetting means the peninsula does not know of them; a conventional force entering the Southernmost meets Thread operations that make it irrelevant (:44-55).
  - Conflict-as-disturbance: each inter-faction battle registers (MS -1/battle, -2 at Campaign/War); as Turmoil rises and MS decays her work gets harder; PCs working with her see how their faction's choices undermine what she preserves (:69).
  - PC access ladder by expedition progress: no contact (border) -> wary (Season 2; TS <=20 dismissed, 21-39 limited guidance, 40+ useful) -> substantive (Season 3) -> collaboration (Season 4+ after Extraordinary Weaving) -> campaign-altering knowledge after multiple seasons; she never leaves the Southernmost (:75-85).
  - Dramatic engine: she cannot fix the Calamity alone and cannot ask for help from people who do not know she exists (:93).
- **Conflicts / stale:** "Game Master" notes; Niflhel mention already redirected; Varfell Path B (WR 4 = "Edeyja substantive contact") is struck.
- **Open items:** pronoun/name confirmation editorial.

### .designs/systems/npcs/reference/npc_behavior_system_v1.md
- **What it is:** the original NPC ethical-stance and resonance behaviour system v1 (2026-04-13): Stance Triangle, named-NPC triangles, Beliefs and Scars, decision procedure, arc state machines, Resonant Style targeting, framework drift, and seven-level faction priority trees.
- **Status:** "SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md ... Retained as historical reference" (:11). Reading: superseded by v30 (and later by whatever engine/season carries) but it is the most complete extant statement of the NPC decision procedure and AI-chooser intent in this lane.
- **Bears on:** CHAR (NPC/AI chooser), FA, SC, WR, ARCS.
- **Content that matters:**
  - Stance Triangle = Conviction (what they want), Ethical Framework (what the institution rewards), Resonant Style (the argument form that bypasses their defences); Convictions listed Faith, Order, Reason, Equity, Precedent, Autonomy, Continuity (7); Resonant Styles Evidence, Consequence, Authority, Solidarity (4) with primary and secondary (escalation) (:21-56).
  - Named triangles for Almud, Himlensendt, Baralta (Precedent), Vaynard, Ehrenwall, Vossen, Hann, Torben (blank, set by first faction to Loyalty >= 5, else Autonomy by Year-End of Year 2), Edeyja, Maret Uln, Guilds, Niflhel, four Cardinals; Leadership Deviation Ob per leader (1 Baralta, 2-3 others) (:62-316).
  - Beliefs: 2-3 per named NPC; revision needs decisive contest outcome AND winning argument on a Resonant Style AND engaging the specific Belief; old Belief becomes a Scar; Scars 0/1/2/3+ change Conviction (secondary activates; primary may shift; at 3+ crisis table d6: 1-2 original primary, 3-4 secondary, 5 Autonomy, 6 relational pull) (:324-358).
  - Decision procedure for named NPCs: Institutional filter -> Conviction filter -> Decision Fork (Scar count 0 conviction over framework with Leadership Deviation Stability check; Stability <= 1 Autonomy regardless) -> Resonant Style interaction suspends the fork during a contest; non-named NPCs follow only the framework filter (:364-387).
  - Generic transition triggers (:409-417); per-NPC arc maps (Almud Reformer/Fortress/Overthrown; Himlensendt Zealot/Crisis of Faith/Confrontation; Baralta Constitutional Triumph/Pragmatist/Excommunication; Vaynard Scholar/Awakened/Consumed; Edeyja Holdout/Collaboration/Crisis) with branch conditions on Truth, Stability, Coup Counter, TS (:425-535). Transformation Knot strain propagation by TS band (:393-405).
  - Framework Drift table per faction (Church TC +1; Crown Truth +1/yr; Hafenmark Influence +1/season if all actions aligned; Varfell TK +0.5/season capped at 3; RM Presence spread; Guilds Favour; Niflhel overexposure; Löwenritter Military Consolidation) (:590-600).
  - Seven-level priority-tree template (Survival, Conviction-critical, Framework-aligned opportunity, Institutional Tendency, Conviction-secondary, Reactive, Pass) and concrete trees for Church, Crown, Hafenmark, Varfell, Guilds, Löwenritter, Niflhel, Restoration, Wardens (:618-740).
  - Evidence targeting against TS 0 NPCs restricted to ontic evidence; Thread-level evidence invalid until TS >= 30 (:548-550); targeting bonus +1D only, positional cap +5D (:578).
- **Conflicts / stale:** Conviction taxonomy here is 7 values; later PP-684 taxonomy is 13 and the code roster is 9 (see characters flow skeleton); Autonomy renamed Liberty; "Continuity" roster-determined; GM adjudication throughout; Niflhel dissolved; Yrsa Vossen vs Maret Vossen rename (:9, :836); Torben Conviction blank vs conflicts with later ED-525.
- **Open items:** ED-515..ED-530 (Conviction/Style taxonomy sufficiency, arc shapes, BG priority trees "P1-BLOCKER for BG sim", drift confirmation); SIM-NPC-01..05 simulation debt (:772-803).

### .designs/systems/npcs/reference/npc_behavior_system_v1_index.md
- **What it is:** generated heading/size index (2026-04-19) of `npc_behavior_system_v1.md` (~16.4k tokens); navigation index renamed from `_skeleton.md` (PP-673).
- **Status:** indexed doc "SUPERSEDED — canonical doc is designs/systems/npc_behavior_v30.md ... retained as historical reference" (:25). Reading: historical; the body is in `npc_behavior_system_v1.md` (read above).
- **Bears on:** CHAR.
- **Content that matters:**
  - Heaviest sections: §2 Named NPC Stance Triangles (5.1k tokens), §5 Arc Emergence (3.3k), §8 BG priority trees (2.6k) (:108, :129, :148).
  - Line numbers differ from the body (index line 4 vs body 10): the index tracks an earlier layout.
- **Conflicts / stale:** none beyond the body.
- **Open items:** none.

### .designs/systems/npcs/reference/npc_behavior_v30_index.md
- **What it is:** generated heading/size index (2026-04-20) of `npc_behavior_v30.md` (~22.5k tokens): the canonical successor to v1; body is not in this lane.
- **Status:** indexed doc "CANONICAL — approved 2026-04-17 (editorial batch acceptance)" (:24). Reading: the v30 map of what grew beyond v1; this is the doc `CURRENT.md` heads for NPC behaviour, though the contract `doc:` was repointed to `systems/factions/`.
- **Bears on:** CHAR (NPC/AI chooser), FA, WR.
- **Content that matters:**
  - Additions over v1: §2.13a Extra-Territorial Heresy Jurisdiction (ED-670); §2.14 Registrar Lennart Haelgrund (Ministry, 1,578 tokens); §2.15-2.17 Crown Inner Circle, Hafenmark Inner Council, Varfell Jarl Council; §3.4 Thread Operation -> Conviction Scar triggers (ED-663/664); §4.3 NPC Practitioner Coherence decision thresholds (ED-665) (:47-58, :66).
  - §8.11 NPC Personal Outreach Generation (outreach conditions, demand conditions, outreach by faction, scene structure, volume control, subnational faction outreach) feeding the player_agency scene slate step 5 (1,437 tokens) (:92-98).
  - §9.5 NPC Recruitment Procedure (PP-642): Identify, Approach, Offer, Resolution by Degree, Hooks, Defection (939 tokens) (:103-109).
  - Second §7 BG Faction Priority Trees (Crown, Church, Hafenmark, Varfell, Löwenritter, Ministry, Schoenland, Altonian Vanguard at IP >= 75, override conditions, NPC stat values TS/Truth) (:113-123); §11 Named NPC Roster Tracking Capacity (PP-661): tiers, capacity, demotion triggers, background tier, inner-circle NPCs, companion app display (:125-131).
  - Duplicate section numbers (two §7, two §11, two §5.2) show unmerged patches (:64-65, :90, :102).
- **Conflicts / stale:** duplicated headings; the PP-661 roster capacity numbers are only in the body.
- **Open items:** §10 editorial items and §11 simulation debt still open.

### .designs/systems/npcs/reference/npc_character_analyses_v30.md
- **What it is:** consolidated NPC character analyses (2026-04-11), skeleton: Part One 13 roster NPCs, Part Two ruler diamond and named NPCs. Most prose is in the `_infill`; this part carries structure, arcs and mechanical hooks.
- **Status:** "Status: DESIGN"; "All analyses flagged for user review" (:14, :16). Reading: character intent and arc inventory; no mechanism; several arcs conflict with later struck material.
- **Bears on:** ARCS, CHAR, WR, FA.
- **Content that matters:**
  - Roster of arc-bearing NPCs: Edeyja (fixed point), Maret Uln (Sorge parallel), Yrsa Vossen (Luxemburg trap, TS 25 below Forgetting threshold 29), Sæmund Haelgrund (Inquisitor, hidden TS 12), Sigrid Torsvald (TS 35 from archive exposure; ~30% abort rate), Halvar Brandt (external-threat fixated), Annika Feldhaus (Guilds, Thread-touched supply chain), Peder Almstedt (Parliament registrar, co-opt Influence vs Ob 3), Gerik Strand (flattery vulnerability -1 Ob), Dalla Virke, Doux Alexios Laskaris (sandbags IP -1/season while Elske Loyalty >= 3, flips IP +3 if Loyalty <= 2), Rikard Solberg, Prudence Cardinal (:22-146).
  - Ruler diamond on the Einhir/caste axis (Almud pragmatism, Lenneth revival, Baralta adversary, Vaynard expulsion) (:150-157). Lenneth TS pathway slow scholarly loosening, SA-gated, ceiling 10-20 (D-6, ED-727) (:182); Lenneth arcs A (Reformist Queen), B (Widow Regent if Almud assassinated), C (target) tied to the Royal Assassination Fuse sub-roll (:184-197).
  - Torben fuse target (sub-roll 3-4) leads to Almud Arc E and Elske retrieval via T4 (:210-220); Baralta wants the Crown actively, PP-487 PI-gated succession (PI < 4 fractures Hafenmark) (:239-249); Baralta theological profile ED-732 (:247).
  - Almud: Crown Mandate 5 answers "competent custodian" (:164); Discovery Event arc is rupture not confirmation (:174).
- **Conflicts / stale:** the assassination backstory removal (infill :84) vs earlier text; Niflhel/Coup Counter assumptions; empty paragraphs (Maret, Vossen, etc. have gaps between headings because prose moved to infill).
- **Open items:** Torsvald TS threshold "GM discretion (TS 40? 45?)" (:69); NPC name pending for the Prudence Cardinal.

### .designs/systems/npcs/reference/npc_character_analyses_v30_index.md
- **What it is:** generated heading/size index (2026-04-20) of the NPC character analyses (~4.8k tokens).
- **Status:** none stated ("Status: DESIGN" in the indexed doc). Reading: historical map.
- **Bears on:** ARCS, CHAR.
- **Content that matters:**
  - 13 roster NPCs + 11 ruler/named NPCs; heaviest entries Lenneth (587 tokens), Almud (420), Baralta (412) (:77-89). Dalla Virke 12 tokens, Prudence Cardinal 18 tokens, Vaynard 14, Klapp 14 in the skeleton show that most prose is in the infill.
- **Conflicts / stale:** none.
- **Open items:** none.

### .designs/systems/npcs/reference/npc_character_analyses_v30_infill.md
- **What it is:** prose infill of the NPC character analyses with historical parallels per NPC.
- **Status:** "Status: DESIGN" (:13). Reading: reference character design; richest narrative-hook source for ARCS.
- **Bears on:** ARCS, CHAR, WR.
- **Content that matters:**
  - Per-NPC flaw/engine and historical anchor: Edeyja maintenance engineer, Maret (Sorge), Vossen (Luxemburg), Haelgrund (Bellarmine; arc branches A undiscovered TS, B defects, C suppresses with Coherence degradation), Torsvald (Granville; Lenneth archive hinge), Brandt (Aetius), Feldhaus (Jacques Coeur; shared supply chain with Virke), Almstedt (Byzantine logothetes), Strand (William Marshal), Virke (Medici branch manager), Laskaris (Palaiologos; oikonomia), Solberg (Xenophon; homesickness steers Schoenland toward stability), Prudence Cardinal (Suger; OPTIMISER flaw: Church Wealth +1/season while Mandate -0.5 per squeezed territory at Year-End and PT erosion +1; Parish Revolt at >= 3 squeezed territories with Mandate <= 3) (:17-75).
  - Ruler diamond narrative: Almud as Manuel I Komnenos, deed-monarchy logic (competence = legitimacy, deposition is the system working), Almud's father assassination backstory STRUCK in favour of the forward fuse (:79-85); Lenneth as Catherine the Great, builds up not tears down, stages: cultural recognition, institutional reform, Thread work (:88-94); Vaynard as Reinhard von Lohengramm, Forgetting is his political prison (:99-107); Baralta as Isabella I, "Henry VIII not Luther" (jurisdiction) (:109-112); Himlensendt as structural keystone whose compassion and suppression are the same act (:114-119); Ehrenwall's Coup Counter as the deed-logic's enforcement mechanism, loyalty to the institution not the bloodline (:126-127).
- **Conflicts / stale:** Baralta "does not question the Church's theology" (:109) refined by the ED-732 supplement in the skeleton; "TC"/"CV" terminology; Coup Counter mechanics.
- **Open items:** Cardinals Klapp, Olafsson, Jarnstal mostly "unchanged" with no body in this part.

### .designs/systems/npcs/reference/npc_roster_v30_index.md
- **What it is:** generated heading/size index (2026-04-19) of "Named NPC Roster" (~8.7k tokens), skeleton body not in this lane.
- **Status:** indexed doc "Status: CANONICAL" (:24). Reading: historical map.
- **Bears on:** CHAR, ARCS.
- **Content that matters:**
  - 13 roster NPCs with titles: Edeyja, Maret Uln, Yrsa Vossen, Sæmund Haelgrund, Sigrid Torsvald, Halvar Brandt, Annika Feldhaus, Peder Almstedt, Gerik Strand, Dalla Virke, Doux Alexios Laskaris, Rikard Solberg, Aldric Tormann (Prudence Cardinal) (:28-40).
  - A "Mode Interface Matrix" (4.5k tokens) and "Mode Coverage Summary": each NPC must have presence in at least 2 of 3 modes (:43-58). Summary Table, Cross-Reference Faction Axis Positions, Stat Blocks, and "Caste System Impact on Roster NPCs" (:41-63).
- **Conflicts / stale:** the cast gets name "Aldric Tormann" in the roster vs "[Name Pending]" in analyses.
- **Open items:** Stat Blocks "to be generated after identities are confirmed" (infill :112).

### .designs/systems/npcs/reference/npc_roster_v30_infill.md
- **What it is:** roster prose: each NPC's compromise, historical echo, ethics and behavioural AI flaw; mode bridges; caste annotations.
- **Status:** "Status: CANONICAL" but "All NPC identities, motivations, and arc trajectories flagged for user review" and stat blocks provisional (:13, :15, :112). Reading: the NPC "Behavioral AI Profile" design (named flaws) is the most concrete intent statement for NPC AI in this lane.
- **Bears on:** CHAR (NPC AI), ARCS, WR, FA, FI.
- **Content that matters:**
  - Design principle: every NPC except Edeyja carries a structural compromise; each has a named Behavioral AI flaw that produces suboptimal play players can exploit (:17-18).
  - Behavioural AI flaws: Edeyja evidence-driven no flaw; Maret CONFLICTED (1-season delay against RM); Vossen IDEALIST (spreads Presence markers thin, 5 territories at 1 rather than 3 at 2); Haelgrund PROCEDURALIST (investigations +1 season but Overwhelming when resolved); Torsvald TS 35 (cover vs truth); Brandt EXTERNAL THREAT FIXATED; Feldhaus PROFIT-MAXIMISING (~15% of Guilds luxury revenue from Thread-touched supply chain); Almstedt CONSERVATIVE; Strand OVERPERFORMER; Virke NETWORK PROTECTOR; Laskaris PROTECTIVE; Solberg STABILITY-SEEKING (arms shipments conservative, intel downplays, better deals to the losing faction, policy ~1 season behind optimal aggression); Tormann OPTIMISER (:23-80).
  - Niflhel is not a coordinated faction but a constellation of syndicate houses (Virke family one of several) (:61).
  - Caste system as load-bearing: Feldhaus/Virke profit, Almstedt preserves, Prudence Cardinal's extraction deepens, Haelgrund enforces, Strand's frustration rebukes; "NPCs collectively reproduce the caste without intending to" (:114-130).
  - Mode bridges: how each NPC's compromise expresses in TTRPG (personal choice), BG (stat delay or card trigger) and Hybrid (Zoom In) (:85-109).
- **Conflicts / stale:** the named-flaw approach is a design for a scripted-flaw NPC AI (risk of scripting drift if hard-coded per entity); three-mode (TTRPG/BG/Hybrid) bridging text presumes a GM.
- **Open items:** ED-NEW-24 (RM internal split on Crown patronage) (:116); stat blocks pending.

### .designs/systems/npcs/reference/npcs_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `6545067`) of NPC code, which lives outside `systems/npcs/` (zero `.py` files): `systems/world/sim/npe.py`, `engine/autoload/npc_ai.py`.
- **Status:** "REFERENCE — traced structure only". Reading: historical trace; the census of what NPC code existed and was dead.
- **Bears on:** CHAR, WR, CORE.
- **Content that matters:**
  - NPE: `generate_npc` (ecology weights from Territory accord/prosperity via `canonical_accord`; Tier-1 archetype seed with Stance per active issue, worldview convictions, compromise category, volatility, loyalty; Tier-2 deviation roll with `DEVIATION_DIE_MAX` that flips one of four axes, with a fifth hidden-allegiance branch that computes but is never applied) (:53-75, :137).
  - `simulate_npc_actions`: for same-territory NPC pairs sharing a conviction with exactly-adjacent Stances, roll d6 against average Volatility, drift both one step, emit `NPCAction('stance_drift')`; its return is discarded by accounting (:76-88, :100).
  - `generate_npc` has no production call site; mc_v18 records a `stubwire` marker `generate_npc(world-gen|season-tick)`, with a golden pinning `npcs_generated == 0` (:132).
  - `npc_ai.select_action`/`evaluate_priority_stack` are stub no-ops with no callers (:133); `npc_behavior` contract declares Procedures B/C/D/E flows against `sim_module: none`; `npc_memory` contract has no code at all (:134).
  - `role` param never read; `PIETY_HIGH/LOW` never used (Territory has no piety field) (:46, :138).
  - `CURRENT.md`'s NPC head is `npc_behavior_v30` while the contract's `doc:` was repointed to a doc under `systems/factions/` (:139).
- **Conflicts / stale:** the CHAR lane should confirm whether `engine/season/` supplies NPC generation/decisions in place of these; the audit-brief intent on the AI chooser is not met by this code.
- **Open items:** none; gap table is the content.

### .designs/systems/overview/reference/clock_registry_v30.md
- **What it is:** Valoria Clock & Track Registry (created 2026-04-08, updated 2026-06-24): the "single source of truth" table of every clock, track and counter with ranges, starts and source docs. Skeleton.
- **Status:** "Status: CANONICAL"; "Registry maintained by hand" (:14, :124). Reading: a doc-side inventory, superseded in function by the typed registries (a `.md` is not the head of a fact, §0.05 cl.1); useful as a checklist of tracks to confirm exist in code.
- **Bears on:** CORE, WR, SE, FA, CHAR, FI, SC.
- **Content that matters:**
  - Shared clocks: MS 0-100 start 60 (videogame uses TTRPG default 60; BG 72; reconciliation 60-vs-72 pending creative layer), CI 0-100 start 28, IP 0-100 start 20, Turmoil 0-10 start 0 (:22-27).
  - Faction tracks: Torben Loyalty 0-7 start 7 (PP-599 supersedes start 3), Elske Loyalty start 4, Löwenritter Autonomy Loyal/Restless/Autonomous/Split, Popular Will, Warden Cooperation 0-3, Warden Recognition 0-4, Intel Advancement Counter (flagged STRUCK, unverified) (:35-41); faction stats 1-7, Stability 0-7 (:47-54).
  - Per-territory: Accord 0-3, PT 0-5, Fort 0-4, Prosperity 1-7, Guild Favour 0-7, Church Attention Pool 0-10 (first Inquisitor at AP >=3, second >=6) (:67-72).
  - Personal: Coherence 10, Truth 0-5, TS 0-100, Composure 3-21 (`Charisma x 3`), Concentration 5-35 (`3 x Focus + 2 x Spirit`), Health 13-55 (`(End+6) x (MW+1)`, MW cap 3), Stamina 5-47 (`3 x End + 2 x Spirit`), Momentum 0-4, Knot Count (:78-87) — note these differ from canonical_registry (Composure `Cha+6`, Stamina `End+1`) and combat_reference (Stamina `End x 5`) (a three-way two-ladders defect).
  - Contest: Persuasion Track 0-10 (A wins >=7, B wins <=3, compromise 4-6, Total Victory >=9/<=1); Obligation clocks cap ~3 active (ED-619) (:95-97). Fieldwork: Exposure, Cover, Evidence Track 3/5/8, Disposition -5..+5 (:110-113). Settlement tracks Prosperity/Defense/Order 0-5, Local Economy `Prosperity x 50`, Garrison Strength `Defense x 20 + Fort x 30`, Public Order `Order x 20` (:137-150).
- **Conflicts / stale:** the Persuasion Track in code vs doc; Torben Loyalty start 7 vs 3; contest resource formulas disagree with canonical_registry; Accord ranges 0-3 here vs 0-4 in canonical_registry; Intelligence and Popular Will flagged struck but still listed.
- **Open items:** ED-793 (IP start), ED-794/795/796 (struck items to verify), MS 60 vs 72.

### .designs/systems/overview/reference/clock_registry_v30_infill.md
- **What it is:** infill stub for the clock registry (headings only).
- **Status:** "Status: CANONICAL" (updated 2026-04-13 PP-548-554) (:13). Reading: historical, no prose.
- **Bears on:** CORE.
- **Content that matters:**
  - Only headings; no rationale text survives in this part (:16-23).
- **Conflicts / stale:** its "Updated 2026-04-13" header is older than the skeleton's 2026-06-24 update.
- **Open items:** none.

### .designs/systems/overview/reference/ms_budget.md
- **What it is:** Mending Stability Budget (ED-668, 2026-04-17/20): the single table of all MS drain and recovery sources, three budget scenarios and a three-path conclusion.
- **Status:** "ED-668 | Status: CANONICAL". Reading: design intent for MS dynamics; fact table belongs in code; see FA/WR/SE for the clock.
- **Bears on:** WR, MB, FI, PC, ARCS.
- **Content that matters:**
  - Starting MS TTRPG 60, BG 72, Hybrid 60 (:21-25). Seasonal cap +/-10 net at Accounting (:129).
  - Drain: baseline -1/year (-0.25/season); Gap -4/season each; Lock -1 to -2/season; Strain 9-10 extra -1; Dissolution Success -5 / Failure -8; POP Success >= -3; battle on Valorian soil -1 (Campaign/War -2); siege -1/season; Popular Uprising -1; TS 90+ Reality Strain -1/season; Substrate Saturation (>=3 Thread ops/turn) -1; mass-battle x3 multiplier STRUCK, replaced by flat -1 (:33-59).
  - Recovery: Mending +1 (Overwhelming +2); Weaving OW (Relational+) +1; WC >=2 halves Gap/Lock drain; WC >=3 +2/season; Gap self-closure by scale via d10 (Object 1-3, Personal 1-2, Relational 1, Territorial+ never) (:65-72).
  - Scenarios: A Year 10 moderate: net ~-11.75/season (Fragile by S8, Fractured by S13); B peak military: -20 to -22; C with WC 3: -4 to -8 capped (:78-105).
  - Four late-game paths: disciplined non-Warden, WC 3 with discipline, WC 3 with successful Wager (Arc E), and the non-viable trap (:111-121); "the substrate ontology does not permit Thread without consequence" (:121).
- **Conflicts / stale:** the end note ("WC 3 is the singular endgame survival path") contradicts ED-740 reframing in the same file (:123 vs :149); drain rates conflict with canonical_registry "Decay -1/year" claims only mildly; code implementation of these sources [UNVERIFIED].
- **Open items:** MS start 60 vs 72 resolution pending (clock registry).

### .designs/systems/overview/reference/overview_flow_skeleton_v1.md
- **What it is:** traced flow skeleton (at commit `6545067`) of the season loop as built before the engine/season rebuild: `engine/mc_v18.py:run_campaign`, `systems/overview/sim/{season,accounting,ci_track,ms_track,ip_track,rs_track}.py`.
- **Status:** "REFERENCE — traced structure only". Reading: historical trace of the pre-`engine/season/` loop; the best census of clock wiring defects at that time; CORE lane should check which survive in `engine/season/`.
- **Bears on:** CORE, WR, FA, SE.
- **Content that matters:**
  - Season loop: `advance_season` -> faction actions (`faction_take_action` per parliamentary faction with territory, exceptions caught and logged) -> `run_scene_phase` -> parliamentary scene -> `accounting_boundary()` + `next_tick()` -> `run_accounting` (6 steps: CI every season, MS baseline decay at year end, insurgency triggers, insurgency promotion, NPC ecology, report-only Accord drift probe) -> victory check (:76-97).
  - Dead/dormant clocks: `Turmoil` read as the victory gate but never written, so the Political Stability gate is permanently satisfied (:177); `PI` and `Strain` seeded and never read or written (:178); `IP` writer `apply_ip_delta` and `check_phased_occupation_threshold` are stubs with zero production callers (:179); `rs_track.apply_rs_delta` stub reachable only via a dormant echo leg (:180); CI Assert/Suppress steps always no-op because `run_accounting` never supplies them (:187); no Mandate/Treasury accrual step (PRE-LPS-1 PORT-BLOCKING) (:184).
  - Dead params: `VICTORY_THRESHOLD = 11` in `DEFAULT_PARAMS` is dead (live gate `victory.py` constant = 15); `max_seasons` argument shadowed (:172-173). Fallback winner by territory-count score when no victory fired (:96).
  - NPC generation and Knot formation are stub markers only (`generate_npc(world-gen|season-tick)`, `form_knot(...)`) so they never run (:174-176).
  - `check_arc_boundary` has zero callers; `SeasonResult` discarded; "13-step cascade" docstring vs actual 6 steps (:181-183). `peninsular_strain` contract emits (`env.*`) produced by no code (:188).
- **Conflicts / stale:** the victory threshold 15 vs "11/15 territories" in canon docs (GD-1); module-level globals `scene_slate._queue` and `victory._qualifying_streak` not world-scoped (:136, :138).
- **Open items:** none; every row is a traced gap.

## Cross-subsystem leads

- **CORE / CHAR / WR (narrative render):** the articulation skeleton shows Tier 1 protagonist lens, Tier 3 chronicle entry and Tier 2 trigger evaluation were all stubs with zero callers, and 10 of 13 subscribed trigger types had no emitter (`articulation_flow_skeleton_v1.md` :130-137). The design intent (cut scenes, chronicle, "Why?" causal-chain diagnostic) lives in `key_substrate_v30.md` §5.4, `integration_proposal_v30_index.md` Part 4/6 and `campaign_architecture_v30_index.md` Part 7. The WR/CORE lanes should check whether `engine/season/harness/chronicle.py` is the successor and whether the "Why?" walk exists.
- **CHAR / FI / SC (NPC AI chooser):** the fullest statement of intended NPC decision logic is `npc_behavior_system_v1.md` §1-§5 and §8 (Stance Triangle, Decision Fork with Scar count, Resonant Style targeting, seven-level priority template, Framework Drift) plus the "named Behavioral AI flaw" per NPC in `npc_roster_v30_infill.md`. `political_dynamics_keys_migration_v30.md` adds Procedures B-E (Concern, Project, Opinion Drift, Off-Screen Interaction, Gossip, 10-memory cap). The audit brief's AI-chooser intent should be compared with these; the named-flaw approach is a scripting-drift risk if encoded per entity.
- **CHAR / FA (Conviction vocabulary):** three rosters coexist in the design set: 7 values (`npc_behavior_system_v1`), 13 with a 4-axis matrix (`key_substrate_v30` §2.5, PP-684/718), and 9 in code (`conviction.py`; single owner `descriptor_registry.yaml:conviction_roster`). Also two unrelated "conviction" stats: per-character Convictions and the per-territory Piety Track originally called "Conviction (PT)" (`conviction_track_v30.md`). Name collisions flagged in `governance_type_registry_v1.md` §2.8 (Prosperity, Disposition, Guild Favour, Standing, Mandate).
- **FA / SE / SC (legitimacy and consent):** Legitimacy/Popular Support are "declared but inert in `sim/`" per `governance_consolidation_v1.md`, `governance_type_registry_v1.md` and `ners_vsg_reconciliation_v1.md` (E5, lps_inert_check 100/100), yet the ruled hierarchy (`scale_hierarchy_v1.md`, per the reconciliation doc) makes L/PS the consent modulator on the governance-type cascade. Mandate has two meanings (faction meter vs settlement-derived `round(7T/(T+K))`, retired as collapse carrier by D4). Compare with `engine/season` faction/settlement state.
- **FA / WR (hierarchy and territory):** B12 ruling: Settlement -> Territory (new tier) -> Province (formed only while a common faction holder) -> Duchy -> Country; overrules PP-726 fracturing, which `fractional_province_ownership_v30.md` and `session_a_spec_patches.md` still implement. SE and FA lanes should not audit against the older fracture rules.
- **FA (succession, treaties, transfer):** `faction_succession_split_v30.md` (two-stage resolution, 60/40 splits, RM settlement emergence at Order = 0), `treaty_expiration_v30.md` (per-arc 90% lapse as a Crown-nerf lever), `parliamentary_transfer_v30.md` (CB-gated transfer, 8 CB sources) and `factions_flow_skeleton_v1.md` (`world.casus_belli` has no production writer so most CB sources are dead; `mass_seizure` and treaty-expiration functions have no callers; Varfell and Hafenmark have no faction-unique action).
- **FI / SC (detective play):** `fieldwork_investigation.md` (Evidence Track, reliability tags, Desperate Trail with "every failure is a clue", contested investigation via Concealment Ob, Thread-Read), `fieldwork_exposure.md` (Cover and Exposure with faction responses), `fieldwork_socializing.md` (Disposition table, Knots), `investigation_systems_v30_index.md` (NPC Population Engine, Scene-as-Graph, Case Board, Dialogue Lattice, Five-Filter Response Matrix) and `fieldwork_flow_skeleton_v1.md` (all of these are stubs). The Case Board/Dialogue Lattice bodies are not in this lane (index only).
- **MB / FA / PC (mass battle seam and combat plan):** `mass_battle_flow_skeleton_v1.md` records the strategic Unit mapping (one Line subunit, Mil as power) as an unanswered design question, the adapter degree ladder as non-canonical, and `rally_check`/`threadwork_check` hooks as empty. `military_layer_v30.md` carries the faction-to-unit bridge (Military ceilings, muster, Experience, Wealth-Zero degradation). `phase4_5_plan_v1.md` carries the primitive/convergence/tradition principles and unbuilt Phases 4/5 (game-theoretic psychology, abilities-as-access); `combat_flow_skeleton_v1.md` shows a contact axis already exists in the traced code.
- **SE / WR (clocks and MS):** `ms_budget.md` (all MS drain/recovery sources, seasonal cap +/-10, four late-game paths), `clock_registry_v30.md` (clock inventory), `overview_flow_skeleton_v1.md` (Turmoil, PI, Strain, IP were dead clocks; Political Stability victory gate permanently satisfied). Check each against `engine/season/` clock owners.
- **ARCS:** `edeyja_npc.md`, `baralta_v30.md`, `npc_character_analyses_v30(.infill).md` and `npc_roster_v30_infill.md` hold per-NPC flaws, historical parallels and arc ladders (Edeyja access by expedition season and TS band; Haelgrund hidden TS 12; Torsvald TS 35; Laskaris IP sandbagging flip; Solberg stabilising bias; Prudence Cardinal Parish Revolt). `conflict_architecture_proposal.md` carries the Royal Assassination fuse (S8-S12 window; Almud/Lenneth/Torben sub-roll) and graduated Löwenritter autonomy.
- **PROCESS / all:** `decision_policy_v1.md` §2 precedence (measured engine behaviour outranks mechanical canon; §3 metaphysical canon tier never ruled) is the origin of CLAUDE.md §0.05's direction; `repository_keep_set_v1.md` explains why this tree is "information only".

## Likely stale or superseded

- **Retired apparatus (ED-IN-0232):** `key_substrate_v30.md`, `key_type_registry_v30.md`, `key_echo_armature_v1.md`, `propagation_spec_v1.md`, `_architecture_flow_skeleton_v1.md`, `articulation_flow_skeleton_v1.md`, `political_dynamics_keys_migration_v30.md`, `governance_ripple_substrate_v1.md` (Key-emission and resolution-quality bridge), `governance_type_registry_v1.md` §4 (`Field` sketch on the armature), `holonic_container_doctrine_v1.md` §1 cross-map. Their rulings (OF-7 deferred-apply, OF-B1 no re-entry, ER-2 symmetric continuity, per-tick termination theorems) describe a mechanism that no longer exists; the season-as-tick ordering and ORD-1/ORD-2 discipline are the part with a successor.
- **Superseded or struck mechanics:** `early_game_ignition_analysis.md` (by `conflict_architecture_proposal.md`); `npc_behavior_system_v1.md` (by `npc_behavior_v30`); `varfell_path_b_v30.md` and its infill (GD-1 strikes it); `conviction_track_v30.md` §4.2, §4.3, §6, §7 (GD-1) and §4.1 and CI-75 pacing (PP-421); Niflhel as faction (dissolved), VTM, Intelligence stat, Public Instability, Coup Counter (replaced by graduated autonomy), Popular Will (STRUCK per registry note), TCV (renamed PV).
- **Pre-d+sigma combat:** `combat_c4_draft_v0.md` entirely (d10 pool, TN 7, stance counter-table, `1D + History` out-of-range gate); `combat_reference_v1.md` §1-§5, §8 (Feint versus roll, resolution-order table, TN matrix, Fibonacci group), ranged tables; `canonical_registry.md` combat/pool rows.
- **Three-mode (TTRPG/BG/Hybrid) texts with a GM:** `hybrid_gaps_v30(.infill).md`, `fieldwork_bg/hybrid/summary`, `military_layer_v30.md` §1-§2 (BG token model), `mass_battle_v30_infill.md` Part B, `scale_transitions_v30_infill.md` (GM final call on scope); the videogame mode spec discards these but the index is only a stub here.
- **Terminology drift inside files marked CANONICAL:** TC/CV/RS/Theocracy Counter in `conviction_track_v30_infill/index`, `faction_politics_v30_index`, `ci_political_v30_index`; "13-step cascade" vs 6-step accounting; Disposition rules (`fieldwork_editorial.md` PP-632 values vs `fieldwork_socializing.md` ED-912; line 62 of socializing still says direct subtraction).
- **Stale registers and plan docs:** `clock_registry_v30.md` conflicting Torben/Intel/PW rows; `repo_state_armature_v1.md` (describes a banner and `review_core.py`, both retired); `repository_keep_set_v1.md` counts; `phase4_5_plan_v1.md` statuses (2026-07-01).
- **Dated traces:** all `*_flow_skeleton_v1.md` anchors (commit `6545067` etc.) predate the engine/season rebuild and several moves (`modules/`, `engine/substrate/composition`), so every file:line is [UNVERIFIED] now.

## Items that could change an audit finding

- **F-CORE (season loop / clocks):** `overview_flow_skeleton_v1.md` :177-179 lists dead clocks (Turmoil never written so the Political Stability victory gate is always satisfied; PI and Strain never read or written; IP writer a stub) and a dead `VICTORY_THRESHOLD = 11` param against a live 15. If `engine/season` kept any of these, a CORE finding on inert clocks or on the victory gate needs a falsifier. `propagation_spec_v1.md` :75 records a deliberate one-tick arc/year cadence offset (arc fires season%4==1, year-end season%4==0) "not a bug"; a CORE audit that flags cadence misalignment should check it.
- **F-CHAR-01..03, 05, 14 (chooser, interior, knowledge, refusal rate):** the design intent for NPC deliberation (`npc_behavior_system_v1.md` Decision Fork, Scar thresholds, Stability <= 1 -> Autonomy, Resonant Style as the lever by which others move a person) and for memory/opinion/concern/project/gossip (`political_dynamics_keys_migration_v30.md` Procedures B-E, salience clamp 0..3 with horizon factors 1.5/1.0/0.5, concern regeneration cooldown, project stall >= 8 / complete >= 10) is documented and can be used as a standard for the findings that the chooser does not read what an act would do and that the interior does not move. `characters_flow_skeleton_v1.md` gap 7 (scar landed nowhere for a roster-name mismatch) is the same class as F-CHAR-04 (runaway scar) and F-CHAR-06 (headline cannot fail).
- **F-FA-01..04 (decree, turnover, war, military verbs):** `faction_systems_overview_v30.md`, `faction_succession_split_v30.md` (leader loss opens a contest unless a sole heir has Disposition >= +3 and Standing >= 4; gap G thresholds), `parliamentary_transfer_v30.md`, `baralta_crown_claim_v30.md`, `factions_flow_skeleton_v1.md` (GD-2 mandatory response false; Varfell/Hafenmark have no unique action; `world.casus_belli` unwritten). If an FA finding claims "power does not change hands" or "war has no producer", these supply the intended rules and the earlier dead-code census to cross-check.
- **F-SE-01..04, 12 (economy, population, hunger, world never grows):** `fractional_province_ownership_v30.md`, `franchise_v30.md` (Franchise-weighted national Influence), `governance_consolidation_v1.md` E7 (no positive-feedback path; Flourishing 3.7 vs 659 per seed), `ners_vsg_reconciliation_v1.md` (unaugmented Pi term pins 298/300 settlements at ceiling; E1+E3+E7 must be bundled). A SE finding on a one-way-down or runaway dynamic is supported by this prior record.
- **F-FI-01..03, 09, 10 (unwitnessed facts, broadcast, investigation does not play, evidence untyped, detective borrowings not built):** `fieldwork_investigation.md` reliability-tag table and half-value Inert Knowledge rule, `fieldwork_flow_skeleton_v1.md` (all investigation entry points are stubs; no scene ever queued), `investigation_systems_v30_index.md` (Case Board, Scene-as-Graph, Dialogue Lattice, Five-Filter Chain exist only as design). These are the standard for F-FI-03/09; `fieldwork_exposure.md` Cover/Exposure thresholds table is the intended covertness mechanic.
- **F-PC-01, 02, 09, 13, 14 (combat unreached, same fighter, tradition layer unreachable, design intent, NPC not an agent):** `combat_currency_v1.md` (U10 activation; `IMPOSITION_GATE=False`; per-fight texture instrument), `phase4_5_plan_v1.md` (Phases 4/5 unbuilt at 2026-07-01), `combat_flow_skeleton_v1.md` (contact axis `grab_available`/`grab_outcome` exists in traced code, `engagement` has no outside caller), `ability_armature.md` (`seize` dead lever), `tradition_decomposition_v1.md`.
- **F-MB-01..03, 05, 14 (battle scale, headcount ratio, no natural trigger, two code paths, individual attributes):** `mass_battle_flow_skeleton_v1.md` :189-194 (adapter Unit mapping unanswered, degree ladder non-canonical, multi-unit orchestration unreached), `military_layer_v30.md` (Experience, Military ceiling, Wealth-Zero degradation, siege pool `Mil + 3`), `mass_battle_v30_index.md` (v4.10 per-sub-unit rout/Morale/Discipline canon).
- **F-WR-01, 03, 04 (stories do not escalate, story bar cannot fail, world's readings have no reader):** `ms_budget.md` (MS dynamics), `conflict_architecture_proposal.md` (assassination fuse, bishop appointment, black markets), `early_game_ignition_analysis.md` §2 (six historical ignition mechanisms as a design checklist), `tensions_pair_validation.md`. The decision to cut the Tensions Deck to 6 cards/draw 1 is a design precedent for ignition by structure rather than events.
- **F-GO / ARCS adjudication:** `fieldwork_godot.md` (UI blockers A-02, DA-03, B-03, A-05; Journal and Inert Knowledge UI treatment), `edeyja_npc.md` access ladder, `npc_roster_v30_infill.md` named flaws as testable behaviours.
- **Self-contradicting design inputs (design-doc claims should not be cited as correct):** Mass Seizure Ob has two forms (`2 + Fort + max(0, 3 - PT)` in `conviction_track_v30.md` vs `10 - PT - infrastructure` in `ci_political_v30.md`), Piety Yield differs between `conviction_track_v30` (PT 5 +1, PT 4 +0.5, else 0) and `military_layer_v30` (PT 3 +0.25 then +0.5), starting capital Accord 3 vs 4, Composure/Stamina/Concentration formulas disagree across `canonical_registry`, `clock_registry_v30`, `combat_reference_v1`; a finding that treats any one of these as "the canon" needs the code to arbitrate.
