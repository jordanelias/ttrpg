# Valoria Governance Consolidated Compendium (v1)

## Status: PROPOSED — 2026-07-12 · Lane: IN (cross-cutting; SE, FA, GO) · Read-only research consolidation. NOT canon; nothing here flips a `Status:` line. The single home for this session's entire governance-design body of work, so nothing is left stranded as unused research.

**Why this exists.** The 2026-07-09 → 2026-07-12 session produced a large body of governance research and
proposals that had accumulated across six dockets, plus a stress test and a reconciliation against the
pre-existing built substrate. Much of it — most visibly ~94 fully-worked event cards, the NPC roster/officer
system, and the proactive four-scale action menus — was **researched but never assembled or acted upon**.
This compendium collates all of it into one properly-formed structure, extensively, with no ideas lost, and
reconciles it against what is actually built (`sim/territory/`, `goldenfurt_slice`, the 500-seed
`settlement_mgmt_stress_01`).

**Companion head.** The *decision surface* for this material — the five architecture reconciliations (Compact
vs Leverage, §1.0d vs Goldenfurt recall, event-model fork, Mandate carrier, AP model) and the twelve PR#119
item dispositions — lives in `../../architecture/governance_consolidation_v1.md`. Read that for "what to decide"; read this
for "everything there is."

---

## Contents

### The event corpus (the world's moves)
| Part | What | Count |
|---|---|---|
| `event_cards/00_integration_map.md` | Maps the 58-card grounded deck + 28-card Goldenfurt deck against the HEV cards; dedup cross-refs; combined family totals | 58 + 28 mapped |
| `event_cards/21_…` … `event_cards/210_…` | **All 94 historical event cards**, extracted from the 2026-07-10 catalogue's §2.1–§2.10 (each: family, trigger, response branches with deltas, follow-on, the Action it introduces, the Loop) | **94 cards, 10 categories** |
| `event_cards/30_ripple_chains.md` | The §3 cross-domain ripple chains as Thread/chained cards | **12 chains** |

Categories: succession/civil-war (8) · blockade/embargo (10) · siege/sack/garrison (10) · earthquake/eruption (9) · flood/drought/siltation (10) · famine (9) · plague/epidemic (9) · climate-shift/storm (9) · debasement/fiscal (10) · trade-monopoly (10). **Combined event corpus across all three decks ≈ 180 cards.**

### The player's moves & the mechanics they need (Tier 1 + Tier 2)
| Part | What |
|---|---|
| `40_roster_officer_system.md` | **NPC Roster / Officer / Advancement System** — the full §3 design (one-engine-two-scale-bindings, shared rank-space + auxiliary meters, NPC sheet extension, autonomous loop, downfall/Ω-d mechanic, naming) + the 10 rise-to-influence mechanisms (patronage, merit, marriage, court favorites, bureaucratic capture, military retinues, purges, rival factions, venality, religious authority). *How characters gain/maintain/lose standing and consolidate power.* |
| `41_proactive_scale_menus.md` | **Proactive Player-Action Menus** — the four scales defined; a new Organization-scale menu; a new Territory-scale menu; Settlement + Faction/Ministry extensions; the reuse-vs-new-lever ledger. *The player-initiated counterpart to the event deck.* |
| `42_action_verb_catalogue.md` | **Consolidated Domain-Action / Verb Catalogue** — every new verb/method the 94 events introduce, deduped and grouped by parent verb | **109 entries** |
| `43_directive_types.md` | **Directive-Type Expansion** — Embargo, Recall, Quarter, Multilateral Embargo, Nationalize Charter + the reconciled full Directive enum |
| `44_standing_institutions.md` | **Standing Crisis-Defusing Institutions** (Water Board, Ever-Normal Granary, River Conservancy, Coalition Fortify Pool, …) **+ the recoverable-vs-doom-loop synthesis** — the bridge between the event research and the stress test's negative-spiral finding |
| `45_hidden_longfuse_stats.md` | **Hidden Long-Fuse Environmental Stats** (SiltLevel, OreGrade, SalinityLevel, …) — PROPOSED optional depth layer, with a per-stat abstract-to-Prosperity vs track-explicitly decision (honoring the standing "abstract, don't over-granulate" ruling) |

### Status closure & open-work registers (Tier 3 + Tier 4)
| Part | What |
|---|---|
| `tier3_proposal_status_closure.md` | **Proposal-Status Closure Register** — all 58 comparative-governance proposals triaged (12 authored / 9 promote-ready / 23 needs-Jordan / 14 cut); the vindicated rejected proposals (IT-3, VEN-SE-4, VEN-SE-7, BYZ-4); the Crown Administrative flat-rank problem; the collected needs-Jordan handoff items |
| `reeval/reeval_*.md` | **The 44 proposals re-evaluated against the built substrate** — each: STILL-VALID / REDUNDANT / COLLIDES / RECONCILE / SUPERSEDED + whether the discovery changes its prior NERS verdict | **all 44** |
| `tier4_discovered_open_work.md` | **Discovered Open-Work Register** — Goldenfurt v1.1 backlog; the 2026-06-22 baseline audit gaps (G2/G3/H3, G1 since-closed); the 500-seed framework's F1/F6 + the 24 un-run NERS probes |

---

## Provenance (what this draws from)

- **Research dockets:** `2026-07-09-comparative-governance-research` (44+14 proposals), `2026-07-10-historical-concerns-action-catalogue` (the 94 event cards + ripple chains), `2026-07-11-rise-to-power-roster-system-research` (Part 40), `2026-07-11-proactive-governance-scale-research` (Part 41), `2026-07-11-grounded-event-card-deck` (58 cards), `2026-07-11-comparative-governance-pessimist-ners-audit` (NERS verdicts), `2026-07-12-settlement-season-stress-sim` (stress test + reconciliation).
- **Built substrate (reconciled against):** `sim/territory/` (registry/ledger/infrastructure), `designs/territory/goldenfurt_slice/`, `tests/sim/settlement_mgmt_stress_01/`, `designs/audit/2026-06-22-territory-settlement-audit/`, the march/hierarchy layer.
- **Canon it proposes changes to:** `faction_politics_v30.md`, `settlement_layer_v30.md`, `governance_play_redesign_v1.md`, `governance_ripple_substrate_v1.md`.

## Reading order

1. `../../architecture/governance_consolidation_v1.md` §6 — the decisions to make (start here for "what now").
2. This index → `tier3_proposal_status_closure.md` — the proposal state of play.
3. The event corpus (`event_cards/`) and player-move parts (`40`–`45`) — the content, when authoring.
4. `tier4_discovered_open_work.md` — what else is open in the surrounding built work.

**Everything here is PROPOSED and read-only.** No canon `Status:` line is flipped, no ledger entry written,
no `module_contracts.yaml` edited. Ratification of any part is a separate, explicit Jordan decision.
