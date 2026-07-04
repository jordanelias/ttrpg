# Dossier — Faction/Political Lane

## Status: WORKING NOTES (qualitative NERS audit, 2026-07-04)
_Lane: faction_political. Read: faction_canon_v30.md, faction_layer_v30.md, faction_behavior_v30.md,
faction_state_authoring_v30.md, faction_systems_overview_v30.md (skim). Also spot-checked
faction_politics_v30.md and references/module_contracts.yaml for the boundary question._

---

## Core loop (as read from the corpus)

Each season a faction spends its Domain Action slot(s) across 7 turn priorities (`faction_layer_v30`
§7): Intel/Tribune → Military → **Domain** (Consul/Muster/Govern/Trade/Fortify) → **Social**
(Parliamentary Motion / Treaty / Hafenmark Manoeuvre) → Thread → **Special/Unique** (Royal Decree,
Excommunication, faction signature) → Project. Phase 5 Accounting (10 steps, `faction_layer_v30`
§7) then applies attribute deltas, runs Stability checks/collapse, advances CI/RS/IP clocks, resolves
Turmoil/Accord, checks Occupation duration, and checks victory (GD-1: 11+ territories, 2 seasons
sustained). Underneath, a 4-component behavioral engine (Mission / Cascade / Public Expectation /
Legitimacy+Popular Support — `faction_behavior_v30` §3) computes faction disposition every season via
named-coefficient formulas (α/β/γ/λ, cosine-similarity cascade fidelity), feeding **Mandate**
(`faction_canon_v30` §5.1: `clamp(round(7T/(T+6)),0,7)` over settlement-weighted L/PS) — the one
headline stat gating each faction's signature action.

## Domain Action menu — myriad options or accounting chores?

Universal actions: `govern`, `muster`, `military_conquest`, `parliamentary_transfer`
(`faction_systems_overview_v30` §3.1). Each player faction gets exactly **one** signature action
(`faction_canon_v30` §9): a single d+σ roll vs an Ob, resolved on a 2-4 rung degree ladder producing a
stat push (±1 Mandate/Legitimacy/Wealth typically). Parliamentary Motions (`faction_layer_v30` §5.4)
are the richest layer — 10 named motions with proposer minimums, vote thresholds, rebuttal math,
veto counterplay (Church Sacred Veto cadence) — genuine multi-faction coalition politics. But the
4-component behavioral engine that determines *disposition* (Cascade, Public Expectation, L/PS drift)
runs entirely on formulas the player never touches directly (`faction_behavior_v30` §3.2-3.5): it is
computed, not chosen. Net picture: a narrow, mostly-numeric action menu wrapped in a dense
simulation layer that outputs one number (Mandate) per faction per season.

## Decision points

1. **Domain Action selection** (govern/muster/conquest/transfer + 1 signature action) —
   `faction_layer_v30` §7, `faction_canon_v30` §9. **thin** — few named verbs, each a single roll,
   binary/near-binary outcome ladder.
2. **Parliamentary Motion targeting + coalition/veto play** — `faction_layer_v30` §5.3-§5.5.
   **moderate** — real multi-actor stakes (Mandate-weighted votes, Church veto cadence, Rebuttal
   math), but the motion list is fixed/closed (10 items).
3. **Treaty negotiation (3-phase)** — `faction_layer_v30` §3.3. **moderate** — Positioning +
   Concession structure gives real bargaining texture.
4. **Mandate/Legitimacy/Popular Support management** — `faction_behavior_v30` §3.2-§3.5.
   **degenerate as a player decision** — entirely formula-computed (α/β/γ/λ coefficients, cascade
   fidelity cosine similarity); the player influences it only indirectly via which DA was spent.
5. **NPC faction voting (Guilds, Niflhel)** — `faction_layer_v30` §5.8. **degenerate** —
   literally "GM controls NPC faction votes," with Guilds reduced to 3 hardcoded if/then rules.
