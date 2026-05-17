# VALORIA — Faction Systems Overview

## Status: REFERENCE — Pass 2 follow-up 2026-05-17

## Scope: Single-pane reference cataloging every faction-related system and mechanic in Valoria. Points at canon; does not duplicate it. Source of truth for "what surface area do factions touch in the engine." Companion to `canon/mechanics_index.yaml` (mechanic-level entries) and `designs/audit/2026-05-17-v18-integration/integration_plan_v18.md` (implementation phasing).

## GD constraints: GD-1 binding (sole victory path) · GD-2 binding (mandatory threat response) · GD-3 binding (faction-emergence pipeline).

## Authority: catalog derived from `canon/mechanics_index.yaml` `categories.faction_unique_actions` + `canon/02_canon_constraints.md §B` + Pass 2 canonized docs. 83 mechanics total in index; ~50 are faction-touched (the rest are primitives, services, peninsular cascade, cross-scale bridges).

---

## §1. Layer Architecture

Factions touch six layers. Mechanics are distributed across them:

```
┌───────────────────────────────────────────────────────────┐
│  L6. PENINSULAR LAYER — accounting, cascade, ci/rs/ms/ip  │  ← end-of-season aggregation
├───────────────────────────────────────────────────────────┤
│  L5. WORLD LAYER — RM, miraculous, insurgency, NPE        │  ← background processes + emergence
├───────────────────────────────────────────────────────────┤
│  L4. INTER-FACTION RESOLUTION — vote, transfer, treaty,   │  ← faction-to-faction surface
│       tribunal, seizure, conquest, CB matrix              │
├───────────────────────────────────────────────────────────┤
│  L3. FACTION ACTION — per-season actions (universal +     │  ← what factions do each turn
│       faction-unique)                                     │
├───────────────────────────────────────────────────────────┤
│  L2. FACTION IDENTITY — stats, status, Standing matrix,   │  ← what a faction IS
│       Conviction Scars, AI priority stack                 │
├───────────────────────────────────────────────────────────┤
│  L1. PRIMITIVES + SERVICES — dice, registry, game_state,  │  ← infra (faction-agnostic)
│       season_manager                                      │
└───────────────────────────────────────────────────────────┘
```

GD enforcement crosses layers: GD-1 at L6 (victory check), GD-2 at L3 (mandatory action eligibility), GD-3 at L4 (status-flag gates) + L5 (emergence).

---

## §2. Faction Identity (L2)

What defines a faction in the engine.

### §2.1 Faction stat block

Every faction carries: **Wealth (W)**, **Military (Mil)**, **Influence (I)**, **Stability (Sta)**, **Mandate (M)** — typically 0-10 ranges. Plus **Legitimacy (L)** as the cross-stat governance metric. Canon: `params/factions.md`.

### §2.2 Parliamentary status flag

Three states relevant to engagement with the political surface:

- **Parliamentary** — full participation (vote, initiate transfer, sign treaties). Starting factions (Crown, Church, Hafenmark, Varfell) and Stage-4 promoted factions with PT ≥ 3 avg.
- **Extra-parliamentary** — political-surface participation without parliamentary actions. Stage-4 promoted factions with PT < 3 avg (RM-variant Insurgency).
- **Non-parliamentary** — territorial actor only (hold + invade), no political surface. Stage-3 Insurgency.

Canon: `designs/world/insurgency_pipeline_v30.md §4.3, §5.3` (Pass 2i). Status semantics enforced at L4 via hook gates.

### §2.3 Standing matrix

Pairwise Standing-with-X tracks between every faction pair. Changes via political/military events; gates Treaty eligibility, Parliamentary Vote bloc dynamics, CB sources. Canon: `params/factions.md` + `designs/provincial/parliamentary_transfer_v30.md §4` (Pass 2h).

### §2.4 Conviction Scars

Per-faction grievance ledger. Accumulates from being-wronged events (territory taken via Transfer, excommunicated, treaty violated, etc.). Affects future action eligibility, AI priorities, RM growth (per v12c §4.2). Canon: `designs/scene/conviction_track_v30.md`.

### §2.5 Faction-specific Conviction values

Each faction has canonical Convictions (ethical-axis positions) shaping action costs and Belief revisions. **AUDIT-PENDING per Jordan diagnosis 2026-05-17** — current Conviction values may contain contamination from prior sessions. Canon: `params/factions.md` + faction_canon docs. Tracker: per-faction audit needed.

### §2.6 NPC AI priority stack

Per-faction AI priorities driving action choice when faction is NPC-controlled. **AUDIT-PENDING** per `canon/placeholder_names.yaml NPC-AI-PRIORITY-STACK-001`. Module `sim/autoload/npc_ai.py` — name retained, content audit blocks finalization.

