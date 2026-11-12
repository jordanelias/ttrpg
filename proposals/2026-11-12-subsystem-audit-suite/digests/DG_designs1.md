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