6. **Cascade root selection (single vs multi-root)** — `faction_behavior_v30` §3.2.2. **thin** —
   every faction defaults single-root ("deferred to Stage 10"), so "Cascade" (many-actor conviction
   blending) collapses to one leader's stat for all 6 canonical factions at scenario init.

## North Star assessment

Choice density: **thin-to-moderate**. The lane's prose (faction sheets, Doctrine Notes, Arc
Trajectories, Foil Dynamics — `faction_canon_v30` Part B) is narratively rich and legible, but the
*mechanical* decision surface a player actually operates each season is narrow: a handful of named
actions plus Parliament. What the subsystem feeds the collision engine: Standing/CB/Conviction-Scar
accumulation, Mandate-gated signature actions, and Foil/Axis positioning (`faction_canon_v30` §7,
§10) — decent seeding for cross-faction narrative collisions (Consecration Triangle, CI 60 Seizure,
Excommunication chain), but a large share of "faction behavior" is accounting output, not player
choice, which narrows rather than widens the decision space the North Star calls for.

## N/Omega/Q observations

- **Omega(c) autonomous world — FAILS at the letter of the doc.** `faction_layer_v30` §5.8: "GM
  controls NPC faction votes (Guilds, Niflhel...)." This is a TTRPG-era instruction sitting inside
  the doc chain feeding the no-GM Godot engine (CLAUDE.md: "There is no GM — the engine resolves
  everything"). No engine-side NPC-vote-generation logic is specified beyond 3 Guild if/then rules;
  Niflhel's is dead (struck). The faction AI priority stack itself is `AUDIT-PENDING`
  (`faction_systems_overview_v30` §2.6, citing `sim/autoload/npc_ai.py`).
- **Q-robust dramatic legibility — partial.** From the Crown/Church sheets alone (`faction_canon_v30`
  Part B) a designer *can* answer whose position is at risk (Crown: "structurally fragile," Doctrine
  Notes) and what each wants (Mission text). "What happens if no one acts" is answerable for Church
  (Arc A default: CI → 75+, territorial seizure begins) but the underlying Mandate/Legitimacy math
  that would let a screen *render* this live is buried in coefficient formulas with no declared UI
  surface (Godot skeleton covers 0/6 faction modules per CLAUDE.md §6).
- **Q-elegant — questionable.** The 4-component model (Mission text + Cascade α-weighted blending +
  Public Expectation cosine similarity + per-settlement L/PS with 5-temperament typology) is
  substantial machinery whose sole player-visible output is a single 0-7 Mandate scalar gating one
  action/season (`faction_canon_v30` §5.1, §9). Depth-to-payoff ratio is thin.

## Threadwork junctures

- **present:** `conviction_track_v30` §1.3b PT drift (ED-676); `scale_transitions_v30` §3.5/§3.6/§5.6
  (Thread op IS the Domain Action; ED-673); `faction_layer_v30` Priority-5 Thread Domain Action slot
  in the turn sequence (§7).
- **absent-but-plausible (confirmed against this lane's own core files):** `faction_behavior_v30`
  — the 4-component engine that actually computes Cascade/Legitimacy/Popular Support has **no**
  Thread/Coherence/Calamity input path; a practitioner's Leap, Weave-brittleness, or Rendering Crisis
  never enters the α/β/γ/λ formulas directly — only via generic `env.*` shock terms (§3.4.2). This
  matches grounding-doc-03's corpus-wide note ("faction_behavior_v30 — one incidental mention; no
  mechanical hook into faction AI") but is here scoped specifically to the political-behavior engine's
  own math, not just a general absence.
- **absent-deliberate:** none identified in this lane's core files (no citation found stating thread
  exclusion from faction behavior is intentional).

## Dramatic-legibility test (from faction_political subsystem state alone)

- Whose position is at risk? **Partial** — per-faction Doctrine Notes answer this qualitatively
  (Crown: assailed from every axis simultaneously); no numeric threshold ("Stability ≤ X ⇒ at risk")
  is surfaced as a single readable line — a designer must cross-reference 5 Stability Triggers
  (`faction_layer_v30` §1.2) to reconstruct it.
- What does each actor want? **Yes** — Mission text is explicit and machine-readable per faction
  (`faction_state_authoring_v30` §2-§3 YAML blocks).
- What happens if no one acts next season? **Partial** — Arc Trajectories give a per-faction default
  path (Church Arc A: CI climbs), but the general case (any faction, arbitrary season) has no single
  citable "if nothing happens, X" rule; it must be derived from the Accounting step order (§7).

## Degenerate-line candidates

- Institutional Consolidation passive recovery (`faction_layer_v30` §1.3, `faction_canon_v30` §12
  D-adjacent): "no Trigger 1-5 fired this season → Stability +1 + Accord +1" rewards inaction with a
  guaranteed gain, a turtle-and-wait line, compounded by the ±2/season Stability cap making active
  recovery no better than doing nothing some seasons.
- Single-root Cascade default (`faction_behavior_v30` §3.2.2) for all 6 factions at scenario init —
  reduces the "many-actor conviction blending" mechanic to one leader-stat lookup, a collapse of the
  advertised mechanism's own state space.

## Edges in/out

| Dir | Other system | Mechanism | Status |
|---|---|---|---|
| in | Settlement (L/PS) | Mandate = size-weighted saturating aggregate | implemented (`faction_canon_v30` §5.1) |
| in | Personal/Scene (Domain Echo) | Debate→Mandate, Tribunal→Standing | declared-only (scale_transitions §5; scene.combat_resolved is declared-but-unconsumed per grounding-doc-02) |
| in | Thread | conviction_track PT drift, Priority-5 slot | declared-only for the behavior-engine math itself (see Threadwork above) |
| in | Peninsular Strain | temperament drift toward outcomes-only | implemented (`faction_behavior_v30` §3.4.2) |
| out | Settlement | Mandate drifts L/PS back ±1/season (mean-reverting) | implemented |
| out | Victory (GD-1) | 11+ territories, 2 seasons sustained | implemented, reader-only consumer |
| out/in | faction_politics ↔ faction_state | succession/coup/standing dual-emit | divergent — module_contracts marks `faction_politics` doc:null despite a 1115-line CANONICAL `faction_politics_v30.md` (rank ladders, succession, caste) existing under a matching name; boundary "[OPEN — Jordan]" |
| out | Mass Battle | Military/Stability feed | implemented |

## Six directions

- **top-down:** Omega(c) (autonomous world) is contradicted at the letter by `faction_layer_v30` §5.8's
  explicit "GM controls NPC faction votes" — a TTRPG-authoring instruction unresolved for the no-GM
  engine target.
- **bottom-up:** the accounting substrate (named coefficients, cosine similarity) is precise and
  heavy but surfaces almost no direct player choice — substrate outweighs surfaced decision.
- **lateral:** faction sheets are narratively thick (Doctrine Notes, Arcs, Foils) while the actual
  L/PS mechanic they reference lives one layer down in settlement_layer — faction "identity" is prose
  bolted onto borrowed numbers.
- **diagonal:** Thread and Domain Echo are the two designed cross-scale levers into faction state, but
  Thread's hook into the faction_behavior engine itself is only incidental — thin diagonal wiring
  relative to what scale_transitions promises.
- **forwards:** faction systems carry ~80% of Pass 2's forward-flag load (`faction_systems_overview_v30`
  §10) and 0/6 faction modules are represented in the Godot skeleton (CLAUDE.md §6) — the largest
  unresolved cluster on the path to Godot.
- **backwards:** the faction stat lineup (6-stat vs 7-stat, L/PS scope) has been re-litigated at least
  three times in one file (`faction_canon_v30` §5.1-§5.3, §12 D3/D7 — 2026-05-07 flag → LPS-1 → LPS-2e)
  without yet reaching a typed engine surface.