---

## §3. Faction Action Layer (L3)

The per-season action surface. Per `canon/mechanics_index.yaml::categories.faction_unique_actions`.

### §3.1 Universal actions (4)

Available to all parliamentary + extra-parliamentary factions:

| Action | Canon | Status |
|---|---|---|
| `govern` | `faction_canon` + `params/factions.md` | READY |
| `muster` | `faction_canon` + `params/factions.md` | READY |
| `military_conquest` | `designs/provincial/mass_battle_v30.md` + `mass_battle_integration_v30.md` (Pass 2n) | READY (v22-port plan) |
| `parliamentary_transfer` | `designs/provincial/parliamentary_transfer_v30.md` (Pass 2h) | READY (3 forward-flags) |

### §3.2 Crown unique (4)

| Action | Canon | Status |
|---|---|---|
| `royal_progress` | `part10 §3.2` (Pass 2h Ob iteration; ED-840 closed) | READY |
| `great_work` | `part10 §3.3` | READY |
| `coronation_renewal` | `part10 §3.4` | READY |
| `crown_treaty` | `treaty_expiration_v30.md` (Pass 2h) | READY (3 flags) |

### §3.3 Church unique (6)

| Action | Canon | Status |
|---|---|---|
| `excommunication_action` | `faction_canon §8.2` + `social_contest §7.1` | READY |
| `absolution` | `faction_canon §8` | READY |
| `council_solmund` | `faction_canon` | READY |
| `mass_seizure` | `conviction_track §2 PP-411` + `ci_political §7.6` + `victory_v30 §3.2` | 3-source drift; reconciliation pending Pass 2f |
| `infrastructure_reclamation` | placeholder; canon doc Pass 2f pending | BLOCKED (content audit; placeholder retained-name per CHURCH-INFRASTRUCTURE-INVASION-CONTENT-001) |
| `home_sanctuary_t9` | placeholder; canon doc Pass 2f pending | BLOCKED (content audit per CHURCH-STARTING-PROTECTION-CONTENT-001) |

### §3.4 Hafenmark unique (3)

| Action | Canon | Status |
|---|---|---|
| `charter_of_liberties` | `faction_canon §6` | READY (mechanic-canon; flavor frame in identity-territory) |
| `altonian_reinforcements` | v12c §4.3 (validated_n1000) | READY mechanism; choice-lock content audit pending Pass 2e (HAFENMARK-EXTERNAL-MILITARY-CONTENT-001) |
| `hafenmark_equipment` | placeholder; Wagenburg+Bombards spec | BLOCKED on tactic_cards audit + Pass 2e (HAFENMARK-TACTIC-EXTENSION-CONTENT-001) |

### §3.5 Varfell unique (2 — both placeholder-named per Option A)

| Action | Canon | Status |
|---|---|---|
| `varfell_mandate_action` | placeholder (renamed from `vaynards_hall`); mechanism broken per Jordan 2026-05-17 (double-cost asymmetry) | BLOCKED — name + mechanism redesign pending audit (VARFELL-MANDATE-ACTION-001) |
| `varfell_territorial_acquisition` | placeholder (renamed from `einhir_revival`); v12c §4.1 mechanism canonized | READY mechanism; identity wrapping pending audit (VARFELL-TERRITORIAL-ACQUISITION-001) |

### §3.6 Personal-scale contests inherited by factions

Faction agents (tribunes, advocates, senators, party-members) participate in personal-scale resolution surfaces that determine faction outcomes:

- `social_contest` — multi-Exchange political resolution per `designs/scene/social_contest_v30.md`
- `excommunication_tribunal` (per `social_contest §7.1` ED-625)
- `parliamentary_vote` (per `social_contest §10`)
- `parliamentary_stay` (per `social_contest §10.1` ED-631)
- `fieldwork` — investigation/evidence accumulation
- `combat` — personal-scale violence (rare for factions; Champions and key agents only)

---

## §4. Inter-Faction Resolution Layer (L4)

How factions interact. The political and military surface.

### §4.1 Parliamentary contest stack

Vote at the top; Stay as the block; Transfer as the territorial expression.

- **`parliamentary_vote`** — N-faction vote on a proposed action. 4-faction baseline at game start. Insurgency-promoted factions (parliamentary status only) join the vote pool. Canon: `social_contest §10`.
- **`parliamentary_stay`** — block mechanism. Per ED-631. Canon: `social_contest §10.1`.
- **`parliamentary_transfer`** — territory transfer via vote contest. 4 modes (Adversarial / Consensual / Punishment / Appeasement) × 8 CB sources (per Pass 2h §3). Universal mechanic. Wraps Parliamentary Vote.

