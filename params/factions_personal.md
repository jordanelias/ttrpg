<!-- version: v1.0 | source: designs/ttrpg/factions_ttrpg_v30.md | last_updated: 2026-04-13 -->
<!-- PATCHES APPLIED: SIM-FAC verification pass 2026-04-13. No mechanical changes. -->
<!-- SIM STATUS: VERIFIED — domain actions, unique actions, ethical framework modifiers -->

# params_factions_ttrpg.md — TTRPG Faction Mechanics

## Faction Stats — 1-7 Scale
<!-- [PP-686 v2 NOTE 2026-05-01] Mandate split into Legitimacy + Popular Support per designs/provincial/faction_behavior_v30.md §3.4–3.5. Mandate retained as derived for backward compat. -->

| Stat | Represents |
|------|-----------|
| Legitimacy | Populace acceptance — slow-integrating per faction_behavior_v30 §3.5 (PP-686 v2) |
| Popular Support | Active populace backing — faster-moving per faction_behavior_v30 §3.4 (PP-686 v2) |
| ~~Mandate~~ (derived) | `Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)` per faction_behavior_v30 §4 — retained for backward compat |
| Influence | Political reach and diplomatic weight |
| Wealth | Economic capacity |
| Military | Armed force and unit capacity |
| Intel | Intelligence network and covert operations |
| Stability | Internal cohesion and crisis resistance |

## Starting Values (game start, 45 AG)
| Faction | Legitimacy | Popular_Support | Influence | Wealth | Military | Intel | Stability |
|---------|------------|------------------|----------|--------|----------|-------|-----------|
| Crown | 5 | 5 | 5 | 4 | 4 | — | 4 |
| Church | 5 | 5 | 6 | 5 | 4 | — | 5 |
| Hafenmark | 4 | 4 | 4 | 5 | 3 | — | 4 |
| Varfell | 4 | 4 | 4 | 4 | 4 | — | 4 |
| Guilds | 3 | 3 | 4 | 6 | 2 | — | 5 |
<!-- Niflhel row deleted 2026-04-30 — STRUCK per CR-STRIKE-2026-04-19 / ED-764. -->
| Revolution | — | — | 3 | — | — | — | 3 |
| Löwenritter | — | — | 3 | — | 5 | 3 | 5 |

<!-- Niflhel STRUCK explanatory block deleted 2026-04-30 — see canon/editorial_ledger.yaml ED-770/ED-772 for context. -->

Partial sheets: Revolution (Influence, Stability, Intel only). [Niflhel removed per ED-764.]
Löwenritter (no L, no PS, no Wealth — see L_init=PS_init=0 note below). Guilds NPC-only: no deviation mechanic.

**Legitimacy + Popular Support init (PP-686 v2 / 2026-05-02 ED-784 finalization):** Per the table above, both scalars seed at the same value at game start (Crown L=PS=5, Church L=PS=5, Hafenmark L=PS=4, Varfell L=PS=4, Guilds L=PS=3). The seed-equal rule reflects PP-686 v2 §3.4-3.5: at t=0 the populist and procedural axes carry equal weight; Mission outcomes, cascade alignment, and expectation-resolution cycles drive subsequent divergence. Factions with no L+PS at start (Revolution, Löwenritter) seed L=PS=0; PS may climb via Mission outcomes from zero. After first Accounting, dynamics replace seed values per faction_behavior_v30 §3.4–3.5.

## Domain Action Resolution
Pool = character's relevant attribute + faction's relevant stat (if PC holds leadership).
NPC factions: Pool = faction's relevant stat.
Ob = target faction's relevant stat (1–7 scale, no division).
Seasonal cap: ±2 per stat per season at accounting. Minimum Ob: 1 (PP-285).

### ~~Ethical Framework Modifiers~~ — SUPERSEDED 2026-05-01 (PP-686 v2)
<!-- [SUPERSEDED 2026-05-01 — SUPERSESSION-PP686-001] Replaced by triadic Ob decomposition in designs/provincial/faction_behavior_v30.md §3.7. Min Ob floor 1 retained. -->

| ~~Alignment~~ (struck) | ~~Ob Modifier~~ (struck) |
|------------------------|--------------------------|
| ~~Aligned with faction framework~~ | ~~−1 Ob~~ |
| ~~Neutral / unrelated~~ | ~~±0~~ |
| ~~Opposed to framework~~ | ~~+1 Ob~~ |
| ~~Church revealing Thread truth~~ | ~~+2 Ob~~ |

**Replacement** per faction_behavior_v30 §3.7: `Ob_modifier = clamp(mission_alignment + cascade_alignment + expectation_alignment, -2, +2)`. Mission alignment reads PP-687 `da_outcome.*` subtypes; cascade alignment reads PP-684 13-Conviction projection; expectation alignment reads role templates §3.3.1. Min Ob floor 1 retained per PP-285.