### §4.2 Excommunication chain

Church-initiated CB / faction-state event:

- **`excommunication_action`** — Church L3 action initiating Tribunal
- **`excommunication_tribunal`** — `social_contest §7.1` resolution
- **`absolution`** — Church reversal action restoring status post-Tribunal

### §4.3 Treaty system

Universal Crown-nerf and political-surface stabilizer:

- **`crown_treaty`** — bind action (Pass 2h)
- **`treaty_expiration`** — arc-boundary lapse check (90-95%/arc validated_n1000_v12c). Treaty-violation generates CB; voiding immediate. Memoryless invariant. Canon: `treaty_expiration_v30.md` (Pass 2h).

### §4.4 Mass Seizure (Church-on-territory)

Church seizes territory infrastructure (Religious Building / Templar Station / Inquisitor Base) under PT-threshold conditions. **3-source canon drift** (`conviction_track §2 PP-411` / `ci_political §7.6` / `victory_v30 §3.2`) — reconciliation pending Pass 2f.

### §4.5 Military Conquest

Mass battle resolution (no parliamentary contest required). Canon: `mass_battle_v30.md` + `mass_battle_integration_v30.md` (Pass 2n). 4 forward-flags (SPEED-1, POOL-0.5, D-2, D-8-interim).

### §4.6 Casus Belli (CB) matrix

8 CB sources canonized in `parliamentary_transfer_v30.md §3` (Pass 2h):
1. Adjacent Instability
2. Treaty Violation
3. Excommunication-current
4. Religious Building Desecration
5. Crown Diktat (rare)
6. Combined-Standing Threshold
7. Conviction Scar Accumulation
8. RM Adjacent-Movement Pressure

CB sources gate which factions can initiate which Transfers. Some CBs only valid in specific Transfer modes (Punishment-mode CBs vs Consensual-mode CBs).

---

## §5. Faction-Emergent Layer (L5)

The GD-3 pipeline. 4-stage layered model per `designs/world/insurgency_pipeline_v30.md` (Pass 2i).

| Stage | Name | Mechanical character | Module |
|---|---|---|---|
| 1 | World-level RM PT decay | Background; reduces piety at arc boundary | `sim/world/restoration_movement.py` |
| 2 | Latent RM | Ambient influence; does NOT control territory; per `conviction_track §5 PP-416` | `sim/world/restoration_movement.py` |
| 3 | Insurgency formation | Territorial-controlling; non-parliamentary; per GD-3 (a-b) | `sim/world/insurgency_pipeline.py` |
| 4 | Promoted Faction | Full faction; parliamentary OR extra-parliamentary; per GD-3 (c-e) | `sim/world/insurgency_pipeline.py` |

**Critical:** Promoted Factions ARE eligible to win via Peninsular Sovereignty per GD-1. No status-gate on victory. Successful insurgencies (11+ territories sustained 2 seasons) WIN, including against parent faction.

7 forward-flags surfaced (INSURGENCY-STATS-001 through LATENT-RM-vs-INSURGENCY-RM-001) — Pass 2k entries ED-850 through ED-856.

---

## §6. Cross-Scale Faction Interactions (L1-L5 bridges)

Faction state changes via scale-handoff:

- **`domain_echo`** — personal-scene results echo up to faction state (e.g., a Tribunal verdict updates Church Standing). Canon: `articulation_layer_v30.md`.
- **`articulation_layer`** — Tier 1/2/3 articulation governs when faction-state events trigger personal-scale resolution.
- **`zoom_in_out`** — engine UX flow for transitioning between scales.
- **`handoff_rules`** — 8 canonical handoff rules per `scale_transitions_v30.md`.

---

## §7. Peninsular Accounting Cascade (L6)

End-of-season faction state reconciliation. 13-step cascade per `campaign_architecture_v30.md`. Faction-relevant steps:

1. Action resolutions (already applied during season)
2. RM PT decay (Stage 1 background)
3. Insurgency formation check (GD-3 (a))
4. Treaty expiration check (90-95%/arc lapse)
5. Conviction Scar accumulation
6. Standing matrix updates
7. ci_track / rs_track / ms_track / ip_track updates
8. Promoted Faction promotion check (GD-3 (c))
9. Victory check (GD-1 — 11+ territories sustained 2 seasons)

---

## §8. GD Enforcement Surface

| GD | What it enforces | Where in faction systems |
|---|---|---|
| **GD-1** | Sole victory path = peninsular_sovereignty (11+ territories sustained 2 seasons). No faction-specific victories. | `sim/autoload/victory.py` (sole victory module). All factions including emergents eligible. |
| **GD-2** | Mandatory threat response when Accord below threshold in owned territory. | `sim/provincial/faction_action.py` action eligibility pass. Mandatory before stochastic. |
| **GD-3** | Insurgency / Promoted Faction status semantics — non-parliamentary blocks vote/transfer/treaty; extra-parliamentary blocks vote/transfer/formal-treaty. | `sim/personal/parliamentary_vote.py`, `sim/provincial/parliamentary_transfer.py`, `sim/provincial/treaty.py`, `sim/world/insurgency_pipeline.py` |

---

## §9. Implementation Status Summary

Per `integration_plan_v18.md` Phase mapping:

| Layer | Mechanics count | Status |
|---|---|---|
| L1 Primitives + Services | 11 + 6 | Phase 1 — READY |
| L2 Faction Identity | infra-distributed | Phase 1-2 — mostly READY; convictions + AI audit-pending |
| L3 Faction Action — universal | 4 | Phase 8 — READY |
| L3 Faction Action — Crown | 4 | Phase 8 — READY (post Pass 2h) |
| L3 Faction Action — Church | 6 | Phase 8/9 — 2 READY, 2 placeholder-content, 2 audit-blocked |
| L3 Faction Action — Hafenmark | 3 | Phase 9 — 1 READY, 2 audit-pending |
| L3 Faction Action — Varfell | 2 | Phase 9 — 1 READY-mechanism (placeholder-name), 1 redesign-pending |
| L4 Inter-Faction Resolution | 11 | Phase 5-8 — READY except mass_seizure (3-source drift) |
| L5 Faction-Emergent | 4 | Phase 10 — READY (post Pass 2i, 7 derivation flags) |
| L6 Peninsular Accounting | 6 | Phase 11 — READY |

**Aggregate:** ~50 faction-touched mechanics. ~35 READY. ~8 placeholder-content (Option A unblocked). ~7 blocked on Jordan contamination audit (faction identity, AI priorities, tactic_cards, Conviction values, Pass 2d/e/f canon authoring).

---

## §10. Forward-Flag Concentrations

Faction systems carry most of Pass 2's forward-flag load:

| Concentration | Flags | ED IDs |
|---|---|---|
| Parliamentary Transfer (Pass 2h) | 3 | ED-844, 845, 846 |
| Treaty (Pass 2h) | 3 | ED-847, 848, 849 |
| Insurgency Pipeline (Pass 2i) | 7 | ED-850 through 856 |
| Mass Battle (Pass 2n) | 4 | ED-857, 858, 859, 860 |

Plus 8 placeholder registry entries (canon/placeholder_names.yaml) — all faction-related.

**Total forward-flags on faction surface: ~25 of 31 Pass 2 flags (~80%).** Faction systems are the densest forward-flag concentration in Valoria; integration plan Phase 9 is the heaviest blocked phase.

---

## §11. Cross-references

| Topic | Authority |
|---|---|
| Master mechanic registry | `canon/mechanics_index.yaml` |
| GD constraints | `canon/02_canon_constraints.md §B` |
| Faction stats baseline | `params/factions.md` |
| Universal mechanics (Pass 2h) | `parliamentary_transfer_v30.md`, `treaty_expiration_v30.md` |
| Faction-emergent (Pass 2i) | `insurgency_pipeline_v30.md` |
| Mass battle (Pass 2n) | `mass_battle_integration_v30.md` |
| Personal-scale contests | `social_contest_v30.md` |
| Implementation phasing | `integration_plan_v18.md` |
| Placeholder lifecycle | `canon/placeholder_names.yaml` |
| Editorial state | `canon/editorial_ledger.yaml` |

---

## §12. Status Declaration

[STATUS: REFERENCE — Pass 2 follow-up 2026-05-17. Single-pane catalog of all faction-related systems and mechanics in Valoria. Points at canon rather than duplicating; gives Jordan + Pass 3 reviewer + implementation team an integration-tier overview of faction surface area. Self-authored bias risk applies — this overview was authored by same-chat Claude that authored the Pass 2 work it summarizes; alternate readings of faction-surface coverage are possible. Verification surface: cross-check this doc against `canon/mechanics_index.yaml::categories.faction_unique_actions` (8 categories) and `integration_plan_v18.md §1.4` (per-module status table).]

---

## §13. Changelog

- **v30 init (2026-05-17, Pass 2 follow-up):** Initial authoring. Consolidates all faction-related mechanics from `canon/mechanics_index.yaml` `categories.faction_unique_actions` + Pass 2 canonized docs (knots, parliamentary_transfer, treaty_expiration, insurgency_pipeline, mass_battle_integration, integration_plan_v18) + faction-state systems (Standing, Conviction Scars, AI priority, status flags) into 6-layer architecture overview with GD enforcement surface, implementation status, and forward-flag concentration analysis.