## Unique Actions
| Faction | Action | Pool | Ob | Notes |
|---------|--------|------|-----|-------|
| Crown | Royal Decree | L | 2 | 1/season. Consecutive: +1 Ob per season. Cannot target absent stats. |
| Church | Excommunication | L | vs target L (or Ob 2 if non-leader) | Requires L ≥ 3. |
| Hafenmark | Sovereign Authority Doctrine | L | 4 | 1/campaign arc. Heresy Investigation risk. |
| Varfell | Private Collection | Intel | 2 | 1/season. +1 TS on use. TS 14+: triggers Spirit check. |
| Guilds | Economic Leverage | Wealth | vs target Wealth | Requires Guild Favour ≥ 5 in territory. |
| ~~Niflhel Quiet~~ STRUCK | — | — | — | Per ED-764. Settlement-level intelligence-broker NPCs use individual Intel; no faction-level Quiet action exists. |
| Revolution | Community Weaving | Influence | TT ÷ 20 (round up) | Requires practitioner TS 30+. Co-movement fires. |
| Löwenritter | Graduated Autonomy | — | track-state | Replaces Coup Counter (ED-589). Track stages: Loyal → Restless → Autonomous → Split. Per worldbuilding §3 / clock_registry §3. |

## Probability Reference (verified by SIM-FAC-01/02)
| Pool | Ob | P(Success+) | P(Overwhelming) |
|------|----|------------|----------------|
| 5D (L or PS, generic) | 2 | 60% | 23% |
| 6D | 3 | 48% | 8% |
| 4D | 4 | 14% | 0% |
| 5D | 4 | 23% | 0% |
| 5D | 6 | 4% | 0% |

NPC-only equal-stat contest: ~14% success, ~59% partial, ~27% fail (design intent: PC agency matters).

## Stability Check — Seasonal Accounting
| Situation | Ob |
|-----------|-----|
| Quiet season | 1 |
| One active threat | 2 |
| Two concurrent threats | 3 |
| Active attack on L, PS, or Wealth | 4 |
| Campaign-level crisis | 5 |
Anti-death-spiral floor: Stability ≤ 2 → treat as Ob 4 regardless of actual pressure.
P(survive, Stab 2 vs Ob 4) ≈ 59%. ~2 seasons at Stab 2 before probable collapse.

## Parliamentary Vote
Pool: relevant faction stat (typically L, PS, or Influence depending on action's procedural-vs-populist nature).
Ob: opponent's relevant stat.
Format: best of 3 exchanges. First to 2 wins. Ties (neither wins 2): motion fails, TT+1, CI+1.

## Church Influence Generation
Church L ≥ 5: CI +1/season at accounting.
Piety Domain Action (1/season): L pool, Ob 2. Success: CI +1 (stacks with above).
CI seasonal cap: ±5 combined from all sources.
Stability ≤ 4: CI generation pauses.

## ~~Coup Counter (Löwenritter)~~ STRUCK (ED-781 — supersedes per ED-589)

Per `designs/architecture/conflict_architecture_proposal.md §Graduated Löwenritter Autonomy` and `designs/provincial/clock_registry_v30.md L30 Löwenritter Autonomy`, the Coup Counter binary mechanism is replaced by a four-stage progression: **Loyal → Restless → Autonomous → Split** (track-state, not numeric counter). Triggers, Crown effects, and reversibility rules are in `conflict_architecture_proposal.md` L67-L82. Above §59 of this file (Löwenritter Graduated Autonomy entry) is the canonical reference for params lookup. The legacy Coup Counter spec is preserved in `deprecated/` per editorial policy.

Migration note: prior canonical text was "Counter never decrements. At 3: coup fires at next accounting." This is replaced by stage-based progression where stages 1-3 are reversible and only stage 4 (Split) is permanent. References to "Coup Counter" in NPC priority trees (`params/bg/npc_priority_trees.md` L42, L86, L149, L197) refer to the legacy track and should be migrated to "Löwenritter Autonomy stage" in a future cleanup pass.

## Southernmost Awareness (Faction Stat, 0–7 or 0–10 for research factions)
| Faction | Starting Awareness |
|---------|--------------------|
| Crown | 0 |
| Church | 0 |
| Hafenmark | 1 |
| Varfell | 2 |
| Revolution | 3 |
[NAME-PENDING: ED-048] Text holder: floor = 1.

<!-- patch_history: references/params_factions_history.md (to be created) -->
<!-- canonical_sources: references/canonical_sources.yaml -->
